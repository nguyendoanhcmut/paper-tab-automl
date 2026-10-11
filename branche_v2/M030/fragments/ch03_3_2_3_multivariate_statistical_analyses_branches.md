### 2.3. Multivariate statistical analyses

- Phương pháp luận nghiên cứu và quy trình xử lý dữ liệu được thiết lập theo sơ đồ phân tích đa biến tích hợp (Hình 2):
  - **Hình 2.** Sơ đồ phương pháp nghiên cứu và xử lý dữ liệu
    - <img src="assets/fig_02_p6.jpeg" alt="Hình 2" />
    - **Hình này chứng minh điều gì**
      - Tiền xử lý loại bỏ dữ liệu thiếu thu gọn tập dữ liệu thô từ $n = 1{,}131$ xuống $n = 479$ mẫu.
      - Ba nhánh phân tích vận hành song song gồm PCA ($n = 479$), ANN ($287/144/48$) và MSPC ($n = 422$, chia $272/150$).
    - **Từ đâu mà thấy được**
      - Luồng dọc từ trên xuống: mũi tên từ "Raw data" qua "Variables selection" đến "Elimination of samples with missing data".
      - Nhánh rẽ ngang phía dưới: ba cột song song gồm "PCA model" (trái), "ANN model" (giữa) và "MSPC control charts" (phải).
- Nền tảng phần mềm và công cụ triển khai mô hình hóa:
  - Tất cả các mô hình phân tích đa biến được phát triển bằng phần mềm R phiên bản 4.0.2.
  - Gói thư viện `readxl` được sử dụng để nhập dữ liệu từ Microsoft Excel® 2016.

#### 2.3.1. ANN model development

- Tiền xử lý và chuẩn hóa dữ liệu:
  - Tập dữ liệu cuối cùng được chuẩn hóa về điểm số $Z$ ($Z$ score) với giá trị trung bình bằng $0$ ($\mu = 0$) và độ lệch chuẩn bằng $1$ ($\sigma = 1$) theo Phương trình (1):
    $$Z_i = \frac{x_i - \mu}{\sigma} \quad (1)$$
    trong đó:
    - $Z_i$ là điểm số đã chuẩn hóa (standardized score).
    - $x_i$ là giá trị của một biến số cụ thể (specific variable).
    - $\mu$ là giá trị trung bình của tập biến số (mean of the set of variables).
    - $\sigma$ là độ lệch chuẩn của tập biến số (standard deviation of the set of variables).
  - Phép chuẩn hóa $Z$ score thu hẹp khoảng cách bậc độ lớn (orders of magnitude) giữa các biến số khác nhau, đưa chúng về thang đo có thể so sánh trực tiếp và đảm bảo tầm quan trọng ngang nhau trong các mô hình đa biến.
- Cấu trúc biến số và công cụ xây dựng mô hình ANN:
  - Mô hình Mạng nơ-ron nhân tạo (ANN - Artificial Neural Network) được xây dựng trong R sử dụng các gói thư viện `NeuralNet` và `Keras`.
  - Bộ biến đầu vào (input variables) bao gồm $13$ thông số vận hành và chất lượng nước:
    - Độ lọc của bùn (sludge filterability).
    - Nồng độ chất rắn lơ lửng bay hơi trong bùn lỏng ($MLVSS$ - mixed liquor volatile suspended solids).
    - $pH$.
    - Nồng độ amoniac dòng vào (influent concentration of ammonia).
    - Nồng độ dầu mỡ dòng vào ($OG$ - oil and grease).
    - Nồng độ sulfua dòng vào (influent concentration of sulphides).
    - Nồng độ photpho dòng vào (influent concentration of phosphorous).
    - $COD$ dòng vào (influent COD).
    - $COD$ dòng ra (effluent COD).
    - Hiệu quả khử $COD$ (COD removal).
    - Nhiệt độ (temperature).
    - Thời gian lưu bùn ($SRT$ - sludge retention time).
    - Độ thấm của màng (membrane permeability).
  - Biến đầu ra (output variable): Hiệu quả khử amoniac (ammonia removal) được lựa chọn làm biến mục tiêu nhằm dự đoán chuẩn xác giá trị và đánh giá động thái vận hành của hệ thống MBR.
