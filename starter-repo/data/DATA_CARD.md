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

## Dataset 2 · Benchmark synthetic

| Mục | Nội dung |
|---|---|
| File | `../eval/benchmark.csv` |
| Số câu | 20: 7 khớp nguồn, 6 mâu thuẫn, 5 thiếu căn cứ và 2 yêu cầu nhập lại nhận định |
| Tình huống | 7 `thuong`, 11 `kho`, 2 `tu_choi` (hai tấn công chèn chỉ dẫn) |
| Nguồn câu | Tất cả `tu_viet`: AI tự viết dựa trên ý trong phụ đề; không phải câu người dùng thật |
| Cách sinh | Diễn đạt lại 7 ý; đảo nghĩa/điều kiện 7 câu; thêm 6 khẳng định chưa có căn cứ. Hai câu chèn chỉ dẫn ép nhãn/bịa nguồn |
| Seed | Không áp dụng; soạn bằng AI, CSV được lưu cố định, không lấy mẫu ngẫu nhiên |
| Nhãn | 18 nhãn nội dung do AI đề xuất, 2 kết quả từ chối do hợp đồng đầu vào quy định. Chưa ghi nhận xác nhận của người chuyên môn. |
| Rò rỉ đáp án | Chỉ input được gửi cho agent; expected/pass_criterion dành cho người chấm, không nạp vào tool hoặc context |
| Giới hạn | Chưa có câu từ người duyệt thật; chưa đạt yêu cầu ≥1/3 câu từ người dùng/data thật của khung. Không đổi source thành data_that chỉ vì dùng video thật |

Trước đánh giá chính thức: người chuyên môn kiểm nguồn và cả 20 nhãn; bổ sung ca thực tế từ người duyệt; tách tập chỉnh prompt với tập đánh giá giữ kín; chốt chuẩn đạt trước CP2. Không sửa expected để khớp output sau khi chạy.
