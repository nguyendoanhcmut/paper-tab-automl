## 2.2 - 2.3. Khám phá dữ liệu (EDA) và Kỹ thuật đặc trưng (Feature Engineering)

### 2.2 Khám phá dữ liệu (Exploratory Data Analysis - EDA)

#### 2.2.1 Mục tiêu và quy trình phân tích thăm dò
- Phân tích khám phá dữ liệu (EDA) cung cấp cái nhìn toàn diện về cấu trúc dữ liệu vận hành hệ thống MBR.
- Phương pháp kiểm tra hình dạng phân phối, mối liên kết tiềm ẩn và các dạng mẫu cơ bản trong tập dữ liệu.
- Quy trình tích hợp thống kê mô tả, kỹ thuật trực quan hóa, ma trận tương quan và kiểm định phân phối chuẩn.
- Dữ liệu thu thập gồm 194 mẫu đo liên tục trong hơn 6 tháng từ trạm MBR quy mô thực (Full-Scale MBR).
- Bước EDA xác lập cơ sở dữ liệu sạch và định hướng cấu trúc mô hình học máy trước khi huấn luyện.

#### 2.2.2 Thống kê mô tả các thông số vận hành (Operational Feature Statistics)
- Quy mô mẫu kiểm định đạt $N = 194$ quan sát độc lập cho tất cả thông số đầu vào và biến mục tiêu.
- Thống kê mô tả tính toán các chỉ số: giá trị trung bình (Mean), độ lệch chuẩn (Std), giá trị nhỏ nhất (Min), phân vị 25% ($Q_1$), trung vị 50% ($Q_2$), phân vị 75% ($Q_3$) và giá trị lớn nhất (Max).
- Nồng độ chất rắn lơ lửng trong bùn hoạt tính (MLSS) thể hiện mức biến động biên độ lớn nhất trong hệ thống:
  - Giá trị trung bình đạt $7813\text{ mg/L}$, độ lệch chuẩn đạt $1361\text{ mg/L}$.
  - Khoảng giá trị dao động rộng từ cực tiểu $3390\text{ mg/L}$ đến cực đại $11{,}980\text{ mg/L}$.
  - Các phân vị tương ứng gồm $Q_1 = 7080\text{ mg/L}$, trung vị $Q_2 = 7900\text{ mg/L}$, và $Q_3 = 8628\text{ mg/L}$.
  - Sự dao động mạnh của MLSS phản ánh biến động nồng độ cơ chất dòng vào và hoạt tính sinh khối vi sinh vật.
- Thể tích bùn sau 30 phút lắng ($\text{SV}_{30}$):
  - Giá trị trung bình đạt $95.8\%$, độ lệch chuẩn $8.9\%$, biên độ biến thiên từ $30.0\%$ đến $99.0\%$.
  - Các giá trị phân vị gồm $Q_1 = 96.0\%$, trung vị $Q_2 = 98.0\%$, $Q_3 = 99.0\%$.
  - Chỉ số $\text{SV}_{30}$ tập trung cao ở vùng trên $95\%$, phản ánh mật độ bùn đậm đặc trong bể màng.
- Chỉ số thể tích bùn (Sludge Volume Index - SVI):
  - Công thức tính toán chuẩn:
    $$\text{SVI} = \frac{\text{SV}_{30} \times 1000}{\text{MLSS}} \quad (\text{mL/g})$$
  - Giá trị trung bình đạt $125.1\text{ mL/g}$, độ lệch chuẩn $18.9\text{ mL/g}$.
  - Khoảng phân bố ghi nhận từ cực tiểu $82.6\text{ mL/g}$ đến cực đại $182.7\text{ mL/g}$.
  - Các ngưỡng tứ phân vị gồm $Q_1 = 112.5\text{ mL/g}$, trung vị $Q_2 = 122.4\text{ mL/g}$, $Q_3 = 135.0\text{ mL/g}$.
  - Mức phân tán SVI phản ánh đặc tính lắng biến đổi vừa phải của hỗn hợp bùn sinh học tại hiện trường.
