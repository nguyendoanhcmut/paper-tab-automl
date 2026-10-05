### 2.5 Model interpretation

- Phương pháp lý thuyết trò chơi Shapley Additive Explanations (SHAP) nâng cao khả năng diễn giải mô hình:
  - Giá trị SHAP định lượng đóng góp biên của từng đặc trưng đầu vào bằng cách xét tất cả các tổ hợp đặc trưng có thể có.
  - Mô hình diễn giải tuyến tính cục bộ được xác định bởi công thức toán học:
    - $g(z') = \phi_0 + \sum_{i=1}^M \phi_i z'_i$ (Phương trình 6)
    - Ký hiệu $g(z')$ là hàm giải thích xấp xỉ; $M$ là tổng số lượng biến đặc trưng đầu vào ($M = 13$).
    - Đại lượng $\phi_i$ là giá trị Shapley đại diện cho mức độ đóng góp của đặc trưng thứ $i$.
    - Biến nhị phân $z'_i \in \{0, 1\}$ thể hiện trạng thái xuất hiện hoặc vắng mặt của đặc trưng trong phép tính tổ hợp.
- Bốn công cụ trực quan hóa bổ trợ nhau cung cấp góc nhìn toàn cục và cục bộ:
  - Biểu đồ tổng quan SHAP summary plot: xếp hạng thứ bậc tầm quan trọng toàn cục của các biến dựa trên độ lớn giá trị SHAP trung bình.
  - Biểu đồ lực SHAP force plot: minh họa trực quan sự hội tụ của từng biến kéo giá trị dự đoán cao hơn hoặc thấp hơn mức kỳ vọng nền.
  - Biểu đồ thác nước SHAP waterfall plot: phân rã chi tiết mức độ đóng góp lũy tích từng bước của từng biến cho một mẫu dự đoán cụ thể.
  - Đồ thị phụ thuộc một phần (PDP): mô tả hàm đáp ứng phi tuyến giữa một hoặc hai biến quan tâm và biến mục tiêu khi cố định các biến còn lại.
  - Việc kết hợp đồng thời bốn công cụ này cho phép giải mã các cơ chế phản ứng sinh hóa ẩn sâu trong mô hình hộp đen.
