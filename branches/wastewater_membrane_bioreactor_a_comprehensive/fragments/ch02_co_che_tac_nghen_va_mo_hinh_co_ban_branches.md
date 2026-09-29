## Chương 3 (Phần 1): Cơ chế Tắc nghẽn Màng (3.1) và Các Mô hình Học máy Cơ bản / Dựa trên Hạt nhân (3.2)

### 3.1 Cơ chế Tắc nghẽn Màng và Bối cảnh Mô hình hóa Cơ chế

#### 3.1.1 Phân loại Tắc nghẽn Màng và Động học Tăng Áp suất Qua Màng (TMP)
- Bản chất vật lý của tắc nghẽn màng trong MBR:
  - Hiện tượng tích tụ chất rắn, polyme sinh học và hạt keo lên bề mặt màng hoặc bên trong lỗ rỗng mao quản.
  - Quá trình này làm suy giảm lưu lượng thấm nước và làm tăng áp suất qua màng (Transmembrane Pressure - TMP).
  - Tắc nghẽn màng diễn ra trên nhiều quy mô không gian và thời gian.
- Phân loại ba hình thái tắc nghẽn theo khả năng phục hồi kỹ thuật:
  - Tắc nghẽn có thể đảo ngược (Reversible fouling):
    - Tích tụ lớp bánh cặn (cake layer) lỏng lẻo bám trên bề mặt ngoài của màng lọc.
    - Người vận hành loại bỏ dễ dàng bằng các biện pháp vật lý thông thường.
    - Biện pháp xử lý gồm chu kỳ tạm dừng hút (relaxation) và sục rửa ngược định kỳ (backwashing).
  - Tắc nghẽn không thể đảo ngược (Irreversible fouling):
    - Chất bẩn bít tắc sâu vào lòng lỗ rỗng mao quản màng (pore blocking).
    - Polyme sinh học hấp phụ mạnh lên thành lỗ xốp của màng mỏng.
    - Rửa cơ học thông thường không thể loại bỏ trở lực này.
    - Trạm bắt buộc phải ngâm rửa bằng hóa chất chuyên dụng tại chỗ (Clean-In-Place - CIP) bằng dung dịch axit, kiềm hoặc chất oxy hóa.
  - Tắc nghẽn vĩnh viễn (Irrecoverable fouling):
    - Hiện tượng suy giảm tính thấm tích lũy sau nhiều năm vận hành liên tục.
    - Ngay cả quy trình rửa hóa chất nồng độ cao cũng không thể phục hồi độ thấm.
    - Nguyên nhân cốt lõi do lão hóa vật liệu polyme màng hoặc khoáng hóa không hòa tan ăn sâu vào cấu trúc màng.
    - Trạm phải loại bỏ và thay thế mô-đun màng mới.
- Động học tăng TMP hai giai đoạn (Two-stage TMP rise kinetics):
  - Ngưỡng lưu lượng thấm tới hạn (Critical Flux - $J_c$):
    - Khi lưu lượng vận hành thấp hơn $J_c$ ($J < J_c$), cặn tích tụ chậm và phần lớn có thể đảo ngược. Lực cắt bọt khí lấn át lực kéo đối lưu.
    - Khi lưu lượng vận hành vượt quá $J_c$ ($J > J_c$), tắc nghẽn không thể đảo ngược bùng phát dữ dội. Hiện tượng này rút ngắn chu kỳ làm sạch và tuổi thọ màng.
  - Giai đoạn 1 (Tăng TMP chậm và ổn định):
    - Diễn ra trong thời gian dài từ vài chục đến hàng trăm giờ lọc liên tục.
    - Polyme sinh học hòa tan và hạt keo hấp phụ từ từ vào vách lỗ màng.
    - Lớp bánh cặn mỏng ban đầu hình thành trên bề mặt.
    - Tốc độ tăng áp suất duy trì ở mức rất thấp: $\frac{d(TMP)}{dt} \approx \text{const} \ll 1\text{ kPa/h}$.
  - Giai đoạn 2 (Tăng vọt đột biến áp suất - TMP jump):
    - Khi các lỗ rỗng mao quản bị bít kín cục bộ, lưu lượng thấm cục bộ tại các vị trí màng còn lại tăng vượt ngưỡng tới hạn $J_c$.
    - Lớp bánh cặn bị nén ép cơ học dữ dội dưới gradient áp suất cao.
    - Độ rỗng của lớp bánh cặn giảm mạnh, đẩy trở lực thủy lực tăng phi tuyến.
    - Đồ thị TMP tăng vọt theo phương thẳng đứng. Áp suất nhanh chóng chạm ngưỡng bảo vệ quá áp của bơm hút, buộc trạm phải dừng lọc.

