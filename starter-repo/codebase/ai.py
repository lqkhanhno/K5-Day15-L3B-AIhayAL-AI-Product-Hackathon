"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    đối chiếu chữ/phủ định đơn giản bằng mock_review.py, model "fake", token 0.
    Chỉ để luồng A3 chạy hết trước CP2, không phải suy luận mô hình thật.
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: đã có nhánh OpenAI, Gemini và Ollama; điền .env theo
docs/cp3-thanh-handoff.md. Không dán API key vào file này.
"""
import os
import json
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call
from mock_review import mock_review

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
MODEL_TIMEOUT = float(os.environ.get("MODEL_TIMEOUT") or "120")
OLLAMA_BASE_URL = (os.environ.get("OLLAMA_BASE_URL") or "http://localhost:11434").rstrip("/")


def post_json(url, headers, body):
    """Một request; không in key/raw response và không tự chạy lại lượt tính phí."""
    request = urllib.request.Request(
        url, data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=MODEL_TIMEOUT) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        hints = {400: "Kiểm MODEL_NAME và định dạng request.",
                 401: "Kiểm API_KEY trong .env.", 403: "Kiểm quyền truy cập model/API key.",
                 404: "Kiểm MODEL_NAME hoặc địa chỉ dịch vụ.",
                 429: "Hết quota hoặc giới hạn tốc độ; kiểm tài khoản, thêm --wait 4 khi eval."}
        raise RuntimeError("Model API HTTP %d. %s" % (
            exc.code, hints.get(exc.code, "Dịch vụ model gặp lỗi; thử lại thành lượt mới."))) from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError("Không kết nối được model hoặc hết thời gian chờ; kiểm mạng/dịch vụ.") from None


def _tokens(usage, key):
    value = usage[key]
    if type(value) is not int or value < 0:
        raise ValueError("API không trả số token hợp lệ cho " + key)
    return value


def _openai(system, user):
    data = post_json("https://api.openai.com/v1/chat/completions",
        {"Authorization": "Bearer " + API_KEY}, {
            "model": MODEL_NAME,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "response_format": {"type": "json_object"}})
    choice = data["choices"][0]
    if choice["finish_reason"] != "stop":
        raise ValueError("Model chưa hoàn tất câu trả lời hoặc đã từ chối.")
    usage = data["usage"]
    return {"text": choice["message"]["content"], "model": data.get("model") or MODEL_NAME,
            "tokens_in": _tokens(usage, "prompt_tokens"),
            "tokens_out": _tokens(usage, "completion_tokens")}


def _gemini(system, user):
    name = MODEL_NAME[7:] if MODEL_NAME.startswith("models/") else MODEL_NAME
    model = urllib.parse.quote(name, safe="")
    data = post_json("https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % model,
        {"x-goog-api-key": API_KEY}, {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": {"responseMimeType": "application/json"}})
    candidates = data.get("candidates") or []
    if not candidates or candidates[0].get("finishReason") != "STOP":
        raise ValueError("Gemini không trả câu trả lời hoàn chỉnh; kiểm chặn nội dung/quota.")
    parts = candidates[0]["content"]["parts"]
    usage = data["usageMetadata"]
    # Gemini báo thinking riêng; cộng đúng một lần vào token đầu ra.
    thoughts = _tokens(usage, "thoughtsTokenCount") if "thoughtsTokenCount" in usage else 0
    return {"text": "".join(p.get("text", "") for p in parts if not p.get("thought")),
            "model": data.get("modelVersion") or MODEL_NAME,
            "tokens_in": _tokens(usage, "promptTokenCount"),
            "tokens_out": _tokens(usage, "candidatesTokenCount") + thoughts}


def _ollama(system, user):
    data = post_json(OLLAMA_BASE_URL + "/api/chat", {}, {
        "model": MODEL_NAME, "stream": False, "format": "json",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]})
    if data.get("done") is not True or data.get("done_reason", "stop") != "stop":
        raise ValueError("Ollama chưa hoàn tất câu trả lời.")
    return {"text": data["message"]["content"], "model": data.get("model") or MODEL_NAME,
            "tokens_in": _tokens(data, "prompt_eval_count"), "tokens_out": _tokens(data, "eval_count")}


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        result = mock_review(json.loads(user))
        return {"text": json.dumps(result, ensure_ascii=False), "model": "fake", "tokens_in": 0, "tokens_out": 0}

    providers = {"openai": _openai, "gemini": _gemini, "ollama": _ollama}
    if MODEL_PROVIDER not in providers:
        raise ValueError("MODEL_PROVIDER phải là fake, openai, gemini hoặc ollama.")
    if not MODEL_NAME:
        raise ValueError("Cần điền MODEL_NAME trong starter-repo/.env.")
    if MODEL_PROVIDER != "ollama" and not API_KEY:
        raise ValueError("Cần điền API_KEY trong starter-repo/.env; không gửi key vào chat.")
    if MODEL_TIMEOUT <= 0:
        raise ValueError("MODEL_TIMEOUT phải lớn hơn 0.")
    result = providers[MODEL_PROVIDER](system, user)
    if not isinstance(result["text"], str) or not result["text"].strip():
        raise ValueError("Model trả nội dung rỗng.")
    return result
