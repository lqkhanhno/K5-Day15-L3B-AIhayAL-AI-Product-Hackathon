"""Quy tắc chữ cho demo CP2; không phải model thật, không đọc benchmark."""
import re
import unicodedata


def _normalize(text):
    text = unicodedata.normalize("NFC", text).casefold().strip().rstrip(".。")
    return " ".join(text.split())


def _opposite(left, right):
    """Nhận ra một từ phủ định trực tiếp; không chứng minh quan hệ ngữ nghĩa."""
    def remove_not(text):
        return re.sub(r"(?<!\w)không\s+", "", text)
    return left != right and (
        (len(re.findall(r"\bkhông\b", left)) == 1 and remove_not(left) == right)
        or (len(re.findall(r"\bkhông\b", right)) == 1 and remove_not(right) == left)
    )


def mock_review(payload):
    original_claim = payload["claim"]
    claim = _normalize(original_claim)
    clauses = [claim] + re.split(r"\s+(?:và|nhưng)\s+|;\s*", claim)
    matches, conflicts, contradicted = [], [], []
    for passage in payload["sources"]:
        source = _normalize(passage["text"])
        if claim == source:
            matches.append(passage["code"])
        else:
            for clause in clauses:
                if _opposite(clause, source):
                    conflicts.append(passage["code"])
                    contradicted.append('Vế “%s” bị đoạn [%s] bác bỏ: “%s”.'
                                        % (clause, passage["code"], passage["text"]))
                    break
    if matches and conflicts:
        return {"label": "thieu_can_cu", "source_ids": [], "reason": "Các nguồn chưa nhất quán; cần kiểm lại nguồn."}
    if matches:
        return {"label": "khop_nguon", "source_ids": matches,
                "reason": 'Mô phỏng: nguồn xác nhận nhận định “%s” qua nội dung trùng sau chuẩn hóa chữ.' % original_claim}
    if conflicts:
        return {"label": "mau_thuan", "source_ids": conflicts,
                "reason": "Mô phỏng phủ định chữ, cần người duyệt kiểm nghĩa: " + " ".join(contradicted)}
    return {"label": "thieu_can_cu", "source_ids": [],
            "reason": "Mô phỏng không xác định được quan hệ; cần bổ sung hoặc kiểm lại nguồn."}
