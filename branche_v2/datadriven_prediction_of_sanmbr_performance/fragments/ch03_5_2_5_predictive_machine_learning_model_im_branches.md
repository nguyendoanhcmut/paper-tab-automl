### 2.5 Predictive Machine Learning Model Implementation

- Tổng quan triển khai ba thuật toán học máy đối sánh
  - Ba thuật toán gồm Hồi quy tuyến tính bội (MLR), Mạng nơ-ron nhân tạo (ANN) và Hồi quy vector hỗ trợ (SVR) được triển khai độc lập
  - Mục tiêu cốt lõi là dự đoán chính xác hiệu suất loại bỏ COD dưới các điều kiện sốc tải hợp chất phenolic

#### 2.5.1 Multiple Linear Regression (MLR)

- Vai trò mô hình đường cơ sở (Baseline model)
  - Mô hình MLR được sử dụng để đánh giá mức độ tuyến tính nội tại của hệ thống phản ứng màng SAnMBR
  - Đóng vai trò mốc tham chiếu định lượng để xác định sự cải thiện độ chính xác của các thuật toán phi tuyến
- Công thức toán học hồi quy tuyến tính bình phương tối thiểu (OLS)
  - Phương trình hồi quy thiết lập mối tương quan tuyến tính giữa 6 biến đầu vào ($X_i$) và hiệu suất xử lý COD dự đoán ($\hat{Y}$):
    $$\hat{Y} = \beta_0 + \sum_{i=1}^6 \beta_i X_i$$
  - Trong đó $\hat{Y}$ là phần trăm loại bỏ COD dự đoán, $X_i$ là các thông số vận hành độc lập, $\beta_i$ là hệ số hồi quy trọng số, và $\beta_0$ là hệ số chặn (intercept)

#### 2.5.2 Support Vector Regression (SVR)

- Cơ chế ánh xạ không gian nhiều chiều và hàm nhân phi tuyến
  - SVR được lựa chọn làm công cụ dự đoán phi tuyến chính nhờ khả năng tổng quát hóa cao đối với dữ liệu môi trường phức tạp
  - Sử dụng hàm nhân (kernel function) ánh xạ không gian đầu vào 6 chiều lên không gian đặc trưng nhiều chiều để tuyến tính hóa bài toán hồi quy
- Lựa chọn hàm nhân RBF và tối ưu hóa siêu tham số
  - Hàm nhân cơ sở xuyên tâm (Radial Basis Function - RBF) được lựa chọn nhờ khả năng mô tả động học sinh học chính xác và tin cậy cao:
    $$K(x, x') = \exp(-\gamma ||x - x'||^2)$$
  - Hiệu suất mô hình được tinh chỉnh tỉ mỉ thông qua tối ưu hóa hai siêu tham số then chốt: tham số phạt $C$ (penalty parameter) và độ rộng hàm nhân $\gamma$ (kernel width)

#### 2.5.3 Artificial Neural Network (ANN)

- Kiến trúc mạng Perceptron đa tầng (MLP)
  - Mô hình ANN được xây dựng dựa trên cấu trúc mạng truyền thẳng nhiều lớp với thuật toán lan truyền ngược (backpropagation)
  - Cấu trúc mạng nơ-ron được tối ưu hóa theo mô hình 6-N-1 để cân bằng giữa độ phức tạp tính toán và nguy cơ quá khớp (overfitting)
- Kiến trúc cấu hình mạng nơ-ron nhân tạo MLP theo mô hình 6-N-1
  - **Hình 2. Kiến trúc mạng nơ-ron nhân tạo ANN với cấu trúc 6-N-1**
    - ![Hình 2. Kiến trúc mạng nơ-ron ANN](assets/fig_03_p6.jpeg)
    - Lớp đầu vào gồm 6 neuron tiếp nhận các giá trị đặc trưng vận hành sau chuẩn hóa
    - Lớp ẩn đơn lẻ gồm N neuron áp dụng hàm kích hoạt phi tuyến tansig
    - Lớp đầu ra gồm 1 neuron đơn lẻ sử dụng hàm kích hoạt tuyến tính purelin
    - Thuật toán tối ưu hóa lan truyền ngược điều chỉnh ma trận trọng số và độ lệch
- Hàm truyền kích hoạt phi tuyến và cấu trúc dòng thông tin
  - Lớp ẩn áp dụng hàm tiếp tuyến sigmoid (tansig) nhằm đưa tính phi tuyến phức tạp vào quá trình biến đổi dữ liệu:
    $$f(z) = \frac{2}{1 + e^{-2z}} - 1$$
  - Lớp đầu ra sử dụng hàm tuyến tính (purelin) $f(z) = z$ để xuất giá trị dự đoán liên tục của hiệu suất xử lý COD

#### 2.5.4 Computational Tools and Environment

- Môi trường phần mềm và các thư viện tính toán khoa học
  - Tất cả các mô hình học máy và phân tích diễn giải được xây dựng trên ngôn ngữ Python phiên bản 3.10
  - Thư viện Scikit-learn (phiên bản 1.2.2) thực thi các thuật toán SVR, MLR và quy trình tiền xử lý
  - Framework TensorFlow/Keras hỗ trợ thiết kế, huấn luyện và tối ưu cấu trúc mạng nơ-ron nhân tạo ANN
  - Thư viện Pandas xử lý dữ liệu bảng, phân chia tập dữ liệu; Matplotlib và Seaborn phục vụ biểu diễn đồ họa
- Sơ đồ quy trình tổng thể từ thu thập dữ liệu đến diễn giải mô hình học máy
  - **Hình 3. Quy trình làm việc tổng thể của quá trình mô hình hóa học máy (ML)**
    - ![Hình 3. Quy trình làm việc tổng thể ML](assets/fig_04_p6.jpeg)
    - Thu thập 189 quan sát thực nghiệm và chuẩn hóa Min-Max theo tỷ lệ 70/30
    - Huấn luyện và tinh chỉnh siêu tham số độc lập cho ba thuật toán MLR, ANN và SVR
    - Đánh giá kiểm định mô hình qua các chỉ số $R^2$, RMSE và phân tích phần dư
    - Triển khai công cụ diễn giải đồ thị phụ thuộc một phần PDP và phân tích độ nhạy
- Chu trình triển khai mô hình và công cụ giải thích kỹ thuật
  - Chu trình gồm 4 pha tuần tự: thu thập dữ liệu, huấn luyện mô hình, kiểm định trên tập kiểm tra độc lập, và phân tích cơ chế
  - Đồ thị phụ thuộc một phần (PDP) kiểm tra tác động biên của từng biến vận hành lên hiệu suất loại bỏ COD
  - Phân tích độ nhạy lượng hóa tầm quan trọng tương đối của từng biến đầu vào trên toàn bộ dải vận hành quan sát
