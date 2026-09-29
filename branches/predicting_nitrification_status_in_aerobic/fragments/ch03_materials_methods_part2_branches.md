### 3. Vật liệu và phương pháp - Phần 2: Thuật toán ML, Chỉ số đánh giá và Giải thích hậu nghiệm

#### 3.1 Phân tích tương quan thống kê xác định đặc trưng đầu vào
##### 3.1.1 Phân tích ma trận tương quan Pearson và Spearman
###### 3.1.1.1 Cơ sở toán học của hệ số tương quan hạng Spearman
- Phương pháp Spearman là kỹ thuật thống kê phi tham số (nonparametric method).
- Phương pháp không yêu cầu dữ liệu tuân theo phân phối chuẩn (normal distribution).
- Công thức tính hệ số tương quan hạng Spearman giữa hai biến ngẫu nhiên $X$ và $Y$:
  $$r_s = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)}$$
- Biến $d_i = \text{rank}(X_i) - \text{rank}(Y_i)$ biểu thị chênh lệch giữa hai thứ hạng của quan sát thứ $i$.
- Đại lượng $n$ biểu thị tổng số mẫu dữ liệu phân tích ($n = 120$ mẫu).
- Hệ số $r_s$ nhận giá trị trong đoạn $[-1, 1]$.
- Giá trị $r_s = +1$ chỉ ra quan hệ đồng biến đơn điệu hoàn hảo (perfect monotonic positive association).
- Giá trị $r_s = -1$ chỉ ra quan hệ nghịch biến đơn điệu hoàn hảo (perfect monotonic negative association).
- Giá trị $r_s = 0$ chỉ ra việc không tồn tại mối liên hệ đơn điệu giữa hai biến.
- Kiểm định ý nghĩa thống kê sử dụng giá trị $p$ ($p\text{-value}$).
- Giả thuyết vô hiệu $H_0$ phát biểu: Không tồn tại quan hệ đơn điệu giữa hai biến trong tổng thể.
- Nghiên cứu đặt ngưỡng ý nghĩa thống kê $\alpha = 0.05$.
- Điều kiện $p < 0.05$ cho phép bác bỏ giả thuyết vô hiệu $H_0$.
- Hàm `scipy.stats.spearmanr` trong thư viện SciPy (Python 3.9.13) tính toán ma trận hệ số và giá trị $p$.

###### 3.1.1.2 Định lượng quan hệ giữa các biến đầu vào và nhãn trạng thái Nitrification
- Quá trình sàng lọc sơ bộ định tính ban đầu giữ lại 9 biến ứng viên từ hệ MBR.
- Ma trận Spearman định lượng mối quan hệ giữa 9 biến ứng viên và nhãn trạng thái nhị phân.
- Ba biến vận hành gồm: Lưu lượng khí cấp (Air Flow Rate), Lưu lượng nước vào (Influent Flow Rate) và Áp suất xuyên màng (TMP).
- Ba biến chất lượng dòng thấm gồm: Nồng độ $COD_{eff}$, $NO_3^- \text{-} N_{eff}$ và $NH_4^+ \text{-} N_{eff}$.
- Tương quan giữa $NH_4^+ \text{-} N_{eff}$ và nhãn phản ánh mức độ chuyển hóa cơ chất nitrogen:
  - Khi Nitrification diễn ra triệt để, nồng độ $NH_4^+ \text{-} N_{eff}$ giảm sâu về mức $0.9 \pm 0.2 \text{ mg/L}$.
  - Nồng độ $NH_4^+ \text{-} N_{eff}$ thể hiện tương quan âm rất mạnh và có ý nghĩa thống kê cao ($p < 0.001$).
- Tương quan giữa $NO_3^- \text{-} N_{eff}$ và nhãn phản ánh sự tích lũy sản phẩm cuối:
  - Phản ứng oxy hóa hoàn toàn tạo ra lượng lớn ion nitrate trong nước sau lọc.
  - Nồng độ $NO_3^- \text{-} N_{eff}$ thể hiện tương quan dương mạnh mẽ với nhãn trạng thái ($p < 0.001$).
- Tương quan giữa lưu lượng khí cấp (Air Flow Rate: $2 \text{ L/min}$ và $6 \text{ L/min}$) và nhãn:
  - Tốc độ sục khí quyết định trực tiếp tốc độ chuyển khối oxy hòa tan vào sinh khối bùn.
  - Tương quan thể hiện giá trị dương có ý nghĩa thống kê ($p < 0.05$).

###### 3.1.1.3 Đánh giá hiện tượng đa cộng tuyến và sàng lọc tối ưu tập đặc trưng
- Hiện tượng đa cộng tuyến (Multicollinearity) xuất hiện khi hai biến đầu vào tương quan tuyến tính rất cao.
- Lưu lượng nước đầu vào (Influent Flow Rate: $11.7 - 20.6 \text{ mL/min}$) và lưu lượng dòng thấm ra (Effluent Flow Rate) có tương quan $r_s > 0.98$.
- Màng phẳng SiC duy trì độ phục hồi lưu lượng dòng thấm vượt mức $97\%$.
- Nhóm nghiên cứu loại bỏ biến Effluent Flow Rate nhằm triệt tiêu dư thừa thông tin.
- Áp suất xuyên màng (TMP) thể hiện tương quan thống kê yếu với trạng thái Nitrification ngắn hạn.
- Nhóm nghiên cứu vẫn giữ lại biến TMP ($< 10 \text{ kPa}$) trong tập đặc trưng:
  - Biến TMP phản ánh trạng thái bám bẩn bề mặt màng (membrane fouling) theo chu kỳ dài.
  - Biến TMP nâng cao năng lực thích ứng mô hình khi vận hành liên tục 235 ngày.
