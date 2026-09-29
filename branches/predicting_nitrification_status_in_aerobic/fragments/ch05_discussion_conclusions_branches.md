### 5. Thảo luận, Triển vọng kiểm soát bền vững và Kết luận

#### 5.1 Giới hạn dữ liệu và chiến lược thu thập dữ liệu thông minh

##### 5.1.1 Thách thức từ kích thước mẫu nhỏ và sự mất cân bằng dữ liệu
- Quy mô tập dữ liệu thực nghiệm:
  + Nghiên cứu thu thập $N = 120$ mẫu dữ liệu trong $235$ ngày vận hành liên tục của hai hệ MBR ($10\text{ L}$).
  * Chi phí và thời gian phân tích phòng thí nghiệm tạo ra rào cản lớn cho việc mở rộng dữ liệu.
  * Các phép đo ướt cho $\text{COD}$, $\text{NH}_4^+-\text{N}$, $\text{NO}_2^--\text{N}$, $\text{NO}_3^--\text{N}$ và $\text{TN}$ đòi hỏi quy trình phức tạp.
- Ảnh hưởng của hiện tượng mất cân bằng dữ liệu:
  * Tỷ lệ chênh lệch giữa trạng thái Đầy đủ ($y = 1$) và Không đầy đủ ($y = 0$) làm lệch siêu phẳng quyết định.
  * Hiện tượng mất cân bằng mẫu làm giảm khả năng nhận diện các trạng thái chuyển tiếp sinh học.
  * Quá trình Nitrification và khử Nitrat đồng thời (SND) tạo ra nhiều điểm dữ liệu biên khó phân tách.
- Nguy cơ quá khớp và khoảng tin cậy mở rộng:
  * Kích thước mẫu nhỏ làm tăng nguy cơ quá khớp cục bộ dù độ chính xác kiểm tra đạt mức cao ($\text{Accuracy} > 0.80$).
  * Khoảng tin cậy $95\%$ ($95\%\text{ CI}$) của các chỉ số hiệu năng bị nới rộng đáng kể.
  * Dữ liệu hạn chế gây khó khăn cho việc tối ưu hóa đường cong quan hệ giữa $\text{TPR}$ và $\text{FPR}$.
- Đánh giá rủi ro định lượng đối với kết quả dương tính giả ($\text{FP}$):
  * Lỗi dương tính giả xảy ra khi mô hình dự đoán nhầm trạng thái thiếu hụt thành trạng thái đầy đủ.
  * Phân loại nhầm $\text{FP}$ khiến hệ thống điều khiển giảm cấp sục khí một cách sai lầm.
  * Quyết định sai lầm này dẫn đến tích tụ amoni độc hại và phá vỡ tiêu chuẩn nước tái sử dụng.
  * Hệ thống tái sử dụng nước xám tại chỗ đòi hỏi kiểm soát nghiêm ngặt rủi ro $\text{FP}$ để bảo vệ người dùng.
- Mở rộng không gian đặc trưng để phân tích độ nhạy:
  * Việc chỉ dựa vào nồng độ dòng ra $\text{NH}_4^+-\text{N}$ và $\text{NO}_3^--\text{N}$ chưa phản ánh toàn diện biến động của bể.
  * Nghiên cứu cần tích hợp thêm các thông số động học dòng vào và chuỗi thời gian để nâng cao độ tin cậy.

##### 5.1.2 Chiến lược mở rộng dữ liệu và tự động hóa giám sát
- Triển khai cảm biến quang học và điện cực đo tự động trên dòng lọc:
  * Lắp đặt cảm biến đo dòng ra (permeate online sensors) giúp tăng tần suất lấy mẫu từ hàng ngày lên hàng phút.
  * Cảm biến quang phổ hấp thụ tia khả kiến UV-Vis hỗ trợ giám sát liên tục nồng độ $\text{COD}$ và $\text{NO}_3^--\text{N}$.
  * Điện cực chọn lọc ion ($\text{ISE}$) trên dòng lọc cung cấp tín hiệu amoni tức thời với độ trễ thấp.
