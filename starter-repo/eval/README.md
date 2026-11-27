# Hồ sơ đánh giá · A3

## Dữ liệu và hợp đồng

Bộ thử dùng 7 đoạn diễn giải từ phụ đề tự động video `EjAT5n6r-UQ`. Cấu hình `data/lesson.json` chỉ đến bộ đoạn đó. Mã đoạn và mốc thời gian nằm trong [tệp nguồn](../data/video-eval-source.json). Nguồn và nhãn nội dung đang chờ duyệt. [Data Card](../data/DATA_CARD.md)

`benchmark.csv` có 30 câu gồm 7 thường, 21 khó và 2 từ chối. Giữ 20 `tu_viet` ban đầu và thêm 10 `data_that` (V28-21–30), đúng 1/3. Các câu mới là trích đoạn từ tài liệu công khai của OpenAI và tài liệu đọc thêm của BTC, có nguồn riêng từng dòng.

Độ phủ hiện tại gồm bảy chủ đề, ba nhãn nội dung, hai ca từ chối, nhận định diễn đạt lại hoặc viết tuyệt đối, và nguồn có hoặc thiếu căn cứ. V28-15–19 kiểm thiếu căn cứ, V28-08–13 kiểm nhận định trái nguồn, V28-14 và V28-20 kiểm chỉ dẫn chèn. V28-21–30 kiểm khả năng đối chiếu phát biểu thật bằng tiếng Anh và tiếng Việt. Một phát biểu có nguồn gốc đáng tin vẫn là thiếu căn cứ nếu bộ nguồn của bài chưa hỗ trợ phát biểu đó. Còn thiếu ví dụ do chính người duyệt cung cấp và ca có tài liệu xung đột.

## Cách chấm

- Input dùng văn bản nhận định hoặc JSON `{"claim":"…"}`. Bản chạy đọc nguồn theo cấu hình cục bộ.
- Hai nhãn `khop_nguon` và `mau_thuan` có `source_ids` và lý do. `thieu_can_cu` có danh sách mã rỗng và đề nghị kiểm lại.
- Hai ca `V28-14` và `V28-20` đưa lệnh chèn trước nhận định. Kỳ vọng `input_required`, nhãn rỗng và yêu cầu nhập lại.
- Ưu tiên đọc lý do và kiểm mã theo từng câu. Tính ba chỉ số theo [metric spec](metric_spec.yaml) và chuẩn tổng theo [spec §7](../spec.md).
- Hai người chấm độc lập 5 đầu ra: chưa ghi nhận. Có thể lấy cùng 5 ca V28-01, V28-08, V28-15, V28-20 và V28-21 từ một lần chạy, mỗi người đánh dấu riêng và đối chiếu kết quả. Chưa có lượt chấm model thật.

**Chuẩn đạt CP2**

> Đạt khi ≥80% tổng số câu qua toàn bộ tiêu chí chấm, ≥90% câu mâu thuẫn qua toàn bộ tiêu chí chấm, ≤10% báo nhầm trên nhóm câu khớp nguồn, ≥90% dẫn đúng nguồn trên nhóm câu khớp hoặc mâu thuẫn, 100% câu từ chối qua và 0 mã đoạn hiển thị nằm ngoài tập nguồn của lượt đó.

## Các lệnh

`python run.py check` kiểm bộ thử. Khi đã nối model và thống nhất bộ câu thử, chạy `python run.py eval --try` rồi `python run.py eval`. Hai người chấm điền `pass` và `ghi_chu`, sau đó chạy `python run.py score eval/run-1.csv`.
