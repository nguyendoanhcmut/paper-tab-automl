## 2. Vật liệu và phương pháp nghiên cứu (Materials and methods)

### 2.1 Thu thập dữ liệu từ các trạm nguồn và trạm đích (Data collection)

#### 2.1.1 Trạm đích: Cấu hình hệ thống và tập dữ liệu hạn chế (Target Plant)
- Quy mô và địa điểm: Trạm xử lý nước thải sinh hoạt quy mô pilot đặt tại Singapore.
- Đặc tính nước đầu vào: Nước thải sinh hoạt bổ sung sắt ($10\text{--}30\text{ mg/L Fe}$) ở thượng nguồn.
- Công suất xử lý định mức: $24\text{ m}^3/\text{ngày}$.
- Cấu hình công nghệ:
  - Cụm tiền xử lý cơ học.
  - Bể phản ứng sinh học 5 ngăn nạp liệu phân đoạn (five-pass step-feed bioreactor) kết hợp vùng kỵ khí/hiếu khí (anaerobic/oxic zonation).
  - Bể màng ngập (submerged membrane tank) tách sinh khối.
- Hồ sơ áp suất xuyên màng:
  - Áp suất xuyên màng (TMP) ghi nhận liên tục qua hệ thống giám sát tự động.
  - Cấu trúc module màng dạng sợi rỗng ngập nước vận hành chu kỳ hút/rửa ngắt quãng.
- Khung thời gian và kích thước mẫu:
  - Thời gian thu thập từ tháng 09/2021 đến tháng 06/2022.
  - Tần suất phân tích các chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP) là 2 lần/tuần.
  - Mô hình chỉ sử dụng các ngày có đầy đủ tất cả biến đầu vào và giá trị TMP.
  - Tập dữ liệu hợp lệ đạt 71 mẫu ghép cặp theo thời gian ($N_{\text{target}} = 71$).
- Thách thức dữ liệu:
  - Kích thước mẫu nhỏ phản ánh hạn chế thực tế trong giám sát trạm pilot.
  - Số liệu thưa tạo kịch bản thực tế để kiểm chứng học chuyển giao (Transfer Learning).

#### 2.1.2 Các trạm nguồn: Cấu hình hệ thống và tập dữ liệu quy mô lớn (Source Plants)
- Đối tượng nghiên cứu: Ba trạm MBR quy mô pilot xử lý nước thải sinh hoạt tại Singapore.
- Tổng số bản ghi dữ liệu: Đạt 332 mẫu hợp lệ ($N_{\text{source}} = 332$):
  - Trạm 1 (Plant 1): 100 bản ghi.
  - Trạm 2 (Plant 2): 132 bản ghi.
  - Trạm 3 (Plant 3): 100 bản ghi.
- Cấu hình công nghệ chung:
  - Xử lý sinh học thiếu khí/hiếu khí (anoxic/oxic).
  - Tách màng ngập trong bể (immersed membrane separation).
  - Hệ thống tuần hoàn bùn hoạt tính và xả bùn dư truyền thống.
- Tính tương đồng và cơ sở chuyển giao tri thức:
  - Trạm đích nhận nước thải giàu sắt nhưng giữ cấu hình xử lý tương đồng các trạm nguồn.
  - Cơ chế tắc nghẽn màng (MBR fouling) chia sẻ các quy luật thủy lực và sinh học chung.
  - Độ tương đồng này làm nền tảng cho việc áp dụng học chuyển giao xuyên trạm.

#### 2.1.3 Tập biến số vận hành và hóa lý được giám sát (Monitored Variables)
- Tổng số biến số giám sát: Mỗi trạm ghi nhận đồng thời 11 biến đầu vào và 1 biến đầu ra.
- Nhóm thông số vận hành thủy lực:
  - Thời gian lưu nước (HRT, đơn vị $\text{h}$).
  - Thời gian lưu bùn (SRT, đơn vị $\text{d}$).
  - Lưu lượng riêng qua màng (FLUX, đơn vị $\text{L}/(\text{m}^2\cdot\text{h})$).
