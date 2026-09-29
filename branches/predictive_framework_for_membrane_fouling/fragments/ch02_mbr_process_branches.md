## 2.1. Quy trình MBR và Thu thập Dữ liệu (MBR Process and Data Collection)

### 2.1.1. Cấu hình Kỹ thuật và Quy trình Xử lý Nước thải Thực phẩm

#### 2.1.1.1. Sơ đồ chuỗi công nghệ và ranh giới mô hình hóa
- Vị trí địa lý và quy mô: Hệ thống xử lý nước thải chế biến thực phẩm quy mô thực địa (Full-Scale MBR) vận hành tại Bắc Kinh, Trung Quốc.
- Chuỗi quy trình đơn vị: Dây chuyền xử lý nước thải gồm bể lắng, bể song chắn rác, bể điều hòa, hai bể vi hiếu khí nối tiếp, bể phản ứng sinh học màng (MBR) và bể chứa nước sau xử lý.
- Vị trí quan trắc và thu thập dữ liệu: Dữ liệu vận hành và chất lượng nước được ghi nhận tại dòng vào, dòng ra và trực tiếp trong ngăn màng MBR.
- Ranh giới mô hình hóa AI: Khung phân tích AI chỉ sử dụng dữ liệu vận hành từ hệ thống MBR. Nghiên cứu lược bỏ mô hình hóa chi tiết cho các bể tiền xử lý để bảo đảm sự tập trung vào cơ chế tắc nghẽn màng.
- Bản chất dữ liệu thực địa: Toàn bộ dữ liệu thu thập trực tiếp từ chu kỳ vận hành thường nhật trong điều kiện sản xuất thực tế. Bộ dữ liệu không bắt nguồn từ môi trường phòng thí nghiệm hay các kịch bản nhân tạo.

#### 2.1.1.2. Thông số kỹ thuật module màng sợi rỗng chìm
- Công suất xử lý thiết kế: Hệ thống MBR đạt công suất thiết kế $150\text{ m}^3/\text{ngày}$, đáp ứng yêu cầu xử lý của nhà máy chế biến thực phẩm.
- Lưu lượng nạp thực tế: Lưu lượng nạp trung bình vào hệ thống màng duy trì ở mức $114\text{ m}^3/\text{ngày}$.
- Thời gian lưu nước thủy lực (HRT): Giá trị HRT trung bình của bể MBR xấp xỉ $0.75\text{ ngày}$ ($\approx 18\text{ giờ}$).
- Cấu tạo vật liệu màng lọc: Màng sợi rỗng ngập nước (submerged hollow fiber) chế tạo từ vật liệu Polyethylene tích hợp.
- Kích thước lỗ màng: Đường kính lỗ màng danh định nhỏ hơn $0.4\ \mu\text{m}$ ($< 0.4\ \mu\text{m}$), giữ lại toàn bộ bùn hoạt tính trong bể sinh học.
- Kích thước hình học sợi màng: Đường kính trong của sợi màng đạt $0.41\text{ mm}$. Đường kính ngoài của sợi màng đạt $0.65\text{ mm}$.
- Giới hạn cơ học: Độ giãn dài cực đại trước khi nứt đứt sợi (elongation rate) nhỏ hơn $17\%$.
- Diện tích lọc hữu hiệu: Mỗi cụm màng có diện tích bề mặt lọc danh định là $200.7\text{ m}^2$. Hệ thống vận hành đồng thời $9\text{ cụm màng}$, tạo tổng diện tích màng hoạt động đạt $1806.3\text{ m}^2$.
- Cấu phần phụ trợ: Module màng tích hợp hệ thống đường ống thu nước sau lọc, dàn sục khí xáo trộn đáy và bơm tuần hoàn bùn.

