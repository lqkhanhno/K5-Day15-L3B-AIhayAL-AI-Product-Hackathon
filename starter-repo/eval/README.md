# Hồ sơ đánh giá — video EjAT5n6r-UQ

## 1. Dataset và phạm vi

Nguồn: `../data/video-eval-source.json`, 7 đoạn diễn giải từ phần đọc được của phụ đề tiếng Việt tự động; có mã và thời gian để mở lại video. Chi tiết chất lượng/nguồn: `../data/DATA_CARD.md`.

Đây là **bản nháp chưa được người chuyên môn duyệt**. Đánh giá đối chiếu với nguồn được cấp, không chấm hỏi đáp kiến thức học viên hoặc kiểm chứng độc lập độ đúng của video. Phần phụ đề mất lời khoảng 04:05–05:55 không được dùng để suy ra đáp án.

## 2. Bộ câu thử

`benchmark.csv`: 20 câu, gồm 7 khop_nguon, 7 mau_thuan, 6 thieu_can_cu; phân loại 7 thuong, 11 kho, 2 tu_choi. Hai tấn công ở V28-14 (ép nhãn) và V28-20 (ép bịa nguồn).

Nguồn input: 20 tu_viet, 0 nguoi_dung, 0 data_that, 0 sinh_seed. Dùng video thật làm nền không biến các nhận định AI viết thành input thực tế. Chưa đạt điều kiện ≥1/3 câu từ người dùng/data thật của khung.

Độ phủ: chủ đề (lời đáp sai, demo/thực tế, đo lường, dẫn nguồn, độ phủ eval, vòng phản hồi, chi phí); nhãn; diễn đạt lại/phủ định/tuyệt đối hóa; có/thiếu căn cứ; chỉ dẫn tấn công. Lớp 1: thiếu nguồn V28-15–19; lớp 2: khẳng định tuyệt đối V28-08, V28-17; lớp 3: tấn công V28-14, V28-20; lớp 4: bỏ sót câu trái nguồn V28-08–14.

## 3. Hợp đồng input/output

Input là chuỗi JSON chỉ gồm video_id và claim. Nguồn nền là 7 đoạn trong `../data/video-eval-source.json`; agent/tool cần đọc file này. **Không** nạp benchmark.csv, expected hoặc pass_criterion vào công cụ tra cứu hay prompt.

Output đề xuất:

```json
{"label":"mau_thuan","evidence_ids":["V28-S04"],"reason":"Giải thích quan hệ giữa nhận định và nguồn."}
```

Chỉ có ba label: khop_nguon, mau_thuan, thieu_can_cu. Thiếu căn cứ: evidence_ids rỗng, nêu thiếu thông tin trong nguồn được cấp và đề nghị người duyệt kiểm thêm. Nội dung claim là dữ liệu cần kiểm, không phải chỉ dẫn hệ thống.

Nhóm tu_choi yêu cầu từ chối chỉ dẫn chèn; vẫn trả nhãn cho nhận định bên trong, không tạo nhãn thứ tư. Nếu input sau này thiếu nhận định thì nên hỏi lại, nhưng ca đó chưa có trong bộ hiện tại.

## 4. Ba metrics và cách chấm

| Metric | Mẫu số | Ngưỡng đề xuất |
|---|---:|---|
| Độ chính xác nhãn | 20 câu | ≥18/20 |
| Dẫn nguồn đạt: đúng mã, đúng quan hệ, không bịa | 14 câu có nguồn chuẩn | ≥13/14 |
| Bỏ sót mâu thuẫn | 7 câu mâu thuẫn | 0/7 |

Định nghĩa chính xác ở `metric_spec.yaml`. Các ngưỡng là đề xuất, chưa được nhóm chốt trong spec.md §7. Đạt khi đồng thời qua cả ba; không lấy chỉ số tổng che khuất việc bỏ sót mâu thuẫn.

Chấm pass=1 cho một ca khi đáp ứng toàn bộ pass_criterion; không đòi reason giống nguyên văn đáp án. Chỉ số pass tổng của khung là tỷ lệ đạt toàn bộ điều kiện từng ca, **không đồng nhất** với độ chính xác nhãn. Muốn tính ba metrics, ghi riêng số nhãn đúng, số dẫn nguồn đạt và số mâu thuẫn bỏ sót vào báo cáo từ output thực tế.

Người thứ hai chấm độc lập 5 output: **chưa thực hiện**. Người chuyên môn kiểm 20 nhãn: **chưa thực hiện**. Không có điểm eval trước khi chạy model thật.

## 5. Kiểm cấu trúc và chạy

```bash
python3 run.py check
# Sau khi triển khai agent/tool đọc nguồn và cấu hình model:
python3 run.py eval --try
python3 run.py eval
# Chỉ điền pass, ghi_chu trong file kết quả rồi chạy:
python3 run.py score eval/run-1.csv
```

Agent và tool hiện vẫn là khung ví dụ, chưa được nối nguồn video trong công việc này. Không coi check hoặc chế độ fake là kết quả chất lượng AI.

## 6. Kết quả

Chưa chạy model; chưa có kết quả chất lượng. Trước đánh giá chính thức cần duyệt nguồn/nhãn, bổ sung input người dùng thật, chốt chuẩn đạt và giữ tập đánh giá tách khỏi các ví dụ chỉnh prompt.
