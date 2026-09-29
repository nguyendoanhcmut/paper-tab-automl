## 4. Kết luận và Định hướng ứng dụng thực tế

### 4.1. Kết luận nghiên cứu cốt lõi

#### 4.1.1. Hiệu năng vượt trội và tính thích ứng của mô hình AutoML RF
- Độ chính xác dự báo tổng thể: Mô hình Rừng ngẫu nhiên (RF) do khung TPOT AutoML tối ưu đạt hệ số xác định $R^2 = 0.96$ trên tập kiểm thử độc lập gồm 268 mẫu.
- Chỉ số sai số thực nghiệm mức thấp: Mô hình ghi nhận sai số toàn phương trung bình $\text{RMSE} = 0.89\text{ mg/L}$ và sai số tuyệt đối trung bình $\text{MAE} = 0.47\text{ mg/L}$.
- Ưu thế chu kỳ phát triển thuật toán: Khung AutoML tự động hóa hoàn toàn các khâu tiền xử lý, chọn mô hình và tinh chỉnh siêu tham số. Quy trình này rút ngắn đáng kể thời gian phát triển so với các phương pháp lập trình thủ công truyền thống.
- Vượt trội so với các thuật toán nền tảng: Mô hình RF tối ưu vượt xa hiệu năng của Cây tăng cường độ dốc (GBT với $R^2 = 0.91$), Hồi quy tuyến tính (LR với $R^2 = 0.84$), Cây quyết định (DT với $R^2 = 0.80$), K láng giềng gần nhất (KNN với $R^2 = 0.43$) và Hồi quy vector hỗ trợ (SVR với $R^2 = 0.06$).
- Công cụ điều khiển định lượng tin cậy: Kết quả nghiên cứu chứng minh mô hình RF là công cụ tính toán hiệu quả cao để dự báo và tự động hóa quy trình châm chất keo tụ trong các nhà máy xử lý nước cấp (DWTP).

#### 4.1.2. Minh bạch hóa cơ chế keo tụ thông qua lý thuyết SHAP
- Thứ tự phân cấp tầm quan trọng đặc trưng: Khi độ đục nước thô ($\text{NTU-RW}$) duy trì ở mức thấp và ổn định, độ dẫn điện ($\text{EC-RW}$) trở thành yếu tố chi phối mạnh nhất đến liều lượng châm PACl.
- Trật tự ảnh hưởng của các thông số kế tiếp: Mức độ ảnh hưởng giảm dần theo thứ tự từ nồng độ amoniac ($\text{NH}_3\text{-N-RW}$), nhu cầu oxy hóa học pemanganat ($\text{COD}_{\text{Mn}}\text{-RW}$), nhiệt độ nước thô ($\text{T-RW}$) đến lưu lượng nước xử lý ($\text{WTR}$).
- Cơ chế giải thích cục bộ trực quan: Biểu đồ thác nước (waterfall plot) và biểu đồ quyết định (decision plot) định lượng chính xác mức độ tăng hoặc giảm liều lượng châm chất keo tụ so với giá trị kỳ vọng nền của từng mẫu kiểm thử.
- Mối liên hệ hóa lý của chỉ số pH: Độ pH nước sau keo tụ ($\text{pH-TW}$) có mối liên hệ nghịch đảo tuyến tính với liều lượng keo tụ do ion $\text{Al}^{3+}$ thủy phân giải phóng các ion $\text{H}^+$.
- Nhận diện ngưỡng đáp ứng bão hòa: Phân tích phụ thuộc biên SHAP xác định khoảng biến thiên nhạy cảm của $\text{EC-RW}$ nằm trong vùng $300\text{ đến }550\ \mu\text{S/cm}$ và điểm bùng phát nhu cầu hóa chất khi $\text{COD}_{\text{Mn}}\text{-RW}$ vượt ngưỡng $4\text{ mg/L}$.

