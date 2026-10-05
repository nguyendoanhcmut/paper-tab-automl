## 6 Conclusion

- **Đề xuất khung làm việc LLM-FE cho kỹ thuật đặc trưng tự động**: Nghiên cứu giới thiệu khung làm việc mới mang tên LLM-FE, ứng dụng các mô hình ngôn ngữ lớn (Large Language Models - LLMs) đóng vai trò là các bộ tối ưu hóa tiến hóa (evolutionary optimizers) nhằm tự động khám phá các đặc trưng mới cho các tác vụ dự đoán trên dữ liệu dạng bảng (tabular prediction tasks).
  - **Cơ chế hoạt động cốt lõi**: Tự động hóa hiệu quả toàn bộ quy trình kỹ thuật đặc trưng (feature engineering - FE) bằng cách kết hợp ba thành phần then chốt:
    - Cơ chế sinh giả thuyết do LLM dẫn dắt (LLM-driven hypothesis generation).
    - Tín hiệu phản hồi thực nghiệm dựa trên dữ liệu (data-driven feedback).
    - Thuật toán tìm kiếm tiến hóa (evolutionary search).
- **Khẳng định tính ưu việt thực nghiệm trên dữ liệu bảng**: Qua các thực nghiệm toàn diện trên nhiều tác vụ học dữ liệu bảng đa dạng, LLM-FE liên tục vượt trội hơn các phương pháp cơ sở hiện đại nhất (state-of-the-art baselines - SOTA baselines).
  - **Mức độ cải thiện hiệu năng**: Mang lại sự nâng cao đáng kể về hiệu năng dự đoán (predictive performance) trên nhiều kiến trúc mô hình dự đoán dữ liệu bảng khác nhau (như XGBoost, MLP, và TabPFN).
- **Định hướng nghiên cứu và phát triển trong tương lai (Future Work)**:
  - **Tích hợp mô hình ngôn ngữ chuyên biệt**: Khám phá việc tích hợp các mô hình ngôn ngữ mạnh mẽ hơn hoặc các mô hình ngôn ngữ chuyên sâu theo từng lĩnh vực (domain-specific language models) nhằm cải thiện chất lượng và độ phù hợp ngữ cảnh của các đặc trưng được sinh ra đối với các bài toán đặc thù của từng miền tri thức.
  - **Mở rộng sang chu trình dữ liệu toàn diện (data-centric pipeline)**: Mở rộng khung làm việc ra ngoài phạm vi kỹ thuật đặc trưng tới các giai đoạn khác trong quy trình học máy và xử lý dữ liệu:
    - Tăng cường dữ liệu (data augmentation).
    - Làm sạch dữ liệu tự động (automated data cleaning), bao gồm điền khuyết giá trị thiếu (imputation) và phát hiện điểm ngoại lai (outlier detection).
    - Tinh chỉnh mô hình (model tuning / hyperparameter optimization).

### Tuyên bố Tác động (Impact Statement)

- **Nâng cao hiệu năng mô hình và giảm thiểu chi phí kỹ thuật thủ công**: Khung làm việc LLM-FE giúp nâng cao năng lực dự đoán đồng thời giảm thiểu đáng kể công sức kỹ thuật thủ công của con người, đặc biệt có ý nghĩa thiết thực trong các lĩnh vực tiêu tốn nhiều tài nguyên (resource-intensive domains).
  - **Khai phá biểu diễn đặc trưng phức tạp**: Sự kết hợp giữa tri thức miền (domain knowledge) và tối ưu hóa tiến hóa (evolutionary optimization) cho phép phát hiện các biểu diễn đặc trưng hiệu quả mà các kỹ sư dữ liệu rất khó tự thiết kế thủ công.
  - **Tiềm năng ứng dụng xuyên suốt quy trình học máy**: Dù trọng tâm nghiên cứu tập trung vào kỹ thuật đặc trưng, khung làm việc có tiềm năng mở rộng sang các công đoạn liên quan trong quy trình học máy (machine learning pipeline - ML pipeline) như làm sạch dữ liệu (data cleaning), phân tích khám phá (exploratory analysis), tăng cường dữ liệu, và tinh chỉnh mô hình.
