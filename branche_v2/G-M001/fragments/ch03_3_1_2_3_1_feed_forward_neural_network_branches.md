#### 2.3.1. Feed-forward neural network

- FFNN (Feed-forward neural network - Mạng nơ-ron truyền thẳng) bao gồm hai hoặc nhiều lớp phần tử xử lý (processing elements) được liên kết với nhau bằng các kết nối trọng số (weight connections).
  - Cấu trúc FFNN gồm ba lớp: một lớp đầu vào (input layer), một lớp ẩn (hidden layer), và một lớp đầu ra (output layer) (Figure S1 trong Supplementary Material) (Ghasemi et al. 2023).
  - Nghiên cứu trước đây (Said et al. 2018) đã báo cáo rằng mạng có một lớp ẩn thường được sử dụng phổ biến trong thực tế.
- Cơ chế huấn luyện (training):
  - Sai số được truyền tiến (fed forward) qua mạng trong quá trình huấn luyện nhằm điều chỉnh các trọng số và cực tiểu hóa sai số (minimize the error).
  - Quá trình này được lặp lại cho đến khi đạt được sai số tối thiểu (minimum error) hoặc đạt tới một số lượng epoch (chu kỳ huấn luyện) cụ thể.
- Mô hình FFNN được sử dụng trong nghiên cứu này dựa trên Phương trình (3):
  $$\hat{y}_1(t) = \left[ \sum_{j=1}^{n_h} W_{ij} f_j \left( \sum_{l=1}^{n_w} w_{ij} + w_{j0} \right) + W_{i0} \right] \tag{3}$$
  - $\hat{y}_1(t)$ đại diện cho đầu ra dự đoán (prediction output).
  - $f_j$ là hàm của mạng (function of the network).
  - $w$ là vectơ đầu vào (input vector).
  - $W_{ij}$ và $w_{ij}$ lần lượt đại diện cho trọng số kết nối lớp (layer weights) và độ lệch (biases) của mạng.
  - $n_h$ là số lượng nơ-ron trong lớp ẩn.
  - $n_w$ là kích thước của vectơ đầu vào.
  - $w_{j0}$ và $W_{i0}$ đại diện cho các giá trị bias tương ứng.
