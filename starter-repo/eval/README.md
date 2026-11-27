# Hồ sơ đánh giá · A3

## Dữ liệu và hợp đồng

Bộ thử dùng 7 đoạn diễn giải từ phụ đề tự động video `EjAT5n6r-UQ`. Cấu hình `data/lesson.json` chỉ đến bộ đoạn đó. Mã đoạn và mốc thời gian nằm trong [tệp nguồn](../data/video-eval-source.json). Nguồn và nhãn nội dung đang chờ duyệt. [Data Card](../data/DATA_CARD.md)

`benchmark.csv` có 20 câu gồm 7 thường, 11 khó và 2 từ chối. Nguồn đầu vào là 20 `tu_viet`. `python run.py check` báo 0/20 câu từ người dùng hoặc dữ liệu thật. Nếu giữ tổng 20, cần ít nhất 7 ca có nguồn thực tế.

Độ phủ hiện tại gồm bảy chủ đề, ba nhãn nội dung, hai ca từ chối, nhận định diễn đạt lại hoặc viết tuyệt đối, và nguồn có hoặc thiếu căn cứ. V28-15–19 kiểm thiếu căn cứ, V28-08–13 kiểm nhận định trái nguồn, V28-14 và V28-20 kiểm chỉ dẫn chèn. Còn thiếu ví dụ từ người duyệt và ca dùng tài liệu có phiên bản hoặc nội dung bất nhất.

## Cách chấm

- Input dùng văn bản nhận định hoặc JSON `{"claim":"…"}`. Bản chạy đọc nguồn theo cấu hình cục bộ.
- Hai nhãn `khop_nguon` và `mau_thuan` có `source_ids` và lý do. `thieu_can_cu` có danh sách mã rỗng và đề nghị kiểm lại.
- Hai ca `V28-14` và `V28-20` đưa lệnh chèn trước nhận định. Kỳ vọng `input_required`, nhãn rỗng và yêu cầu nhập lại.
- Ưu tiên đọc lý do và kiểm mã theo từng câu. Tính ba chỉ số theo [metric spec](metric_spec.yaml) và chuẩn tổng theo [spec §7](../spec.md).
- Hai người chấm độc lập 5 đầu ra: chưa ghi nhận. Chưa có lượt chấm model thật.

**Chuẩn đạt CP2**

> Đạt khi ≥80% tổng số câu qua toàn bộ tiêu chí chấm, ≥90% câu mâu thuẫn qua toàn bộ tiêu chí chấm, ≤10% báo nhầm trên nhóm câu khớp nguồn, ≥90% dẫn đúng nguồn trên nhóm câu khớp hoặc mâu thuẫn, 100% câu từ chối qua và 0 mã đoạn hiển thị nằm ngoài tập nguồn của lượt đó.

## Các lệnh

`python run.py check` kiểm bộ thử. Khi đã nối model và thống nhất bộ câu thử, chạy `python run.py eval --try` rồi `python run.py eval`. Hai người chấm điền `pass` và `ghi_chu`, sau đó chạy `python run.py score eval/run-1.csv`.
