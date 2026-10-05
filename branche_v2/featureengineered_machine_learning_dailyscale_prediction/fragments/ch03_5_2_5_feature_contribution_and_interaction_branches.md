### 2.5 Feature contribution and interaction analysis using SHAP

- Cơ sở lý thuyết trò chơi hợp tác của phương pháp SHapley Additive exPlanations (SHAP):
  - SHAP định lượng đóng góp biên của từng đặc trưng đầu vào $i$ thông qua giá trị Shapley trung bình trên mọi tập con đặc trưng khả dĩ:
    $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} [f(S \cup \{i\}) - f(S)]$$
  - $F$: Tập hợp toàn bộ các đặc trưng đầu vào của mô hình.
  - $S$: Tập con đặc trưng bất kỳ trích xuất từ $F$ không bao gồm đặc trưng $i$.
  - $f(\cdot)$: Đầu ra dự báo nồng độ $T\text{-}P$ của mô hình ứng với tập đặc trưng khảo sát.
- Hai phương thức phân tích giải thích chuyên sâu áp dụng cho mô hình tối ưu:
  - Đóng góp đặc trưng toàn cục (global feature contribution): Xếp hạng mức độ chi phối dựa trên giá trị tuyệt đối trung bình Shapley ($\text{mean } |\text{SHAP value}|$) qua toàn bộ tập dữ liệu quan trắc.
  - Mẫu hình tương tác đặc trưng cặp đôi (pairwise feature interactions): Tính toán giá trị tương tác SHAP để khám phá các mối phụ thuộc phi tuyến giữa các điều kiện vận hành thủy lực và liều lượng hóa chất.
- Không gian tìm kiếm siêu tham số tối ưu hóa Bayes cho các mô hình học máy:
  - Độ sâu cây tối đa (`max_depth`): Phạm vi tìm kiếm từ $2$ đến $10$ cho cả Decision Tree, Random Forest, XGBoost và LightGBM.
  - Số lượng cây (`n_estimators`): Tìm kiếm từ $100$ đến $2{,}000$ cây đối với các mô hình ensemble (RF, XGBoost, LightGBM).
  - Tốc độ học (`learning_rate`): Thiết lập trong khoảng $0.001$ đến $0.1$ cho các mô hình tăng cường độ dốc.
  - Tỷ lệ lấy mẫu con (`subsample` và `colsample_bytree`): Khảo sát từ $0.6$ đến $1.0$ nhằm nâng cao khả năng khái quát hóa.
