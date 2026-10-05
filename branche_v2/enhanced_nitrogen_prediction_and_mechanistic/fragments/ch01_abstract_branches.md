## Abstract

- Khung học máy có thể giải thích (interpretable machine learning) dự đoán quá trình khử nitơ trong bể phản ứng sinh học màng (MBR) xử lý nước thải độ mặn cao:
  - Nghiên cứu tích hợp phương pháp giải thích Shapley (SHAP) với thuật toán tăng cường độ dốc CatBoost (Categorical Boosting).
  - Mô hình giải quyết khoảng trống then chốt giữa độ chính xác dự đoán và việc ra quyết định điều khiển vận hành hệ thống xử lý nước mặn.
  - CatBoost đạt hiệu năng cao nhất trên tập kiểm tra độc lập cho cả hai chỉ tiêu nitơ đầu ra:
    - Đối với amoni đầu ra ($NH_4^+\text{-N}_{out}$): hệ số xác định $R^2 = 0.88$ và sai số căn bậc hai trung bình bình phương $RMSE = 4.27\ \text{mg/L}$.
    - Đối với tổng nitơ đầu ra ($TN_{out}$): hệ số xác định $R^2 = 0.91$ và sai số $RMSE = 4.35\ \text{mg/L}$.
- Phân tích SHAP làm sáng tỏ vai trò kép của nồng độ muối hòa tan trong hệ vi sinh vật bùn hoạt tính:
  - Độ mặn cao đồng thời ức chế các enzyme nitrat hóa và làm gián đoạn quá trình chuyển hóa nguồn cơ chất cacbon.
  - Nồng độ oxy hòa tan ($DO$), độ $pH$ và hiệu suất khử nhu cầu oxy hóa học ($COD_{eff}$) đóng vai trò là các yếu tố điều hòa then chốt.
  - Nhiệt độ dòng vào và tỷ lệ cacbon trên nitơ ($C/N$) điều tiết động học chuyển hóa tổng nitơ thông qua mức độ sẵn có của chất cho electron.
  - Mô hình kết hợp SHAP và CatBoost liên kết mô hình hóa dự đoán với việc kiểm soát cơ chế sinh hóa thực tế trong các trạm xử lý.
