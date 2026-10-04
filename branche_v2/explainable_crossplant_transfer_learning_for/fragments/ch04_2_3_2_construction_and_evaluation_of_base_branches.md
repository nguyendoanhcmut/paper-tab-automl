### 3.2. Construction and evaluation of base models

#### 3.2.1. Correlation-based feature selection

- **Phân tích tương quan Pearson giữa đặc trưng và biến mục tiêu ($X\text{–}y$) để sàng lọc sơ bộ không gian đầu vào (Hình S4)**:
  - Phân tích tương quan xếp hạng chỉ ra FLUX, $\text{EPS}_c$, HRT và $\text{SMP}_p$ có tương quan tương đối mạnh với áp suất xuyên màng (transmembrane pressure - TMP), với các giá trị tuyệt đối $|r_{x,y}|$ lần lượt là $0.471$, $0.462$, $0.440$ và $0.347$.
  - Ngược lại, SCOD, $\text{SMP}_c$ và TCOD thể hiện tương quan yếu với TMP khi tất cả các giá trị tuyệt đối hệ số tương quan đều dưới $0.1$ ($|r_{x,y}| < 0.1$).
  - Ba biến SCOD, $\text{SMP}_c$ và TCOD bị loại bỏ khỏi tập biến đầu vào rút gọn dùng cho mô hình hóa tiếp theo, các biến còn lại được giữ lại để tiếp tục sàng lọc đa cộng tuyến.
- **Phân tích tương quan Pearson liên đặc trưng ($X\text{–}X$) nhằm kiểm soát hiện tượng đa cộng tuyến (Hình 3(b))**:
  - Thời gian lưu thủy lực (hydraulic retention time - HRT) tương quan nghịch mạnh với thông lượng lọc (permeate flux - FLUX) với hệ số tương quan $r_{x_j, x_k} = -0.86$, phản ánh mối ràng buộc vận hành (operational coupling) khi HRT tỷ lệ nghịch với lưu lượng dòng xử lý còn FLUX đại diện cho lưu lượng nước sau lọc trên một đơn vị diện tích màng $[8]$.
  - Nồng độ chất rắn lơ lửng trong bùn lỏng (mixed liquor suspended solids - MLSS) và chất rắn lơ lửng bay hơi trong bùn lỏng (mixed liquor volatile suspended solids - MLVSS) có tương quan thuận rất mạnh với hệ số tương quan $r_{x_j, x_k} = 0.96$, phù hợp với bản chất MLVSS là phần sinh khối dễ bay hơi cấu thành MLSS $[40]$.
  - Trong hai cặp đặc trưng cộng tuyến trên, FLUX và MLVSS sở hữu giá trị $|r_{x,y}|$ với TMP cao hơn so với HRT và MLSS nên được ưu tiên giữ lại.
- **Tập biến đầu vào rút gọn (reduced input set) được thiết lập cho việc phát triển các mô hình cơ sở**:
  - Sáu biến đặc trưng cuối cùng được giữ lại gồm FLUX, thời gian lưu bùn (solids retention time - SRT), MLVSS, carbohydrate trong chất polyme ngoại bào ($\text{EPS}_c$), protein trong chất polyme ngoại bào ($\text{EPS}_p$) và protein trong sản phẩm vi sinh vật hòa tan ($\text{SMP}_p$).

#### 3.2.2. Performance evaluation of base models

- **Đồ thị phân tán dự đoán thể hiện sự tương đồng cao giữa giá trị TMP dự đoán và thực nghiệm ở các nhà máy nguồn**:
  - Phần lớn các điểm dữ liệu trên cả tập huấn luyện và kiểm tra đều phân bố bám sát đường đẳng trị (line of equality), cho thấy độ chính xác tin cậy của mô hình trên miền nguồn.
  - Cả hai mô hình cơ sở đều nắm bắt thành công các biến thiên TMP chủ đạo trong các tập dữ liệu nguồn.
- **Hiệu năng dự đoán định lượng của các mô hình cơ sở trên tập kiểm tra (testing set)**:
  - Mô hình cây quyết định tăng cường độ dốc cực đại cơ sở (XGBoost-base) đạt hệ số xác định $R^2 = 0.86$, sai số căn bậc hai trung bình $\text{RMSE} = 3.01\text{ kPa}$ và sai số tuyệt đối trung bình $\text{MAE} = 1.94\text{ kPa}$ (Hình 3(c)).
  - Mô hình mạng bộ nhớ ngắn-dài cơ sở (LSTM-base) đạt hiệu năng tốt hơn một chút, với $R^2 = 0.87$, $\text{RMSE} = 2.86\text{ kPa}$ và $\text{MAE} = 1.68\text{ kPa}$ (Hình 3(d)).
  - LSTM-base duy trì lợi thế nhỏ nhưng nhất quán so với XGBoost-base trên dữ liệu nhà máy nguồn.
