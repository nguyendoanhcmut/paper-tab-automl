### 2.6 Model Evaluation Criteria

- Nguyên tắc đánh giá độ chính xác trên tập kiểm tra độc lập
  - Độ chính xác dự đoán và năng lực tổng quát hóa của ba mô hình MLR, ANN, SVR được kiểm định trên tập kiểm tra độc lập
  - Sử dụng hai chỉ số thống kê chuẩn mực quốc tế gồm hệ số xác định ($R^2$) và sai số căn bậc hai trung bình (RMSE)
- Định nghĩa toán học của hệ số xác định ($R^2$)
  - Hệ số xác định lượng hóa tỷ lệ phương sai của biến mục tiêu được giải thích bởi các biến đầu vào trong mô hình
  - Công thức tính toán $R^2$ theo phương trình (2):
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó $y_i$ là giá trị quan sát thực nghiệm thực tế, $\hat{y}_i$ là giá trị dự đoán từ mô hình, $\bar{y}$ là giá trị trung bình cộng của các giá trị thực nghiệm, và $n$ là tổng số mẫu thử nghiệm
  - Giá trị $R^2$ tiến gần đến $1.0$ thể hiện mức độ khớp hoàn hảo giữa dự đoán mô hình và thực nghiệm
- Định nghĩa toán học của sai số căn bậc hai trung bình (RMSE)
  - Chỉ số RMSE lượng hóa độ lệch chuẩn của các phần dư dự đoán, phản ánh độ lớn trung bình của sai số
  - Công thức tính toán RMSE theo phương trình (3):
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  - Các ký hiệu $y_i$, $\hat{y}_i$ và $n$ giữ nguyên ý nghĩa như trong công thức tính $R^2$
  - Giá trị RMSE càng nhỏ phản ánh sai số ngẫu nhiên càng thấp và độ chuẩn xác dự đoán của thuật toán càng cao
