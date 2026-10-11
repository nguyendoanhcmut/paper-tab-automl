### 2.1. Experimental setup

* Quá trình xử lý lọc MBR (Membrane Bioreactor) được tiến hành ở quy mô pilot với thể tích làm việc $30\text{ L}$.
* Mẫu nước thải được thu thập từ hồ cuối (final pond) của trạm xử lý, có nhu cầu oxy sinh hóa (biochemical oxygen demand - BOD) dưới $10.000\text{ mg}\cdot\text{L}^{-1}$, nhằm kích thích hiện tượng tắc nghẽn màng (fouling) trong quá trình lọc SMBR (Submerged MBR).
* Hệ thống được trang bị một bể phản ứng sinh học đơn (single bioreactor tank) chứa các màng sợi rỗng ngập nước (submerged hollow fibre membranes).
  * Màng sợi rỗng được chế tạo từ polyethersulfone (PES), có kích thước lỗ màng khoảng $80$–$100\text{ kDa}$ và diện tích bề mặt hiệu dụng khoảng $0{,}35\text{ m}^2$.
* Sơ đồ bố trí hệ thống pilot cho thí nghiệm được thể hiện trong Hình 1, và Bảng S1 (xem Supplementary Material) xác định các thiết bị đo được sử dụng trong hệ thống pilot:
  * **Hình 1.** Sơ đồ hệ thống SMBR quy mô pilot (Schematic diagram of the SMBR system).
    <img src="assets/fig_01_p4.jpeg" alt="Hình 1" />
    - Cấu hình hệ thống gồm bể bioreactor chứa màng sợi rỗng ngập nước (submerged hollow fibre membrane), phao kiểm soát mức chất lỏng (Level controller) và bể cấp nguyên liệu vào (Influent Supply Tank).
    - Hệ thống sục khí: máy nén khí C-$101$ dẫn qua van điều khiển PV-$101$ và lưu lượng kế FA-$101$ tới bộ khuếch tán khí (Air Diffuser) đặt bên dưới module màng.
    - Tuyến hút permeate: chỉ báo áp suất PI-$101$, van SV-$101$, bơm hút permeate P-$101$ và lưu lượng kế FM-$101$ dẫn tới bể chứa permeate (Permeate Tank).
    - Tuyến rửa ngược (backwash): bể chứa rửa ngược (Backwash Tank), bơm P-$102$ và van SV-$102$ kết nối vào đường ống màng.
* Quá trình thu thập dữ liệu (data acquisition) được kiểm soát và giám sát thông qua phần mềm National Instruments Labview 2009, kết nối giao tiếp với phần cứng NI USB 6009.

#### 2.1.1. Data collection

* Tổng cộng $4.000$ điểm dữ liệu được thu thập cho mỗi thông số trong suốt thí nghiệm, bao gồm lưu lượng khí sục (airflow tính bằng standard litres per minute - $\text{SLPM}$), điện áp bơm hút permeate (permeate pump voltage), áp suất qua màng (transmembrane pressure - TMP tính bằng $\text{mbar}$), và thông lượng permeate (permeate flux tính bằng $\text{L}\cdot\text{m}^{-2}\cdot\text{h}^{-1}$).
* Các bước nhảy biên độ ngẫu nhiên (random magnitude steps) biến thiên từ $1{,}4$ đến $3\text{ V}$ đối với bơm hút và từ $0$ đến $270\text{ mbar}$ đối với áp suất qua màng ($\text{TMP}$), nhằm tạo ra phản ứng động học (dynamic behaviour) của quá trình lọc.
* Cả bơm hút permeate và TMP đều ở trạng thái TẮT (OFF) trong chu kỳ nghỉ (relaxation period).
* Chu kỳ vận hành hút permeate - nghỉ (permeate-to-relaxation period) được duy trì ở mức $120\text{ s}$ cho hút permeate và $30\text{ s}$ cho nghỉ (relaxation), kết hợp sục khí liên tục (continuous aeration airflow).
* Lưu lượng sục khí được điều chỉnh trong khoảng $6$ đến $8\text{ SLPM}$ trong suốt quá trình lọc để duy trì cường độ bọt khí cao phục vụ làm sạch bề mặt màng (membrane surface cleansing).
* Tập dữ liệu lọc SMBR được minh họa trong Hình 2, bao gồm điện áp bơm permeate và TMP đóng vai trò các đầu vào (inputs) cùng thông lượng permeate là đầu ra (output):
  * **Hình 2.** Tập dữ liệu từ thí nghiệm lọc SMBR (Dataset from the SMBR filtration experiment).
    <img src="assets/fig_02_p5.jpeg" alt="Hình 2" />
    - Bốn đồ thị biến thiên theo thời gian ($0$ đến $4.000\text{ s}$):
      - Điện áp bơm hút (Permeate pump voltage): các xung bậc ngẫu nhiên từ $1{,}4$ đến $3\text{ V}$, về $0\text{ V}$ trong chu kỳ relaxation.
      - Lưu lượng khí sục (Airflow): duy trì liên tục quanh $6$–$8\text{ SLPM}$ để làm sạch bề mặt màng.
      - Áp suất qua màng (TMP): biến thiên từ $0$ đến $270\text{ mbar}$ trong giai đoạn lọc và giảm về $0\text{ mbar}$ khi nghỉ.
      - Thông lượng thấm qua (Permeate flux): biến thiên đồng pha với điện áp và TMP, về $0\text{ L}\cdot\text{m}^{-2}\cdot\text{h}^{-1}$ trong thời gian nghỉ ($120\text{ s}$ lọc / $30\text{ s}$ nghỉ).
* Phân tích dữ liệu được thực hiện bằng phần mềm MATLAB R2015a và Design-Expert phiên bản $12.0$.

#### 2.1.2. Experimental analyses

* Hiệu suất quá trình lọc được đánh giá dựa trên thông lượng permeate ($J$), được tính toán theo công thức:
  $$J = \frac{v}{A \cdot t} \tag{1}$$
  * Trong đó:
    * $J$ là thông lượng permeate ($\text{L}\cdot\text{m}^{-2}\cdot\text{h}^{-1}$).
    * $v$ là lưu lượng thể tích tính bằng lít ($\text{L}$).
    * $A$ là diện tích bề mặt màng ($\text{m}^2$).
    * $t$ là thời gian ($\text{h}$).
