## 2.2. Exploratory Data Analysis (EDA)

- Phân tích khám phá dữ liệu (Exploratory Data Analysis - $EDA$) được tiến hành nhằm kiểm tra phân phối (distribution), các mối quan hệ (relationships) và các quy luật tiềm ẩn (underlying patterns) trong tập dữ liệu.
  - Phân tích bao gồm thống kê mô tả (descriptive statistics), các kỹ thuật trực quan hóa (visualization techniques), phân tích tương quan (correlation analysis) và các kiểm định phân phối chuẩn (normality tests).
  - Mục tiêu là đánh giá các đặc tính của các đặc trưng (features) và thông số mục tiêu (target parameters) trước khi bước vào giai đoạn phát triển mô hình (model development).

### 2.2.1. Operational Feature Statistics

- Các thước đo thống kê mô tả (Descriptive statistical measures) được tính toán cho tất cả các đặc trưng và biến mục tiêu (target variables).
  - Các giá trị thống kê được tính toán gồm: giá trị trung bình (mean), trung vị (median), độ lệch chuẩn (standard deviation - $std$), giá trị nhỏ nhất (minimum) và giá trị lớn nhất (maximum).
  - Phân tích cung cấp cái nhìn tổng quan về xu hướng tập trung (central tendency) và mức độ biến thiên (variability) của dữ liệu.
  - Hỗ trợ nhận diện các dị thường (anomalies) hoặc giá trị ngoại lai (outliers) tiềm ẩn trong tập dữ liệu.

### 2.2.2. Pair Plot

- Biểu đồ cặp (Pair plot) được thiết lập nhằm khảo sát các mối quan hệ theo cặp (pairwise relationships) giữa các đặc trưng và các thông số mục tiêu.
  - Trực quan hóa này cung cấp thông tin chi tiết về các mối tương quan tuyến tính hoặc phi tuyến tính tiềm ẩn (potential linear or non-linear correlations), các mẫu phân cụm (clustering patterns) và các giá trị ngoại lai (outliers).
  - Thúc đẩy việc hiểu sâu hơn về tập dữ liệu trước khi phát triển mô hình.
  - Biểu đồ cặp được xây dựng bằng thư viện Seaborn ($0.13.2$) trong môi trường Python ($3.13.1$).
  - Biểu đồ tích hợp các đường hồi quy (regression lines) để quan sát các xu hướng tuyến tính khả dĩ và các khoảng tin cậy (confidence intervals) nhằm đánh giá mức độ biến thiên (variability).

### 2.2.3. Scatter Plot

- Các biểu đồ phân tán riêng lẻ (Individual scatter plots) được sử dụng để khám phá mối quan hệ giữa các đặc trưng đầu vào cụ thể (specific input features) và các thông số mục tiêu ($TMP$ và $Spec.\ Flux$).
  - Các biểu đồ hỗ trợ phát hiện các xu hướng tuyến tính hoặc phi tuyến tính khả dĩ.
  - Hỗ trợ phát hiện các giá trị ngoại lai (outliers) có nguy cơ ảnh hưởng đến hiệu năng của mô hình (model performance).

### 2.2.4. Pearson Correlation

- Hệ số tương quan Pearson ($r$) được tính toán nhằm định lượng mối quan hệ tuyến tính (linear relationship) giữa từng đặc trưng và các thông số mục tiêu.
  - Ma trận tương quan (correlation matrix) được xây dựng nhằm trực quan hóa cường độ (strength) và chiều hướng (direction) của các mối liên kết.
  - Phân tích hỗ trợ quá trình lựa chọn đặc trưng (feature selection) bằng cách xác định các biến có tương quan cao (highly correlated variables) có thể ảnh hưởng đến hiệu năng của mô hình.

### 2.2.5. Normality Check

- Kiểm định Shapiro–Wilk (Shapiro–Wilk test) được thực hiện cho tất cả các đặc trưng và biến mục tiêu nhằm đánh giá tính phân phối chuẩn (normality) của tập dữ liệu.
  - Kiểm định đánh giá liệu một tập dữ liệu cho trước có tuân theo phân phối chuẩn (normal distribution) hay không.
  - Giả thuyết không ($H_0$) giả định dữ liệu tuân theo phân phối chuẩn.
  - Giả thuyết đối ($H_1$) cho rằng dữ liệu có sự sai lệch so với phân phối chuẩn (deviation from normality).
  - Giá trị thống kê kiểm định Shapiro–Wilk nằm trong khoảng từ $0$ đến $1$, với các giá trị tiệm cận $1$ biểu thị mức độ tương đồng cao hơn với phân phối chuẩn.
  - Ngưỡng $p\text{-value}$ bằng $0.05$ được sử dụng để đánh giá ý nghĩa thống kê (statistical significance).
  - Nếu $p\text{-value} > 0.05$, giả thuyết không ($H_0$) không bị bác bỏ, xác nhận dữ liệu tuân theo phân phối chuẩn.
