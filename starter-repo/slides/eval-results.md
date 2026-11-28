# Số liệu cho slide 5 — Đánh giá AIhayAL

**20/30 → 21/30** trên cùng 30 câu và cùng model **gpt-5.4-nano-2026-03-17**. Tăng **3,33 điểm phần trăm**, **chưa đạt CP2**.

- Lượt 1: `run-1@20261127-224225`; lượt 2: `run-2@20261128-114555`.
- Thay đổi: prompt commit **32e490a**, PR #9; giữ nguyên benchmark và chuẩn chấm.
- Chấm bằng **Codex (AI)**; chưa chấm chéo lượt 2. Lượt 1 có đối chiếu người dùng 4/5, không tái sử dụng cho lượt 2.

| Chỉ số | Lượt 1 | Lượt 2 | Chuẩn CP2 | Lượt 2 |
|---|---|---|---|---|
| Qua toàn bộ tiêu chí | 20/30 (66,67%) | **21/30 (70%)** | ≥80% | Không đạt |
| Bắt đúng mâu thuẫn, tính toàn bộ tiêu chí | 5/6 (83,33%) | **3/6 (50%)** | ≥90% | Không đạt |
| Báo nhầm câu khớp | 1/10 (10%) | **0/10 (0%)** | ≤10% | Đạt |
| Dẫn đúng nguồn theo danh sách của từng ca | 12/16 (75%) | **10/16 (62,5%)** | ≥90% | Không đạt |
| Ca từ chối qua | 2/2 (100%) | **2/2 (100%)** | 100% | Đạt |
| Mã hiển thị ngoài tập nguồn của lượt | 0 | **0** | 0 | Đạt |

**5 ca sửa / 4 ca mới trượt / 5 ca còn trượt / 16 ca giữ đạt.** Ca mục tiêu V28-16 sửa được; V28-26 và V28-28 chưa sửa. Lỗi mới đáng chú ý: V28-08, V28-12 không còn phát hiện mâu thuẫn.

Lời trình bày đề xuất: “Sau khi siết căn cứ, tổng đạt tăng từ 20 lên 21/30. Tuy nhiên bắt mâu thuẫn giảm từ 5 xuống 3/6, nên chưa thể kết luận phiên bản mới tốt hơn về an toàn. Chúng em giữ nguyên đáp án và ngưỡng, công khai cả lỗi mới và lỗi còn lại.”

Nguồn số liệu: [CSV lượt 1](../eval/run-1.csv), [CSV lượt 2](../eval/run-2.csv), [bảng đối chiếu](../eval/run-1-to-2-comparison.csv), [metrics](../eval/run-2-metrics.json), [báo cáo](../eval/report.md). Nguồn kiến thức còn draft_unreviewed; một lượt trước/sau không chứng minh ý nghĩa thống kê.

Dữ liệu chi phí cho slide 6: [bàn giao Quốc Khánh](../docs/cp4-eval-handoff.md). Lượt 2: **28 lần gọi, 21.506 token vào / 3.726 token ra**, chưa gắn đơn giá.
