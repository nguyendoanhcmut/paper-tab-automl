## Chương 5: Tối ưu hóa Năng lượng Tiêu thụ trong Hệ thống MBR bằng Học máy

### 5.1 Cấu trúc tiêu thụ năng lượng và Mục tiêu tối ưu hóa

#### 5.1.1 Suất tiêu hao năng lượng riêng (SEC) và Cấu trúc chi phí vận hành
- Chi phí năng lượng trong vận hành MBR:
  - Chi phí điện năng là khoản chi phí vận hành (OPEX) lớn nhất trong hệ thống MBR, chỉ đứng sau chi phí thay màng định kỳ.
  - Quá trình sục khí tiêu thụ phần lớn điện năng của toàn bộ trạm xử lý.
- Dải giá trị suất tiêu hao năng lượng riêng (SEC - Specific Energy Consumption):
  - Suất tiêu hao năng lượng riêng biểu thị lượng điện năng tiêu thụ trên một đơn vị thể tích nước xử lý ($\text{kWh/m}^3$).
  - Hệ thống MBR tiêu thụ điện năng tổng cộng trong khoảng $0.4\text{--}1.5\text{ kWh/m}^3$.
  - Mức tiêu thụ năng lượng trung bình của trạm MBR điển hình dao động trong khoảng $0.8\text{--}1.1\text{ kWh/m}^3$ [15].
  - Mức tiêu hao năng lượng của MBR cao gấp $2\text{--}3\text{ lần}$ so với công nghệ bùn hoạt tính truyền thống (CAS - Conventional Activated Sludge).
  - Trạm xử lý bằng công nghệ CAS truyền thống chỉ tiêu thụ khoảng $0.3\text{--}0.6\text{ kWh/m}^3$.
- Biến thiên năng lượng theo cấu hình trạm và tính chất nước thải:
  - Khảo sát thực nghiệm của Germain và cộng sự [57] chỉ ra nhu cầu năng lượng riêng biến động lớn giữa các cấu hình MBR khác nhau.
  - Đánh giá đối chuẩn (benchmarking) giữa các trạm đòi hỏi phải chuẩn hóa cẩn thận theo độ mạnh của nước thải đầu vào (influent strength) và các mục tiêu chất lượng xử lý [57].
  - Các yếu tố chính chi phối phân bố SEC gồm chiến lược điều khiển sục khí, điểm đặt thông lượng màng ($J$) và khả năng lắng của bùn hoạt tính [15].

#### 5.1.2 Phân bổ các thành phần năng lượng trong trạm MBR
- Tỷ trọng tiêu thụ điện năng giữa các phân hệ thiết bị:
  - Sục khí màng (thổi bọt khí thô cọ rửa bề mặt màng): Chiếm $60\%\text{--}75\%$ tổng điện năng tiêu thụ của toàn bộ trạm MBR.
  - Sục khí sinh học (thổi bọt khí mịn cấp oxy hòa tan cho vi sinh vật hiếu khí): Chiếm $15\%\text{--}20\%$ tổng điện năng tiêu thụ.
  - Hệ thống bơm hút màng (bơm thấm qua màng) và bơm bùn tuần hoàn: Chiếm $10\%\text{--}15\%$ tổng điện năng tiêu thụ.
- Bằng chứng kiểm chuẩn mô hình cơ chế từ Verrecht và cộng sự [56]:
  - Tác giả xây dựng mô hình năng lượng cơ chế và kiểm chuẩn trên hai trạm MBR quy mô thực tế.
  - Kết quả xác định tổng năng lượng dành cho sục khí cọ rửa màng kết hợp sục khí xử lý sinh học tiêu tốn từ $0.4\text{--}0.8\text{ kWh/m}^3$.
  - Sục khí cọ rửa cơ học nhằm hạn chế phân cực nồng độ và bám cặn chiếm tỷ trọng áp đảo trong tổng nhu cầu sục khí.

