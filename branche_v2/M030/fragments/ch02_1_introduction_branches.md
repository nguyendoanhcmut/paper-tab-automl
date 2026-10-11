## 1. Introduction

* Bể phản ứng sinh học màng (MBR - membrane bioreactors) kết hợp quá trình xử lý sinh học (biological treatment) với phân tách bằng màng (membrane separation), tạo ra nước sau xử lý có chất lượng cao (high effluent quality) và hiệu quả xử lý vượt trội [1].
  * Công nghệ MBR sở hữu nhiều ưu điểm vận hành quan trọng so với công nghệ truyền thống:
    * Đạt hiệu suất loại bỏ cao đối với các chất ô nhiễm hữu cơ vi lượng và khó phân hủy (micro- and persistent organic pollutants) [1].
    * Yêu cầu diện tích mặt bằng công nghiệp nhỏ (small industrial area requirement) và phát sinh bùn thải thấp (low sludge production) [1].
  * Công nghệ MBR đã được nghiên cứu và phát triển trong xử lý nước thải hơn ba thập kỷ qua, chứng minh hiệu quả vận hành vượt trội trên nhiều loại hình nước thải:
    * Nước thải đô thị (municipal wastewater) [2].
    * Các nguồn nước thải công nghiệp đặc thù gồm dệt nhuộm (textile) [3], nhà máy bia (brewery) [4], chế biến sữa (dairy) [5] và lọc dầu (oil refinery) [6,7].
* Quản lý tài nguyên nước và tái sử dụng nước đã qua xử lý (water reuse) là thách thức hàng đầu đối với các ngành công nghiệp hiện nay, đặc biệt là các nhà máy lọc dầu (oil refineries) [8].
  * Để đáp ứng yêu cầu tái sử dụng nước, đặc biệt cho hệ thống tháp giải nhiệt (cooling towers), nồng độ amoniac trong dòng nước sau xử lý (effluent ammonia concentration) bắt buộc phải đạt mức đủ thấp [8].
  * MBR là giải pháp công nghệ đầy tiềm năng cho mục tiêu này do cho phép loại bỏ amoniac vượt trội so với hệ thống bùn hoạt tính truyền thống (CAS - conventional activated sludge) [8]:
    * Thời gian lưu bùn ($SRT$ - sludge retention time) kéo dài hơn đáng kể [8].
    * Đạt khả năng lưu giữ bùn hoàn toàn (complete sludge retention) trong bể phản ứng [8].
* Tiềm năng loại bỏ amoniac từ nước thải lọc dầu của MBR đã được chứng minh qua nhiều nghiên cứu thực nghiệm dài hạn (bao gồm hơn $10$ năm nghiên cứu của nhóm tác giả) [9–11]:
  * Amaral et al. [9] và Alkmim et al. [10] đánh giá trên các hệ thống MBR quy mô pilot, đạt hiệu suất loại bỏ amoniac trung bình lần lượt là $90\ \%$ và $92\ \%$.
  * Moser et al. [11] khảo sát các cấu hình MBR khác nhau ở quy mô phòng thí nghiệm (lab-scale), ghi nhận hiệu suất loại bỏ amoniac vượt trên $95\ \%$.
* Việc ứng dụng MBR quy mô lớn (large-scale) tập trung vào mục tiêu khử amoniac vẫn đối mặt với nhiều thách thức nghiêm trọng [12,13]:
  * Tổng quan nghiên cứu của Mao et al. [12] chỉ ra các rào cản kỹ thuật phức tạp khi vận hành MBR quy mô lớn để loại bỏ amoniac.
  * Quá trình loại bỏ amoniac sinh học trong MBR rất nhạy cảm với sự dao động của các điều kiện vận hành (operating conditions), gây khó khăn cho công tác kiểm soát [13].
  * Nghiên cứu của Sun et al. [13] ghi nhận hiệu suất loại bỏ amoniac sụt giảm đột ngột từ $95\ \%$ xuống khoảng $54\ \%$ khi nồng độ nhu cầu oxy hóa học ($COD$ - chemical oxygen demand) dòng vào tăng sốc từ mức $100\text{–}400\text{ mg}\cdot\text{L}^{-1}$ lên $615\text{ mg}\cdot\text{L}^{-1}$.
