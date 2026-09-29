## 3.1 Phân phối dữ liệu trạm nguồn - trạm đích và phân tích PCA

### 3.1.1 Phân phối các biến đo lường giữa trạm nguồn và trạm đích
- So sánh các thông số vận hành cốt lõi:
  - Giá trị vận hành của trạm đích nằm trong hoặc sát dải biến thiên của các trạm nguồn.
  - Thời gian lưu thủy lực (HRT): Trạm đích duy trì cố định ở mức $5.5\text{ h}$. Các trạm nguồn dao động từ $5.0\text{ h}$ đến $5.5\text{ h}$.
  - Thời gian lưu bùn (SRT): Trạm đích duy trì ở mức $6.8\text{ d}$. Các trạm nguồn dao động từ $5.0\text{ d}$ đến $7.0\text{ d}$.
  - Thông lượng lọc (FLUX): Trạm đích vận hành ở mức $25\text{ LMH}$ ($\text{L/(m}^2\cdot\text{h)}$). Các trạm nguồn biến thiên trong dải rộng từ $25\text{ LMH}$ đến $44\text{ LMH}$.
- Dải biến thiên các thông số sinh khối và bám bẩn tại các trạm nguồn:
  - Nồng độ chất rắn lơ lửng trong bùn hoạt tính (MLSS): Biến thiên từ $900\text{ mg/L}$ đến $9730\text{ mg/L}$.
  - Nồng độ chất rắn lơ lửng bay hơi (MLVSS): Biến thiên từ $639\text{ mg/L}$ đến $7671\text{ mg/L}$.
  - Phân đoạn protein của chất polyme ngoại bào (EPSp): Dao động từ $25.0\text{ mg/L}$ đến $658.8\text{ mg/L}$.
  - Phân đoạn carbohydrate của chất polyme ngoại bào (EPSc): Dao động từ $0.0\text{ mg/L}$ đến $117.1\text{ mg/L}$.
  - Phân đoạn carbohydrate của sản phẩm vi sinh hòa tan (SMPc): Dao động từ $0.8\text{ mg/L}$ đến $33.3\text{ mg/L}$.
  - Phân đoạn protein của sản phẩm vi sinh hòa tan (SMPp): Dao động từ $2.7\text{ mg/L}$ đến $44.5\text{ mg/L}$.
- Phân phối các biến sinh thái và bám bẩn tại trạm đích:
  - Trạm đích ghi nhận biên độ phân phối hẹp hơn so với các trạm nguồn.
  - Chỉ số MLSS: Dao động từ $3580\text{ mg/L}$ đến $7340\text{ mg/L}$.
  - Chỉ số MLVSS: Dao động từ $3340\text{ mg/L}$ đến $5920\text{ mg/L}$.
  - Chỉ số EPSp: Dao động từ $73.5\text{ mg/L}$ đến $469.9\text{ mg/L}$.
  - Chỉ số EPSc: Dao động từ $17.1\text{ mg/L}$ đến $81.3\text{ mg/L}$.
  - Chỉ số SMPc: Dao động từ $2.6\text{ mg/L}$ đến $20.1\text{ mg/L}$.
  - Chỉ số SMPp: Dao động từ $4.8\text{ mg/L}$ đến $10.8\text{ mg/L}$.

