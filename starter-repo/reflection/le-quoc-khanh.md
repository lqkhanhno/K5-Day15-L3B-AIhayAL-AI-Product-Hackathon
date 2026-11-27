# Reflection — Lê Quốc Khánh

> Bản nháp tổng hợp từ repo và các issue/PR. Thành viên xác nhận phần việc, chỉnh bằng lời của mình và bổ sung kết quả thật khi có.

## 1. Vai trò và phần việc

- Đội trưởng, phụ trách thiết kế luồng rà một nhận định trước khi duyệt kịch bản.
- Phần việc có trong commit dc8fc08, gồm sơ đồ, bước kiểm mã nguồn và tiêu chí đánh giá.
- Tổng hợp tiến độ khảo sát và thay đổi so với CP1. [Spec](../spec.md) · [Canvas](../canvas.md)

## 2. AI hỗ trợ thế nào

- Codex hỗ trợ soạn sơ đồ, tiêu chí chấm và tóm tắt tiến độ từ repo.
- Ở bản tích hợp, quy tắc đo được đối chiếu lại để YAML và spec dùng cùng ngưỡng.
- Cần xác nhận cá nhân về cách kiểm phần thiết kế và các sửa đổi trước khi nộp. [Khai báo dùng AI](../docs/ai-usage.md)

## 3. Một câu thử và bài học

- V28-01 từng bị từ chối ở bước đọc đầu vào vì benchmark thêm video_id ngoài hợp đồng.
- Kiểm tra tích hợp xác nhận ca đi được vào luồng sau khi dùng chung JSON claim.
- Bài học dự kiến là cần thử sớm một đầu vào nguyên bản từ CSV trước khi hai nhánh tiếp tục làm độc lập. [Báo cáo đánh giá](../eval/report.md)
