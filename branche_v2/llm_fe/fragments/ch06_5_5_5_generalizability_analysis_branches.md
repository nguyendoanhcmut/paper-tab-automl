### 5.5 Generalizability Analysis

- **Mục tiêu và thiết lập đánh giá khả năng tổng quát hóa (generalizability)**:
  - Tiến hành đánh giá có hệ thống (systematic assessment) về hiệu năng của LLM-FE trên nhiều mô hình dự đoán dữ liệu dạng bảng (tabular prediction models) và các mô hình ngôn ngữ lớn nền tảng (LLM backbones) đa dạng.
  - Khảo sát sự kết hợp chéo giữa 2 đại diện LLM và 3 kiến trúc mô hình dự đoán dữ liệu bảng phổ biến nhằm kiểm chứng tính độc lập và khả năng thích ứng rộng rãi của khung làm việc kỹ thuật đặc trưng.

- **Các mô hình dự đoán dữ liệu dạng bảng (tabular prediction models) được đánh giá**:
  - **XGBoost** (Chen & Guestrin, 2016): Mô hình cơ sở dựa trên cây (tree-based baseline) mạnh mẽ dành cho dữ liệu có cấu trúc (structured data).
  - **Multilayer Perceptron (MLP)** (Gorishniy et al., 2021): Cung cấp một kiến trúc học sâu (deep-learning architecture) đơn giản nhưng có tính cạnh tranh cao cho đầu vào dữ liệu bảng.
  - **TabPFN** (Hollmann et al., 2023): Mô hình nền tảng dựa trên transformer (transformer-based foundation model) mới được thiết kế chuyên biệt cho học dữ liệu bảng; do giới hạn dung lượng xử lý, TabPFN chỉ được đánh giá trên $10{,}000$ mẫu (ký hiệu $\text{TabPFN}^*$).

- **Các mô hình ngôn ngữ lớn nền tảng (LLM backbones)**:
  - **Llama-3.1-8B-Instruct**: Đại diện cho dòng mô hình ngôn ngữ lớn mã nguồn mở (open-source LLM).
  - **GPT-3.5-Turbo**: Đại diện cho dòng mô hình ngôn ngữ lớn thương mại qua API.

- **Kết quả thực nghiệm định lượng trên các tác vụ phân loại và hồi quy (Bảng 5)**:
  - Hiệu năng cải thiện được đo lường thông qua giá trị tổng hợp của độ chính xác (accuracy) $\uparrow$ trên các tác vụ phân loại (classification tasks) và sai số căn bậc hai trung bình chuẩn hóa (normalized root mean square error - NRMSE) $\downarrow$ trên các tác vụ hồi quy (regression tasks).
  - Toàn bộ kết quả thể hiện giá trị trung bình và độ lệch chuẩn ($\text{mean} \pm \text{std}$) tính trên 5 lượt phân chia (five splits); số in đậm thể hiện hiệu năng tốt nhất.

| Phương pháp (Method) | LLM Backbone | Phân loại (Classification) $\uparrow$ | Hồi quy (Regression) $\downarrow$ |
| :--- | :--- | :---: | :---: |
| **XGBoost** | | | |
| Base (không dùng FE) | – | $0.820 \pm 0.020$ | $0.324 \pm 0.016$ |
| LLM-FE | Llama 3.1-8B | $0.832 \pm 0.021$ | $0.310 \pm 0.022$ |
| LLM-FE | GPT-3.5 Turbo | $\mathbf{0.840 \pm 0.022}$ | $\mathbf{0.306 \pm 0.015}$ |
| **MLP** | | | |
| Base (không dùng FE) | – | $0.745 \pm 0.034$ | $0.871 \pm 0.027$ |
| LLM-FE | Llama 3.1-8B | $0.768 \pm 0.032$ | $0.794 \pm 0.016$ |
| LLM-FE | GPT-3.5 Turbo | $\mathbf{0.791 \pm 0.029}$ | $\mathbf{0.631 \pm 0.043}$ |
| **$\text{TabPFN}^*$** | | | |
| Base (không dùng FE) | – | $0.852 \pm 0.028$ | $0.289 \pm 0.016$ |
| LLM-FE | Llama 3.1-8B | $0.856 \pm 0.017$ | $0.288 \pm 0.016$ |
| LLM-FE | GPT-3.5 Turbo | $\mathbf{0.863 \pm 0.018}$ | $\mathbf{0.286 \pm 0.015}$ |

  > **Ghi chú**: $\text{TabPFN}^*$ biểu thị việc đánh giá chỉ sử dụng $10{,}000$ mẫu do năng lực xử lý hạn chế của kiến trúc này.

- **Quan sát và phân tích cốt lõi (Key Findings & Insights)**:
  - **Cải thiện nhất quán trên mọi mô hình dự đoán**: LLM-FE xác định thành công các đặc trưng chứa nhiều thông tin hữu ích và liên quan mật thiết tới bài toán (informative and task-relevant features), giúp nâng cao hiệu năng hạ nguồn (downstream performance) của cả 3 mô hình dự đoán dưới cả 2 LLM backbones.
  - **Vượt trội ổn định so với mô hình gốc không qua kỹ thuật đặc trưng**: Các tập đặc trưng do LLM-FE tạo ra luôn vượt trội đáng tin cậy so với các mô hình cơ sở đối chứng không dùng kỹ thuật đặc trưng (non-feature-engineering counterparts).
  - **Độ vững chắc xuyên suốt các họ mô hình và tác vụ**: Kết quả chứng minh phương pháp mang lại lợi ích vững chắc (robust benefits) trên nhiều họ mô hình (model classes), lựa chọn backbone và các tác vụ khác nhau, khẳng định tính phổ quát và khả năng ứng dụng rộng rãi của khung làm việc kỹ thuật đặc trưng đề xuất.
  - **Thực nghiệm mở rộng**: Phụ lục D.2 (Appendix D.2) cung cấp thêm các thực nghiệm với các LLM và mô hình dự đoán bổ sung khác, tiếp tục củng cố kết luận về tính tổng quát hóa của phương pháp.