- Tối ưu hóa tần suất đo lường và chi phí vận hành:
  * Tần suất đo cần cân bằng giữa yêu cầu an toàn chất lượng nước và chi phí bảo trì thiết bị ($\text{OPEX}$).
  * Nghiên cứu tăng tần suất đo vào các khung giờ cao điểm phát sinh nước xám trong tòa nhà.
  * Hệ thống giảm tần suất đo trong các chu kỳ lưu lượng thấp để kéo dài tuổi thọ đầu dò cảm biến.
- Phân tích các điểm phân loại nhầm để thiết lập hệ thống cảnh báo sớm:
  * Phân tích các giá trị đầu vào tại điểm phân loại sai giúp làm sáng tỏ cơ chế suy giảm vi sinh.
  * Dữ liệu bất thường đóng vai trò then chốt để xây dựng ranh giới an toàn cho thuật toán cảnh báo sớm.
- Lộ trình kiểm chứng 3 pha từ nước thải tổng hợp đến thực tế:
  * Pha I (Nước xám tổng hợp $\rightarrow$ Nước xám tổng hợp): Xác lập bằng chứng khái niệm (Proof-of-Concept) trên hệ pilot phòng thí nghiệm.
  * Pha II (Nước xám tổng hợp $\rightarrow$ Nước xám thực tế): Đánh giá độ trôi dạt phân phối. Thử nghiệm trên nguồn thải thực của tòa nhà.
  * Pha III (Mô hình huấn luyện lai): Huấn luyện với tỷ lệ phối trộn. Sử dụng $60\%$ dữ liệu thực tế và $40\%$ dữ liệu tổng hợp.
- Tích hợp có chủ đích các kịch bản hỏng hóc và điều kiện cực đoan:
  * Mở rộng dải thực nghiệm bao gồm sự cố máy nén khí và hiện tượng nghẽn diffusers phân phối khí.
  * Thu thập dữ liệu khi xảy ra tổn thương màng lọc hoặc rò rỉ bùn hoạt tính sang dòng permeate.
  * Ghi nhận động học hệ thống dưới các cú sốc tải nạp hữu cơ và điều kiện sục khí cưỡng bức mức thấp.

#### 5.2 Đánh đổi giữa các đặc trưng đầu vào và chi phí phần cứng

##### 5.2.1 So sánh chi phí và độ tin cậy giữa cảm biến trong bể và sau lọc
- Hạn chế nghiêm trọng của cảm biến ngập trực tiếp trong bể phản ứng:
  * Nồng độ bùn hoạt tính cao ($\text{MLSS} = 3000 - 8000\text{ mg/L}$) gây hiện tượng bám bẩn sinh học nặng nề trên đầu dò.
  * Cảm biến oxy hòa tan ($\text{DO}$) và tổng nitơ ($\text{TN}$) ngập nước bị trôi dạt tín hiệu đo liên tục.
  * Người vận hành phải thực hiện vệ sinh cơ học hàng ngày và hiệu chuẩn hóa chất hàng tuần.
  * Tỷ lệ dữ liệu khuyết thiếu của cảm biến $\text{DO}$ trong nghiên cứu vượt quá $50\%$, buộc phải loại bỏ khỏi mô hình.
  * Chi phí đầu tư ban đầu ($\text{CAPEX}$) và chi phí duy tu ($\text{OPEX}$) của cụm cảm biến ngập nước rất tốn kém.
