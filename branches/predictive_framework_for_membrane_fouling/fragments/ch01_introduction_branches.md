## 1. Giới thiệu tổng quan (Introduction)

### 1.1 Tổng quan công nghệ MBR và ưu thế xử lý nước thải

#### 1.1.1 Nguyên lý tích hợp màng sinh học
- Công nghệ màng sinh học (Membrane Bioreactor - MBR) kết hợp xử lý sinh học bùn hoạt tính với công nghệ lọc màng.
- Hệ thống MBR thay thế hoàn toàn bể lắng thứ cấp truyền thống trong các quy trình xử lý nước thải.
- Quá trình phân tách pha rắn và pha lỏng diễn ra trực tiếp qua các lỗ màng lọc bán thấm.
- Công nghệ này áp dụng phổ biến trong xử lý nước thải đô thị và các cơ sở công nghiệp.

#### 1.1.2 Các ưu thế kỹ thuật vượt trội
- MBR giảm thiểu đáng kể diện tích chiếm dụng mặt bằng (compact footprint) so với quy trình bùn hoạt tính truyền thống.
- Hệ thống tạo ra lượng bùn thải dư thấp hơn nhờ duy trì thời gian lưu giữ bùn (SRT) kéo dài.
- Nước sau xử lý có độ trong suốt cao và loại bỏ triệt để vi sinh vật gây bệnh (pathogens).
- Công nghệ loại bỏ hiệu quả các hợp chất ô nhiễm khó phân hủy và vi chất ô nhiễm (micropollutants).
- Nước sau lọc đáp ứng các tiêu chuẩn khắt khe cho mục đích tái sử dụng trực tiếp.

### 1.2 Thách thức cốt lõi: Hiện tượng nghẹt màng (Membrane Fouling) và cơ chế hình thành

#### 1.2.1 Bản chất vật lý và hóa sinh của nghẹt màng
- Nghẹt màng (Membrane Fouling) hình thành do sự tích tụ chất rắn, chất keo và chất hữu cơ hòa tan.
- Các tạp chất bám dính lên bề mặt màng hoặc lắng đọng bên trong các mao quản màng.
- Cơ chế nghẹt màng bao gồm hình thành lớp bánh cặn (cake layer), nghẽn lỗ màng (pore blocking) và phát triển màng sinh học (biofilm).
- Quá trình nghẹt làm suy giảm độ thấm thủy lực và làm gia tăng áp suất xuyên màng (TMP).

#### 1.2.2 Tác động vận hành và kinh tế
- Mức tăng TMP làm tăng điện năng tiêu thụ của hệ thống bơm màng và máy thổi khí sục khí.
- Người vận hành phải thực hiện làm sạch hóa chất tại chỗ (Cleaning-in-Place - CIP) thường xuyên hơn.
- Hóa chất làm sạch ăn mòn dần vật liệu màng, làm giảm tuổi thọ của cụm màng lọc.
- Chi phí bảo trì, tiêu thụ điện năng và thay thế màng chiếm tỷ trọng lớn trong ngân sách vận hành.

#### 1.2.3 Các yếu tố ảnh hưởng đa biến
- Đặc tính nước thải đầu vào chi phối quá trình tạo cặn, bao gồm COD, nhiệt độ và nồng độ chất dinh dưỡng.
- Thông số vận hành bao gồm lưu lượng lọc qua màng (flux $J$), tốc độ sục khí và chu kỳ bơm hút.
- Vận hành ở mức flux quá cao làm tăng nhanh tốc độ nghẹt màng và phát sinh rủi ro sự cố.
- Đặc tính bùn sinh học gồm nồng độ chất rắn lơ lửng (MLSS), các chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP).

### 1.3 Hạn chế của các mô hình cơ chế và thực nghiệm quy mô phòng thí nghiệm

#### 1.3.1 Khoảng cách giữa phòng thí nghiệm và hệ thống quy mô thực
- Nghiên cứu quy mô phòng thí nghiệm (lab-scale) sử dụng dòng vào nhân tạo với thành phần đồng nhất và lưu lượng cố định.
- Hệ thống MBR quy mô thực (Full-Scale MBR) phải đối mặt với dòng chảy biến đổi liên tục và tải lượng bất định.
- Dữ liệu thu thập từ trạm thực tế chứa nhiều giá trị dị biệt, xung nhiễu tín hiệu và khoảng trống mất dữ liệu.
- Các mô hình thực nghiệm trong phòng thí nghiệm thường mất tính chuẩn xác khi áp dụng vào trạm xử lý công nghiệp.

#### 1.3.2 Rào cản của mô hình cơ chế truyền thống
- Mô hình cơ chế (Mechanistic Models) xây dựng dựa trên động lực học chất lưu, truyền khối và định luật Darcy.
- Công thức Darcy mô tả trở lực màng:
  $$J = \frac{\Delta \text{TMP}}{\mu \cdot R_t}$$
- Trong đó $\mu$ là độ nhớt động học, $R_t$ là tổng trở lực lọc gồm màng lọc và lớp bánh cặn.
- Mô hình cơ chế đòi hỏi nhiều giả định lý tưởng hóa cấu trúc màng và các đặc tính vi mô của bùn.
- Việc đo đạc các tham số vi mô như điện tích bề mặt hạt keo hoặc độ nén bánh cặn rất khó thực hiện tại hiện trường.
- Các phương trình vi phân phi tuyến phức tạp gặp khó khăn khi phản ánh biến động sinh học đột ngột.

