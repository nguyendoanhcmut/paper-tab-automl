### 2.5 Predictive Machine Learning Model Implementation

- **Kiến trúc và thiết lập các thuật toán học máy**:
  - Mô hình mạng nơ-ron nhân tạo ($ANN$) dạng truyền thẳng nhiều lớp đa tầng ($MLP$) với cấu trúc $6	ext{-}N	ext{-}1$, sử dụng thuật toán lan truyền ngược Levenberg-Marquardt.
  - **Hình 3.** Kiến trúc mạng nơ-ron nhân tạo ANN (6-N-1)
    - <img src="assets/fig_03_p6.jpeg" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - Thể hiện liên kết đầy đủ giữa 6 biến đầu vào, tầng ẩn với số nơ-ron tối ưu hóa và biến mục tiêu dự đoán loại bỏ COD.
    - **Từ đâu mà thấy được**
      - Sơ đồ mạng gồm 6 nút vào, các trọng số kết nối $w_{ij}$, hàm kích hoạt Sigmoid và nút ra duy nhất dự đoán COD removal.
  - Quy trình mô hình hóa bao gồm chuẩn hóa dữ liệu ($StandardScaler$), phân chia tập huấn luyện/kiểm tra tỷ lệ $80/20$ và tối ưu siêu tham số qua kiểm định chéo $5	ext{-fold\ CV}$.
  - **Hình 4.** Quy trình mô hình hóa học máy tổng thể
    - <img src="assets/fig_04_p6.jpeg" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Mô tả chu trình khép kín từ tiền xử lý dữ liệu, huấn luyện 3 mô hình, tối ưu hóa đến đánh giá độ chính xác và phân tích độ nhạy.
    - **Từ đâu mà thấy được**
      - Các khối chức năng liên hoàn: Thu thập dữ liệu thực nghiệm, làm sạch dữ liệu, huấn luyện SVR/ANN/MLR, đánh giá $R^2/RMSE$, và phân tích PDP.
