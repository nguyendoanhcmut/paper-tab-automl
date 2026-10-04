#### 2.2.7. Evaluation metrics and hyperparameter tuning criteria

- Đánh giá hiệu năng của các mô hình phân loại (classification models) thông qua ma trận nhầm lẫn (confusion matrix), đối chiếu kết quả dự đoán ("Sufficient" / "Insufficient") với điều kiện vận hành thực tế:
  - Nhãn "Positive" biểu thị trạng thái nitrate hóa đầy đủ (sufficient nitrification), trong khi nhãn "Negative" biểu thị trạng thái nitrate hóa không đầy đủ (insufficient nitrification), theo định nghĩa tại Section 2.1.
  - Các chỉ số cốt lõi trong ma trận nhầm lẫn bao gồm (Section 2.2.1):
    - True positive ($\text{TP}$): Phân loại chính xác trạng thái nitrate hóa đầy đủ (correctly classified sufficient nitrification).
    - False positive ($\text{FP}$): Phân loại sai thành nitrate hóa đầy đủ trong điều kiện thực tế không đầy đủ (erroneously classified sufficient under insufficient conditions).
    - False negative ($\text{FN}$): Phân loại sai thành nitrate hóa không đầy đủ dù thực tế đạt mức đầy đủ (insufficient misclassifications despite actual sufficiency).
    - True negative ($\text{TN}$): Phân loại chính xác trạng thái nitrate hóa không đầy đủ (accurate classified as insufficient).
- Cực tiểu hóa tỷ lệ dương tính giả (false positive rate - $\text{FPR}$) là yêu cầu then chốt nhằm bảo đảm chất lượng nước đầu ra (effluent water quality) an toàn:
  - Trong hệ thống điều khiển tích hợp mô hình giám sát nitrate hóa, khi xảy ra hiện tượng nitrate hóa không đầy đủ, lượng không khí cấp vào cần được tăng cường (more air should be supplied).
  - Khi xảy ra lỗi $\text{FP}$, mô hình dự đoán sai thành trạng thái nitrate hóa đầy đủ, dẫn đến việc hệ thống điều khiển ngừng bổ sung thêm oxy, gây ra tình trạng nước thải đầu ra không an toàn và không thích hợp để tái sử dụng (unsafe effluent unsuitable for reuse).
- Tỷ lệ dương tính thật (true positive rate - $\text{TPR}$) cao hơn là yêu cầu cần thiết để phát hiện trạng thái nitrate hóa đầy đủ trong các điều kiện vận hành thông thường (conventional operation conditions):
  - Mức $\text{TPR}$ cao giúp giảm chi phí vận hành (operational costs) bằng cách ngăn chặn việc cấp oxy không cần thiết do lỗi $\text{FN}$ kích hoạt (preventing unnecessary oxygen supply triggered by $\text{FN}$).
- Tối ưu hóa đơn lẻ để giảm $\text{FPR}$ có thể làm suy giảm nghiêm trọng $\text{TPR}$ theo các ghi nhận từ các nghiên cứu trước (Reynaert et al., 2023; Salvia et al., 2021; Yang et al., 2019):
  - Nghiên cứu áp dụng phương pháp tiếp cận cân bằng, đồng thời xem xét cả $\text{TPR}$ (Eq. 1) và $\text{FPR}$ (Eq. 2).
  - Độ chuẩn xác ($\text{Precision}$, Eq. 3) được chọn làm chỉ số tối ưu hóa then chốt (key optimization metric).
  - Chỉ số $\text{Precision}$ phản ánh tỷ lệ các dự đoán $\text{TP}$ trong tổng số tất cả các dự đoán dương tính (positive predictions).
- Các phương trình toán học xác định $\text{TPR}$, $\text{FPR}$ và $\text{Precision}$:
  - Tỷ lệ dương tính thật ($\text{TPR}$):
    $$\text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}} \quad (1)$$
  - Tỷ lệ dương tính giả ($\text{FPR}$):
    $$\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}} \quad (2)$$
  - Độ chuẩn xác ($\text{Precision}$):
    $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \quad (3)$$
- Độ chính xác ($\text{Accuracy}$) đại diện cho tỷ lệ các dự đoán chính xác trên tổng số tất cả các trường hợp và được sử dụng để đánh giá mô hình trên các nhóm kiểm tra (test groups):
  - Mặc dù $\text{Precision}$ được ưu tiên trong quá trình tinh chỉnh siêu tham số (hyperparameter tuning), $\text{Accuracy}$ vẫn được sử dụng kết hợp để đánh giá mô hình.
  - Phương trình tính toán $\text{Accuracy}$ (Eq. 4):
    $$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \quad (4)$$
- Đánh giá độ ổn định của hiệu năng mô hình (stability of model performance) trên tập dữ liệu kiểm tra (test dataset) bằng cách tính toán khoảng tin cậy $95\,\%$ ($95\text{ \% confidence intervals}$):
  - Kỹ thuật tái lấy mẫu bootstrap $1000$ lần ($1000\text{-times bootstrap resampling}$) được triển khai theo các thực hành chuẩn trong kiểm định học máy (standard practices in machine learning validation).
  - Khoảng tin cậy $95\,\%$ được xác định cho các chỉ số $\text{Accuracy}$, $\text{Precision}$, độ nhạy ($\text{Recall}$), và điểm số $F_1$ ($F_1\text{ score}$).
