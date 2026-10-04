### 2.3. Evaluation

- Các chỉ số đánh giá (evaluation metrics) hiệu năng dự đoán được sử dụng trong nghiên cứu bao gồm 5 thước đo:
  - Sai số bình phương trung bình ($\text{MSE}$ - mean squared error).
  - Sai số tuyệt đối trung bình ($\text{MAE}$ - mean absolute error).
  - Căn bậc hai của sai số bình phương trung bình ($\text{RMSE}$ - root mean squared error).
  - Sai số phần trăm tuyệt đối trung bình ($\text{MAPE}$ - mean absolute percentage error).
  - Hệ số xác định ($R^2$ - coefficient of determination).
  - Định nghĩa biến trong các công thức: $y_i$ là giá trị quan sát thực tế (observations), $\hat{y}_i$ là giá trị dự đoán của mô hình (model predictions), $n$ là số lượng mẫu (number of samples), và $\bar{y}$ là giá trị trung bình của các quan sát thực tế.
- Công thức xác định sai số tuyệt đối trung bình ($\text{MAE}$):
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \tag{2}$$
  - $\text{MAE}$ là giá trị trung bình của các chênh lệch tuyệt đối giữa quan sát thực tế $y_i$ và giá trị dự đoán $\hat{y}_i$.
  - Cùng với $\text{RMSE}$, $\text{MAE}$ đại diện cho độ chụm/độ chính xác (precision) của các dự đoán mô hình.
  - Đơn vị đo của $\text{MAE}$ trong nghiên cứu này là phần trăm ($\%$) (đồng nhất với đơn vị của biến đầu ra).
- Công thức xác định căn bậc hai của sai số bình phương trung bình ($\text{RMSE}$):
  $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \tag{3}$$
  - $\text{RMSE}$ là căn bậc hai của giá trị trung bình các sai số bình phương giữa $y_i$ và $\hat{y}_i$.
  - $\text{RMSE}$ gán trọng số cao hơn cho các sai số lớn do cơ chế bình phương sai số so với $\text{MAE}$.
  - Cùng với $\text{MAE}$, $\text{RMSE}$ đại diện cho độ chính xác (precision) của dự đoán mô hình.
  - Đơn vị đo của $\text{RMSE}$ trong nghiên cứu này là phần trăm ($\%$) (đồng nhất với đơn vị của biến đầu ra).
- Công thức xác định sai số phần trăm tuyệt đối trung bình ($\text{MAPE}$):
  $$\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100 \tag{4}$$
  - $\text{MAPE}$ là độ lệch phần trăm trung bình giữa giá trị quan sát $y_i$ và giá trị dự đoán $\hat{y}_i$.
  - Đơn vị đo của $\text{MAPE}$ là phần trăm ($\%$) (sai số tương đối tính theo phương trình (4)).
- Công thức xác định hệ số xác định ($R^2$):
  $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \tag{5}$$
  - Giá trị $R^2 = 1$ biểu thị sự khớp hoàn hảo (perfect fit) của mô hình đối với dữ liệu.
  - Giá trị $R^2$ tiến gần về $0$ chỉ ra rằng mô hình có năng lực giải thích tối thiểu (minimal explanatory power) đối với biến mục tiêu.
  - Giá trị $R^2$ âm ($R^2 < 0$) chỉ ra rằng sai số dự đoán vượt quá phương sai nội tại (inherent variance) của tập dữ liệu.
  - Nhìn chung, giá trị $R^2$ càng tiến gần đến $1$ thì mô hình càng tốt.
- Phân tích Bland-Altman (Bland-Altman analysis) được thực hiện nhằm đánh giá mức độ tương đồng (concordance) giữa hiệu suất loại bỏ COD (COD removal efficiency) dự đoán và giá trị thực nghiệm:
  - Các thước đo sai số (chẳng hạn như $\text{RMSE}$) chỉ đánh giá hiệu năng dự đoán tổng thể (overall predictive performance), không định lượng rõ ràng mức độ phù hợp (agreement) giữa giá trị dự đoán và giá trị thực nghiệm (ground truth) (Martin Bland and Altman, 1986).
  - Phương pháp Bland-Altman phân tích sai khác giữa hai phương pháp so với giá trị trung bình của chúng (Martin Bland and Altman, 1986).
  - Trong nghiên cứu này, sai khác được tính bằng giá trị thực nghiệm trừ đi giá trị dự đoán: $\text{difference} = \text{ground truth} - \text{prediction}$.
  - Sai khác khác 0 (non-zero difference) phản ánh xu hướng của mô hình: giá trị sai khác âm ($\text{difference} < 0$) cho thấy mô hình nhìn chung đánh giá cao hơn thực tế (overestimates), trong khi giá trị sai khác dương ($\text{difference} > 0$) cho thấy mô hình đánh giá thấp hơn thực tế (underestimates) so với phép đo.
- Tiêu chí đánh giá tính nhất quán tốt (good consistency) giữa hai phương pháp (Li et al., 2022):
  - Các giới hạn phù hợp (limits of agreement) không vượt quá phạm vi giá trị có thể chấp nhận được về mặt chuyên môn (professionally acceptable value range).
  - Có $95\%$ các điểm sai khác nằm trong các giới hạn phù hợp $95\%$ ($95\%$ limits of agreement).
  - Giới hạn phù hợp $95\%$ ($95\%$ limits of agreement) được xác định bằng cách cộng và trừ $1.96$ lần độ lệch chuẩn (standard deviations) vào giá trị sai khác trung bình (mean difference):
    $$\text{limits of agreement } 95\% = \text{mean difference} \pm 1.96 \times \text{standard deviation}$$
