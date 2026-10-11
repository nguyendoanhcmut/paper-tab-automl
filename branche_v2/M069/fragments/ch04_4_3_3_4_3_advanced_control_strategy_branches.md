#### 3.4.3. Advanced control strategy

* Kịch bản mô phỏng mở rộng (*in-silico* extended scenario) ghi nhận bước cải thiện đáng kể khi tối ưu hóa đồng thời cả tải trọng nitơ (nitrogen loading rate - $NLR$) và lưu lượng sục khí ($F_{\text{air}}$) bên cạnh thời gian lưu bùn (solids retention time - $SRT$) và thời gian lưu nước (hydraulic retention time - $HRT$) (Bảng S10):
  * Trong kịch bản mô phỏng mở rộng này, $NLR$ và $F_{\text{air}}$ được tối ưu hóa đồng bộ cùng với $SRT$ và $HRT$ nhằm kiểm soát động học hệ thống (Bảng S10).
  * Việc kết hợp tối ưu đồng thời cả $4$ thông số ($SRT$, $HRT$, $NLR$, $F_{\text{air}}$) khắc phục các giới hạn của chiến lược kiểm soát vận hành cố định truyền thống.
* Mô phỏng dự báo nồng độ amoni dòng ra ($NH_4\text{–}N_{\text{eff}}$) giảm từ $12\text{--}50\%$ xuyên suốt các giai đoạn vận hành được đánh giá (Bảng 2):
  * **Bảng 2.** Cải thiện mô phỏng về hiệu suất xử lý amoni, tiềm năng tái sử dụng nước và nhu cầu sục khí
    * <img src="assets/table_02_p16.png" alt="Bảng 2" />
    * **Bảng này chứng minh điều gì**
      * Chiến lược điều khiển nâng cao giúp đồng thời giảm nồng độ amoni ($NH_4\text{–}N$), gia tăng thể tích nước tái sử dụng đạt chuẩn và tiết kiệm nhu cầu sục khí ($F_{\text{air}}$) qua cả $4$ giai đoạn vận hành ($28\text{--}89\text{ d}$) khi tối ưu hóa đồng thời $SRT$, $HRT$, $NLR$ và $F_{\text{air}}$.
    * **Từ đâu mà thấy được**
      * Nồng độ amoni giảm trung bình $12\text{--}50\%$ qua các giai đoạn (Giai đoạn $1$ giảm $27\%$, Giai đoạn $2$ giảm $36\%$, Giai đoạn $3$ giảm $50\%$, Giai đoạn $4$ giảm $12\%$).
      * Thể tích nước đạt chuẩn tái sử dụng tăng từ $105\text{--}712\text{ L}\cdot\text{m}^{-3}$ lên $145\text{--}750\text{ L}\cdot\text{m}^{-3}$, và lưu lượng khí sục khí giảm $32\text{--}38\%$ ở các Giai đoạn $2, 3, 4$ ($35\%$, $38\%$, $32\%$).
  * Sự suy giảm nồng độ amoni này giúp gia tăng thể tích nước sau xử lý đáp ứng quy chuẩn tái sử dụng (water reuse standard) thêm $5\text{--}67\%$ so với mức cơ sở.
  * Sản lượng nước đạt chuẩn tái sử dụng tăng lên mức tối đa $750\text{ L}\cdot\text{m}^{-3}$ nước xử lý ở giai đoạn thuận lợi nhất (Giai đoạn 4).
  * Các kết quả đại diện cho dự báo mô phỏng và cần được kiểm chứng trong điều kiện vận hành thực nghiệm có kiểm soát.
