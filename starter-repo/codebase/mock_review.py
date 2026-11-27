"""Mô phỏng CP2 bằng quy tắc chữ; không phải suy luận AI hoặc benchmark thật.

Không chứa câu thử hay bảng expected. Chỉ nhận ra trùng câu và thêm/bỏ đúng
một từ 'không' giữa hai câu; diễn đạt khác luôn chuyển người duyệt.
"""
import re
import unicodedata


def _normalize(text):
    text = unicodedata.normalize("NFC", text).casefold().strip().rstrip(".。")
    return " ".join(text.split())


def _opposite(left, right):
    # Chỉ hỗ trợ một phép phủ định trực tiếp, không đoán quan hệ ngữ nghĩa.
    def remove_not(text):
        return re.sub(r"(?<!\w)không\s+", "", text)
    return left != right and (
        (len(re.findall(r"\bkhông\b", left)) == 1 and remove_not(left) == right)
        or (len(re.findall(r"\bkhông\b", right)) == 1 and remove_not(right) == left)
    )


def mock_review(payload):
    claim = _normalize(payload["claim"])
    matches, conflicts = [], []
    for passage in payload["sources"]:
        source = _normalize(passage["text"])
        citation = {"code": passage["code"], "quote": passage["text"]}
        if claim == source:
            matches.append(citation)
        elif _opposite(claim, source):
            conflicts.append(citation)
    if matches and conflicts:
        return {"label": "thieu_can_cu", "reason": "Các nguồn vừa khớp vừa phủ định nhau; người duyệt cần xác minh nguồn.", "citations": []}
    if matches:
        return {"label": "khop_nguon", "reason": "Mô phỏng: nhận định trùng nội dung đoạn nguồn sau khi chuẩn hóa chữ.", "citations": matches}
    if conflicts:
        return {"label": "mau_thuan", "reason": "Mô phỏng: nhận định và nguồn khác nhau bởi một từ phủ định 'không'; cần người duyệt kiểm nghĩa.", "citations": conflicts}
    return {"label": "thieu_can_cu", "reason": "Mô phỏng không xác định được quan hệ với nguồn; không suy đoán kiến thức ngoài.", "citations": []}