Table 1: So sánh dải phân phối các biến đo lường giữa các trạm nguồn và trạm đích.
| Nhóm thông số | Biến số đo lường | Đơn vị | Dải biến thiên trạm nguồn | Dải biến thiên trạm đích |
| :--- | :--- | :--- | :--- | :--- |
| Vận hành cốt lõi | HRT | $\text{h}$ | $5.0\text{--}5.5$ | $5.5$ |
| Vận hành cốt lõi | SRT | $\text{d}$ | $5.0\text{--}7.0$ | $6.8$ |
| Vận hành cốt lõi | FLUX | $\text{LMH}$ | $25\text{--}44$ | $25$ |
| Sinh khối bùn | MLSS | $\text{mg/L}$ | $900\text{--}9730$ | $3580\text{--}7340$ |
| Sinh khối bùn | MLVSS | $\text{mg/L}$ | $639\text{--}7671$ | $3340\text{--}5920$ |
| Polyme ngoại bào (EPS) | EPSp | $\text{mg/L}$ | $25.0\text{--}658.8$ | $73.5\text{--}469.9$ |
| Polyme ngoại bào (EPS) | EPSc | $\text{mg/L}$ | $0.0\text{--}117.1$ | $17.1\text{--}81.3$ |
| Vi sinh hòa tan (SMP) | SMPc | $\text{mg/L}$ | $0.8\text{--}33.3$ | $2.6\text{--}20.1$ |
| Vi sinh hòa tan (SMP) | SMPp | $\text{mg/L}$ | $2.7\text{--}44.5$ | $4.8\text{--}10.8$ |

### 3.1.2 Phân tích thành phần chính PCA và độ lệch phân phối
- Tỷ lệ giải thích phương sai của PCA:
  - Hai thành phần chính đầu tiên (PC1 và PC2) giải thích $74.0\%$ tổng phương sai của bộ dữ liệu kết hợp.
  - Hình chiếu hai chiều này phản ánh đầy đủ các biến động chính của các đặc trưng bám bẩn màng.
- Mức độ tương đồng không gian giữa các trạm nguồn:
  - Các cụm dữ liệu trạm nguồn xuất hiện mức độ chồng lấn (overlap) rất lớn trên mặt phẳng PC1-PC2.
  - Sự chồng lấn này chứng minh các trạm nguồn chia sẻ quy luật bám bẩn tương đồng trong xử lý nước thải sinh hoạt.
- Hiện tượng lệch phân phối tại trạm đích:
  - Tập dữ liệu trạm đích tạo thành một cụm co cụm chặt hơn và tách biệt một phần khỏi các trạm nguồn.
  - Vị trí tách biệt này xác nhận sự tồn tại của độ lệch phân phối (distribution shift) giữa hai miền dữ liệu.
- Vùng chồng lấn liên miền và tính khả thi của Transfer Learning:
  - Dữ liệu trạm đích và trạm nguồn vẫn duy trì một vùng chồng lấn rõ rệt.
  - Vùng chồng lấn cung cấp nền tảng vững chắc để xây dựng các mô hình cơ sở từ trạm nguồn.
  - Sự tồn tại của miền chung này bảo đảm tính khả thi cho quy trình tinh chỉnh học chuyển giao tiếp theo.

---

## 3.2 Xây dựng và đánh giá các mô hình cơ sở

### 3.2.1 Lựa chọn đặc trưng dựa trên phân tích tương quan
#### 3.2.1.1 Phân tích tương quan đặc trưng - mục tiêu ($X\text{--}y$)
- Phương pháp phân tích mức độ liên kết:
  - Hệ số tương quan tuyến tính Pearson ($r_{x,y}$) đo lường mức độ phụ thuộc giữa từng đặc trưng đầu vào và áp suất xuyên màng TMP.
- Nhóm đặc trưng có tương quan mạnh với TMP:
  - Thông lượng lọc (FLUX): Đạt hệ số tương quan $|r_{x,y}| = 0.471$.
  - Carbohydrate ngoại bào (EPSc): Đạt hệ số tương quan $|r_{x,y}| = 0.462$.
  - Thời gian lưu thủy lực (HRT): Đạt hệ số tương quan $|r_{x,y}| = 0.440$.
  - Protein hòa tan (SMPp): Đạt hệ số tương quan $|r_{x,y}| = 0.347$.
- Nhóm đặc trưng có tương quan yếu với TMP:
  - Nhu cầu oxy hóa học hòa tan (SCOD): Đạt hệ số tương quan $|r_{x,y}| < 0.1$.
  - Carbohydrate vi sinh hòa tan (SMPc): Đạt hệ số tương quan $|r_{x,y}| < 0.1$.
  - Tổng nhu cầu oxy hóa học (TCOD): Đạt hệ số tương quan $|r_{x,y}| < 0.1$.