#### 5.1.3 Các chiến lược điều khiển sục khí truyền thống và Giới hạn kỹ thuật
- Điều khiển lưu lượng khí theo điểm đặt cố định (Fixed air flow rate setpoints):
  - Kỹ sư xác định các điểm đặt lưu lượng khí cố định trong các thử nghiệm vận hành ban đầu (commissioning trials).
  - Máy thổi khí duy trì tốc độ sục khí cọ rửa màng ở mức thiết kế cực đại liên tục trong suốt quá trình vận hành.
  - Chế độ cố định không xét đến điều kiện tắc nghẽn thực tế trên bề mặt màng.
  - Trạm gặp tình trạng sục khí dư thừa liên tục (systematic over-aeration), gây lãng phí năng lượng lớn trong các giai đoạn màng còn sạch (ngay sau chu kỳ rửa ngược hoặc sau khi tẩy rửa hóa chất CIP).
- Điều khiển hồi tiếp tích phân tỷ lệ (PI) theo oxy hòa tan ($DO$ feedback control):
  - Bộ điều khiển PI điều chỉnh tốc độ cấp khí sinh học dựa trên giá trị nồng độ oxy hòa tan ($DO$) đo trực tuyến.
  - Cơ chế này nâng cao hiệu quả sử dụng năng lượng của hệ thống sục khí sinh học bọt mịn.
  - Cơ chế không quản lý và không điều khiển trực tiếp hệ thống sục khí bọt thô cọ rửa màng.
  - Thành phần tiêu thụ năng lượng lớn nhất (sục khí màng, chiếm $60\%\text{--}75\%$) tiếp tục hoạt động ở chế độ điều khiển vòng hở (open-loop control) [36].
- Các phương thức tiết giảm năng lượng cơ học thông thường:
  - Sục khí ngắt quãng (Intermittent aeration): Vận hành máy thổi khí luân phiên theo chu kỳ thời gian cố định (ví dụ chu kỳ $10\text{ s}$ bật / $10\text{ s}$ tắt).
  - Kiểm soát tỷ lệ sục khí riêng: Theo dõi tỷ lệ sục khí trên diện tích màng ($SAD_m$, $\text{m}^3/(\text{m}^2\cdot\text{h})$) hoặc tỷ lệ sục khí trên thể tích nước thấm thu hồi ($SAD_p$, $\text{m}^3_{\text{air}}/\text{m}^3_{\text{permeate}}$).
  - Giới hạn vận hành: Các chu kỳ bật tắt cố định không thích ứng kịp thời với biến động tải lượng hữu cơ, biến động lưu lượng bùn và sự hình thành lớp bánh cặn bất thường.

#### 5.1.4 Cân bằng động đa mục tiêu và Vai trò của Học máy (ML)
- Bản chất động học phi tuyến của quá trình cọ rửa màng:
  - Tốc độ sục khí cọ rửa tối ưu không phải là một thông số vận hành cố định [58].
  - Nhu cầu sục khí cọ rửa tối ưu phụ thuộc đồng thời vào trạng thái tắc nghẽn hiện tại (chiều dày và độ nén của lớp bánh cặn), độ nhớt của bùn lỏng (mixed-liquor viscosity), điểm đặt thông lượng màng ($J$) và tuổi thọ màng.
  - Các cảm biến chuẩn của mạng SCADA nhà máy không thể đo trực tiếp các đại lượng này theo thời gian thực [58].
- Bài toán đánh đổi đa mục tiêu (Trade-off):
  - Mục tiêu 1: Giảm tối đa lưu lượng thổi khí để cắt giảm chi phí điện năng vận hành máy thổi.
  - Mục tiêu 2: Duy trì ứng suất cắt thủy lực đủ mạnh để ngăn chặn các chất bẩn bám dính và giữ áp suất qua màng ($TMP$) dưới ngưỡng tới hạn.
  - Nguy cơ đánh đổi: Việc cắt giảm sục khí cọ rửa quá mức làm gia tăng tốc độ tích tụ hạt bùn và polymer ngoại bào (EPS/SMP), gây hiện tượng vọt áp $TMP$ đột ngột, làm giảm tuổi thọ màng sợi rỗng/tấm phẳng và tăng vọt chi phí hóa chất tẩy rửa CIP.
