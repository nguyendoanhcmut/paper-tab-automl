### 2.3 Model construction and optimization

- Quy trình xây dựng, cấu hình không gian tham số và kiểm định các thuật toán học máy:
  - Nghiên cứu thiết lập hệ thống mô hình hóa học máy gồm sáu thuật toán để dự đoán hai chỉ tiêu nitơ đầu ra trong MBR.
  - Sử dụng mười ba biến vận hành thực nghiệm đầu vào để huấn luyện và đánh giá đối chuẩn các thuật toán.

#### 2.3.1 Machine learning algorithms

- Sáu thuật toán học máy học có giám sát được ứng dụng để mô phỏng chất lượng nước thải:
  - Gradient Boosting Decision Trees ($GBDT$): phương pháp học kết hợp xây dựng tuần tự các cây quyết định để sửa lỗi cây trước.
  - Light Gradient Boosting Machine ($LightGBM$): biến thể tối ưu của GBDT sử dụng thuật toán phân chia dựa trên biểu đồ tần số ($histogram$).
  - Random Forest ($RF$): phương pháp kết hợp xây dựng nhiều cây quyết định độc lập trên các tập con ngẫu nhiên của mẫu và đặc trưng.
  - XGBoost: thuật toán tăng cường độ dốc kết hợp kỹ thuật chính quy hóa ($regularization$) và tính toán song song hóa tốc độ cao.
  - Adaptive Boosting ($AdaBoost$): thuật toán gán trọng số lớn hơn cho các mẫu phân loại sai ở các vòng lặp trước để tạo bộ phân loại mạnh.
  - Categorical Boosting ($CatBoost$): thuật toán tăng cường độ dốc sử dụng cấu trúc cây đối xứng và xử lý biến phân loại hiệu quả.

#### 2.3.2 Bayesian optimization

- Tối ưu hóa siêu tham số bằng suy luận Bayes trên mô hình quá trình Gaussian ($Gaussian\ Process$):
  - Phương pháp xây dựng mô hình phân phối xác suất để cân bằng giữa khám phá vùng mới ($exploration$) và khai thác vùng tối ưu ($exploitation$).
  - Không gian tìm kiếm bao gồm tốc độ học ($learning\ rate$), độ sâu cây ($tree\ depth$) và số vòng lặp tối đa.
  - Tối ưu hóa Bayes đạt kết quả tốt hơn tìm kiếm lưới ($grid\ search$) và tìm kiếm ngẫu nhiên ($random\ search$) với số lần thử nghiệm ít hơn.
  - Mối quan hệ giữa dữ liệu quan trắc $D$ và hàm mục tiêu $f$ được mô hình hóa qua hệ phương trình toán học:
    - Tập dữ liệu quan trắc: $D = \{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$
    - Quan hệ quan trắc có sai số: $y_i = f(x_i) + \epsilon_i$, với $x_i$ là véc-tơ quyết định và $\epsilon_i$ là sai số quan trắc.
    - Phân phối xác suất hậu nghiệm theo định lý Bayes: $p(f|D) = \frac{p(D|f) \cdot p(f)}{p(D)}$
    - Trong đó $p(D|f)$ là phân phối hợp lý, $p(f)$ là phân phối tiền nghiệm và $p(D)$ là hợp lý biên.

#### 2.3.3 K-fold cross-validation

- Đánh giá độ ổn định và giảm thiểu độ lệch mô hình bằng kiểm định chéo $10\text{-fold}$:
  - Toàn bộ tập dữ liệu huấn luyện được chia đều thành $k = 10$ tập con có kích thước bằng nhau.
  - Trong mỗi vòng lặp, chín tập con được dùng để huấn luyện và một tập con đóng vai trò tập kiểm định chéo độc lập.
  - Quy trình lặp lại đúng $10$ lần để mỗi mẫu dữ liệu đều được kiểm định đúng một lần.
  - Giá trị trung bình trên các tập gấp phản ánh năng lực khái quát hóa khách quan và giảm thiểu hiện tượng quá khớp ($overfitting$).

#### 2.3.4 Implementation of machine learning models

- Triển khai lập trình mô hình trên ngôn ngữ Python 3.11.4 và thư viện scikit-learn:
  - Môi trường thực thi sử dụng ngôn ngữ Python 3.11.4 kết hợp các gói tính toán khoa học chuẩn.
  - Dữ liệu đầu vào được tiền xử lý qua các bước co giãn tỷ lệ (scaling) và mã hóa số học tương thích với từng mô hình.
  - Cấu hình siêu tham số tối ưu thu được từ quá trình tối ưu hóa Bayes được nạp trực tiếp vào từng mô hình.
  - Thuật toán CatBoost tự động chuyển đổi các đặc trưng phân loại thành đại diện số học trong quá trình huấn luyện.
  - Cấu trúc cây đối xứng của CatBoost giúp nâng cao tốc độ tính toán và kiểm soát nhiễu dữ liệu nồng độ muối cao.
  - Kiểm định chéo 10-fold bảo đảm tính nhất quán trong đánh giá hiệu năng giữa các vòng huấn luyện độc lập.
  - Kết quả kiểm định chéo $10\text{-fold}$ xác nhận CatBoost đạt độ tin cậy cao nhất với $R^2 = 0.78 \pm 0.09$ cho $NH_4^+\text{-N}$ và $0.86 \pm 0.06$ cho $TN$:
  - **Hình 2. Dải giá trị đặc trưng và kết quả kiểm định chéo 10-fold cho 6 thuật toán học máy**
    - <img src="assets/fig_02_p4.jpeg" alt="Hình 2" />
    - Minh họa phân bố dải giá trị đặc trưng (a) và bản đồ nhiệt ma trận tương quan giữa các thông số (b).
    - Biểu đồ thanh hiển thị kết quả kiểm định chéo $10\text{-fold}$ về hệ số $R^2$ và sai số $RMSE$ cho $NH_4^+\text{-N}_{out}$ (c, d) và $TN_{out}$ (e, f).
    - Kết quả kiểm định xác nhận CatBoost đạt giá trị $R^2$ trung bình cao nhất và độ lệch chuẩn thấp nhất so với 5 mô hình còn lại.
