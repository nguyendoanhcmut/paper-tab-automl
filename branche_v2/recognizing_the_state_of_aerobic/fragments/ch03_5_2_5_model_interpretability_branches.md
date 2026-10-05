### 2.5 Model interpretability

- Phương pháp giảm chiều $t\text{-SNE}$ trực quan hóa không gian đặc trưng ngữ nghĩa.
  - Kỹ thuật $t\text{-SNE}$ chuyển đổi dữ liệu từ không gian nhiều chiều về không gian 2D mà vẫn bảo toàn cấu trúc lân cận cục bộ.
  - Xác suất tương đồng giữa hai điểm $x_i$ và $x_j$ trong không gian cao chiều được mô hình hóa bằng phân phối Gauss:
    $$p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i}\exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$$
  - Đại lượng $\sigma_i$ là phương sai của $N$ điểm lân cận gần nhất, xác định qua siêu tham số độ phức tạp (perplexity).
  - Tương đồng giữa hai điểm $y_i$ và $y_j$ trong không gian chiếu thấp được chuẩn hóa qua phân phối xác suất:
    $$q_{j|i} = \frac{\exp(-\|y_i - y_j\|^2)}{\sum_{k \neq i}\exp(-\|y_i - y_k\|^2)}$$
  - Hàm mất mát phân kỳ Kullback-Leibler ($KLD$) được tối thiểu hóa bằng thuật toán hạ độ dốc:
    $$C = \sum_{i}\sum_{j} p_{j|i} \log \frac{p_{j|i}}{q_{j|i}}$$
  - Trích xuất đầu ra từ các tầng trung gian của YOLOv8 làm đặc trưng ngữ nghĩa và chiếu giảm chiều bằng thư viện `sklearn.manifold`.
- Phương pháp giải thích đóng góp đặc trưng SHAP dựa trên lý thuyết trò chơi.
  - Phương pháp SHAP (SHapley Additive exPlanations) kết hợp lý thuyết trò chơi với giải thích cục bộ cộng tính để định lượng đóng góp của từng đặc trưng.
  - Hàm dự đoán $f(x)$ được xấp xỉ tuyến tính thông qua biến nhị phân $z$:
    $$f(x) = g(z) = \phi_0 + \sum_{i=1}^{M}\phi_i z_i$$
  - Trong đó $z \in \{0, 1\}^M$, $M$ là số lượng đặc trưng đầu vào, và $\phi_0$ là giá trị cơ sở kỳ vọng.
  - Giá trị Shapley $\phi_i$ của đặc trưng thứ $i$ được tính bằng tổng trọng số đóng góp biên:
    $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(M - |S| - 1)!}{M!} [f_x(S \cup \{i\}) - f_x(S)]$$
  - Ký hiệu $F$ là tập các đặc trưng đầu vào khác không, $S$ là tập con không chứa đặc trưng $i$.
- Quy trình triển khai Deep SHAP trên mạng nơ-ron học sâu.
  - Thuật toán Deep SHAP tính toán đóng góp lan truyền từng tầng từ đầu vào đến đầu ra so với điểm tham chiếu nền (baseline).
  - Cấu hình thực nghiệm thiết lập batch size bằng 50 và số vòng lặp tối ưu hóa là 8000 lần.
  - Sử dụng mặt nạ làm mờ kích thước $64 \times 64\text{ px}$ để che phủ từng vùng cục bộ trên ảnh đầu vào.
  - Bản đồ nhiệt (heatmap) trực quan hóa ảnh hưởng: màu đỏ thể hiện đóng góp dương, màu xanh thể hiện đóng góp âm, cường độ màu càng đậm phản ánh tác động càng lớn.