- Kiến trúc mạng và tối ưu hóa siêu tham số:
  - Áp dụng kiến trúc mạng truyền thẳng nhiều lớp (multilayer feedforward architecture).
  - Tiến hành hàng loạt thử nghiệm kết hợp giữa các hàm kích hoạt (activation function), số lượng lớp ẩn (hidden layers), số lượng nơ-ron trong từng lớp và số chu kỳ huấn luyện (epochs) nhằm xác định cấu hình có sai số toàn phương trung bình ($MSE$ - mean square error) nhỏ nhất.
  - Cấu hình mạng nơ-ron tối ưu được xác định cho mô hình hóa MBR:
    - Hàm kích hoạt: Hàm chỉnh lưu kết hợp dropout (rectifier with dropout).
    - Số lớp ẩn: $2$ lớp ẩn, trong đó lớp thứ nhất chứa $12$ nơ-ron và lớp thứ hai chứa $7$ nơ-ron (cấu hình $12$ và $7$ neurons theo thứ tự).
    - Số chu kỳ huấn luyện: $5000$ epochs.
- Phân chia tập dữ liệu và tính đại diện của mẫu huấn luyện:
  - Mô hình phục vụ hai mục đích chính: phân tích độ nhạy (sensitivity analysis) của hiệu quả khử amoniac đối với các biến đầu vào, và dự báo (forecasting) hiệu quả khử amoniac từ các điều kiện đầu vào cho trước.
  - Toàn bộ dữ liệu được phân chia ngẫu nhiên thành $3$ tập con:
    - Tập huấn luyện (training set): $60\,\%$ tổng số dữ liệu.
    - Tập kiểm định (validation set): $30\,\%$ tổng số dữ liệu.
    - Tập kiểm tra (test set): $10\,\%$ tổng số dữ liệu.
  - Đảm bảo tính đại diện của dữ liệu theo khuyến nghị của Zhong et al. đối với ứng dụng học máy trong Khoa học và Kỹ thuật Môi trường ($ESE$ - Environmental Science and Engineering): dữ liệu mang tính "đại diện" quan trọng hơn việc chỉ có dữ liệu "lớn" để tạo nên các mô hình mạnh mẽ và ổn định.
  - Quy trình phân chia tập dữ liệu được kiểm tra và lặp lại liên tục cho đến khi tập huấn luyện bao phủ dải rộng các tỷ lệ phần trăm khử amoniac, giúp mô hình học tập đầy đủ các điều kiện vận hành đa dạng.
  - Cơ chế sử dụng các tập dữ liệu:
    - Các tập con huấn luyện và kiểm định được kết hợp để huấn luyện và hiệu chuẩn mạng phục vụ phân tích độ nhạy.
    - Tập con kiểm tra độc lập được sử dụng làm cấu hình đầu vào để đánh giá khả năng dự đoán hiệu quả khử amoniac.
- Thông số thống kê đánh giá hiệu năng mô hình:
  - Hiệu năng của mô hình ANN được định lượng thông qua ba chỉ số: hệ số xác định ($R^2$ - coefficient of determination), sai số tuyệt đối trung bình ($MAE$ - mean absolute error), và sai số toàn phương trung bình ($MSE$ - mean square error).

#### 2.3.2. PCA model development

- Mục tiêu phân tích thành phần chính (PCA - Principal Component Analysis):
  - Khám phá sâu hơn các mối quan hệ tương quan giữa các biến số với hiệu quả khử amoniac đạt được.
  - Phân tích và làm rõ bản chất chiều hướng tương quan (mang dấu dương hay dấu âm) mà mô hình ANN đã nhận diện.
- Nguyên lý toán học của phép biến đổi trực giao:
  - PCA thực hiện giảm chiều dữ liệu (dimensionality reduction) bằng phép biến đổi trực giao (orthogonal transformation), chuyển nhóm vectơ gốc thành nhóm vectơ mới là tổ hợp tuyến tính của các vectơ ban đầu.
  - Phương trình triển khai toán học được xác định theo Phương trình (2):
    $$P_i = Z_i \cdot \mathrm{cov} \quad (2)$$
    trong đó:
    - $Z_i$ là ma trận số đã chuẩn hóa trước khi thực hiện PCA (standardized numerical matrix before PCA).
    - $\mathrm{cov}$ là ma trận hiệp phương sai của ma trận $Z_i$.
    - $P_i$ là ma trận số sau khi biến đổi PCA (numerical matrix after PCA).
- Công cụ tính toán và trực quan hóa:
  - Phân tích PCA được tính toán bằng hàm `PCA` trong gói thư viện `FactoMineR`.
  - Toàn bộ dữ liệu trước đó được chuẩn hóa về điểm số $Z$ theo Phương trình (1).
  - Các biểu đồ tải (loading plots) được xây dựng và trực quan hóa bằng các gói `factoextra`, `ggplot2` và `ggpubr`.
