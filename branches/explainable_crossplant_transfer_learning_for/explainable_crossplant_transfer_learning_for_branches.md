---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Học chuyển giao giải thích được giữa các trạm để dự báo bám bẩn màng trong các bể phản ứng sinh học màng (MBR) quy mô pilot hạn chế dữ liệu

## Tóm tắt tổng quan (Abstract)

- **Vấn đề bám bẩn và nhu cầu dự báo áp suất xuyên màng ($TMP$):**
  - Quá trình bám bẩn màng làm tăng trở lực lọc và làm tăng áp suất xuyên màng ($TMP$) trong chế độ vận hành duy trì lưu lượng không đổi (constant-flux operation).
  - Dự báo chính xác diễn biến bám bẩn màng là điều kiện tiên quyết để thực hiện điều khiển chuyển tiếp (feedforward control) và vận hành tiết kiệm năng lượng trong các bể phản ứng sinh học màng (MBR).
  - Việc phát triển mô hình tin cậy tại các trạm nghèo dữ liệu (data-limited plants) gặp trở ngại lớn do thiếu hụt các phép đo định kỳ về chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP).

- **Khung học chuyển giao liên trạm giải thích được (Explainable Cross-Plant Transfer Learning Framework):**
  - Nghiên cứu thiết lập một khung học chuyển giao liên trạm có khả năng giải thích nhằm dự báo $TMP$ cho các hệ MBR quy mô pilot khan hiếm dữ liệu.
  - Hai kiến trúc mô hình cơ sở gồm mạng nơ-ron hồi quy có nhớ dài-ngắn (LSTM) và cây tăng cường độ dốc cực đại (XGBoost).
  - Mô hình cơ sở được tiền huấn luyện (pretrained) trên tập dữ liệu đa nguồn từ 3 trạm MBR xử lý nước thải sinh hoạt giàu dữ liệu hơn (data-richer source MBRs).
  - Sau đó, mô hình cơ sở được tinh chỉnh (fine-tuned) bằng một lượng dữ liệu hạn chế từ một trạm đích (domestic target plant) xử lý nước thải sinh hoạt.

- **Hiệu năng định lượng của mô hình cơ sở và hạn chế khi chuyển giao trực tiếp:**
  - Mô hình cơ sở dự báo tốt $TMP$ trên miền dữ liệu nguồn: LSTM đạt hệ số xác định $R^2 = 0.87$ và XGBoost đạt $R^2 = 0.86$.
  - Kỹ thuật SHAP (SHapley Additive exPlanations) xác định cacbohydrat trong EPS (EPSc), protein trong EPS (EPSp) và protein trong SMP (SMPp) là các tác nhân chi phối chính đối với quá trình bám bẩn.
  - Chuyển giao trực tiếp (direct transfer mà không tinh chỉnh) sang trạm đích cho độ chính xác rất thấp ($R^2 = 0.39\text{--}0.41$).
  - Kết quả này chứng minh các mô hình cơ sở nguồn chưa thể nắm bắt trọn vẹn đặc tính bám bẩn riêng biệt của trạm đích.

- **Hiệu quả vượt trội của quá trình tinh chỉnh (Fine-Tuning):**
  - Quá trình tinh chỉnh cải thiện rõ rệt độ chính xác dự báo bám bẩn.
  - Mô hình LSTM tinh chỉnh (LSTM-FT) đạt độ chính xác cao $R^2 = 0.89$ khi chỉ cần dùng tỷ lệ dữ liệu tinh chỉnh $40\%$ ($40\%$ fine-tuning ratio) từ trạm đích.

- **Phát hiện cơ chế thông qua giải thích AI và phân tích hóa lý:**
  - Phân tích SHAP kết hợp với phân tích loại trừ từng đặc trưng (Leave-One-Feature-Out - LOFO) chỉ ra cơ chế chuyển dịch tín hiệu bám bẩn.
  - Phân đoạn EPSc duy trì vai trò là tín hiệu bám bẩn có thể chuyển giao cốt lõi (critical transferable fouling signal) giữa các trạm.
  - Phân đoạn EPSp tăng mạnh mức độ quan trọng sau khi mô hình trải qua bước tinh chỉnh.
  - Sự thay đổi này phản ánh con đường bám bẩn liên kết với EPSp do nước thải đầu vào của trạm đích chứa nồng độ sắt cao (Fe-enriched influent).

- **Xác thực mở rộng trên hệ nước thải công nghiệp:**
  - Khung phương pháp tiếp tục được kiểm chứng tại một trạm MBR quy mô pilot xử lý nước thải công nghiệp.
  - Mô hình LSTM-FT đạt hiệu năng ấn tượng với $R^2 \approx 0.90$.
  - Tại trạm công nghiệp này, phân đoạn SMPp nổi lên thành đặc trưng bám bẩn quan trọng nhất.

- **Ý nghĩa khoa học và thực tiễn:**
  - Khung học chuyển giao bảo tồn hiệu quả các thông tin bám bẩn chung do EPS làm trung tâm.
  - Đồng thời, mô hình tự động tái hiệu chuẩn các tác nhân đặc thù theo từng công trình.
  - Phương pháp mở ra giải pháp thực tiễn để xây dựng mô hình dự báo bám bẩn dựa trên cơ chế tại các trạm MBR thiếu hụt dữ liệu đo đạc.


## 1. Giới thiệu (Introduction)

### 1.1 Các vấn đề bám bẩn màng và chi phí vận hành MBR (Membrane fouling challenges and operational costs)

- **Động lực phát triển công nghệ xử lý nước tiên tiến:**
  - Quá trình đô thị hóa nhanh và nhu cầu tái sử dụng nước ngày càng tăng thúc đẩy ngành xử lý nước thải hướng tới các quy trình tăng cường [1].
  - Các hệ thống xử lý cần tạo ra nước sau xử lý đạt chất lượng cao và ổn định trong phạm vi diện tích xây dựng hạn chế.
  - Bể phản ứng sinh học màng (MBR) tích hợp quá trình phân hủy sinh học với kỹ thuật tách màng lọc, đáp ứng tốt các yêu cầu khắt khe này.
  - MBR được triển khai rộng rãi cho cả xử lý nước thải sinh hoạt và nước thải công nghiệp nhờ chất lượng nước đầu ra vượt trội và thiết kế nhỏ gọn.

- **Hiện tượng bám bẩn màng (Membrane Fouling) và áp suất xuyên màng ($TMP$):**
  - Hiện tượng bám bẩn màng vẫn là trở ngại hàng đầu cản trở việc phát huy tối đa các ưu điểm của MBR [2].
  - Dưới chế độ vận hành duy trì lưu lượng thấm không đổi (constant-flux operation), chất bám bẩn tích tụ dần trên bề mặt và trong lỗ màng.
  - Sự tích tụ này làm gia tăng liên tục trở lực lọc của màng.
  - Trở lực lọc gia tăng được phản ánh trực tiếp qua sự gia tăng của áp suất xuyên màng ($TMP$) [3].

- **Hệ quả tiêu cực về năng lượng và chi phí vòng đời thiết bị:**
  - Sự gia tăng $TMP$ làm tăng nhu cầu sục khí để xáo trộn làm sạch bề mặt màng.
  - Năng lượng tiêu hao cho hệ thống bơm hút dòng thấm tăng lên tương ứng.
  - Tần suất tẩy rửa hóa học (chemical cleaning) tăng cao, làm đẩy nhanh quá trình lão hóa màng và làm hỏng cấu trúc vật liệu màng [3].
  - Chi phí vòng đời (lifecycle costs) của hệ thống bị đội lên đáng kể.
  - MBR thường tiêu thụ năng lượng cao hơn quy trình bùn hoạt tính truyền thống ($0.4\text{--}1.6\text{ kWh}\cdot\text{m}^{-3}$ so với $0.3\text{--}0.8\text{ kWh}\cdot\text{m}^{-3}$) [4].

- **Yêu cầu cấp bách về dự báo bám bẩn chủ động:**
  - Dự báo chính xác diễn biến bám bẩn màng và $TMP$ là yêu cầu cấp thiết để triển khai điều khiển chuyển tiếp (feedforward fouling control) [5,6].
  - Điều khiển chuyển tiếp giúp vận hành MBR ở mức tiêu thụ năng lượng thấp và ngăn chặn sự cố tắc màng đột ngột.
  - Mặc dù giới nghiên cứu đạt nhiều bước tiến trong xác định đặc tính và giảm thiểu bám bẩn, việc quản lý bám bẩn chủ động trong thực tế vẫn là bài toán rất khó khăn.

### 1.2 Hạn chế về dữ liệu sinh hóa tại các trạm quy mô pilot (Biochemical data limitations in pilot plants)

- **So sánh mô hình cơ chế và mô hình hướng dữ liệu:**
  - Mô hình cơ chế và mô hình lai sinh học - vật lý (mechanistic and hybrid biological-physical models) giúp tăng cường khả năng diễn giải bản chất quá trình.
  - Tuy nhiên, việc xác định hệ số tham số và tái hiệu chuẩn các mô hình cơ chế trong các trạm thực tế gặp rất nhiều trở ngại [7].
  - Các mô hình học máy (ML) và học sâu (DL) nổi lên thành giải pháp thay thế hiệu quả [7-9].
  - ML và DL có khả năng nắm bắt mạnh mẽ các mối quan hệ phi tuyến phức tạp giữa điều kiện vận hành, chất lượng nước và các thông số sinh khối bùn hoạt tính.

- **Đặc tính kiến trúc của các mô hình học máy trong dự báo bám bẩn:**
  - Các mô hình học máy dạng cây (tree-based ML models), đặc biệt là họ tăng cường độ dốc như Extreme Gradient Boosting (XGBoost), rất phù hợp với dữ liệu quá trình dạng bảng [8,9].
  - Mạng nơ-ron hồi quy học sâu, điển hình là mạng bộ nhớ dài-ngắn (LSTM), đặc biệt thích hợp cho dự báo bám bẩn màng [10-12].
  - Bản chất của bám bẩn màng là một quá trình tích lũy liên tục và phụ thuộc sâu sắc vào tiến trình lịch sử (cumulative and path-dependent process).
  - Quá trình này chịu sự điều khiển trực tiếp bởi các thay đổi theo thời gian của đặc tính bùn và điều kiện thủy động lực học [10-12].

- **Khiếm khuyết trong việc lựa chọn biến đầu vào của các mô hình hiện nay:**
  - Việc thiết kế biến đầu vào toàn diện và hợp lý là yếu tố quyết định để mô hình AI đạt độ chính xác cao [13].
  - Đa số mô hình dự báo $TMP$ hiện nay ở quy mô pilot và quy mô thực tế chỉ dựa vào các biến vận hành thông thường được giám sát định kỳ [14,15].
  - Các biến thông thường bao gồm: Nồng độ chất rắn lơ lửng trong hỗn hợp bùn (MLSS), nồng độ chất rắn lơ lửng dễ bay hơi (MLVSS), thời gian lưu thủy lực (HRT) và thời gian lưu bùn (SRT).
  - Những biến số thông thường này không đủ năng lực để theo dõi sát sao động thái bám bẩn màng [14,15].

- **Tầm quan trọng cơ chế của EPS và SMP đối với bám bẩn màng:**
  - Các chỉ thị sinh hóa mang tính cơ chế cao như chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP) thường bị thiếu hụt hoặc lấy mẫu rất thưa thớt tại các trạm pilot và quy mô lớn [15,16].
  - Đây là một thiếu sót nghiêm trọng trong thực hành mô hình hóa.
  - Nhiều nghiên cứu thực nghiệm khẳng định EPS và SMP quyết định trực tiếp đến xu hướng bám bẩn màng [17].
  - Các phân đoạn protein và polysacarit trong EPS/SMP điều khiển quá trình hình thành lớp bánh bùn (cake formation), độ nén của lớp bánh (compressibility) và hiện tượng tắc nghẽn lỗ màng (pore-blocking behavior) [17].
  - Axit humic và axit fulvic cũng tham gia thúc đẩy quá trình bám bẩn màng [18-20].
  - Việc đưa trực tiếp EPS và SMP vào tập đặc trưng đầu vào của mô hình là hoàn toàn có cơ sở khoa học, giúp nâng cao cả độ chính xác dự báo lẫn khả năng diễn giải cơ chế [11,12].

- **Thực trạng dữ liệu thưa thớt và hạn chế tại trạm pilot đơn lẻ:**
  - Các phép đo phân đoạn EPS và SMP thường rất thưa và không đều đặn theo thời gian.
  - Phép phân tích này hoàn toàn phụ thuộc vào xét nghiệm thủ công trong phòng thí nghiệm, chưa thể quan trắc tự động bằng cảm biến trực tuyến (online sensors).
  - Dữ liệu vận hành thực tế thường đi kèm giá trị thiếu hụt (missing values), sai số cảm biến (sensor errors) và các điểm ngoại lai (outliers) [21,22].
  - Những rào cản này khiến một trạm MBR nghèo dữ liệu không thể tự huấn luyện độc lập một mô hình dự báo chất lượng cao [21,22].
  - Phần lớn mô hình ML hiện có chỉ được xây dựng và kiểm chứng trên tập dữ liệu lịch sử dài hoặc dày đặc của riêng một trạm cụ thể.
  - Khả năng tổng quát hóa liên trạm (cross-plant generalizability) của các mô hình này dưới điều kiện dữ liệu hạn chế chưa từng được chứng minh thỏa đáng [7,8,23].

### 1.3 Giải pháp học chuyển giao liên trạm (Cross-Plant Transfer Learning)

- **Cơ sở tương đồng cơ chế giữa các trạm MBR:**
  - Các trạm MBR khác nhau đều chia sẻ các cơ chế bám bẩn nền tảng tương đương nhau.
  - Các cơ chế chung bao gồm: Sự tích lũy lớp bánh bùn, tắc nghẽn lỗ màng và sự đóng góp của các sản phẩm chuyển hóa vi sinh vật vào trở lực màng [17].
  - Sự tương đồng cơ chế này cho thấy khả năng tồn tại các mô hình có thể chuyển giao tri thức bám bẩn qua lại giữa các trạm MBR.

- **Học chuyển giao phá vỡ tình trạng cô lập dữ liệu (Data Silos):**
  - Học chuyển giao (Transfer Learning) cung cấp chiến lược hứa hẹn để giải quyết đồng thời bài toán khan hiếm dữ liệu và các đảo dữ liệu cô lập trong vận hành MBR [24,25].
  - Khung học chuyển giao hoạt động theo hai giai đoạn:
    1. Tiền huấn luyện mô hình cơ sở trên dữ liệu đa nguồn từ nhiều trạm MBR khác nhau để học mối quan hệ tổng quát giữa thông số vận hành, dấu hiệu EPS/SMP và động thái tăng $TMP$.
    2. Tinh chỉnh mô hình bằng một lượng nhỏ dữ liệu từ trạm MBR đích để học các động lực bám bẩn đặc thù của riêng trạm đích đó.

- **Những thách thức kỹ thuật trong chuyển giao liên trạm:**
  - Học chuyển giao liên trạm trong MBR không phải là bài toán sao chép mô hình đơn giản.
  - Trạm nguồn và trạm đích có thể khác biệt lớn về thành phần nước thải đầu vào, tính chất hóa lý của bùn hoạt tính, tỷ lệ các phân đoạn EPS/SMP, các tương tác hữu cơ - kim loại (metal-organic interactions) và điều kiện vận hành.
  - Khi lượng dữ liệu trạm đích quá nhỏ, bước tinh chỉnh có thể không nắm bắt đầy đủ các nhân tố bám bẩn mới nổi đóng vai trò chi phối tại trạm đích nếu các nhân tố này vốn yếu hoặc vắng mặt ở trạm nguồn.
  - Sự thành công của học chuyển giao không thể chỉ đánh giá bằng sai số dự báo thuần túy ($R^2$, RMSE, MAE).
  - Cần phải phân tích rõ cách thức và lý do tại sao các tín hiệu bám bẩn có ý nghĩa vật lý được lưu giữ, loại bỏ hoặc tái cân bằng trọng số trong suốt tiến trình chuyển giao [26,27].