- Bản ghi rửa màng (membrane cleaning record) tương quan chặt với TMP nhưng bị loại bỏ:
  - Quyết định này giúp loại trừ độ lệch phụ thuộc vật liệu màng cụ thể (material-specific biases).
- Nồng độ tổng nitơ ($TN$) thể hiện tương quan với trạng thái phản ứng nhưng bị loại bỏ:
  - Cảm biến đo $TN$ trực tuyến thương mại có chi phí thiết bị và bảo trì rất cao.
  - Cảm biến $TN$ yêu cầu thời gian phân tích mẫu trễ từ $30 - 60 \text{ phút}$.
  - Độ trễ này không đáp ứng yêu cầu điều khiển sục khí phản hồi nhanh.
- Biến oxy hòa tan ($DO$) bị loại bỏ do tỷ lệ dữ liệu bị khuyết vượt mức $50\%$.
- Bộ 6 đặc trưng rút gọn cuối cùng gồm:
  $$\mathbf{x} = \left[ \text{Air Flow Rate}, \text{Influent Flow Rate}, \text{TMP}, COD_{eff}, NO_3^- \text{-} N_{eff}, NH_4^+ \text{-} N_{eff} \right]^T$$

---

#### 3.2 Khả năng giải thích nội tại mô hình: Ba thuật toán học máy đại diện
##### 3.2.1 Hồi quy Logistic (Logistic Regression - LR)
###### 3.2.1.1 Cấu trúc toán học và ánh xạ xác suất
- Hồi quy Logistic thiết lập mối liên hệ tuyến tính giữa các biến độc lập và log-odds của nhãn mục tiêu.
- Vector đầu vào gồm 6 đặc trưng: $\mathbf{x} = [x_1, x_2, \dots, x_6]^T \in \mathbb{R}^6$.
- Hàm tuyến tính kết hợp vector trọng số $\boldsymbol{\beta} = [\beta_1, \dots, \beta_6]^T$ và hệ số chặn $\beta_0$:
  $$z = \beta_0 + \sum_{j=1}^6 \beta_j x_j = \boldsymbol{\beta}^T \mathbf{x} + \beta_0$$
- Hàm kích hoạt Sigmoid (Logistic function) ánh xạ miền giá trị $z \in (-\infty, +\infty)$ sang khoảng xác suất $(0, 1)$:
  $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
- Xác suất dự báo mẫu thuộc lớp Nitrification đầy đủ ($y = 1$):
  $$P(y=1|\mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \sum_{j=1}^6 \beta_j x_j)}}$$
- Xác suất dự báo mẫu thuộc lớp Nitrification không đầy đủ ($y = 0$):
  $$P(y=0|\mathbf{x}) = 1 - P(y=1|\mathbf{x}) = \frac{e^{-(\beta_0 + \sum_{j=1}^6 \beta_j x_j)}}{1 + e^{-(\beta_0 + \sum_{j=1}^6 \beta_j x_j)}}$$

###### 3.2.1.2 Hàm mất mát và cơ chế tối ưu hóa
- Mô hình ước lượng vector tham số $\boldsymbol{\beta}$ thông qua cực tiểu hóa hàm mất mát Negative Log-Likelihood:
  $$\mathcal{L}_{LR}(\boldsymbol{\beta}) = -\frac{1}{m} \sum_{i=1}^m \left[ y_i \ln\left(\hat{y}_i\right) + (1 - y_i) \ln\left(1 - \hat{y}_i\right) \right] + \frac{1}{2C} \|\boldsymbol{\beta}\|_2^2$$
- Ký hiệu $m$ biểu thị số lượng mẫu trong tập huấn luyện ($m = 78$ mẫu).
- Đại lượng $\hat{y}_i = P(y_i=1|\mathbf{x}_i)$ là xác suất đầu ra dự báo cho mẫu thứ $i$.
- Tham số $C$ kiểm soát cường độ chính quy hóa L2 (Ridge penalty).
- Thuật toán tối ưu hóa sử dụng phương pháp chuẩn L-BFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno).

###### 3.2.1.3 Đặc tính đánh đổi và khả năng giải thích trực tiếp
- Mô hình LR có cấu trúc giả định tuyến tính cố định.
- Đặc tính đánh đổi mô hình: Độ chệch cao (High bias), phương sai thấp (Low variance).
- Rủi ro quá mức khớp dữ liệu (overfitting) của LR ở mức rất thấp trên tập dữ liệu nhỏ ($n = 78$).
- Khả năng giải thích nội tại thông qua tỷ số chênh (Odds Ratio - OR):
  $$\text{Odds} = \frac{P(y=1|\mathbf{x})}{1 - P(y=1|\mathbf{x})} = \exp\left(\beta_0 + \sum_{j=1}^6 \beta_j x_j\right)$$
  $$\ln(\text{Odds}) = \beta_0 + \beta_1 x_1 + \dots + \beta_6 x_6$$
- Dấu của trọng số $\beta_j$ biểu thị chiều tác động trực tiếp của biến:
  - Giá trị $\beta_j > 0$ nghĩa là tăng đặc trưng $x_j$ sẽ làm tăng xác suất đạt chuẩn Nitrification.
  - Giá trị $\beta_j < 0$ nghĩa là tăng đặc trưng $x_j$ sẽ làm giảm xác suất đạt chuẩn Nitrification.
- Độ lớn tuyệt đối $|\beta_j|$ định lượng mức độ đóng góp tuyến tính của đặc trưng vào hàm quyết định.