- Loại bỏ các biến không liên quan:
  - Tác giả loại bỏ SCOD, SMPc và TCOD khỏi tập biến đầu vào do tương quan thực nghiệm quá thấp.
  - Các biến có liên kết có ý nghĩa được chuyển sang bước sàng lọc đa cộng tuyến tiếp theo.

#### 3.2.1.2 Phân tích đa cộng tuyến đặc trưng - đặc trưng ($X\text{--}X$) và bộ biến tối giản
- Kiểm soát đa cộng tuyến giữa các cặp đặc trưng:
  - Phân tích tương quan Pearson cặp ($r_{x_j, x_k}$) xác định mức độ phụ thuộc lẫn nhau giữa các biến đầu vào.
- Cặp biến vận hành gắn kết HRT và FLUX:
  - Hai thông số thể hiện tương quan âm rất mạnh với $r_{x_j, x_k} = -0.86$.
  - Cơ chế thủy lực: HRT tỉ lệ nghịch với lưu lượng cấp nước vào hệ thống. FLUX phản ánh lưu lượng lọc qua một đơn vị diện tích màng.
  - Tiêu chí lựa chọn: FLUX có hệ số tương quan với TMP ($|r_{x,y}| = 0.471$) cao hơn so với HRT ($0.440$).
  - Quyết định xử lý: Giữ lại FLUX và loại bỏ HRT để loại trừ xung đột tuyến tính.
- Cặp biến nồng độ sinh khối MLSS và MLVSS:
  - Hai thông số ghi nhận tương quan dương gần như tuyệt đối với $r_{x_j, x_k} = 0.96$.
  - Bản chất sinh học: MLVSS thể hiện hàm lượng sinh khối hữu cơ hoạt tính nằm trong tổng bùn lơ lửng MLSS.
  - Tiêu chí lựa chọn: MLVSS có tương quan cao hơn với TMP so với MLSS.
  - Quyết định xử lý: Giữ lại MLVSS và loại bỏ MLSS khỏi tập biến huấn luyện.
- Tập 6 đặc trưng tối giản phục vụ mô hình cơ sở:
  - Bộ dữ liệu đầu vào thu gọn cuối cùng gồm 6 thông số: FLUX, SRT, MLVSS, EPSc, EPSp và SMPp.

Table 2: Kết quả phân tích tương quan Pearson với TMP ($X\text{--}y$) và tương quan cặp ($X\text{--}X$).
| Đặc trưng khảo sát | Tương quan với TMP ($|r_{x,y}|$) | Biến cộng tuyến cặp | Tương quan cặp ($r_{x_j, x_k}$) | Quyết định chọn lọc | Rationale kỹ thuật |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FLUX | $0.471$ | HRT | $-0.86$ | Giữ lại | Tương quan cao nhất với TMP; đại diện thông lượng thủy lực |
| EPSc | $0.462$ | — | — | Giữ lại | Tương quan mạnh; thành phần tạo gel cản trở thủy lực |
| HRT | $0.440$ | FLUX | $-0.86$ | Loại bỏ | Đa cộng tuyến cao với FLUX; $|r_{x,y}|$ thấp hơn FLUX |
| SMPp | $0.347$ | — | — | Giữ lại | Tương quan đáng kể; tác nhân chính gây tắc nghẽn lỗ rỗng |
| MLVSS | Cao hơn MLSS | MLSS | $0.96$ | Giữ lại | Sinh khối hữu cơ mang EPS; tương quan TMP cao hơn MLSS |
| MLSS | Thấp hơn MLVSS | MLVSS | $0.96$ | Loại bỏ | Đa cộng tuyến rất mạnh với MLVSS |
| EPSp | Mức trung bình | — | — | Giữ lại | Đóng vai trò keo tụ bùn và kích hoạt bám dính ban đầu |
| SRT | Mức trung bình | — | — | Giữ lại | Thông số vận hành then chốt kiểm soát sinh trưởng bùn |
| SCOD | $< 0.1$ | — | — | Loại bỏ | Tương quan không đáng kể với áp suất xuyên màng |
| SMPc | $< 0.1$ | — | — | Loại bỏ | Tương quan không đáng kể với áp suất xuyên màng |
| TCOD | $< 0.1$ | — | — | Loại bỏ | Tương quan không đáng kể với áp suất xuyên màng |

