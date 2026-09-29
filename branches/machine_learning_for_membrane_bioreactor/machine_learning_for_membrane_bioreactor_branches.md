---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Học Máy Trong Nghiên Cứu Bể Sinh Học Màng: Nguyên Lý, Phương Pháp, Ứng Dụng và Hướng Dẫn Thực Hành

## 1. Giới thiệu và Bối cảnh Công nghệ MBR

### 1.1 Tổng quan Công nghệ Bể phản ứng Sinh học Màng (MBR)

#### 1.1.1 Khái niệm và Nguyên lý Phân tách Pha
- Khái niệm hệ thống MBR: MBR kết hợp quá trình phân hủy sinh học bằng bùn hoạt tính và quá trình phân tách pha rắn lỏng bằng màng vi lọc (MF) hoặc siêu lọc (UF).
- Cột mốc lịch sử phát triển: Yamamoto và các cộng sự giới thiệu hệ thống MBR màng ngập (submerged MBR) lần đầu tiên vào năm 1989. Sáng kiến này đặt nền móng cho các hệ thống MBR hiện đại.
- Nguyên lý thay thế bể lắng thứ cấp: Màng lọc thay thế hoàn toàn bể lắng trọng lực truyền thống trong quy trình bùn hoạt tính (CAS). Màng lọc giữ lại toàn bộ chất rắn lơ lửng trong bể phản ứng.
- Cơ chế phân tách vật lý: Kích thước lỗ rỗng màng vi lọc (0.1 đến 0.4 $\mu m$) và siêu lọc (0.01 đến 0.1 $\mu m$) tạo hàng rào vật lý tuyệt đối. Hàng rào này ngăn chặn bùn vi sinh và vi khuẩn đi vào dòng thấm.
- Nồng độ sinh khối duy trì: Hệ thống duy trì nồng độ vi sinh vật cao trong bể sinh học. Quá trình vận hành không còn phụ thuộc vào đặc tính lắng của bông bùn.

#### 1.1.2 Các Ưu thế Kỹ thuật Vượt trội của Hệ thống MBR
- Chất lượng nước sau xử lý cao và ổn định: Nước đầu ra đạt độ đục thấp dưới 0.2 NTU. Nồng độ chất rắn lơ lửng (SS) giảm xuống mức không phát hiện được (Xiao et al., 2014; Krzeminski et al., 2017).
- Khả năng loại bỏ mầm bệnh: Màng lọc loại bỏ hoàn toàn vi khuẩn coliform, u nang nguyên sinh và phần lớn virus. Nước sau lọc đáp ứng trực tiếp các tiêu chuẩn tái sử dụng nước nghiêm ngặt.
- Tiết kiệm diện tích mặt bằng (Footprint): Hệ thống loại bỏ bể lắng thứ cấp và cụm bể lọc khử trùng phụ trợ. Diện tích xây dựng giảm từ 50% đến 70% so với hệ thống CAS truyền thống (Xiao et al., 2019; Qu et al., 2022).
- Vận hành tách biệt giữa HRT và SRT: Thời gian lưu nước thủy lực (HRT) tách rời hoàn toàn khỏi thời gian lưu giữ bùn (SRT). Kỹ sư có thể kiểm soát tuổi bùn dài mà không cần tăng dung tích bể sinh học.
- Giảm thiểu phát sinh bùn thải dư: Tỷ số dinh dưỡng trên vi sinh vật ($F/M$) thấp thúc đẩy quá trình hô hấp nội sinh của vi khuẩn. Lượng bùn thải dư phát sinh giảm từ 30% đến 50%.

### 1.2 Thách thức Tắc nghẽn Màng (Membrane Fouling) và Cơ chế Lý hóa

#### 1.2.1 Định nghĩa, Biểu hiện Đo đạc và Tác động Kỹ thuật - Kinh tế
- Định nghĩa tắc nghẽn màng: Tắc nghẽn màng là hiện tượng tích tụ các chất bẩn (foulants) trên bề mặt ngoài màng hoặc bên trong mạng lưới mao quản của màng.
- Biểu hiện qua thông lượng thẩm thấu ($J$): Trong chế độ vận hành áp suất không đổi, lưu lượng nước qua một đơn vị diện tích màng theo thời gian suy giảm liên tục:
  $$J = \frac{V}{A \cdot \Delta t}$$
  Trong đó:
  - $J$ là thông lượng nước lọc ($L \cdot m^{-2} \cdot h^{-1}$, viết tắt là LMH).
  - $V$ là thể tích dòng thấm thu được ($L$).
  - $A$ là diện tích bề mặt hiệu dụng của màng lọc ($m^2$).
  - $\Delta t$ là khoảng thời gian thu thập mẫu ($h$).
- Biểu hiện qua áp suất xuyên màng ($TMP$): Trong chế độ vận hành thông lượng không đổi, áp suất xuyên màng gia tăng liên tục để duy trì tốc độ lọc:
  $$TMP = P_{feed} - P_{permeate}$$
  Hoặc đối với hệ thống màng ngập hút chân không:
  $$TMP = P_{tank} - P_{permeate\_suction}$$
  Trong đó: $P_{feed}$ là áp suất dòng cấp ($kPa$), $P_{permeate}$ là áp suất dòng thấm ($kPa$), $P_{tank}$ là áp suất thủy tĩnh trong bể ($kPa$), $P_{permeate\_suction}$ là áp suất hút chân không ($kPa$).
- Gia tăng chi phí năng lượng: Khi $TMP$ tăng cao, bơm hút dòng thấm phải tiêu tốn công suất điện lớn hơn. Hệ thống cũng cần tăng lưu lượng sục khí để cọ rửa bề mặt màng.
- Giảm tuổi thọ vật liệu màng: Tắc nghẽn không phục hồi đòi hỏi quy trình làm sạch hóa chất khắc nghiệt. Các hóa chất oxy hóa mạnh làm giòn sợi màng và suy giảm độ bền cơ học (Xiao et al., 2019; Qu et al., 2022).

#### 1.2.2 Đặc tính Vật liệu Màng và Tương tác Bề mặt
- Các loại polymer chế tạo màng thông dụng:
  - Polyvinylidene fluoride (PVDF): Vật liệu có độ bền cơ học cao, kháng hóa chất oxy hóa tốt, được dùng rộng rãi trong các module sợi rỗng và tấm phẳng thương mại.
  - Polyethersulfone (PES): Vật liệu chịu nhiệt tốt, dải pH làm việc rộng từ 2 đến 12, dễ tạo màng có độ xốp đồng đều.
  - Polyethylene (PE): Vật liệu có độ bền kéo cao, trơ hóa học tốt, nhưng bề mặt mang tính kỵ nước tự nhiên lớn.
  - Polyacrylonitrile (PAN): Vật liệu có tính ưa nước tự nhiên cao, hạn chế bám dính dầu mỡ, nhưng độ bền cơ học kém hơn PVDF.
- Ảnh hưởng của tính ưa nước và kỵ nước (Hydrophilicity/Hydrophobicity):
  - Màng kỵ nước có góc tiếp xúc nước cao ($\theta > 70^\circ$). Tương tác kỵ nước giữa màng và các hợp chất hữu cơ thúc đẩy quá trình bám dính chất bẩn (Choi et al., 2002).
  - Màng ưa nước có góc tiếp xúc nước nhỏ ($\theta < 45^\circ$). Nước liên kết trên bề mặt tạo thành lớp hydrat hóa bảo vệ, cản trở sự lắng đọng của các phân tử protein và vi sinh vật.
- Cấu trúc lỗ rỗng và phân bố kích thước:
  - Phân bố kích thước lỗ rỗng hẹp giúp phân bố dòng chảy đều trên toàn bộ diện tích lọc. Cấu trúc này ngăn chặn hiện tượng quá tải cục bộ và duy trì thông lượng ổn định (Shimizu et al., 1990; Meireles et al., 1991).
  - Cấu trúc màng đối xứng và bất đối xứng tạo ra các hành vi cản trở dòng chảy khác nhau khi chất bẩn xâm nhập vào mao quản.
- Độ nhám bề mặt ở quy mô micromet:
  - Bề mặt màng nhám tạo ra các rãnh vi mô. Các rãnh này bẫy các hạt cặn lơ lửng và cản trở lực cắt thủy động lực học của bọt khí (Xu et al., 2020).
  - Bề mặt màng nhẵn phẳng làm giảm diện tích tiếp xúc với chất bẩn và làm chậm quá trình hình thành lớp bánh bùn (cake layer) (Vatanpour et al., 2011; Sadeghi et al., 2013; Panda et al., 2015).

#### 1.2.3 Động học Tương tác Kích thước Lỗ rỗng và Chất bẩn (Foulant-Pore Dynamics)
- Cơ chế loại trừ theo kích thước (Size Exclusion): Các hạt bùn và đại phân tử có đường kính lớn hơn kích thước lỗ rỗng màng ($d_{particle} > d_{pore}$) bị giữ lại hoàn toàn trên bề mặt màng (Meireles et al., 1991).
- Cơ chế bít tắc lỗ rỗng (Pore Clogging): Các hạt chất bẩn có kích thước xấp xỉ đường kính lỗ rỗng ($d_{particle} \approx d_{pore}$) thâm nhập vào miệng lỗ. Chúng chèn khít các mao quản và gây suy giảm diện tích lọc hiệu dụng tức thì.
- Cơ chế hấp phụ trong thành lỗ rỗng (Adsorptive Fouling): Các phân tử hữu cơ hòa tan kích thước nhỏ ($d_{molecule} \ll d_{pore}$) khuếch tán vào bên trong lỗ rỗng (Kawakatsu et al., 1993). Lực liên kết tĩnh điện và tương tác Van der Waals giữ các phân tử này trên thành mao quản, làm thu hẹp dần bán kính thủy lực $r_{pore}$.
- Phân loại trạng thái tắc nghẽn:
  - Tắc nghẽn thuận nghịch (Reversible Fouling): Lớp bánh bùn liên kết yếu trên bề mặt ngoài màng, có thể loại bỏ bằng sục khí hoặc rửa nước cơ học.
  - Tắc nghẽn không thuận nghịch vật lý (Irreversible Fouling): Lớp gel đặc quánh và các chất bẩn bám chặt trong mao quản, chỉ có thể loại bỏ bằng dung dịch hóa chất.
  - Tắc nghẽn không phục hồi (Irrecoverable Fouling): Chất bẩn bám vĩnh viễn vào cấu trúc polymer sau thời gian dài vận hành, không thể phục hồi bằng bất kỳ phương pháp nào.

#### 1.2.4 Đặc tính Bùn hoạt tính và Dung dịch Hỗn hợp (Mixed Liquor Characteristics)
- Nồng độ chất rắn lơ lửng trong hỗn hợp bùn (MLSS):
  - Dải nồng độ vận hành điển hình: Hệ thống MBR thường vận hành ở nồng độ MLSS từ 8000 mg/L đến 12000 mg/L.
  - Mối quan hệ phi tuyến với độ nhớt: Nồng độ MLSS tăng cao làm tăng độ nhớt biểu kiến của hỗn dịch sinh học. Độ nhớt cao cản trở quá trình khuếch tán oxy và giảm lực cắt rửa màng của bọt khí.
  - Ảnh hưởng của nồng độ MLSS quá thấp: Nồng độ MLSS thấp dưới 2000 mg/L khiến vi sinh vật chịu tải trọng cao và kích thích giải phóng lượng lớn EPS tự do (Yoon, 2015).
- Chất polyme ngoại bào (Extracellular Polymeric Substances - EPS):
  - Thành phần hóa học: EPS chứa polysaccharide ngoại bào, protein, axit nucleic, lipid và các hợp chất humic do tế bào vi sinh tiết ra.
  - EPS liên kết chặt (Tight-bound EPS - TB-EPS): Nằm sát bề mặt màng tế bào vi khuẩn, đóng vai trò duy trì cấu trúc khung của bông bùn.
  - EPS liên kết lỏng lẻo (Loose-bound EPS - LB-EPS): Phân tán ở lớp ngoài bông bùn. LB-EPS có độ dính cao và là tác nhân chính gây tắc nghẽn màng không thuận nghịch.
- Sản phẩm vi sinh hòa tan (Soluble Microbial Products - SMP):
  - Nguồn gốc phát sinh: SMP là các chất hữu cơ hòa tan giải phóng trong quá trình trao đổi chất của vi sinh vật hoặc do tế bào bị phân giải nội sinh.
  - Phân loại thành phần: SMP bao gồm protein hòa tan (SMPp) và polysaccharide hòa tan (SMPc). Tỷ lệ carbohydrate trên protein ($SMPc/SMPp$) ảnh hưởng trực tiếp đến độ bền gel và khả năng phục hồi của màng lọc.
- Vai trò của cation kim loại hóa trị hai ($Ca^{2+}, Mg^{2+}$):
  - Cơ chế cầu nối cation: Các ion $Ca^{2+}$ và $Mg^{2+}$ liên kết với các nhóm chức tích điện âm (như carboxylate, phosphate) trên chuỗi biopolymer của EPS và SMP.
  - Ổn định cấu trúc bông bùn: Cầu nối ion kết nối các vi hạt thành các bông bùn lớn và đặc chắc, làm giảm lượng chất keo hòa tan tự do trong dung dịch.
  - Rủi ro đóng cặn vô cơ: Nồng độ $Ca^{2+}$ quá cao kết hợp với ion carbonate hoặc phosphate tạo thành lớp cặn vô cơ nén chặt trên bề mặt màng.

#### 1.2.5 Ảnh hưởng của Các Thông số Kỹ thuật Vận hành
- Khái niệm Thông lượng tới hạn (Critical Flux - $J_c$):
  - Định nghĩa thông lượng tới hạn: $J_c$ là giá trị thông lượng phân định giữa chế độ lọc ít tắc nghẽn và chế độ lọc có tốc độ bám bẩn tăng vọt.
  - Vận hành dưới thông lượng tới hạn ($J < J_c$): Tốc độ lắng đọng hạt cặn cân bằng với tốc độ cuốn trôi thủy động lực học, giúp $TMP$ duy trì ổn định.
  - Vận hành vượt thông lượng tới hạn ($J > J_c$): Các hạt cặn tích tụ nhanh chóng trên bề mặt màng, kích hoạt hiện tượng bùng nổ áp suất ($TMP$ jump) và hình thành lớp bánh bùn nén chặt.
- Thời gian lưu nước thủy lực (HRT) và Thời gian lưu giữ bùn (SRT):
  - Dải giá trị vận hành tối ưu: HRT tiêu chuẩn dao động từ 4 đến 12 giờ. SRT tối ưu dao động từ 20 đến 60 ngày (Huang et al., 2011).
  - Tác động của HRT ngắn: HRT ngắn làm tăng tải trọng hữu cơ thể tích, thúc đẩy vi sinh vật sản sinh SMP nhanh hơn tốc độ phân hủy nội sinh.
  - Tác động của SRT cực đoan: SRT dưới 10 ngày làm bùn phân tán và giải phóng nhiều LB-EPS. SRT trên 80 ngày làm bùn bị già hóa, tích tụ nhiều mảnh vụn tế bào chết và cặn khoáng mịn.
- Cường độ sục khí và Ứng suất cắt thủy động lực học (Aeration Scouring):
  - Cơ chế cọ rửa bọt khí: Dòng bọt khí thô tạo ra chuyển động hỗn loạn hai pha khí lỏng dọc theo bề mặt màng lọc.
  - Ứng suất cắt bề mặt ($\tau_w$): Lực cắt thủy động lực học bóc tách lớp cặn bánh bùn lỏng lẻo và đưa các hạt cặn trở lại dòng huyền phù (Liu et al., 2020b).
  - Tối ưu hóa chu kỳ lọc và gián đoạn (Filtration/Relaxation): Chế độ lọc ngắt quãng định kỳ (ví dụ lọc 9 phút, nghỉ sục khí 1 phút) giải phóng sức căng bề mặt và giúp bọt khí cuốn trôi cặn bẩn bám dính.

#### 1.2.6 Phân loại Chiến lược Kiểm soát Tắc nghẽn và Giới hạn Thực tế
- Điều hòa huyền phù bùn (Mixed Liquor Conditioning):
  - Bổ sung chất trợ keo tụ vô cơ: Kỹ sư thêm phèn nhôm hoặc polyaluminium chloride (PAC) để kết tụ các hạt keo và trung hòa điện tích (Wu and Huang, 2008; Juntawang et al., 2017).
  - Bổ sung hạt mang và chất hấp phụ: Bổ sung than hoạt tính bột (PAC) hoặc biochar để hấp phụ SMP và cải thiện khả năng lọc của bùn (Zhang et al., 2017; Zhang et al., 2022).
  - Bổ sung ozone liều lượng thấp: Ozone hóa oxy hóa có chọn lọc các chất hữu cơ hòa tan khó phân hủy và làm giảm độ nhớt bùn (Kurita et al., 2014, 2015).
- Điều chỉnh chế độ thủy động lực học:
  - Tối ưu hóa lưu lượng khí sục: Điều chỉnh tỷ lệ khí trên nước ($SAD_m$ hoặc $SAD_p$) để duy trì lực cắt thích hợp mà không làm vỡ vụn cấu trúc bông bùn.
  - Chu kỳ rửa ngược thủy lực (Backwash): Bơm ngược một phần nước lọc với lưu lượng cao kết hợp sục khí để đẩy các chất bẩn kẹt trong lỗ rỗng ra ngoài.
- Quy trình làm sạch hóa chất (Chemical Cleaning):
  - Rửa hóa chất duy trì (Maintenance Cleaning): Sử dụng hóa chất nồng độ thấp hàng tuần để làm chậm quá trình tích tụ trở lực.
  - Rửa hóa chất phục hồi (Recovery Cleaning): Ngâm màng trong dung dịch axit (axit citric, HCl) để hòa tan muối khoáng và dung dịch kiềm oxy hóa (NaOCl kết hợp NaOH) để phân hủy cặn hữu cơ.
- Hạn chế của phương pháp can thiệp thụ động (A Posteriori Lag):
  - Độ trễ trong phát hiện: Các can thiệp truyền thống chỉ bắt đầu sau khi $TMP$ đã tăng cao rõ rệt trên cảm biến.
  - Hậu quả của can thiệp muộn: Tắc nghẽn sâu trong mao quản đã diễn ra nghiêm trọng, làm giảm hiệu quả phục hồi của hóa chất và lãng phí năng lượng vận hành.
  - Yêu cầu kỹ thuật cấp thiết: Hệ thống cần các mô hình toán học có khả năng cảnh báo sớm nguy cơ tắc nghẽn ngay từ giai đoạn vi mô ban đầu.

### 1.3 Vai trò Chiến lược của Machine Learning trong MBR

#### 1.3.1 Hạn chế của Các Mô hình Cơ chế Toán lý Cổ điển
- Định luật Darcy mở rộng cho lọc màng:
  $$J = \frac{\Delta P}{\mu \cdot R_t}$$
  Trong đó:
  - $J$ là thông lượng dòng thấm ($m \cdot s^{-1}$ hoặc $L \cdot m^{-2} \cdot h^{-1}$).
  - $\Delta P$ là áp suất xuyên màng ($Pa$).
  - $\mu$ là độ nhớt động lực học của nước lọc ($Pa \cdot s$).
  - $R_t$ là tổng trở lực của hệ thống lọc ($m^{-1}$).
- Mô hình trở lực nối tiếp (Resistance-in-Series Model):
  $$R_t = R_m + R_p + R_c$$
  Trong đó:
  - $R_m$ là trở lực thủy lực nội tại của màng sạch ($m^{-1}$).
  - $R_p$ là trở lực gây ra bởi hiện tượng tắc nghẽn mao quản ($m^{-1}$).
  - $R_c$ là trở lực của lớp bánh bùn hình thành trên bề mặt màng ($m^{-1}$).
- Giả định đồng nhất không thực tế: Các mô hình cơ chế giả định lỗ rỗng có hình trụ tròn đồng nhất và chất bẩn là các hạt cầu cứng. Thực tế lỗ rỗng màng có mạng lưới phức tạp và chất bẩn sinh học có tính biến dạng cao.
- Thiếu khả năng tích hợp tương tác sinh học: Định luật Darcy không thể hiện được động học phát triển vi sinh vật, sự biến thiên chất lượng nước thải đầu vào và hoạt tính enzyme.
- Khó khăn trong hiệu chuẩn thông số thời gian thực: Việc đo đạc phân tách các thành phần trở lực $R_p$ và $R_c$ đòi hỏi các phép thử ngoại tuyến gián đoạn, không thể áp dụng cho giám sát trực tuyến liên tục.

#### 1.3.2 Rào cản Kỹ thuật của Các Mô hình Thống kê Truyền thống
- Phương pháp hồi quy bình phương bé nhất từng phần (Partial Least Squares - PLS):
  - Khả năng dự báo hạn chế: Mô hình PLS đạt hệ số xác định $R^2 \approx 0.84$ khi dự báo thông lượng từ các biến nồng độ MLSS, EPS, SMP và kích thước hạt (Zhang et al., 2012).
  - Giả định mối quan hệ tuyến tính: Phương pháp PLS cố định cấu trúc tuyến tính giữa các biến số, bỏ qua các tương tác hiệp đồng phi tuyến phức tạp trong bể sinh học.
- Mô hình chuỗi thời gian tuyến tính (Time Series Models):
  - Ứng dụng điều kiện thực tế: Mô hình tích hợp nhiệt độ và các sự kiện làm sạch màng đạt $R^2 \approx 0.91$ trên hệ thống màng kỵ khí (AnMBR) (Chen et al., 2022).
  - Phụ thuộc kiến thức tiên nghiệm: Mô hình đòi hỏi giả định trước về mối liên hệ giữa các biến số, dễ dẫn đến hiện tượng sai lệch mô hình (model misspecification).
- Năng lực tổng quát hóa kém: Khi điều kiện môi trường thay đổi đột ngột (như sốc tải hữu cơ hoặc nhiệt độ thay đổi theo mùa), mô hình thống kê truyền thống mất độ chính xác nhanh chóng.
- Tốc độ tính toán chậm trên dữ liệu lớn: Cấu trúc toán học cổ điển gặp khó khăn khi xử lý dữ liệu đa biến tần số cao và có độ trễ hội tụ lớn.

#### 1.3.3 Ưu thế Đột phá của Phương pháp Machine Learning trong Dự báo MBR
- Khả năng xấp xỉ hàm phi tuyến phức tạp: Theo Định lý Xấp xỉ Phổ quát (Universal Approximation Theorem), các mô hình học máy có thể mô phỏng chính xác các phản ứng phi tuyến mà không cần định dạng hàm trước.
- Cơ chế mô hình hộp đen định hướng dữ liệu (Data-driven Black-box): Thuật toán học máy tự động khai phá các quy luật ẩn từ dữ liệu thực nghiệm mà không phụ thuộc vào các giả định cơ chế lý hóa nghiêm ngặt (Bishop, 2006).
- Khả năng xử lý dữ liệu cảm biến đa biến tần số cao: Mô hình học máy tiếp nhận và xử lý đồng thời hàng chục thông số vận hành trực tuyến như lưu lượng khí, nồng độ oxy hòa tan (DO), pH, thế oxy hóa khử (ORP), nhiệt độ và $TMP$.
- Khả năng tự học và cập nhật động (Adaptive Continual Learning): Mô hình có thể thích nghi linh hoạt với sự thay đổi của nguồn nước cấp bằng cách định kỳ tái huấn luyện trên các mẫu dữ liệu mới.
- Hỗ trợ phân tích cơ chế tắc nghẽn chuyên sâu: Các thuật toán học máy cung cấp công cụ định lượng mới để đánh giá mức độ đóng góp của từng biến số môi trường vào quá trình tắc nghẽn màng (Niu et al., 2022).
- Cung cấp nền tảng cho điều khiển thông minh: Dự báo sớm hiện tượng bùng nổ áp suất $TMP$ trước nhiều giờ, giúp tối ưu hóa thời điểm sục khí và liều lượng hóa chất làm sạch chính xác.

## 2. Nguyên lý và Phương pháp Học máy trong MBR

### 2.1 Quy trình Xây dựng Mô hình Học máy Tổng quát

#### 2.1.1 Khung Quy trình Chuẩn hóa trong Nghiên cứu MBR
- **Định nghĩa học máy trong kỹ thuật môi trường**: Học máy xây dựng mô hình toán học từ dữ liệu thực nghiệm ("training data"). Mô hình đưa ra dự báo hoặc quyết định vận hành mà không cần giả định cơ chế tiên nghiệm hoặc lập trình quy tắc cố định.
- **Chuỗi quy trình chuẩn hóa gồm 7 bước liên tục**:
  1. **Thu thập dữ liệu (Data acquisition)**: Thu nhận dữ liệu cảm biến đo trực tuyến (áp suất xuyên màng TMP, lưu lượng thấm, nhiệt độ, oxy hòa tan DO, pH) và dữ liệu xét nghiệm phòng thí nghiệm (nồng độ bùn hoạt tính MLSS, nhu cầu oxy hóa học COD, tổng nitơ TN, tổng phospho TP, chất cao phân tử ngoại bào EPS, sản phẩm vi sinh hòa tan SMP).
  2. **Tiền xử lý dữ liệu (Data preprocessing)**: Làm sạch dữ liệu thô. Xử lý giá trị khuyết (missing values) bằng nội suy tuyến tính hoặc thuật toán KNN. Phát hiện và loại bỏ giá trị dị biệt (outliers) bằng phương pháp lọc thống kê ($3\sigma$ hoặc IQR). Chuẩn hóa thang đo đặc trưng về dải $[0, 1]$ bằng Min-Max Scaling hoặc đưa về phân phối chuẩn hóa bằng Z-score Scaling:
     $$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}, \quad z = \frac{x - \mu}{\sigma}$$
  3. **Phân chia tập dữ liệu (Dataset splitting)**: Chia tập dữ liệu thành ba phần độc lập gồm tập huấn luyện (Training set, 70%), tập kiểm định (Validation set, 15%) và tập kiểm tra (Testing set, 15%). Quy trình này ngăn chặn hiện tượng rò rỉ dữ liệu (data leakage).
  4. **Lựa chọn và huấn luyện mô hình (Model selection & training)**: Lựa chọn cấu trúc thuật toán phù hợp với kiểu bài toán (hồi quy thông lượng, phân loại tắc nghẽn màng, dự báo chuỗi thời gian). Mô hình học các trọng số tham số nội tại từ tập huấn luyện.
  5. **Tối ưu hóa siêu tham số (Hyperparameter optimization)**: Tinh chỉnh các tham số cấu trúc mô hình bằng kỹ thuật tìm kiếm lưới (Grid Search), tìm kiếm ngẫu nhiên (Random Search), kiểm định chéo $k$-fold ($k$-fold Cross-Validation), hoặc kết hợp các thuật toán tối ưu hóa thông minh (GA, PSO, GWO).
  6. **Đánh giá hiệu năng mô hình (Model evaluation)**: Đo lường độ chính xác và sai số trên tập kiểm tra độc lập bằng các chỉ số thống kê định lượng ($R^2$, RMSE, MAE, MAPE).
  7. **Triển khai và giám sát thực tế (Model deployment & monitoring)**: Tích hợp mô hình vào hệ thống điều khiển giám sát tự động SCADA của nhà máy MBR. Mô hình cảnh báo sớm tốc độ tắc nghẽn màng và tự động điều chỉnh chu kỳ rửa ngược hoặc lưu lượng sục khí.

#### 2.1.2 Phân loại Các Phương thức Học máy trong MBR
- **Học có giám sát (Supervised Learning)**:
  - **Bản chất**: Tập dữ liệu huấn luyện chứa cặp biến đầu vào và nhãn đích tương ứng: $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$.
  - **Bài toán hồi quy (Regression)**: Đầu ra $y$ là biến liên tục. Ứng dụng dự báo áp suất xuyên màng TMP, thông lượng lọc $J$, tốc độ tăng trở lực màng $dR/dt$, nồng độ COD và amoni trong nước sau xử lý.
  - **Bài toán phân loại (Classification)**: Đầu ra $y$ là nhãn rời rạc. Ứng dụng nhận diện các giai đoạn nghẹt màng (nghẹt thuận nghịch, nghẹt không thuận nghịch), phân loại chất bám bẩn (hữu cơ, vô cơ, sinh học), chẩn đoán lỗi thiết bị cảm biến.
- **Học không giám sát (Unsupervised Learning)**:
  - **Bản chất**: Tập dữ liệu chỉ chứa các biến đặc trưng đầu vào không có nhãn đích: $\mathcal{D} = \{x_i\}_{i=1}^N$.
  - **Phân cụm dữ liệu (Clustering)**: Gom nhóm các mẫu nước thải hoặc đặc tính bùn có tính chất tương đồng bằng thuật toán $k$-Means hoặc Phân cụm phân cấp (Hierarchical Clustering).
  - **Giảm số chiều (Dimensionality reduction)**: Nén dữ liệu nhiều chiều từ phổ huỳnh quang 3D-EEM hoặc ảnh hiển vi mà vẫn giữ lại phần lớn phương sai thông qua phân tích thành phần chính (PCA) hoặc t-SNE.
  - **Phát hiện dị biệt (Anomaly detection)**: Nhận diện các điểm vận hành bất thường hoặc hỏng hóc cảm biến dựa trên mật độ phân bố dữ liệu.