### 1.4 Mục tiêu nghiên cứu và tính mới về khả năng giải thích (Explainability)

- **Lỗ hổng của các phương pháp giải thích học máy thuần túy:**
  - Các phương pháp giải thích như SHAP và LOFO thường chỉ tập trung xếp hạng mức độ quan trọng của đặc trưng ở cấp độ mô hình [26].
  - Trọng số quy kết của SHAP phụ thuộc chặt chẽ vào cấu trúc mô hình và hoàn toàn thiếu chuẩn đối chứng thực nghiệm (ground truth) để xác thực [27].
  - Độ chính xác dự báo cao đơn thuần không đảm bảo các đặc trưng được mô hình nhấn mạnh phản ánh đúng hành vi bám bẩn thực tế trong bể lọc [27].
  - Cần kết hợp phân tích giải thích AI với các phép đo đặc trưng hóa lý độc lập để chứng minh tính hợp lý của sự chuyển dịch quy kết đặc trưng.

- **Các phương pháp phân tích hóa lý độc lập đối chứng:**
  - Phổ ma trận huỳnh quang kích thích - phát xạ (Excitation-Emission Matrix - EEM).
  - Sắc ký lỏng phát hiện cacbon hữu cơ (Liquid Chromatography-Organic Carbon Detection - LC-OCD).
  - Phân tích trực tiếp thành phần chất bám bẩn bám trên sợi màng (foulant analysis).

- **Bốn mục tiêu nghiên cứu cụ thể của công trình:**
  1. *Tiền huấn luyện mô hình cơ sở đa nguồn:* Xây dựng các mô hình cơ sở dựa trên mạng LSTM và thuật toán XGBoost. Tiền huấn luyện mô hình trên các tập dữ liệu thu thập từ 3 trạm MBR quy mô pilot xử lý nước thải sinh hoạt (trạm nguồn), bao quát điều kiện vận hành phong phú, đặc tính hóa sinh thông thường và các phân đoạn chính của EPS và SMP.
  2. *Tinh chỉnh và định lượng ảnh hưởng của tỷ lệ dữ liệu:* Sử dụng tập dữ liệu hạn chế từ trạm MBR đích (xử lý nước thải sinh hoạt) để tinh chỉnh mô hình cơ sở. Lập biểu đồ định lượng mối quan hệ giữa tỷ lệ dữ liệu tinh chỉnh ($10\%\text{--}100\%$) và hiệu năng dự báo $TMP$. Đồng thời, so sánh tác động của hai loại kiến trúc LSTM và XGBoost đến hiệu quả chuyển giao sau tinh chỉnh.
  3. *Làm rõ cơ chế chuyển giao bằng công cụ XAI và phân tích hóa lý:* Đánh giá hành vi chuyển giao và các tín hiệu bám bẩn có thể chuyển giao thông qua SHAP và LOFO. Đối chiếu trực tiếp với dữ liệu hóa lý từ EEM, LC-OCD và phân tích chất bám bẩn. Làm sáng tỏ cách các chỉ thị sinh hóa EPS và SMP được bảo tồn hoặc phân bổ lại trọng số, cung cấp bằng chứng cơ chế cho sự thay đổi này (đặc biệt là tác động của dòng vào giàu ion Fe).
  4. *Xác thực tính tổng quát hóa trên nước thải công nghiệp:* Thử nghiệm mở rộng khung học chuyển giao trên trạm MBR pilot xử lý nước thải công nghiệp. Đánh giá tính khả thi và độ bền vững của mô hình chuyển giao liên trạm dưới một nền nước thải hoàn toàn khác biệt.

- **Đóng góp then chốt của bài báo:**
  - Thiết lập lộ trình thực nghiệm và tính toán tin cậy cho việc xây dựng mô hình dự báo bám bẩn màng tại các cơ sở MBR khan hiếm dữ liệu.
  - Kết hợp chặt chẽ giữa thuật toán học chuyển giao và cơ chế hóa lý thực nghiệm để đảm bảo mô hình vừa có độ chính xác cao vừa giải thích được rõ ràng.

## 2. Vật liệu và phương pháp nghiên cứu (Materials and methods)

### 2.1 Thu thập dữ liệu từ các trạm nguồn và trạm đích (Data collection)

#### 2.1.1 Trạm đích: Cấu hình hệ thống và tập dữ liệu hạn chế (Target Plant)
- Quy mô và địa điểm: Trạm xử lý nước thải sinh hoạt quy mô pilot đặt tại Singapore.
- Đặc tính nước đầu vào: Nước thải sinh hoạt bổ sung sắt ($10\text{--}30\text{ mg/L Fe}$) ở thượng nguồn.
- Công suất xử lý định mức: $24\text{ m}^3/\text{ngày}$.
- Cấu hình công nghệ:
  - Cụm tiền xử lý cơ học.
  - Bể phản ứng sinh học 5 ngăn nạp liệu phân đoạn (five-pass step-feed bioreactor) kết hợp vùng kỵ khí/hiếu khí (anaerobic/oxic zonation).
  - Bể màng ngập (submerged membrane tank) tách sinh khối.
- Hồ sơ áp suất xuyên màng:
  - Áp suất xuyên màng (TMP) ghi nhận liên tục qua hệ thống giám sát tự động.
  - Cấu trúc module màng dạng sợi rỗng ngập nước vận hành chu kỳ hút/rửa ngắt quãng.
- Khung thời gian và kích thước mẫu:
  - Thời gian thu thập từ tháng 09/2021 đến tháng 06/2022.
  - Tần suất phân tích các chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP) là 2 lần/tuần.
  - Mô hình chỉ sử dụng các ngày có đầy đủ tất cả biến đầu vào và giá trị TMP.
  - Tập dữ liệu hợp lệ đạt 71 mẫu ghép cặp theo thời gian ($N_{\text{target}} = 71$).
- Thách thức dữ liệu:
  - Kích thước mẫu nhỏ phản ánh hạn chế thực tế trong giám sát trạm pilot.
  - Số liệu thưa tạo kịch bản thực tế để kiểm chứng học chuyển giao (Transfer Learning).

#### 2.1.2 Các trạm nguồn: Cấu hình hệ thống và tập dữ liệu quy mô lớn (Source Plants)
- Đối tượng nghiên cứu: Ba trạm MBR quy mô pilot xử lý nước thải sinh hoạt tại Singapore.
- Tổng số bản ghi dữ liệu: Đạt 332 mẫu hợp lệ ($N_{\text{source}} = 332$):
  - Trạm 1 (Plant 1): 100 bản ghi.
  - Trạm 2 (Plant 2): 132 bản ghi.
  - Trạm 3 (Plant 3): 100 bản ghi.
- Cấu hình công nghệ chung:
  - Xử lý sinh học thiếu khí/hiếu khí (anoxic/oxic).
  - Tách màng ngập trong bể (immersed membrane separation).
  - Hệ thống tuần hoàn bùn hoạt tính và xả bùn dư truyền thống.
- Tính tương đồng và cơ sở chuyển giao tri thức:
  - Trạm đích nhận nước thải giàu sắt nhưng giữ cấu hình xử lý tương đồng các trạm nguồn.
  - Cơ chế tắc nghẽn màng (MBR fouling) chia sẻ các quy luật thủy lực và sinh học chung.
  - Độ tương đồng này làm nền tảng cho việc áp dụng học chuyển giao xuyên trạm.

#### 2.1.3 Tập biến số vận hành và hóa lý được giám sát (Monitored Variables)
- Tổng số biến số giám sát: Mỗi trạm ghi nhận đồng thời 11 biến đầu vào và 1 biến đầu ra.
- Nhóm thông số vận hành thủy lực:
  - Thời gian lưu nước (HRT, đơn vị $\text{h}$).
  - Thời gian lưu bùn (SRT, đơn vị $\text{d}$).
  - Lưu lượng riêng qua màng (FLUX, đơn vị $\text{L}/(\text{m}^2\cdot\text{h})$).
- Nhóm thông số chất lượng nước và nồng độ bùn:
  - Nhu cầu oxy hóa học tổng số (TCOD, đơn vị $\text{mg/L}$).
  - Nhu cầu oxy hóa học hòa tan (SCOD, đơn vị $\text{mg/L}$).
  - Nồng độ chất rắn lơ lửng trong dịch hỗn hợp (MLSS, đơn vị $\text{mg/L}$).
  - Nồng độ chất rắn lơ lửng bay hơi trong dịch hỗn hợp (MLVSS, đơn vị $\text{mg/L}$).
- Nhóm hoạt chất sinh học gây tắc nghẽn màng:
  - Protein trong EPS (EPSp, đơn vị $\text{mg/L}$).
  - Carbohydrate trong EPS (EPSc, đơn vị $\text{mg/L}$).
  - Protein trong SMP (SMPp, đơn vị $\text{mg/L}$).
  - Carbohydrate trong SMP (SMPc, đơn vị $\text{mg/L}$).
- Biến mục tiêu giám sát:
  - Áp suất xuyên màng TMP (đơn vị $\text{kPa}$) thu từ cảm biến tự động trực tuyến.
  - Dữ liệu TMP được căn chỉnh thời gian khớp chính xác với từng ngày lấy mẫu hóa lý.


### 2.2 Phương pháp phân tích hóa lý (Physicochemical analytical methods)

#### 2.2.1 Quy trình phân tích các chỉ tiêu vận hành và chất lượng bùn (Standard Methods)
- Thông số vận hành: HRT, SRT và FLUX được ghi chép liên tục từ nhật ký vận hành thực địa.
- Phân tích nhu cầu oxy hóa học:
  - Xác định TCOD và SCOD theo phương pháp so màu hồi lưu kín APHA 5220D.
  - Mẫu SCOD được lọc qua màng lọc có kích thước lỗ $0{,}45\ \mu\text{m}$ trước khi phân tích.
- Phân tích nồng độ chất rắn sinh khối:
  - Xác định MLSS và MLVSS theo Tiêu chuẩn kiểm tra nước và nước thải (Standard Methods 2540D và 2540E).
  - Sấy mẫu tại $105\ ^\circ\text{C}$ để đo MLSS và nung tại $550\ ^\circ\text{C}$ để xác định MLVSS.

#### 2.2.2 Quy trình chiết tách và định lượng phân đoạn EPS và SMP (EPS/SMP Fractionation)
- Định nghĩa và chiết tách phân đoạn SMP:
  - Ly tâm dịch hỗn hợp bùn ở tốc độ thấp.
  - Thu dịch nổi và lọc qua màng $0{,}45\ \mu\text{m}$ để lấy phân đoạn SMP hòa tan.
- Quy trình chiết tách phân đoạn EPS liên kết:
  - Sử dụng phương pháp nhiệt (heat extraction method) trên phần bùn lắng còn lại.
  - Đưa huyền phù bùn vào bể ổn nhiệt ở $80\ ^\circ\text{C}$ trong khoảng thời gian quy định để giải phóng EPS từ bông bùn.
  - Ly tâm và thu dịch chứa EPS liên kết.
- Phương pháp định lượng thành phần sinh hóa:
  - Định lượng protein (EPSp và SMPp): Áp dụng phương pháp Lowry cải tiến (Modified Lowry Protein Assay) với chuẩn albumin huyết thanh bò (BSA).
  - Định lượng carbohydrate (EPSc và SMPc): Áp dụng phương pháp Dubois (phương pháp Phenol-Sulfuric Acid) với chuẩn D-glucose.

#### 2.2.3 Đặc trưng hóa chất hữu cơ hòa tan và cấu trúc bùn (Spectroscopic & Organic Profiling)
- Sắc ký lỏng phát hiện cacbon hữu cơ (LC-OCD):
  - Phân tách chất hữu cơ hòa tan thành các phân đoạn theo kích thước phân tử.
  - Nhóm biopolymer: Khối lượng phân tử $\text{MW} > 20\text{ kDa}$.
  - Nhóm hợp chất phân tử lượng thấp ($\text{MW} < 1000\text{ Da}$): Chất humic, khối xây dựng (building blocks), axit trọng lượng thấp và hợp chất trung tính.
- Phân bố kích thước hạt (PSD):
  - Đo phổ kích thước hạt bùn hoạt tính bằng thiết bị nhiễu xạ laser (laser diffraction particle analyzer).
- Thời gian hút mao dẫn (CST):
  - Đánh giá khả năng lọc và tách nước của bùn bằng thiết bị đo CST tiêu chuẩn.
- Tổng cacbon hữu cơ (TOC):
  - Đo nồng độ cacbon hữu cơ bằng máy phân tích TOC-VCSH (Shimadzu, Nhật Bản).
- Phổ huỳnh quang ma trận kích thích - phát xạ (EEM):
  - Đo phổ huỳnh quang ba chiều bằng máy quang phổ huỳnh quang để nhận diện các hợp chất tương tự humic và tryptophan.
- Định lượng hàm lượng sắt tổng:
  - Phân tích sắt trong nước đầu vào và bùn bằng quang phổ phát xạ nguyên tử plasma cảm ứng (ICP-OES).


### 2.3 Tiền xử lý dữ liệu và lựa chọn đặc trưng (Data preprocessing and feature selection)

#### 2.3.1 Xử lý ngoại lai, gán giá trị thiếu và chuẩn hóa thang đo Z-score (Standardization)
- Làm sạch dữ liệu:
  - Kiểm tra và xử lý điểm ngoại vi bằng khoảng tứ phân vị và ngưỡng vật lý thực nghiệm.
  - Nội suy dữ liệu thiếu dựa trên tính liên tục cục bộ của chuỗi thời gian.
- Chuẩn hóa Z-score:
  - Đưa tất cả biến số về cùng thang đo nhằm tránh ưu tiên các biến có khoảng biến thiên lớn:
    $$z = \frac{x - \mu}{\sigma}$$
  - Trong đó: $x$ là giá trị ban đầu, $\mu$ là giá trị trung bình mẫu, $\sigma$ là độ lệch chuẩn của mẫu.
  - Bộ chuẩn hóa chỉ khớp (fit) trên tập dữ liệu huấn luyện để ngăn chặn rò rỉ dữ liệu (data leakage).
  - Giá trị dự báo của mô hình được biến đổi ngược về đơn vị gốc sau khi suy luận.

#### 2.3.2 Tái định dạng biến mục tiêu chênh lệch áp suất lọc dTMP (Target Reconstruction)
- Mục tiêu dự đoán cuối cùng: Áp suất màng ngày tiếp theo ($\text{TMP}_{t+1}$).
- Định dạng biến mục tiêu trung gian:
  - Sử dụng mức tăng áp suất lọc $\Delta \text{TMP}_t$ (kí hiệu là $\text{dTMP}_t$) làm đích huấn luyện mô hình:
    $$\text{dTMP}_t = \text{TMP}_{t+1} - \text{TMP}_t$$
- Ưu điểm cơ chế:
  - Giảm tính không dừng (non-stationarity) của chuỗi thời gian áp suất màng.
  - Khắc phục sự sai lệch mức áp suất nền tuyệt đối giữa các trạm khác nhau.
  - Tạo ra phân phối dữ liệu tập trung quanh giá trị 0.
- Khôi phục giá trị thực tế:
  - Giá trị dự đoán $\widehat{\text{TMP}}_{t+1}$ được tái tạo bằng cách cộng dTMP dự báo vào TMP đo đạc hiện tại:
    $$\widehat{\text{TMP}}_{t+1} = \text{TMP}_t + \widehat{\text{dTMP}}_t$$

#### 2.3.3 Phân tích thành phần chính liên hợp đánh giá độ lệch phân phối (Joint PCA)
- Mục đích phân tích:
  - Đo lường mức độ trùng lặp không gian và độ lệch phân phối giữa miền nguồn và miền đích.
