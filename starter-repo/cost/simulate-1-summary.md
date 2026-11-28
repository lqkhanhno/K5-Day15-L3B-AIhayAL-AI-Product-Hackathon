# Tóm tắt mô phỏng simulate-1@20261128-145218

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| duyet_it | 22 | 1 | 734 | 137 | 1.0 | 1.0 |
| duyet_vua | 16 | 1 | 721 | 129 | 0.9 | 0.9 |
| duyet_nhieu | 12 | 1 | 703 | 124 | 0.9 | 0.9 |

Tỉ lệ đạt dùng để tính: 21/30 (70%) — lượt run-2@20261128-114555

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (2 người) | Chi phí / tháng — cơ sở (4 người) | Chi phí / tháng — cao (8 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano-2026-03-17 (vào 0.2 · ra 1.25 $/1M) | $0.00031 | $0.00044 | $0.00044 | $0.0046 | $0.0093 | $0.0185 | $0.0023 |
| gpt-5.4-mini-2026-03-17 (vào 0.75 · ra 4.5 $/1M) | $0.0011 | $0.0016 | $0.0016 | $0.0170 | $0.0340 | $0.0680 | $0.0085 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-nano-2026-03-17. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