- Lợi thế kỹ thuật vượt trội của bộ 6 đặc trưng đo dòng ra và thông số máy móc:
  * Nhóm 3 thông số máy móc gồm lưu lượng khí $Q_{air}$ ($\text{L/min}$), lưu lượng vào $Q_{in}$ ($\text{L/h}$) và áp suất xuyên màng $\text{TMP}$ ($\text{kPa}$).
  * Nhóm 3 thông số chất lượng dòng lọc gồm nồng độ $\text{COD}$, $\text{NO}_3^--\text{N}$ và $\text{NH}_4^+-\text{N}$ ($\text{mg/L}$).
  * Cảm biến lắp đặt sau màng gốm phẳng $\text{SiC}$ (kích thước lỗ $0.1\ \mu\text{m}$) tiếp xúc với dòng nước không chứa bùn lơ lửng ($\text{TSS} \approx 0\text{ mg/L}$).
  * Dòng lọc trong suốt ngăn ngừa triệt để sự hình thành màng biofilm trên bề mặt quang học và điện cực.
  * Tuổi thọ cảm biến kéo dài trên 24 tháng với chu kỳ bảo dưỡng định kỳ giãn cách theo quý.
  * Giải pháp giúp tối ưu hóa tổng chi phí sở hữu và rút ngắn thời gian thu hồi vốn đầu tư cho công trình.

##### 5.2.2 Cân bằng giữa độ phức tạp mô hình và hiệu quả ứng dụng thực tế
- Đánh đổi giữa số lượng biến đầu vào và độ chính xác dự đoán:
  * Bổ sung quá nhiều thông số đầu vào không bảo đảm tăng độ chính xác phân loại của mô hình học máy.
  * Dữ liệu dư thừa làm tăng độ phức tạp tính toán và gia tăng rủi ro quá khớp trên tập mẫu nhỏ.
  * Cấu trúc 6 biến đầu vào tinh gọn đạt được sự cân bằng tối ưu giữa tương quan thống kê và ý nghĩa công nghệ.
- Xử lý độ trễ thời gian giữa dòng vào và dòng ra:
  * Biến động của lưu lượng dòng vào $Q_{in}$ làm thay đổi thời gian lưu nước thủy lực ($\text{HRT} = 8 - 16\text{ h}$).
  * Nồng độ các chất trong dòng permeate phản ánh trạng thái sinh hóa của bể tại thời điểm trong quá khứ.
  * Xây dựng các mô hình con chuyên biệt theo dải lưu lượng giúp khắc phục sai lệch do độ trễ vận chuyển chất.
- Khắc phục sự không đồng nhất nồng độ oxy hòa tan trong bể sinh học:
  * Gradient nồng độ $\text{DO}$ trong bể MBR biến thiên phức tạp do thủy động lực học và sự phân bố bọt khí.
  * Cảm biến $\text{DO}$ đơn điểm không thể đại diện cho môi trường vi mô của toàn bộ thể tích bùn.
  * Sử dụng lưu lượng cấp khí $Q_{air}$ làm biến đại diện gián tiếp đem lại độ ổn định cao hơn phép đo $\text{DO}$ cục bộ.
- Tối ưu hóa triển khai trên thiết bị tính toán biên (Edge Computing):
  * Các thuật toán nhẹ như Logistic Regression và Random Forest tiêu tốn dung lượng bộ nhớ nhỏ dưới $10\text{ MB}$.
  * Thuật toán có thể nhúng trực tiếp vào vi điều khiển cục bộ hoặc bộ điều khiển lập trình $\text{PLC}$.
  * Hệ thống xử lý dữ liệu và đưa ra quyết định tại chỗ mà không cần truyền dữ liệu lên đám mây.

#### 5.3 Giải pháp nâng cao tính chuyển giao mô hình (Model transferability)

##### 5.3.1 Thích ứng miền (Domain Adaptation) và học chuyển giao (Transfer Learning)
- Định nghĩa và vai trò của tính chuyển giao mô hình:
  * Tính chuyển giao biểu thị năng lực thích ứng của mô hình sang trạm mới. Quá trình chỉ cần lượng dữ liệu tái huấn luyện tối thiểu.
  * Kỹ thuật này giải quyết triệt để vấn đề khan hiếm dữ liệu nhãn khi khởi động các trạm MBR mới.
