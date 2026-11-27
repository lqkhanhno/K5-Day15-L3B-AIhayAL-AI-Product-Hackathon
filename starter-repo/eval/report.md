# Báo cáo đánh giá · A3

## Kiểm tra tích hợp CP2 · 27/11

| Hạng mục | Kết quả thực tế |
|---|---|
| Luồng nhập liệu | Trước khi tích hợp, 20/20 đầu vào bị từ chối vì trường `video_id` không thuộc hợp đồng. Sau khi thống nhất JSON `claim`, 18 câu nội dung đi đến bước đọc nguồn và gọi model giả. Hai ca chèn chỉ dẫn được yêu cầu nhập lại và có 0 lần gọi model. |
| Kiểm thử tự động | 20 kiểm thử Python chạy qua. |
| Bộ chạy eval | Sau khi bổ sung nguồn đầu vào, `python run.py eval` xử lý 30 câu ở chế độ fake. 28 câu đọc nguồn và gọi model giả. Hai ca từ chối yêu cầu nhập lại và có 0 lần gọi model. Khung ghi `run-mock.csv` và không tạo lượt chính thức. |
| Demo CP2 | `python run.py` hiển thị ba nhãn trên nguồn `A3-V28` và ghi rõ nguồn chưa được duyệt. |
| Độ phủ nguồn | 10/30 câu là trích đoạn có nguồn gốc công khai, gồm 4 đoạn từ tài liệu OpenAI và 6 đoạn từ tài liệu đọc thêm của BTC. Còn chờ người chuyên môn duyệt tập đoạn đối chiếu và nhãn. Chưa ghi nhận chấm độc lập. |

Ví dụ từ kiểm tra giả: **V28-01** kỳ vọng khớp nguồn nhưng trả thiếu căn cứ vì cách diễn đạt khác chữ trong đoạn. **V28-08** kỳ vọng mâu thuẫn nhưng trả thiếu căn cứ vì phủ định được diễn đạt bằng một câu khác. Đây là giới hạn của cách so chữ trong mock. Hai ví dụ thuộc kiểm tra tích hợp, không tính vào lượt chấm chính thức.

## Kết quả model thật

| Lượt | Run ID | Đạt / tổng | % | So với chuẩn đạt |
|---|---|---|---|---|
| 1 · CP3 | Chưa chạy | Chưa có | Chưa có | Chưa chấm |
| 2 · CP4 | Chưa chạy | Chưa có | Chưa có | Chưa chấm |

Sau khi nối model và chấm lượt 1, ghi ít nhất 3 lỗi có đầu vào, đầu ra và lý do. Chọn một lỗi để sửa rồi chạy lại cùng bộ thử. Cập nhật bảng bằng kết quả của `python run.py score`. [Hồ sơ đánh giá](README.md) · [Metric spec](metric_spec.yaml)
