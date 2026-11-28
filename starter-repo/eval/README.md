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

**Chuẩn đạt CP2**

> Đạt khi ≥80% tổng số câu qua toàn bộ tiêu chí chấm, ≥90% câu mâu thuẫn qua toàn bộ tiêu chí chấm, ≤10% báo nhầm trên nhóm câu khớp nguồn, ≥90% dẫn đúng nguồn trên nhóm câu khớp hoặc mâu thuẫn, 100% câu từ chối qua và 0 mã đoạn hiển thị nằm ngoài tập nguồn của lượt đó.

## Các lệnh

`python run.py check` kiểm bộ thử. Khi đã nối model và thống nhất bộ câu thử, chạy `python run.py eval --try` rồi `python run.py eval`. Hai người chấm điền `pass` và `ghi_chu`, sau đó chạy `python run.py score eval/run-1.csv`.

## Lượt 1 · CP3

| Hạng mục | Trạng thái |
|---|---|
| File kết quả / trace | [run-1.csv](run-1.csv) · [run-1.jsonl](../traces/run-1.jsonl), 30/30 ca, 0 lỗi kỹ thuật |
| Run ID | `run-1@20261127-224225` |
| Model thực tế / token | `gpt-5.4-nano-2026-03-17`; 28 lần gọi; 16.578 token vào / 3.116 ra. Hai ca từ chối không gọi model |
| Kết quả toàn bộ | **20/30 (66,67%)**, chưa đạt ngưỡng ≥24/30. `score` làm tròn hiển thị 67% |
| Bắt đúng mâu thuẫn | **5/6 (83,33%)**, không đạt ≥90%. V28-09 đúng nhãn nhưng trượt toàn bộ tiêu chí vì dẫn thêm mã |
| Báo nhầm câu khớp | **1/10 (10%)**, đạt ≤10%; ca V28-21 |
| Dẫn đúng nguồn | **12/16 (75%)**, không đạt ≥90%. Trượt ở V28-03, V28-09, V28-21, V28-24 |
| Ca từ chối | **2/2 (100%)**, đạt |
| Mã nguồn hiển thị ngoài tập nguồn | **0**, đạt. Mã thuộc tập nguồn chung vẫn có thể sai danh sách chấp nhận của từng ca |
| Đạt chuẩn CP2 | **Không đạt** theo chấm bằng AI |

### Đối chiếu điểm trên 5 ca

Phiếu chấm bằng AI và phiếu của một người dùng khớp **4/5 (80%)**. Ở V28-21, người dùng chấm 1 và phiếu chấm bằng AI chấm 0. Tiêu chí yêu cầu `khop_nguon` với mã V28-S01, còn đầu ra trả `thieu_can_cu` với danh sách mã rỗng. Kết quả 20/30 trong CSV theo phiếu chấm bằng AI. [Phiếu chấm](crosscheck-run-1.md) · [Bản ghi đối chiếu](crosscheck-run-1.json)

## Hồ sơ chấm lượt 1

- Công cụ chấm đối chiếu 30 đầu ra với tiêu chí và đoạn nguồn. Việc rà nhãn và nguồn bởi người chuyên môn vẫn đang chờ. [Khai báo công cụ chấm](../docs/ai-usage.md)
- Chỉ điền `pass`, `ghi_chu` trong file kết quả; output, input, expected, pass_criterion, metadata và trace được giữ nguyên. Bộ thử và metric spec giống hệt main; spec §7 giữ nguyên.
- [Số đo và SHA-256 phục vụ kiểm lại](run-1-metrics.json) · [Kết quả lệnh score](run-1-score.txt) · [Phân tích lỗi](report.md).
- Theo type: thường 6/7, khó 12/21, từ chối 2/2. Theo nhãn mong đợi: khớp nguồn 7/10, mâu thuẫn 5/6, thiếu căn cứ 6/12, yêu cầu nhập lại 2/2. Các ca thiếu căn cứ đúng tiêu chí đã được tính đạt.
- Các ca trượt: V28-03, V28-09, V28-16, V28-17, V28-19, V28-21, V28-24, V28-26, V28-27, V28-28.


## Lượt 2 · CP4 · 2026-11-28T11:52+07:00

