### 2.5. Machine learning model selection and training

- Nghiên cứu đánh giá $16$ thuật toán hồi quy (regression algorithms) thuộc $6$ họ mô hình hóa (modelling families) nhằm dự báo $3$ biến mục tiêu (targets) từ $7$ thông số vận hành (operational parameters) (Bảng 2 / Table 2):
  - Danh mục mô hình được xây dựng như một phép kiểm định giả thuyết có cấu trúc (structured hypothesis test) thay vì một bài toán mô hình hóa không định hướng (undirected modelling exercise).
  - Mỗi họ mô hình kiểm định một giả thuyết có thể bác bỏ (falsifiable hypothesis) về cấu trúc của mối quan hệ sinh học – màng lọc (biology–membrane relationship).
- Sáu họ mô hình hóa và các giả thuyết kiểm định tương ứng:
  - Các mô hình tuyến tính và tuyến tính điều chuẩn (Linear and regularised linear models): kiểm định xem mối quan hệ có tính cộng tính (adequately additive) và đơn điệu (monotonic) thỏa đáng hay không, trong đó kỹ thuật điều chuẩn (regularisation) thăm dò thêm liệu tầm quan trọng biểu kiến (apparent importance) có phải là một hiện tượng giả tạo do cộng tuyến (artefact of collinearity) hay không.
  - Hồi quy vector hỗ trợ với nhân hàm bán kính cơ sở RBF (Support vector regression - SVR with an RBF kernel): kiểm định xem một mặt cong phi tuyến trơn toàn cục (smooth global non-linear surface) có đáp ứng đầy đủ hay không.
  - K láng giềng gần nhất (K-nearest neighbours - KNN): kiểm định xem hành vi tắc nghẽn màng (fouling behaviour) có tính đều cục bộ (locally regular) trong không gian vận hành hay không (tức các điều kiện tương đồng có tạo ra các phản hồi tương đồng một cách đáng tin cậy hay không) — giả định nền tảng cho mọi khuyến nghị về cửa sổ vận hành (operating-window recommendation).
  - Các mô hình tổ hợp dựa trên cây (Tree-based ensembles): kiểm định xem các hiệu ứng ngưỡng (threshold effects) và tương tác đặc trưng (feature interactions) có chi phối hay không, theo đúng dự đoán của lý thuyết tắc nghẽn màng cổ điển (classical fouling theory).
    - Phép đối chiếu giữa bagging và boosting (bagging-versus-boosting contrast) bên trong họ mô hình cây kiểm định xem giảm phương sai (variance reduction) hay giảm độ chệch tuần tự (sequential bias reduction) là giải pháp phản hồi tốt hơn đối với dữ liệu cảm biến công nghiệp chứa nhiễu (noisy industrial sensor data).
  - Mạng perceptron đa tầng với $2$ lớp ẩn (Multi-layer perceptron - MLP with two hidden layers): kiểm định xem các biểu diễn phân cấp (hierarchical representations) có đóng góp thêm giá trị nào vượt ngoài các mô hình trên hay không.
- Quy luật thành công và thất bại của các họ mô hình cung cấp bằng chứng thực nghiệm về cấu trúc tắc nghẽn màng trong hệ thống (được báo cáo tại Mục 3.1 / Section 3.1):
  - Một mô hình duy nhất (single model) được lựa chọn tiếp nối cho phân tích giải thích (interpretation) và tối ưu hóa (optimisation) nhằm duy trì tính nhất quán của khung phân tích trên cả $3$ biến mục tiêu.
- Cấu hình triển khai, siêu tham số và thư viện phần mềm:
  - Công thức toán học (formulations), siêu tham số (hyperparameters) và cấu hình huấn luyện (training configurations) cho toàn bộ $16$ thuật toán được cung cấp tại Mục S3 (Section S3) và Bảng S2 (Table S2).
  - Toàn bộ quy trình tính toán được thực hiện trong môi trường Python 3.10 sử dụng các thư viện NumPy, pandas, scikit-learn, XGBoost, LightGBM và SHAP.
