### 1. Giới thiệu và Bối cảnh nghiên cứu (Introduction & Background)

#### 1.1 Tái sử dụng nước xám và công nghệ MBR phân tán

##### 1.1.1 Tiềm năng và đặc tính nước xám sinh hoạt
- Định nghĩa nước xám (Greywater): Dòng nước thải sinh hoạt không chứa nguồn thải đen từ bồn cầu (toilet contributions). Dòng nước này bắt nguồn từ vòi tắm, vòi sen, máy giặt và bồn rửa tay.
- Tỷ trọng phát sinh: Nước xám chiếm khoảng $70\%$ tổng lượng nước thải sinh hoạt hộ gia đình (Shaikh và Ahammed, 2020).
- Dải lưu lượng phát sinh: Lượng phát sinh dao động từ $20$ đến $220\text{ L/người/ngày}$ phụ thuộc vào hành vi tiêu dùng và mức độ tiện nghi.
- Lợi ích của tái sử dụng tại nguồn (On-site reuse):
  - Bảo tồn tài nguyên nước sạch đô thị.
  - Tăng cường tính chống chịu và độ phục hồi của hệ thống cấp nước đô thị trước hạn hán (Liu và cộng sự, 2023; Maggiotto, 2022).
  - Giảm tải áp lực dòng chảy và thể tích xả thải lên mạng lưới thoát nước tập trung.
- Đặc tính dao động tải nạp trong hệ phân tán:
  - Tải nạp biến thiên mạnh theo chu kỳ sinh hoạt ngày đêm và theo các mùa trong năm.
  - Chu kỳ xả nước thấp kéo dài xen kẽ những đỉnh xả đột biến trong các khung giờ cao điểm.
  - Nồng độ chất hữu cơ và chất hoạt động bề mặt biến động lớn, gây khó khăn cho các phương án kiểm soát vận hành theo kinh nghiệm (DelaPaz-Ruíz và cộng sự, 2024; Hassan và cộng sự, 2024).

##### 1.1.2 Vai trò và cấu tạo của hệ MBR hiếu khí
- Vị trí công nghệ: Bể phản ứng sinh học màng (Membrane Bioreactor - MBR) là giải pháp công nghệ hàng đầu cho xử lý nước xám phân tán tại chỗ (Gao và cộng sự, 2025).
- Cơ chế vận hành tích hợp: MBR kết hợp quá trình bùn hoạt tính hiếu khí với quá trình phân tách pha rắn - lỏng qua màng lọc (Boleydei và Vaneeckhaute, 2024).
- Phản ứng sinh học trong bể hiếu khí:
  - Quá trình oxy hóa dị dưỡng (Heterotrophic oxidation) để loại bỏ nhu cầu oxy hóa học (COD).
  - Quá trình chuyển hóa nitơ tự dưỡng (Autotrophic nitrification) để oxy hóa amoni.
- Tách pha chất rắn qua màng lọc:
  - Màng vi lọc hoặc siêu lọc (như màng gốm phẳng SiC) giữ lại toàn bộ sinh khối bùn vi sinh trong bể phản ứng.
  - Hệ thống loại bỏ hoàn toàn nhu cầu xây dựng bể lắng thứ cấp truyền thống.
- Các ưu thế kỹ thuật nổi bật:
  - Dấu chân diện tích (footprint) nhỏ gọn, tối ưu không gian cho các công trình phân tán.
  - Chất lượng nước sau lọc ổn định và đạt tiêu chuẩn khắt khe cho mục đích tái sử dụng như dội bồn cầu hoặc tưới cây.

#### 1.2 Thách thức trong giám sát và kiểm soát quá trình Nitrification