- Nồng độ oxy hòa tan (DO):
  - Giá trị trung bình đạt $5.43\text{ mg/L}$, độ lệch chuẩn $0.79\text{ mg/L}$, dao động từ $3.62\text{ mg/L}$ đến $7.55\text{ mg/L}$.
  - Các mốc phân vị gồm $Q_1 = 4.90\text{ mg/L}$, trung vị $Q_2 = 5.30\text{ mg/L}$, $Q_3 = 5.98\text{ mg/L}$.
  - Dải giá trị hẹp chứng minh hệ thống kiểm soát sục khí ổn định, cung cấp đủ oxy cho quá trình hiếu khí.
- Độ pH trong bể màng:
  - Giá trị trung bình đạt $8.11$, độ lệch chuẩn $0.40$ (hoặc $0.39$), biên độ ghi nhận từ $5.02$ đến $8.97$.
  - Các phân vị xác định gồm $Q_1 = 7.85$, trung vị $Q_2 = 7.98$, $Q_3 = 8.45$.
  - Môi trường kiềm nhẹ chiếm ưu thế, duy trì điều kiện tối ưu cho hệ vi sinh và bảo vệ màng lọc.
- Nhiệt độ nước thải (Temp):
  - Giá trị trung bình đạt $26.4^\circ\text{C}$, độ lệch chuẩn $4.5^\circ\text{C}$, dải đo từ $13.0^\circ\text{C}$ đến $31.6^\circ\text{C}$.
  - Các ngưỡng phân vị gồm $Q_1 = 25.0^\circ\text{C}$, trung vị $Q_2 = 28.3^\circ\text{C}$, $Q_3 = 29.7^\circ\text{C}$.
  - Dao động nhiệt độ theo mùa ảnh hưởng trực tiếp đến độ nhớt động học của nước và hoạt tính phân giải sinh học.
- Tỷ lệ tải trọng hữu cơ trên sinh khối (Food-to-Microorganism ratio - F/M):
  - Đơn vị tính toán: $\text{kgCOD}/(\text{kgMLSS}\cdot\text{d})$.
  - Giá trị trung bình đạt $0.012$, độ lệch chuẩn $0.004$, dải biến thiên từ $0.003$ đến $0.024$.
  - Các phân vị thực nghiệm gồm $Q_1 = 0.009$, trung vị $Q_2 = 0.011$, $Q_3 = 0.014$.
  - Mức biến thiên tương đối thấp chứng tỏ tải trọng hữu cơ nạp vào trạm xử lý giữ được sự ổn định.
- Hiệu suất loại bỏ COD ($\text{COD RM}$):
  - Giá trị trung bình đạt $64.7\%$, độ lệch chuẩn $16.9\%$, biên độ phân bố từ $18.7\%$ đến $87.6\%$.
  - Các phân vị gồm $Q_1 = 56.4\%$, trung vị $Q_2 = 70.8\%$, $Q_3 = 76.6\%$.
  - Hiệu suất loại bỏ dao động tùy thuộc thành phần hữu cơ nước thải chế biến thực phẩm theo từng mẻ sản xuất.
- Thông lượng lọc (Flux):
  - Đơn vị đo lường: $\text{LMH} = \text{L}/(\text{m}^2\cdot\text{h})$.
  - Giá trị trung bình đạt $2.65\text{ LMH}$, độ lệch chuẩn $0.52\text{ LMH}$, dao động từ $0.60\text{ LMH}$ đến $3.87\text{ LMH}$.
  - Các mức phân vị ghi nhận $Q_1 = 2.45\text{ LMH}$, trung vị $Q_2 = 2.73\text{ LMH}$, $Q_3 = 2.92\text{ LMH}$.
