## Abstract

- Phát triển các mô hình machine learning (ML - học máy) nhằm dự đoán hiệu suất loại bỏ chất dinh dưỡng (nutrient removal) trong hệ thống màng lọc sinh học kỵ khí - thiếu khí - hiếu khí ($A^2O\text{-MBR}$ / anaerobic-anoxic-oxic membrane bioreactor).
- Ứng dụng mô hình extreme gradient boosting (XGBoost) kết hợp chiến lược tối ưu hóa tìm kiếm theo lưới (Grid-XGBoost / grid search strategy) để dự đoán hiệu suất loại bỏ các chất dinh dưỡng gồm ammonium ($\text{NH}_4$), tổng phốt pho ($\text{TP}$ / total phosphorus), và tổng nitơ ($\text{TN}$ / total nitrogen).
- Đối chứng và kiểm chứng hiệu năng mô hình với mạng nơ-ron nhân tạo multilayer perceptron (MLP - perceptron đa tầng) phổ biến.
- Phân chia các thông số đầu vào (input parameters) thành hai nhóm:
  - Nhóm điều kiện vận hành (operating conditions): oxy hòa tan ($\text{DO}$ / dissolved oxygen), thế oxy hóa - khử ($\text{ORP}$ / oxidation-reduction potential), và nồng độ chất rắn lơ lửng trong hỗn hợp bùn lỏng ($\text{MLSS}$ / mixed liquor suspended solids).
  - Nhóm đặc tính nước thải đầu vào (influent characteristics): $\text{NH}_4$, $\text{TN}$, $\text{TP}$, tổng hàm lượng carbon hữu cơ ($\text{TOC}$ / total organic content), nhu cầu oxy hóa học ($\text{COD}$ / chemical oxygen demand), và chất rắn lơ lửng ($\text{SS}$ / suspended solids).
- Phát triển tổng cộng $9$ mô hình cho mỗi kỹ thuật ML, khảo sát độc lập trên từng bộ dữ liệu điều kiện vận hành, đặc tính nước đầu vào và kết hợp cả hai bộ dữ liệu cho từng chất dinh dưỡng mục tiêu (trên tập dữ liệu gồm $7{,}897$ mẫu / samples).
- Việc chỉ sử dụng riêng rẽ nhóm thông số điều kiện vận hành hoặc nhóm đặc tính nước đầu vào làm đầu vào cho mô hình XGBoost và MLP đều mang lại kết quả dự đoán kém.
- Hiệu quả dự đoán (predictive efficacy) của mô hình được cải thiện đáng kể khi kết hợp đồng thời toàn bộ các thông số để dự đoán loại bỏ chất dinh dưỡng mục tiêu.
- Dự đoán hiệu suất loại bỏ $\text{NH}_4$ bằng mô hình XGBoost đạt các giá trị hệ số xác định ($R^2$) cao nhất:
  - $R^2 = 0.763$ khi chỉ sử dụng nhóm thông số điều kiện vận hành.
  - $R^2 = 0.814$ khi chỉ sử dụng nhóm thông số đặc tính nước đầu vào.
  - $R^2 = 0.876$ khi kết hợp cả hai nhóm thông số (combined dataset).
- Mô hình ensemble XGBoost thể hiện hiệu suất vượt trội so với mô hình MLP trong tất cả các kịch bản thử nghiệm.
- Cả hai mô hình (XGBoost và MLP) đều không đạt yêu cầu độ chính xác (inadequate) khi dự đoán hiệu suất loại bỏ $\text{TN}$ và $\text{TP}$ trong mọi kịch bản.
- Mô hình XGBoost đề xuất chứng minh là một kỹ thuật ML tin cậy và mạnh mẽ (reliable and robust) cho dự đoán loại bỏ $\text{NH}_4$, hỗ trợ hiệu quả công tác ra quyết định trước để nâng cao hiệu suất vận hành hệ thống $A^2O\text{-MBR}$.
