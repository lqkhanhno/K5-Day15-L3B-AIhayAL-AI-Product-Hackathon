# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Viết workflow A3; cập nhật theo spec §4 với get_approved_passages, cấu hình bài, source_ids, nhánh cần nhập nhận định và xóa lý do chưa xác minh | Đã chạy 20 kiểm thử tự động; Nguyễn Minh Thành cần đọc/kiểm tay trước khi nộp, chưa có xác nhận | Nguyễn Minh Thành |
| Prompt / thiết kế lời gọi mô hình | Codex | Soạn prompt trả label/source_ids/reason, coi nguồn là dữ liệu và chuyển người khi thiếu căn cứ; quyết định CP2 đang dùng mock | Chưa kiểm với model thật | Nguyễn Minh Thành |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Codex | Tổng hợp 7 đoạn từ phụ đề, soạn 20 ca tự viết và chọn 10 trích đoạn từ tài liệu công khai. Đề xuất nhãn và lý do dựa trên 7 đoạn đối chiếu. | Đã kiểm vị trí và nguồn 10 đoạn trích. Chưa ghi nhận người chuyên môn duyệt nhãn hoặc hai người chấm độc lập. | Nguyễn Nam Khánh |
| Sinh data `synthetic` (nếu có) | Codex | Soạn trực tiếp 3 đoạn nguồn và 3 ca minh họa CP2; không dùng làm bằng chứng pain | Không lấy mẫu ngẫu nhiên; chưa có xác nhận kiểm tay của thành viên nhóm | Nguyễn Minh Thành |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Spec, Canvas, báo cáo và reflection | Codex | Soạn luồng, tổng hợp tiến độ GitHub, ghi kiểm tra tích hợp và soạn bản nháp reflection | Thành viên xác nhận nội dung gắn tên mình và bổ sung kết quả thật | Cả nhóm |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
