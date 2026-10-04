#### 3.3.2 Other model applications

- **Các mô hình học máy khác ngoài ANN được ứng dụng trong dự đoán nghẽn màng MBR**: Bên cạnh mạng nơ-ron nhân tạo (ANN - Artificial Neural Network), các mô hình khác như SVM (Support Vector Machine - máy vector hỗ trợ, bao gồm cả SVR - Support Vector Regression), least squares SVM (LSSVM - máy vector hỗ trợ bình phương tối thiểu), RF (Random Forest - rừng ngẫu nhiên), limit GBDT và GBDT (Gradient Boosting Decision Tree - cây quyết định tăng cường gradient) cũng đã được áp dụng để dự đoán tắc nghẽn màng (membrane fouling prediction) trong các hệ MBR (Membrane Bioreactor - bể phản ứng sinh học màng):
  - Bảng S4 trong Phụ lục A (Table S4 in Appendix A) trình bày các ví dụ về việc sử dụng SVM hoặc các mô hình dựa trên cây (tree-based models) để dự đoán hiện tượng nghẽn màng.
  - Mặc dù mức độ ứng dụng của những mô hình này không phổ biến rộng rãi như ANN, chúng vẫn thể hiện khả năng dự đoán tốt trong nhiều tình huống và kịch bản khác nhau.

- **Mô hình LSSVM giúp đơn giản hóa việc tối ưu hóa hệ phương trình tuyến tính**: Hamedi và cộng sự (2019) đã thiết lập một mô hình LSSVM để đơn giản hóa quá trình tối ưu hóa một hệ phương trình tuyến tính (linear equation system):
  - Các thông số đầu vào được lựa chọn gồm MLSS (Mixed Liquor Suspended Solids - chất rắn lơ lửng trong bùn lỏng), TMP (Transmembrane Pressure - áp suất xuyên màng), thông lượng (flux) và nhiệt độ (temperature) để dự đoán trở lực lọc (filtration resistance).
  - Mô hình LSSVM đạt hiệu suất cao hơn cả mô hình PSO-MLP ($R^2 = 0.96$) và mô hình lập trình biểu thức gen (gene expression programming model, $R^2 = 0.98$), đạt giá trị $R^2 = 0.99$.

- **Mô hình Random Forest (RF) trong dự đoán thông lượng màng và so sánh hiệu suất**: Li và cộng sự (2020) đã phát triển một mô hình RF với $300$ cây ($300\text{ trees}$) và $2$ biến nút ($2\text{ node variables}$):
  - MLSS, TMP và trở lực màng (membrane resistance) được chọn làm các đặc trưng đầu vào chính, sau khi được đánh giá sơ bộ thông qua phân tích thành phần chính (PCA - Principal Component Analysis), để dự đoán thông lượng màng (membrane flux).
  - Kết quả cho thấy mô hình RF ($R^2 = 0.95$) đạt hiệu suất cao hơn so với mô hình SVM ($R^2 = 0.92$) và mô hình MLP ($R^2 = 0.89$).
  - Từ ví dụ nghiên cứu này, các mô hình RF cho thấy khả năng phù hợp hơn so với mô hình SVM và MLP trong việc dự đoán tắc nghẽn màng.

- **Ý nghĩa của việc dùng PCA và triển vọng quan trắc trực tuyến**: Việc ứng dụng PCA để lựa chọn đặc trưng trong các nghiên cứu này chỉ ra khả năng xảy ra hiện tượng đa cộng tuyến (multicollinearity) giữa các nhân tố tác động đến tắc nghẽn màng:
  - Mặc dù các yếu tố đóng góp vào quá trình nghẽn màng mang tính phức tạp, một số ít chỉ số mang tính đại diện có thể được chọn lọc để phục vụ quan trắc và dự đoán trực tuyến (online monitoring and prediction).