#### 3.1.2 Các Tác nhân Hóa sinh và Thông số Vận hành Chi phối
- Các tác nhân hóa sinh gây tắc nghẽn cốt lõi:
  - Chất polyme ngoại bào (Extracellular Polymeric Substances - EPS):
    - Hợp chất hữu cơ do vi sinh vật bùn hoạt tính tiết ra trong quá trình sinh trưởng và trao đổi chất.
    - EPS liên kết (Bound EPS): Bao bọc quanh thành tế bào vi khuẩn. Gồm lớp liên kết lỏng lẻo (LB-EPS) và lớp liên kết chặt chẽ (TB-EPS). Nồng độ LB-EPS tương quan thuận trực tiếp với trở lực bánh cặn và tốc độ tăng TMP.
    - Thành phần hóa sinh chính: Protein (tạo liên kết kỵ nước) và Polysaccharide / Carbohydrate (tạo mạng gel ưa nước kết dính).
  - Sản phẩm vi sinh vật hòa tan (Soluble Microbial Products - SMP):
    - Các đại phân tử hữu cơ hòa tan giải phóng khi vi khuẩn chuyển hóa cơ chất hoặc tự phân hủy nội sinh.
    - Kích thước hạt rất nhỏ (< 0.45 $\mu$m). SMP dễ thâm nhập sâu vào mạng mao quản màng, trực tiếp gây bít tắc lỗ rỗng không thể đảo ngược.
  - Polyme sinh học dạng keo (Colloidal biopolymers):
    - Cầu nối liên kết giữa pha hòa tan và pha lơ lửng, tạo cấu trúc cặn nhớt khó phân tách.
- Năm thông số vận hành then chốt chi phối động học tắc nghẽn:
  - Nồng độ chất rắn lơ lửng trong bùn lỏng (Mixed Liquor Suspended Solids - MLSS):
    - Quyết định khối lượng sinh khối sẵn có tạo thành lớp bánh cặn.
    - Nồng độ MLSS cao làm tăng độ nhớt biểu kiến của bùn lỏng, làm suy giảm hiệu quả cọ rửa bề mặt màng của bọt khí.
  - Thời gian lưu bùn (Sludge Retention Time - SRT):
    - Kiểm soát tốc độ sinh trưởng của sinh khối và trạng thái trao đổi chất tế bào.
    - SRT ngắn (< 10 ngày) thúc đẩy vi khuẩn tiết nhiều LB-EPS và SMP nhớt, làm trầm trọng hóa tắc nghẽn màng.
    - SRT tối ưu (15–30 ngày) giúp tạo bông bùn ổn định, giảm lượng polyme tự do.
    - SRT quá dài (> 50 ngày) tích lũy nhiều mảnh vụn trơ và khoáng chất, làm tăng độ nhớt bùn.
  - Thời gian lưu thủy lực (Hydraulic Retention Time - HRT):
    - Quy định tốc độ pha loãng và thời gian lưu giữ chất ô nhiễm keo trong bể phản ứng.
    - HRT ngắn làm tăng tải trọng hữu cơ thể tích, giảm thời gian tiếp xúc xử lý sinh học.
  - Nồng độ oxy hòa tan (Dissolved Oxygen - DO):
    - Chi phối sự cân bằng giữa quá trình chuyển hóa hiếu khí và thiếu khí / kỵ khí.
    - Nồng độ DO quá thấp (< 1.5 mg/L) kích thích vi khuẩn tiết nhiều chất nhầy bảo vệ, phá vỡ cấu trúc bông bùn.
  - Cường độ sục khí màng (Membrane Aeration Intensity):
    - Dòng bọt khí thô liên tục tạo ứng suất cắt thủy lực (shear stress) trên bề mặt màng.
    - Ứng suất cắt cuốn trôi các phần tử bùn bám dính, ức chế lớp bánh cặn phát triển dày thêm.