##### 1.2.1 Cơ chế phản ứng Nitrification
- Định nghĩa: Nitrification là quá trình sinh học oxy hóa các hợp chất nitơ khử thành ion nitrat bền vững. Quá trình này giúp nước sau xử lý đạt chuẩn an toàn tái sử dụng.
- Cơ chế phản ứng sinh hóa hai giai đoạn nối tiếp:
  - Giai đoạn 1 (Nitrit hóa - Nitritation): Vi khuẩn oxy hóa amoni (Ammonia-Oxidizing Bacteria - AOB) chuyển hóa $NH_4^+-N$ thành $NO_2^--N$:
    $$2NH_4^+ + 3O_2 \xrightarrow{AOB} 2NO_2^- + 4H^+ + 2H_2O$$
  - Giai đoạn 2 (Nitrat hóa - Nitratation): Vi khuẩn oxy hóa nitrit (Nitrite-Oxidizing Bacteria - NOB) chuyển hóa $NO_2^--N$ thành $NO_3^--N$:
    $$2NO_2^- + O_2 \xrightarrow{NOB} 2NO_3^-$$
  - Phương trình chuyển hóa tổng quát:
    $$NH_4^+ + 2O_2 \xrightarrow{} NO_3^- + 2H^+ + H_2O$$
- Nhu cầu tiêu thụ oxy hòa tan và độ kiềm:
  - Quá trình oxy hóa hoàn toàn $1\text{ g } NH_4^+-N$ đòi hỏi lý thuyết $4.57\text{ g } O_2$.
  - Phản ứng giải phóng ion $H^+$, làm tiêu hao khoảng $7.14\text{ g } CaCO_3$ độ kiềm trên mỗi gam $NH_4^+-N$ bị chuyển hóa.
- Độ nhạy cảm của vi sinh vật tự dưỡng:
  - Quần thể AOB và NOB có tốc độ sinh trưởng riêng ($\mu_{max}$) chậm hơn nhiều so với vi khuẩn dị dưỡng.
  - Vi sinh vật tự dưỡng rất dễ bị ức chế bởi sốc tải nạp độc chất, dao động nhiệt độ, giảm pH và thiếu oxy cục bộ.

##### 1.2.2 Hạn chế của chiến lược điều khiển PID và cảm biến DO truyền thống
- Nguyên lý điều khiển PID: Các trạm xử lý nước thải tập trung sử dụng bộ điều khiển tỷ lệ - tích phân - vi phân (PID) để duy trì oxy hòa tan (DO) tại một điểm đặt cố định (Gu và cộng sự, 2023).
- Lãng phí năng lượng sục khí: Điểm đặt DO cố định không thích ứng theo tải nạp thực tế, gây tiêu tốn điện năng sục khí dư thừa trong các khung giờ tải nạp thấp.
- Kém thích ứng với biến động động học trong hệ phân tán:
  - Hệ thống xử lý tại chỗ chịu biến động tải nạp lớn và đột ngột (amplified load variability).
  - Bộ điều khiển PID chỉ chỉnh van khí theo nồng độ DO dư, thiếu khả năng điều chỉnh động theo tải lượng $NH_4^+-N$ thực tế đi vào hệ thống (Li và cộng sự, 2022; Shi và cộng sự, 2024).
- Suy giảm chất lượng đo lường của cảm biến DO ngập nước:
  - Đầu dò DO ngâm trực tiếp trong bùn hoạt tính chịu sục khí liên tục.
  - Tích tụ bùn và màng bám sinh học (biofouling) diễn ra nhanh trên màng cảm biến, dẫn đến hiện tượng trôi dạt tín hiệu đo (sensor drift).
  - Sai lệch tín hiệu làm bộ điều khiển nhầm lẫn giữa sự cố cảm biến và sự biến đổi tải nạp thật, gây mất ổn định kiểm soát quá trình.

##### 1.2.3 Khó khăn khi sử dụng cảm biến online đo hợp chất Nitơ
- Chi phí đầu tư và bảo trì cao:
  - Các cảm biến đo online $NH_4^+-N$, $NO_2^--N$ và $NO_3^--N$ thương mại có giá thành rất cao (Huang và cộng sự, 2024).
  - Cần quy trình bảo dưỡng liên tục và hóa chất chuẩn phức tạp, vượt quá khả năng tài chính của các hệ xử lý phân tán.
- Tác động bất lợi của môi trường bùn nồng độ cao:
  - Nồng độ bùn hoạt tính lơ lửng cao trong bể MBR nhanh chóng làm tắc nghẽn bề mặt màng bán thấm hoặc thấu kính quang học.
  - Chất hữu cơ hòa tan, chất rắn lơ lửng và các ion cản trở trong nước xám gây méo mó kết quả đo.
