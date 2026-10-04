## 2.4. Models

- Hai nhóm mô hình bao gồm các mô hình hồi quy thống kê (statistical regression models) và các mô hình học máy (machine learning models) được áp dụng nhằm xây dựng các mô hình dự đoán hiện tượng nghẹt màng (membrane fouling):
  - Các mô hình thống kê nhằm nắm bắt các mối quan hệ tuyến tính (linear relationships) giữa các đặc trưng đầu vào (input features) và các thông số mục tiêu (target parameters).
  - Các mô hình học máy khai thác các quy luật phi tuyến (non-linear patterns) để nâng cao độ chính xác dự đoán (predictive accuracy).

### 2.4.1. Statistical Models

- Hồi quy tuyến tính (Linear Regression) là phương pháp thống kê cơ bản được sử dụng để mô hình hóa mối quan hệ giữa biến phụ thuộc $Y$ và nhiều biến độc lập $X_i$:
  - Mô hình được biểu diễn theo Equation (3):
    $$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon \tag{3}$$
  - $\beta_0$: hệ số chặn (intercept).
  - $\beta_1$ đến $\beta_p$: các hệ số hồi quy (regression coefficients).
  - $\epsilon$: số hạng sai số (error term).
  - Mô hình giả định mối quan hệ tuyến tính giữa các biến dự đoán (predictors) và các thông số mục tiêu (target parameters).
- Hồi quy Lasso (Least Absolute Shrinkage and Selection Operator - Lasso regression) bổ sung số hạng điều chuẩn $L_1$ vào mô hình hồi quy tuyến tính, thực hiện lựa chọn đặc trưng (feature selection) hiệu quả bằng cách phạt độ lớn tuyệt đối của các hệ số hồi quy:
  - Hàm mục tiêu (objective function) được xác định theo Equation (4):
    $$\min_{\beta} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p |\beta_j| \tag{4}$$
  - $\lambda$: siêu tham số (hyperparameter) kiểm soát cường độ điều chuẩn (regularization strength).
  - $y_i$: giá trị thực tế của biến mục tiêu tại quan sát thứ $i$.
  - $x_{ij}$: giá trị của đặc trưng thứ $j$ tại quan sát thứ $i$.
  - $\beta_0$: hệ số chặn và $\beta_j$: hệ số hồi quy tương ứng với đặc trưng thứ $j$.
  - Hồi quy Lasso giúp giảm thiểu hiện tượng quá khớp (mitigate overfitting) bằng cách thu hẹp một số hệ số hồi quy về đúng bằng $0$ (shrinking some coefficients to zero), qua đó chỉ lựa chọn các đặc trưng quan trọng nhất (most relevant features).
- Hồi quy Ridge (Ridge regression) mở rộng hồi quy tuyến tính bằng cách tích hợp số hạng điều chuẩn $L_2$, thực hiện phạt các hệ số hồi quy có giá trị lớn và giảm phương sai mô hình (model variance):
  - Hàm mục tiêu được xác định theo Equation (5):
    $$\min_{\beta} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2 \tag{5}$$
  - $\lambda$: siêu tham số kiểm soát cường độ điều chuẩn.
  - $\beta_j^2$: bình phương của hệ số hồi quy $\beta_j$, cấu thành số hạng phạt theo chuẩn $L_2$.
  - Hồi quy Ridge đặc biệt hữu ích trong việc xử lý các vấn đề đa cộng tuyến (multicollinearity issues), bảo đảm độ ổn định của mô hình (model stability) và cải thiện khả năng khái quát hóa (generalization).
- Hồi quy Elastic Net (Elastic Net regression) kết hợp các kỹ thuật điều chuẩn $L_1$ (Lasso) và $L_2$ (Ridge), tận dụng ưu điểm của cả hai phương pháp:
  - Hàm mục tiêu được thiết lập theo Equation (6):
    $$\min_{\beta} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \left[ \alpha \sum_{j=1}^p |\beta_j| + \frac{1 - \alpha}{2} \sum_{j=1}^p \beta_j^2 \right] \tag{6}$$
  - $\alpha$: kiểm soát sự cân bằng giữa số hạng phạt $L_1$ và $L_2$.
  - $\lambda$: xác định cường độ điều chuẩn tổng thể.
  - Mô hình đặc biệt hiệu quả khi làm việc với các tập dữ liệu nhiều chiều (high-dimensional datasets) chứa các đặc trưng tương quan với nhau (correlated features).

### 2.4.2. Machine Learning Models

