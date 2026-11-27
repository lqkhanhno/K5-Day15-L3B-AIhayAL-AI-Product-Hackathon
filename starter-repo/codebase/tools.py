"""Nguồn cho demo A3; chỉ đọc, không gửi hoặc xuất bản dữ liệu."""
import json
from pathlib import Path
import re

from tracing import tool

DEMO_SOURCES = Path(__file__).resolve().parents[1] / "data" / "demo_sources.json"


def validate_sources(sources):
    if not isinstance(sources, list) or len(sources) > 20:
        raise ValueError("sources phải là danh sách tối đa 20 đoạn {code, text}.")
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
def get_sources() -> list:
    """get_sources · Input: không có · Output: [{code, text}] từ file demo.
    Không tác động ra ngoài; chỉ đọc nguồn synthetic cố định, không tra Internet.
    """
    try:
        with DEMO_SOURCES.open(encoding="utf-8") as handle:
            return validate_sources(json.load(handle))
    except (OSError, ValueError) as exc:
        raise ValueError("Không đọc được nguồn demo; bổ sung nguồn hợp lệ. " + str(exc)) from exc
