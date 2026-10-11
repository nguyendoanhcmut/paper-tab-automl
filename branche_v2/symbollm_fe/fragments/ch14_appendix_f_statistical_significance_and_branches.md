## Appendix F Statistical Significance and Stability Analysis of Ablation Study

- Thiết lập thực nghiệm nhằm đảm bảo tính vững (robustness) và tính hợp lệ thống kê (statistical validity) của nghiên cứu loại bỏ thành phần (ablation study):
  - Khung thực nghiệm được triển khai dựa trên cơ chế kiểm định chéo (cross-validation framework) qua nhiều hạt giống ngẫu nhiên độc lập (independent random seeds).
  - Thước đo định lượng độ ổn định (stability): Báo cáo hiệu năng trung bình (mean performance) kết hợp cùng độ lệch chuẩn (standard deviation).
- Khung làm việc hoàn chỉnh (complete framework) đạt độ chính xác (accuracy) cao nhất đồng thời có độ lệch chuẩn thấp nhất:
  - Thể hiện tính nhất quán vượt trội (superior consistency) khi so sánh với toàn bộ các biến thể bị loại bỏ thành phần (ablated variants).
  - Các biến thể thiếu kỹ thuật nhắc lệnh có cấu trúc (structured prompting) hoặc thiếu tìm kiếm tiến hóa (evolutionary search) đều thể hiện phương sai (variance) cao hơn rõ rệt.
  - Việc tích hợp các mô hình ngôn ngữ lớn (Large Language Models - LLMs) đóng vai trò như một bộ lọc ngữ nghĩa ổn định (stable semantic filter), giảm thiểu dao động hiệu năng (performance fluctuation) một cách hiệu quả.
- Đánh giá nghiêm ngặt ý nghĩa thống kê của các kết quả thông qua kiểm định $t$ theo cặp (paired $t$-tests):
  - Thực hiện các phép kiểm định $t$ theo cặp (paired $t$-tests) giữa phương pháp đề xuất (SymboLLM-FE) và từng biến thể cắt bỏ (ablation variant).
  - Kết quả xác nhận SymboLLM-FE vượt trội đáng kể (significantly outperforms) so với toàn bộ các đường cơ sở (baselines), với các giá trị $p$ ($p$-values) nằm sâu dưới ngưỡng ý nghĩa thống kê (significance threshold).
  - Mức độ cải thiện vẫn duy trì ý nghĩa thống kê (statistically significant) ngay cả khi đối chiếu với biến thể cắt bỏ mạnh nhất (strongest ablation variant).
- Phân tích khoảng tin cậy (confidence intervals) và khẳng định tính cần thiết của các thành phần:
  - Các khoảng tin cậy (confidence intervals) củng cố thêm các phát hiện, cho thấy mức độ chồng lấn tối thiểu (minimal overlap) giữa phương pháp đề xuất và các biến thể, đặc biệt là các biến thể khuyết thiếu các thành phần then chốt.
  - Kết quả chứng minh tính tất yếu (necessity) của từng thành phần trong khung làm việc.
  - Xác nhận phương pháp nâng cao đồng thời cả hiệu năng dự đoán (predictive performance) lẫn độ ổn định của quá trình sinh đặc trưng (stability of feature generation), giảm thiểu sự biến động (volatility) thường thấy trong các quá trình tối ưu hóa ngẫu nhiên (stochastic optimization processes).