##### 3.2.2 Rừng ngẫu nhiên (Random Forest - RF)
###### 3.2.2.1 Nguyên lý kết hợp Bagging và không gian ngẫu nhiên
- Random Forest là thuật toán học máy kết hợp (ensemble learning) dựa trên kỹ thuật Bagging (Bootstrap Aggregating).
- Thuật toán xây dựng một tập hợp gồm $B$ cây quyết định phân loại độc lập: $\{T_b\}_{b=1}^B$.
- Mỗi cây con $T_b$ được huấn luyện trên một tập dữ liệu con kích thước $m$.
- Tập dữ liệu con được tạo bằng cách rút mẫu có hoàn lại (bootstrap sample) từ tập huấn luyện gốc.
- Tính ngẫu nhiên đặc trưng (Feature bagging):
  - Tại mỗi nút phân nhánh, thuật toán chỉ chọn ngẫu nhiên một tập con gồm $m_{try}$ đặc trưng từ tổng số $p = 6$ đặc trưng:
    $$m_{try} \approx \sqrt{p} = \sqrt{6} \approx 2$$
  - Cây tìm kiếm điểm cắt tối ưu duy nhất trong phạm vi tập con $m_{try}$ đặc trưng này.
- Quy tắc giảm tương quan giữa các cây phân nhánh (de-correlating trees) ngăn ngừa các cây giống nhau.

###### 3.2.2.2 Giảm thiểu phương sai mà không làm tăng độ chệch
- Phương sai của trung bình $B$ biến ngẫu nhiên có cùng phương sai $\sigma^2$ và hệ số tương quan cặp $\rho$:
  $$\text{Var}(\bar{T}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$
- Khi số lượng cây $B$ tăng lên đủ lớn, thành phần $\frac{1 - \rho}{B} \sigma^2$ triệt tiêu dần về 0.
- Phương sai tổng thể của mô hình RF tiệm cận giới hạn dưới:
  $$\lim_{B \to \infty} \text{Var}(f_{RF}) = \rho \sigma^2$$
- Kỹ thuật chọn ngẫu nhiên đặc trưng làm giảm mạnh hệ số tương quan $\rho$ giữa các cây.
- Kết quả là RF giảm thiểu đáng kể phương sai mà vẫn duy trì độ chệch thấp của từng cây quyết định riêng lẻ.
- Dự báo phân loại thực hiện qua cơ chế biểu quyết đa số (majority voting):
  $$\hat{y}_{RF}(\mathbf{x}) = \text{mode} \left\{ T_1(\mathbf{x}), T_2(\mathbf{x}), \dots, T_B(\mathbf{x}) \right\}$$
- Xác suất trung bình của lớp dương tính:
  $$P_{RF}(y=1|\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B P_{T_b}(y=1|\mathbf{x})$$

###### 3.2.2.3 Độ quan trọng đặc trưng dựa trên chỉ số giảm độ mờ Gini
- Độ mờ Gini (Gini Impurity) tại nút $t$ đo lường độ không thuần nhất của các mẫu:
  $$I_G(t) = 1 - \sum_{k=0}^1 p_k(t)^2$$
- Ký hiệu $p_k(t)$ là tỷ lệ mẫu thuộc lớp $k \in \{0, 1\}$ tại nút $t$.
- Mức giảm độ mờ Gini khi phân chia nút $t$ thành nút con trái $t_L$ và nút con phải $t_R$:
  $$\Delta I_G(t) = I_G(t) - \frac{N_L}{N_t} I_G(t_L) - \frac{N_R}{N_t} I_G(t_R)$$
- Điểm quan trọng đặc trưng toàn cục MDI (Mean Decrease Impurity) của biến $x_j$:
  $$\text{MDI}(x_j) = \frac{1}{B} \sum_{b=1}^B \sum_{t \in T_b, v(t)=j} \frac{N_t}{N_{total}} \Delta I_G(t)$$
- Biến $v(t) = j$ biểu thị nút $t$ sử dụng đặc trưng $x_j$ để thực hiện phân tách.

##### 3.2.3 Tăng cường độ dốc cực đại (Extreme Gradient Boosting - XGBoost)
###### 3.2.3.1 Cơ chế Boosting tuần tự và hàm mục tiêu chính quy hóa
- Thuật toán XGBoost xây dựng mô hình cộng dồn tuần tự qua $K$ vòng lặp cây quyết định:
  $$\hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + f_t(\mathbf{x}_i), \quad f_t \in \mathcal{F}$$
- Không gian hàm $\mathcal{F}$ biểu thị tập hợp tất cả các cây hồi quy (Classification and Regression Trees - CART).
- Hàm mục tiêu tổng quát tại bước lặp $t$ tích hợp số hạng phạt độ phức tạp cấu trúc:
  $$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t-1)} + f_t(\mathbf{x}_i)\right) + \Omega(f_t)$$
- Hàm phạt chính quy hóa $\Omega(f_t)$ ngăn ngừa hiện tượng quá mức khớp:
  $$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
- Ký hiệu $T$ biểu thị tổng số lá của cây thứ $t$.
- Vector $\mathbf{w} = [w_1, w_2, \dots, w_T]^T$ đại diện cho trọng số giá trị dự báo tại mỗi nút lá.
- Tham số $\gamma$ kiểm soát ngưỡng phân nhánh tối thiểu.
- Tham số $\lambda$ đại diện cho hệ số co ngót chính quy hóa L2 trên các nút lá.

###### 3.2.3.2 Xấp xỉ chuỗi Taylor bậc hai và tiêu chuẩn phân tách nhánh Gain
- XGBoost áp dụng khai triển Taylor bậc hai trên hàm mục tiêu quanh điểm dự báo bước trước $\hat{y}_i^{(t-1)}$:
  $$\tilde{\mathcal{L}}^{(t)} \approx \sum_{i=1}^n \left[ l\left(y_i, \hat{y}_i^{(t-1)}\right) + g_i f_t(\mathbf{x}_i) + \frac{1}{2} h_i f_t^2(\mathbf{x}_i) \right] + \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
