#### 2.1.4 k-nearest neighbors

- $k$-nearest neighbors ($KNN$ - $k$ láng giềng gần nhất) là một mô hình học máy không giám sát (unsupervised machine learning model) đo lường khoảng cách giữa các giá trị đặc trưng (feature values) khác nhau làm cơ sở cho phân loại (classification) hoặc hồi quy (regression).
  - Mô hình $KNN$ được áp dụng để giải quyết bài toán phân loại (classification problem).
  - Đối với bài toán hồi quy (regression problem), phương pháp bao gồm việc xác định $k$ láng giềng gần nhất ($k$-nearest neighbors) của mẫu cần dự đoán.
- $KNN$ sở hữu các ưu điểm rõ rệt bao gồm độ chính xác cao (high precision), tính không nhạy với các giá trị ngoại lai (insensitivity to outliers), và không có giả định đầu vào đối với nhãn mẫu (no input assumption for sample labels).
  - $KNN$ tồn tại một số nhược điểm nhất định, bao gồm độ phức tạp tính toán (computational complexity) và độ phức tạp không gian (space complexity) cao.
  - Do các đặc tính trên, $KNN$ chủ yếu áp dụng phù hợp để xử lý dữ liệu dạng số (numerical data) và dữ liệu định danh (nominal data).
- $KNN$ có phạm vi ứng dụng trong lĩnh vực môi trường (environmental domain) hạn chế hơn (more circumscribed range of applications) so với $SVM$, $ANN$ và các mô hình cây (tree models).
  - Tuy vậy, mô hình vẫn có thể được triển khai để giải quyết nhiều bài toán môi trường phức tạp:
    - Giám sát chất lượng nước (water quality monitoring) (Uddin et al., 2023).
    - Kiểm soát xử lý nước thải (wastewater treatment control) (Xu et al., 2022).
    - Đánh giá quá trình hấp phụ (adsorption evaluation) (Nguyen et al., 2022).
    - Dự đoán chất lượng không khí (air quality prediction) (Tella et al., 2021).