- Phương pháp thực hiện:
  - Tiến hành phân tích thành phần chính liên hợp (Joint Principal Component Analysis - Joint PCA).
  - Đưa toàn bộ các biến đầu vào cùng biến trung gian $\text{dTMP}$ vào ma trận phân tích.
  - Khối biến đầu vào và khối biến đầu ra được chuẩn hóa độc lập và gán trọng số tổng thể ngang nhau.

#### 2.3.4 Sàng lọc biến số theo tỷ lệ SFR và kiểm định tương quan Pearson (Feature Screening)
- Tỷ lệ kích thước mẫu trên số đặc trưng (SFR):
  - Chỉ số $\text{SFR} = N/p$ quyết định nguy cơ quá khớp trong bài toán mẫu nhỏ.
  - Yêu cầu thực nghiệm cần $\text{SFR} > 10$ để mô hình đạt độ tin cậy thống kê cao.
- Sàng lọc thô tương quan đặc trưng - mục tiêu ($X\text{--}y$ Pearson correlation):
  - Đánh giá tương quan Pearson trực tiếp với $\text{TMP}$ ngày tiếp theo:
    $$r_{x,y} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}$$
  - Các đặc trưng tương quan mạnh được giữ lại:
    - $\text{FLUX}$: $|r| = 0{,}471$.
    - $\text{EPSc}$: $|r| = 0{,}462$.
    - $\text{HRT}$: $|r| = 0{,}440$.
    - $\text{SMPp}$: $|r| = 0{,}347$.
  - Loại bỏ các đặc trưng có $|r| < 0{,}10$: $\text{SCOD}$, $\text{SMPc}$ và $\text{TCOD}$.
- Sàng lọc đa cộng tuyến đặc trưng - đặc trưng ($X\text{--}X$ Pearson collinearity):
  - Cặp $\text{HRT}$ và $\text{FLUX}$ có tương quan âm rất mạnh ($r = -0{,}86$) do ràng buộc lưu lượng thủy lực. Giữ lại $\text{FLUX}$ do có tương quan với $\text{TMP}$ cao hơn.
  - Cặp $\text{MLSS}$ và $\text{MLVSS}$ có tương quan dương gần như tuyệt đối ($r = 0{,}96$). Giữ lại $\text{MLVSS}$ do đại diện cho phần sinh khối hoạt tính mang EPS.
- Tập đặc trưng thu gọn cuối cùng:
  - Gồm 6 thông số: $\text{FLUX}$, $\text{SRT}$, $\text{MLVSS}$, $\text{EPSc}$, $\text{EPSp}$, $\text{SMPp}$.


### 2.4 Xây dựng mô hình cơ sở dựa trên trạm nguồn (Construction of base models)

#### 2.4.1 Phân chia dữ liệu theo thời gian và kiến trúc mô hình chuỗi LSTM-base (LSTM Architecture)
- Phân chia tập dữ liệu nguồn:
  - Chia tách dữ liệu của từng trạm nguồn theo thứ tự thời gian tuyến tính thay vì ngẫu nhiên.
  - Loại bỏ hiện tượng rò rỉ thông tin giữa các mẫu thời gian kề cận nhau.
- Độ dài cửa sổ lịch sử:
  - Thiết lập cửa sổ chuỗi thời gian độ dài $T = 3$ bước thời gian liên tiếp.
- Kiến trúc mạng LSTM-base:
  - Sử dụng mạng bộ nhớ dài - ngắn (Long Short-Term Memory) nhỏ gọn chuyên biệt cho học chuỗi.
  - Nhận đầu vào là chuỗi đặc trưng chuẩn hóa độ dài 3 bước để mô hình hóa động học tích lũy chất tắc nghẽn.

#### 2.4.2 Kiến trúc mô hình cây quyết định XGBoost-base với đặc trưng trễ (XGBoost Architecture)
- Kiến trúc mô hình:
  - Thuật toán tăng cường độ dốc cây quyết định (eXtreme Gradient Boosting - XGBoost).
- Mã hóa biến trễ thời gian:
  - Sử dụng thông tin lịch sử 3 bước được làm phẳng thành các biến trễ (lagged features).
  - Tổng số đặc trưng đầu vào cho cây là $6 \times 3 = 18$ biến trễ.
  - Đảm bảo tính công bằng thực nghiệm khi mô hình cây nhận đúng dung lượng thông tin như mô hình mạng LSTM.

#### 2.4.3 Tối ưu hóa siêu tham số bằng Optuna và kiểm định chéo chuỗi thời gian (Hyperparameter Tuning)
- Khung kiểm định chéo:
  - Áp dụng kiểm định chéo chuỗi thời gian 5 nếp (5-fold time-series cross-validation) trên tập huấn luyện nguồn.
  - Huấn luyện trên các mốc quá khứ và đánh giá trên mốc tương lai nhằm ngăn ngừa thiên lệch thời gian.
- Khung tối ưu hóa Bayes Optuna:
  - Tự động dò tìm bộ siêu tham số tối ưu (tốc độ học, số tầng, số cây, độ sâu, hệ số điều chuẩn).
  - Sau tối ưu, hai mô hình hoàn chỉnh được huấn luyện trên toàn bộ tập huấn luyện nguồn và lưu trữ làm trọng số gốc cho học chuyển giao.


### 2.5 Xây dựng mô hình đường cơ sở cho trạm đích (Construction of target baseline model)

#### 2.5.1 Chiến lược phân chia dữ liệu kiểm thử độc lập 50:50 (Data Splitting Strategy)
- Tỷ lệ phân chia tập dữ liệu trạm đích:
  - Phân chia tập 71 mẫu trạm đích theo thứ tự thời gian chuẩn tỷ lệ 50:50.
  - Nửa đầu 50% ($N \approx 35$ mẫu) dùng làm nguồn dữ liệu huấn luyện và tinh chỉnh.
  - Nửa sau 50% ($N = 36$ mẫu) đóng vai trò tập kiểm thử độc lập (test set), hoàn toàn không được nhìn thấy trước.
- Mục đích phân chia:
  - Ngăn ngừa hoàn toàn hiện tượng rò rỉ dữ liệu theo trục thời gian.
  - Đánh giá khả năng dự báo dài hạn trên dữ liệu thực tế.

#### 2.5.2 Cấu hình mô hình XGBoost-baseline độc lập (Standalone Baseline Configuration)
- Lựa chọn thuật toán đường cơ sở:
  - Chọn XGBoost độc lập làm mô hình đối chứng thay vì huấn luyện một mạng LSTM riêng biệt.
  - Mạng LSTM độc lập dễ rơi vào trạng thái mất ổn định và quá khớp nặng khi chỉ có khoảng 35 mẫu huấn luyện.
- Thiết lập huấn luyện:
  - Mô hình cây XGBoost-baseline chỉ sử dụng dữ liệu trong nửa đầu của trạm đích.
  - Bộ chuẩn hóa biến mục tiêu và đặc trưng được khớp hoàn toàn độc lập trên nửa đầu này.
  - Sử dụng cùng 6 đặc trưng đầu vào để bảo đảm tính đối sánh trực tiếp với mô hình học chuyển giao.


### 2.6 Xây dựng mô hình học chuyển giao (Construction of transfer learning models)

#### 2.6.1 Thiết lập tỷ lệ tinh chỉnh FT và phân đoạn lấy mẫu (Fine-Tuning Ratio Setup)
- Định nghĩa tỷ lệ tinh chỉnh ($\text{FT}$):
  - Tỷ lệ $\text{FT}$ biểu thị phần trăm dữ liệu từ tổng tập trạm đích được sử dụng để tinh chỉnh mô hình:
    $$\text{FT} \in \{0\%,\ 10\%,\ 20\%,\ 30\%,\ 40\%,\ 50\%\}$$
  - Tại $\text{FT} = 0\%$: Mô hình chuyển giao trực tiếp không qua tinh chỉnh (zero-shot direct transfer).
  - Tại $\text{FT} = 10\%\text{ đến }50\%$: Thích ứng gia tăng với số lượng mẫu tăng dần lấy từ vùng 50% đầu.
- Giao thức lấy mẫu nhiều phân đoạn liên tục:
  - Rút ngẫu nhiên nhiều phân đoạn chuỗi thời gian liên tục từ vùng tinh chỉnh.
  - Tránh phụ thuộc vào một giai đoạn lịch sử cục bộ duy nhất.
  - Mỗi thực nghiệm được lặp lại với 5 hạt giống ngẫu nhiên (random seeds).
  - Kết quả báo cáo dưới dạng giá trị trung bình kèm độ lệch chuẩn ($\text{mean} \pm \text{SD}$).

#### 2.6.2 Chiến lược cập nhật trọng số và tinh chỉnh cho LSTM-FT và XGBoost-FT (Model Adaptation)
- Mô hình mạng chuỗi LSTM-FT:
  - Khởi tạo trọng số từ mô hình LSTM-base đã học các quy luật tắc nghẽn chung ở trạm nguồn.
  - Tinh chỉnh các tầng mạng bằng dữ liệu trạm đích với tốc độ học nhỏ (fine-tuning learning rate).
  - Giữ lại các đặc trưng tổng quát và cập nhật biểu diễn thích ứng với đặc tính nước thải giàu sắt.
- Mô hình cây XGBoost-FT:
  - Bổ sung và cập nhật cây trên cơ sở cấu trúc cây XGBoost-base đã huấn luyện từ trước.
  - Điều chỉnh trọng số lá và ngưỡng tách nhánh để thích ứng với sai lệch phân phối của trạm đích.

#### 2.6.3 Môi trường phần cứng và khung phần mềm thực nghiệm (Computational Environment)
- Ngôn ngữ và thư viện lập trình:
  - Ngôn ngữ Python phiên bản 3.10.18.
  - Xây dựng và huấn luyện mạng học sâu trên thư viện PyTorch phiên bản 2.7.0.
  - Sử dụng thư viện XGBoost, Scikit-learn và Optuna cho mô hình cây và tối ưu hóa siêu tham số.
- Cấu hình phần cứng máy tính:
  - Bộ vi xử lý trung tâm: Intel Core i7-14700KF (28 luồng logic).
  - Bộ nhớ truy xuất ngẫu nhiên: 32 GB RAM.
  - Bộ xử lý đồ họa chuyên dụng: NVIDIA GeForce RTX 5060 Ti GPU.


### 2.7 Đánh giá hiệu năng mô hình (Evaluation of model performance)

#### 2.7.1 Các chỉ số định lượng đánh giá sai số và độ phù hợp ($R^2$, RMSE, MAE)
- Hệ số xác định ($R^2$):
  - Đánh giá tỷ lệ phương sai của giá trị TMP quan trắc được giải thích bởi mô hình:
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - Trong đó: $y_i$ là giá trị TMP quan trắc thực tế, $\hat{y}_i$ là giá trị dự đoán, $\bar{y}$ là giá trị trung bình quan trắc, $n$ là số mẫu kiểm thử.
- Sai số căn bậc hai trung bình bình phương (RMSE):
  - Đo lường độ lệch chuẩn của phần dư dự đoán, phản ánh độ nhạy với sai số lớn:
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
- Sai số tuyệt đối trung bình (MAE):
  - Đo mức sai số trung bình trực tiếp theo đơn vị đo áp suất ($\text{kPa}$):
    $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$

#### 2.7.2 Phân tích độ quan trọng đặc trưng bằng LOFO và SHAP (Model Interpretability)
- Phương pháp loại bỏ từng đặc trưng (Leave-One-Feature-Out - LOFO):
  - Lần lượt loại bỏ từng biến số đầu vào, huấn luyện lại hoặc đánh giá lại mô hình trên cùng điều kiện.
  - Mức độ gia tăng sai số (RMSE/MAE) hoặc suy giảm $R^2$ phản ánh vai trò không thể thay thế của biến đó.
  - Sử dụng kiểm định phi tham số Wilcoxon signed-rank test cặp đôi hai phía để đánh giá ý nghĩa thống kê ($p < 0{,}05$).
- Phương pháp giá trị phân bổ Shapley (SHapley Additive exPlanations - SHAP):
  - Dựa trên lý thuyết trò chơi hợp tác để tính toán đóng góp biên công bằng của từng biến số:
    $$\phi_j = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} [f(S \cup \{j\}) - f(S)]$$
  - Trong đó: $F$ là toàn bộ tập đặc trưng, $S$ là tập con các đặc trưng không chứa biến $j$, $f(S)$ là giá trị dự đoán của mô hình khi chỉ có tập $S$.
  - Biểu đồ tóm tắt SHAP giải thích hướng tác động âm/dương của nồng độ EPS, SMP và thông số vận hành lên tốc độ tăng áp suất TMP.


### 2.8 Khả năng thích ứng của mô hình trong điều kiện xuyên kịch bản (Cross-scenario adaptability)

#### 2.8.1 Cấu hình trạm MBR xử lý nước thải công nghiệp hóa dầu và dược phẩm (Industrial Scenario)
- Bối cảnh mở rộng thực nghiệm:
  - Kiểm tra tính tổng quát hóa của khung học chuyển giao trên hệ thống MBR pilot xử lý nước thải công nghiệp hỗn hợp tại Singapore.
  - Nguồn nước thải kết hợp giữa nhà máy hóa dầu và cơ sở sản xuất dược phẩm.
- Đặc thù nước thải công nghiệp:
  - Chứa nhiều hợp chất hữu cơ khó phân hủy sinh học, chất hoạt động bề mặt và độc chất ức chế bùn.
  - Cấu trúc chất gây tắc nghẽn và động thái màng khác biệt sâu sắc so với nước thải sinh hoạt đô thị.

#### 2.8.2 Giao thức kiểm thử chuyển giao xuyên kịch bản không tái tối ưu (Zero-retuning Protocol)
- Thiết lập mô hình chuyển giao:
  - Sử dụng mô hình mạng LSTM-FT đã được tiền huấn luyện trên các trạm nguồn sinh hoạt.
  - Kiểm thử tại hai chế độ tinh chỉnh: $\text{FT} = 0\%$ (chuyển giao trực tiếp) và $\text{FT} = 40\%$ (tinh chỉnh với 40% dữ liệu công nghiệp).
- Nguyên tắc giữ nguyên cấu hình (Frozen settings):
  - Giữ nguyên cấu trúc mô hình tiền huấn luyện ban đầu.
  - Áp dụng nguyên vẹn quy trình phân chia chuỗi thời gian, phương pháp làm sạch và chuẩn hóa dữ liệu.
  - Không tiến hành tìm kiếm lại siêu tham số hay can thiệp cấu trúc mạng.
- Mục tiêu đánh giá:
  - Xác nhận xem khung học chuyển giao có duy trì độ chính xác cao ($R^2 \approx 0{,}9$) khi môi trường hóa lý thay đổi đột ngột hay không.
  - Khám phá sự dịch chuyển của các tín hiệu tắc nghẽn then chốt (như vai trò vượt trội của SMPp trong nước thải công nghiệp).

## 3. Kết quả và thảo luận (Results and discussion)

### 3.1 Phân phối dữ liệu trạm nguồn - trạm đích và phân tích PCA (Source-target distribution and PCA analysis)

#### 3.1.1 Phân phối các biến đo lường giữa trạm nguồn và trạm đích
- So sánh các thông số vận hành cốt lõi:
  - Giá trị vận hành của trạm đích nằm trong hoặc sát dải biến thiên của các trạm nguồn.
  - Thời gian lưu thủy lực (HRT): Trạm đích duy trì cố định ở mức $5.5\text{ h}$. Các trạm nguồn dao động từ $5.0\text{ h}$ đến $5.5\text{ h}$.
  - Thời gian lưu bùn (SRT): Trạm đích duy trì ở mức $6.8\text{ d}$. Các trạm nguồn dao động từ $5.0\text{ d}$ đến $7.0\text{ d}$.
  - Thông lượng lọc (FLUX): Trạm đích vận hành ở mức $25\text{ LMH}$ ($\text{L/(m}^2\cdot\text{h)}$). Các trạm nguồn biến thiên trong dải rộng từ $25\text{ LMH}$ đến $44\text{ LMH}$.
