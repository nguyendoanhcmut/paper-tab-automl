## 7. Chín Khoảng trống Nghiên cứu Then chốt và Định hướng Tương lai (Research Gaps and Future Directions)

### 7.1. Khoảng trống 1: Khan hiếm tập dữ liệu chuẩn mở đa cơ sở (Scarcity of Benchmark Datasets)

#### 7.1.1. Thực trạng dữ liệu đơn cơ sở và sự suy giảm hiệu năng do dịch chuyển tập dữ liệu (Dataset Shift)
- Giới hạn quy mô dữ liệu nghiên cứu: Phần lớn nghiên cứu chỉ huấn luyện và kiểm định mô hình trên tập dữ liệu của một cơ sở đơn lẻ.
- Hạn chế về khung thời gian quan trắc: Dữ liệu vận hành thường chỉ được thu thập trong vài tuần hoặc vài tháng. Khoảng thời gian ngắn này cản trở việc đánh giá khả năng tổng quát hóa liên cơ sở.
- Hiện tượng suy giảm độ chính xác: Khi áp dụng mô hình sang công trình MBR khác, hiệu năng dự báo suy giảm đáng kể.
- Nguyên nhân từ dịch chuyển phân phối dữ liệu (dataset shift): Mối quan hệ thống kê giữa đặc trưng đầu vào và tắc nghẽn màng khác nhau giữa các nhà máy. Dữ liệu một cơ sở không thể bao quát các biến thiên này.
- Thiếu vắng bộ dữ liệu chuẩn mực cộng đồng: Ngành học máy xử lý nước thải hiện chưa có bộ dữ liệu chuẩn. Ngành nước thiếu công cụ tương đương ImageNet trong thị giác máy tính.
- Nhu cầu cấp thiết về nền tảng dữ liệu mở Open-MBR: Cộng đồng khoa học cần xây dựng kho dữ liệu vận hành MBR mở và đa cơ sở [17, 24, 47].
- Phạm vi dữ liệu cần thu thập: Kho dữ liệu cần bao quát đa dạng công suất và cấu hình màng. Bộ dữ liệu phải đại diện cho nhiều tính chất nước thải và vùng khí hậu.
- Giới hạn của nền tảng mô phỏng BSM-MBR: Nền tảng BSM-MBR cung cấp môi trường mô phỏng giá trị [36, 50]. Tuy nhiên, dữ liệu mô phỏng không tái hiện đầy đủ đặc tính phi dừng, độ nhiễu và các ràng buộc vận hành thực tế.

#### 7.1.2. Thách thức tổng quát hóa liên cơ sở và giải pháp thích ứng miền
- Khác biệt hình học module màng: Dạng hình học module màng sợi rỗng (hollow-fiber) và màng tấm phẳng (flat-sheet) tạo ra các chế độ thủy động lực học rất khác nhau.
- Biến động hệ vi sinh vật bùn hoạt tính: Cấu trúc quần xã vi sinh vật thay đổi liên tục theo thành phần nước thải cục bộ và nhiệt độ môi trường.
- Sai lệch cửa sổ thông số vận hành: Mỗi cơ sở duy trì các khoảng thời gian lưu bùn (SRT) và thời gian lưu thủy lực (HRT) riêng biệt.
- Xung tải xả thải công nghiệp bất thường: Các đợt xả thải công nghiệp tạo ra biến động tải trọng đột ngột và biên độ lớn. Các biến động này thường vắng mặt trong tập dữ liệu huấn luyện định kỳ.
- Ứng dụng học chuyển giao (Transfer Learning): Kỹ sư lấy mô hình tiền huấn luyện từ nhà máy giàu dữ liệu. Sau đó, họ tinh chỉnh mô hình bằng ít dữ liệu tại trạm đích.
- Áp dụng thích ứng miền (Domain Adaptation): Phương pháp này giảm thiểu sự sai lệch phân phối giữa không gian đặc trưng nguồn và không gian mục tiêu.
- Bằng chứng thực nghiệm từ kỹ thuật môi trường: Transfer Learning và Domain Adaptation đã chứng minh hiệu quả trong các ứng dụng quan trắc chất lượng nước [17, 47].
- Định hướng ưu tiên nghiên cứu: Các nghiên cứu MBR đa cơ sở cần ưu tiên thử nghiệm hai phương pháp trên các tập dữ liệu chuẩn mở dùng chung.

