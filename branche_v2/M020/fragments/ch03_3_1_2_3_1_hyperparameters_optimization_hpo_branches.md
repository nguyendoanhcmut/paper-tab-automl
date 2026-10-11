#### 2.3.1. Hyperparameters optimization (HPO)

* **Quy trình phát triển mô hình tổng thể và tầm quan trọng của siêu tham số**:
  * Quy trình phát triển mô hình dự đoán áp suất xuyên màng ($\text{TMP}$ - transmembrane pressure) được minh họa khái quát trong Hình 2 (Fig. 2):
    * **Hình 2.** Sơ đồ quy trình phát triển và giải thích mô hình TMP.
      * <img src="assets/fig_02_p5.jpeg" alt="Hình 2" />
      * **Hình này chứng minh điều gì**
        * Quy trình 3 giai đoạn nối tiếp: tự động tối ưu siêu tham số (HPO), huấn luyện đối sánh MLP và LSTM và giải thích bằng SHAP.
      * **Từ đâu mà thấy được**
        * Luồng xử lý từ trái sang phải liên kết qua mũi tên xanh: Auto-tuning HPO $\to$ Model building & validation $\to$ Model interpretability Analysis based on SHAP.
        * Khối 1 tối ưu 9 siêu tham số; khối 2 huấn luyện MLP và LSTM dự đoán TMP (đánh giá bằng $R^2$, RMSE); khối 3 phân tích SHAP (Feature importance, Global, Local).
  * Trong tất cả các kỹ thuật học máy (machine learning), các siêu tham số (hyperparameters) đóng vai trò sống còn quyết định trực tiếp đến hiệu suất của mô hình.
  * Các giá trị của siêu tham số phải được xác định và cố định trước khi bắt đầu quá trình học (learning process) (Agarwal et al., 2023).
  * Đối với các mạng nơ-ron nhân tạo (neural networks - NN), siêu tham số bao gồm các thông số cốt lõi như tốc độ học (learning rate), số lượng tầng ẩn (number of layers), số lượng nơ-ron trong từng tầng (number of neurons in each layer), v.v.
  * Siêu tham số tác động sâu sắc đến năng lực học từ dữ liệu và khả năng tổng quát hóa (generalization) của mô hình trên dữ liệu mới chưa từng thấy, cũng như chi phối hiệu suất tổng thể, hiệu quả tính toán và tính thích ứng của mô hình.
  * Việc tinh chỉnh siêu tham số hiệu quả (effectively tuned) là điều kiện thiết yếu hàng đầu trong quy trình xây dựng bất kỳ mô hình học máy nào.