- Dải biến thiên các thông số sinh khối và bám bẩn tại các trạm nguồn:
  - Nồng độ chất rắn lơ lửng trong bùn hoạt tính (MLSS): Biến thiên từ $900\text{ mg/L}$ đến $9730\text{ mg/L}$.
  - Nồng độ chất rắn lơ lửng bay hơi (MLVSS): Biến thiên từ $639\text{ mg/L}$ đến $7671\text{ mg/L}$.
  - Phân đoạn protein của chất polyme ngoại bào (EPSp): Dao động từ $25.0\text{ mg/L}$ đến $658.8\text{ mg/L}$.
  - Phân đoạn carbohydrate của chất polyme ngoại bào (EPSc): Dao động từ $0.0\text{ mg/L}$ đến $117.1\text{ mg/L}$.
  - Phân đoạn carbohydrate của sản phẩm vi sinh hòa tan (SMPc): Dao động từ $0.8\text{ mg/L}$ đến $33.3\text{ mg/L}$.
  - Phân đoạn protein của sản phẩm vi sinh hòa tan (SMPp): Dao động từ $2.7\text{ mg/L}$ đến $44.5\text{ mg/L}$.
- Phân phối các biến sinh thái và bám bẩn tại trạm đích:
  - Trạm đích ghi nhận biên độ phân phối hẹp hơn so với các trạm nguồn.
  - Chỉ số MLSS: Dao động từ $3580\text{ mg/L}$ đến $7340\text{ mg/L}$.
  - Chỉ số MLVSS: Dao động từ $3340\text{ mg/L}$ đến $5920\text{ mg/L}$.
  - Chỉ số EPSp: Dao động từ $73.5\text{ mg/L}$ đến $469.9\text{ mg/L}$.
  - Chỉ số EPSc: Dao động từ $17.1\text{ mg/L}$ đến $81.3\text{ mg/L}$.
  - Chỉ số SMPc: Dao động từ $2.6\text{ mg/L}$ đến $20.1\text{ mg/L}$.
  - Chỉ số SMPp: Dao động từ $4.8\text{ mg/L}$ đến $10.8\text{ mg/L}$.

Bảng 1 (Table 1): So sánh dải phân phối các biến đo lường giữa các trạm nguồn và trạm đích.
| Nhóm thông số | Biến số đo lường | Đơn vị | Dải biến thiên trạm nguồn | Dải biến thiên trạm đích |
| :--- | :--- | :--- | :--- | :--- |
| Vận hành cốt lõi | HRT | $\text{h}$ | $5.0\text{--}5.5$ | $5.5$ |
| Vận hành cốt lõi | SRT | $\text{d}$ | $5.0\text{--}7.0$ | $6.8$ |
| Vận hành cốt lõi | FLUX | $\text{LMH}$ | $25\text{--}44$ | $25$ |
| Sinh khối bùn | MLSS | $\text{mg/L}$ | $900\text{--}9730$ | $3580\text{--}7340$ |
| Sinh khối bùn | MLVSS | $\text{mg/L}$ | $639\text{--}7671$ | $3340\text{--}5920$ |
| Polyme ngoại bào (EPS) | EPSp | $\text{mg/L}$ | $25.0\text{--}658.8$ | $73.5\text{--}469.9$ |
| Polyme ngoại bào (EPS) | EPSc | $\text{mg/L}$ | $0.0\text{--}117.1$ | $17.1\text{--}81.3$ |
| Vi sinh hòa tan (SMP) | SMPc | $\text{mg/L}$ | $0.8\text{--}33.3$ | $2.6\text{--}20.1$ |
| Vi sinh hòa tan (SMP) | SMPp | $\text{mg/L}$ | $2.7\text{--}44.5$ | $4.8\text{--}10.8$ |

#### 3.1.2 Phân tích thành phần chính PCA và độ lệch phân phối
- Tỷ lệ giải thích phương sai của PCA:
  - Hai thành phần chính đầu tiên (PC1 và PC2) giải thích $74.0\%$ tổng phương sai của bộ dữ liệu kết hợp.
  - Hình chiếu hai chiều này phản ánh đầy đủ các biến động chính của các đặc trưng bám bẩn màng.
- Mức độ tương đồng không gian giữa các trạm nguồn:
  - Các cụm dữ liệu trạm nguồn xuất hiện mức độ chồng lấn (overlap) rất lớn trên mặt phẳng PC1-PC2.
  - Sự chồng lấn này chứng minh các trạm nguồn chia sẻ quy luật bám bẩn tương đồng trong xử lý nước thải sinh hoạt.
- Hiện tượng lệch phân phối tại trạm đích:
  - Tập dữ liệu trạm đích tạo thành một cụm co cụm chặt hơn và tách biệt một phần khỏi các trạm nguồn.
  - Vị trí tách biệt này xác nhận sự tồn tại của độ lệch phân phối (distribution shift) giữa hai miền dữ liệu.
- Vùng chồng lấn liên miền và tính khả thi của Transfer Learning:
  - Dữ liệu trạm đích và trạm nguồn vẫn duy trì một vùng chồng lấn rõ rệt.
  - Vùng chồng lấn cung cấp nền tảng vững chắc để xây dựng các mô hình cơ sở từ trạm nguồn.
  - Sự tồn tại của miền chung này bảo đảm tính khả thi cho quy trình tinh chỉnh học chuyển giao tiếp theo.


### 3.2 Xây dựng và đánh giá các mô hình cơ sở (Construction and evaluation of base models)

#### 3.2.1 Lựa chọn đặc trưng dựa trên phân tích tương quan
##### 3.2.1.1 Phân tích tương quan đặc trưng - mục tiêu ($X\text{--}y$)
- Phương pháp phân tích mức độ liên kết:
  - Hệ số tương quan tuyến tính Pearson ($r_{x,y}$) đo lường mức độ phụ thuộc giữa từng đặc trưng đầu vào và áp suất xuyên màng TMP.
- Nhóm đặc trưng có tương quan mạnh với TMP:
  - Thông lượng lọc (FLUX): Đạt hệ số tương quan $|r_{x,y}| = 0.471$.
  - Carbohydrate ngoại bào (EPSc): Đạt hệ số tương quan $|r_{x,y}| = 0.462$.
  - Thời gian lưu thủy lực (HRT): Đạt hệ số tương quan $|r_{x,y}| = 0.440$.
  - Protein hòa tan (SMPp): Đạt hệ số tương quan $|r_{x,y}| = 0.347$.
- Nhóm đặc trưng có tương quan yếu với TMP:
  - Nhu cầu oxy hóa học hòa tan (SCOD): Đạt hệ số tương quan $|r_{x,y}| < 0.1$.
  - Carbohydrate vi sinh hòa tan (SMPc): Đạt hệ số tương quan $|r_{x,y}| < 0.1$.
  - Tổng nhu cầu oxy hóa học (TCOD): Đạt hệ số tương quan $|r_{x,y}| < 0.1$.
- Loại bỏ các biến không liên quan:
  - Tác giả loại bỏ SCOD, SMPc và TCOD khỏi tập biến đầu vào do tương quan thực nghiệm quá thấp.
  - Các biến có liên kết có ý nghĩa được chuyển sang bước sàng lọc đa cộng tuyến tiếp theo.

##### 3.2.1.2 Phân tích đa cộng tuyến đặc trưng - đặc trưng ($X\text{--}X$) và bộ biến tối giản
- Kiểm soát đa cộng tuyến giữa các cặp đặc trưng:
  - Phân tích tương quan Pearson cặp ($r_{x_j, x_k}$) xác định mức độ phụ thuộc lẫn nhau giữa các biến đầu vào.
- Cặp biến vận hành gắn kết HRT và FLUX:
  - Hai thông số thể hiện tương quan âm rất mạnh với $r_{x_j, x_k} = -0.86$.
  - Cơ chế thủy lực: HRT tỉ lệ nghịch với lưu lượng cấp nước vào hệ thống. FLUX phản ánh lưu lượng lọc qua một đơn vị diện tích màng.
  - Tiêu chí lựa chọn: FLUX có hệ số tương quan với TMP ($|r_{x,y}| = 0.471$) cao hơn so với HRT ($0.440$).
  - Quyết định xử lý: Giữ lại FLUX và loại bỏ HRT để loại trừ xung đột tuyến tính.
- Cặp biến nồng độ sinh khối MLSS và MLVSS:
  - Hai thông số ghi nhận tương quan dương gần như tuyệt đối với $r_{x_j, x_k} = 0.96$.
  - Bản chất sinh học: MLVSS thể hiện hàm lượng sinh khối hữu cơ hoạt tính nằm trong tổng bùn lơ lửng MLSS.
  - Tiêu chí lựa chọn: MLVSS có tương quan cao hơn với TMP so với MLSS.
  - Quyết định xử lý: Giữ lại MLVSS và loại bỏ MLSS khỏi tập biến huấn luyện.
- Tập 6 đặc trưng tối giản phục vụ mô hình cơ sở:
  - Bộ dữ liệu đầu vào thu gọn cuối cùng gồm 6 thông số: FLUX, SRT, MLVSS, EPSc, EPSp và SMPp.

Bảng 2 (Table 2): Kết quả phân tích tương quan Pearson với TMP ($X\text{--}y$) và tương quan cặp ($X\text{--}X$).
| Đặc trưng khảo sát | Tương quan với TMP ($|r_{x,y}|$) | Biến cộng tuyến cặp | Tương quan cặp ($r_{x_j, x_k}$) | Quyết định chọn lọc | Rationale kỹ thuật |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FLUX | $0.471$ | HRT | $-0.86$ | Giữ lại | Tương quan cao nhất với TMP; đại diện thông lượng thủy lực |
| EPSc | $0.462$ | — | — | Giữ lại | Tương quan mạnh; thành phần tạo gel cản trở thủy lực |
| HRT | $0.440$ | FLUX | $-0.86$ | Loại bỏ | Đa cộng tuyến cao với FLUX; $|r_{x,y}|$ thấp hơn FLUX |
| SMPp | $0.347$ | — | — | Giữ lại | Tương quan đáng kể; tác nhân chính gây tắc nghẽn lỗ rỗng |
| MLVSS | Cao hơn MLSS | MLSS | $0.96$ | Giữ lại | Sinh khối hữu cơ mang EPS; tương quan TMP cao hơn MLSS |
| MLSS | Thấp hơn MLVSS | MLVSS | $0.96$ | Loại bỏ | Đa cộng tuyến rất mạnh với MLVSS |
| EPSp | Mức trung bình | — | — | Giữ lại | Đóng vai trò keo tụ bùn và kích hoạt bám dính ban đầu |
| SRT | Mức trung bình | — | — | Giữ lại | Thông số vận hành then chốt kiểm soát sinh trưởng bùn |
| SCOD | $< 0.1$ | — | — | Loại bỏ | Tương quan không đáng kể với áp suất xuyên màng |
| SMPc | $< 0.1$ | — | — | Loại bỏ | Tương quan không đáng kể với áp suất xuyên màng |
| TCOD | $< 0.1$ | — | — | Loại bỏ | Tương quan không đáng kể với áp suất xuyên màng |

#### 3.2.2 Đánh giá hiệu năng dự đoán của các mô hình cơ sở
##### 3.2.2.1 So sánh định lượng sai số giữa LSTM-base và XGBoost-base
- Mức độ hội tụ quanh đường đẳng lượng:
  - Biểu đồ phân tán dự đoán cho thấy các điểm huấn luyện và kiểm tra phân bố bám sát đường $1:1$.
  - Cả hai mô hình cơ sở tái hiện chính xác diễn biến của TMP tại các trạm nguồn.
- Chỉ số kiểm tra định lượng của XGBoost-base:
  - Hệ số xác định ($R^2$): Đạt $0.86$ trên tập kiểm tra độc lập của trạm nguồn.
  - Sai số toàn phương trung bình (RMSE): Đạt $3.01\text{ kPa}$.
  - Sai số tuyệt đối trung bình (MAE): Đạt $1.94\text{ kPa}$.
- Chỉ số kiểm tra định lượng của LSTM-base:
  - Hệ số xác định ($R^2$): Đạt $0.87$ trên tập kiểm tra độc lập của trạm nguồn.
  - Sai số toàn phương trung bình (RMSE): Đạt $2.86\text{ kPa}$.
  - Sai số tuyệt đối trung bình (MAE): Đạt $1.68\text{ kPa}$.
- So sánh hiệu quả tổng thể:
  - LSTM-base thể hiện ưu thế vượt trội ổn định so với XGBoost-base trên toàn bộ các chỉ số kiểm tra.
  - Giá trị $R^2$ tăng $0.01$. Sai số RMSE giảm $0.15\text{ kPa}$. Sai số MAE giảm $0.26\text{ kPa}$.

Bảng 3 (Table 3): So sánh hiệu năng dự đoán TMP giữa hai mô hình cơ sở trên tập dữ liệu kiểm tra trạm nguồn.
| Mô hình cơ sở | $R^2$ | RMSE ($\text{kPa}$) | MAE ($\text{kPa}$) | Đặc trưng chi phối chính trong SHAP |
| :--- | :--- | :--- | :--- | :--- |
| XGBoost-base | $0.86$ | $3.01$ | $1.94$ | FLUX chiếm ưu thế tuyệt đối |
| LSTM-base | $0.87$ | $2.86$ | $1.68$ | EPSc, MLVSS, EPSp, SMPp phân bổ cân bằng |

##### 3.2.2.2 Sai lệch dự đoán tại vùng áp suất xuyên màng cao
- Hiện tượng gia tăng sai số ở mức áp suất lớn:
  - Cả hai mô hình đều xuất hiện độ phân tán dự đoán lớn hơn khi TMP đạt các ngưỡng giá trị cao.
  - Độ chính xác dự đoán suy giảm trong điều kiện bám bẩn màng nghiêm trọng.
- Nguyên nhân cơ chế hóa lý:
  - Lớp bánh bùn bị nén ép với cường độ cao dưới áp suất hút lớn.
  - Trở lực thủy lực bám bẩn chuyển sang trạng thái tăng trưởng phi tuyến tính phức tạp ở giai đoạn bám bẩn sâu.

#### 3.2.3 Giải thích mô hình cơ sở bằng SHAP và đối chiếu đặc tính hóa lý
##### 3.2.3.1 Phân tích phân bổ giá trị SHAP của hai mô hình cơ sở
- Phương pháp luận giải thích mô hình:
  - Giá trị SHAP định lượng mức đóng góp biên của từng biến vào kết quả dự đoán TMP.
  - Tác giả phân tích trực tiếp biểu đồ đóng góp và biểu đồ phân bổ tổng thể SHAP.
- Mô hình phân bổ đóng góp của LSTM-base:
  - Bốn biến có ảnh hưởng lớn nhất gồm EPSc, MLVSS, EPSp và SMPp.
  - Hai thông số vận hành FLUX và SRT đóng góp ở mức độ thấp hơn.
  - Kiến trúc học chuỗi thời gian của LSTM thích ứng tự nhiên với các biến sinh hóa có tính biến thiên từ từ và liên tục.
- Mô hình phân bổ đóng góp của XGBoost-base:
  - Mức độ đóng góp tập trung cục bộ vào một yếu tố duy nhất.
  - Thông lượng FLUX chi phối toàn diện giá trị SHAP và vượt trội hoàn toàn so với các biến còn lại.
  - Mô hình dựa trên cây quyết định có khuynh hướng phụ thuộc cực đoan vào tín hiệu dự đoán mạnh nhất.
- Tác động cấu trúc lên tiềm năng học chuyển giao:
  - Hai mô hình đạt độ chính xác tương đương trên trạm nguồn nhưng vận hành theo hai cơ chế suy luận khác biệt.
  - Sự phụ thuộc đơn lẻ vào FLUX khiến XGBoost-FT chỉ cải thiện rất hạn chế khi chuyển giao sang trạm đích.
  - LSTM-base nắm bắt toàn diện các thành phần sinh hóa tạo tiền đề chuyển giao vững chắc.

