## 4 Tutorial example

### 4.1 Method

- Mạng nơ-ron lan truyền ngược (BPNN - Back Propagation Neural Network), máy vector hỗ trợ (SVM - Support Vector Machine) và rừng ngẫu nhiên (RF - Random Forest) đã nổi lên như các mô hình học máy phổ biến (prevalent machine learning models):
  - Các mô hình BP và SVM được ứng dụng rộng rãi nhất trong hệ thống bể phản ứng sinh học màng (MBR - Membrane Bioreactor).
  - Thuật toán di truyền (GA - Genetic Algorithm) là thuật toán chiếm ưu thế nhất được sử dụng cho tối ưu hóa mô hình (model optimization).
- Việc đưa cơ chế bộ nhớ ngắn-dài hạn vào LSTM (Long Short-Term Memory, một biến thể của mạng nơ-ron hồi quy - RNN, Recurrent Neural Network) đã thể hiện tiềm năng rõ rệt trong việc giải quyết các bài toán phụ thuộc thời gian (time issues).
- Dự đoán thời gian thực (real-time prediction) về hiện tượng tắc nghẽn màng (membrane fouling) đóng vai trò then chốt do bản chất hình thành tắc nghẽn phức tạp hơn nhiều so với quá trình loại bỏ chất ô nhiễm (pollutant removal):
  - Dự đoán đòi hỏi phải nắm bắt các tương tác động học và nhạy cảm theo thời gian (dynamic and time-sensitive interactions) giữa các chất gây tắc nghẽn (foulants) và màng lọc (membranes).
- Bài hướng dẫn (tutorial) này áp dụng 5 phương pháp học máy điển hình (SVM, RF, BPNN, LSTM và GA-BP) để dự đoán hiện tượng tắc nghẽn màng trong các hệ thống MBR:
  - Một tập dữ liệu ảo (virtual data set; tham khảo bảng dữ liệu tại S Appendix B) được tạo ra phục vụ cho việc thực hành học máy.
  - Quy trình thực hành và tính toán được thực hiện trên nền tảng phần mềm MATLAB.

#### 4.1.1 Data preprocessing

- Bước đầu tiên trong quy trình là xác định các biến độc lập (independent variables - đóng vai trò các đặc trưng đầu vào / input characteristics) và các biến phụ thuộc (dependent variables - đóng vai trò các đặc trưng đầu ra / output characteristics) từ tập dữ liệu thô (raw data set).
- Áp suất xuyên màng (TMP - Transmembrane Pressure) được lựa chọn làm đại lượng đầu ra mục tiêu (target output) nhằm đặc trưng hóa trạng thái tắc nghẽn của màng (fouling state).
- Các yếu tố ảnh hưởng quan trọng tiềm năng đối với quá trình tắc nghẽn màng được lựa chọn làm các đặc trưng đầu vào, dựa trên cơ sở hiểu biết chung và các khảo sát sơ bộ:
  - Các biến đầu vào được lựa chọn bao gồm nhiệt độ ($T$ - temperature), chất rắn lơ lửng trong bùn lỏng (MLSS - Mixed Liquor Suspended Solids), $pH$, oxy hòa tan (DO - Dissolved Oxygen) trong vùng hiếu khí (aerobic zone), chất lượng nước đầu vào (influent water quality) gồm nhu cầu oxy hóa học (COD - Chemical Oxygen Demand), tổng nitơ (TN - Total Nitrogen), tổng phospho (TP - Total Phosphorus), và thông lượng màng (membrane flux).
- Hàm `mapminmax` trong MATLAB được áp dụng để chuẩn hóa (normalize) dữ liệu đầu vào và đầu ra về khoảng $[0, 1]$:
  - Quá trình chuẩn hóa nhằm loại bỏ các tác động tiêu cực do dữ liệu kỳ dị (singular data) gây ra và đẩy nhanh tốc độ hội tụ (expedite convergence).
- Dữ liệu mẫu được phân chia ngẫu nhiên thành hai tập con:
  - $70\%$ dữ liệu mẫu được chọn ngẫu nhiên làm tập huấn luyện (training set).
  - $30\%$ dữ liệu mẫu còn lại được dùng làm tập kiểm thử (test set).

#### 4.1.2 Selection of model and policy

