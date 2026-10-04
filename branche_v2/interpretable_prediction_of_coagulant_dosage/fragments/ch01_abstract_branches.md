## Abstract

- Dự đoán chính xác liều lượng châm chất keo tụ (coagulant dosing) đóng vai trò thiết yếu để bảo đảm hiệu quả kỹ thuật và hiệu quả chi phí của quy trình xử lý nước.
- Nghiên cứu phát triển mô hình dự đoán chính xác liều lượng chất keo tụ trong nhà máy xử lý nước uống (drinking water treatment plants) bằng học máy tự động (AutoML - automated machine learning):
  - Phương pháp SHAP (Shapley Additive explanation - giải thích cộng tính Shapley) được áp dụng để nâng cao tính minh bạch của mô hình.
- Mô hình Random Forest (RF - rừng ngẫu nhiên) do AutoML xây dựng đạt hiệu suất cao hơn rõ rệt so với mô hình đơn Gradient Boosting Tree (cây tăng cường độ dốc) tốt nhất:
  - Sai số $\text{RMSE}$ (Root Mean Square Error) đạt $0.89$, thấp hơn $37\,\%$.
  - Sai số $\text{MAE}$ (Mean Absolute Error) đạt $0.47$, thấp hơn $52\,\%$.
  - Hệ số xác định $R^2$ (Coefficient of Determination) đạt $0.96$, cao hơn $5\,\%$.
- Mô hình RF có tiềm năng tiết kiệm $10.25\,\%$ liều lượng chất keo tụ mỗi năm, đồng thời bảo đảm chất lượng nước sau xử lý ổn định hơn:
  - Nguồn nước sông Dương Tử (Yangtze River): Tiết kiệm $222\,\text{kg/d}$ chất keo tụ PACl (polyaluminum chloride), tương đương chi phí $180.7\,\text{yuan/d}$.
  - Nguồn nước sông Loan (Luan River): Tiết kiệm $225\,\text{kg/d}$ PACl, tương đương chi phí $183.2\,\text{yuan/d}$.
- Phân tích SHAP xác định độ dẫn điện (conductivity), nitơ amoniac (ammonia nitrogen), nhu cầu oxy hóa học (chemical oxygen demand) và nhiệt độ (temperature) của nước thô là các yếu tố then chốt ảnh hưởng đến liều lượng PACl:
  - Liều lượng PACl tác động đáng kể đến độ $\text{pH}$ của nước sau xử lý.
- Việc kết hợp AutoML và phương pháp SHAP trong quản lý nước thông minh (intelligent water management) nâng cao hiệu quả xử lý nước và thực hành quản lý, đem lại các lợi ích lớn về môi trường, kinh tế và xã hội.