- Áp suất xuyên màng (Transmembrane Pressure - TMP):
  - Giá trị trung bình đạt $51.0\text{ kPa}$, độ lệch chuẩn $6.8\text{ kPa}$, dải biến thiên từ $37.0\text{ kPa}$ (hoặc $37.08\text{ kPa}$) đến $69.0\text{ kPa}$.
  - Các ngưỡng phân vị gồm $Q_1 = 46.3\text{ kPa}$, trung vị $Q_2 = 50.5\text{ kPa}$, $Q_3 = 55.0\text{ kPa}$.
  - Mức TMP phản ánh hệ thống màng đang chịu nghẹt ở mức độ trung bình với sự gia tăng trở lực định kỳ.
- Thông lượng lọc riêng (Specific Flux - Spec. Flux):
  - Công thức xác định:
    $$\text{Spec. Flux} = \frac{\text{Flux}}{\text{TMP}} \quad (\text{LMH/kPa})$$
  - Giá trị trung bình đạt $0.053\text{ LMH/kPa}$, độ lệch chuẩn $0.013\text{ LMH/kPa}$, dải đo từ $0.012$ đến $0.099\text{ LMH/kPa}$.
  - Các mức phân vị gồm $Q_1 = 0.046\text{ LMH/kPa}$, trung vị $Q_2 = 0.055\text{ LMH/kPa}$, $Q_3 = 0.062\text{ LMH/kPa}$.
  - Đại lượng thể hiện độ thấm thủy lực chuẩn hóa, duy trì tính ổn định giữa các chu kỳ vận hành khác nhau.

#### 2.2.3 Biểu đồ phân tán và đồ thị cặp (Scatter Plot và Pair Plot)
- Đồ thị cặp (Pair Plot) được khởi tạo bằng thư viện Seaborn (phiên bản 0.13.2) chạy trên nền tảng Python (phiên bản 3.13.1).
- Biểu đồ tích hợp các đường hồi quy tuyến tính và khoảng tin cậy (Confidence Intervals) $95\%$ để đánh giá xu thế dữ liệu.
- Phân tích tương quan cặp cung cấp trực quan hóa hai chiều về liên kết giữa các biến quá trình và chỉ số nghẹt màng.
- Quan sát thực nghiệm phát hiện tương quan nghịch rõ rệt giữa TMP và nồng độ DO:
  - Nồng độ DO cao đi kèm với giá trị TMP thấp hơn.
  - Tác dụng sục khí cường độ mạnh tạo lực cắt bọt khí giúp cuốn trôi các chất bám bẩn trên bề mặt màng.
  - Sục khí đầy đủ hạn chế sự tích lũy màng vi sinh vật (biofilm) và làm chậm tốc độ tắc nghẽn mao quản màng.
- Tương quan thuận yếu xuất hiện giữa TMP và nồng độ MLSS:
  - Sinh khối MLSS tăng cao làm tăng mật độ cặn bám, thúc đẩy quá trình nén lớp bánh cặn (cake layer) trên sợi màng.
- Mối liên hệ nghịch rất mạnh thể hiện rõ giữa TMP và Spec. Flux:
  - Khi hiện tượng nghẹt màng gia tăng, TMP tăng dần và thông lượng lọc riêng Spec. Flux suy giảm nhanh chóng.
  - Đồ thị xác nhận tính chất cơ học trực tiếp của sự suy giảm tính thấm qua màng lọc.
- Thông lượng riêng Spec. Flux biểu hiện tương quan thuận mức độ vừa với hiệu suất khử COD (COD RM):
  - Hiệu quả loại bỏ chất hữu cơ cao làm giảm các tiền chất gây nghẹt như polyme ngoại bào (EPS) hòa tan.
  - Nhờ đó, nước qua màng ít gây tắc nghẽn mao quản, duy trì thông lượng lọc riêng ở mức cao.
- Tương quan giữa Spec. Flux và MLSS biểu hiện rất mờ nhạt:
  - Sự thay đổi đơn lẻ của nồng độ MLSS không trực tiếp quyết định khả năng thấm của màng trong điều kiện khảo sát.
- Phân tích phụ thuộc nội bộ giữa các biến đặc trưng phát hiện tương quan nghịch chặt chẽ giữa MLSS và SVI ($r = -0.77$):
  - Khi nồng độ MLSS tăng cao, thể tích bùn lắng tương đối bị nén chặt, làm giảm chỉ số SVI danh định.
