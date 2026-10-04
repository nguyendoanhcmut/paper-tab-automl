## 2. Methodology

### 2.1. Dataset characteristics and preprocessing
- Nghiên cứu kế thừa tập dữ liệu thực nghiệm do Alnaimat et al. [30] tuyển chọn, ghi nhận quá trình phân hủy điện hóa (electrochemical degradation) của axit perfluorooctanoic (PFOA) dưới nhiều điều kiện khác nhau.
  - Tập dữ liệu bao gồm các kịch bản xử lý riêng biệt, mỗi kịch bản được định nghĩa bởi sự kết hợp giữa các thông số vận hành (operational parameters) và bối cảnh môi trường (environmental contexts).
  - Các biến độc lập then chốt (key independent variables) bao gồm:
    - Thời gian điện phân (electrolysis duration).
    - Mật độ dòng điện (current density).
    - Chủng loại vật liệu cực dương (anode material type) và cực âm (cathode material type).
    - Nồng độ và thành phần chất điện phân (electrolyte concentration and composition).
    - Nền nước (water matrix).
- Các phân tích thăm dò (exploratory analyses) được tiến hành nhằm mô tả đặc tính của biến đầu vào và biến mục tiêu trước khi mô hình hóa:
  - Cấu trúc phụ thuộc giữa các biến dự đoán được thể hiện tại Hình S1 (bản đồ nhiệt tương quan thứ hạng Spearman - Spearman rank-correlation heatmap kèm ký hiệu mức ý nghĩa thống kê).
  - Mối quan hệ hai biến (bivariate relationships) được trực quan hóa tại Hình S2 (biểu đồ phân tán từng cặp với đường khớp LOWESS và chú giải hệ số Pearson/Spearman).
  - Phân phối của biến mục tiêu cùng chẩn đoán phân phối chuẩn tắc Shapiro–Wilk (Shapiro–Wilk normality diagnostic) được trình bày tại Hình S3.
  - Một số biến điện hóa thể hiện mức độ liên kết dương trung bình, điển hình như giữa thời gian điện phân và mật độ dòng điện ($|\rho| \approx 0.35\text{--}0.55$), phản ánh sự đồng biến thiên thực nghiệm điển hình (typical experimental co-variation).
- Quy trình tiền xử lý dữ liệu tuân thủ các quy ước phù hợp với từng thuật toán:
  - Các biến liên tục (continuous variables) được chuẩn hóa theo thang đo điểm chuẩn $z$ ($z\text{-score}$) đối với các mô hình đường cơ sở dựa trên khoảng cách (distance-based) và đạo hàm (gradient-based) nhằm đảm bảo độ ổn định số học và tỷ lệ tương thích.
  - Các mô hình học dựa trên cây (tree-based learners) được huấn luyện trên dữ liệu đầu vào không co giãn (unscaled inputs) nhờ đặc tính bất biến theo thang đo (scale-invariance) của các tiêu chí phân nhánh (split criteria).
  - Các biến mô tả phân loại (categorical descriptors) gồm cực dương (anode), cực âm (cathode), chất điện phân (electrolyte), và nền nước (water matrix) được mã hóa one-hot (one-hot encoded) để duy trì tính bình đẳng giữa các thuật toán đối chuẩn và cho phép tổng hợp lại theo đặc trưng gốc (parent feature) khi giải thích mô hình.
  - Lực lượng phần tử (cardinalities) của mỗi trường đặc trưng đều nhỏ ($\le 6$ giá trị trên mỗi trường), giúp hạn chế độ thưa (sparsity) và số chiều của dữ liệu.

### 2.2. Data splitting and evaluation protocol
- Quy trình đánh giá mô hình áp dụng phân chia giữ lại (holdout partition) theo tỷ lệ $80:20$ có phân tầng (stratified) theo loại cực dương (anode type):
  - Phân tầng theo cực dương nhằm giảm thiểu sự dịch chuyển đồng biến (covariate shift) phát sinh từ phân phối cực dương không đồng đều trên toàn tập dữ liệu.
  - Biến mục tiêu (hiệu suất loại bỏ PFOA, $\%$) không thực hiện phân tầng, phù hợp với bài toán hồi quy (regression setting).
  - Giá trị mầm ngẫu nhiên cố định ($\text{random seed} = 42$) được sử dụng xuyên suốt nhằm đảm bảo tính tái lập (reproducibility).
