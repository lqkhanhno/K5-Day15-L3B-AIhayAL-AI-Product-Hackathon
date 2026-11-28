# Tổng hợp bằng chứng pain · A3

## Tình trạng tại CP3 · 28/11

**Lương Đức Anh** phụ trách thu bằng chứng. Quốc Khánh tổng hợp kết quả vào Canvas và spec. [Phân công trên Issue #2](https://github.com/lqkhanhno/K5-Day15-L3B-AIhayAL-AI-Product-Hackathon/issues/2)

**Giả thuyết.** Người duyệt phải lần lại tài liệu để đối chiếu nhận định, làm chậm việc duyệt và có thể bỏ sót lỗi kiến thức.

- **Khảo sát.** Đức Anh bàn giao **9 lượt sau khi loại 2 lượt thử** trong 11 lượt gửi. Trong 9 lượt, 1 người tự khai từng làm nội dung cho AI20K, 3 người từng làm cho khóa khác và 5 người chưa từng. Nhóm chưa xác minh họ có ngoài nhóm hay trực tiếp duyệt kịch bản pre-class. [PR #8](https://github.com/lqkhanhno/K5-Day15-L3B-AIhayAL-AI-Product-Hackathon/pull/8) · [Bản ghi đã bỏ thông tin liên hệ](survey/responses-draft.md) · [Bộ câu hỏi và cách lọc phản hồi](survey/questions.md) · [Form khảo sát](https://docs.google.com/forms/d/e/1FAIpQLSeOVbCCEn564qpXljP-23PB7YIuRyXd0jzqhC38SZzwfsKWJQ/viewform)
- **Phỏng vấn.** Repo chưa có ghi chép từ người từng trực tiếp duyệt kịch bản pre-class.
- **Bối cảnh từ đề A3.** Đề A3 của BTC đặt trọng tâm vào kiểm kiến thức, tìm nguồn cho từng nhận định và xác định người duyệt. Nhóm cần hỏi người duyệt về lần làm việc gần nhất, tần suất và thời gian thực tế. [Đề Track A3](../../tracks/track-a-edtech.md#a3--sản-xuất-bài-giảng-bằng-ai)
- **Dữ liệu BTC.** Tệp pre-class ghi hoạt động học viên. Bộ này không ghi các lượt người duyệt dò nguồn cho kịch bản. [Mô tả bộ dữ liệu](../../data/preclass/README.md)

### Trích dẫn nguyên văn từ khảo sát sơ bộ

| Mã | Bối cảnh tự khai | Trích dẫn |
|---|---|---|
| S04 | Sản xuất nội dung cho AI20K, khó khăn khi kiểm tra | “Kiểm tra lại kết quả ai” |
| S02 | Sản xuất nội dung cho khóa khác, bước đã làm | “Đối chiếu với nội dung bài học xem đã đúng hay chưa” |
| S05 | Sản xuất nội dung cho khóa khác, khó khăn khi kiểm tra | “Ít nguồn” |
| S07 | Sản xuất nội dung cho khóa khác, cách dùng công cụ | “giao cho claude bản draft rồi vẫn double-check” |
| S07 | Sản xuất nội dung cho khóa khác, phản hồi về khó khăn | “không có khó khăn đáng kể” |

Trong 4 người tự khai có kinh nghiệm, 3 người chọn khoảng 15–30 phút và 1 người chọn 31–60 phút cho bước kiểm tra gần nhất. Khảo sát chưa tách được thời gian mỗi nhận định. [Từng phản hồi](survey/responses-draft.md)

**Kết luận tại CP3.** Đã có 5 trích dẫn sơ bộ để rà lại. Mẫu chưa đạt ngưỡng 20 người ngoài nhóm đúng đối tượng. Giả thuyết và số liệu impact vẫn cần kiểm chứng. Xem cách tính tại §2 của [spec](../spec.md).

## Cách tổng hợp khi có câu trả lời

Ghi vai trò, lần duyệt gần nhất, số lần gặp trong tháng và số phút thực tế mất để tra nguồn. Với khảo sát, chỉ tính người ngoài nhóm có kinh nghiệm trực tiếp phù hợp với lát cắt, lưu bộ câu hỏi và phản hồi đã ẩn danh. Với phỏng vấn, dùng mã P1, P2… trong [thư mục ghi chép](interviews/). Cập nhật số đầu tiên và một trích dẫn đã bỏ tên vào Canvas.

Để đạt yêu cầu bằng chứng, cần ít nhất 3 phỏng vấn hoặc 20 phản hồi khảo sát đúng đối tượng ngoài nhóm, cùng ít nhất 5 trích dẫn hoặc ví dụ có nguồn. Hiện chưa thể tính impact bằng số.
