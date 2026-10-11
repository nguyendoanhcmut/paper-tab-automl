## Appendix H: Quantifying Hallucination Reduction and Improving Understandability

### H.1 Feature Traceability to Symbolic Regression Rules
* **Kiểm toán hệ thống (systematic audit) về nguồn gốc đặc trưng (feature provenance) trên tập dữ liệu Titanic**:
  * Đánh giá và phân loại toàn bộ các thao tác tạo đặc trưng do LLM sinh ra dựa trên liên kết nguồn gốc (provenance link) đối với tập biểu thức được hồi quy ký hiệu (symbolic regression - SR) tìm ra.
  * Toàn bộ quy trình kỹ thuật đặc trưng (feature engineering) của LLM tuân thủ chặt chẽ và chỉ rơi vào đúng 2 danh mục có căn cứ (grounded categories):
    * **Danh mục I (Category I) — Tiếp nhận trực tiếp kèm nâng cao khả năng diễn giải (Direct adoption with interpretability enhancement)**:
      * LLM trực tiếp tích hợp các biểu thức sinh bởi hồi quy ký hiệu có tính hợp lệ toán học vào pipeline xử lý.
      * Bổ sung các diễn giải chuyên biệt theo miền (domain-specific explanations), tên biến có tính mô tả (descriptive variable names) và chú thích nội dòng (inline documentation).
      * Chuyển hóa các công thức ký hiệu trừu tượng, khó hiểu thành mã nguồn minh bạch về ngữ nghĩa (semantically transparent code), tăng cường đáng kể khả năng đọc hiểu của con người mà không làm thay đổi tính đúng đắn toán học nền tảng.
      * Ánh xạ tường minh các đầu ra hồi quy ký hiệu trừu tượng thành các chỉ số được công nhận về mặt lâm sàng hoặc vật lý, đi kèm chú thích đơn vị rõ ràng và lập luận theo ngữ cảnh, đảm bảo mọi biến đổi đều có thể hiểu được ngay đối với chuyên gia trong ngành.
    * **Danh mục II (Category II) — Nhận diện và hợp nhất phần dư thừa (Redundancy identification and consolidation)**:
      * LLM chủ động so sánh các biểu thức do hồi quy ký hiệu khám phá với kho lưu trữ đặc trưng hiện có nhằm phát hiện sự trùng lặp về mặt ngữ nghĩa hoặc toán học.
      * Thực hiện các thao tác gộp (merge), thay thế (replacement), hoặc xóa bỏ (deletion) khi phát hiện dư thừa nhằm ngăn ngừa hiện tượng đa cộng tuyến (multicollinearity) và tinh gọn tập dữ liệu.
      * Trường hợp điển hình với đặc trưng kế thừa (legacy feature) `bmi`: LLM nhận diện đặc trưng này tương đương toán học với biểu thức do hồi quy ký hiệu suy ra là $\text{weight}/\text{height}^2$.
      * Thay vì nhân đôi tín hiệu dự đoán, LLM tiến hành hợp nhất bằng cách giữ lại dạng thức hồi quy ký hiệu ổn định về mặt số học và loại bỏ cột dữ liệu kế thừa dư thừa, qua đó tối ưu hóa không gian đặc trưng.
  * **Kết quả kiểm toán định lượng**:
    * $100\%$ các quy tắc do LLM tạo ra đều có thể truy xuất nguồn gốc chặt chẽ (strictly traceable) về các đầu ra của hồi quy ký hiệu.
    * LLM hoạt động độc quyền thông qua việc tiếp nhận diễn giải trực tiếp hoặc tối ưu hóa dựa trên việc loại bỏ trùng lặp.
    * Không gian sinh (generative space) của LLM bị ràng buộc hoàn toàn bởi các biểu thức hồi quy ký hiệu đã được xác thực toán học, không có bất kỳ sai lệch nào dẫn đến các phép biến đổi không có căn cứ (ungrounded transformations).

### H.2 Elimination of Hallucination and Bias through Grounded Generation
* **Triệt tiêu các phương thức lỗi chính của LLM không ràng buộc**:
  * Thiết kế pipeline loại bỏ triệt để hiện tượng ảo giác (hallucination) và định kiến dữ liệu tiềm ẩn (latent dataset bias) vốn thường gặp trong quá trình tổng hợp đặc trưng tự do bằng LLM.