- Tương quan nghịch mạnh giữa nhiệt độ (Temp) và nồng độ DO ($r = -0.70$):
  - Hiện tượng này tuân thủ định luật vật lý về độ hòa tan của khí oxy suy giảm khi nhiệt độ chất lỏng gia tăng.
- Đồ thị phân tán đơn lẻ (Scatter Plot) giúp sàng lọc các điểm dị biệt (outliers) cực đoan gây nhiễu cho mô hình học máy.

#### 2.2.4 Phân tích ma trận hệ số tương quan Pearson
- Hệ số tương quan Pearson ($r$) định lượng mức độ liên kết tuyến tính giữa từng biến đặc trưng và biến mục tiêu.
- Công thức toán học tính hệ số tương quan tuyến tính mẫu:
  $$r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \cdot \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$
- Trong đó $\bar{x}$ và $\bar{y}$ là giá trị trung bình mẫu của biến đặc trưng $x$ và biến mục tiêu $y$.
- Ma trận tương quan toàn diện giữa 11 thông số vận hành và chỉ số màng lọc:
  - F/M: tương quan với SV30 ($0.09$), SVI ($0.01$), MLSS ($0.03$), DO ($-0.28$), pH ($-0.13$), Temp ($0.11$), Flux ($0.45$), COD RM ($0.46$), TMP ($-0.30$), Spec. Flux ($0.52$).
  - SV30: tương quan với SVI ($0.08$), MLSS ($0.54$), DO ($-0.31$), pH ($-0.27$), Temp ($-0.04$), Flux ($0.15$), COD RM ($0.23$), TMP ($-0.14$), Spec. Flux ($0.20$).
  - SVI: tương quan với MLSS ($-0.77$), DO ($0.01$), pH ($0.25$), Temp ($0.26$), Flux ($-0.22$), COD RM ($-0.21$), TMP ($0.34$), Spec. Flux ($-0.34$).
  - MLSS: tương quan với DO ($-0.19$), pH ($-0.38$), Temp ($-0.25$), Flux ($0.26$), COD RM ($0.32$), TMP ($-0.36$), Spec. Flux ($0.39$).
  - DO: tương quan với pH ($-0.06$), Temp ($-0.70$), Flux ($-0.33$), COD RM ($-0.10$), TMP ($0.20$), Spec. Flux ($-0.36$).
  - pH: tương quan với Temp ($0.42$), Flux ($0.22$), COD RM ($-0.54$), TMP ($0.42$), Spec. Flux ($-0.05$).
  - Temp: tương quan với Flux ($0.25$), COD RM ($-0.18$), TMP ($0.07$), Spec. Flux ($0.16$).
  - Flux: tương quan với COD RM ($-0.13$), TMP ($-0.18$), Spec. Flux ($0.85$).
  - COD RM: tương quan với TMP ($-0.41$), Spec. Flux ($0.11$).
  - TMP: tương quan nghịch mạnh nhất với Spec. Flux ($r = -0.65$).
- Đánh giá tương quan với áp suất xuyên màng TMP:
  - TMP có tương quan thuận mạnh nhất với độ pH ($r = 0.42$).
  - Cơ chế vi sinh và hóa lý: pH tăng kiềm hóa làm biến đổi điện tích bề mặt tế bào vi khuẩn và giảm độ tan của muối khoáng vô cơ, đẩy mạnh hiện tượng đóng cặn vô cơ (inorganic scaling).
  - TMP có tương quan nghịch với COD RM ($r = -0.41$) và MLSS ($r = -0.36$).
  - Khả năng xử lý chất hữu cơ cao và mật độ sinh khối ổn định giúp hạn chế tích tụ các tác nhân hòa tan gây nghẹt màng.
