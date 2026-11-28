"""Cửa sổ quay demo CP3: dùng nguyên answer() và tracing của ứng dụng CLI."""
import json
from pathlib import Path
import queue
import re
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime, timezone

from agent import answer
from ai import MODEL_PROVIDER, MODEL_NAME
from tools import load_lesson
import tracing

ROOT = Path(__file__).resolve().parents[1]


def configure_result_view(view):
    """Định dạng hiển thị; nội dung kết luận vẫn lấy từ workflow."""
    view.tag_configure("heading", font=("Segoe UI", 11, "bold"), foreground="#53627a",
                       spacing1=12, spacing3=4)
    view.tag_configure("body", foreground="#172b4d", spacing3=6)
    view.tag_configure("quote", foreground="#334864", background="#eef3fa",
                       lmargin1=12, lmargin2=12, rmargin=12, spacing1=4, spacing3=8)
    view.tag_configure("muted", foreground="#637086", spacing3=8)
    view.tag_configure("warning", foreground="#805600", background="#fff4d6", spacing3=8)
    view.tag_configure("review", font=("Segoe UI", 12, "bold"), foreground="#1749a0", spacing1=12)
    for tag, color in (("khop_nguon", "#147348"), ("mau_thuan", "#b42332"),
                       ("thieu_can_cu", "#956000"), ("input_required", "#1749a0"),
                       ("error", "#b42332")):
        view.tag_configure(tag, font=("Segoe UI", 19, "bold"), foreground=color, spacing3=12)


def show_message(view, title, body, tag="muted"):
    view.configure(state="normal")
    view.delete("1.0", "end")
    view.insert("end", title + "\n", tag)
    view.insert("end", body + "\n", "body")
    view.configure(state="disabled")
    view.yview_moveto(0)


def render_review(view, result):
    """Dùng kết quả đã kiểm và trích đoạn từ snapshot output của đúng lượt này."""
    text = result["output"]
    input_required = result["status"] == "input_required"
    label = result.get("label")
    title = {"khop_nguon": "Khớp nguồn", "mau_thuan": "Mâu thuẫn",
             "thieu_can_cu": "Thiếu căn cứ"}.get(label, "Cần nhập nhận định")
    view.configure(state="normal")
    view.delete("1.0", "end")
    view.insert("end", title + "\n", "input_required" if input_required else label)
    if result.get("mode") == "fake":
        view.insert("end", "MÔ PHỎNG · Chưa gọi model thật\n", "warning")
    for line in text.splitlines():
        if line.startswith("Bài đối chiếu: "):
            view.insert("end", line + "\n", "muted")
        elif line.startswith("Nguồn: "):
            view.insert("end", line + "\n", "warning")
    if result.get("claim"):
        view.insert("end", "NHẬN ĐỊNH\n", "heading")
        view.insert("end", result["claim"] + "\n", "body")
    view.insert("end", "HƯỚNG DẪN NHẬP\n" if input_required else "LÝ DO\n", "heading")
    view.insert("end", result["reason"] + "\n", "body")
    # Không đọc lại file nguồn có thể đã đổi sau lượt gọi model.
    excerpts = dict(re.findall(
        r"^Nguồn \[([^\]\r\n]+)\]: (.*?)(?=^Nguồn \[|^Bước tiếp theo:|\Z)",
        text, re.MULTILINE | re.DOTALL))
    for code in result.get("source_ids", []):
        if code in excerpts:
            view.insert("end", "NGUỒN · " + code + "\n", "heading")
            view.insert("end", excerpts[code].rstrip() + "\n", "quote")
    if label == "thieu_can_cu":
        view.insert("end", "Chưa có đoạn nguồn đủ căn cứ để trích dẫn.\n", "muted")
    view.insert("end", "Cần nhập nhận định\n" if input_required else "Chờ người duyệt\n", "review")
    action = text.rpartition("\nBước tiếp theo: ")[2].splitlines()
    if action:
        view.insert("end", action[0] + "\n", "body")
    view.configure(state="disabled")
    view.yview_moveto(0)


