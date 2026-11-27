# Data card — nguồn video và benchmark kiểm chứng nhận định

## Dataset 1 · Nguồn đối chiếu bản nháp

| Mục | Nội dung |
|---|---|
| Nguồn | [Video EjAT5n6r-UQ](https://www.youtube.com/watch?v=EjAT5n6r-UQ), “Bài 28 - Đánh giá và chất lượng AI: eval, hallucination, guardrails và an toàn”, kênh Code toàn bug; 449 giây |
| Ngày lấy | 27/11/2026 |
| Cách lấy | Phụ đề tiếng Việt tự động của YouTube, tải bằng yt-dlp chính thức vào thư mục tạm; không tải video/audio |
| Bản lưu trong repo | `video-eval-source.json`: 7 đoạn diễn giải ngắn bằng AI, có mã và thời gian; không phải transcript nguyên văn |
| Xử lý | Đọc phụ đề, bỏ đoạn mất lời/thuật ngữ trọng yếu; diễn giải ý rõ; giữ thời gian để tra lại |
| Trạng thái | `draft_unreviewed`: chưa đối chiếu âm thanh/hình và chưa có người chuyên môn xác nhận |
| Giới hạn | Phụ đề thiếu nhiều thuật ngữ tiếng Anh, thiếu lời hữu ích khoảng 04:05–05:55. Không suy diễn phần ba cách chấm/guardrails bị thiếu. Chưa phải tài liệu đã duyệt theo canvas |

Bản chạy đọc bộ đoạn này qua `data/lesson.json` và hiển thị trạng thái nguồn chưa duyệt.

Chỉ thử tính nhất quán với các đoạn nguồn được cấp. Không kết luận kiến thức video đúng ngoài thực tế hoặc toàn video không có thông tin chỉ vì 7 đoạn không nhắc tới. Không dùng nguồn này làm bằng chứng pain. Không lưu lại toàn bộ lời video trong repo; chỉ giữ phần diễn giải ngắn phục vụ benchmark.

## Dataset 2 · Benchmark kiểm chứng nhận định

| Mục | Nội dung |
|---|---|
| File | `../eval/benchmark.csv` |
| Số câu | 30: 10 khớp nguồn, 6 mâu thuẫn, 12 thiếu căn cứ và 2 yêu cầu nhập lại nhận định |
| Tình huống | 7 `thuong`, 21 `kho`, 2 `tu_choi` (hai ca chèn chỉ dẫn) |
| Nguồn câu | V28-01–20 là `tu_viet` tạo từ phụ đề. V28-21–30 là `data_that`: trích ngắn bốn phát biểu từ tài liệu OpenAI và sáu phát biểu từ tài liệu đọc thêm của BTC. Cột `source` liên kết đoạn trích gốc. |
| Cách dựng | Tập ban đầu gồm diễn đạt lại, đảo nghĩa, thiếu căn cứ và hai ca chèn chỉ dẫn. 10 câu bổ sung giữ nguyên nội dung trích, bỏ đánh dấu Markdown nếu có. Mỗi đáp án chỉ dựa trên 7 đoạn được cung cấp cho bản chạy. |
| Seed | Không áp dụng. Ca tự viết và đoạn trích chọn thủ công đều lưu cố định trong CSV. |
| Nhãn | 28 nhãn nội dung do Codex đề xuất sau khi đối chiếu 7 đoạn nguồn. Hai kết quả từ chối theo hợp đồng đầu vào. Chưa ghi nhận xác nhận của người chuyên môn. |
| Rò rỉ đáp án | Chỉ input được gửi cho agent; expected/pass_criterion dành cho người chấm, không nạp vào tool hoặc context |
| Giới hạn | 10/30 đầu vào là trích đoạn thật. Chưa có ca từ người duyệt hoặc bản nháp pre-class do người duyệt cung cấp. Bốn đoạn tiếng Anh và sáu đoạn tiếng Việt không đại diện cho tần suất gặp trong công việc thực tế. |

Trước đánh giá chính thức, người chuyên môn kiểm nguồn và nhãn. Giữ nguyên chuẩn đạt CP2 và các đáp án đã dùng khi báo cáo kết quả.