---

### 7.2. Khoảng trống 2: Thiếu hụt định lượng độ bất định trong dự đoán (Absence of Uncertainty Quantification - UQ)

#### 7.2.1. Rủi ro vận hành của dự báo điểm đơn lẻ (Point Predictions)
- Thực trạng áp đảo của dự báo tất định: Hầu hết nghiên cứu hiện nay chỉ cung cấp giá trị dự báo điểm đơn lẻ cho các thông số MBR.
- Thiếu hụt khoảng tin cậy: Rất ít nghiên cứu công bố khoảng dự đoán (prediction intervals) hoặc giới hạn tin cậy (confidence bounds) đi kèm dự báo điểm.
- Tầm quan trọng của độ bất định trong vận hành thực tế: Giá trị bất định định hướng trực tiếp hành vi của hệ thống điều khiển tự động.
- Minh họa tác động điều khiển áp suất xuyên màng (TMP): Sai số dự báo TMP mức $\pm 2\text{ kPa}$ tạo ra phản ứng điều khiển rất khác. Mức đáp ứng này khác biệt lớn so với sai số $\pm 12\text{ kPa}$.
- Yêu cầu an toàn cho Bản sao số Cấp độ III (Tier III Prescriptive DT): Hệ thống AI ra quyết định vòng kín bắt buộc phải có biên bất định. Điều này đảm bảo an toàn tuyệt đối khi vận hành tự động.

#### 7.2.2. Phương pháp luận định lượng độ bất định: Mạng Bayes, Conformal Prediction và Monte Carlo Dropout
- Mạng nơ-ron Bayes (Bayesian Neural Networks - BNNs): Thuật toán gán phân phối xác suất lên các trọng số mạng thay vì sử dụng trọng số điểm cố định.
- Đặc điểm và rào cản của BNNs: BNNs cung cấp cơ sở toán học chặt chẽ để định lượng độ bất định. Tuy nhiên, phương pháp đòi hỏi tài nguyên tính toán rất lớn.
- Kỹ thuật Conformal Prediction: Phương pháp thiết lập các bảo đảm bao phủ không phụ thuộc phân phối (distribution-free coverage guarantees) dựa trên giả định khả hoán.
- Ưu thế tính toán của Conformal Prediction: Thuật toán có chi phí tính toán thấp. Kỹ thuật này đang được ứng dụng rộng rãi trong các hệ thống kỹ thuật đòi hỏi an toàn cao [28, 48].
- Kỹ thuật Monte Carlo Dropout: Kỹ thuật kích hoạt ngẫu nhiên lớp dropout trong giai đoạn suy luận để ước tính khoảng tin cậy với chi phí thấp.
- Định hướng nghiên cứu tương lai: Các nhóm nghiên cứu cần đánh giá hệ thống các phương pháp UQ trên các mô hình học máy ứng dụng cho công nghệ MBR.

---

### 7.3. Khoảng trống 3: Thiếu vắng triển khai Bản sao số tích hợp XAI ở quy mô thực tế (Lack of Full-Scale DT Deployments with Integrated XAI)

