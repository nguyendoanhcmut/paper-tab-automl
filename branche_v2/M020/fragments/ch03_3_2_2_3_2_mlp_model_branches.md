#### 2.3.2. MLP model

* **Kiến trúc mạng nơ-ron và quy trình phát triển mô hình (Network architecture)**:
  * **Cấu trúc mạng Perceptron đa lớp (MLP - Multilayer Perceptron)**:
    * Mô hình MLP bao gồm tầng đầu vào (input layer), 4 tầng ẩn (four hidden layers), và tầng đầu ra (output layer).
    * Tầng đầu vào: Mỗi nơ-ron đại diện cho một trong $7$ đặc trưng đầu vào (seven input features).
    * Bốn tầng ẩn: Mỗi tầng ẩn chứa $222$ nơ-ron ($222$ neurons).
    * Mỗi nơ-ron thực hiện phép biến đổi tuyến tính trên dữ liệu đầu vào và chuyển kết quả đến một hàm kích hoạt (activation function) để tạo ra đầu ra.
    * Quy trình phát triển mô hình và cấu trúc chi tiết được minh họa trong Hình 3 (Fig. 3):
      * **Hình 3.** Cấu trúc mô hình mạng MLP và LSTM
        * <img src="assets/fig_03_p6.jpeg" alt="Hình 3" />
        * **Hình này chứng minh điều gì**
          * MLP gồm 4 lớp Fully connected xen kẽ 4 Dropout; LSTM gồm 1 lớp LSTM tiếp nối 2 lớp Fully connected xen kẽ Dropout.
        * **Từ đâu mà thấy được**
          * Hướng đọc từ trên xuống: từ Input layer tách thành hai nhánh MLP (trái) và LSTM (phải), cùng dẫn về Output layer.
          * Khung MLP chứa 4 khối Fully connected layer xen kẽ Dropout; khung LSTM có khối LSTM layer tiếp nối 2 khối Fully connected layer xen kẽ Dropout.
  * **Cơ chế tính toán tại từng nơ-ron (Eq. (3))**:
    * Đối với một nơ-ron cho trước ở tầng $l$, quá trình tính toán được xác định theo Phương trình (3):
      $$a^l = f\left(W^l \cdot a^{l-1} + b^l\right) \quad (3)$$
    * $a^l$: Biểu diễn vectơ kích hoạt (activation vector) tại tầng $l$.
    * $W^l$: Biểu diễn ma trận trọng số (weight matrix) kết nối từ tầng $l-1$ đến tầng $l$.
    * $b^l$: Biểu diễn vectơ độ chệch (bias vector) tại tầng $l$.
    * $f$: Biểu diễn hàm kích hoạt được áp dụng theo từng phần tử (element-wise) lên kết quả biến đổi tuyến tính.

* **Cấu hình hàm kích hoạt (Activation functions)**:
  * **Hàm kích hoạt cho các tầng ẩn**:
    * Quá trình tối ưu hóa siêu tham số (HPO - Hyperparameter Optimization) lựa chọn hàm kích hoạt cho từng tầng ẩn.
    * Thứ tự các hàm kích hoạt được lựa chọn từ tầng ẩn thứ 1 đến tầng ẩn thứ 4 lần lượt là $\text{Tanh}$, $\text{Tanh}$, $\text{ReLU}$, và $\text{Tanh}$ (Eqs. (4) và (5)):
      * **Hàm Tanh (Eq. (4))**:
        $$\text{Tanh}(z) = f(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} \quad (4)$$
      * **Hàm ReLU (Rectified Linear Unit - Eq. (5))**:
        $$\text{ReLU}(z) = f(z) = \max(0, z) \quad (5)$$
      * Trong đó $z$ là giá trị đầu vào của hàm kích hoạt và $f(z)$ là giá trị đầu ra tương ứng.
  * **Hàm kích hoạt cho tầng đầu ra**:
    * Biến mục tiêu duy nhất trong bài toán dự đoán hồi quy là áp suất qua màng (TMP - Transmembrane Pressure), vốn là một biến số liên tục (continuous value).
    * Do đó, tầng đầu ra của mô hình hồi quy chỉ gồm $1$ nơ-ron đại diện cho TMP.
    * Thông thường, hàm kích hoạt tuyến tính (linear activation function) hay được áp dụng ở tầng đầu ra của các tác vụ hồi quy, cho phép mạng xuất trực tiếp các giá trị kỳ vọng mà không cần biến đổi bổ sung (Dubey et al., 2022).
    * Tuy nhiên, việc lựa chọn hàm kích hoạt phù hợp với đặc trưng của bài toán và hành vi đầu ra mong muốn là điều thiết yếu: Đối với dự đoán TMP, giá trị bắt buộc phải dương; do đó, hàm $\text{ReLU}$ được chọn làm hàm kích hoạt cho tầng đầu ra trong nghiên cứu này.

* **Hàm mất mát và các siêu tham số huấn luyện lan truyền ngược (Loss function, optimizer, and training hyperparameters)**:
  * **Hàm mất mát (Loss function - Eq. (6))**:
    * Sai số toàn phương trung bình (MSE - Mean Square Error) được chọn làm hàm mất mát cho mô hình hồi quy MLP:
      $$\text{MSE}(y, p) = \frac{1}{n} \sum_{i=1}^n (y_i - p_i)^2 \quad (6)$$
    * Trong đó $n$ là số lượng mẫu (number of samples), $y_i$ là giá trị thực nghiệm của biến mục tiêu, và $p_i$ là giá trị dự đoán của mô hình.
  * **Thuật toán tối ưu hóa và các siêu tham số huấn luyện (Optimizer and hyperparameters)**:
    * Thuật toán tối ưu hóa (Optimizer): $\text{RMSProp}$ được lựa chọn để cập nhật trọng số qua lan truyền ngược.
    * Tốc độ học (Learning rate): $0{,}0001056$.
    * Tỷ lệ loại bỏ ngẫu nhiên (Dropout rate): $0{,}1410$ cho mỗi tầng ẩn.
    * Hệ số suy giảm trọng số (Weight decay): $0{,}000001258$ cho mỗi tầng ẩn.

