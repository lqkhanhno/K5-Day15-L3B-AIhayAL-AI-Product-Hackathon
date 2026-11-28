# CP4 — bàn giao phần Nguyễn Minh Thành

## Thay đổi đã chuẩn bị

Siết prompt trong `codebase/agent.py`: model phải rà từng vế, chỉ chọn `khop_nguon` khi nguồn xác nhận đủ nhận định, chỉ chọn `mau_thuan` khi nguồn trực tiếp bác bỏ một vế, và không suy rộng từ nguồn chung sang quan hệ nhân quả, so sánh hay yêu cầu cụ thể. Khi có vế không được nguồn nói rõ, hướng xử lý là `thieu_can_cu` với danh sách mã nguồn rỗng.

Thay đổi nhắm vào nhóm lỗi suy diễn ở V28-16, V28-26 và V28-28. Lượt 2 đo commit `32e490a` trên cùng 30 câu và cùng model. Kết quả tăng từ 20/30 lên 21/30, còn chỉ số bắt mâu thuẫn và dẫn nguồn giảm. [Báo cáo lượt 2](../eval/report.md)

## Hai ca demo CP4

Giao diện `python codebase/demo_window.py` đã chia kết quả thành nhãn màu, nhận định, lý do đầy đủ, từng đoạn nguồn và bước người duyệt cần làm. Cảnh báo nguồn bản nháp vẫn hiện rõ; model/token ở cuối cửa sổ. Nhánh cần nhập lại và lỗi kết nối có thông báo riêng. Đã kiểm các trạng thái bằng widget Tkinter ẩn, không gọi API; 30/30 unit test hiện có qua. Đây là kiểm hiển thị và code, chưa phải kết quả benchmark lượt 2.

Nguồn A3 hiện vẫn là `draft_unreviewed`; cần nói rõ đây là đối chiếu với các đoạn nguồn của bản nháp, không phải xác minh độc lập nội dung toàn video.

1. **Ca thường — khớp nguồn:** “Một vài câu demo được chuẩn bị kỹ không đại diện cho môi trường thực tế có lỗi gõ, tiếng lóng và đầu vào phá hoại.” Kỳ vọng: `khop_nguon`, `V28-S02`.
2. **Ca khó — thiếu căn cứ:** “LLM-as-judge luôn chính xác hơn người chấm chuyên môn.” Kỳ vọng: `thieu_can_cu`, không có mã nguồn. Các đoạn hiện cấu hình không thực hiện phép so sánh này.

Video dự phòng hiện có: [video demo 30 giây trên Drive](https://drive.google.com/file/d/1sh0NQ_hLLD2H2mUOyOTdfxqV1cJ0JKV1/view). Bàn giao CP3 ghi Quốc Khánh đã mở và phát được video trong tab Chrome ẩn danh ngày 28/11/2026. Dùng video này làm dự phòng; nếu quay bản CP4, kiểm tra lại link phát trước khi gửi.

## Kiểm tra và phần cần phối hợp

- Kiểm thử hợp đồng hiện có cùng một kiểm tra prompt mới: `python -m unittest discover -s tests -v`.
- Kiểm cấu trúc benchmark: `python run.py check`.
- Nam Khánh đã bàn giao lượt `run-2@20261128-114555`. Lượt này đo bản sửa prompt của Thành. Phần định dạng kết quả giao diện được kiểm riêng. [Bàn giao đánh giá](cp4-eval-handoff.md)