#### 7.3.1. Rào cản kỹ thuật và an ninh mạng ở quy mô công nghiệp
- Thực trạng nghiên cứu quy mô nhỏ: Toàn bộ công trình Digital Twin (DT) cho MBR chỉ dừng ở mô phỏng. Một số thử nghiệm khác chỉ triển khai ở quy mô pilot phòng thí nghiệm.
- Thiếu hụt triển khai cấp độ cao ngoài hiện trường: Chưa có nghiên cứu nào công bố hệ thống DT Cấp II hoặc III tại hiện trường. Toàn bộ trạm xử lý đô thị quy mô thực chưa có hệ thống này.
- Thiếu hụt tích hợp giải thích đồng thời: Chưa có hệ thống thực địa nào tạo giải thích XAI tức thời. Nhân viên vận hành chưa thể nhận khuyến nghị AI song song với giám sát.
- Thách thức hiệu chuẩn cảm biến: Cảm biến tại trạm xử lý đối mặt với hiện tượng trôi tín hiệu và bám bẩn sinh học nhanh chóng.
- Yêu cầu độ tin cậy của đường ống dữ liệu (Data Pipeline): Hệ thống truyền dẫn dữ liệu SCADA lên nền tảng DT đòi hỏi tính toàn vẹn và độ trễ thấp.
- Hạ tầng tính toán và an ninh mạng: Việc kết nối điều khiển công nghiệp với thuật toán đám mây làm tăng nguy cơ tấn công mạng.

#### 7.3.2. Yêu cầu tổ chức, trách nhiệm pháp lý và hợp tác liên ngành
- Quản trị thay đổi và đào tạo nhân sự: Đơn vị vận hành cần thích ứng với quy trình vận hành khuyến nghị bởi trí tuệ nhân tạo.
- Khung trách nhiệm hợp đồng (Contractual Liability): Trách nhiệm pháp lý khi xảy ra sự cố nghẹt màng chưa rõ ràng [33, 37]. Cơ chế phân định trách nhiệm khi vi phạm chuẩn xả thải tự động còn thiếu.
- Thiếu hụt tài liệu trong y văn học thuật: Các yếu tố tổ chức và pháp lý hầu như chưa được phân tích trong các bài báo khoa học.
- Mô hình hợp tác liên ngành mẫu mực: Nghiên cứu kiểm chứng quy mô thực của Kovacs và cộng sự [26] nêu bật giá trị hợp tác ba bên. Mô hình này kết nối nhà máy nước, đơn vị công nghệ và viện nghiên cứu.
- Lộ trình tạo lập bằng chứng thực nghiệm: Các bên cần thiết lập chương trình thử nghiệm dài hạn để làm tiền đề cho việc thương mại hóa và cấp phép công nghệ.

---

### 7.4. Khoảng trống 4: Hạn chế trong đặc tính hóa động học nước thải đầu vào (Dynamic Influent Characterization Limitations)

#### 7.4.1. Sự thiếu hụt của cảm biến SCADA thông thường trước các xung tải trọng
- Hạn chế của thiết bị đo SCADA truyền thống: Các đầu đo hiện hữu chỉ thu thập các chỉ số gộp như $\text{COD}$, $\text{BOD}$, $\text{TSS}$, độ đục, $\text{DO}$, $\text{pH}$ và độ dẫn điện.
- Tính chất gộp của thông số dòng vào: Các chỉ số trên chỉ phản ánh bức tranh tổng quát của hỗn hợp nước thải đi vào bể sinh học.
- Tác động của nước thải công nghiệp đột xuất: Sự kiện xả thải công nghiệp đưa vào hệ thống các chất độc hại và chất hoạt động bề mặt.
- Ảnh hưởng của hiện tượng nước mưa thâm nhập: Nước mưa thâm nhập pha loãng dòng vào và thay đổi đột ngột tải trọng thủy lực.
- Biến thiên chu kỳ ngày đêm của nước thải sinh hoạt: Nồng độ ô nhiễm hữu cơ và chất rắn dao động mạnh theo từng khung giờ trong ngày.
- Bất cập của phương pháp lấy mẫu hỗn hợp: Mẫu gộp 24 giờ và cảm biến trực tuyến phản ứng chậm không bắt kịp các xung dao động nhanh [3, 22].
- Hậu quả nghẹt màng bất ngờ: Các biến động động học không được đặc tính hóa là nguyên nhân chính gây ra các đợt tắc nghẽn màng nghiêm trọng.

