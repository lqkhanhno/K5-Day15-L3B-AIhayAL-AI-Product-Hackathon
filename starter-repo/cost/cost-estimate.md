# Chi phí khi dùng thật · AIhayAL A3

## Phạm vi và trạng thái CP4

Một phiên rà một nhận định của người duyệt kịch bản pre-class. Ước tính dưới đây dùng token API đã ghi ở lượt đánh giá 2 và đơn giá trả phí. **Chưa có lượt mô phỏng ≥50 phiên thật.** Lượt thử kết nối 3 phiên bị OpenAI từ chối xác thực (HTTP 401). [Lượt 2 và token](../eval/run-2-metrics.json) · [Cấu hình mô phỏng](personas.yaml)

## Đầu vào

| Đầu vào | Dữ liệu dùng |
|---|---|
| Tác vụ đạt | Lượt `run-2@20261128-114555` đạt 21/30 (70%) theo chấm bằng AI. Model trả về `gpt-5.4-nano-2026-03-17`. |
| Token API | 21.506 token vào, 3.726 token ra, 28 lần gọi trong 30 ca. Hai ca bị chặn hợp lệ trước lời gọi model. Mô phỏng lấy mẫu từ cả ba nhóm câu thử. |
| Phân bố người duyệt | Rà ít 50% × 4, rà vừa 30% × 8, rà nhiều 20% × 16. Trung bình 7,6 lượt/người/tháng *(tự ước tính)*. |
| Quy mô triển khai thử | Thấp 2, cơ sở 4, cao 8 người trực tiếp duyệt *(tự ước tính)*. |
| Giá API | GPT-5.4 nano 0,20 vào / 1,25 ra. GPT-5.4 mini 0,75 vào / 4,50 ra. Đơn vị USD/triệu token, đầu vào tính giá không cache. Xem 28/11/2026. [Giá nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano) · [Giá mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini) |

Khảo sát của Đức Anh là nguồn bằng chứng chính. 9 lượt sau khi loại thử chưa đủ để xác nhận số người trực tiếp duyệt, tần suất rà theo nhận định hay thời gian tiết kiệm. Vì vậy quy mô, tỉ trọng và tần suất ở bảng trên là giả định để dự báo, còn số token và tỷ lệ đạt đến từ lượt 2. [Khảo sát sơ bộ](../evidence/summary.md)

## Dự báo chi phí API

Chi phí bình quân một lượt thử với GPT-5.4 nano = (21.506 × 0,20 + 3.726 × 1,25) ÷ 1.000.000 ÷ 30 = **0,00029862 USD**. Ước tính chi phí mỗi tác vụ đạt = 0,00029862 ÷ 70% = **0,00042660 USD**. Phép tính tính cả chi phí ca trượt và dùng tỷ lệ đạt của cùng model. Tỷ lệ của lượt 2 là tỷ lệ qua bộ thử.

| Kịch bản | Người duyệt | Lượt thử/tháng | Nano USD/tháng | Mini USD/tháng, áp giá lên token nano |
|---|---:|---:|---:|---:|
| Thấp | 2 | 15,2 | 0,00454 | 0,01667 |
| Cơ sở | 4 | 30,4 | 0,00908 | 0,03334 |
| Cao | 8 | 60,8 | 0,01816 | 0,06667 |

Chi phí/tháng = số người duyệt × 7,6 lượt/người × chi phí bình quân một lượt thử. Kịch bản cơ sở với nano tương ứng khoảng **0,00227 USD/người/tháng**. Cột mini so sánh đơn giá với cùng lượng token. Chưa đo token và tỷ lệ đạt của mini nên chưa tính chi phí tác vụ đạt cho model này.

## So với impact

Ví dụ để thử độ nhạy, nếu mỗi lượt thủ công mất 3 phút *(tự ước tính)* thì kịch bản cơ sở có 4 × 7,6 × 3 = **91,2 phút công việc/tháng**. Nhóm chưa đo thời gian thực tế hoàn thành cùng một nhận định trước và sau khi dùng bản thử. Số 91,2 là thời gian công việc giả định, còn thời gian tiết kiệm chưa có số đo. Chi phí trên chỉ gồm token API, chưa gồm hosting hay thời gian của người duyệt. Đề xuất tiếp tục thử với người duyệt trước khi đánh giá hiệu quả triển khai.

## Chạy mô phỏng để thay số dự báo

Dùng cấu hình OpenAI của nhóm cho đúng model `gpt-5.4-nano-2026-03-17`. Chạy trong `starter-repo`:

```text
python run.py simulate --try 3
python run.py simulate --rate-from eval/run-2.csv --wait 4
```

Đối chiếu 50 phiên, model API trả về, số token, lỗi và `run_id` của đầu ra `cost/simulate-N.csv`. Nếu hoàn tất, lấy chi phí phiên thực đo và chia cho 21/30 để cập nhật báo cáo và slide 6. [Hướng dẫn nối model](../docs/connect-model.md)