- Độ ổn định của giao thức phân chia được kiểm chứng qua các lượt chạy lặp lại và các cách thức phân chia dữ liệu thay thế:
  - Độ nhạy của việc phân tầng trên các phân chia thay thế được ghi nhận tại Hình S4 (độ nhạy phân tầng - stratification sensitivity).
  - Quy trình lựa chọn mô hình nội bộ và tính nhất quán về hiệu năng được tổng hợp tại Hình S5 (chẩn đoán kiểm định chéo lồng nhau - nested cross-validation diagnostics).

### 2.3. Automated model selection via FLAML
- Quá trình tự động hóa lựa chọn mô hình và siêu tham số được thực hiện bằng FLAML (Fast Lightweight AutoML):
  - FLAML là khung làm việc AutoML nhận biết chi phí (cost-aware AutoML framework), thay thế quy trình tinh chỉnh thủ công theo dạng lưới (manual grid-style tuning) bằng chiến lược tìm kiếm có giới hạn ngân sách và dừng sớm (budgeted, early-stopped search).
  - Ngân sách thời gian thực tế (wall-time budget) được ấn định cho quá trình tìm kiếm của FLAML là $300\text{ s}$.
  - Cơ chế tìm kiếm của FLAML bao gồm:
    - Khởi tạo với các cấu hình có chi phí tính toán thấp.
    - Phân bổ linh hoạt các lượt thử nghiệm (trials) về phía các vùng thuật toán và siêu tham số có triển vọng.
    - Cắt tỉa (pruning) các lượt chạy kém hiệu quả khi sai số kiểm thực đạt trạng thái bình nguyên (plateau) trong phạm vi ngân sách được cấp.
  - Hàm mục tiêu tối ưu hóa là chỉ số RMSE qua kiểm định chéo 5 lần ($5\text{-fold cross-validation RMSE}$).
  - Cơ chế dừng sớm (early stopping) được áp dụng ở cả hai cấp độ: cấp độ vòng lặp tăng cường (boosting-iteration level) đối với các mô hình học lặp và cấp độ lượt thử nghiệm (trial level) đối với các cấu hình không triển vọng.
  - Tiêu chí hội tụ (convergence) được xác định khi không ghi nhận cải thiện nào trong cửa sổ ngân sách và cấu hình tối ưu đương nhiệm (incumbent) giữ nguyên không đổi qua các đánh giá liên tiếp.
- Mô hình đạt hiệu năng cao nhất do FLAML lựa chọn là bộ hồi quy XGBoost (XGBoost regressor):
  - Tốc độ học ($\text{learning rate}$): $0.1403$.
  - Số lượng cây ($\text{n\_estimators}$): $379$.
  - Số lá tối đa trên mỗi cây ($\text{max\_leaves}$): $13$.
  - Hệ số điều chuẩn L1/L2 ($\text{L1/L2 regularization}$): $\alpha = 0.0995$, $\lambda = 0.0010$.
  - Tỷ lệ lấy mẫu con của quan sát ($\text{subsample}$): $0.85$.
  - Tỷ lệ lấy mẫu con của đặc trưng theo cây ($\text{colsample\_bytree}$): $0.83$.
  - Cấu hình này cân bằng giữa độ chệch và phương sai (bias–variance balance) bằng cách kết hợp tốc độ học vừa phải với độ phức tạp của cây bị ràng buộc và các số hạng điều chuẩn.
  - Toàn bộ không gian tìm kiếm và các siêu tham số được chọn cho XGBoost cùng tất cả các mô hình cơ sở được tổng hợp trong Bảng SI S1 (SI Table S1).