- Vai trò và Trường hợp ứng dụng tự nhiên của Học máy (ML-based aeration optimization):
  - Mô hình ML tiếp nhận luồng dữ liệu liên tục từ các cảm biến SCADA trực tuyến ($TMP$, lưu lượng thấm, $DO$, nhiệt độ, độ đục).
  - Mô hình ML dự báo chính xác tốc độ sục khí cọ rửa tối thiểu cần thiết để duy trì $TMP$ dưới ngưỡng tắc nghẽn tới hạn trong điều kiện vận hành hiện tại.
  - Mô hình cho phép điều chỉnh động lưu lượng khí: Giảm sục khí khi điều kiện vận hành thuận lợi và tự động tăng sục khí khi phát hiện nguy cơ tắc nghẽn gia tăng.
  - Kiến trúc ML cung cấp năng lực ánh xạ phi tuyến, đa biến phức tạp mà các phương pháp giải tích truyền thống không thể đáp ứng [17, 38].

---

### 5.2 Bằng chứng thực nghiệm về giảm tiêu hao năng lượng và Khoảng trống nghiên cứu

#### 5.2.1 Phân định ranh giới giữa Điều khiển cơ chế (ASM) và Điều khiển học máy (ML)
- Cảnh báo về sự nhầm lẫn kỹ thuật trong y văn:
  - Nhiều tài liệu nghiên cứu đánh đồng kết quả tiết kiệm năng lượng của mô hình cơ chế sinh hóa với mô hình dữ liệu học máy.
  - Sự đánh đồng này dẫn đến việc phóng đại mức độ sẵn sàng và trưởng thành thực tế của công nghệ học máy trong tối ưu hóa năng lượng MBR.
- Hai trường phái điều khiển năng lượng riêng biệt:
  - Trường phái 1 - Điều khiển cơ chế dựa trên mô hình bùn hoạt tính (ASM-based mechanistic control): Sử dụng các phương trình vi phân mô tả quá trình chuyển hóa sinh học (mô hình ASM1 hoặc ASM2d) kết hợp với thuật toán hồi tiếp tỷ lệ tích phân (PI).
  - Trường phái 2 - Điều khiển dựa trên dữ liệu học máy (ML-based data-driven control): Sử dụng các thuật toán học máy huấn luyện trên dữ liệu quá khứ và thời gian thực để dự báo và tối thiểu hóa nhu cầu năng lượng.
- Phân nhóm kết quả tiết kiệm năng lượng trong y văn MBR:
  - Nhóm kết quả 1: Mức tiết kiệm năng lượng đã xác thực thực nghiệm (Validated energy savings) đo đạc trực tiếp tại các nhà máy đang vận hành ở quy mô thực tế bằng chiến lược điều khiển cơ chế hoặc điều khiển hồi tiếp.
  - Nhóm kết quả 2: Mức tiết kiệm dự phóng (Projected savings) công bố trong các nghiên cứu mô phỏng số hoặc các thử nghiệm điều khiển ở quy mô pilot, nơi thuật toán và điều kiện biên thay đổi giữa các bài báo và kết quả tiết kiệm không trực tiếp đến từ thuật toán ML.

#### 5.2.2 Bằng chứng thực nghiệm điển hình từ các công trình nghiên cứu
- Công trình thực nghiệm điển hình của Sun và cộng sự (Sun et al., 2016) [59]:
  - Quy mô triển khai: Trạm xử lý nước thải MBR quy mô công nghiệp thực tế (Full-scale operational plant).
  - Phương pháp điều khiển: Mô phỏng mô hình bùn hoạt tính (ASM) kết hợp bộ điều khiển hồi tiếp tỷ lệ tích phân (ASM + PI feedback control) cho hệ thống sục khí.
  - Cơ chế vận hành: Mô hình ASM dự báo nhu cầu oxy vi sinh theo thời gian thực để tự động điều chỉnh điểm đặt sục khí sinh học.
  - Kết quả định lượng: Đạt mức giảm $20\%$ nhu cầu năng lượng sục khí của máy thổi khí.
  - Suất tiêu hao năng lượng: Hạ mức tiêu thụ năng lượng riêng toàn trạm xuống còn $0.45\text{ kWh/m}^3$.
  - Mốc đối chuẩn so sánh: Thấp hơn đáng kể so với mức cơ sở quy mô pilot $0.73\text{ kWh/m}^3$ do Verrecht và cộng sự thiết lập [14].
  - Ranh giới kỹ thuật then chốt: Thuật toán điều khiển của Sun et al. là điều khiển PI dựa trên mô hình cơ chế ASM, không phải là mô hình học máy (ML). Mức giảm $20\%$ năng lượng sục khí là mốc chuẩn xác thực cho điều khiển dựa trên mô hình cơ chế chứ không phải minh chứng riêng cho thuật toán ML.
