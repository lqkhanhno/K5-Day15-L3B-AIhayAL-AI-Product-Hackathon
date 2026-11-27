# Chi phí khi dùng thật · A3

**Trạng thái CP2.** Demo dùng model giả, token ghi nhận bằng 0 trong chế độ này. Chi phí triển khai đang chờ số đo từ model thật và tỉ lệ đạt của lượt 2. Giả thuyết về thời gian dò nguồn vẫn đang được khảo sát. [Bằng chứng](../evidence/summary.md)

| Đầu vào cần đo | Nguồn dự kiến |
|---|---|
| Phiên rà ít, vừa và nhiều | Số nhận định cần đối chiếu trong các buổi duyệt, ước lượng theo tháng từ khảo sát hoặc phỏng vấn. |
| Token vào/ra và số lần gọi | Kết quả `python run.py simulate` trên ít nhất 50 phiên. |
| Tỉ lệ tác vụ đạt | Lượt 2 và `python run.py score`. |
| Giá ít nhất hai mức model | Bảng giá của BTC hoặc trang giá chính thức của nhà cung cấp tại lúc lập báo cáo. |

Sau khi có đầu vào, dùng `python run.py simulate` để lập bảng theo ba kịch bản thấp, cơ sở và cao. Chi phí một tác vụ thành công bằng chi phí trung bình mỗi phiên chia tỉ lệ đạt. So chi phí theo người/tháng với thời gian tiết kiệm đã đo.
