### 2.1. Measurement data

#### 2.1.1. Experimental pilot plant

* Dữ liệu thực nghiệm thu thập từ quá trình vận hành ngoài trời liên tục kéo dài $1{,}5\text{ năm}$ của hệ thống photobioreactor màng (membrane photobioreactor - MPBR) quy mô pilot có dung tích làm việc $470\text{ L}$:
  * Hệ thống gồm hai bể quang sinh học dạng tấm phẳng (flat-panel PBRs, kích thước $1{,}25 \times 2 \times 0{,}1\text{ m}$).
  * Hệ thống kết nối với cụm thu hồi sinh khối hai giai đoạn (two-step harvesting system) gồm các bể dung tích $14\text{ L}$ trang bị màng siêu lọc sợi rỗng (ultrafiltration hollow-fibre membranes, nhãn hiệu PURON® KMS PUR-PSH31, kích thước lỗ màng $0{,}03\text{ }\mu\text{m}$, tổng diện tích bề mặt màng $3{,}44\text{ m}^2$).
  * Hai bể PBR được giám sát liên tục bằng các cảm biến trực tuyến (on-line sensors) được hiệu chuẩn định kỳ để đo $\text{pH}$, nhiệt độ ($T$), oxy hòa tan ($DO$), và bức xạ quang hợp hoạt hóa đo theo phương thẳng đứng (photosynthetically active radiation - $PAR$).
  * Bộ điều khiển logic lập trình được (PLC) tích hợp SCADA chịu trách nhiệm thu thập dữ liệu và điều tiết các biến vận hành, bao gồm lưu lượng dòng vào và dòng ra, thời gian lưu nước ($HRT$), thời gian lưu bùn ($SRT$) và lưu lượng sục khí ($F_{air}$), mô phỏng các điều kiện vận hành điển hình ở quy mô công nghiệp lớn.
* Hệ thống MPBR tiếp nhận và xử lý nước thải sau xử lý từ hệ thống màng kỵ khí (anaerobic membrane bioreactor - AnMBR) quy mô pilot:
  * Nước thải đầu vào là nước thải đô thị từ nhà máy xử lý nước thải Carraixet (Carraixet WWTP, tọa độ $39^\circ 30' 04{,}0''\text{N } 0^\circ 20' 00{,}1''\text{W}$, Valencia, Tây Ban Nha), vận hành ngoài trời liên tục.
  * Hệ thống AnMBR chịu trách nhiệm xử lý các chất hữu cơ và loại bỏ mầm bệnh, trong khi giai đoạn MPBR thúc đẩy quá trình loại bỏ chất dinh dưỡng để tái sử dụng nước (water reclamation).
  * Sinh khối tạo ra từ cả hai bước được đưa vào quá trình đồng phân hủy kỵ khí (anaerobic co-digestion - AcoD) nhằm tối đa hóa sản lượng thu hồi khí sinh học (biogas).
  * Nghiên cứu này tập trung phân tích chuyên sâu giai đoạn hai (MPBR) do vai trò quyết định của quá trình vi tảo đối với tiềm năng tái sử dụng nước:
    * Dòng cấp vào MPBR được phân tích qua các mẫu đơn (grab samples) với cùng tần suất như các thông số khác của MPBR, cho phép đánh giá độc lập giai đoạn hai mà không cần phụ thuộc vào giai đoạn AnMBR trước đó.
    * Hiệu suất sinh học của hệ thống AnMBR không được đưa vào khung mô hình hồi quy logistic (logistic regression - LR) do bộ dữ liệu thực nghiệm của hệ thống này chưa đủ lớn.

#### 2.1.2. Data pre-processing and input variables

