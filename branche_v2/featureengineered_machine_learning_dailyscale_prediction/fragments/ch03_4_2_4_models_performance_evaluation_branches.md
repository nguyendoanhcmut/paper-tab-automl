### 2.4 Model’s performance evaluation

- Ba chỉ số thống kê tiêu chuẩn đánh giá độ chính xác và tính ổn định của mô hình dự đoán:
  - Hệ số xác định ($R^2$): Đo lường tỷ lệ phương sai của nồng độ $T\text{-}P$ quan sát được mô hình giải thích, phản ánh năng lực khớp dữ liệu tổng quát:
    $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
  - Sai số căn phương trung bình ($\text{RMSE}$): Định lượng độ lớn sai số dự báo tổng thể, đặc biệt nhạy cảm với các sai lệch lớn nhằm đánh giá nguy cơ dự báo thiếu hoặc thừa nghiêm trọng:
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$
  - Sai số tuyệt đối trung bình ($\text{MAE}$): Đo khoảng cách tuyệt đối trung bình giữa giá trị thực nghiệm và dự báo, thể hiện tính ổn định trước các điểm dị biệt:
    $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
- Định nghĩa các biến số trong công thức định lượng:
  - $y_i$: Nồng độ $T\text{-}P$ đầu ra thực nghiệm quan trắc tại ngày thứ $i$.
  - $\hat{y}_i$: Nồng độ $T\text{-}P$ đầu ra dự đoán từ mô hình học máy tại ngày thứ $i$.
  - $\bar{y}$: Giá trị trung bình số học của các quan sát thực nghiệm trong tập mẫu.
  - $n$: Tổng số lượng mẫu dữ liệu đánh giá.
