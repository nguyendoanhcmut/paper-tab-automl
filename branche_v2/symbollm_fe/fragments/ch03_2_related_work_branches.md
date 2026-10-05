## 2 Related Work

### 2.1 Tabular Machine Learning on LLMs

- Sự xuất hiện của các LLM (Large Language Model - mô hình ngôn ngữ lớn) sở hữu lượng lớn tri thức tiên nghiệm đặc thù miền (domain-specific prior knowledge) đã thúc đẩy việc khám phá tiềm năng ứng dụng của chúng trong các tác vụ học máy trên dữ liệu bảng (tabular machine learning) (Jia et al., 2026).
  - LIFT (Dinh et al., 2022) tinh chỉnh (fine-tune) GPT-3 (Floridi and Chiriatti, 2020) trên dữ liệu huấn luyện, chứng minh rằng các LLM đa năng có thể cải thiện hiệu năng dù chưa vượt qua được các mô hình dựa trên cây (tree-based models).
  - TabLLM (Hegselmann et al., 2023) sử dụng T0 (Sanh et al., 2021) để tinh chỉnh, tận dụng hiệu quả tri thức tiền huấn luyện với lượng dữ liệu có nhãn tối thiểu.
  - UniPredict (Wang et al., 2023) huấn luyện GPT-2 (Ethayarajh, 2019) trên 169 tập dữ liệu bảng, đạt kết quả cạnh tranh mà không cần tinh chỉnh đặc thù theo từng tập dữ liệu (dataset-specific tuning).
- Các phương pháp tiếp cận dựa trên LLM thể hiện hiệu năng vượt trội chủ yếu trong các thiết lập thực nghiệm zero-shot hoặc few-shot (Hegselmann et al., 2023).
  - Trong các kịch bản thực tế, các phương pháp này vẫn tụt hậu so với các mô hình cây và mô hình học sâu (deep learning) về cả hiệu quả tính toán lẫn độ chính xác dự đoán (Cheng et al., 2025b).
- Việc sử dụng trực tiếp LLM làm bộ dự đoán (predictor) là chưa tối ưu (suboptimal).
  - Nhận định này thúc đẩy các nhà nghiên cứu chuyển sang tận dụng LLM như một phương pháp kỹ thuật đặc trưng (feature engineering) nhằm nâng cao biểu diễn dữ liệu (data representation), qua đó cải thiện hiệu năng của các bộ dự đoán xuôi dòng (downstream predictors) như mô hình cây hoặc mô hình học sâu (Hollmann et al., 2023b).

### 2.2 Traditional and LLM-based AutoFE

- AutoFE truyền thống (Automated Feature Engineering - kỹ thuật đặc trưng tự động) chủ yếu dựa vào tìm kiếm heuristic (heuristic search) hoặc học tăng cường (reinforcement learning).
  - Các phương pháp phát triển từ khung vét cạn (exhaustive frameworks) (Katz et al., 2016) và DFS (Deep Feature Synthesis) (Kanter and Veeramachaneni, 2015) sang các cách tiếp cận định hướng theo độ hữu dụng hiệu quả (utility-driven approaches) (Zhang et al., 2023b) và các mô hình định hướng theo quan hệ nhân quả (causally-guided models) (Malarkkan et al., 2026).
  - Hạn chế: thường gặp khó khăn trước sự bùng nổ tổ hợp (combinatorial explosion) trong không gian tìm kiếm phức tạp và thiếu sự gióng hàng ngữ nghĩa (semantic alignment) với logic nghiệp vụ đặc thù miền.
- Các tiến bộ gần đây của LLM đã thúc đẩy sự phát triển của AutoFE dựa trên LLM, phân nhánh thành hai hướng chính: sinh đặc trưng (feature generation) và chọn lọc đặc trưng (feature selection).
  - Hướng sinh đặc trưng bao gồm các khung làm việc nhận biết ngữ cảnh (context-aware frameworks) (Hollmann et al., 2023b), cây quyết định để khám phá quy tắc (Nam et al., 2024), ánh xạ đặc trưng khả vi (differentiable feature mapping) (Han et al., 2024), sinh có cấu trúc qua ký pháp Ba Lan ngược (reverse Polish notation) (Zou et al., 2026), và các mô hình lai giữa tiến hóa và chưng cất tri thức (evolutionary-knowledge distillation hybrids) (Abhyankar et al., 2025).
  - Hướng chọn lọc đặc trưng áp dụng các ngưỡng xác suất log (log-probability thresholds) (Choi et al., 2022) và mô hình xếp hạng (ranking paradigms) (Jeong et al., 2024).
- Các thách thức của AutoFE dựa trên LLM gồm: đặc trưng sinh ra không hữu dụng (uselessness of generated features), hiện tượng ảo giác (hallucinations) và thiên kiến (biases).

### 2.3 Automated Feature Engineering on Symbolic Regression

- Hồi quy ký hiệu (Symbolic Regression - SR) là một phương pháp học máy khám phá các biểu thức toán học tối ưu để làm sáng tỏ các mối quan hệ tiềm ẩn trong dữ liệu (latent data relationships) (Yang et al., 2025).
  - Khả năng rút ra các dạng giải tích có thể diễn giải được (interpretable analytical forms) giúp hồi quy ký hiệu có giá trị lớn trong kỹ thuật đặc trưng (Shmuel et al., 2024), vừa nâng cao tính minh bạch của mô hình và độ chính xác dự đoán, vừa giảm bớt công sức thủ công.
- Các tiến bộ gần đây trong kỹ thuật đặc trưng bằng hồi quy ký hiệu:
  - Tích hợp tính toán tiến hóa (evolutionary computation) để trích xuất các hiện tượng vật lý (Yu et al., 2026).
  - Quy hoạch di truyền đa cây dạng mô-đun (modular multi-tree genetic programming) nhằm tái sử dụng đặc trưng trong không gian nhiều chiều (high-dimensional feature reuse) (San et al., 2021).
  - Chọn lọc đặc trưng dựa trên tương quan Spearman (Spearman-based feature selection) nhằm tăng cường khả năng khái quát hóa (generalization) (Kim et al., 2020).
- Hạn chế của hồi quy ký hiệu: vẫn gặp khó khăn trước độ phức tạp của biểu thức (expression complexity) trong không gian nhiều chiều.
- Khoảng trống nghiên cứu: mặc dù các nghiên cứu hiện có đã khám phá tương tác giữa LLM và hồi quy ký hiệu để sinh phương trình (như trong xử lý ngôn ngữ tự nhiên (Shao et al., 2026) và tổng hợp mã nguồn (Shojaee et al., 2025)), chưa có công trình nào mở rộng để đưa các phương trình do hồi quy ký hiệu sinh ra vào LLM phục vụ kỹ thuật đặc trưng.