- Các chiến lược học chuyển giao then chốt:
  * Căn chỉnh không gian đặc trưng (Feature alignment) để giảm thiểu khoảng cách phân phối giữa hai nguồn nước thải.
  * Khởi tạo trọng số mô hình từ mô hình huấn luyện trước (Pre-trained models) trên hệ thống cơ sở.
  * Áp dụng kiến trúc siêu học (Meta-learning) nhằm tối ưu hóa khả năng thích nghi nhanh qua vài mẫu dữ liệu mới.
  * Tăng cường dữ liệu (Data augmentation) dựa trên các biến thiên vận hành thực tế đã ghi nhận.
- Kinh nghiệm thực tiễn từ các ngành kỹ thuật liên quan:
  * Mô hình $\text{LSTM}$ xếp chồng dự đoán lưu lượng giao thông chính xác nhờ tinh chỉnh mô hình từ vùng giàu dữ liệu.
  * Thuật toán ước lượng tuổi thọ pin xe điện duy trì độ chính xác cao nhờ tăng cường dữ liệu thích ứng điều kiện tải.
  * Mạng $\text{MobileNetV2}$ chẩn đoán lỗi vòng bi cơ khí hiệu quả thông qua tinh chỉnh miền mục tiêu.
- Ba định hướng nâng cao tính chuyển giao cho công nghệ xử lý nước:
  * Tối ưu hóa quy trình lấy dữ liệu làm trung tâm: Thiết kế thực nghiệm đa dạng. Cần bao quát nhiều chế độ tải thủy lực và tải hữu cơ.
  * Khung mô hình huấn luyện trước đặc thù ngành: Kết nối cơ sở dữ liệu mở giữa các viện nghiên cứu và doanh nghiệp.
  * Đổi mới cấu trúc mô hình: Phân cụm mô hình con theo dải công suất trạm kết hợp các biến quy mô hình học.
- Kỹ thuật tinh chỉnh mô hình với tập dữ liệu nhỏ (Fine-tuning):
  * Kế thừa toàn bộ cấu trúc cây quyết định hoặc ma trận trọng số ban đầu của mô hình gốc.
  * Sử dụng $10 - 20\%$ mẫu dữ liệu thực nghiệm tại trạm mới để cập nhật ngưỡng phân loại xác suất.

##### 5.3.2 Ứng dụng mô hình lai kết hợp cơ chế vi sinh (Hybrid mechanistic-ML models)
- Hạn chế của mô hình học máy thuần túy dữ liệu:
  * Mô hình học máy thuần túy hoạt động như hàm nội suy thống kê thiếu sự ràng buộc của các định luật bảo toàn.
  * Dự đoán dễ sai lệch vật lý khi điều kiện vận hành vượt ngoài biên dữ liệu huấn luyện.
- Cơ chế tích hợp mô hình bùn hoạt tính $\text{ASM}$ với cảm biến mềm học máy:
  * Khối mô hình cơ chế $\text{ASM}$ (Activated Sludge Models) thiết lập cân bằng khối lượng và động học phản ứng sinh hóa.
  * Tốc độ phản ứng tiêu thụ cơ chất amoni tuân theo phương trình động học $\text{Monod}$:
    $$r_{NH4} = -\mu_{max, AOB} \cdot \frac{S_{NH4}}{K_{NH4} + S_{NH4}} \cdot \frac{S_{O2}}{K_{O,AOB} + S_{O2}} \cdot X_{AOB}$$
    Trong đó:
    * $\mu_{max, AOB}$ là tốc độ sinh trưởng tối đa của vi khuẩn oxy hóa amoni ($\text{d}^{-1}$).
    * $S_{NH4}$ là nồng độ chất nền amoni hòa tan ($\text{mg N/L}$).
    * $K_{NH4}$ là hằng số bán bão hòa amoni ($\text{mg N/L}$).
    * $S_{O2}$ là nồng độ oxy hòa tan trong bể ($\text{mg } \text{O}_2\text{/L}$).
    * $K_{O,AOB}$ là hằng số ái lực oxy của vi khuẩn hiếu khí ($\text{mg } \text{O}_2\text{/L}$).
    * $X_{AOB}$ là sinh khối của chủng vi khuẩn oxy hóa amoni ($\text{mg COD/L}$).
  * Cảm biến mềm học máy đảm nhận nhiệm vụ bù đắp các thành phần động học phi tuyến chưa được mô hình hóa.
  * Mô hình lai nâng cao khả năng khái quát hóa vật lý. Cấu trúc này bảo đảm tính khả thi cho dự báo chất lượng dòng ra.