- Nhóm thông số chất lượng nước và nồng độ bùn:
  - Nhu cầu oxy hóa học tổng số (TCOD, đơn vị $\text{mg/L}$).
  - Nhu cầu oxy hóa học hòa tan (SCOD, đơn vị $\text{mg/L}$).
  - Nồng độ chất rắn lơ lửng trong dịch hỗn hợp (MLSS, đơn vị $\text{mg/L}$).
  - Nồng độ chất rắn lơ lửng bay hơi trong dịch hỗn hợp (MLVSS, đơn vị $\text{mg/L}$).
- Nhóm hoạt chất sinh học gây tắc nghẽn màng:
  - Protein trong EPS (EPSp, đơn vị $\text{mg/L}$).
  - Carbohydrate trong EPS (EPSc, đơn vị $\text{mg/L}$).
  - Protein trong SMP (SMPp, đơn vị $\text{mg/L}$).
  - Carbohydrate trong SMP (SMPc, đơn vị $\text{mg/L}$).
- Biến mục tiêu giám sát:
  - Áp suất xuyên màng TMP (đơn vị $\text{kPa}$) thu từ cảm biến tự động trực tuyến.
  - Dữ liệu TMP được căn chỉnh thời gian khớp chính xác với từng ngày lấy mẫu hóa lý.

---

### 2.2 Phương pháp phân tích hóa lý (Physicochemical analytical methods)

#### 2.2.1 Quy trình phân tích các chỉ tiêu vận hành và chất lượng bùn (Standard Methods)
- Thông số vận hành: HRT, SRT và FLUX được ghi chép liên tục từ nhật ký vận hành thực địa.
- Phân tích nhu cầu oxy hóa học:
  - Xác định TCOD và SCOD theo phương pháp so màu hồi lưu kín APHA 5220D.
  - Mẫu SCOD được lọc qua màng lọc có kích thước lỗ $0{,}45\ \mu\text{m}$ trước khi phân tích.
- Phân tích nồng độ chất rắn sinh khối:
  - Xác định MLSS và MLVSS theo Tiêu chuẩn kiểm tra nước và nước thải (Standard Methods 2540D và 2540E).
  - Sấy mẫu tại $105\ ^\circ\text{C}$ để đo MLSS và nung tại $550\ ^\circ\text{C}$ để xác định MLVSS.

#### 2.2.2 Quy trình chiết tách và định lượng phân đoạn EPS và SMP (EPS/SMP Fractionation)
- Định nghĩa và chiết tách phân đoạn SMP:
  - Ly tâm dịch hỗn hợp bùn ở tốc độ thấp.
  - Thu dịch nổi và lọc qua màng $0{,}45\ \mu\text{m}$ để lấy phân đoạn SMP hòa tan.
- Quy trình chiết tách phân đoạn EPS liên kết:
  - Sử dụng phương pháp nhiệt (heat extraction method) trên phần bùn lắng còn lại.
  - Đưa huyền phù bùn vào bể ổn nhiệt ở $80\ ^\circ\text{C}$ trong khoảng thời gian quy định để giải phóng EPS từ bông bùn.
  - Ly tâm và thu dịch chứa EPS liên kết.
- Phương pháp định lượng thành phần sinh hóa:
  - Định lượng protein (EPSp và SMPp): Áp dụng phương pháp Lowry cải tiến (Modified Lowry Protein Assay) với chuẩn albumin huyết thanh bò (BSA).
  - Định lượng carbohydrate (EPSc và SMPc): Áp dụng phương pháp Dubois (phương pháp Phenol-Sulfuric Acid) với chuẩn D-glucose.

