## Appendix H Quantifying Hallucination Reduction and Improving Understandability

### H.1 Feature Traceability to Symbolic Regression Rules

- **Kiểm toán có hệ thống (systematic audit) trên tập dữ liệu Titanic (Titanic dataset)**:
  - Phân loại toàn bộ các thao tác đặc trưng do mô hình ngôn ngữ lớn (LLM - Large Language Model) sinh ra theo mối liên kết nguồn gốc (provenance link) với tập biểu thức do hồi quy ký hiệu (Symbolic Regression - SR) khám phá.
  - Quy trình kỹ thuật đặc trưng (feature engineering) của LLM rơi hoàn toàn vào hai nhóm có cơ sở xác thực (grounded categories):
    - **Category I — Áp dụng trực tiếp kết hợp tăng cường khả năng diễn giải (Direct adoption with interpretability enhancement)**:
      - LLM tích hợp trực tiếp các biểu thức hợp lệ về mặt toán học do hồi quy ký hiệu sinh ra vào đường ống (pipeline).
      - Bổ sung các giải thích chuyên biệt theo miền (domain-specific explanations), tên biến mang tính mô tả (descriptive variable names) và tài liệu chú thích nội dòng (inline documentation).
      - Chuyển đổi các công thức ký hiệu mờ đục (opaque symbolic formulas) thành mã nguồn minh bạch về mặt ngữ nghĩa (semantically transparent code), cải thiện đáng kể khả năng đọc hiểu của con người mà không làm thay đổi tính hợp lệ toán học cốt lõi.
      - Các đầu ra hồi quy ký hiệu trừu tượng được ánh xạ tường minh sang các số đo được công nhận về mặt lâm sàng hoặc vật lý, đi kèm chú thích đơn vị rõ ràng và lập luận theo ngữ cảnh, đảm bảo mọi biến đổi đều có thể hiểu được ngay đối với chuyên gia lĩnh vực.
    - **Category II — Nhận diện và hợp nhất phần dư thừa (Redundancy identification and consolidation)**:
      - LLM chủ động so sánh các biểu thức được hồi quy ký hiệu khám phá với kho lưu trữ đặc trưng hiện có nhằm phát hiện các phần chồng chéo về mặt toán học hoặc ngữ nghĩa.
      - Khi phát hiện dư thừa, LLM thực thi các thao tác hợp nhất (merge), thay thế (replacement) hoặc xóa bỏ (deletion) để ngăn chặn hiện tượng đa cộng tuyến đặc trưng (feature multicollinearity) và tinh giản tập dữ liệu.
      - Trường hợp điển hình liên quan đến đặc trưng kế thừa `bmi`: LLM nhận diện đặc trưng này tương đương toán học với biểu thức $\text{weight}/\text{height}^2$ do hồi quy ký hiệu suy dẫn; thay vì nhân đôi tín hiệu dự đoán, LLM hợp nhất chúng bằng cách giữ lại công thức hồi quy ký hiệu ổn định về mặt số học và loại bỏ cột kế thừa dư thừa, tối ưu hóa không gian đặc trưng.
- **Tỷ lệ truy xuất nguồn gốc tuyệt đối ($100\%$) của các quy tắc do LLM sinh ra**:
  - Đợt kiểm toán xác nhận $100\%$ các quy tắc do LLM tạo ra đều có thể truy xuất nguồn gốc nghiêm ngặt (strictly traceable) về các đầu ra của hồi quy ký hiệu.
  - Các quy tắc chỉ vận hành duy nhất thông qua việc tiếp nhận diễn giải trực tiếp hoặc tối ưu hóa dựa trên việc khử trùng lặp.
  - Không gian tạo sinh của LLM bị giới hạn hoàn toàn trong các biểu thức hồi quy ký hiệu đã được xác thực toán học, với độ lệch bằng không (zero deviation, 0) sang các phép biến đổi không có căn cứ (ungrounded transformations).

### H.2 Elimination of Hallucination and Bias through Grounded Generation

