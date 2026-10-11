#### 2.3.5. Performance evaluation

- Đánh giá hiệu năng phát triển mô hình mạng nơ-ron nhân tạo (ANN model development) được đo lường bằng sai số toàn phương trung bình (MSE - Mean Squared Error), căn bậc hai sai số toàn phương trung bình (RMSE - Root Mean Squared Error), hệ số tương quan (correlation coefficient, $R$), và hệ số xác định (determination coefficient, $R^2$), theo các Phương trình $(11)$–$(14)$ (Nourbakhsh et al. 2014; Jawad et al. 2021):
  - Sai số toàn phương trung bình ($\text{MSE}$):
    $$\text{MSE} = \frac{1}{N} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2 \quad (11)$$
  - Căn bậc hai sai số toàn phương trung bình ($\text{RMSE}$):
    $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \quad (12)$$
  - Hệ số tương quan ($R$):
    $$R = \frac{\sum_{i=1}^{n} (y_i - \bar{y})(\hat{y}_i - \bar{\hat{y}})}{\sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2 \sum_{i=1}^{n} (\hat{y}_i - \bar{\hat{y}})^2}} \quad (13)$$
  - Hệ số xác định ($R^2$):
    $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \quad (14)$$
- Ý nghĩa các biến số trong các công thức đánh giá:
  - $y_i$ và $\hat{y}_i$ lần lượt biểu thị biến độc lập thứ $i$ ($i\text{th}$ independent variable) và biến phụ thuộc thứ $i$ ($i\text{th}$ dependent variable).
  - $\bar{y}$ và $\bar{\hat{y}}$ lần lượt biểu thị giá trị trung bình của các biến độc lập (mean of independent variables) và giá trị trung bình của các biến phụ thuộc (mean of dependent variables).
  - Biến độc lập và biến phụ thuộc lần lượt được đo bằng thông lượng dòng thấm (permeate flux) thực nghiệm và thông lượng dòng thấm dự đoán (predicted permeate flux) của POME.
- Mục đích sử dụng và tiêu chí đánh giá mô hình dự đoán:
  - Hệ số tương quan ($R$) được sử dụng để đánh giá độ mạnh của mối quan hệ giữa các biến đầu vào (bơm rút permeate / permeate pump và áp suất xuyên màng TMP) và đầu ra thông lượng dòng thấm (permeate flux output).
  - Giá trị $\text{MSE}$ (hoặc $\text{RMSE}$) tiến gần $0$, và giá trị $R$ (hoặc $R^2$) tiến gần $1$ chỉ ra độ chính xác cao của mô hình dự đoán (high accuracy of the prediction model) (Ibrahim & Wahab 2022; Idris et al. 2022).