##### 3.2.3.2 Đối chiếu đặc tính hóa lý của bùn hoạt tính và cơ chế bám bẩn EPS
- Cơ sở kiểm chứng thực nghiệm:
  - Nghiên cứu khảo sát đặc tính hóa lý bùn trạm nguồn để xác nhận tính xác thực sinh học của phân bổ SHAP.
  - Chất polyme ngoại bào EPS liên kết chặt chẽ với bông bùn và quá trình hình thành lớp bánh bùn.
  - Sản phẩm vi sinh hòa tan SMP đại diện cho các hợp chất hữu cơ hòa tan trong pha lỏng.
- Dấu ấn phổ huỳnh quang EEM của EPS:
  - Cả ba trạm nguồn thể hiện đỉnh huỳnh quang chung của protein dạng thơm trong phổ huỳnh quang 3D (EEM).
  - Tọa độ bước sóng kích thích và phát xạ: $\text{Ex/Em} \approx 220\text{--}225 / 325\text{--}355\text{ nm}$.
- Phân bố kích thước hạt của bùn hoạt tính:
  - Kích thước hạt bùn phân bố tập trung chủ yếu trong khoảng $20\text{--}40\ \mu\text{m}$.
  - Cấu trúc hạt này rất dễ lắng đọng lên bề mặt màng và hình thành nhanh lớp bánh bùn lọc.
- Cơ chế tác động của phân đoạn EPSp:
  - Thành phần EPSp chứa các protein dạng thơm liên kết với sự kết tụ của các bông bùn.
  - Phân đoạn này chịu trách nhiệm cho quá trình bám dính ban đầu của các chất bám bẩn lên bề mặt màng.
- Cơ chế tác động của phân đoạn EPSc:
  - Phân đoạn EPSc hình thành ma trận gel polysaccharide giữ nước.
  - Lớp gel polysaccharide nén chặt cấu trúc lớp bẩn và làm tăng đột biến trở lực thủy lực qua màng.
- Ý nghĩa vật lý của biến sinh khối MLVSS:
  - Mức đóng góp cao của MLVSS trong SHAP hoàn toàn phù hợp với thực tế vận hành.
  - MLVSS đại diện cho khối lượng sinh học mang EPS và cung cấp vật liệu lắng đọng trực tiếp lên bề mặt màng.

##### 3.2.3.3 Đặc tính sản phẩm vi sinh hòa tan SMP và cơ chế giữ lại của màng
- Dấu ấn huỳnh quang EEM của dịch lọc SMP:
  - Ba trạm nguồn ghi nhận đỉnh huỳnh quang protein dạng thơm chung tại $\text{Ex/Em} \approx 220\text{--}230 / 330\text{--}350\text{ nm}$.
  - Protein dạng thơm hòa tan này hấp phụ lên màng hoặc bị bẫy lại trong lớp bánh bùn đang phát triển.
- Phân tích sắc ký rây phân tử LC-OCD:
  - Dịch SMP tại ba trạm nguồn chứa chủ yếu carbon hữu cơ hòa tan ưa nước (hydrophilic DOC).
  - Hai phân đoạn chiếm tỷ trọng lớn nhất gồm các chất humic (humics) và hợp chất cao phân tử sinh học (biopolymers).
- Công thức tính tỷ lệ loại bỏ các phân đoạn LC-OCD qua màng:
  $$\text{Rejection (\%)} = \frac{C_{\text{SMP}} - C_{\text{effluent}}}{C_{\text{SMP}}} \times 100\%$$
  Trong đó: $C_{\text{SMP}}$ là nồng độ phân đoạn hữu cơ trong dịch SMP bể sinh học. $C_{\text{effluent}}$ là nồng độ phân đoạn tương ứng trong nước sau lọc.
- Tỷ lệ giữ lại thực nghiệm của màng đối với biopolymers:
  - Phân đoạn biopolymers ghi nhận mức giữ lại cao nhất tại cả ba trạm nguồn.
  - Tỷ lệ loại bỏ thực nghiệm nằm trong dải từ $90.0\%$ đến $95.3\%$.
- Cơ chế bám bẩn của thành phần SMPp:
  - SMPp phản ánh chính xác nhóm protein dạng thơm thuộc phân đoạn biopolymers bị màng giữ lại ưu tiên.
  - Nhóm protein này tham gia trực tiếp vào hiện tượng tắc nghẽn lỗ rỗng màng và bám bẩn hữu cơ không thể đảo ngược.

Bảng 4 (Table 4): Tổng hợp đặc tính hóa lý của bùn và dịch vi sinh tại ba trạm nguồn.
| Đối tượng hóa lý | Phương pháp phân tích | Dải đo thực nghiệm | Cơ chế tác động bám bẩn màng MBR |
| :--- | :--- | :--- | :--- |
| Đỉnh huỳnh quang EPS | Phổ huỳnh quang 3D (EEM) | $\text{Ex/Em} \approx 220\text{--}225 / 325\text{--}355\text{ nm}$ | Protein dạng thơm kích hoạt kết tụ bùn và bám dính ban đầu |
| Kích thước hạt bùn | Tán xạ laser hạt | Tập trung $20\text{--}40\ \mu\text{m}$ | Cấu trúc hạt dễ lắng đọng tạo thành lớp bánh bùn dày |
| Đỉnh huỳnh quang SMP | Phổ huỳnh quang 3D (EEM) | $\text{Ex/Em} \approx 220\text{--}230 / 330\text{--}350\text{ nm}$ | Protein hòa tan hấp phụ lên màng và bẫy trong lớp cặn |
| Phân đoạn hữu cơ SMP | Sắc ký rây LC-OCD | Hydrophilic DOC (humics và biopolymers) | Nguồn cung cấp chất hữu cơ bám bẩn vi mô |
| Tỷ lệ giữ lại biopolymers | Tính toán chênh lệch nồng độ | $90.0\%\text{--}95.3\%$ | Biopolymers bị giữ lại ưu tiên gây tắc nghẽn lỗ rỗng màng |

##### 3.2.3.4 Cơ sở cơ chế cho mô hình tiền huấn luyện LSTM-base
- Tính vững chắc của kiến trúc học máy:
  - Các đặc tính hóa lý nhất quán giữa ba trạm nguồn cung cấp bằng chứng cơ chế cho cấu trúc SHAP của LSTM-base.
  - Phân bổ trọng số của mô hình phản ánh đúng các tương tác sinh hóa tự nhiên thay vì trùng hợp thống kê ngẫu nhiên.
  - LSTM-base là mô hình cơ sở đáng tin cậy phục vụ quá trình chuyển giao tri thức sang trạm đích khan hiếm dữ liệu.

### 3.3 Hiệu năng và giải thích học chuyển giao (Transfer learning performance and interpretation)

#### 3.3.1 Ảnh hưởng của tỷ lệ tinh chỉnh đến hiệu năng học chuyển giao (Effect of fine-tuning ratio on transfer learning performance)

##### 3.3.1.1 Hiệu năng khi chuyển giao trực tiếp (Zero-shot transfer, FT = 0%)
- Định nghĩa điều kiện chuyển giao trực tiếp: Tỷ lệ tinh chỉnh $FT = 0\%$ đại diện cho quá trình chuyển giao không mẫu (zero-shot transfer). Mô hình tiền huấn luyện từ trạm nguồn dự báo trực tiếp trên trạm đích mà không qua thích ứng dữ liệu đích.
- Suy giảm hiệu năng của mô hình nguồn: Cả hai mô hình LSTM và XGBoost tiền huấn luyện đều cho hệ số xác định thấp. Mô hình LSTM đạt $R^2 = 0.41$. Mô hình XGBoost đạt $R^2 = 0.39$.
- Nguyên nhân suy giảm dự báo: Phân tích PCA trước đó xác nhận sự tồn tại của độ lệch phân phối (distribution shift) có thể đo lường được giữa trạm nguồn và trạm đích.
- Giới hạn của chuyển giao trực tiếp: Việc chỉ áp dụng chuyển giao trực tiếp không đủ độ tin cậy để dự báo áp suất xuyên màng ($\text{TMP}$) tại trạm xử lý mới [53].

##### 3.3.1.2 Động học cải thiện hiệu năng theo tỷ lệ tinh chỉnh (FT từ 10% đến 50%)
- Bước nhảy vọt ban đầu của LSTM-FT: Mức tăng hiệu năng lớn nhất xuất hiện khi nâng tỷ lệ tinh chỉnh từ $FT = 0\%$ lên $FT = 10\%$. Hệ số xác định $R^2$ tăng vọt từ $0.41$ lên $0.81$ (Hình 5(a)).
- Quỹ đạo cải thiện tiệm tiến của LSTM-FT: Khi tăng dần $FT$ từ $10\%$ đến $40\%$, hiệu năng mô hình tiếp tục tăng trưởng ổn định. Tại $FT = 40\%$, mô hình đạt $R^2 = 0.89$, sai số $\text{RMSE} = 0.50\text{ kPa}$ và $\text{MAE} = 0.33\text{ kPa}$ (Hình 5(b) và (c)).
- Hiện tượng bão hòa tại mức tinh chỉnh cao: Khi tăng lên $FT = 50\%$, mức cải thiện sai số và tương quan so với mức $FT = 40\%$ chỉ mang tính thứ yếu, không đáng kể.
- Quỹ đạo thích ứng của XGBoost-FT: Mô hình XGBoost-FT cũng cải thiện hiệu năng khi tăng tỷ lệ $FT$, nhưng tốc độ tăng chậm và biên độ cải thiện thấp hơn nhiều so với LSTM-FT.
- Số liệu tiến hóa của XGBoost-FT: Hệ số $R^2$ của XGBoost-FT chỉ tăng từ $0.39$ ở $FT = 0\%$ lên $0.58$ ở $FT = 40\%$, và đạt $0.61$ ở $FT = 50\%$.

##### 3.3.1.3 Điểm bão hòa tối ưu và độ ổn định mô hình tại FT = 40%
- Vượt trội của mô hình chuỗi thời gian: LSTM-FT tạo ra bước nhảy hiệu năng lớn ngay ở các mức dữ liệu đích rất thấp ($FT = 10\%$) so với XGBoost-FT. Việc bổ sung dữ liệu vượt quá $40\%$ không mang lại lợi ích gia tăng rõ rệt.
- Bản chất học chuyển giao trong điều kiện khan hiếm dữ liệu: Hai mô hình thích ứng từ mạng tiền huấn luyện trạm nguồn phản ánh năng lực thích ứng với tập dữ liệu đích hạn chế ($N = 71$ bản ghi thực tế), thay vì phát triển mô hình truyền thống từ đầu.
- Phân tích phương sai và độ phân tán mô hình: Độ lệch chuẩn (standard deviation) qua các phân đoạn tinh chỉnh và các lần lặp ngẫu nhiên đạt giá trị lớn nhất tại $FT = 10\%$. Độ phân tán này giảm dần khi tăng $FT$ và đạt mức rất nhỏ tại $FT = 40\%$.
- Giao thức đánh giá độ vững: Quá trình đánh giá sử dụng tối đa 6 phân đoạn dữ liệu liên tục từ kho tinh chỉnh và thử nghiệm trên 5 hạt giống ngẫu nhiên (random seeds) cho mỗi phân đoạn giữ lại.
- Cơ chế ổn định: Lượng dữ liệu đích quá ít làm giảm tính vững chắc của quá trình thích ứng. Một lượng dữ liệu đích vừa phải ($FT = 40\%$) đã đủ để mô hình đạt trạng thái ổn định cao nhất. Do đó, $FT = 40\%$ được chọn làm điều kiện chuẩn cho các phân tích chuyên sâu tiếp theo.

Bảng 5 (Table 5): So sánh động học hiệu năng dự báo theo tỷ lệ tinh chỉnh ($FT$) của mô hình LSTM-FT và XGBoost-FT.
| Tỷ lệ tinh chỉnh ($FT$) | LSTM-FT: $R^2$ | LSTM-FT: RMSE ($\text{kPa}$) | LSTM-FT: MAE ($\text{kPa}$) | XGBoost-FT: $R^2$ | Ghi chú trạng thái mô hình |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $0\%$ (Zero-shot) | $0.41$ | - | - | $0.39$ | Chuyển giao trực tiếp, lệch phân phối dữ liệu |
| $10\%$ | $0.81$ | - | - | - | Bước nhảy vọt lớn nhất, phương sai giữa các lần chạy cao |
| $20\%$ | - | - | - | - | Hiệu năng cải thiện tiệm tiến |
| $30\%$ | - | - | - | - | Cấu trúc phân bổ đặc trưng bắt đầu cân bằng |
| $40\%$ (Tối ưu) | $0.89$ | $0.50$ | $0.33$ | $0.58$ | Điểm bão hòa tối ưu, sai số tối thiểu, độ ổn định cao |
| $50\%$ | $0.89$ | - | - | $0.61$ | Lợi ích gia tăng bão hòa, cải thiện không đáng kể |


#### 3.3.2 So sánh hiệu năng giữa mô hình đường cơ sở và các mô hình học chuyển giao (Performance comparison of baseline model and transfer learning models)

##### 3.3.2.1 Phân bố mẫu thử nghiệm và độ lệch dự báo TMP
- Miền giá trị mẫu thử nghiệm: Tập mẫu thử nghiệm tại trạm đích phân bố chủ yếu trong dải áp suất xuyên màng $\text{TMP} \approx 19\text{--}21.5\text{ kPa}$. Một số lượng ít mẫu thử phân bố ở dải $\text{TMP}$ thấp hơn từ $15.5\text{--}18\text{ kPa}$ (Hình 5(d)).
- Độ chụm quỹ đạo của LSTM-FT: Trong toàn bộ dải $\text{TMP}$, các điểm dự báo của LSTM-FT ($FT = 40\%$) phân bố sát nhất quanh đường phân giác lý tưởng ($y = x$), thể hiện độ tương thích cao nhất giữa giá trị dự báo và giá trị quan trắc thực tế.
- Sai lệch của mô hình đường cơ sở: Mô hình đường cơ sở (Baseline model huấn luyện thuần túy trên dữ liệu trạm đích) thể hiện các độ lệch phân tán ở mức trung bình.
- Độ phân tán nghiêm trọng của XGBoost-FT: Mô hình XGBoost-FT thể hiện vùng phân tán rộng nhất và rời xa rõ rệt nhất khỏi đường phân giác lý tưởng.

##### 3.3.2.2 So sánh định lượng giữa LSTM-FT, XGBoost-FT và Baseline
- Sai số của mô hình đường cơ sở trạm đích: Mô hình Baseline thuần túy chỉ sử dụng tập dữ liệu đích đạt $R^2 = 0.82$, sai số $\text{RMSE} = 0.63\text{ kPa}$ và $\text{MAE} = 0.45\text{ kPa}$.
- Cải thiện vượt trội của LSTM-FT: So với mô hình đường cơ sở, LSTM-FT giảm sai số $\text{RMSE}$ từ $0.63\text{ kPa}$ xuống $0.50\text{ kPa}$ (giảm $20.6\%$). Mô hình giảm sai số $\text{MAE}$ từ $0.45\text{ kPa}$ xuống $0.33\text{ kPa}$ (giảm $26.7\%$). Hệ số xác định $R^2$ tăng từ $0.82$ lên $0.89$.
- Thất bại của XGBoost-FT trong việc thích ứng: Mô hình XGBoost-FT không mang lại lợi thế chuyển giao. Sai số $\text{RMSE}$ tăng vọt lên $0.96\text{ kPa}$. Sai số $\text{MAE}$ tăng lên $0.81\text{ kPa}$. Hệ số xác định $R^2$ sụt giảm xuống mức thấp $0.58$.
- Khẳng định tính hiệu quả của mạng hồi quy: Phương pháp học chuyển giao phát huy tối đa hiệu quả khi kết hợp với cấu trúc mạng nơ-ron hồi quy LSTM, vượt qua cả mô hình nội tại trạm đích và mô hình cây quyết định tăng cường.