#### 2.1.1.3. Chế độ vận hành thủy lực và kiểm soát làm sạch màng
- Chu kỳ hút lọc gián đoạn: Bơm hút dịch lọc hoạt động theo chu kỳ ngắt quãng gồm $10\text{ phút chạy}$ (on) và $5\text{ phút nghỉ}$ (off). Chế độ ngắt quãng này giải phóng áp lực hút và giảm thiểu mật độ bám dính của bánh bùn.
- Ngưỡng kiểm soát rửa màng: Quy trình làm sạch màng được kích hoạt khi áp suất xuyên màng TMP tăng trên $30\%$ so với đường nền hoặc khi vượt ngưỡng an toàn $60\text{ kPa}$.
- Trạng thái rửa hóa chất thực tế: Trong suốt $194\text{ ngày}$ giám sát, hệ thống không thực hiện các quy trình rửa hóa chất như rửa ngược tăng cường hóa chất (CEB) hay làm sạch tại chỗ (CIP).
- Nguyên nhân không rửa hóa chất: Giá trị TMP thực tế không chạm ngưỡng kích hoạt $60\text{ kPa}$.
- Ảnh hưởng đến mô hình hóa: Khung mô hình học máy loại bỏ các biến số liên quan đến can thiệp hóa chất ra khỏi tập đặc trưng đầu vào.

### 2.1.2. Tập Dữ liệu Thực địa 194 Ngày và Thiết bị Quan trắc

#### 2.1.2.1. Đặc điểm dữ liệu vận hành thực địa
- Thời lượng quan trắc: Tập dữ liệu thực địa ghi nhận liên tục trong $194\text{ ngày}$ vận hành thực tế.
- Điều kiện dao động thực tế: Số liệu phản ánh sự biến đổi tự nhiên của thành phần nước thải công nghiệp và nhiệt độ môi trường.
- Tính ứng dụng: Bộ dữ liệu bảo đảm tính tương thích thực tiễn cho việc phát triển mô hình dự báo tắc nghẽn trong các trạm xử lý quy mô lớn.

#### 2.1.2.2. Danh mục thiết bị đo kiểm và phương pháp phân tích chuẩn
- Phân tích nồng độ COD: Mẫu bùn lỏng lọc qua màng mixed cellulose $0.45\ \mu\text{m}$ (Advantec, Tokyo, Nhật Bản) trước khi đo. Quy trình đo tuân thủ Hướng dẫn Tiêu chuẩn APHA.
- Thiết bị quang phổ COD: Nồng độ COD dòng vào và dòng ra đo bằng máy so màu DR1010 (HACH, Loveland, CO, Hoa Kỳ).
- Đo pH và Nhiệt độ: Đo lường bằng điện cực đa năng cầm tay Multi 3630 (WTW, Munich, Đức) kèm mạng phối hợp tín hiệu.
- Đo Oxy hòa tan (DO): Nồng độ DO trong bể màng đo bằng máy đo đa chỉ tiêu cầm tay PHB-4 (Zsynet, Thượng Hải, Trung Quốc).
- Đo nồng độ bùn MLSS: Nồng độ chất rắn lơ lửng xác định bằng phương pháp khối lượng sấy khô (gravimetric method).
- Giám sát TMP và Lưu lượng: Áp suất xuyên màng TMP và lưu lượng dòng thấm đo liên tục bằng cảm biến áp suất và lưu lượng kế chuyên dụng gắn trên đường ống thu nước.
- Đo đạc chỉ số bùn: Các chỉ số SV30, SVI, tỷ lệ F/M và thông lượng màng Flux phân tích theo tiêu chuẩn ngành nước thải.

#### 2.1.2.3. Quy trình đồng bộ hóa và xử lý tần suất dữ liệu
- Phân loại tần suất lấy mẫu: Các biến thủ công gồm F/M, SV30, SVI, MLSS và COD được phân tích với tần suất $1\text{ lần/ngày}$.
- Đồng bộ biến cảm biến liên tục: Các biến trực tuyến gồm DO, pH, Nhiệt độ, TMP và Lưu lượng được lấy trung bình ngày (daily average).
- Khắc phục giới hạn tần suất: Việc tính giá trị trung bình ngày làm giảm nhiễu tần số cao nhưng có thể làm mờ biến động ngắn hạn. Nghiên cứu sử dụng biến đổi trung bình trượt (Moving Average) tại bước tiền xử lý để bảo toàn thông tin chuỗi thời gian.
- Hướng phát triển tương lai: Thu thập dữ liệu tần số cao trong tương lai sẽ giúp trực quan hóa sâu hơn các pha dao động tắc nghẽn trong ngày.

### 2.1.3. Các Thông số Vận hành và Đặc tính Sinh học Giám sát