#### 5.4 Khung điều khiển bền vững dựa trên dữ liệu (Data-driven sustainable control framework)

##### 5.4.1 Cơ chế điều khiển sục khí thích ứng từng nấc (Stepwise Adaptive Aeration Control)
- Hạn chế của chiến lược điều khiển $\text{PID}$ truyền thống:
  * Bộ điều khiển $\text{PID}$ cố định nồng độ $\text{DO}$ tại ngưỡng $2.0 - 3.0\text{ mg/L}$ bất kể tải lượng amoni thực tế.
  * Phương pháp này dẫn đến sục khí dư thừa nghiêm trọng vào ban đêm và các chu kỳ tải thấp.
  * Sục khí liên tục làm triệt tiêu các vùng thiếu khí vi mô cần thiết cho quá trình khử nitrat đồng thời ($\text{SND}$).
- Nguyên lý vận hành của sơ đồ điều khiển thích ứng từng nấc:
  * Hệ thống xác định lưu lượng khí cơ sở $a_i$ ($\text{L/min}$) và nấc tăng gia lưu lượng $A$ ($\text{L/min}$).
  * Giả định lưu lượng nước vào $Q_{in}$ không đổi trong chu kỳ tính toán để giữ ổn định thời gian lưu nước.
  * Tại mốc thời gian $t_i$, mô hình học máy thu nhận 6 đặc trưng và đưa ra phân loại trạng thái Nitrification.
  * Nếu mô hình dự đoán trạng thái Đầy đủ ($y = 1$): Hệ thống duy trì lưu lượng khí tại mức nền $a_i$.
  * Khi dự đoán Không đầy đủ ($y = 0$): Bộ điều khiển tự động tăng lưu lượng khí lên mức $a_i + A$.
  * Tại chu kỳ kiểm tra tiếp theo $t_{i+1}$:
    + Nếu kết quả dự đoán chuyển sang Đầy đủ: Lưu lượng khí lập tức hạ về mức nền $a_i$.
    + Nếu kết quả dự đoán vẫn Không đầy đủ: Lưu lượng khí tiếp tục nâng thêm một nấc lên mức $a_i + 2A$.
  * Quy trình tăng giảm nấc lặp lại liên tục qua các mốc thời gian $t_{i+2}, t_{i+3}, \dots$ theo bước nhảy $A$.
- Cơ chế bảo vệ và xử lý ngưỡng dung hạn thiết bị:
  * Khi lưu lượng khí chạm công suất giới hạn tối đa của máy thổi khí ($Q_{air, max}$), bộ điều khiển kích hoạt báo động.
  * Hệ thống cảnh báo sớm phát tín hiệu để nhân viên vận hành bổ sung máy nén hoặc chuyển hướng dòng nước xám dư thừa.
- Nâng cấp sơ đồ phân loại sang mô hình đa mức (Multiclass scheme):
  * Phát triển khung phân loại 4 trạng thái tương ứng với các mức hoàn thành Nitrification: $25\%$, $50\%$, $75\%$ và $100\%$.
  * Mô hình đa mức hỗ trợ điều khiển cấp khí tỷ lệ. Giải pháp loại bỏ sự thay đổi đột ngột giữa các nấc sục khí.
  * Chiến lược giảm cấp khí dần dần (Gradual reduction) giúp bảo vệ hệ vi sinh vật tự dưỡng khỏi hiện tượng sốc tải.