Bảng 6 (Table 6): So sánh định lượng hiệu năng trên tập kiểm tra trạm đích tại $FT = 40\%$.
| Mô hình đánh giá | $R^2$ | RMSE ($\text{kPa}$) | MAE ($\text{kPa}$) | Tỷ lệ giảm RMSE so với Baseline | Tỷ lệ giảm MAE so với Baseline |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LSTM-FT** | $\mathbf{0.89}$ | $\mathbf{0.50}$ | $\mathbf{0.33}$ | $\mathbf{-20.6\%}$ | $\mathbf{-26.7\%}$ |
| **Target Baseline** | $0.82$ | $0.63$ | $0.45$ | Quy chuẩn cơ sở ($0\%$) | Quy chuẩn cơ sở ($0\%$) |
| **XGBoost-FT** | $0.58$ | $0.96$ | $0.81$ | $+52.4\%$ (Tăng sai số) | $+80.0\%$ (Tăng sai số) |

##### 3.3.2.3 Nguyên nhân kiến trúc LSTM vượt trội hơn XGBoost trong học chuyển giao chuỗi thời gian
- Bản chất tích lũy lịch sử của bám bẩn màng: Hiện tượng tắc nghẽn màng lọc trong hệ thống MBR diễn ra qua chuỗi tích tụ liên tục theo thời gian của các hạt keo, bông bùn và hợp chất cao phân tử trên bề mặt màng.
- Cơ chế bộ nhớ cổng của LSTM: Mạng LSTM sở hữu các cổng quên (forget gate), cổng vào (input gate) và cổng ra (output gate). Cấu trúc này cho phép lưu giữ thông tin phụ thuộc thời gian dài hạn và quy luật suy thoái màng từ trạm nguồn.
- Điểm yếu cố hữu của XGBoost dạng bảng: Cấu trúc cây quyết định phân vùng của XGBoost giả định các mẫu quan sát độc lập tĩnh. Thuật toán không nắm bắt được mối liên hệ chuỗi thời gian và sự phụ thuộc trễ của các chu kỳ lọc - rửa ngược.
- Hiện tượng quá khớp do cỡ mẫu nhỏ: Khi trạm đích bị hạn chế dữ liệu ($N = 41$ mẫu huấn luyện trong tổng số $71$ bản ghi), mô hình Baseline thuần túy dễ rơi vào hiện tượng quá khớp (overfitting) cục bộ. Trong khi đó, LSTM-FT tận dụng trọng số biểu diễn sâu trạm nguồn để dẫn hướng tối ưu hóa chính xác.


#### 3.3.3 Giải thích đóng góp đặc trưng trong quá trình chuyển giao bằng LOFO và SHAP (LOFO and SHAP interpretation of feature contributions during transfer)

##### 3.3.3.1 Phân tích độ nhạy loại bỏ một đặc trưng (LOFO analysis tại FT = 40%)
- Giao thức phân tích LOFO: Phân tích Leave-One-Feature-Out (LOFO) đánh giá trực tiếp vai trò của từng biến đầu vào trên mô hình LSTM-FT tại điều kiện chuẩn $FT = 40\%$ (Hình 5(e)).
- Mô hình tham chiếu đầy đủ: Mô hình tham chiếu huấn luyện với toàn bộ các biến đầu vào đạt sai số $\text{MAE} = 0.33\text{ kPa}$.
- Quy chuẩn kiểm định thống kê: Sự suy giảm hiệu năng khi loại bỏ từng biến được kiểm tra qua kiểm định cặp dấu hạng Wilcoxon hai phía (paired two-sided Wilcoxon signed-rank tests, Bảng S10).
- Tác động áp đảo của EPSc: Việc loại bỏ đặc trưng polysaccharide ngoại bào ($\text{EPSc}$) gây ra tổn thất hiệu năng nghiêm trọng nhất. Sai số $\text{MAE}$ tăng vọt từ $0.33\text{ kPa}$ lên $0.37\text{ kPa}$ ($p \le 0.001$). Điều này xác nhận $\text{EPSc}$ là biến quan trọng nhất duy trì độ chính xác của LSTM-FT.
- Tác động của protein ngoại bào và tuổi bùn: Khi loại bỏ đặc trưng protein ngoại bào ($\text{EPSp}$) hoặc thời gian lưu giữ bùn ($\text{SRT}$), sai số $\text{MAE}$ cùng tăng lên mức $0.35\text{ kPa}$ với ý nghĩa thống kê cao ($p \le 0.001$).
- Tác động của thông lượng màng: Loại bỏ biến thông lượng ($\text{FLUX}$) làm tăng nhẹ sai số nhưng vẫn đạt độ tin cậy thống kê ($p \le 0.01$).
- Kết luận từ kiểm định LOFO: Các biến liên quan đến EPS, đặc biệt là $\text{EPSc}$ và $\text{EPSp}$, chi phối áp đảo hiệu năng mô hình chuyển giao. Các biến vận hành $\text{SRT}$ và $\text{FLUX}$ đóng vai trò bổ trợ thứ cấp.

Bảng 7 (Table 7): Kết quả phân tích độ nhạy loại bỏ từng biến (LOFO) của mô hình LSTM-FT tại $FT = 40\%$.
| Biến đầu vào bị loại trừ | MAE sau khi loại biến ($\text{kPa}$) | Mức tăng sai số so với chuẩn | Giá trị p (Wilcoxon test) | Mức độ ý nghĩa thống kê |
| :--- | :--- | :--- | :--- | :--- |
| **Mô hình tham chiếu (Đầy đủ)** | $\mathbf{0.33}$ | $0.00$ | - | Điểm chuẩn tham chiếu |
| $\text{EPSc}$ (EPS polysaccharide) | $0.37$ | $+0.04$ | $p \le 0.001$ | Tác động nghiêm trọng nhất |
| $\text{EPSp}$ (EPS protein) | $0.35$ | $+0.02$ | $p \le 0.001$ | Rất quan trọng |
| $\text{SRT}$ (Tuổi bùn) | $0.35$ | $+0.02$ | $p \le 0.001$ | Quan trọng |
| $\text{FLUX}$ (Thông lượng lọc) | - | Nhỏ hơn | $p \le 0.01$ | Có ý nghĩa thống kê |

##### 3.3.3.2 Động thái tiến hóa phân bổ giá trị SHAP qua các mức FT
- Trạng thái chuyển giao không mẫu ($FT = 0\%$): Biến $\text{EPSc}$ đứng vị trí số 1 tuyệt đối, chiếm tỷ trọng quy gán giá trị SHAP lớn nhất, vượt xa các biến $\text{MLVSS}$ và $\text{EPSp}$ (Hình 6(b), Hình S8(a)). Mô hình bảo toàn quán tính cấu trúc quy gán tập trung vào $\text{EPSc}$ học được từ trạm nguồn.
- Giai đoạn chuyển tiếp ($FT = 10\%\text{--}30\%$): Cấu trúc quy gán SHAP trở nên phân bổ đồng đều hơn. Mức đóng góp của $\text{EPSp}$ tăng trưởng rõ rệt. Đóng góp của $\text{EPSc}$, $\text{SRT}$ và $\text{MLVSS}$ tiến dần đến trạng thái tương đương nhau (Hình S9 và S10).
- Trạng thái hoàn thiện tối ưu ($FT = 40\%$): Hai biến $\text{EPSc}$ và $\text{EPSp}$ trở thành hai đặc trưng xếp hạng cao nhất. Tổng giá trị đóng góp của $\text{EPSc}$ và $\text{EPSp}$ chiếm hơn $50\%$ tổng quy gán toàn mô hình (Hình 6(c), Hình S8(b)).
- Trạng thái bão hòa ổn định ($FT = 50\%$): Cấu trúc phân hạng đặc trưng và giá trị SHAP tại $FT = 50\%$ gần như trùng khớp hoàn toàn với trạng thái tại $FT = 40\%$ (Hình S11). Điều này giải thích hiện tượng bão hòa hiệu năng khi tăng tỷ lệ dữ liệu đích.

##### 3.3.3.3 Cấu trúc quy gán đặc trưng tập trung vào EPS sau tinh chỉnh
- Sự tái định chuẩn trọng số: Quá trình tinh chỉnh không xóa bỏ tri thức nguồn mà tái định chuẩn (recalibrate) trọng số để phù hợp với môi trường sinh hóa mới.
- Vị thế song hành của hệ EPS: Kết quả LOFO và SHAP hội tụ tại một kết luận then chốt: $\text{EPSc}$ duy trì vai trò rường cột bất biến, trong khi $\text{EPSp}$ được đánh thức và nâng tầm ảnh hưởng để phản ánh cấu trúc lớp bám bẩn trạm đích.


#### 3.3.4 Cơ chế khoa học giúp học chuyển giao dự báo chính xác bám bẩn màng tại trạm đích (Mechanistic physicochemical evidence for transfer learning)

##### 3.3.4.1 Vai trò nền tảng phổ quát của EPSc trong ma trận bám bẩn màng
- Tri thức bám bẩn phổ quát được bảo lưu: Tại $FT = 0\%$, mô hình tiền huấn luyện vẫn giữ được độ chính xác nhất định ($R^2 = 0.41$) nhờ cấu trúc quy gán tập trung vào $\text{EPSc}$. Quy luật polysaccharide thúc đẩy bám bẩn là một đặc tính phổ quát giữa các trạm xử lý sinh học.
- Nồng độ polysaccharide cao tại trạm đích: Phân tích thực nghiệm cho thấy nồng độ $\text{EPSc}$ tại trạm đích đạt mức rất cao là $49.6\text{ mg/L}$.
- Cơ chế tạo lớp bánh bùn ngậm nước: Polysaccharide mang nhiều nhóm chức ưa nước (-OH). Nồng độ $\text{EPSc}$ cao làm tăng khả năng giữ nước tự do và ức chế khả năng tách nước của bùn hoạt tính. Quá trình này hình thành lớp bánh bùn có độ hydrat hóa cao, độ nén ép lớn và sức cản thủy lực đặc biệt cao.
- Bằng chứng kiểm chứng qua thời gian hút mao dẫn: Trạm đích ghi nhận giá trị thời gian hút mao dẫn cao $\text{CST} = 49.45\text{ s}$ và thời gian hút mao dẫn riêng đạt $4.36\text{ s/(g/L)}$ (Hình 7(a)). Các số liệu này xác nhận $\text{EPSc}$ đại diện cho ma trận bám bẩn cốt lõi được bảo lưu nguyên vẹn qua quá trình chuyển giao.

##### 3.3.4.2 Tương tác Fe-EPS thúc đẩy vai trò EPSp và nén chặt lớp bánh bùn
- Hiện tượng gia tăng độ nhạy với EPSp: Khi mô hình đạt hiệu năng đỉnh cao tại $FT = 40\%$ ($R^2 = 0.89$), biến $\text{EPSp}$ vươn lên thành đặc trưng quan trọng thứ hai trong SHAP. Quá trình tinh chỉnh đã giúp mạng LSTM nhận thức được tín hiệu protein ngoại bào đặc thù của trạm đích.
- Dấu vết huỳnh quang protein thơm: Phổ ma trận kích thích - phát xạ huỳnh quang ($\text{EEM}$) của mẫu EPS trạm đích ghi nhận đỉnh tín hiệu vượt trội của các hợp chất giống protein thơm (aromatic protein-like peak, Hình 7(b)).
- Ảnh hưởng từ điều kiện châm sắt ($\text{Fe}^{3+}$): Nước thải đầu vào của trạm đích được bổ sung sắt nhằm tăng cường keo tụ photpho [54]. Nghiên cứu so sánh hai giai đoạn định lượng Fe tại bể khuấy trộn trước xử lý với nồng độ mục tiêu là $9\text{ mg/L}$ và $26\text{ mg/L}$ (Bảng S11).
- Tích lũy sắt và phản ứng tăng tiết EPSp: Khi liều lượng Fe tăng từ $9$ lên $26\text{ mg/L}$:
  - Hàm lượng sắt liên kết trong bùn tăng từ $45\text{ mg/g-MLVSS}$ lên $101\text{ mg/g-MLVSS}$.
  - Nồng độ $\text{EPSp}$ trong bùn tăng tương ứng từ $47.96\text{ mg/g-MLVSS}$ lên $62.30\text{ mg/g-MLVSS}$.
- Cơ chế nén chặt và bám dính bề mặt màng: Các phân tử protein chứa nhiều chuỗi bên kỵ nước. Sự gia tăng nồng độ $\text{EPSp}$ kết hợp với cầu nối cation đa hóa trị $\text{Fe}^{3+}$ thúc đẩy liên kết liên phân tử, làm tăng tính kỵ nước cục bộ và cường độ kết tụ bông bùn. Hiện tượng này gia tăng độ bám dính lên bề mặt màng và nén đặc lớp bánh bùn [46, 55].
- Bằng chứng đo độ nhớt bùn: Hỗn dịch bùn trạm đích có độ nhớt biểu kiến lên tới $50.03\text{ mPa}\cdot\text{s}$ và độ nhớt riêng đạt $9.46\text{ mPa}\cdot\text{s/(g/L)}$ (Hình 7(d)). Các giá trị này chứng minh tính nén chặt cao của ma trận bùn giàu Fe-EPSp.

##### 3.3.4.3 Bằng chứng thực nghiệm từ quy trình rửa hóa chất tại chỗ (Two-step CIP)
- Giao thức rửa hóa chất hai giai đoạn: Màng lọc trước khi rửa được tháo cạn và tráng sạch bằng nước sau lọc. Quy trình CIP gồm 2 bước liên tiếp: rửa axit citric ($\text{CA}$, $15\text{ g/L}$, $\text{pH} = 2.5$) sau đó rửa natri hypoclorit ($\text{NaClO}$, $1\text{ g/L}$, $\text{pH} = 10$).
- Giai đoạn hòa tan sắt bằng axit citric: Trong dung dịch rửa axit citric, nồng độ sắt tổng số tăng đột biến từ $0.62\text{ mg/L}$ lên $43.02\text{ mg/L}$ (Hình 7(e)). Kết quả này chứng minh sự tồn tại của một lượng lớn các hợp chất chứa sắt kết tủa trong lớp bám bẩn.
- Giai đoạn oxy hóa chất hữu cơ bằng NaClO: Trong dung dịch rửa kiềm oxy hóa $\text{NaClO}$, nồng độ tổng cacbon hữu cơ ($\text{TOC}$) tăng vọt từ $5.19\text{ mg/L}$ lên $43.22\text{ mg/L}$ (Hình 7(f)). Đồng thời nồng độ sắt tổng số tiếp tục tăng từ $1.85\text{ mg/L}$ lên $11.16\text{ mg/L}$.
- Bản chất lớp bám bẩn chính: Sự giải phóng đồng thời của hợp chất hữu cơ bị oxy hóa và các ion kim loại sắt, cùng với sự chênh lệch lớn giữa COD hòa tan ($\text{SCOD} = 93\text{ mg/L}$) và COD tổng số ($\text{TCOD} = 271\text{ mg/L}$), khẳng định lớp bám bẩn bề mặt màng không hình thành từ chất hữu cơ hòa tan đơn thuần. Lớp tắc nghẽn chủ đạo là một ma trận hữu cơ liên kết bùn hoạt tính kết hợp chặt chẽ với các thành phần vô cơ chứa sắt.

