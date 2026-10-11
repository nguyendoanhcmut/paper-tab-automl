#### 3.4.1. Interaction between operating parameters

* Chiến lược kiểm soát dựa trên tương tác giữa tỷ số $\text{SRT}\cdot\text{HRT}^{-1}$, lưu lượng sục khí $F_{\text{air}}$ và tải trọng nạp nitơ $\text{NLR}$ cho thấy việc gia tăng tỷ số $\text{SRT}\cdot\text{HRT}^{-1}$ (tức $\text{SRT}/\text{HRT}$) dẫn đến sự suy giảm gần như tuyến tính của $F_{\text{air}}$ cần thiết để duy trì ngưỡng tuân thủ $p_{\text{reuse}} = 0{,}50$.
  * **Hình 5.** Mối quan hệ giữa lưu lượng sục khí $F_{\text{air}}$ và các thông số vận hành tại ngưỡng $p_{\text{reuse}} = 0{,}50$
    * <img src="assets/fig_06_p13.jpeg" alt="Hình 5" />
    * **Hình này chứng minh điều gì**
      * Tăng tỷ số $\text{SRT}\cdot\text{HRT}^{-1}$ giúp giảm tuyến tính $F_{\text{air}}$ để duy trì $p_{\text{reuse}} = 0{,}50$, cân bằng tối ưu giữa chi phí sục khí (tới $78\%$ năng lượng) và lượng nước tái sử dụng.
      * Quan hệ giữa $\text{SRT}$ và $\text{HRT}$ mang tính phi tuyến với đường biên $\text{SRT}_{\min} = 0{,}7657 e^{0{,}4802\cdot\text{HRT}}$ ($R^2 = 0{,}996$), chứng minh cần điều khiển động thay cho điểm đặt cố định.
    * **Từ đâu mà thấy được**
      * Phân ban $(a)$, $(b)$: $F_{\text{air}}$ ($0{,}10\text{--}0{,}26\text{ vvm}$) giảm tuyến tính theo $\text{SRT}\cdot\text{HRT}^{-1}$ ($1{,}0\text{--}4{,}0$) qua các mức $\text{NLR}$ ($13{,}16\text{--}19{,}70\text{ kgN/d}$) và điều kiện môi trường ($\text{PAR}$, $T$, $\text{DO}$).
      * Phân ban $(c)$, $(d)$: $\text{SRT}$ ($1{,}5\text{--}4{,}5\text{ d}$) giảm phi tuyến theo $\text{HRT}$ ($1{,}4\text{--}2{,}2\text{ d}$) trên các mức $F_{\text{air}}$ ($0{,}06\text{--}0{,}24\text{ vvm}$) tiệm cận đường biên đỏ $\text{SRT}_{\min}$, và tại $F_{\text{air}} = 0{,}12\text{ vvm}$.
  * Tăng $F_{\text{air}}$ cải thiện mức độ đồng nhất của huyền phù sinh khối và gia tăng tần suất chu kỳ sáng–tối (light–dark cycle hay duty cycle) bên trong bể phản ứng quang sinh học màng (membrane photobioreactor - MPBR).
  * Duty cycle cao hơn giúp tăng cường hiệu suất quang hợp và giảm hiện tượng quang ức chế (photoinhibition) do vi tảo tiếp xúc với bức xạ cao gần bề mặt trong thời gian ngắn hơn và có nhiều thời gian phục hồi trong các vùng tối hơn.
  * Hiệu ứng quang hợp cải thiện hỗ trợ loại bỏ chất dinh dưỡng, từ đó nâng cao tiềm năng tái sử dụng nước và sản lượng nước thu hồi ($p_{\text{reuse}}$).
  * Sự gia tăng sản lượng nước tái sử dụng theo $F_{\text{air}}$ thể hiện rõ nét hơn ở các tỷ số $\text{SRT}\cdot\text{HRT}^{-1}$ cao, phản ánh mối liên hệ mật thiết giữa thời gian lưu sinh khối và thời gian lưu thủy lực.
* Đánh giá mối liên kết nước–năng lượng (water–energy nexus) đặt ra bài toán cân bằng tối ưu giữa chi phí vận hành gia tăng do sục khí $F_{\text{air}}$ và giá trị kinh tế của thể tích nước tái sử dụng thu hồi được.
* Mối quan hệ $\text{SRT} = f(\text{HRT}, F_{\text{air}})$ biểu hiện hành vi phi tuyến tính đặc trưng cho các hệ thống vi tảo ngoài trời chịu ảnh hưởng của các yếu tố biến động môi trường.
  * Các xu hướng phi tuyến này tương đồng với các công bố trước đây giữa $\text{SRT}$ và nồng độ sinh khối ở khoảng $\text{SRT} = 10\text{--}30\text{ ngày}$, cũng như khoảng dao động vận hành rộng của $\text{HRT}$ ngoài trời ($2{,}7\text{--}14\text{ ngày}$).
  * Việc duy trì các điểm đặt $\text{SRT}$ và $\text{HRT}$ cố định như trong xử lý nước thải truyền thống là không đủ để đáp ứng độ biến thiên cao của điều kiện tự nhiên.
* Từ góc độ kỹ thuật, lưu lượng sục khí cơ học $F_{\text{air}}$ phải được ghép nối động (dynamically coupled) với tỷ số tổ hợp $\text{SRT}\cdot\text{HRT}^{-1}$ và tải trọng nitơ nạp vào $\text{NLR}$:
  * Trong các giai đoạn $\text{NLR}$ tăng cao hoặc bức xạ quang hợp ($\text{PAR}$) không tối ưu, người vận hành không thể chỉ dựa vào điều chỉnh lưu lượng thủy lực mà cần tăng tự động và đón đầu $F_{\text{air}}$ để đáp ứng nhu cầu oxy đột ngột từ vi khuẩn nitrat hóa cạnh tranh và duy trì trạng thái lơ lửng của sinh khối vi tảo mật độ cao.
  * Trong điều kiện quang hợp mạnh và tải nạp đầu vào thấp, mô hình cho phép giảm $F_{\text{air}}$ an toàn mà vẫn bảo đảm chất lượng nước đầu ra.
  * Vì sục khí chiếm tới $78\%$ tổng năng lượng tiêu thụ trong hệ MPBR, việc chuyển đổi các ngưỡng thống kê này thành các điểm đặt điều khiển tự động trong hệ thống SCADA giúp ngăn ngừa sự cố sinh học đồng thời giảm thiểu tối đa chi phí năng lượng vận hành.