def main():
    window = tk.Tk()
    window.title("AIhayAL - CP3 - Nguyen Minh Thanh")
    window.geometry("1100x760+40+40")
    window.configure(bg="#f4f6fa")
    window.option_add("*Font", "{Segoe UI} 12")
    tk.Label(window, text="AIhayAL · Rà một nhận định pre-class", font=("Segoe UI", 22, "bold"),
             bg="#f4f6fa", fg="#172b4d").pack(anchor="w", padx=24, pady=(16, 4))
    lesson = load_lesson()
    tk.Label(window, text="AI đề xuất · Người duyệt quyết định",
             bg="#f4f6fa").pack(anchor="w", padx=24)
    source_status = {"draft_unreviewed": "Nguồn bản nháp từ phụ đề, chờ kiểm duyệt",
                     "synthetic": "Nguồn minh họa tổng hợp", "approved": "Nguồn đã duyệt"}
    tk.Label(window, text="%s · %s" % (lesson["lesson_id"], source_status[lesson["source_status"]]),
             bg="#f4f6fa", fg="#775600").pack(anchor="w", padx=24, pady=(4, 10))
    tk.Label(window, text="Nhận định cần đối chiếu", bg="#f4f6fa").pack(anchor="w", padx=24)
    claim = tk.Text(window, height=3, wrap="word", font=("Segoe UI", 13), padx=10, pady=8)
    claim.pack(fill="x", padx=24, pady=(4, 8))
    cases = json.loads((ROOT / "data/demo_cases.json").read_text(encoding="utf-8"))
    claim.insert("1.0", cases[0]["input"])
    messages = queue.Queue()
    status = tk.StringVar(value="Sẵn sàng · Nhập một nhận định rồi bấm đối chiếu")
    metrics = tk.StringVar(value="%s / %s · Chưa gọi model trong lượt này" % (MODEL_PROVIDER, MODEL_NAME or "fake"))

    def worker(text):
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        tracing.begin("cp3-demo-" + stamp)
        try:
            result = answer(text)
            summary, events = tracing.end()
            evidence = {"recorded_at_utc": stamp, "kind": "connection_demo_not_benchmark",
                        "result": result, "summary": summary, "events": events}
            path = ROOT / "docs" / ("cp3-live-" + stamp + ".json")
            path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
            messages.put((result, summary, None))
        except Exception as exc:
            tracing.end()
            messages.put((None, None, "%s: %s" % (type(exc).__name__, exc)))

    def run():
        text = claim.get("1.0", "end").strip()
        button.configure(state="disabled")
        status.set("Đang đối chiếu…")
        metrics.set("Đang xử lý lượt hiện tại…")
        show_message(output, "Đang đối chiếu…", "Kết quả sẽ xuất hiện khi xử lý xong.")
        threading.Thread(target=worker, args=(text,), daemon=True).start()

    button = tk.Button(window, text="Đối chiếu với nguồn bài học", command=run,
                       bg="#1749a0", fg="white", padx=18, pady=8)
    button.pack(anchor="w", padx=24)
    tk.Label(window, textvariable=status, bg="#f4f6fa", fg="#1749a0").pack(anchor="w", padx=24, pady=8)
    # Đặt chân trang trước vùng co giãn để token luôn nằm trong cửa sổ.
    tk.Label(window, textvariable=metrics, bg="#f4f6fa", fg="#1749a0",
             font=("Segoe UI", 10)).pack(side="bottom", anchor="w", padx=24, pady=12)
    output = ScrolledText(window, height=10, wrap="word", font=("Segoe UI", 12),
                          padx=18, pady=14, relief="flat", state="disabled")
    output.pack(fill="both", expand=True, padx=24)
    configure_result_view(output)
    show_message(output, "Kết quả đối chiếu", "Nhãn, lý do và đoạn nguồn sẽ hiển thị tại đây.")

    def poll():
        try:
            result, summary, error = messages.get_nowait()
        except queue.Empty:
            pass
        else:
            if error:
                show_message(output, "Không thể hoàn tất đối chiếu", error, "error")
                status.set("Đối chiếu gặp lỗi · Có thể thử lại")
                metrics.set("Lượt này gặp lỗi; chưa có số token xác nhận.")
            else:
                render_review(output, result)
                status.set("Cần nhập lại nhận định" if result["status"] == "input_required"
                           else "Đã nhận kết quả · Chờ người duyệt quyết định")
            if summary:
                metrics.set("Model: %s · %d lần gọi · Token vào %d / ra %d" % (
                    ", ".join(summary["models"]) or "—", summary["model_calls"],
                    summary["tokens_in"], summary["tokens_out"]))
            button.configure(state="normal")
        window.after(100, poll)

    poll()
    window.mainloop()


if __name__ == "__main__":
    main()
