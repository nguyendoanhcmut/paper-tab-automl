#### 2.3.3. LSTM model

* **Kiến trúc tổng thể và cấu hình các tầng của mô hình**:
  * **Đặc tính tầng đầu vào và đầu ra**: Mô hình Mạng bộ nhớ ngắn-dài hạn (long short-term memory - LSTM) và Perceptron đa lớp (multilayer perceptron - MLP) có cùng các đặc tính tầng đầu vào (input layer) và tầng đầu ra (output layer) phục vụ bài toán dự đoán hồi quy (regression prediction).
  * **Cấu trúc ba tầng ẩn (three hidden layers)**:
    * Tầng ẩn thứ nhất là một tầng LSTM (LSTM layer) với 45 đơn vị bộ nhớ (memory units).
    * Hai tầng ẩn còn lại là các tầng liên kết đầy đủ (fully connected layers), mỗi tầng chứa 140 nơ-ron (neurons).
  * **Hàm kích hoạt (activation functions)**: Được cấu hình lần lượt cho từng tầng ẩn theo thứ tự là $\text{ReLU}$, $\tanh$, và $\tanh$.

* **Cấu trúc ô nhớ và cơ chế cổng (Memory cell architecture and gating mechanisms)**:
  * **Chức năng của đơn vị LSTM**: Mỗi đơn vị trong tầng LSTM đảm nhiệm vai trò xử lý và lưu trữ dữ liệu theo thời gian (processing and storing data over time).
  * **Các thành phần cốt lõi**: Bao gồm cổng đầu vào (input gates), cổng quên (forget gates), cổng đầu ra (output gates) và các ô nhớ (memory cells).
  * **Cơ chế điều phối thông tin**: Các thành phần này cùng phối hợp quản lý luồng thông tin đi qua đơn vị nhớ, cho phép giữ lại hoặc loại bỏ dữ liệu tùy thuộc vào mức độ liên quan (relevance).
  * **Hệ phương trình trạng thái và các cổng (Eqs. (11)–(15))**: Xác định cách thức kết hợp và biến đổi giữa đầu vào, trạng thái ẩn trước đó và trạng thái ô nhớ trước đó để tạo ra trạng thái ẩn đầu ra và trạng thái ô nhớ cập nhật cho từng bước thời gian:
    * **Cổng đầu vào (Input Gate - $i_t$)**:
      $$i_t = \text{Sigmoid}(W_i \cdot z_t + U_i \cdot h_{t-1} + b_i) \quad (11)$$
    * **Cổng quên (Forget Gate - $f_t$)**:
      $$f_t = \text{Sigmoid}(W_f \cdot z_t + U_f \cdot h_{t-1} + b_f) \quad (12)$$
    * **Ô nhớ (Memory cell - $c_t$)**:
      $$c_t = f_t \cdot c_{t-1} + i_t \cdot \tanh(W_c \cdot z_t + U_c \cdot h_{t-1} + b_c) \quad (13)$$
      *(Lưu ý: trong văn bản gốc, ký hiệu hệ số đầu được in là $f_f \cdot c_{t-1}$ đại diện cho cổng quên $f_t$)*
    * **Cổng đầu ra (Output Gate - $o_t$)**:
      $$o_t = \text{Sigmoid}(W_o \cdot z_t + U_o \cdot h_{t-1} + b_o) \quad (14)$$
    * **Trạng thái ẩn (Hidden State - $h_t$)**:
      $$h_t = o_t \cdot \tanh(c_t) \quad (15)$$
  * **Định nghĩa các biến số và tham số**:
    * $z_t$ (trong nguồn ghi $z_i$): Biểu diễn đầu vào tại bước thời gian $t$.
    * $h_{t-1}$: Biểu diễn đầu ra của tầng LSTM trước đó hoặc trạng thái ẩn ban đầu (initial hidden state).
    * $c_{t-1}$: Trạng thái ô nhớ trước đó (previous cell state).
    * $c_t$: Trạng thái ô nhớ được cập nhật (updated cell state).
    * $h_t$: Trạng thái ẩn đầu ra (output hidden state).
    * **Hàm Sigmoid**: Hàm kích hoạt nén các giá trị về khoảng giữa 0 và 1 (Eq. (16)):
      $$\text{Sigmoid}(z) = f(z) = \frac{1}{1 + e^{-z}} \quad (16)$$
    * **Hàm Tanh**: Hàm kích hoạt nén các giá trị về khoảng giữa $-1$ và $1$.
    * $W_i, W_f, W_c, W_o$: Các ma trận trọng số (weight matrices) lần lượt cho cổng đầu vào, cổng quên, ô nhớ và cổng đầu ra.
    * $U_i, U_f, U_c, U_o$: Các ma trận trọng số hồi quy (recurrent weight matrices) tương ứng.
    * $b_i, b_f, b_c, b_o$: Các vectơ độ chệch (bias vectors) cho từng cổng và ô nhớ tương ứng.

* **Phương thức mô hình hóa chuỗi phi truyền thống (Unorthodox sequence modeling)**:
  * **Khả năng xử lý chuỗi của LSTM**: Mô hình LSTM được cấu trúc tự nhiên để xử lý chuỗi (sequences); kiến trúc có thể đánh giá các bước thời gian (time steps) nhằm xác định các liên kết và quy luật mẫu hình thời gian (temporal links and patterns) trong dữ liệu.
  * **Thiết lập bước thời gian cố định $\text{time step} = 1$**:
    * Thông thường, các bước thời gian trong mô hình LSTM phản ánh các thời điểm hoặc điểm dữ liệu trong một chuỗi.
    * Trong nghiên cứu này, bước thời gian được chủ đích thiết lập bằng $1$.
    * Mỗi đặc trưng trong tập dữ liệu được coi như một trường hợp độc lập (unique instance) thay vì một điểm đơn lẻ trong một chuỗi.
    * Cấu hình này chỉ ghi nhận giá trị tức thời của đặc trưng mà không khai thác khả năng xử lý tuần tự theo thời gian (temporal sequencing capability) của mô hình.
  * **Mục tiêu thử nghiệm**: Phương pháp phi truyền thống này được lựa chọn có chủ đích nhằm so sánh năng lực dự đoán của LSTM với MLP trên cùng một thiết lập tập dữ liệu phi tuần tự (non-sequential data set-up).

* **Siêu tham số huấn luyện và điều chuẩn (Training hyperparameters and regularization)**:
  * **Bộ tối ưu hóa (Optimizer)**: Sử dụng thuật toán Adam với tốc độ học (learning rate) là $0.0003677$.
  * **Kỹ thuật điều chuẩn (Regularization)**: Kỹ thuật loại bỏ ngẫu nhiên (dropout) và suy giảm trọng số (weight decay) được áp dụng trên từng tầng ẩn:
    * Tỷ lệ dropout (dropout rate): $0.1663$.
    * Hệ số suy giảm trọng số (weight decay): $0.0004726$.