* Việc chủ động cắt giảm lưu lượng sục khí mang lại mức tiết kiệm năng lượng cho hệ thống photobioreactor màng (membrane photobioreactor - MPBR):
  * Phân tích kinh tế sơ bộ đối với cấu hình MPBR thực nghiệm của González-Camejo và cộng sự [36] ghi nhận nhu cầu điện năng là $0{,}288\text{ kWh}\cdot\text{m}^{-3}$ cho sục khí và $0{,}369\text{ kWh}\cdot\text{m}^{-3}$ cho toàn bộ hệ thống dưới điều kiện vận hành cố định.
  * Dựa trên các kết quả mô phỏng, triển khai hệ thống điều khiển nâng cao có thể giảm nhu cầu năng lượng cho công đoạn sục khí xuống còn $0{,}179\text{--}0{,}196\text{ kWh}\cdot\text{m}^{-3}$.
  * Mức cắt giảm năng lượng sục khí này kéo tổng mức tiêu thụ năng lượng của hệ thống MPBR xuống còn $0{,}260\text{--}0{,}277\text{ kWh}\cdot\text{m}^{-3}$.
  * Mức giảm tổng năng lượng tiêu thụ từ $0{,}369\text{ kWh}\cdot\text{m}^{-3}$ xuống còn $0{,}260\text{--}0{,}277\text{ kWh}\cdot\text{m}^{-3}$ tương đương với mức tiết kiệm $25\text{--}30\%$ tổng năng lượng tiêu thụ của toàn trạm.
* Chiến lược điều khiển nâng cao tích hợp đồng thời cả $F_{\text{air}}$ và $NLR$ nhằm tối ưu hóa hiệu suất sinh học và hiệu quả sử dụng tài nguyên (Hình 7):
  * **Hình 7.** So sánh thông số vận hành ($HRT$, $SRT$, $F_{\text{air}}$, $NLR$) và xác suất tái sử dụng ($p_{\text{reuse}}$)
    * <img src="assets/fig_08_p17.jpeg" alt="Hình 7" />
    * **Hình này chứng minh điều gì**
      * Chiến lược điều khiển nâng cao tối ưu hóa đồng thời $4$ thông số ($HRT$, $SRT$, $F_{\text{air}}$, $NLR$) giúp nâng cao và duy trì ổn định xác suất tái sử dụng nước vượt ngưỡng tuân thủ ($p_{\text{reuse}} > 0{,}50$) xuyên suốt cả $4$ giai đoạn theo mùa, khắc phục tình trạng vi phạm thường xuyên ở điều kiện thực nghiệm cơ sở.
      * Điều biến động học các thông số (kéo dài $HRT$, điều chỉnh $SRT$, và tiết giảm $F_{\text{air}}$ khi nhu cầu thấp) vừa đảm bảo chất lượng nước đầu ra vừa tiết kiệm năng lượng sục khí.
    * **Từ đâu mà thấy được**
      * Trên cả $4$ giai đoạn (a–d), xác suất tái sử dụng sau điều khiển ($p_{\text{reuse\_control}}$, tam giác xanh lá đậm) luôn nằm trên ngưỡng tiêu chuẩn $p_{\text{reuse}} = 0{,}50$ và đạt mức cao ($0{,}70\text{--}0{,}95$), trong khi điều kiện thực nghiệm thường xuyên rớt xuống dưới $0{,}50$ (dao động $0{,}10\text{--}0{,}40$).
      * Đồ thị ghi nhận $HRT$ được tăng linh hoạt từ $1{,}2\text{--}1{,}6\text{ d}$ lên $2\text{--}6\text{ d}$ ở thời điểm tải cao, $SRT$ được giữ ổn định quanh $3\text{--}6\text{ d}$, và $F_{\text{air}}$ được kiểm soát tối ưu ($2{,}7\text{--}7{,}0\text{ vvm}$) theo biến động của $NLR$ ($8\text{--}30\text{ kg N}\cdot\text{d}^{-1}$) qua từng thời kỳ vận hành.
  * Điều biến linh hoạt $F_{\text{air}}$ bám sát biến động $NLR$ giúp duy trì nồng độ oxy hòa tan tối ưu mà không gây lãng phí năng lượng máy thổi khí.
  * Tối ưu hóa động học đảm bảo xác suất tái sử dụng nước luôn đạt yêu cầu bất chấp dao động thời tiết và tải trọng theo mùa.