##### Bài toán ví dụ: Tính toán điều khiển sục khí thích ứng từng nấc và đánh giá năng lượng
- **Bài toán (Problem)**:
  Mô phỏng thuật toán điều khiển sục khí thích ứng từng nấc cho hệ MBR hiếu khí xử lý nước xám ($V = 10\text{ L}$). Lưu lượng dòng vào duy trì không đổi $Q_{in} = 0.833\text{ L/h}$ ($\text{HRT} = 12\text{ h}$). Xác định lưu lượng khí cấp $Q_{air}(t_k)$ và điện năng tiêu thụ qua 4 chu kỳ $t_0, t_1, t_2, t_3$. Mỗi chu kỳ kéo dài $\Delta t = 2\text{ h}$. Đánh giá tỷ lệ phần trăm điện năng tiết kiệm được so với chiến lược điều khiển $\text{PID}$ duy trì nồng độ $\text{DO}$ cố định.
- **Dữ liệu cho trước (Given)**:
  * Lưu lượng khí sục mức cơ sở: $a_i = 1.0\text{ L/min}$.
  * Nấc tăng gia lưu lượng khí: $A = 0.5\text{ L/min}$.
  * Lưu lượng khí tối đa của máy nén: $Q_{air, max} = 3.0\text{ L/min}$.
  * Công suất tiêu thụ điện của máy thổi khí theo lưu lượng: $P(Q_{air}) = k_p \cdot Q_{air}$ với $k_p = 40\text{ W}/(\text{L/min})$.
  * Lưu lượng khí trung bình của hệ thống $\text{PID}$ truyền thống: $Q_{PID} = 2.5\text{ L/min}$.
  * Chu kỳ điều khiển: $\Delta t = 2\text{ h}$.
  * Chuỗi kết quả dự đoán trạng thái Nitrification từ mô hình Random Forest:
    + Thời điểm $t_0$: Dự đoán Đầy đủ ($y(t_0) = 1$).
    + Thời điểm $t_1$: Tải amoni tăng, dự đoán Không đầy đủ ($y(t_1) = 0$).
    + Thời điểm $t_2$: Amoni chưa xử lý hết, dự đoán Không đầy đủ ($y(t_2) = 0$).
    + Thời điểm $t_3$: Hệ thống hồi phục, dự đoán Đầy đủ ($y(t_3) = 1$).
- **Công thức (Formula)**:
  * Quy tắc điều chỉnh lưu lượng khí sục từng nấc:
    $$Q_{air}(t_k) = \begin{cases} a_i & \text{khi } y(t_k) = 1 \\ \min(Q_{air}(t_{k-1}) + A, Q_{air, max}) & \text{khi } y(t_k) = 0 \end{cases}$$
  * Điện năng tiêu thụ trong chu kỳ thứ $k$:
    $$E_k = k_p \cdot Q_{air}(t_k) \cdot \Delta t \quad (\text{Wh})$$
  * Tổng điện năng tiêu thụ của phương pháp học máy qua 4 chu kỳ ($8\text{ h}$):
    $$E_{total, ML} = \sum_{k=0}^{3} E_k \quad (\text{Wh})$$
  * Tổng điện năng tiêu thụ của hệ thống điều khiển $\text{PID}$ cố định:
    $$E_{total, PID} = k_p \cdot Q_{PID} \cdot 4\Delta t \quad (\text{Wh})$$
  * Tỷ lệ phần trăm điện năng tiết kiệm:
    $$\eta_{saving} = \frac{E_{total, PID} - E_{total, ML}}{E_{total, PID}} \times 100\%$$