#### 7.4.2. Tích hợp cảm biến quang phổ học nâng cao và công cụ sinh học phân tử vào tầng cảm biến DT
- Cảm biến quang phổ hấp thụ trực tuyến UV-Vis: Thiết bị cung cấp dữ liệu quang phổ liên tục để phát hiện nhanh các nhóm hợp chất hữu cơ hòa tan đặc thù.
- Đo quang phổ huỳnh quang (Fluorescence Spectrophotometry): Công nghệ này nhận diện các tín hiệu protein-like và humic-like. Các tín hiệu này thuộc chất cao phân tử ngoại bào (EPS) và chất hòa tan vi sinh (SMP).
- Chụp cắt lớp kết hợp quang học (Optical Coherence Tomography - OCT): Kỹ thuật OCT hỗ trợ quan sát trực tiếp bề mặt màng theo thời gian thực. Phương pháp này định lượng cấu trúc lớp bánh bùn (cake layer) với độ chính xác cao.
- Công cụ dấu vân tay cộng đồng vi sinh vật (Microbial Fingerprinting): Kỹ thuật sinh học phân tử giúp theo dõi sự biến đổi cấu trúc quần xã vi sinh vật gây tắc nghẽn sinh học.
- Nâng cao năng lực dự báo mô hình ML: Tích hợp chuỗi dữ liệu cao tần vào tầng cảm biến DT giúp mô hình cảnh báo sớm. Thuật toán nhận diện kịp thời các sự cố nhiễu động nguy hiểm.

---

### 7.5. Khoảng trống 5: Rào cản và khung công nhận pháp lý cho XAI (Regulatory Dimension and Acceptance Frameworks)

#### 7.5.1. Khoảng cách giữa lý thuyết XAI học thuật và thực tiễn cấp phép môi trường
- Nền tảng lý thuyết phát triển nhanh: Y văn học thuật đã chứng minh rõ tiềm năng của XAI [29, 51]. Công cụ này xây dựng niềm tin cho hệ thống quản lý nước thông minh.
- Thiếu vắng tiền lệ pháp lý thực tế: Chưa có nghiên cứu nào ghi nhận giải thích SHAP định hình điều kiện cấp phép môi trường. Tiền lệ pháp lý cho XAI trong ngành nước vẫn hoàn toàn trống.
- Thiếu tác động trong thanh tra thực tế: Đầu ra XAI chưa từng ảnh hưởng đến kết luận thanh tra hay giấy phép vận hành. Cơ quan quản lý chưa dùng XAI để điều chỉnh quy chuẩn xả thải.
- Đứt gãy giữa lý thuyết và pháp lý: Tồn tại khoảng cách lớn giữa năng lực thuật toán trong phòng thí nghiệm và cơ chế pháp lý quản lý nhà máy nước thải.
- Nguy cơ pháp lý khi tự động hóa: Đơn vị vận hành lo ngại rủi ro khi dùng mô hình chưa cấp phép. Nếu xả thải vượt ngưỡng, nhà máy phải chịu xử phạt hành chính nặng.

#### 7.5.2. Xây dựng tiêu chuẩn bằng chứng, kiểm toán và ca sử dụng được công nhận
- Đối thoại với cơ quan quản lý: Cộng đồng kỹ thuật môi trường cần làm việc chặt chẽ với cơ quan quản lý môi trường để thống nhất khung pháp lý.
- Xây dựng tiêu chuẩn bằng chứng kiểm định: Hai bên cần lập tiêu chuẩn định lượng để kiểm tra XAI. Tiêu chuẩn này xác nhận tính chính xác và an toàn của các giải thích thuật toán.
- Xác định phạm vi các ca sử dụng được chấp thuận: Quy định cần phân định rõ hai nhóm quy trình. Nhóm một cho phép AI tự động điều khiển. Nhóm hai bắt buộc con người giám sát trực tiếp.
- Yêu cầu lưu vết kiểm toán (Audit-trail Requirements): Hệ thống phải lưu trữ toàn bộ quyết định điều khiển và giải thích thuật toán để phục vụ công tác thanh tra độc lập.
- Điều kiện tiên quyết để chuyển giao công nghệ: Xây dựng khung pháp lý là bước bắt buộc để đưa hệ thống DT tích hợp XAI từ nghiên cứu vào ứng dụng thương mại.

