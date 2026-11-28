# Bàn giao eval CP4 cho Lê Quốc Khánh

Ngày ghi: 2026-11-28T11:52+07:00. Gửi số đo thật để ghép báo cáo chi phí và slide đánh giá; chưa gắn đơn giá tiền.

## Kết quả cần dùng

| Mục | Lượt 1 | Lượt 2 |
|---|---|---|
| Run ID | `run-1@20261127-224225` | **`run-2@20261128-114555`** |
| Model API trả về | gpt-5.4-nano-2026-03-17 | **gpt-5.4-nano-2026-03-17** |
| Commit code | 2097f24 | **32e490a** (PR #9) |
| Đạt / tổng | 20/30 | **21/30 (70%)** |
| Lỗi kỹ thuật | 0 | **0** |
| Lần gọi model | 28 | **28** |
| Token vào từ API | 16.578 | **21.506** |
| Token ra từ API | 3.116 | **3.726** |
| Tổng token | 19.694 | **25.232** |
| Ca đạt có gọi model | 18 | **19** |
| Ca đạt không gọi model | 2 | **2** |

Tỷ lệ đạt theo **Codex (AI) chấm**, chưa có người chấm độc lập lượt 2. Mức 70% chỉ là benchmark, không phải tỷ lệ thành công đã đo ở người dùng thực tế. Các ca thiếu căn cứ đúng tiêu chí vẫn tính đạt. Bất đồng V28-21 của lượt 1 không bị sửa; lượt 2 câu đó đã trả khớp S01 đúng tiêu chí.

## Dùng để tính chi phí

- Đơn giá chưa được gắn; dùng cùng model/snapshot và bảng giá có nguồn/ngày kiểm của người tính chi phí.
- Số token là usage thật, không ước lượng. Khung lưu token vào/ra tổng, không giữ phân rã cache hoặc reasoning riêng; không tự suy ra cached token.
- Nếu giả định cùng đơn giá đầu vào/đầu ra không cache: chi phí benchmark lượt 2 = 21.506/1.000.000 × giá vào + 3.726/1.000.000 × giá ra. Đây là công thức có điều kiện, không phải tiền thực trả đã xác nhận.
- Khi phân bổ toàn bộ chi phí lượt benchmark cho task đạt, mẫu số là **21**, gồm 19 ca gọi model và 2 ca bị chặn hợp lệ. Không chỉ tính chi phí các ca đạt rồi bỏ chi phí ca trượt.
- Không dùng 30 ca này thay thế mô phỏng ≥50 phiên/3 persona hoặc ước lượng chi phí tháng.

## Diễn giải đánh giá

| Chỉ số | Lượt 1 | Lượt 2 | Chuẩn CP2 | Lượt 2 |
|---|---|---|---|---|
| Qua toàn bộ tiêu chí | 20/30 (66,67%) | **21/30 (70%)** | ≥80% | Không đạt |
| Bắt đúng mâu thuẫn, tính toàn bộ tiêu chí | 5/6 (83,33%) | **3/6 (50%)** | ≥90% | Không đạt |
| Báo nhầm câu khớp | 1/10 (10%) | **0/10 (0%)** | ≤10% | Đạt |
| Dẫn đúng nguồn theo danh sách của từng ca | 12/16 (75%) | **10/16 (62,5%)** | ≥90% | Không đạt |
| Ca từ chối qua | 2/2 (100%) | **2/2 (100%)** | 100% | Đạt |
| Mã hiển thị ngoài tập nguồn của lượt | 0 | **0** | 0 | Đạt |

5 ca được sửa: V28-03, 16, 17, 21, 27. 4 ca mới trượt: V28-02, 08, 12, 22. Còn trượt từ lượt 1: V28-09, 19, 24, 26, 28. Chưa đạt CP2; không chỉ dùng điểm tổng tăng để kết luận tốt hơn.

## File bàn giao

- [Kết quả lượt 2](../eval/run-2.csv), [trace](../traces/run-2.jsonl), [kết quả score](../eval/run-2-score.txt).
- [Run ID/model/token/metrics và SHA-256](../eval/run-2-metrics.json).
- [Đối chiếu từng câu](../eval/run-1-to-2-comparison.csv), [hồ sơ eval](../eval/README.md), [phân tích lỗi](../eval/report.md).
- [Nội dung slide đánh giá](../slides/eval-results.md).

Giữ nguyên bộ 30 câu, đáp án, pass_criterion, nguồn và chuẩn CP2. Không có API key hoặc .env trong bàn giao.