* Yêu cầu cấp thiết đặt ra là phải thấu hiểu và kiểm soát các yếu tố then chốt ảnh hưởng đến hiệu quả loại bỏ amoniac trong MBR, đồng thời xây dựng năng lực dự báo và phát hiện sớm các sự cố suy giảm hiệu suất [14–16].
  * Các nghiên cứu thực nghiệm thuần túy về biến vận hành ảnh hưởng đến xử lý amoniac sinh học [17,18] gặp nhiều trở ngại do nước thải công nghiệp có thành phần phức tạp và biến động liên tục.
  * Trí tuệ nhân tạo (AI - artificial intelligence) là công cụ đắc lực giải quyết thách thức này [19]:
    * Thực hiện hiệu quả quá trình trích xuất đặc trưng (feature extraction) và phân tích tương quan (correlation analysis) giữa các tập dữ liệu đầu vào và đầu ra [19].
    * Đạt hiệu suất vượt trội hơn các phương pháp truyền thống trong tác vụ phân loại mẫu (pattern classification) và hồi quy logic (logical regression) [19].
    * Giảm thiểu độ phức tạp trong nghiên cứu, hạn chế can thiệp thủ công của con người, nâng cao hiệu quả vận hành, tiết kiệm thời gian và tối ưu hóa chi phí [19].
* Học máy (ML - machine learning) cung cấp các thuật toán toán học và thống kê giúp phát hiện quy luật dữ liệu và dự báo dữ liệu đầu ra đối với các hệ thống phân bố phi tuyến và đa chiều phức tạp [18]:
  * Các kỹ thuật AI phổ biến trong giám sát hiệu năng MBR gồm máy vector hỗ trợ (SVM - support vector machine), logic mờ (FL - fuzzy logic), rừng ngẫu nhiên (RF - random forest), và máy học cực trị (ELM - extreme learning machine) [19].
  * Chang et al. [19] đã thử nghiệm $7$ thuật toán ML để mô hình hóa thông lượng nước (water flux) và độ mặn (salinity) của bể phản ứng sinh học màng thẩm thấu (OMBR - osmotic membrane bioreactor) quy mô phòng thí nghiệm, khẳng định tính khả thi của mô hình hóa ML.
  * Trong các kỹ thuật ML, mạng nơ-ron nhân tạo (ANN - artificial neural networks) [20], phân tích thành phần chính (PCA - principal components analysis) và kiểm soát quá trình thống kê đa biến (MSPC - multivariate statistical process control) nổi bật với hiệu suất cao khi xử lý dữ liệu nước thải vốn thường thiếu hụt dữ liệu gán nhãn quy mô lớn [21].
* Mạng nơ-ron nhân tạo (ANN) mô phỏng cấu trúc nơ-ron sinh học và cơ chế học của não bộ con người để giải quyết bài toán ánh xạ phi tuyến giữa các biến đầu vào và đầu ra [22,23]:
  * Mô hình ANN bao gồm các đơn vị xử lý (nơ-ron) bố trí theo các lớp liên kết, thiết lập tương quan giữa biến độc lập (đầu vào) và biến phụ thuộc (đầu ra) thông qua tập dữ liệu huấn luyện [23].
  * ANN được ưa chuộng nhờ thời gian tính toán nhanh, độ chính xác cao, và khả năng mô hình hóa phi tuyến phục vụ phân loại (classification), nhận dạng mẫu (pattern recognition), phân cụm (clustering), và dự báo (forecasting) [24].
  * Ứng dụng ANN trong giám sát hệ thống MBR phức tạp đã chứng minh độ chính xác cao:
    * Banerjee et al. [25] sử dụng ANN để phân tích ảnh hưởng của thời gian lưu thủy lực ($HRT$ - hydraulic retention time), hàm lượng chất rắn lơ lửng trong bùn lỏng ($MLSS$ - mixed liquor suspended solid), và $COD$ dòng vào đến hiệu suất loại bỏ $COD$ trong MBR xử lý nước thải thuộc da thực tế (real tannery wastewater).
    * Kovacs et al. [26] áp dụng thành công ANN để dự báo hiện tượng tắc nghẽn màng (membrane fouling) trong MBR xử lý nước thải đô thị.
    * Các mô hình ANN đóng vai trò là công cụ hỗ trợ ra quyết định (decision support), giúp cắt giảm chi phí vận hành [25,26].
