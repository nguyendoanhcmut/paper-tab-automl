### 3.1 Problem Formulation

- **Ký hiệu hình thức và định nghĩa tập dữ liệu dạng bảng (Tabular Dataset Formulation)**:
  - Một tập dữ liệu dạng bảng (tabular dataset) $\mathcal{D}$ bao gồm $N$ hàng (instances - mẫu dữ liệu), mỗi hàng được đặc trưng bởi $d$ cột (features - đặc trưng).
  - Mỗi mẫu dữ liệu $x_i$ là một vector đặc trưng $d$-chiều ($d$-dimensional feature vector) với tập hợp tên đặc trưng tương ứng được ký hiệu là $C = \{c_j\}_{j=1}^d$.
  - Tập dữ liệu đi kèm với siêu dữ liệu (metadata) $M$, bao gồm các mô tả ngữ nghĩa của từng đặc trưng (feature descriptions) và thông tin chuyên biệt của tác vụ (task-specific information).
  - Đối với các tác vụ học có giám sát (supervised learning tasks), mỗi mẫu dữ liệu $x_i$ liên kết với một nhãn mục tiêu tương ứng $y_i$:
    - $y_i \in \{0, 1, \dots, K\}$ đối với bài toán phân loại (classification tasks) có $K$ lớp.
    - $y_i \in \mathbb{R}$ đối với bài toán hồi quy (regression tasks).

- **Mục tiêu kỹ thuật đặc trưng và không gian biểu diễn tăng cường (Feature Engineering Objective)**:
  - Cho một tập dữ liệu dạng bảng có gán nhãn $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$ và một mô hình dự đoán (prediction model) $f$ thực hiện ánh xạ từ không gian đặc trưng đầu vào $\mathcal{X}$ sang không gian nhãn tương ứng $\mathcal{Y}$.
  - Mục tiêu của kỹ thuật đặc trưng (feature engineering) là xác định một chương trình biến đổi đặc trưng tối ưu (optimal feature transformation program) $T$.
  - Chương trình $T$ thực hiện ánh xạ không gian đặc trưng gốc $\mathcal{X}$ sang một biểu diễn tăng cường (augmented representation) $T(\mathcal{X})$, từ đó cải thiện hiệu năng dự đoán (predictive performance) khi huấn luyện mô hình hạ nguồn (downstream model).

- **Thiết lập bài toán tối ưu hai cấp (Bilevel Optimization Formulation)**:
  - Nhiệm vụ kỹ thuật đặc trưng được định nghĩa một cách chặt chẽ dưới dạng bài toán tối ưu hai cấp (bilevel optimization problem):
    $$\max_{T} E(f^*(T(X_{\text{val}})), Y_{\text{val}}) \quad (1)$$
    thỏa mãn điều kiện (subject to):
    $$f^* \in \arg\min_{f} \mathcal{L}_f(f(T(X_{\text{tr}})), Y_{\text{tr}}) \quad (2)$$
  - Các thành phần trong công thức tối ưu hóa:
    - $(X_{\text{tr}}, Y_{\text{tr}})$ là tập con huấn luyện (sub-training set) và $(X_{\text{val}}, Y_{\text{val}})$ là tập kiểm định (validation set), cả hai đều được phân tách từ tập dữ liệu huấn luyện $(X_{\text{train}}, Y_{\text{train}})$.
    - $\mathcal{L}_f$ là hàm mất mát (loss function) dùng để huấn luyện mô hình dự đoán $f$ trên tập dữ liệu con đã qua biến đổi $T(X_{\text{tr}})$.
    - $E(\cdot, \cdot)$ là thước đo đánh giá hiệu năng (evaluation metric) của mô hình tối ưu $f^*$ trên tập kiểm định $T(X_{\text{val}})$.
    - Sau khi xác định được chương trình biến đổi đặc trưng, mô hình dự đoán $f^*$ được huấn luyện trên toàn bộ tập dữ liệu huấn luyện đã biến đổi $T(X_{\text{train}})$ nhằm tối thiểu hóa tổn thất.

- **Cơ chế sinh chương trình thông qua Mô hình Ngôn ngữ Lớn (LLM-Based Program Generation)**:
  - Chương trình biến đổi đặc trưng $T$ được sinh ra bởi một Mô hình Ngôn ngữ Lớn (LLM) $\pi_\theta$ phụ thuộc vào câu nhắc (prompt) $p$.
  - Các chương trình ứng viên (candidate programs) được lấy mẫu theo phân phối:
    $$T \sim \pi_\theta(p)$$
  - Prompt $p$ được xây dựng có cấu trúc từ ba thành phần:
    - Siêu dữ liệu tập dữ liệu $M$ (dataset metadata).
    - Các mẫu dữ liệu thực tế $X$ (data samples).
    - Các chương trình đạt điểm cao từ các vòng lặp trước đó (high-scoring programs from prior iterations) nhằm cung cấp gợi ý ngữ cảnh (chi tiết tại Mục 3.2).

- **Phương pháp xấp xỉ bằng tìm kiếm tiến hóa (Evolutionary Search Approximation)**:
  - Mục tiêu tối ưu hai cấp trong Phương trình (1)–(2) là bài toán bất khả quy / không thể giải trực tiếp (intractable) do không gian tổ hợp (combinatorial space) của các chương trình biến đổi đặc trưng là vô cùng lớn.
  - LLM-FE giải quyết thách thức này bằng cách xấp xỉ nghiệm thông qua tìm kiếm tiến hóa (evolutionary search) tại mỗi vòng lặp (tham khảo Thuật toán 1):
    - LLM $\pi_\theta$ đề xuất tập hợp các chương trình ứng viên $\{T_j\}$ dựa trên điều kiện của prompt $p$.
    - Mỗi chương trình ứng viên $T_j$ được đánh giá bằng cách huấn luyện mô hình $f^*$ trên tập $T_j(X_{\text{tr}})$ và tính điểm đánh giá trên tập $T_j(X_{\text{val}})$.
    - Điểm số kiểm định này đóng vai trò là tín hiệu độ thích nghi (fitness signal) dẫn dắt quá trình tinh chỉnh lặp (iterative refinement) trong các thế hệ kế tiếp.
