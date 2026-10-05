### 2.6 Model Evaluation Criteria

- **Các chỉ số định lượng đánh giá hiệu năng mô hình**:
  - Hệ số xác định ($R^2$): Đánh giá mức độ giải thích phương sai của mô hình:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Sai số toàn phương trung bình ($RMSE$):
    $$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  - Sai số tuyệt đối trung bình ($MAE$):
    $$MAE = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
  - Đánh giá tính khái quát hóa thông qua sai khác hiệu năng giữa tập huấn luyện và tập kiểm tra ($\Delta R^2 < 0.05$).