* **Khung tối ưu hóa Optuna và không gian siêu tham số cần tối ưu**:
  * Để đạt được hiệu suất tối ưu, khung tối ưu hóa Optuna (Optuna framework) (Akiba et al., 2019) xây dựng trên nền tảng Python được sử dụng để tối ưu hóa tự động các siêu tham số.
  * Đối với mô hình Perceptron đa lớp (multilayer perceptron - MLP), các siêu tham số được đưa vào tối ưu hóa bao gồm:
    * Số lượng tầng ẩn (number of hidden layers).
    * Số lượng nơ-ron trong các tầng ẩn (number of neurons in the hidden layers).
    * Hàm kích hoạt (activation functions) tại từng tầng ẩn.
    * Thuật toán tối ưu hóa (optimizers) và tốc độ học (learning rate) trong suốt quá trình huấn luyện.
    * Tỷ lệ loại bỏ (dropout rate) cho từng tầng ẩn.
    * Suy giảm trọng số (weight decay) đóng vai trò điều hòa $L_2$ ($L_2$ regularization).
    * Hàm mất mát (loss function).
  * Đối với mô hình Mạng bộ nhớ ngắn-dài hạn (long short-term memory - LSTM): bên cạnh các siêu tham số được tối ưu như MLP, số lượng đơn vị bộ nhớ (number of memory units / LSTM units) được tối ưu bổ sung để nâng cao năng lực học chuỗi thời gian.
  * Bảng 3 (Table 3) trình bày chi tiết các phương án thay thế khả dĩ (available alternatives) và các lựa chọn tối ưu (selected options) cho từng siêu tham số của mô hình MLP và LSTM:
    * **Bảng 3.** Cấu hình siêu tham số cho MLP và LSTM
      * <img src="assets/table_03_p5.png" alt="Bảng 3" />
      * **Bảng này chứng minh điều gì**
        * MLP chọn $4$ lớp ẩn ($222$ neuron, RMSProp), LSTM chọn $3$ lớp ($140$ neuron, $45$ đơn vị LSTM, Adam), và Simple MLP chọn $1$ lớp ($10$ neuron).
        * Cả hai mô hình đều chọn loss MSE, learning rate lần lượt là $0.0001056$ (MLP) và $0.0003677$ (LSTM).
      * **Từ đâu mà thấy được**
        * Hàng "Selected options" đối chiếu với "Available alternatives" ở cột "Models" (MLP, LSTM, Simple MLP).
        * Các cột "Number of hidden layers", "Number of neurons", "Optimizers", "Learning rate" và "Number of LSTM units".
  * Chi tiết không gian tìm kiếm khả dĩ và cấu hình tối ưu được xác định từ Bảng 3:
    * **Mô hình MLP**:
      * Số tầng ẩn: không gian khảo sát $1\text{–}5$ tầng; tùy chọn được chọn là $4$ tầng.
      * Số lượng nơ-ron: không gian khảo sát $8\text{–}256$ nơ-ron; tùy chọn được chọn là $222$ nơ-ron.
      * Hàm kích hoạt: không gian khảo sát gồm ReLU, Sigmoid, Tanh; tùy chọn được chọn từ tầng 1 đến tầng 4 lần lượt là Tanh, Tanh, ReLU, Tanh.
      * Hàm mất mát: không gian khảo sát gồm MSE, MAE, Huber; tùy chọn được chọn là sai số bình phương trung bình ($\text{MSE}$).
      * Bộ tối ưu hóa: không gian khảo sát gồm Adam, AdaDelta, RMSProp; tùy chọn được chọn là $\text{RMSProp}$.
      * Tốc độ học: không gian khảo sát $0.0001\text{–}0.01$; tùy chọn được chọn là $0.0001056$.
      * Tỷ lệ dropout: không gian khảo sát $0.1\text{–}0.5$; tùy chọn được chọn là $0.1410$.
      * Suy giảm trọng số (weight decay): không gian khảo sát $0.000001\text{–}0.1$; tùy chọn được chọn là $0.000001258$.
    * **Mô hình LSTM**:
      * Số tầng ẩn: không gian khảo sát $1\text{–}6$ tầng (bao gồm một tầng LSTM đóng vai trò cố định là tầng ẩn đầu tiên); tùy chọn được chọn là $3$ tầng.
      * Số lượng nơ-ron: không gian khảo sát $8\text{–}256$ nơ-ron; tùy chọn được chọn là $140$ nơ-ron.
      * Hàm kích hoạt: không gian khảo sát gồm ReLU, Sigmoid, Tanh; tùy chọn được chọn lần lượt là ReLU, Tanh, Tanh.
      * Hàm mất mát: không gian khảo sát gồm MSE, MAE, Huber; tùy chọn được chọn là $\text{MSE}$.
      * Bộ tối ưu hóa: không gian khảo sát gồm Adam, AdaDelta, RMSProp; tùy chọn được chọn là $\text{Adam}$.
      * Tốc độ học: không gian khảo sát $0.0001\text{–}0.01$; tùy chọn được chọn là $0.0003677$.
      * Tỷ lệ dropout: không gian khảo sát $0.1\text{–}0.5$; tùy chọn được chọn là $0.1663$.
      * Suy giảm trọng số: không gian khảo sát $0.000001\text{–}0.1$; tùy chọn được chọn là $0.0004726$.
      * Số đơn vị bộ nhớ LSTM: không gian khảo sát $5\text{–}50$ đơn vị; tùy chọn được chọn là $45$ đơn vị.
    * **Mô hình MLP đơn giản đối chứng (Simple MLP)**:
      * Cấu hình lựa chọn gồm $1$ tầng ẩn, $10$ nơ-ron, hàm kích hoạt Tanh, hàm mất mát $\text{MSE}$, bộ tối ưu $\text{RMSProp}$, tốc độ học $0.003987$, suy giảm trọng số $0.0002208$ (không áp dụng dropout).

* **Thuật toán TPE và Hàm mục tiêu tối ưu hóa**:
  * Thuật toán tối ưu hóa mặc định: Optuna triển khai thuật toán Ước lượng Parzen cấu trúc cây (Tree-structured Parzen Estimator - TPE) làm phương pháp mặc định cho HPO.
  * Bản chất kỹ thuật của TPE: TPE là một biến thể tiên tiến của phương pháp tối ưu hóa Bayes (Bayesian optimization technique), cho phép thăm dò hiệu quả không gian tìm kiếm và nhận diện các tổ hợp siêu tham số tiềm năng (J. Li et al., 2022).
  * Tiêu chuẩn đánh giá hiệu suất dự đoán: Hiệu suất dự đoán hồi quy của các mô hình MLP và LSTM được định lượng thông qua hệ số xác định ($R^2$ - coefficient of determination) theo công thức (2):
    $$R^2 = \frac{\sum_i (y_i - p_i)^2}{\sum_i (y_i - m)^2} \qquad (2)$$
    trong đó:
    * $y_i$: giá trị áp suất xuyên màng ($\text{TMP}$) thực tế trong tập kiểm tra (test set).
    * $p_i$: giá trị $\text{TMP}$ được mô hình dự đoán.
    * $m$: giá trị trung bình của các giá trị $\text{TMP}$ thực tế trong tập kiểm tra.
  * Mục tiêu của HPO (Objective of HPO): Quá trình tối ưu hóa siêu tham số nhắm tới việc tối đa hóa hệ số xác định $R^2$ ($\max R^2$) để đạt được độ chính xác dự đoán cao nhất.