#### 4.1.3. Hiệu quả kinh tế, năng lượng và tối ưu hóa vận hành
- Tiết kiệm hóa chất nguồn Sông Dương Tử: Mô hình giúp cắt giảm $222\text{ kg PACl/ngày}$, tương đương giảm $11\%$ tổng lượng chất keo tụ tiêu thụ và tiết kiệm $180.7\text{ CNY/ngày}$ chi phí vận hành.
- Tiết kiệm hóa chất nguồn Sông Loan Hà: Mô hình giúp cắt giảm $225\text{ kg PACl/ngày}$, tương ứng giảm $8\%$ hóa chất châm vào và tiết kiệm $183.2\text{ CNY/ngày}$ chi phí thực tế.
- Tỷ lệ tiết kiệm bình quân gia quyền cả năm: Tính theo chu kỳ cấp nước luân phiên thực tế (Sông Dương Tử chiếm phần lớn thời gian, Sông Loan Hà cấp vào mùa đông), nhà máy giảm $10.25\%$ lượng hóa chất PACl hàng năm.
- Giảm thiểu rủi ro định liều quá mức: Mô hình loại bỏ sai số do thao tác theo thói quen của công nhân vận hành, ngăn ngừa triệt để hiện tượng hạt keo bị tái ổn định điện tích (colloidal restabilization).
- Đảm bảo chất lượng nước sau xử lý: Độ đục nước đầu ra ($\text{NTU-TW}$) luôn duy trì ổn định dưới ngưỡng tiêu chuẩn quốc gia, khẳng định việc giảm liều lượng không gây tổn hại đến chất lượng nước thành phẩm.

---

### 4.2. Khuyến nghị kỹ thuật xanh và giải pháp giảm thiểu tác động môi trường

#### 4.2.1. Tích hợp liên hoàn quy trình tiền xử lý và hấp phụ nâng cao
- Kết hợp quy trình tiền clo hóa (pre-chlorination): Tích hợp thuật toán dự báo với khâu châm clo sơ bộ giúp oxy hóa các hợp chất hữu cơ hòa tan phức tạp và phá vỡ liên kết chelate kim loại - hữu cơ.
- Hấp phụ than hoạt tính dạng hạt hoặc bột: Bố trí công đoạn hấp phụ than hoạt tính trước bể keo tụ để hấp phụ chọn lọc các tiền chất hữu cơ khó phân hủy và các chất gây mùi.
- Hiệu ứng cộng hưởng làm suy giảm nhu cầu keo tụ: Quá trình oxy hóa sơ bộ kết hợp hấp phụ than giúp hạ thấp nồng độ $\text{COD}_{\text{Mn}}\text{-RW}$, tạo điều kiện giảm mạnh liều lượng chất keo tụ vô cơ PACl châm vào hệ thống.
- Tối ưu hóa điều khiển đa quy trình: Các nhà máy nên xây dựng hệ thống điều khiển liên hoàn giữa liều lượng chất oxy hóa, vật liệu hấp phụ và hóa chất keo tụ nhằm tối đa hóa hiệu quả loại bỏ chất ô nhiễm hữu cơ vi lượng.

#### 4.2.2. Phát triển chất keo tụ sinh học bền vững và công nghệ xúc tác mới
- Nghiên cứu chất tạo bông sinh học có nguồn gốc tự nhiên: Ứng dụng chitosan, tinh bột biến tính hoặc chất tạo bông vi sinh vật để thay thế một phần hoặc toàn bộ chất keo tụ gốc nhôm.
- Cơ chế keo tụ bổ trợ của phân tử chitosan: Cấu trúc phân tử mang mật độ điện tích dương cao và chuỗi mạch polymer dài của chitosan kích hoạt cơ chế bắc cầu hạt keo hiệu quả, tăng kích thước bông cặn và tốc độ lắng trong điều kiện nước lạnh.
- Giảm phụ thuộc tài nguyên khoáng sản không tái tạo: Khai thác chất keo tụ hữu cơ sinh học giúp giảm sự lệ thuộc vào quặng bauxite và giảm lượng hóa chất vô cơ tiêu thụ trong ngành cấp nước.
- Ứng dụng công nghệ quang xúc tác tiên tiến: Tích hợp vật liệu quang xúc tác mới như composite aerogel MIL-53(Fe)/graphene hoặc cấu trúc dị thể dưới ánh sáng khả kiến nhằm khoáng hóa triệt để kháng sinh và chất ô nhiễm hữu cơ khó xử lý.

