## 2. Methodology

### 2.1. Description of the selected wastewater treatment plant
- Hiệu suất loại bỏ chất dinh dưỡng (đối với $\text{NH}_4$, $\text{TN}$ và $\text{TP}$) của hệ thống $A_2O\text{-MBR}$ được theo dõi trong vòng một năm vận hành tại một trạm xử lý nước thải (WWTP) ở Okcheon, Hàn Quốc (Republic of Korea).
- Sơ đồ khối quy trình xử lý tại trạm Okcheon bao gồm một bể lắng sơ cấp (primary sedimentation tank); các bể phản ứng màng kỵ khí (anaerobic), thiếu khí (anoxic) và hiếu khí (oxic membrane bioreactor - MBR); cùng một bể lắng trong (clarifier) (Hình 1).
    - **Hình 1.** Sơ đồ khối quy trình xử lý nước thải Okcheon
      - <img src="assets/fig_01_p2_vector.png" alt="Hình 1" />
      - **Hình này chứng minh điều gì**
        - Dây chuyền xử lý bố trí nối tiếp từ lắng sơ cấp qua Anaerobic, Anoxic, MBR đến Clarifier để tách dòng nước và bùn.
      - **Từ đâu mà thấy được**
        - Hướng đọc từ trái sang phải: Influent lần lượt đi qua 5 khối chức năng theo chiều mũi tên.
        - Tại khối Clarifier, dòng ra tách thành mũi tên xanh phía trên (Effluent) và mũi tên đen phía dưới (Sludge disposal).
  - Bể lắng sơ cấp tiếp nhận nước thải đầu vào (influent) nhằm tăng cường quá trình axit hóa (acidification) và thủy phân (hydrolysis) các chất dạng hạt (particulate matter), từ đó duy trì lưu lượng dòng vào ổn định đến bể kỵ khí.
  - Các thiết bị khuấy trộn (mixers) được bố trí trong bể kỵ khí và bể thiếu khí để nâng cao hiệu quả xử lý và thích ứng với các điều kiện vi sinh thông qua động học phản ứng (reaction kinetics).
- Các thông số kỹ thuật và cấu tạo của hệ thống màng MBR:
  - Tổng diện tích bề mặt màng của MBR đạt $64,000\text{ m}^2$.
  - Kích thước lỗ màng danh định (nominal pore size) là $0.4\ \mu\text{m}$.
  - Vật liệu chế tạo màng là polyvinylidene fluoride (PVDF).
  - MBR được cấu thành từ nhiều module màng sợi rỗng (hollow-fiber membrane modules) đặt trong bể phản ứng kèm hệ thống đĩa phân phối khí (air diffusers) để duy trì nồng độ oxy hòa tan ($\text{DO}$).
  - Một bơm hút (suction pump) được vận hành liên tục cho quá trình lọc màng MBR.
- Quy trình vệ sinh và giới hạn vận hành màng:
  - Khi áp suất qua màng (transmembrane pressure - TMP) tăng vượt quá $40\text{ kPa}$, module màng được nhấc ra khỏi bể phản ứng và rửa sạch bằng nước cùng dung dịch natri hypoclorit $0.5\%$ ($0.5\%\text{ sodium hypochlorite}$).
  - Nồng độ chất rắn lơ lửng trong hỗn hợp bùn lỏng ($\text{MLSS}$) trong bể hiếu khí oxic-MBR luôn được duy trì trong giới hạn tiêu chuẩn.
- Các thông số vận hành và đặc tính nước thải được quan trắc tại trạm gồm: $\text{DO}$, thế oxy hóa khử ($\text{ORP}$), $\text{MLSS}$, tổng carbon hữu cơ ($\text{TOC}$), tổng phospho ($\text{TP}$), tổng nitơ ($\text{TN}$), nhu cầu oxy hóa học ($\text{COD}$), amoni ($\text{NH}_4$), và chất rắn lơ lửng ($\text{SS}$).
  - Các điều kiện vận hành có thể kiểm soát và đặc tính nước vào cung cấp thông tin thiết yếu về các thông số chất có thể oxy hóa (oxidizable matter parameters), giữ vai trò then chốt trong xử lý nước thải [33].
  - Các chất dinh dưỡng gốc nitơ và phospho là các chất gây ô nhiễm đáng lo ngại do tác động tiêu cực đến môi trường thủy sinh [34].
  - Tất cả các thông số quan trắc đều được đưa vào phát triển mô hình học máy (machine learning - ML) nhằm xác lập mối quan hệ giữa các biến đầu vào và hiệu quả loại bỏ dinh dưỡng mục tiêu trong hệ thống $A_2O\text{-MBR}$.

