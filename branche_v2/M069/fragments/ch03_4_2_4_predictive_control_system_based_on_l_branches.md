### 2.4. Predictive control system based on LR modelling

* Chiến lược điều khiển dự báo dựa trên mô hình hồi quy logistic (logistic regression - LR) được phát triển cho hệ thống photobioreactor màng (membrane photobioreactor - MPBR) dung tích $470\text{ L}$ nhằm tối ưu hóa đồng thời 4 biến vận hành thao tác (manipulated operational variables):
  * Thời gian lưu bùn (solids retention time - $\text{SRT}$, $\text{d}$): đại diện cho mức độ lưu giữ sinh khối vi tảo - vi khuẩn trong bể.
  * Thời gian lưu nước (hydraulic retention time - $\text{HRT}$, $\text{d}$): quyết định tải trọng thủy lực cấp vào hệ thống.
  * Lưu lượng sục khí (aeration flow rate - $F_{\text{air}}$, $\text{L}\cdot\text{min}^{-1}$): kiểm soát việc hòa tan khí, xáo trộn bùn và mức tiêu thụ năng lượng sục khí.
  * Tải trọng nitơ amoni (ammonium nitrogen loading rate - $\text{NLR}$, khối lượng $\text{N}$ trên đơn vị thời gian): tải trọng cơ chất dinh dưỡng nạp vào bể MPBR.
* Hai quan hệ thực nghiệm được tích hợp làm ràng buộc vận hành (operational constraints) trong kiến trúc điều khiển:
  * Sự phụ thuộc của nồng độ sinh khối vào thời gian lưu bùn thông qua mật độ quang ở bước sóng $680\text{ nm}$: $OD_{680} = f(\text{SRT})$ (Hình S3).
  * Mối quan hệ liên thuộc giữa tải trọng amoni $\text{NLR}$ và thời gian lưu nước $\text{HRT}$ thông qua nồng độ amoni dòng vào ($NH_4\text{–}N_{\text{inf}}$) theo phương trình (5):
    $$\text{NLR} = \frac{NH_4\text{–}N_{\text{inf}} \cdot 470}{\text{HRT}}$$
    trong đó $\text{NLR}$ là tải trọng amoni nạp vào MPBR ($\text{mg N}\cdot\text{d}^{-1}$ hoặc khối lượng $\text{N}$ trên đơn vị thời gian), $NH_4\text{–}N_{\text{inf}}$ là nồng độ amoni dòng vào ($\text{mg N}\cdot\text{L}^{-1}$), $470$ là thể tích phản ứng của bể MPBR ($\text{L}$), và $\text{HRT}$ là thời gian lưu nước ($\text{d}$).
