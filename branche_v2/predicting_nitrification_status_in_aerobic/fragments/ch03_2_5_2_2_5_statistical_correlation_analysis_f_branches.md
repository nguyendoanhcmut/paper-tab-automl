### 2.2.5. Statistical correlation analysis for inputs determination

- Tương quan thứ hạng Spearman (Spearman's rank correlation) được áp dụng để đánh giá các mối quan hệ thống kê giữa biến đầu vào (inputs) và đầu ra (outputs), dựa trên kết quả lựa chọn đặc trưng đầu vào sơ bộ thông qua phân tích định tính tại Mục 2.2.2.
  - Đây là phương pháp phi tham số (nonparametric method) định lượng độ mạnh của các mối liên hệ đơn điệu (monotonic associations) giữa các biến mà không yêu cầu giả định về phân phối chuẩn (normal distribution).
  - Đặc tính này giúp phương pháp phù hợp với các bối cảnh phân loại phi tuyến nhưng có tính đơn điệu (nonlinear yet monotonic classification contexts) (Hastie et al., 2009).
- Ý nghĩa thống kê (statistical significance) của các tương quan được xác định thông qua giá trị $p$ ($p\text{-values}$):
  - Giá trị $p$ biểu thị xác suất thu được hệ số tương quan Spearman quan sát được, hoặc một giá trị cực đoan hơn, theo giả thuyết không (null hypothesis) rằng không tồn tại mối quan hệ đơn điệu giữa các biến.
  - Ngưỡng $p\text{-value} < 0.05$ được sử dụng để bác bỏ giả thuyết không và xác nhận mối tương quan đạt mức ý nghĩa thống kê.
- Hàm `"spearmanr"` thuộc thư viện SciPy trong môi trường Python được sử dụng để tính toán các hệ số tương quan và giá trị $p$ cho toàn bộ các cặp biến (all variable pairs) (Van Rossum and Drake, 2009).
