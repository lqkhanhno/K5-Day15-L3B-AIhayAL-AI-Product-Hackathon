# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Viết workflow A3, công cụ đọc nguồn, CLI, kiểm trích dẫn và kiểm thử tự động | Đã chạy kiểm tự động; Nguyễn Minh Thành cần đọc/kiểm tay trước khi nộp, chưa có xác nhận | Nguyễn Minh Thành |
| Prompt / thiết kế lời gọi mô hình | Codex | Soạn prompt trả JSON, coi nguồn là dữ liệu và chuyển người khi thiếu căn cứ; quyết định CP2 đang dùng mock | Chưa kiểm với model thật | Nguyễn Minh Thành |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | Codex | Soạn trực tiếp 3 đoạn nguồn và 3 ca minh họa CP2; không dùng làm bằng chứng pain | Không lấy mẫu ngẫu nhiên; chưa có xác nhận kiểm tay của thành viên nhóm | Nguyễn Minh Thành |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