- PR #9, đúng commit Thành bàn giao: `32e490a839eed81b77f481e7af7b39c78da06a77`. Thay đổi prompt yêu cầu xác nhận đủ từng vế, bác bỏ trực tiếp và không suy rộng nguồn. Không chỉnh prompt sau khi xem kết quả lượt 2.
- Run ID: **`run-2@20261128-114555`**. Model API trả về **`gpt-5.4-nano-2026-03-17`**, giống hệt lượt 1; cấu hình gọi `MODEL_PROVIDER=openai`, `MODEL_NAME=gpt-5.4-nano`, timeout 120.
- Chạy `PYTHONUNBUFFERED=1 python3 run.py eval --wait 4`: **30/30 ca**, **0 lỗi kỹ thuật**, 28 lần gọi model; V28-14 và V28-20 chặn trước model.
- **Codex (AI) chấm** cả 30 ca theo expected, pass_criterion và chuẩn CP2. Chỉ sửa pass/ghi_chu. Chưa có người chấm độc lập lượt 2; kết quả chấm chéo 4/5 của lượt 1 không được tính lại cho lượt 2. Metric spec vẫn ghi grader=nguoi nên điểm AI này cần người kiểm, không được trình bày thành hai người chấm độc lập.
- Đã xác nhận bằng SHA-256: cùng benchmark 30 câu, đáp án, tiêu chí, 7 đoạn nguồn, cấu hình bài, provider và khung chạy như lượt 1. Nội dung điều kiện/ngưỡng CP2 không đổi; dòng tiến độ trong §7 đã được main cập nhật trước đó. Lượt 1 và trace lượt 1 giữ nguyên.

**Kết quả: 20/30 → 21/30, tăng 1 câu (+3,33 điểm phần trăm), vẫn chưa đạt CP2.**

| Chỉ số | Lượt 1 | Lượt 2 | Chuẩn CP2 | Lượt 2 |
|---|---|---|---|---|
| Qua toàn bộ tiêu chí | 20/30 (66,67%) | **21/30 (70%)** | ≥80% | Không đạt |
| Bắt đúng mâu thuẫn, tính toàn bộ tiêu chí | 5/6 (83,33%) | **3/6 (50%)** | ≥90% | Không đạt |
| Báo nhầm câu khớp | 1/10 (10%) | **0/10 (0%)** | ≤10% | Đạt |
| Dẫn đúng nguồn theo danh sách của từng ca | 12/16 (75%) | **10/16 (62,5%)** | ≥90% | Không đạt |
| Ca từ chối qua | 2/2 (100%) | **2/2 (100%)** | 100% | Đạt |
| Mã hiển thị ngoài tập nguồn của lượt | 0 | **0** | 0 | Đạt |

| Nhóm | Số ca | ID |
|---|---:|---|
| Lượt 1 trượt → lượt 2 đạt | 5 | V28-03, V28-16, V28-17, V28-21, V28-27 |
| Lượt 1 đạt → lượt 2 trượt | 4 | V28-02, V28-08, V28-12, V28-22 |
| Cả hai lượt đều trượt | 5 | V28-09, V28-19, V28-24, V28-26, V28-28 |
| Cả hai lượt đều đạt | 16 | Xem bảng đối chiếu từng ca |


Dẫn đúng nguồn không chỉ là mã tồn tại trong tập nguồn chung: tất cả mã trả về phải nằm trong danh sách chấp nhận của chính ca đó. Vì vậy ca đúng nhãn nhưng dẫn dư mã vẫn trượt, không nới tiêu chí sau khi xem output. Các ca thiếu căn cứ đáp ứng tiêu chí được tính đạt; lượt 2 nhóm này đạt 9/12, so với 6/12 lượt 1.

Tệp bàn giao: [run-2.csv](run-2.csv) · [trace](../traces/run-2.jsonl) · [score](run-2-score.txt) · [metrics và hashes](run-2-metrics.json) · [đối chiếu 30 ca](run-1-to-2-comparison.csv). [Bàn giao cho Quốc Khánh](../docs/cp4-eval-handoff.md) · [Số liệu slide đánh giá](../slides/eval-results.md).

Token thật từ usage API: **21.506 vào / 3.726 ra**, tổng 25.232, 28 lần gọi. Tỷ lệ đạt benchmark **21/30**, trong đó 19 ca đạt có gọi model và 2 ca đạt do chặn trước model. Chỉ là dữ liệu tính chi phí của lượt benchmark, không thay thế mô phỏng persona/tháng. Chưa tính tiền khi chưa gắn đơn giá phù hợp.