### 1.4 Tiềm năng và rào cản của Trí tuệ nhân tạo (AI) / Học máy (Machine Learning) truyền thống

#### 1.4.1 Tiềm năng của các thuật toán học máy
- Mô hình học máy (Machine Learning - ML) mô phỏng chính xác các quan hệ phi tuyến phức tạp giữa nhiều thông số đầu vào.
- Thuật toán học máy có khả năng trích xuất các quy luật ẩn sâu trong các chuỗi dữ liệu lớn.
- Các thuật toán phổ biến gồm mạng nơ-ron nhân tạo (ANN), máy học vectơ hỗ trợ (SVM), Random Forest và học sâu.
- Mô hình dữ liệu cung cấp khả năng dự báo trước sự cố suy giảm lưu lượng lọc.

#### 1.4.2 Rào cản mô hình hộp đen (Black-box) và thiếu khả năng diễn giải
- Thuật toán học máy truyền thống hoạt động như một hệ thống hộp đen (black-box).
- Kỹ sư trạm xử lý không hiểu được căn cứ logic mà mô hình sử dụng để đưa ra cảnh báo.
- Sự thiếu minh bạch làm giảm độ tin cậy và cản trở việc triển khai AI vào kiểm soát thực tế.

#### 1.4.3 Thách thức về chất lượng dữ liệu và tính phụ thuộc thời gian
- Thiết bị cảm biến hiện trường chịu tác động của môi trường bẩn, gây sai lệch và trôi số đo.
- Các biến đầu vào có thang đo và đơn vị khác biệt lớn, dễ gây sai lệch trọng số mô hình.
- Nghẹt màng có tính chất tích lũy theo thời gian (time-dependent cumulative nature).
- Đa số mô hình truyền thống chỉ dùng dữ liệu điểm tức thời, bỏ qua tác động tích lũy từ lịch sử vận hành.
- Thông số mục tiêu truyền thống thường dùng riêng biệt TMP hoặc flux $J$, không phản ánh đầy đủ khi cả hai cùng biến thiên.

### 1.5 Mục tiêu và cấu trúc nghiên cứu: Tích hợp Kỹ thuật đặc trưng và XAI trên MBR quy mô thực

#### 1.5.1 Mục tiêu nghiên cứu cốt lõi
- Xây dựng khung phân tích và dự báo nghẹt màng ứng dụng cho trạm MBR quy mô thực (Full-Scale MBR).
- Đối tượng kiểm chứng là hệ thống MBR xử lý nước thải chế biến thực phẩm vận hành thực tế.
- Khung nghiên cứu tích hợp kỹ thuật đặc trưng dựa trên AI (AI-Driven Feature Engineering) và AI có thể giải thích (XAI).
- Bộ dữ liệu thực nghiệm bao gồm chuỗi thời gian liên tục kéo dài hơn 6 tháng.

#### 1.5.2 Kỹ thuật đặc trưng thích ứng dữ liệu hiện trường
- Đề xuất biến mục tiêu là độ thông lượng riêng (Specific Flux, $J_s$):
  $$J_s = \frac{J}{\text{TMP}}$$
- Đại lượng $J_s$ tương đương với độ thấm thủy lực của màng, phản ánh đồng thời biến động của cả $J$ và TMP.
- Bổ sung biến hiệu suất khử COD ($\text{Eff}_{\text{COD}}$) để phản ánh trực tiếp hoạt tính phân hủy sinh học:
  $$\text{Eff}_{\text{COD}} = \frac{\text{COD}_{\text{in}} - \text{COD}_{\text{eff}}}{\text{COD}_{\text{in}}} \times 100\%$$
- Áp dụng kỹ thuật trung bình động (Moving Average) cho các chuỗi dữ liệu:
  $$\overline{X}_t = \frac{1}{k} \sum_{i=0}^{k-1} X_{t-i}$$
- Phương pháp trung bình động giúp làm phẳng xung nhiễu cảm biến và giữ lại xu hướng tích lũy thời gian của màng bẩn.

#### 1.5.3 Hiệu năng mô hình và cơ chế giải thích XAI
- Thuật toán CatBoost đạt độ chính xác dự báo cao nhất trong các mô hình kiểm nghiệm ($R^2 = 0.8374$).
- CatBoost vượt trội hoàn toàn so với các mô hình thống kê truyền thống và các giải thuật học máy khác.
- Phương pháp XAI sử dụng giá trị SHAP để phân tích độ nhạy biến số.
- Kết quả xác định tỷ lệ F/M và nồng độ MLSS là hai biến chi phối mạnh nhất.
- Khung mô hình cung cấp các giải thích định lượng minh bạch cho người vận hành trạm.

#### 1.5.4 Giá trị ứng dụng thực tiễn và định hướng tích hợp
- Khung dự báo hỗ trợ kỹ sư vận hành điều chỉnh kịp thời các thông số sục khí và chu kỳ hút lọc.
- Mô hình cho phép lập kế hoạch làm sạch màng chủ động trước khi màng rơi vào trạng thái tắc nghẽn nghiêm trọng.
- AI kết hợp với mạng lưới cảm biến hiện có để tạo thành hệ thống cảnh báo lai (hybrid decision support system).
- Dữ liệu dự báo AI có thể điều chỉnh tham số đầu vào cho các mô phỏng vật lý, tăng cường hiệu quả quản lý trạm.
