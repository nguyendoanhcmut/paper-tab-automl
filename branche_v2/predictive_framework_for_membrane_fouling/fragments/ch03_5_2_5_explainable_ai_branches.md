## 2.5. Explainable AI

- Các kỹ thuật Trí tuệ nhân tạo có thể giải thích (Explainable AI - XAI) được áp dụng nhằm nâng cao khả năng diễn giải (interpretability) của các mô hình học máy (machine learning) và cải thiện độ tin cậy đối với các kết quả dự đoán.
  - Phân tích độ quan trọng của đặc trưng (feature importance analysis) và Shapley Additive Explanations ($SHAP$) được sử dụng để đánh giá mức độ đóng góp của từng đặc trưng riêng lẻ (individual features) vào kết quả dự đoán của mô hình.
  - Các phương pháp này hỗ trợ hiểu rõ cơ chế tác động của các biến số khác nhau đến dự đoán hiện tượng nghẹt màng (membrane fouling), qua đó gia tăng tính minh bạch của khung dự đoán (predictive framework) [31].

### 2.5.1. Feature Importance

- Độ quan trọng của đặc trưng (Feature importance) định lượng mức độ đóng góp của từng biến số đầu vào (input variable) vào kết quả dự đoán của mô hình.
  - Việc xác định các đặc trưng có ảnh hưởng lớn nhất cung cấp thông tin chi tiết về các thông số đóng vai trò thiết yếu trong dự đoán áp suất xuyên màng ($TMP$) và thông lượng riêng ($Spec.\ Flux$).

### 2.5.2. Shapley Additive Explanations

- Shapley Additive Explanations ($SHAP$) là kỹ thuật $XAI$ dựa trên lý thuyết trò chơi (game theory), được thiết kế nhằm phân bổ công bằng mức độ đóng góp giữa các đặc trưng trong mô hình dự đoán.
  - Giá trị $SHAP$ định lượng đóng góp biên (marginal contribution) của từng đặc trưng vào đầu ra của mô hình bằng cách tính toán độ chênh lệch dự đoán khi một đặc trưng được đưa vào so với khi đặc trưng đó bị loại trừ khỏi tất cả các tập hợp con đặc trưng (feature subsets) khả dĩ.
- Giá trị Shapley $\phi_i$ cho đặc trưng $i$ được tính toán theo Equation (9):
  $$\phi_i(f) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(n - |S| - 1)!}{n!} [f_x(S \cup \{i\}) - f_x(S)] \tag{9}$$
  - $\phi_i$: giá trị Shapley đại diện cho đặc trưng $i$, định lượng mức đóng góp trung bình của đặc trưng này vào kết quả dự đoán của mô hình.
  - $N$: tập hợp tất cả các đặc trưng.
  - $S$: tập hợp con các đặc trưng loại trừ đặc trưng $i$ ($S \subseteq N \setminus \{i\}$).
  - $f_x(S)$: hàm đại diện cho kết quả dự đoán của mô hình khi chỉ sử dụng tập hợp con đặc trưng $S$.
  - $[f_x(S \cup \{i\}) - f_x(S)]$: độ thay đổi trong kết quả dự đoán khi đặc trưng $i$ được bổ sung vào tập hợp con $S$.
  - $\frac{|S|!(n - |S| - 1)!}{n!}$: số hạng giai thừa tính toán tất cả các tổ hợp đặc trưng–tập hợp con khả dĩ, đảm bảo phân bổ công bằng mức đóng góp giữa các đặc trưng.