- Đánh giá tương quan với thông lượng riêng Spec. Flux:
  - Spec. Flux có tương quan thuận cao nhất với tỷ lệ tải trọng F/M ($r = 0.52$).
  - Điều kiện F/M tối ưu kích thích hoạt tính trao đổi chất của vi sinh vật và cải thiện đặc tính keo tụ, giảm tắc nghẽn mao quản màng.
  - Spec. Flux có tương quan thuận mức vừa với nồng độ MLSS ($r = 0.39$), chứng tỏ sinh khối duy trì chức năng lọc ổn định trong khoảng khảo sát.
  - Spec. Flux có tương quan nghịch với DO ($r = -0.36$). Nồng độ DO quá mức có thể kích thích sản sinh màng sinh học bám dính dày đặc trên bề mặt sợi màng.
- Kết quả khẳng định mối quan hệ tương tác đa biến phi tuyến phức tạp trong quy trình MBR, đòi hỏi các mô hình học máy phi tuyến thay vì mô hình tuyến tính đơn giản.

#### 2.2.5 Kiểm định phân phối chuẩn Shapiro-Wilk (Normality Check)
- Mục đích kiểm định: Đánh giá giả định phân phối chuẩn của các biến số trước khi đưa vào các thuật toán thống kê và học máy.
- Thiết lập giả thuyết thống kê:
  - Giả thuyết vô hiệu ($H_0$): Dữ liệu tuân theo phân phối chuẩn.
  - Giả thuyết đối lập ($H_1$): Dữ liệu sai lệch có ý nghĩa thống kê so với phân phối chuẩn.
- Công thức thống kê kiểm định Shapiro-Wilk:
  $$W = \frac{\left( \sum_{i=1}^n a_i x_{(i)} \right)^2}{\sum_{i=1}^n (x_i - \bar{x})^2}$$
  Trong đó $x_{(i)}$ là giá trị quan sát thứ $i$ sau khi sắp xếp theo thứ tự tăng dần, và $a_i$ là các hệ số trọng số từ ma trận hiệp phương sai.
- Giá trị thống kê $W$ biến thiên từ $0$ đến $1$; giá trị càng tiệm cận $1$ thể hiện phân phối dữ liệu càng gần với phân phối chuẩn.
- Ngưỡng mức ý nghĩa thống kê được ấn định tại $\alpha = 0.05$:
  - Nếu $p\text{-value} > 0.05$, không đủ bằng chứng bác bỏ $H_0$, dữ liệu tuân theo phân phối chuẩn.
  - Nếu $p\text{-value} \le 0.05$, bác bỏ $H_0$, xác nhận dữ liệu sai lệch có ý nghĩa khỏi phân phối chuẩn.
- Kết quả kiểm định thực nghiệm đối với toàn bộ các biến số:
  - Tỷ lệ F/M là biến duy nhất tuân theo phân phối chuẩn với $p = 0.0518 > 0.05$.
  - Toàn bộ 10 biến còn lại (SV30, SVI, MLSS, DO, pH, Temp, Flux, COD RM, TMP, Spec. Flux) đều có $p\text{-value} < 0.05$.
  - Bằng chứng thực nghiệm khẳng định hầu hết các thông số vận hành trạm MBR đều có phân phối lệch chuẩn, đuôi dày hoặc đa đỉnh.
- Ý nghĩa phương pháp luận:
  - Các mô hình hồi quy tuyến tính cổ điển (Linear Regression, Ridge, Lasso) dựa trên giả định chuẩn tắc sẽ bị suy giảm hiệu năng nghiêm trọng.
  - Tập dữ liệu đòi hỏi kỹ thuật chuẩn hóa bền vững (Robust Scaling) và các thuật toán học máy phi tham số (như Gradient Boosting Decision Trees).

---

### 2.3 Tiền xử lý dữ liệu và Kỹ thuật đặc trưng (Feature Engineering)