- **Triệt tiêu các chế độ lỗi chính trong tổng hợp đặc trưng LLM**:
  - Thiết kế đường ống loại bỏ hiệu quả hai chế độ lỗi chính của quá trình tổng hợp đặc trưng bằng LLM không bị ràng buộc: ảo giác (hallucination) và thiên kiến dữ liệu tiềm ẩn (latent dataset bias).
  - LLM vận hành nghiêm ngặt với vai trò bộ diễn giải ngữ nghĩa (semantic interpreter) và cơ chế hợp nhất (consolidation engine) cho các biểu thức thu được từ hồi quy ký hiệu, do đó không thể tự bịa đặt các phép biến đổi không có cơ sở toán học hay tiêm vào các tương quan giả tạo (spurious correlations).
- **Cơ chế neo vào chân lý nền tảng (ground-truth anchoring)**:
  - Mọi đặc trưng sinh ra đều được neo chặt vào một quy tắc ký hiệu được tối ưu hóa nghiêm ngặt, vốn đã được kiểm chứng đối với biến mục tiêu thông qua quá trình tìm kiếm tiến hóa (evolutionary search).
  - Vai trò của LLM bị giới hạn trong phạm vi dịch mã (translation), giải thích (explanation) và khử trùng lặp (deduplication).
  - Đảm bảo tập đặc trưng cuối cùng duy trì tính minh bạch ngữ nghĩa, có khả năng tái lập (reproducible) và miễn nhiễm với hiện tượng ảo giác ngẫu nhiên (stochastic hallucinations) thường gặp trong sinh mã hộp đen (black-box code generation).
  - Quyết định của mô hình có thể giải thích được và hoàn toàn không chứa các tạo tác sinh chưa được kiểm chứng (unverified generative artifacts), giảm thiểu căn bản cả ảo giác thuật toán (algorithmic hallucination) lẫn các thiên kiến dữ liệu kế thừa (inherited data biases).

### H.3 Feasibility on High-Dimensional Datasets

- **Khả năng mở rộng trên tập dữ liệu số chiều cao (high-dimensional datasets)**:
  - SymboLLM-FE tránh được việc tìm kiếm vét cạn bất khả thi (intractable exhaustive searches) nhờ áp dụng hai cơ chế chiến lược:
    1. **Tìm kiếm có cấu trúc định hướng theo tương quan (Correlation-Guided Structured Search)**: Sắp xếp trước các đặc trưng theo hệ số tương quan Spearman (Spearman correlation) với biến mục tiêu, gom cụm các biến có khả năng dự đoán cao; cơ chế cửa sổ mở rộng - trượt (expanding-sliding window) sau đó sinh ra các tập con liền kề, thu giảm hiệu quả không gian tìm kiếm từ hàm mũ $\mathcal{O}(2^n)$ (hoặc $O(2^n)$) xuống đa thức $\mathcal{O}(n^2)$ (hoặc $O(n^2)$).
    2. **Dừng sớm tạo độ thưa (Sparsity-Inducing Early Stopping)**: Tận dụng áp lực tiết giảm / phạt độ phức tạp vốn có (inherent parsimony pressure) của các mô hình hồi quy ký hiệu để thực thi các tiêu chí dừng sớm nghiêm ngặt.
- **Tính khả thi và tối ưu hóa không gian đặc trưng cuối cùng**:
  - Sự kết hợp hiệp đồng giữa việc cắt tỉa không gian tìm kiếm (search space pruning) và quá trình tiến hóa bị chặn về mặt tính toán (computationally bounded evolution) giúp hồi quy ký hiệu hoàn toàn khả thi trên các tập dữ liệu nhiều chiều.
  - Cơ chế hợp nhất có chọn lọc do LLM dẫn dắt (LLM-driven selective merging mechanism) được áp dụng nhằm giảm thiểu hiện tượng tích lũy đặc trưng từ nhiều tập con.
  - Mô-đun này đóng vai trò như một bộ lọc ngữ nghĩa (semantic filter), tích hợp hoặc loại bỏ các ứng viên dựa trên hiệu năng và tính mạch lạc logic (logical coherence), đảm bảo tập đặc trưng cuối cùng nhỏ gọn, không dư thừa và được tối ưu hóa cho các mô hình dự đoán xuôi dòng (downstream predictors).
