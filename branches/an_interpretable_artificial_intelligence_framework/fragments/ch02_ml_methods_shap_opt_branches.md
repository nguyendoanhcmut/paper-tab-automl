## 2. Mô hình và phương pháp: Học máy, SHAP & Tối ưu hóa

### 2.5. Lựa chọn và huấn luyện mô hình học máy

#### 2.5.1. Khảo sát 16 thuật toán qua 6 họ mô hình và kiểm định giả thuyết cấu trúc
- Nghiên cứu khảo sát 16 thuật toán hồi quy thuộc 6 họ mô hình. Các mô hình dự đoán 3 biến trạng thái từ 7 thông số vận hành.
- Việc so sánh các họ mô hình là một kiểm định giả thuyết cấu trúc. Thí nghiệm kiểm tra bản chất quan hệ giữa sinh học và màng lọc:
  - Họ Tuyến tính (Linear Regression - OLS, 1 mô hình): Kiểm tra mối quan hệ cộng tính và đơn điệu giữa các thông số.
  - Họ Tuyến tính hiệu chỉnh (Ridge, Lasso, ElasticNet, 3 mô hình): Kiểm tra giả thuyết cộng tính. Mô hình đồng thời đánh giá tác động của đa cộng tuyến.
  - Họ Máy vector hỗ trợ (SVR nhân RBF, 1 mô hình): Kiểm tra khả năng biểu diễn của bề mặt phi tuyến trơn toàn cục.
  - Họ Dựa trên cá thể (K-Nearest Neighbors - KNN, 1 mô hình): Kiểm tra tính quy luật cục bộ trong không gian vận hành. Các điều kiện lân cận phải tạo ra phản ứng tương đồng.
  - Họ Tập hợp cây (Decision Tree, Random Forest, Extra Trees, Bagging, AdaBoost, Gradient Boosting, Hist Gradient Boosting, XGBoost, LightGBM, 9 mô hình).
  - Họ tập hợp cây kiểm tra tác động ngưỡng và tương tác phi tuyến. Đây là các đặc tính dự báo theo lý thuyết tắc nghẽn màng kinh điển.
  - Họ Mạng nơ-ron (MLP hai tầng ẩn, 1 mô hình): Kiểm tra đóng góp của biểu diễn phân cấp phi tuyến sâu.
- Phân tích đối lập giữa Bagging và Boosting xác định giải pháp xử lý dữ liệu cảm biến công nghiệp:
  - Kỹ thuật Bagging (Extra Trees, Random Forest, Bagging) giảm phương sai. Kỹ thuật này làm mịn dao động ngẫu nhiên của cảm biến hiệu quả.
  - Kỹ thuật Boosting (XGBoost, LightGBM, CatBoost) giảm độ lệch tuần tự. Kỹ thuật này nhạy cảm hơn với dữ liệu nhiễu ngoại lai.
- Mô hình Extra Trees đạt độ chính xác cao nhất cho cả 3 mục tiêu. Mô hình này được chọn làm đại diện duy nhất cho phân tích tiếp theo.

#### 2.5.2. Tối ưu hóa siêu tham số bằng Bayesian Optimization qua FLAML
- Nghiên cứu tối ưu hóa siêu tham số bằng giải thuật Bayesian Optimization thông qua thư viện FLAML.
- Không gian tìm kiếm siêu tham số được định nghĩa trên các phân phối liên tục và rời rạc:
  - Số lượng cây quyết định ($n_{\text{estimators}}$): Khảo sát trong khoảng từ 50 đến 500 cây.
  - Độ sâu tối đa của cây ($max\_depth$): Khảo sát từ 3 đến 30 tầng hoặc không giới hạn độ sâu.
  - Số mẫu tối thiểu để phân tách nhánh ($min\_samples\_split$): Khảo sát từ 2 đến 20 mẫu.
  - Tỷ lệ đặc trưng ngẫu nhiên cho mỗi vết cắt ($max\_features$): Khảo sát liên tục từ 0.3 đến 1.0.
  - Tốc độ học ($learning\_rate$) cho các mô hình boosting: Tìm kiếm logarit trong khoảng $10^{-3}$ đến $0.3$.
