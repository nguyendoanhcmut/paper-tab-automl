## 3. Tối ưu hóa, Đánh giá Hiệu năng, Giải thích và Lựa chọn Mô hình

### 3.1 Tối ưu hóa Siêu tham số Mô hình (Model Optimization)

#### 3.1.1 Hiện tượng Quá khớp (Overfitting) và Dưới khớp (Underfitting)
- Quá trình huấn luyện mô hình học máy tìm kiếm tập hợp tham số tối ưu nhằm cực tiểu hóa hàm mất mát trên dữ liệu quan sát.
- Hiện tượng Dưới khớp (Underfitting) xuất hiện khi mô hình có cấu trúc quá đơn giản.
  - Mô hình không đủ khả năng học các mối quan hệ phi tuyến tiềm ẩn giữa các biến vận hành MBR và biến mục tiêu.
  - Sai số trên cả tập huấn luyện (training error) và tập kiểm tra (testing error) đều duy trì ở mức cao.
  - Nguyên nhân chính: Số lượng nơ-ron hoặc số tầng ẩn quá ít, hàm nhân (kernel) không phù hợp, hoặc mức độ điều chuẩn hóa (regularization) quá lớn.
- Hiện tượng Quá khớp (Overfitting) xảy ra khi mô hình có độ phức tạp vượt mức cần thiết.
  - Mô hình học thuộc lòng cả nhiễu ngẫu nhiên và biến động cá biệt của tập huấn luyện.
  - Sai số huấn luyện tiệm cận 0, nhưng sai số kiểm định trên dữ liệu độc lập tăng vọt.
  - Khả năng khái quát hóa (generalization capability) của mô hình bị suy giảm nghiêm trọng.
  - Nguyên nhân: Kích thước mẫu dữ liệu MBR hạn chế trong khi số lượng tham số tự do quá lớn.
- Đánh đổi Độ chệch và Phương sai (Bias-Variance Trade-off):
  - Sai số tổng quát của mô hình gồm ba thành phần: $\text{Error} = \text{Bias}^2 + \text{Variance} + \sigma^2$.
  - $\text{Bias}$ (Độ chệch) đại diện cho sai số do giả định đơn giản hóa của thuật toán.
  - $\text{Variance}$ (Phương sai) đo lường độ nhạy của mô hình trước các biến động nhỏ trong tập dữ liệu huấn luyện.
  - $\sigma^2$ là nhiễu không thể quy giảm (irreducible noise) vốn có của hệ thống thực nghiệm.
  - Mục tiêu tối ưu hóa: Cân bằng bias và variance để cực tiểu hóa sai số tổng quát.

#### 3.1.2 Kỹ thuật Xác thực Chéo K-lần (K-Fold Cross-Validation)
- Cơ chế phân chia dữ liệu:
  - Tập dữ liệu huấn luyện gồm $N$ mẫu được chia ngẫu nhiên thành $K$ phần con (folds) có kích thước xấp xỉ bằng nhau và không giao nhau.
  - Quá trình đánh giá thực hiện lặp lại $K$ vòng độc lập.
  - Trong mỗi vòng lặp $k \in \{1, 2, \dots, K\}$, mô hình sử dụng $K-1$ phần con để huấn luyện (training subsets).
  - Phần con thứ $k$ còn lại đóng vai trò tập xác thực (validation subset) để kiểm tra sai số.
- Công thức tính toán sai số xác thực chéo:
  - Sai số kiểm định chéo trung bình $CV_{(K)}$ xác định theo công thức:
    $$CV_{(K)} = \frac{1}{K} \sum_{k=1}^K MSE_k$$
  - Trong đó $MSE_k$ là sai số bình phương trung bình trên tập kiểm định của vòng thứ $k$:
    $$MSE_k = \frac{1}{n_k} \sum_{i=1}^{n_k} (y_i - \hat{y}_i)^2$$
- Đặc điểm vận hành và chi phí tính toán:
  - Giá trị $K$ thường chọn bằng 5 hoặc 10 theo kinh nghiệm thực nghiệm.
  - Khi $K = N$, phương pháp trở thành xác thực chéo loại một mẫu (Leave-One-Out Cross-Validation - LOOCV).
  - Ưu điểm: Tận dụng tối đa dữ liệu có sẵn, loại bỏ thiên lệch do chia tập tĩnh, đánh giá khách quan độ bền vững của mô hình.
  - Nhược điểm: Chi phí tính toán cao do phải tái huấn luyện mô hình $K$ lần liên tục.

#### 3.1.3 Các Chiến lược Tìm kiếm Siêu tham số (Hyperparameter Search Strategies)
- Tìm kiếm vét cạn theo lưới (Grid Search):
  - Người dùng thiết lập không gian tìm kiếm gồm các tập giá trị rời rạc cho từng siêu tham số.
  - Thuật toán kiểm tra toàn bộ tích Descartes (Cartesian product) của tất cả các tổ hợp siêu tham số.
  - Với mỗi tổ hợp, thuật toán chạy quy trình K-Fold CV để ghi nhận điểm số hiệu năng trung bình.
  - Ưu điểm: Đảm bảo duyệt hết không gian định trước, dễ thực thi song song hóa.
  - Nhược điểm: Bị bùng nổ tổ hợp khi số chiều siêu tham số tăng cao, tốn kém tài nguyên tính toán.