- Gradient bậc một của hàm mất mát đối với giá trị dự đoán:
  $$g_i = \partial_{\hat{y}^{(t-1)}} l\left(y_i, \hat{y}^{(t-1)}\right)$$
- Hessian bậc hai của hàm mất mát đối với giá trị dự đoán:
  $$h_i = \partial^2_{\hat{y}^{(t-1)}} l\left(y_i, \hat{y}^{(t-1)}\right)$$
- Loại bỏ các hằng số độc lập với $f_t$, hàm mục tiêu rút gọn trên các tập mẫu thuộc nút lá $I_j = \{i | q(\mathbf{x}_i) = j\}$:
  $$\tilde{\mathcal{L}}^{(t)} = \sum_{j=1}^T \left[ \left(\sum_{i \in I_j} g_i\right) w_j + \frac{1}{2} \left(\sum_{i \in I_j} h_i + \lambda\right) w_j^2 \right] + \gamma T$$
- Đặt $G_j = \sum_{i \in I_j} g_i$ và $H_j = \sum_{i \in I_j} h_i$.
- Trọng số tối ưu tại lá $j$ được giải tích trực tiếp:
  $$w_j^* = -\frac{G_j}{H_j + \lambda}$$
- Giá trị mất mát cực tiểu tương ứng của cấu trúc cây:
  $$\tilde{\mathcal{L}}^{(t)}(q) = -\frac{1}{2} \sum_{j=1}^T \frac{G_j^2}{H_j + \lambda} + \gamma T$$
- Điểm đánh giá mức tăng chất lượng phân nhánh (Gain) khi chia nút thành hai lá $L$ và $R$:
  $$\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$
- Nếu $\text{Gain} \le 0$, thuật toán dừng mở rộng nhánh (cắt tỉa tự động).

###### 3.2.3.3 Đặc tính đánh đổi Bias-Variance của ba thuật toán
- Hồi quy Logistic (LR):
  - Thuộc tính: Độ chệch cao, phương sai rất thấp.
  - Phù hợp nhất cho bài toán tuyến tính hoặc dữ liệu quy mô nhỏ.
  - Hạn chế bỏ sót các tương tác phi tuyến phức tạp giữa các chất phản ứng sinh học.
- Rừng ngẫu nhiên (RF):
  - Thuộc tính: Cân bằng trung gian giữa độ chệch và phương sai.
  - Triệt tiêu phương sai thông qua lấy mẫu ngẫu nhiên độc lập.
  - Khả năng chống chịu nhiễu và độ lệch phân bố cực tốt trên môi trường sinh học không ổn định.
- Tăng cường độ dốc cực đại (XGBoost):
  - Thuộc tính: Độ chệch rất thấp, phương sai cao.
  - Năng lực khớp dữ liệu phi tuyến mạnh mẽ trên tập huấn luyện.
  - Dễ gặp rủi ro quá mức khớp khi tập dữ liệu bị mất cân bằng và kích thước mẫu nhỏ ($n = 78$).

---

#### 3.3 Chỉ số đánh giá hiệu năng và tiêu chí tinh chỉnh siêu tham số
##### 3.3.1 Ma trận nhầm lẫn và các chỉ số đo lường hiệu năng
###### 3.3.1.1 Bốn thành phần cốt lõi của ma trận nhầm lẫn
- Bảng ma trận đối sánh giữa giá trị thực tế và giá trị dự báo từ mô hình:
  - Dương tính thật (True Positive - TP): Mẫu thực tế đạt Nitrification đầy đủ, mô hình dự đoán chính xác là Đầy đủ.
  - Dương tính giả (False Positive - FP): Mẫu thực tế không đạt Nitrification, mô hình dự đoán nhầm là Đầy đủ (Sai lầm loại I).
  - Âm tính giả (False Negative - FN): Mẫu thực tế đạt Nitrification đầy đủ, mô hình dự đoán nhầm là Không đầy đủ (Sai lầm loại II).
  - Âm tính thật (True Negative - TN): Mẫu thực tế không đạt Nitrification, mô hình dự đoán chính xác là Không đầy đủ.

###### 3.3.1.2 Các công thức định lượng hiệu năng phân loại
- Tỷ lệ phát hiện thực thể (True Positive Rate - TPR) hay Độ nhạy (Sensitivity / Recall):
  $$\text{TPR} = \frac{TP}{TP + FN}$$
  - Công thức phản ánh tỷ lệ các trường hợp Nitrification đạt chuẩn được mô hình nhận diện thành công.
- Tỷ lệ dương tính sai lầm (False Positive Rate - FPR) hay Tỷ lệ báo động nhầm:
  $$\text{FPR} = \frac{FP}{FP + TN}$$
  - Công thức phản ánh tỷ lệ mẫu chưa đạt yêu cầu xử lý nhưng bị gán nhầm nhãn an toàn.
- Độ chuẩn xác dự báo dương (Precision):
  $$\text{Precision} = \frac{TP}{TP + FP}$$
  - Công thức đo lường mức độ tin cậy khi mô hình phát ra tín hiệu khẳng định nước sau lọc đạt chuẩn.
- Độ chuẩn xác toàn cục (Accuracy):
  $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
  - Công thức phản ánh tỷ lệ dự đoán đúng trên toàn bộ tập dữ liệu quan sát.
- Điểm số điều hòa F1 (F1-score):
  $$\text{F1-score} = 2 \cdot \frac{\text{Precision} \cdot \text{TPR}}{\text{Precision} + \text{TPR}} = \frac{2 TP}{2 TP + FP + FN}$$