#### 4.2.3. Kiểm soát rủi ro tồn dư nhôm hòa tan và quản lý bùn thải nhôm hydroxit
- Loại bỏ nguy cơ tồn dư nhôm hòa tan ($\text{Al}_{\text{res}}$): Nồng độ ion nhôm hòa tan vượt mức tiêu chuẩn trong nước sạch có thể gây độc tính thần kinh cho người sử dụng và tạo cặn kết tủa thứ cấp làm tắc nghẽn đường ống phân phối.
- Cắt giảm phát sinh bùn nhôm hydroxit ($\text{Al(OH)}_3$): Việc tiết kiệm $10.25\%$ lượng PACl châm vào giúp giảm trực tiếp khối lượng kết tủa $\text{Al(OH)}_3$ dạng keo xốp cồng kềnh tích tụ tại đáy bể lắng.
- Tối ưu chi phí xử lý và khử nước bùn: Khối lượng bùn phát sinh thấp hơn giúp giảm áp lực vận hành của sân phơi bùn, tiết kiệm năng lượng cho máy ép bùn và giảm tiêu hao hóa chất polymer trợ lắng bùn.
- Thúc đẩy kinh tế tuần hoàn từ phụ phẩm bùn thải: Bùn lắng chứa nhôm hydroxit sau khi nung xử lý nhiệt có thể tái sinh thành hạt vật liệu hấp phụ để loại bỏ asen ($\text{As(V)}$) hoặc tái sử dụng làm nguyên liệu chế tạo vật liệu xây dựng.

---

### 4.3. Phần thông tin bổ trợ và Tuyên bố trách nhiệm khoa học

#### 4.3.1. Phân công đóng góp của các tác giả theo tiêu chuẩn CRediT
- Liyan Feng: Trực tiếp đảm nhiệm các vai trò Conceptualization, Methodology, Software, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization, Supervision, Validation, Resources, Project administration.
- Ying Zhang: Đảm nhiệm các khâu Resources, Project administration, Methodology, Investigation, Funding acquisition, Data curation.
- Xiaoting Wei: Đảm nhiệm các vai trò Writing – original draft, Visualization, Supervision, Software.
- Mengyuan Wang: Đảm nhiệm các công việc Visualization, Validation, Software, Resources, Project administration.
- Zhiguang Niu: Đảm nhiệm các vai trò Resources, Project administration, Methodology, Investigation, Data curation.
- Chenchen Wang: Đảm nhiệm các vai trò Writing – review & editing, Visualization, Supervision, Software, Project administration.

#### 4.3.2. Tuyên bố xung đột lợi ích và tính khả dụng của dữ liệu
- Tuyên bố xung đột lợi ích (Declaration of competing interest): Nhóm tác giả khẳng định không có bất kỳ lợi ích tài chính cạnh tranh hoặc quan hệ cá nhân nào làm ảnh hưởng đến các kết quả và kết luận trong bài báo.
- Khả năng tiếp cận dữ liệu (Data availability): Toàn bộ dữ liệu quan trắc chất lượng nước và vận hành thực tế sẽ được nhóm tác giả cung cấp khi có yêu cầu hợp lý.

#### 4.3.3. Nguồn tài trợ và Lời cảm ơn đơn vị thực địa
- Nguồn tài trợ từ đề tài trọng điểm quốc gia: Nghiên cứu nhận hỗ trợ kinh phí từ National Key Research and Development Programme của Trung Quốc theo mã đề tài 2022YFC3203803.
- Nguồn tài trợ từ quỹ khoa học địa phương: Công trình được tài trợ bởi Department of Science and Technology of Fujian Province thông qua đề tài mang mã số 2022J01522.
- Tri ân doanh nghiệp hỗ trợ dữ liệu: Các tác giả gửi lời cảm ơn sâu sắc đến Công ty Cấp nước TEDA Thiên Tân (Tianjin TEDA Water Industry Co., Ltd.) vì đã hỗ trợ kỹ thuật và cung cấp toàn bộ chuỗi dữ liệu vận hành thực địa.

---

### 4.4. Tổng hợp các tài liệu tham khảo cốt lõi làm nền tảng lý thuyết