#### 2.3.1 Chuẩn hóa bền vững (Robust Scaling)
- Hạn chế của các phương pháp chuẩn hóa truyền thống trong môi trường công nghiệp:
  - Phương pháp chuẩn hóa cực trị (Min-Max Scaling) nhạy cảm với các điểm cực trị ngoài biên, làm co cụm đa số dữ liệu về khoảng rất hẹp.
  - Phương pháp chuẩn hóa điểm chuẩn (Z-score Standardization) sử dụng giá trị trung bình mẫu ($\mu$) và độ lệch chuẩn ($\sigma$), hai đại lượng bị bóp méo nặng nề bởi giá trị ngoại lai (outliers).
- Nguyên lý của chuẩn hóa bền vững (Robust Scaling):
  - Phương pháp loại bỏ hoàn toàn sự phụ thuộc vào trung bình và độ lệch chuẩn.
  - Thuật toán định tâm dữ liệu xung quanh trung vị ($Q_2$) và co giãn theo khoảng tứ phân vị (Interquartile Range - $\text{IQR}$).
- Công thức toán học thực thi chuẩn hóa bền vững:
  $$x_{\text{scaled}} = \frac{x - \text{Median}}{Q_3 - Q_1} = \frac{x - Q_2}{\text{IQR}}$$
  Trong đó $Q_1$ là phân vị $25\%$, $Q_3$ là phân vị $75\%$, và $\text{IQR} = Q_3 - Q_1$ chứa $50\%$ mật độ dữ liệu trung tâm.
- Vai trò xử lý giá trị ngoại lai cực đoan trong nhà máy MBR thực tế:
  - Cảm biến hiện trường chịu tác động của bám bẩn sinh học, bọt khí và xung điện, thường xuyên tạo ra các gai tín hiệu giả mạo.
  - Robust Scaling duy trì tính nhận diện của các điểm ngoại lai nhưng triệt tiêu sức ảnh hưởng áp đảo của chúng lên hàm mất mát của mô hình.
- Cân bằng thang đo giữa các biến đặc trưng:
  - Trước khi chuẩn hóa, nồng độ MLSS có độ lớn lên tới $11{,}980\text{ mg/L}$, trong khi tỷ lệ F/M chỉ ở mức $0.012\text{ kgCOD}/(\text{kgMLSS}\cdot\text{d})$.
  - Sự chênh lệch biên độ hàng triệu lần khiến các thuật toán tối ưu hóa dễ bị chi phối sai lệch bởi biến có giá trị tuyệt đối lớn.
  - Sau chuẩn hóa, tất cả biến đều quy tụ về thang đo tương đương với trung vị bằng $0$, giúp các thuật toán học máy hội tụ nhanh và ổn định.
- Tác động thực nghiệm lên hiệu năng mô hình (Trường hợp Case IV dự báo Spec. Flux):
  - Mô hình CatBoost với Robust Scaling đạt hệ số xác định $R^2 = 0.7969$, sai số tuyệt đối trung bình $\text{MAE} = 0.0050$, sai số căn bậc hai trung bình $\text{RMSE} = 0.0060$, sai số phần trăm $\text{MAPE} = 0.1074$.
  - Mô hình XGBoost với Robust Scaling đạt $R^2 = 0.6555$, $\text{MAE} = 0.0059$, $\text{RMSE} = 0.0078$, $\text{MAPE} = 0.1304$.
  - Mô hình Linear Regression và Ridge Regression đạt $R^2 \approx 0.635$, cải thiện đáng kể so với việc sử dụng dữ liệu thô.
  - Mô hình Lasso ($R^2 = -0.0048$) và ElasticNet ($R^2 = 0.2953$) kém hiệu quả do áp đặt phạt trọng số quá mức trên tập biến có tương quan phức tạp.

#### 2.3.2 Kỹ thuật trung bình trượt theo thời gian (Moving Average)
- Cơ chế trễ thời gian (Time Delay) trong hệ thống MBR thực tế:
  - Quá trình phân hủy chất ô nhiễm sinh học và sự tích lũy trở lực lọc không diễn ra tức thời.
  - Luôn tồn tại độ trễ động học giữa biến đổi chất lượng dòng vào, hoạt tính sinh khối trong bể và sự suy giảm lưu lượng lọc tại bề mặt màng.
  - Khái niệm độ trễ thời gian áp dụng trong nghiên cứu là một phương pháp kỹ thuật đặc trưng định hướng dữ liệu (Data-Driven Feature Engineering).
  - Phương pháp này nhằm tối ưu hóa sự bắt cặp dữ liệu đầu vào - đầu ra cho quá trình huấn luyện mô hình, không nhằm đại diện trực tiếp cho thời gian lưu thủy lực (HRT) hay độ trễ vật lý thuần túy.