- Xung đột vận hành đa mục tiêu (Multi-Objective Trade-offs):
  - Tăng MLSS giúp tăng hiệu quả phân hủy sinh học nhưng lại đẩy nhanh tốc độ tắc nghẽn màng.
  - Tăng cường độ sục khí màng giúp kiểm soát lớp cặn bám nhưng tiêu thụ 60–75% tổng điện năng toàn trạm.
  - Mối quan hệ giữa các biến số mang tính phi tuyến cao và xung đột lẫn nhau. Mô hình giải tích đơn giản không thể mô tả trọn vẹn hiện tượng này.
- Cơ sở chọn lọc đặc trưng cho Học máy (Feature Engineering):
  - Nhóm thông số {MLSS, SRT, HRT, DO, Cường độ sục khí} tạo thành tập đặc trưng đầu vào nền tảng.
  - Việc chọn các biến này xuất phát từ bản chất cơ chế hóa sinh học thay vì lựa chọn ngẫu nhiên theo trực giác thực nghiệm.

#### 3.1.3 Mô hình Dãy Trở lực Thủy lực và Mô hình Bùn Hoạt tính (ASM)
- Mô hình dãy trở lực cơ học (Resistance-in-Series Model):
  - Biểu thức mở rộng của định luật Darcy:
    $$J = \frac{\Delta P}{\mu R_t} = \frac{\Delta P}{\mu (R_m + R_c + R_p)}$$
  - Giải thích các biến số và tham số:
    - $J$: Lưu lượng thấm qua màng (Permeate flux, đơn vị: $\text{m}^3/(\text{m}^2\cdot\text{s})$ hoặc $\text{L}/(\text{m}^2\cdot\text{h})$ - LMH).
    - $\Delta P$: Áp suất qua màng (TMP, đơn vị: $\text{Pa}$ hoặc $\text{kPa}$).
    - $\mu$: Độ nhớt động học của dòng nước thấm (Permeate viscosity, phụ thuộc trực tiếp vào nhiệt độ $T$, đơn vị: $\text{Pa}\cdot\text{s}$).
    - $R_t$: Tổng trở lực thủy lực của hệ thống (Total filtration resistance, đơn vị: $\text{m}^{-1}$).
    - $R_m$: Trở lực nội tại của màng sạch (Intrinsic membrane resistance).
    - $R_c$: Trở lực của lớp bánh cặn đảo ngược được (Reversible cake layer resistance).
    - $R_p$: Trở lực bít tắc mao quản và hấp phụ không đảo ngược (Irreversible pore blocking resistance).
- Giới hạn của mô hình dãy trở lực thuần túy:
  - Giả định tĩnh: Coi các đại lượng trở lực là hằng số hoặc tăng tuyến tính theo thời gian.
  - Bỏ qua hiện tượng nén ép phi tuyến của bánh cặn khi áp suất tăng cao.
  - Bỏ qua tính chất lưu biến phi Newton của bùn hoạt tính nồng độ cao.
  - Không thể tự thích ứng khi đặc tính nước thải đầu vào biến động bất thường.
- Mô hình bùn hoạt tính (Activated Sludge Models - ASM):
  - Họ mô hình chuẩn do IWA ban hành: ASM1 (chuyển hóa COD và nitơ), ASM2d (chuyển hóa nitơ và phốt pho sinh học), ASM3 (mô hình hóa tích lũy nội bào).
  - Khung chuẩn mô phỏng BSM-MBR: Ghép nối động học phân hủy sinh học với quá trình phân tách pha bằng màng.
- Rào cản mô hình hóa cơ chế trong vận hành thực tế:
  - Đo đạc trực tuyến các phân đoạn EPS và SMP theo thời gian thực tại hiện trường rất khó khăn và tốn kém.
  - Các tham số động học sinh học rất nhạy cảm với nhiệt độ nước và lịch sử thích nghi của bùn vi sinh.
  - Chi phí giải thuật số mô phỏng toàn phần rất cao, không đáp ứng yêu cầu tính toán tức thời trên hệ thống điều khiển thực tế.
  - Cấu hình MBR thẩm thấu (Osmotic MBR - OMBR): Ghép nối màng thẩm thấu thuận (Forward Osmosis - FO) sinh ra hiện tượng phân cực nồng độ nội (ICP) và ngoại (ECP), làm phương trình giải tích vượt quá khả năng giải số đơn giản.