---

### 7.6. Khoảng trống 6: Chi phí kinh tế phát triển và bảo trì mô hình ML (Economic Cost of ML Model Development and Retraining)

#### 7.6.1. Cơ cấu chi phí vòng đời: Đầu tư ban đầu và vận hành duy trì
- Yêu cầu nguồn lực phát triển hệ thống ML: Xây dựng mô hình MBR cấp công nghiệp đòi hỏi nguồn lực lớn. Doanh nghiệp phải đầu tư vào hạ tầng dữ liệu, chuyên gia và máy chủ tính toán.
- Chi phí phát triển ban đầu (Initial Development Costs):
  - Khảo sát và chuẩn hóa hệ thống cảm biến: Chi phí kiểm định thiết bị đo và cải tạo hệ thống SCADA.
  - Làm sạch dữ liệu lịch sử SCADA: Quá trình chuẩn hóa cơ sở dữ liệu quá khứ thường tiêu tốn nhiều tháng nhân công.
  - Lập trình mô hình và kiểm định chéo: Kinh phí dành cho các chu kỳ đào tạo và kiểm định thuật toán.
  - Hồ sơ pháp lý phê duyệt thay đổi quy trình: Chi phí hoàn thiện thủ tục đánh giá an toàn và tác động môi trường.
- Chi phí vận hành thường xuyên (Ongoing Maintenance Costs):
  - Tái huấn luyện mô hình định kỳ (Periodic Retraining): Nhu cầu tái huấn luyện phát sinh liên tục trong thực tế. Quá trình này bắt buộc khi tính chất nước thay đổi, thay màng hoặc đổi cấu hình trạm.
  - Thiết bị điện toán biên (Edge Computing Hardware): Chi phí khấu hao và bảo trì phần cứng xử lý tại trạm.
  - Bảo mật thông tin và an toàn mạng IT: Chi phí duy trì bản quyền phần mềm và ngăn ngừa xâm nhập.
  - Đào tạo liên tục cho kỹ thuật viên: Kinh phí nâng cao kỹ năng cho đội ngũ vận hành nhà máy.

#### 7.6.2. Nhu cầu phân tích chi phí - lợi ích định lượng đối với đơn vị vận hành
- Thiếu hụt báo cáo tài chính trong nghiên cứu: Các bài báo khoa học hiện nay hầu như không công bố chi phí phát triển và bảo trì hệ thống ML.
- Khoảng trống thông tin kinh tế: Chưa có nghiên cứu bình duyệt nào công bố bảng phân tích chi phí - lợi ích (cost-benefit analysis). Báo cáo toàn diện cho trạm MBR ứng dụng ML vẫn chưa xuất hiện.
- Khó khăn trong việc ra quyết định đầu tư: Đơn vị quản lý nước thiếu cơ sở đánh giá tính khả thi kinh tế. Họ không thể so sánh chi phí giữa ML và điều khiển cổ điển.
- Yêu cầu chuẩn mực cho nghiên cứu tương lai: Nghiên cứu tương lai cần công bố chi phí phát triển, kiểm định và bảo trì hàng năm. Các số liệu tài chính này phải đi kèm chỉ số ^2$, $	ext{RMSE}$ hay $	ext{MAPE}$.
- Khuyến nghị đánh giá tiền khả thi: Doanh nghiệp cần thực hiện đánh giá tiền khả thi chi tiết theo từng cơ sở. Bước đánh giá này phải hoàn thành trước khi đầu tư hệ thống ML.

---

### 7.7. Khoảng trống 7: Yêu cầu về nguồn nhân lực vận hành hệ thống DT và XAI (Human Capital and Workforce Requirements)