### 2.2. Analytical methods
- Phương pháp đo đạc trực tuyến (online monitoring):
  - Nhiệt độ (temperature), $\text{ORP}$, $\text{DO}$ và $\text{pH}$ được đo và ghi nhận liên tục bằng các cảm biến trực tuyến (installed online sensors).
  - Nồng độ $\text{TOC}$ và $\text{TN}$ được phân tích trực tuyến bằng máy phân tích Shimadzu TOC-L (Shimadzu TOC-L online analyzer).
- Phương pháp phân tích trong phòng thí nghiệm: Các thông số $\text{MLSS}$, $\text{COD}$, $\text{NH}_4$, $\text{SS}$ và $\text{TP}$ được kiểm nghiệm theo các phương pháp tiêu chuẩn phân tích nước và nước thải [35].
- Tần suất quan trắc: Toàn bộ các thông số được giám sát và ghi nhận theo từng giờ (every hour) trong suốt chu kỳ nghiên cứu kéo dài một năm.

### 2.3. Prediction models
- Các thông số đầu vào của bộ dữ liệu và ký hiệu viết tắt tương ứng được phân loại thành nhóm điều kiện vận hành (operating conditions) và nhóm đặc tính nước vào (influent characteristics) (Hình 2).
    - **Hình 2.** Các thông số đầu vào và ký hiệu viết tắt
      - <img src="assets/fig_02_p3_vector.png" alt="Hình 2" />
      - **Hình này chứng minh điều gì**
        - Cấu trúc rẽ nhánh chuẩn hóa tên gọi đầy đủ tương ứng từng ký hiệu viết tắt cho nhóm điều kiện vận hành và đặc tính nước vào.
      - **Từ đâu mà thấy được**
        - Hướng đọc từ trái sang phải: khối "Operating conditions" bên trái nối mũi tên sang DO, ORP và MLSS.
        - Khối "Influent characteristics" ở giữa nối mũi tên sang TOC, TN, TP, COD, $\text{NH}_4$ và SS.
- Hai mô hình máy học dự đoán gồm XGBoost và MLP được phát triển theo các kịch bản đầu vào và đầu ra khác nhau để dự đoán hiệu suất loại bỏ dinh dưỡng của WWTP (Hình 3).
    - **Hình 3.** Khung kiến trúc các kịch bản đầu vào và đầu ra
      - <img src="assets/fig_03_p3_vector.png" alt="Hình 3" />
      - **Hình này chứng minh điều gì**
        - Thiết kế đơn đầu ra độc lập: mỗi mô hình ($M_1$–$M_9$) dự đoán riêng một chỉ tiêu $\text{NH}_4$, $\text{TN}$ hoặc $\text{TP}$.
        - Chi tiết hóa các biến đầu vào: $M_1$–$M_3$ nhận 3 biến, $M_4$–$M_6$ nhận 6 biến, $M_7$–$M_9$ nhận 8 biến.
      - **Từ đâu mà thấy được**
        - Đọc từ trái sang phải: khối Dataset dẫn vào cột Models input, qua mũi tên lớn chỉ sang cột Models.
        - Các hàng $M_1, M_4, M_7$ xuất ra $\text{NH}_4$; $M_2, M_5, M_8$ xuất ra $\text{TN}$; $M_3, M_6, M_9$ xuất ra $\text{TP}$.