- **Các bước tính toán (Steps)**:
  * Bước 1: Tại $t_0$, mô hình dự đoán $y(t_0) = 1$. Lưu lượng khí đặt ở mức nền:
    $$Q_{air}(t_0) = a_i = 1.0\text{ L/min}$$
    $$E_0 = 40 \times 1.0 \times 2 = 80\text{ Wh}$$
  * Bước 2: Tại $t_1$, mô hình dự đoán $y(t_1) = 0$. Tăng lưu lượng khí thêm một nấc $A$:
    $$Q_{air}(t_1) = 1.0 + 0.5 = 1.5\text{ L/min}$$
    $$E_1 = 40 \times 1.5 \times 2 = 120\text{ Wh}$$
  * Bước 3: Tại $t_2$, mô hình dự đoán $y(t_2) = 0$. Tiếp tục nâng lưu lượng khí thêm nấc thứ hai:
    $$Q_{air}(t_2) = 1.5 + 0.5 = 2.0\text{ L/min} \le Q_{air, max}$$
    $$E_2 = 40 \times 2.0 \times 2 = 160\text{ Wh}$$
  * Bước 4: Tại $t_3$, mô hình dự đoán $y(t_3) = 1$. Quá trình Nitrification hoàn thành, lưu lượng khí hạ về mức nền:
    $$Q_{air}(t_3) = a_i = 1.0\text{ L/min}$$
    $$E_3 = 40 \times 1.0 \times 2 = 80\text{ Wh}$$
  * Bước 5: Tính tổng điện năng tiêu thụ của hệ thống kiểm soát thông minh:
    $$E_{total, ML} = 80 + 120 + 160 + 80 = 440\text{ Wh}$$
  * Bước 6: Tính tổng điện năng tiêu thụ của hệ thống $\text{PID}$ truyền thống:
    $$E_{total, PID} = 40 \times 2.5 \times (4 \times 2) = 40 \times 2.5 \times 8 = 800\text{ Wh}$$
  * Bước 7: Xác định tỷ lệ năng lượng tiết kiệm được:
    $$\eta_{saving} = \frac{800 - 440}{800} \times 100\% = \frac{360}{800} \times 100\% = 45.0\%$$
- **Kết quả (Result)**:
  * Lưu lượng khí sục qua các chu kỳ lần lượt là $1.0\text{ L/min}$, $1.5\text{ L/min}$, $2.0\text{ L/min}$ và $1.0\text{ L/min}$.
  * Hệ thống kiểm soát học máy tiêu thụ $440\text{ Wh}$, tiết kiệm chính xác $45.0\%$ điện năng so với chiến lược $\text{PID}$ ($800\text{ Wh}$).

##### 5.4.2 Lợi ích kép về tiết kiệm năng lượng và chống tắc màng lọc
- Cắt giảm mạnh chi phí năng lượng sục khí:
  * Máy nén khí chiếm $50 - 70\%$ tổng điện năng tiêu thụ của toàn bộ công trình MBR.
  * Kiểm soát cấp khí bám sát tải nạp thực tế giúp giảm $20 - 40\%$ lượng điện tiêu thụ của máy thổi khí.
  * Giảm tiêu thụ điện năng trực tiếp hạ thấp phát thải khí nhà kính tương đương ($\text{CO}_2\text{e}$) của trạm.
- Kiểm soát và giảm tốc độ tắc bẩn màng lọc ($\text{TMP}$ control):
  * Cường độ sục khí quá mức tạo lực cắt thủy lực mạnh làm vỡ vụn các bông bùn hoạt tính.
  * Bông bùn vỡ giải phóng lượng lớn chất cao phân tử ngoại bào ($\text{EPS}$) và sản phẩm vi sinh hòa tan ($\text{SMP}$).
  * $\text{EPS}$ và $\text{SMP}$ bám dính sâu vào hệ thống mao quản của màng gốm phẳng $\text{SiC}$, gây tắc màng không thuận nghịch.
  * Duy trì lưu lượng khí ở mức vừa đủ giúp hạn chế hiện tượng phân rã bông bùn trong bể.
  * Tốc độ gia tăng áp suất xuyên màng ($d\text{TMP}/dt$) giảm xuống rõ rệt, kéo dài chu kỳ rửa hóa chất tại chỗ ($\text{CIP}$).
