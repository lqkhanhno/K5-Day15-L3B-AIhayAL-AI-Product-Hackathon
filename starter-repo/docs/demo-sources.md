# Nguồn synthetic cho bản demo A3

| Mục | Thông tin |
|---|---|
| File | `data/demo_sources.json` |
| Mục đích | Nguồn synthetic của bản Minh Thành thực hiện ban đầu, giữ làm fixture kiểm thử. Cấu hình tích hợp đọc `data/video-eval-source.json`. |
| Xuất xứ | Codex tự soạn 3 câu quy trình minh họa từ lát cắt trong canvas; không trích tài liệu khóa học |
| Ngày tạo | 27/11/2026 |
| Nhãn | `synthetic`; không phải tài liệu đã duyệt, dữ liệu thật hay bằng chứng pain |
| Mã đoạn | DEMO-A3-01, DEMO-A3-02, DEMO-A3-03 |
| Xử lý | UTF-8, mã duy nhất, kiểm kiểu dữ liệu và giới hạn độ dài khi đọc |
| Sinh dữ liệu | Soạn trực tiếp bởi Codex, không lấy mẫu ngẫu nhiên nên không có seed |
| Dữ liệu cá nhân | Không có |
| Người phụ trách nhận bàn giao | Nguyễn Minh Thành |
| Người kiểm nội dung | Chưa có xác nhận kiểm tay của thành viên nhóm |
| Giới hạn | Chỉ ba câu quy trình; không đủ để đo đúng/sai kiến thức chuyên môn, lỗi tinh vi hoặc nguồn lỗi thời |

`data/demo_cases.json` chứa 3 nhận định tự dựng để trình diễn giao diện, không phải tập đánh giá chính thức. Bộ kiểm thử trong `tests/` kiểm đường đi và hợp đồng mã, không chứng minh nguồn đúng về chuyên môn.

Khi có nguồn đã duyệt: Nguyễn Nam Khánh bổ sung nguồn gốc, phạm vi, xử lý và tình trạng kiểm tay vào `data/DATA_CARD.md`, rồi cung cấp file đoạn `{code, text}` và cập nhật `data/lesson.json` theo [hợp đồng demo](a3-demo.md). Không đưa nguồn vào đầu vào người dùng; mỗi lượt chỉ rà nhận định với tập đoạn cấu hình sẵn của bài.
