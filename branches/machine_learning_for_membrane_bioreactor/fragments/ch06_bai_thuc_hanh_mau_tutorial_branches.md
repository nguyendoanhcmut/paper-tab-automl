## 6. Bài thực hành Mẫu và Bài tập Mô phỏng Dự đoán Áp suất Xuyên màng (Tutorial Example)

- Bài thực hành triển khai 5 thuật toán Machine Learning tiêu biểu gồm SVM, RF, BPNN, LSTM và GA-BP.
- Mục tiêu chính là mô phỏng và dự đoán động học áp suất xuyên màng ($\text{TMP}$) trong hệ thống màng phản ứng sinh học (MBR).
- Quá trình thực nghiệm được lập trình và tính toán trên nền tảng phần mềm MATLAB.
- Tập dữ liệu nghiên cứu bao gồm 2.000 mẫu quan sát chuỗi thời gian liên tục từ hệ thống MBR vận hành thực tế.
- Kết quả mô phỏng cung cấp cơ sở định lượng để so sánh độ chính xác và khả năng tổng quát hóa giữa các kiến trúc học máy.

---

### 6.1 Quy trình Phương pháp Xây dựng Mô hình (Methodology)

- Quy trình mô hình hóa bao gồm 4 giai đoạn kỹ thuật kế tiếp nhau.
- Giai đoạn 1 thu thập và làm sạch chuỗi dữ liệu vận hành.
- Giai đoạn 2 chuẩn hóa dữ liệu và phân chia tập mẫu thử nghiệm.
- Giai đoạn 3 cấu hình kiến trúc mạng và tối ưu siêu tham số.
- Giai đoạn 4 tính toán các chỉ số thống kê để đánh giá độ chính xác dự báo.

#### 6.1.1 Tiền xử lý Dữ liệu và Chuẩn hóa Min-Max

- **Quy mô tập dữ liệu thực nghiệm**:
  - Tập dữ liệu thô gồm $N = 2.000$ điểm dữ liệu chuỗi thời gian vận hành liên tục từ trạm MBR.
  - Mỗi mẫu dữ liệu ghi nhận đồng thời 8 biến đặc trưng đầu vào và 1 biến mục tiêu đầu ra.
  - Biến mục tiêu đầu ra ($y$) là áp suất xuyên màng $\text{TMP}$ ($\text{kPa}$) phản ánh trực tiếp mức độ tắc nghẽn màng.
  - Tám biến đặc trưng đầu vào ($\mathbf{x}$) phản ánh điều kiện vận hành, chất lượng nước và đặc tính sinh khối:
    1. Nhiệt độ nước thải trong bể phản ứng ($T$, $^{\circ}\text{C}$).
    2. Nồng độ chất rắn lơ lửng trong bùn hoạt tính ($\text{MLSS}$, $\text{mg/L}$).
    3. Độ $\text{pH}$ của hỗn hợp bùn lỏng trong bể sinh học.
    4. Nồng độ oxy hòa tan trong vùng hiếu khí ($\text{DO}_{\text{aerobic}}$, $\text{mg/L}$).
    5. Nhu cầu oxy hóa học của nước thải đầu vào ($\text{COD}_{\text{in}}$, $\text{mg/L}$).
    6. Tổng nitơ của nước thải đầu vào ($\text{TN}_{\text{in}}$, $\text{mg/L}$).
    7. Tổng photpho của nước thải đầu vào ($\text{TP}_{\text{in}}$, $\text{mg/L}$).
    8. Lưu lượng dòng thấm xuyên màng ($\text{Flux}$, $\text{L/(m}^2\cdot\text{h)}$).

- **Làm sạch dữ liệu và loại bỏ giá trị dị biệt**:
  - Dữ liệu thô chứa các điểm nhiễu do lỗi cảm biến đo và bọt khí bám vào đầu dò.
  - Thuật toán kiểm tra giới hạn $3\sigma$ lọc bỏ các giá trị nằm ngoài khoảng tin cậy $[\mu - 3\sigma, \mu + 3\sigma]$.
  - Quá trình làm sạch bảo đảm tính toàn vẹn của chuỗi dữ liệu trước khi đưa vào mô hình học máy.