#### 7.7.1. Sự thiếu hụt nhân lực liên ngành MLOps và kỹ thuật xử lý nước
- Đòi hỏi kỹ năng chuyên môn phức hợp: Hệ thống Bản sao số Cấp II và III đòi hỏi kỹ năng phức hợp. Kỹ sư phải thành thạo kỹ thuật dữ liệu, MLOps và điều khiển quá trình.
- Thực trạng thiếu hụt kỹ sư kép trong ngành nước: Đa số đơn vị cấp thoát nước thiếu đội ngũ kỹ sư chuyên môn kép. Họ không có nhân sự am hiểu đồng thời công nghệ vi sinh và AI.
- Rào cản chuyển giao công nghệ do nhân lực: Khoảng cách ứng dụng thực tiễn bắt nguồn từ sự thiếu hụt nhân lực. Đây là rào cản về lực lượng lao động, không chỉ là rào cản công nghệ.
- Nguy cơ phụ thuộc nhà thầu ngoài: Thiếu năng lực nội bộ khiến trạm nước phụ thuộc nhà thầu phần mềm ngoài. Tình trạng này làm tăng chi phí và gây rủi ro vận hành.

#### 7.7.2. Định lượng nhu cầu nhân sự và xây dựng chương trình đào tạo
- Trách nhiệm công bố thông số nhân sự trong nghiên cứu: Nghiên cứu DT cần nêu rõ định biên nhân sự tối thiểu. Báo cáo phải mô tả chi tiết yêu cầu kỹ năng của kỹ thuật viên vận hành.
- Xây dựng mô đun đào tạo tương tác người - máy: Nhà phát triển cần thiết kế giao diện XAI trực quan. Giao diện này giúp công nhân vận hành hiểu rõ căn cứ ra quyết định của thuật toán.
- Thiết lập chương trình đào tạo chuyển đổi nghề nghiệp: Viện nghiên cứu và doanh nghiệp cần tổ chức các khóa bồi dưỡng MLOps. Chương trình đào tạo tập trung vào ứng dụng thực tế cho kỹ sư môi trường.
- Chuẩn hóa quy trình vận hành tiêu chuẩn (SOP): Đơn vị vận hành cần chuẩn hóa quy trình can thiệp thủ công (SOP). Tài liệu hướng dẫn xử lý khi hệ thống AI đưa ra quyết định sai lệch.

---

### 7.8. Khoảng trống 8: Thiếu đối chuẩn hệ thống với các phương pháp điều khiển phi-ML (Inadequate Baselines and Benchmarking against Non-ML Alternatives)

#### 7.8.1. Thực trạng đối chuẩn thiếu khách quan trong các nghiên cứu học máy
- Vị thế của các bộ điều khiển kinh điển: Bộ điều khiển PID và điều khiển mờ (Fuzzy Logic) rất phổ biến trong trạm MBR. Các thiết bị này có chi phí lắp đặt thấp và độ tin cậy đã chứng minh.
- Thiếu hụt đường cơ sở so sánh tương đương: Rất ít nghiên cứu ML so sánh đối chuẩn với bộ điều khiển PID hoặc Fuzzy Logic. Thực nghiệm đối chứng trong cùng điều kiện vận hành còn hiếm hoi.
- Thiên lệch trong việc chọn mốc so sánh: Tác giả thường so sánh mô hình ML với vận hành thủ công không tối ưu. Một số nghiên cứu chỉ so sánh với mô hình hồi quy tuyến tính thô sơ.
- Thiếu định lượng giá trị gia tăng thực chất: Thiếu mốc so chuẩn tiên tiến khiến ngành nước khó đánh giá công nghệ. Nhà máy không thể định lượng lợi ích gia tăng thực tế từ thuật toán ML.
- Bỏ qua các thuật toán điều khiển dự báo dựa trên mô hình cơ chế (Mechanistic MPC): Bộ điều khiển MPC cơ chế dựa trên mô hình bùn hoạt tính ASM đạt hiệu quả cao. Tuy nhiên, các bài báo ML hiếm khi so sánh với công nghệ này.

