#### 2.1.2 Artificial neural network

- **Định nghĩa, nguyên lý phỏng sinh học và bản chất học kết nối (connectionist learning)**:
  - Mạng nơ-ron nhân tạo (artificial neural network - $\text{ANN}$) bao gồm nhiều nơ-ron (neurons) cơ bản mô phỏng quá trình học hỏi của não bộ con người nhằm giải quyết đa dạng các bài toán thực tế.
  - $\text{ANN}$ là một trong những mô hình được sử dụng thường xuyên nhất trong học máy (machine learning - $\text{ML}$), đại diện tiêu biểu cho trường phái học kết nối (connectionist learning).

- **Kiến trúc phân tầng và cơ chế ánh xạ đầu vào - đầu ra (input-to-output mapping)**:
  - Cấu trúc điển hình của một $\text{ANN}$ gồm ba thành phần chính: tầng đầu vào (input layer), tầng ẩn (hidden layer), và tầng đầu ra (output layer).
  - Quy mô nơ-ron: Mỗi tầng có thể chứa từ một vài cho đến hàng triệu nơ-ron; số lượng nơ-ron quy định độ phức tạp của các mối quan hệ tiềm ẩn bên trong dữ liệu cần học.
  - Cơ chế ánh xạ phi tuyến: Tầng đầu vào tiếp nhận dữ liệu huấn luyện (training data), dữ liệu này được biến đổi phi tuyến qua một hoặc nhiều tầng ẩn, và tầng đầu ra cung cấp dữ liệu giá trị đã qua chuyển đổi phi tuyến, hoàn tất quá trình ánh xạ từ đầu vào sang đầu ra (input-to-output mapping).

- **Chiến lược gia tăng năng lực xử lý phi tuyến, phạm vi bài toán và định dạng dữ liệu đầu vào**:
  - Khả năng xử lý các bài toán phi tuyến phức tạp của $\text{ANN}$ được nâng cao thông qua ba giải pháp kỹ thuật:
    - Gia tăng "độ sâu" (depth) bằng cách bổ sung thêm các tầng ẩn.
    - Gia tăng "độ rộng" (width) bằng cách tăng số lượng nơ-ron trong một tầng đơn lẻ.
    - Tối ưu hóa hàm kích hoạt (activation function).
  - Phạm vi bài toán: $\text{ANN}$ có thể được triển khai để giải quyết bài toán phân loại (classification), hồi quy (regression), và bài toán chuỗi thời gian (time-series).
  - Thích ứng cỡ mẫu: Phù hợp để xử lý các bài toán có quy mô cỡ mẫu biến thiên (varying sample sizes) thông qua việc linh hoạt áp dụng nhiều biến thể kiến trúc khác nhau.
  - Định dạng dữ liệu đầu vào: Dữ liệu đầu vào thuộc dạng đa biến (multivariate), bao gồm dữ liệu liên tục (continuous), dữ liệu rời rạc (discrete), hoặc dữ liệu dạng ma trận/hình ảnh (matrix/image data).

- **Các kiến trúc mạng nơ-ron: Từ mô hình mạng nông (MLP, RBFNN) đến mạng nơ-ron sâu (DNN: CNN, RNN, GNN)**:
  - Perceptron đa tầng (multilayer perceptron - $\text{MLP}$, còn gọi là mạng nơ-ron lan truyền ngược - back-propagation neural network ($\text{BPNN}$)) (Fig. 3(a)) và mạng nơ-ron hàm cơ sở xuyên tâm (radial basis function neural network - $\text{RBFNN}$) (Fig. 3(b)) là các cấu trúc mạng nơ-ron đơn giản nhất, thường được áp dụng cho bài toán hồi quy (regression), phân loại (classification) và các câu đố chuỗi thời gian (time series puzzles).
  - So với $\text{MLP}$ và $\text{RBFNN}$, mạng nơ-ron sâu (deep neural network - $\text{DNN}$) (ví dụ: mạng nơ-ron tích chập - convolutional neural network ($\text{CNN}$) (Fig. 3(c)), mạng nơ-ron hồi quy - recurrent neural network ($\text{RNN}$) (Fig. 3(d)), và mạng nơ-ron đồ thị - graph neural network ($\text{GNN}$)) sở hữu cấu trúc mạng phức tạp hơn và có năng lực tự động trích xuất đặc trưng (autonomously extracting features), giúp giảm bớt nhu cầu can thiệp của con người và nâng cao chất lượng trích xuất đặc trưng (Zhang et al., 2018).
  - **Figure 3: Schematic diagrams of artificial neural networks**
    - ![Figure 3](assets/fig_03_p7.jpeg)
    - **Hình này chứng minh điều gì**:
      - Thể hiện sơ đồ cấu trúc kiến trúc và cơ chế lan truyền tín hiệu của bốn mô hình mạng nơ-ron điển hình: $\text{MLP}$, $\text{RBFNN}$, $\text{CNN}$ và $\text{RNN}$/$\text{LSTM}$.
    - **Từ đâu mà thấy được**:
      - Panel (a) Mô hình $\text{MLP}$: Tầng đầu vào tiếp nhận $x_i$, tầng ẩn $b_h = \varphi\left(\sum_{i=1}^{k} v_{ih}x_i + \gamma_h\right)$, tầng đầu ra $z_j = \phi\left(\sum w_{hj}b_h + \theta_j\right)$, với tổng số tham số chưa biết $N = kq + ql + q + l$.
      - Panel (b) Mô hình $\text{RBFNN}$: Trọng số $v_{ij}$ kết nối vào tầng ẩn hàm cơ sở xuyên tâm ($\text{RBF}$), chuyển tiếp qua trọng số $w_j$ tới nút cộng tuyến tính ($\sum$) ở đầu ra $z_j$.
      - Panel (c) Mô hình $\text{CNN}$: Quá trình xử lý từ ảnh đầu vào qua các tầng tích chập trích xuất bản đồ đặc trưng (convolved feature maps), tầng gộp (pooled feature maps) và các tầng kết nối đầy đủ (fully connected layers) tới đầu ra.
      - Panel (d) Mô hình $\text{RNN}$: Dữ liệu chuỗi theo bước thời gian ($t-1, t, t+1$) với trọng số $U, W, V$; khối phóng to $\text{LSTM}$ chi tiết hóa trạng thái ô nhớ $c^t$, trạng thái ẩn $h^t$ cùng các cổng kích hoạt $\sigma$ và $\tanh$.

