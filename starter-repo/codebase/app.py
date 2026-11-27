"""Khung chạy bản chạy thử tối thiểu (dòng lệnh): gõ đầu vào → answer() trong agent.py → in kết quả.

Chạy bằng: python run.py   (macOS/Linux có thể là python3, Windows có thể là py)
Nhóm thay bằng giao diện của mình (web, bot…) nhưng giữ `python run.py` là lệnh duy nhất
để chạy bản chạy thử (sửa hàm run_app() trong run.py nếu cần).
"""
import os
import sys
import json
from pathlib import Path

for _stream in (sys.stdout, sys.stderr, sys.stdin):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _where(e):
    """File (trong codebase/) gây lỗi khi nạp: SyntaxError có e.filename, lỗi khác lấy khung cuối của traceback."""
    import traceback
    path = getattr(e, "filename", None) or (traceback.extract_tb(e.__traceback__)[-1].filename if e.__traceback__ else "")
    if not path:
        return "codebase/"
    p = os.path.abspath(path)
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.relpath(p, base).replace(os.sep, "/") if p.startswith(base) else path

def main() -> int:
    try:
        import tracing
        from agent import answer
        from ai import MODEL_PROVIDER
    except Exception as e:  # lỗi cú pháp, thiếu thư viện… trong codebase/
        print("Không nạp được codebase/ — lỗi ở %s: %s: %s" % (_where(e), type(e).__name__, e))
        print("Sửa lỗi rồi chạy lại. Cách nối model: docs/connect-model.md")
        return 1
    def review(text):
        tracing.begin("app")
        try:
            result = answer(text)
        except Exception:
            tracing.end()
            raise
        summary, _ = tracing.end()
        print(result["output"])
        print("   (model: %s · gọi model %d lần · công cụ %d lần · token vào %d / ra %d)"
              % (", ".join(summary["models"]) or "—", summary["model_calls"], summary["tool_calls"],
                 summary["tokens_in"], summary["tokens_out"]))

    def demo():
        path = Path(__file__).resolve().parents[1] / "data" / "demo_cases.json"
        with path.open(encoding="utf-8") as handle:
            cases = json.load(handle)
        for case in cases:
            print("\n--- Demo: %s ---" % case["name"])
            review(case["input"])

    print("AIhayAL · Track A3 · Rà một nhận định pre-class · Nguyễn Minh Thành")
    print("Nguồn mặc định: 3 đoạn SYNTHETIC trong data/demo_sources.json, chưa phải tài liệu đã duyệt.")
    print("Nhập một nhận định, hoặc JSON một dòng: " + '{"claim":"…","sources":[{"code":"S1","text":"…"}]}')
    print(":demo = xem 3 nhánh · Thoát: Ctrl+C (hoặc Enter 2 lần với dòng trống).")
    if MODEL_PROVIDER == "fake":
        print("Chế độ MÔ PHỎNG CP2; chỉ so chữ/phủ định đơn giản, chưa kiểm kiến thức bằng AI.")
        demo()
    blank = 0
    while True:
        try:
            text = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not text:
            blank += 1
            if blank >= 2:
                return 0
            continue
        blank = 0
        try:
            if text == ":demo":
                demo()
            else:
                review(text)
        except NotImplementedError as e:
            print("Chưa nối model: %s" % e)
            return 1
        except Exception as e:  # lỗi gọi model: báo rồi cho hỏi tiếp
            print("[lỗi] %s: %s" % (type(e).__name__, e))
            continue


if __name__ == "__main__":
    sys.exit(main())