- Phần mềm MATLAB được sử dụng để xây dựng mô hình và lập trình tính toán (xem mã nguồn mẫu tại Appendix C).
- Đối với mô hình SVM, bộ công cụ LibSVM được áp dụng cho bài toán dự đoán hồi quy (regression prediction), trong đó hàm nhân cơ sở hướng kính (RBF kernel - Radial Basis Function) được lựa chọn làm hàm hạt nhân (kernel function):
  - Tham số $C$ (hệ số phạt - penalty coefficient, đại diện cho mức dung sai đối với sai số / tolerance for error) và tham số $G$ được tối ưu hóa thông qua kiểm định chéo (CV - Cross-Validation).
  - Tham số $G$ của hàm nhân RBF được tính theo công thức:
    $$G = \frac{1}{2\sigma_{\text{RBF}}^2}$$
  - Tham số $G$ xác định một cách ẩn định phân bố của dữ liệu khi được ánh xạ vào không gian đặc trưng mới (new feature space).
- Để xây dựng các mô hình BPNN, LSTM và RF, hộp công cụ mạng nơ-ron (neural network toolbox) và hộp công cụ rừng ngẫu nhiên (random forest toolbox) được lựa chọn từ các gói thư viện của MATLAB:
  - Thuật toán huấn luyện lan truyền ngược (backpropagation training algorithm) được áp dụng để phát triển mô hình mạng nơ-ron.
- Mô hình GA-BP được thiết lập dưới dạng mô hình lai ghép (hybrid model) kết hợp giữa thuật toán GA và thuật toán BPNN:
  - Mô hình vận hành theo quy trình ba bước gồm chọn lọc (selection), lai ghép (crossover) và đột biến (mutation).
  - Quy trình này nhằm tối ưu hóa toàn cục (globally optimize) trọng số (weight) và độ lệch (bias) của mạng nơ-ron.

#### 4.1.3 Model evaluation

- Độ tin cậy (reliability) và độ chính xác (accuracy) của từng mô hình được đánh giá thông qua ba thông số thống kê (statistical parameters):
  - Hệ số xác định ($R^2$ - Coefficient of Determination).
  - Căn bậc hai sai số bình phương trung bình (RMSE - Root Mean Square Error).
  - Sai số phần trăm tuyệt đối trung bình (MAPE - Mean Absolute Percentage Error).
- Tiêu chí đánh giá chất lượng mô hình:
  - Giá trị MAPE và RMSE càng tiến gần về $0$ (hoặc $R^2$ càng tiến gần về $1$) cho thấy dự đoán càng chính xác và hiệu năng của mô hình càng tốt.

### 4.2 Results and discussion

#### 4.2.1 Presentation of raw data

- Bảng S5 (Table S5) trình bày giá trị trung bình (mean), độ lệch chuẩn (standard deviation), cùng các giá trị cực đại (maximum) và cực tiểu (minimum) của dữ liệu đầu vào và đầu ra.
- Các biến đầu vào (input variables) gồm có nhiệt độ ($T$), MLSS, $pH$, DO vùng hiếu khí (aerobic-zone DO), COD đầu vào, TN đầu vào, TP đầu vào và thông lượng màng (flux).
- Biến đầu ra (output variable) là áp suất xuyên màng (TMP):
  - Các mô hình học máy thiết lập mối quan hệ ánh xạ (mapping relationship) giữa các biến đầu vào và biến đầu ra để dự đoán hiện tượng tắc nghẽn màng.
- Tập dữ liệu thô (raw data set) bao gồm $2000$ mẫu:
  - $70\%$ số mẫu ($1400$ mẫu) được chọn ngẫu nhiên cho tập huấn luyện (training).
  - $30\%$ số mẫu còn lại ($600$ mẫu) được dành cho tập kiểm thử (testing).

#### 4.2.2 Model performance

- Tập hợp các tham số mô hình được trình bày chi tiết tại Phần 1 của Phụ lục A (Section 1 of Appendix A).
- Bảng 3 (Table 3) so sánh kết quả dự đoán của năm phương pháp SVM, RF, BPNN, LSTM và GA-BP:

Table 3: Hiệu năng của các mô hình học máy khác nhau đối với ví dụ hướng dẫn (Performance of different machine learning models for the tutorial example).

