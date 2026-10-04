## Abstract

- Hệ thống màng lọc sinh học (Membrane Bioreactor - $\text{MBR}$) dùng cho xử lý và tái sử dụng nước xám tại chỗ (on-site greywater treatment and reuse) đòi hỏi quy trình giám sát nitrat hóa (nitrification monitoring) ổn định nhằm ngăn ngừa gián đoạn vận hành và duy trì tiêu chuẩn nước đầu ra.
- Khung làm việc dựa trên học máy có khả năng giải thích (interpretable machine learning framework) được đề xuất để dự đoán hiệu quả nitrat hóa (nitrification efficacy) trong hệ thống $\text{MBR}$:
  - Trạng thái nitrat hóa được phân loại nhị phân thành "đạt yêu cầu" ("sufficient") hoặc "chưa đạt yêu cầu" ("insufficient").
  - Khung làm việc tích hợp khả năng giải thích dựa trên mô hình (model-based interpretability) và giải thích hậu nghiệm (post hoc interpretability).
- Ba thuật toán ($3$ algorithms) học máy có khả năng giải thích được đánh giá có hệ thống, xem xét sự đánh đổi giữa độ chệch và phương sai (bias-variance trade-offs) trong phân loại nhị phân:
  - Hồi quy logistic (Logistic Regression - $\text{LR}$).
  - Rừng ngẫu nhiên (Random Forest - $\text{RF}$).
  - Tăng cường độ dốc cực đại (Extreme Gradient Boosting - $\text{XGB}$).
- Sáu đặc trưng đầu vào ($6$ input features) được lựa chọn dựa trên khả năng đo trực tiếp, tính tương thích với cảm biến thương mại và mức độ liên quan đến vận hành thực tế.
- Tiêu chí tối ưu hóa mô hình tập trung vào việc cực đại hóa độ chuẩn xác ($\text{Precision}$) nhằm ngăn ngừa các can thiệp điều khiển sai lệch khi quá trình nitrat hóa chưa đạt yêu cầu:
  - Duy trì tỷ lệ dương tính giả thấp ($\text{FPR}$ - False Positive Rate: phân loại nhầm trạng thái nitrat hóa chưa đạt thành đạt yêu cầu).
  - Đạt tỷ lệ dương tính thật cao ($\text{TPR}$ - True Positive Rate: nhận diện chính xác trạng thái nitrat hóa đạt yêu cầu).
- Cả $\text{LR}$ và $\text{XGB}$ đều đạt điểm số độ chuẩn xác tương đồng $\text{Precision} > 0.85$ trong các điều kiện tiêu chuẩn.
- Kiểm chứng chéo kịch bản (cross-scenario validation) chứng minh mô hình $\text{RF}$ có tính khái quát hóa cao hơn ($\text{Precision} = 0.87$) khi dự đoán trạng thái nitrat hóa trong hệ thống $\text{MBR}$ có bổ sung giá thể sinh học (biocarrier-amended MBRs) bằng dữ liệu huấn luyện từ hệ thống không bổ sung giá thể sinh học, thể hiện khả năng chuyển giao tiềm năng của mô hình.
- Phân tích giải thích hậu nghiệm và phân tích độ ổn định (stability analysis) xác định độ nhạy của dự đoán đối với các giới hạn dữ liệu và độ lệch phân phối (distributional biases), cung cấp cơ sở để cải thiện và triển khai mô hình trong thực tế.