- Diện tích dưới đường cong ROC (Receiver Operating Characteristic - AUC-ROC):
  $$\text{AUC} = \int_{0}^{1} \text{TPR}(\tau) \, d(\text{FPR}(\tau))$$
  - Chỉ số phản ánh năng lực phân tách tổng quát giữa hai lớp nhãn trên toàn dải ngưỡng quyết định $\tau \in [0, 1]$.

###### 3.3.1.3 Ví dụ tính toán thực chứng: Đánh giá hiệu năng và ma trận nhầm lẫn của mô hình Random Forest
- **Bài toán (Problem)**:
  Tính toán các chỉ số hiệu năng phân loại gồm $\text{TPR}$, $\text{FPR}$, $\text{Precision}$, $\text{Accuracy}$, $\text{F1-score}$ cho mô hình Random Forest trên tập kiểm tra độc lập ($n = 19$). Phân tích định lượng rủi ro an toàn nước xám khi phát sinh sai số dương tính giả.
- **Dữ liệu cho trước (Given)**:
  - Tổng số mẫu kiểm tra độc lập: $N = 19$ mẫu (không bổ sung giá thể).
  - Số mẫu thực tế đạt Nitrification đầy đủ (Positive): $N_{pos} = 8$ mẫu.
  - Số mẫu thực tế không đạt Nitrification (Negative): $N_{neg} = 11$ mẫu.
  - Kết quả phân loại thực nghiệm từ mô hình RF:
    - Dương tính thật ($TP$): $5$ mẫu.
    - Âm tính giả ($FN$): $3$ mẫu.
    - Dương tính giả ($FP$): $1$ mẫu.
    - Âm tính thật ($TN$): $10$ mẫu.
- **Công thức áp dụng (Formula)**:
  - $\text{TPR} = \frac{TP}{TP + FN}$
  - $\text{FPR} = \frac{FP}{FP + TN}$
  - $\text{Precision} = \frac{TP}{TP + FP}$
  - $\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$
  - $\text{F1-score} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$
- **Các bước tính toán (Steps)**:
  - *Bước 1: Tính tỷ lệ phát hiện thực thể (Độ nhạy - $\text{TPR}$)*:
    $$\text{TPR} = \frac{5}{5 + 3} = \frac{5}{8} = 0.6250 \quad (62.50\%)$$
  - *Bước 2: Tính tỷ lệ dương tính sai lầm ($\text{FPR}$)*:
    $$\text{FPR} = \frac{1}{1 + 10} = \frac{1}{11} \approx 0.0909 \quad (9.09\%)$$
  - *Bước 3: Tính độ chuẩn xác dự báo dương ($\text{Precision}$)*:
    $$\text{Precision} = \frac{5}{5 + 1} = \frac{5}{6} \approx 0.8333 \quad (83.33\%)$$
  - *Bước 4: Tính độ chính xác toàn cục ($\text{Accuracy}$)*:
    $$\text{Accuracy} = \frac{5 + 10}{19} = \frac{15}{19} \approx 0.7895 \quad (78.95\%)$$
  - *Bước 5: Tính điểm điều hòa F1 ($\text{F1-score}$)*:
    $$\text{F1-score} = \frac{2 \cdot 5}{2 \cdot 5 + 1 + 3} = \frac{10}{14} \approx 0.7143 \quad (71.43\%)$$
  - *Bước 6: Phân tích rủi ro kỹ thuật chất lượng nước*:
    - Giá trị $\text{FPR} = 0.0909$ biểu thị $1$ mẫu nước xám chưa đạt chuẩn bị gán nhãn an toàn.
    - Sự cố này dẫn tới rủi ro xả nước chứa $NH_4^+ > 0.9 \text{ mg/L}$ vào hệ thống tái sử dụng.
    - Giá trị $\text{TPR} = 0.6250$ phản ánh sự suy giảm từ tập validation ($> 0.90$) do độ lệch phân bố lưu lượng khí.
- **Kết quả tổng hợp (Result)**:
  - $\text{TPR} = 0.6250$, $\text{FPR} = 0.0909$, $\text{Precision} = 0.8333$, $\text{Accuracy} \approx 0.79$, $\text{F1-score} \approx 0.7143$. Mô hình đạt Precision vượt ngưỡng 0.80 nhưng cần tiếp tục nén FPR.

##### 3.3.2 Cơ sở ưu tiên tối đa hóa Precision trong quản lý chất lượng nước
###### 3.3.2.1 Phân tích rủi ro môi trường và bất đối xứng chi phí
- Sai lầm dương tính giả (FP) gây ra thảm họa chất lượng trong quy trình tái sử dụng nước xám:
  - Khi xuất hiện sự cố sụt giảm vi sinh tự dưỡng, Nitrification bị gián đoạn sinh học.
  - Nước sau lọc còn tồn dư nồng độ cao ammonium ($NH_4^+$) và nitrite ($NO_2^-$).
  - Nếu mô hình dự báo nhầm là "Sufficient" (FP), bộ điều khiển tự động sẽ không kích hoạt tăng cường sục khí.
  - Lượng nước xám độc hại chưa được khử nitơ sẽ được dẫn thẳng vào mục đích tái sử dụng (xả bồn cầu, tưới tiêu đô thị).
  - Sự cố này gây nguy hiểm trực tiếp cho sức khỏe con người và vi phạm quy chuẩn xả thải EU Directive 91/271/EEC.
- Sai lầm âm tính giả (FN) chỉ gây tổn thất kinh tế nhỏ:
  - Mô hình cảnh báo nhầm là "Insufficient" khi hệ thống đã đạt Nitrification hoàn toàn.
  - Bộ điều khiển kích hoạt cấp thêm khí nén tạm thời vào bể MBR.
  - Hậu quả chỉ là tiêu tốn thêm một phần điện năng thổi khí không cần thiết.