- Tìm kiếm ngẫu nhiên (Random Search):
  - Lấy mẫu ngẫu nhiên các cấu hình siêu tham số từ phân phối xác suất liên tục hoặc rời rạc xác định trước.
  - Số lần thử nghiệm cố định theo ngân sách tính toán $N_{\text{iter}}$.
  - Hiệu quả: Vượt trội hơn Grid Search khi chỉ có một số ít siêu tham số chi phối hiệu năng mô hình (Bergstra & Bengio, 2012).
- Tối ưu hóa Bayes (Bayesian Optimization):
  - Phù hợp tối ưu hóa các hàm mục tiêu tốn nhiều thời gian tính toán như mạng nơ-ron sâu hoặc rừng ngẫu nhiên quy mô lớn.
  - Xây dựng mô hình đại diện xác suất (thường dùng Quá trình Gaussian - Gaussian Process, GP) cho hàm mục tiêu chưa biết $f(\theta)$:
    $$f(\theta) \sim \mathcal{GP}\left(m(\theta), k(\theta, \theta')\right)$$
  - Trong đó $m(\theta)$ là hàm kỳ vọng và $k(\theta, \theta')$ là hàm hiệp phương sai (kernel covariance).
  - Sử dụng hàm thu nạp (Acquisition Function) để quyết định điểm đánh giá tiếp theo, cân bằng giữa thăm dò (exploration) và khai thác (exploitation).
  - Hàm Cải thiện Kỳ vọng (Expected Improvement - EI):
    $$EI(\theta) = \mathbb{E}\left[\max\left(0, f_{best} - f(\theta)\right)\right]$$
  - Thuật toán ưu tiên đánh giá các vùng có giá trị trung bình dự báo tốt hoặc độ bất định cao.

#### 3.1.4 Các Thuật toán Bầy đàn và Siêu phỏng sinh học (Metaheuristic Optimization Algorithms)
- Giải thuật Di truyền (Genetic Algorithm - GA):
  - Lấy cảm hứng từ quá trình chọn lọc tự nhiên và di truyền học của Darwin.
  - Mã hóa mỗi cấu hình siêu tham số thành một chuỗi nhiễm sắc thể (chromosome).
  - Khởi tạo quần thể gồm nhiều cá thể ngẫu nhiên.
  - Đánh giá độ thích nghi (fitness function) của từng cá thể thông qua chỉ số sai số mô hình (như $1/RMSE$ hoặc $R^2$).
  - Áp dụng các toán tử di truyền qua từng thế hệ:
    - Toán tử chọn lọc (Selection): Giữ lại các cá thể có độ thích nghi cao.
    - Toán tử lai ghép (Crossover): Trao đổi thông tin di truyền giữa hai cá thể bố mẹ để sinh cá thể con.
    - Toán tử đột biến (Mutation): Thay đổi ngẫu nhiên một số gen để duy trì tính đa dạng và thoát khỏi cực trị địa phương.
- Tối ưu hóa Bầy đàn Hạt (Particle Swarm Optimization - PSO):
  - Mô phỏng hành vi di chuyển tìm mồi của bầy chim hoặc đàn cá.
  - Mỗi hạt đại diện cho một nghiệm siêu tham số trong không gian tìm kiếm đa chiều.
  - Mỗi hạt $i$ sở hữu vectơ vị trí $x_i^{(t)}$ và vectơ vận tốc $v_i^{(t)}$ tại vòng lặp $t$.
  - Công thức cập nhật vận tốc và vị trí:
    $$v_i^{(t+1)} = w \cdot v_i^{(t)} + c_1 r_1 \left(p_{\text{best}, i} - x_i^{(t)}\right) + c_2 r_2 \left(g_{\text{best}} - x_i^{(t)}\right)$$
    $$x_i^{(t+1)} = x_i^{(t)} + v_i^{(t+1)}$$
  - Trong đó:
    - $w$ là trọng số quán tính (inertia weight), kiểm soát ảnh hưởng của vận tốc trước đó.
    - $c_1, c_2$ là các hệ số gia tốc nhận thức cá nhân (cognitive) và gia tốc xã hội bầy đàn (social).
    - $r_1, r_2$ là các biến ngẫu nhiên phân phối đều trong khoảng $[0, 1]$.
    - $p_{\text{best}, i}$ là vị trí tối ưu từng đạt được của bản thân hạt $i$.
    - $g_{\text{best}}$ là vị trí tối ưu toàn cục của toàn bộ bầy hạt.
- Luyện kim Mô phỏng (Simulated Annealing - SA):
  - Mô phỏng quá trình nhiệt luyện kim loại từ nhiệt độ cao rồi làm nguội chậm có kiểm soát.
  - Tại mỗi mức nhiệt độ $T$, thuật toán tạo một cấu hình lân cận $\theta'$.
  - Nếu nghiệm mới tốt hơn ($\Delta E = f(\theta') - f(\theta) < 0$), thuật toán chấp nhận nghiệm mới ngay lập tức.
  - Nếu nghiệm mới kém hơn, thuật toán vẫn chấp nhận nghiệm đó với xác suất Boltzmann:
    $$P(\text{chấp nhận}) = \exp\left(-\frac{\Delta E}{T}\right)$$
  - Cơ chế này cho phép thuật toán thoát khỏi các cực tiểu địa phương khi nhiệt độ còn cao.
- Các thuật toán metaheuristic bầy đàn khác trong nghiên cứu MBR:
  - Thuật toán Đàn ong Nhân tạo (Artificial Bee Colony - ABC): Phân chia bầy ong thành ong thợ, ong quan sát và ong trinh sát để khai thác nguồn mật.
  - Thuật toán Đàn kiến (Ant Colony Optimization - ACO): Dựa trên dấu vết pheromone của kiến để tìm đường đi ngắn nhất.
  - Thuật toán Đom đóm (Firefly Algorithm - FFA): Dựa trên cường độ phát sáng để các cá thể đom đóm hút nhau.
  - Thuật toán Dơi (Bat Algorithm - BA): Ứng dụng sóng định vị bằng tiếng vang để săn mồi và điều chỉnh tần số phát xung.
  - Bộ tối ưu Chó sói Xám (Gray Wolf Optimizer - GWO): Mô phỏng trật tự phân cấp săn mồi của đàn sói xám (sói $\alpha$, $\beta$, $\delta$, và $\omega$).

---

### 3.2 Đánh giá Hiệu năng Định lượng Mô hình (Model Performance Assessment)

#### 3.2.1 Các Chỉ số Đánh giá Bài toán Hồi quy (Regression Metrics)
- Hệ số xác định ($R^2$ - Coefficient of Determination):
  - Đo lường tỷ lệ phương sai của biến mục tiêu thực tế được giải thích bởi các biến đầu vào qua mô hình:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó $y_i$ là giá trị thực nghiệm, $\hat{y}_i$ là giá trị mô hình dự báo, và $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ là giá trị trung bình thực nghiệm.
  - Miền giá trị danh nghĩa: $R^2 \le 1.0$. Giá trị càng gần 1.0, độ khớp của mô hình càng cao. Giá trị âm xuất hiện khi mô hình dự báo kém hơn mức trung bình tĩnh $\bar{y}$.
- Sai số Bình phương Trung bình (MSE - Mean Squared Error):
  - Trung bình cộng của bình phương các độ lệch giữa giá trị dự báo và giá trị thực tế:
    $$MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$
  - MSE phạt rất nặng các sai số lớn do có số mũ bậc hai. Chỉ số này nhạy cảm với các giá trị ngoại lai dị biệt.
- Sai số Căn bậc hai Bình phương Trung bình (RMSE - Root Mean Squared Error):
  - Căn bậc hai của sai số bình phương trung bình:
    $$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  - RMSE giữ nguyên đơn vị đo lường vật lý của biến đầu ra (ví dụ: $L/(m^2 \cdot h)$ đối với thông lượng màng, hoặc $kPa$ đối với TMP).
- Sai số Tuyệt đối Trung bình (MAE - Mean Absolute Error):
  - Trung bình cộng của các độ lệch tuyệt đối giữa giá trị thực tế và giá trị dự báo:
    $$MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$
  - MAE phản ánh độ lớn sai số trung bình một cách trực quan, ít chịu ảnh hưởng thái quá bởi các điểm dữ liệu ngoại lai so với RMSE.
- Sai số Phần trăm Tuyệt đối Trung bình (MAPE - Mean Absolute Percentage Error):
  - Tỷ lệ phần trăm sai số trung bình so với giá trị thực tế:
    $$MAPE = \frac{100\%}{n}\sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
  - MAPE cho phép so sánh hiệu năng giữa các tập dữ liệu có thang đo khác nhau.
  - Hạn chế: MAPE không xác định hoặc tăng vô hạn khi giá trị thực tế $y_i$ tiến dần về 0.

#### 3.2.2 Tiêu chuẩn Thông tin Đánh giá Độ phức tạp Mô hình (Information Criteria)
- Giới hạn của các chỉ số hiệu năng thông thường ($R^2$, MSE, RMSE):
  - Các chỉ số này chỉ đánh giá độ khớp thuần túy trên dữ liệu mà không xét đến số lượng tham số tự do của mô hình.
  - Mô hình càng nhiều tham số càng dễ đạt $R^2$ cao trên tập huấn luyện, nhưng đối mặt nguy cơ quá khớp lớn.
- Tiêu chuẩn Thông tin Akaike (AIC - Akaike Information Criterion):
  - Dựa trên lý thuyết thông tin và khoảng cách Kullback-Leibler:
    $$AIC = 2k - 2\ln(L)$$
  - Trong đó $k$ là số lượng tham số ước lượng trong mô hình, $L$ là giá trị cực đại của hàm hợp lý (maximum likelihood).
  - Đối với bài toán hồi quy với sai số chuẩn:
    $$AIC = n \ln(MSE) + 2k$$
- Tiêu chuẩn Thông tin Bayes (BIC - Bayesian Information Criterion / Schwarz Criterion):
  - Dựa trên phương pháp tiếp cận xác suất hậu nghiệm Bayes:
    $$BIC = k\ln(n) - 2\ln(L)$$
  - Đối với bài toán hồi quy:
    $$BIC = n \ln(MSE) + k\ln(n)$$
  - Với kích thước mẫu $n \ge 8$, ta có $\ln(n) > 2$, do đó BIC phạt số lượng tham số $k$ nghiêm khắc hơn AIC.
- Tiêu chuẩn Hannan-Quinn (HQC - Hannan-Quinn Criterion):
  - Cân bằng giữa tốc độ hội tụ và mức độ phạt tham số:
    $$HQC = 2k\ln(\ln(n)) - 2\ln(L)$$
- So sánh mức độ phạt tham số (Penalty Gradient):
  - Khi kích thước mẫu $n$ đủ lớn, độ lớn hình phạt tham số tuân theo thứ tự:
    $$AIC < HQC < BIC$$
  - Hình phạt càng mạnh thì tiêu chuẩn càng ưu tiên lựa chọn các mô hình tinh gọn, ít chiều (low-dimensional models).
  - Giá trị AIC, BIC hoặc HQC càng nhỏ chứng tỏ mô hình đạt được sự cân bằng tối ưu giữa độ chính xác và tính đơn giản.

#### 3.2.3 Các Chỉ số Đánh giá Bài toán Phân loại (Classification Metrics)
- Ma trận Nhầm lẫn (Confusion Matrix):
  - Bảng tổng hợp kết quả phân loại nhị phân gồm 4 ô giá trị:
    - Dương tính thật (True Positive - $TP$): Mẫu dương tính được dự báo chính xác là dương tính.
    - Âm tính thật (True Negative - $TN$): Mẫu âm tính được dự báo chính xác là âm tính.
    - Dương tính giả (False Positive - $FP$, Sai số loại I): Mẫu âm tính bị dự báo nhầm thành dương tính.
    - Âm tính giả (False Negative - $FN$, Sai số loại II): Mẫu dương tính bị bỏ sót thành âm tính.
- Độ chính xác Tổng thể (Accuracy):
  - Tỷ lệ số mẫu dự báo đúng trên toàn bộ tập dữ liệu:
    $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
  - Hạn chế: Dễ đưa ra đánh giá sai lệch khi dữ liệu bị mất cân bằng lớp nghiêm trọng.
- Độ chuẩn xác (Precision):
  - Tỷ lệ mẫu thực sự dương tính trong tổng số mẫu được mô hình gắn nhãn dương tính:
    $$Precision = \frac{TP}{TP + FP}$$
- Độ thu hồi / Độ nhạy (Recall / Sensitivity):
  - Tỷ lệ mẫu dương tính được mô hình phát hiện thành công trên tổng số mẫu thực sự dương tính:
    $$Recall = \frac{TP}{TP + FN}$$
- Điểm số F1 (F1-score):
  - Trung bình điều hòa giữa Precision và Recall:
    $$F1\text{-score} = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$
  - F1-score là thước đo cân bằng, đặc biệt hiệu quả khi dữ liệu phân loại tắc nghẽn màng bị mất cân bằng lớp.
- Đường cong ROC (Receiver Operating Characteristic) và Diện tích AUC (Area Under Curve):
  - Đường cong ROC biểu diễn mối quan hệ giữa Tỷ lệ dương tính thật (TPR = Recall) và Tỷ lệ dương tính giả (FPR):
    $$TPR = \frac{TP}{TP + FN}, \quad FPR = \frac{FP}{FP + TN}$$
  - Giá trị AUC đo lường toàn diện năng lực phân biệt giữa hai lớp của mô hình:
    - $\text{AUC} = 0.5$: Mô hình dự báo ngẫu nhiên, không có giá trị phân biệt.
    - $0.7 \le \text{AUC} < 0.8$: Khả năng phân biệt chấp nhận được.
    - $0.8 \le \text{AUC} < 0.9$: Khả năng phân biệt xuất sắc.
    - $\text{AUC} \ge 0.9$: Khả năng phân biệt rất cao, tiệm cận phân loại hoàn hảo ($\text{AUC} = 1.0$).

---

### 3.3 Đánh giá Khả năng Giải thích Mô hình Học máy (Model Interpretation & XAI)

#### 3.3.1 Thách thức của Mô hình Hộp đen (Black-box Models) trong MBR
- Các thuật toán học máy phức tạp (mạng nơ-ron nhân tạo nhiều tầng, mô hình tổng hợp rừng ngẫu nhiên, mô hình tăng cường gradient) đạt độ chính xác cao nhưng hoạt động như các "hộp đen".
- Cơ chế bên trong của mô hình hộp đen ẩn giấu các hàm truyền phi tuyến phức tạp.
- Kỹ sư vận hành không thể quan sát quy luật đưa ra dự báo của mô hình.
- Hệ quả trong công nghệ MBR:
  - Khó kiểm tra tính nhất quán giữa dự báo của mô hình và các định luật bảo toàn khối lượng, động học sinh học và thủy lực màng.
  - Nguy cơ đưa ra các cảnh báo sai hoặc quyết định điều khiển rửa màng sai lầm khi dữ liệu quan trắc xuất hiện nhiễu.
  - Thiếu sự tin cậy từ phía các nhà quản lý và chuyên gia vận hành nhà máy xử lý nước thải.
- Nhu cầu cấp thiết về Trí tuệ Nhân tạo Giải thích được (Explainable Artificial Intelligence - XAI):
  - Chuyển đổi mô hình học máy từ trạng thái hộp đen sang mô hình minh bạch.
  - Xác định mức độ đóng góp định lượng của từng biến số đầu vào (nồng độ bùn hoạt tính MLSS, thông lượng khí sục aeration, áp suất lọc TMP, nồng độ EPS/SMP).

#### 3.3.2 Phương pháp Phân tích Trọng số Kết nối Nơ-ron (Connection Weight Methods)
- Thuật toán Garson (Garson's Algorithm, 1991):
  - Phân tích ma trận trọng số kết nối giữa lớp đầu vào ($i$), lớp ẩn ($j$) và lớp đầu ra ($k$) trong mạng nơ-ron nhiều tầng (MLP).
  - Tỷ lệ đóng góp tương đối $Q_{ik}$ của biến đầu vào $i$ đối với biến đầu ra $k$ xác định theo công thức:
    $$Q_{ik} = \frac{\sum_{j=1}^{N_h} \left( \frac{|w_{ij}|}{\sum_{m=1}^{N_i} |w_{mj}|} \cdot |v_{jk}| \right)}{\sum_{i=1}^{N_i} \left[ \sum_{j=1}^{N_h} \left( \frac{|w_{ij}|}{\sum_{m=1}^{N_i} |w_{mj}|} \cdot |v_{jk}| \right) \right]}$$
  - Trong đó:
    - $w_{ij}$ là trọng số liên kết từ nơ-ron đầu vào $i$ đến nơ-ron ẩn $j$.
    - $v_{jk}$ là trọng số liên kết từ nơ-ron ẩn $j$ đến nơ-ron đầu ra $k$.
    - $N_i$ là tổng số nơ-ron lớp đầu vào.
    - $N_h$ là tổng số nơ-ron lớp ẩn.
  - Nhược điểm của thuật toán Garson: Sử dụng giá trị tuyệt đối $|w|$, do đó triệt tiêu dấu của trọng số, không phân biệt được biến đầu vào mang tác động kích thích (tích cực) hay ức chế (tiêu cực) lên đầu ra.
- Phương pháp Trọng số Kết nối có dấu của Goh (1995) và Olden (Olden et al., 2004):
  - Giữ nguyên dấu đại số của các liên kết để xác định chiều hướng tác động:
    $$S_{ik} = \sum_{j=1}^{N_h} \left( w_{ij} \cdot v_{jk} \right)$$
  - Giá trị $S_{ik}$ dương thể hiện biến đầu vào $i$ tỷ lệ thuận với biến đầu ra $k$ (ví dụ: MLSS tăng làm tăng tốc độ tắc nghẽn màng).
  - Giá trị $S_{ik}$ âm thể hiện mối quan hệ tỷ lệ nghịch (ví dụ: tăng cường độ sục khí giúp làm giảm tốc độ bám bẩn màng).
  - Nghiên cứu của Olden chứng minh phương pháp này đạt độ chính xác phân loại tầm quan trọng cao hơn thuật toán Garson trên dữ liệu mô phỏng.
- Thuật toán Gedeon (1997):
  - Mở rộng phân tích đóng góp trọng số cho các cấu trúc mạng nơ-ron có nhiều lớp ẩn liên tiếp.
  - Phù hợp phân tích cơ chế nội tại của các kiến trúc học sâu (Deep Learning).

#### 3.3.3 Phân tích Độ nhạy và Độ quan trọng Biến trong Mô hình Cây
- Phân tích Độ nhạy (Sensitivity Analysis):
  - Đánh giá mức độ thay đổi của biến đầu ra khi biến thiên có kiểm soát từng biến đầu vào trong khi cố định các biến còn lại ở giá trị cơ sở (trung bình hoặc trung vị).
  - Giúp phát hiện ngưỡng phản ứng tới hạn của hệ thống MBR (ví dụ: ngưỡng nồng độ chất keo sinh học gây đột biến TMP).
- Độ quan trọng của biến trong Mô hình Cây Quyết định và Rừng Ngẫu nhiên (Random Forest):
  - Độ suy giảm tạp chất trung bình (Mean Decrease Impurity - MDI):
    - Tính toán tổng mức độ suy giảm chỉ số Gini (đối với phân loại) hoặc MSE (đối với hồi quy) tại tất cả các nút phân nhánh sử dụng đặc trưng đó.
    - Hạn chế: Thường thiên lệch đối với các đặc trưng có nhiều giá trị phân loại rời rạc hoặc liên tục.
  - Độ chính xác ngoài túi (Mean Decrease Accuracy / Out-of-Bag - OOB Permutation Importance):
    - Hoán vị ngẫu nhiên các giá trị của một đặc trưng cụ thể trên tập dữ liệu kiểm định OOB.
    - Đo lường mức độ sụt giảm độ chính xác dự báo sau khi hoán vị:
      $$\Delta \text{Error}_j = \text{Error}_{\text{permuted}(j)} - \text{Error}_{\text{original}}$$
    - Nếu sai số tăng mạnh sau khi hoán vị, đặc trưng đó đóng vai trò trọng yếu trong việc ra quyết định của mô hình.

#### 3.3.4 Đồ thị Phụ thuộc Một phần (PDP), ICE và Phương pháp LIME
- Đồ thị Phụ thuộc Một phần (Partial Dependence Plot - PDP):
  - Minh họa tác động biên phi tuyến (marginal effect) của một hoặc hai biến đầu vào lên dự báo của mô hình học máy:
    $$\hat{f}_{x_S}(x_S) = \frac{1}{n}\sum_{i=1}^n \hat{f}\left(x_S, x_C^{(i)}\right)$$
  - Trong đó:
    - $x_S$ là tập hợp đặc trưng cần phân tích (thường là 1 hoặc 2 biến).
    - $x_C$ là tập hợp tất cả các đặc trưng còn lại trong mô hình.
    - $x_C^{(i)}$ là giá trị thực tế của tập đặc trưng còn lại từ mẫu dữ liệu thứ $i$.
  - Ứng dụng trong MBR: Vẽ đường cong mô tả mối quan hệ giữa thông lượng thấm (flux) và tốc độ gia tăng áp suất xuyên màng $dTMP/dt$, giúp xác định vùng thông lượng tới hạn (critical flux).
  - Hạn chế: PDP giả định tính độc lập giữa các biến $x_S$ và $x_C$. Khi các biến đầu vào tương quan chặt chẽ (như MLSS và độ nhớt nhớt bùn), PDP có thể tính toán trên các điểm dữ liệu phi thực tế.
- Đường Kỳ vọng Có điều kiện Cá thể (Individual Conditional Expectation - ICE):
  - Hiển thị mối quan hệ phụ thuộc cho từng mẫu dữ liệu riêng lẻ thay vì lấy trung bình như PDP.
  - Giúp phát hiện các mối quan hệ không đồng nhất hoặc các hiệu ứng tương tác ẩn giữa các nhóm vi sinh vật khác nhau.
- Phương pháp LIME (Local Interpretable Model-agnostic Explanations):
  - Giải thích dự báo cục bộ cho từng điểm dữ liệu đơn lẻ.
  - Thuật toán làm nhiễu nhẹ điểm dữ liệu quan tâm, lấy dự báo từ mô hình phức tạp, sau đó huấn luyện một mô hình giải thích được (như hồi quy tuyến tính có trọng số theo khoảng cách) cục bộ xung quanh điểm đó.

#### 3.3.5 Phương pháp SHAP (SHapley Additive exPlanations)
- Nền tảng Lý thuyết Trò chơi Hợp tác (Cooperative Game Theory):
  - Do nhà toán học Lloyd Shapley đề xuất (1953) nhằm phân chia công bằng phần thưởng của một liên minh người chơi.
  - Trong học máy: Tập hợp các đặc trưng đầu vào đóng vai trò là "liên minh người chơi", và giá trị dự báo của mô hình đóng vai trò là "phần thưởng".
- Công thức tính toán giá trị Shapley:
  - Giá trị đóng góp biên trung bình $\phi_i(x)$ của đặc trưng $i$ đối với mẫu dữ liệu $x$ xác định bởi:
    $$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
  - Ý nghĩa các ký hiệu:
    - $F$ là tập hợp đầy đủ của tất cả các đặc trưng đầu vào ($|F|$ là tổng số đặc trưng).
    - $S$ là một tập con bất kỳ của các đặc trưng không chứa đặc trưng $i$.
    - $|S|$ là số lượng đặc trưng có mặt trong tập hợp con $S$.
    - $f_x(S)$ là giá trị kỳ vọng dự báo của mô hình khi chỉ sử dụng tập đặc trưng $S$.
    - $[f_x(S \cup \{i\}) - f_x(S)]$ là đóng góp biên (marginal contribution) thuần túy khi thêm đặc trưng $i$ vào tập hợp $S$.
    - Tỷ số $\frac{|S|!(|F| - |S| - 1)!}{|F|!}$ là trọng số tổ hợp xác suất, tương ứng với tỷ lệ xuất hiện của cấu hình liên minh $S$ khi các đặc trưng được đưa vào theo thứ tự ngẫu nhiên.
- Ba tính chất toán học nền tảng bắt buộc của SHAP:
  - 1. Tính Chính xác Cục bộ (Local Accuracy / Additivity):
    - Tổng giá trị đóng góp của tất cả các đặc trưng cộng với giá trị kỳ vọng nền bằng chính giá trị dự báo của mô hình:
      $$f(x) = \phi_0 + \sum_{i=1}^{|F|} \phi_i(x), \quad \text{với } \phi_0 = \mathbb{E}[f(X)]$$
    - Tính chất này bảo đảm mô hình giải thích hoàn toàn khớp với đầu ra thực tế của mô hình gốc.
  - 2. Tính Bị khuyết (Missingness):
    - Nếu một đặc trưng không hiện diện trong quan sát đầu vào của mẫu thử, giá trị đóng góp gán cho nó bằng 0:
      $$x_i = \text{missing} \implies \phi_i = 0$$
  - 3. Tính Nhất quán (Consistency):
    - Nếu cấu trúc mô hình thay đổi khiến đóng góp biên của đặc trưng $i$ tăng lên hoặc giữ nguyên đối với mọi tập con $S$, thì giá trị $\phi_i$ của nó trên mô hình mới không bao giờ giảm:
      $$\forall S, \left[ f'_x(S \cup \{i\}) - f'_x(S) \ge f_x(S \cup \{i\}) - f_x(S) \right] \implies \phi_i(f', x) \ge \phi_i(f, x)$$
- Ba cấp độ phân tích thực nghiệm của SHAP trong nghiên cứu MBR:
  - Phân tích Cục bộ (Local Interpretation):
    - Sử dụng biểu đồ thác nước (Waterfall plot) hoặc biểu đồ lực đẩy (Force plot).
    - Định lượng chính xác từng yếu tố làm tăng hay giảm nguy cơ tắc nghẽn màng tại một thời điểm vận hành cụ thể.
  - Phân tích Toàn cục (Global Interpretation):
    - Sử dụng biểu đồ tóm tắt SHAP (Beeswarm plot) và biểu đồ cột xếp hạng tầm quan trọng (Bar plot).
    - Xác định xếp hạng tổng thể của các biến vận hành trên toàn bộ cơ sở dữ liệu.
    - Màu sắc hiển thị giá trị thực tế của biến (đỏ: cao, xanh: thấp) kết hợp trục hoành $\phi_i$ cho biết hướng tác động lên thông lượng hoặc TMP.
  - Phân tích Tương tác Đặc trưng (Feature Interaction):
    - Sử dụng biểu đồ phụ thuộc SHAP (SHAP dependence plot).
    - Bóc tách tương tác phi tuyến bậc hai giữa hai biến (ví dụ tác động hiệp đồng giữa nồng độ polysaccharide ngoại bào EPS và nhiệt độ nước thải lên sức cản bánh bùn).

---

### 3.4 Bảng Hướng dẫn Lựa chọn Mô hình Học máy (Model Selection Guide)

#### 3.4.1 Quy trình Ra Quyết định Phân tầng (Hierarchical Decision Workflow)
- Bước 1: Xác định loại dữ liệu và cấu trúc nhãn mục tiêu:
  - Dữ liệu không có nhãn đầu ra $\to$ Sử dụng các thuật toán Học không giám sát (Unsupervised Learning):
    - Phân cụm K-means, Phân cụm phân cấp (Hierarchical Clustering), Phân tích thành phần chính (PCA) để phân loại cụm bùn hoặc phát hiện dị biệt.
  - Dữ liệu có nhãn đầu ra liên tục $\to$ Sử dụng các bài toán Hồi quy (Regression):
    - Dự báo thông lượng thấm (membrane flux), áp suất xuyên màng (TMP), điện trở màng tổng cộng ($R_t$), hiệu suất loại bỏ chất ô nhiễm (COD, $\text{NH}_4^+$, TN, TP).
    - Các mô hình phù hợp: SVR, Random Forest, GBDT, XGBoost, ANN, MLP.
  - Dữ liệu có nhãn đầu ra rời rạc hoặc phân loại $\to$ Sử dụng các bài toán Phân loại (Classification):
    - Nhận diện trạng thái tắc nghẽn (bình thường / tắc nghẽn nhẹ / nghẽn nghiêm trọng), dự đoán sự cố sốc tải vi sinh.
    - Các mô hình phù hợp: SVC, Random Forest Classifier, ANN, Naive Bayes.
  - Tác vụ tối ưu hóa chuỗi quyết định thích nghi $\to$ Sử dụng Học tăng cường (Reinforcement Learning - RL):
    - Tự động điều khiển chu kỳ bật tắt sục khí, điều tiết van rửa ngược màng theo thời gian thực nhằm tiết kiệm năng lượng.
- Bước 2: Đánh giá theo Kích thước Mẫu Dữ liệu ($N$):
  - Kích thước mẫu hạn chế ($N < 500$ mẫu):
    - Ưu tiên lựa chọn: Máy vector hỗ trợ (SVM/SVR), Rừng ngẫu nhiên (Random Forest), hoặc Mạng nơ-ron nhiều tầng cấu trúc nông (MLP với 1-2 lớp ẩn).
    - Lý do: Các mô hình này kiểm soát hiện tượng quá khớp rất tốt trên tập dữ liệu nhỏ nhờ cơ chế biên cực đại (SVM) hoặc lấy mẫu ngẫu nhiên đóng bao (RF).
  - Kích thước mẫu lớn ($N > 10,000$ mẫu):
    - Ưu tiên lựa chọn: Mạng nơ-ron sâu (Deep Neural Network - DNN), Mạng nơ-ron hồi quy sâu.
    - Lý do: Mạng nơ-ron sâu giải phóng sức mạnh biểu diễn phi tuyến cao khi được cung cấp đủ dữ liệu lớn, tránh bão hòa hiệu năng như các mô hình truyền thống.
- Bước 3: Phù hợp Cấu trúc Không gian và Thời gian của Dữ liệu:
  - Dữ liệu chuỗi thời gian liên tục (Time-series data: dữ liệu cảm biến đo online lưu lượng, nhiệt độ, pH, DO theo từng giây/phút):
    - Lựa chọn mô hình có bộ nhớ hồi quy: LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit), RNN.
  - Dữ liệu dạng ma trận hoặc hình ảnh (Ảnh chụp cấu trúc bề mặt màng bằng kính hiển vi điện tử quét SEM, ảnh phân bố vi sinh vật bằng kính hiển vi huỳnh quang CLSM):
    - Lựa chọn Mạng nơ-ron Tích chập (Convolutional Neural Network - CNN) để trích xuất đặc trưng hình thái lỗ xốp và lớp bánh bùn.
  - Dữ liệu có cấu trúc đồ thị topo mạng lưới (Mạng lưới phân phối đường ống, cấu trúc liên kết chuỗi thức ăn sinh thái vi sinh vật trong bùn hoạt tính):
    - Lựa chọn Mạng nơ-ron Đồ thị (Graph Neural Network - GNN).

#### 3.4.2 Ma trận Lựa chọn Mô hình theo 5 Tiêu chí Kỹ thuật
- Tiêu chí 1: Số lượng mẫu dữ liệu khả dụng ($N$): Phân định khả năng huấn luyện hiệu quả từ tập dữ liệu vi mô đến dữ liệu lớn.
- Tiêu chí 2: Số chiều của không gian đặc trưng ($P$): Đánh giá năng lực xử lý khi dữ liệu có nhiều biến quan trắc đầu vào.
- Tiêu chí 3: Bản chất quan hệ phi tuyến (Non-linearity): Đánh giá khả năng xấp xỉ các phản ứng sinh học và thủy lực phức tạp trong MBR.
- Tiêu chí 4: Chi phí tính toán huấn luyện và triển khai (Computational Resource Cost): Xem xét tài nguyên phần cứng và tốc độ đáp ứng thời gian thực.
- Tiêu chí 5: Yêu cầu về mức độ minh bạch và giải thích cơ chế (Interpretability Need): Đánh giá khả năng hiểu rõ quy luật vận hành phục vụ ra quyết định kỹ thuật.

#### 3.4.3 Bảng So sánh Tổng hợp và Khuyến nghị Mô hình trong Nghiên cứu MBR

| Thuật toán Học máy | Cỡ mẫu khuyến nghị ($N$) | Năng lực Phi tuyến | Chi phí Huấn luyện | Khả năng Giải thích | Ưu điểm cốt lõi trong MBR | Nhược điểm cốt lõi trong MBR | Ứng dụng điển hình trong MBR |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hồi quy Tuyến tính / Ridge / Lasso** | Nhỏ đến lớn ($N \ge 30$) | Thấp (chỉ giải quyết quan hệ tuyến tính) | Rất thấp (tính toán giải tích tức thì) | Rất cao (hộp trắng, trọng số biểu thị hệ số trực tiếp) | Cực kỳ nhanh, không bị quá khớp khi số mẫu ít, dễ chuẩn hóa | Không mô phỏng được quá trình tắc nghẽn màng phi tuyến phức tạp | Đánh giá sơ bộ mối quan hệ cơ bản giữa các thông số nước thải |
| **K-Nearest Neighbors (KNN)** | Nhỏ đến trung bình ($50 < N < 2000$) | Trung bình (phi tuyến cục bộ dựa trên khoảng cách) | Thấp khi huấn luyện, cao khi suy luận dự báo | Trung bình (dựa trên các trường hợp láng giềng cụ thể) | Trực quan, không cần giả định phân phối dữ liệu, dễ triển khai | Rất nhạy cảm với dữ liệu nhiễu và bùng nổ số chiều đặc trưng | Phân loại trạng thái vận hành MBR dựa trên các ca vận hành tương đồng |
| **Support Vector Machine (SVM / SVR)** | Nhỏ đến trung bình ($50 < N < 5000$) | Rất cao (thông qua các hàm nhân phi tuyến RBF, Poly) | Trung bình đến cao (độ phức tạp $\mathcal{O}(N^2)$ đến $\mathcal{O}(N^3)$) | Thấp (mô hình hộp đen, phụ thuộc hàm nhân) | Hiệu năng dự báo vượt trội trên tập dữ liệu nhỏ, khả năng khái quát hóa cao | Tốn kém bộ nhớ khi dữ liệu lớn, nhạy cảm với việc chọn siêu tham số $C, \gamma, \epsilon$ | Dự báo áp suất xuyên màng TMP, dự đoán điện trở màng và thông lượng |
| **Random Forest (RF)** | Trung bình đến lớn ($N > 100$) | Rất cao (tổng hợp từ hàng trăm cây quyết định) | Trung bình (hỗ trợ phân tán song song tốt) | Khá cao (tính được MDI, OOB importance, kết hợp SHAP tốt) | Không bị quá khớp, chịu đựng tốt dữ liệu thiếu và nhiễu ngoại lai | Có thể bị chậm khi suy luận thời gian thực nếu số lượng cây quá lớn | Dự đoán hiệu suất loại bỏ chất ô nhiễm COD, N, P và chẩn đoán tắc nghẽn |
| **Gradient Boosted Decision Trees (GBDT / XGBoost / LightGBM)** | Trung bình đến lớn ($N > 500$) | Cực cao (tối ưu hóa theo hàm mất mát gradient tuần tự) | Cao (huấn luyện tuần tự từng cây) | Khá cao (tương thích hoàn hảo với SHAP TreeExplainer) | Độ chính xác thực nghiệm cao hàng đầu đối với dữ liệu dạng bảng (tabular data) | Cần tinh chỉnh kỹ lưỡng siêu tham số để tránh quá khớp trên dữ liệu nhiễu | Dự báo tốc độ tắc nghẽn màng dài hạn, phân tích tương tác đa biến XAI |
| **Mạng Nơ-ron Nhân tạo (ANN / MLP)** | Trung bình đến lớn ($N > 500$) | Cực cao (định lý xấp xỉ phổ quát) | Cao (huấn luyện lan truyền ngược Backpropagation) | Rất thấp (hộp đen hoàn toàn, cần công cụ Garson hoặc SHAP) | Mô hình hóa linh hoạt mọi hàm phi tuyến phức tạp của hệ thống sinh học | Dễ rơi vào cực tiểu địa phương, đòi hỏi tiền xử lý chuẩn hóa dữ liệu chặt chẽ | Mô phỏng động học sinh học và diễn biến tắc nghẽn màng MBR |
| **Mạng Học sâu Hồi quy (LSTM / GRU)** | Lớn ($N > 2000$) | Cực cao (học biểu diễn phụ thuộc thời gian đa bước) | Rất cao (đòi hỏi xử lý tính toán GPU) | Rất thấp (cần kỹ thuật XAI chuyên sâu cho chuỗi thời gian) | Ghi nhớ phụ thuộc thời gian dài hạn cực tốt từ chuỗi tín hiệu cảm biến | Đòi hỏi lượng dữ liệu chuỗi liên tục rất lớn, thời gian huấn luyện dài | Dự báo chuỗi thời gian online TMP, tối ưu hóa chu kỳ sục khí động |
