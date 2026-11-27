# Reflection — Nguyễn Nam Khánh

> Bản nháp tổng hợp từ repo và các issue/PR. Thành viên xác nhận phần việc, chỉnh bằng lời của mình và bổ sung kết quả thật khi có.

## 1. Vai trò và phần việc

- Phụ trách tập đoạn nguồn, bộ câu thử và hồ sơ chấm của hướng A3.
- PR #4 bổ sung 7 đoạn nguồn có mã và mốc video, 20 câu thử và 3 metric.
- Phần cần xác nhận là nguồn và nhãn nội dung. [Data Card](../data/DATA_CARD.md) · [Hồ sơ đánh giá](../eval/README.md)

## 2. AI hỗ trợ thế nào

- Theo khai báo của PR, Codex hỗ trợ xử lý phụ đề, diễn giải đoạn nguồn và soạn câu thử, nhãn đề xuất.
- PR ban đầu có 20 đầu vào tu_viet. Bản gộp bổ sung 10 trích đoạn từ tài liệu công khai có dẫn nguồn. Đối chiếu nguồn và đáp án với người chuyên môn trước lượt đánh giá chính thức.
- Cần bổ sung nhận xét cá nhân về chỗ đã xác minh hoặc sửa sau khi đọc các đoạn và câu thử. [Khai báo dùng AI](../docs/ai-usage.md)

## 3. Một câu thử và bài học

- V28-08 được gán kỳ vọng mâu thuẫn nhưng mock trả thiếu căn cứ khi câu viết khác nguồn.
- Cần tách kiểm tra định dạng đầu ra khỏi đánh giá năng lực đọc hiểu với model thật.
- Bài học dự kiến là giữ các câu diễn đạt lại trong bộ thử và yêu cầu lý do chỉ rõ vế bị bác bỏ. [Báo cáo đánh giá](../eval/report.md)
