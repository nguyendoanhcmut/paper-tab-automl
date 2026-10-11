## 3. Models development

- Phân loại toàn bộ thông số đầu vào thành hai nhóm: đặc tính dòng vào (influent characteristics) và điều kiện vận hành (operating conditions).
  - Tập dữ liệu được phân chia thành ba kịch bản (scenarios):
    - Kịch bản thứ nhất ($M_1, M_2, M_3$) xem xét các điều kiện vận hành.
    - Kịch bản thứ hai ($M_4, M_5, M_6$) xem xét các thông số đầu vào.
    - Kịch bản thứ ba ($M_7, M_8, M_9$) xem xét đồng thời điều kiện vận hành cùng với đặc tính dòng vào (xem Hình 2).
  - Trong mỗi kịch bản, ba mô hình được phát triển cho cả $\text{XGBoost}$ và $\text{MLP}$ để dự đoán từng chỉ tiêu loại bỏ chất dinh dưỡng ($\text{NH}_4$, $\text{TN}$, $\text{TP}$).
  - Hiệu suất của các mô hình được so sánh tập trung vào các thông số đầu vào nhằm xác định mô hình tối ưu.
  - Một kịch bản bị loại bỏ trong mỗi lượt đánh giá nhằm xác định mô hình kinh tế nhất (most economical model).
- Mục đích phân chia tập dữ liệu đầu vào thành các kịch bản là để khảo sát tầm quan trọng của các đặc trưng được lựa chọn (selected features) đối với hiệu quả loại bỏ dinh dưỡng khỏi nước thải.
  - Sơ đồ khung của hai mô hình đề xuất ($\text{XGBoost}$ và $\text{MLP}$) được thể hiện tại Hình 3.
  - Số lượng biến đầu vào quy định từng kịch bản: kịch bản thứ nhất gồm $3$ đầu vào cho mỗi mô hình; kịch bản thứ hai gồm $6$ đầu vào; kịch bản thứ ba gồm $9$ đầu vào.
  - Biến đầu ra tập trung vào hiệu suất loại bỏ chất dinh dưỡng được bố trí dưới dạng một nút đơn (single node) ở tầng đầu ra.

### 3.1. Development of XGBoost model

- Môi trường và thư viện phát triển mô hình $\text{XGBoost}$:
  - Phần mềm Python phiên bản 3.9 (2021-06-05) được sử dụng để xây dựng mô hình $\text{XGBoost}$.
  - Thư viện `sklearn` được sử dụng để phân chia dữ liệu thành tập huấn luyện (training dataset) và tập kiểm tra (testing dataset) thông qua hàm `train_test_split` và các hàm phân chia tập con (subset functions).
  - Tập dữ liệu lớn được phân chia ngẫu nhiên thành $90\%$ cho huấn luyện và $10\%$ cho kiểm tra.
- Tinh chỉnh siêu tham số (hyperparameter tuning) mô hình $\text{XGBoost}$:
  - Tinh chỉnh siêu tham số là bước then chốt trong phát triển mô hình, với các kỹ thuật tiềm năng như Grid Search, Random Search hoặc Bayes Search để tìm thông số tối ưu.
  - Kỹ thuật `GridSearch` được lựa chọn dựa trên tài liệu tham khảo do số lượng tổ hợp thông số khảo sát trong nghiên cứu ở mức giới hạn.
  - Phương pháp `GridSearch` được áp dụng với tham số `n_estimators` trong khoảng $10\text{–}1000$ để thu được bộ siêu tham số tối ưu cho mô hình $\text{XGBoost}$.
- Bộ tham số cấu hình của mô hình $\text{XGBoost}$:
  - `base_score` = $0.1$.
  - `booster` = 'gbtree'.
  - `colsample_bylevel` = $1$, `colsample_bynode` = $1$, `colsample_bytree` = $1$.
  - `gamma` = $0$.
  - `gpu_id` = $-1$.
  - `importance_type` = 'gain'.
  - `interaction_constraints` = ''.
  - `learning_rate` = $0.001$.
  - `max_delta_step` = $0$.
  - `max_depth` = $9$.
  - `min_child_weight` = $1$.
  - `monotone_constraints` = '()'.
  - `n_estimators` = $1000$.
  - `n_jobs` = $4$.
  - `num_parallel_tree` = $2$.
  - `random_state` = $5$.
  - `reg_alpha` = $0$, `reg_lambda` = $1$.
  - `scale_pos_weight` = $1$.
  - `subsample` = $1$.
  - `tree_method` = 'exact'.
  - `validate_parameters` = $1$.
  - `verbosity` = $0$.
  - Hàm kích hoạt (activation function) là hàm sigmoid do tập dữ liệu biến thiên trong khoảng giữa $0$ và $1$.