- Độ trễ thời gian phản hồi:
  - Đầu dò đo hợp chất nitơ có độ trễ đo lường (response lag) tương đối lớn.
  - Độ trễ này không bắt kịp các biến động nitơ diễn ra tức thời, cản trở việc kiểm soát tối ưu theo thời gian thực.
- Thách thức chưa được giải quyết trong hệ MBR phân tán:
  - Hiệu suất Nitrification biến động tạo ra nguy cơ đứt gãy quy trình, ngay cả khi chất lượng nước sau lọc tạm thời đạt chuẩn.
  - Các nghiên cứu trước đây chưa cung cấp giải pháp giám sát online khả thi và kinh tế cho trạng thái Nitrification trong lòng bể MBR phân tán.

#### 1.3 Ứng dụng Machine Learning giải thích được trong giám sát quá trình

##### 1.3.1 Khái niệm cảm biến mềm (Soft Sensor) dựa trên dữ liệu
- Cơ chế cảm biến mềm:
  - Ước tính trạng thái sinh học phức tạp khó đo trực tiếp (trạng thái Nitrification) thông qua mô hình toán học và các biến đo lường sẵn có (Van de Walle và cộng sự, 2023).
  - Cảm biến mềm khai thác dữ liệu vận hành vật lý của hệ thống cùng với các chỉ tiêu chất lượng nước sau lọc màng.
- Lợi ích loại bỏ cảm biến xâm lấn:
  - Không đặt đầu dò đo nitơ trực tiếp trong bùn lơ lửng, loại bỏ nguy cơ bám bẩn sinh học trên cảm biến.
  - Thời gian phản hồi tức thì với chi phí bảo trì rất thấp, hỗ trợ can thiệp quy trình kịp thời (Bahramian và cộng sự, 2023).
- So sánh với mô hình cơ chế sinh học:
  - Mô hình học máy dựa trên dữ liệu (Data-driven ML) cần ít thông số đầu vào hơn mô hình cơ chế bùn hoạt tính truyền thống (như dòng mô hình ASM) (Duarte và cộng sự, 2024).
  - Tránh được quy trình hiệu chuẩn hàng chục thông số động học phức tạp, phù hợp cho trạm phân tán vận hành tự động.
- Chuyển đổi từ giám sát thụ động dòng ra sang giám sát tiến trình chủ động:
  - Nghiên cứu trước đây chủ yếu tập trung dự đoán chất lượng nước đầu ra cuối cùng, hiệu suất tách chất ô nhiễm hoặc hiện tượng tắc màng lọc (Muniz de Queiroz và cộng sự, 2025; Shi và cộng sự, 2022; Zhong và cộng sự, 2022).
  - Việc chỉ giám sát dòng ra có tính chất thụ động, tốn công sức, không thể can thiệp kịp thời trước các biến cố bất thường và không thể truy nguyên khiếm khuyết tiến trình (Moretti và cộng sự, 2024).
  - Giám sát tiến trình thời gian thực (Real-time process monitoring) cho phép kiểm soát chủ động, tăng cường độ dẻo dai của hệ thống và cảnh báo sớm sự cố sinh học.

##### 1.3.2 Nhu cầu về tính giải thích được (Interpretable ML)
- Yêu cầu xây dựng niềm tin pháp lý và cộng đồng:
  - Nước xám tái sử dụng tiếp xúc gần với con người, đòi hỏi độ tin cậy tuyệt đối về mặt dịch tễ và quy chuẩn xả thải (Allen và cộng sự, 2024).
  - Mô hình học máy phải minh bạch lý do ra quyết định, tránh hiện tượng "hộp đen" (black box) gây e ngại cho người vận hành.
- Khám phá cơ chế và khắc phục khiếm khuyết mô hình:
  - Khả năng giải thích nội tại và hậu nghiệm giúp kỹ sư hiểu rõ tương tác giữa các biến vận hành và phản ứng sinh học.
  - Nhận diện độ nhạy của dự đoán trước các hạn chế của dữ liệu huấn luyện và hiện tượng lệch phân phối dữ liệu (distributional biases).
  - Cung cấp định hướng cụ thể để tinh chỉnh thuật toán trước khi triển khai ngoài thực địa.