- Tiêu chí lựa chọn thành phần chính và đánh giá mô hình:
  - Số lượng thành phần chính giữ lại được xác định dựa trên tiêu chí Kaiser (Kaiser criterion) và kiểm định sườn dốc (scree test).
  - Chất lượng mô hình PCA được đánh giá thông qua giá trị hệ số xác định ($R^2$).

#### 2.3.3. MSPC model development

- Khung phương pháp kiểm soát quá trình thống kê đa biến (MSPC - Multivariate Statistical Process Control):
  - Các biểu đồ kiểm soát đa biến được xây dựng dựa trên phương pháp tiếp cận biến tiềm ẩn (latent-variable based approach) cho MSPC, sử dụng PCA làm phương pháp chiếu thống kê (MSPC-PCA) theo khuôn khổ của Ferrer và Taghezouit et al.
  - Số lượng thành phần giữ lại trong mô hình PCA của MSPC tiếp tục được lựa chọn dựa trên tiêu chí Kaiser và kiểm định sườn dốc scree test.
- Tiêu chí ngoài kiểm soát và phân tách dữ liệu thành hai giai đoạn:
  - Tiêu chí ngoài kiểm soát (out-of-control criteria) được định nghĩa là hiệu quả khử amoniac dưới $90\,\%$.
  - Tập dữ liệu được phân chia thành hai giai đoạn:
    - Giai đoạn I (Phase I): Chỉ bao gồm các mẫu nằm trong vùng kiểm soát (in-control, hiệu quả khử amoniac $> 90\,\%$) từ $3$ năm quan trắc đầu tiên ($n = 272$).
    - Giai đoạn II (Phase II): Bao gồm toàn bộ các mẫu từ năm quan trắc cuối cùng, chứa cả các mẫu trong vùng kiểm soát và ngoài vùng kiểm soát ($n = 150$).
- Thiết lập mô hình, thống kê bổ trợ và giới hạn kiểm soát trên (UCL):
  - Tập dữ liệu Phase I được chuẩn hóa về điểm số $Z$ (Phương trình 1) và sử dụng để phát triển mô hình PCA nền tảng.
  - Từ mô hình PCA Phase I, hai thống kê bổ trợ $T^2$ (Hotelling's $T^2$) và $Q$ (thống kê lỗi bình phương hay khoảng cách dự đoán vuông góc) được tính toán cho từng quan sát.
  - Các biểu đồ kiểm soát đa biến tương ứng được thiết lập với giới hạn kiểm soát trên ($UCL$ - upper control limits) được quy ước là phân vị thứ $95\,\%$ ($95\,\%$ percentiles) của từng đại lượng thống kê.
- Chiếu dữ liệu Phase II và phát hiện bất thường:
  - Tập dữ liệu Phase II được chuẩn hóa về điểm số $Z$ (Phương trình 1) và chiếu lên mô hình PCA đã huấn luyện ở Phase I để tính toán các giá trị thống kê $T^2$ và $Q$.
  - Các giá trị thống kê được vẽ trên biểu đồ kiểm soát để đối chiếu trực tiếp với các ngưỡng $UCL$.
- Chẩn đoán nguyên nhân biến động bằng biểu đồ đóng góp (contribution plots):
  - Đối với các quan sát được phát hiện vượt quá ngưỡng $UCL$ trên biểu đồ kiểm soát thống kê $Q$, phương pháp chẩn đoán dựa trên biểu đồ đóng góp được áp dụng.
  - Mức độ đóng góp của từng biến số $j$ cho từng quan sát bất thường $i$ ($\mathrm{cont}_{j,i}$) được định lượng theo Phương trình (3):
    $$\mathrm{cont}_{j,i} = \frac{e_{i,j}^2}{\sum_{j=1}^{J} e_{i,j}^2} \quad (3)$$
    trong đó:
    - $e_{i,j}$ là sai số phần dư (residual) của biến số $j$ tại quan sát bất thường $i$.
    - $J$ là tổng số lượng các biến số tham gia mô hình.
- Thư viện phần mềm hỗ trợ tính toán:
  - Các bước tính toán phương pháp luận MSPC được triển khai với sự hỗ trợ của các gói R gồm `scales`, `rstatix`, `ggplot2` và `ggpubr`.