#### 2.2.3 Đặc trưng hóa chất hữu cơ hòa tan và cấu trúc bùn (Spectroscopic & Organic Profiling)
- Sắc ký lỏng phát hiện cacbon hữu cơ (LC-OCD):
  - Phân tách chất hữu cơ hòa tan thành các phân đoạn theo kích thước phân tử.
  - Nhóm biopolymer: Khối lượng phân tử $\text{MW} > 20\text{ kDa}$.
  - Nhóm hợp chất phân tử lượng thấp ($\text{MW} < 1000\text{ Da}$): Chất humic, khối xây dựng (building blocks), axit trọng lượng thấp và hợp chất trung tính.
- Phân bố kích thước hạt (PSD):
  - Đo phổ kích thước hạt bùn hoạt tính bằng thiết bị nhiễu xạ laser (laser diffraction particle analyzer).
- Thời gian hút mao dẫn (CST):
  - Đánh giá khả năng lọc và tách nước của bùn bằng thiết bị đo CST tiêu chuẩn.
- Tổng cacbon hữu cơ (TOC):
  - Đo nồng độ cacbon hữu cơ bằng máy phân tích TOC-VCSH (Shimadzu, Nhật Bản).
- Phổ huỳnh quang ma trận kích thích - phát xạ (EEM):
  - Đo phổ huỳnh quang ba chiều bằng máy quang phổ huỳnh quang để nhận diện các hợp chất tương tự humic và tryptophan.
- Định lượng hàm lượng sắt tổng:
  - Phân tích sắt trong nước đầu vào và bùn bằng quang phổ phát xạ nguyên tử plasma cảm ứng (ICP-OES).

---

### 2.3 Tiền xử lý dữ liệu và lựa chọn đặc trưng (Data preprocessing and feature selection)

#### 2.3.1 Xử lý ngoại lai, gán giá trị thiếu và chuẩn hóa thang đo Z-score (Standardization)
- Làm sạch dữ liệu:
  - Kiểm tra và xử lý điểm ngoại vi bằng khoảng tứ phân vị và ngưỡng vật lý thực nghiệm.
  - Nội suy dữ liệu thiếu dựa trên tính liên tục cục bộ của chuỗi thời gian.
- Chuẩn hóa Z-score:
  - Đưa tất cả biến số về cùng thang đo nhằm tránh ưu tiên các biến có khoảng biến thiên lớn:
    $$z = \frac{x - \mu}{\sigma}$$
  - Trong đó: $x$ là giá trị ban đầu, $\mu$ là giá trị trung bình mẫu, $\sigma$ là độ lệch chuẩn của mẫu.
  - Bộ chuẩn hóa chỉ khớp (fit) trên tập dữ liệu huấn luyện để ngăn chặn rò rỉ dữ liệu (data leakage).
  - Giá trị dự báo của mô hình được biến đổi ngược về đơn vị gốc sau khi suy luận.

#### 2.3.2 Tái định dạng biến mục tiêu chênh lệch áp suất lọc dTMP (Target Reconstruction)
- Mục tiêu dự đoán cuối cùng: Áp suất màng ngày tiếp theo ($\text{TMP}_{t+1}$).
- Định dạng biến mục tiêu trung gian:
  - Sử dụng mức tăng áp suất lọc $\Delta \text{TMP}_t$ (kí hiệu là $\text{dTMP}_t$) làm đích huấn luyện mô hình:
    $$\text{dTMP}_t = \text{TMP}_{t+1} - \text{TMP}_t$$
- Ưu điểm cơ chế:
  - Giảm tính không dừng (non-stationarity) của chuỗi thời gian áp suất màng.
  - Khắc phục sự sai lệch mức áp suất nền tuyệt đối giữa các trạm khác nhau.
  - Tạo ra phân phối dữ liệu tập trung quanh giá trị 0.
- Khôi phục giá trị thực tế:
  - Giá trị dự đoán $\widehat{\text{TMP}}_{t+1}$ được tái tạo bằng cách cộng dTMP dự báo vào TMP đo đạc hiện tại:
    $$\widehat{\text{TMP}}_{t+1} = \text{TMP}_t + \widehat{\text{dTMP}}_t$$