- **Độ lệch dự đoán gia tăng ở các dải giá trị TMP cao do cơ chế tắc nghẽn phi tuyến**:
  - Cả hai mô hình đều xuất hiện sai số phân tán lớn hơn khi giá trị TMP tiến lên các mức cao.
  - Hiện tượng này chỉ ra việc dự đoán TMP trở nên khó khăn hơn trong điều kiện tắc nghẽn nghiêm trọng, nhiều khả năng bắt nguồn từ sự nén ép mạnh của lớp bánh bùn (fouling-layer compression) và trở lực tắc nghẽn phi tuyến (nonlinear fouling resistance) khi mức TMP dâng cao $[41]$.

#### 3.2.3. SHAP interpretation of base models and physicochemical characterization

- **Phân tích quy kết đặc trưng SHAP chỉ ra sự khác biệt về cấu trúc dự báo giữa hai mô hình cơ sở**:
  - Công cụ ChatGPT-5.4 chỉ được sử dụng làm phương tiện phụ trợ hỗ trợ tóm tắt các mẫu quy kết, trong khi việc diễn giải kết quả cuối cùng do các tác giả thực hiện dựa trên đồ thị SHAP và kết quả gán mức độ quan trọng đặc trưng tương ứng (Hình 6(d)).
  - Đối với LSTM-base, các đồ thị tóm tắt SHAP cho thấy $\text{EPS}_c$, MLVSS, $\text{EPS}_p$ và $\text{SMP}_p$ đóng góp lớn nhất (Hình 6(a); Hình S5), trong khi FLUX và SRT có ảnh hưởng tương đối thấp hơn.
  - Đối với XGBoost-base, mẫu quy kết tập trung hơn rõ rệt, trong đó FLUX chi phối toàn bộ quy kết SHAP và đóng góp vượt lên trên các biến đầu vào khác (Hình S6(a); Hình S6(b)).
  - Hai mô hình cơ sở đạt hiệu năng dự đoán tương đương nhau nhưng dựa trên hai cấu trúc dự báo khác biệt trong giai đoạn tiền huấn luyện trên các nhà máy nguồn.
  - Sự phụ thuộc rộng của LSTM-base vào $\text{EPS}_c$, MLVSS, $\text{EPS}_p$ và $\text{SMP}_p$ phản ánh tính tương thích của kiến trúc học chuỗi (sequence-learning) đối với các biến có tính liên tục theo thời gian và biến thiên từ từ $[42]$.
  - Mẫu quy kết phụ thuộc chủ đạo vào FLUX của XGBoost-base nhất quán với phân tích tương quan $X\text{–}y$ và phản ánh xu hướng của các mô hình dựa trên cây (tree-based) phụ thuộc nhiều vào một tín hiệu dự báo chiếm ưu thế $[43, 44]$.
  - Cấu trúc dự báo khác biệt này hoàn toàn nhất quán với kết quả học chuyển giao tiếp theo, khi mô hình XGBoost tinh chỉnh (XGBoost-FT) chỉ đạt sự cải thiện giới hạn so với LSTM tinh chỉnh (LSTM-FT).
- **Khảo sát đặc trưng hóa lý của sinh khối ở các nhà máy nguồn nhằm kiểm chứng tính hợp lý cơ chế của LSTM-base**:
  - Do LSTM-base đạt hiệu năng dự báo nguồn mạnh và nhiều triển vọng trong học chuyển giao, các đặc tính hóa lý của sinh khối ở ba nhà máy nguồn được phân tích để xác định xem cấu trúc quy kết mô hình học được có phù hợp với cơ chế tắc nghẽn thực tế hay không.
  - Hai thông số EPS và SMP được chú trọng đặc biệt vì đóng vai trò quan trọng trong phân tích SHAP, trong đó EPS liên kết chặt chẽ với bông bùn và tắc nghẽn bề mặt màng $[45]$, còn SMP đại diện chủ yếu cho chất hữu cơ hòa tan $[46]$.
