"""Cửa sổ quay demo CP3: dùng nguyên answer() và tracing của ứng dụng CLI."""
import json
from pathlib import Path
import queue
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime, timezone

from agent import answer
from ai import MODEL_PROVIDER, MODEL_NAME
from tools import load_lesson
import tracing

ROOT = Path(__file__).resolve().parents[1]


def main():
    window = tk.Tk()
    window.title("AIhayAL - CP3 - Nguyen Minh Thanh")
    window.geometry("1100x760+40+40")
    window.configure(bg="#f4f6fa")
    window.option_add("*Font", "{Segoe UI} 12")
    tk.Label(window, text="AIhayAL · Rà một nhận định pre-class", font=("Segoe UI", 22, "bold"),
             bg="#f4f6fa", fg="#172b4d").pack(anchor="w", padx=24, pady=(16, 4))
    lesson = load_lesson()
    tk.Label(window, text="Nguyễn Minh Thành · CP3 · %s / %s" % (MODEL_PROVIDER, MODEL_NAME),
             bg="#f4f6fa").pack(anchor="w", padx=24)
    tk.Label(window, text="%s · Nguồn bản nháp từ phụ đề, chờ kiểm duyệt" % lesson["lesson_id"],
             bg="#f4f6fa", fg="#775600").pack(anchor="w", padx=24, pady=(4, 10))
    tk.Label(window, text="Nhận định cần đối chiếu", bg="#f4f6fa").pack(anchor="w", padx=24)
    claim = tk.Text(window, height=3, wrap="word", font=("Segoe UI", 13), padx=10, pady=8)
    claim.pack(fill="x", padx=24, pady=(4, 8))
    cases = json.loads((ROOT / "data/demo_cases.json").read_text(encoding="utf-8"))
    claim.insert("1.0", cases[0]["input"])
    messages = queue.Queue()
    status = tk.StringVar(value="Sẵn sàng · Bấm để gọi model thật")
    metrics = tk.StringVar(value="Chưa gọi model trong lượt này")

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
            messages.put((result["output"], summary, None))
        except Exception as exc:
            tracing.end()
            messages.put(("", None, "%s: %s" % (type(exc).__name__, exc)))

    def run():
        text = claim.get("1.0", "end").strip()
        button.configure(state="disabled")
        status.set("Đang gọi model thật…")
        output.configure(state="normal")
        output.delete("1.0", "end")
        output.configure(state="disabled")
        threading.Thread(target=worker, args=(text,), daemon=True).start()

    button = tk.Button(window, text="Đối chiếu với nguồn bài học", command=run,
                       bg="#1749a0", fg="white", padx=18, pady=8)
    button.pack(anchor="w", padx=24)
    tk.Label(window, textvariable=status, bg="#f4f6fa", fg="#1749a0").pack(anchor="w", padx=24, pady=8)
    output = ScrolledText(window, height=10, wrap="word", font=("Segoe UI", 12), padx=10, pady=10, state="disabled")
    output.pack(fill="both", expand=True, padx=24)
    tk.Label(window, textvariable=metrics, bg="#f4f6fa", fg="#1749a0",
             font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=24, pady=12)

    def poll():
        try:
            text, summary, error = messages.get_nowait()
        except queue.Empty:
            pass
        else:
            output.configure(state="normal")
            output.insert("1.0", error or text)
            output.configure(state="disabled")
            status.set("Lỗi kết nối" if error else "Đã nhận kết quả · Chờ người duyệt quyết định")
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