#### 2.3.3 Phân tích thành phần chính liên hợp đánh giá độ lệch phân phối (Joint PCA)
- Mục đích phân tích:
  - Đo lường mức độ trùng lặp không gian và độ lệch phân phối giữa miền nguồn và miền đích.
- Phương pháp thực hiện:
  - Tiến hành phân tích thành phần chính liên hợp (Joint Principal Component Analysis - Joint PCA).
  - Đưa toàn bộ các biến đầu vào cùng biến trung gian $\text{dTMP}$ vào ma trận phân tích.
  - Khối biến đầu vào và khối biến đầu ra được chuẩn hóa độc lập và gán trọng số tổng thể ngang nhau.

#### 2.3.4 Sàng lọc biến số theo tỷ lệ SFR và kiểm định tương quan Pearson (Feature Screening)
- Tỷ lệ kích thước mẫu trên số đặc trưng (SFR):
  - Chỉ số $\text{SFR} = N/p$ quyết định nguy cơ quá khớp trong bài toán mẫu nhỏ.
  - Yêu cầu thực nghiệm cần $\text{SFR} > 10$ để mô hình đạt độ tin cậy thống kê cao.
- Sàng lọc thô tương quan đặc trưng - mục tiêu ($X\text{--}y$ Pearson correlation):
  - Đánh giá tương quan Pearson trực tiếp với $\text{TMP}$ ngày tiếp theo:
    $$r_{x,y} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}$$
  - Các đặc trưng tương quan mạnh được giữ lại:
    - $\text{FLUX}$: $|r| = 0{,}471$.
    - $\text{EPSc}$: $|r| = 0{,}462$.
    - $\text{HRT}$: $|r| = 0{,}440$.
    - $\text{SMPp}$: $|r| = 0{,}347$.
  - Loại bỏ các đặc trưng có $|r| < 0{,}10$: $\text{SCOD}$, $\text{SMPc}$ và $\text{TCOD}$.
- Sàng lọc đa cộng tuyến đặc trưng - đặc trưng ($X\text{--}X$ Pearson collinearity):
  - Cặp $\text{HRT}$ và $\text{FLUX}$ có tương quan âm rất mạnh ($r = -0{,}86$) do ràng buộc lưu lượng thủy lực. Giữ lại $\text{FLUX}$ do có tương quan với $\text{TMP}$ cao hơn.
  - Cặp $\text{MLSS}$ và $\text{MLVSS}$ có tương quan dương gần như tuyệt đối ($r = 0{,}96$). Giữ lại $\text{MLVSS}$ do đại diện cho phần sinh khối hoạt tính mang EPS.
- Tập đặc trưng thu gọn cuối cùng:
  - Gồm 6 thông số: $\text{FLUX}$, $\text{SRT}$, $\text{MLVSS}$, $\text{EPSc}$, $\text{EPSp}$, $\text{SMPp}$.

---

### 2.4 Xây dựng mô hình cơ sở dựa trên trạm nguồn (Construction of base models)

#### 2.4.1 Phân chia dữ liệu theo thời gian và kiến trúc mô hình chuỗi LSTM-base (LSTM Architecture)
- Phân chia tập dữ liệu nguồn:
  - Chia tách dữ liệu của từng trạm nguồn theo thứ tự thời gian tuyến tính thay vì ngẫu nhiên.
  - Loại bỏ hiện tượng rò rỉ thông tin giữa các mẫu thời gian kề cận nhau.
- Độ dài cửa sổ lịch sử:
  - Thiết lập cửa sổ chuỗi thời gian độ dài $T = 3$ bước thời gian liên tiếp.
- Kiến trúc mạng LSTM-base:
  - Sử dụng mạng bộ nhớ dài - ngắn (Long Short-Term Memory) nhỏ gọn chuyên biệt cho học chuỗi.
  - Nhận đầu vào là chuỗi đặc trưng chuẩn hóa độ dài 3 bước để mô hình hóa động học tích lũy chất tắc nghẽn.

