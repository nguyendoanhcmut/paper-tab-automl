### 2.5 Model selection guide

- **Tầm quan trọng của lựa chọn phương pháp mô hình hóa (modeling method selection)**: Việc lựa chọn một phương pháp mô hình hóa phù hợp (appropriate modeling method) có vai trò then chốt tối quan trọng (paramount importance).
- **Phân loại phương pháp theo sự hiện diện của nhãn dữ liệu (data labeling status)**:
  - Các phương pháp học không giám sát (unsupervised learning methods) được áp dụng khi tập dữ liệu thiếu các nhãn đầu ra (output labels).
  - Các phương pháp học có giám sát (supervised learning methods) được sử dụng khi tập dữ liệu chứa các nhãn đầu ra.
- **Xác định loại bài toán (type of problem)** là bước đầu tiên trong quy trình lựa chọn mô hình:
  - Đối với các bài toán có nhãn đầu ra dạng số (numerical output labels), tức các bài toán hồi quy (regression) hoặc chuỗi thời gian (time-series problems): Các mô hình như SVR (Support Vector Regression), RF (Random Forest), và ANN (Artificial Neural Network) có thể được lựa chọn.
  - Đối với các bài toán có dữ liệu đầu ra dạng rời rạc hoặc định danh (discrete or nominal output data), tức các bài toán phân loại (classification problems): Các mô hình như SVC (Support Vector Classification), RF, và ANN là phù hợp.
  - Đối với các trường hợp liên quan đến nhiều quá trình ra quyết định (multiple decision-making processes): Học tăng cường (reinforcement learning) có thể là một giải pháp mang lại lợi thế (advantageous solution).
- **Cân nhắc quy mô của tập dữ liệu (magnitude of the data set)** là bước tiếp theo cần xem xét:
  - Khi kích thước mẫu bị giới hạn (sample size is limited): Các mô hình SVM (Support Vector Machine), RF, và MLP (Multilayer Perceptron) với cấu trúc tương đối đơn giản đã được chứng minh là có thể đạt được kết quả có độ bền vững thỏa đáng (adequately robust results).
  - Khi kích thước mẫu lớn (sample size is large): Hiệu suất của DNN (Deep Neural Network) có thể được tối ưu hóa.
- **Đặc tính của dữ liệu đầu vào (characteristics of the input data)** giữ vai trò trọng yếu trong việc lựa chọn kiến trúc chuyên biệt:
  - LSTM (Long Short-Term Memory) phù hợp cho dữ liệu chuỗi thời gian (time-series data).
  - CNN (Convolutional Neural Network) phù hợp cho dữ liệu ma trận mang đặc tính hình ảnh (matrix data with image characteristics).
  - GNN (Graph Neural Network) phù hợp để xử lý trực tiếp dữ liệu có cấu trúc đồ thị (graph-structured data).
