## Abstract

- Quy trình xử lý nước thải dựa trên công nghệ anammox (anammox-based processes) mang lại nhiều triển vọng trong việc cắt giảm phát thải carbon (reducing carbon emissions) và đang được nghiên cứu chuyên sâu:
  - Quá trình vận hành thực tế của các quy trình anammox dòng chính (mainstream anammox processes) vẫn còn gặp trở ngại do các chiến lược điều tiết bên ngoài (external regulation strategies) chưa rõ ràng.
- Nghiên cứu ứng dụng thuật toán học máy tự động (AutoML - automated machine learning) nền tảng H2O kết hợp phân tích có thể giải thích (interpretable analysis):
  - Khai phá các mối quan hệ nội tại (internal relationships) trong tập dữ liệu lớn (big dataset) thu thập từ các công trình nghiên cứu quy trình anammox xử lý nước thải đô thị (municipal wastewater).
  - Ứng dụng phân tích tổng hợp (meta-analysis) nhằm đánh giá hiệu quả loại bỏ nitơ (nitrogen removal efficiency).
- Các mô hình tăng cường độ dốc cực đại (XGBoost - eXtreme Gradient Boosting) và máy tăng cường độ dốc (GBM - gradient boosting machine) do thuật toán AutoML tự động thiết lập đạt độ chính xác dự đoán cao nhất:
  - Hệ số xác định đạt $R^2 = 0.814 - 0.993$.
  - Mô hình tối ưu thể hiện khả năng tổng quát hóa (generalization ability) tốt trên tập dữ liệu chưa từng thấy (unseen data) thu thập từ nghiên cứu này với $R^2 = 0.725 - 0.945$.
- Biểu đồ phụ thuộc một phần một chiều (1D-PDP - one-dimensional partial dependence plots) và hai chiều (2D-PDP - two-dimensional partial dependence plots) làm sáng tỏ khoảng thích hợp của các điều kiện vận hành và đặc tính dòng vào:
  - Xác định các khoảng thích hợp của điều kiện vận hành (operation conditions) và đặc tính nước thải đầu vào (influent characteristics).
  - Tương ứng với hiệu quả loại bỏ chất ô nhiễm nitơ cao (high removal efficiency of nitrogen pollutants) và tốc độ loại bỏ nitơ cao thông qua con đường phản ứng anammox (high nitrogen removal rate through the anammox reaction pathway).
- Nghiên cứu thúc đẩy hiểu biết khoa học về cách cải thiện quá trình vận hành thực tế của các quy trình khử nitơ dựa trên anammox dòng chính trong xử lý nước thải đô thị.