- Hàm mục tiêu tối ưu hóa là cực tiểu hóa sai số căn bậc hai trung bình bình phương (RMSE) trên tập kiểm thực chéo.
- Giải thuật tìm kiếm Bayesian phân bổ tài nguyên tính toán hiệu quả. Giải thuật tập trung khai thác các vùng siêu tham số tiềm năng cao.

#### 2.5.3. Môi trường triển khai và cấu hình mô hình đại diện
- Toàn bộ quy trình huấn luyện và đánh giá thực hiện trên ngôn ngữ Python phiên bản 3.10.
- Các thư viện cốt lõi gồm NumPy, pandas, scikit-learn, XGBoost, LightGBM và SHAP.
- Mô hình Extra Trees đại diện sử dụng 100 cây quyết định ngẫu nhiên hóa cực độ.
- Thuật toán Extra Trees chọn các điểm cắt phân nhánh hoàn toàn ngẫu nhiên cho từng đặc trưng con.
- Cơ chế ngẫu nhiên hóa điểm cắt giúp giảm mạnh phương sai của mô hình. Cơ chế này không làm tăng độ lệch dự báo.
- Cấu hình thống nhất này bảo đảm tính nhất quán xuyên suốt cho cả ba biến mục tiêu: TMP, Flow và Level.

### 2.6. Phân tích khả năng diễn giải qua SHAP đa mô hình

#### 2.6.1. Khung lý thuyết giá trị Shapley và mô hình phụ gia cục bộ
- Phương pháp SHAP bắt nguồn từ lý thuyết trò chơi hợp tác của Lloyd Shapley (1953).
- Giá trị Shapley định lượng mức đóng góp biên công bằng của từng đặc trưng vào kết quả dự đoán của mô hình.
- Mô hình giải thích phụ gia cục bộ biểu diễn đầu ra $f(x)$ thành tổng tuyến tính của các giá trị phân bổ:
  $$f(x) = \phi_0 + \sum_{j=1}^M \phi_j(x)$$
  Trong đó:
  - $\phi_0 = \mathbb{E}[f(x)]$ là giá trị dự đoán kỳ vọng gốc trên tập dữ liệu nền.
  - $\phi_j(x)$ là giá trị Shapley của đặc trưng thứ $j$ đối với mẫu dữ liệu $x$.
  - $M$ là tổng số lượng đặc trưng đầu vào ($M = 7$).
- Công thức giải tích tính toán giá trị Shapley thỏa mãn tính công bằng cổ điển:
  $$\phi_j = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{j\}) - f_x(S) \right]$$
  Trong đó:
  - $F$ là tập hợp toàn bộ các đặc trưng đầu vào.
  - $S$ là tập hợp con các đặc trưng không chứa đặc trưng $j$.
  - $f_x(S)$ là giá trị dự báo kỳ vọng có điều kiện khi chỉ quan sát tập đặc trưng $S$.
- Phân tích SHAP thỏa mãn ba tiên đề toán học cốt lõi: Tính hiệu quả cục bộ, tính đối xứng và tính đơn điệu.

#### 2.6.2. Thuật toán TreeSHAP tối ưu so với KernelSHAP mô hình thay thế
- Nghiên cứu triển khai TreeSHAP cho 9 mô hình dạng cây và KernelSHAP cho 7 mô hình phi cây.
- Thuật toán TreeSHAP khai thác cấu trúc phân nhánh cây để tính toán chính xác kỳ vọng có điều kiện.
- Độ phức tạp tính toán của TreeSHAP đạt mức $O(TLD^2)$. Trong đó, $T$ là số cây, $L$ là số lá tối đa và $D$ là độ sâu tối đa.
- TreeSHAP xử lý tin cậy và chính xác cấu trúc tương quan mạnh giữa các biến vận hành thực tế.
- Thuật toán KernelSHAP là phương pháp xấp xỉ không phụ thuộc mô hình. Phương pháp này dùng hồi quy tuyến tính cục bộ có trọng số.
- Khi các biến đầu vào có tương quan mạnh, KernelSHAP dễ tạo ra các liên minh mẫu ngoài phân phối thực tế.
- Hiện tượng này dẫn đến việc phóng đại tầm quan trọng của các biến điều khiển ngắn hạn như sục khí.
- KernelSHAP đồng thời đánh giá thấp vai trò của các biến sinh học biến thiên chậm như SRT.
- Khung so sánh đa mô hình giúp phát hiện sai lệch thuật toán mà các phân tích mô hình đơn lẻ không thể nhận diện.

