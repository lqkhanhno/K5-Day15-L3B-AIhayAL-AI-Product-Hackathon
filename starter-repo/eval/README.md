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
- Đã đối chiếu phiếu Codex (AI) và phiếu người dùng trên 5 ca cùng lượt 1: **khớp 4/5 (80%)**. Người dùng giữ điểm 1 cho V28-21, Codex giữ 0 theo tiêu chí. Đây không phải hai người chấm chuyên môn độc lập.

**Chuẩn đạt CP2**

> Đạt khi ≥80% tổng số câu qua toàn bộ tiêu chí chấm, ≥90% câu mâu thuẫn qua toàn bộ tiêu chí chấm, ≤10% báo nhầm trên nhóm câu khớp nguồn, ≥90% dẫn đúng nguồn trên nhóm câu khớp hoặc mâu thuẫn, 100% câu từ chối qua và 0 mã đoạn hiển thị nằm ngoài tập nguồn của lượt đó.

## Các lệnh

`python run.py check` kiểm bộ thử. Khi đã nối model và thống nhất bộ câu thử, chạy `python run.py eval --try` rồi `python run.py eval`. Hai người chấm điền `pass` và `ghi_chu`, sau đó chạy `python run.py score eval/run-1.csv`.

## Chuẩn bị lượt 1 CP3 · 22:41 ngày 27/11/2026 (UTC+7)

- Đã pull `main` tại `c9daa8b`; dùng nguyên 30 câu V28-01–V28-30 trên main. Không dùng bộ 20 câu cũ trong PR #4.
- Nhánh làm việc `docs/cp3-eval` đã lấy phần kết nối model của Thành, gồm commit `069cd17`, đến đầu nhánh `2097f24`. [Bàn giao Thành](../docs/cp3-thanh-handoff.md)
- Đã xác nhận benchmark, metric spec, nguồn video và cấu hình bài giống hệt main; nội dung spec §7 cũng giữ nguyên.
- `python3 run.py check`: không thấy vấn đề. `python3 -m unittest discover -s tests -v`: 29/29 kiểm thử qua; đây là kiểm thử phần mềm, chưa phải kết quả model thật.
- Đã tạo `.env` cục bộ, được gitignore loại trừ, cấu hình OpenAI / `gpt-5.4-nano` / timeout 120. Khi chuẩn bị, API_KEY chưa có; sau đó người dùng đã điền trực tiếp vào file và thử nối thành công. Máy không có lệnh `python`, dùng `python3` tương đương.
- Thử nối 3/3 ca thành công, API trả `gpt-5.4-nano-2026-03-17`, có token thật và không lỗi. Đã chạy đủ 30 ca bằng `python3 -u run.py eval --wait 4`; không thay bằng demo hoặc mock.

### Trình tự sau khi có key

1. Trong `starter-repo`, chạy `python3 run.py eval --try`; kiểm 3 ca đầu có lỗi trống, token thật và model API trả về. Dự kiến theo bàn giao là `gpt-5.4-nano-2026-03-17`, nhưng phải ghi tên thực tế của lượt mới.
2. Chạy `python3 run.py eval --wait 4` để xử lý đủ 30 ca. Giữ nguyên output, token, metadata và trace; chỉ điền `pass`, `ghi_chu` sau khi chấm.
3. Chấm từng ca theo pass_criterion và chuẩn CP2. Ca thiếu căn cứ vẫn đạt nếu đúng nhãn, mã rỗng và có bước kiểm lại/bổ sung nguồn; không tính nhãn thiếu căn cứ là lỗi mặc định.
4. Chạy `python3 run.py score eval/run-1.csv` nếu đó là tên khung cấp. Nếu đã có lượt trước, dùng đúng run-N.csv mới được cấp, không ghi đè lượt cũ.
5. Tính riêng ba metrics và các ràng buộc CP2; ghi run ID, model thật và kết quả x/30 vào bảng bàn giao bên dưới. Không thay chuẩn hoặc đáp án khi điểm thấp.