- **Học tăng cường (Reinforcement Learning - RL)**:
  - **Bản chất**: Tác tử học máy (Agent) tự động tương tác với môi trường bể phản ứng sinh học màng (Environment) theo cơ chế thử và sai thông qua Quá trình Quyết định Markov (Markov Decision Process - MDP).
  - **Cơ chế hoạt động**: Tại mỗi bước thời gian $t$, tác tử quan sát trạng thái hệ thống $s_t \in \mathcal{S}$ (TMP, DO, mực bùn), thực hiện hành động điều khiển $a_t \in \mathcal{A}$ (tốc độ bơm hút, cường độ sục khí bọt khí), và nhận tín hiệu phần thưởng $r_t \in \mathbb{R}$ (tiết kiệm năng lượng điện, kéo dài chu kỳ lọc).
  - **Mục tiêu**: Tối đa hóa tổng phần thưởng tích lũy có chiết khấu theo thời gian:
    $$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}, \quad \gamma \in [0, 1)$$

---

### 2.2 Các Thuật toán Học máy Cốt lõi

#### 2.2.1 Máy Vector Hỗ trợ (Support Vector Machine - SVM / SVR)
- **Nền tảng lý thuyết học thống kê**:
  - Do Vapnik phát triển dựa trên Nguyên lý Cực tiểu hóa Rủi ro Cấu trúc (Structural Risk Minimization - SRM).
  - Khác với mạng nơ-ron truyền thống áp dụng Nguyên lý Cực tiểu hóa Rủi ro Thực nghiệm (Empirical Risk Minimization - ERM), SRM tối ưu hóa đồng thời sai số huấn luyện và độ phức tạp mô hình. SRM kiểm soát cận trên của sai số khái quát hóa, giúp ngăn chặn hiện tượng quá khớp (overfitting).
- **Nguyên lý siêu phẳng phân tách và biên cực đại**:
  - Dữ liệu đầu vào được ánh xạ phi tuyến từ không gian gốc sang không gian đặc trưng Hilbert nhiều chiều qua hàm $\Phi(x)$.
  - Phương trình siêu phẳng hồi quy tuyến tính trong không gian đặc trưng:
    $$f(x) = \langle w, \Phi(x) \rangle + b$$
  - Khoảng cách hình học của dải biên bằng $\frac{2}{||w||}$. Việc cực đại hóa biên tương đương với bài toán cực tiểu hóa chuẩn Euclid $\frac{1}{2} ||w||^2$.
- **Hàm mất mát không nhạy cảm $\epsilon$ ($\epsilon$-insensitive loss function)**:
  - Mô hình chấp nhận sai số dự báo nằm trong dải ống độ rộng $\pm\epsilon$ xung quanh siêu phẳng:
    $$L_\epsilon(y, f(x)) = |y - f(x)|_\epsilon = \max(0, |y - f(x)| - \epsilon) = \begin{cases} 0, & \text{nếu } |y - f(x)| \le \epsilon \\ |y - f(x)| - \epsilon, & \text{ngược lại} \end{cases}$$
  - Các điểm dữ liệu nằm trong dải ống $\epsilon$ không tạo ra chi phí phạt sai số.
  - Các điểm dữ liệu nằm ngoài dải ống $\epsilon$ vi phạm biên và được đo lường bằng hai biến bù sai số $\xi_i, \xi_i^* \ge 0$.
- **Bài toán tối ưu hóa lồi SVR**:
  - Công thức bài toán gốc (Primal optimization problem):
    $$\min_{w, b, \xi, \xi^*} \frac{1}{2} ||w||^2 + C \sum_{i=1}^l (\xi_i + \xi_i^*)$$
    thỏa mãn các điều kiện ràng buộc:
    $$\begin{cases} y_i - \langle w, \Phi(x_i) \rangle - b \le \epsilon + \xi_i \\ \langle w, \Phi(x_i) \rangle + b - y_i \le \epsilon + \xi_i^* \\ \xi_i, \xi_i^* \ge 0, \quad \forall i = 1, \dots, l \end{cases}$$
  - Công thức bài toán đối ngẫu Lagrange (Dual formulation):
    $$\max_{\alpha, \alpha^*} -\frac{1}{2} \sum_{i,j=1}^l (\alpha_i - \alpha_i^*)(\alpha_j - \alpha_j^*) K(x_i, x_j) - \epsilon \sum_{i=1}^l (\alpha_i + \alpha_i^*) + \sum_{i=1}^l y_i (\alpha_i - \alpha_i^*)$$
    thỏa mãn:
    $$\sum_{i=1}^l (\alpha_i - \alpha_i^*) = 0 \quad \text{và} \quad 0 \le \alpha_i, \alpha_i^* \le C$$
  - Hàm dự báo cuối cùng chỉ phụ thuộc vào tích vô hướng giữa các điểm dữ liệu:
    $$f(x) = \sum_{i=1}^l (\alpha_i - \alpha_i^*) K(x_i, x) + b$$
  - Các điểm có $(\alpha_i - \alpha_i^*) \neq 0$ nằm tại hoặc ngoài biên dải $\epsilon$ đóng vai trò là các vector hỗ trợ (Support Vectors).
- **Hàm nhân phi tuyến (Kernel Trick)**:
  - Hàm nhân RBF (Radial Basis Function - hàm nhân Gauss):
    $$K(x, x_i) = \exp(-\gamma ||x - x_i||^2) = \exp\left(-\frac{||x - x_i||^2}{2\sigma^2}\right)$$
  - RBF ánh xạ dữ liệu đầu vào vào không gian đặc trưng vô hạn chiều. Hàm nhân này xử lý hiệu quả các quan hệ phi tuyến phức tạp trong cơ chế nghẹt màng MBR.
- **Vai trò của hai siêu tham số then chốt**:
  - **Tham số phạt $C$ ($C > 0$)**: Cân bằng giữa độ phẳng của hàm hồi quy ($||w||^2$) và mức phạt cho các điểm vượt quá giới hạn sai số $\epsilon$. Giá trị $C$ quá lớn khiến mô hình quá khớp với dữ liệu nhiễu; giá trị $C$ quá nhỏ khiến mô hình bị thiếu khớp (underfitting).
  - **Hệ số nhân $\gamma$ ($\gamma = \frac{1}{2\sigma^2}$)**: Quyết định bán kính ảnh hưởng của từng vector hỗ trợ đơn lẻ. Giá trị $\gamma$ lớn tạo ra bề mặt quyết định cục bộ và uốn lượn; giá trị $\gamma$ nhỏ tạo ra bề mặt quyết định quá phẳng, mất khả năng nắm bắt dao động thực tế.
- **Phạm vi ứng dụng và đặc điểm thực nghiệm trong MBR**:
  - Ưu thế vượt trội khi mẫu dữ liệu nhỏ ($N < 125$ mẫu thực nghiệm) như đã chứng minh bởi Qian và cộng sự (2015).
  - Ứng dụng chính: Dự báo áp suất xuyên màng TMP, dự báo tổng trở lực màng $R_t$, nhận diện rò rỉ hệ thống đường ống, cảnh báo sớm ô nhiễm nguồn nước cấp (Liu et al., 2020a).
  - Hạn chế: Rất nhạy cảm với dữ liệu khuyết; độ phức tạp tính toán xấp xỉ $\mathcal{O}(N^3)$, không phù hợp khi số lượng mẫu dữ liệu quá lớn ($N > 10^5$).

#### 2.2.2 Mạng Nơ-ron Nhân tạo (Artificial Neural Network - ANN)
- **Kiến trúc ba tầng cơ bản**:
  - **Tầng vào (Input layer)**: Tiếp nhận các biến quá trình MBR (thời gian lưu bùn SRT, thời gian lưu nước HRT, nồng độ bùn MLSS, nhiệt độ, pH, DO, thông lượng).
  - **Tầng ẩn (Hidden layers)**: Thực hiện tính toán tổ hợp tuyến tính và biến đổi phi tuyến qua hàm kích hoạt. Số lượng tầng ẩn xác định độ sâu (depth), số nơ-ron trong một tầng xác định độ rộng (width) của mạng.
  - **Tầng ra (Output layer)**: Xuất kết quả dự báo (giá trị TMP tương lai, nồng độ chất lượng nước đầu ra, sản lượng khí sinh học methane).
- **Mô hình toán học của nơ-ron nhân tạo**:
  $$z = \sum_{j=1}^n w_j x_j + b = w^T x + b, \quad a = f(z)$$
  trong đó $w_j$ là trọng số liên kết, $b$ là độ lệch (bias), $f(\cdot)$ là hàm kích hoạt phi tuyến.
- **Các hàm kích hoạt thông dụng**:
  - Hàm Sigmoid (Logistic): $\sigma(z) = \frac{1}{1 + e^{-z}}$, xuất giá trị trong khoảng $(0, 1)$, dễ gây bão hòa và triệt tiêu đạo hàm khi $|z|$ lớn.
  - Hàm Tanh (Hyperbolic Tangent): $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$, xuất giá trị trong khoảng $(-1, 1)$, đối xứng qua gốc tọa độ.
  - Hàm ReLU (Rectified Linear Unit): $\text{ReLU}(z) = \max(0, z)$, giải quyết hiện tượng triệt tiêu đạo hàm đối với miền giá trị dương, tăng tốc độ hội tụ.
- **Mạng Perceptron Đa tầng (MLP) và Mạng Lan truyền Ngược Sai số (BPNN)**:
  - Lan truyền tiến: Dữ liệu tính toán từ tầng vào qua các tầng ẩn đến tầng ra.
  - Lan truyền ngược (Backpropagation): Sai số đầu ra được lan truyền ngược về từng tầng để tính đạo hàm riêng $\frac{\partial E}{\partial w_{ij}}$ dựa trên quy tắc chuỗi (chain rule).
  - Thuật toán Giảm độ dốc (Gradient Descent):
    $$w^{(t+1)} = w^{(t)} - \eta \nabla E(w^{(t)})$$
    với $\eta$ là tốc độ học (learning rate).
  - Thuật toán Levenberg-Marquardt (LM): Kết hợp giữa phương pháp Gradient Descent và phương pháp Gauss-Newton. Thuật toán LM sử dụng ma trận xấp xỉ Hessian để cập nhật trọng số:
    $$\Delta w = (J^T J + \mu I)^{-1} J^T e$$
    trong đó $J$ là ma trận Jacobian của các đạo hàm riêng sai số, $\mu$ là tham số điều chỉnh độ dốc giảm, $I$ là ma trận đơn vị, $e$ là vector sai số huấn luyện. Thuật toán LM tăng tốc độ hội tụ nhanh hơn hàng chục lần so với Gradient Descent cổ điển trên mạng quy mô nhỏ và vừa.
- **Mạng Nơ-ron Hàm Cơ sở Xuyên tâm (RBFNN)**:
  - Cấu trúc ba tầng: Tầng vào, một tầng ẩn phi tuyến duy nhất dùng hàm cơ sở đối xứng tâm, và một tầng ra tuyến tính.
  - Hàm kích hoạt Gaussian tại nơ-ron ẩn thứ $j$:
    $$\phi_j(x) = \exp\left(-\frac{||x - c_j||^2}{2\sigma_j^2}\right)$$
    với $c_j$ là vector tâm và $\sigma_j$ là độ rộng của hàm Gaussian.
  - Tầng ra tính toán tổng tuyến tính:
    $$y = \sum_{j=1}^m w_j \phi_j(x) + b$$
  - Ưu thế: Khả năng xấp xỉ tối ưu cục bộ, không gặp vấn đề kẹt cực trị địa phương như BPNN, tốc độ huấn luyện nhanh do có thể xác định tâm bằng $k$-means và xác định trọng số tầng ra bằng giải hệ phương trình tuyến tính.
- **Mạng Nơ-ron Tích chập (Convolutional Neural Network - CNN)**:
  - Kiến trúc chuyên biệt xử lý dữ liệu lưới không gian và hình ảnh:
    1. **Lớp tích chập (Convolutional layer)**: Quét các bộ lọc (kernels) qua ma trận đầu vào để tính tích chập hai chiều:
       $$S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(i-m, j-n) K(m, n)$$
    2. **Lớp gộp (Pooling layer)**: Sử dụng Max-pooling hoặc Average-pooling để giảm kích thước không gian đặc trưng, giảm tải số lượng tham số và tăng tính bất biến với phép dịch chuyển.
    3. **Lớp kết nối đầy đủ (Fully connected layer)**: Tổng hợp các đặc trưng bậc cao thành giá trị đầu ra.
  - Các cấu trúc cải tiến tiêu biểu: GoogLeNet, DenseNet, ResNet (Wide Residual Networks), CNN hai kênh (dual-channel CNN).
  - Ứng dụng trong MBR: Trích xuất đặc trưng hình thái bề mặt màng từ ảnh hiển vi điện tử quét (SEM) hoặc kính hiển vi lực nguyên tử (AFM); nhận diện mẫu huỳnh quang từ ma trận phổ huỳnh quang kích thích - phát xạ (EEM) để định lượng thành phần protein-like và humic-like gây nghẹt màng (Ma et al., 2023).
- **Mạng Nơ-ron Hồi quy (RNN) và Mạng Bộ nhớ Ngắn-Dài hạn (LSTM)**:
  - RNN truyền thống lưu trạng thái ẩn qua bước thời gian: $h_t = \tanh(W x_t + U h_{t-1} + b)$. RNN thường gặp hiện tượng tiêu biến đạo hàm (vanishing gradient) khi chuỗi thời gian dài.
  - Mạng LSTM khắc phục triệt để bằng cấu trúc tế bào nhớ (Cell State $C_t$) kết hợp cơ chế ba cổng điều khiển:
    1. **Cổng quên (Forget gate)**: Quyết định tỷ lệ loại bỏ thông tin cũ từ trạng thái tế bào trước:
       $$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
    2. **Cổng vào (Input gate)**: Quyết định lượng thông tin mới được nạp vào tế bào nhớ:
       $$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
       $$\tilde{C}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$$
    3. **Cập nhật trạng thái tế bào (Cell state update)**: Kết hợp thông tin giữ lại và thông tin nạp mới:
       $$C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$$
    4. **Cổng ra (Output gate)**: Quyết định giá trị trạng thái ẩn xuất ra ngoài:
       $$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$
       $$h_t = o_t * \tanh(C_t)$$
  - Ứng dụng trong MBR: Dự báo chuỗi thời gian áp suất TMP động học nhiều bước thời gian tiếp theo, dự báo sự suy giảm thông lượng thấm và dự báo động học sinh khí biogas trong bể phản ứng sinh học màng kỵ khí (AnMBR).
- **Mạng Nơ-ron Wavelet (WNN)**:
  - Thay thế hàm kích hoạt truyền thống bằng hàm wavelet (như Morlet wavelet):
    $$\psi_{a, b}(x) = \frac{1}{\sqrt{|a|}} \psi\left(\frac{x - b}{a}\right)$$
  - Ưu thế: Khả năng phân tích cục bộ đồng thời cả miền thời gian và miền tần số; tốc độ hội tụ nhanh hơn MLP truyền thống và hạn chế tối đa nguy cơ rơi vào cực tiểu cục bộ.
- **Tổng kết ứng dụng ANN trong MBR**:
  - Dự báo chất lượng nước đầu ra (COD, $\text{NH}_4^+$-N) và sản lượng khí sinh học methane (Li et al., 2022).
  - Dự báo thông lượng lọc và tỷ lệ phục hồi thông lượng sau rửa màng (Zhao et al., 2020).
  - Phân loại cơ chế nghẹt màng (Shi et al., 2022).
  - Thách thức: Mô hình dạng "hộp đen" (black-box), khó diễn giải cơ chế hóa lý trực tiếp, đòi hỏi cấu hình mạng phức tạp và có nguy cơ quá khớp khi dữ liệu nhỏ.

#### 2.2.3 Cây Quyết định và Học kết hợp (Decision Tree & Ensemble Learning)
- **Cây Quyết định Phân loại và Hồi quy (CART)**:
  - Cấu trúc dạng cây phân cấp nhị phân gồm nút gốc (root node), nút nội bộ (internal nodes) và nút lá (leaf nodes). Mỗi nút nội bộ thực hiện một phép kiểm tra logic dạng if-then trên một thuộc tính đầu vào đơn lẻ.
  - **Tiêu chuẩn phân tách cho bài toán phân loại**:
    - Chỉ số bất thuần Gini (Gini Impurity):
      $$\text{Gini}(D) = 1 - \sum_{k=1}^K p_k^2$$
      với $p_k$ là tỷ lệ mẫu thuộc lớp $k$ trong tập dữ liệu $D$. Thuật toán chọn thuộc tính phân tách tối đa hóa độ giảm chỉ số Gini: $\Delta \text{Gini} = \text{Gini}(D) - \frac{|D_1|}{|D|} \text{Gini}(D_1) - \frac{|D_2|}{|D|} \text{Gini}(D_2)$.
    - Độ hỗn loạn thông tin (Entropy):
      $$H(D) = -\sum_{k=1}^K p_k \log_2(p_k)$$
  - **Tiêu chuẩn phân tách cho bài toán hồi quy**:
    - Cực tiểu hóa tổng bình phương sai số (MSE reduction):
      $$\min_{j, s} \left[ \sum_{x_i \in R_1(j, s)} (y_i - c_1)^2 + \sum_{x_i \in R_2(j, s)} (y_i - c_2)^2 \right]$$
      trong đó $j$ là biến phân tách, $s$ là điểm ngưỡng cắt, $c_1, c_2$ là trung bình giá trị đích tại hai vùng không gian con $R_1$ và $R_2$.
  - Ưu nhược điểm: Mô hình có tính minh bạch cao, dễ diễn giải trực quan cho kỹ sư vận hành. Tuy nhiên, một cây quyết định đơn lẻ rất dễ bị quá khớp (overfitting) và kém ổn định trước nhiễu nhỏ trong dữ liệu. Khắc phục bằng kỹ thuật cắt tỉa cành (pruning) và kiểm định chéo (cross-validation).