#### 2.6.3. Xây dựng 48 hồ sơ giải thích đặc trưng và phân tích tương tác
- Nghiên cứu thiết lập 48 hồ sơ diễn giải đặc trưng riêng biệt từ tổ hợp 16 thuật toán và 3 biến mục tiêu.
- Ba công cụ trực quan hóa định lượng được xây dựng cho từng tổ hợp mô hình và mục tiêu:
  - Biểu đồ bầy ong (Beeswarm plot): Thể hiện phân phối giá trị SHAP của từng mẫu và hướng tác động tăng hoặc giảm.
  - Giá trị SHAP tuyệt đối trung bình ($\text{mean}(|\text{SHAP}|)$): Xác định thứ hạng mức độ quan trọng toàn cục của 7 thông số.
  - Biểu đồ phụ thuộc (Dependence plot): Phản ánh tác động phi tuyến của từng biến và nhận diện các ngưỡng vận hành giới hạn.
- Phân tích tương tác đặc trưng bậc hai qua ma trận giá trị tương tác SHAP:
  $$\phi_{i,j} = \sum_{S \subseteq F \setminus \{i,j\}} \frac{|S|!(|F| - |S| - 2)!}{2(|F|!)} \left[ f_x(S \cup \{i,j\}) - f_x(S \cup \{i\}) - f_x(S \cup \{j\}) + f_x(S) \right]$$
- Giá trị này phân tách tác động độc lập của biến $i$ khỏi hiệu ứng hiệp đồng khi kết hợp cùng biến $j$.

#### 2.6.4. Ý nghĩa nhận thức luận giữa liên kết thống kê và cơ chế vật lý
- Giá trị SHAP định lượng mức độ liên kết thống kê trong phân phối dữ liệu huấn luyện SCADA.
- SHAP không chứng minh quan hệ nhân quả vật lý thực nghiệm nếu không có kiểm chứng thực nghiệm độc lập.
- Các diễn giải cơ chế được đối chiếu nghiêm ngặt với lý thuyết lọc màng, động học bùn hoạt tính và thủy lực MBR.
- Khung tiếp cận này loại bỏ các tương quan giả tạo và cung cấp cơ sở khoa học tin cậy cho người vận hành.

### 2.7. Xác định điều kiện vận hành tối ưu (Operational Basin)

#### 2.7.1. Định nghĩa không gian vận hành khả thi và ba tiêu chuẩn kỹ thuật đồng thời
- Không gian vận hành khả thi (Operational Basin) là tập hợp các trạng thái đáp ứng đồng thời 3 tiêu chí kỹ thuật:
  - Tiêu chí Áp suất xuyên màng: $\text{TMP} \le \text{TMP}_{\text{threshold}}$, với dải vận hành an toàn $-0.09\text{ bar} \le \text{TMP} \le -0.03\text{ bar}$.
  - Giới hạn này ngăn ngừa tắc nghẽn màng nghiêm trọng và bảo vệ cấu trúc sợi màng PVDF.
  - Tiêu chí Lưu lượng thấm: $\text{Flow} \ge \text{Flow}_{\text{design}}$, với dải sản lượng yêu cầu $1.5\text{ m}^3/\text{min} \le \text{Flow} \le 2.2\text{ m}^3/\text{min}$.
  - Tiêu chí này bảo đảm công suất xử lý nước thải liên tục cho nhà máy chế tạo bán dẫn.
  - Tiêu chí Mức nước bể màng: $\text{Level}_{\text{min}} \le \text{Level} \le \text{Level}_{\text{max}}$, với dải kiểm soát $65.0\% \le \text{Level} \le 67.0\%$.
  - Tiêu chí này duy trì cân bằng thủy lực, bảo đảm màng ngập nước và chống tràn bể màng.
