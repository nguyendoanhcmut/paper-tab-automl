### 2.3 Development of ML-based models for DAF effluent T-P prediction model

- Lựa chọn bốn thuật toán học máy đại diện dựa trên cây (tree-based models) để so sánh các cơ chế học khác nhau:
  - Cây quyết định (Decision Tree - DT): Cấu trúc cây đơn lẻ mang tính diễn giải trực tiếp.
  - Rừng ngẫu nhiên (Random Forest - RF): Mô hình kết hợp tập hợp theo cơ chế lấy mẫu lặp có hoàn lại (bootstrap aggregation / bagging) giúp giảm phương sai.
  - XGBoost: Khung tăng cường độ dốc (gradient boosting) kết hợp cơ chế phạt điều chuẩn để kiểm soát độ phức tạp mô hình và tránh quá khớp.
  - LightGBM: Thuật toán tăng cường độ dốc dựa trên phân rã biểu đồ tần số (histogram-based) tối ưu hóa tốc độ huấn luyện cho dữ liệu dạng bảng.
- Quy trình tinh chỉnh siêu tham số bằng tối ưu hóa Bayes (Bayesian Optimization):
  - Tối ưu hóa Bayes thăm dò không gian tham số đa chiều nhằm tìm kiếm cấu hình tối ưu với chi phí tính toán thấp nhất.
  - Hàm mục tiêu xác định là cực tiểu hóa sai số bình phương trung bình ($\text{MSE}$) giữa nồng độ $T\text{-}P$ đầu ra thực nghiệm và nồng độ dự đoán.