- Kết luận kỹ thuật: Chi phí rủi ro của sai lầm FP lớn hơn rất nhiều so với sai lầm FN.
- Do đó, mục tiêu tối thượng của mô hình giám sát là triệt tiêu tối đa tỷ lệ FPR và cực đại hóa chỉ số Precision.

###### 3.3.2.2 Quy tắc điều chỉnh ngưỡng quyết định
- Ngưỡng quyết định mặc định của các thuật toán phân loại xác suất là $\theta = 0.5$:
  $$\hat{y} = \begin{cases} 1 & \text{khi } P(y=1|\mathbf{x}) \ge \theta \\ 0 & \text{khi } P(y=1|\mathbf{x}) < \theta \end{cases}$$
- Tối ưu hóa cho hệ thống chất lượng nước áp dụng quy tắc dịch chuyển ngưỡng bảo thủ:
  - Nâng ngưỡng phân loại lên mức cao hơn: $\theta^* > 0.5$ (ví dụ: $\theta^* = 0.65 - 0.75$).
  - Mô hình chỉ xác nhận trạng thái Nitrification đầy đủ khi bằng chứng dữ liệu có xác suất vượt trội.
  - Biện pháp này trực tiếp nén số lượng ca FP về mức 0, ép tỷ lệ FPR xuống ngưỡng an toàn.
  - Đánh đổi kỹ thuật: Tăng Precision sẽ kéo theo suy giảm một phần tỷ lệ phát hiện thực thể TPR.

###### 3.3.2.3 Quy trình kiểm chứng chéo 5-lớp phân tầng và đánh giá Bootstrap
- Tập dữ liệu huấn luyện và kiểm định nội bộ gồm 78 mẫu:
  - Lớp dương tính (Positive - Sufficient): 28 mẫu ($35.90\%$).
  - Lớp âm tính (Negative - Insufficient): 50 mẫu ($64.10\%$).
- Hiện tượng mất cân bằng lớp (class imbalance) biểu hiện rõ nét.
- Kỹ thuật kiểm chứng chéo 5-lớp phân tầng (Stratified 5-Fold Cross Validation):
  - Sử dụng module `StratifiedKFold` từ thư viện Scikit-Learn 1.0.2.
  - Phân chia 78 mẫu thành 5 tập con độc lập.
  - Mỗi tập con bắt buộc bảo toàn chính xác tỷ lệ phân bố nhãn gốc ($35.9\%$ Positive và $64.1\%$ Negative).
  - Ngăn ngừa hiện tượng phân bổ lệch mẫu dương tính giữa các fold gây méo mó hàm tối ưu.
- Tối ưu hóa siêu tham số bằng thuật toán tìm kiếm lưới (GridSearchCV):
  - Mục tiêu tối ưu hàm mục tiêu: $\max(\text{Precision})$.
  - Đối với LR: Tìm kiếm không gian tham số nghịch đảo điều hòa $C \in [10^{-3}, 10^3]$ và chuẩn phạt `penalty`.
  - Đối với RF: Tinh chỉnh số cây `n_estimators`, độ sâu tối đa `max_depth`, số đặc trưng ngẫu nhiên `max_features`.
  - Đối với XGBoost: Tinh chỉnh tốc độ học `learning_rate`, độ sâu `max_depth`, hệ số điều hòa `reg_lambda` ($\lambda$) và `gamma` ($\gamma$).
- Đánh giá độ ổn định mô hình bằng phương pháp tái lấy mẫu Bootstrap (Bootstrap resampling):
  - Thực hiện $N = 1000$ lần rút mẫu ngẫu nhiên có hoàn lại trên tập kiểm tra độc lập ($n = 19$ mẫu và $n = 23$ mẫu).
  - Ước lượng phân phối thực nghiệm của các chỉ số: Accuracy, Precision, Recall và F1-score.
  - Tính toán khoảng tin cậy $95\%$ ($95\%$ Confidence Interval - CI) định lượng mức độ ổn định vận hành:
    $$\text{CI}_{95\%} = \left[ q_{0.025}, \, q_{0.975} \right]$$

---

#### 3.4 Phương pháp giải thích hậu nghiệm (Post hoc interpretability)
##### 3.4.1 Phân tích giá trị đóng góp SHAP (SHapley Additive exPlanations)
###### 3.4.1.1 Cơ sở toán học lý thuyết trò chơi hợp tác
- Giá trị Shapley xuất phát từ lý thuyết trò chơi hợp tác liên minh cổ điển.
- Phương pháp coi tập hợp $F = \{1, 2, \dots, p\}$ gồm $p = 6$ biến đầu vào như các người chơi trong liên minh.
- Hàm giá trị $f(S)$ đo lường đầu ra dự báo của mô hình khi chỉ có tập con đặc trưng $S \subseteq F$ hiện diện.
- Giá trị đóng góp biên trung bình (marginal contribution) của đặc trưng thứ $i$ trên mọi liên minh khả dĩ:
  $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f(S \cup \{i\}) - f(S) \right]$$
- Đại lượng $|S|$ biểu thị số lượng đặc trưng đang có mặt trong liên minh $S$.
- Thành phần thừa số tổ hợp $\frac{|S|!(|F| - |S| - 1)!}{|F|!}$ là xác suất xuất hiện của thứ tự liên minh ngẫu nhiên.
- Hiệu số $[f(S \cup \{i\}) - f(S)]$ là giá trị đóng góp bổ sung khi thêm đặc trưng $i$ vào liên minh $S$.

