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
