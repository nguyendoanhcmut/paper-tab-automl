### 2.2 Deep Learning Model Development and Architecture Optimization

- Kiến trúc mô hình cơ sở LSTM hai lớp (two-layer baseline LSTM):
  - Thiết kế gồm 2 lớp LSTM xếp chồng (mỗi lớp gồm 32 units).
  - Mỗi lớp được bổ sung chuẩn hóa theo lô (Batch Normalization) và điều chuẩn dropout (tỷ lệ $0.2$).
  - Lớp đầu ra là một lớp tuyến tính kết nối đầy đủ (dense linear layer) để dự đoán nồng độ $N_2O$.
- Chiến lược mở rộng kiến trúc học sâu qua ba cấu hình chính:
  - Cấu hình 1: Tối ưu hóa kiến trúc mở rộng (Tuned LSTM):
    - Tìm kiếm tự động không gian kiến trúc với độ sâu lớp và số nơ-ron biến thiên bằng khung Optuna.
    - Tối ưu hóa đồng thời số lớp LSTM, số đơn vị mỗi lớp và các siêu tham số điều chuẩn nhằm xác định cấu hình tối ưu.
  - Cấu hình 2: Mô hình Attention-LSTM tích hợp cơ chế chú ý tự thân đa đầu:
    - Áp dụng cơ chế multi-head self-attention trên chiều không gian đặc trưng (feature dimension) trước khi đưa vào các lớp LSTM xử lý chuỗi thời gian.
    - Ưu tiên trích xuất các đặc trưng giàu thông tin nhất ngay từ đầu chu trình xử lý, gia tăng độ linh hoạt khi xử lý dữ liệu số chiều cao.
    - Công thức toán học của cơ chế chú ý đa đầu:
      $$\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$
      $$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O$$
      Trong đó $Q, K, V$ lần lượt là các ma trận truy vấn (query), khóa (key) và giá trị (value); các ma trận $W_i^Q, W_i^K, W_i^V, W^O$ là ma trận chiếu học được (learnable projection matrices).
  - Cấu hình 3: Mô hình lai CNN-LSTM:
    - Lớp tích chập một chiều (1D-CNN) áp dụng bộ lọc theo thời gian để trích xuất các đặc trưng cục bộ ngắn hạn (short-range patterns).
    - Các lớp LSTM tiếp nhận biểu diễn cô đọng từ CNN để nắm bắt các phụ thuộc dài hạn (long-range temporal dependencies).
- Quy trình tối ưu hóa siêu tham số có hệ thống bằng Optuna:
  - Sử dụng thuật toán lấy mẫu TPE (Tree-structured Parzen Estimator) kết hợp cơ chế cắt tỉa Hyperband pruning.
  - Tiến hành 100 lượt thử nghiệm (trials) cho mỗi kiến trúc: gồm 15 lượt lấy mẫu ngẫu nhiên khởi tạo quần thể trước khi kích hoạt thuật toán TPE.
  - Hàm mục tiêu tối ưu là sai số $\text{MAE}$ trên tập kiểm định, tính toán trực tiếp trên giá trị đã nghịch đảo chuẩn hóa để bảo đảm đúng thang đo vật lý thực nghiệm.
- Thiết lập huấn luyện và phân chia dữ liệu bảo toàn tính thứ tự thời gian (chronological split):
  - Triển khai trên nền tảng TensorFlow/Keras API với hàm mất mát Huber loss và thuật toán tối ưu Adam.
  - Sử dụng kỹ thuật giảm tốc độ học thích ứng (adaptive learning rate reduction) và dừng sớm (early stopping) để kiểm soát nguy cơ quá khớp.
  - Phân chia tập dữ liệu A1 (tổng số 51 ngày nội miền):
    - 30 ngày cho huấn luyện (training).
    - 10 ngày cho kiểm định (validation).
    - 11 ngày cho kiểm tra (testing).
  - Phân chia tập dữ liệu B1 (tổng số 39 ngày):
    - 25 ngày cho huấn luyện.
    - 5 ngày cho kiểm định.
    - 9 ngày cho kiểm tra.
  - Huấn luyện lặp lại 20 lần độc lập cho mỗi cấu hình mô hình với các hạt giống ngẫu nhiên (random seeds) khác nhau; tính trung bình $\text{MAE}$ và $R^2$ để loại trừ nhiễu ngẫu nhiên trong quá trình khởi tạo trọng số.