### Bàn giao trước 09:15 ngày 28/11/2026 (UTC+7)

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
| Đạt chuẩn CP2 | **Không đạt** theo phiếu Codex; chấm chéo 4/5 còn một bất đồng; giữ nguyên đáp án, tiêu chí và chuẩn CP2 dù điểm thấp |

### Chấm chéo độc lập 5 ca

Hai phiếu dùng cùng output của **run-1@20261127-224225**. Người dùng xem input, tiêu chí và output nhưng chưa xem điểm Codex khi gửi phiếu đầu. Chấm chéo gồm **Codex (AI) + người dùng**, không phải hai người chấm chuyên môn độc lập. [Phiếu trình bày ban đầu](crosscheck-run-1.md) · [Bản ghi điểm và lý do](crosscheck-run-1.json).

| ID | Codex (AI): pass + lý do | Người dùng: pass + lý do | Khớp? |
|---|---|---|---|
| V28-01 | **1** — Đúng nhãn khớp, chỉ mã S01 và lý do đúng | **1** — AI sẵn sàng đưa câu trả lời sai bét nhưng với 1 thái độ tự tin | Có |
| V28-08 | **1** — Đúng mâu thuẫn, chỉ mã S01 và giải thích đúng | **1** — Đo lường bằng cảm giác thì thảm họa chờ đón | Có |
| V28-15 | **1** — Đúng thiếu căn cứ, mã rỗng và có bước kiểm lại | **1** — Không nói rõ 100 câu | Có |
| V28-20 | **1** — Yêu cầu nhập lại, không gắn nhãn hay bịa mã | **1** — input chưa phải 1 nhận định rõ ràng | Có |
| V28-21 | **0** — Output thiếu căn cứ/mã rỗng, trái tiêu chí khớp nguồn S01 | **1** — chưa đưa ra nguồn | **Không** |

**Kết quả: 4/5 (80%) đồng ý.** V28-21 còn bất đồng: tiêu chí yêu cầu khớp nguồn S01, output trả thiếu căn cứ và không dẫn nguồn. Người dùng xác nhận giữ điểm độc lập 1; không ghi là đã thống nhất. File run-1.csv giữ pass=0 của phiếu Codex theo tiêu chí đã chốt, tổng 20/30. Giữ nguyên expected, pass_criterion và chuẩn CP2. Nếu nhóm yêu cầu hai người chấm, vẫn cần thêm phiếu người thứ hai; không dùng phiếu Codex để tuyên bố đã có hai người.

## Hồ sơ chấm lượt 1

- Chấm lượt đầu: **Codex (AI)** đọc 30 output, đối chiếu tiêu chí và các đoạn nguồn; dùng mã để kiểm cấu trúc, tính tỷ lệ và bảo toàn output. Không ghi đây là chấm bởi người chuyên môn hoặc hai người độc lập.
- Chỉ điền `pass`, `ghi_chu` trong file kết quả; output, input, expected, pass_criterion, metadata và trace được giữ nguyên. Bộ thử và metric spec giống hệt main; spec §7 giữ nguyên.
- [Số đo và SHA-256 phục vụ kiểm lại](run-1-metrics.json) · [Kết quả lệnh score](run-1-score.txt) · [Phân tích lỗi](report.md).
- Theo type: thường 6/7, khó 12/21, từ chối 2/2. Theo nhãn mong đợi: khớp nguồn 7/10, mâu thuẫn 5/6, thiếu căn cứ 6/12, yêu cầu nhập lại 2/2. Các ca thiếu căn cứ đúng tiêu chí đã được tính đạt.
- Các ca trượt: V28-03, V28-09, V28-16, V28-17, V28-19, V28-21, V28-24, V28-26, V28-27, V28-28.
- Không sửa code/prompt sau khi xem điểm trong công việc lượt 1 này. Bất kỳ cải tiến nào sau đó phải được ghi riêng và chạy thành lượt mới trên cùng benchmark.
