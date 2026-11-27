"""Nguồn cục bộ của một bài pre-class; không gửi, sửa hoặc xuất bản dữ liệu."""
import json
from pathlib import Path
import re

from tracing import tool

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
LESSON_CONFIG = DATA_DIR / "lesson.json"


def load_lesson():
    """Đọc cấu hình bài do nhóm quản lý, không nhận đường dẫn từ người dùng."""
    try:
        with LESSON_CONFIG.open(encoding="utf-8") as handle:
            lesson = json.load(handle)
        if not isinstance(lesson, dict):
            raise ValueError("Cấu hình bài phải là JSON object.")
        for key in ("lesson_id", "title"):
            if not isinstance(lesson.get(key), str) or not lesson[key].strip():
                raise ValueError("Cấu hình bài thiếu " + key + ".")
        if lesson.get("source_status") not in ("synthetic", "draft_unreviewed", "approved"):
            raise ValueError("source_status phải là synthetic, draft_unreviewed hoặc approved.")
        filename = lesson.get("passages_file")
        if not isinstance(filename, str) or not re.fullmatch(r"[A-Za-z0-9_-]+\.json", filename):
            raise ValueError("passages_file phải là tên file JSON trong data/.")
        return lesson
    except (OSError, ValueError) as exc:
        raise ValueError("Không đọc được cấu hình bài; cần người phụ trách kiểm lại. " + str(exc)) from exc


def validate_sources(sources):
    if not isinstance(sources, list) or len(sources) > 20:
        raise ValueError("Nguồn phải là danh sách tối đa 20 đoạn {code, text}.")
    cleaned, codes = [], set()
    for passage in sources:
        if not isinstance(passage, dict):
            raise ValueError("Mỗi đoạn nguồn phải có code và text.")
        code, text = passage.get("code"), passage.get("text")
        if not isinstance(code, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}", code):
            raise ValueError("Mã đoạn phải dài 1–64 ký tự: chữ không dấu, số, _, - hoặc dấu chấm.")
        if code in codes:
            raise ValueError("Mã đoạn nguồn bị trùng: " + code)
        if not isinstance(text, str) or not text.strip() or len(text) > 5000:
            raise ValueError("Nội dung mỗi đoạn phải dài 1–5.000 ký tự.")
        codes.add(code)
        cleaned.append({"code": code, "text": text.strip()})
    return cleaned


@tool
def get_approved_passages() -> list:
    """get_approved_passages · Input: bộ nguồn cấu hình sẵn cho một bài, không có tham số.
    Output: danh sách {code, text} của bài trong data/lesson.json.
    Chỉ đọc dữ liệu cục bộ, không có tác động ra ngoài.
    CP2 dùng nguồn synthetic có ghi rõ trạng thái, chưa phải tài liệu đã duyệt thật.
    """
    lesson = load_lesson()
    try:
        path = (DATA_DIR / lesson["passages_file"]).resolve()
        if path.parent != DATA_DIR.resolve():
            raise ValueError("Nguồn phải nằm trong thư mục data/.")
        with path.open(encoding="utf-8") as handle:
            passages = json.load(handle)
        if isinstance(passages, dict):
            passages = passages.get("segments")
        return validate_sources(passages)
    except (OSError, ValueError) as exc:
        raise ValueError("Không đọc được đoạn nguồn của bài; cần kiểm lại hoặc bổ sung nguồn. " + str(exc)) from exc
