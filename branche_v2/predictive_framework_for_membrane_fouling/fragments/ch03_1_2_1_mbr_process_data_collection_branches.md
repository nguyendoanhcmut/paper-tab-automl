## 2.1. MBR Process (Data Collection)

- Quy trình xử lý nước thải chế biến thực phẩm quy mô thực tế (full-scale food processing wastewater treatment process) tại Bắc Kinh và hệ thống MBR làm trọng tâm thu thập dữ liệu (Figure 1):
  - **Hình 1.** Sơ đồ quy trình công nghệ xử lý nước thải và hệ thống MBR
    - <img src="assets/fig_01_p6.jpeg" alt="Figure 1a" />
    - <img src="assets/fig_02_p6.png" alt="Figure 1b" />
    - **Hình này chứng minh điều gì**
      - Chuỗi công nghệ xử lý hoàn chỉnh và vị trí các điểm đo thông số vận hành, chất lượng nước phục vụ mô hình hóa AI.
    - **Từ đâu mà thấy được**
      - Sơ đồ liên hoàn các đơn vị xử lý và ký hiệu chữ màu đỏ tại các vị trí thu thập dữ liệu trên cụm MBR.
  - Chuỗi công nghệ xử lý gồm bể lắng (settling tank), bể chắn rác (grate tank), bể điều hòa (equalization tank), hai bể phản ứng vi hiếu khí nối tiếp (two sequential micro-aerobic reactors: reactor 1 và reactor 2), hệ thống bể phản ứng sinh học màng (membrane bioreactor - MBR), bể chứa nước đầu ra (effluent tank) và đường tuần hoàn bùn (sludge return) từ MBR về bể vi hiếu khí 1.
  - Khung phân tích và dự đoán tắc nghẽn màng bằng AI (AI-driven fouling analytic and predictive framework) được phát triển dựa trên dữ liệu liên quan trực tiếp đến quy trình MBR, không mô tả chi tiết các đơn vị xử lý khác trong chuỗi công nghệ.
  - Vị trí đo đạc và các thông số vận hành cùng chất lượng nước phục vụ mô hình hóa được biểu diễn bằng chữ màu đỏ tại các điểm thu thập tương ứng trên sơ đồ (Figure 1).
  - Toàn bộ dữ liệu nghiên cứu được biên soạn từ các hoạt động vận hành thực địa thường nhật (routine field operations) dưới điều kiện thực tế (real-world conditions), không xuất phát từ kịch bản phòng thí nghiệm hay các thiết lập thử nghiệm chuyên biệt, bảo đảm tính thực tiễn và khả năng ứng dụng cho mô hình dự đoán trên hệ thống MBR quy mô công nghiệp.
- Cấu tạo và đặc tính kỹ thuật của cụm màng sợi rỗng MBR:
  - Hệ thống MBR sử dụng các mô-đun màng sợi rỗng nhúng polyethylene (polyethylene-embedded hollow fiber membranes) với kích thước lỗ lọc nhỏ hơn $0{,}4\text{ }\mu\text{m}$.
  - Sợi màng có đường kính trong là $0{,}41\text{ mm}$ và đường kính ngoài là $0{,}65\text{ mm}$.
  - Độ giãn dài cực đại trước khi đứt gãy (elongation rate - biến dạng tối đa màng sợi rỗng có thể chịu đựng trước khi hỏng) đạt mức dưới $17\%$.
  - Diện tích bề mặt lọc của một nhóm màng đơn lẻ (filtrable surface area of a single membrane group) đạt $200{,}7\text{ m}^2$.
  - Tổng số nhóm màng đưa vào vận hành thực tế là $9\text{ nhóm màng}$ (tổng diện tích bề mặt lọc khả dụng đạt $1806{,}3\text{ m}^2$).
  - Các thành phần cốt lõi của hệ thống MBR bao gồm mô-đun màng (membrane module), hệ thống cấp nước vào và thu nước ra (influent and effluent systems), hệ thống sục khí (aeration system), và hệ thống tuần hoàn (recirculation system).
