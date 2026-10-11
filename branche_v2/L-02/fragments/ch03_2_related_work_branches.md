## 2 Related Work

### 2.1 Tabular Machine Learning on LLMs

* **Khám phá ứng dụng của mô hình ngôn ngữ lớn (LLMs) trong học máy dạng bảng (tabular machine learning):**
  * Sự ra đời của các mô hình ngôn ngữ lớn (large language models - LLMs) sở hữu tri thức tiên nghiệm đặc thù miền (domain-specific prior knowledge) phong phú đã thúc đẩy việc khám phá tiềm năng ứng dụng của chúng trong việc giải quyết các bài toán học máy dạng bảng (tabular machine learning tasks) (Jia et al., 2026).

* **Các phương pháp tiếp cận tiêu biểu sử dụng LLM trực tiếp làm bộ dự đoán (LLMs as predictors):**
  * Phương pháp LIFT (Dinh et al., 2022):
    * Thực hiện tinh chỉnh (fine-tunes) mô hình GPT-$3$ (Floridi and Chiriatti, 2020) trên dữ liệu huấn luyện.
    * Minh chứng rằng các LLM đa mục đích (general-purpose LLMs) có thể cải thiện hiệu năng, mặc dù chưa vượt qua được các mô hình dựa trên cây (tree-based models).
  * Phương pháp TabLLM (Hegselmann et al., 2023):
    * Sử dụng mô hình T$0$ (Sanh et al., 2021) để thực hiện fine-tuning.
    * Khai thác hiệu quả tri thức đã được huấn luyện trước (pre-trained knowledge) chỉ với lượng dữ liệu gán nhãn tối thiểu (minimal labelled data).
  * Phương pháp UniPredict (Wang et al., 2023):
    * Huấn luyện GPT-$2$ (Ethayarajh, 2019) trên $169$ tập dữ liệu dạng bảng (tabular datasets).
    * Đạt được các kết quả cạnh tranh mà không cần tinh chỉnh riêng biệt theo từng tập dữ liệu cụ thể (dataset-specific tuning).

* **Hạn chế thực tế của việc sử dụng trực tiếp LLM làm bộ dự đoán:**
  * Giới hạn về phạm vi hiệu năng:
    * Các phương pháp tiếp cận dựa trên LLM này chỉ chứng minh được hiệu năng vượt trội chủ yếu trong các thiết lập thực nghiệm không mẫu (zero-shot) hoặc ít mẫu (few-shot) (Hegselmann et al., 2023).
  * Tụt hậu so với các mô hình truyền thống trong các kịch bản thực tế (real-world scenarios):
    * Các phương pháp này vẫn tụt hậu so với các mô hình dựa trên cây (tree-based models) và các mô hình học sâu (deep learning models) xét về cả hiệu quả tính toán (computational efficiency) lẫn độ chính xác dự đoán (prediction accuracy) (Cheng et al., 2025b).

* **Chuyển dịch hướng tiếp cận sang kỹ thuật đặc trưng bằng LLM (LLMs as feature engineering):**
  * Việc trực tiếp sử dụng LLM làm bộ dự đoán là phương án dưới mức tối ưu (suboptimal).
  * Thực tế này thúc đẩy các nhà nghiên cứu chuyển hướng sang việc khai thác LLM như các phương pháp kỹ thuật đặc trưng (feature engineering methods) nhằm nâng cao khả năng biểu diễn dữ liệu (enhance data representation).
  * Mục tiêu là cải thiện hiệu năng của các bộ dự đoán hạ nguồn (downstream predictors) như các mô hình dựa trên cây hoặc mô hình học sâu (Hollmann et al., 2023b).

### 2.2 Traditional and LLM-based AutoFE

* **Đặc điểm và quá trình tiến hóa của kỹ thuật đặc trưng tự động truyền thống (Traditional AutoFE):**
  * Nguyên lý hoạt động nền tảng:
    * AutoFE truyền thống chủ yếu dựa vào các thuật toán tìm kiếm heuristic (heuristic search) hoặc học tăng cường (reinforcement learning).
  * Lịch trình tiến hóa của các khung làm việc:
    * Phát triển từ các khung làm việc tìm kiếm vét cạn (exhaustive frameworks) (Katz et al., 2016) và tìm kiếm theo chiều sâu (Deep First Search - DFS) (Kanter and Veeramachaneni, 2015).
    * Tiến tới các phương pháp tiếp cận hiệu quả, định hướng theo độ hữu dụng (utility-driven approaches) (Zhang et al., 2023b) và các mô hình được dẫn dắt bởi quan hệ nhân quả (causally-guided models) (Malarkkan et al., 2026).
  * Hạn chế cố hữu của AutoFE truyền thống:
    * Thường gặp bế tắc trước hiện tượng bùng nổ tổ hợp (combinatorial explosion) trong các không gian tìm kiếm phức tạp.
    * Thiếu sự đồng căn ngữ nghĩa (lack semantic alignment) với logic nghiệp vụ đặc thù theo miền dữ liệu (domain-specific business logic).