- Nghiên cứu mô phỏng chuẩn BSM-MBR của Verrecht và cộng sự (Verrecht et al., 2010) [14]:
  - Nền tảng thử nghiệm: Mô hình mô phỏng chuẩn Benchmark Simulation Model cho MBR (BSM-MBR).
  - Phương pháp: Tối ưu hóa kịch bản vận hành trên nền tảng mô hình ASM (ASM scenario optimization).
  - Cơ chế tác động: Tinh chỉnh thời gian lưu bùn (SRT) và lưu lượng bùn tuần hoàn nội bộ.
  - Kết quả: Xác lập mốc tiêu thụ năng lượng riêng cơ sở quy mô pilot là $0.73\text{ kWh/m}^3$.
- Dải tiết kiệm năng lượng công bố trong các nghiên cứu mô phỏng:
  - Các công trình nghiên cứu mô phỏng và tối ưu hóa thiết kế MBR báo cáo mức giảm điện năng lý thuyết trong khoảng $15\%\text{--}35\%$ (hoặc phổ biến trong dải $15\%\text{--}25\%+$).
  - Các kết quả này phần lớn xuất phát từ mô phỏng số hoặc quy mô pilot với các thuật toán biến thiên, chưa chứng minh được sự đóng góp riêng biệt của ML trên hiện trường.

#### 5.2.3 Bảng tổng hợp các nghiên cứu tối ưu hóa năng lượng trong MBR (Bảng 3)
- Bảng tổng hợp các mốc chuẩn suất tiêu hao năng lượng và bằng chứng tối ưu hóa thực nghiệm (Tổng hợp từ Table 4 trong bài báo gốc):

| Quy mô nghiên cứu (Scale) | Phương pháp tiếp cận / Điều khiển (Method) | Phát hiện chính và Cơ chế vận hành (Key Finding) | Chỉ số năng lượng đã xác thực (Confirmed Energy Metric) | Tài liệu trích dẫn (Reference) |
| :--- | :--- | :--- | :--- | :--- |
| Quy mô thực tế (Full-scale) | Mô hình năng lượng cơ chế (Mechanistic energy model) | Mô hình được kiểm chuẩn thực nghiệm với sai số nằm trong phạm vi $20\%$ trên tất cả các thông số vận hành của nhà máy. | Năng lượng sục khí tiêu thụ: $0.4\text{--}0.8\text{ kWh/m}^3$ | Verrecht et al. [56] |
| Mô phỏng chuẩn BSM-MBR (BSM-MBR simulation) | Tối ưu hóa kịch bản mô hình ASM (ASM scenario optimization) | Giảm tiêu hao năng lượng vận hành bằng cách tinh chỉnh điểm đặt thời gian lưu bùn (SRT) và lưu lượng dòng tuần hoàn bùn nội bộ. | Mốc đối chuẩn quy mô pilot: $0.73\text{ kWh/m}^3$ | Verrecht et al. [14] |
| Đa trạm quy mô thực tế (Multiple full-scale) | Khảo sát thực nghiệm diện rộng (Empirical survey) | Phân tích đối chuẩn chi tiết trên nhiều trạm MBR thương mại hoạt động trong các điều kiện tải trọng và cấu hình khác nhau. | Dải tiêu thụ năng lượng điển hình: $0.8\text{--}1.1\text{ kWh/m}^3$ | Krzeminski et al. [15] |
| Quy mô thực tế (Full-scale) | Điều khiển hồi tiếp tích phân tỷ lệ dựa trên ASM (ASM + PI feedback control) | Điều khiển sục khí động học dựa trên dự báo nhu cầu oxy của mô hình ASM giúp giảm tải cho hệ thống máy thổi khí mà vẫn bảo đảm hiệu quả nitrat hóa. | Tổng tiêu thụ: $0.45\text{ kWh/m}^3$ (Giảm $20\%$ năng lượng sục khí máy thổi) | Sun et al. [59] |