##### 3.3.4.4 Cơ chế suy giảm đóng góp của SMPp do sự xuyên màng không giữ lại
- Xu hướng hạ thấp tỷ trọng của SMPp: Phân tích SHAP cho thấy đóng góp của protein hòa tan ($\text{SMPp}$) giảm dần sau khi mô hình được tinh chỉnh.
- Phổ huỳnh quang của SMP và nước sau lọc: Mặc dù phổ huỳnh quang EEM của dịch SMP trạm đích có tín hiệu protein thơm vùng kích thích thấp (Hình 7(c)), phổ EEM của dòng nước sau lọc (effluent) cũng xuất hiện các dải huỳnh quang mở rộng tương đồng tại tọa độ $\text{Ex/Em} \approx 220\text{--}250 / 300\text{--}460\text{ nm}$ (Hình S12).
- Hiện tượng xuyên màng tự do: Sự trùng lặp quang phổ huỳnh quang chứng minh phần lớn các phân tử protein hòa tan kích thước nhỏ không bị màng lọc giữ lại mà đi xuyên qua các lỗ màng vào nước thành phẩm.
- Nhận thức chuẩn xác của mạng nơ-ron: Vì $\text{SMPp}$ tự do thoát qua màng nên nó không tham gia tích cực vào việc tạo thành lớp bánh bám bẩn bề mặt. Mạng LSTM-FT sau tinh chỉnh đã học được thực tế vật lý này và tự động giảm bớt trọng số quy gán cho $\text{SMPp}$.

##### 3.3.4.5 Bản chất nhận thức của mô hình học chuyển giao qua tinh chỉnh
- Tóm tắt cơ chế ba mũi nhọn:
  1. Bảo lưu tri thức bám bẩn polysaccharide ngoại bào ($\text{EPSc}$) mang tính phổ quát chuyển giao từ trạm nguồn.
  2. Tái hiệu chỉnh để nâng cao độ nhạy với tín hiệu protein ngoại bào ($\text{EPSp}$) do tương tác giàu sắt đặc thù tại trạm đích.
  3. Giảm bớt sự phụ thuộc vào protein hòa tan ($\text{SMPp}$) vì thành phần này đi xuyên qua màng lọc.


#### 3.3.5 Khả năng thích ứng xuyên kịch bản sang MBR xử lý nước thải công nghiệp (Cross-scenario adaptability to an industrial wastewater MBR)

##### 3.3.5.1 Bối cảnh vận hành khắc nghiệt và đặc tính bùn nước thải công nghiệp
- Quy mô kiểm chứng độc lập: Thử nghiệm thẩm định bổ sung thực hiện trên hệ thống MBR quy mô pilot xử lý nước thải công nghiệp hỗn hợp hóa dầu và dược phẩm.
- Thách thức phân phối khắc nghiệt: Nước thải công nghiệp có thành phần hóa học phức tạp, tải trọng hữu cơ biến động mạnh và động học sinh khối thường xuyên chịu các cú sốc tải vận hành.
- Diễn biến áp suất bất thường: Đồ thị $\text{TMP}$ thể hiện một xu hướng tăng dài hạn kèm theo nhiều đợt dao động đột biến do các sự cố kỹ thuật thực tế (Hình 8(a)).
- So sánh các thông số hóa lý cốt lõi: Nước thải và bùn công nghiệp có các chỉ số $\text{TCOD}$, $\text{SCOD}$, $\text{MLSS}$ và $\text{MLVSS}$ cao hơn vượt trội so với các trạm nguồn sinh hoạt (Hình 8(b)).
- Các đặc trưng bám bẩn tương đồng then chốt:
  - Hàm lượng $\text{EPSc}$ trạm công nghiệp đạt $43.6 \pm 20.2\text{ mg/L}$, nằm sát dải trạm nguồn ($32.3\text{--}43.5\text{ mg/L}$).
  - Hàm lượng $\text{EPSp}$ đạt $256.8 \pm 126.7\text{ mg/L}$, cùng bậc độ lớn với trạm nguồn ($184\text{--}229\text{ mg/L}$).
  - Hàm lượng $\text{SMPc}$ đạt $6.9 \pm 5.0\text{ mg/L}$, nằm hoàn toàn trong dải trạm nguồn ($5.2\text{--}11.5\text{ mg/L}$).
  - Sự giao thoa này là cơ sở vật lý cho phép học chuyển giao thành công qua các kịch bản nước thải khác biệt sâu sắc.

##### 3.3.5.2 Hiệu năng chuyển giao không mẫu và phục hồi vượt bậc sau tinh chỉnh (FT = 40%)
- Giới hạn khi chưa tinh chỉnh ($FT = 0\%$): Mô hình LSTM nguồn chỉ đạt hiệu năng khiêm tốn trên MBR công nghiệp với $R^2 = 0.46$ (Hình 8(c)). Tri thức trạm nguồn chỉ nắm bắt được một phần động học $\text{TMP}$.
- Bước nhảy vọt sau tinh chỉnh tại $FT = 40\%$: Áp dụng quy trình tinh chỉnh theo thời gian thực chuẩn hóa mà không cần thay đổi kiến trúc mô hình giúp phục hồi hiệu năng xuất sắc:
  - Hệ số xác định $R^2$ tăng vọt từ $0.46$ lên $0.89$ (và đạt $0.90$ trên đồ thị phân tán Hình 8(c)).
  - Sai số $\text{MAE}$ giảm mạnh $68.6\%$ so với mức $FT = 0\%$.
  - Sai số $\text{RMSE}$ giảm mạnh $54.7\%$ so với mức $FT = 0\%$.
- Khẳng định tính tương thích thực tế: Khung học chuyển giao có khả năng áp dụng linh hoạt trên nền nước thải công nghiệp mà không đòi hỏi tái cấu trúc thuật toán hay tối ưu hóa siêu tham số phức tạp.

Bảng 8 (Table 8): Hiệu năng chuyển giao mô hình LSTM trên hệ thống MBR nước thải công nghiệp.
| Điều kiện tinh chỉnh | $R^2$ | Biến thiên MAE so với $FT = 0\%$ | Biến thiên RMSE so với $FT = 0\%$ | Đánh giá trạng thái mô hình |
| :--- | :--- | :--- | :--- | :--- |
| **$FT = 0\%$ (Zero-shot)** | $0.46$ | Điểm chuẩn gốc ($0\%$) | Điểm chuẩn gốc ($0\%$) | Nắm bắt được xu thế thô, sai số lớn do sốc tải |
| **$FT = 40\%$ (Sau tinh chỉnh)** | $\mathbf{0.89\text{--}0.90}$ | $\mathbf{-68.6\%}$ (Giảm sâu) | $\mathbf{-54.7\%}$ (Giảm sâu) | Khôi phục dự báo chính xác cao, thích ứng hoàn hảo |

##### 3.3.5.3 Tái hiệu chỉnh cấu trúc SHAP: Sự trỗi dậy của SMPp do sốc tải sinh khối
- Bảo tồn vị trí số 1 của EPSc: Phân tích SHAP sau tinh chỉnh cho thấy $\text{EPSc}$ tiếp tục giữ vị thế đặc trưng quan trọng nhất (Hình 8(d)), tái khẳng định vai trò trụ cột bất biến của polysaccharide.
- Vươn lên vị trí số 2 của protein hòa tan: Khác biệt hoàn toàn với trạm sinh hoạt đích (nơi $\text{EPSp}$ đứng thứ 2), tại MBR công nghiệp, biến $\text{SMPp}$ vươn lên thành đặc trưng quan trọng thứ hai sau tinh chỉnh.
- Cơ chế giải thích nồng độ SMPp tăng vọt: Nồng độ $\text{SMPp}$ trung bình trong MBR công nghiệp đạt tới $27.6 \pm 17.4\text{ mg/L}$, cao gấp đôi so với các trạm nguồn ($10.8\text{--}13.8\text{ mg/L}$).
- Ảnh hưởng của sốc tải độc tính và suy thoái tế bào: Trong nước thải công nghiệp hóa dược, các đợt sốc tải hóa chất gây độc tính ức chế vi sinh vật, làm giảm mật độ bùn $\text{MLSS}$ và $\text{MLVSS}$ [56].
- Quá trình phân hủy tế bào sinh khối giải phóng ồ ạt các protein hòa tan ($\text{SMPp}$) vào dịch hỗn dịch.
- Hình thành bám bẩn từ keo protein công nghiệp: Dịch SMP trong trạm công nghiệp bị chi phối bởi protein thay vì carbohydrate. Khối lượng lớn protein hòa tan tích tụ dưới điều kiện biến động vận hành đóng vai trò là tác nhân chính gây tắc nghẽn lỗ màng và kết tụ lớp bám bẩn. Mô hình sau tinh chỉnh đã thích ứng chính xác với tín hiệu $\text{SMPp}$ trỗi dậy này.

##### 3.3.5.4 Tính phổ quát và linh hoạt của khung học chuyển giao xuyên kịch bản
- Tính thống nhất của cơ chế bám bẩn xuyên hệ thống: Khung học chuyển giao thành công giữa các kịch bản nước thải không phải vì cơ chế bám bẩn hoàn toàn đồng nhất, mà vì mô hình tách biệt được hai nhóm tri thức:
  - **Tri thức bất biến chung (Transferable Core)**: Quy luật bám bẩn nền do $\text{EPSc}$ chi phối được bảo toàn qua mọi hệ thống MBR.
  - **Tri thức thích ứng cục bộ (Plant-Specific Adaptation)**: Quá trình tinh chỉnh tái định chuẩn linh hoạt cấu trúc quy gán hướng về tác nhân xung yếu nhất của từng trạm:
    - Trạm sinh hoạt giàu sắt: Tái định chuẩn nhạy bén với $\text{EPSp}$ (tương tác keo tụ kết dính Fe-Protein).
    - Trạm công nghiệp chịu sốc tải: Tái định chuẩn nhạy bén với $\text{SMPp}$ (suy thoái sinh khối giải phóng protein hòa tan).
- Ý nghĩa công nghệ: Nghiên cứu cung cấp giải pháp dự báo bám bẩn màng đáng tin cậy cho các trạm MBR mới vận hành hoặc trạm công nghiệp thiếu dữ liệu lịch sử dài hạn, giải quyết rào cản khan hiếm dữ liệu trong công nghệ màng sinh học.

## 4. Ý nghĩa thực tiễn và triển vọng tương lai (Implications and Outlook)

### 4.1 Khắc phục rào cản chi phí và tối ưu hóa giám sát bám bẩn màng
- Giải quyết bài toán khan hiếm dữ liệu sinh hóa chuyên sâu:
  - Đo đạc thông số vi sinh hòa tan (SMP) và polyme ngoại bào (EPS) tốn nhiều thời gian.
  - Phân tích EPS carbohydrate (EPSc) và EPS protein (EPSp) đòi hỏi quy trình chiết tách nhiệt hóa học phức tạp.
  - Các trạm MBR quy mô pilot hoặc trạm công nghiệp nhỏ thường thiếu ngân sách và nhân lực phân tích định kỳ.
  - Phương pháp học chuyển giao (Transfer Learning) giải quyết rào cản chi phí này.
  - Mô hình chuyển giao tri thức từ trạm nguồn giàu dữ liệu sang trạm đích thiếu dữ liệu.
  - Trạm đích không cần xây dựng cơ sở dữ liệu bám bẩn lại từ đầu.
- Tín hiệu quang phổ thay thế trực tuyến (Surrogate Fingerprints):
  - Phân tích ngoại tuyến các biến EPSc và EPSp gây ra độ trễ thời gian lớn.
  - Nhóm nghiên cứu đề xuất sử dụng tín hiệu quang phổ trực tuyến làm biến thay thế (surrogate markers).
  - Quang phổ tử ngoại - khả kiến (UV-vis) cung cấp thông tin liên tục về chất hữu cơ hòa tan.
  - Bản đồ huỳnh quang kích thích - phát xạ (EEM) ghi nhận nhanh các nhóm chất giống protein và humic [57].
  - Các dấu vân tay quang phổ này cho phép mô hình học máy tự thích ứng với biến động chất lượng nước theo thời gian thực.

### 4.2 Ứng dụng điều khiển dự báo cấp tiến và bản sao số (Digital Twin)
- Hệ thống điều khiển dự báo cấp tiến (Feedforward Control):
  - Mô hình LSTM tinh chỉnh (LSTM-FT) dự báo chính xác áp suất xuyên màng TMP trước nhiều giờ hoặc nhiều ngày.
  - Vận hành viên chủ động điều chỉnh cường độ sục khí màng trước khi áp suất tăng vọt.
  - Hệ thống tự động tối ưu hóa chu kỳ hút lọc và rửa ngược định kỳ.
  - Điều khiển cấp tiến triệt tiêu độ trễ phản hồi so với phương pháp điều khiển hồi tiếp truyền thống (Feedback Control).
- Kiến trúc bản sao số (Digital Twin) và giám sát thông minh IoT:
  - Bản sao số mô phỏng liên tục quá trình tích tụ lớp bánh bùn (cake layer) trên bề mặt màng.
  - Cảm biến IoT truyền dữ liệu vận hành gồm lưu lượng màng ($J$), TMP, oxy hòa tan (DO), pH, MLSS và nhiệt độ.
  - Thuật toán AI phân tích xu hướng tích lũy trở lực lọc và phát hiện sớm hiện tượng bám bẩn bất thường.
  - Hệ thống hỗ trợ ra quyết định xác định thời điểm tẩy rửa hóa chất tại chỗ (CIP) tối ưu (Hình S13).
  - Quy trình vận hành tối ưu giúp tiết kiệm năng lượng sục khí, giảm hóa chất tẩy rửa và kéo dài tuổi thọ màng.
- Khuyến nghị tần suất lấy mẫu tối thiểu cho các trạm pilot mới:
  - Giai đoạn khởi động trạm mới chỉ cần thu thập một chuỗi mẫu hóa lý ngắn hạn ghép cặp.
  - Tỷ lệ tinh chỉnh $40\%$ tương ứng với khoảng 16 đến 20 điểm đo thực nghiệm đầy đủ.
  - Sau khi nạp đủ lượng dữ liệu nhỏ này, mô hình hoàn thành quá trình tái hiệu chuẩn trọng số.
  - Sau giai đoạn tinh chỉnh, hệ thống chủ yếu dựa vào các cảm biến vận hành trực tuyến sẵn có để dự báo dài hạn.

### 4.3 Giới hạn hiện tại và định hướng nghiên cứu mở rộng
- Khoảng cách quy mô giữa hệ thống pilot và nhà máy xử lý nước thải quy mô thực tế (Full-Scale MBR):
  - Nghiên cứu hiện tại phát triển trên 4 hệ thống MBR quy mô pilot với điều kiện vận hành tương đối ổn định.
  - Tại nhà máy quy mô đầy đủ, thủy lực dòng chảy và phân bố bọt khí sục thay đổi theo không gian bể lọc [58].
  - Biến động tải trọng hữu cơ và lưu lượng nước thải đô thị biến thiên mạnh hơn so với trạm pilot.
  - Mối quan hệ tiền huấn luyện từ trạm pilot có thể chưa phản ánh hết động học bám bẩn phức tạp ở quy mô thương mại.
  - Nhóm tác giả kiến nghị mở rộng kiểm thực mô hình trên các tập dữ liệu lớn hơn từ nhiều vùng địa lý khác nhau.
- Đóng góp của bám bẩn vô cơ và tính chưa toàn diện của tập đặc trưng:
  - Hệ số xác định của mô hình đích đạt $R^2 = 0.89$, chưa đạt mức tuyệt đối ($1.00$).
  - Kết quả tẩy rửa hóa chất CIP tại trạm đích cho thấy sự hiện diện rõ nét của bám bẩn vô cơ chứa sắt (Fe fouling).
  - Tập dữ liệu đầu vào hiện tại tập trung chủ yếu vào các hợp chất hữu cơ sinh học (EPS và SMP).
  - Tập biến này chưa bao gồm nồng độ ion kim loại tự do ($\text{Fe}^{3+}$, $\text{Ca}^{2+}$, $\text{Mg}^{2+}$) và độ kiềm.
  - Bổ sung các chỉ số vô cơ sẽ giúp nâng cao độ chính xác dự báo khi nước thải đầu vào có nồng độ muối khoáng cao.