* **Cơ chế ràng buộc toán học (mathematical grounding mechanism)**:
  * LLM đóng vai trò thuần túy là bộ máy diễn giải ngữ nghĩa (semantic interpreter) và cơ chế hợp nhất (consolidation engine) cho các biểu thức do hồi quy ký hiệu tạo ra.
  * LLM không thể bịa đặt các phép biến đổi không có cơ sở toán học hoặc tự ý đưa vào các tương quan giả tạo (spurious correlations).
  * Mọi đặc trưng được sinh ra đều neo chặt vào một quy tắc ký hiệu được tối ưu hóa nghiêm ngặt, vốn đã được xác thực đối với biến mục tiêu thông qua tìm kiếm tiến hóa (evolutionary search).
* **Đảm bảo tính minh bạch và khả năng tái lập**:
  * Vai trò của LLM bị giới hạn trong việc dịch mã (translation), giải thích (explanation) và loại bỏ trùng lặp (deduplication).
  * Tập đặc trưng cuối cùng duy trì tính minh bạch về ngữ nghĩa, khả năng tái lập (reproducible), và miễn nhiễm với ảo giác ngẫu nhiên (stochastic hallucinations) điển hình của quá trình sinh mã hộp đen.
* **Định vị chân lý thực tế (ground-truth anchoring)**:
  * Đảm bảo các quyết định của mô hình có thể giải thích được và hoàn toàn không chứa các tạo tác sinh chưa được kiểm chứng (unverified generative artifacts).
  * Giảm thiểu căn bản cả ảo giác thuật toán (algorithmic hallucination) lẫn các thiên kiến kế thừa từ dữ liệu (inherited data biases).

### H.3 Feasibility on High-Dimensional Datasets
* **Khả năng mở rộng trên tập dữ liệu nhiều chiều (scalability to high-dimensional datasets)**:
  * Framework SymboLLM-FE loại bỏ việc tìm kiếm vét cạn bất khả thi (intractable exhaustive searches) bằng cách triển khai hai cơ chế chiến lược:
    1. **Tìm kiếm có cấu trúc định hướng theo tương quan (Correlation-Guided Structured Search)**:
       * Sắp xếp trước (pre-sort) các đặc trưng theo hệ số tương quan Spearman với biến mục tiêu, gom cụm các biến có khả năng dự đoán cao.
       * Sử dụng cửa sổ trượt mở rộng (expanding-sliding window) để tạo ra các tập con liền kề (contiguous subsets).
       * Giảm không gian tìm kiếm từ quy mô hàm mũ $\mathcal{O}(2^n)$ xuống quy mô đa thức $\mathcal{O}(n^2)$.
    2. **Dừng sớm tạo độ thưa (Sparsity-Inducing Early Stopping)**:
       * Tận dụng áp lực tinh gọn vốn có (inherent parsimony pressure) của các mô hình hồi quy ký hiệu.
       * Áp dụng các tiêu chí dừng sớm nghiêm ngặt để khống chế chi phí tính toán.
* **Hiệu quả hiệp đồng và giới hạn tính toán**:
  * Sự kết hợp giữa việc cắt tỉa không gian tìm kiếm (search space pruning) và tiến hóa giới hạn tính toán (computationally bounded evolution) giúp hồi quy ký hiệu khả thi trên các tập dữ liệu số chiều lớn.
* **Cơ chế hợp nhất chọn lọc do LLM dẫn dắt (LLM-driven selective merging mechanism)**:
  * Để giảm thiểu hiện tượng tích tụ đặc trưng (feature accumulation) phát sinh từ nhiều tập con, cơ chế hợp nhất chọn lọc đóng vai trò như một bộ lọc ngữ nghĩa (semantic filter).
  * Tích hợp hoặc loại bỏ các đặc trưng ứng viên dựa trên hiệu năng thực nghiệm và tính mạch lạc logic (logical coherence).
  * Đảm bảo tập đặc trưng cuối cùng nhỏ gọn, không dư thừa và được tối ưu hóa tối đa cho các mô hình dự đoán ở hạ nguồn (downstream predictors).
