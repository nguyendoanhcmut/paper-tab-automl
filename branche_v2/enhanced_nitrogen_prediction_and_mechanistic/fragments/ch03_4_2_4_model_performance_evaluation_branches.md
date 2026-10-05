### 2.4 Model performance evaluation

- Các chỉ số thống kê định lượng đánh giá hiệu năng mô hình dự đoán:
  - Hiệu năng của từng mô hình học máy được đánh giá bằng hệ số xác định ($R^2$) và sai số căn bậc hai trung bình bình phương ($RMSE$).
  - Công thức tính toán hệ số xác định $R^2$:
    - $R^2 = 1 - \frac{\sum_{i=1}^n (\hat{y}_i - y_i)^2}{\sum_{i=1}^n (\bar{y} - y_i)^2}$ (Phương trình 4)
    - Thang điểm $R^2$ đo lường tỷ lệ phương sai của biến mục tiêu được giải thích bởi các biến đặc trưng đầu vào.
  - Công thức tính toán sai số $RMSE$:
    - $RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)^2}$ (Phương trình 5)
    - Chỉ số $RMSE$ định lượng độ lệch tuyệt đối trung bình giữa giá trị dự đoán và giá trị thực tế theo đơn vị $\text{mg/L}$.
  - Ý nghĩa các ký hiệu toán học trong các phương trình đánh giá:
    - Ký hiệu $n$ đại diện cho tổng số lượng mẫu quan trắc trong tập kiểm tra độc lập.
    - Đại lượng $y_i$ và $\hat{y}_i$ lần lượt là nồng độ nitơ đo đạc thực nghiệm và giá trị nồng độ do mô hình dự đoán.
    - Giá trị $\bar{y}$ biểu thị nồng độ trung bình cộng của toàn bộ các mẫu đo thực nghiệm.
  - Cả hai chỉ số được tính toán trên tập dữ liệu kiểm tra sau khi hoàn thành kiểm định chéo để đảm bảo tính khách quan.
