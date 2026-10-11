#### 2.3.2. Radial basis function neural network

- Cấu trúc mạng RBFNN (Radial basis function neural network - Mạng nơ-ron hàm xuyên tâm):
  - RBFNN có cấu trúc tương tự như FFNN, bao gồm ba lớp (three layers).
  - Trong RBFNN, các nơ-ron ở lớp ẩn (hidden layer) và lớp đầu ra (output layer) được liên kết với nhau bằng các trọng số (weights).
  - Thông thường, các nơ-ron trong RBFNN dựa trên hàm Gauss (Gaussian function) (Kasiviswanathan & Agarwal 2012).
  - Cấu trúc của mạng được thể hiện trong Figure S2.
- Phương trình toán học biểu diễn đầu ra của mạng RBFNN được xác định theo Equation (4):
  $$y(t) = \sum_{i=1}^{k} w_i u_i(t); \quad i = 1, 2, 3, \dots, k \tag{4}$$
  - $y$ biểu thị đầu ra của mạng (output of the network).
  - $w$ đại diện cho giá trị trọng số của lớp đầu ra (weight number of the output layer).
  - $u_i(t)$ là đầu ra của nút ẩn thứ $i$ tại thời điểm $t$.
  - $k$ là số lượng nút ẩn (number of hidden nodes).
- Đầu ra của lớp ẩn được biểu diễn theo Equation (5):
  $$u_i = e^{-\frac{\|x(t) - c_i(t)\|^2}{\psi_i^2}} \tag{5}$$
  - $x$ là vectơ đầu vào (input vector).
  - $c$ là tâm của nút ẩn (centre of the hidden node).
  - $\psi$ là độ rộng của nút ẩn (width of the hidden node).
  - $k$ là số lượng nút ẩn (number of hidden nodes).
- Điều hòa siêu tham số (hyperparameters regulation) nhằm đạt hiệu suất mạng tối ưu:
  - Để đạt hiệu suất mạng tối ưu trong RBFNN, việc điều hòa các siêu tham số nhất định là cần thiết, cụ thể là số lượng spread (number of spreads) và số lượng nơ-ron trong lớp ẩn (number of neurons in the hidden layer).
  - Lựa chọn sai hằng số spread (spread constant) có thể dẫn đến hiện tượng dưới khớp (underfitting) hoặc quá khớp (overfitting).
  - Giá trị spread cao khiến các điểm dữ liệu bị phân tán trên khoảng cách đáng kể so với tâm, dẫn đến làm giảm phản hồi hàm tối đa (maximum function response) (Kasiviswanathan 2012).
  - Giá trị spread mặc định trong Matlab toolbox được thiết lập bằng $1$.