- **Đặc trưng hóa lý liên quan đến EPS và phân bố kích thước hạt bùn củng cố mẫu quy kết của LSTM-base**:
  - Ba nhà máy nguồn thể hiện dấu ấn đặc trưng EPS nhất quán, gồm đỉnh phổ ma trận kích thích - phát xạ huỳnh quang (excitation-emission matrix - EEM) của EPS tương tự protein thơm chung tại $\text{Ex}/\text{Em} \approx 220\text{–}225 / 325\text{–}355\text{ nm}$ (Hình 4(a)–(c)) và kích thước hạt bùn chủ yếu tập trung ở dải $20\text{–}40\ \mu\text{m}$ (Hình 4(d)).
  - Các đặc tính này gợi ý cấu trúc bùn dễ lắng đọng, tạo điều kiện thuận lợi cho sự hình thành lớp bánh bùn (cake-layer formation) trong các bể MBR $[47]$.
  - Phân đoạn protein đại diện bởi $\text{EPS}_p$ nhiều khả năng gồm các thành phần giống protein thơm, liên quan mật thiết đến sự kết tụ bông bùn và bám dính ban đầu của chất bẩn lên bề mặt màng $[48]$.
  - Phân đoạn carbohydrate đại diện bởi $\text{EPS}_c$ liên quan trực tiếp đến hiệu ứng tạo gel và tăng trở lực của khung nền polysaccharide, làm gia tăng trở lực thủy lực của lớp tắc nghẽn $[49]$.
  - Mức quy kết SHAP tương đối cao của MLVSS có cơ sở vật lý rõ ràng vì MLVSS đại diện cho phân đoạn sinh khối mang EPS và tham gia trực tiếp vào quá trình lắng đọng bùn lên bề mặt màng $[3]$.
  - **Hình 4.** Bằng chứng hóa lý củng cố mẫu quy kết của LSTM-base
    - <img src="assets/fig_04_p8.jpeg" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Ba nhà máy nguồn thể hiện dấu ấn hóa lý nhất quán về đỉnh protein thơm trong EPS, bùn dễ lắng đọng và độ lưu giữ biopolymer của SMP đạt $90.0\text{–}95.3\%$.
    - **Từ đâu mà thấy được**
      - Bảng (a)–(c): Đỉnh EEM tập trung ở $\text{Ex}/\text{Em} \approx 220\text{–}225 / 325\text{–}355\text{ nm}$ với cường độ phát xạ trên $720$.
      - Bảng (d): Phân bố thể tích hạt bùn đạt đỉnh tại $20\text{–}40\ \mu\text{m}$ trên cả ba nhà máy nguồn và nhà máy mục tiêu.
      - Bảng (e)–(f): Biopolymer giảm từ $2.5\text{–}6.0\text{ mg/L}$ ở SMP xuống $0.2\text{–}0.6\text{ mg/L}$ ở nước sau lọc.
- **Đặc trưng hóa lý liên quan đến SMP và cơ chế lưu giữ biopolymer qua phân tích LC-OCD**:
  - SMP từ ba nhà máy nguồn thể hiện các đặc trưng phổ EEM tương đồng với đỉnh huỳnh quang protein thơm chung tại $\text{Ex}/\text{Em} \approx 220\text{–}230 / 330\text{–}350\text{ nm}$ (Hình S7(a)–(c)).
  - Các hợp chất SMP giống protein thơm này có thể đóng góp vào quá trình phát triển tắc nghẽn thông qua hấp phụ bề mặt màng hoặc bị lưu giữ bên trong lớp tắc nghẽn đang hình thành, đặc biệt trong giai đoạn tắc nghẽn ban đầu $[50, 51]$.
  - Phân tích sắc ký lỏng loại trừ kích thước kết hợp phát hiện cacbon hữu cơ (liquid chromatography–organic carbon detection - LC-OCD) chỉ ra SMP ở ba nhà máy nguồn bị chi phối bởi cacbon hữu cơ hòa tan (dissolved organic carbon - DOC) ưa nước, trong đó chất humic và biopolymer là các phân đoạn chủ đạo (Hình 4(e) và (f); Bảng S9).
  - Tỷ lệ lưu giữ của từng phân đoạn LC-OCD được tính bằng phần trăm suy giảm nồng độ từ SMP sang nước sau lọc tương ứng so với nồng độ ban đầu trong SMP.
  - Phân đoạn biopolymer thể hiện tỷ lệ lưu giữ cao nhất trên cả ba nhà máy nguồn, dao động từ $90.0\%$ đến $95.3\%$.
  - Kết quả này gợi ý rằng $\text{SMP}_p$ chủ yếu phản ánh thành phần giống protein thơm nằm trong nhóm biopolymer bị màng giữ lại ưu tiên và trực tiếp tham gia vào quá trình tắc nghẽn màng hữu cơ $[52]$.
- **Ý nghĩa cơ chế và độ tin cậy của mô hình tiền huấn luyện LSTM-base**:
  - Các đặc tính hóa lý chung giữa ba nhà máy nguồn cung cấp bằng chứng cơ chế rõ ràng hỗ trợ mẫu quy kết liên quan đến EPS và SMP mà LSTM-base học được.
  - Cấu trúc tri thức mà mô hình học được không đơn thuần mang tính thống kê thuần túy mà gắn liền với các đặc tính tắc nghẽn vật lý thực tế.
  - Kết quả khẳng định việc sử dụng LSTM-base làm mô hình tiền huấn luyện đáng tin cậy cho các bước học chuyển giao tiếp theo.
