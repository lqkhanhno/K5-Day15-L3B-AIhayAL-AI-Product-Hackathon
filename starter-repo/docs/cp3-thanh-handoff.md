# CP3 — bàn giao phần Nguyễn Minh Thành

Hạn nội bộ: **08:30 ngày 28/11/2026 (giờ Việt Nam)**. CP3 của nhóm: **10:00 cùng ngày**.

## Tình trạng thực tế

- Đã viết kết nối Gemini, OpenAI và Ollama tại `codebase/ai.py`, dùng thư viện chuẩn Python.
- Giữ `@model_call`, tên model API trả về và token thật. Gemini cộng token suy nghĩ riêng; OpenAI dùng completion_tokens đã bao gồm reasoning. Thiếu usage hoặc lỗi API thì báo lỗi, không chuyển sang mock.
- Đã cấu hình OpenAI và xác nhận gọi thật bằng `gpt-5.4-nano-2026-03-17`: `python run.py eval --try` chạy xong V28-01, V28-02, V28-03, không lỗi kỹ thuật; token vào/ra lần lượt 594/90, 599/110, 597/132. Đây là thử kết nối, chưa chấm đúng/sai theo §7.
- Kiểm tra cục bộ: 29/29 unit test qua (gồm 9 test kết nối giả lập HTTP); `python run.py check` không thấy vấn đề, đủ 30 câu (21 khó, 2 từ chối) và 3 metric. Đây chưa phải kết quả chất lượng AI thật.
- Đã quay [video thao tác thật trên Drive](https://drive.google.com/file/d/1sh0NQ_hLLD2H2mUOyOTdfxqV1cJ0JKV1/view), H.264, 1100×760, đúng 30 giây. Lượt demo trả `khop_nguon`, dẫn V28-S02, một lần gọi model, token vào 605 / ra 71; [bằng chứng và trace](cp3-live-20261127T144554571059Z.json). Lượt này không phải benchmark.
- Ngày 27/11/2026: đã kiểm [thư mục Drive do Thành cung cấp](https://drive.google.com/drive/folders/103IdP5_gMO_1R00NAaAuMCVybrXvmR5h) và tải đọc video **không đăng nhập, không cookie**: HTTP 200, `video/mp4`, 362.016 byte. `ffprobe` xác nhận 30,000 giây; `ffmpeg` giải mã toàn bộ không lỗi. Đây là kiểm truy cập và dữ liệu video; chưa kiểm nút phát trong trình duyệt ẩn danh. SHA-256: `0b40c093d62339c92d505d3cf70ae85bcbee3bc9b0d447655635c8995585cf56`.
- Nguồn bài A3-V28 vẫn có trạng thái `draft_unreviewed`; người phụ trách cần kiểm nguồn trước khi diễn giải kết quả.

## Cấu hình trên máy

Chạy PowerShell từ thư mục gốc repo:

```powershell
Set-Location starter-repo
Copy-Item .env.example .env
notepad .env
```

Chỉ chép khi chưa có `.env`. Điền các biến sau trong file, giữ key trên máy hoặc chuyển qua kênh riêng của nhóm:

```dotenv
MODEL_PROVIDER=openai
MODEL_NAME=gpt-5.4-nano
API_KEY=<key của nhóm>
MODEL_TIMEOUT=120
```

OpenAI đã chạy thật theo bằng chứng phía trên. Nếu đổi sang Gemini, dùng provider `gemini` và mã model tài khoản có quyền gọi. Ollama: provider `ollama`, tên model đã cài sẵn, `API_KEY` để trống, `OLLAMA_BASE_URL=http://localhost:11434`. Hai nhánh Gemini/Ollama mới được kiểm bằng phản hồi giả lập, chưa chạy dịch vụ thật. Không cần cài thêm gói Python.

Biến môi trường đã có sẽ ưu tiên hơn `.env`. Sau khi đổi cấu hình, khởi động lại lệnh Python.

## Thử nối trước khi bàn giao

```powershell
python run.py check
python run.py eval --try
python run.py
```

`eval --try` chỉ là thử kết nối, không tính là lượt 1. Xem `eval/run-try.csv` và `traces/run-try.jsonl`: model phải khác `fake`, token lớn hơn 0, cột lỗi trống; kiểm thêm đầu ra có nhãn, lý do và mã nguồn hợp lệ. Test giả lập HTTP không chứng minh model thật đã chạy.

Dùng đúng cấu hình đó để chạy toàn bộ:

```powershell
python run.py eval --wait 4
```

Khung tự cấp run ID và tên file. Không ghi đè lượt cũ; không mặc định kết quả sẽ là `run-1.csv` nếu đã có lượt trước. Chấm theo chuẩn CP2, sau đó dùng `python run.py score eval/run-N.csv`. Không thay benchmark/chuẩn đạt để khớp output.

## Video thao tác thật 30 giây

Link bàn giao: [cp3-thanh-demo.mp4](https://drive.google.com/file/d/1sh0NQ_hLLD2H2mUOyOTdfxqV1cJ0JKV1/view). Video nằm trong [thư mục hackathon](https://drive.google.com/drive/folders/103IdP5_gMO_1R00NAaAuMCVybrXvmR5h). Không cần commit MP4 vào repo. Thành nên mở link trong cửa sổ ẩn danh và bấm phát lần cuối trước khi gửi.

Video hiện có được quay từ cửa sổ `python codebase/demo_window.py`, dùng nguyên `agent.answer()` và tracing của CLI. Bấm nút đối chiếu để gọi API thật; giao diện không hiển thị key. Hướng dẫn bên dưới là cách quay lại bằng CLI nếu cần.

Chuẩn bị trước: mở terminal ở `starter-repo`, chạy `python run.py`, tăng cỡ chữ, đóng mọi màn hình có key. Chọn nhận định đầu trong `data/demo_cases.json`:

> Một vài câu demo được chuẩn bị kỹ không đại diện cho môi trường thực tế có lỗi gõ, tiếng lóng và đầu vào phá hoại.

1. 0–5 giây: hiển thị tên ứng dụng/bài và nhập nhận định, bấm Enter thật.
2. 5–23 giây: quay quá trình chờ và đầu ra thật. Đọc nhãn, mã nguồn, lý do, trạng thái chờ người duyệt và dòng model/token. Nếu API chậm, thử model nhanh hơn rồi quay lại toàn bộ lượt thật; không dựng kết quả giả.
3. 23–30 giây: giữ màn hình kết quả đủ rõ. Lời thoại gợi ý: “Em là Nguyễn Minh Thành. Đây là bản rà một nhận định của AIhayAL, gọi model thật, dẫn đoạn nguồn và chuyển người duyệt quyết định cuối cùng.”

Quay bằng công cụ ghi màn hình sẵn có. Lưu MP4, tải lên Drive với quyền “Bất kỳ ai có đường liên kết — Người xem” hoặc YouTube “Không công khai”. Mở link trong cửa sổ ẩn danh, khi không đăng nhập, và kiểm video phát được. Chưa kiểm thì ghi chưa kiểm.

## Nội dung 

> Đã nối và thử OpenAI thật: model `gpt-5.4-nano-2026-03-17`, 3 câu thử kết nối chạy xong không lỗi và có token thật. 29 unit test qua, kiểm cấu trúc benchmark đạt. [Video 30 giây](https://drive.google.com/file/d/1sh0NQ_hLLD2H2mUOyOTdfxqV1cJ0JKV1/view) đã truy cập/tải không đăng nhập và giải mã được toàn bộ; chưa kiểm phát trong trình duyệt ẩn danh. Bằng chứng demo tại `docs/cp3-live-20261127T144554571059Z.json`. Cấu hình provider/model ở tài liệu này; key chuyển qua kênh riêng. Cần chạy đủ 30 câu và chấm theo chuẩn CP2; chưa có kết quả x/30 hoặc xác nhận đạt §7.

## Tài liệu API đã đối chiếu

- [Gemini generateContent và usageMetadata](https://ai.google.dev/api/generate-content)
- [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat/create)
- [Model OpenAI cấu hình dự kiến: GPT-5.4 nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)
- [Ollama chat và token counts](https://docs.ollama.com/api/chat)
