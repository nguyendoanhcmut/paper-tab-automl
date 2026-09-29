## Abstract và Tóm tắt tổng quan

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

---

## 1. Giới thiệu (Introduction)

### Các vấn đề bám bẩn màng và chi phí vận hành MBR

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

### Hạn chế về dữ liệu sinh hóa tại các trạm quy mô pilot

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

### Giải pháp học chuyển giao liên trạm (Cross-Plant Transfer Learning)

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

### Mục tiêu nghiên cứu và tính mới về khả năng giải thích (Explainability)

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