###### 3.4.1.2 Ba tiên đề toán học bảo đảm tính nhất quán của SHAP
- Tiên đề 1: Tính hiệu quả (Efficiency):
  $$\sum_{i=1}^p \phi_i = f(\mathbf{x}) - \mathbb{E}[f(\mathbf{x})]$$
  - Tổng các giá trị đóng góp phân bổ $\phi_i$ của 6 đặc trưng bằng đúng độ lệch giữa giá trị dự báo thực tế $f(\mathbf{x})$ và giá trị dự báo kỳ vọng nền $\mathbb{E}[f(\mathbf{x})]$.
- Tiên đề 2: Tính đối xứng (Symmetry):
  - Nếu hai đặc trưng $i$ và $j$ đóng góp như nhau vào mọi liên minh:
    $$f(S \cup \{i\}) = f(S \cup \{j\}), \quad \forall S \subseteq F \setminus \{i, j\}$$
  - Khi đó giá trị Shapley của hai đặc trưng bắt buộc phải bằng nhau: $\phi_i = \phi_j$.
- Tiên đề 3: Tính cộng dồn (Additivity):
  - Nếu mô hình tổng hợp là tổng của hai mô hình độc lập $f(\mathbf{x}) = f_1(\mathbf{x}) + f_2(\mathbf{x})$, thì:
    $$\phi_i(f) = \phi_i(f_1) + \phi_i(f_2)$$

###### 3.4.1.3 Phân rã đóng góp toàn cục và cục bộ
- Biểu đồ phân tán đám đông (Beeswarm plot / Summary plot) phân tích tầm quan trọng toàn cục:
  - Sắp xếp 6 biến theo thứ tự giảm dần của độ lớn trung bình tuyệt đối giá trị Shapley:
    $$I_j = \frac{1}{n} \sum_{k=1}^n |\phi_j^{(k)}|$$
  - Vị trí điểm dọc trục hoành biểu thị giá trị $\phi_{ij}$ tác động tích cực ($> 0$) hoặc tiêu cực ($< 0$) tới đầu ra.
  - Màu sắc đại diện cho độ lớn thực tế của biến: Màu đỏ biểu thị giá trị cao, màu xanh biểu thị giá trị thấp.
  - Biểu đồ xác nhận vai trò áp đảo của $NH_4^+ \text{-} N_{eff}$ và $NO_3^- \text{-} N_{eff}$ trên cả 3 thuật toán LR, RF và XGB.
- Biểu đồ thác nước (Waterfall plot) phân rã cục bộ cho từng trường hợp quan sát:
  - Bắt đầu từ giá trị kỳ vọng nền $E[f(X)]$.
  - Từng thanh ngang cộng tích lũy lần lượt các giá trị $\phi_i$ tương ứng của mẫu.
  - Điểm kết thúc biểu đồ chạm đúng giá trị xác suất log-odds dự báo cuối cùng $f(\mathbf{x})$.
  - Cung cấp cơ chế giải thích minh bạch tại sao một mẫu nước xám cụ thể bị cảnh báo là Insufficient.

###### 3.4.1.4 Ví dụ tính toán thực chứng: Phân rã giá trị đóng góp SHAP cho một mẫu dự báo
- **Bài toán (Problem)**:
  Thực hiện phân rã cục bộ giá trị SHAP trên một mẫu nước xám thực tế. Chứng minh tiên đề hiệu quả (Efficiency axiom) và xác định xác suất dự báo trạng thái Nitrification cuối cùng.
- **Dữ liệu cho trước (Given)**:
  - Giá trị kỳ vọng nền của mô hình trên toàn tập huấn luyện:
    $$\mathbb{E}[f(\mathbf{x})] = -0.45 \quad (\text{tương ứng xác suất nền } P_{base} \approx 0.389)$$
  - Giá trị đóng góp biên cục bộ $\phi_i$ của 6 đặc trưng đo được từ một mẫu nước xám biên:
    - $\phi_{NH_4^+} = -1.82$ (nồng độ $NH_4^+ \text{-} N_{eff} = 5.2 \text{ mg/L}$, kéo giảm mạnh dự báo)
    - $\phi_{NO_3^-} = +0.65$ (nồng độ $NO_3^- \text{-} N_{eff} = 11.4 \text{ mg/L}$, tăng xác suất)
    - $\phi_{\text{AirFlow}} = -0.30$ (lưu lượng khí cấp $2 \text{ L/min}$, kéo giảm dự báo)
    - $\phi_{COD} = +0.12$ (nồng độ $COD_{eff} = 28 \text{ mg/L}$)
    - $\phi_{\text{TMP}} = -0.05$ (áp suất xuyên màng $8.5 \text{ kPa}$)
    - $\phi_{\text{Influent}} = +0.03$ (lưu lượng nước vào $16.2 \text{ mL/min}$)
- **Công thức áp dụng (Formula)**:
  - Tiên đề hiệu quả SHAP (Efficiency):
    $$f(\mathbf{x}) = \mathbb{E}[f(\mathbf{x})] + \sum_{i=1}^6 \phi_i$$
  - Ánh xạ sang xác suất phân loại (Hàm Sigmoid):
    $$P(y=1|\mathbf{x}) = \frac{1}{1 + e^{-f(\mathbf{x})}}$$
- **Các bước tính toán (Steps)**:
  - *Bước 1: Tính tổng giá trị đóng góp của tất cả các đặc trưng*:
    $$\sum_{i=1}^6 \phi_i = (-1.82) + (+0.65) + (-0.30) + (+0.12) + (-0.05) + (+0.03) = -1.37$$
  - *Bước 2: Tính giá trị đầu ra log-odds cuối cùng*:
    $$f(\mathbf{x}) = -0.45 + (-1.37) = -1.82$$
  - *Bước 3: Chuyển đổi log-odds sang xác suất dự báo*:
    $$P(y=1|\mathbf{x}) = \frac{1}{1 + e^{-(-1.82)}} = \frac{1}{1 + e^{1.82}} = \frac{1}{1 + 6.1719} \approx 0.1394 \quad (13.94\%)$$
  - *Bước 4: So sánh với ngưỡng quyết định và đưa ra cảnh báo*:
    - Giả định ngưỡng quyết định vận hành an toàn là $\theta = 0.50$.
    - Xác suất $P(y=1|\mathbf{x}) = 0.1394 < \theta$.
    - Mô hình gán nhãn dự báo là Âm tính (Insufficient Nitrification).
    - Hệ thống điều khiển tự động tăng cường lưu lượng khí cấp lên $6 \text{ L/min}$.
