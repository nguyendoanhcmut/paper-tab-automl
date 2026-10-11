## 6 Conclusion

* Nghiên cứu giới thiệu khung làm việc (framework) mới LLM-FE, tận dụng các mô hình ngôn ngữ lớn (Large Language Models - LLMs) làm bộ tối ưu hóa tiến hóa (evolutionary optimizers) để khám phá các đặc trưng (features) mới cho các tác vụ dự đoán trên dữ liệu dạng bảng (tabular prediction tasks).
* Bằng cách kết hợp quá trình sinh giả thuyết do LLM điều hướng (LLM-driven hypothesis generation) với phản hồi dựa trên dữ liệu (data-driven feedback) và tìm kiếm tiến hóa (evolutionary search), LLM-FE tự động hóa quy trình kỹ thuật đặc trưng (feature engineering process) một cách hiệu quả.
* Thông qua các thực nghiệm toàn diện trên nhiều tác vụ học dữ liệu bảng đa dạng, LLM-FE liên tục vượt trội hơn các đường cơ sở tiên tiến nhất (state-of-the-art baselines), mang lại sự cải thiện đáng kể về hiệu năng dự đoán trên nhiều mô hình dự đoán dạng bảng khác nhau.
* Các hướng nghiên cứu trong tương lai:
  * Khám phá việc tích hợp các mô hình ngôn ngữ mạnh mẽ hơn hoặc các mô hình ngôn ngữ chuyên biệt theo miền (domain-specific language models) nhằm nâng cao độ phù hợp và chất lượng của các đặc trưng được tạo ra cho các bài toán thuộc từng miền cụ thể.
  * Mở rộng khung làm việc ra ngoài phạm vi kỹ thuật đặc trưng tới các giai đoạn khác của quy trình học trên dữ liệu bảng và quy trình lấy dữ liệu làm trung tâm (data-centric pipeline), bao gồm tăng cường dữ liệu (data augmentation), làm sạch dữ liệu tự động (automated data cleaning, gồm gán giá trị khuyết thiếu - imputation và phát hiện giá trị ngoại lai - outlier detection), và tinh chỉnh mô hình (model tuning).

### Impact Statement

* Khung làm việc LLM-FE cho kỹ thuật đặc trưng tự động do LLM dẫn dắt giúp nâng cao hiệu năng dự đoán đồng thời giảm thiểu công sức thủ công, đặc biệt trong các miền tiêu tốn nhiều tài nguyên (resource-intensive domains).
* Bằng cách kết hợp tri thức miền (domain knowledge) với tối ưu hóa tiến hóa (evolutionary optimization), LLM-FE hỗ trợ khám phá các biểu diễn đặc trưng (feature representations) hiệu quả vốn khó có thể thiết kế thủ công.
* Tiềm năng mở rộng của khung làm việc:
  * Mặc dù nghiên cứu này tập trung vào kỹ thuật đặc trưng, khung làm việc có thể mở rộng sang các giai đoạn liên quan trong quy trình học máy (ML pipeline) như làm sạch dữ liệu (data cleaning), phân tích khám phá (exploratory analysis), tăng cường dữ liệu (data augmentation), và tinh chỉnh mô hình (model tuning).
* Vấn đề quyền riêng tư dữ liệu (privacy considerations) và các giải pháp giảm thiểu rủi ro:
  * LLM-FE có thể đưa các mẫu dữ liệu đã được tuần tự hóa (serialized data samples) vào câu lệnh nhắc (prompts), đặt ra lưu ý quan trọng về quyền riêng tư dữ liệu trong các miền nhạy cảm (sensitive domains) (tương tự các phương pháp kỹ thuật đặc trưng dựa trên LLM trước đó vốn cũng dựa vào ví dụ trong prompt).
  * Các biện pháp giảm thiểu rủi ro khả thi trong thực tế:
    * LLM-FE có thể hoạt động với các mô hình mã nguồn mở được triển khai cục bộ (locally deployed open-source models) để tránh truyền dữ liệu ra bên ngoài.
    * Sử dụng các mẫu dữ liệu đã được ẩn danh (anonymized) hoặc dữ liệu tổng hợp (synthetic samples) thay cho dữ liệu thô.
    * Lược bỏ hoàn toàn các ví dụ mẫu dữ liệu khỏi prompt với mức suy giảm hiệu năng không đáng kể, như đã được chứng minh trong phân tích triệt tiêu (ablation analysis).
* Định vị trong lĩnh vực AutoML và vai trò con người trong vòng lặp (Human-in-the-loop AutoML):
  * Việc tự động hóa khám phá đặc trưng là hướng đi đã được xác lập vững chắc trong y văn AutoML, và LLM-FE tiếp nối quỹ đạo nghiên cứu này.
  * LLM-FE phụ thuộc cốt lõi vào các thông tin đầu vào từ người dùng như mô tả tác vụ (task descriptions), siêu dữ liệu đặc trưng (feature metadata), và ngữ cảnh miền (domain context), đóng vai trò là một ví dụ điển hình của AutoML có con người tham gia trong vòng lặp (human-in-the-loop AutoML).
  * LLM-FE được thiết kế để tăng cường năng lực cho các chuyên gia miền (augment domain experts) thay vì thay thế họ, giúp các nhà khoa học dữ liệu (data scientists) tập trung vào việc giải quyết vấn đề và ra quyết định ở cấp độ cao hơn.
  * Trong các miền quan trọng về độ an toàn (safety-critical domains), các kết quả đầu ra của LLM-FE cần được xem là các giả thuyết cần chuyên gia thẩm định (expert-reviewable hypotheses) thay vì các phép biến đổi có thể triển khai trực tiếp ngay lập tức.

### Reproducibility Statement

* Nhằm đảm bảo khả năng tái lập (reproducibility) của nghiên cứu, các chi tiết cài đặt toàn diện của LLM-FE được cung cấp đầy đủ:
  * Mục $3$ trình bày toàn bộ phương pháp luận (methodology).
  * Phụ lục $B.1$ cung cấp mô tả chuyên sâu về khung làm việc, bao gồm các câu nhắc LLM (LLM prompts) cụ thể được sử dụng.
  * Các tập dữ liệu được sử dụng trong các thực nghiệm được mô tả chi tiết tại Phụ lục $C$.
  * Mã nguồn và dữ liệu được công bố công khai tại: https://github.com/nikhilsab/LLMFE để tạo điều kiện thuận lợi cho các nghiên cứu tiếp theo.
* Lời cảm ơn và tài trợ:
  * Nghiên cứu này được hỗ trợ một phần bởi Quỹ Khoa học Quốc gia Hoa Kỳ (U.S. National Science Foundation - NSF) theo Mã tài trợ số $2416728$.