- Phân tích tương quan giữa biến điều khiển và nguy cơ tắc nghẽn màng:
  - Các biến điều khiển chủ yếu trong các nghiên cứu gồm lưu lượng máy thổi khí sục màng ($Q_{air}$), lưu lượng sục khí sinh học, chu kỳ sục khí ngắt quãng và tỷ lệ bùn tuần hoàn ($Q_r$).
  - Mọi chiến lược giảm công suất máy thổi cọ rửa màng đều làm suy giảm ứng suất cắt bề mặt màng. Điều này đòi hỏi thuật toán điều khiển phải giám sát liên tục tốc độ gia tăng áp suất $\text{d}TMP/\text{d}t$ để tự động can thiệp sục khí bù trước khi xảy ra tắc nghẽn nghiêm trọng không thể phục hồi.

#### 5.2.4 Phân định ranh giới then chốt và Khoảng trống nghiên cứu thực tế
- Sự chênh lệch giữa tiềm năng mô phỏng và thực tế nhà máy:
  - Tiềm năng giảm năng lượng $15\%\text{--}35\%$ chủ yếu tồn tại trong môi trường mô phỏng toán học lý tưởng với giả định điều kiện biên không đổi.
  - Trạm xử lý thực tế đối mặt với biến động lưu lượng lớn, dao động thành phần chất ô nhiễm theo giờ, hiện tượng trôi dạt cảm biến và độ trễ phản hồi cơ học của hệ thống đường ống và máy thổi.
- Thực trạng thiếu vắng kiểm chứng học máy vòng kín quy mô thương mại:
  - Số lượng nghiên cứu ứng dụng ML chuyên sâu vào tối ưu hóa nhu cầu sục khí MBR hiện vẫn còn rất khan hiếm trong y văn học thuật.
  - Chưa có nghiên cứu bình duyệt nào chứng minh được con số tiết kiệm năng lượng định lượng đến từ một thuật toán điều khiển ML triển khai trực tiếp tại nhà máy MBR quy mô thực tế.
  - Kết quả giảm $20\%$ của Sun et al. hoàn toàn dựa trên thuật toán điều khiển hồi tiếp PI tích hợp mô hình cơ chế ASM, không phải là kết quả của thuật toán ML độc lập.
- Các định hướng nghiên cứu ưu tiên cấp bách:
  - Phát triển và xác thực mô hình tối ưu hóa sục khí động học dựa trên ML kết nối trực tiếp với luồng dữ liệu SCADA thời gian thực.
  - Triển khai các thử nghiệm điều khiển vòng kín (Closed-loop control) dài hạn trên các trạm MBR quy mô công nghiệp thực tế.
  - Thiết lập quy trình hạch toán và kiểm toán năng lượng độc lập, minh bạch và nghiêm ngặt để đo lường chính xác hiệu quả năng lượng thực tế do thuật toán ML mang lại.
- Cầu nối tích hợp sang kiến trúc Bản sao số (Digital Twin):
  - Giải quyết đồng thời bài toán dự đoán tắc nghẽn màng và bài toán tối ưu hóa năng lượng ở quy mô vận hành thực tế đòi hỏi một khung kiến trúc hợp nhất.
  - Khung kiến trúc cần kết hợp năng lực dự báo của mô hình ML, tính minh bạch kiểm toán của công cụ XAI và các quy luật động học của mô hình cơ chế ASM thành một công cụ vận hành cập nhật liên tục.
  - Công nghệ Bản sao số (Digital Twin) cung cấp tầng tích hợp kỹ thuật này để chuyển đổi từ giám sát bị động sang điều khiển tối ưu tự trị vòng kín (chuyển tiếp sang Chương 6).