- Điểm vận hành đạt mức khả thi khi cả 3 giá trị dự báo đồng thời thỏa mãn các ngưỡng trên.

#### 2.7.2. Phương pháp lấy mẫu tái lập ràng buộc theo đa tạp (Manifold-Constrained Resampling)
- Việc lấy mẫu độc lập từng biến trên dải biên độ tạo ra các điểm phi thực tế ngoài không gian hoạt động.
- Nghiên cứu áp dụng kỹ thuật lấy mẫu hạt nhân hiệp phương sai cục bộ bị ràng buộc bởi đa tạp:
  - Bước 1: Rút ngẫu nhiên đồng đều một mẫu giờ gốc ($\mathbf{x}_{\text{seed}}$) từ 4593 bản ghi thực tế của nhà máy.
  - Bước 2: Xác định $k = 30$ điểm lân cận gần nhất của mẫu gốc trong không gian đầu vào chuẩn hóa Z-score.
  - Bước 3: Tính toán ma trận hiệp phương sai cục bộ $\mathbf{\Sigma}_k$ từ 30 điểm lân cận này.
  - Bước 4: Tạo mẫu ứng viên bằng cách nhiễu loạn điểm gốc theo phân phối Gauss với hệ số băng thông $\gamma = 0.6$:
    $$\mathbf{x}_{\text{cand}} = \mathbf{x}_{\text{seed}} + \mathcal{N}\left(\mathbf{0}, \gamma^2 \mathbf{\Sigma}_k\right)$$
  - Bước 5: Áp dụng điều kiện loại bỏ kép để kiểm soát mẫu ứng viên:
    - Loại bỏ mẫu ứng viên nếu bất kỳ biến nào vượt ra ngoài khoảng giá trị biên quan sát thực tế.
    - Loại bỏ mẫu nếu khoảng cách đến điểm thực tế gần nhất vượt quá phân vị 99 ($d_{99} = 0.539$ đơn vị chuẩn).
- Quy trình tạo ra 500000 trạng thái vận hành ứng viên liên tục trên đa tạp dữ liệu thực tế.
- Khoảng cách trung vị đến điểm thực tế gần nhất của tập mẫu đạt $0.121$, tương đương khoảng cách $0.119$ giữa các giờ thực tế.
- Đặc tính này bảo đảm quá trình nội suy phản ánh trung thực các chế độ vận hành khả dĩ của nhà máy.

#### 2.7.3. Định lượng độ bất định dự báo từ tập hợp 100 cây quyết định
- Độ bất định dự báo được định lượng trực tiếp từ độ phân tán kết quả của 100 cây trong mô hình Extra Trees.
- Khoảng tin cậy $95\%$ của các giá trị dự báo đạt mức độ chuẩn xác cao:
  - Khoảng tin cậy của TMP đạt $\pm 0.008\text{ bar}$.
  - Khoảng tin cậy của Flow đạt $\pm 0.17\text{ m}^3/\text{min}$.
  - Khoảng tin cậy của Level đạt $\pm 0.71\%$.
- Biên độ bất định khuyến cáo người vận hành nên đặt điểm làm việc ở vùng lõi của không gian khả thi.
- Vận hành tại vùng lõi giúp hệ thống tránh rủi ro vi phạm ngưỡng do các dao động ngẫu nhiên ngắn hạn.
- Trong số 500000 trạng thái vận hành mô phỏng, có 207238 trạng thái ($41.4\%$) thỏa mãn đồng thời cả 3 mục tiêu.