#### 3.1.4 Cấu trúc Vật lý Trạm MBR và Luồng Dữ liệu Cảm biến SCADA
- Sơ đồ nguyên lý vật lý hệ thống MBR (tham chiếu Hình 2 của bài báo):
  - Cụm bể phản ứng sinh học hiếu khí (Aerated bioreactor): Chứa hỗn hợp bùn lỏng hoạt tính thực hiện quá trình oxy hóa sinh hóa.
  - Cụm mô-đun màng siêu lọc đặt chìm (Submerged UF membrane modules): Thiết kế dạng sợi rỗng (Hollow-fiber) hoặc tấm phẳng (Flat-sheet), làm việc dưới áp suất hút chân không âm.
  - Bơm hút nước thấm (Permeate extraction pump) và đường ống xả nước sau xử lý (Effluent outlet).
  - Tuyến tuần hoàn bùn (Sludge recycle line): Ổn định nồng độ MLSS đồng đều giữa các ngăn bể.
  - Tuyến xả bùn dư (Waste Activated Sludge - WAS): Kiểm soát chính xác giá trị thời gian lưu bùn SRT.
  - Hệ thống sục khí màng bọt thô (Coarse-bubble aeration): Bố trí phía dưới mô-đun màng để tạo lực cắt thủy lực cọ rửa liên tục.
  - Cụm đường ống rửa ngược (Backwash) và chu trình châm hóa chất làm sạch tại chỗ (CIP).
- Hệ thống thiết bị đo đạc cảm biến trực tuyến (Online sensors):
  - Cảm biến oxy hòa tan (DO probes) đo liên tục nồng độ DO trong bể sinh học.
  - Đầu dò áp suất qua màng (TMP transducers) gắn trực tiếp trên đường ống hút nước thấm.
  - Lưu lượng kế nước thải đầu vào (Influent flow meter) và lưu lượng kế nước thấm (Permeate flow meter).
  - Đầu đo độ đục trực tuyến (Online turbidity meter) phát hiện tức thời rủi ro rách màng hoặc bùn rò rỉ.
  - Đầu đo nhiệt độ bùn lỏng (Temperature sensors) bù sai số độ nhớt thủy lực.
- Luồng dữ liệu ba tầng từ thiết bị hiện trường đến trí tuệ nhân tạo:
  - Tầng 1 (Tầng vật lý hiện trường): Cảm biến đo đạc và truyền tín hiệu dòng điện / điện áp với chu kỳ từ 1 giây đến vài phút.
  - Tầng 2 (Tầng giám sát SCADA): Hệ thống SCADA tiếp nhận, tiền xử lý, gán nhãn thời gian và lưu trữ chuỗi thời gian vào cơ sở dữ liệu lịch sử.
  - Tầng 3 (Tầng phân tích AI & Bản sao số): Mô hình học máy đọc dữ liệu SCADA để dự báo sớm giá trị TMP và đưa ra chỉ dẫn điều khiển tối ưu.

---

### 3.2 Các Mô hình Học máy Cơ bản và Dựa trên Hạt nhân

#### 3.2.1 Mạng Nơ-ron Nhân tạo Nông (ANN, MLP, RBF)
- Cấu trúc và nguyên lý toán học của mạng nơ-ron nông:
  - Mạng Perceptron đa tầng (Multilayer Perceptron - MLP): Gồm một lớp đầu vào, một đến hai lớp ẩn nông và một lớp đầu ra.
  - Tín hiệu lan truyền qua các trọng số kết nối và hàm kích hoạt phi tuyến (Sigmoid, Tanh, ReLU).
  - Thuật toán lan truyền ngược (Backpropagation): Sử dụng phương pháp hạ gradient (Gradient Descent) để cập nhật ma trận trọng số nhằm giảm thiểu hàm mất mát sai số bình phương trung bình (MSE).