#### 2.4.2 Kiến trúc mô hình cây quyết định XGBoost-base với đặc trưng trễ (XGBoost Architecture)
- Kiến trúc mô hình:
  - Thuật toán tăng cường độ dốc cây quyết định (eXtreme Gradient Boosting - XGBoost).
- Mã hóa biến trễ thời gian:
  - Sử dụng thông tin lịch sử 3 bước được làm phẳng thành các biến trễ (lagged features).
  - Tổng số đặc trưng đầu vào cho cây là $6 \times 3 = 18$ biến trễ.
  - Đảm bảo tính công bằng thực nghiệm khi mô hình cây nhận đúng dung lượng thông tin như mô hình mạng LSTM.

#### 2.4.3 Tối ưu hóa siêu tham số bằng Optuna và kiểm định chéo chuỗi thời gian (Hyperparameter Tuning)
- Khung kiểm định chéo:
  - Áp dụng kiểm định chéo chuỗi thời gian 5 nếp (5-fold time-series cross-validation) trên tập huấn luyện nguồn.
  - Huấn luyện trên các mốc quá khứ và đánh giá trên mốc tương lai nhằm ngăn ngừa thiên lệch thời gian.
- Khung tối ưu hóa Bayes Optuna:
  - Tự động dò tìm bộ siêu tham số tối ưu (tốc độ học, số tầng, số cây, độ sâu, hệ số điều chuẩn).
  - Sau tối ưu, hai mô hình hoàn chỉnh được huấn luyện trên toàn bộ tập huấn luyện nguồn và lưu trữ làm trọng số gốc cho học chuyển giao.

---

### 2.5 Xây dựng mô hình đường cơ sở cho trạm đích (Construction of target baseline model)

#### 2.5.1 Chiến lược phân chia dữ liệu kiểm thử độc lập 50:50 (Data Splitting Strategy)
- Tỷ lệ phân chia tập dữ liệu trạm đích:
  - Phân chia tập 71 mẫu trạm đích theo thứ tự thời gian chuẩn tỷ lệ 50:50.
  - Nửa đầu 50% ($N \approx 35$ mẫu) dùng làm nguồn dữ liệu huấn luyện và tinh chỉnh.
  - Nửa sau 50% ($N = 36$ mẫu) đóng vai trò tập kiểm thử độc lập (test set), hoàn toàn không được nhìn thấy trước.
- Mục đích phân chia:
  - Ngăn ngừa hoàn toàn hiện tượng rò rỉ dữ liệu theo trục thời gian.
  - Đánh giá khả năng dự báo dài hạn trên dữ liệu thực tế.

#### 2.5.2 Cấu hình mô hình XGBoost-baseline độc lập (Standalone Baseline Configuration)
- Lựa chọn thuật toán đường cơ sở:
  - Chọn XGBoost độc lập làm mô hình đối chứng thay vì huấn luyện một mạng LSTM riêng biệt.
  - Mạng LSTM độc lập dễ rơi vào trạng thái mất ổn định và quá khớp nặng khi chỉ có khoảng 35 mẫu huấn luyện.
- Thiết lập huấn luyện:
  - Mô hình cây XGBoost-baseline chỉ sử dụng dữ liệu trong nửa đầu của trạm đích.
  - Bộ chuẩn hóa biến mục tiêu và đặc trưng được khớp hoàn toàn độc lập trên nửa đầu này.
  - Sử dụng cùng 6 đặc trưng đầu vào để bảo đảm tính đối sánh trực tiếp với mô hình học chuyển giao.

---

### 2.6 Xây dựng mô hình học chuyển giao (Construction of transfer learning models)