- Bảo đảm an toàn sinh học cho các ứng dụng tái sử dụng nước tại nguồn:
  * Tiêu chí tối ưu hóa ưu tiên độ chính xác $\text{Precision}$ giúp loại bỏ nguy cơ phát tán dòng nước chưa khử hết amoni.
  * Nước sau lọc đáp ứng tiêu chuẩn khắt khe phục vụ xả bồn cầu, rửa sàn và tưới cây cảnh quan đô thị.

#### 5.5 Kết luận và Khuyến nghị triển khai (Conclusions & Recommendations)

##### 5.5.1 Tóm tắt các phát hiện cốt lõi
- Tính khả thi của giải pháp cảm biến mềm giải thích được:
  * Nghiên cứu chứng minh thành công khả năng dự đoán chuẩn xác trạng thái Nitrification chỉ với 6 thông số đo dòng ra.
  * Các mô hình không đòi hỏi lắp đặt cảm biến chìm phức tạp trong môi trường bùn hoạt tính.
  * Trong điều kiện chuẩn không giá thể, cả Logistic Regression và XGBoost đều đạt chỉ số $\text{Precision} > 0.85$.
- Hiệu năng vượt trội của Random Forest trong kiểm chứng liên kịch bản:
  * Mô hình Random Forest đạt $\text{Precision} = 0.87$ khi áp dụng trực tiếp lên hệ thống MBR bổ sung giá thể vi sinh $\text{PVDF}$.
  * Tất cả mô hình duy trì độ nhạy $\text{TPR} \ge 0.80$ và độ chính xác tổng thể $\text{Accuracy} > 0.75$ khi chuyển giao miền.
  * Khoảng tin cậy $95\%$ của Random Forest thu hẹp hơn so với XGBoost, chứng minh độ ổn định cao trước nhiễu phân phối.
- Minh bạch hóa cơ chế ra quyết định qua phân tích giải thích hậu nghiệm:
  * Kết quả phân tích $\text{SHAP}$, $\text{KDE}$ và ma trận phân tán xác nhận $\text{NO}_3^--\text{N}$ và $\text{NH}_4^+-\text{N}$ là hai biến chi phối cốt lõi.
  * Lỗi dương tính giả tập trung tại vùng ranh giới. Ngưỡng sai số nằm quanh $\text{NO}_3^--\text{N} \approx 9\text{ mg/L}$ và $\text{NH}_4^+-\text{N} \approx 2\text{ mg/L}$.

##### 5.5.2 Khuyến nghị cho công tác thiết kế và triển khai công nghiệp
- Tích hợp mô hình học máy vào hệ thống điều khiển công nghiệp:
  * Nhúng thuật toán Random Forest vào bộ điều khiển lập trình $\text{PLC}$ hoặc phần mềm giám sát $\text{SCADA}$ của trạm.
  * Tự động hóa hoàn toàn quy trình đóng mở van sục khí thích ứng mà không cần nhân viên vận hành can thiệp thủ công.
- Ứng dụng rộng rãi cho các trạm xử lý nước xám phi tập trung:
  * Triển khai giải pháp tại các tòa nhà văn phòng, chung cư cao tầng, khách sạn và cụm dân cư cách ly.
  * Cắt giảm đáng kể chi phí đầu tư $\text{CAPEX}$ nhờ loại trừ các cảm biến ngập bể đắt đỏ.
  * Giảm thiểu chi phí bảo trì $\text{OPEX}$ và ngăn ngừa triệt để sự cố vận hành do trôi dạt cảm biến.
- Xây dựng kho dữ liệu mở chuẩn hóa cho ngành tài nguyên nước:
  * Thiết lập các bộ dữ liệu đo chuẩn hóa công khai để cộng đồng nghiên cứu đánh giá chéo năng lực thuật toán $\text{AI/ML}$.
  * Thúc đẩy quá trình chuyển đổi số và nâng cao độ tin cậy của công nghệ xử lý nước tuần hoàn.
