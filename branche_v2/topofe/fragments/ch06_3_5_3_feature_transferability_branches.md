### 5.3 Feature Transferability

- **Mục tiêu và thiết lập đánh giá tính khả chuyển đặc trưng (Feature Transferability)**:
  - Một đặc tính sống còn của phương pháp kỹ nghệ đặc trưng (feature engineering) là các phép biến đổi được phát hiện phải mã hóa cấu trúc nội tại của tập dữ liệu (dataset-intrinsic structure), thay vì trở thành các dị vật phụ thuộc vào mô hình được dùng ở pha tìm kiếm (search-time model artifacts).
  - Quy trình thực nghiệm: Cố định toàn bộ các chương trình đặc trưng được tiến hóa thông qua XGBoost, sau đó áp dụng trực tiếp ma trận đặc trưng mở rộng (augmented feature matrix)—hoàn toàn không tái tạo (regenerating), không chọn lọc lại (reselecting) hay sửa đổi—sang các mô hình đích gồm CatBoost, MLP và TabPFN, với Qwen2.5-Coder-7B đóng vai trò mô hình nền tảng (backbone).
- **Kết quả chuyển giao sang CatBoost và tính bất biến thuật toán**:
  - CatBoost đạt điểm số $0.849$ ($+1.43\%$) và $\text{RMSE} = 2.624$ ($-2.05\%$) theo Bảng 4 (Table 4).
  - Kết quả này khẳng định các đặc trưng của TOPOFE chuyển giao trơn tru mà không bị suy giảm hiệu năng (transfer without degradation) giữa các biến thể gradient boosting có cơ chế thuật toán cốt lõi hoàn toàn khác nhau, chứng minh các đặc trưng không bị quá khớp (overfit) vào thuật toán tìm điểm chia (split-finding algorithm) của XGBoost.
- **Phân tích hiệu năng trên mô hình nơ-ron MLP và yêu cầu phân phối**:
  - MLP thể hiện hiệu năng dưới mức kỳ vọng (underperforms), tuy nhiên sự sụt giảm này xuất phát từ độ nhạy cố hữu đã được chứng minh của các thuật toán tối ưu hóa mạng nơ-ron đối với các phân phối đặc trưng lệch chưa chuẩn hóa (unnormalized skewed feature distributions) chứ không phải do sự thất bại của tính khả chuyển.
  - Việc áp dụng chuẩn hóa tiêu chuẩn (standard normalization) được kỳ vọng sẽ thu hẹp đáng kể khoảng cách hiệu năng này.
- **Hiện tượng siêu chuyển giao (Super-transfer) trên TabPFN**:
  - TabPFN đạt hiệu năng cao nhất trên cả hai tác vụ, thậm chí vượt qua mô hình tham chiếu tìm kiếm XGBoost oracle thêm $4.30\%$ và $3.29\%$.
  - Hiện tượng siêu chuyển giao (super-transfer) này chứng minh rằng các chương trình đặc trưng của TOPOFE mã hóa cấu trúc dữ liệu phong phú hơn mức một mô hình đại diện (surrogate model) đơn lẻ có thể khai thác trọn vẹn.
  - Cơ chế chú ý được meta-học (meta-learned attention mechanism) của TabPFN đặc biệt tương thích để khai thác các biểu diễn trực giao (orthogonal representations)—bao gồm số học (arithmetic), thời gian (temporal), dựa trên thứ hạng (rank-based) và tổng hợp (aggregation)—được sản sinh từ các đảo chuyên biệt theo họ (family-specialized islands) của TOPOFE.
- **Tính khái quát và khả năng thích ứng của biểu diễn đặc trưng**:
  - Tính khả chuyển là một thuộc tính ổn định, độc lập với tác vụ (task-agnostic) của các chương trình đặc trưng TOPOFE.
  - Biên độ cải thiện tỷ lệ thuận với năng lực của từng mô hình dự đoán trong việc khai thác các biểu diễn có cấu trúc và độ dư thừa thấp (structured low-redundancy representations).