- **Kết quả tổng hợp (Result)**:
  - Giá trị log-odds $f(\mathbf{x}) = -1.82$, xác suất $P(y=1|\mathbf{x}) \approx 13.94\%$. Đặc trưng $NH_4^+ \text{-} N_{eff}$ giữ vai trò chi phối áp đảo dẫn đến quyết định phân loại thiếu oxy.

##### 3.4.2 Ước lượng mật độ hạt nhân (Kernel Density Estimation - KDE)
###### 3.4.2.1 Cơ chế xấp xỉ hàm mật độ xác suất phi tham số
- Kỹ thuật KDE xấp xỉ liên tục hàm mật độ xác suất $f(x)$ từ tập dữ liệu rời rạc $\{X_1, X_2, \dots, X_n\}$:
  $$\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - X_i}{h}\right)$$
- Đại lượng $n$ là số điểm dữ liệu quan sát.
- Thông số $h > 0$ là độ rộng băng thông làm mượt (smoothing bandwidth parameter).
- Hàm nhân đối xứng Gaussian $K(u)$ chuẩn hóa:
  $$K(u) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{1}{2} u^2\right)$$
- Đường cong KDE ước tính hàm mật độ riêng biệt cho hai nhóm:
  - Nhóm dự báo dương tính (Predicted Positive - Đường đỏ): Biểu diễn vùng mật độ của trạng thái Nitrification đầy đủ.
  - Nhóm dự báo âm tính (Predicted Negative - Đường xanh): Biểu diễn vùng mật độ của trạng thái Nitrification không đầy đủ.

###### 3.4.2.2 Giải mã ý nghĩa hình học của đường cong KDE
- Đỉnh đường cong (Peak location): Xác định vùng tập trung dữ liệu phổ biến nhất của phân lớp:
  - Ví dụ: Nồng độ $COD_{eff}$ của lớp Positive tạo đỉnh rất nhọn tại khoảng $30 \text{ mg/L}$.
- Độ rộng của đường cong (Curve width): Đo lường phương sai và độ phân tán của đặc trưng:
  - Đường hẹp phản ánh đặc trưng có độ biến thiên thấp, dữ liệu ổn định đồng nhất.
  - Đường bè rộng phản ánh đặc trưng có độ phân tán cao trong quá trình vận hành.
  - Hệ số biến thiên (Coefficient of Variance - $CV = \frac{\sigma}{\mu}$):
    - $COD_{eff}$ có $CV = 55.25\%$ (đường hẹp).
    - $NH_4^+ \text{-} N_{eff}$ có $CV = 93.82\%$ (đường rộng).
    - $NO_3^- \text{-} N_{eff}$ có $CV = 101.72\%$ (đường rất rộng).
- Mức độ chồng lấn diện tích (Curve overlap area): Đánh giá năng lực phân tách ranh giới của biến:
  - Vùng diện tích giao nhau giữa hai đường cong đỏ và xanh càng nhỏ thì năng lực phân loại của biến càng cao.
  - Đặc trưng Air Flow Rate và $NH_4^+ \text{-} N_{eff}$ thể hiện vùng chồng lấn rất nhỏ, tạo ranh giới phân tách lớp rõ rệt.
  - Đặc trưng TMP và Influent Flow Rate thể hiện mức độ chồng lấn lớn, cho thấy năng lực phân biệt đơn lẻ hạn chế.

###### 3.4.2.3 Ma trận tán xạ cặp biến phát hiện ranh giới quyết định và mẫu nhầm lẫn
- Biểu đồ tán xạ cặp biến (Pairwise scatter plot matrix) kết hợp trực quan:
  - Đường chéo chính hiển thị đường cong phân phối KDE 1 chiều của từng biến đơn lẻ.
  - Các ô ngoài đường chéo hiển thị đồ thị phân tán 2 chiều (bivariate scatter plot) giữa từng cặp đặc trưng.
  - Các điểm dữ liệu được gán nhãn theo kết quả ma trận nhầm lẫn (TP, FP, FN, TN).
- Phát hiện các điểm dữ liệu biên nguy kịch (Borderline cases):
  - Mẫu dữ liệu có $NO_3^- \text{-} N_{eff} \approx 9 \text{ mg/L}$ và $NH_4^+ \text{-} N_{eff} \approx 2 \text{ mg/L}$ nằm ngay trên ranh giới phân tách.
  - Đây chính là tọa độ phát sinh các lỗi phân loại nhầm lẫn chính (FP và FN).
  - Vùng không gian đặc trưng thưa dữ liệu (data sparsity) phản ánh sự thiếu hụt các trạng thái vận hành chuyển tiếp.
  - Kết quả KDE và Pairwise plot hướng dẫn chiến lược thu thập dữ liệu mục tiêu:
    - Bổ sung các thí nghiệm chủ động trong dải nồng độ chuyển tiếp $NO_3^- \text{-} N \in [8, 12] \text{ mg/L}$ và $NH_4^+ \text{-} N \in [1.5, 3.5] \text{ mg/L}$.
    - Khắc phục triệt để hiện tượng quá mức khớp và cải thiện độ chuẩn xác ranh giới của các thuật toán ML.