- Các siêu tham số được tinh chỉnh bằng Grid Search kết hợp với mô hình $\text{XGBoost}$ nhằm đạt sai số nhỏ nhất, với các giá trị tối ưu được đưa vào xây dựng mô hình để kiểm soát phần dư dự đoán qua các kịch bản:
  - Phân bố phần dư (residual) trên tập kiểm tra của các mô hình $\text{XGBoost}$ phản ánh mức độ hội tụ sai số theo từng kịch bản:
    - **Hình 5.** Biểu đồ phần dư của các mô hình XGBoost
      - <img src="assets/fig_05_p5_vector.png" alt="Hình 5" />
      - **Hình này chứng minh điều gì**
        - Phần dư của $M_7$ gom sát nhất quanh trục $0$ trong dải $[-10, 10]$, ít điểm dị biệt hơn rõ rệt so với $M_1$ và $M_4$.
      - **Từ đâu mà thấy được**
        - Ox: tập dữ liệu kiểm tra (Testing dataset), dải $0$–$800$. Oy: sai số phần dư (Residual), đường đỏ là vạch $0$.
        - Đồ thị (a) ($\text{NH}_4$): ký hiệu tam giác $M_7$ nén chặt trong dải $[-10, 10]$ (hai đường nét đứt xanh), đối xứng qua trục $0$.
        - Đồ thị (b) ($\text{TN}$) và (c) ($\text{TP}$): sai số phân tán rộng vượt xa hai biên xanh $\pm 25$, trong đó $\text{TP}$ rơi sâu đến $-70$.

### 3.2. Development of MLP model

- Môi trường và cấu trúc mạng của mô hình $\text{MLP}$:
  - Phần mềm Python phiên bản 3.9 (2021-06-05) được sử dụng để phát triển mô hình $\text{MLP}$.
  - Mô hình $\text{MLP}$ được xây dựng bằng cách nhập các thư viện: `sklearn.preprocessing` để chuẩn hóa dữ liệu, `sklearn.model_selection` với hàm `train_test_split`, và `sklearn.neural_network` với lớp `MLPRegressor`.
  - Tập dữ liệu lớn được phân chia ngẫu nhiên thành $90\%$ cho huấn luyện và $10\%$ cho kiểm tra.
  - Dữ liệu đầu vào được đưa vào mô hình với $1$ tầng ẩn (one hidden layer).
  - Số lượng nơ-ron khác nhau trong tầng ẩn được thử nghiệm cho từng kịch bản.
  - Hàm kích hoạt tuyến tính chỉnh lưu (ReLU / rectified linear activation function) được lựa chọn nhằm khắc phục hiện tượng triệt tiêu gradient (vanishing gradient problem), giúp mô hình học nhanh hơn và hoạt động tốt hơn; đây cũng là hàm kích hoạt mặc định khi phát triển các mô hình $\text{MLP}$.
- Quy trình tinh chỉnh siêu tham số mô hình $\text{MLP}$:
  - Việc tinh chỉnh siêu tham số mô hình $\text{MLP}$ được thực hiện chủ yếu bằng phương pháp thử và sai (trial-and-error method) để xác định các siêu tham số quan trọng gồm: tốc độ học (learning rate), số nơ-ron trong tầng ẩn, trạng thái ngẫu nhiên (random state) và số vòng lặp (iterations).
  - Trạng thái ngẫu nhiên (`random_state`) được áp dụng để tái lập tập dữ liệu đồng nhất qua các lần chạy, với số giả ngẫu nhiên được sinh ngẫu nhiên.
  - Tốc độ học (`learning_rate`) là siêu tham số then chốt điều tiết mức độ biến đổi phản ứng của mô hình dựa trên sai số phát sinh và hỗ trợ điều chỉnh trọng số của mô hình.
- Bộ siêu tham số then chốt được tinh chỉnh cho từng kịch bản mô hình bằng cách thay đổi giá trị nhằm đạt kết quả dự đoán tốt nhất:
  - `hidden_layer_sizes` = $(4\text{–}30)$.
  - `activation` = 'ReLU'.
  - `solver` = 'lbfgs'.
  - `alpha` = $(0.01\text{–}0.000001)$.
  - `random_state` = $(3\text{–}19)$.
  - `max_iter` = $(100\text{–}100)$.
  - `warm_start` = True.