- Thực nghiệm điển hình của Mirbagheri và cộng sự (2015):
  - Hệ pilot MBR chìm vận hành liên tục trong 60 ngày.
  - Mục tiêu dự báo: Áp suất TMP và độ thấm màng (Permeability).
  - Tập biến đầu vào gồm 5 thông số: Thời gian vận hành ($t$), TSS, COD, SRT và MLSS.
  - So sánh đối đầu giữa hai kiến trúc mạng nơ-ron:
    - Mạng MLP truyền thống.
    - Mạng hàm cơ sở xuyên tâm (Radial Basis Function - RBF).
  - Kết quả so sánh: Cả hai mô hình đều đạt độ chính xác khả quan. Mạng RBF vượt trội hơn nhờ tốc độ hội tụ nhanh và ít nhạy cảm với việc khởi tạo trọng số ngẫu nhiên ban đầu. Đây là ưu thế lớn khi triển khai trực tuyến.
  - Kết luận nghiên cứu: Việc lựa chọn đúng biến đầu vào và đảm bảo tính đa dạng của dữ liệu quyết định năng lực tổng quát hóa của mạng.
- Thực nghiệm của Schmitt và cộng sự (2018):
  - Xây dựng mạng ANN lan truyền ngược dự báo tắc nghẽn màng cho hệ MBR thiếu khí - hiếu khí xử lý nước thải sinh hoạt.
  - Hiệu năng định lượng: Mô hình đạt hệ số xác định $R^2 = 0.850$ trên tập dữ liệu kiểm tra độc lập (held-out test data).
  - Ý nghĩa kết quả: Phản ánh biến động mạnh của nước thải thực tế và rào cản khi mô phỏng động học tắc nghẽn bằng số lượng biến đầu vào hạn chế.
- Hạn chế cố hữu của kiến trúc mạng nơ-ron nhân tạo nông:
  - Bề mặt hàm mất mát phi lồi khiến thuật toán dễ rơi vào các cực tiểu cục bộ (local minima).
  - Tốc độ huấn luyện chậm khi gặp dữ liệu nhiễu cao.
  - Quy trình dò tìm siêu tham số (số nơ-ron lớp ẩn, tốc độ học, hệ số quán tính) phụ thuộc hoàn toàn vào kỹ thuật thử-sai.
  - Xuất hiện nguy cơ quá khớp (overfitting) nghiêm trọng khi tập dữ liệu thực nghiệm có kích thước mẫu nhỏ.

#### 3.2.2 Máy Véc-tơ Hỗ trợ (SVM / SVR) và Biến thể Bình phương Tối thiểu (LSSVM)
- Hồi quy Véc-tơ Hỗ trợ (Support Vector Regression - SVR):
  - Áp dụng nguyên lý Tối thiểu hóa Rủi ro Cấu trúc (Structural Risk Minimization - SRM): Giới hạn biên trên của sai số khái quát hóa thay vì chỉ tối thiểu hóa sai số kinh nghiệm trên tập huấn luyện như ANN.
  - Kỹ thuật hạt nhân (Kernel Trick): Ánh xạ phi tuyến các véc-tơ dữ liệu từ không gian đầu vào sang không gian đặc trưng Hilbert vô hạn chiều. Mô hình xây dựng siêu phẳng hồi quy tuyến tính tối ưu trong không gian mới.
  - Hàm nhân cơ sở xuyên tâm Gauss (Gaussian RBF Kernel):
    $$K(x, x') = \exp\left(-\gamma \|x - x'\|^2\right)$$
    Trong đó: $\gamma = \frac{1}{2\sigma^2}$ đại diện cho tham số độ rộng vùng lân cận của hạt nhân; $\|x - x'\|^2$ là bình phương khoảng cách Euclid giữa hai véc-tơ dữ liệu đầu vào $x$ và $x'$.
  - Ưu thế tối ưu hóa: Bài toán quy hoạch bậc hai lồi (Convex Quadratic Programming - QP) đảm bảo nghiệm tìm được luôn là cực trị toàn cục duy nhất.