* Tập dữ liệu thu thập gồm $230\text{ mẫu}$ trong suốt $10\text{ giai đoạn}$ thực nghiệm ($2016\text{--}2018$, tần suất lấy mẫu $2\text{--}3\text{ mẫu/tuần}$), loại trừ các giai đoạn khởi động (start-up) và bảo trì hệ thống.
* Lựa chọn biến đầu vào cho mô hình LR từ $40\text{ biến}$ được giám sát:
  * Việc lựa chọn biến dựa trên kết quả phân tích đa biến trước đó (phân tích thành phần chính - PCA, bình phương tối thiểu từng phần - PLS) và phân tích hồi quy tuyến tính bội (multiple linear regression - MLR) để xác định các biến có mối liên hệ mật thiết nhất với hiệu suất quá trình.
  * Các biến đầu vào được lựa chọn cho mô hình LR phản ánh đặc tính vận hành và môi trường trong suốt thời gian nghiên cứu (Hình 2):
    * **Hình 2.** Biểu đồ hộp phân bố các thông số vận hành thực nghiệm MPBR
      * <img src="assets/fig_03_p6.jpeg" alt="Hình 2" />
      * **Hình này chứng minh điều gì**
        * Khoảng biến thiên thực tế của 12 biến đầu vào (thuộc 5 nhóm thông số) và nồng độ amoni đầu ra $NH_4\text{--}N_{eff}$ trong suốt vận hành ngoài trời.
      * **Từ đâu mà thấy được**
        * Trục hoành $Ox$: phân nhóm 13 biểu đồ hộp theo 5 nhóm thông số và dòng ra; Trục tung $Oy$: giá trị theo thang đo và đơn vị của từng biến.
        * Nhóm vận hành và môi trường: $HRT$ ($0{,}90\text{--}3{,}17\text{ d}$), $F_{air}$ ($0{,}15\text{--}0{,}27\text{ vvm}$), $SRT$ ($1{,}65\text{--}5{,}92\text{ d}$), $NLR$ ($8{,}75\text{--}46{,}82\text{ gN/d}$), $PLR$ ($0{,}08\text{--}3{,}72\text{ gP/d}$), $T$ ($12{,}64\text{--}27{,}14\ ^\circ\text{C}$), $PAR$ ($13\text{--}449\ \mu\text{mol}\cdot\text{m}^{-2}\cdot\text{s}^{-1}$).
        * Nhóm vi sinh, ánh sáng và dòng ra: $DO$ ($9{,}01\text{--}14{,}17\text{ gO}_2/\text{d}$), $DO_{max}$ ($10{,}91\text{--}21{,}27\text{ gO}_2/\text{d}$), $OD_{680}$ ($0{,}16\text{--}1{,}54$), $NH_4\text{--}N_{eff}$ ($0{,}00\text{--}37{,}15\text{ mgN/L}$).
    * (i) Các thông số vận hành có thể kiểm soát: thời gian lưu bùn ($SRT$), thời gian lưu nước ($HRT$) và lưu lượng sục khí ($F_{air}$).
    * (ii) Các điều kiện dòng cấp: tải trọng nitơ ($NLR$) và tải trọng phospho ($PLR$).
    * (iii) Các chỉ số hoạt tính quang hợp/vi sinh: nồng độ oxy hòa tan trung bình ngày ($DO$) và cực đại ngày ($DO_{max}$).
    * (iv) Các điều kiện môi trường xung quanh: bức xạ $PAR$ trung bình ngày và cực đại ngày ($PAR_{max}$), cùng nhiệt độ trung bình ngày ($T$) và cực đại ngày ($T_{max}$).
    * (v) Phân bố ánh sáng: được đánh giá thông qua mật độ quang ở bước sóng $680\text{ nm}$ ($OD_{680}$).
    * (vi) Nồng độ amoni dòng ra ($NH_4\text{–}N_{eff}$).
* Tách rời mối phụ thuộc giữa tải trọng dinh dưỡng và thời gian lưu nước:
  * Mặc dù $NLR$ và $PLR$ thông thường phụ thuộc vào $HRT$, chúng có thể được tách rời thông qua phối trộn dòng (stream blending) nhằm tối ưu hóa hoạt tính sinh học và kích hoạt các chiến lược kiểm soát nâng cao.
* Tác động chi phối của các yếu tố môi trường và quang học:
  * Giá trị trung bình và giá trị cực đại hàng ngày của $PAR$ và $T$ được tích hợp vào mô hình do sự dao động tự nhiên của thời tiết ngoài trời chi phối trực tiếp đến hiệu suất hệ thống.
  * $OD_{680}$ và $DO$ đóng vai trò là các chỉ số chính thể hiện hiệu quả sử dụng ánh sáng và năng suất tổng thể của quần xã vi tảo.
* Sàng lọc dữ liệu ngoại lai (outlier screening) và kiểm tra sai số đo đạc:
  * Quy trình chuẩn hóa Z-score được áp dụng theo công thức $Z_i = (x_i - \mu_i)/\sigma_i$ để phát hiện các giá trị dị biệt và sai số đo đạc tiềm ẩn.
  * Toàn bộ các giá trị quan trắc đều nằm trong ngưỡng chấp nhận ($Z_i = 0{,}01\text{--}2{,}95 < 3{,}0$, Bảng S2), chứng minh tập dữ liệu phân tích không có sai số đo đạc bất thường.