### 3.2.2 Đánh giá hiệu năng dự đoán của các mô hình cơ sở
#### 3.2.2.1 So sánh định lượng sai số giữa LSTM-base và XGBoost-base
- Mức độ hội tụ quanh đường đẳng lượng:
  - Biểu đồ phân tán dự đoán cho thấy các điểm huấn luyện và kiểm tra phân bố bám sát đường $1:1$.
  - Cả hai mô hình cơ sở tái hiện chính xác diễn biến của TMP tại các trạm nguồn.
- Chỉ số kiểm tra định lượng của XGBoost-base:
  - Hệ số xác định ($R^2$): Đạt $0.86$ trên tập kiểm tra độc lập của trạm nguồn.
  - Sai số toàn phương trung bình (RMSE): Đạt $3.01\text{ kPa}$.
  - Sai số tuyệt đối trung bình (MAE): Đạt $1.94\text{ kPa}$.
- Chỉ số kiểm tra định lượng của LSTM-base:
  - Hệ số xác định ($R^2$): Đạt $0.87$ trên tập kiểm tra độc lập của trạm nguồn.
  - Sai số toàn phương trung bình (RMSE): Đạt $2.86\text{ kPa}$.
  - Sai số tuyệt đối trung bình (MAE): Đạt $1.68\text{ kPa}$.
- So sánh hiệu quả tổng thể:
  - LSTM-base thể hiện ưu thế vượt trội ổn định so với XGBoost-base trên toàn bộ các chỉ số kiểm tra.
  - Giá trị $R^2$ tăng $0.01$. Sai số RMSE giảm $0.15\text{ kPa}$. Sai số MAE giảm $0.26\text{ kPa}$.

Table 3: So sánh hiệu năng dự đoán TMP giữa hai mô hình cơ sở trên tập dữ liệu kiểm tra trạm nguồn.
| Mô hình cơ sở | $R^2$ | RMSE ($\text{kPa}$) | MAE ($\text{kPa}$) | Đặc trưng chi phối chính trong SHAP |
| :--- | :--- | :--- | :--- | :--- |
| XGBoost-base | $0.86$ | $3.01$ | $1.94$ | FLUX chiếm ưu thế tuyệt đối |
| LSTM-base | $0.87$ | $2.86$ | $1.68$ | EPSc, MLVSS, EPSp, SMPp phân bổ cân bằng |

#### 3.2.2.2 Sai lệch dự đoán tại vùng áp suất xuyên màng cao
- Hiện tượng gia tăng sai số ở mức áp suất lớn:
  - Cả hai mô hình đều xuất hiện độ phân tán dự đoán lớn hơn khi TMP đạt các ngưỡng giá trị cao.
  - Độ chính xác dự đoán suy giảm trong điều kiện bám bẩn màng nghiêm trọng.
- Nguyên nhân cơ chế hóa lý:
  - Lớp bánh bùn bị nén ép với cường độ cao dưới áp suất hút lớn.
  - Trở lực thủy lực bám bẩn chuyển sang trạng thái tăng trưởng phi tuyến tính phức tạp ở giai đoạn bám bẩn sâu.

### 3.2.3 Giải thích mô hình cơ sở bằng SHAP và đối chiếu đặc tính hóa lý
#### 3.2.3.1 Phân tích phân bổ giá trị SHAP của hai mô hình cơ sở
- Phương pháp luận giải thích mô hình:
  - Giá trị SHAP định lượng mức đóng góp biên của từng biến vào kết quả dự đoán TMP.
  - Tác giả phân tích trực tiếp biểu đồ đóng góp và biểu đồ phân bổ tổng thể SHAP.