* **Cài đặt số chu kỳ huấn luyện (Epochs) và kích thước lô (Batch size)**:
  * Số chu kỳ (epochs) và kích thước lô (batch sizes) là các tham số quan trọng ảnh hưởng sâu sắc đến tiến trình học của mạng nơ-ron.
  * Mỗi epoch đại diện cho một lượt duyệt hoàn chỉnh qua toàn bộ tập dữ liệu trong quá trình huấn luyện; số lượng epochs là siêu tham số bắt buộc phải được định nghĩa trước khi khởi chạy huấn luyện.
  * Việc cập nhật trọng số sau từng mẫu huấn luyện riêng lẻ trong mạng nơ-ron đòi hỏi chi phí tính toán rất lớn; vì vậy kích thước lô (batch size) là một siêu tham số then chốt cần được ấn định cụ thể (Masters and Luschi, 2018).
  * Căn cứ vào quy mô bộ dữ liệu và tỷ lệ phân chia tập huấn luyện - kiểm tra (train-test split) đối với bài toán dự đoán $\text{TMP}$, kích thước lô và số epochs trong quy trình HPO được thiết lập cố định lần lượt là $32$ và $1000$.
  * Thiết lập này được duy trì đồng nhất cho các mô hình dự đoán MLP và LSTM được huấn luyện tiếp sau đó.

* **Cơ chế huấn luyện lan truyền ngược (BP), bộ tối ưu hóa và tốc độ học**:
  * Thuật toán lan truyền ngược (Backpropagation - BP): Cả hai mô hình MLP và LSTM đều được huấn luyện bằng thuật toán lan truyền ngược BP.
  * Vai trò của bộ tối ưu hóa: Bộ tối ưu hóa được sử dụng trong quá trình huấn luyện BP để cập nhật và điều chỉnh các trọng số (weights) cùng độ chệch (biases) của mạng nơ-ron dựa trên các gradient tính toán được; mục đích chính là cực tiểu hóa các sai số hoặc hàm mất mát trong huấn luyện (Sun, 2019).
  * Lựa chọn bộ tối ưu hóa: Quá trình HPO khảo sát giữa ba bộ tối ưu hóa gồm Adam, RMSProp và AdaDelta.
  * Vai trò của tốc độ học (Learning rate):
    * HPO tối ưu hóa tốc độ học - một siêu tham số tối quan trọng trong các giải thuật tối ưu hóa.
    * Trong quá trình huấn luyện mạng nơ-ron, tốc độ học kiểm soát độ lớn bước nhảy (step size) mà bộ tối ưu hóa áp dụng để hiệu chỉnh trọng số và độ lệch.
    * Tốc độ học điều tiết biên độ cập nhật mô hình và có thể tác động căn bản đến tính hội tụ (convergence) cũng như hiệu suất tổng thể của mô hình (Smith, 2017).

* **Kiểm soát hiện tượng quá khớp (Overfitting) và thiết lập số lượt thử nghiệm (Trials) trong Optuna**:
  * Nguy cơ quá khớp trong học máy:
    * Quá khớp (overfitting) là một thách thức phổ biến khi mô hình hoạt động rất tốt trên dữ liệu huấn luyện nhưng lại kém hiệu quả trên dữ liệu mới chưa từng thấy.
    * Hiện tượng này xuất hiện khi mô hình trở nên quá phức tạp và có xu hướng học vẹt/ghi nhớ các trường hợp huấn luyện thay vì nắm bắt các quy luật và mối quan hệ bản chất cốt lõi (Ying, 2019).
  * Biện pháp kiểm soát quá khớp trong HPO: Kỹ thuật Dropout và Suy giảm trọng số (Weight decay) được áp dụng đồng thời cho từng tầng ẩn trong HPO, đồng thời tỷ lệ dropout và cường độ điều hòa của weight decay được tối ưu hóa nhằm cực tiểu hóa nguy cơ quá khớp.
  * Khái niệm lượt thử nghiệm (trial) trong Optuna:
    * Một trial là một bước lặp đơn lẻ của quá trình HPO, tại đó một tập hợp siêu tham số cụ thể được khởi tạo và đánh giá.
    * Trong mỗi trial, Optuna nỗ lực tìm kiếm các siêu tham số tối ưu nhằm tối đa hóa hàm mục tiêu đã được chỉ định.
    * Trong nghiên cứu này, tổng cộng $1000$ lượt thử nghiệm ($1000\text{ trials}$) được phân bổ độc lập cho mỗi mô hình MLP và LSTM.