- Thông số vận hành thủy lực và kiểm soát sinh học của hệ thống MBR:
  - Công suất xử lý nước thải thiết kế của hệ thống MBR đạt $150\text{ m}^3/\text{d}$, đáp ứng yêu cầu xử lý của nhà máy chế biến thực phẩm.
  - Lưu lượng dòng vào trung bình (average influent flow rate) thực tế tới hệ thống MBR là $114\text{ m}^3/\text{d}$.
  - Thời gian lưu nước thủy lực (hydraulic retention time - HRT) của hệ thống đạt xấp xỉ $0{,}75\text{ ngày}$.
  - Nồng độ oxy hòa tan (dissolved oxygen - DO) duy trì ở mức $5{,}43\text{ mg/L}$.
  - Nồng độ chất rắn lơ lửng trong bùn hoạt tính (mixed liquor suspended solids - MLSS) dao động trong khoảng từ $5000\text{ mg/L}$ đến $9000\text{ mg/L}$.
  - Hệ thống duy trì nồng độ MLSS ổn định và không tiến hành xả bùn chủ đích (no intentional sludge wasting) trong suốt giai đoạn theo dõi.
  - Thời gian lưu bùn (solid retention time - SRT) không được kiểm soát hay ghi nhận tường minh (not explicitly controlled or recorded) do không áp dụng xả bùn có chủ ý.
- Chế độ lọc gián đoạn và kiểm soát ngưỡng làm sạch màng:
  - Nước sau xử lý được hút lọc gián đoạn qua màng bằng hệ thống bơm (intermittent filtration), vận hành theo chu kỳ $10\text{ phút}$ hút lọc và $5\text{ phút}$ nghỉ ($10\text{ min on}$ và $5\text{ min off}$).
  - Chu kỳ làm sạch màng (membrane cleaning cycle) được kích hoạt theo kế hoạch khi áp suất xuyên màng (transmembrane pressure - TMP) tăng hơn $30\%$ so với đường cơ sở (baseline value), hoặc khi TMP vượt ngưỡng $60\text{ kPa}$, phù hợp với thực hành vận hành MBR đặt ngập tiêu chuẩn.
  - Không có bất kỳ sự kiện làm sạch hóa chất nào xảy ra—kể cả rửa ngược tăng cường hóa chất (chemical-enhanced backwash - CEB) hay làm sạch tại chỗ (cleaning in place - CIP)—trong suốt chu kỳ theo dõi $194\text{ ngày}$ do TMP chưa từng vượt các ngưỡng làm sạch quy định.
  - Khung mô hình hóa dự đoán không đưa các dữ liệu liên quan đến sự kiện làm sạch hóa chất vào danh sách biến số đầu vào.
- Phương pháp phân tích mẫu và thiết bị đo đạc các chỉ tiêu chất lượng nước:
  - Mẫu bùn hoạt tính từ bể phản ứng MBR được lọc qua màng cellulose hỗn hợp $0{,}45\text{ }\mu\text{m}$ (Advantec, Tokyo, Japan) để phân tích nhu cầu oxy hóa học (chemical oxygen demand - COD) theo tiêu chuẩn Standard Methods for the Examination of Water and Wastewater của APHA.
  - Nồng độ COD trước và sau xử lý ($\text{COD}_{\text{in}}$ và $\text{COD}_{\text{out}}$) được đo bằng máy đo COD chuyên dụng (DR1010, HACH, Loveland, CO, USA).
  - Độ pH và nhiệt độ ($\text{Temp.}$) được phân tích định lượng bằng điện cực đa năng cầm tay (Multi 3630, Munich, Germany) tích hợp mạng phối hợp đo.
  - Nồng độ oxy hòa tan (DO) được đo bằng đồng hồ đo đa năng cầm tay (PHB-4, Zsynet, Shanghai, China).
  - Nồng độ MLSS được xác định bằng phương pháp khối lượng (gravimetric method).
  - Áp suất xuyên màng (TMP) và lưu lượng (flow rate) được theo dõi và ghi nhận hàng ngày qua các đồng hồ đo áp suất (pressure gauges) và lưu lượng kế (flow meters) kết nối trực tiếp với hệ thống MBR.
  - Thể tích bùn lắng sau 30 phút (SV30), chỉ số thể tích bùn (sludge volume index - SVI), tỷ số thức ăn trên vi sinh vật (food-to-microorganism ratio - F/M), và thông lượng màng (flux) được phân tích theo các phương pháp chuẩn.