- Mô hình phân bổ đóng góp của LSTM-base:
  - Bốn biến có ảnh hưởng lớn nhất gồm EPSc, MLVSS, EPSp và SMPp.
  - Hai thông số vận hành FLUX và SRT đóng góp ở mức độ thấp hơn.
  - Kiến trúc học chuỗi thời gian của LSTM thích ứng tự nhiên với các biến sinh hóa có tính biến thiên từ từ và liên tục.
- Mô hình phân bổ đóng góp của XGBoost-base:
  - Mức độ đóng góp tập trung cục bộ vào một yếu tố duy nhất.
  - Thông lượng FLUX chi phối toàn diện giá trị SHAP và vượt trội hoàn toàn so với các biến còn lại.
  - Mô hình dựa trên cây quyết định có khuynh hướng phụ thuộc cực đoan vào tín hiệu dự đoán mạnh nhất.
- Tác động cấu trúc lên tiềm năng học chuyển giao:
  - Hai mô hình đạt độ chính xác tương đương trên trạm nguồn nhưng vận hành theo hai cơ chế suy luận khác biệt.
  - Sự phụ thuộc đơn lẻ vào FLUX khiến XGBoost-FT chỉ cải thiện rất hạn chế khi chuyển giao sang trạm đích.
  - LSTM-base nắm bắt toàn diện các thành phần sinh hóa tạo tiền đề chuyển giao vững chắc.

#### 3.2.3.2 Đối chiếu đặc tính hóa lý của bùn hoạt tính và cơ chế bám bẩn EPS
- Cơ sở kiểm chứng thực nghiệm:
  - Nghiên cứu khảo sát đặc tính hóa lý bùn trạm nguồn để xác nhận tính xác thực sinh học của phân bổ SHAP.
  - Chất polyme ngoại bào EPS liên kết chặt chẽ với bông bùn và quá trình hình thành lớp bánh bùn.
  - Sản phẩm vi sinh hòa tan SMP đại diện cho các hợp chất hữu cơ hòa tan trong pha lỏng.
- Dấu ấn phổ huỳnh quang EEM của EPS:
  - Cả ba trạm nguồn thể hiện đỉnh huỳnh quang chung của protein dạng thơm trong phổ huỳnh quang 3D (EEM).
  - Tọa độ bước sóng kích thích và phát xạ: $\text{Ex/Em} \approx 220\text{--}225 / 325\text{--}355\text{ nm}$.
- Phân bố kích thước hạt của bùn hoạt tính:
  - Kích thước hạt bùn phân bố tập trung chủ yếu trong khoảng $20\text{--}40\ \mu\text{m}$.
  - Cấu trúc hạt này rất dễ lắng đọng lên bề mặt màng và hình thành nhanh lớp bánh bùn lọc.
- Cơ chế tác động của phân đoạn EPSp:
  - Thành phần EPSp chứa các protein dạng thơm liên kết với sự kết tụ của các bông bùn.
  - Phân đoạn này chịu trách nhiệm cho quá trình bám dính ban đầu của các chất bám bẩn lên bề mặt màng.
- Cơ chế tác động của phân đoạn EPSc:
  - Phân đoạn EPSc hình thành ma trận gel polysaccharide giữ nước.
  - Lớp gel polysaccharide nén chặt cấu trúc lớp bẩn và làm tăng đột biến trở lực thủy lực qua màng.
- Ý nghĩa vật lý của biến sinh khối MLVSS:
  - Mức đóng góp cao của MLVSS trong SHAP hoàn toàn phù hợp với thực tế vận hành.
  - MLVSS đại diện cho khối lượng sinh học mang EPS và cung cấp vật liệu lắng đọng trực tiếp lên bề mặt màng.

#### 3.2.3.3 Đặc tính sản phẩm vi sinh hòa tan SMP và cơ chế giữ lại của màng
- Dấu ấn huỳnh quang EEM của dịch lọc SMP:
  - Ba trạm nguồn ghi nhận đỉnh huỳnh quang protein dạng thơm chung tại $\text{Ex/Em} \approx 220\text{--}230 / 330\text{--}350\text{ nm}$.
  - Protein dạng thơm hòa tan này hấp phụ lên màng hoặc bị bẫy lại trong lớp bánh bùn đang phát triển.
