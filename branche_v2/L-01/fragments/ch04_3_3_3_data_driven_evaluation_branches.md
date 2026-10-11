### 3.3 Data-Driven Evaluation (Feature Verification)

* **Tăng cường tập dữ liệu bằng các đặc trưng mới được sinh ra:**
  * Các đặc trưng mới sinh được áp dụng để tăng cường tập dữ liệu gốc với các thuộc tính mới được trích xuất (as illustrated in Figure $1\text{(b)}$).
  * Quy trình này tạo ra không gian biểu diễn mở rộng $T(X)$, kết hợp các đặc trưng nguyên bản cùng với các đặc trưng do chương trình biến đổi tạo ra.
* **Quy trình đánh giá đặc trưng hai giai đoạn (Two-stage feature evaluation process):**
  * Tương tự như các phương pháp tiền nhiệm trong tài liệu chuyên ngành (Hollmann et al., 2024; Nam et al., 2024), quy trình đánh giá chất lượng đặc trưng bao gồm hai giai đoạn độc lập:
    * **Giai đoạn (i) Huấn luyện mô hình trên tập dữ liệu tăng cường (Model training on the augmented dataset):**
      * Khớp (fit) một mô hình dự đoán dạng bảng (tabular predictive model) $f^*$ vào tập dữ liệu huấn luyện đã qua biến đổi $T(X_{\text{tr}})$.
      * Quá trình huấn luyện thực hiện cực tiểu hóa hàm mất mát $\mathcal{L}_f$ theo điều kiện tối ưu ở bài toán cấp dưới (lower-level optimization problem):
        $$f^* \in \arg\min_{f} \mathcal{L}_f(f(T(X_{\text{tr}})), Y_{\text{tr}}), \quad (2)$$
        như đã được thiết lập trong Eq. (1) và Eq. (2) tại Section 3.1.
    * **Giai đoạn (ii) Đánh giá hiệu năng để xác định chất lượng đặc trưng (Performance assessment for feature quality):**
      * Tiến hành đánh giá chất lượng của các phép biến đổi đặc trưng $T$ do LLM sinh ra bằng cách đo lường trực tiếp hiệu năng của mô hình $f^*$ trên tập kiểm định tăng cường $T(X_{\text{val}})$ (minh họa tại Figure $1\text{(c)}$).
      * Phép đánh giá này phản ánh khả năng khái quát hóa của tập đặc trưng mới khi áp dụng vào dữ liệu chưa thấy trong quá trình khớp mô hình:
        $$\max_{T} E(f^*(T(X_{\text{val}})), Y_{\text{val}}), \quad (1)$$
* **Mục tiêu tối ưu hóa và các thước đo hiệu năng ($E$):**
  * Như đã giải thích trong Section 3.1, mục tiêu tối thượng của quá trình đánh giá là tìm ra các đặc trưng tối ưu nhằm tối đa hóa thước đo hiệu năng $E$ (maximize performance $E$).
  * Đối với các tác vụ phân loại (classification tasks): thước đo hiệu năng $E$ là độ chính xác (accuracy).
  * Đối với các tác vụ hồi quy (regression tasks): thước đo hiệu năng $E$ là các thang đo sai số chuẩn (error metrics, chẳng hạn như RMSE).
  * Kết quả hiệu năng $E$ đóng vai trò là tín hiệu độ thích nghi (fitness signal) phản hồi cho cơ chế Quản lý Kinh nghiệm (Experience Management, Section 3.4) nhằm định hướng các vòng lặp sinh đặc trưng tiếp theo.