#### 2.6.1 Thiết lập tỷ lệ tinh chỉnh FT và phân đoạn lấy mẫu (Fine-Tuning Ratio Setup)
- Định nghĩa tỷ lệ tinh chỉnh ($\text{FT}$):
  - Tỷ lệ $\text{FT}$ biểu thị phần trăm dữ liệu từ tổng tập trạm đích được sử dụng để tinh chỉnh mô hình:
    $$\text{FT} \in \{0\%,\ 10\%,\ 20\%,\ 30\%,\ 40\%,\ 50\%\}$$
  - Tại $\text{FT} = 0\%$: Mô hình chuyển giao trực tiếp không qua tinh chỉnh (zero-shot direct transfer).
  - Tại $\text{FT} = 10\%\text{ đến }50\%$: Thích ứng gia tăng với số lượng mẫu tăng dần lấy từ vùng 50% đầu.
- Giao thức lấy mẫu nhiều phân đoạn liên tục:
  - Rút ngẫu nhiên nhiều phân đoạn chuỗi thời gian liên tục từ vùng tinh chỉnh.
  - Tránh phụ thuộc vào một giai đoạn lịch sử cục bộ duy nhất.
  - Mỗi thực nghiệm được lặp lại với 5 hạt giống ngẫu nhiên (random seeds).
  - Kết quả báo cáo dưới dạng giá trị trung bình kèm độ lệch chuẩn ($\text{mean} \pm \text{SD}$).

#### 2.6.2 Chiến lược cập nhật trọng số và tinh chỉnh cho LSTM-FT và XGBoost-FT (Model Adaptation)
- Mô hình mạng chuỗi LSTM-FT:
  - Khởi tạo trọng số từ mô hình LSTM-base đã học các quy luật tắc nghẽn chung ở trạm nguồn.
  - Tinh chỉnh các tầng mạng bằng dữ liệu trạm đích với tốc độ học nhỏ (fine-tuning learning rate).
  - Giữ lại các đặc trưng tổng quát và cập nhật biểu diễn thích ứng với đặc tính nước thải giàu sắt.
- Mô hình cây XGBoost-FT:
  - Bổ sung và cập nhật cây trên cơ sở cấu trúc cây XGBoost-base đã huấn luyện từ trước.
  - Điều chỉnh trọng số lá và ngưỡng tách nhánh để thích ứng với sai lệch phân phối của trạm đích.

#### 2.6.3 Môi trường phần cứng và khung phần mềm thực nghiệm (Computational Environment)
- Ngôn ngữ và thư viện lập trình:
  - Ngôn ngữ Python phiên bản 3.10.18.
  - Xây dựng và huấn luyện mạng học sâu trên thư viện PyTorch phiên bản 2.7.0.
  - Sử dụng thư viện XGBoost, Scikit-learn và Optuna cho mô hình cây và tối ưu hóa siêu tham số.
- Cấu hình phần cứng máy tính:
  - Bộ vi xử lý trung tâm: Intel Core i7-14700KF (28 luồng logic).
  - Bộ nhớ truy xuất ngẫu nhiên: 32 GB RAM.
  - Bộ xử lý đồ họa chuyên dụng: NVIDIA GeForce RTX 5060 Ti GPU.

---

### 2.7 Đánh giá hiệu năng mô hình (Evaluation of model performance)

#### 2.7.1 Các chỉ số định lượng đánh giá sai số và độ phù hợp ($R^2$, RMSE, MAE)
- Hệ số xác định ($R^2$):
  - Đánh giá tỷ lệ phương sai của giá trị TMP quan trắc được giải thích bởi mô hình:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó: $y_i$ là giá trị TMP quan trắc thực tế, $\hat{y}_i$ là giá trị dự đoán, $\bar{y}$ là giá trị trung bình quan trắc, $n$ là số mẫu kiểm thử.
- Sai số căn bậc hai trung bình bình phương (RMSE):
  - Đo lường độ lệch chuẩn của phần dư dự đoán, phản ánh độ nhạy với sai số lớn:
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
- Sai số tuyệt đối trung bình (MAE):
  - Đo mức sai số trung bình trực tiếp theo đơn vị đo áp suất ($\text{kPa}$):
    $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$

