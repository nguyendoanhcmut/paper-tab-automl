### 2.4 LLM-RAG Feature Selection Framework

- Khung tích hợp tri thức y văn khoa học qua kỹ thuật RAG (Retrieval-Augmented Generation):
  - Xây dựng trên nền tảng thư viện PaperQA nhằm cho phép các mô hình ngôn ngữ lớn truy xuất và lập luận trên tập tài liệu nghiên cứu chuyên ngành.
  - Kết hợp đồng thời 3 mô hình ngôn ngữ lớn (LLMs) đa dạng về kiến trúc và phương pháp huấn luyện (Bảng 2):
    - GPT-5.2 (OpenAI).
    - Claude Sonnet 4.6 (Anthropic).
    - Gemini 2.5 Flash (Google).
  - Tận dụng thế mạnh lập luận bổ trợ giữa các kiến trúc mô hình khác nhau để hạn chế sai lệch phán đoán cá thể.
- Xây dựng kho ngữ liệu chuyên ngành và cơ chế tìm kiếm ngữ nghĩa:
  - Tập hợp kho ngữ liệu cục bộ gồm 520 bài báo khoa học chuyên sâu về phát thải $N_2O$ và xử lý nước thải sinh học từ các tạp chí uy tín.
  - Lập chỉ mục vector hóa (vector embeddings) sử dụng mô hình `text-embedding-3-small` của OpenAI để hỗ trợ tìm kiếm độ tương đồng ngữ nghĩa chính xác.
- Quy trình bảo mật dữ liệu và chuẩn bị ngữ cảnh:
  - Khử định danh dữ liệu (data anonymization): Loại bỏ hoàn toàn tên nhà máy, vị trí địa lý và các siêu dữ liệu vận hành nhạy cảm trước khi truy vấn nhằm bảo đảm tính bảo mật.
  - Tạo cấu trúc tóm tắt dữ liệu: trích xuất đặc tính thống kê, phân tích phân phối dữ liệu khuyết thiếu, và ma trận tương quan giữa các biến quá trình với nồng độ phát thải $N_2O$.
- Cơ chế truy xuất bằng chứng khoa học và quyết định chọn đặc trưng:
  - Truy xuất các phân đoạn văn bản cơ chế có độ liên quan cao nhất từ kho 520 bài báo khoa học.
  - Tổng hợp đồng thời ngữ cảnh dữ liệu vận hành và tri thức y văn để kết luận danh sách đặc trưng đầu vào phục vụ mô hình học sâu.
