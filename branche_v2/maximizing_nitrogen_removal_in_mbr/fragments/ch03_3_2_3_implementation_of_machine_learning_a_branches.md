### 2.3 Implementation of machine learning algorithms

- Hai thuật toán học máy được triển khai để giải bài toán hồi quy đa biến
  - Rừng ngẫu nhiên (Random Forest Regressor - $\text{RFR}$) hoạt động theo nguyên lý tập hợp (ensemble) kết hợp kết quả từ nhiều cây quyết định độc lập.
  - Mỗi cây trong $\text{RFR}$ được huấn luyện trên một tập con ngẫu nhiên của dữ liệu và đặc trưng để giảm thiểu hiện tượng quá khớp (overfitting).
  - Mạng nơ-ron sâu ($\text{DNN}$) được thiết kế với nhiều tầng liên kết đầy đủ (Dense layers) để học các mối quan hệ phi tuyến tính phức tạp thông qua thuật toán lan truyền ngược.
- Thiết lập môi trường phần mềm và cấu trúc mạng nơ-ron
  - Mô hình $\text{RF}$ được xây dựng bằng lớp `RandomForestRegressor` trong thư viện `scikit-learn`.
  - Mô hình $\text{DNN}$ được phát triển trên nền tảng `TensorFlow/Keras` với kiến trúc tuần tự (`Sequential`), tích hợp kỹ thuật ngắt kết nối ngẫu nhiên (`Dropout`) để chống quá khớp.
  - Các thư viện hỗ trợ xử lý dữ liệu và thống kê bao gồm `pandas`, `numpy`, `matplotlib` và `seaborn`.
- Hệ thống $18$ thông số đầu vào và $3$ chỉ tiêu đầu ra được mã hóa chuẩn xác
  - Phân vùng kỵ khí gồm $5$ biến: nhiệt độ ($\text{Tem-An}$, $^\circ\text{C}$), $\text{pH-An}$, nồng độ bùn ($\text{MLSS-An}$, $\text{mg/L}$), oxy hòa tan ($\text{DO-An}$, $\text{mg/L}$) và thế oxy hóa khử ($\text{ORP-An}$, $\text{mV}$).
  - Phân vùng thiếu khí/chuyển đổi gồm $5$ biến: $\text{Tem-Ax}$ ($^\circ\text{C}$), $\text{pH-Ax}$, $\text{MLSS-Ax}$ ($\text{mg/L}$), $\text{DO-Ax}$ ($\text{mg/L}$) và $\text{ORP-Ax}$ ($\text{mV}$).
  - Phân vùng hiếu khí gồm $6$ biến: $\text{Tem-Ae}$ ($^\circ\text{C}$), $\text{pH-Ae}$, $\text{MLSS-Ae}$ ($\text{mg/L}$), nồng độ bùn bay hơi ($\text{MLVSS-Ae}$, $\text{mg/L}$), $\text{DO-Ae}$ ($\text{mg/L}$) và chỉ số thể tích bùn ($\text{SVI-Ae}$, $\text{mL/g}$).
  - Bể giảm oxy hòa tan và dòng hồi lưu gồm $2$ biến: $\text{DO-R}$ ($\text{mg/L}$) và lưu lượng bùn tuần hoàn ($\text{Sludge-R}$, $\text{m}^3/\text{ngày}$).
  - Ba mục tiêu chất lượng nước đầu ra cần dự đoán đồng thời: $\text{COD}$ ($\text{mg/L}$), $\text{TN}$ ($\text{mg/L}$) và $\text{TP}$ ($\text{mg/L}$).
- Tiêu chí lựa chọn mô hình phục vụ tối ưu hóa hệ thống
  - Đánh giá song song giữa phương pháp học máy tập hợp và mạng nơ-ron sâu trên cùng một tập dữ liệu chuẩn hóa.
  - Thuật toán đạt độ chính xác cao nhất được chọn làm mô hình nền tảng cho phân tích giải thích bằng $\text{SHAP}$ và tối ưu hóa vận hành.