#### 2.1.3.1. Các thông số vận hành lý - hóa liên tục
- Nồng độ oxy hòa tan (DO): Nồng độ DO duy trì ở mức trung bình $5.43\text{ mg/L}$, cung cấp đủ dưỡng khí cho vi sinh vật hiếu khí phân giải cơ chất.
- Độ pH môi trường phản ứng: Giá trị pH ổn định giúp duy trì hoạt tính sinh học của màng tế bào và cấu trúc bông bùn.
- Nhiệt độ nước thải (Temp): Nhiệt độ thay đổi theo điều kiện tự nhiên, chi phối độ nhớt động học của nước thải và tốc độ trao đổi chất của vi sinh vật.

#### 2.1.3.2. Đặc tính sinh khối bùn hoạt tính và khả năng lắng
- Dải nồng độ bùn hoạt tính (MLSS): Nồng độ MLSS trong bể duy trì dao động ổn định trong khoảng $5000\text{ mg/L}$ đến $9000\text{ mg/L}$.
- Kiểm soát tuổi bùn (SRT): Trạm xử lý không thực hiện xả bùn có chủ đích (no intentional sludge wasting) trong 194 ngày giám sát.
- Hệ quả đối với biến số SRT: Nồng độ bùn tự cân bằng động, vì vậy thông số SRT không được kiểm soát hay lưu trữ tường minh.
- Thể tích bùn lắng sau 30 phút (SV30): Tỷ lệ thể tích bùn lắng biểu thị dung tích bông bùn chiếm chỗ sau 30 phút lắng tĩnh trong ống đong.
- Chỉ số thể tích bùn (SVI): Thể tích chiếm chỗ của $1\text{ gam}$ bùn khô sau 30 phút lắng tĩnh, phản ánh nguy cơ trương nở bùn và khả năng tạo màng bánh.

#### 2.1.3.3. Tải trọng dinh dưỡng và tương tác sinh học - màng lọc
- Tỷ lệ thức ăn trên vi sinh vật (F/M): Chỉ số đánh giá tải lượng chất nền hữu cơ phân bổ trên một đơn vị khối lượng bùn hoạt tính mỗi ngày.
- Cơ chế gây tắc nghẽn màng: Sự mất cân bằng F/M kích thích vi khuẩn bài tiết chất polyme ngoại bào (EPS) và sản phẩm vi sinh vật hòa tan (SMP). EPS và SMP bám chặt vào bề mặt màng gây suy giảm độ thấm nghiêm trọng.
- Tương tác sinh khối và lực cắt: Nồng độ bùn cao làm gia tăng độ nhớt bùn, đòi hỏi sục khí liên tục để duy trì lực cắt dòng chảy bề mặt màng.

### 2.1.4. Thiết lập Kịch bản Mô hình hóa và Cơ sở Toán học

#### 2.1.4.1. Định nghĩa toán học của biến mục tiêu và biến phái sinh
- Áp suất xuyên màng ($\text{TMP}$): Chênh lệch áp suất thủy lực qua hai phía màng lọc ($\Delta P$), biểu thị bằng đơn vị kilopascal ($\text{kPa}$).
- Thông lượng riêng (Specific Flux - $\text{Spec. Flux}$): Tỷ số giữa thông lượng thấm qua màng và áp suất xuyên màng:
  $$\text{Spec. Flux} = \frac{J}{\Delta P} = \frac{\text{Flux}}{\text{TMP}}$$
  Trong đó:
  - $J$ hay $\text{Flux}$: Thông lượng dòng thấm qua bề mặt màng hữu hiệu ($\text{L}/(\text{m}^2\cdot\text{h})$ hoặc $\text{LMH}$).
  - $\Delta P$ hay $\text{TMP}$: Áp suất xuyên màng thực tế ($\text{kPa}$).
- Hiệu suất loại bỏ COD ($\text{COD RM}$): Tỷ lệ phần trăm loại bỏ nhu cầu oxy hóa học qua hệ thống MBR:
  $$\text{COD RM} = \frac{\text{COD}_{\text{in}} - \text{COD}_{\text{eff}}}{\text{COD}_{\text{in}}} \times 100\%$$
  Trong đó:
  - $\text{COD}_{\text{in}}$: Nồng độ COD của dòng nạp vào bể MBR ($\text{mg/L}$).
  - $\text{COD}_{\text{eff}}$: Nồng độ COD của dòng nước thấm qua màng sau xử lý ($\text{mg/L}$).