* **Khung chỉ số thống kê đánh giá hiệu năng hồi quy (Evaluation metrics framework)**:
  * **Căn bậc hai sai số toàn phương trung bình (RMSE - Root Mean Square Error - Eq. (7))**:
    * Bên cạnh hệ số xác định $R^2$, RMSE là chỉ số thông dụng để định lượng độ lớn trung bình của sai số dự đoán.
    * Cung cấp đánh giá trực quan về độ chính xác của mô hình theo cùng đơn vị đo với biến mục tiêu (kPa).
    * RMSE được tính bằng căn bậc hai của MSE:
      $$\text{RMSE} = \sqrt{\text{MSE}} \quad (7)$$
    * Trong bài toán hồi quy, RMSE được tính toán trên cả tập huấn luyện (training set) và tập kiểm thử (test set) nhằm mang lại bức tranh toàn diện về hiệu năng mô hình.
  * **Hệ số xác định hiệu chỉnh (Adjusted $R^2$ - Eq. (8))**:
    * Bổ sung nhằm xem xét số lượng biến dự đoán (đặc trưng đầu vào) trong mô hình, mang lại đánh giá chính xác hơn về khả năng giải thích (explanatory capability):
      $$\text{Adjusted } R^2 = 1 - \left(1 - R^2\right) \cdot \frac{n - 1}{n - p - 1} \quad (8)$$
    * Trong đó $R^2$ là hệ số xác định, $n$ là số lượng mẫu, và $p$ là số lượng biến dự đoán / đặc trưng đầu vào trong mô hình ($p = 7$).
  * **Sai số tuyệt đối trung bình (MAE - Mean Absolute Error - Eq. (9))**:
    * Đo lường độ sai lệch tuyệt đối trung bình giữa giá trị dự đoán và giá trị thực tế, phản ánh trực tiếp độ lớn sai số trung bình:
      $$\text{MAE}(y, p) = \frac{1}{n} \sum_{i=1}^n |y_i - p_i| \quad (9)$$
    * Trong đó $n$ là số lượng mẫu, $y_i$ là giá trị thực tế, và $p_i$ là giá trị dự đoán.
  * **Sai số tuyệt đối trung vị (MedAE - Median Absolute Error - Eq. (10))**:
    * Lấy giá trị trung vị của tập hợp các sai số tuyệt đối $|y_i - p_i|$ khi sắp xếp theo thứ tự tăng dần:
      $$\text{MedAE}(y, p) = \text{median}(|y_i - p_i|) \quad (10)$$
    * Là một chỉ số bền vững (robust metric), ít bị nhạy cảm hoặc sai lệch bởi các giá trị ngoại lai (outliers) trong tập dữ liệu so với MAE.
  * **Tính toàn diện của khung đánh giá**: Sự kết hợp các chỉ số ($R^2$, Adjusted $R^2$, RMSE, MAE, MedAE) tạo thành khung chuẩn mực để thẩm định chặt chẽ năng lực dự đoán của các mô hình.

* **Mô hình MLP đơn giản dùng làm chuẩn đối sánh (Simple MLP benchmark model - s-MLP)**:
  * **Mục tiêu xây dựng**: Do quy trình HPO tối ưu hóa sâu tạo ra mô hình có cấu trúc phức tạp đòi hỏi nhiều tài nguyên tính toán và thời gian, mô hình MLP đơn giản (s-MLP) được phát triển làm mốc chuẩn (benchmark) để so sánh và đánh giá hiệu năng của các mô hình mạng nơ-ron nhân tạo.
  * **Đặc tính giữ nguyên**: Tập dữ liệu sử dụng, các thuộc tính của tầng đầu vào ($7$ đặc trưng) và tầng đầu ra ($1$ nơ-ron với hàm kích hoạt $\text{ReLU}$) giữ nguyên như mô hình MLP chính.
  * **Cấu trúc mạng và điều chuẩn**:
    * s-MLP chỉ có đúng $1$ tầng ẩn (single hidden layer) với dải tìm kiếm nơ-ron từ $1$ đến $10$.
    * Do cấu trúc đơn giản, kỹ thuật Dropout không được áp dụng (Dropout rate = 0).
  * **Không gian siêu tham số và kết quả sau HPO**:
    * Các cấu hình HPO khác (hàm kích hoạt, hàm mất mát, bộ tối ưu hóa, tốc độ học, suy giảm trọng số, số lượt thử nghiệm) hoàn toàn tương đồng với mô hình MLP chính.
    * Cấu hình tối ưu nhận được sau HPO:
      * Số nơ-ron tầng ẩn: $10$ nơ-ron.
      * Hàm kích hoạt tầng ẩn: $\text{Tanh}$.
      * Hàm mất mát: $\text{MSE}$.
      * Thuật toán tối ưu: $\text{RMSProp}$.
      * Tốc độ học (Learning rate): $0{,}003987$.
      * Hệ số suy giảm trọng số (Weight decay): $0{,}0002208$.
