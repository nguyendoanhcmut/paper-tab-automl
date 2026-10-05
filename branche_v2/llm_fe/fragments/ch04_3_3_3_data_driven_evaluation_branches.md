### 3.3 Data-Driven Evaluation

- **Tăng cường tập dữ liệu bằng đặc trưng mới sinh**:
  - Các đặc trưng do mô hình ngôn ngữ lớn (LLM - Large Language Model) tạo ra được sử dụng để tăng cường (augment) tập dữ liệu gốc, tích hợp các đặc trưng phái sinh mới (derived features) vào không gian dữ liệu ban đầu (minh họa tại Figure 1(b)).
- **Quy trình đánh giá đặc trưng gồm hai giai đoạn (two-stage feature evaluation process)**:
  - Tương tự phương pháp tiếp cận trong Hollmann et al. (2024) và Nam et al. (2024), quy trình đánh giá chất lượng đặc trưng được chia thành hai giai đoạn kế tiếp:
    - **(i) Huấn luyện mô hình trên tập dữ liệu đã tăng cường (model training on the augmented dataset)**:
      - Khớp mô hình dự đoán dữ liệu dạng bảng (tabular predictive model) $f^*$ trên tập huấn luyện con đã biến đổi $T(X_{\text{tr}})$ bằng cách cực tiểu hóa hàm mất mát $\mathcal{L}_f$ (loss function) theo bài toán tối ưu cấp dưới (xem Eq. 1 và Eq. 2):
        $$f^* \in \arg\min_f \mathcal{L}_f(f(T(X_{\text{tr}})), Y_{\text{tr}})$$
    - **(ii) Đánh giá hiệu năng để xác định chất lượng đặc trưng (performance assessment for feature quality)**:
      - Đo lường chất lượng của các chương trình biến đổi đặc trưng $T$ do LLM tạo ra (Figure 1(c)) thông qua việc tính toán hiệu năng dự đoán của mô hình $f^*$ trên tập kiểm định đã tăng cường $T(X_{\text{val}})$ (augmented validation set) (xem Eq. 1 và Eq. 2):
        $$\max_T E(f^*(T(X_{\text{val}})), Y_{\text{val}})$$
- **Mục tiêu tối ưu hóa hiệu năng dự đoán**:
  - Tương tự bài toán tối ưu hai cấp (bilevel optimization) đã trình bày trong Section 3.1, mục tiêu cốt lõi là xác định các phép biến đổi đặc trưng tối ưu nhằm tối đa hóa thước đo hiệu năng $E$:
    - Sử dụng độ chính xác (accuracy) cho bài toán phân loại (classification).
    - Sử dụng các thước đo sai số (error metrics, ví dụ RMSE) cho bài toán hồi quy (regression).
  - Điểm số đánh giá trên tập kiểm định đóng vai trò là tín hiệu phản hồi dựa trên dữ liệu (data-driven feedback / fitness score) để định hướng quá trình sàng lọc và tinh chỉnh tiến hóa trong các vòng lặp tiếp theo.