#### 2.1.4.2. Cơ chế suy giảm tính thấm và quan hệ nghịch đảo giữa TMP và Specific Flux
- Bản chất vật lý của Specific Flux: Specific Flux đại diện trực tiếp cho độ thấm màng (membrane permeability), là chỉ số định lượng cốt lõi của mức độ tắc nghẽn màng (fouling severity).
- Biến động trong vận hành thực tế: Dù vận hành ở chế độ kiểm soát thông lượng danh định, cả Flux và TMP vẫn biến thiên đồng thời do dao động tải trọng và nhiệt độ.
- Cơ chế quan hệ nghịch đảo: Khi cặn bẩn tích tụ trên bề mặt và trong mao quản màng, lực cản dòng chảy tăng lên. Để duy trì thông lượng, giá trị TMP phải tăng, dẫn đến sự sụt giảm tức thời của Specific Flux:
  $$\text{Tắc nghẽn màng} \uparrow \implies \Delta P\ (\text{TMP}) \uparrow \implies \text{Spec. Flux} \downarrow$$
- Lợi ích của Specific Flux trong mô hình hóa: Specific Flux phản ánh đồng thời cả áp suất và lưu lượng, tạo thành biến mục tiêu có tính đại diện và ổn định hơn TMP đơn lẻ.

#### 2.1.4.3. Cấu trúc 4 kịch bản mô hình hóa (Case I đến Case IV)
- Tiêu chí thiết lập kịch bản: Phân loại dựa trên việc bổ sung biến hiệu suất xử lý sinh học $\text{COD RM}$ và việc chọn lựa biến mục tiêu dự báo ($\text{TMP}$ hoặc $\text{Spec. Flux}$).
- Kịch bản I (Case I):
  - Tập đặc trưng đầu vào (7 biến): F/M, SV30, SVI, MLSS, DO, pH, Nhiệt độ (Temp).
  - Biến mục tiêu: Áp suất xuyên màng ($\text{TMP}$).
  - Mục tiêu: Dự báo áp suất màng thuần túy dựa trên các thông số vận hành lý - hóa và đặc tính bùn cơ bản.
- Kịch bản II (Case II):
  - Tập đặc trưng đầu vào (8 biến): F/M, SV30, SVI, MLSS, DO, pH, Nhiệt độ (Temp), Hiệu suất loại bỏ COD ($\text{COD RM}$).
  - Biến mục tiêu: Áp suất xuyên màng ($\text{TMP}$).
  - Mục tiêu: Khảo sát ảnh hưởng của hiệu suất xử lý hữu cơ $\text{COD RM}$ đối với độ chính xác dự báo TMP.
- Kịch bản III (Case III):
  - Tập đặc trưng đầu vào (7 biến): F/M, SV30, SVI, MLSS, DO, pH, Nhiệt độ (Temp).
  - Biến mục tiêu: Thông lượng riêng ($\text{Spec. Flux}$).
  - Mục tiêu: Dự báo độ thấm màng từ các thông số vận hành cơ bản mà không cần dữ liệu hiệu suất loại bỏ chất hữu cơ.
- Kịch bản IV (Case IV):
  - Tập đặc trưng đầu vào (8 biến): F/M, SV30, SVI, MLSS, DO, pH, Nhiệt độ (Temp), Hiệu suất loại bỏ COD ($\text{COD RM}$).
  - Biến mục tiêu: Thông lượng riêng ($\text{Spec. Flux}$).
  - Mục tiêu: Thiết lập mô hình hoàn chỉnh nhất để dự báo độ thấm màng kết hợp toàn diện thông số vận hành và hiệu suất xử lý sinh học.
- Bảng đối chiếu các kịch bản mô hình hóa (Table 1):
| Kịch bản | Tập đặc trưng đầu vào (Factors) | Biến mục tiêu (Target) | Ý nghĩa mô hình |
| :--- | :--- | :--- | :--- |
| **Case I** | F/M, SV30, SVI, MLSS, DO, pH, Temp | TMP | Mô hình cơ sở dự báo áp lực xuyên màng |
| **Case II** | F/M, SV30, SVI, MLSS, DO, pH, Temp, COD RM | TMP | Mô hình nâng cao dự báo TMP kết hợp hiệu suất COD |
| **Case III** | F/M, SV30, SVI, MLSS, DO, pH, Temp | Spec. Flux | Mô hình cơ sở dự báo độ thấm màng |
| **Case IV** | F/M, SV30, SVI, MLSS, DO, pH, Temp, COD RM | Spec. Flux | Mô hình toàn diện dự báo độ thấm màng kết hợp hiệu suất COD |