- Máy Véc-tơ Hỗ trợ Bình phương Tối thiểu (Least Squares Support Vector Machine - LSSVM):
  - Biến đổi công thức của Suykens và Vandewalle:
    - Thay thế hàm mất mát $\varepsilon$-insensitive trong SVM tiêu chuẩn bằng hàm mất mát sai số bình phương.
    - Chuyển đổi toàn bộ các ràng buộc bất đẳng thức phức tạp thành hệ ràng buộc đẳng thức tuyến tính.
  - Giải thuật toán học tương đương:
    - Điều kiện tối ưu Karush-Kuhn-Tucker (KKT) chuyển bài toán quy hoạch bậc hai thành việc giải một hệ phương trình đại số tuyến tính:
      $$\begin{bmatrix} 0 & \mathbf{1}_N^T \\ \mathbf{1}_N & \mathbf{\Omega} + \gamma^{-1} \mathbf{I}_N \end{bmatrix} \begin{bmatrix} b \\ \boldsymbol{\alpha} \end{bmatrix} = \begin{bmatrix} 0 \\ \mathbf{y} \end{bmatrix}$$
      Trong đó: $\mathbf{\Omega}_{i,j} = K(x_i, x_j)$ là phần tử ma trận hạt nhân, $\boldsymbol{\alpha} = [\alpha_1, \dots, \alpha_N]^T$ là véc-tơ nhân tử Lagrange, $b$ là hệ số chệch, và $\gamma$ là tham số điều chuẩn.
  - Tốc độ huấn luyện: Giảm mạnh thời gian tính toán và độ phức tạp phần mềm so với việc giải quy hoạch bậc hai trong SVR tiêu chuẩn.

#### 3.2.3 Đánh giá Thực nghiệm Đối sánh và Khoảng trống Dự báo Tuổi thọ Màng
- Nghiên cứu đối sánh của Hamedi và cộng sự (2019):
  - Bối cảnh thử nghiệm: Dự báo trở lực lọc màng tổng cộng ($R_t$) trên hệ MBR phòng thí nghiệm.
  - So sánh trực tiếp 4 thuật toán: Mạng MLP tiêu chuẩn (ANN-MLP), Mạng nơ-ron tối ưu hóa bầy đàn hạt (ANN-PSO), Lập trình biểu thức gen (Gene Expression Programming - GEP), và LSSVM.
  - Kết quả định lượng vượt trội:
    - Mô hình LSSVM đạt hiệu năng dẫn đầu tuyệt đối: $R^2 = 0.990$ và $\text{MSE} = 0.0002$.
    - LSSVM vượt trội hoàn toàn so với toàn bộ các biến thể mạng nơ-ron nhân tạo.
  - Phân tích độ nhạy (Sensitivity Analysis):
    - Xác định hai biến số chi phối mạnh nhất là Lưu lượng thấm ($J$) và Áp suất qua màng (TMP).
    - Kết quả xếp hạng biến số của mô hình học máy trùng khớp hoàn hảo với lý thuyết vật lý của mô hình dãy trở lực.
- Nghiên cứu MBR nước thải công nghiệp của Giwa và cộng sự (2020):
  - Ứng dụng ANN cho hệ MBR chìm xử lý nước thải công nghiệp kết hợp sinh hoạt tại Các Tiểu Vương quốc Ả Rập Thống nhất (UAE).
  - Đầu vào gồm đặc tính nước thải thô: Độ dẫn điện, pH, tổng chất rắn lơ lửng.
  - Đầu ra dự báo: Các thông số chất lượng nước sạch (COD, BOD, độ đục).
  - Phát hiện quan trọng: Hiệu năng của mạng ANN phụ thuộc chặt chẽ vào độ phong phú của dữ liệu khi nước thải biến động tải trọng lớn.
- Thử nghiệm của Nguyen và cộng sự (2021) và bài học về nguy cơ quá khớp:
  - So sánh Hồi quy Cây quyết định (Decision Tree Regression), SVR và Hồi quy tuyến tính để dự báo TMP nước thải sinh hoạt.
  - Cây quyết định ghi nhận chỉ số danh nghĩa $R^2 = 0.99$.
  - Khuyến cáo phản biện: Kết quả $R^2$ cao bất thường này do cây quyết định ghi nhớ cấu trúc nhiễu trên tập dữ liệu nhỏ từ một trạm duy nhất. Mô hình này không có khả năng tổng quát hóa thực tế.