- **Kiến trúc mạng nơ-ron tích chập (CNN) và các bước cải tiến kiến trúc**:
  - Cơ chế trích xuất không gian: $\text{CNN}$ thường sử dụng dữ liệu không gian hoặc dữ liệu hình ảnh làm đầu vào để thực hiện nhận dạng hình ảnh hoặc trích xuất đặc trưng không gian thông qua các phép tính tích chập (convolutional computation) (Zeiler and Fergus, 2014; Gao et al., 2019; Kiranyaz et al., 2021).
  - Các cải tiến kiến trúc nổi bật của $\text{CNN}$:
    - GoogLeNet (Szegedy et al., 2015).
    - $\text{CNN}$ dựa trên độ sâu (depth-based $\text{CNNs}$) (Szegedy et al., 2016).
    - DenseNet (Huang et al., 2017).
    - Mạng phần dư mở rộng (wide residual networks) (Zagoruyko and Komodakis, 2016).
    - $\text{CNN}$ hai kênh (dual-channel $\text{CNN}$) (Ma et al., 2023).

- **Kiến trúc mạng nơ-ron hồi quy (RNN), mô hình LSTM và thách thức đánh đổi của DNN**:
  - Xử lý dữ liệu chuỗi thời gian: $\text{RNN}$, đặc biệt là mạng bộ nhớ ngắn-dài (long short-term memory - $\text{LSTM}$) (Greff et al., 2017), thể hiện những ưu thế nhất định khi dữ liệu đầu vào mang đặc tính phụ thuộc thời gian (temporal characteristics).
  - Thách thức đánh đổi kỹ thuật của $\text{DNN}$: Các mô hình $\text{DNN}$ đối mặt với thách thức lớn khi độ phức tạp mô hình gia tăng (increased model complexity) đi kèm sự suy giảm khả năng diễn giải/giải thích (reduced interpretability).

- **Hàm kích hoạt tầng ẩn và Mạng nơ-ron Wavelet (WNN)**:
  - Tính đa dạng của hàm kích hoạt: Các mạng nơ-ron khác nhau có thể áp dụng các hàm kích hoạt tầng ẩn khác nhau; Bảng S1 trong Phụ lục A (Table S1 in Appendix A) cung cấp bản tổng hợp các hàm kích hoạt tầng ẩn khả dụng.
  - Đặc tính của mạng nơ-ron Wavelet ($\text{WNN}$): Khác với hàm kích hoạt dạng chữ S truyền thống (conventional S-type activation function), $\text{WNN}$ áp dụng hàm wavelet làm hàm kích hoạt cho tầng ẩn (Alexandridis and Zapranis, 2013).
  - Các lợi thế kỹ thuật của $\text{WNN}$ so với $\text{MLP}$ truyền thống:
    - Tốc độ hội tụ mạng nhanh hơn (faster network convergence).
    - Ngăn ngừa hiện tượng rơi vào tối ưu cục bộ (prevention of local optimization).
    - Khả năng thực hiện phân tích tần số - thời gian cục bộ (local time-frequency analysis).

- **Các lĩnh vực ứng dụng của ANN trong kỹ thuật môi trường**:
  - Ứng dụng của $\text{ANN}$ lan tỏa rộng rãi trong lĩnh vực kỹ thuật môi trường (environmental field), bao gồm nhiều phân ngành:
    - Vận hành hoặc tối ưu hóa các hệ thống quy trình màng (membrane process systems) (Wang et al., 2024b).
    - Xử lý nước thải (wastewater treatment) (Al-Ghazawi and Alawneh, 2021).
    - Dự đoán các chất ô nhiễm mới nổi (novel pollutants) như phụ phẩm khử trùng (disinfection by-products) (Kulkarni and Chellam, 2010).
    - Dự đoán chất lượng nước mặt hoặc nước ngầm (surface or groundwater quality).
    - Quá trình sản xuất khí sinh học (biogas production) (Liu et al., 2021).
    - Hiện tượng hấp phụ môi trường (environmental adsorption).