- **Công thức chuẩn hóa Min-Max Scaling**:
  - Các biến đầu vào có thứ nguyên và khoảng giá trị chênh lệch lớn ($\text{MLSS} > 6.000\text{ mg/L}$, $\text{pH} \approx 7$).
  - Sự chênh lệch thứ nguyên làm sai lệch quá trình cập nhật trọng số trong thuật toán hạ gradient.
  - Hàm `mapminmax` trong MATLAB chuyển đổi toàn bộ miền giá trị của các vector đặc trưng về đoạn $[0, 1]$:
    $$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
  - Trong đó:
    * $x$ là giá trị thực tế của biến đầu vào hoặc biến đầu ra quan sát.
    * $x_{\min}$ là giá trị nhỏ nhất của đặc trưng tương ứng trong toàn bộ tập mẫu dữ liệu.
    * $x_{\max}$ là giá trị lớn nhất của đặc trưng tương ứng trong toàn bộ tập mẫu dữ liệu.
    * $x_{\text{norm}}$ là giá trị chuẩn hóa không thứ nguyên nằm trong đoạn giới hạn $[0, 1]$.
  - Sau khi tính toán dự báo, giá trị $\text{TMP}$ được giải chuẩn hóa về thang đo ban đầu:
    $$\hat{y} = \hat{y}_{\text{norm}} \cdot (y_{\max} - y_{\min}) + y_{\min}$$

- **Chiến lược phân chia tập dữ liệu**:
  - Phương án phân chia ngẫu nhiên trong bài thực hành sử dụng tỷ lệ 70% và 30%.
  - Tập huấn luyện (Training Set) chiếm 70% dữ liệu với $1.400$ mẫu quan sát.
  - Tập kiểm tra độc lập (Testing Set) chiếm 30% dữ liệu với $600$ mẫu quan sát.
  - Phân bố xác suất của tập kiểm tra tương thích chặt chẽ với phân bố của tập huấn luyện.
  - Phân chia độc lập ngăn ngừa hiện tượng rò rỉ thông tin (data leakage) giữa các tập dữ liệu.

#### 6.1.2 Thiết lập Cấu hình 5 Mô hình và Tối ưu Siêu tham số

- **Mô hình 1: Support Vector Machine / Support Vector Regression (SVM / SVR)**:
  - Công cụ thực thi: Thư viện LibSVM tích hợp trên môi trường MATLAB.
  - Dạng hàm nhân: Hàm nhân bán kính xuyên tâm RBF (Radial Basis Function Kernel):
    $$K(\mathbf{x}_i, \mathbf{x}_j) = \exp\left(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2\right) = \exp\left(-\frac{\|\mathbf{x}_i - \mathbf{x}_j\|^2}{2\sigma_{\text{RBF}}^2}\right)$$
  - Tham số hạt nhân $G$ (hoặc $\gamma$): $G = \frac{1}{2\sigma_{\text{RBF}}^2}$ xác định miền ảnh hưởng của từng điểm dữ liệu mẫu.
  - Hệ số phạt $C$: Cân bằng giữa độ phức tạp mô hình và mức độ chấp nhận sai số dải biên $\varepsilon$.
  - Phương pháp tối ưu: Thuật toán tìm kiếm lưới (Grid Search) kết hợp kiểm định chéo (Cross-Validation) tìm cặp $(C, \gamma)$ tối ưu.

