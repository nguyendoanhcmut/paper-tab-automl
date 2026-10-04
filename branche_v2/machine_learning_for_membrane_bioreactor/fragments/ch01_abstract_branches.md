## Abstract

- Hiện tượng tắc nghẽn màng (membrane fouling) đặt ra thách thức lớn đối với sự phát triển bền vững của các công nghệ bể phản ứng sinh học màng (MBR - membrane bioreactor) trong xử lý nước thải (wastewater treatment).
  - Dự đoán chính xác quá trình lọc màng (membrane filtration process) có tầm quan trọng lớn nhằm nhận diện và kiểm soát hiện tượng tắc nghẽn màng.
- Các phương pháp học máy (machine learning) giải quyết các hạn chế của các phương pháp tiếp cận thống kê truyền thống (traditional statistical approaches):
  - Khắc phục các nhược điểm về độ chính xác thấp (low accuracy), khả năng tổng quát hóa kém (poor generalization ability) và tốc độ hội tụ chậm (slow convergence).
  - Phát huy hiệu quả đặc biệt trong việc dự đoán các quá trình lọc và tắc nghẽn phức tạp trong bối cảnh dữ liệu lớn (big data).
- Nghiên cứu trình bày chi tiết về lý thuyết học máy (machine learning theory) và tổng quan các tiến bộ ứng dụng trong hệ thống MBR:
  - Các phương pháp học máy được tổng quan bao gồm mạng nơ-ron nhân tạo (ANN - artificial neural networks), máy vector hỗ trợ (SVM - support vector machines), cây quyết định (decision trees) và học kết hợp (ensemble learning).
- Nghiên cứu tóm tắt và so sánh các đặc trưng đầu vào và đầu ra của mô hình (model input and output characteristics) dựa trên y văn hiện hành:
  - Các nhóm đặc trưng bao gồm đặc tính chất gây tắc nghẽn (foulant characteristics), môi trường dung dịch (solution environments), điều kiện lọc (filtration conditions), điều kiện vận hành (operating conditions) và các yếu tố thời gian (time factors).
  - So sánh việc lựa chọn mô hình và các thuật toán tối ưu hóa (optimization algorithms).
- Quy trình xây dựng mô hình (modeling procedures) được minh họa chi tiết thông qua một ví dụ hướng dẫn (tutorial example) cho năm phương pháp:
  - Năm phương pháp bao gồm SVM, rừng ngẫu nhiên (RF - random forest), mạng nơ-ron lan truyền ngược (BPNN - back propagation neural network), mạng bộ nhớ ngắn-dài hạn (LSTM - long short-term memory) và mạng lan truyền ngược tối ưu hóa bằng thuật toán di truyền (GA-BP - genetic algorithm-back propagation).
  - Kết quả mô phỏng chứng minh cả năm phương pháp đều đem lại dự đoán chính xác với $R^2 > 0.8$.
- Các thách thức hiện tại trong việc triển khai các mô hình học máy vào hệ thống MBR được phân tích cụ thể:
  - Sự tích hợp của học sâu (deep learning), học máy tự động (AutoML - automated machine learning) và trí tuệ nhân tạo có thể giải thích (XAI - explainable artificial intelligence) có thể tạo điều kiện thuận lợi cho việc ứng dụng mô hình vào thực tế kỹ thuật.
  - Các phân tích chuyên sâu được kỳ vọng sẽ thúc đẩy việc thiết lập khuôn khổ điều khiển thông minh (intelligent control framework) cho các quy trình MBR trong tương lai.
