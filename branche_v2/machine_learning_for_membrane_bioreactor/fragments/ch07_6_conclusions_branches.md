## 6 Conclusions

* Bài báo tổng kết các tiến bộ gần đây trong lĩnh vực machine learning (học máy) nhằm dự đoán hiệu suất loại bỏ chất ô nhiễm (pollutants removal) và hiện tượng nghẽn màng (membrane fouling) trong quy trình MBR (membrane bioreactor - bể phản ứng sinh học màng).
* Dựa trên tổng quan tài liệu (literature review), nhiều phương pháp machine learning đã được ứng dụng trong phạm vi nghiên cứu này:
  * Mạng nơ-ron nhân tạo ANN (artificial neural networks).
  * Máy vector hỗ trợ SVM (support vector machines).
  * Cây quyết định (decision trees).
* Các mô hình ANN thông thường (ordinary ANNs) chiếm ưu thế chủ đạo trong số các mô hình dự đoán được công bố.
  * Nghiên cứu về các mô hình deep learning (học sâu) trong lĩnh vực này vẫn còn nhiều giới hạn (limitations).
* Bài báo đánh giá các nguyên lý cơ bản của machine learning, đồng thời trình bày một ví dụ hướng dẫn (tutorial example) để người đọc thực hành $5$ mô hình (five models) trong việc dự đoán TMP (transmembrane pressure - áp suất xuyên màng).
* Bên cạnh tiềm năng lớn của machine learning trong nghiên cứu MBR, việc tiếp tục phát triển và triển khai mô hình ở quy mô kỹ thuật thực tế (full-scale engineering) đối mặt với các thách thức chính:
  * Sự thiếu hụt về các đặc trưng đầu vào (input features) và các chỉ số giám sát (monitoring metrics).
  * Khả năng giải thích mô hình (model interpretability) và khả năng tổng quát hóa (generalizability) chưa đáp ứng đầy đủ yêu cầu thực tiễn.
  * Thiếu tính khả thi thực tế (lack of practicability) trong việc kiểm soát quy trình tự động (automated process control).
* Việc xây dựng một hệ thống chỉ số đầu vào hoàn chỉnh hơn (a more complete input index system) được hỗ trợ bởi công nghệ giám sát trực tuyến (online monitoring) đóng vai trò then chốt:
  * Cho phép phát triển các mô hình phản hồi theo thời gian thực (real-time responsive models) hoặc các mô hình điều khiển đón đầu / cấp nguồn trước (feedforward models).
  * Thu hẹp khoảng cách giữa kết quả dự đoán lý thuyết của mô hình và kiểm soát vận hành thực tế (practical control).
* Một cơ sở dữ liệu vận hành MBR mở và chia sẻ (open and shared MBR operation database) mang lại lợi ích lớn trong việc thúc đẩy khả năng tổng quát hóa (generalizability) và khả năng giải thích (interpretability) của mô hình.
* Ứng dụng deep learning và các thuật toán tối ưu hóa thông minh (intelligent optimization algorithms) có thể nâng cao hiệu suất hoạt động của mô hình (model performance).
* Tích hợp AutoML (automated machine learning - học máy tự động) và XAI (explainable artificial intelligence - trí tuệ nhân tạo có thể giải thích) có thể tạo điều kiện thuận lợi cho việc triển khai mô hình vào các ứng dụng kỹ thuật thực tế.
* Các nội dung và phân tích trong bài báo được kỳ vọng sẽ cung cấp định hướng cho các nghiên cứu tương lai hướng đến vận hành và bảo trì thông minh (intelligent operation and maintenance) các hệ thống MBR trên nền tảng machine learning.
* Thông tin tài trợ và công bố bài báo (Acknowledgements & Article Information):
  * Nghiên cứu nhận được sự tài trợ từ National Natural Science Foundation of China (Mã số: $52370059$), Beijing Natural Science Foundation (Mã số: $\text{JQ}22027$), và Fundamental Research Funds for the Central Universities (Mã số: $\text{E2EG0502X2}$).
  * Tuyên bố xung đột lợi ích (Conflict of Interests): Kang Xiao và Xia Huang là thành viên ban biên tập của tạp chí Frontiers of Environmental Science & Engineering; các tác giả khẳng định không có xung đột lợi ích thương mại hay tài chính.
  * Tài liệu bổ trợ trực tuyến (Electronic Supplementary Material): Có sẵn tại DOI $10.1007/\text{s}11783-025-1954-2$ (năm $2025$, tập $19$, số $(3)$: $34$).
