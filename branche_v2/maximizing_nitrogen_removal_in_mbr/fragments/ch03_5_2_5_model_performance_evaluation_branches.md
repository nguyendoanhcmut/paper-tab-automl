### 2.5 Model performance evaluation

- Phương pháp kiểm định chéo $5$ phần ($5\text{-fold cross-validation}$) làm chuẩn đánh giá khách quan
  - Toàn bộ tập dữ liệu được phân chia thành $5$ tập con đồng đều và luân phiên kiểm thử.
  - Mỗi vòng kiểm định sử dụng $4$ phần để huấn luyện mô hình và $1$ phần dữ liệu độc lập chưa từng thấy để kiểm tra độ chính xác.
  - Quy trình được lặp lại $5$ lần để đảm bảo mọi quan sát đều được sử dụng làm tập kiểm thử đúng một lần.
  - Kết quả đánh giá cuối cùng là giá trị trung bình trên toàn bộ $5$ lượt kiểm định chéo.
- Ưu điểm rõ rệt so với phương pháp phân chia dữ liệu đơn lẻ (single train-test split)
  - Triệt tiêu hiện tượng sai lệch do ngẫu nhiên hóa và giảm thiểu nguy cơ quá khớp đối với một tập dữ liệu con cụ thể.
  - Đảm bảo mô hình có khả năng khái quát hóa cao trên các tập dữ liệu vận hành thực tế độc lập.
- Hệ thống ba chỉ số sai số đánh giá độ chính xác dự đoán
  - Căn bậc hai sai số trung bình bình phương ($\text{RMSE}$) phản ánh mức độ phân tán và độ lệch của giá trị dự đoán so với thực tế.
  - Sai số tuyệt đối trung bình ($\text{MAE}$) đo lường độ lớn sai số bình quân mà không khuếch đại các điểm dị biệt.
  - Sai số trung bình bình phương ($\text{MSE}$) cung cấp thêm cơ sở xác thực tính đồng nhất của mô hình.
