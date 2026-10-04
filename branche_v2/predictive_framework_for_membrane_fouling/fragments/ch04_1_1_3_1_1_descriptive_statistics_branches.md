#### 3.1.1. Descriptive Statistics

- Phân tích thống kê mô tả (descriptive statistical analysis) tóm tắt xu hướng tập trung (central tendency), độ phân tán (dispersion) và phân phối tổng thể (overall distribution) của tập dữ liệu gồm $194$ mẫu quan trắc từ quy trình bể phản ứng sinh học màng (MBR - membrane bioreactor) (Bảng 2 / Table 2):
  - Bảng 2 tóm tắt các giá trị thống kê mô tả cho $11$ thông số quy trình MBR bao gồm số lượng mẫu (Count: $194$), trung bình (Mean), độ lệch chuẩn (Std), giá trị nhỏ nhất (Min), phân vị $25\%$, trung vị $50\%$, phân vị $75\%$ và giá trị lớn nhất (Max):

| Thông số (Features) | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\text{F/M}\ (\text{kgCOD/(kgMLSS}\cdot\text{d)})$ | $194$ | $0.012$ | $0.004$ | $0.003$ | $0.009$ | $0.011$ | $0.014$ | $0.024$ |
| $\text{SV30}\ (\%)$ | $194$ | $95.8$ | $8.9$ | $30.0$ | $96.0$ | $98.0$ | $99.0$ | $99.0$ |
| $\text{SVI}\ (\text{mL/g})$ | $194$ | $125.1$ | $18.9$ | $82.6$ | $112.5$ | $122.4$ | $135.0$ | $182.7$ |
| $\text{MLSS}\ (\text{mg/L})$ | $194$ | $7813$ | $1361$ | $3390$ | $7080$ | $7900$ | $8628$ | $11{,}980$ |
| $\text{DO}\ (\text{mg/L})$ | $194$ | $5.43$ | $0.79$ | $3.62$ | $4.90$ | $5.30$ | $5.98$ | $7.55$ |
| $\text{pH}$ | $194$ | $8.11$ | $0.40$ | $5.02$ | $7.85$ | $7.98$ | $8.45$ | $8.97$ |
| $\text{Temp}\ (^\circ\text{C})$ | $194$ | $26.4$ | $4.5$ | $13.0$ | $25.0$ | $28.3$ | $29.7$ | $31.6$ |
| $\text{Flux}\ (\text{LMH})$ | $194$ | $2.65$ | $0.52$ | $0.60$ | $2.45$ | $2.73$ | $2.92$ | $3.87$ |
| $\text{COD RM}\ (\%)$ | $194$ | $64.7$ | $16.9$ | $18.7$ | $56.4$ | $70.8$ | $76.6$ | $87.6$ |
| $\text{TMP}\ (\text{kPa})$ | $194$ | $51.0$ | $6.8$ | $37.08$ | $46.3$ | $50.5$ | $55.0$ | $69.0$ |
| $\text{Spec. Flux}\ (\text{LMH/kPa})$ | $194$ | $0.053$ | $0.013$ | $0.012$ | $0.046$ | $0.055$ | $0.062$ | $0.099$ |

- Hỗn hợp chất rắn lơ lửng trong bùn hoạt tính ($\text{MLSS}$ - mixed liquor suspended solids) thể hiện mức độ biến động lớn nhất trong số các đặc trưng đầu vào (input features):
  - Giá trị trung bình của $\text{MLSS}$ đạt $7813\text{ mg/L}$ với độ lệch chuẩn là $1361\text{ mg/L}$.
  - Giá trị nhỏ nhất ($\text{Min}$) và lớn nhất ($\text{Max}$) của $\text{MLSS}$ lần lượt là $3390\text{ mg/L}$ và $11{,}980\text{ mg/L}$ ($11,980\text{ mg/L}$).
  - Các phân vị của $\text{MLSS}$ theo Bảng 2 đạt $7080\text{ mg/L}$ (phân vị $25\%$), $7900\text{ mg/L}$ (phân vị $50\%$, trung vị) và $8628\text{ mg/L}$ (phân vị $75\%$).
  - Sự dao động biên độ lớn của $\text{MLSS}$ trong quy trình MBR chịu ảnh hưởng từ các biến động của đặc tính nước thải đầu vào (influent characteristics) và hoạt tính vi sinh vật (microbial activity), tác động trực tiếp đến tốc độ nghẹt màng (membrane fouling rates).
