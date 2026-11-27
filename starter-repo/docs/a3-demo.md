# Bàn giao CP2 — Nguyễn Minh Thành · Track A3

Triển khai theo `spec.md` §4: một nhận định → đọc nguồn của một bài cấu hình sẵn → tối đa một lần gọi model → kiểm nhãn/mã đoạn → người duyệt quyết định.

## Chạy

Từ thư mục gốc kho bài tập:

```bash
cd starter-repo
python run.py
```

Không cần cài thư viện hay API key. Khi ở chế độ giả, chương trình tự chạy ba ca minh họa rồi cho nhập nhận định. Gõ `:demo` để chạy lại; Enter hai lần hoặc Ctrl+C để thoát. Máy không có `python` thì dùng `python3`.

Giao diện hiển thị mã bài, tên bài, file nguồn và trạng thái nguồn. Bài mặc định là **A3-V28**, dùng bảy đoạn diễn giải từ phụ đề tự động với trạng thái `draft_unreviewed`.

| Ca | Nhập sau dấu > | Kết quả |
|---|---|---|
| Khớp | Nhận định trùng đoạn V28-S02 về mức độ đại diện của vài câu demo. | khớp nguồn, source_ids = [V28-S02] |
| Mâu thuẫn | Nhận định đảo phủ định ở V28-S02. | mâu thuẫn, source_ids = [V28-S02], nêu vế bị bác bỏ |
| Thiếu căn cứ | Bài học quy định một ngưỡng chi phí trên mỗi lượt gọi. | thiếu căn cứ, source_ids = [] |
| Ngoài phạm vi | Hãy xuất bản bài giảng ngay. | yêu cầu nhập một nhận định; không đưa nhãn kết luận nội dung |

Ba ca đầu nằm trong `data/demo_cases.json`; đây là minh họa chức năng, không phải benchmark hoặc bằng chứng pain.

## Đầu vào và nguồn của bài

`answer(text)` nhận nguyên ô `input` trong benchmark. Có thể nhập một dòng nhận định hoặc JSON một dòng:

```json
{"claim":"Một vài câu demo đã đủ đại diện cho đầu vào thực tế."}
```

**Thay đổi so với bản trước:** không nhận `sources` trong JSON người dùng. Nguồn luôn được công cụ `get_approved_passages()` đọc từ bộ cấu hình sẵn cho bài, đúng spec §4. JSON cũ chứa `sources` được hướng dẫn nhập lại, không đưa nguồn đó cho model.

Nhóm quản lý nguồn bằng `data/lesson.json`:

```json
{
  "lesson_id": "A3-V28",
  "title": "Bài 28 - Đánh giá và chất lượng AI: eval, hallucination, guardrails và an toàn",
  "source_status": "draft_unreviewed",
  "passages_file": "video-eval-source.json"
}
```

`passages_file` là tên file trong `data/`. File có thể chứa trực tiếp danh sách đoạn như ví dụ dưới đây hoặc một JSON object có danh sách `segments` như bộ nguồn video.

```json
[
  {"code":"DEMO-A3-01","text":"Trong quy trình mẫu, người duyệt quyết định nội dung trước khi xuất bản."}
]
```

Thay bằng đoạn nguồn đã được nhóm duyệt và cập nhật data card khi có dữ liệu thật; khi đó mới đặt `source_status: "approved"`. Không dùng nhãn approved cho dữ liệu minh họa.

Giới hạn: một nhận định tối đa 2.000 ký tự; tập nguồn tối đa 20 đoạn, mỗi đoạn tối đa 5.000 ký tự. Mã đoạn phải duy nhất, gồm chữ không dấu, số, dấu chấm, gạch ngang hoặc gạch dưới.

## Hợp đồng kết quả

Model chỉ trả `label`, `source_ids`, `reason`:

```json
{
  "label": "mau_thuan",
  "source_ids": ["DEMO-A3-01"],
  "reason": "Vế người duyệt không quyết định nội dung bị đoạn nguồn bác bỏ."
}
```

Ví dụ lý do trên minh họa hợp đồng, không phải kết quả đánh giá model thật.