#### 2.7.2 Phân tích độ quan trọng đặc trưng bằng LOFO và SHAP (Model Interpretability)
- Phương pháp loại bỏ từng đặc trưng (Leave-One-Feature-Out - LOFO):
  - Lần lượt loại bỏ từng biến số đầu vào, huấn luyện lại hoặc đánh giá lại mô hình trên cùng điều kiện.
  - Mức độ gia tăng sai số (RMSE/MAE) hoặc suy giảm $R^2$ phản ánh vai trò không thể thay thế của biến đó.
  - Sử dụng kiểm định phi tham số Wilcoxon signed-rank test cặp đôi hai phía để đánh giá ý nghĩa thống kê ($p < 0{,}05$).
- Phương pháp giá trị phân bổ Shapley (SHapley Additive exPlanations - SHAP):
  - Dựa trên lý thuyết trò chơi hợp tác để tính toán đóng góp biên công bằng của từng biến số:
    $$\phi_j = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} [f(S \cup \{j\}) - f(S)]$$
  - Trong đó: $F$ là toàn bộ tập đặc trưng, $S$ là tập con các đặc trưng không chứa biến $j$, $f(S)$ là giá trị dự đoán của mô hình khi chỉ có tập $S$.
  - Biểu đồ tóm tắt SHAP giải thích hướng tác động âm/dương của nồng độ EPS, SMP và thông số vận hành lên tốc độ tăng áp suất TMP.

---

### 2.8 Khả năng thích ứng của mô hình trong điều kiện xuyên kịch bản (Cross-scenario adaptability)

#### 2.8.1 Cấu hình trạm MBR xử lý nước thải công nghiệp hóa dầu và dược phẩm (Industrial Scenario)
- Bối cảnh mở rộng thực nghiệm:
  - Kiểm tra tính tổng quát hóa của khung học chuyển giao trên hệ thống MBR pilot xử lý nước thải công nghiệp hỗn hợp tại Singapore.
  - Nguồn nước thải kết hợp giữa nhà máy hóa dầu và cơ sở sản xuất dược phẩm.
- Đặc thù nước thải công nghiệp:
  - Chứa nhiều hợp chất hữu cơ khó phân hủy sinh học, chất hoạt động bề mặt và độc chất ức chế bùn.
  - Cấu trúc chất gây tắc nghẽn và động thái màng khác biệt sâu sắc so với nước thải sinh hoạt đô thị.

#### 2.8.2 Giao thức kiểm thử chuyển giao xuyên kịch bản không tái tối ưu (Zero-retuning Protocol)
- Thiết lập mô hình chuyển giao:
  - Sử dụng mô hình mạng LSTM-FT đã được tiền huấn luyện trên các trạm nguồn sinh hoạt.
  - Kiểm thử tại hai chế độ tinh chỉnh: $\text{FT} = 0\%$ (chuyển giao trực tiếp) và $\text{FT} = 40\%$ (tinh chỉnh với 40% dữ liệu công nghiệp).
- Nguyên tắc giữ nguyên cấu hình (Frozen settings):
  - Giữ nguyên cấu trúc mô hình tiền huấn luyện ban đầu.
  - Áp dụng nguyên vẹn quy trình phân chia chuỗi thời gian, phương pháp làm sạch và chuẩn hóa dữ liệu.
  - Không tiến hành tìm kiếm lại siêu tham số hay can thiệp cấu trúc mạng.
- Mục tiêu đánh giá:
  - Xác nhận xem khung học chuyển giao có duy trì độ chính xác cao ($R^2 \approx 0{,}9$) khi môi trường hóa lý thay đổi đột ngột hay không.
  - Khám phá sự dịch chuyển của các tín hiệu tắc nghẽn then chốt (như vai trò vượt trội của SMPp trong nước thải công nghiệp).