#### 4.4.1. Nền tảng thuật toán AutoML và Khung giải thích mô hình SHAP
- Thuật toán tối ưu đường ống học máy TPOT: Olson và cộng sự (2016) công bố công cụ TPOT sử dụng lập trình di truyền trên nền scikit-learn để tự động hóa toàn bộ quy trình thiết kế và tối ưu đường ống học máy [25].
- Đánh giá tổng quan các hệ thống AutoML hiện đại: Baratchi và cộng sự (2024), Eldeeb và cộng sự (2024) tổng hợp các bước phát triển của AutoML và phân tích thực nghiệm so sánh các khung AutoML phổ biến [19, 20].
- Ứng dụng AutoML trong phân tích chất lượng nước: Venkata Vara Prasad và cộng sự (2021), Luo và cộng sự (2023) ứng dụng AutoML để tự động hóa phân tích chất lượng nước và dự báo hiệu quả xử lý dinh dưỡng sinh học trong nhà máy nước thải [26, 27].
- Cơ sở lý thuyết trò chơi của phương pháp SHAP: Lundberg và Lee (2017) thiết lập khung giải thích mô hình thống nhất dựa trên giá trị phân bổ Shapley trong lý thuyết trò chơi hợp tác [28].
- Chuẩn hóa lựa chọn đặc trưng bằng SHAP: Hancock và cộng sự (2025) chuẩn hóa phương pháp lựa chọn đặc trưng độc lập với mô hình bằng cách ứng dụng phân tích giá trị SHAP [29].
- Ứng dụng XAI giải mã quá trình xử lý nước: Li và cộng sự (2024), Makumbura và cộng sự (2024), Park và cộng sự (2022) kết hợp mô hình học sâu và học máy quần thể với SHAP để dự báo và giải thích các chỉ số chất lượng dòng ra [35-37].

#### 4.4.2. Cơ chế keo tụ bằng muối kim loại và Mô hình hóa định liều trong DWTP
- Động học keo tụ bằng muối kim loại thủy phân: Duan và Gregory (2003) giải thích chi tiết các cơ chế trung hòa điện tích, kết tủa bẫy cặn và động học thủy phân phức tạp của các ion muối kim loại như nhôm và sắt [59].
- Dự báo liều lượng keo tụ bằng mô hình chuỗi thời gian sâu: Lin, Kim và cộng sự (2023, 2024) phát triển mô hình mạng chú ý đồ thị đa biến (GAT) và so sánh mạng nơ-ron nhân tạo với mạng nơ-ron sâu trong việc dự đoán liều lượng chất keo tụ trên tập dữ liệu vận hành lớn [39, 46, 48].
- Kết hợp mạng Elman và Rừng ngẫu nhiên: Wang và cộng sự (2023) ứng dụng thành công mạng nơ-ron hồi quy Elman kết hợp với mô hình Rừng ngẫu nhiên để dự đoán đồng thời liều chất keo tụ và độ đục nước sau lắng [44, 47].
- Tối ưu hóa phản ứng keo tụ bằng phương pháp bề mặt đáp ứng: Ji và cộng sự (2024) áp dụng phương pháp bề mặt đáp ứng (RSM) để xác định các thông số vận hành tối ưu cho quá trình keo tụ bằng Poly-aluminum Chloride [56].
- Điều khiển dự báo đa mô hình cho quy trình keo tụ: Bello và cộng sự (2014) thiết kế hệ thống điều khiển dự báo dựa trên nhiều mô hình (MMPC) để kiểm soát tự động liều hóa chất châm vào trong nhà máy xử lý nước cấp [9].

#### 4.4.3. Kỹ thuật keo tụ nước độ đục thấp, Polyme sinh học và Quản lý phụ phẩm
- Cơ chế keo tụ nước nhiệt độ thấp và độ đục thấp: Zhang và cộng sự (2018), Liu và cộng sự (2019) nghiên cứu tăng cường keo tụ cho nguồn nước mặt độ đục thấp thông qua việc điều chỉnh độ kiềm (basicity) của PACl và sử dụng chitosan làm chất trợ keo tụ [53, 54].
- Hợp chất keo tụ composite sinh học: El Foulani và cộng sự (2023) so sánh hiệu năng của chất keo tụ hỗn hợp PACl-chitosan và PACl-sodium alginate trong việc loại bỏ chất bẩn ở nguồn nước hồ chứa [50].
- Bột hạt tự nhiên làm chất tạo bông thân thiện môi trường: Vunain và cộng sự (2019) đánh giá hiệu quả tạo bông và khả năng giảm thiểu mầm bệnh của bột hạt chùm ngây (*Moringa oleifera*) [51].
- Tái sử dụng bùn thải nhôm hydroxit nung: Kim và cộng sự (2023) nghiên cứu tác động của nhiệt độ nung lên khả năng hấp phụ của các hạt chế tạo từ bùn thải PACl để loại bỏ asen ($\text{As(V)}$) khỏi môi trường nước [57].
- Công nghệ xúc tác phân hủy ô nhiễm hữu cơ: Luo và cộng sự (2025), Yang và cộng sự (2025) tổng hợp các vật liệu xúc tác mới mở ra triển vọng kết hợp với công đoạn xử lý keo tụ để bảo vệ môi trường nước bền vững [63, 64].
