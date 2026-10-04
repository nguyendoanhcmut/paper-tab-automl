### Predicting nitrogen removal performance in literature-based anammox processes

- Dựa trên phân tích tương quan từng cặp (pairwise correlation analysis, Fig. S3), toàn bộ $15$ biến bao gồm $6$ biến phân loại (categorical variables) và $9$ biến số trị (numerical variables) được lựa chọn làm các biến đầu vào để dự đoán độc lập từng biến trong số $7$ biến đầu ra của quy trình anammox:
  - Bảy biến mục tiêu đầu ra được mô hình hóa riêng biệt gồm: $\text{NH}_4^+ \text{-N}$ đầu ra (effluent $\text{NH}_4^+ \text{-N}$), $\text{NO}_3^- \text{-N}$ đầu ra (effluent $\text{NO}_3^- \text{-N}$), $\text{NO}_2^- \text{-N}$ đầu ra (effluent $\text{NO}_2^- \text{-N}$), tổng nitơ vô cơ đầu ra (effluent $\text{TIN}$), hiệu suất loại bỏ $\text{NH}_4^+ \text{-N}$ ($\text{NH}_4^+ \text{-N}$ removal efficiency), hiệu suất loại bỏ $\text{TIN}$ ($\text{TIN}$ removal efficiency), và tốc độ loại bỏ nitơ qua con đường anammox ($\text{NARR}$).
  - Tập $15$ biến đầu vào này được lựa chọn do không tồn tại đa cộng tuyến tiềm ẩn (lacked potential multicollinearity).
- Các mô hình dạng GBM (GBM-like models, bao gồm Gradient Boosting Machine: GBM và XGBoost) thể hiện lợi thế nổi bật trong việc dự đoán toàn bộ $7$ biến đầu ra:
  - Bảng 1 (Table 1) và phần Thông tin bổ sung (Supporting Information) tóm tắt hiệu suất tối ưu và cấu hình mô hình tốt nhất đối với từng biến mục tiêu qua thuật toán H2O AutoML với $5$ hạt phân chia dữ liệu (five data splitting seeds):
    - Đối với effluent $\text{NH}_4^+ \text{-N}$: Mô hình tối ưu là GBM, đạt Training $\text{MAE} = 0.171$, Training $R^2 = 0.994$, Validation $\text{MAE} = 1.951$, Validation $R^2 = 0.914$, Testing $\text{MAE} = 1.889$, Testing $R^2 = 0.928$.
    - Đối với effluent $\text{NO}_3^- \text{-N}$: Mô hình tối ưu là XGBoost, đạt Training $\text{MAE} = 0.048$, Training $R^2 = 0.998$, Validation $\text{MAE} = 1.677$, Validation $R^2 = 0.727$, Testing $\text{MAE} = 1.626$, Testing $R^2 = 0.824$.
    - Đối với effluent $\text{NO}_2^- \text{-N}$: Mô hình tối ưu là XGBoost, đạt Training $\text{MAE} = 0.004$, Training $R^2 = 0.999$, Validation $\text{MAE} = 0.546$, Validation $R^2 = 0.949$, Testing $\text{MAE} = 0.496$, Testing $R^2 = 0.962$.
    - Đối với effluent $\text{TIN}$: Mô hình tối ưu là XGBoost, đạt Training $\text{MAE} = 0.215$, Training $R^2 = 0.996$, Validation $\text{MAE} = 3.141$, Validation $R^2 = 0.916$, Testing $\text{MAE} = 3.366$, Testing $R^2 = 0.910$.
    - Đối với hiệu suất loại bỏ $\text{NH}_4^+ \text{-N}$ ($\text{NH}_4^+ \text{-N}$ removal efficiency): Mô hình tối ưu là XGBoost, đạt Training $\text{MAE} = 0.305$, Training $R^2 = 0.996$, Validation $\text{MAE} = 3.638$, Validation $R^2 = 0.832$, Testing $\text{MAE} = 3.975$, Testing $R^2 = 0.882$.
    - Đối với hiệu suất loại bỏ $\text{TIN}$ ($\text{TIN}$ removal efficiency): Mô hình tối ưu là XGBoost, đạt Training $\text{MAE} = 0.320$, Training $R^2 = 0.991$, Validation $\text{MAE} = 5.583$, Validation $R^2 = 0.731$, Testing $\text{MAE} = 5.252$, Testing $R^2 = 0.814$.
    - Đối với $\text{NARR}$: Mô hình tối ưu là XGBoost, đạt Training $\text{MAE} = 0.002$, Training $R^2 = 0.999$, Validation $\text{MAE} = 0.013$, Validation $R^2 = 0.981$, Testing $\text{MAE} = 0.014$, Testing $R^2 = 0.993$.