- **Vấn đề bảo mật và quyền riêng tư dữ liệu (Privacy Considerations)**:
  - **Nguy cơ rò rỉ dữ liệu qua prompt**: Do LLM-FE có thể chèn các mẫu dữ liệu đã tuần tự hóa (serialized data samples) vào câu lệnh nhắc (prompts), các cân nhắc về quyền riêng tư và bảo mật trở nên đặc biệt quan trọng trong các lĩnh vực nhạy cảm (sensitive domains) như y tế hoặc tài chính.
  - **Các biện pháp giảm thiểu rủi ro bảo mật khả thi trong thực tế**:
    - *Triển khai mô hình mã nguồn mở cục bộ (locally deployed open-source models)*: Tránh hoàn toàn việc truyền dữ liệu ra bên ngoài qua các giao diện lập trình ứng dụng (Application Programming Interfaces - APIs) của bên thứ ba.
    - *Sử dụng dữ liệu ẩn danh hoặc dữ liệu tổng hợp*: Thay thế các mẫu dữ liệu thô (raw data) bằng các mẫu dữ liệu đã khử định danh (anonymized samples) hoặc dữ liệu nhân tạo (synthetic samples).
    - *Loại bỏ hoàn toàn mẫu dữ liệu trong prompt*: Kết quả phân tích cắt bỏ (ablation analysis) đã chứng minh rằng việc loại bỏ toàn bộ các mẫu dữ liệu khỏi prompt chỉ gây ảnh hưởng thứ yếu không đáng kể đến hiệu năng mô hình.
- **Bản chất AutoML có con người trong vòng lặp (Human-in-the-Loop AutoML)**:
  - **Kế thừa và tiếp nối truyền thống AutoML**: Tự động hóa quá trình khám phá đặc trưng là một hướng nghiên cứu nền tảng trong y văn học máy tự động (Automated Machine Learning - AutoML), và LLM-FE tiếp nối quỹ đạo phát triển này.
  - **Vai trò định hướng của chuyên gia con người**: Khung làm việc phụ thuộc căn bản vào các dữ liệu đầu vào do con người cung cấp, bao gồm mô tả tác vụ (task descriptions), siêu dữ liệu đặc trưng (feature metadata), và ngữ cảnh miền (domain context).
  - **Hỗ trợ tăng cường thay vì thay thế chuyên gia**: LLM-FE được thiết kế để bổ trợ và tăng cường năng lực cho các chuyên gia (augment domain experts), giải phóng các nhà khoa học dữ liệu (data scientists) khỏi các bước thử-sai lặp lại để tập trung vào việc ra quyết định và giải quyết vấn đề ở cấp độ chiến lược cao hơn.
  - **Khuyến nghị an toàn cho các lĩnh vực quan trọng (safety-critical domains)**: Các biến đổi do LLM-FE đề xuất cần được đối xử như các giả thuyết để chuyên gia thẩm định và đánh giá (expert-reviewable hypotheses) trước khi xem xét triển khai trực tiếp vào các hệ thống thực tế.

### Tuyên bố về Khả năng Tái lập (Reproducibility Statement)

- **Cung cấp đầy đủ chi tiết triển khai thực nghiệm**: Đảm bảo khả năng tái lập hoàn toàn kết quả nghiên cứu thông qua tài liệu chi tiết:
  - Phần 3 trình bày toàn bộ phương pháp luận lý thuyết và thuật toán.
  - Phụ lục B.1 (Appendix B.1) cung cấp mô tả chuyên sâu về khung làm việc LLM-FE, bao gồm toàn bộ các khuôn mẫu câu lệnh nhắc LLM cụ thể (LLM prompt templates).
  - Phụ lục C (Appendix C) liệt kê chi tiết đặc tả cấu hình của các tập dữ liệu được sử dụng trong các thí nghiệm.
- **Công khai mã nguồn và dữ liệu nghiên cứu**: Toàn bộ mã nguồn triển khai và dữ liệu thực nghiệm được công bố công khai tại kho lưu trữ GitHub: [https://github.com/nikhilsab/LLMFE](https://github.com/nikhilsab/LLMFE) nhằm tạo điều kiện thuận lợi cho các nghiên cứu tiếp theo của cộng đồng học thuật.

### Lời cảm ơn (Acknowledgments)

- **Nguồn tài trợ nghiên cứu**: Công trình nghiên cứu này được hỗ trợ một phần bởi Quỹ Khoa học Quốc gia Hoa Kỳ (U.S. National Science Foundation - NSF) theo Hợp đồng tài trợ số 2416728 (Grant No. 2416728).