- Phân tích sắc ký rây phân tử LC-OCD:
  - Dịch SMP tại ba trạm nguồn chứa chủ yếu carbon hữu cơ hòa tan ưa nước (hydrophilic DOC).
  - Hai phân đoạn chiếm tỷ trọng lớn nhất gồm các chất humic (humics) và hợp chất cao phân tử sinh học (biopolymers).
- Công thức tính tỷ lệ loại bỏ các phân đoạn LC-OCD qua màng:
  $$\text{Rejection (\%)} = \frac{C_{\text{SMP}} - C_{\text{effluent}}}{C_{\text{SMP}}} \times 100\%$$
  Trong đó: $C_{\text{SMP}}$ là nồng độ phân đoạn hữu cơ trong dịch SMP bể sinh học. $C_{\text{effluent}}$ là nồng độ phân đoạn tương ứng trong nước sau lọc.
- Tỷ lệ giữ lại thực nghiệm của màng đối với biopolymers:
  - Phân đoạn biopolymers ghi nhận mức giữ lại cao nhất tại cả ba trạm nguồn.
  - Tỷ lệ loại bỏ thực nghiệm nằm trong dải từ $90.0\%$ đến $95.3\%$.
- Cơ chế bám bẩn của thành phần SMPp:
  - SMPp phản ánh chính xác nhóm protein dạng thơm thuộc phân đoạn biopolymers bị màng giữ lại ưu tiên.
  - Nhóm protein này tham gia trực tiếp vào hiện tượng tắc nghẽn lỗ rỗng màng và bám bẩn hữu cơ không thể đảo ngược.

Table 4: Tổng hợp đặc tính hóa lý của bùn và dịch vi sinh tại ba trạm nguồn.
| Đối tượng hóa lý | Phương pháp phân tích | Dải đo thực nghiệm | Cơ chế tác động bám bẩn màng MBR |
| :--- | :--- | :--- | :--- |
| Đỉnh huỳnh quang EPS | Phổ huỳnh quang 3D (EEM) | $\text{Ex/Em} \approx 220\text{--}225 / 325\text{--}355\text{ nm}$ | Protein dạng thơm kích hoạt kết tụ bùn và bám dính ban đầu |
| Kích thước hạt bùn | Tán xạ laser hạt | Tập trung $20\text{--}40\ \mu\text{m}$ | Cấu trúc hạt dễ lắng đọng tạo thành lớp bánh bùn dày |
| Đỉnh huỳnh quang SMP | Phổ huỳnh quang 3D (EEM) | $\text{Ex/Em} \approx 220\text{--}230 / 330\text{--}350\text{ nm}$ | Protein hòa tan hấp phụ lên màng và bẫy trong lớp cặn |
| Phân đoạn hữu cơ SMP | Sắc ký rây LC-OCD | Hydrophilic DOC (humics và biopolymers) | Nguồn cung cấp chất hữu cơ bám bẩn vi mô |
| Tỷ lệ giữ lại biopolymers | Tính toán chênh lệch nồng độ | $90.0\%\text{--}95.3\%$ | Biopolymers bị giữ lại ưu tiên gây tắc nghẽn lỗ rỗng màng |

#### 3.2.3.4 Cơ sở cơ chế cho mô hình tiền huấn luyện LSTM-base
- Tính vững chắc của kiến trúc học máy:
  - Các đặc tính hóa lý nhất quán giữa ba trạm nguồn cung cấp bằng chứng cơ chế cho cấu trúc SHAP của LSTM-base.
  - Phân bổ trọng số của mô hình phản ánh đúng các tương tác sinh hóa tự nhiên thay vì trùng hợp thống kê ngẫu nhiên.
  - LSTM-base là mô hình cơ sở đáng tin cậy phục vụ quá trình chuyển giao tri thức sang trạm đích khan hiếm dữ liệu.