| Biến mục tiêu dự đoán (Predicted target) | Mô hình tối ưu (Optimized model) | Training MAE | Training $R^2$ | Validation MAE | Validation $R^2$ | Testing MAE | Testing $R^2$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Effluent $\text{NH}_4^+ \text{-N}$ | GBM | $0.171$ | $0.994$ | $1.951$ | $0.914$ | $1.889$ | $0.928$ |
| Effluent $\text{NO}_3^- \text{-N}$ | XGBoost | $0.048$ | $0.998$ | $1.677$ | $0.727$ | $1.626$ | $0.824$ |
| Effluent $\text{NO}_2^- \text{-N}$ | XGBoost | $0.004$ | $0.999$ | $0.546$ | $0.949$ | $0.496$ | $0.962$ |
| Effluent $\text{TIN}$ | XGBoost | $0.215$ | $0.996$ | $3.141$ | $0.916$ | $3.366$ | $0.910$ |
| $\text{NH}_4^+ \text{-N}$ removal efficiency | XGBoost | $0.305$ | $0.996$ | $3.638$ | $0.832$ | $3.975$ | $0.882$ |
| $\text{TIN}$ removal efficiency | XGBoost | $0.320$ | $0.991$ | $5.583$ | $0.731$ | $5.252$ | $0.814$ |
| $\text{NARR}$ | XGBoost | $0.002$ | $0.999$ | $0.013$ | $0.981$ | $0.014$ | $0.993$ |

- GBM được công nhận là một thuật toán học máy có giám sát (supervised machine learning algorithm) mạnh mẽ theo phương thức học kết hợp (ensemble):
  - Lợi thế hiệu suất rõ nét của GBM bắt nguồn từ việc tích hợp các kỹ thuật điều chuẩn (regularization techniques) giúp ngăn ngừa hiện tượng quá khớp (overfitting) hiệu quả.
  - Thuật toán sở hữu tính năng tích hợp sẵn nhằm xử lý các giá trị khuyết thiếu (built-in handling of missing values), các thuật toán cắt tỉa cây hiệu quả (efficient tree-pruning algorithms) cùng khả năng xử lý tính toán song song (parallel processing capabilities).
  - GBM ứng dụng các phương pháp tiên tiến để giải quyết tình trạng dữ liệu mất cân bằng (imbalanced data).
  - Sự kết hợp đồng thời của các tính năng này giúp tăng cường tính hiệu quả (efficiency), độ chính xác (accuracy) và độ ổn định (stability) của mô hình khi đối mặt với các kịch bản dữ liệu phức tạp, đưa GBM trở thành lựa chọn lý tưởng cho nhiều bài toán học máy.
  - Trước đây, GBM cũng đã từng đạt hiệu suất dự đoán cao trong việc mô phỏng hàm lượng tổng nitơ (total nitrogen) trong nước thải đầu vào của các nhà máy xử lý nước thải (WWTPs) và mô phỏng mức tiêu thụ năng lượng của WWTPs.
- Hiệu suất mô hình trên các tập dữ liệu huấn luyện, kiểm định và kiểm tra phản ánh tính hữu ích của bộ dữ liệu lớn và cơ chế xếp hạng của AutoML:
  - Sai số $\text{MAE}$ tập huấn luyện ở mức thấp cùng giá trị $R^2$ tập huấn luyện rất cao ($0.991\text{--}0.999$) chứng minh rằng bộ dữ liệu lớn thu thập từ các quá trình anammox trong y văn (literature-based anammox processes) rất hữu ích cho công tác huấn luyện mô hình học máy.
  - Hiệu suất trên tập kiểm định (validation performance) thấp hơn so với tập huấn luyện nhưng vẫn đáp ứng tốt yêu cầu dự đoán với $R^2 = 0.727\text{--}0.981$.
  - Đáng chú ý, hiệu suất trên tập kiểm tra (testing performance) của các mô hình này đạt $R^2 = 0.814\text{--}0.993$, cao hơn hiệu suất trên tập kiểm định do bảng xếp hạng mô hình (modeling leaderboard) được sắp xếp dựa trên chính hiệu suất của tập kiểm tra.