- Mô hình học máy (Machine Learning - ML) áp dụng trong nghiên cứu tuân theo quy trình làm việc đa giai đoạn có hệ thống (systematic multi-stage workflow) nhằm bảo đảm cả độ chính xác dự đoán (predictive accuracy) lẫn khả năng diễn giải (interpretability):
  - Đầu vào (Input): Các đặc trưng đã qua tiền xử lý, bao gồm các biến như tỷ số $\text{F/M}$, nồng độ $\text{MLSS}$ và các giá trị trung bình trượt của các thông số vận hành (moving averages of operational parameters), được đưa vào thuật toán.
  - Huấn luyện (Training): Thuật toán xây dựng lặp đi lặp lại các cây quyết định (decision trees), tối ưu hóa để đạt sai số dự đoán tối thiểu (minimal prediction error) đồng thời phạt hiện tượng quá khớp (penalizing overfitting).
  - Đầu ra (Output): Các dự đoán về thông lượng riêng ($\text{Spec. Flux} = \text{flux}/\text{TMP}$) được tạo ra, trực tiếp định lượng mức độ nghiêm trọng của hiện tượng nghẹt màng (fouling severity).
  - Khả năng diễn giải (Interpretation): Các giá trị Shapley Additive Explanation ($\text{SHAP}$) định lượng mức độ đóng góp của từng biến số đầu vào vào kết quả dự đoán, cho phép người vận hành xác định các đòn bẩy khả thi để can thiệp (actionable levers, ví dụ điều chỉnh nồng độ $\text{MLSS}$).
- Các chiến lược then chốt nhằm ngăn ngừa hiện tượng quá khớp (preventing overfitting) trong quy trình mô hình hóa dự đoán:
  - Kiểm định chéo (Cross-validation): Kiểm định chéo $5$ phần ($5\text{-fold cross-validation}$) được sử dụng trong quá trình tinh chỉnh siêu tham số (hyperparameter tuning) nhằm bảo đảm ước lượng hiệu năng có độ tin cậy và bền vững (robust performance estimation), đặc biệt quan trọng đối với các tập dữ liệu quy mô nhỏ (small datasets).
  - Dừng sớm (Early stopping): Đối với CatBoost và XGBoost, kỹ thuật dừng sớm dựa trên mất mát trên tập kiểm định (validation loss) được áp dụng để ngừng quá trình huấn luyện khi hiệu năng không còn cải thiện.
  - Tinh chỉnh siêu tham số (Hyperparameter tuning): Tìm kiếm theo lưới (Grid search) được áp dụng để tối ưu hóa các tham số mô hình như độ sâu của cây (tree depth), tốc độ học (learning rate) và các số hạng điều chuẩn (regularization terms).
  - Kiểm soát độ phức tạp của mô hình (Model complexity control): Giới hạn độ sâu tối đa của cây (maximum tree depth) và trọng số nút con tối thiểu (minimum child weight) để tránh việc mô hình khớp quá mức với các quy luật phức tạp trong điều kiện dữ liệu hạn chế.
- Thuật toán eXtreme Gradient Boosting ($\text{XGBoost}$) là thuật toán tăng cường dựa trên cây (tree-based boosting algorithm) được tối ưu hóa cho tính toán song song (parallel computation) và nâng cao hiệu quả mô hình:
  - Hàm mục tiêu được biểu diễn theo Equation (7):
    $$\sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t)}\right) + \sum_{k=1}^K \left( \gamma T + \frac{1}{2} \lambda \|\omega\|^2 \right) \tag{7}$$
  - $y_i$: giá trị thực tế (true values).
  - $\hat{y}_i^{(t)}$: giá trị dự đoán tại vòng lặp thứ $t$ (predicted values at iteration $t$).
  - $l\left(y_i, \hat{y}_i^{(t)}\right)$: hàm mất mát (loss function) đo lường độ chênh lệch dự đoán.
  - $T$: số lượng nút lá (number of leaf nodes) của cây.
  - $\omega$: véc-tơ trọng số của các nút lá (weights of leaf nodes).
  - $\gamma$ và $\lambda$: các siêu tham số kiểm soát độ phức tạp của mô hình (model complexity) và mức độ điều chuẩn (regularization).
- Thuật toán Category Boosting ($\text{CatBoost}$) là thuật toán tăng cường độ dốc (gradient-boosting algorithm) do Yandex phát triển, được thiết kế nhằm xử lý hiệu quả các đặc trưng phân loại (categorical features) và giảm thiểu hiện tượng dịch chuyển dự đoán (prediction shift) thông qua kỹ thuật tăng cường theo thứ tự (ordered boosting):
  - Hàm mục tiêu được xác định theo Equation (8):
    $$\sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t)}\right) + \sum_{k=1}^K \left( \gamma T + \frac{1}{2} \lambda \|\omega\|^2 \right) + R_{\text{ordered}}(D) \tag{8}$$
  - $R_{\text{ordered}}(D)$: số hạng điều chuẩn bổ sung được đưa vào thông qua phương pháp ordered boosting trên tập dữ liệu $D$, giải quyết triệt để vấn đề độ chệch ước lượng độ dốc (gradient estimation bias).
  - Các số hạng còn lại kế thừa từ hàm mục tiêu của mô hình boosting cây, bao gồm hàm mất mát tổng hợp $l\left(y_i, \hat{y}_i^{(t)}\right)$, số lượng nút lá $T$ và trọng số các nút lá $\omega$ chịu sự điều chuẩn của các siêu tham số $\gamma$ và $\lambda$.