- **Mô hình 2: Rừng ngẫu nhiên (Random Forest - RF)**:
  - Công cụ thực thi: `Random Forest Toolbox` trong phần mềm MATLAB.
  - Số lượng cây quyết định: Thiết lập $n_{\text{estimators}} = 100$ cây hồi quy thành phần (CART trees).
  - Thuật toán Ensemble Bagging:
    * Lấy mẫu hoàn lại (bootstrap) từ tập dữ liệu gốc để huấn luyện riêng cho từng cây.
    * Tại mỗi nút rẽ nhánh, thuật toán chọn ngẫu nhiên một tập con đặc trưng ($m = \lfloor\sqrt{8}\rfloor = 2$ hoặc $m = 3$).
    * Giá trị dự báo của rừng là trung bình cộng kết quả từ tất cả các cây:
      $$\hat{y}_{\text{RF}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B T_b(\mathbf{x})$$
  - Cơ chế lấy mẫu ngẫu nhiên giúp giảm phương sai mô hình và hạn chế hiện tượng quá khớp.

- **Mô hình 3: Mạng nơ-ron lan truyền ngược (Back Propagation Neural Network - BPNN)**:
  - Công cụ thực thi: `Neural Network Toolbox` trong môi trường MATLAB.
  - Kiến trúc mạng: Mạng truyền thẳng 3 tầng gồm tầng vào (8 nút), tầng ẩn ($N_h$ nút) và tầng ra (1 nút).
  - Số lượng nơ-ron tầng ẩn được chọn lọc tối ưu trong khoảng $5 \le N_h \le 12$.
  - Hàm kích hoạt: Hàm Sigmoid phi tuyến tại tầng ẩn và hàm Purelin tuyến tính tại tầng ra:
    $$f(z) = \frac{1}{1 + e^{-z}}$$
  - Thuật toán huấn luyện: Thuật toán lan truyền ngược kết hợp tối ưu Levenberg-Marquardt (`trainlm`).
  - Hàm mục tiêu tổn thất cực tiểu hóa tổng bình phương sai số:
    $$E = \frac{1}{2} \sum_{k=1}^n (y_k - \hat{y}_k)^2$$

- **Mô hình 4: Mạng bộ nhớ ngắn-dài (Long Short-Term Memory - LSTM)**:
  - Bản chất kiến trúc: Dạng mạng hồi quy đặc biệt xử lý phụ thuộc thời gian dài và chống triệt tiêu gradient.
  - Mỗi tế bào nhớ (Memory Cell) chứa 3 cổng điều khiển dòng dữ liệu:
    * Cổng quên (Forget Gate): Loại bỏ các thông tin không cần thiết từ trạng thái cũ:
      $$f_t = \sigma\left(W_f \cdot [h_{t-1}, x_t] + b_f\right)$$
    * Cổng vào (Input Gate): Cập nhật thông tin mới vào tế bào nhớ:
      $$i_t = \sigma\left(W_i \cdot [h_{t-1}, x_t] + b_i\right), \quad \tilde{C}_t = \tanh\left(W_c \cdot [h_{t-1}, x_t] + b_c\right)$$
    * Trạng thái tế bào (Cell State): Kết hợp thông tin lưu trữ cũ và mới:
      $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
    * Cổng ra (Output Gate): Quyết định giá trị đầu ra tại bước thời gian hiện tại:
      $$o_t = \sigma\left(W_o \cdot [h_{t-1}, x_t] + b_o\right), \quad h_t = o_t \odot \tanh(C_t)$$
  - Tham số huấn luyện: Kích thước cửa sổ trượt thời gian $w = 5$, tích hợp lớp Dropout để ngăn quá khớp.

- **Mô hình 5: Mạng nơ-ron lai ghép giải thuật di truyền (GA-BP)**:
  - Bản chất cơ chế: Khắc phục điểm yếu rơi vào cực tiểu cục bộ của thuật toán BPNN cổ điển.
  - Giải thuật di truyền (GA) tìm kiếm toàn cục để xác định vector trọng số và ngưỡng lệch ban đầu.
  - Quy mô quần thể: 50 cá thể nhiễm sắc thể tiến hóa qua 100 thế hệ liên tục.
  - Cấu trúc nhiễm sắc thể: Mã hóa toàn bộ trọng số kết nối ($W$) và độ lệch ($b$) thành chuỗi số thực.
  - Hàm thích nghi (Fitness Function): Tỷ lệ nghịch với sai số toàn phương trung bình của mạng:
    $$F = \frac{1}{\text{MSE}} = \frac{1}{\frac{1}{N}\sum_{k=1}^N (y_k - \hat{y}_k)^2}$$
  - Ba toán tử di truyền cốt lõi:
    1. Chọn lọc (Selection): Áp dụng phương pháp bánh xe roulette ưu tiên cá thể có độ thích nghi cao.
    2. Lai ghép (Crossover): Lai ghép số thực giữa các cặp nhiễm sắc thể với xác suất $P_c = 0.8$.
    3. Đột biến (Mutation): Đột biến gen ngẫu nhiên với xác suất $P_m = 0.05$.
  - Sau 100 thế hệ, cá thể tốt nhất cung cấp trọng số khởi tạo tối ưu cho mạng BPNN tinh chỉnh cục bộ.

#### 6.1.3 Các Chỉ số Đánh giá Thống kê

- **Hệ số xác định ($R^2$ - Coefficient of Determination)**:
  - Đo lường tỷ lệ phần trăm phương sai của áp suất $\text{TMP}$ được mô hình giải thích:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó:
    * $y_i$ là giá trị $\text{TMP}$ thực nghiệm quan sát thứ $i$.
    * $\hat{y}_i$ là giá trị $\text{TMP}$ do mô hình dự đoán.
    * $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ là giá trị trung bình của toàn bộ mẫu thực nghiệm.
    * $n$ là tổng số lượng mẫu quan sát trong tập kiểm tra hoặc tập huấn luyện.
  - Giá trị $R^2 \in [0, 1]$; giá trị tiệm cận $1.0$ thể hiện mức độ khớp mô hình hoàn hảo.

- **Sai số bình phương trung bình căn bậc hai ($\text{RMSE}$ - Root Mean Squared Error)**:
  - Đo lường độ lệch tuyệt đối trung bình giữa giá trị dự đoán và giá trị thực nghiệm:
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  - Đơn vị đo của $\text{RMSE}$ trùng với đơn vị của biến mục tiêu ($\text{kPa}$).
  - Trọng số bình phương làm tăng độ nhạy đối với các điểm sai số lớn ngoài biên.
  - Giá trị $\text{RMSE}$ càng nhỏ phản ánh mô hình khống chế sai số cục bộ càng tốt.

- **Sai số phần trăm tuyệt đối trung bình ($\text{MAPE}$ - Mean Absolute Percentage Error)**:
  - Đánh giá sai số tương đối không phụ thuộc vào thang đo thứ nguyên:
    $$\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right| \quad \text{hoặc} \quad \text{MAPE} = \frac{1}{n} \sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
  - Chỉ số thể hiện độ lệch phần trăm trung bình giữa dự báo và thực tế.
  - Giá trị $\text{MAPE} < 0.10$ ($10\%$) biểu thị độ chính xác dự báo ở mức cao trong kỹ thuật vận hành màng.

---

### 6.2 Kết quả Thực nghiệm và Phân tích So sánh Định lượng 5 Mô hình (Results & Discussion)

- Đánh giá thực nghiệm so sánh định lượng 5 mô hình trên cùng một tập dữ liệu chuẩn hóa.
- Phân tích bao gồm đặc tính dữ liệu chuỗi thời gian và hiệu năng dự đoán chi tiết.

#### 6.2.1 Phân tích Đặc tính Chuỗi Thời gian Dữ liệu Thô

- **Đặc tính phân phối thống kê của tập dữ liệu**:
  - Bảng thống kê mô tả ghi nhận các thông số đặc trưng gồm giá trị trung bình, độ lệch chuẩn, cực tiểu và cực đại:
    * Nhiệt độ $T$ biến động theo mùa trong dải $15\text{--}30^{\circ}\text{C}$, ảnh hưởng trực tiếp đến độ nhớt của nước.
    * Nồng độ sinh khối $\text{MLSS}$ duy trì trong khoảng $6.000\text{--}10.000\text{ mg/L}$.
    * Giá trị $\text{pH}$ ổn định trong ngưỡng tối ưu cho vi sinh vật từ $6.8$ đến $7.8$.
    * Nồng độ oxy hòa tan $\text{DO}$ duy trì ở mức $1.5\text{--}3.5\text{ mg/L}$ trong vùng hiếu khí.
    * Các thông số dòng vào $\text{COD}$, $\text{TN}$, $\text{TP}$ phản ánh tải trọng hữu cơ và dinh dưỡng cấp cho bùn hoạt tính.
    * Lưu lượng màng $\text{Flux}$ duy trì ở chế độ dưới tới hạn (sub-critical flux) để kéo dài tuổi thọ màng.
    * Áp suất $\text{TMP}$ biến thiên từ mức khởi điểm $5\text{ kPa}$ lên đến ngưỡng tới hạn $35\text{--}50\text{ kPa}$.

- **Hai giai đoạn động học tắc nghẽn đặc trưng**:
  - Đồ thị diễn biến $\text{TMP}$ theo thời gian thể hiện rõ hai giai đoạn vật lý kế tiếp:
  - **Giai đoạn 1: Tăng chậm ban đầu (Initial slow TMP rise stage)**:
    * Xảy ra do chất hòa tan vi sinh vật (SMP) và hạt keo hấp phụ vào mao quản màng.
    * Quá trình làm hẹp lỗ rỗng màng (pore narrowing) và tắc nghẽn cục bộ bên trong cấu trúc xốp.
    * Tốc độ gia tăng áp suất $\frac{d\text{TMP}}{dt}$ nhỏ, đường đồ thị có độ dốc thấp và kéo dài.
  - **Giai đoạn 2: Tăng vọt áp suất xuyên màng (TMP jump stage)**:
    * Bề mặt màng bị bao phủ hoàn toàn bởi lớp bánh bùn (cake layer) sinh học dày đặc.
    * Lực cản thủy lực tăng cao khiến dòng thấm dồn qua các lỗ rỗng còn lại với vận tốc rất lớn.
    * Hiện tượng nén chặt bánh bùn kích hoạt điểm nhảy vọt áp suất đột ngột ($\frac{d\text{TMP}}{dt} \gg 0$).
    * Mô hình học máy cần nhận diện chính xác điểm uốn này để cảnh báo chu kỳ rửa màng kịp thời.

#### 6.2.2 So sánh Định lượng Hiệu năng 5 Mô hình (SVM, RF, BPNN, LSTM, GA-BP)

- **Bảng tổng hợp chỉ số thực nghiệm chuẩn xác (Table 3)**:

| Chỉ số đánh giá | Phân vùng dữ liệu | SVM | Random Forest (RF) | BPNN | LSTM | GA-BP |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **$R^2$ (Hệ số xác định)** | **Tập huấn luyện (Training)** | 0.8208 | **0.9017** | 0.8199 | 0.8206 | 0.8201 |
| | **Tập kiểm tra (Testing)** | 0.8124 | 0.7344 | 0.8096 | **0.8175** | 0.8128 |
| | **Toàn bộ dữ liệu (All Data)** | 0.8184 | **0.8537** | 0.8170 | 0.8197 | 0.8180 |
| **RMSE (kPa)** | **Tập huấn luyện (Training)** | 1.4075 | **1.0424** | 1.4107 | 1.4080 | 1.4100 |
| | **Tập kiểm tra (Testing)** | 1.3955 | 1.6605 | 1.4058 | **1.3765** | 1.3940 |
| | **Toàn bộ dữ liệu (All Data)** | 1.4039 | **1.2601** | 1.4092 | 1.3987 | 1.4052 |
| **MAPE (tỷ số / %)** | **Tập huấn luyện (Training)** | 0.0616 (6.16%) | **0.0463 (4.63%)** | 0.0629 (6.29%) | 0.0630 (6.30%) | 0.0628 (6.28%) |
| | **Tập kiểm tra (Testing)** | 0.0624 (6.24%) | 0.0737 (7.37%) | 0.0636 (6.36%) | **0.0619 (6.19%)** | 0.0625 (6.25%) |
| | **Toàn bộ dữ liệu (All Data)** | 0.0618 (6.18%) | **0.0545 (5.45%)** | 0.0631 (6.31%) | 0.0626 (6.26%) | 0.0627 (6.27%) |

- **Phân tích hiệu năng trên tập huấn luyện (Training Set)**:
  - Cả 5 mô hình đều thể hiện khả năng khớp dữ liệu tốt với $R^2 > 0.81$.
  - Random Forest đạt độ khớp huấn luyện cao nhất với $R^2 = 0.9017$.
  - RF đạt sai số huấn luyện thấp nhất: $\text{RMSE} = 1.0424\text{ kPa}$ và $\text{MAPE} = 0.0463$ ($4.63\%$).
  - Bốn mô hình SVM, BPNN, LSTM và GA-BP cho kết quả huấn luyện tương đương nhau.
  - Hệ số $R^2$ huấn luyện của 4 mô hình này nằm trong khoảng hẹp từ $0.8199$ đến $0.8208$.
  - Sai số $\text{RMSE}$ huấn luyện dao động ổn định quanh mức $1.4075\text{--}1.4107\text{ kPa}$.

- **Phân tích hiệu năng trên tập kiểm tra độc lập (Testing Set)**:
  - Toàn bộ 5 mô hình chứng minh tính khả thi kỹ thuật với $R^2 > 0.73$.
  - Mô hình LSTM đạt độ chính xác dự báo cao nhất trên tập dữ liệu kiểm tra độc lập.
  - LSTM đạt $R^2 = 0.8175$, $\text{RMSE} = 1.3765\text{ kPa}$ và $\text{MAPE} = 0.0619$ ($6.19\%$).
  - Cơ chế bộ nhớ cổng của LSTM giúp mô phỏng chính xác độ trễ và thời điểm tăng vọt $\text{TMP}$.
  - Mô hình GA-BP xếp thứ hai về độ chính xác với $R^2 = 0.8128$ và $\text{RMSE} = 1.3940\text{ kPa}$.
  - Mô hình SVM duy trì độ ổn định vững chắc với $R^2 = 0.8124$ và $\text{RMSE} = 1.3955\text{ kPa}$.

- **Cơ chế suy giảm khả năng tổng quát hóa của Random Forest**:
  - Mô hình RF thể hiện sự sụt giảm hiệu năng rõ rệt từ tập huấn luyện sang tập kiểm tra.
  - Hệ số $R^2$ của RF giảm mạnh từ $0.9017$ xuống $0.7344$ (giảm $18.55\%$).
  - Sai số $\text{RMSE}$ tăng vọt từ $1.0424\text{ kPa}$ lên $1.6605\text{ kPa}$ (tăng $59.29\%$).
  - Chỉ số $\text{MAPE}$ tăng từ $4.63\%$ lên $7.37\%$.
  - Về mặt lý thuyết toán học cơ bản, thuật toán RF không bị quá khớp do quy luật số lớn.
  - Tuy nhiên, hiện tượng cộng tuyến đa biến giữa các đặc trưng làm suy giảm khả năng dự đoán.
  - Các biến $\text{COD}$, $\text{MLSS}$, $\text{DO}$ và nhiệt độ trong trạm MBR có mức tương quan dư thừa cao.
  - Việc lấy mẫu đặc trưng ngẫu nhiên tại các nút rẽ nhánh đưa các biến nhiễu vào cây quyết định.
  - Giải pháp cải thiện hiệu năng RF bao gồm:
    * Tăng số lượng cây quyết định lên trên 200 cây.
    * Áp dụng kỹ thuật lọc chọn đặc trưng (Feature Selection) loại bỏ biến dư thừa.
    * Tối ưu hóa thuật toán cắt tỉa cành cây (Pruning Algorithm).

- **Cơ chế ưu việt của mô hình lai GA-BP so với BPNN truyền thống**:
  - Mạng BPNN tiêu chuẩn dùng thuật toán hạ gradient dễ mắc kẹt tại điểm cực tiểu cục bộ.
  - Hiệu quả huấn luyện BPNN phụ thuộc lớn vào việc gán ngẫu nhiên trọng số ban đầu.
  - Giải thuật di truyền GA tìm kiếm đa hướng trên toàn bộ không gian trọng số và ngưỡng lệch.
  - Quá trình chọn lọc, lai ghép và đột biến đưa bộ thông số về vùng trũng tối ưu toàn cục.
  - GA-BP cải thiện chỉ số $R^2$ kiểm tra từ $0.8096$ (BPNN) lên $0.8128$.
  - GA-BP giảm $\text{RMSE}$ kiểm tra từ $1.4058\text{ kPa}$ xuống $1.3940\text{ kPa}$.
  - GA-BP giảm $\text{MAPE}$ kiểm tra từ $0.0636$ xuống $0.0625$, tương đương mức cải thiện sai số từ 8% đến 12%.
  - Khởi tạo trọng số bằng GA tăng tốc độ hội tụ và ngăn ngừa hiện tượng bão hòa tín hiệu đạo hàm.