- Giao thức thu thập dữ liệu hàng ngày và phương pháp xử lý biến đổi chuỗi thời gian:
  - Toàn bộ các phép đo được thu thập liên tục hàng ngày trong suốt thời gian $194\text{ ngày}$, tạo lập tập dữ liệu đầy đủ cho việc huấn luyện và kiểm định mô hình.
  - Các tham số phân tích thủ công gồm $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$ và $\text{COD}$ được đo một lần mỗi ngày và ghi nhận thành các điểm dữ liệu ngày (daily data points).
  - Các biến số theo dõi trực tuyến bằng cảm biến liên tục gồm $\text{DO}$, $\text{pH}$, nhiệt độ ($\text{Temp.}$), $\text{TMP}$ và lưu lượng (flow rate) được xử lý thành các giá trị trung bình ngày (daily average values) nhằm bảo đảm tính đồng nhất và khả năng so sánh trên toàn bộ tập dữ liệu.
  - Quy trình thu thập dữ liệu chịu giới hạn thực địa của hệ thống vận hành thực tế, trong đó phương thức lấy mẫu thủ công và giới hạn kỹ thuật của cảm biến hạn chế khả năng ghi nhận dữ liệu tần suất cao.
  - Dữ liệu trung bình ngày có thể làm che khuất các dao động ngắn hạn của động học tắc nghẽn màng; vì vậy phép biến đổi trung bình trượt (moving average transformation, trình bày tại Mục 2.3.2) đã được áp dụng lên các đặc trưng chính nhằm nắm bắt tương quan thời gian và hạn chế sự suy giảm xu hướng chuỗi dữ liệu.
  - Phân tích trực quan hóa biến động nội ngày (intra-day trends) được định hướng mở rộng khi có sẵn nguồn dữ liệu tần suất cao trong các nghiên cứu tiếp theo.
- Thiết lập biến mục tiêu dự đoán dựa trên động lực học màng:
  - Biến mục tiêu của khung mô hình được xác định là áp suất xuyên màng ($\text{TMP}$) hoặc thông lượng riêng ($\text{Spec. Flux}$).
  - Thông lượng riêng ($\text{Spec. Flux}$) được tính bằng công thức:
    $$\text{Spec. Flux} = \frac{\text{flux}}{\text{TMP}}$$
  - Thông lượng riêng đại diện trực tiếp cho độ thấm của màng (membrane permeability), là chỉ số then chốt định lượng mức độ nghiêm trọng của hiện tượng tắc nghẽn màng (fouling severity).
  - Trong vận hành MBR thực tế, ngay cả ở chế độ thông lượng không đổi (constant flux mode), cả flux và TMP đều liên tục thay đổi do dao động vận hành và điều kiện môi trường; do đó $\text{Spec. Flux}$ phản ánh đồng thời các biến đổi này hiệu quả hơn so với việc chỉ sử dụng từng tham số đơn lẻ, trở thành chỉ số mang tính thực tế và mạnh mẽ (robust) cho mô hình hóa dự đoán.
  - Giữa TMP và Spec. Flux tồn tại mối quan hệ nghịch đảo theo cơ chế tắc nghẽn: khi tắc nghẽn màng gia tăng ở một mức flux cho trước, TMP tăng lên dẫn tới sự suy giảm của Spec. Flux ($\text{TMP} \uparrow \implies \text{Spec. Flux} \downarrow$).
- Thiết lập các trường hợp thử nghiệm so sánh mô hình (Table 1):
  - Bốn kịch bản thử nghiệm được xây dựng nhằm so sánh hiệu năng mô hình một cách có hệ thống, dựa trên việc đưa vào hay loại trừ hiệu suất loại bỏ COD ($\text{COD RM}$ - COD removal efficiency) cùng với sự lựa chọn tham số mục tiêu ($\text{TMP}$ hoặc $\text{Spec. Flux}$) (Table 1):
    - Trường hợp I (Case I): Sử dụng 7 yếu tố vận hành cơ bản ($\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$); biến mục tiêu là $\text{TMP}$.
    - Trường hợp II (Case II): Sử dụng 7 yếu tố cơ bản bổ sung hiệu suất loại bỏ COD ($\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM}$); biến mục tiêu là $\text{TMP}$.
    - Trường hợp III (Case III): Sử dụng 7 yếu tố cơ bản ($\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$); biến mục tiêu là $\text{Spec. Flux}$.
    - Trường hợp IV (Case IV): Sử dụng 7 yếu tố cơ bản bổ sung $\text{COD RM}$ ($\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM}$); biến mục tiêu là $\text{Spec. Flux}$.

| Cases | Factors | Target |
| :--- | :--- | :--- |
| Case I | $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$ | $\text{TMP}$ |
| Case II | $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM}$ | $\text{TMP}$ |
| Case III | $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$ | $\text{Spec. Flux}$ |
| Case IV | $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSS}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM}$ | $\text{Spec. Flux}$ |