#### 2.3.1. XGBoost model
- Giới thiệu và ưu điểm của mô hình XGBoost:
  - XGBoost là một cải tiến tiềm năng từ phương pháp tăng cường độ dốc (gradient boosting) sang cấu trúc tăng cường cây quy mô lớn đầu-cuối (scalable end-to-end tree-boosting structure), được ứng dụng rộng rãi trong khoa học kỹ thuật [36].
  - XGBoost thường được ưu tiên sử dụng nhờ khả năng tinh chỉnh siêu tham số mô hình dễ dàng [37].
  - Trái ngược với các phương pháp truyền thống phải dựa vào khuyến nghị tài liệu, kinh nghiệm chuyên gia và thử-sai (trial-and-error) để giảm thiểu sai số [38], XGBoost tối ưu hóa bằng phương pháp tìm kiếm lưới (grid search) thông qua các tham số tăng cường (booster parameters) gồm `max_depth`, số vòng lặp boosting (`boosting iterations`), `eta` và `gamma`.
- Vai trò của các siêu tham số trong XGBoost:
  - `max_depth` quản lý độ sâu của cây quyết định nhằm hạn chế nguy cơ quá khớp (overfitting) và nâng cấp hàm mất mát trong giới hạn xác định.
  - Tăng cường số lần lặp (boosting iterations) hỗ trợ ngăn ngừa hiện tượng quá khớp mô hình.
  - `eta` (tốc độ học - learning rate) điều chỉnh trọng số đặc trưng (feature weights) để đạt tới các giá trị tối ưu.
  - `gamma` kiểm soát mức độ điều chuẩn (regularization) để giảm thiểu quá khớp, đồng thời quản lý các biến thiên về trọng số và độ lệch (bias) qua từng lần lặp [39].
- Cấu trúc hàm mất mát mục tiêu điều chuẩn trong XGBoost:
  - Mô hình XGBoost đề xuất các cải tiến đối với phương pháp cây quyết định truyền thống áp dụng cho các bài toán hồi quy.
  - Hàm mục tiêu mất mát điều chuẩn $f(L)$ ở lần lặp thứ $L$ được tính toán theo Phương trình (1):
    $$f(L) = \sum_{i=1}^{n} l\left(y_i, y_p^L\right) + \sum_{j=1}^{L} \phi\left(f_j\right) \quad (1)$$
    - Trong đó: $n$ là số lượng mẫu quan sát; $y_p^L$ là giá trị dự đoán của mẫu thứ $i$ tại lần lặp $L$; $l$ đại diện cho hàm mất mát (loss function); $\phi$ thể hiện thành phần điều chuẩn (regularization event).
  - Thành phần điều chuẩn $\phi(f)$ được tính toán theo Phương trình (2):
    $$\phi(f) = \gamma N + \frac{1}{2}\sigma \sum_{j=1}^{N} \omega_j^2 \quad (2)$$
    - Trong đó: $N$ là số lượng nút lá (leaf nodes); $\sigma$ và $\omega$ là các hằng số dùng để kiểm soát điều chuẩn.