- Nồng độ oxy hòa tan ($\text{DO}$ - dissolved oxygen) duy trì trong dải tương đối hẹp, phản ánh điều kiện sục khí ổn định bảo đảm cung cấp đủ oxy cho các quá trình sinh học trong bể MBR:
  - Nồng độ $\text{DO}$ dao động từ $3.62\text{ mg/L}$ đến $7.55\text{ mg/L}$, với giá trị trung bình là $5.43\text{ mg/L}$ và độ lệch chuẩn là $0.79\text{ mg/L}$.
  - Các giá trị phân vị ($25\%$, $50\%$ và $75\%$) lần lượt là $4.90\text{ mg/L}$, $5.30\text{ mg/L}$ và $5.98\text{ mg/L}$.
  - Phần lớn các quan trắc tập trung trong khoảng hẹp thể hiện các điều kiện sục khí (aeration conditions) duy trì ổn định, bảo đảm lượng oxy khả dụng cho quá trình sinh học.
- Độ $\text{pH}$ duy trì trạng thái tương đối ổn định với độ biến động ở mức tối thiểu nhằm bảo đảm môi trường kiểm soát ổn định cho hoạt tính vi sinh vật và độ bền của màng:
  - Giá trị $\text{pH}$ trung bình đạt $8.11$ với độ lệch chuẩn là $0.39$ trong phân tích văn bản (Bảng 2 ghi độ lệch chuẩn là $0.40$).
  - Khoảng giá trị $\text{pH}$ ghi nhận trải dài từ $5.02$ đến $8.97$.
  - Các phân vị thứ $25$, $50$ (trung vị - median) và $75$ lần lượt đạt $7.85$, $7.98$ và $8.45$.
  - Môi trường $\text{pH}$ được kiểm soát chặt chẽ có vai trò quyết định đối với hoạt tính vi sinh vật và độ ổn định của màng lọc (membrane stability).
- Nhiệt độ quy trình ($\text{Temp}$ - temperature) biến thiên trong phạm vi vừa phải, có thể ảnh hưởng đến hoạt tính vi sinh vật nhạy cảm với nhiệt độ và hiệu quả của hệ thống:
  - Nhiệt độ bể MBR biến thiên giữa $13.0^\circ\text{C}$ và $31.6^\circ\text{C}$, với giá trị trung bình là $26.4^\circ\text{C}$ và độ lệch chuẩn là $4.5^\circ\text{C}$.
  - Các giá trị phân vị ($25\%$, $50\%$ và $75\%$) lần lượt là $25.0^\circ\text{C}$, $28.3^\circ\text{C}$ và $29.7^\circ\text{C}$.
  - Do các quá trình sinh học trong MBR rất nhạy cảm với nhiệt độ, sự dao động nhiệt này có khả năng chi phối hoạt tính vi sinh và hiệu suất chung của hệ thống.
- Tỷ lệ chất dinh dưỡng trên vi sinh vật ($F/M$ - food-to-microorganism ratio) thể hiện mức độ biến thiên tương đối thấp, giữ điều kiện tải lượng hữu cơ ổn định:
  - Giá trị $F/M$ trung bình đạt $0.012\text{ kgCOD/(kgMLSS}\cdot\text{d)}$ với độ lệch chuẩn là $0.004\text{ kgCOD/(kgMLSS}\cdot\text{d)}$.
  - Khoảng giá trị biến thiên từ $0.003\text{ kgCOD/(kgMLSS}\cdot\text{d)}$ đến $0.024\text{ kgCOD/(kgMLSS}\cdot\text{d)}$.
  - Các giá trị phân vị thứ $25$, $50$ (trung vị) và $75$ lần lượt là $0.009\text{ kgCOD/(kgMLSS}\cdot\text{d)}$, $0.011\text{ kgCOD/(kgMLSS}\cdot\text{d)}$ và $0.014\text{ kgCOD/(kgMLSS}\cdot\text{d)}$.
  - Tải lượng hữu cơ (organic loading conditions) duy trì ổn định xuyên suốt thời gian nghiên cứu, bảo đảm phản ứng vi sinh vật diễn ra nhất quán trong hệ thống.
- Chỉ số thể tích bùn ($\text{SVI}$ - sludge volume index) phản ánh mức biến động vừa phải về khả năng lắng của bùn hoạt tính:
  - Giá trị $\text{SVI}$ dao động từ $82.6\text{ mL/g}$ đến $182.7\text{ mL/g}$, với giá trị trung bình là $125.1\text{ mL/g}$ và độ lệch chuẩn là $18.9\text{ mL/g}$.
  - Các giá trị phân vị tứ phân lần lượt là $112.5\text{ mL/g}$ (phân vị $25\%$), $122.4\text{ mL/g}$ (phân vị $50\%$) và $135.0\text{ mL/g}$ (phân vị $75\%$).
  - Là thông số then chốt đánh giá đặc tính lắng của bùn (sludge settling characteristics), dải biến động này phản ánh độ lắng bùn (sludge settleability) của hệ thống trải qua mức độ dao động vừa phải.