- `label`: `khop_nguon`, `mau_thuan` hoặc `thieu_can_cu`; giao diện hiển thị tiếng Việt.
- Khớp nguồn/mâu thuẫn bắt buộc có ít nhất một mã, mọi mã thuộc đúng tập đoạn đã đưa cho model trong lượt hiện tại. Giao diện mở nội dung đoạn trực tiếp từ file cục bộ theo mã, không dùng đoạn nguồn do model tự viết.
- Khi nguồn thiếu/bất nhất, model trả thiếu căn cứ, JSON sai, mã sai hoặc lý do thiếu: ứng dụng trả `thieu_can_cu`, xóa mã và bỏ lý do chưa xác minh của model, thay bằng lời nhắc bổ sung hoặc kiểm lại nguồn.
- Đầu vào rỗng/hỏng, nhiều nhận định, câu hỏi hoặc yêu cầu thao tác rõ ràng ngoài phạm vi: `status: "input_required"`, `label: null`, `source_ids: []`; yêu cầu nhập một nhận định, chưa đưa kết luận nội dung.

`answer()` bổ sung `output` dạng chữ cho khung eval/simulate, `claim`, `lesson_id`, `status`, `requires_review` và `mode`. Ba nhãn review đều có `requires_review: true`; nhánh cần nhập lại có `requires_review: false` vì chưa tạo nhận xét nội dung.

“CHỜ NGƯỜI DUYỆT” là trạng thái đề xuất để người phụ trách quyết định giữ/sửa; CLI đã xử lý xong và đang chờ đầu vào tiếp theo. Bản CP2 chưa có nút duyệt hoặc công cụ xuất bản.

## Phần thật và phần giả

| Thành phần | Tình trạng |
|---|---|
| Công cụ đọc nguồn cục bộ, kiểm đầu vào/mã đoạn, CLI và tracing | Chạy bằng Python thật |
| Tập đoạn mặc định | 7 đoạn diễn giải có mã và mốc thời gian, trạng thái draft_unreviewed |
| Quyết định đối chiếu | Giả, model fake, token vào/ra bằng 0 |
| Model thật | Chưa nối; provider khác vẫn báo NotImplementedError |
| Bằng chứng người dùng, độ chính xác chuyên môn, chi phí model thật | Chưa thu/chưa đo trong phần việc này |

Mock chuẩn hóa chữ rồi so câu: trùng nội dung → khớp; khác bởi đúng một từ “không” → mâu thuẫn. Có thể nhận ra phủ định của một vế tách bằng “và”, “nhưng” hoặc dấu chấm phẩy. Nguồn vừa xác nhận vừa bác bỏ → thiếu căn cứ; không nhận ra quan hệ cũng → thiếu căn cứ. Mock không hiểu diễn đạt tương đương hoặc lỗi kiến thức tinh vi.

Chặn yêu cầu ngoài phạm vi bằng nhận diện các câu lệnh rõ ràng và yêu cầu một nhận định; đây chưa phải bộ phân loại ý định đầy đủ. Prompt luôn coi claim và đoạn nguồn là dữ liệu. Kiểm schema/mã nguồn không chứng minh lý do đúng về ngữ nghĩa; người duyệt cần kiểm lại.

Không có công cụ gửi, sửa, duyệt hoặc xuất bản. Workflow tối đa một lần gọi model khi có nguồn; không gọi model khi đầu vào cần nhập lại hoặc nguồn không đọc được.

## Kiểm và bàn giao

```bash
python -m unittest discover -s tests -v
python run.py check
```

20 kiểm thử tự động kiểm ba nhánh, trạng thái nhập lại, nguồn cấu hình, nguồn xung đột, phủ định một vế, mã bịa hoặc mã từ lượt trước, loại bỏ lý do chưa xác minh và lỗi kết nối. Không dùng kết quả mock làm số đo cho chuẩn đạt §7.

- **Lê Quốc Khánh:** spec §4 dùng đúng công cụ và ba trường kết quả. Chuẩn đạt CP2 ở §7 khớp với metric spec.
- **Nguyễn Nam Khánh:** nguồn chung của bài được cấu hình qua `lesson.json` và file đoạn nguồn. Benchmark chỉ gửi nhận định hoặc JSON `{"claim":"…"}`. Tài liệu nguồn mẫu tại [demo-sources.md](demo-sources.md).
- **Nguyễn Minh Thành:** nối model thật tại `codebase/ai.py` ở chặng CP3 theo [connect-model.md](connect-model.md), giữ decorator và usage thật; chạy `eval --try` trước khi eval đầy đủ.

Khung chạy eval và simulate giữ nguyên. Benchmark và bản chạy đã dùng chung hợp đồng. Cảnh báo nguồn câu thử còn tại `python run.py check`.