- Khảo sát hệ thống của Queiroz và cộng sự (2022) và khoảng trống công nghệ:
  - Phân tích thống kê 57 công trình nghiên cứu ứng dụng ML dự báo vận hành MBR.
  - Tỷ lệ áp dụng mạng ANN chiếm tới 88% tổng số công trình.
  - Khoảng trống then chốt được phát hiện: Chưa có bất kỳ nghiên cứu nào sử dụng học máy để dự báo tuổi thọ màng (membrane lifespan) hoặc dự báo thời điểm cần thay thế cụm màng. Khoảng trống này gây thiệt hại kinh tế lớn cho các đơn vị vận hành thương mại.
- Tổng quan của Schmitt & Do (2023) và Shi và cộng sự (2021):
  - Schmitt & Do: Khảo sát hơn 30 công trình mô hình hóa tắc nghẽn MBR. Hai tác giả xác định tính khan hiếm và tính đại diện của dữ liệu là rào cản lớn nhất. Nghiên cứu khuyến nghị phải đo đạc liên tục dài hạn.
  - Shi và cộng sự: Đánh giá rộng rãi ứng dụng ML trong các hệ thống màng lọc. Kết luận khẳng định các mô hình lai (Hybrid ML-mechanistic models - dùng công thức cơ chế để tính toán các biến đặc trưng đầu vào trước khi đưa vào ML) luôn vượt trội hơn mô hình hộp đen thuần túy, đặc biệt khi ngoại suy ngoài tập dữ liệu huấn luyện.

#### 3.2.4 Giới hạn Tính toán và Thách thức Mở rộng Quy mô Dữ liệu SCADA Lớn
- Bản chất bài toán đại số tuyến tính của mô hình hạt nhân:
  - Thuật toán LSSVM yêu cầu xây dựng và thao tác trực tiếp trên ma trận Gram (ma trận hạt nhân $\mathbf{\Omega}$) có kích thước $N \times N$, với $N$ là tổng số điểm dữ liệu huấn luyện.
  - Quá trình huấn luyện đòi hỏi thực hiện phép nghịch đảo ma trận hoặc phân rã Cholesky:
    $$\left(\mathbf{\Omega} + \gamma^{-1}\mathbf{I}_N\right)^{-1}$$
- Đánh giá độ phức tạp tính toán và bộ nhớ:
  - Độ phức tạp thời gian huấn luyện: $\mathcal{O}(N^3)$ phép toán số học.
  - Độ phức tạp không gian lưu trữ bộ nhớ: $\mathcal{O}(N^2)$ dung lượng RAM.
- Rào cản mở rộng trên chuỗi thời gian SCADA công nghiệp:
  - Trạm MBR hiện đại vận hành mạng cảm biến đa biến với chu kỳ lấy mẫu dày đặc từ 1 giây đến 1 phút.
  - Sau vài tháng vận hành, hệ thống ghi nhận hàng trăm nghìn đến hàng triệu bản ghi ($N > 10^5 - 10^6$).
  - Với $N = 100{,}000$, ma trận hạt nhân chiếm khoảng 80 GB bộ nhớ RAM và tiêu tốn hàng triệu tỷ phép tính dấu phẩy động. Các máy tính công nghiệp tại trạm xử lý không thể đáp ứng tải tính toán này.
  - Tính không thưa (Non-sparsity): Trong LSSVM, hầu như mọi nhân tử Lagrange $\alpha_i$ đều khác 0. Khi dự báo một điểm dữ liệu mới, mô hình phải tính toán tổng của toàn bộ $N$ hàm nhân, gây trễ nghiêm trọng cho tác vụ điều khiển thời gian thực.
- Nhu cầu cấp thiết chuyển đổi kiến trúc:
  - Giới hạn tính toán bậc ba $\mathcal{O}(N^3)$ tạo điểm nghẽn ngăn cản các mô hình hạt nhân mở rộng quy mô.
  - Xu hướng nghiên cứu bắt buộc phải dịch chuyển sang các mô hình tập hợp cây (Ensemble Methods: Random Forest, XGBoost) và các mô hình học sâu chuỗi thời gian (Deep Learning: LSTM, GRU) được phân tích chi tiết ở các phần tiếp theo.