- Cơ chế tích lũy màng sinh học và hình thành bánh cặn:
  - Hiện tượng nghẹt màng tiến triển dần theo thời gian thông qua sự tích lũy lâu dài của điều kiện vận hành và sinh khối vi sinh.
  - Các phép đo điểm đơn lẻ tại một thời điểm không thể phản ánh toàn bộ lịch sử chịu tải của màng lọc.
- Công thức toán học của kỹ thuật trung bình trượt (Moving Average):
  $$\text{MA}_t = \frac{x_{n-t+1} + x_{n-t+2} + \dots + x_n}{t} = \frac{1}{t} \sum_{i=n-t+1}^{n} x_i$$
  Biểu diễn theo cửa sổ trượt quá khứ kích thước $k$ ngày cho quan sát tại thời điểm $t$:
  $$\overline{X}_k(t) = \frac{1}{k} \sum_{j=0}^{k-1} x(t - j)$$
- Chức năng lọc nhiễu và làm mịn tín hiệu tần số cao:
  - Dữ liệu chất lượng nước và thông số vận hành hiện trường thường có dao động ngắn hạn ngẫu nhiên do sai số thiết bị đo.
  - Trung bình trượt loại bỏ các xung nhiễu tần số cao, trích xuất xu thế dài hạn và giữ lại các tín hiệu động học thực chất của hệ thống.
- Quy trình tối ưu hóa kích thước cửa sổ trượt:
  - Nghiên cứu đánh giá có hệ thống các khoảng dịch chuyển thời gian từ 1 ngày đến 7 ngày (trong phạm vi một tuần) cho từng biến đặc trưng đầu vào.
  - Hiệu năng của các mô hình dự báo ($R^2$ và RMSE) được so sánh định lượng qua từng kích thước cửa sổ.
  - Cửa sổ trượt 5 ngày ($\text{MA}_5$) cho kết quả tối ưu nhất trên toàn bộ các chỉ số kiểm định.
- Bằng chứng thực nghiệm vượt trội khi tích hợp $\text{MA}_5$ kết hợp Robust Scaling (Case IV):
  - CatBoost nâng hệ số xác định từ $R^2 = 0.7969$ lên $R^2 = 0.8374$ (cải thiện hơn $10\%$ so với mô hình dữ liệu thô ban đầu).
  - Sai số căn bậc hai trung bình của CatBoost giảm mạnh xuống $\text{RMSE} = 0.0054$, $\text{MAE} = 0.0042$, và $\text{MAPE} = 0.0863$.
  - XGBoost tăng vọt độ chính xác từ $R^2 = 0.6555$ lên $R^2 = 0.7404$, $\text{RMSE} = 0.0068$, $\text{MAE} = 0.0055$, $\text{MAPE} = 0.1168$.
  - Hồi quy tuyến tính Linear Regression đạt $R^2 = 0.6623$ ($\text{RMSE} = 0.0078$), Ridge Regression đạt $R^2 = 0.6617$ ($\text{RMSE} = 0.0078$).
  - ElasticNet tăng nhẹ lên $R^2 = 0.3145$, trong khi Lasso duy trì ở mức $R^2 = -0.0048$.
- Khẳng định giá trị thực tiễn:
  - Tích hợp chuỗi thời gian trượt nắm bắt chính xác tác động lũy tích của lịch sử vận hành lên động lực học nghẹt màng.
  - Đây là nền tảng cốt lõi giúp các mô hình học máy nâng cao độ tin cậy và khả năng dự báo sớm trong các trạm MBR công nghiệp thực tế.