- **Rừng Ngẫu nhiên (Random Forest - RF)**:
  - Hoạt động dựa trên cơ chế kết hợp Đóng bao (Bagging - Bootstrap Aggregating).
  - Thuật toán rút mẫu ngẫu nhiên có hoàn lại (bootstrap sampling) để tạo ra $B$ tập dữ liệu huấn luyện con độc lập từ tập dữ liệu gốc.
  - Áp dụng phương pháp Không gian con Ngẫu nhiên (Random Subspace Method): Tại mỗi nút phân nhánh của mỗi cây, chỉ chọn ngẫu nhiên một tập con gồm $m$ thuộc tính (thường $m \approx \sqrt{p}$ đối với phân loại hoặc $m \approx p/3$ đối với hồi quy) trong tổng số $p$ thuộc tính đầu vào để tìm điểm cắt tối ưu.
  - Đầu ra tổng hợp:
    $$\hat{y}_{\text{RF}} = \frac{1}{B} \sum_{b=1}^B T_b(x)$$
  - Cơ chế giảm phương sai: Việc lấy mẫu ngẫu nhiên và chọn tập đặc trưng con giúp giảm đáng kể hệ số tương quan giữa các cây thành phần. Phương sai của mô hình tổ hợp giảm theo công thức:
    $$\text{Var}(\bar{X}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$
    khi số cây $B$ tăng và độ tương quan $\rho$ giảm, phương sai mô hình tiệm cận về $\rho \sigma^2$, giúp chống quá khớp vượt trội.
  - Cung cấp đánh giá tầm quan trọng của đặc trưng (Feature Importance) dựa trên độ giảm chỉ số Gini trung bình hoặc mức tăng sai số ngoài bao (Out-Of-Bag - OOB error) khi xáo trộn giá trị đặc trưng.
- **Cây Quyết định Tăng cường Độ dốc (GBDT) và XGBoost**:
  - **Cơ chế Tăng cường (Boosting)**: Xây dựng tuần tự các mô hình học yếu (base learners). Cây quyết định mới được huấn luyện để dự báo và bù đắp sai số phần dư (residuals) của toàn bộ các cây xây dựng trước đó:
    $$f_m(x) = f_{m-1}(x) + \eta h_m(x)$$
    với $h_m(x)$ là cây ước lượng phần dư và $\eta$ là tốc độ co hẹp (shrinkage / learning rate).
  - **Thuật toán XGBoost (eXtreme Gradient Boosting)**:
    - Mở rộng hàm mục tiêu bằng khai triển Taylor bậc hai quanh giá trị dự báo hiện tại $\hat{y}_i^{(t-1)}$:
      $$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$
      trong đó $g_i$ và $h_i$ là đạo hàm bậc một (gradient) và đạo hàm bậc hai (Hessian) của hàm mất mát:
      $$g_i = \frac{\partial l(y_i, \hat{y}^{(t-1)})}{\partial \hat{y}^{(t-1)}}, \quad h_i = \frac{\partial^2 l(y_i, \hat{y}^{(t-1)})}{\partial (\hat{y}^{(t-1)})^2}$$
    - Hàm phạt kiểm soát độ phức tạp cấu trúc cây $\Omega(f_t)$:
      $$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
      với $T$ là số lượng nút lá, $w_j$ là điểm trọng số tại lá thứ $j$, $\gamma$ là hệ số phạt bổ sung nút lá mới, $\lambda$ là hệ số chính quy hóa chuẩn $L_2$ trên trọng số lá.
    - Điểm trọng số tối ưu tại nút lá $j$:
      $$w_j^* = -\frac{G_j}{H_j + \lambda}, \quad G_j = \sum_{i \in I_j} g_i, \quad H_j = \sum_{i \in I_j} h_i$$
    - Công thức tính độ lợi phân tách (Split Gain) tại mỗi nút:
      $$\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$
      nếu $\text{Gain} \le 0$, thuật toán dừng phân nhánh (tự động cắt tỉa).
  - Ưu thế vượt bậc: Tính toán phân tán song song, tự động xử lý giá trị khuyết, chính quy hóa bậc hai chống quá khớp hiệu quả, độ chính xác dự báo cao nhất trong các bảng dữ liệu vận hành.
- **Ứng dụng cây quyết định và học kết hợp trong MBR**:
  - Dự báo chất lượng nước đầu ra nhà máy MBR (Zhuang et al., 2021).
  - Dự báo suy giảm thông lượng lọc (Li et al., 2020).
  - Hỗ trợ ra quyết định vận hành và đánh giá độ quan trọng của các thông số điều khiển (Jiang et al., 2021).

#### 2.2.4 Thuật toán k Láng giềng Gần nhất (KNN)
- **Nguyên lý học lười (Lazy learning / Instance-based learning)**:
  - Thuật toán không xây dựng hàm ánh xạ toàn cục trong pha huấn luyện. Quá trình học thực chất là việc lưu trữ toàn bộ tập dữ liệu mẫu vào bộ nhớ.
  - Phép tính dự báo chỉ bắt đầu khi nhận được một điểm truy vấn mới $x_{\text{query}}$.
- **Đo lường khoảng cách trong không gian đặc trưng**:
  - Khoảng cách Euclid (Euclidean distance):
    $$d(x, y) = \sqrt{\sum_{i=1}^p (x_i - y_i)^2} = ||x - y||_2$$
  - Khoảng cách Manhattan: $d(x, y) = \sum_{i=1}^p |x_i - y_i|$.
  - Khoảng cách Minkowski tổng quát: $d(x, y) = \left( \sum_{i=1}^p |x_i - y_i|^q \right)^{1/q}$.
- **Cơ chế ra quyết định dự báo**:
  - Tìm tập hợp $N_k(x)$ chứa $k$ điểm dữ liệu mẫu có khoảng cách ngắn nhất đến $x$.
  - Bài toán phân loại: Bỏ phiếu theo đa số:
    $$y = \arg\max_{c} \sum_{i \in N_k(x)} I(y_i = c)$$
  - Bài toán hồi quy: Tính trung bình có trọng số nghịch đảo khoảng cách:
    $$\hat{y} = \frac{\sum_{i \in N_k(x)} w_i y_i}{\sum_{i \in N_k(x)} w_i}, \quad w_i = \frac{1}{d(x, x_i) + \varepsilon}$$
- **Đặc tính kỹ thuật và hạn chế**:
  - Ưu điểm: Đơn vị thuật toán đơn giản; không yêu cầu giả định phân phối xác suất tiên nghiệm; không nhạy với nhiễu cục bộ khi chọn $k$ hợp lý.
  - Nhược điểm: Độ phức tạp tính toán và bộ nhớ lớn ở pha suy luận $\mathcal{O}(N \cdot p)$; rất nhạy cảm với thang đo đặc trưng (bắt buộc phải chuẩn hóa dữ liệu trước); hiệu năng suy giảm nghiêm trọng khi số chiều đặc trưng lớn (hiện tượng lời nguyền số chiều - curse of dimensionality).
- **Ứng dụng trong MBR**:
  - Sàng lọc và loại bỏ giá trị ngoại lai của dữ liệu cảm biến MBR (Table 1).
  - Giám sát chất lượng nước và hỗ trợ điều khiển hệ thống xử lý nước thải (Uddin et al., 2023; Xu et al., 2022).

#### 2.2.5 Các Phương pháp Học máy Khác (Other ML Methods)
- **Hồi quy Tuyến tính Đa biến (Multiple Linear Regression - MLR)**:
  - Mô hình tham số biểu diễn quan hệ tuyến tính:
    $$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p + \epsilon$$
  - Ước lượng vector hệ số $\beta$ bằng phương pháp Bình phương Tối thiểu Thông thường (Ordinary Least Squares - OLS):
    $$\hat{\beta} = (X^T X)^{-1} X^T y$$
  - Đóng vai trò là mô hình mốc chuẩn (baseline) để so sánh hiệu năng với các thuật toán học máy phi tuyến phức tạp trong MBR.
- **Hồi quy Phi tuyến (Nonlinear Regression)**:
  - Khớp các phương trình bán thực nghiệm hoặc phương trình vật lý (mô hình điện trở lọc màng Darcy, mô hình các cơ chế nghẹt màng Hermia: nghẹt hoàn toàn, nghẹt trung gian, nghẹt tiêu chuẩn, hình thành bánh bùn) vào dữ liệu thông qua giải thuật Gauss-Newton hoặc Levenberg-Marquardt.
- **Thuật toán Naive Bayes**:
  - Dựa trên Định lý Xác suất Bayes và giả định độc lập có điều kiện giữa các biến đặc trưng:
    $$P(y|x_1, \dots, x_p) = \frac{P(y) \prod_{j=1}^p P(x_j|y)}{P(x_1, \dots, x_p)}$$
  - Tốc độ huấn luyện và phân loại tức thời, sử dụng tốt trong phân loại nhị phân trạng thái vận hành màng (bình thường / tắc nghẽn nghiêm trọng).
- **Học Tăng cường Nâng cao (Advanced Reinforcement Learning - RL)**:
  - Áp dụng các thuật toán Deep Q-Network (DQN) hoặc Actor-Critic (DDPG, PPO) để điều khiển liên tục hệ thống MBR.
  - Ứng dụng: Tự động hóa quá trình loại bỏ phospho sinh học (Mohammadi et al., 2024), tối ưu hóa lưu lượng sục khí định kỳ, giảm thiểu điện năng tiêu thụ từ 15% đến 30% mà vẫn đảm bảo độ bền của màng.
- **Mô hình Nền tảng và Mô hình Lớn (Foundation & Large Models)**:
  - Các mạng nơ-ron quy mô tham số khổng lồ (hàng tỷ tham số), được tiền huấn luyện trên lượng dữ liệu lớn và có khả năng giải quyết đa nhiệm.
  - Ứng dụng: Dự báo xu hướng biến đổi khí hậu ảnh hưởng đến nguồn nước cấp, mô hình hóa phát thải khí nhà kính methane toàn cầu từ các công trình xử lý sinh học (Rouet-Leduc & Hulbert, 2024), phát triển trợ lý ảo hỗ trợ vận hành hệ thống MBR.
- **Học máy Tự động (Automated Machine Learning - AutoML)**:
  - Tự động hóa toàn diện chu trình học máy: Tiền xử lý dữ liệu $\rightarrow$ Trích xuất và chọn lọc đặc trưng $\rightarrow$ Tìm kiếm cấu trúc mô hình tối ưu $\rightarrow$ Tối ưu siêu tham số $\rightarrow$ Tích hợp mô hình (Salehin et al., 2024).
  - Giảm thiểu nhu cầu can thiệp thủ công của chuyên gia dữ liệu, nâng cao tốc độ triển khai mô hình học máy trong dự báo chất lượng nước và kiểm soát MBR (Senthil Kumar et al., 2024).

#### 2.2.6 Các Thuật toán Tối ưu hóa Thông minh Liên quan (Related Optimization Algorithms)
- **Hệ Logic Mờ (Fuzzy Logic) và Mạng Nơ-ron Mờ (FNN)**:
  - Logic mờ mô phỏng tư duy định tính của con người bằng cách gán cho mỗi biến một giá trị chân lý thuộc đoạn $[0, 1]$ thông qua hàm thuộc tính (membership functions: hình tam giác, hình thang, hàm Gauss).
  - Cấu trúc hệ mờ gồm 4 khối: Khối mờ hóa (Fuzzification) $\rightarrow$ Khối cơ sở luật If-Then $\rightarrow$ Động cơ suy luận mờ (Mamdani hoặc Sugeno) $\rightarrow$ Khối giải mờ (Defuzzification).
  - Mạng nơ-ron mờ (Fuzzy Neural Network - FNN): Kết hợp khả năng diễn giải bằng quy tắc mờ của Logic mờ với năng lực tự học từ dữ liệu của ANN. FNN sinh ra cơ sở tri thức chuyên gia từ dữ liệu vận hành có độ bất định và nhiễu lớn trong hệ thống MBR (de Campos Souza, 2020).
- **Phương pháp Mô phỏng Monte Carlo**:
  - Phương pháp tính toán số học dựa trên lý thuyết xác suất và Định lý Số lớn (Law of Large Numbers):
    $$\bar{X}_N = \frac{1}{N} \sum_{i=1}^N f(X_i) \xrightarrow{P} \mathbb{E}[f(X)]$$
  - Cơ chế: Thực hiện lấy mẫu ngẫu nhiên hàng nghìn đến hàng triệu lần từ các phân phối xác suất của biến đầu vào (nhiệt độ nước, chất lượng nước thải đầu vào dao động) để mô phỏng phân phối độ bất định của đầu ra (tuổi thọ màng, chi phí vận hành).
  - Kết hợp với học tăng cường (như thuật toán tìm kiếm cây Monte Carlo - MCTS trong AlphaGo, Silver et al., 2016) nhằm tăng cường năng lực ra quyết định điều khiển tối ưu trong điều kiện thiếu dữ liệu chính xác.
- **Giải thuật Di truyền (Genetic Algorithm - GA)**:
  - Thuật toán tìm kiếm ngẫu nhiên mô phỏng quá trình tiến hóa sinh học tự nhiên của Darwin (Katoch et al., 2021).
  - **Mã hóa cá thể**: Các siêu tham số (như cặp $[C, \gamma]$ của SVM hoặc số nơ-ron tầng ẩn và tốc độ học của ANN) được mã hóa thành chuỗi nhiễm sắc thể (dạng nhị phân hoặc vector số thực).
  - **Hàm thích nghi (Fitness function)**: Định nghĩa dựa trên sai số của mô hình học máy, ví dụ: $\text{Fitness} = \frac{1}{\text{RMSE} + \epsilon}$ hoặc $\text{Fitness} = R^2$.
  - **Các toán tử tiến hóa cốt lõi**:
    1. **Toán tử chọn lọc (Selection)**: Lựa chọn các cá thể có độ thích nghi cao vào quần thể sinh sản qua cơ chế Bánh xe Roulette (Roulette Wheel Selection) hoặc Chọn lọc Giải đấu (Tournament Selection).
    2. **Toán tử lai ghép (Crossover)**: Trao đổi đoạn gen giữa hai nhiễm sắc thể cha mẹ với xác suất lai ghép $P_c \in [0.6, 0.9]$ để sinh ra các cá thể con mới.
    3. **Toán tử đột biến (Mutation)**: Biến đổi ngẫu nhiên một hoặc nhiều gen trong nhiễm sắc thể với xác suất đột biến nhỏ $P_m \in [0.001, 0.05]$. Toán tử này duy trì tính đa dạng di truyền của quần thể và ngăn ngừa bầy rơi vào cực tiểu cục bộ.
- **Tối ưu hóa Bầy đàn (Particle Swarm Optimization - PSO)**:
  - Mô phỏng hành vi di chuyển tìm mồi có tính xã hội của đàn chim hoặc đàn cá (Eberhart & Kennedy).
  - Mỗi hạt trong bầy đại diện cho một nghiệm siêu tham số trong không gian tìm kiếm đa chiều. Hạt sở hữu vị trí hiện tại $x_i^t$ và vector vận tốc $v_i^t$.
  - **Công thức cập nhật vận tốc và vị trí**:
    $$v_{i}^{t+1} = w v_i^t + c_1 r_1 (pbest_i - x_i^t) + c_2 r_2 (gbest - x_i^t)$$
    $$x_i^{t+1} = x_i^t + v_i^{t+1}$$
    trong đó:
    - $w$: Hệ số quán tính (inertia weight), điều khiển khả năng cân bằng giữa thăm dò toàn cục (exploration) và khai thác cục bộ (exploitation).
    - $c_1$: Hệ số học tập nhận thức cá nhân (cognitive parameter), thúc đẩy hạt quay lại vị trí tốt nhất trong lịch sử bản thân $pbest_i$.
    - $c_2$: Hệ số học tập xã hội (social parameter), hướng hạt di chuyển về phía vị trí tốt nhất của toàn bộ bầy $gbest$.
    - $r_1, r_2$: Các số ngẫu nhiên phân bố đều trong khoảng $[0, 1]$.
  - Ưu thế: Cấu trúc toán học đơn giản, dễ cài đặt, không cần tính toán ma trận đạo hàm, tốc độ hội tụ nhanh hơn GA trong tối ưu siêu tham số SVR và ANN.
- **Thuật toán Đàn dơi (Bat Algorithm - BA) và Tối ưu Sói xám (Grey Wolf Optimizer - GWO)**:
  - **Thuật toán Đàn dơi (BA)**: Do Yang (2010) phát triển, mô phỏng hành vi định vị bằng tiếng vang (echolocation) của dơi. Thuật toán điều chỉnh tần số phát xung $f_i = f_{\min} + (f_{\max} - f_{\min})\beta$, cập nhật vận tốc và vị trí, đồng thời kiểm soát độ to âm thanh $A_i$ và tỷ lệ phát xung $r_i$ để hội tụ về nghiệm tối ưu.
  - **Tối ưu Sói xám (GWO)**: Do Mirjalili và cộng sự (2014) phát triển, mô phỏng thứ bậc xã hội nghiêm ngặt của loài sói xám gồm 4 cấp bậc: sói đầu đàn alpha ($\alpha$), sói cố vấn beta ($\beta$), sói chấp hành delta ($\delta$), và bầy sói cấp dưới omega ($\omega$). Thuật toán mô phỏng 3 giai đoạn săn mồi: theo dõi/bao vây con mồi, rượt đuổi, và tấn công con mồi theo hướng dẫn của bộ ba $\alpha, \beta, \delta$.
  - **Hiệu quả thực nghiệm**: Việc lai ghép các thuật toán metaheuristic (GA, PSO, BA, GWO) với các mô hình học máy (SVM, ANN, RF) giúp nâng cao hệ số xác định $R^2$ từ 5% đến 20%, đồng thời giảm sai số RMSE từ 15% đến 40% so với phương pháp thử-sai thủ công trong dự báo hiện tượng nghẹt màng MBR.

## 3. Tối ưu hóa, Đánh giá Hiệu năng, Giải thích và Lựa chọn Mô hình

### 3.1 Tối ưu hóa Siêu tham số Mô hình (Model Optimization)

#### 3.1.1 Hiện tượng Quá khớp (Overfitting) và Dưới khớp (Underfitting)
- Quá trình huấn luyện mô hình học máy tìm kiếm tập hợp tham số tối ưu nhằm cực tiểu hóa hàm mất mát trên dữ liệu quan sát.
- Hiện tượng Dưới khớp (Underfitting) xuất hiện khi mô hình có cấu trúc quá đơn giản.
  - Mô hình không đủ khả năng học các mối quan hệ phi tuyến tiềm ẩn giữa các biến vận hành MBR và biến mục tiêu.
  - Sai số trên cả tập huấn luyện (training error) và tập kiểm tra (testing error) đều duy trì ở mức cao.
  - Nguyên nhân chính: Số lượng nơ-ron hoặc số tầng ẩn quá ít, hàm nhân (kernel) không phù hợp, hoặc mức độ điều chuẩn hóa (regularization) quá lớn.
- Hiện tượng Quá khớp (Overfitting) xảy ra khi mô hình có độ phức tạp vượt mức cần thiết.
  - Mô hình học thuộc lòng cả nhiễu ngẫu nhiên và biến động cá biệt của tập huấn luyện.
  - Sai số huấn luyện tiệm cận 0, nhưng sai số kiểm định trên dữ liệu độc lập tăng vọt.
  - Khả năng khái quát hóa (generalization capability) của mô hình bị suy giảm nghiêm trọng.
  - Nguyên nhân: Kích thước mẫu dữ liệu MBR hạn chế trong khi số lượng tham số tự do quá lớn.
- Đánh đổi Độ chệch và Phương sai (Bias-Variance Trade-off):
  - Sai số tổng quát của mô hình gồm ba thành phần: $\text{Error} = \text{Bias}^2 + \text{Variance} + \sigma^2$.
  - $\text{Bias}$ (Độ chệch) đại diện cho sai số do giả định đơn giản hóa của thuật toán.
  - $\text{Variance}$ (Phương sai) đo lường độ nhạy của mô hình trước các biến động nhỏ trong tập dữ liệu huấn luyện.
  - $\sigma^2$ là nhiễu không thể quy giảm (irreducible noise) vốn có của hệ thống thực nghiệm.
  - Mục tiêu tối ưu hóa: Cân bằng bias và variance để cực tiểu hóa sai số tổng quát.

#### 3.1.2 Kỹ thuật Xác thực Chéo K-lần (K-Fold Cross-Validation)
- Cơ chế phân chia dữ liệu:
  - Tập dữ liệu huấn luyện gồm $N$ mẫu được chia ngẫu nhiên thành $K$ phần con (folds) có kích thước xấp xỉ bằng nhau và không giao nhau.
  - Quá trình đánh giá thực hiện lặp lại $K$ vòng độc lập.
  - Trong mỗi vòng lặp $k \in \{1, 2, \dots, K\}$, mô hình sử dụng $K-1$ phần con để huấn luyện (training subsets).
  - Phần con thứ $k$ còn lại đóng vai trò tập xác thực (validation subset) để kiểm tra sai số.
- Công thức tính toán sai số xác thực chéo:
  - Sai số kiểm định chéo trung bình $CV_{(K)}$ xác định theo công thức:
    $$CV_{(K)} = \frac{1}{K} \sum_{k=1}^K MSE_k$$
  - Trong đó $MSE_k$ là sai số bình phương trung bình trên tập kiểm định của vòng thứ $k$:
    $$MSE_k = \frac{1}{n_k} \sum_{i=1}^{n_k} (y_i - \hat{y}_i)^2$$
- Đặc điểm vận hành và chi phí tính toán:
  - Giá trị $K$ thường chọn bằng 5 hoặc 10 theo kinh nghiệm thực nghiệm.
  - Khi $K = N$, phương pháp trở thành xác thực chéo loại một mẫu (Leave-One-Out Cross-Validation - LOOCV).
  - Ưu điểm: Tận dụng tối đa dữ liệu có sẵn, loại bỏ thiên lệch do chia tập tĩnh, đánh giá khách quan độ bền vững của mô hình.
  - Nhược điểm: Chi phí tính toán cao do phải tái huấn luyện mô hình $K$ lần liên tục.

#### 3.1.3 Các Chiến lược Tìm kiếm Siêu tham số (Hyperparameter Search Strategies)
- Tìm kiếm vét cạn theo lưới (Grid Search):
  - Người dùng thiết lập không gian tìm kiếm gồm các tập giá trị rời rạc cho từng siêu tham số.
  - Thuật toán kiểm tra toàn bộ tích Descartes (Cartesian product) của tất cả các tổ hợp siêu tham số.
  - Với mỗi tổ hợp, thuật toán chạy quy trình K-Fold CV để ghi nhận điểm số hiệu năng trung bình.
  - Ưu điểm: Đảm bảo duyệt hết không gian định trước, dễ thực thi song song hóa.
  - Nhược điểm: Bị bùng nổ tổ hợp khi số chiều siêu tham số tăng cao, tốn kém tài nguyên tính toán.
- Tìm kiếm ngẫu nhiên (Random Search):
  - Lấy mẫu ngẫu nhiên các cấu hình siêu tham số từ phân phối xác suất liên tục hoặc rời rạc xác định trước.
  - Số lần thử nghiệm cố định theo ngân sách tính toán $N_{\text{iter}}$.
  - Hiệu quả: Vượt trội hơn Grid Search khi chỉ có một số ít siêu tham số chi phối hiệu năng mô hình (Bergstra & Bengio, 2012).
- Tối ưu hóa Bayes (Bayesian Optimization):
  - Phù hợp tối ưu hóa các hàm mục tiêu tốn nhiều thời gian tính toán như mạng nơ-ron sâu hoặc rừng ngẫu nhiên quy mô lớn.
  - Xây dựng mô hình đại diện xác suất (thường dùng Quá trình Gaussian - Gaussian Process, GP) cho hàm mục tiêu chưa biết $f(\theta)$:
    $$f(\theta) \sim \mathcal{GP}\left(m(\theta), k(\theta, \theta')\right)$$
  - Trong đó $m(\theta)$ là hàm kỳ vọng và $k(\theta, \theta')$ là hàm hiệp phương sai (kernel covariance).
  - Sử dụng hàm thu nạp (Acquisition Function) để quyết định điểm đánh giá tiếp theo, cân bằng giữa thăm dò (exploration) và khai thác (exploitation).
  - Hàm Cải thiện Kỳ vọng (Expected Improvement - EI):
    $$EI(\theta) = \mathbb{E}\left[\max\left(0, f_{best} - f(\theta)\right)\right]$$
  - Thuật toán ưu tiên đánh giá các vùng có giá trị trung bình dự báo tốt hoặc độ bất định cao.

#### 3.1.4 Các Thuật toán Bầy đàn và Siêu phỏng sinh học (Metaheuristic Optimization Algorithms)
- Giải thuật Di truyền (Genetic Algorithm - GA):
  - Lấy cảm hứng từ quá trình chọn lọc tự nhiên và di truyền học của Darwin.
  - Mã hóa mỗi cấu hình siêu tham số thành một chuỗi nhiễm sắc thể (chromosome).
  - Khởi tạo quần thể gồm nhiều cá thể ngẫu nhiên.
  - Đánh giá độ thích nghi (fitness function) của từng cá thể thông qua chỉ số sai số mô hình (như $1/RMSE$ hoặc $R^2$).
  - Áp dụng các toán tử di truyền qua từng thế hệ:
    - Toán tử chọn lọc (Selection): Giữ lại các cá thể có độ thích nghi cao.
    - Toán tử lai ghép (Crossover): Trao đổi thông tin di truyền giữa hai cá thể bố mẹ để sinh cá thể con.
    - Toán tử đột biến (Mutation): Thay đổi ngẫu nhiên một số gen để duy trì tính đa dạng và thoát khỏi cực trị địa phương.
- Tối ưu hóa Bầy đàn Hạt (Particle Swarm Optimization - PSO):
  - Mô phỏng hành vi di chuyển tìm mồi của bầy chim hoặc đàn cá.
  - Mỗi hạt đại diện cho một nghiệm siêu tham số trong không gian tìm kiếm đa chiều.
  - Mỗi hạt $i$ sở hữu vectơ vị trí $x_i^{(t)}$ và vectơ vận tốc $v_i^{(t)}$ tại vòng lặp $t$.
  - Công thức cập nhật vận tốc và vị trí:
    $$v_i^{(t+1)} = w \cdot v_i^{(t)} + c_1 r_1 \left(p_{\text{best}, i} - x_i^{(t)}\right) + c_2 r_2 \left(g_{\text{best}} - x_i^{(t)}\right)$$
    $$x_i^{(t+1)} = x_i^{(t)} + v_i^{(t+1)}$$
  - Trong đó:
    - $w$ là trọng số quán tính (inertia weight), kiểm soát ảnh hưởng của vận tốc trước đó.
    - $c_1, c_2$ là các hệ số gia tốc nhận thức cá nhân (cognitive) và gia tốc xã hội bầy đàn (social).
    - $r_1, r_2$ là các biến ngẫu nhiên phân phối đều trong khoảng $[0, 1]$.
    - $p_{\text{best}, i}$ là vị trí tối ưu từng đạt được của bản thân hạt $i$.
    - $g_{\text{best}}$ là vị trí tối ưu toàn cục của toàn bộ bầy hạt.
- Luyện kim Mô phỏng (Simulated Annealing - SA):
  - Mô phỏng quá trình nhiệt luyện kim loại từ nhiệt độ cao rồi làm nguội chậm có kiểm soát.
  - Tại mỗi mức nhiệt độ $T$, thuật toán tạo một cấu hình lân cận $\theta'$.
  - Nếu nghiệm mới tốt hơn ($\Delta E = f(\theta') - f(\theta) < 0$), thuật toán chấp nhận nghiệm mới ngay lập tức.
  - Nếu nghiệm mới kém hơn, thuật toán vẫn chấp nhận nghiệm đó với xác suất Boltzmann:
    $$P(\text{chấp nhận}) = \exp\left(-\frac{\Delta E}{T}\right)$$
  - Cơ chế này cho phép thuật toán thoát khỏi các cực tiểu địa phương khi nhiệt độ còn cao.
- Các thuật toán metaheuristic bầy đàn khác trong nghiên cứu MBR:
  - Thuật toán Đàn ong Nhân tạo (Artificial Bee Colony - ABC): Phân chia bầy ong thành ong thợ, ong quan sát và ong trinh sát để khai thác nguồn mật.
  - Thuật toán Đàn kiến (Ant Colony Optimization - ACO): Dựa trên dấu vết pheromone của kiến để tìm đường đi ngắn nhất.
  - Thuật toán Đom đóm (Firefly Algorithm - FFA): Dựa trên cường độ phát sáng để các cá thể đom đóm hút nhau.
  - Thuật toán Dơi (Bat Algorithm - BA): Ứng dụng sóng định vị bằng tiếng vang để săn mồi và điều chỉnh tần số phát xung.
  - Bộ tối ưu Chó sói Xám (Gray Wolf Optimizer - GWO): Mô phỏng trật tự phân cấp săn mồi của đàn sói xám (sói $\alpha$, $\beta$, $\delta$, và $\omega$).

---

### 3.2 Đánh giá Hiệu năng Định lượng Mô hình (Model Performance Assessment)

#### 3.2.1 Các Chỉ số Đánh giá Bài toán Hồi quy (Regression Metrics)
- Hệ số xác định ($R^2$ - Coefficient of Determination):
  - Đo lường tỷ lệ phương sai của biến mục tiêu thực tế được giải thích bởi các biến đầu vào qua mô hình:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó $y_i$ là giá trị thực nghiệm, $\hat{y}_i$ là giá trị mô hình dự báo, và $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ là giá trị trung bình thực nghiệm.
  - Miền giá trị danh nghĩa: $R^2 \le 1.0$. Giá trị càng gần 1.0, độ khớp của mô hình càng cao. Giá trị âm xuất hiện khi mô hình dự báo kém hơn mức trung bình tĩnh $\bar{y}$.
- Sai số Bình phương Trung bình (MSE - Mean Squared Error):
  - Trung bình cộng của bình phương các độ lệch giữa giá trị dự báo và giá trị thực tế:
    $$MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$
  - MSE phạt rất nặng các sai số lớn do có số mũ bậc hai. Chỉ số này nhạy cảm với các giá trị ngoại lai dị biệt.
- Sai số Căn bậc hai Bình phương Trung bình (RMSE - Root Mean Squared Error):
  - Căn bậc hai của sai số bình phương trung bình:
    $$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  - RMSE giữ nguyên đơn vị đo lường vật lý của biến đầu ra (ví dụ: $L/(m^2 \cdot h)$ đối với thông lượng màng, hoặc $kPa$ đối với TMP).
- Sai số Tuyệt đối Trung bình (MAE - Mean Absolute Error):
  - Trung bình cộng của các độ lệch tuyệt đối giữa giá trị thực tế và giá trị dự báo:
    $$MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$
  - MAE phản ánh độ lớn sai số trung bình một cách trực quan, ít chịu ảnh hưởng thái quá bởi các điểm dữ liệu ngoại lai so với RMSE.
- Sai số Phần trăm Tuyệt đối Trung bình (MAPE - Mean Absolute Percentage Error):
  - Tỷ lệ phần trăm sai số trung bình so với giá trị thực tế:
    $$MAPE = \frac{100\%}{n}\sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
  - MAPE cho phép so sánh hiệu năng giữa các tập dữ liệu có thang đo khác nhau.
  - Hạn chế: MAPE không xác định hoặc tăng vô hạn khi giá trị thực tế $y_i$ tiến dần về 0.

#### 3.2.2 Tiêu chuẩn Thông tin Đánh giá Độ phức tạp Mô hình (Information Criteria)
- Giới hạn của các chỉ số hiệu năng thông thường ($R^2$, MSE, RMSE):
  - Các chỉ số này chỉ đánh giá độ khớp thuần túy trên dữ liệu mà không xét đến số lượng tham số tự do của mô hình.
  - Mô hình càng nhiều tham số càng dễ đạt $R^2$ cao trên tập huấn luyện, nhưng đối mặt nguy cơ quá khớp lớn.
- Tiêu chuẩn Thông tin Akaike (AIC - Akaike Information Criterion):
  - Dựa trên lý thuyết thông tin và khoảng cách Kullback-Leibler:
    $$AIC = 2k - 2\ln(L)$$
  - Trong đó $k$ là số lượng tham số ước lượng trong mô hình, $L$ là giá trị cực đại của hàm hợp lý (maximum likelihood).
  - Đối với bài toán hồi quy với sai số chuẩn:
    $$AIC = n \ln(MSE) + 2k$$
- Tiêu chuẩn Thông tin Bayes (BIC - Bayesian Information Criterion / Schwarz Criterion):
  - Dựa trên phương pháp tiếp cận xác suất hậu nghiệm Bayes:
    $$BIC = k\ln(n) - 2\ln(L)$$
  - Đối với bài toán hồi quy:
    $$BIC = n \ln(MSE) + k\ln(n)$$
  - Với kích thước mẫu $n \ge 8$, ta có $\ln(n) > 2$, do đó BIC phạt số lượng tham số $k$ nghiêm khắc hơn AIC.
- Tiêu chuẩn Hannan-Quinn (HQC - Hannan-Quinn Criterion):
  - Cân bằng giữa tốc độ hội tụ và mức độ phạt tham số:
    $$HQC = 2k\ln(\ln(n)) - 2\ln(L)$$
- So sánh mức độ phạt tham số (Penalty Gradient):
  - Khi kích thước mẫu $n$ đủ lớn, độ lớn hình phạt tham số tuân theo thứ tự:
    $$AIC < HQC < BIC$$
  - Hình phạt càng mạnh thì tiêu chuẩn càng ưu tiên lựa chọn các mô hình tinh gọn, ít chiều (low-dimensional models).
  - Giá trị AIC, BIC hoặc HQC càng nhỏ chứng tỏ mô hình đạt được sự cân bằng tối ưu giữa độ chính xác và tính đơn giản.

#### 3.2.3 Các Chỉ số Đánh giá Bài toán Phân loại (Classification Metrics)
- Ma trận Nhầm lẫn (Confusion Matrix):
  - Bảng tổng hợp kết quả phân loại nhị phân gồm 4 ô giá trị:
    - Dương tính thật (True Positive - $TP$): Mẫu dương tính được dự báo chính xác là dương tính.
    - Âm tính thật (True Negative - $TN$): Mẫu âm tính được dự báo chính xác là âm tính.
    - Dương tính giả (False Positive - $FP$, Sai số loại I): Mẫu âm tính bị dự báo nhầm thành dương tính.
    - Âm tính giả (False Negative - $FN$, Sai số loại II): Mẫu dương tính bị bỏ sót thành âm tính.
- Độ chính xác Tổng thể (Accuracy):
  - Tỷ lệ số mẫu dự báo đúng trên toàn bộ tập dữ liệu:
    $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
  - Hạn chế: Dễ đưa ra đánh giá sai lệch khi dữ liệu bị mất cân bằng lớp nghiêm trọng.
- Độ chuẩn xác (Precision):
  - Tỷ lệ mẫu thực sự dương tính trong tổng số mẫu được mô hình gắn nhãn dương tính:
    $$Precision = \frac{TP}{TP + FP}$$
- Độ thu hồi / Độ nhạy (Recall / Sensitivity):
  - Tỷ lệ mẫu dương tính được mô hình phát hiện thành công trên tổng số mẫu thực sự dương tính:
    $$Recall = \frac{TP}{TP + FN}$$
- Điểm số F1 (F1-score):
  - Trung bình điều hòa giữa Precision và Recall:
    $$F1\text{-score} = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$
  - F1-score là thước đo cân bằng, đặc biệt hiệu quả khi dữ liệu phân loại tắc nghẽn màng bị mất cân bằng lớp.
- Đường cong ROC (Receiver Operating Characteristic) và Diện tích AUC (Area Under Curve):
  - Đường cong ROC biểu diễn mối quan hệ giữa Tỷ lệ dương tính thật (TPR = Recall) và Tỷ lệ dương tính giả (FPR):
    $$TPR = \frac{TP}{TP + FN}, \quad FPR = \frac{FP}{FP + TN}$$
  - Giá trị AUC đo lường toàn diện năng lực phân biệt giữa hai lớp của mô hình:
    - $\text{AUC} = 0.5$: Mô hình dự báo ngẫu nhiên, không có giá trị phân biệt.
    - $0.7 \le \text{AUC} < 0.8$: Khả năng phân biệt chấp nhận được.
    - $0.8 \le \text{AUC} < 0.9$: Khả năng phân biệt xuất sắc.
    - $\text{AUC} \ge 0.9$: Khả năng phân biệt rất cao, tiệm cận phân loại hoàn hảo ($\text{AUC} = 1.0$).

---

### 3.3 Đánh giá Khả năng Giải thích Mô hình Học máy (Model Interpretation & XAI)

#### 3.3.1 Thách thức của Mô hình Hộp đen (Black-box Models) trong MBR
- Các thuật toán học máy phức tạp (mạng nơ-ron nhân tạo nhiều tầng, mô hình tổng hợp rừng ngẫu nhiên, mô hình tăng cường gradient) đạt độ chính xác cao nhưng hoạt động như các "hộp đen".
- Cơ chế bên trong của mô hình hộp đen ẩn giấu các hàm truyền phi tuyến phức tạp.
- Kỹ sư vận hành không thể quan sát quy luật đưa ra dự báo của mô hình.
- Hệ quả trong công nghệ MBR:
  - Khó kiểm tra tính nhất quán giữa dự báo của mô hình và các định luật bảo toàn khối lượng, động học sinh học và thủy lực màng.
  - Nguy cơ đưa ra các cảnh báo sai hoặc quyết định điều khiển rửa màng sai lầm khi dữ liệu quan trắc xuất hiện nhiễu.
  - Thiếu sự tin cậy từ phía các nhà quản lý và chuyên gia vận hành nhà máy xử lý nước thải.
- Nhu cầu cấp thiết về Trí tuệ Nhân tạo Giải thích được (Explainable Artificial Intelligence - XAI):
  - Chuyển đổi mô hình học máy từ trạng thái hộp đen sang mô hình minh bạch.
  - Xác định mức độ đóng góp định lượng của từng biến số đầu vào (nồng độ bùn hoạt tính MLSS, thông lượng khí sục aeration, áp suất lọc TMP, nồng độ EPS/SMP).

#### 3.3.2 Phương pháp Phân tích Trọng số Kết nối Nơ-ron (Connection Weight Methods)
- Thuật toán Garson (Garson's Algorithm, 1991):
  - Phân tích ma trận trọng số kết nối giữa lớp đầu vào ($i$), lớp ẩn ($j$) và lớp đầu ra ($k$) trong mạng nơ-ron nhiều tầng (MLP).
  - Tỷ lệ đóng góp tương đối $Q_{ik}$ của biến đầu vào $i$ đối với biến đầu ra $k$ xác định theo công thức:
    $$Q_{ik} = \frac{\sum_{j=1}^{N_h} \left( \frac{|w_{ij}|}{\sum_{m=1}^{N_i} |w_{mj}|} \cdot |v_{jk}| \right)}{\sum_{i=1}^{N_i} \left[ \sum_{j=1}^{N_h} \left( \frac{|w_{ij}|}{\sum_{m=1}^{N_i} |w_{mj}|} \cdot |v_{jk}| \right) \right]}$$
  - Trong đó:
    - $w_{ij}$ là trọng số liên kết từ nơ-ron đầu vào $i$ đến nơ-ron ẩn $j$.
    - $v_{jk}$ là trọng số liên kết từ nơ-ron ẩn $j$ đến nơ-ron đầu ra $k$.
    - $N_i$ là tổng số nơ-ron lớp đầu vào.
    - $N_h$ là tổng số nơ-ron lớp ẩn.
  - Nhược điểm của thuật toán Garson: Sử dụng giá trị tuyệt đối $|w|$, do đó triệt tiêu dấu của trọng số, không phân biệt được biến đầu vào mang tác động kích thích (tích cực) hay ức chế (tiêu cực) lên đầu ra.
- Phương pháp Trọng số Kết nối có dấu của Goh (1995) và Olden (Olden et al., 2004):
  - Giữ nguyên dấu đại số của các liên kết để xác định chiều hướng tác động:
    $$S_{ik} = \sum_{j=1}^{N_h} \left( w_{ij} \cdot v_{jk} \right)$$
  - Giá trị $S_{ik}$ dương thể hiện biến đầu vào $i$ tỷ lệ thuận với biến đầu ra $k$ (ví dụ: MLSS tăng làm tăng tốc độ tắc nghẽn màng).
  - Giá trị $S_{ik}$ âm thể hiện mối quan hệ tỷ lệ nghịch (ví dụ: tăng cường độ sục khí giúp làm giảm tốc độ bám bẩn màng).
  - Nghiên cứu của Olden chứng minh phương pháp này đạt độ chính xác phân loại tầm quan trọng cao hơn thuật toán Garson trên dữ liệu mô phỏng.
- Thuật toán Gedeon (1997):
  - Mở rộng phân tích đóng góp trọng số cho các cấu trúc mạng nơ-ron có nhiều lớp ẩn liên tiếp.
  - Phù hợp phân tích cơ chế nội tại của các kiến trúc học sâu (Deep Learning).

#### 3.3.3 Phân tích Độ nhạy và Độ quan trọng Biến trong Mô hình Cây
- Phân tích Độ nhạy (Sensitivity Analysis):
  - Đánh giá mức độ thay đổi của biến đầu ra khi biến thiên có kiểm soát từng biến đầu vào trong khi cố định các biến còn lại ở giá trị cơ sở (trung bình hoặc trung vị).
  - Giúp phát hiện ngưỡng phản ứng tới hạn của hệ thống MBR (ví dụ: ngưỡng nồng độ chất keo sinh học gây đột biến TMP).
- Độ quan trọng của biến trong Mô hình Cây Quyết định và Rừng Ngẫu nhiên (Random Forest):
  - Độ suy giảm tạp chất trung bình (Mean Decrease Impurity - MDI):
    - Tính toán tổng mức độ suy giảm chỉ số Gini (đối với phân loại) hoặc MSE (đối với hồi quy) tại tất cả các nút phân nhánh sử dụng đặc trưng đó.
    - Hạn chế: Thường thiên lệch đối với các đặc trưng có nhiều giá trị phân loại rời rạc hoặc liên tục.
  - Độ chính xác ngoài túi (Mean Decrease Accuracy / Out-of-Bag - OOB Permutation Importance):
    - Hoán vị ngẫu nhiên các giá trị của một đặc trưng cụ thể trên tập dữ liệu kiểm định OOB.
    - Đo lường mức độ sụt giảm độ chính xác dự báo sau khi hoán vị:
      $$\Delta \text{Error}_j = \text{Error}_{\text{permuted}(j)} - \text{Error}_{\text{original}}$$
    - Nếu sai số tăng mạnh sau khi hoán vị, đặc trưng đó đóng vai trò trọng yếu trong việc ra quyết định của mô hình.

#### 3.3.4 Đồ thị Phụ thuộc Một phần (PDP), ICE và Phương pháp LIME
- Đồ thị Phụ thuộc Một phần (Partial Dependence Plot - PDP):
  - Minh họa tác động biên phi tuyến (marginal effect) của một hoặc hai biến đầu vào lên dự báo của mô hình học máy:
    $$\hat{f}_{x_S}(x_S) = \frac{1}{n}\sum_{i=1}^n \hat{f}\left(x_S, x_C^{(i)}\right)$$
  - Trong đó:
    - $x_S$ là tập hợp đặc trưng cần phân tích (thường là 1 hoặc 2 biến).
    - $x_C$ là tập hợp tất cả các đặc trưng còn lại trong mô hình.
    - $x_C^{(i)}$ là giá trị thực tế của tập đặc trưng còn lại từ mẫu dữ liệu thứ $i$.
  - Ứng dụng trong MBR: Vẽ đường cong mô tả mối quan hệ giữa thông lượng thấm (flux) và tốc độ gia tăng áp suất xuyên màng $dTMP/dt$, giúp xác định vùng thông lượng tới hạn (critical flux).
  - Hạn chế: PDP giả định tính độc lập giữa các biến $x_S$ và $x_C$. Khi các biến đầu vào tương quan chặt chẽ (như MLSS và độ nhớt nhớt bùn), PDP có thể tính toán trên các điểm dữ liệu phi thực tế.
- Đường Kỳ vọng Có điều kiện Cá thể (Individual Conditional Expectation - ICE):
  - Hiển thị mối quan hệ phụ thuộc cho từng mẫu dữ liệu riêng lẻ thay vì lấy trung bình như PDP.
  - Giúp phát hiện các mối quan hệ không đồng nhất hoặc các hiệu ứng tương tác ẩn giữa các nhóm vi sinh vật khác nhau.
- Phương pháp LIME (Local Interpretable Model-agnostic Explanations):
  - Giải thích dự báo cục bộ cho từng điểm dữ liệu đơn lẻ.
  - Thuật toán làm nhiễu nhẹ điểm dữ liệu quan tâm, lấy dự báo từ mô hình phức tạp, sau đó huấn luyện một mô hình giải thích được (như hồi quy tuyến tính có trọng số theo khoảng cách) cục bộ xung quanh điểm đó.

#### 3.3.5 Phương pháp SHAP (SHapley Additive exPlanations)
- Nền tảng Lý thuyết Trò chơi Hợp tác (Cooperative Game Theory):
  - Do nhà toán học Lloyd Shapley đề xuất (1953) nhằm phân chia công bằng phần thưởng của một liên minh người chơi.
  - Trong học máy: Tập hợp các đặc trưng đầu vào đóng vai trò là "liên minh người chơi", và giá trị dự báo của mô hình đóng vai trò là "phần thưởng".
- Công thức tính toán giá trị Shapley:
  - Giá trị đóng góp biên trung bình $\phi_i(x)$ của đặc trưng $i$ đối với mẫu dữ liệu $x$ xác định bởi:
    $$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
  - Ý nghĩa các ký hiệu:
    - $F$ là tập hợp đầy đủ của tất cả các đặc trưng đầu vào ($|F|$ là tổng số đặc trưng).
    - $S$ là một tập con bất kỳ của các đặc trưng không chứa đặc trưng $i$.
    - $|S|$ là số lượng đặc trưng có mặt trong tập hợp con $S$.
    - $f_x(S)$ là giá trị kỳ vọng dự báo của mô hình khi chỉ sử dụng tập đặc trưng $S$.
    - $[f_x(S \cup \{i\}) - f_x(S)]$ là đóng góp biên (marginal contribution) thuần túy khi thêm đặc trưng $i$ vào tập hợp $S$.
    - Tỷ số $\frac{|S|!(|F| - |S| - 1)!}{|F|!}$ là trọng số tổ hợp xác suất, tương ứng với tỷ lệ xuất hiện của cấu hình liên minh $S$ khi các đặc trưng được đưa vào theo thứ tự ngẫu nhiên.
- Ba tính chất toán học nền tảng bắt buộc của SHAP:
  - 1. Tính Chính xác Cục bộ (Local Accuracy / Additivity):
    - Tổng giá trị đóng góp của tất cả các đặc trưng cộng với giá trị kỳ vọng nền bằng chính giá trị dự báo của mô hình:
      $$f(x) = \phi_0 + \sum_{i=1}^{|F|} \phi_i(x), \quad \text{với } \phi_0 = \mathbb{E}[f(X)]$$
    - Tính chất này bảo đảm mô hình giải thích hoàn toàn khớp với đầu ra thực tế của mô hình gốc.
  - 2. Tính Bị khuyết (Missingness):
    - Nếu một đặc trưng không hiện diện trong quan sát đầu vào của mẫu thử, giá trị đóng góp gán cho nó bằng 0:
      $$x_i = \text{missing} \implies \phi_i = 0$$
  - 3. Tính Nhất quán (Consistency):
    - Nếu cấu trúc mô hình thay đổi khiến đóng góp biên của đặc trưng $i$ tăng lên hoặc giữ nguyên đối với mọi tập con $S$, thì giá trị $\phi_i$ của nó trên mô hình mới không bao giờ giảm:
      $$\forall S, \left[ f'_x(S \cup \{i\}) - f'_x(S) \ge f_x(S \cup \{i\}) - f_x(S) \right] \implies \phi_i(f', x) \ge \phi_i(f, x)$$
- Ba cấp độ phân tích thực nghiệm của SHAP trong nghiên cứu MBR:
  - Phân tích Cục bộ (Local Interpretation):
    - Sử dụng biểu đồ thác nước (Waterfall plot) hoặc biểu đồ lực đẩy (Force plot).
    - Định lượng chính xác từng yếu tố làm tăng hay giảm nguy cơ tắc nghẽn màng tại một thời điểm vận hành cụ thể.
  - Phân tích Toàn cục (Global Interpretation):
    - Sử dụng biểu đồ tóm tắt SHAP (Beeswarm plot) và biểu đồ cột xếp hạng tầm quan trọng (Bar plot).
    - Xác định xếp hạng tổng thể của các biến vận hành trên toàn bộ cơ sở dữ liệu.
    - Màu sắc hiển thị giá trị thực tế của biến (đỏ: cao, xanh: thấp) kết hợp trục hoành $\phi_i$ cho biết hướng tác động lên thông lượng hoặc TMP.
  - Phân tích Tương tác Đặc trưng (Feature Interaction):
    - Sử dụng biểu đồ phụ thuộc SHAP (SHAP dependence plot).
    - Bóc tách tương tác phi tuyến bậc hai giữa hai biến (ví dụ tác động hiệp đồng giữa nồng độ polysaccharide ngoại bào EPS và nhiệt độ nước thải lên sức cản bánh bùn).

---

### 3.4 Bảng Hướng dẫn Lựa chọn Mô hình Học máy (Model Selection Guide)

#### 3.4.1 Quy trình Ra Quyết định Phân tầng (Hierarchical Decision Workflow)
- Bước 1: Xác định loại dữ liệu và cấu trúc nhãn mục tiêu:
  - Dữ liệu không có nhãn đầu ra $\to$ Sử dụng các thuật toán Học không giám sát (Unsupervised Learning):
    - Phân cụm K-means, Phân cụm phân cấp (Hierarchical Clustering), Phân tích thành phần chính (PCA) để phân loại cụm bùn hoặc phát hiện dị biệt.
  - Dữ liệu có nhãn đầu ra liên tục $\to$ Sử dụng các bài toán Hồi quy (Regression):
    - Dự báo thông lượng thấm (membrane flux), áp suất xuyên màng (TMP), điện trở màng tổng cộng ($R_t$), hiệu suất loại bỏ chất ô nhiễm (COD, $\text{NH}_4^+$, TN, TP).
    - Các mô hình phù hợp: SVR, Random Forest, GBDT, XGBoost, ANN, MLP.
  - Dữ liệu có nhãn đầu ra rời rạc hoặc phân loại $\to$ Sử dụng các bài toán Phân loại (Classification):
    - Nhận diện trạng thái tắc nghẽn (bình thường / tắc nghẽn nhẹ / nghẽn nghiêm trọng), dự đoán sự cố sốc tải vi sinh.
    - Các mô hình phù hợp: SVC, Random Forest Classifier, ANN, Naive Bayes.
  - Tác vụ tối ưu hóa chuỗi quyết định thích nghi $\to$ Sử dụng Học tăng cường (Reinforcement Learning - RL):
    - Tự động điều khiển chu kỳ bật tắt sục khí, điều tiết van rửa ngược màng theo thời gian thực nhằm tiết kiệm năng lượng.
- Bước 2: Đánh giá theo Kích thước Mẫu Dữ liệu ($N$):
  - Kích thước mẫu hạn chế ($N < 500$ mẫu):
    - Ưu tiên lựa chọn: Máy vector hỗ trợ (SVM/SVR), Rừng ngẫu nhiên (Random Forest), hoặc Mạng nơ-ron nhiều tầng cấu trúc nông (MLP với 1-2 lớp ẩn).
    - Lý do: Các mô hình này kiểm soát hiện tượng quá khớp rất tốt trên tập dữ liệu nhỏ nhờ cơ chế biên cực đại (SVM) hoặc lấy mẫu ngẫu nhiên đóng bao (RF).
  - Kích thước mẫu lớn ($N > 10,000$ mẫu):
    - Ưu tiên lựa chọn: Mạng nơ-ron sâu (Deep Neural Network - DNN), Mạng nơ-ron hồi quy sâu.
    - Lý do: Mạng nơ-ron sâu giải phóng sức mạnh biểu diễn phi tuyến cao khi được cung cấp đủ dữ liệu lớn, tránh bão hòa hiệu năng như các mô hình truyền thống.
- Bước 3: Phù hợp Cấu trúc Không gian và Thời gian của Dữ liệu:
  - Dữ liệu chuỗi thời gian liên tục (Time-series data: dữ liệu cảm biến đo online lưu lượng, nhiệt độ, pH, DO theo từng giây/phút):
    - Lựa chọn mô hình có bộ nhớ hồi quy: LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit), RNN.
  - Dữ liệu dạng ma trận hoặc hình ảnh (Ảnh chụp cấu trúc bề mặt màng bằng kính hiển vi điện tử quét SEM, ảnh phân bố vi sinh vật bằng kính hiển vi huỳnh quang CLSM):
    - Lựa chọn Mạng nơ-ron Tích chập (Convolutional Neural Network - CNN) để trích xuất đặc trưng hình thái lỗ xốp và lớp bánh bùn.
  - Dữ liệu có cấu trúc đồ thị topo mạng lưới (Mạng lưới phân phối đường ống, cấu trúc liên kết chuỗi thức ăn sinh thái vi sinh vật trong bùn hoạt tính):
    - Lựa chọn Mạng nơ-ron Đồ thị (Graph Neural Network - GNN).

#### 3.4.2 Ma trận Lựa chọn Mô hình theo 5 Tiêu chí Kỹ thuật
- Tiêu chí 1: Số lượng mẫu dữ liệu khả dụng ($N$): Phân định khả năng huấn luyện hiệu quả từ tập dữ liệu vi mô đến dữ liệu lớn.
- Tiêu chí 2: Số chiều của không gian đặc trưng ($P$): Đánh giá năng lực xử lý khi dữ liệu có nhiều biến quan trắc đầu vào.
- Tiêu chí 3: Bản chất quan hệ phi tuyến (Non-linearity): Đánh giá khả năng xấp xỉ các phản ứng sinh học và thủy lực phức tạp trong MBR.
- Tiêu chí 4: Chi phí tính toán huấn luyện và triển khai (Computational Resource Cost): Xem xét tài nguyên phần cứng và tốc độ đáp ứng thời gian thực.
- Tiêu chí 5: Yêu cầu về mức độ minh bạch và giải thích cơ chế (Interpretability Need): Đánh giá khả năng hiểu rõ quy luật vận hành phục vụ ra quyết định kỹ thuật.

#### 3.4.3 Bảng So sánh Tổng hợp và Khuyến nghị Mô hình trong Nghiên cứu MBR

| Thuật toán Học máy | Cỡ mẫu khuyến nghị ($N$) | Năng lực Phi tuyến | Chi phí Huấn luyện | Khả năng Giải thích | Ưu điểm cốt lõi trong MBR | Nhược điểm cốt lõi trong MBR | Ứng dụng điển hình trong MBR |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hồi quy Tuyến tính / Ridge / Lasso** | Nhỏ đến lớn ($N \ge 30$) | Thấp (chỉ giải quyết quan hệ tuyến tính) | Rất thấp (tính toán giải tích tức thì) | Rất cao (hộp trắng, trọng số biểu thị hệ số trực tiếp) | Cực kỳ nhanh, không bị quá khớp khi số mẫu ít, dễ chuẩn hóa | Không mô phỏng được quá trình tắc nghẽn màng phi tuyến phức tạp | Đánh giá sơ bộ mối quan hệ cơ bản giữa các thông số nước thải |
| **K-Nearest Neighbors (KNN)** | Nhỏ đến trung bình ($50 < N < 2000$) | Trung bình (phi tuyến cục bộ dựa trên khoảng cách) | Thấp khi huấn luyện, cao khi suy luận dự báo | Trung bình (dựa trên các trường hợp láng giềng cụ thể) | Trực quan, không cần giả định phân phối dữ liệu, dễ triển khai | Rất nhạy cảm với dữ liệu nhiễu và bùng nổ số chiều đặc trưng | Phân loại trạng thái vận hành MBR dựa trên các ca vận hành tương đồng |
| **Support Vector Machine (SVM / SVR)** | Nhỏ đến trung bình ($50 < N < 5000$) | Rất cao (thông qua các hàm nhân phi tuyến RBF, Poly) | Trung bình đến cao (độ phức tạp $\mathcal{O}(N^2)$ đến $\mathcal{O}(N^3)$) | Thấp (mô hình hộp đen, phụ thuộc hàm nhân) | Hiệu năng dự báo vượt trội trên tập dữ liệu nhỏ, khả năng khái quát hóa cao | Tốn kém bộ nhớ khi dữ liệu lớn, nhạy cảm với việc chọn siêu tham số $C, \gamma, \epsilon$ | Dự báo áp suất xuyên màng TMP, dự đoán điện trở màng và thông lượng |
| **Random Forest (RF)** | Trung bình đến lớn ($N > 100$) | Rất cao (tổng hợp từ hàng trăm cây quyết định) | Trung bình (hỗ trợ phân tán song song tốt) | Khá cao (tính được MDI, OOB importance, kết hợp SHAP tốt) | Không bị quá khớp, chịu đựng tốt dữ liệu thiếu và nhiễu ngoại lai | Có thể bị chậm khi suy luận thời gian thực nếu số lượng cây quá lớn | Dự đoán hiệu suất loại bỏ chất ô nhiễm COD, N, P và chẩn đoán tắc nghẽn |
| **Gradient Boosted Decision Trees (GBDT / XGBoost / LightGBM)** | Trung bình đến lớn ($N > 500$) | Cực cao (tối ưu hóa theo hàm mất mát gradient tuần tự) | Cao (huấn luyện tuần tự từng cây) | Khá cao (tương thích hoàn hảo với SHAP TreeExplainer) | Độ chính xác thực nghiệm cao hàng đầu đối với dữ liệu dạng bảng (tabular data) | Cần tinh chỉnh kỹ lưỡng siêu tham số để tránh quá khớp trên dữ liệu nhiễu | Dự báo tốc độ tắc nghẽn màng dài hạn, phân tích tương tác đa biến XAI |
| **Mạng Nơ-ron Nhân tạo (ANN / MLP)** | Trung bình đến lớn ($N > 500$) | Cực cao (định lý xấp xỉ phổ quát) | Cao (huấn luyện lan truyền ngược Backpropagation) | Rất thấp (hộp đen hoàn toàn, cần công cụ Garson hoặc SHAP) | Mô hình hóa linh hoạt mọi hàm phi tuyến phức tạp của hệ thống sinh học | Dễ rơi vào cực tiểu địa phương, đòi hỏi tiền xử lý chuẩn hóa dữ liệu chặt chẽ | Mô phỏng động học sinh học và diễn biến tắc nghẽn màng MBR |
| **Mạng Học sâu Hồi quy (LSTM / GRU)** | Lớn ($N > 2000$) | Cực cao (học biểu diễn phụ thuộc thời gian đa bước) | Rất cao (đòi hỏi xử lý tính toán GPU) | Rất thấp (cần kỹ thuật XAI chuyên sâu cho chuỗi thời gian) | Ghi nhớ phụ thuộc thời gian dài hạn cực tốt từ chuỗi tín hiệu cảm biến | Đòi hỏi lượng dữ liệu chuỗi liên tục rất lớn, thời gian huấn luyện dài | Dự báo chuỗi thời gian online TMP, tối ưu hóa chu kỳ sục khí động |

## Cây Tri Thức: Ứng dụng Học máy trong MBR - Tổng quan và Dự đoán Loại bỏ Chất ô nhiễm

## 4. Ứng dụng Học máy trong MBR: Tổng quan và Dự đoán Loại bỏ Chất ô nhiễm

### 4.1 Tổng quan Tình hình Ứng dụng và Xu hướng Phát triển

#### 4.1.1 Thống kê Phân bố Nghiên cứu và Mô hình Học máy
- Số lượng công bố khoa học về ứng dụng học máy trong MBR tăng nhanh từ năm 2015. Tốc độ tăng trưởng đạt mức bùng nổ sau năm 2018.
- Trọng tâm nghiên cứu chia thành hai nhóm chính. Nghiên cứu dự đoán tắc nghẽn màng chiếm $67.1\%$. Nghiên cứu dự đoán hiệu suất loại bỏ chất ô nhiễm chiếm $34.3\%$.
- Mạng nơ-ron nhân tạo (ANN) giữ vai trò chủ đạo trong toàn bộ các ứng dụng. Tỷ lệ sử dụng ANN đạt trên $50\%$ trong dự đoán ô nhiễm và $72.9\%$ trong dự đoán tắc nghẽn.
- Mô hình Perceptron đa tầng (MLP) chiếm tỷ trọng cao nhất với $66.7\%$ ở mô hình xử lý chất ô nhiễm và $39.6\%$ ở mô hình tắc nghẽn màng.
- Mạng nơ-ron hàm cơ sở xuyên tâm (RBFNN) chiếm $18.8\%$ trong các nghiên cứu màng.
- Máy vector hỗ trợ (SVM/SVR) chiếm $18.8\%$ tổng số ứng dụng dự đoán tắc nghẽn.
- Mạng nơ-ron sâu (DNN) chiếm $8.3\%$ số lượng mô hình được thiết lập.
- Chiến lược tinh chỉnh siêu tham số thể hiện sự phân hóa rõ rệt:
  + Khoảng $56.3\%$ số nghiên cứu không dùng thuật toán tối ưu hóa tự động.
  + Khoảng $33.3\%$ nghiên cứu áp dụng các thuật toán tối ưu hóa thông minh.
  + Khoảng $8.3\%$ nghiên cứu sử dụng phương pháp kiểm định chéo (Cross-Validation).
- Giải thuật di truyền (GA) dẫn đầu nhóm thuật toán tối ưu hóa bầy đàn với $56.5\%$. Thuật toán tối ưu hóa bầy đàn hạt (PSO) đứng thứ hai với $18.9\%$. Các thuật toán khác gồm thuật toán đom đóm (FFA) và thuật toán bầy sói xám (GWO).

#### 4.1.2 Xu hướng Dịch chuyển từ Dự đoán Tĩnh sang Động học Chuỗi Thời gian
- Giai đoạn đầu tập trung vào các mô hình tĩnh truyền thống như hồi quy tuyến tính và MLP đơn giản. Các mô hình này dự đoán nồng độ đầu ra tại trạng thái ổn định.
- Giai đoạn hiện nay dịch chuyển mạnh sang dự đoán chuỗi thời gian liên tục. MBR vận hành với đặc tính động học thay đổi liên tục theo tải trọng thủy lực và nồng độ dòng vào.
- Kiến trúc mạng nơ-ron hồi quy với bộ nhớ ngắn-dài (LSTM) giúp mô hình nắm bắt phụ thuộc thời gian dài của quá trình tích tụ sinh khối.
- Mạng nơ-ron tích chập (CNN) và mạng kết nối dày đặc (DenseNet) được ứng dụng để trích xuất đặc trưng không gian từ dữ liệu cảm biến đa chiều và ảnh phổ.
- Mạng nơ-ron sóng nhỏ (WNN) kết hợp phân tích đa độ phân giải với mạng nơ-ron truyền thẳng. Mô hình này giúp nắm bắt các biến động tần số cao của chất lượng nước.

#### 4.1.3 Phân tích Dung lượng Tham số và Tính Ổn định của Kiến trúc Mạng Nơ-ron
- Khả năng biểu diễn của mô hình phụ thuộc trực tiếp vào số lượng tham số huấn luyện (Weights và Biases).
- Mô hình MLP bộc lộ độ ổn định kém trên các tập dữ liệu thực nghiệm biến động mạnh. Hiện tượng này xuất phát từ việc khởi tạo trọng số ngẫu nhiên và nguy cơ rơi vào cực tiểu cục bộ.
- Tích hợp giải thuật tối ưu hóa toàn cục như GA hoặc PSO giúp cải thiện vượt bậc độ ổn định và giá trị $R^2$ của mạng MLP.
- Mạng WNN thể hiện hiệu năng xuất sắc với số lượng tham số rất khiêm tốn. Hàm kích hoạt wavelet dạng sóng cục bộ hóa giúp mạng đạt hệ số xác định $R^2 > 0.99$.
- Hàm kích hoạt Wavelet Morlet chuẩn hóa:
  $$\psi(x) = \cos(1.75 x) \exp\left(-\frac{x^2}{2}\right)$$
- Hàm biến đổi Wavelet liên tục với hệ số co giãn $a$ và độ dịch $b$:
  $$\psi_{a,b}(x) = \frac{1}{\sqrt{|a|}} \psi\left(\frac{x - b}{a}\right)$$
- Hàm kích hoạt RBF Gauss trong mạng RBFNN:
  $$\phi_j(x) = \exp\left(-\frac{\|x - c_j\|^2}{2\sigma_j^2}\right)$$
  trong đó $c_j$ là tâm cụm nơ-ron thứ $j$, $\sigma_j$ là độ rộng vùng tác động của hàm nhân.

#### 4.1.4 Bốn Giới hạn Cốt lõi của các Mô hình Học máy Hiện hành
- Hệ thống chỉ số đầu vào thiếu đồng bộ: Phần lớn mô hình dự đoán loại bỏ chất ô nhiễm bỏ qua các chỉ số lọc màng (MFI chỉ chiếm $20.8\%$) và đặc tính chất gây tắc nghẽn (CFI chiếm $0\%$).
- Thiếu kiểm chứng quy mô công nghiệp thực tế: Đa số nghiên cứu thực hiện ở quy mô phòng thí nghiệm (Lab-scale) hoặc mô hình thí điểm (Pilot-scale). Dữ liệu vận hành trạm quy mô lớn dài hạn còn khan hiếm.
- Rào cản thu thập dữ liệu trực tuyến thời gian thực: Các chỉ số sinh hóa như $\text{BOD}_5$, COD, TN, TP đòi hỏi thời gian phân tích phòng thí nghiệm từ vài giờ đến vài ngày. Điều này cản trở việc dự đoán và điều khiển vòng kín tức thời.
- Thiếu đóng góp vào việc hiểu sâu cơ chế sinh học: Các mô hình hoạt động như hộp đen toán học (Black-box). Mô hình thiếu sự tích hợp tri thức hóa lý và động học phản ứng bùn hoạt tính.

---

### 4.2 Hệ thống Hóa 5 Nhóm Biến số Đầu vào (Input Variables Framework)

```
                            HỆ THỐNG BIẾN SỐ ĐẦU VÀO MBR
                                         │
        ┌──────────────┬─────────────────┼────────────────┬──────────────┐
        ▼              ▼                 ▼                ▼              ▼
     Nhóm 1         Nhóm 2            Nhóm 3           Nhóm 4         Nhóm 5
      CCI            EI                OI               CFI            MFI
  (Chỉ số        (Chỉ số           (Chỉ số          (Đặc tính      (Chỉ số
   Nồng độ)       Môi trường)       Vận hành)        Chất bẩn)      Lọc màng)
        │              │                 │                │              │
   • COD, BOD     • pH, Temp        • HRT, SRT       • SMP, EPS     • TMP, Flux
   • MLSS, MLVSS  • DO, ORP         • Sục khí Qair   • Floc size    • Kháng lực R
   • TN, NH₄⁺-N   • OLR, EC         • Tỉ lệ lọc/nghỉ • Điện thế ζ   • Độ thấm Lm
   • TP, PO₄³⁻                      • Rửa ngược      • Độ nhớt μ    • ΔTMP/Δt
```

#### 4.2.1 Nhóm 1: Chỉ số Nồng độ Thông thường (CCI - Conventional Concentration Indices)
- Tỷ lệ ứng dụng: Nhóm CCI chiếm tỷ lệ cao nhất trong các mô hình dự đoán xử lý ô nhiễm ($75.2\%$) và chiếm $60.4\%$ trong mô hình tắc nghẽn màng.
- Nhu cầu oxy hóa học (COD) và Nhu cầu oxy sinh hóa (BOD): Đo lường hàm lượng cơ chất hữu cơ trong dòng vào ($COD_{\text{in}}, BOD_{\text{in}}$) và dòng ra ($COD_{\text{eff}}, BOD_{\text{eff}}$).
- Tổng cacbon hữu cơ (TOC): Phản ánh tổng lượng cacbon hữu cơ hòa tan và không tan trong hệ thống phản ứng.
- Nồng độ bùn hoạt tính lơ lửng (MLSS) và Bùn lơ lửng dễ bay hơi (MLVSS): Phản ánh mật độ sinh khối vi sinh vật trong bể phản ứng.
- Các hợp chất Nitơ: Tổng nitơ (TN), Amoni ($NH_4^+$-$N$ hoặc $NH_3$-$N$), Nitrit ($NO_2^-$-$N$), Nitrat ($NO_3^-$-$N$).
- Các hợp chất Phốt pho: Tổng phốt pho (TP) và Phốt phát hòa tan ($PO_4^{3-}$).
- Tổng chất rắn lơ lửng dòng vào (TSS) và Tổng chất rắn hòa tan (TDS).
- Sản phẩm polyme sinh học hòa tan và gắn kết:
  + Polyme ngoại bào (EPS) gồm phân đoạn protein ($EPS_p$) và polysaccharide ($EPS_c$).
  + EPS bám lỏng lẻo (LB-EPS) và EPS bám chặt (TB-EPS).
  + Sản phẩm vi sinh vật hòa tan (SMP).

#### 4.2.2 Nhóm 2: Chỉ số Môi trường Dung dịch (EI - Environment Indices)
- Tỷ lệ ứng dụng: Nhóm EI xuất hiện trong $54.2\%$ mô hình dự đoán ô nhiễm.
- Nhiệt độ dung dịch ($T$, °C): Ảnh hưởng trực tiếp đến hoạt tính enzyme vi sinh, độ nhớt chất lỏng và hằng số phân hủy sinh học.
- Nồng độ oxy hòa tan (DO, mg/L): Yếu tố quyết định ranh giới giữa điều kiện hiếu khí, thiếu khí và kỵ khí.
- Độ pH: Tác động mạnh đến cân bằng ion hóa của amoni/amoniac ($NH_4^+ / NH_3$) và hiệu suất enzyme nitrat hóa.
- Thế oxy hóa khử (ORP, mV): Phản ánh trạng thái oxy hóa khử sinh hóa thực tế trong buồng phản ứng.
- Tải trọng hữu cơ thể tích (OLR, $\text{kg COD}/(\text{m}^3 \cdot \text{ngày})$):
  $$\text{OLR} = \frac{COD_{\text{in}} \cdot Q}{V} = \frac{COD_{\text{in}}}{\text{HRT}}$$
- Độ dẫn điện (EC, $\mu\text{S/cm}$) và Độ mặn (Salinity, g/L): Tác động đến áp suất thẩm thấu và cân bằng ion tế bào vi khuẩn.

#### 4.2.3 Nhóm 3: Chỉ số Vận hành Công nghệ (OI - Operation Indices)
- Tỷ lệ ứng dụng: Xuất hiện trong $62.5\%$ mô hình dự đoán chất lượng nước đầu ra.
- Thời gian lưu thủy lực (HRT, giờ):
  $$\text{HRT} = \frac{V}{Q}$$
  trong đó $V$ là thể tích bể phản ứng ($m^3$), $Q$ là lưu lượng nước cấp ($m^3/h$).
- Thời gian lưu bùn (SRT, ngày):
  $$\text{SRT} = \frac{V \cdot X}{Q_w \cdot X_w + Q_{\text{eff}} \cdot X_{\text{eff}}}$$
  trong đó $X$ là nồng độ MLSS trong bể, $Q_w$ và $X_w$ là lưu lượng và nồng độ bùn thải bỏ.
- Thông lượng lọc qua màng ($J$, $\text{L}/(\text{m}^2 \cdot \text{h})$): Đại lượng đo lưu lượng thể tích trên diện tích màng hiệu dụng.
- Cường độ sục khí ($Q_{\text{air}}$ hoặc $SAD_m$, $\text{m}^3/(\text{m}^2 \cdot \text{h})$): Cung cấp oxy hòa tan và tạo lực cắt thủy động lực học rung màng để giảm tắc nghẽn.
- Tỷ lệ lọc - nghỉ (Filtration-Relaxation Ratio): Chu kỳ xen kẽ giữa giai đoạn hút nước lọc và giai đoạn tạm dừng để màng tự phục hồi.
- Cường độ và thời gian rửa ngược (Backwash Duration and Flux): Chu kỳ bơm nước lọc hoặc dung dịch hóa chất ngược chiều để làm sạch lỗ rỗng màng.

#### 4.2.4 Nhóm 4: Đặc tính Chất gây Tắc nghẽn (CFI - Characteristic Foulant Indices)
- Tỷ lệ ứng dụng: Chiếm $0\%$ trong các mô hình dự đoán ô nhiễm trước đây. Tác giả nhấn mạnh đây là thiếu sót kỹ thuật lớn cần khắc phục.
- Nồng độ SMP và các phân đoạn EPS: Tác nhân chính gây bít tắc lỗ rỗng và kết tụ màng sinh học.
- Kích thước bông bùn hoạt tính (Floc size, $\mu\text{m}$) và Phân bố kích thước hạt bùn (PSD - Particle Size Distribution).
- Điện thế Zeta ($\zeta$, mV): Đo điện tích bề mặt bông bùn. Điện thế Zeta âm lớn cản trở sự kết cụm hạt bùn.
- Độ nhớt động lực học hỗn dịch bùn ($\mu$, $\text{mPa}\cdot\text{s}$): Thay đổi phi tuyến tính theo nồng độ MLSS và nhiệt độ.
- Chỉ số thể tích bùn (SVI, mL/g): Phản ánh khả năng lắng và độ xốp của bùn hoạt tính.
- Kích thước lỗ rỗng màng danh định ($d_p$, $\mu\text{m}$) và Hệ số tắc nghẽn màng ($K_b$).

#### 4.2.5 Nhóm 5: Chỉ số Lọc Màng (MFI - Membrane Filtration Indices) và Tham số Thời gian ($t$)
- Tỷ lệ ứng dụng: Chỉ có $20.8\%$ mô hình chất ô nhiễm tích hợp MFI. Tuy nhiên MFI chiếm tới $68.8\%$ trong mô hình tắc nghẽn màng.
- Áp suất xuyên màng (TMP, kPa): Chênh lệch áp suất động lực giữa phía cấp liệu và phía nước thẩm thấu:
  $$\text{TMP} = P_{\text{feed}} - P_{\text{permeate}}$$
- Tốc độ tăng áp suất xuyên màng theo thời gian ($\Delta \text{TMP}/\Delta t$): Đo lường gia tốc bám bẩn trên bề mặt màng.
- Tổng trở lực lọc thủy lực ($R_t$, $\text{m}^{-1}$): Xác định theo định luật Darcy kết hợp mô hình trở lực nối tiếp:
  $$J = \frac{\text{TMP}}{\mu \cdot R_t} = \frac{\text{TMP}}{\mu \cdot (R_m + R_c + R_p)}$$
  trong đó $R_m$ là trở lực màng sạch, $R_c$ là trở lực lớp bánh bùn trên bề mặt, $R_p$ là trở lực bít tắc lỗ rỗng màng không thuận nghịch.
- Độ thấm lọc của màng ($L_m$, $\text{L}/(\text{m}^2 \cdot \text{h} \cdot \text{bar})$):
  $$L_m = \frac{J}{\text{TMP}}$$
- Tham số thời gian vận hành tích lũy ($t$, giờ hoặc ngày): Biểu diễn tuổi thọ của màng và chu kỳ lão hóa vật liệu.

#### 4.2.6 Ma trận Tương quan và Tỷ lệ Ứng dụng Biến số Đầu vào

| Nhóm biến số | Tỷ lệ trong Mô hình Ô nhiễm (%) | Tỷ lệ trong Mô hình Tắc nghẽn (%) | Các thông số đo đạc đại diện chính |
| :--- | :--- | :--- | :--- |
| **CCI** (Chỉ số nồng độ) | $75.2\%$ | $60.4\%$ | COD, BOD, TOC, MLSS, MLVSS, TN, TP, $NH_4^+$-$N$, $NO_3^-$-$N$ |
| **OI** (Chỉ số vận hành) | $62.5\%$ | $45.8\%$ | HRT, SRT, Thông lượng $J$, Cường độ sục khí $Q_{\text{air}}$, Chu kỳ rửa ngược |
| **EI** (Chỉ số môi trường) | $54.2\%$ | $38.5\%$ | Nhiệt độ $T$, pH, Nồng độ oxy hòa tan DO, Thế khử ORP, Độ mặn |
| **MFI** (Chỉ số lọc màng) | $20.8\%$ | $68.8\%$ | Áp suất TMP, Trở lực $R_t$, $R_m$, $R_c$, Độ thấm lọc $L_m$, $\Delta \text{TMP}/\Delta t$ |
| **CFI** (Đặc tính tắc nghẽn)| $0.0\%$ | $31.2\%$ | SMP, EPS bám lỏng/chặt, Kích thước bông bùn, Điện thế Zeta $\zeta$, SVI |
| **Thời gian** ($t$) | $18.5\%$ | $42.6\%$ | Thời gian vận hành tích lũy, Thời gian giữa hai chu kỳ rửa ngược |

---

### 4.3 Ứng dụng Dự đoán Hiệu suất Loại bỏ Chất ô nhiễm

#### 4.3.1 Dự đoán Động học Loại bỏ Hợp chất Hữu cơ (COD, BOD, TOC)
- Mục tiêu đầu ra: Nồng độ COD dòng ra ($COD_{\text{eff}}$) và Hiệu suất loại bỏ COD ($E_{\text{COD}}$) chiếm tới $79.2\%$ các mô hình khảo sát:
  $$E_{\text{COD}} = \frac{COD_{\text{in}} - COD_{\text{eff}}}{COD_{\text{in}}} \times 100\%$$
- Các biến đầu vào có trọng số quyết định: Nồng độ $COD_{\text{in}}$, thời gian lưu thủy lực (HRT), nồng độ sinh khối (MLSS) và nồng độ DO.
- Mô hình phương trình cân bằng vật chất truyền thống:
  $$\frac{dS}{dt} = \frac{Q}{V}(S_{\text{in}} - S) - \frac{\mu_{\max} S}{K_s + S} \frac{X}{Y}$$
  trong đó $S$ là nồng độ COD, $X$ là MLVSS, $\mu_{\max}$ là tốc độ sinh trưởng vi sinh tối đa, $K_s$ là hằng số bán bão hòa, $Y$ là hệ số sản lượng tế bào.
- Hiệu năng mô hình học máy:
  + Mạng MLP chuẩn và SVM đạt hệ số tương quan $R^2$ dao động trong khoảng $0.85$ đến $0.98$.
  + Nghiên cứu của Cai et al. (2019b) áp dụng mạng nơ-ron sóng nhỏ (WNN) cấu trúc 3-2-1 với đầu vào ($COD_{\text{in}}$, $NH_3$-$N_{\text{in}}$, Salinity). Mô hình đạt độ chính xác gần như tuyệt đối với $R^2 = 0.999$.
  + Nghiên cứu của Li et al. (2022) ứng dụng mạng DenseNet trên hệ thống AnMBR. Mô hình dự đoán $COD_{\text{eff}}$ và tốc độ sinh khí sinh học ($CH_4, N_2, CO_2$) đạt độ chính xác $97.4\%$, vượt trội hoàn toàn so với mạng FCN ($92.6\%$) và CNN ($91.8\%$).

#### 4.3.2 Dự đoán Quá trình Chuyển hóa và Loại bỏ Hợp chất Nitơ (TN, NH₄⁺-N, NO₃⁻-N)
- Các biến mục tiêu liên quan đến nitơ chiếm $58.3\%$ số lượng mô hình công bố.
- Bản chất động học sinh học gồm hai công đoạn liên hợp:
  + Quá trình nitrat hóa hiếu khí chuyển hóa amoni thành nitrit và nitrat:
    $$NH_4^+ + 1.5 O_2 \xrightarrow{\text{AOB}} NO_2^- + H_2O + 2H^+$$
    $$NO_2^- + 0.5 O_2 \xrightarrow{\text{NOB}} NO_3^-$$
    Tốc độ phản ứng phụ thuộc mạnh vào nồng độ DO và kiềm:
    $$r_{\text{nit}} = \mu_{\text{max,AUT}} \left( \frac{S_{NH}}{K_{NH} + S_{NH}} \right) \left( \frac{S_O}{K_O + S_O} \right) X_{\text{AUT}}$$
  + Quá trình khử nitrat thiếu khí chuyển nitrat thành khí nitơ:
    $$NO_3^- + 1.08 \text{CH}_3\text{OH} + 0.24 H_2\text{CO}_3 \rightarrow 0.056 C_5H_7O_2N + 0.47 N_2 \uparrow + 1.68 H_2O + HCO_3^-$$
- Ứng dụng mô hình học máy:
  + Mô hình chuỗi thời gian LSTM của Yaqub et al. (2020) cho hệ $A^2/O$-MBR dự đoán loại bỏ $NH_3$-$N$ đạt sai số toàn phương trung bình siêu nhỏ $\text{MSE} = 0.0047$.
  + Mạng lai thông minh GA-ANN và PSO-ANN tối ưu trọng số liên kết giúp xử lý hoàn hảo tương tác phi tuyến phức tạp giữa nồng độ DO, ORP và tỷ lệ hồi lưu bùn ($R^2 > 0.90$).
  + Kim et al. (2021b) kết hợp quang phổ cận hồng ngoại (NIRS) với mạng MLP cấu trúc 5-9-1. Mô hình dự đoán chính xác hàm lượng $TN_{\text{eff}}$, $NH_3$-$N_{\text{eff}}$, $NO_2^-$-$N$ và $NO_3^-$-$N$ với $R^2 > 0.97$.

#### 4.3.3 Dự đoán Quá trình Tích lũy và Loại bỏ Phốt pho (TP, PO₄³⁻)
- Cơ chế loại bỏ phốt pho sinh học tăng cường (EBPR):
  + Sinh vật tích lũy polyphosphate (PAO) giải phóng phốt phát trong điều kiện kỵ khí. PAO hấp thụ lượng lớn phốt phát vượt mức (Luxury Uptake) trong điều kiện hiếu khí.
  + Phốt pho được loại bỏ vật lý khỏi hệ thống thông qua việc xả bùn dư ($Q_w$).
- Tác động hỗ trợ của màng lọc: Màng vi lọc/siêu lọc giữ lại hoàn toàn sinh khối chứa phốt pho. Màng ngăn chặn hiện tượng trôi bông bùn như trong bể lắng truyền thống.
- Dự đoán bằng học máy:
  + Mirbagheri et al. (2015b) sử dụng mô hình RBFNN cấu trúc 5-5-1 cho hệ MBR chìm. Đầu vào gồm $BOD_{\text{in}}$, $COD_{\text{in}}$, $NH_3$-$N$, TP, TDS, HRT, MLVSS và pH. Mô hình dự đoán $TP_{\text{eff}}$ đạt $R^2 > 0.98$.
  + Yaqub et al. (2020) ứng dụng mạng LSTM dự đoán động học loại bỏ TP đạt độ khớp cao trên chuỗi dữ liệu vận hành thực tế.
  + Các biến đầu vào mang tính quyết định bao gồm tỷ số $COD/TP$, chu kỳ kỵ khí-hiếu khí, thời gian lưu bùn SRT và pH hỗn dịch.

#### 4.3.4 Dự đoán Loại bỏ Vi chất Ô nhiễm Nguy hại (Trace Organic Pollutants)
- Nhóm vi chất ô nhiễm bao gồm dược phẩm, thuốc kháng sinh, hợp chất gây rối loạn nội tiết (EDCs), chất hoạt động bề mặt và hóa chất công nghiệp.
- Tỷ lệ nghiên cứu còn khiêm tốn với $16.7\%$ số lượng công bố.
- Cơ chế loại bỏ kép trong hệ màng MBR:
  + Cơ chế hấp phụ và phân hủy sinh học bởi màng sinh học và bùn hoạt tính với thời gian lưu bùn dài (High SRT).
  + Cơ chế cản lọc cơ học bởi kích thước lỗ màng và lớp bánh lọc động sinh học (Dynamic cake layer).
- Thách thức của mô hình học máy:
  + Nồng độ chất ô nhiễm cực thấp ở ngưỡng nanogram hoặc microgram trên lít ($ng/L$ - $\mu g/L$).
  + Cơ chế chuyển hóa động học phân kỳ phức tạp khiến mạng nơ-ron ANN truyền thống kém hiệu quả hơn dự đoán các chỉ số thông thường.
  + Các mô hình cây quyết định (Random Forest, XGBoost) và mô hình tối ưu bầy đàn thể hiện tiềm năng vượt trội trong việc phân loại và dự đoán nồng độ vết.
  + Wolf et al. (2001, 2003) tiên phong ứng dụng MLP dự đoán thành công khả năng loại bỏ các phân tử hữu cơ độc hại gốc clo và hợp chất thơm trong nước thải công nghiệp.

#### 4.3.5 Bảng Tổng hợp Nghiên cứu Thực nghiệm và Kiến trúc Mô hình Tiêu biểu

| Nhóm tác giả & Năm | Loại hình công nghệ MBR | Cấu trúc mô hình ML | Các biến đầu vào chính (Inputs) | Các biến mục tiêu dự đoán (Outputs) | Hiệu năng dự đoán thực nghiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kim et al. (2021b)** | MBR phòng thí nghiệm + Phổ NIRS | MLP (5-11-6, 5-9-1, 5-9-2) | Dữ liệu quang phổ hấp thụ cận hồng ngoại (NIRS) | $COD_{\text{eff}}$, TN, $NH_3$-$N$, $NO_2^-$, $NO_3^-$, $PO_4^{3-}$, SMP, EPS | $R^2 > 0.97$ cho toàn bộ các chỉ tiêu chất lượng |
| **Mirbagheri et al. (2015b)** | MBR ngập nước (Xử lý nước thải đô thị & công nghiệp) | RBFNN (5-5-1) | $BOD_{\text{in}}$, $COD_{\text{in}}$, $NH_3$-$N$, TP, TDS, HRT, MLVSS, pH | $BOD_{\text{eff}}$, $COD_{\text{eff}}$, $NH_3$-$N_{\text{eff}}$, $TP_{\text{eff}}$ | $R^2 > 0.98$ trên toàn bộ tập kiểm tra |
| **Cai et al. (2019b)** | MBR sợi rỗng | WNN (3-2-1) | $COD_{\text{in}}$, $NH_3$-$N_{\text{in}}$, Độ mặn (Salinity) | $COD_{\text{eff}}$, $NH_3$-$N_{\text{eff}}$ | COD đạt $R^2 = 0.999$, $NH_3$-$N$ đạt $R^2 = 0.997$ |
| **Li et al. (2022)** | Bể phản ứng sinh học màng kỵ khí (AnMBR) | DenseNet, CNN, FCN | Nhiệt độ môi trường, Nhiệt độ nước vào, pH vào, $COD_{\text{in}}$, Nhiệt độ bùn, Thông lượng $J$ | pH ra, $COD_{\text{eff}}$, Tỷ lệ khử COD, Sản lượng khí sinh học ($CH_4, N_2, CO_2$), ORP | DenseNet đạt độ chính xác $97.4\%$ (FCN $92.6\%$, CNN $91.8\%$) |
| **Yaqub et al. (2020)** | Hệ thống liên hợp $A^2/O$-MBR | LSTM (Long Short-Term Memory) | $TOC_{\text{in}}$, TN, TP, COD, $NH_3$-$N$, SS, DO, ORP, MLSS | Tỷ lệ loại bỏ TN, TP, $NH_3$-$N$ | Loại bỏ $NH_3$-$N$ tối ưu với sai số $\text{MSE} = 0.0047$ |
| **Wolf et al. (2001, 2003)** | MBR công nghiệp | MLP liên kết truyền thẳng | Chỉ số ô nhiễm cơ bản, Tải trọng hữu cơ, Điều kiện sục khí | Nồng độ vết các hợp chất vi ô nhiễm hữu cơ nguy hại | Dự đoán chính xác xu hướng suy giảm nồng độ vết |

## 5. Ứng dụng Học máy trong Dự đoán Tắc nghẽn Màng (Membrane Fouling)

### 5.1 Tắc nghẽn Màng: Trọng tâm Nghiên cứu Lớn nhất của MBR

#### 5.1.1 Bản chất Vật lý, Hóa học và Sinh học của Hiện tượng Tắc nghẽn Màng
- Khái niệm Tắc nghẽn Màng: Tắc nghẽn màng là sự tích tụ vật chất trên bề mặt màng hoặc bên trong mao quản màng.
- Phân loại Tác nhân Gây bẩn (Foulants): Tắc nghẽn gồm chất hữu cơ, vô cơ, sinh học và hỗn hợp.
- Tắc nghẽn Hữu cơ (Organic Fouling): Hợp chất keo và hòa tan gồm polysaccharides, proteins và humic substances. Các chất này chi phối nhiều giai đoạn tắc nghẽn (Lin et al., 2014, Xu et al., 2020).
- Tắc nghẽn Vô cơ (Inorganic Fouling và Scaling): Các muối khoáng kết tủa như $\text{CaCO}_3$, $\text{CaSO}_4$, muối phosphate, hydroxide sắt và silica bám vào màng.
- Tắc nghẽn Sinh học (Biofouling): Vi sinh vật bám dính, sinh trưởng và tạo lớp màng sinh học (biofilm). Lớp này liên kết nhờ polyme ngoại bào (EPS).
- Tắc nghẽn Hỗn hợp (Composite Fouling): Chất hữu cơ, vi sinh vật và ion $\text{Ca}^{2+}$, $\text{Mg}^{2+}$ tương tác đồng thời. Quá trình này tạo cặn bẩn bền vững.
- Phân loại theo Khả năng Phục hồi:
  - Tắc nghẽn Thuận nghịch (Reversible Fouling): Lực cắt thủy lực, sục khí hoặc rửa ngược (backwash) loại bỏ được lớp cặn bẩn này.
  - Tắc nghẽn Bất thuận nghịch (Irreversible Fouling): Chất bẩn bám dính mạnh hoặc bít sâu lỗ rỗng. Vận hành viên phải dùng hóa chất $\text{NaOCl}$, $\text{NaOH}$ hoặc citric acid.
- Mối Liên hệ Nội tại giữa Xử lý Ô nhiễm và Tắc nghẽn Màng:
  - Quá trình xử lý trong MBR kết hợp bùn hoạt tính sinh học và giữ lại vật lý qua màng.
  - Sự hình thành tắc nghẽn màng gắn liền trực tiếp với quá trình phân hủy chất ô nhiễm.
  - Tắc nghẽn màng có tính phi tuyến rất cao giữa các thông số.
  - Độ phức tạp này tạo tiềm năng lớn cho mô hình học máy phát huy ưu thế mô phỏng.

#### 5.1.2 Tác động Vận hành và Các Chỉ số Trạng thái Màng Cần Dự đoán
- Tác động Tiêu cực của Tắc nghẽn Màng:
  - Làm suy giảm nghiêm trọng thông lượng lọc màng ($J$).
  - Làm tăng đột ngột áp suất xuyên màng ($TMP$). Hiện tượng này tạo nên bước nhảy vọt $TMP$ ($TMP$ jump).
  - Gia tăng điện năng tiêu thụ của máy thổi khí và bơm hút màng.
  - Làm giảm tuổi thọ sợi màng. Hiện tượng này làm tăng chi phí thay màng mới.
- Phân loại Hai Nhóm Bài toán Dự đoán Tắc nghẽn trong Học máy:
  - Nhóm 1: Dự đoán trạng thái lọc (Filtration state prediction).
  - Nhóm 2: Phân tích tắc nghẽn màng (Membrane fouling analysis).
- Các Biến Mục tiêu Đo lường Trạng thái Lọc:
  - Áp suất Xuyên màng ($TMP$): Đơn vị là $\text{kPa}$ hoặc $\text{bar}$. $TMP$ biểu thị chênh lệch áp suất qua màng tại một thông lượng lọc xác định.
  - Thông lượng Lọc ($J$ hay Flux): Đơn vị là $\text{L}/(\text{m}^2\cdot\text{h})$ (viết tắt là $\text{LMH}$). $J$ đo thể tích nước sạch qua một đơn vị diện tích màng trong một giờ.
  - Tốc độ Tăng Áp suất Xuyên màng ($dTMP/dt$): Đơn vị là $\text{kPa/h}$ hoặc $\text{kPa/d}$. Đạo hàm theo thời gian này xác định tốc độ tích tụ chất bẩn.
  - Độ thấm Thủy lực của Màng (Permeability, ký hiệu $P$): $P = \frac{J}{TMP}$, đơn vị là $\text{LMH/bar}$. Chỉ số này đánh giá trực tiếp năng lực dẫn chất lỏng của màng.
  - Tổng Trở lực Lọc Thủy lực ($R_t$): Đơn vị tính là $\text{m}^{-1}$. Định luật Darcy mở rộng mô tả mối quan hệ giữa các biến:
    $$J = \frac{TMP}{\mu \cdot R_t} = \frac{TMP}{\mu \cdot (R_m + R_p + R_c)}$$
    Trong đó:
    - $J$ là thông lượng lọc ($\text{m}^3/(\text{m}^2\cdot\text{s})$).
    - $TMP$ là áp suất xuyên màng ($\text{Pa}$).
    - $\mu$ là độ nhớt động học của chất lỏng lọc ($\text{Pa}\cdot\text{s}$).
    - $R_m$ là trở lực thủy lực bản thân màng sạch ($\text{m}^{-1}$).
    - $R_p$ là trở lực do bít tắc lỗ rỗng màng ($\text{m}^{-1}$).
    - $R_c$ là trở lực của lớp bánh bùn bám trên bề mặt màng ($\text{m}^{-1}$).
- Các Biến Mục tiêu Đo lường Phân tích Tắc nghẽn Màng:
  - Phân loại Dạng Tắc nghẽn (Fouling Type): Nhận diện bít lỗ rỗng hoàn toàn, bít trung gian, bít tiêu chuẩn, hoặc lắng đọng bánh bùn.
  - Tỷ lệ Phục hồi Thông lượng Lọc ($FRR$ - Flux Recovery Rate): Đơn vị tính là $\%$. Công thức xác định:
    $$FRR = \left(\frac{J_c}{J_0}\right) \times 100\%$$
    Trong đó $J_c$ là thông lượng sau khi rửa màng. Ký hiệu $J_0$ là thông lượng ban đầu của màng sạch.
  - Năng lượng Liên diện Bề mặt Màng (Membrane Interfacial Energy): Đơn vị tính là $\text{mJ/m}^2$. Đại lượng này định lượng lực tương tác bám dính giữa hạt bùn và vật liệu màng.

### 5.2 Ứng dụng Mạng Nơ-ron Nhân tạo (ANN) Dự đoán Tắc nghẽn Màng

#### 5.2.1 Tổng quan Kiến trúc và Các Kỹ thuật Tối ưu Hóa Mạng ANN
- Năng lực Học Phi tuyến của ANN: Mạng nơ-ron nhân tạo có khả năng xấp xỉ hàm phi tuyến mạnh mẽ. ANN mô hình hóa chính xác tương tác phức tạp giữa bùn hoạt tính và màng lọc.
- Ba Hướng Cải tiến Mô hình MLP (Multilayer Perceptron):
  - Tối ưu hóa Thuật toán Huấn luyện: Thay thế giải thuật hạ độ dốc bằng Levenberg-Marquardt (LM), Quasi-Newton BFGS, hoặc điều hòa Bayes (Bayesian regularization).
  - Tùy chỉnh Hàm Kích hoạt Tầng Ẩn: Ứng dụng hàm log-sigmoid, tan-sigmoid, hàm cơ sở Gauss (RBF), hoặc hàm sóng Bandelet.
  - Tối ưu hóa Cấu trúc Phân tầng: Tinh chỉnh số tầng và số nơ-ron qua CV, giải thuật di truyền (GA) hoặc bầy hạt (PSO).
- Phân tích Độ nhạy (Sensitivity Factor Analysis): Kỹ thuật này trích xuất tầm quan trọng tương đối của từng biến đầu vào. Phương pháp này giải mã cấu trúc hộp đen của mô hình.

#### 5.2.2 Bảng Tổng hợp và Đối sánh Thực nghiệm Các Mô hình ANN (Table 2)
- Dữ liệu Thực nghiệm: Bảng 2 hệ thống hóa các nghiên cứu dùng ANN dự đoán trạng thái lọc MBR.

| Mô hình | Thuật toán Tối ưu | Hàm Kích hoạt Tầng ẩn | Cấu trúc Mạng ($I\text{-}H\text{-}O$) | Thông số Đầu vào (Inputs) | Thông số Đầu ra (Outputs) | Thuật toán Huấn luyện | Hiệu năng Khớp Thực nghiệm | Tài liệu Trích dẫn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ENN | - | - | 9-55-1 | $T$, SRT, TSS, ODR, $TMP$, $dTMP/dt$, Thời gian lọc và rửa ngược | Thông lượng lọc ($J$) | - | $AD = 2.7\%$ | Geissler et al., 2005 |
| MLP | - | - | 3-5-1 | Thời gian rửa ngược, Thời gian vận hành, Thông lượng lọc ($J$) | Thông lượng lọc ($J$) | LM | $R^2 = 0.99$ | Aidan et al., 2008 |
| MLP | GA | log-sigmoid | - | MLSS, $TMP$, Trở lực màng ($R_t$) | Thông lượng lọc ($J$) | LM | $MAPE = 0.0331$ | Li et al., 2014 |
| MLP | GA | tan-sigmoid | 5-10-1 | Thời gian, MLSS, COD, SRT, TSS | $TMP$, Độ thấm ($P$) | LM | $TMP$: $R^2 = 0.98$, $P$: $R^2 = 0.98$ | Mirbagheri et al., 2015b |
| RBFNN | GA | RBF | 5-5-1 | Thời gian, MLSS, COD, SRT, TSS | $TMP$, Độ thấm ($P$) | LM | $TMP$: $R^2 = 0.98$, $P$: $R^2 = 0.99$ | Mirbagheri et al., 2015b |
| MLP | GA | tan-sigmoid | 6-8-1 | Thông lượng $J$, Tỷ lệ sục khí, Nồng độ SMP và EPS, $TMP$ ban đầu, Thời gian vận hành | $TMP$ (xác định điểm nhảy $TMP$) | Bayesian rule | $\text{Relative MSE} = 0.024$ | Wang và Wu, 2015 |
| RBFNN | CV | RBF | 2-2-1 | Thể tích sục khí, $TMP$ | Thông lượng lọc ($J$) | - | $R^2 = 0.80$ | 2017 |
| MLP | - | log-sigmoid | 6-5-1 | Dòng vào (TN, $\text{NO}_3^-$-N, TP), Dòng ra (TN, $\text{NO}_3^-$-N, TP) | $TMP$ | LM | $R^2 = 0.85$ | Schmitt et al., 2018 |
| Fuzzy-RBFNN | PSO | log-sigmoid | 2-14-49-1 | Thông lượng $J$, Độ biến thiên thông lượng màng | Thông lượng lọc ($J$) | - | $MAPE = 0.0287$ | Tao và Li, 2018 |
| MLP | PSO | - | - | Nhiệt độ $T$, Thông lượng $J$, $TMP$, MLSS | Trở lực lọc ($R_t$) | LM | $R^2 = 0.97$ | Hamedi et al., 2019 |
| MLP | - | tan-sigmoid | 4-8-1 | MLSS, EC, DO, Thời gian | Thông lượng lọc ($J$) | LM | $R^2 = 0.98$ | Hosseinzadeh et al., 2020 |
| RBFNN | - | RBF | 1-3-1 | Áp suất bơm hút thẩm thấu | Thông lượng $J$, $TMP$ | LM | $R^2 > 0.90$ | Abdul Wahab et al. |
| MLP | - | tan-sigmoid | 1-5(7)-1 | Áp suất bơm hút thẩm thấu | Thông lượng $J$, $TMP$ | LM | $R^2 > 0.88$ | Abdul Wahab et al. |
| RNN | - | - | - | EC, Thông lượng lọc ($J$) | EC, Thông lượng lọc ($J$) | - | EC: $RMSE = 18\text{ mS/cm}$, $J$: $RMSE = 1.1\text{ LMH}$ | Viet et al., 2021 |
| MLP | - | tan-sigmoid | 4-30-30-1 | pH, EC, Dòng vào (TN, $\text{NH}_3$-N) | Thông lượng lọc ($J$) | LM | $R^2 = 0.88$ | Viet và Jang, 2021 |
| MLP | - | tan-sigmoid | 4-5-5-5-5-5-5-1 | pH, EC, Dòng vào (TN, $\text{NH}_3$-N) | Trở lực lọc ($R_t$) | LM | $R^2 = 0.86$ | Viet và Jang, 2021 |
| WNN | BA | Bandelet | 5-12-2 | MLSS, Kích thước hạt bùn, EPS, SMP, Độ nhớt bùn, RH, Thế Zeta | Thông lượng $J$, Tỷ lệ phục hồi $FRR$ | Gradient descent | $MAPE = 0.032$ ($3.2\%$) | Zhao et al., 2020 |
| MLP | - | - | 3-17-2 | MLSS, HRT, Thời gian | Thông lượng $J$, Tỷ lệ khử COD | LM | $R^2 = 0.9996$ | Hazrati et al., 2017 |
| ANFIS | - | - | - | Tải trọng OLR, pH dòng ra, MLSS, MLVSS | $TMP$ | LM | $R^2 = 0.98$ | Taheri et al., 2021 |
| MLP | - | log-sigmoid | 6-9-1 | Thời gian, Flux, COD vào, pH, MLSS, Tốc độ thay đổi $TMP$ | Độ thấm ($P$) | - | $R^2 = 0.9985$ | Yao et al., 2022 |
| MLP | - | tan-sigmoid | 3-9-1 | Tốc độ quay đĩa, Khe hở màng-đĩa, Tải nạp OLR | Độ thấm ($P$) | LM | $R^2 = 0.999$ | Irfan et al., 2022 |
| MLP | CV | tan-sigmoid | 6-6-1 | Khả năng lọc của bùn, MLVSS, pH, COD vào, $T$, Chu kỳ rửa | Độ thấm ($P$) | BFGS | $R^2 = 0.93$ | Alkmim et al., 2020 |

- Chú thích thuật ngữ trong bảng: ENN là Elman Neural Network. ODR là Oxygen Decay Rate. EC là Electrical Conductivity. ANFIS là Adaptive Network-based Fuzzy Inference System. BFGS là Broyden-Fletcher-Goldfarb-Shanno. RH là Relative Hydrophobicity. BA là Bat Algorithm. WNN là Wavelet/Bandelet Neural Network. LM là Levenberg-Marquardt. AD là Average Deviation. MAPE là Mean Absolute Percentage Error.

#### 5.2.3 Phân tích Chi tiết Các Công trình Nghiên cứu Điển hình
- Nghiên cứu của Aidan et al. (2008):
  - Nhóm tác giả xây dựng mô hình MLP với cấu trúc 3-5-1.
  - Biến đầu vào gồm thời gian rửa ngược, thời gian vận hành và thông lượng ban đầu.
  - Thuật toán Levenberg-Marquardt (LM) mang lại tốc độ hội tụ cao.
  - Mô hình đạt hệ số xác định thực nghiệm rất cao với $R^2 = 0.99$.
- Nghiên cứu của Li et al. (2014):
  - Nhóm tác giả dùng giải thuật di truyền (GA) tối ưu hóa trọng số khởi tạo của mạng MLP.
  - Tầng ẩn sử dụng hàm kích hoạt phi tuyến log-sigmoid.
  - Biến đầu vào gồm MLSS, áp suất $TMP$ và trở lực màng.
  - Mô hình dự đoán thông lượng lọc ($J$) đạt sai số tuyệt đối trung bình $MAPE = 0.0331$ ($3.31\%$).
- Nghiên cứu của Mirbagheri et al. (2015a, 2015b):
  - Nhóm tác giả đối sánh hai kiến trúc mạng: MLP cấu trúc 5-10-1 (hàm tan-sigmoid) và RBFNN cấu trúc 5-5-1 (hàm Gauss).
  - Thuật toán GA tối ưu cấu trúc mạng. Thuật toán LM thực hiện huấn luyện.
  - Biến đầu vào gồm thời gian, MLSS, COD, SRT và TSS.
  - Hiệu năng mô hình: Cả MLP và RBFNN đều đạt $R^2 = 0.98$ khi dự đoán $TMP$.
  - Khi dự đoán độ thấm ($P$), RBFNN đạt $R^2 = 0.99$ còn MLP đạt $R^2 = 0.98$.
  - Phân tích độ nhạy chỉ ra thời gian vận hành và nồng độ MLSS chi phối mạnh mẽ nhất đến tắc nghẽn màng.
- Nghiên cứu của Wang và Wu (2015):
  - Nhóm nghiên cứu thiết lập mô hình MLP cấu trúc 6-8-1 với hàm tan-sigmoid.
  - Giải thuật GA tối ưu hóa trọng số và bias. Quy tắc điều hòa Bayes (Bayesian rule) thực hiện huấn luyện mạng.
  - Biến đầu vào gồm: Thông lượng $J$, tỷ lệ sục khí, nồng độ SMP và EPS, $TMP$ ban đầu và thời gian vận hành.
  - Mô hình nhận diện chính xác bước nhảy áp suất ($TMP$ jump) với $\text{Relative MSE} = 0.024$.
  - Phát hiện quan trọng: Mô hình MLP trên tập dữ liệu nhỏ kém ổn định hơn mô hình toán truyền thống.
- Nghiên cứu của Alkmim et al. (2020):
  - Mô hình MLP cấu trúc 6-6-1 dùng giải thuật Quasi-Newton BFGS và kiểm định chéo CV.
  - Biến đầu vào gồm: Độ lọc của bùn (sludge filterability), MLVSS, pH, COD vào, nhiệt độ $T$ và chu kỳ làm sạch.
  - Mô hình dự đoán độ thấm màng đạt $R^2 = 0.93$. Kết quả khẳng định vai trò tích cực của thuật toán huấn luyện.
- Nghiên cứu của Zhao et al. (2020):
  - Nhóm tác giả phát triển mạng nơ-ron Bandelet cấu trúc 5-12-2. Mô hình dùng hàm Bandelet làm hàm kích hoạt tầng ẩn.
  - Thuật toán hạ độ dốc huấn luyện mạng. Thuật toán đàn dơi (Bat Algorithm - BA) tối ưu siêu tham số.
  - Biến đầu vào gồm 7 đặc tính bùn: MLSS, kích thước hạt, EPS, SMP, độ nhớt, độ kỵ nước tương đối (RH) và thế Zeta.
  - Mô hình dự đoán đồng thời thông lượng $J$ và tỷ lệ phục hồi $FRR$. Sai số đạt $MAPE = 3.2\%$ trên toàn bộ tập dữ liệu.
- Nghiên cứu của Geissler et al. (2005):
  - Nhóm tác giả dùng mạng nơ-ron hồi quy Elman (ENN) cấu trúc 9-55-1 dự đoán thông lượng màng.
  - Biến đầu vào gồm: Nhiệt độ $T$, SRT, TSS, tốc độ suy giảm oxy (ODR), $TMP$, $dTMP/dt$, thời gian lọc và rửa ngược.
  - Mô hình đạt độ lệch trung bình thực nghiệm $AD = 2.7\%$.
  - Phân tích độ nhạy chứng minh chế độ rửa ngược tối ưu là áp suất cao kết hợp chu kỳ ngắn.
- Nghiên cứu của Viet et al. (2021) và Viet & Jang (2021):
  - Viet et al. (2021) dùng mô hình RNN dự đoán độ dẫn điện ($EC$) và thông lượng ($J$) trong hệ OMBR suốt 40 ngày.
  - Mô hình đạt sai số $RMSE = 18\text{ mS/cm}$ đối với $EC$. Mô hình đạt sai số $RMSE = 1.1\text{ LMH}$ đối với thông lượng lọc.
  - Viet và Jang (2021) phát triển các mạng MLP tầng ẩn sâu với cấu trúc 4-30-30-1 và 4-5-5-5-5-5-5-1.
  - Các mô hình dự đoán thành công thông lượng lọc ($R^2 = 0.88$) và trở lực lọc ($R^2 = 0.86$) từ pH, EC, TN và $\text{NH}_3$-N.

#### 5.2.4 Ứng dụng ANN Phân tích Năng lượng và Tương tác Liên diện Bề mặt Màng
- Dự đoán Năng lượng Tiêu thụ trên Đơn vị Nước sạch:
  - Chen et al. (2012) phát triển mô hình MLP dự đoán điện năng trên một mét khối nước ở trạm MBR quy mô thực.
  - Biến đầu vào gồm công suất sục khí sinh học, sục khí màng, lưu lượng tuần hoàn bùn và thông lượng lọc.
  - Mô hình đạt hệ số xác định $R^2 > 0.55$, giúp tối ưu hóa chi phí vận hành trạm xử lý.
- Định lượng Năng lượng Bề mặt Liên diện Màng (Membrane Interfacial Energy):
  - Zhao et al. (2019) thiết lập mô hình RBFNN định lượng năng lượng liên diện màng sinh học MBR.
  - Biến đầu vào gồm góc tiếp xúc của 3 chất lỏng chuẩn (nước, glycerol, diiodomethane) trên bề mặt bùn và màng.
  - Đầu vào còn có thế zeta của bề mặt bùn và màng cùng khoảng cách giữa hạt bùn và màng.
  - Thời gian tính toán của RBFNN chỉ bằng khoảng $1/50$ thời gian của phương pháp giải tích XDLVO mở rộng.
- Chẩn đoán Tắc nghẽn bằng Xử lý Ảnh với Mạng Nơ-ron Tích chập (CNN):
  - Shi et al. (2022) ứng dụng mạng CNN tích hợp cơ chế tập trung (Attention Mechanism).
  - Mô hình nhận tập ảnh thang độ xám (grayscale images) bề mặt màng để chẩn đoán phân loại trạng thái tắc nghẽn.
  - Độ chính xác chẩn đoán thực nghiệm đạt mức $98\%$.
- Phương pháp Học Không Giám sát (Unsupervised Learning):
  - Woo et al. (2022) ứng dụng thuật toán phân cụm không giám sát để phân tích cơ chế tắc nghẽn màng. Nghiên cứu hỗ trợ tối ưu hóa quy trình rửa lọc.

#### 5.2.5 Phân tích Chuyên sâu Bốn Kiến trúc Mạng Nơ-ron Cốt lõi
- Mạng Nơ-ron Nhiều Tầng Truyền thẳng (MLP và BPNN):
  - Cấu trúc: Mô hình gồm 3 thành phần liên kết: tầng vào ($I$), một hoặc nhiều tầng ẩn ($H$), và tầng ra ($O$).
  - Thuật toán Lan truyền ngược (Back-Propagation): Tín hiệu lan truyền thuận để tính sai số đầu ra. Thuật toán lan truyền ngược đạo hàm hàm mất mát qua quy tắc chuỗi để hiệu chỉnh trọng số $W$ và độ lệch $b$.
  - Ưu điểm: Cấu trúc toán học đơn giản, tốn ít tài nguyên tính toán, khả năng xấp xỉ phi tuyến mạnh.
  - Nhược điểm: BPNN dễ rơi vào cực tiểu cục bộ (local minima). Mạng nhạy cảm với trọng số ban đầu và không có bộ nhớ quá khứ.
- Mạng Nơ-ron Hồi quy Elman (ENN):
  - Cấu trúc Nút Ngữ cảnh (Context Layer): ENN lưu đầu ra của tầng ẩn tại bước trước ($t-1$) vào tầng ngữ cảnh. Tầng này phản hồi lại tầng ẩn tại bước hiện tại ($t$).
  - Phương trình Toán học của ENN:
    $$h(t) = f_H\left(W_{ih} x(t) + W_{ch} h(t-1) + b_h\right)$$
    $$y(t) = f_O\left(W_{ho} h(t) + b_o\right)$$
    Trong đó: $x(t)$ là vector đầu vào tại thời điểm $t$. Ký hiệu $h(t)$ là trạng thái tầng ẩn. Ký hiệu $h(t-1)$ là trạng thái ngữ cảnh lưu vết. Ký hiệu $y(t)$ là đầu ra mạng. Các ma trận $W_{ih}, W_{ch}, W_{ho}$ là trọng số liên kết. Các vector $b_h, b_o$ là ngưỡng lệch.
  - Ưu điểm: Phản ánh trực tiếp động học trễ của quá trình bám bẩn màng. ENN đạt độ chính xác cao hơn MLP tĩnh khi mô phỏng chuỗi thời gian lọc.
- Mạng Nơ-ron Tích chập (CNN):
  - Cấu trúc: Mô hình gồm các lớp tích chập (Convolutional layers), kích hoạt ReLU, lớp gộp (Pooling) và tầng kết nối đầy đủ.
  - Cơ chế Toán học: Toán tử tích chập 2 chiều quét qua ma trận điểm ảnh với bộ lọc hạt nhân $K$:
    $$S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(i-m, j-n) K(m, n)$$
  - Ứng dụng: Nhận diện cấu trúc cặn bẩn qua ảnh vi thể bề mặt màng hoặc bản đồ quang phổ huỳnh quang 3 chiều (3D-EEM).
- Mạng Nơ-ron Bộ nhớ Dài-Ngắn hạn (LSTM) và Mạng Nơ-ron Hồi quy (RNN):
  - Cấu trúc Khối Ô nhớ (Memory Cell): LSTM điều khiển luồng thông tin qua cổng quên ($f_t$), cổng vào ($i_t$) và cổng ra ($o_t$). Ô nhớ trung tâm ($C_t$) duy trì thông tin dài hạn.
  - Hệ Phương trình Toán học Điều khiển LSTM:
    $$f_t = \sigma\left(W_f \cdot [h_{t-1}, x_t] + b_f\right)$$
    $$i_t = \sigma\left(W_i \cdot [h_{t-1}, x_t] + b_i\right)$$
    $$\tilde{C}_t = \tanh\left(W_c \cdot [h_{t-1}, x_t] + b_c\right)$$
    $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
    $$o_t = \sigma\left(W_o \cdot [h_{t-1}, x_t] + b_o\right)$$
    $$h_t = o_t \odot \tanh(C_t)$$
    Trong đó: $\sigma$ là hàm sigmoid chuẩn hóa về khoảng $[0, 1]$. Ký hiệu $\odot$ là phép nhân Hadamard từng phần tử. Ký hiệu $C_t$ là trạng thái ô nhớ lưu giữ thông tin dài hạn. Ký hiệu $h_t$ là vector trạng thái ẩn đầu ra.
  - Ưu thế Tuyệt đối: LSTM triệt tiêu hiện tượng tiêu biến đạo hàm (vanishing gradient) trên chuỗi thời gian dài. Mô hình lưu giữ dữ liệu nhiều chu kỳ lọc và phát hiện sớm bước nhảy vọt $TMP$ ($TMP$ jump).

### 5.3 Ứng dụng các Mô hình Học máy Khác và Mô hình Lai (Hybrid AI)

#### 5.3.1 Máy Véc-tơ Hỗ trợ (SVM / SVR) và Biến thể Bình phương Tối thiểu (LSSVM)
- Nguyên lý Học Thống kê: Mô hình hồi quy véc-tơ hỗ trợ (SVR) hoạt động theo nguyên lý giảm thiểu rủi ro cấu trúc. SVR kiểm soát độ phức tạp để ngăn ngừa hiện tượng quá khớp (overfitting).
- Hàm nhân Gauss (RBF Kernel): SVR dùng hàm nhân RBF để chiếu dữ liệu lên không gian đặc trưng nhiều chiều:
  $$K(x_i, x_j) = \exp\left(-\gamma \|x_i - x_j\|^2\right)$$
  Với $\gamma$ là tham số độ rộng của hàm nhân.
- Nghiên cứu Thực nghiệm của Hamedi et al. (2019):
  - Nhóm tác giả áp dụng mô hình máy véc-tơ hỗ trợ bình phương tối thiểu (LSSVM).
  - Biến đổi Toán học: LSSVM thay thế các bất đẳng thức ràng buộc bằng hệ phương trình đại số tuyến tính:
    $$\begin{bmatrix} 0 & \mathbf{1}^T \\ \mathbf{1} & \mathbf{\Omega} + \gamma^{-1} \mathbf{I} \end{bmatrix} \begin{bmatrix} b \\ \mathbf{\alpha} \end{bmatrix} = \begin{bmatrix} 0 \\ \mathbf{y} \end{bmatrix}$$
    Trong đó $\mathbf{\Omega}_{ij} = K(x_i, x_j)$. Vector $\mathbf{\alpha}$ là nhân tử Lagrange. Tham số $b$ là hệ số chệch.
  - Biến đầu vào gồm: MLSS, $TMP$, thông lượng lọc $J$ và nhiệt độ nước $T$.
  - Biến đầu ra: Trở lực lọc màng ($R_t$).
  - Đối sánh Hiệu năng: LSSVM đạt $R^2 = 0.99$.
  - LSSVM vượt trội hơn mô hình lai PSO-MLP ($R^2 = 0.96$).
  - LSSVM vượt trội hơn mô hình lập trình biểu thức gen GEP ($R^2 = 0.98$).
- Ưu thế Kỹ thuật của SVM/LSSVM: Khả năng khái quát hóa vượt trội trên tập dữ liệu kích thước nhỏ và vừa. Thuật toán tìm ra nghiệm cực tiểu toàn cục duy nhất.

#### 5.3.2 Rừng Ngẫu nhiên (Random Forest) và Các Cây Quyết định Phân cấp
- Nguyên lý Hoạt động của Random Forest (RF):
  - RF là phương pháp học tổ hợp (Ensemble learning) dựa trên kỹ thuật đóng bao (Bagging) từ nhiều cây quyết định.
  - Thuật toán chọn ngẫu nhiên tập dữ liệu con có hoàn lại (bootstrap). Thuật toán cũng chọn ngẫu nhiên tập đặc trưng con tại mỗi điểm phân nhánh.
- Nghiên cứu Thực nghiệm của Li et al. (2020):
  - Cấu trúc Mô hình: Mô hình RF thiết lập 300 cây quyết định với 2 biến đặc trưng tại mỗi nút phân chia.
  - Tiền xử lý bằng Phân tích Thành phần Chính (PCA): Tác giả dùng PCA để sàng lọc biến và loại bỏ đa cộng tuyến (multicollinearity).
  - Biến đầu vào chọn lọc gồm nồng độ MLSS, áp suất $TMP$ và trở lực màng.
  - Biến đầu ra: Thông lượng lọc màng ($J$).
  - Đối sánh Hiệu năng: Mô hình RF đạt $R^2 = 0.95$. RF vượt trội hơn mô hình SVM ($R^2 = 0.92$) và mô hình MLP ($R^2 = 0.89$).
- Định lượng Mức độ Quan trọng của Đặc trưng (Feature Importance):
  - RF cung cấp chỉ số suy giảm độ tinh khiết Gini hoặc sai số mẫu ngoài bao (Out-Of-Bag Importance).
  - Kết quả phân tích chứng minh protein và polysaccharide trong SMP và EPS đóng vai trò chi phối tăng trở lực màng.
  - Đặc tính Mô hình: RF xử lý tốt dữ liệu đa chiều và phi tuyến. RF không đòi hỏi phân phối chuẩn của dữ liệu.

#### 5.3.3 Các Mô hình Lai Thông minh Kết hợp Giải thuật Siêu phỏng sinh (Metaheuristic Hybrid AI)
- 1. Mô hình Lai GA-BP (Genetic Algorithm kết hợp BPNN):
  - Cơ chế Hoạt động: Giải thuật di truyền (GA) mô phỏng tiến hóa tự nhiên gồm chọn lọc, lai ghép và đột biến.
  - GA tìm kiếm toàn cục để xác định trọng số khởi tạo $W_0$ và ngưỡng lệch $b_0$ tối ưu cho mạng BPNN.
  - Khắc phục Nhược điểm: GA loại bỏ sự phụ thuộc khởi tạo ngẫu nhiên của BPNN. Thuật toán giúp mạng tránh rơi vào cực tiểu cục bộ.
  - Bằng chứng Thực nghiệm: Wang và Wu (2015) và Mirbagheri et al. (2015b) chứng minh GA-BP đạt $R^2 > 0.98$. Mô hình tăng tốc độ hội tụ và giảm độ nhạy với nhiễu.
- 2. Mô hình Lai PSO-BP (Particle Swarm Optimization kết hợp BPNN):
  - Cơ chế Hoạt động: Thuật toán tối ưu hóa bầy hạt (PSO) mô phỏng hành vi di chuyển bầy đàn của chim hoặc cá. Mỗi hạt tương ứng với một bộ tham số mạng nơ-ron.
  - Phương trình Cập nhật Vận tốc và Vị trí của Hạt:
    $$v_{i, d}^{(t+1)} = w \cdot v_{i, d}^{(t)} + c_1 r_1 \left(pbest_{i, d} - x_{i, d}^{(t)}\right) + c_2 r_2 \left(gbest_d - x_{i, d}^{(t)}\right)$$
    $$x_{i, d}^{(t+1)} = x_{i, d}^{(t)} + v_{i, d}^{(t+1)}$$
    Trong đó: $w$ là trọng số quán tính. Ký hiệu $c_1, c_2$ là các hệ số gia tốc học tập cá nhân và xã hội. Ký hiệu $r_1, r_2$ là các số ngẫu nhiên phân bố trong đoạn $[0, 1]$. Ký hiệu $pbest_i$ là vị trí tốt nhất của cá nhân hạt $i$. Ký hiệu $gbest$ là vị trí tốt nhất của toàn bầy hạt.
  - Ứng dụng Thực nghiệm: Hamedi et al. (2019) dùng PSO tối ưu cấu trúc MLP đạt $R^2 = 0.97$. Tao và Li (2018) kết hợp PSO với mạng Fuzzy-RBFNN đạt sai số $MAPE = 0.0287$.
- 3. Hệ Suy luận Mờ Thích ứng Nơ-ron (ANFIS - Adaptive Neuro-Fuzzy Inference System):
  - Cơ chế Tích hợp: ANFIS kết hợp cấu trúc suy luận mờ Takagi-Sugeno-Kang (TSK) với khả năng tự học của mạng nơ-ron. Mô hình chuyển đổi dữ liệu cảm biến thành các luật mờ IF-THEN dễ hiểu.
  - Cấu trúc 5 Tầng Chức năng của ANFIS:
    - Tầng 1 (Tầng Mờ hóa): Tính toán độ thuộc của biến đầu vào qua hàm liên thuộc dạng Gauss hoặc Bell:
      $$O_{1, i} = \mu_{A_i}(x) = \exp\left(-\frac{1}{2}\left(\frac{x - c_i}{\sigma_i}\right)^2\right)$$
    - Tầng 2 (Tầng Tính Luật Mờ): Thực hiện phép nhân logic để xác định độ kích hoạt của từng luật:
      $$O_{2, i} = w_i = \mu_{A_i}(x) \cdot \mu_{B_i}(y)$$
    - Tầng 3 (Tầng Chuẩn hóa Trọng số Luật): Tính toán tỷ lệ kích hoạt tương đối của từng luật:
      $$O_{3, i} = \bar{w}_i = \frac{w_i}{\sum_{k} w_k}$$
    - Tầng 4 (Tầng Kết luận Luật): Tính giá trị đầu ra của từng luật tuyến tính con:
      $$O_{4, i} = \bar{w}_i f_i = \bar{w}_i \left(p_i x + q_i y + r_i\right)$$
    - Tầng 5 (Tầng Giải mờ Tổng hợp): Tính toán đầu ra cuối cùng bằng phép cộng dồn tất cả các luật:
      $$O_{5, 1} = y = \sum_{i} \bar{w}_i f_i$$
  - Bằng chứng Thực nghiệm: Taheri et al. (2021) áp dụng ANFIS để dự đoán $TMP$ từ OLR, pH, MLSS và MLVSS với $R^2 = 0.98$.
  - Ưu điểm Nổi bật: ANFIS cung cấp tính minh bạch cơ chế rất cao. Kỹ sư vận hành có thể đọc hiểu và hiệu chỉnh trực tiếp các luật mờ chuyên gia.
- 4. Mạng Nơ-ron Sóng kết hợp Giải thuật Đàn dơi (BA-WNN):
  - Zhao et al. (2020) áp dụng giải thuật dơi (Bat Algorithm - BA) để tối ưu hóa mạng nơ-ron Bandelet. Thuật toán này mô phỏng cơ chế định vị bằng sóng siêu âm.
  - Mô hình dự đoán chính xác cả thông lượng $J$ và tỷ lệ phục hồi $FRR$ với sai số chỉ $3.2\%$.

#### 5.3.4 Bàn luận Kỹ thuật: Quy mô Mẫu Dữ liệu, Đa cộng tuyến và Khả thi Vận hành Trực tuyến
- Độ nhạy với Quy mô Mẫu Dữ liệu (Sample Size Impact):
  - Các mạng nơ-ron sâu và MLP đòi hỏi số lượng mẫu dữ liệu lớn để đạt độ khái quát hóa cao.
  - Khi tập mẫu huấn luyện nhỏ ($N < 100$), mô hình MLP kém ổn định hơn mô hình toán truyền thống (Wang và Wu, 2015).
  - Khi dữ liệu hạn chế, các mô hình SVM, LSSVM và Random Forest đạt độ ổn định cao hơn. Các mô hình này không bị quá khớp.
- Hiện tượng Đa cộng tuyến giữa các Biến Môi trường (Multicollinearity):
  - Tương quan Chéo: Các thông số bùn như MLSS, COD, pH, độ nhớt, EPS và SMP thường tương quan chặt chẽ với nhau.
  - Đưa toàn bộ các biến này vào mô hình dễ gây đa cộng tuyến và làm sai lệch trọng số hồi quy.
  - Giải pháp Kỹ thuật: Sử dụng PCA hoặc phân tích độ nhạy để loại bỏ đặc trưng dư thừa trước khi huấn luyện (Li et al., 2020).
- Thách thức và Định hướng Quan trắc Trực tuyến (Online Real-time Monitoring):
  - Hạn chế Đo đạc: Nhiều nghiên cứu phụ thuộc vào các biến ngoại tuyến như SMP, EPS hoặc góc tiếp xúc bề mặt. Các chỉ tiêu này không thể đo liên tục ngoài hiện trường.
  - Định hướng Thực tế: Mô hình điều khiển tự động thời gian thực cần ưu tiên các biến đo được bằng cảm biến trực tuyến.
  - Biến Trực tuyến Khả thi: Các biến gồm $TMP$, thông lượng $J$, tốc độ tăng áp $dTMP/dt$, độ dẫn điện EC, pH, DO, nhiệt độ $T$ và sục khí màng.

## 6. Bài thực hành Mẫu và Bài tập Mô phỏng Dự đoán Áp suất Xuyên màng (Tutorial Example)

- Bài thực hành triển khai 5 thuật toán Machine Learning tiêu biểu gồm SVM, RF, BPNN, LSTM và GA-BP.
- Mục tiêu chính là mô phỏng và dự đoán động học áp suất xuyên màng ($\text{TMP}$) trong hệ thống màng phản ứng sinh học (MBR).
- Quá trình thực nghiệm được lập trình và tính toán trên nền tảng phần mềm MATLAB.
- Tập dữ liệu nghiên cứu bao gồm 2.000 mẫu quan sát chuỗi thời gian liên tục từ hệ thống MBR vận hành thực tế.
- Kết quả mô phỏng cung cấp cơ sở định lượng để so sánh độ chính xác và khả năng tổng quát hóa giữa các kiến trúc học máy.

---

### 6.1 Quy trình Phương pháp Xây dựng Mô hình (Methodology)

- Quy trình mô hình hóa bao gồm 4 giai đoạn kỹ thuật kế tiếp nhau.
- Giai đoạn 1 thu thập và làm sạch chuỗi dữ liệu vận hành.
- Giai đoạn 2 chuẩn hóa dữ liệu và phân chia tập mẫu thử nghiệm.
- Giai đoạn 3 cấu hình kiến trúc mạng và tối ưu siêu tham số.
- Giai đoạn 4 tính toán các chỉ số thống kê để đánh giá độ chính xác dự báo.

#### 6.1.1 Tiền xử lý Dữ liệu và Chuẩn hóa Min-Max

- **Quy mô tập dữ liệu thực nghiệm**:
  - Tập dữ liệu thô gồm $N = 2.000$ điểm dữ liệu chuỗi thời gian vận hành liên tục từ trạm MBR.
  - Mỗi mẫu dữ liệu ghi nhận đồng thời 8 biến đặc trưng đầu vào và 1 biến mục tiêu đầu ra.
  - Biến mục tiêu đầu ra ($y$) là áp suất xuyên màng $\text{TMP}$ ($\text{kPa}$) phản ánh trực tiếp mức độ tắc nghẽn màng.
  - Tám biến đặc trưng đầu vào ($\mathbf{x}$) phản ánh điều kiện vận hành, chất lượng nước và đặc tính sinh khối:
    1. Nhiệt độ nước thải trong bể phản ứng ($T$, $^{\circ}\text{C}$).
    2. Nồng độ chất rắn lơ lửng trong bùn hoạt tính ($\text{MLSS}$, $\text{mg/L}$).
    3. Độ $\text{pH}$ của hỗn hợp bùn lỏng trong bể sinh học.
    4. Nồng độ oxy hòa tan trong vùng hiếu khí ($\text{DO}_{\text{aerobic}}$, $\text{mg/L}$).
    5. Nhu cầu oxy hóa học của nước thải đầu vào ($\text{COD}_{\text{in}}$, $\text{mg/L}$).
    6. Tổng nitơ của nước thải đầu vào ($\text{TN}_{\text{in}}$, $\text{mg/L}$).
    7. Tổng photpho của nước thải đầu vào ($\text{TP}_{\text{in}}$, $\text{mg/L}$).
    8. Lưu lượng dòng thấm xuyên màng ($\text{Flux}$, $\text{L/(m}^2\cdot\text{h)}$).

- **Làm sạch dữ liệu và loại bỏ giá trị dị biệt**:
  - Dữ liệu thô chứa các điểm nhiễu do lỗi cảm biến đo và bọt khí bám vào đầu dò.
  - Thuật toán kiểm tra giới hạn $3\sigma$ lọc bỏ các giá trị nằm ngoài khoảng tin cậy $[\mu - 3\sigma, \mu + 3\sigma]$.
  - Quá trình làm sạch bảo đảm tính toàn vẹn của chuỗi dữ liệu trước khi đưa vào mô hình học máy.

- **Công thức chuẩn hóa Min-Max Scaling**:
  - Các biến đầu vào có thứ nguyên và khoảng giá trị chênh lệch lớn ($\text{MLSS} > 6.000\text{ mg/L}$, $\text{pH} \approx 7$).
  - Sự chênh lệch thứ nguyên làm sai lệch quá trình cập nhật trọng số trong thuật toán hạ gradient.
  - Hàm `mapminmax` trong MATLAB chuyển đổi toàn bộ miền giá trị của các vector đặc trưng về đoạn $[0, 1]$:
    $$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
  - Trong đó:
    * $x$ là giá trị thực tế của biến đầu vào hoặc biến đầu ra quan sát.
    * $x_{\min}$ là giá trị nhỏ nhất của đặc trưng tương ứng trong toàn bộ tập mẫu dữ liệu.
    * $x_{\max}$ là giá trị lớn nhất của đặc trưng tương ứng trong toàn bộ tập mẫu dữ liệu.
    * $x_{\text{norm}}$ là giá trị chuẩn hóa không thứ nguyên nằm trong đoạn giới hạn $[0, 1]$.
  - Sau khi tính toán dự báo, giá trị $\text{TMP}$ được giải chuẩn hóa về thang đo ban đầu:
    $$\hat{y} = \hat{y}_{\text{norm}} \cdot (y_{\max} - y_{\min}) + y_{\min}$$

- **Chiến lược phân chia tập dữ liệu**:
  - Phương án phân chia ngẫu nhiên trong bài thực hành sử dụng tỷ lệ 70% và 30%.
  - Tập huấn luyện (Training Set) chiếm 70% dữ liệu với $1.400$ mẫu quan sát.
  - Tập kiểm tra độc lập (Testing Set) chiếm 30% dữ liệu với $600$ mẫu quan sát.
  - Phân bố xác suất của tập kiểm tra tương thích chặt chẽ với phân bố của tập huấn luyện.
  - Phân chia độc lập ngăn ngừa hiện tượng rò rỉ thông tin (data leakage) giữa các tập dữ liệu.

#### 6.1.2 Thiết lập Cấu hình 5 Mô hình và Tối ưu Siêu tham số

- **Mô hình 1: Support Vector Machine / Support Vector Regression (SVM / SVR)**:
  - Công cụ thực thi: Thư viện LibSVM tích hợp trên môi trường MATLAB.
  - Dạng hàm nhân: Hàm nhân bán kính xuyên tâm RBF (Radial Basis Function Kernel):
    $$K(\mathbf{x}_i, \mathbf{x}_j) = \exp\left(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2\right) = \exp\left(-\frac{\|\mathbf{x}_i - \mathbf{x}_j\|^2}{2\sigma_{\text{RBF}}^2}\right)$$
  - Tham số hạt nhân $G$ (hoặc $\gamma$): $G = \frac{1}{2\sigma_{\text{RBF}}^2}$ xác định miền ảnh hưởng của từng điểm dữ liệu mẫu.
  - Hệ số phạt $C$: Cân bằng giữa độ phức tạp mô hình và mức độ chấp nhận sai số dải biên $\varepsilon$.
  - Phương pháp tối ưu: Thuật toán tìm kiếm lưới (Grid Search) kết hợp kiểm định chéo (Cross-Validation) tìm cặp $(C, \gamma)$ tối ưu.

- **Mô hình 2: Rừng ngẫu nhiên (Random Forest - RF)**:
  - Công cụ thực thi: `Random Forest Toolbox` trong phần mềm MATLAB.
  - Số lượng cây quyết định: Thiết lập $n_{\text{estimators}} = 100$ cây hồi quy thành phần (CART trees).
  - Thuật toán Ensemble Bagging:
    * Lấy mẫu hoàn lại (bootstrap) từ tập dữ liệu gốc để huấn luyện riêng cho từng cây.
    * Tại mỗi nút rẽ nhánh, thuật toán chọn ngẫu nhiên một tập con đặc trưng ($m = \lfloor\sqrt{8}\rfloor = 2$ hoặc $m = 3$).
    * Giá trị dự báo của rừng là trung bình cộng kết quả từ tất cả các cây:
      $$\hat{y}_{\text{RF}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B T_b(\mathbf{x})$$
  - Cơ chế lấy mẫu ngẫu nhiên giúp giảm phương sai mô hình và hạn chế hiện tượng quá khớp.

- **Mô hình 3: Mạng nơ-ron lan truyền ngược (Back Propagation Neural Network - BPNN)**:
  - Công cụ thực thi: `Neural Network Toolbox` trong môi trường MATLAB.
  - Kiến trúc mạng: Mạng truyền thẳng 3 tầng gồm tầng vào (8 nút), tầng ẩn ($N_h$ nút) và tầng ra (1 nút).
  - Số lượng nơ-ron tầng ẩn được chọn lọc tối ưu trong khoảng $5 \le N_h \le 12$.
  - Hàm kích hoạt: Hàm Sigmoid phi tuyến tại tầng ẩn và hàm Purelin tuyến tính tại tầng ra:
    $$f(z) = \frac{1}{1 + e^{-z}}$$
  - Thuật toán huấn luyện: Thuật toán lan truyền ngược kết hợp tối ưu Levenberg-Marquardt (`trainlm`).
  - Hàm mục tiêu tổn thất cực tiểu hóa tổng bình phương sai số:
    $$E = \frac{1}{2} \sum_{k=1}^n (y_k - \hat{y}_k)^2$$

- **Mô hình 4: Mạng bộ nhớ ngắn-dài (Long Short-Term Memory - LSTM)**:
  - Bản chất kiến trúc: Dạng mạng hồi quy đặc biệt xử lý phụ thuộc thời gian dài và chống triệt tiêu gradient.
  - Mỗi tế bào nhớ (Memory Cell) chứa 3 cổng điều khiển dòng dữ liệu:
    * Cổng quên (Forget Gate): Loại bỏ các thông tin không cần thiết từ trạng thái cũ:
      $$f_t = \sigma\left(W_f \cdot [h_{t-1}, x_t] + b_f\right)$$
    * Cổng vào (Input Gate): Cập nhật thông tin mới vào tế bào nhớ:
      $$i_t = \sigma\left(W_i \cdot [h_{t-1}, x_t] + b_i\right), \quad \tilde{C}_t = \tanh\left(W_c \cdot [h_{t-1}, x_t] + b_c\right)$$
    * Trạng thái tế bào (Cell State): Kết hợp thông tin lưu trữ cũ và mới:
      $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
    * Cổng ra (Output Gate): Quyết định giá trị đầu ra tại bước thời gian hiện tại:
      $$o_t = \sigma\left(W_o \cdot [h_{t-1}, x_t] + b_o\right), \quad h_t = o_t \odot \tanh(C_t)$$
  - Tham số huấn luyện: Kích thước cửa sổ trượt thời gian $w = 5$, tích hợp lớp Dropout để ngăn quá khớp.

- **Mô hình 5: Mạng nơ-ron lai ghép giải thuật di truyền (GA-BP)**:
  - Bản chất cơ chế: Khắc phục điểm yếu rơi vào cực tiểu cục bộ của thuật toán BPNN cổ điển.
  - Giải thuật di truyền (GA) tìm kiếm toàn cục để xác định vector trọng số và ngưỡng lệch ban đầu.
  - Quy mô quần thể: 50 cá thể nhiễm sắc thể tiến hóa qua 100 thế hệ liên tục.
  - Cấu trúc nhiễm sắc thể: Mã hóa toàn bộ trọng số kết nối ($W$) và độ lệch ($b$) thành chuỗi số thực.
  - Hàm thích nghi (Fitness Function): Tỷ lệ nghịch với sai số toàn phương trung bình của mạng:
    $$F = \frac{1}{\text{MSE}} = \frac{1}{\frac{1}{N}\sum_{k=1}^N (y_k - \hat{y}_k)^2}$$
  - Ba toán tử di truyền cốt lõi:
    1. Chọn lọc (Selection): Áp dụng phương pháp bánh xe roulette ưu tiên cá thể có độ thích nghi cao.
    2. Lai ghép (Crossover): Lai ghép số thực giữa các cặp nhiễm sắc thể với xác suất $P_c = 0.8$.
    3. Đột biến (Mutation): Đột biến gen ngẫu nhiên với xác suất $P_m = 0.05$.
  - Sau 100 thế hệ, cá thể tốt nhất cung cấp trọng số khởi tạo tối ưu cho mạng BPNN tinh chỉnh cục bộ.

#### 6.1.3 Các Chỉ số Đánh giá Thống kê

- **Hệ số xác định ($R^2$ - Coefficient of Determination)**:
  - Đo lường tỷ lệ phần trăm phương sai của áp suất $\text{TMP}$ được mô hình giải thích:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó:
    * $y_i$ là giá trị $\text{TMP}$ thực nghiệm quan sát thứ $i$.
    * $\hat{y}_i$ là giá trị $\text{TMP}$ do mô hình dự đoán.
    * $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ là giá trị trung bình của toàn bộ mẫu thực nghiệm.
    * $n$ là tổng số lượng mẫu quan sát trong tập kiểm tra hoặc tập huấn luyện.
  - Giá trị $R^2 \in [0, 1]$; giá trị tiệm cận $1.0$ thể hiện mức độ khớp mô hình hoàn hảo.

- **Sai số bình phương trung bình căn bậc hai ($\text{RMSE}$ - Root Mean Squared Error)**:
  - Đo lường độ lệch tuyệt đối trung bình giữa giá trị dự đoán và giá trị thực nghiệm:
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  - Đơn vị đo của $\text{RMSE}$ trùng với đơn vị của biến mục tiêu ($\text{kPa}$).
  - Trọng số bình phương làm tăng độ nhạy đối với các điểm sai số lớn ngoài biên.
  - Giá trị $\text{RMSE}$ càng nhỏ phản ánh mô hình khống chế sai số cục bộ càng tốt.

- **Sai số phần trăm tuyệt đối trung bình ($\text{MAPE}$ - Mean Absolute Percentage Error)**:
  - Đánh giá sai số tương đối không phụ thuộc vào thang đo thứ nguyên:
    $$\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right| \quad \text{hoặc} \quad \text{MAPE} = \frac{1}{n} \sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
  - Chỉ số thể hiện độ lệch phần trăm trung bình giữa dự báo và thực tế.
  - Giá trị $\text{MAPE} < 0.10$ ($10\%$) biểu thị độ chính xác dự báo ở mức cao trong kỹ thuật vận hành màng.

---

### 6.2 Kết quả Thực nghiệm và Phân tích So sánh Định lượng 5 Mô hình (Results & Discussion)

- Đánh giá thực nghiệm so sánh định lượng 5 mô hình trên cùng một tập dữ liệu chuẩn hóa.
- Phân tích bao gồm đặc tính dữ liệu chuỗi thời gian và hiệu năng dự đoán chi tiết.

#### 6.2.1 Phân tích Đặc tính Chuỗi Thời gian Dữ liệu Thô

- **Đặc tính phân phối thống kê của tập dữ liệu**:
  - Bảng thống kê mô tả ghi nhận các thông số đặc trưng gồm giá trị trung bình, độ lệch chuẩn, cực tiểu và cực đại:
    * Nhiệt độ $T$ biến động theo mùa trong dải $15\text{--}30^{\circ}\text{C}$, ảnh hưởng trực tiếp đến độ nhớt của nước.
    * Nồng độ sinh khối $\text{MLSS}$ duy trì trong khoảng $6.000\text{--}10.000\text{ mg/L}$.
    * Giá trị $\text{pH}$ ổn định trong ngưỡng tối ưu cho vi sinh vật từ $6.8$ đến $7.8$.
    * Nồng độ oxy hòa tan $\text{DO}$ duy trì ở mức $1.5\text{--}3.5\text{ mg/L}$ trong vùng hiếu khí.
    * Các thông số dòng vào $\text{COD}$, $\text{TN}$, $\text{TP}$ phản ánh tải trọng hữu cơ và dinh dưỡng cấp cho bùn hoạt tính.
    * Lưu lượng màng $\text{Flux}$ duy trì ở chế độ dưới tới hạn (sub-critical flux) để kéo dài tuổi thọ màng.
    * Áp suất $\text{TMP}$ biến thiên từ mức khởi điểm $5\text{ kPa}$ lên đến ngưỡng tới hạn $35\text{--}50\text{ kPa}$.

- **Hai giai đoạn động học tắc nghẽn đặc trưng**:
  - Đồ thị diễn biến $\text{TMP}$ theo thời gian thể hiện rõ hai giai đoạn vật lý kế tiếp:
  - **Giai đoạn 1: Tăng chậm ban đầu (Initial slow TMP rise stage)**:
    * Xảy ra do chất hòa tan vi sinh vật (SMP) và hạt keo hấp phụ vào mao quản màng.
    * Quá trình làm hẹp lỗ rỗng màng (pore narrowing) và tắc nghẽn cục bộ bên trong cấu trúc xốp.
    * Tốc độ gia tăng áp suất $\frac{d\text{TMP}}{dt}$ nhỏ, đường đồ thị có độ dốc thấp và kéo dài.
  - **Giai đoạn 2: Tăng vọt áp suất xuyên màng (TMP jump stage)**:
    * Bề mặt màng bị bao phủ hoàn toàn bởi lớp bánh bùn (cake layer) sinh học dày đặc.
    * Lực cản thủy lực tăng cao khiến dòng thấm dồn qua các lỗ rỗng còn lại với vận tốc rất lớn.
    * Hiện tượng nén chặt bánh bùn kích hoạt điểm nhảy vọt áp suất đột ngột ($\frac{d\text{TMP}}{dt} \gg 0$).
    * Mô hình học máy cần nhận diện chính xác điểm uốn này để cảnh báo chu kỳ rửa màng kịp thời.

#### 6.2.2 So sánh Định lượng Hiệu năng 5 Mô hình (SVM, RF, BPNN, LSTM, GA-BP)

- **Bảng tổng hợp chỉ số thực nghiệm chuẩn xác (Table 3)**:

| Chỉ số đánh giá | Phân vùng dữ liệu | SVM | Random Forest (RF) | BPNN | LSTM | GA-BP |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **$R^2$ (Hệ số xác định)** | **Tập huấn luyện (Training)** | 0.8208 | **0.9017** | 0.8199 | 0.8206 | 0.8201 |
| | **Tập kiểm tra (Testing)** | 0.8124 | 0.7344 | 0.8096 | **0.8175** | 0.8128 |
| | **Toàn bộ dữ liệu (All Data)** | 0.8184 | **0.8537** | 0.8170 | 0.8197 | 0.8180 |
| **RMSE (kPa)** | **Tập huấn luyện (Training)** | 1.4075 | **1.0424** | 1.4107 | 1.4080 | 1.4100 |
| | **Tập kiểm tra (Testing)** | 1.3955 | 1.6605 | 1.4058 | **1.3765** | 1.3940 |
| | **Toàn bộ dữ liệu (All Data)** | 1.4039 | **1.2601** | 1.4092 | 1.3987 | 1.4052 |
| **MAPE (tỷ số / %)** | **Tập huấn luyện (Training)** | 0.0616 (6.16%) | **0.0463 (4.63%)** | 0.0629 (6.29%) | 0.0630 (6.30%) | 0.0628 (6.28%) |
| | **Tập kiểm tra (Testing)** | 0.0624 (6.24%) | 0.0737 (7.37%) | 0.0636 (6.36%) | **0.0619 (6.19%)** | 0.0625 (6.25%) |
| | **Toàn bộ dữ liệu (All Data)** | 0.0618 (6.18%) | **0.0545 (5.45%)** | 0.0631 (6.31%) | 0.0626 (6.26%) | 0.0627 (6.27%) |

- **Phân tích hiệu năng trên tập huấn luyện (Training Set)**:
  - Cả 5 mô hình đều thể hiện khả năng khớp dữ liệu tốt với $R^2 > 0.81$.
  - Random Forest đạt độ khớp huấn luyện cao nhất với $R^2 = 0.9017$.
  - RF đạt sai số huấn luyện thấp nhất: $\text{RMSE} = 1.0424\text{ kPa}$ và $\text{MAPE} = 0.0463$ ($4.63\%$).
  - Bốn mô hình SVM, BPNN, LSTM và GA-BP cho kết quả huấn luyện tương đương nhau.
  - Hệ số $R^2$ huấn luyện của 4 mô hình này nằm trong khoảng hẹp từ $0.8199$ đến $0.8208$.
  - Sai số $\text{RMSE}$ huấn luyện dao động ổn định quanh mức $1.4075\text{--}1.4107\text{ kPa}$.

- **Phân tích hiệu năng trên tập kiểm tra độc lập (Testing Set)**:
  - Toàn bộ 5 mô hình chứng minh tính khả thi kỹ thuật với $R^2 > 0.73$.
  - Mô hình LSTM đạt độ chính xác dự báo cao nhất trên tập dữ liệu kiểm tra độc lập.
  - LSTM đạt $R^2 = 0.8175$, $\text{RMSE} = 1.3765\text{ kPa}$ và $\text{MAPE} = 0.0619$ ($6.19\%$).
  - Cơ chế bộ nhớ cổng của LSTM giúp mô phỏng chính xác độ trễ và thời điểm tăng vọt $\text{TMP}$.
  - Mô hình GA-BP xếp thứ hai về độ chính xác với $R^2 = 0.8128$ và $\text{RMSE} = 1.3940\text{ kPa}$.
  - Mô hình SVM duy trì độ ổn định vững chắc với $R^2 = 0.8124$ và $\text{RMSE} = 1.3955\text{ kPa}$.

- **Cơ chế suy giảm khả năng tổng quát hóa của Random Forest**:
  - Mô hình RF thể hiện sự sụt giảm hiệu năng rõ rệt từ tập huấn luyện sang tập kiểm tra.
  - Hệ số $R^2$ của RF giảm mạnh từ $0.9017$ xuống $0.7344$ (giảm $18.55\%$).
  - Sai số $\text{RMSE}$ tăng vọt từ $1.0424\text{ kPa}$ lên $1.6605\text{ kPa}$ (tăng $59.29\%$).
  - Chỉ số $\text{MAPE}$ tăng từ $4.63\%$ lên $7.37\%$.
  - Về mặt lý thuyết toán học cơ bản, thuật toán RF không bị quá khớp do quy luật số lớn.
  - Tuy nhiên, hiện tượng cộng tuyến đa biến giữa các đặc trưng làm suy giảm khả năng dự đoán.
  - Các biến $\text{COD}$, $\text{MLSS}$, $\text{DO}$ và nhiệt độ trong trạm MBR có mức tương quan dư thừa cao.
  - Việc lấy mẫu đặc trưng ngẫu nhiên tại các nút rẽ nhánh đưa các biến nhiễu vào cây quyết định.
  - Giải pháp cải thiện hiệu năng RF bao gồm:
    * Tăng số lượng cây quyết định lên trên 200 cây.
    * Áp dụng kỹ thuật lọc chọn đặc trưng (Feature Selection) loại bỏ biến dư thừa.
    * Tối ưu hóa thuật toán cắt tỉa cành cây (Pruning Algorithm).

- **Cơ chế ưu việt của mô hình lai GA-BP so với BPNN truyền thống**:
  - Mạng BPNN tiêu chuẩn dùng thuật toán hạ gradient dễ mắc kẹt tại điểm cực tiểu cục bộ.
  - Hiệu quả huấn luyện BPNN phụ thuộc lớn vào việc gán ngẫu nhiên trọng số ban đầu.
  - Giải thuật di truyền GA tìm kiếm đa hướng trên toàn bộ không gian trọng số và ngưỡng lệch.
  - Quá trình chọn lọc, lai ghép và đột biến đưa bộ thông số về vùng trũng tối ưu toàn cục.
  - GA-BP cải thiện chỉ số $R^2$ kiểm tra từ $0.8096$ (BPNN) lên $0.8128$.
  - GA-BP giảm $\text{RMSE}$ kiểm tra từ $1.4058\text{ kPa}$ xuống $1.3940\text{ kPa}$.
  - GA-BP giảm $\text{MAPE}$ kiểm tra từ $0.0636$ xuống $0.0625$, tương đương mức cải thiện sai số từ 8% đến 12%.
  - Khởi tạo trọng số bằng GA tăng tốc độ hội tụ và ngăn ngừa hiện tượng bão hòa tín hiệu đạo hàm.

## 7. Thách thức Cốt lõi, Triển vọng Công nghệ Mới và Kết luận Chung

### 7.1 Bốn Thách thức Kỹ thuật Cốt lõi Hiện nay

#### 7.1.1 Rào cản Hệ biến số Đầu vào (Input Feature Barrier)
- Hiện trạng lựa chọn biến số: Các mô hình học máy hiện nay chủ yếu dùng các chỉ số vĩ mô quy ước. Các chỉ số này gồm COD, BOD, MLSS, pH và nhiệt độ. Chúng không phản ánh bản chất hóa lý ở cấp độ phân tử của màng lọc và bùn hoạt tính.
- Thiếu hụt thông số keo tụ và tương tác liên bề mặt: Mô hình bỏ qua các lực liên kết bề mặt theo lý thuyết XDLVO (Extended Derjaguin-Landau-Verwey-Overbeek). Lực tương tác bề mặt tổng cộng quyết định bám dính chất bẩn được xác định bởi:
  $$\Delta G_{total}(h) = \Delta G^{LW}(h) + \Delta G^{AB}(h) + \Delta G^{EL}(h)$$
  Trong đó: $\Delta G^{LW}$ là năng lượng tương tác Van der Waals Lifshitz. $\Delta G^{AB}$ là năng lượng tương tác axit bazơ Lewis (tương tác kỵ nước). $\Delta G^{EL}$ là năng lượng tương tác tĩnh điện hai lớp điện tích.
- Thiếu hụt đặc trưng nano bề mặt màng: Cấu trúc hình thái lỗ màng, độ nhám bề mặt ($R_a$, $R_q$), điện tích bề mặt qua điện thế Zeta ($\zeta$), và góc tiếp xúc nước ($\theta$) hiếm khi được đưa vào tập huấn luyện. Sự biến đổi của các thông số này theo thời gian vận hành làm sai lệch dự đoán.
- Phân đoạn chưa đầy đủ của chất ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP): Mô hình chỉ ghi nhận tổng nồng độ protein ($PN$) và polysaccharide ($PS$). Mô hình bỏ qua phân bố trọng lượng phân tử, hàm lượng chất mùn và cấu trúc gel 3D của các polyme sinh học này.
- Thiếu liên kết giữa chỉ số vận hành và trạng thái thủy lực: Các chỉ số lọc màng thông thường (MFI, CCI) thường được sử dụng. Tuy nhiên, các chỉ số vận hành (OI) liên quan trực tiếp đến chu kỳ rửa ngược (backwash), chu kỳ ngừng hút (relaxation) và chế độ sục khí sủi bọt (scouring) chưa được tích hợp đầy đủ.

#### 7.1.2 Rào cản Phương pháp Quan trắc Ngoại tuyến (Online Monitoring Barrier)
- Độ trễ thời gian của lấy mẫu ngoại tuyến: Các phép phân tích hóa lý cốt lõi (COD, MLSS, EPS, SMP) hiện phụ thuộc vào lấy mẫu thủ công định kỳ. Thời gian xử lý trong phòng thí nghiệm kéo dài từ 2 giờ đến 5 ngày.
- Mất mát động học thời gian thực: Hiện tượng tăng vọt TMP (TMP jump) trong MBR diễn ra đột ngột chỉ trong vài phút đến vài giờ. Dữ liệu lấy mẫu ngoại tuyến không thể bắt kịp điểm chuyển pha tới hạn này.
- Sự bất cập của các cảm biến trực tuyến thông thường: Các cảm biến công nghiệp truyền thống (pH, DO, ORP, độ đục) chỉ cung cấp thông tin sơ cấp về môi trường lỏng. Chúng không cung cấp cấu trúc hóa học hoặc hoạt tính sinh học của chất gây tắc màng.
- Chi phí bảo trì đầu đo cao: Cảm biến nhúng chìm trong bể hiếu khí thường xuyên bị bám bẩn sinh học (biofouling). Đầu đo cần nhân công vệ sinh và hiệu chuẩn liên tục.

#### 7.1.3 Rào cản Chiến lược Điều khiển và Vận hành Tự động (Feedforward Control Barrier)
- Tình trạng mô phỏng thụ động: Đa số các công bố học máy dừng lại ở việc dự đoán ngoại tuyến giá trị TMP hoặc thông lượng $J$ từ dữ liệu lịch sử.
- Thiếu cơ chế phản hồi trước (Feedforward Control): Hệ thống MBR cần hành động phòng ngừa trước khi tắc nghẽn xảy ra. Việc phản ứng thụ động sau khi TMP đã tăng cao gây hư hại cấu trúc màng không thể phục hồi.
- Thiếu liên kết với bộ điều khiển vật lý: Đầu ra mô hình chưa được liên kết trực tiếp với hệ thống SCADA hoặc PLC. Mô hình chưa thể tự động điều chỉnh tần số biến tần của máy thổi khí, bơm hút màng và van định lượng hóa chất tẩy rửa.
- Động học tắc màng phi tuyến phức tạp: Sự tích tụ lớp bánh bùn (cake layer) tuân theo động học phi tuyến kép:
  $$\frac{dR_c}{dt} = \frac{\alpha \cdot C_b \cdot J^2}{\Delta \text{TMP}} - k_{wash} \cdot G_a \cdot R_c$$
  Trong đó: $\alpha$ là trở lực riêng của lớp bánh lọc. $C_b$ là nồng độ bùn trong bể. $G_a$ là cường độ sục khí cắt bề mặt. $k_{wash}$ là hệ số rửa trôi cơ học. Các mô hình điều khiển tuyến tính truyền thống (PID) không đáp ứng được động thái phi tuyến này.

#### 7.1.4 Rào cản Dữ liệu Chuẩn hóa và Khả năng Tổng quát hóa (Open Benchmark Dataset Barrier)
- Thiếu cơ sở dữ liệu mở chuẩn hóa: Ngành xử lý nước chưa có kho dữ liệu mở quy mô lớn tương tự như ImageNet trong thị giác máy tính.
- Sự phân tán và sai lệch điều kiện thử nghiệm: Dữ liệu hiện tại bị phân mảnh tại từng phòng thí nghiệm riêng lẻ. Quy mô bể, loại nước thải, vật liệu màng (PVDF, PTFE, PES) và thông số thủy lực khác nhau hoàn toàn.
- Hiện tượng suy giảm năng lực tổng quát hóa (Domain Shift): Một mô hình huấn luyện trên bể phản ứng quy mô pilot trong phòng thí nghiệm thường thất bại khi áp dụng vào trạm xử lý nước thải đô thị quy mô lớn. Nguyên nhân là sự thay đổi bất thường của lưu lượng tải và thành phần nước thải công nghiệp hòa trộn.
- Thiếu quy chuẩn tiền xử lý dữ liệu: Các nghiên cứu áp dụng các phương pháp lọc nhiễu, chuẩn hóa (Min-Max, Z-score) và chia tập dữ liệu huấn luyện khác nhau. Điều này gây khó khăn khi đối chiếu khách quan giữa các công trình.

---

### 7.2 Định hướng Công nghệ Mới và Kiến trúc AI Thế hệ Mới

#### 7.2.1 Công nghệ Quan trắc Trực tuyến Nâng cao bằng Quang phổ (UV-Vis và 3D-EEM)
- Quang phổ tử ngoại khả kiến (UV-Vis Spectroscopy): Cảm biến quang học đo độ hấp thụ tại bước sóng 254 nm ($\text{UV}_{254}$) và tỷ số $\text{SUVA}_{254} = \frac{\text{UV}_{254} \times 100}{\text{DOC}}$. Chỉ số này định lượng hàm lượng hợp chất thơm và tiền chất gây tắc nghẽn màng trong vòng vài giây.
- Bản đồ huỳnh quang kích thích phát xạ 3 chiều (3D-EEM): Phân giải các vùng quang phổ huỳnh quang huỳnh quang đặc trưng:
  + Vùng I và II (Kích thích $\lambda_{ex} = 220 - 250$ nm, Phát xạ $\lambda_{em} = 280 - 380$ nm): Hợp chất thơm dạng protein (Tyrosine và Tryptophan).
  + Vùng III ($\lambda_{ex} = 220 - 250$ nm, $\lambda_{em} > 380$ nm): Axit fulvic.
  + Vùng IV ($\lambda_{ex} = 250 - 400$ nm, $\lambda_{em} = 280 - 380$ nm): Sản phẩm hòa tan của vi sinh vật (SMP).
  + Vùng V ($\lambda_{ex} > 250$ nm, $\lambda_{em} > 380$ nm): Axit humic.
- Tích hợp dấu vân tay quang học vào mô hình AI: Chuyển đổi dữ liệu quang phổ trực tuyến thành ma trận số học đầu vào. Mô hình nhận diện biến động nồng độ chất gây tắc màng trước khi màng bị nghẽn vật lý.

#### 7.2.2 Học máy Tự động (AutoML - Automated Machine Learning)
- Tự động hóa toàn bộ đường ống dẫn dữ liệu (End-to-End Pipeline):
  $$\mathcal{P}^* = \arg\min_{\mathcal{P} \in \mathbf{\Omega}} \mathcal{L}(\mathcal{P}(\mathcal{D}_{train}), \mathcal{D}_{val})$$
  Quy trình tự động thực hiện: làm sạch dữ liệu, chọn lọc đặc trưng (Feature Selection), lựa chọn thuật toán học máy, và tối ưu hóa siêu tham số (HPO).
- Giải phóng rào cản nhân lực chuyên gia: Kỹ sư công nghệ môi trường không cần kiến thức sâu về khoa học máy tính vẫn xây dựng được mô hình dự đoán TMP đạt chuẩn.
- Tối ưu hóa dưới ràng buộc tài nguyên cố định: AutoML áp dụng thuật toán Bayesian Optimization hoặc Tree-structured Parzen Estimator (TPE). Phương pháp tìm kiếm siêu tham số tối ưu với số lượt chạy tính toán thấp nhất.

#### 7.2.3 Trí tuệ Nhân tạo có thể Giải thích (XAI và Phân tích SHAP)
- Giải quyết bài toán hộp đen (Black-box Problem): Các mạng nơ-ron sâu thường không minh bạch. XAI giúp các nhà vận hành trạm hiểu rõ lý do mô hình đưa ra dự báo.
- Định lượng đóng góp đặc trưng bằng giá trị Shapley (SHAP):
  $$\phi_i(x) = \sum_{S \subseteq \mathcal{F} \setminus \{i\}} \frac{|S|!(|\mathcal{F}| - |S| - 1)!}{|\mathcal{F}|!} \left[ f(S \cup \{i\}) - f(S) \right]$$
  Trong đó: $\mathcal{F}$ là tập hợp tất cả biến đặc trưng đầu vào. $S$ là tập con các biến không chứa biến thứ $i$. Biểu thức $f(S \cup \{i\}) - f(S)$ thể hiện đóng góp biên của biến thứ $i$.
- Mô hình giải thích cục bộ cộng tính:
  $$g(z') = \phi_0 + \sum_{i=1}^M \phi_i z_i'$$
  Biểu đồ SHAP Summary Plot và SHAP Dependence Plot vạch rõ mối quan hệ phi tuyến và ngưỡng nồng độ tới hạn của MLSS, pH và nhiệt độ đối với tốc độ tăng TMP.

#### 7.2.4 Mạng Nơ-ron Tích hợp Tri thức Vật lý (PINN - Physics-Informed Neural Networks)
- Bản chất cấu trúc PINN: Nhúng các định luật bảo toàn khối lượng, phương trình động học Monod và định luật lọc Darcy trực tiếp vào hàm mất mát của mạng nơ-ron.
- Hàm mất mát đa mục tiêu kết hợp tri thức vật lý:
  $$\mathcal{L}_{total}(\theta) = \mathcal{L}_{data}(\theta) + \lambda_{phys} \mathcal{L}_{phys}(\theta) + \lambda_{bc} \mathcal{L}_{bc}(\theta)$$
  Trong đó:
  $$\mathcal{L}_{data}(\theta) = \frac{1}{N_d} \sum_{i=1}^{N_d} \left| y_i - \hat{y}(x_i; \theta) \right|^2$$
  $$\mathcal{L}_{phys}(\theta) = \frac{1}{N_c} \sum_{j=1}^{N_c} \left| \mathcal{F}\left[ \hat{y}(x_j; \theta) \right] \right|^2$$
- Phương trình chi phối vật lý màng MBR:
  $$J(t) = \frac{\Delta \text{TMP}(t)}{\mu(T) \cdot \left[ R_m + R_p(t) + R_c(t) \right]}$$
  Toán tử vi phân phần dư:
  $$\mathcal{F}[\hat{y}] = \frac{\partial R_c}{\partial t} - \left( \alpha_{spec} C_b J^2 - k_e G \tau R_c \right)$$
- Ưu thế vượt trội: Mô hình vẫn cho kết quả chính xác cao ngay cả khi dữ liệu thực đo bị thiếu hụt hoặc lẫn nhiều nhiễu cảm biến. Dự đoán luôn tuân thủ nguyên lý nhiệt động lực học và thủy lực học.

#### 7.2.5 Mạng Kolmogorov-Arnold (KAN - Kolmogorov-Arnold Networks)
- Cơ sở lý thuyết toán học: Dựa trên định lý xấp xỉ hàm Kolmogorov-Arnold. Một hàm số liên tục nhiều biến có thể phân rã thành tổng các hàm đơn biến liên tục:
  $$f(x_1, \dots, x_n) = \sum_{q=1}^{2n+1} \Phi_q \left( \sum_{p=1}^n \phi_{q,p}(x_p) \right)$$
- Khác biệt cấu trúc so với MLP truyền thống:
  + Mạng MLP đặt các hàm kích hoạt cố định ($\text{ReLU}, \text{Sigmoid}$) tại các nơ-ron và học các ma trận trọng số tuyến tính trên cạnh nối.
  + Mạng KAN đặt các hàm kích hoạt học được dạng đường cong B-spline trực tiếp trên các liên kết trọng số:
    $$\phi(x) = w_b \cdot b(x) + w_s \cdot \text{spline}(x)$$
    Trong đó $b(x) = \frac{x}{1 + e^{-x}}$ là hàm cơ sở siLU.
- Khả năng trích xuất công thức tường minh: KAN cho phép chuyển đổi mạng nơ-ron đã huấn luyện thành công thức toán học giải tích đơn giản. Kỹ sư có thể kiểm tra trực tiếp cơ chế tắc màng mà không cần dựa vào mạng hộp đen.

#### 7.2.6 Kiến trúc Hồi quy Mở rộng xLSTM và Mô hình Nền tảng Transformer
- Hạn chế của mạng LSTM cổ điển: LSTM truyền thống không thể cập nhật bộ nhớ theo cấu trúc ma trận. Mô hình bị suy giảm khả năng ghi nhớ khi chiều dài chuỗi vượt quá vài tuần vận hành MBR.
- Đổi mới của xLSTM (Extended Long Short-Term Memory):
  + Cổng điều khiển hàm mũ (Exponential Gating) giúp cải thiện độ ổn định gradient trong chuỗi thời gian dài:
    $$i_t = \exp\left(W_i x_t + R_i h_{t-1}\right)$$
    $$f_t = \exp\left(W_f x_t + R_f h_{t-1}\right)$$
  + Bộ nhớ ma trận (Matrix Memory mLSTM) với quy tắc cập nhật tích ngoài:
    $$C_t = f_t C_{t-1} + i_t v_t k_t^T$$
    Trạng thái ẩn đầu ra được chuẩn hóa trực tiếp:
    $$h_t = \tilde{o}_t \odot \frac{C_t q_t}{\max\left( m_t, k_t^T q_t \right)}$$
- Ứng dụng Transformer đa phương thức: Xử lý đồng thời dữ liệu chuỗi cảm biến thời gian thực, hình ảnh kính hiển vi bám bẩn bề mặt màng và tín hiệu quang phổ 3D-EEM trên quy mô toàn nhà máy.

#### 7.2.7 Hệ thống Bản sao Số Thông minh (Digital Twin for MBR)
- Cấu trúc hệ thống Digital Twin: Tạo lập một bản sao ảo tương đương thời gian thực của trạm MBR vật lý thông qua 3 lớp:
  + Lớp Vật lý: Cụm màng sợi rỗng hoặc màng tấm phẳng, máy thổi khí, bơm tuần hoàn bùn, cảm biến đo đạc và bộ điều khiển PLC.
  + Lớp Truyền thông IoT: Kết nối dữ liệu thời gian thực thông qua giao thức Modbus TCP/IP, OPC UA và MQTT với độ trễ dưới một giây.
  + Lớp Không gian Ảo (Virtual Cyber Space): Tích hợp đồng thời mô hình thủy lực PINN, mô hình dự đoán tăng trưởng vi sinh và thuật toán tối ưu hóa đa mục tiêu.
- Cơ chế vận hành tối ưu hóa năng lượng và kiểm soát tắc màng:
  ```mermaid
  flowchart LR
    A["Cảm biến Online: TMP, Flux, UV-Vis, DO"] --> B["SCADA / IoT Gateway"]
    B --> C["Bản sao số Digital Twin: PINN + AutoML"]
    C --> D["Cảnh báo sớm xu hướng tắc màng dTMP/dt"]
    D --> E["Bộ điều khiển phản hồi trước Feedforward"]
    E --> F["Tối ưu biến tần sục khí Q_air"]
    E --> G["Tối ưu chu kỳ sục rửa ngược Delta t_bw"]
    F --> H["Trạm MBR Vật lý"]
    G --> H
  ```
- Lợi ích kinh tế và kỹ thuật: Giảm 15% đến 25% điện năng sục khí màng. Kéo dài tuổi thọ cụm màng thêm 20% đến 30%. Hạn chế tối đa số lần tẩy rửa hóa học phục hồi (CIP).

---

### 7.3 Kết luận Chung (Conclusions)

#### 7.3.1 Tổng kết Vai trò Chuyển đổi của Học máy trong MBR
- Khẳng định vị trí khoa học: Học máy giải quyết triệt để sự bế tắc của các mô hình toán lý cổ điển trong việc nắm bắt các tương tác vi mô phi tuyến của quá trình tắc màng.
- Đa dạng hóa kiến trúc mô hình: Các thuật toán chuyển dịch từ mô hình cấu trúc nông (SVM, Random Forest, BPNN) sang các hệ thống mạng nơ-ron động lực học (LSTM, xLSTM) và mô hình tích hợp tri thức vật lý (PINN, KAN).
- Đóng góp vào chuyển đổi số trạm xử lý nước: AI chuyển đổi trạm MBR từ vận hành thủ công dựa vào kinh nghiệm sang hệ thống tự động hóa hoàn toàn.

#### 7.3.2 Phân tích Đối sánh Kết quả Thực hành (Tutorial Benchmark Evaluation)
- Tổng hợp số liệu định lượng: Bảng đối soát hiệu năng giữa 5 thuật toán học máy dựa trên 2000 điểm dữ liệu vận hành thực nghiệm MBR:

| Mô hình Học máy | Tập Huấn luyện $R^2$ | Tập Kiểm tra $R^2$ | Toàn bộ Dữ liệu $R^2$ | Huấn luyện RMSE | Kiểm tra RMSE | Toàn bộ RMSE | Huấn luyện MAPE | Kiểm tra MAPE | Toàn bộ MAPE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SVM** | 0.8208 | 0.8124 | 0.8184 | 1.4075 | 1.3955 | 1.4039 | 0.0616 | 0.0624 | 0.0618 |
| **RF** | **0.9017** | 0.7344 | **0.8537** | **1.0424** | 1.6605 | **1.2601** | **0.0463** | 0.0737 | **0.0545** |
| **BPNN** | 0.8199 | 0.8096 | 0.8170 | 1.4107 | 1.4058 | 1.4092 | 0.0629 | 0.0636 | 0.0631 |
| **LSTM** | 0.8206 | **0.8175** | 0.8197 | 1.4080 | **1.3765** | 1.3987 | 0.0630 | **0.0619** | 0.0626 |
| **GA-BP** | 0.8201 | 0.8128 | 0.8180 | 1.4100 | 1.3940 | 1.4052 | 0.0628 | 0.0625 | 0.0627 |

- Phân tích chi tiết hành vi của từng mô hình:
  + Cả 5 mô hình đều chứng minh tính khả thi cao với $R^2 > 0.80$ trên toàn bộ tập dữ liệu, sai số MAPE dưới 6.5%.
  + Hiện tượng quá khớp (Overfitting) nghiêm trọng của Random Forest (RF): RF đạt $R^2$ huấn luyện cao nhất (0.9017) và RMSE thấp nhất (1.0424). Tuy nhiên, trên tập kiểm tra độc lập, $R^2$ của RF giảm mạnh xuống 0.7344 và RMSE tăng lên 1.6605. Nguyên nhân là do cấu trúc cây quyết định phân chia không gian quá chi tiết, dễ bắt nhiễu khi các biến đặc trưng có độ dư thừa cao.
  + Hiệu năng vượt trội của LSTM trên dữ liệu kiểm tra: LSTM đạt $R^2$ kiểm tra cao nhất (0.8175), RMSE kiểm tra thấp nhất (1.3765) và MAPE thấp nhất (0.0619). Điều này chứng minh cấu trúc cổng nhớ ghi nhận xuất sắc tính phụ thuộc thời gian của sự tích lũy trở lực màng.
  + Độ ổn định và bền bỉ của mô hình lai GA-BP: Giải thuật di truyền tối ưu hóa trọng số khởi tạo ban đầu, giúp mạng BPNN tránh rơi vào cực tiểu cục bộ. GA-BP duy trì sai số cực kỳ cân bằng giữa tập huấn luyện ($R^2 = 0.8201$, $\text{RMSE} = 1.4100$) và tập kiểm tra ($R^2 = 0.8128$, $\text{RMSE} = 1.3940$).

#### 7.3.3 Lộ trình Triển khai Trạm Xử lý MBR Tự hành Thông minh
- Giai đoạn 1: Chuẩn hóa dữ liệu và cảm biến hóa trực tuyến (Năm 1 - 2): Lắp đặt đầu dò UV-Vis, cảm biến huỳnh quang và chuẩn hóa hạ tầng SCADA. Xây dựng kho dữ liệu mở MBR toàn cầu.
- Giai đoạn 2: Tích hợp mô hình AI giải thích được và tối ưu hóa siêu tham số (Năm 2 - 3): Triển khai AutoML để rút ngắn thời gian phát triển mô hình. Áp dụng SHAP để cung cấp khuyến nghị vận hành minh bạch cho kỹ sư trạm.
- Giai đoạn 3: Triển khai mô hình kết hợp vật lý PINN và kiến trúc xLSTM/KAN (Năm 3 - 4): Xây dựng mô hình động học chính xác cao, bền vững với dữ liệu nhiễu và trích xuất phương trình chi phối.
- Giai đoạn 4: Vận hành Bản sao số tự hành hoàn toàn (Năm 4 - 5): Khép kín vòng lặp điều khiển phản hồi trước. Trạm MBR tự động điều chỉnh lưu lượng khí, tự động kích hoạt rửa ngược và định lượng hóa chất tẩy rửa. Mô hình hướng tới mục tiêu tối ưu hóa chi phí vòng đời (LCC) và trung hòa carbon (Net-Zero Carbon).

---

### 7.4 Danh mục Chữ viết tắt và Thuật ngữ Viết tắt (Abbreviations)

Dưới đây là bảng đối soát toàn diện các thuật ngữ viết tắt trong lĩnh vực công nghệ MBR và trí tuệ nhân tạo được sử dụng xuyên suốt công trình:

| Viết tắt | Tên Tiếng Anh Đầy Đủ | Định nghĩa và Ý nghĩa Kỹ thuật trong MBR & AI | Lĩnh vực Phân loại |
| :--- | :--- | :--- | :--- |
| **AIC** | Akaike Information Criterion | Tiêu chuẩn thông tin Akaike để đánh giá và lựa chọn độ phức tạp của mô hình thống kê | Thống kê & ML |
| **ANFIS** | Adaptive Network-based Fuzzy Inference System | Hệ thống suy luận mờ thích ứng dựa trên mạng nơ-ron kết hợp logic mờ | Trí tuệ nhân tạo |
| **AnMBR** | Anaerobic Membrane Bioreactor | Bể phản ứng sinh học màng kỵ khí xử lý nước thải tạo khí sinh học | Công nghệ màng |
| **ANN** | Artificial Neural Networks | Mạng nơ-ron nhân tạo mô phỏng mạng lưới thần kinh sinh học | Học máy |
| **AUC** | Area Under Curve | Diện tích dưới đường cong ROC đánh giá độ phân tách của mô hình phân loại | Đo lường hiệu năng |
| **AutoML** | Automated Machine Learning | Học máy tự động hóa quy trình tiền xử lý, chọn mô hình và tinh chỉnh tham số | Trí tuệ nhân tạo |
| **BA** | Bat Algorithm | Thuật toán bầy dơi mô phỏng định vị bằng tiếng vang để tối ưu hóa siêu tham số | Giải thuật metaheuristic |
| **BFGS** | Broyden-Fletcher-Goldfarb-Shanno | Thuật toán tối ưu hóa quasi-Newton giải bài toán phi tuyến không ràng buộc | Thuật toán tối ưu |
| **BIC** | Bayesian Information Criterion | Tiêu chuẩn thông tin Bayes phạt số lượng tham số để tránh quá khớp | Thống kê & ML |
| **BOD** | Biochemical Oxygen Demand | Nhu cầu oxy sinh hóa đo lượng chất hữu cơ dễ bị vi sinh vật phân hủy | Chất lượng nước |
| **BPNN** | Back Propagation Neural Network | Mạng nơ-ron truyền thẳng lan truyền ngược sai số để cập nhật trọng số | Mạng nơ-ron |
| **CART** | Classification and Regression Tree | Cây phân loại và hồi quy phân chia không gian dữ liệu dạng nhị phân | Cây quyết định |
| **CCI** | Conventional Concentration Indices | Nhóm chỉ số nồng độ thông thường gồm COD, BOD, MLSS, TN, TP | Biến số đầu vào MBR |
| **CFI** | Characteristic Foulant Indices | Nhóm chỉ số đặc trưng chất bẩn gồm kích thước hạt và thế Zeta | Biến số đầu vào MBR |
| **CNN** | Convolutional Neural Network | Mạng nơ-ron tích chập trích xuất đặc trưng không gian đa lớp | Học sâu |
| **COD** | Chemical Oxygen Demand | Nhu cầu oxy hóa học đo tổng lượng oxy cần để oxy hóa chất hữu cơ | Chất lượng nước |
| **CV** | Cross-Validation | Phương pháp kiểm định chéo đánh giá khả năng tổng quát hóa của mô hình | Kiểm định mô hình |
| **DNN** | Deep Neural Network | Mạng nơ-ron sâu với nhiều tầng ẩn trích xuất biểu diễn phi tuyến phức tạp | Học sâu |
| **DO** | Dissolved Oxygen | Nồng độ oxy hòa tan trong bể bùn hoạt tính hiếu khí | Chỉ số môi trường |
| **EC** | Electrical Conductivity | Độ dẫn điện phản ánh tổng lượng ion khoáng hòa tan trong nước | Chỉ số môi trường |
| **EI** | Environment Indices | Nhóm chỉ số môi trường vận hành gồm pH, DO, nhiệt độ và ORP | Biến số đầu vào MBR |
| **ENN** | Elman Neural Network | Mạng nơ-ron hồi quy Elman có lớp ngữ cảnh lưu giữ trạng thái trước đó | Mạng nơ-ron hồi quy |
| **EPS** | Extracellular Polymeric Substances | Các chất polyme ngoại bào do vi sinh vật tiết ra gây nghẽn màng chính | Sinh học bùn MBR |
| **FFA** | Firefly Algorithm | Thuật toán bầy đom đóm tối ưu hóa dựa trên cường độ phát sáng hấp dẫn | Giải thuật metaheuristic |
| **FCN** | Fully Connected Network | Mạng nơ-ron kết nối đầy đủ mọi nơ-ron giữa các tầng kế tiếp | Cấu trúc nơ-ron |
| **GA** | Genetic Algorithms | Giải thuật di truyền mô phỏng chọn lọc tự nhiên để tìm kiếm lời giải toàn cục | Thuật toán tiến hóa |
| **GA-BP** | Genetic Algorithm-Back Propagation | Mô hình lai dùng giải thuật di truyền tối ưu hóa trọng số ban đầu của BPNN | Mô hình lai |
| **GBDT** | Gradient Boosting Decision Tree | Cây quyết định tăng cường độ dốc kết hợp chuỗi cây yếu thành mô hình mạnh | Học kết hợp |
| **GNN** | Graph Neural Network | Mạng nơ-ron đồ thị học biểu diễn trên cấu trúc dữ liệu đồ thị phi Euclid | Học sâu |
| **GWO** | Grey Wolf Optimizer | Thuật toán tối ưu hóa bầy sói xám mô phỏng cơ chế săn mồi phân cấp | Giải thuật metaheuristic |
| **HQC** | Hannan-Quinn Criterion | Tiêu chuẩn thống kê Hannan-Quinn để xác định bậc tự hồi quy tối ưu | Thống kê chuỗi thời gian |
| **HRT** | Hydraulic Retention Time | Thời gian lưu nước thủy lực trong bể phản ứng sinh học | Vận hành MBR |
| **KAN** | Kolmogorov-Arnold Network | Mạng nơ-ron đặt hàm kích hoạt học được B-spline trên cạnh trọng số | Kiến trúc AI mới |
| **KNN** | K-Nearest Neighbors | Thuật toán láng giềng gần nhất dự đoán dựa trên khoảng cách đa chiều | Học máy cổ điển |
| **LM** | Levenberg-Marquardt | Thuật toán tối ưu hóa bình phương tối thiểu phi tuyến tăng tốc độ hội tụ | Thuật toán tối ưu |
| **LSSVM** | Least-Squares Support Vector Machine | Máy vector hỗ trợ bình phương tối thiểu chuyển bài toán QP thành hệ tuyến tính | Máy vector hỗ trợ |
| **LSTM** | Long Short-Term Memory | Mạng nơ-ron bộ nhớ dài-ngắn hạn với các cổng điều khiển chuỗi thời gian | Học sâu chuỗi thời gian |
| **MAPE** | Mean Absolute Percentage Error | Phần trăm sai số tuyệt đối trung bình đánh giá độ chuẩn xác tương đối | Đo lường sai số |
| **MBR** | Membrane Bioreactor | Bể phản ứng sinh học màng tích hợp xử lý sinh học và lọc màng | Công nghệ màng |
| **MFI** | Membrane Filtration Indices | Nhóm chỉ số lọc màng gồm TMP, trở lực thủy lực và thông lượng lọc | Biến số lọc MBR |
| **MLP** | Multilayer Perceptron | Mạng Perceptron đa tầng truyền thẳng kinh điển với hàm kích hoạt cố định | Mạng nơ-ron |
| **MLSS** | Mixed Liquor Suspended Solids | Nồng độ chất rắn lơ lửng trong hỗn hợp bùn lỏng của bể sinh học | Trạng thái bùn MBR |
| **MLVSS** | Volatile Mixed Liquor Suspended Solids | Nồng độ chất rắn lơ lửng bay hơi phản ánh sinh khối vi sinh hoạt tính | Trạng thái bùn MBR |
| **MSE** | Mean Square Error | Sai số bình phương trung bình đo mức độ chênh lệch dự đoán | Đo lường sai số |
| **NH3-N** | Ammonium Nitrogen | Nồng độ nitơ amoni trong nước thải cần được vi sinh vật nitrat hóa | Chất lượng nước |
| **NO3--N** | Nitrate Nitrogen | Nồng độ nitơ nitrat sản phẩm của quá trình nitrat hóa hiếu khí | Chất lượng nước |
| **ODR** | Oxygen Decay Rate | Tốc độ tiêu thụ oxy đo mức độ hoạt tính sinh học của bùn vi sinh | Động học sinh học |
| **OI** | Operation Indices | Nhóm chỉ số vận hành gồm lưu lượng sục khí, chu kỳ rửa màng và HRT | Biến số đầu vào MBR |
| **OLR** | Organic Loading Rate | Tải trọng hữu cơ nạp vào bể sinh học trên một đơn vị thể tích ngày | Vận hành MBR |
| **ORP** | Oxidation Reduction Potential | Thế oxy hóa khử đánh giá trạng thái hiếu khí, thiếu khí hoặc kỵ khí | Chỉ số môi trường |
| **PCA** | Principal Component Analysis | Phân tích thành phần chính giảm chiều dữ liệu giữ phương sai cực đại | Xử lý đặc trưng |
| **PSO** | Particle Swarm Optimization | Thuật toán tối ưu hóa bầy đàn mô phỏng hành vi di chuyển bầy chim cá | Giải thuật metaheuristic |
| **RBF** | Radial Basis Function | Hàm cơ sở xuyên tâm đo khoảng cách Euclidean làm hàm nhân phi tuyến | Hàm nhân toán học |
| **RBFNN** | Radial Basis Function Neural Network | Mạng nơ-ron sử dụng hàm cơ sở xuyên tâm ở tầng ẩn xấp xỉ cục bộ | Mạng nơ-ron |
| **RF** | Random Forest | Rừng ngẫu nhiên thuật toán học kết hợp bagging trên nhiều cây quyết định | Cây quyết định |
| **RH** | Relative Hydrophobicity | Độ kỵ nước tương đối của bùn hoạt tính ảnh hưởng kết tụ bám màng | Hóa lý bề mặt |
| **RL** | Reinforcement Learning | Học tăng cường tác nhân học chính sách tối ưu tương tác môi trường qua phần thưởng | Học máy |
| **RMSE** | Root Mean Square Error | Căn bậc hai sai số bình phương trung bình cùng đơn vị với biến mục tiêu | Đo lường sai số |
| **RNN** | Recurrent Neural Network | Mạng nơ-ron hồi quy có liên kết phản hồi xử lý dữ liệu chuỗi tuần tự | Học sâu chuỗi thời gian |
| **ROC** | Receiver Operating Characteristic | Đường cong đặc trưng hoạt động máy thu đối sánh độ nhạy và độ đặc hiệu | Đo lường hiệu năng |
| **SA** | Simulated Annealing | Thuật toán tôi kim loại mô phỏng nhiệt động học tinh thể để thoát cực tiểu cục bộ | Giải thuật metaheuristic |
| **SHAP** | Shapley Additive Explanations | Phương pháp giải thích đóng góp của biến dựa trên lý thuyết trò chơi hợp tác | AI có thể giải thích |
| **SMP** | Soluble Microbial Products | Các sản phẩm vi sinh hòa tan gồm protein và đường tự do gây nghẽn lỗ màng | Hóa sinh MBR |
| **SRT** | Sludge Retention Time | Thời gian lưu bùn (tuổi bùn) quyết định nồng độ sinh khối vi sinh | Vận hành MBR |
| **SVC** | Support Vector Classification | Máy vector hỗ trợ chuyên biệt cho các bài toán phân loại nhị phân và đa lớp | Học máy cổ điển |
| **SVM** | Support Vector Machines | Máy vector hỗ trợ tối ưu hóa khoảng cách siêu phẳng phân tách dữ liệu | Học máy cổ điển |
| **SVR** | Support Vector Regression | Hồi quy vector hỗ trợ tối ưu biên dung sai epsilon cho biến liên tục | Học máy cổ điển |
| **t** | Time Parameter | Tham số thời gian vận hành liên tục hoặc thời gian chu kỳ lọc | Biến số vận hành |
| **T** | Temperature | Nhiệt độ nước thải ảnh hưởng trực tiếp độ nhớt và hoạt tính vi sinh | Chỉ số môi trường |
| **TMP** | Transmembrane Pressure | Áp suất xuyên màng động lực lọc và chỉ số cảnh báo tắc nghẽn màng | Vận hành màng cốt lõi |
| **TN** | Total Nitrogen | Tổng nitơ bao gồm nitơ hữu cơ, amoni, nitrit và nitrat trong nước | Chất lượng nước |
| **TOC** | Total Organic Carbon | Tổng cacbon hữu cơ đo tổng lượng cacbon liên kết trong hợp chất hữu cơ | Chất lượng nước |
| **TP** | Total Phosphorus | Tổng phốt pho bao gồm phốt phát hòa tan và phốt pho hữu cơ | Chất lượng nước |
| **TSS** | Total Suspended Solids | Tổng chất rắn lơ lửng trong mẫu nước thải | Chất lượng nước |
| **WNN** | Wavelet Neural Network | Mạng nơ-ron kết hợp biến đổi sóng con trích xuất đặc trưng đa tần số | Mạng nơ-ron |
| **XAI** | Explainable Artificial Intelligence | Trí tuệ nhân tạo có thể giải thích nhằm mở hộp đen và minh bạch hóa mô hình | Hướng đi AI hiện đại |