- Phát triển mô hình lai vật lý - trí tuệ nhân tạo (Hybrid Physical-AI Models):
  - Các mô hình thuần dữ liệu (data-driven) dễ mất tính khái quát khi gặp các sự cố quá tải đột ngột.
  - Hướng nghiên cứu tiếp theo sẽ kết hợp phương trình trở lực màng mắc nối tiếp (resistance-in-series) với mạng LSTM.
  - Mô hình vật lý cung cấp khung ràng buộc bảo toàn vật chất và thủy lực màng.
  - Mạng nơ-ron học các phi tuyến phức tạp sinh ra từ tương tác vi sinh và hóa học nước thải.
  - Cấu trúc lai giúp tăng độ tin cậy và đảm bảo tính giải thích vật lý vững chắc.


## 5. Kết luận then chốt của công trình (Key Conclusions)

### 5.1 Bốn kết luận khoa học và thực tiễn cốt lõi
- Kết luận 1: Tính khả thi của mô hình cơ sở tiền huấn luyện (LSTM-base) trên các trạm nguồn:
  - Nhóm tác giả xây dựng thành công mô hình cơ sở tiền huấn luyện trên dữ liệu tổng hợp từ 3 trạm MBR nguồn.
  - Phân tích SHAP chứng minh mô hình LSTM-base nắm bắt quy luật bám bẩn mang bản chất hóa lý rõ ràng.
  - Ba đặc trưng quyết định dự báo gồm EPSc, EPSp và SMPp, thay vì phụ thuộc đơn lẻ vào một biến vận hành.
  - Kết quả này phù hợp với các đặc tính chung của trạm nguồn: phổ huỳnh quang protein thơm, kích thước hạt bùn bông và xu hướng giữ lại SMP của màng lọc.
  - Mô hình LSTM-base tạo tiền đề tri thức vững chắc cho quá trình chuyển giao học máy sang các trạm mới.
- Kết luận 2: Vai trò của tỷ lệ tinh chỉnh (FT Ratio) và cơ chế hóa lý qua SHAP và LOFO:
  - Tinh chỉnh mô hình với tập dữ liệu nhỏ của trạm đích giúp cải thiện vượt bậc độ chính xác dự báo áp suất TMP.
  - Mô hình LSTM-FT đạt hệ số xác định $R^2 = 0.89$, $\text{RMSE} = 0.41\text{ kPa}$ và $\text{MAE} = 0.33\text{ kPa}$ ở mức $\text{FT} = 40\%$.
  - Phân tích SHAP và LOFO chỉ ra rằng biến EPSc tiếp tục đóng vai trò nền tảng bám bẩn ổn định.
  - Đồng thời, tầm quan trọng của biến EPSp tăng rõ rệt sau khi tinh chỉnh mô hình.
  - Sự thay đổi này phù hợp hoàn toàn với điều kiện nước thải giàu sắt ($10\text{--}30\text{ mg/L Fe}$) tại trạm đích.
  - Ion sắt liên kết mạnh với protein ngoại bào tạo thành lớp bám bẩn hữu cơ - vô cơ đặc thù.
- Kết luận 3: Khả năng thích ứng xuyên kịch bản (Cross-Scenario Adaptability) với nước thải công nghiệp:
  - Nhóm nghiên cứu thử nghiệm thành công mô hình trên trạm MBR xử lý nước thải công nghiệp hóa dầu và dược phẩm.
  - Khi chưa tinh chỉnh ($\text{FT} = 0\%$), mô hình nguồn hoàn toàn thất bại ($R^2 = -0.46$) do bản chất nước thải khác biệt sâu sắc.
  - Tinh chỉnh với tỷ lệ $\text{FT} = 40\%$ đưa hiệu năng mô hình lên mức xuất sắc với $R^2 = 0.90$ và $\text{MAE} = 0.54\text{ kPa}$.
  - Biến SMP protein (SMPp) vươn lên thành yếu tố dự báo quan trọng thứ hai, phản ánh sự phân hủy bùn do độc tính công nghiệp.
  - Biến EPSc vẫn duy trì vai trò dẫn đầu, khẳng định tính khái quát cao của khung học chuyển giao.
- Kết luận 4: Nền tảng ra quyết định kiểm soát bám bẩn có khả năng giải thích khoa học:
  - Nghiên cứu chứng minh tri thức bám bẩn chung có thể chuyển giao và tái hiệu chuẩn chính xác bằng lượng dữ liệu rất nhỏ.
  - Phân tích hóa lý độc lập biến quy trình thích ứng mô hình thành một hệ thống minh bạch, có cơ sở khoa học rõ ràng.
  - Công trình mở ra hướng tiếp cận mới trong việc dự báo TMP và hỗ trợ ra quyết định thông minh tại các trạm xử lý nước thải thiếu dữ liệu.


## 6. Đóng góp tác giả và thông tin mở rộng (Author Contributions and Extended Information)

### 6.1 Tuyên bố đóng góp của tác giả theo chuẩn CRediT
- Tác giả Xiaohang Han (Đồng tác giả thứ nhất):
  - Khởi xướng ý tưởng nghiên cứu (Conceptualization).
  - Quản lý và xử lý dữ liệu thực nghiệm (Data curation).
  - Phân tích dữ liệu định lượng (Formal analysis).
  - Thực hiện điều tra thực nghiệm (Investigation).
  - Phát triển phương pháp học chuyển giao (Methodology).
  - Lập trình kiến trúc mô hình học máy (Software).
  - Kiểm thực kết quả dự báo (Validation).
  - Xây dựng biểu đồ và đồ họa trực quan (Visualization).
  - Soạn thảo bản thảo gốc đầu tiên (Writing – original draft).
- Tác giả Liu Yang (Đồng tác giả thứ nhất):
  - Khởi xướng ý tưởng nghiên cứu (Conceptualization).
  - Quản lý và thẩm định dữ liệu (Data curation).
  - Phân tích dữ liệu định lượng (Formal analysis).
  - Thực hiện điều tra thực nghiệm (Investigation).
  - Hoàn thiện phương pháp nghiên cứu (Methodology).
  - Lập trình và thử nghiệm thuật toán (Software).
  - Kiểm thực hiệu năng mô hình (Validation).
  - Trực quan hóa kết quả phân tích SHAP và LOFO (Visualization).
  - Soạn thảo bản thảo gốc đầu tiên (Writing – original draft).
- Tác giả Huan Qin:
  - Quản lý dữ liệu quan trắc trạm MBR (Data curation).
  - Điều tra và hỗ trợ thí nghiệm (Investigation).
- Tác giả Shujuan Huang:
  - Quản lý dữ liệu hóa lý (Data curation).
  - Điều tra và theo dõi phân tích mẫu (Investigation).
- Tác giả Han Zhang:
  - Quản lý tập dữ liệu phân tích màng (Data curation).
  - Điều tra và thu thập thông số vận hành (Investigation).
- Tác giả Boyan Xu (Tác giả liên hệ / Giám sát):
  - Khởi xướng và định hướng ý tưởng khoa học (Conceptualization).
  - Huy động các nguồn tài trợ nghiên cứu (Funding acquisition).
  - Quản trị dự án và điều phối nhóm nghiên cứu (Project administration).
  - Giám sát toàn diện quá trình nghiên cứu (Supervision).
  - Đọc phản biện, rà soát và chỉnh sửa hoàn thiện bản thảo (Writing – review & editing).
- Tác giả How Yong Ng (Giáo sư, Tác giả liên hệ / Giám sát):
  - Khởi xướng khung lý thuyết và định hướng ứng dụng (Conceptualization).
  - Huy động nguồn tài trợ và cơ sở vật chất (Funding acquisition).
  - Định hướng và giám sát chuyên môn cao cấp (Supervision).
  - Phản biện chuyên sâu, rà soát và hoàn thiện bản thảo (Writing – review & editing).

### 6.2 Cam kết lợi ích, tài trợ và tính khả dụng của dữ liệu
- Tuyên bố xung đột lợi ích (Declaration of Competing Interests):
  - Nhóm tác giả khẳng định không có bất kỳ xung đột lợi ích tài chính hoặc quan hệ cá nhân nào ảnh hưởng đến công trình nghiên cứu này.
- Khung tài trợ nghiên cứu (Acknowledgement):
  - Quỹ Học giả Thái Sơn tỉnh Sơn Đông (Taishan Scholar Foundation of Shandong Province), mã số tài trợ `tsqn202312222`.
  - Quỹ Khoa học Tự nhiên Quốc gia Trung Quốc (National Natural Science Foundation of China - NSFC), mã số tài trợ `42406133`.
  - Quỹ Nghiên cứu Cơ bản và Nghiên cứu Cơ bản Ứng dụng tỉnh Quảng Đông (Guangdong Province Foundation), mã số tài trợ `2023A1515110786`.
  - Nhóm tác giả gửi lời cảm ơn trân trọng tới các thành viên nhóm nghiên cứu của Giáo sư How Yong Ng tại Singapore (bao gồm Wei Hao Loh, David Imanuel Tanaka và các cộng sự).
  - Các cộng sự đã tích cực hỗ trợ thu thập dữ liệu vận hành từ các trạm MBR quy mô pilot.
  - Toàn bộ dữ liệu chỉ sử dụng duy nhất cho mục đích mô phỏng và mô hình hóa trí tuệ nhân tạo.
  - Mọi thông tin định danh nhạy cảm hoặc mang tính bảo mật đều được ẩn danh và mã hóa trước khi phân tích.
- Khả dụng của dữ liệu (Data Availability):
  - Dữ liệu nghiên cứu sẵn sàng được cung cấp khi nhận được yêu cầu hợp lý gửi trực tiếp đến tác giả liên hệ.
- Dữ liệu bổ sung trực tuyến (Supplementary Data):
  - Dữ liệu và hình ảnh bổ sung (Phụ lục từ Hình S1 đến S13 và các Bảng S1 đến S8) được lưu trữ tại cổng thông tin Elsevier.
  - Đường dẫn truy cập định danh số: `https://doi.org/10.1016/j.memsci.2026.126065`.

### 6.3 Phân loại các tài liệu tham khảo cốt lõi của nghiên cứu
- Nhóm 1: Trí tuệ nhân tạo và học máy trong xử lý nước thải và bám bẩn MBR:
  - Niu et al. (2022) [2]: Tổng quan phân tích ứng dụng trí tuệ nhân tạo trong dự báo bám bẩn màng suốt 20 năm qua. Tạp chí *Water Research*.
  - Meng et al. (2017) [3]: Tổng quan cập nhật về cơ chế và biện pháp kiểm soát bám bẩn trong bể phản ứng sinh học màng. Tạp chí *Water Research*.
  - Xiao et al. (2019) [4]: Đánh giá hiện trạng và thách thức của các trạm MBR quy mô thương mại đầy đủ. Tạp chí *Bioresource Technology*.
  - Zhu et al. (2025) [7]: Ứng dụng học máy dự báo bám bẩn màng trong các nhà máy xử lý nước thải MBR đặt ngập. Tạp chí *Environmental Science & Technology*.
  - Kovacs et al. (2022) [8]: Dự báo bám bẩn màng và phân tích độ không đảm bảo bằng học máy tại nhà máy xử lý nước thải. Tạp chí *Journal of Membrane Science*.
  - Lai et al. (2025) [14]: Nguyên lý, phương pháp và hướng dẫn thực hành ứng dụng học máy trong nghiên cứu MBR. Tạp chí *Frontiers of Environmental Science & Engineering*.
  - Lai et al. (2026) [15]: Giám sát bám bẩn thông minh trong các công nghệ xử lý nước thải dựa trên màng lọc. Tạp chí *Nature Sustainability*.
- Nhóm 2: Học chuyển giao liên trạm và xử lý dữ liệu chuỗi thời gian môi trường:
  - Wang et al. (2026) [24]: Phá vỡ các ốc đảo dữ liệu bằng phương pháp mô hình hóa dựa trên chuyển giao tri thức giữa các nhà máy xử lý nước thải. Tạp chí *Process Safety and Environmental Protection*.
  - Cao et al. (2024) [53]: Khả năng chuyển giao của các mô hình học máy đối với nguồn nước ngầm ô nhiễm tự nhiên. Tạp chí *Environmental Science & Technology*.
  - Elahi et al. (2025) [25]: Khả năng tổng quát hóa và học chuyển giao trong dự báo vượt ngưỡng vi khuẩn chỉ thị tại các bãi biển. Tạp chí *Environmental Science & Technology*.
  - Chen et al. (2025) [36]: Tinh chỉnh mô hình LSTM phục vụ chuyển tiếp liền mạch trong mô hình hóa thủy văn từ tiền huấn luyện đến ứng dụng. Tạp chí *Environmental Modelling & Software*.
  - Ribeiro et al. (2018) [33]: Học chuyển giao kết hợp hiệu chỉnh mùa vụ phục vụ dự báo tiêu thụ năng lượng giữa các tòa nhà. Tạp chí *Energy and Buildings*.
- Nhóm 3: Cơ chế hóa lý của chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP):
  - Mannina et al. (2023) [17]: Mô hình hóa các quá trình sinh học trong hệ thống MBR tập trung vào vai trò của SMP và EPS. Tạp chí *Water Research*.
  - Lin et al. (2014) [46]: Tổng quan chuyên sâu về EPS trong MBR: đặc tính, vai trò bám bẩn và chiến lược kiểm soát. Tạp chí *Journal of Membrane Science*.
  - Poorasgari et al. (2015) [41]: Khả năng chịu nén của lớp bám bẩn bánh bùn trong các hệ thống MBR. Tạp chí *Journal of Membrane Science*.
  - Chen et al. (2017) [45]: Hành vi bám bẩn của SMP và EPS trong MBR kỵ khí ngập nước xử lý nước thải nồng độ thấp ở nhiệt độ phòng. Tạp chí *Journal of Membrane Science*.
  - Shen et al. (2015) [47]: Tác động của kích thước hạt bông bùn đến động học bám bẩn màng trong MBR ngập nước. Tạp chí *Chemical Engineering Journal*.
  - Ding et al. (2020) [51]: Khảo sát dài hạn hành vi bám bẩn màng trong MBR kỵ khí xử lý nước thải đô thị ở hai mức nhiệt độ. Tạp chí *Membranes*.
- Nhóm 4: Ảnh hưởng của ion sắt (Fe) và bám bẩn vô cơ:
  - Gao et al. (2024) [54]: Làm rõ vai trò của muối sắt clorua ($FeCl_3$) trong việc thu hồi cacbon từ nước thải đô thị nồng độ thấp và cơ chế tác động lên bông bùn. Tạp chí *Journal of Cleaner Production*.
  - Peng et al. (2022) [55]: Ảnh hưởng của các dạng và thành phần EPS khác nhau đến quá trình kết tụ bùn hạt hiếu khí. Tạp chí *Chemosphere*.
  - Su et al. (2025) [56]: Độ bền và tính ổn định của màng polyme trong các hệ thống MBR xử lý nước thải công nghiệp. Tạp chí *Journal of Environmental Chemical Engineering*.
- Nhóm 5: Giám sát quang phổ trực tuyến và vận hành MBR quy mô thực tế:
  - Lai et al. (2026) [57]: Điều khiển bám bẩn cấp tiến định hướng bởi cảnh báo sớm từ quang phổ huỳnh quang và UV trực tuyến phục vụ vận hành MBR tiết kiệm năng lượng. Tạp chí *Water Research*.
  - Delrue et al. (2011) [58]: Mối quan hệ giữa đặc tính bùn hoạt tính, điều kiện vận hành và bám bẩn trên hai nhà máy MBR quy mô thương mại đầy đủ. Tạp chí *Desalination*.
  - Takefuji (2026) [27]: Các giới hạn của phương pháp giải thích dựa trên SHAP trong ứng dụng môi trường và lọc màng. Tạp chí *Water Research*.