#### 7.8.2. Quy định bắt buộc tích hợp PID và Fuzzy Logic làm đường cơ sở đối chứng
- Tiêu chuẩn hóa phương pháp đánh giá: Nghiên cứu tương lai phải đưa PID tinh chỉnh và Fuzzy Logic làm đường cơ sở. Đây là yêu cầu bắt buộc khi công bố hiệu năng thuật toán mới.
- Đánh giá toàn diện đa tiêu chí: Nghiên cứu cần so sánh thuật toán ML với điều khiển cổ điển qua nhiều chỉ tiêu. Các tiêu chí gồm mức giảm TMP, độ ổn định dòng thấm, điện năng và tuổi thọ màng.
- Định vị miền ứng dụng tối ưu của ML: Bài báo cần xác định rõ miền làm việc tối ưu của ML. Phân tích phải chỉ ra các kịch bản mà ML vượt trội so với vòng lặp phản hồi kín.
- Phối hợp lai ghép giữa điều khiển cổ điển và AI: Các tác giả nên kết hợp cấu trúc lai giữa điều khiển cổ điển và AI. Mạng nơ-ron đóng vai trò bù sai số hoặc tinh chỉnh động $, $, $ cho bộ PID.

---

### 7.9. Khoảng trống 9: Dấu chân carbon và tiêu hao năng lượng tính toán của AI (Carbon and Computational Energy Footprint of AI)

#### 7.9.1. Gánh nặng tiêu thụ điện năng từ huấn luyện mô hình sâu và suy luận biên
- Tiêu hao năng lượng trong giai đoạn huấn luyện: Huấn luyện mô hình sâu như LSTM hoặc Transformer tiêu tốn nhiều điện năng. Quá trình xử lý các tập dữ liệu SCADA khổng lồ tạo ra phát thải lớn.
- Tiêu hao năng lượng trong giai đoạn suy luận liên tục: Hoạt động suy luận thời gian thực trên phần cứng biên (Edge AI) tiêu thụ điện liên tục. Thiết bị tại trạm đòi hỏi nguồn năng lượng 24/7.
- Nghịch lý môi trường của AI trong ngành xử lý nước: Mục tiêu của MBR thông minh là tiết kiệm năng lượng và giảm phát thải. Dấu chân carbon của phần cứng AI có thể làm triệt tiêu lợi ích môi trường này.
- Tác động nhiệt và làm mát trung tâm dữ liệu: Nhu cầu tản nhiệt cho các cụm máy chủ phân tích dữ liệu cục bộ góp phần gia tăng phát thải gián tiếp.

#### 7.9.2. Minh bạch hóa năng lượng tính toán để bảo toàn mục tiêu giảm phát thải của MBR
- Đo lường và báo cáo điện năng tính toán: Nghiên cứu MBR ứng dụng AI cần công bố điện năng huấn luyện mô hình. Tác giả cũng phải đo lường năng lượng tiêu hao trên mỗi lượt dự đoán (kWh/prediction).
- Đánh giá cân bằng năng lượng thực (Net Energy Balance): Nghiên cứu cần lập phương trình cân bằng năng lượng thực tế. Phương trình so sánh điện năng sục khí tiết kiệm với điện năng hệ thống AI tiêu thụ:
  $$\Delta E_{\text{net}} = E_{\text{saved, aeration}} - (E_{\text{train}} + E_{\text{inference}} + E_{\text{infrastructure}})$$
- Phát triển mô hình học máy tiết kiệm năng lượng (Green AI): Kỹ sư cần ưu tiên giải pháp học máy xanh (Green AI). Các kỹ thuật gồm lượng tử hóa mô hình (quantization) và cắt tỉa trọng số (pruning) để giảm công suất tính.
- Đánh giá vòng đời phát thải (LCA) cho các giải pháp số: Đơn vị nghiên cứu cần đưa hạ tầng công nghệ vào đánh giá vòng đời (LCA). Phương pháp này lượng hóa toàn diện phát thải của nhà máy MBR thông minh.