- Tối ưu hóa số lượng cây: Số lượng cây trong mô hình hồi quy được tối ưu hóa nhằm tạo ra các kết quả dự đoán chính xác cho một số lần lặp xác định [39].
- Đánh giá hiệu suất thống kê của các mô hình hồi quy XGBoost trên tập kiểm tra:
  - Hiệu suất thống kê của 9 kịch bản mô hình XGBoost ($M_1$–$M_9$) được đánh giá trên tập kiểm tra qua các chỉ số sai số MAE, RMSE, MAPE, $R^2$ và $md$ (Bảng 2).
    - **Bảng 2.** Đánh giá hiệu suất 9 mô hình XGBoost trên tập kiểm tra
      - <img src="assets/table_02_p4.png" alt="Bảng 2" />
      - **Bảng này chứng minh điều gì**
        - Ba mô hình $M_1, M_4, M_7$ có độ chính xác vượt trội ($R^2 \ge 0.764$, $md \ge 0.926$), trong khi các mô hình còn lại đều có hiệu suất dự báo thấp ($R^2 \le 0.596$).
      - **Từ đâu mà thấy được**
        - Cột "$R^2$" và "md": hàng $M_7$ đạt cao nhất ($0.877$ và $0.998$), kế tiếp là $M_4$ ($0.814$ và $0.971$) và $M_1$ ($0.764$ và $0.926$); hàng $M_3$ có $R^2$ thấp nhất ($0.354$).
        - Cột sai số (MAE, RMSE, MAPE): hàng $M_4$ có MAE ($0.00024$) và RMSE ($0.00004$) nhỏ nhất, hàng $M_7$ có MAPE nhỏ nhất ($0.02333$); hàng $M_8$ có sai số lớn nhất ($\text{RMSE} = 0.06678$, $\text{MAPE} = 4.51399$).
  - Tương quan giữa giá trị thực tế và giá trị dự đoán của mô hình XGBoost qua các kịch bản khác nhau được thể hiện thông qua các đồ thị phân tán (scatter plots) (Hình 4).
    - **Hình 4.** Đồ thị phân tán giữa giá trị thực tế và dự đoán
      - <img src="assets/fig_04_p4.jpeg" alt="Hình 4" />
      - **Hình này chứng minh điều gì**
        - Cột mô hình NH4 (M1, M4, M7) có các điểm bám sát đường hồi quy đỏ vượt trội so với TN và TP ở cả ba kịch bản.
      - **Từ đâu mà thấy được**
        - Ox: giá trị thực tế (Actual), dải đo $0$–$100$. Oy: giá trị dự đoán (Predicted), dải đo $0$–$100$.
        - Cột trái (M1, M4, M7 của NH4): dữ liệu tập trung sát đường hồi quy đỏ; hai cột còn lại (TN: M2, M5, M8; TP: M3, M6, M9) phân tán rộng ra xa.

#### 2.3.2. Multiple layer perceptron (MLP) model
- Cấu trúc mạng perceptron nhiều lớp:
  - Mạng nơ-ron truyền thẳng lan truyền ngược (feed-forward back-propagation neural network) bao gồm nhiều hơn một perceptron và cấu thành từ một tầng đầu vào (input layer), một tầng đầu ra (output layer) cùng một hoặc nhiều tầng ẩn (hidden layers) [40].
- Ba bước trong quy trình huấn luyện mô hình MLP:
  - Quá trình huấn luyện là bước thiết yếu trong phát triển mô hình để xác định mối quan hệ giữa biến đầu vào và biến đầu ra.
  - Quy trình huấn luyện gồm 3 bước:
    1. Lan truyền thẳng (feed-forward): Dữ liệu đầu vào được nhân với các trọng số được lựa chọn ngẫu nhiên và truyền tới các tầng ẩn; dự đoán đầu ra được tính toán với độ lệch (bias) được cộng thêm ở từng tầng.
    2. Tính toán sai số (error computation): Tính toán mức độ sai lệch giữa kết quả mô hình dự đoán và kết quả thực tế.
    3. Lan truyền ngược sai số (back-propagation of error): Tinh chỉnh các trọng số/siêu tham số (HPs) và độ lệch (biases) nhằm giảm thiểu sai số tính toán giữa giá trị thực tế và giá trị dự đoán [41].
- Hàm tính toán nơ-ron trong mô hình MLP:
  - Chi tiết các bước tính toán được biểu diễn thông qua hàm nơ-ron ở Phương trình (3):
    $$y = f\left(\sum_{i=1}^{n} W_i x_i + b\right) \quad (3)$$
    - Trong đó: $x_i$ biểu thị các biến đầu vào; $y$ đại diện cho biến đầu ra; $f$ là hàm kích hoạt (activation function); $W_i$ là trọng số của nơ-ron thứ $i$; và $b$ biểu thị độ lệch (bias).
  - Sai số giữa giá trị dự đoán và kết quả thực tế có thể được giảm thiểu thông qua việc biến thiên các trọng số và độ lệch qua quá trình lặp.
- Mục đích phát triển mô hình MLP: Trong nghiên cứu này, các mô hình MLP được phát triển để đối chứng và thẩm định các mô hình XGBoost đề xuất phục vụ nghiên cứu so sánh; thông tin chi tiết về mô hình MLP có thể tham khảo từ các nghiên cứu trước [39,42].

