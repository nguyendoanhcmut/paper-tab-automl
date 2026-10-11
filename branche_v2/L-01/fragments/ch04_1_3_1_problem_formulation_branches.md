### 3.1 Problem Formulation

* **Định nghĩa tập dữ liệu bảng (tabular dataset) $D$ và siêu dữ liệu (metadata) $M$:**
  * Tập dữ liệu bảng $D$ bao gồm $N$ hàng (hoặc thực thể — instances), mỗi thực thể được đặc trưng bởi $d$ cột (hoặc đặc trưng — features).
  * Mỗi thực thể dữ liệu $x_i$ là một vector đặc trưng $d$ chiều ($d$-dimensional feature vector) với tên đặc trưng được ký hiệu bởi $C = \{c_j\}_{j=1}^d$.
  * Tập dữ liệu đi kèm với siêu dữ liệu (metadata) $M$ bao gồm mô tả đặc trưng (feature descriptions) và thông tin đặc thù của tác vụ (task-specific information).
* **Định nghĩa bài toán học có giám sát (supervised learning) trên dữ liệu bảng:**
  * Đối với các tác vụ học có giám sát, mỗi thực thể $x_i$ được liên kết với một nhãn tương ứng $y_i$.
  * Nhãn $y_i \in \{0, 1, \dots, K\}$ đối với các tác vụ phân loại (classification tasks) có $K$ lớp.
  * Nhãn $y_i \in \mathbb{R}$ đối với các tác vụ hồi quy (regression tasks).
  * Cho một tập dữ liệu bảng có nhãn $D = \{(x_i, y_i)\}_{i=1}^N$ và mô hình dự đoán $f$ ánh xạ từ không gian đặc trưng đầu vào $\mathcal{X}$ sang không gian nhãn tương ứng $\mathcal{Y}$.
* **Mục tiêu thiết kế đặc trưng (feature engineering objective) dưới dạng bài toán tối ưu hóa hai cấp (bilevel optimization):**
  * Mục tiêu của kỹ thuật thiết kế đặc trưng là xác định một chương trình biến đổi đặc trưng tối ưu (optimal feature transformation program) $T$, ánh xạ không gian đặc trưng ban đầu $\mathcal{X}$ sang một biểu diễn tăng cường $T(\mathcal{X})$ nhằm cải thiện hiệu năng dự đoán khi dùng để huấn luyện mô hình hạ nguồn (downstream model).
  * Tác vụ thiết kế đặc trưng được định nghĩa toán học thông qua bài toán tối ưu hai cấp:
    $$\max_{T} E(f^*(T(X_{\text{val}})), Y_{\text{val}}), \quad (1)$$
    với điều kiện:
    $$f^* \in \arg\min_{f} \mathcal{L}_f(f(T(X_{\text{tr}})), Y_{\text{tr}}), \quad (2)$$
    trong đó $(X_{\text{tr}}, Y_{\text{tr}})$ và $(X_{\text{val}}, Y_{\text{val}})$ lần lượt là tập con huấn luyện (sub-training set) và tập kiểm định (validation set) được tách ra từ dữ liệu huấn luyện $(X_{\text{train}}, Y_{\text{train}})$.
  * Mô hình dự đoán $f^*$ sau đó được huấn luyện trên dữ liệu huấn luyện đã biến đổi $T(X_{\text{train}})$ để tối thiểu hóa hàm mất mát (loss).
* **Sinh chương trình biến đổi đặc trưng bằng mô hình ngôn ngữ lớn (LLM):**
  * Chương trình biến đổi đặc trưng $T$ được sinh bởi LLM $\pi_\theta$ có điều kiện dựa trên câu nhắc (prompt) $p$.
  * Các chương trình ứng viên được lấy mẫu theo xác suất $T \sim \pi_\theta(p)$, trong đó $p$ được xây dựng từ siêu dữ liệu tập dữ liệu $M$, các mẫu dữ liệu $X$, và các chương trình đạt điểm cao từ các vòng lặp trước (detailed in Section 3.2).
* **Xấp xỉ tối ưu hóa hai cấp thông qua tìm kiếm tiến hóa (evolutionary search):**
  * Mục tiêu tối ưu hai cấp trong Eqs. (1)–(2) không thể giải trực tiếp (intractable to optimize directly) trên không gian tổ hợp (combinatorial space) của các chương trình biến đổi đặc trưng.
  * LLM-FE xấp xỉ mục tiêu này bằng tìm kiếm tiến hóa tại mỗi vòng lặp (iteration) (xem Algorithm 1).
  * Tại mỗi vòng lặp, $\pi_\theta$ đề xuất các chương trình ứng viên $\{T_j\}$ dựa trên điều kiện $p$.
  * Mỗi chương trình ứng viên được đánh giá bằng cách huấn luyện $f^*$ trên $T_j(X_{\text{tr}})$ và chấm điểm trên $T_j(X_{\text{val}})$.
  * Điểm đánh giá này đóng vai trò là tín hiệu độ thích nghi (fitness signal) để dẫn dắt quá trình tinh chỉnh lặp (iterative refinement).