| Thông số thống kê (Metric) | Tập dữ liệu (Dataset) | SVM | RF | BPNN | LSTM | GA-BP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $R^2$ | Training | $0.8208$ | $0.9017$ | $0.8199$ | $0.8206$ | $0.8201$ |
| | Testing | $0.8124$ | $0.7344$ | $0.8096$ | $0.8175$ | $0.8128$ |
| | All Data | $0.8184$ | $0.8537$ | $0.8170$ | $0.8197$ | $0.8180$ |
| RMSE | Training | $1.4075$ | $1.0424$ | $1.4107$ | $1.4080$ | $1.4100$ |
| | Testing | $1.3955$ | $1.6605$ | $1.4058$ | $1.3765$ | $1.3940$ |
| | All Data | $1.4039$ | $1.2601$ | $1.4092$ | $1.3987$ | $1.4052$ |
| MAPE | Training | $0.0616$ | $0.0463$ | $0.0629$ | $0.0630$ | $0.0628$ |
| | Testing | $0.0624$ | $0.0737$ | $0.0636$ | $0.0619$ | $0.0625$ |
| | All Data | $0.0618$ | $0.0545$ | $0.0631$ | $0.0626$ | $0.0627$ |

- Cả năm mô hình đều thể hiện khả năng khớp dữ liệu tốt (good fitting ability) trên tập dữ liệu hoàn chỉnh (All Data, với $R^2$ dao động từ $0.8170$ đến $0.8537$).
- Bốn mô hình SVM, BPNN, LSTM và GA-BP đạt hiệu năng tương đồng giữa tập huấn luyện và tập kiểm thử:
  - SVM đạt $R^2 = 0.8208$ (huấn luyện) và $0.8124$ (kiểm thử); $\text{RMSE} = 1.4075$ và $1.3955$; $\text{MAPE} = 0.0616$ và $0.0624$.
  - BPNN đạt $R^2 = 0.8199$ (huấn luyện) và $0.8096$ (kiểm thử); $\text{RMSE} = 1.4107$ và $1.4058$; $\text{MAPE} = 0.0629$ và $0.0636$.
  - LSTM đạt $R^2 = 0.8206$ (huấn luyện) và $0.8175$ (kiểm thử); $\text{RMSE} = 1.4080$ và $1.3765$; $\text{MAPE} = 0.0630$ và $0.0619$.
  - GA-BP đạt $R^2 = 0.8201$ (huấn luyện) và $0.8128$ (kiểm thử); $\text{RMSE} = 1.4100$ và $1.3940$; $\text{MAPE} = 0.0628$ và $0.0625$.
- Mô hình RF thể hiện khả năng khớp dữ liệu tốt trên tập huấn luyện nhưng có khả năng dự đoán tổng quát hóa yếu hơn (weaker generalized predictability):
  - Trên tập huấn luyện, RF đạt $R^2 = 0.9017$, $\text{RMSE} = 1.0424$ và $\text{MAPE} = 0.0463$.
  - Trên tập kiểm thử, hiệu năng dự đoán của RF giảm xuống với $R^2 = 0.7344$, $\text{RMSE} = 1.6605$ và $\text{MAPE} = 0.0737$.
  - Dù RF không mắc phải vấn đề quá khớp (overfitting) (Peter et al., 1998), sự thiếu hụt khả năng tổng quát hóa có thể bắt nguồn từ mối tương quan và tính dư thừa giữa các biến độc lập sinh ra do việc chọn ngẫu nhiên các đặc trưng (Wu et al., 2012).
  - Khả năng tổng quát hóa của RF có thể được cải thiện bằng cách tăng số lượng cây (increasing the number of trees), thực hiện lựa chọn đặc trưng (feature selection) và tối ưu hóa thuật toán cắt tỉa cây (optimizing the pruning algorithm) (Yang et al., 2012).
- Mô hình LSTM thể hiện khả năng dự đoán nhỉnh hơn một chút (slightly better predictive ability) so với BPNN:
  - Trên tập kiểm thử, LSTM đạt $R^2 = 0.8175$ (so với $0.8096$ của BPNN), $\text{RMSE} = 1.3765$ (so với $1.4058$) và $\text{MAPE} = 0.0619$ (so với $0.0636$).
- Mô hình GA-BP cải thiện kết quả dự đoán so với mô hình BPNN:
  - Trên tập kiểm thử, GA-BP đạt $R^2 = 0.8128$ (so với $0.8096$ của BPNN), $\text{RMSE} = 1.3940$ (so với $1.4058$) và $\text{MAPE} = 0.0625$ (so với $0.0636$).