### 2.4. Data analysis and preparation
- Vai trò của phân tích dữ liệu: Trong mô hình học máy, phân tích dữ liệu là bước bắt buộc để hiểu rõ các xu hướng bên trong bộ dữ liệu.
- Thu thập dữ liệu và phân tách bài toán đánh giá:
  - Dữ liệu đầu vào (các thông số vận hành) và đặc tính nước thải đầu vào ($\text{TOC}$, $\text{TN}$, $\text{TP}$, $\text{COD}$, $\text{NH}_4\text{-N}$, $\text{SS}$, $\text{DO}$, $\text{ORP}$, và $\text{MLSS}$) được thu thập thông qua nghiên cứu thực nghiệm.
  - Nhằm đánh giá hiệu quả của hệ thống $A_2O\text{-MBR}$ tại trạm xử lý nước thải, hiệu quả loại bỏ từng chất dinh dưỡng ($\text{NH}_4$, $\text{TN}$, và $\text{TP}$) được khảo sát riêng rẽ.
- Quy mô bộ dữ liệu: Tổng số lượng quan sát là $7897$ mẫu và tổng số biến số khảo sát là $9$ biến.
- Xu hướng phân bố dữ liệu theo từng chất dinh dưỡng:
  - Hiệu quả loại bỏ $\text{NH}_4$ cho thấy ít điểm ngoại lai (outliers) nhất và giảm độ nhiễu; do đó xu hướng biến thiên mượt mà hơn so với $\text{TN}$ và $\text{TP}$.
  - Điều này đồng nghĩa quá trình học kỳ vọng của các mô hình ML sẽ đạt độ chính xác cao hơn nhờ độ phân tán nhỏ so với giá trị trung bình trong bộ dữ liệu.
- Phân tích thống kê mô tả và độ lệch của bộ dữ liệu:
  - Phân tích thống kê bộ dữ liệu thực nghiệm thể hiện độ lệch âm và dương nhẹ ở các biến đầu vào, trong khi các biến đầu ra có độ lệch âm lớn (Bảng 1).
    - **Bảng 1.** Phân tích thống kê mô tả của bộ dữ liệu
      - <img src="assets/table_01_p4.png" alt="Bảng 1" />
      - **Bảng này chứng minh điều gì**
        - 9 thông số đầu vào biến thiên trên dải rộng (như $\text{MLSS}$ từ $2208.333$ đến $17,966.67$), còn 3 thông số đầu ra duy trì giá trị trung bình cao ($\text{NH}_4$ đạt $97.608$, $\text{TP}$ đạt $86.094$).
      - **Từ đâu mà thấy được**
        - Cột "Minimum" và "Maximum": hàng $\text{MLSS}$ ($2208.333$–$17,966.67$) và $\text{COD}$ ($20.307$–$311.62$) có khoảng giá trị rộng nhất ở nhóm Inputs.
        - Cột "Mean": nhóm Outputs ghi nhận giá trị trung bình cao nhất ở $\text{NH}_4$ ($97.608$), tiếp theo là $\text{TP}$ ($86.094$) và $\text{TN}$ ($67.484$).
        - Lưu ý: hình ghi Median, văn bản ghi standard deviation.
  - Phân bố độ lệch (skewness) của các thông số đầu vào:
    - Các thông số đầu vào có độ lệch âm nhẹ gồm $\text{TN}$ ($-0.198$) và $\text{NH}_4$ ($-0.697$).
    - Các thông số đầu vào có độ lệch dương nhẹ gồm $\text{TOC}$ ($0.681$), $\text{TP}$ ($0.615$), $\text{COD}$ ($0.312$), $\text{ORP}$ ($0.968$), và $\text{MLSS}$ ($0.702$).
    - Các thông số đầu vào có độ lệch dương cao hơn gồm $\text{SS}$ ($1.140$) và $\text{DO}$ ($1.009$).
  - Phân bố độ lệch của các thông số đầu ra: Cả ba thông số đầu ra đều có độ lệch âm rất lớn, cụ thể $\text{NH}_4$ ($-7.843$), tiếp theo là $\text{TP}$ ($-1.949$) và $\text{TN}$ ($-1.119$).