* Chiến lược triển khai điều khiển giám sát (implementation strategy) được phân tầng dựa trên mức nồng độ amoni dòng ra ($NH_4\text{–}N_{\text{eff}}$):
  * Khi nồng độ $NH_4\text{–}N_{\text{eff}}$ cao: tối đa hóa đồng thời $F_{\text{air}}$, $\text{HRT}$ và $\text{SRT}$ nhằm tăng cường hiệu suất loại bỏ amoni và hướng tới đạt chuẩn tái sử dụng.
  * Khi nồng độ $NH_4\text{–}N_{\text{eff}}$ thấp: tối thiểu hóa lưu lượng sục khí $F_{\text{air}}$ ($F_{\text{air}}' \to \min$) nhằm cắt giảm tối đa chi phí năng lượng vận hành.
  * Khi nồng độ $NH_4\text{–}N_{\text{eff}}$ ở mức trung gian: các giá trị $F_{\text{air}}$ được lựa chọn thông qua thuật toán dò tìm lặp (iteratively selected) nhằm đảm bảo các giá trị $\text{SRT}$ và $\text{HRT}$ xác định luôn nằm trong miền giá trị áp dụng (applicability ranges) của các mô hình LR.
  * Khi $\text{SRT}$ và $\text{HRT}$ được điều chỉnh, các biến trạng thái phụ thuộc gồm $OD_{680}$ và $\text{NLR}$ được hiệu chỉnh tỷ lệ thuận tương ứng so với trạng thái hiện tại.
* Điểm đặt vận hành tối ưu (optimal operational parameters: $\text{SRT}'$, $\text{HRT}'$, $\text{NLR}'$, $F_{\text{air}}'$) được thiết lập dựa trên dữ liệu đầu vào hiện tại ($x_i^c$, gồm điều kiện môi trường, sinh khối, hoạt tính vi sinh vật và ánh sáng) cùng nồng độ amoni mục tiêu dòng ra $NH_4\text{–}N_{\text{eff}} = 1{,}6\text{ mg N}\cdot\text{L}^{-1}$ (ngưỡng tiêu chuẩn tái sử dụng nước của Ý/EU):
  * Điểm đặt thời gian lưu bùn $\text{SRT}'$ được xác định theo phương trình (6):
    $$\begin{cases} \text{SRT}' = \frac{1}{\alpha_2} \cdot \left( \ln\left(\frac{p_{NH_4\text{–}N_{\text{eff}}=1{,}6}}{1 - p_{NH_4\text{–}N_{\text{eff}}=1{,}6}}\right) - \sum_{i=1}^{j-2} (\alpha_i \cdot x_i^c) - \alpha_1 \cdot \text{HRT}^c - \alpha_3 \cdot \text{NLR}^c - \alpha_4 \cdot F_{\text{air}}^c \right) \\ \text{SRT}' \le \text{SRT}_{\text{TH}} \\ OD_{680} = f(\text{SRT}) \end{cases}$$
  * Điểm đặt thời gian lưu nước $\text{HRT}'$ được xác định theo phương trình (7):
    $$\begin{cases} \text{HRT}' = \frac{1}{\alpha_1} \cdot \left( \ln\left(\frac{p_{NH_4\text{–}N_{\text{eff}}=1{,}6}}{1 - p_{NH_4\text{–}N_{\text{eff}}=1{,}6}}\right) - \sum_{i=1}^{j-2} (\alpha_i \cdot x_i^c) - \alpha_2 \cdot \text{SRT}_{\max} - \alpha_3 \cdot \text{NLR}^c - \alpha_4 \cdot F_{\text{air}}^c \right) \\ \text{HRT}' \le \text{HRT}_{\text{TH}} \\ \text{NLR} = f(\text{HRT}) \end{cases}$$
  * Điểm đặt lưu lượng sục khí $F_{\text{air}}'$ được xác định theo phương trình (8):
    $$\begin{cases} F_{\text{air}}' = \frac{1}{\alpha_1} \cdot \left( \ln\left(\frac{p_{NH_4\text{–}N_{\text{eff}}=1{,}6}}{1 - p_{NH_4\text{–}N_{\text{eff}}=1{,}6}}\right) - \sum_{i=1}^{j-2} (\alpha_i \cdot x_i^c) - \alpha_2 \cdot \text{SRT}_{\text{TH}} - \alpha_1 \cdot \text{HRT}_{\text{TH}} - \alpha_3 \cdot \text{NLR}_{\text{TH}} \right) \\ F_{\text{air}}' \le F_{\text{air,TH}} \\ F_{\text{air}}' \to \min \end{cases}$$
  * Quy ước ký hiệu toán học:
    * Dấu phẩy ($'$) biểu thị điểm đặt mới được cập nhật (updated setpoints).
    * Chỉ số trên $c$ biểu thị giá trị đo đạc/trạng thái hiện tại (current states).
    * Các hệ số hồi quy: $\alpha_{\text{SRT}} = \alpha_2$, $\alpha_{\text{HRT}} = \alpha_1$, $\alpha_{\text{NLR}} = \alpha_3$, $\alpha_{F_{\text{air}}} = \alpha_4$ là các hệ số của mô hình LR tương ứng với từng biến vận hành.
    * Chỉ số $\text{TH}$ biểu thị ngưỡng kích hoạt tối đa / giới hạn ràng buộc (threshold / actuation limits).
    * $x_i^c$ đại diện cho các biến đầu vào đo đạc khác (chất lượng nước thải dòng vào, điều kiện khí tượng, sinh khối/hoạt tính vi sinh vật và các biến liên quan đến bức xạ ánh sáng).
* Quy trình tính toán lặp và hội tụ (iterative identification workflow):
  * Do việc thay đổi $\text{SRT}$ và $\text{HRT}$ trực tiếp làm biến đổi $OD_{680}$ và $\text{NLR}$ theo các quan hệ hàm số Hình S3 và phương trình (5), các điểm đặt được tính toán thông qua vòng lặp cập nhật tỷ lệ $OD_{680}$ và $\text{NLR}$ sau mỗi bước điều chỉnh tỷ số $\text{SRT}\cdot\text{HRT}^{-1}$ cho đến khi nghiệm hội tụ hoàn toàn bên trong phạm vi áp dụng của mô hình LR.
* Khung mô phỏng kiểm chứng số (*in silico* simulation workflow) và phân tích tính bất định:
  * Tương tác phi tuyến giữa 4 biến vận hành ($\text{SRT}$, $\text{HRT}$, $\text{NLR}$, $F_{\text{air}}$) được khảo sát chi tiết dưới điều kiện đầu vào trung bình (average input conditions).
  * Ảnh hưởng của độ bất định đầu vào (input uncertainty) đối với nhu cầu cấp khí $F_{\text{air}}$ dự đoán được phân tích cho từng cặp giá trị $\text{SRT}\cdot\text{HRT}^{-1}$ và $\text{NLR}$, phản ánh đặc tính biến động động học của chất lượng nước thải và thời tiết thực tế ngoài trời.
  * Chiến lược điều khiển tối ưu nâng cao được thẩm định mô phỏng *in silico* trên 4 giai đoạn thực nghiệm (Periods 1, 2, 3, 4) được chọn lọc từ 10 giai đoạn vận hành MPBR ngoài trời (Mục 2.1, Bảng 1) do tính đại diện cao nhất cho tiềm năng nâng cấp quy mô công nghiệp (upscale) theo các nghiên cứu tiền đề [36,37].