* **Tiến bộ của AutoFE dựa trên LLM (LLM-based AutoFE) và hai hướng tiếp cận cốt lõi:**
  * Những bước tiến gần đây của LLM đã tạo động lực phát triển cho LLM-based AutoFE, phân tách thành hai hướng đi then chốt:
    * Sinh đặc trưng (feature generation).
    * Chọn lọc đặc trưng (feature selection).

* **Các phương pháp sinh đặc trưng dựa trên LLM (LLM-based feature generation):**
  * Khung làm việc nhận biết ngữ cảnh (context-aware frameworks) (Hollmann et al., 2023b).
  * Sử dụng cây quyết định để khám phá quy tắc (decision trees for rule discovery) (Nam et al., 2024).
  * Ánh xạ đặc trưng khả vi (differentiable feature mapping) (Han et al., 2024).
  * Sinh có cấu trúc thông qua ký pháp Ba Lan ngược (reverse Polish notation - RPN) (Zou et al., 2026).
  * Các mô hình lai ghép giữa tính toán tiến hóa và chưng cất tri thức (evolutionary-knowledge distillation hybrids) (Abhyankar et al., 2025).

* **Các kỹ thuật chọn lọc đặc trưng dựa trên LLM (LLM-based feature selection):**
  * Áp dụng ngưỡng xác suất log (log-probability thresholds) (Choi et al., 2022).
  * Sử dụng các mô hình xếp hạng (ranking paradigms) (Jeong et al., 2024).

* **Những thách thức tồn tại trong các phương pháp AutoFE dựa trên LLM:**
  * Nguy cơ tạo ra các đặc trưng không hữu dụng (uselessness of generated features).
  * Xuất hiện ảo giác (hallucinations) từ mô hình ngôn ngữ lớn.
  * Tồn tại các thiên kiến (biases) cố hữu trong quá trình tạo và đánh giá đặc trưng.

### 2.3 Automated Feature Engineering on Symbolic Regression

* **Khái niệm và vai trò của Hồi quy Ký hiệu (Symbolic Regression - SR):**
  * Định nghĩa:
    * Hồi quy ký hiệu (Symbolic Regression - SR) (Yang et al., 2025) là phương pháp học máy (machine learning method) tìm kiếm và khám phá các biểu thức toán học tối ưu (optimal mathematical expressions) nhằm phát hiện các mối quan hệ tiềm ẩn trong dữ liệu (latent data relationships).
  * Giá trị đối với kỹ thuật đặc trưng:
    * Khả năng suy dẫn các dạng biểu diễn giải tích có thể diễn giải (interpretable analytical forms) giúp SR trở nên đặc biệt có giá trị trong kỹ thuật đặc trưng (feature engineering) (Shmuel et al., 2024).
    * Nâng cao đồng thời tính minh bạch của mô hình (model transparency) và độ chính xác dự đoán (predictive accuracy), đồng thời giảm thiểu công sức thủ công (manual effort).

* **Các tiến bộ nghiên cứu gần đây trong kỹ thuật đặc trưng dựa trên Hồi quy Ký hiệu:**
  * Tích hợp tính toán tiến hóa (evolutionary computation integration) nhằm trích xuất các hiện tượng vật lý (physical phenomenon extraction) (Yu et al., 2026).
  * Lập trình di truyền đa cây dạng mô-đun (modular multi-tree genetic programming) phục vụ tái sử dụng đặc trưng trong không gian nhiều chiều (high-dimensional feature reuse) (San et al., 2021).
  * Chọn lọc đặc trưng dựa trên hệ số tương quan Spearman (Spearman-based feature selection) để tăng cường khả năng tổng quát hóa (generalization) (Kim et al., 2020).

* **Hạn chế nội tại của Hồi quy Ký hiệu và khoảng trống nghiên cứu hiện tại:**
  * Thách thức về độ phức tạp:
    * Hồi quy ký hiệu vẫn gặp nhiều khó khăn với sự phức tạp của biểu thức toán học (expression complexity) khi xử lý trong các không gian nhiều chiều (high-dimensional spaces).
  * Khoảng trống kết hợp giữa LLM và SR:
    * Dù các công trình hiện nay đã khám phá sự tương tác giữa LLM và SR (LLM-SR interactions) cho việc sinh phương trình (equation generation) — chẳng hạn như trong xử lý ngôn ngữ tự nhiên (natural language processing) (Shao et al., 2026) và tổng hợp mã nguồn (code synthesis) (Shojaee et al., 2025) — nhưng vẫn chưa mở rộng để kết hợp các phương trình do hồi quy ký hiệu tạo ra vào các LLM nhằm phục vụ kỹ thuật đặc trưng (feature engineering).