* Phân tích thành phần chính (PCA) là phương pháp giảm số chiều dữ liệu hiệu quả, giúp trích xuất cấu trúc ẩn và biểu diễn thông tin cốt lõi dưới dạng các thành phần chính (PC - principal components) là tổ hợp tuyến tính của các biến ban đầu [27,28]:
  * PCA hỗ trợ phân tích toàn diện tập dữ liệu phức tạp: làm sáng tỏ tương quan giữa các biến và quan sát, lượng hóa các mẫu quy luật, và nhận diện các quan sát ngoại lai (extreme observations) [28].
  * Ứng dụng tiếp cận dựa trên dữ liệu (data-driven approach) bằng PCA trong hệ sinh thái MBR đã ghi nhận nhiều thành công:
    * Gutiérrez et al. [29] dùng PCA xác định các yếu tố chủ chốt chi phối quá trình loại bỏ chất ô nhiễm vi lượng trong hệ MBR kết hợp than hoạt tính dạng bột (PAC - powdered activated carbon).
    * Qin et al. [30] phân tích tác động của $HRT$ và tải trọng hữu cơ ($OLR$ - organic loading rate) đến động thái vi nấm trong quá trình phân hủy kỵ khí chất thải thực phẩm bằng MBR màng ngập (immersed MBR).
    * Miwa et al. [31] dùng PCA đánh giá cấu trúc quần xã vi sinh vật liên quan đến sự hình thành màng sinh học (biofilm) và tắc nghẽn màng trong MBR.
    * Viet và Jang [32] ứng dụng PCA chứng minh trở lực tắc nghẽn màng (fouling resistance) đóng vai trò chi phối biến thiên tổng thể trong hệ OMBR kết hợp xử lý nước thải và tưới phân bón bền vững.
* Kiểm soát quá trình thống kê đa biến (MSPC) cung cấp năng lực giám sát động học quá trình thông qua các biểu đồ kiểm soát (control charts) nhằm phát hiện sớm các biến cố bất thường [33,34]:
  * Biểu đồ kiểm soát đa biến duy trì tính trực quan, đơn giản tương tự biểu đồ đơn biến nhưng có độ nhạy vượt trội trong phát hiện các quan sát lệch chuẩn (out-of-control observations) nhờ tích hợp đồng thời thông tin từ mọi biến số đo lường [34].
  * MSPC hỗ trợ truy tìm nguyên nhân khả gán (assignable causes) gây ra các hành vi bất thường, từ đó nâng cao độ chính xác trong kiểm soát vận hành [34].
  * Dù việc áp dụng MSPC cho hệ thống MBR còn rất hạn chế, tiềm năng đã được chứng minh trong kiểm soát chất lượng ở các lĩnh vực khác [35,36] cho thấy tính khả thi cao trong kiểm soát quá trình loại bỏ amoniac [33,34].
* Mục tiêu và đóng góp mới của nghiên cứu:
  * Khảo sát hệ thống MBR quy mô pilot xử lý nước thải nhà máy lọc dầu thực tế trong thời gian liên tục $4$ năm, phản ánh đầy đủ hiệu ứng nền phức tạp (matrix effects) và hành vi vận hành dài hạn [124–146].
  * Kết hợp đồng thời ba công cụ phân tích nâng cao:
    * Mạng nơ-ron nhân tạo (ANN) và phân tích thành phần chính (PCA) để nhận diện các biến vận hành có ảnh hưởng lớn nhất đến hiệu quả loại bỏ amoniac và dự đoán hành vi hệ thống [126–128].
    * Kiểm soát quá trình thống kê đa biến (MSPC) để phát hiện và chẩn đoán sớm các điều kiện dẫn đến sự cố suy giảm hiệu suất loại bỏ amoniac [128,129].
  * Đây là nghiên cứu đầu tiên ứng dụng tích hợp ANN, PCA và MSPC chuyên biệt cho mục tiêu loại bỏ amoniac trong MBR xử lý nước thải lọc dầu [129–131].
  * Các biến đo lường được lựa chọn toàn diện nhằm thu thập thông tin về cả hai cơ chế xử lý nền tảng của MBR: phân hủy sinh học (biodegradation) và phân tách qua màng lọc (membrane separation) [139–141].
  * Đóng góp cơ sở khoa học và kỹ thuật để tối ưu hóa khả năng kiểm soát quá trình loại bỏ amoniac, nâng cao độ tin cậy và hiệu suất xử lý của công nghệ MBR trong công nghiệp lọc hóa dầu [144–146].