### 2.4. Comparative benchmarking and statistical validation
- Nhằm đối chiếu hiệu năng khách quan, mô hình XGBoost do FLAML tối ưu hóa được đối chuẩn so sánh (benchmarking) với $5$ mô hình hồi quy thông dụng:
  - Cây quyết định (Decision Trees - DT).
  - Rừng ngẫu nhiên (Random Forests - RF).
  - Cây quyết định tăng cường độ dốc (Gradient Boosting Decision Trees - GBDT).
  - Học sâu (Deep Learning - DL).
  - $k$ láng giềng gần nhất ($k\text{-Nearest Neighbors}$ - KNN).
  - Mỗi mô hình đều được đánh giá trên cùng tập dữ liệu mã hóa one-hot và chịu cùng các phân chia huấn luyện - kiểm tra phân tầng giống hệt nhau để đảm bảo tính tương đồng về mặt phương pháp (methodological parity).
- Quy trình đánh giá mô hình sử dụng $10$ lần lặp độc lập của phép phân chia phân tầng tỷ lệ $80:20$ nhằm định lượng độ ổn định qua các lần phân chia khác nhau:
  - Với mỗi lần lặp, $5$ chỉ số hiệu năng được tính toán chi tiết:
    - Sai số toàn phương trung bình (Root Mean Squared Error - RMSE).
    - Sai số tuyệt đối trung bình (Mean Absolute Error - MAE).
    - Sai số phần trăm tuyệt đối trung bình (Mean Absolute Percentage Error - MAPE).
    - Hệ số tương quan Pearson (Correlation Coefficient - CC, ký hiệu $r$).
    - Hệ số xác định (Coefficient of Determination - $R^2$).
  - Các chỉ số RMSE, MAE và MAPE định lượng độ lớn của sai số (error magnitude), trong khi CC ($r$) và $R^2$ tóm tắt mức độ liên kết cùng tỷ lệ phương sai giải thích được (explained variance).
- Kiểm định ý nghĩa thống kê của các khác biệt từng cặp mô hình:
  - Phép kiểm định $t$ ghép cặp hai đuôi (paired two-tailed $t\text{-tests}$) được thực hiện ở mức ý nghĩa $\alpha = 0.01$ trên $10$ lần lặp lại.
  - Hiệu chỉnh Bonferroni (Bonferroni correction) được sử dụng để kiểm soát tỷ lệ sai số trên toàn họ kiểm định (family-wise error rate).
  - Chỉ số kích thước hiệu ứng Cohen's $d$ ($d$ của Cohen) được báo cáo bổ sung để định lượng độ lớn của hiệu ứng (effect sizes).
  - Giao thức này cung cấp phép so sánh có độ ổn định cao trước sự biến động phân chia dữ liệu dưới cùng điều kiện dữ liệu và tiền xử lý, thống nhất với khung phân chia dữ liệu mô tả tại Mục 2.2.

### 2.5. Interpretability via SHAP analysis
- Khả năng diễn giải mô hình được đánh giá bằng SHapley Additive exPlanations (SHAP) dựa trên nền tảng lý thuyết trò chơi hợp tác:
  - SHAP phân bổ đóng góp biên (marginal contribution) của từng đặc trưng vào kết quả dự đoán của từng mẫu cá thể.
  - Các giá trị SHAP được tính toán cho mô hình XGBoost đã huấn luyện và được tổng hợp thành độ quan trọng theo nhóm (grouped importances) bằng cách cộng dồn giá trị tuyệt đối $|\text{SHAP}|$ trên các mức mã hóa one-hot của từng biến phân loại gốc (cực dương, cực âm, chất điện phân, nền nước).
- Đánh giá ảnh hưởng của tương quan đối với gán quyền số của TreeSHAP:
  - Do sự phụ thuộc lẫn nhau giữa các biến dự đoán điện hóa (Hình S1 và Hình S2), nguy cơ sai lệch gán quyền do tương quan được khảo sát bằng cách so sánh thứ hạng SHAP theo nhóm với phân tích độ quan trọng hoán vị có điều kiện (Conditional Permutation Importance - CPI) có nhận biết tương quan.
  - Độ quan trọng hoán vị có điều kiện (CPI) được tính toán bằng cách tái lấy mẫu có điều kiện (conditionally resampling) trong các tầng của các biến dự đoán tương quan để giảm thiểu độ lệch tương quan (correlation bias).
  - Mức độ đồng thuận giữa hai phương pháp xếp hạng được định lượng bằng hệ số hạng Kendall ($\tau$ của Kendall) kèm khoảng tin cậy $95\,\%$ trong Bảng S2 (Table S2).
  - Sự kết hợp này mang lại góc nhìn minh bạch, đặt trong bối cảnh tương quan về ảnh hưởng của các đặc trưng, phục vụ cho việc thiết kế quy trình xử lý và tối ưu hóa điện hóa.