##### 1.3.3 Mục tiêu cốt lõi và đóng góp của công trình
- Thiết lập bài toán phân loại nhị phân trạng thái Nitrification:
  - Dự đoán trạng thái Nitrification ở hai mức nhãn: "Đầy đủ" (Sufficient - Positive class) hoặc "Không đầy đủ" (Insufficient - Negative class).
  - Tiêu chuẩn trạng thái Nitrification đầy đủ: Nồng độ $NO_3^--N$ sau màng lớn hơn tổng nồng độ của $NO_2^--N$ và $NH_4^+-N$ ($NO_3^--N > NO_2^--N + NH_4^+-N$).
- Tuyển chọn 6 biến đầu vào tương thích cảm biến thương mại:
  - Tiêu chuẩn tuyển chọn: Đo lường trực tiếp được, tương thích cảm biến online sẵn có, và có ý nghĩa vật lý vận hành.
  - 3 thông số vận hành hệ thống: Lưu lượng sục khí ($AirFlow$), Lưu lượng nước thải đầu vào ($InfluentFlow$), và Áp suất xuyên màng ($TMP$).
  - 3 chỉ tiêu dòng thấm sau màng: Nhu cầu oxy hóa học ($COD$), Nồng độ nitrat ($NO_3^--N$), và Nồng độ amoni ($NH_4^+-N$).
  - Loại bỏ các biến bất khả thi: Biến DO bị loại do tỷ lệ thiếu hụt dữ liệu trên $50\%$; biến tổng nitơ ($TN$) bị loại do cảm biến đắt đỏ và độ trễ đo lớn.
- Đánh giá có hệ thống ba thuật toán học máy giải thích được:
  - Hồi quy Logistic (Logistic Regression - LR): Mô hình tuyến tính đơn giản, có độ chệch cao (high bias) và phương sai thấp (low variance).
  - Rừng ngẫu nhiên (Random Forest - RF): Mô hình kết hợp biểu quyết cây quyết định, cân bằng giữa độ chệch và phương sai.
  - Tăng cường độ dốc cực đại (Extreme Gradient Boosting - XGB): Mô hình chuỗi cây tuần tự, có độ chệch thấp (low bias) và phương sai cao (high variance).
- Chiến lược tối ưu hóa ưu tiên độ chính xác dự đoán dương (Precision):
  - Mục tiêu cốt lõi: Ngăn chặn rủi ro đưa ra quyết định sai lầm khi hệ thống thiếu hụt nitrit hóa nhưng bị mô hình phân loại nhầm thành đầy đủ.
  - Tối đa hóa Precision đạt được thông qua việc ép thấp tỷ lệ dương tính giả ($FPR \to 0$) trong khi vẫn đảm bảo tỷ lệ dương tính thật ($TPR$) cao.
  - Hiệu suất trong điều kiện chuẩn (hệ bùn lơ lửng không giá thể): Cả LR và XGB đều đạt điểm Precision trên $0.85$.
- Giải thích hậu nghiệm và kiểm chứng liên kịch bản (Cross-scenario validation):
  - Sử dụng phân tích SHAP (SHapley Additive exPlanations), tầm quan trọng đặc trưng, và phân tích tương quan cặp để làm rõ cơ chế dự đoán.
  - Kiểm chứng mô hình đã huấn luyện từ hệ MBR bùn lơ lửng sang hệ MBR lai bổ sung giá thể sinh học PVDF thực hiện đồng thời nitrat hóa và khử nitrat (Simultaneous Nitrification-Denitrification - SND).
  - Mô hình RF thể hiện khả năng tổng quát hóa xuất sắc nhất với điểm Precision đạt $0.87$, chứng minh tính chuyển giao thực tiễn cao.
  - Đề xuất khung điều khiển sục khí tự động thích ứng dựa trên kết quả giám sát thời gian thực nhằm tối ưu hóa năng lượng và chất lượng nước.
