## Abstract

- Quá trình electrochemical oxidation (oxy hóa điện hóa) của perfluorooctanoic acid (PFOA) đối mặt với độ phức tạp vận hành lớn do các tương tác phi tuyến giữa nhiều biến số quy trình.
  - PFOA là chất ô nhiễm môi trường bền vững và độc hại (persistent and toxic environmental pollutant).
- Nghiên cứu đề xuất một framework machine learning (ML - học máy) tự động hóa hoàn toàn và có độ ổn định cao dựa trên Fast Lightweight AutoML (FLAML), tích hợp với SHapley Additive exPlanations (SHAP) nhằm tối ưu hóa và diễn giải hiệu năng oxy hóa điện hóa PFOA.
- Mô hình XGBoost được FLAML tối ưu hóa đạt độ chính xác dự đoán cao với $\text{RMSE} = 3.97$ và $R^2 = 0.98$.
  - Hiệu năng của FLAML-optimized XGBoost cao hơn đáng kể so với các mô hình ML truyền thống được tinh chỉnh có hệ thống (systematically tuned traditional ML models) như Random Forest, Gradient Boosting và các kiến trúc Deep Learning.
  - Quy trình kiểm định thống kê nghiêm ngặt xác nhận tính khái quát hóa và độ ổn định cao hơn của mô hình được tối ưu hóa bằng FLAML.
- Phân tích khả năng diễn giải dựa trên SHAP xác định các biến số quy trình chi phối hiệu quả xử lý, nhất quán với động học phân hủy điện hóa đã được thiết lập:
  - Thời gian điện phân (electrolysis time) và vật liệu anode (anode material) là các yếu tố thúc đẩy chính (primary drivers).
  - Nồng độ chất điện phân (electrolyte concentration) và mật độ dòng điện (current density) tạo thành bậc ảnh hưởng tiếp theo (next tier).
- Mô hình XGBoost được FLAML tối ưu hóa đạt mức giảm $72\%$ chi phí tính toán ($\text{computational overhead}$) so với các mô hình được tinh chỉnh thủ công.
  - Kết quả này thiết lập một chuẩn đối sánh (benchmark) có khả năng tái lập (reproducible), có thể diễn giải (interpretable) và hiệu quả về mặt tính toán trong các ứng dụng ML môi trường.
- Framework cung cấp một phương pháp tiếp cận có hệ thống giúp cải thiện độ chính xác dự đoán, tăng cường khả năng diễn giải và củng cố tính ứng dụng thực tế để hỗ trợ tối ưu hóa công nghệ xử lý môi trường và ra quyết định môi trường.
