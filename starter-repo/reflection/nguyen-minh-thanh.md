# Reflection — Nguyễn Minh Thành

> Bản nháp tổng hợp từ repo và các issue/PR. Thành viên xác nhận phần việc, chỉnh bằng lời của mình và bổ sung kết quả thật khi có.

## 1. Vai trò và phần việc

- Phụ trách bản chạy thử từ nhận định đến kết quả đối chiếu và chỗ người duyệt quyết định.
- PR #5 triển khai đọc nguồn cục bộ, kiểm mã đoạn, CLI và 20 kiểm thử tự động.
- Đã kiểm luồng giả trong bản tích hợp. Bước gọi model thật còn ở CP3. [Hướng dẫn demo](../docs/a3-demo.md)

## 2. AI hỗ trợ thế nào

- Theo khai báo của PR, Codex hỗ trợ code workflow, mẫu prompt và kiểm thử.
- Python kiểm cấu trúc đầu ra và mã đoạn. Phần so chữ dùng để minh họa quy trình.
- Cần bổ sung nhận xét cá nhân về cách rà code và lỗi sửa khi chạy model thật. [Khai báo dùng AI](../docs/ai-usage.md)

## 3. Một câu thử và bài học

- V28-01 trước đó bị chặn do trường video_id. Sau khi tích hợp, ca vào đúng luồng và mock trả thiếu căn cứ.
- Ca này giúp phân biệt lỗi đầu vào với giới hạn của phép so chữ.
- Bài học dự kiến là kiểm một dòng CSV qua toàn bộ luồng rồi mới đánh giá nhãn bằng model thật. [Báo cáo đánh giá](../eval/report.md)