- Thể tích bùn lắng sau $30$ phút ($SV30$) và hiệu suất loại bỏ $\text{COD}$ ($COD\ RM$) bổ sung đánh giá trạng thái bùn và xử lý cơ chất hữu cơ:
  - Thể tích bùn lắng $SV30$ đạt giá trị trung bình $95.8\%$ với độ lệch chuẩn $8.9\%$, giá trị nhỏ nhất $30.0\%$, giá trị lớn nhất $99.0\%$, và các phân vị $25\%$, $50\%$, $75\%$ lần lượt là $96.0\%$, $98.0\%$ và $99.0\%$.
  - Hiệu suất loại bỏ chất hữu cơ $COD\ RM$ đạt giá trị trung bình $64.7\%$ với độ lệch chuẩn $16.9\%$, giá trị nhỏ nhất $18.7\%$, giá trị lớn nhất $87.6\%$, và các phân vị $25\%$, $50\%$, $75\%$ tương ứng là $56.4\%$, $70.8\%$ và $76.6\%$.
- Áp suất xuyên màng ($\text{TMP}$ - transmembrane pressure), thông số đo lường nghẹt màng cốt lõi trong các biến mục tiêu, phản ánh hệ thống màng chịu mức độ nghẹt vừa phải:
  - Giá trị $\text{TMP}$ dao động từ $37.0\text{ kPa}$ (Bảng 2 ghi giá trị nhỏ nhất là $37.08\text{ kPa}$) đến $69.0\text{ kPa}$, với giá trị trung bình là $51.0\text{ kPa}$ và độ lệch chuẩn là $6.8\text{ kPa}$.
  - Các phân vị thứ $25$, $50$ (trung vị) và $75$ lần lượt là $46.3\text{ kPa}$, $50.5\text{ kPa}$ và $55.0\text{ kPa}$.
  - Mức độ nghẹt màng trong hệ thống ở mức vừa phải với các dao động chu kỳ có thể do sự thay đổi của điều kiện nước đầu vào hoặc các điều chỉnh quy trình vận hành.
- Thông lượng lọc ($\text{Flux}$), đại diện cho tốc độ lọc của màng, thể hiện mức biến thiên vừa phải về hiệu suất lọc qua màng:
  - Thông lượng lọc trung bình đạt $2.65\text{ LMH}$ (tức $\text{L/(m}^2\cdot\text{h)}$ hoặc $\text{L/m2·h}$) với độ lệch chuẩn là $0.52\text{ LMH}$.
  - Dải giá trị $\text{Flux}$ trải rộng từ $0.60\text{ LMH}$ đến $3.87\text{ LMH}$.
  - Các giá trị phân vị ($25\%$, $50\%$ và $75\%$) lần lượt là $2.45\text{ LMH}$, $2.73\text{ LMH}$ và $2.92\text{ LMH}$.
- Thông lượng riêng ($\text{Spec. Flux}$), chỉ số chuẩn hóa thông lượng lọc theo áp suất xuyên màng $\text{TMP}$, thể hiện hiệu quả lọc tương đối ổn định giữa các điều kiện vận hành khác nhau:
  - Giá trị $\text{Spec. Flux}$ trung bình đạt $0.053\text{ LMH/kPa}$ với độ lệch chuẩn là $0.013\text{ LMH/kPa}$.
  - Khoảng giá trị biến thiên từ $0.012\text{ LMH/kPa}$ đến $0.099\text{ LMH/kPa}$.
  - Các phân vị thứ $25$, $50$ và $75$ lần lượt đạt $0.046\text{ LMH/kPa}$, $0.055\text{ LMH/kPa}$ và $0.062\text{ LMH/kPa}$.
- Ý nghĩa phân tích và định hướng ứng dụng thực tiễn của thống kê mô tả đối với kiểm soát quy trình và mô hình hóa dự đoán:
  - Cung cấp hiểu biết rõ ràng về độ biến thiên của các thông số vận hành chủ chốt trong quy trình MBR, cho phép đánh giá ban đầu về tác động tiềm tàng của chúng đối với hiện tượng nghẹt màng và hiệu suất lọc.
  - Thiết lập cơ sở nền tảng cho phân tích tương quan (correlation analysis) và phát triển mô hình dự đoán (predictive modeling) tiếp theo nhằm nhận diện các yếu tố chính chi phối quá trình nghẹt màng.
  - Định hướng xây dựng các chiến lược tối ưu hóa trong kiểm soát quy trình và cải tiến vận hành, nâng cao hiệu quả tổng thể và tính bền vững của hệ thống xử lý.