#### 2.7.4. Tỷ lệ khả thi có điều kiện (CFR) và giao thức xác định dải khuyến nghị
- Nghiên cứu định nghĩa Tỷ lệ khả thi có điều kiện (Conditional Feasibility Rate - CFR) theo từng biến đầu vào:
  $$\text{CFR}(x) = P(\text{TMP, Flow, Level đạt chuẩn} \mid X = x)$$
- CFR phản ánh xác suất thành công thực tế thay vì mật độ mẫu biểu kiến tại các vùng nhà máy thường vận hành.
- Phân phối mật độ liên tục của các điểm khả thi được ước lượng bằng phương pháp Kernel Density Estimation (KDE):
  - Áp dụng nhân Gauss trơn để khắc phục sự phụ thuộc vào cách chia khoảng của biểu đồ tần số.
  - Độ rộng băng thông được xác định tự động theo quy tắc Scott: $h = n^{-1/(d+4)} \cdot \sigma$.
- Giao thức xác định dải vận hành tối ưu khuyến nghị:
  - Chia toàn bộ dải giá trị của từng thông số thành 10 phân vị (deciles).
  - Chọn dải tối ưu là chuỗi phân vị liên tục rộng nhất có tỷ lệ đạt chuẩn trong khoảng 5% so với mức tối đa.
  - Ràng buộc ngưỡng hỗ trợ thống kê tối thiểu với ít nhất 250 giờ vận hành thực tế đã ghi nhận.
- Bốn trên bảy thông số giữ nguyên cấu trúc dải hẹp, chứng minh sự tồn tại của các điểm tối ưu cục bộ sắc nét.

### 2.8. Chỉ số đánh giá hiệu suất

#### 2.8.1. Các chỉ số thống kê sai số hồi quy (RMSE, R², MAE)
- Nghiên cứu sử dụng 3 chỉ số thống kê bổ trợ để định lượng sai số dự báo của các thuật toán:
  - Căn bậc hai sai số bình phương trung bình (Root Mean Squared Error - RMSE):
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
    Chỉ số này phạt nặng các sai số dự báo lớn và nhạy cảm với các điểm ngoại lai cục bộ.
  - Hệ số xác định (Coefficient of Determination - $R^2$):
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
    Chỉ số này đo tỷ lệ phương sai được mô hình giải thích so với giá trị trung bình $\bar{y}$.
  - Sai số tuyệt đối trung bình (Mean Absolute Error - MAE):
    $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
    Chỉ số này đánh giá sai số tuyến tính trên cùng đơn vị đo vật lý của biến mục tiêu.
- Các chỉ số được tính toán độc lập trên từng phân vùng kiểm định để đánh giá tính khái quát hóa của mô hình.

#### 2.8.2. Đánh giá mức độ cải thiện xác suất qua tỷ số chênh (Odds Ratio)
- Tỷ số chênh (Odds Ratio - OR) đo lường mức tăng xác suất đạt chuẩn vận hành khi hệ thống nằm trong dải khuyến nghị:
  $$\text{OR} = \frac{P(\text{Khả thi} \mid \text{Trong dải}) / [1 - P(\text{Khả thi} \mid \text{Trong dải})]}{P(\text{Khả thi} \mid \text{Ngoài dải}) / [1 - P(\text{Khả thi} \mid \text{Ngoài dải})]}$$
- Phân tích tỷ số chênh lượng hóa hiệu quả can thiệp kỹ thuật so với mức vận hành nền 37.1% của toàn trạm:
  - Vận hành trong dải khuyến nghị nâng tỷ lệ đạt đồng thời cả 3 mục tiêu lên mức $61.9\% - 82.4\%$.
  - Trên tập dữ liệu kiểm định giữ lại 3 tháng độc lập, dải vận hành đạt tỷ lệ thành công 61.9% với $\text{OR} = 3.89$.
  - Giá trị $\text{OR} > 1$ chứng minh việc vận hành trong vùng khuyến nghị giúp tăng xác suất đạt chuẩn.