- Hai phân tích bổ sung được triển khai nhằm khảo sát tính ổn định và hành vi liều - đáp ứng (dose–response behaviour):
  - Biểu đồ phụ thuộc SHAP (SHAP dependence plots):
    - Được thiết lập cho $3$ biến liên tục có ảnh hưởng lớn nhất: thời gian điện phân (electrolysis time), nồng độ chất điện phân (electrolyte concentration), và mật độ dòng điện (current density).
    - Màu sắc của các điểm dữ liệu biểu diễn mối quan hệ tương tác với một thông số điện hóa thứ cấp (secondary electrochemical parameter).
  - Kiểm tra độ ổn định loại trừ một biến (Leave-One-Out stability test - LOO):
    - Được tiến hành trên giá trị trung bình $|\text{SHAP}|$ theo nhóm.
    - Thứ hạng đặc trưng trước hết được xác định trên toàn bộ tập dữ liệu gốc, sau đó đặc trưng xếp hạng cao nhất (thời gian điện phân) bị loại bỏ và độ quan trọng SHAP được tính toán lại trên tập dữ liệu đã giản lược.
    - Mức độ đồng thuận giữa hai bảng thứ hạng được tóm tắt bằng hệ số hạng Kendall ($\tau$ của Kendall).

### 2.6. Reproducibility and deployment considerations
- Toàn bộ các phép tính toán được thực thi trên môi trường Python phiên bản $3.10$ với các gói phụ thuộc được kiểm soát phiên bản chặt chẽ:
  - Thư viện FLAML phiên bản $1.2.0$.
  - Thư viện SHAP phiên bản $0.44.0$.
  - Thư viện scikit-learn phiên bản $1.4.0$.
- Toàn bộ đường ống mô hình hóa (modeling pipeline) được đóng gói trong một bộ chứa Docker (Docker container):
  - Đóng gói container nhằm bảo đảm khả năng tái lập đa nền tảng (cross-platform reproducibility) và hỗ trợ thẩm định độc lập từ cộng đồng (peer validation).
  - Cách tiếp cận này tạo bước cải tiến rõ rệt về độ chuẩn hóa môi trường so với các môi trường kịch bản thiếu kiểm soát phiên bản trong các nghiên cứu học máy điện hóa trước đây.

### 2.7. Methodological contributions and distinctions
- Các đóng góp phương pháp luận và điểm khác biệt chính so với nghiên cứu của Alnaimat et al. [30]:
  - Giới thiệu quy trình lựa chọn mô hình tự động hoàn toàn, nhận biết chi phí bằng FLAML thay thế cho quy trình dò tìm lưới hoặc tinh chỉnh thủ công (Bảng S1 - Table S1).
  - Thiết lập giao thức so sánh đối chuẩn bền vững trước phân chia dữ liệu với các đánh giá lặp lại nhiều lần cùng các phép kiểm định ý nghĩa thống kê và kích thước hiệu ứng chính thức.
  - Triển khai lược đồ diễn giải đặt trong ngữ cảnh tương quan, kết hợp báo cáo TreeSHAP theo nhóm song song với độ quan trọng hoán vị có điều kiện (CPI) cùng các thống kê đồng thuận (Bảng S2 - Table S2).
  - Đóng gói toàn bộ đường ống xử lý trong container với các gói phụ thuộc được cố định phiên bản nhằm phục vụ khả năng tái lập từ đầu đến cuối (end-to-end reproducibility).
  - Tổng hòa các yếu tố này hình thành một phương pháp luận minh bạch, hiệu quả và có thể tái tạo dành riêng cho các tập dữ liệu xử lý điện hóa, làm rõ các mức cải thiện hiệu năng và khả năng diễn giải dưới các giả định và thiết lập kiểm định đã được lập thành tài liệu đầy đủ.