- Kiểm tra hiệu suất mô hình $\text{MLP}$ trên tập dữ liệu kiểm tra:
  - Hiệu suất mô hình được kiểm tra thông qua việc vẽ biểu đồ phần dư và xác định các giá trị $R^2$ cùng các chỉ số hiệu suất thống kê trên tập dữ liệu kiểm tra:
    - **Bảng 3.** Hiệu suất thống kê của mô hình MLP trên tập kiểm tra
      - <img src="assets/table_03_p5.png" alt="Bảng 3" />
      - **Bảng này chứng minh điều gì**
        - Mô hình M4 đạt $R^2$ cao nhất ($0.787$), M3 thấp nhất ($0.182$), sai số $\text{RMSE}$ dao động từ $0.00031$ (M1) đến $0.07707$ (M8).
      - **Từ đâu mà thấy được**
        - Cột $R^2$: hàng M4 đạt giá trị cao nhất ($0.787$), hàng M3 thấp nhất ($0.182$).
        - Cột $\text{RMSE}$ và $\text{MAE}$: hàng M1 thấp nhất ($0.00031$ và $0.00063$), hàng M8 cao nhất ($0.07707$ và $0.00988$).
  - Mối tương quan giữa giá trị thực tế và giá trị do mô hình dự đoán được kiểm tra trên đồ thị phân tán (scatter plots) cho các kịch bản khác nhau:
    - **Hình 6.** Đồ thị phân tán thực tế và dự đoán mô hình MLP
      - <img src="assets/fig_06_p6.jpeg" alt="Hình 6" />
      - **Hình này chứng minh điều gì**
        - Mô hình $M_4$ bám sát thực tế tốt nhất ($>78\%$), trong khi việc tích hợp toàn bộ thông số ở $M_7$–$M_9$ không cải thiện được độ phân tán của MLP.
      - **Từ đâu mà thấy được**
        - Ox: giá trị thực tế (Actual), dải đo $0$–$100$. Oy: giá trị dự đoán (Predicted), dải đo $30$–$105$.
        - Cột $\text{NH}_4$ ($M_1, M_4, M_7$): dữ liệu gom sát đường hồi quy đỏ (chặt nhất ở $M_4$); hai cột $\text{TN}$ ($M_2, M_5, M_8$) và $\text{TP}$ ($M_3, M_6, M_9$) phân tán rộng thành đám mây ngang.

### 3.3. Model performance matrices

- Hiệu suất của các mô hình dự đoán đã phát triển được đánh giá dựa trên các thước đo thống kê:
  - Căn bậc hai sai số toàn phương trung bình ($\text{RMSE}$ / root mean squared error).
  - Phần trăm sai số tuyệt đối trung bình ($\text{MAPE}$ / mean absolute percentage error).
  - Sai số tuyệt đối trung bình ($\text{MAE}$ / mean absolute error).
  - Hệ số xác định ($R^2$ / coefficient of determination).
  - Chỉ số thống nhất cải tiến ($m_d$ / modified index of agreement).
- Các ma trận hiệu suất được tính toán theo các phương trình từ $(4)$ đến $(8)$:
  - Sai số tuyệt đối trung bình ($\text{MAE}$):
    $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} [p_i - y_i] \quad (4)$$
  - Căn bậc hai sai số toàn phương trung bình ($\text{RMSE}$):
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} [p_i - y_i]^2} \quad (5)$$
  - Phần trăm sai số tuyệt đối trung bình ($\text{MAPE}$):
    $$\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left[ \frac{p_i - y_i}{y_i} \right] \quad (6)$$
  - Hệ số xác định ($R^2$):
    $$R^2 = 1 - \frac{\sum (p_i - y_i)^2}{\sum (p_i - u_a)^2} \quad (7)$$
  - Chỉ số thống nhất cải tiến ($m_d$):
    $$m_d = 1 - \frac{\sum_{i=1}^{n} [y_i - p_i]}{\sum_{i=1}^{n} [p_i - \bar{y}] + [y_i - \bar{y}]} \quad (8)$$
- Ký hiệu và định nghĩa các biến trong các phương trình hiệu suất:
  - $n$: biểu thị tổng số mẫu dữ liệu (total number of datasets).
  - $y_i$: biểu thị giá trị thực tế (actual values).
  - $p_i$: biểu thị giá trị dự đoán (predicted values).
  - $u_a$: giá trị trung bình của các giá trị dự đoán $p_i$ (mean of $p_i$ values).
  - $\bar{y}$: giá trị trung bình của các giá trị thực tế (average of the actual values).
  - $i$: số thứ tự quan sát (number of observations).
