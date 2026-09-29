---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Empowerment of accurate modeling of anaerobic membrane bioreactors by automated machine learning

## Chương 1: Giới thiệu và Bối cảnh Nghiên cứu AnMBR

### 1.1 Khủng hoảng tài nguyên nước và vị thế của công nghệ AnMBR
#### Bối cảnh khan hiếm nước toàn cầu và tái tạo tài nguyên từ nước thải
- Hoạt động của con người làm gia tăng ô nhiễm và suy kiệt nguồn nước ngọt tự nhiên. Hiện tượng này đe dọa nghiêm trọng an ninh lương thực và cân bằng sinh thái (Jury and Vaux, 2007).
- Tình trạng khan hiếm nước cản trở nguồn cấp nước sạch cho các đô thị trên toàn cầu.
- Ngành công nghiệp nước xác định nước thải là nguồn tài nguyên tái tạo bền vững (Winkler and van Loosdrecht, 2022).
- Quy trình bùn hoạt tính truyền thống giữ vai trò nòng cốt trong các trạm xử lý nước thải hiện hành (van Loosdrecht and Brdjanovic, 2014).
- Các nhà khoa học ưu tiên nghiên cứu các công nghệ thu hồi tài nguyên để thúc đẩy nền kinh tế tuần hoàn.

#### Nguyên lý tích hợp và ưu điểm kỹ thuật của AnMBR (anaerobic membrane bioreactor)
- AnMBR tích hợp trực tiếp quá trình phân hủy kỵ khí sinh học với module màng lọc tách sinh khối.
- Hệ thống này xử lý nước thải hiệu quả và tạo ra khí sinh học (biogas) giàu năng lượng (Krzeminski et al., 2017; Moideen et al., 2023).
- Chi phí vận hành của AnMBR thấp hơn đáng kể so với các hệ thống hiếu khí truyền thống (Ho and Sung, 2010; Pretel et al., 2015).
- AnMBR hạn chế tối đa lượng bùn thải dư thừa và nâng cao tiềm năng thu hồi năng lượng sạch (Robles et al., 2022).
- Quá trình khởi động hệ thống phản ứng kỵ khí diễn ra nhanh chóng (Robles et al., 2018).
- Dấu chân sinh thái và diện tích xây dựng của AnMBR nhỏ gọn hơn nhiều so với các công nghệ truyền thống.
- Công nghệ này đáp ứng mục tiêu giảm phát thải carbon và tái tạo tài nguyên bền vững.

### 1.2 Rào cản thực nghiệm và sự cần thiết của mô hình hóa định hướng dữ liệu
#### Thách thức tài nguyên và thời gian trong nghiên cứu thực nghiệm AnMBR
- Quá trình phát triển AnMBR chủ yếu dựa vào các thí nghiệm quy mô phòng thí nghiệm và thử nghiệm pilot (Q. Li et al., 2024; Z. Li et al., 2024; Ren et al., 2024).
- Việc vận hành hệ thống thực nghiệm tiêu tốn lượng lớn hóa chất và thuốc thử phân tích (Li et al., 2022).
- Hệ thống phản ứng đòi hỏi trang thiết bị kiểm soát chuyên dụng và nhân sự kỹ thuật cao.
- Các thí nghiệm sinh học kỵ khí kéo dài từ vài tháng đến nhiều năm để đạt trạng thái ổn định.
- Giới hạn không gian và kinh phí phòng thí nghiệm thu hẹp số lượng mẻ vận hành của bể phản ứng.
- Các rào cản thực nghiệm này làm chậm quá trình thương mại hóa và mở rộng quy mô AnMBR.

#### Tiềm năng của mô hình hóa học máy (Machine Learning - ML) trong tối ưu hóa vận hành
- Mô hình hóa dựa trên dữ liệu nổi lên như giải pháp đột phá cho công nghệ AnMBR (Li et al., 2022; Robles et al., 2018; Wang and Li, 2024).
- Các thuật toán học máy sử dụng thông số vận hành và chất lượng nước đầu vào để dự báo chất lượng nước đầu ra (Li et al., 2022; Mahanna et al., 2024; Pal et al., 2024).
- Mô hình nắm bắt chính xác các mối quan hệ phi tuyến phức tạp giữa dòng vào và dòng ra.
- Học máy cung cấp các hiểu biết sâu sắc giúp kỹ sư điều khiển và tối ưu hóa hiệu suất bể phản ứng.
- Mô phỏng thuật toán thay thế các thử nghiệm vật lý tốn kém bằng mức tiêu hao tài nguyên tối thiểu.
- Chuyên viên vận hành đánh giá được nhiều kịch bản công nghệ khác nhau mà không cần gián đoạn hệ thống thực tế.
- Giải pháp này hỗ trợ đắc lực việc thiết kế AnMBR trong điều kiện hạn chế về ngân sách thực nghiệm.

### 1.3 Thách thức cốt lõi khi ứng dụng học máy trong AnMBR
#### Tính không đồng nhất cao của hệ thống sinh học AnMBR
- Hệ thống AnMBR thể hiện tính không đồng nhất rất lớn giữa các công trình xử lý nước thải.
- Cấu trúc quần thể vi sinh vật thay đổi liên tục theo điều kiện cấp cơ chất và nhiệt độ vận hành.
- Cấu hình thiết bị và đặc tính nước thải đầu vào biến động mạnh theo thời gian.
- Kích thước lỗ màng trong AnMBR làm biến đổi nồng độ COD dòng ra và cấu trúc hệ vi sinh (Ji et al., 2020).
- Biến động vi sinh ảnh hưởng trực tiếp đến chất lượng nước đầu ra và hiệu suất sinh khí sinh học.
- Tính không đồng nhất cao ngăn cản việc áp dụng một mô hình tổng quát chung cho nhiều hệ phản ứng.
- Kỹ sư phải hiệu chỉnh mô hình riêng biệt cho từng cấu hình lò phản ứng cụ thể.

#### Rào cản chuyên môn kỹ thuật trong lựa chọn thuật toán và tinh chỉnh siêu tham số
- Quy trình phát triển mô hình học máy bao gồm nhiều tác vụ phức tạp (He et al., 2021; Karmaker et al., 2021).
- Chuyên gia phải sàng lọc và lựa chọn thuật toán phù hợp nhất trong số hàng loạt thuật toán ứng viên.
- Công việc tinh chỉnh siêu tham số đòi hỏi kiến thức toán học sâu rộng và chi phí tính toán lớn.
- Kỹ sư ngành nước thường thiếu chuyên môn chuyên sâu về khoa học dữ liệu và trí tuệ nhân tạo.
- Sự thiếu hụt nhân lực liên ngành cản trở việc ứng dụng học máy trong thực tế vận hành MBR (Lai et al., 2024).

### 1.4 Giải pháp học máy tự động (AutoML) và mục tiêu công trình
#### Khái niệm và tiềm năng dân chủ hóa công nghệ của AutoML (FLAML)
- AutoML tự động hóa các tác vụ lặp lại trong toàn bộ đường ống học máy (Truong et al., 2019).
- Hệ thống tự động thực hiện việc tuyển chọn thuật toán và tối ưu hóa siêu tham số.
- AutoML giảm thiểu đáng kể rào cản kỹ thuật và rút ngắn thời gian xây dựng mô hình dự báo.
- Nền tảng tự động này thúc đẩy mạnh mẽ quá trình triển khai học máy vào thực tiễn ngành nước (Lai et al., 2024).
- AutoML giúp dân chủ hóa công nghệ mô hình hóa cho các chuyên gia môi trường không chuyên về ML (Li et al., 2021).
- Người dùng có thể nhanh chóng làm chủ công nghệ dữ liệu để cải tiến hiệu quả vận hành AnMBR.

#### Các mục tiêu nghiên cứu cốt lõi của bài báo
- Nghiên cứu áp dụng khung làm việc AutoML (thư viện FLAML) để mô hình hóa động học phi tuyến của AnMBR xử lý nước thải sinh hoạt.
- Tác vụ trọng tâm tập trung vào dự báo chính xác nồng độ và hiệu suất loại bỏ COD dòng ra.
- Công trình đánh giá định lượng tác động của việc mở rộng tập đặc trưng vận hành đối với chất lượng mô hình.
- Nhóm nghiên cứu khảo sát ảnh hưởng của kích thước tập dữ liệu huấn luyện nhỏ đối với độ chính xác thuật toán.
- Công trình đối sánh hiệu năng của AutoML với các mạng nơ-ron sâu tiên tiến gồm FCN, CNN và DenseNet.
- AutoML đạt sai số phần trăm tuyệt đối trung bình (MAPE) ở mức $3.11\%$, vượt trội hơn các mô hình học sâu.
- Nghiên cứu phát triển khung diễn giải xếp hạng đặc trưng tổ hợp để giải thích cơ chế dự báo của AutoML.
- Kết quả xếp hạng xác định nồng độ COD dòng vào là đặc trưng chi phối mạnh nhất đến hiệu suất loại bỏ COD.
- Phát hiện của bài báo mở rộng tiềm năng ứng dụng AutoML cho các hệ thống xử lý nước thải có tập dữ liệu nhỏ.

## Chương 2: Phương pháp Luận và Quy trình Mô hình hóa AutoML

### 2.1 Cơ sở dữ liệu thực nghiệm AnMBR và tiền xử lý
#### Cấu hình hệ thống thực nghiệm hai bể AnMBR (AnMBR1 & AnMBR2)
- Nhóm nghiên cứu thu thập dữ liệu từ hai hệ phản ứng màng sinh học kỵ khí (AnMBR) vận hành liên tục dài hạn (Ji et al., 2020, 2021a, 2021b).
- Cả hai lò phản ứng xử lý nước thải sinh hoạt đô thị thực tế.
- Kỹ sư lắp đặt hai hệ thống trực tiếp tại một nhà máy xử lý nước thải đô thị (WWTP) để tiếp cận nguồn nước thải thô.
- Thể tích hiệu dụng của mỗi bể phản ứng đạt $20\text{ L}$.
- Cả hai hệ thống đều sử dụng module màng sợi rỗng bằng chất liệu polyvinylidene difluoride (PVDF).
- Kích thước lỗ màng của bể AnMBR1 là $0.4\ \mu\text{m}$.
- Kích thước lỗ màng của bể AnMBR2 là $0.05\ \mu\text{m}$.
- Bể điều nhiệt (NTT-20S, EYELA, Nhật Bản) duy trì nhiệt độ vận hành ổn định trong khoảng $20^\circ\text{C}$ đến $25^\circ\text{C}$.
- Thời gian lưu nước thủy lực (HRT) của bể AnMBR1 biến thiên trong khoảng $4\text{ h}$ đến $24\text{ h}$.
- Thời gian lưu nước thủy lực (HRT) của bể AnMBR2 biến thiên trong khoảng $10\text{ h}$ đến $24\text{ h}$.
- Nhóm nghiên cứu đo đạc các chỉ tiêu COD, MLSS và MLVSS theo phương pháp tiêu chuẩn quốc tế (Bridgewater et al., 2017).
- Kỹ thuật viên lấy mẫu MLSS và MLVSS định kỳ hàng tuần.
- Nhóm tác giả áp dụng phương pháp nội suy tuyến tính để làm đầy dữ liệu MLSS và MLVSS nhằm đồng bộ tần suất với COD.
- Thiết bị đo chuyên dụng (TOADKK, RM-30P, Nhật Bản) ghi nhận thế oxy hóa khử (ORP) của bùn hoạt tính kỵ khí.
- Dữ liệu cơ sở thu thập trong giai đoạn vận hành lò phản ứng từ ngày 50 đến ngày 414 ($50\text{--}414\text{ ngày}$).

#### Tập biến đặc trưng đầu vào (11 biến đặc trưng) và biến mục tiêu (COD-re)
- Nghiên cứu xác lập tập dữ liệu hoàn chỉnh gồm 11 biến đặc trưng đầu vào ($X$).
- Biến thứ nhất là thời gian vận hành lò phản ứng (OD - reactor operation days, đơn vị: $\text{ngày}$).
- Biến thứ hai là nhiệt độ vận hành lò phản ứng (T-R - reactor operation temperature, đơn vị: $^\circ\text{C}$).
- Biến thứ ba là nhiệt độ nước thải đầu vào (T-in - influent temperature, đơn vị: $^\circ\text{C}$).
- Biến thứ tư là nhiệt độ môi trường xung quanh (T-env - environment temperature, đơn vị: $^\circ\text{C}$).
- Biến thứ năm là độ pH của nước thải đầu vào (pH-in - influent pH, đại lượng không thứ nguyên).
- Biến thứ sáu là nồng độ COD của dòng vào (COD-in - influent COD, đơn vị: $\text{mg/L}$).
- Biến thứ bảy là thông lượng lọc qua màng (flux, đơn vị: $\text{m/ngày}$).
- Biến thứ tám là thế oxy hóa khử của bùn kỵ khí (ORP - oxidation-reduction potential, đơn vị: $\text{mV}$).
- Biến thứ chín là thời gian lưu nước thủy lực (HRT - hydraulic retention time, đơn vị: $\text{giờ}$).
- Biến thứ mười là tổng chất rắn lơ lửng trong hỗn dịch bùn (MLSS - mixed liquor suspended solids, đơn vị: $\text{mg/L}$).
- Biến thứ mười một là chất rắn lơ lửng bay hơi trong hỗn dịch bùn (MLVSS - mixed liquor volatile suspended solids, đơn vị: $\text{mg/L}$).
- Biến mục tiêu đầu ra duy nhất ($Y$) là hiệu suất loại bỏ COD (COD-re - COD removal rate, đơn vị: $\%$).
- Tập dữ liệu cơ sở ban đầu bao gồm 185 mẫu đo đạc thực nghiệm độc lập.

#### Chiến lược phân chia dữ liệu (9:1 split ratio và 10-fold cross-validation)
- Nhóm tác giả phân chia 185 mẫu cơ sở theo tỷ lệ $9:1$ gồm 166 mẫu huấn luyện và 19 mẫu kiểm thử (Li et al., 2022).
- Khung đối chuẩn kế thừa 6 biến đặc trưng đầu vào (T-R, T-in, T-env, pH-in, COD-in, flux) từ nghiên cứu của Li et al. (2022).
- Các mô hình đối chứng nền tảng bao gồm ba kiến trúc mạng học sâu: FCN, CNN và DenseNet.
- Nhóm nghiên cứu áp dụng kiểm định chéo 10 lần (10-fold cross-validation) để đánh giá toàn diện mô hình AutoML.
- Quy trình 10-fold CV huấn luyện 10 mô hình độc lập. Mỗi lần lặp sử dụng phân chia ngẫu nhiên $90\%$ huấn luyện và $10\%$ kiểm thử.
- Chiến lược này đo lường phương sai hiệu năng và bảo đảm mô hình đạt độ bền vững cao trước biến động dữ liệu.

### 2.2 Khung mô hình hóa học máy tự động FLAML AutoML
#### Mô hình toán học tổng quát ($Y = f_{\theta}(X)$) và bài toán tối ưu siêu tham số
- Nghiên cứu thiết lập phương trình toán học tổng quát biểu diễn hệ thống AnMBR:
  $$Y = f_{\theta}(X)$$
- Trong công thức trên, $Y$ biểu diễn vector hiệu suất loại bỏ COD (COD-re).
- Ký hiệu $X$ biểu diễn ma trận chứa các biến đặc trưng vận hành đầu vào.
- Ký hiệu $f_{\theta}$ đại diện cho cấu trúc mô hình thuật toán được tham số hóa bởi vector tham số $\theta$.
- Mô hình hóa dựa trên dữ liệu tìm kiếm bộ tham số tối ưu $\theta^*$ để khớp chính xác nhất với dữ liệu thực nghiệm.
- Hiệu năng của $\theta^*$ phụ thuộc chặt chẽ vào cấu hình siêu tham số (hyperparameters) khởi tạo ban đầu.
- Mạng nơ-ron sâu yêu cầu cấu hình tốc độ học, kích thước lô xử lý và số chu kỳ huấn luyện.
- Mô hình dạng cây yêu cầu cấu hình số lượng cây ước lượng, độ sâu tối đa, số lượng lá và hệ số điều chuẩn.
- Các kỹ thuật tối ưu truyền thống như tìm kiếm lưới, tìm kiếm ngẫu nhiên, tối ưu Bayesian và giải thuật di truyền tiêu tốn nhiều tài nguyên tính toán.
- Phương pháp AutoML tự động hóa hoàn toàn quy trình tinh chỉnh siêu tham số và giúp công nghệ học máy dễ tiếp cận hơn.

#### Bộ học cơ sở dạng cây (Tree-based Learners: RF, Extra Trees, XGBoost, LightGBM, CatBoost)
- Nhóm tác giả tích hợp thư viện học máy tự động FLAML (Fast Library for Automated Machine Learning and Tuning) (Wang et al., 2021b).
- FLAML tự động lựa chọn thứ tự tìm kiếm nhằm tối ưu hóa đồng thời chi phí tính toán và sai số dự báo.
- Dữ liệu dạng bảng có cấu trúc của AnMBR rất phù hợp với các thuật toán dựa trên cây quyết định.
- Khung AutoML tích hợp 5 bộ học cơ sở dạng cây chất lượng cao:
  - Rừng ngẫu nhiên (Random Forest - RF) đóng gói tập hợp các cây quyết định độc lập (Breiman, 2001).
  - Cây cực kỳ ngẫu nhiên (Extra Trees / Extremely Randomized Trees) ngẫu nhiên hóa triệt để ngưỡng phân tách (Geurts et al., 2006).
  - XGBoost triển khai hệ thống tăng cường độ dốc cây có khả năng mở rộng quy mô cao (Chen and Guestrin, 2016).
  - LightGBM tối ưu hóa cây tăng cường độ dốc bằng chiến lược phát triển cây theo lá hiệu năng cao (Ke et al., 2017).
  - CatBoost thực thi thuật toán tăng cường độ dốc với cơ chế xử lý biến phân loại và giảm thiểu dịch chuyển mục tiêu (Dorogush et al., 2018).

#### Chiến lược tối ưu tiết kiệm chi phí CFO (Cost-Frugal Optimization) và thuật toán BlendSearch
- FLAML triển khai chiến lược tối ưu hóa tiết kiệm chi phí CFO (Cost-Frugal Optimization) (Wu et al., 2021).
- CFO bắt đầu tiến trình tìm kiếm từ các cấu hình có chi phí tính toán rất thấp như mô hình kích thước nhỏ.
- Thuật toán chỉ chuyển sang các cấu hình phức tạp hơn khi mức tăng độ chính xác vượt trội hơn chi phí tính toán gia tăng.
- CFO giúp kiểm soát chặt chẽ thời gian và tài nguyên phần cứng so với các thuật toán tối ưu hóa truyền thống.
- Khung làm việc kích hoạt mặc định thuật toán tìm kiếm kết hợp BlendSearch (Wang et al., 2021a).
- BlendSearch là thuật toán tìm kiếm phân cấp kết hợp giữa thăm dò không gian toàn cục và khai thác tối ưu cục bộ.
- Thuật toán giảm thiểu tổng chi phí tính toán cần thiết để phát hiện cấu hình siêu tham số tối ưu nhất.

#### Thiết lập tối ưu hóa (Ngân sách thời gian 300s, 5-fold CV với tiêu chí MSE)
- Toàn bộ tiến trình tối ưu hóa siêu tham số chịu ràng buộc bởi ngân sách thời gian tổng thể là $300\text{ s}$ ($5\text{ phút}$).
- Hệ thống tự động kết thúc tìm kiếm ngay khi thời gian đạt ngưỡng $300\text{ s}$.
- Để ngăn ngừa hiện tượng quá khớp (overfitting), FLAML áp dụng kiểm định chéo 5 lần (5-fold cross-validation) trong mỗi lần tối ưu.
- Tiêu chí hàm mục tiêu trong tối ưu hóa là sai số toàn phương trung bình (MSE - Mean Squared Error).
- Không gian tìm kiếm động bao gồm số lượng cây ước lượng, số lượng lá, tốc độ học và các tham số điều chuẩn.
- Chiến lược CFO tự động điều chỉnh phạm vi tìm kiếm cụ thể dựa trên kích thước thực tế của tập dữ liệu huấn luyện.

### 2.3 Các chỉ số đánh giá hiệu năng và phân tích thỏa thuận Bland-Altman
#### Các chỉ số sai số định lượng (MAE, RMSE, MAPE, $R^2$) - 100% công thức KaTeX
- Nghiên cứu sử dụng 5 chỉ số định lượng để đánh giá độ chính xác của các mô hình dự báo.
- Sai số tuyệt đối trung bình (MAE) đo mức sai lệch tuyệt đối trung bình giữa giá trị thực tế $y_i$ và giá trị dự báo $\hat{y}_i$:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
- MAE mang đơn vị phần trăm ($\%$) và phản ánh độ chuẩn xác của mô hình dự báo.
- Sai số căn bậc hai toàn phương trung bình (RMSE) gán trọng số phạt lớn hơn cho các sai số dự báo lớn:
  $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
- RMSE mang đơn vị phần trăm ($\%$) và đại diện cho độ chụm của các giá trị dự báo.
- Sai số phần trăm tuyệt đối trung bình (MAPE) định lượng sai số tương đối theo tỷ lệ phần trăm:
  $$\text{MAPE} = \frac{1}{n} \sum_{i=1}^n \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100$$
- MAPE mang đơn vị phần trăm ($\%$) và phản ánh sai số tương đối so với thang đo thực nghiệm.
- Hệ số xác định ($R^2$) đo lường tỷ lệ phương sai của biến mục tiêu được giải thích bởi mô hình:
  $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
- Trong công thức trên, $\bar{y}$ là giá trị trung bình số học của các quan sát thực nghiệm:
  $$\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$$
- Giá trị $R^2 = 1$ biểu thị mô hình dự báo khớp hoàn hảo với tập dữ liệu thực nghiệm.
- Giá trị $R^2$ tiệm cận $0$ cho thấy mô hình có năng lực giải thích rất thấp đối với biến mục tiêu.
- Giá trị $R^2 < 0$ chỉ ra rằng sai số của mô hình lớn hơn phương sai nội tại của dữ liệu gốc.
- Giá trị $R^2$ càng gần $1$ chứng minh mô hình đạt chất lượng dự báo càng cao.

#### Phương pháp phân tích mức độ đồng thuận Bland-Altman
- Các chỉ số sai số tổng thể như RMSE không định lượng trực tiếp mức độ đồng thuận giữa dự báo và thực tế (Martin Bland and Altman, 1986).
- Nhóm tác giả áp dụng phân tích Bland-Altman để đánh giá mức độ tương đồng giữa hiệu suất dự báo và số đo thực nghiệm.
- Phương pháp phân tích đồ thị hiệu số giữa hai giá trị đo so với giá trị trung bình của chúng.
- Nghiên cứu xác định hiệu số sai lệch $d_i$ bằng cách lấy giá trị thực tế trừ đi giá trị mô hình dự báo:
  $$d_i = y_i - \hat{y}_i$$
- Hiệu số âm ($d_i < 0$) thể hiện mô hình dự báo cao hơn giá trị đo thực tế (overestimation).
- Hiệu số dương ($d_i > 0$) thể hiện mô hình dự báo thấp hơn giá trị đo thực tế (underestimation).
- Giới hạn đồng thuận $95\%$ (95% Limits of Agreement - LoA) được tính theo công thức:
  $$\text{LoA}_{95\%} = \bar{d} \pm 1.96 \times \text{SD}$$
- Trong đó $\bar{d}$ là sai số hiệu số trung bình và $\text{SD}$ là độ lệch chuẩn của các hiệu số sai lệch.
- Hai phương pháp đạt độ đồng thuận tốt khi tối thiểu $95\%$ các điểm sai số nằm trong dải giới hạn $\bar{d} \pm 1.96 \times \text{SD}$.
- Dải giới hạn đồng thuận không được vượt quá khoảng sai số cho phép trong thực hành kỹ thuật môi trường (Li et al., 2022).

### 2.4 Thiết kế nghiên cứu cắt bỏ biến và dữ liệu (Ablation Studies)
#### Khái niệm và mục tiêu nghiên cứu cắt bỏ thành phần
- Nghiên cứu cắt bỏ thành phần (ablation study) là kỹ thuật đánh giá mức đóng góp của từng nhân tố riêng lẻ vào hiệu năng mô hình.
- Kỹ sư tiến hành loại bỏ hoặc bổ sung có kiểm soát các biến đặc trưng, siêu tham số hoặc tập dữ liệu huấn luyện.
- Mục tiêu chính là xác định xem các nhân tố cụ thể thúc đẩy hay kìm hãm độ chính xác của mô hình học máy.
- Toàn bộ các thử nghiệm cắt bỏ đều giữ nguyên phân chia dữ liệu và tham số huấn luyện chuẩn để bảo đảm tính khách quan.

#### Kịch bản đánh giá các biến đặc trưng (OD, ORP, HRT, MLSS, MLVSS)
- Nghiên cứu khảo sát tác động của 5 biến vận hành bổ sung: OD, ORP, HRT, MLSS và MLVSS.
- Kịch bản thứ nhất kiểm thử việc tích hợp riêng lẻ từng biến đặc trưng vào tập 6 biến đầu vào cơ sở.
- Kịch bản thứ hai kiểm thử việc tích hợp đồng thời cả 5 biến đặc trưng để tạo thành tập 11 biến hoàn chỉnh.
- Nhóm tác giả đối chiếu trực tiếp hiệu năng mô hình trước và sau khi bổ sung biến.
- Thử nghiệm này làm sáng tỏ vai trò cơ chế sinh hóa và thủy lực của từng thông số trong lò phản ứng AnMBR.

#### Kịch bản đánh giá quy mô dữ liệu mở rộng
- Nhóm nghiên cứu thu thập thêm dữ liệu từ các chu kỳ vận hành kéo dài hơn của hai bể AnMBR ($7\text{--}546\text{ ngày}$).
- Tập dữ liệu mở rộng bổ sung thêm 135 mẫu đo đạc thực nghiệm mới.
- Tổng kích thước tập dữ liệu hoàn chỉnh tăng từ 185 mẫu lên 320 mẫu.
- Kịch bản này khảo sát định lượng tác động của việc gia tăng kích thước mẫu đến độ chính xác và tính ổn định của AutoML.

### 2.5 Khung xếp hạng độ quan trọng đặc trưng kết hợp (Ensemble Ranking Score)
#### Phương pháp độ quan trọng dạng cây Gini (Tree-based Gini Importance)
- Phương pháp dạng cây trích xuất độ quan trọng của đặc trưng trực tiếp từ cấu trúc phân nhánh của mô hình cây.
- Trong thuật toán Random Forest, độ quan trọng Gini đo mức suy giảm tiêu chí tạp chất Gini được chuẩn hóa qua các điểm rẽ nhánh.
- Độ giảm tạp chất Gini càng lớn chứng minh biến đặc trưng đóng góp vai trò phân loại và dự báo càng cao.
- Phương pháp này tính toán nhanh nhưng có xu hướng thiên vị các biến đặc trưng có độ biến thiên liên tục.

#### Phương pháp độ quan trọng hoán vị (Permutation Importance qua 30 lần lặp) - Công thức KaTeX
- Phương pháp hoán vị đo lường mức độ suy giảm hiệu năng khi giá trị của một biến đặc trưng bị xáo trộn ngẫu nhiên (Breiman, 2001).
- Việc xáo trộn giá trị phá vỡ hoàn toàn mối tương quan vốn có giữa biến đặc trưng đó với biến mục tiêu COD-re.
- Phương pháp này độc lập với kiến trúc thuật toán (model-agnostic) và tương thích tốt với mọi dữ liệu dạng bảng.
- Độ quan trọng của đặc trưng thứ $j$ ($i_j$) được xác định theo công thức:
  $$i_j = s - \frac{1}{K} \sum_{k=1}^K s_{k,j}$$
- Trong công thức trên, $s$ đại diện cho điểm số sai số gốc của mô hình tham chiếu (sử dụng chỉ số RMSE).
- Ký hiệu $s_{k,j}$ đại diện cho sai số RMSE của mô hình sau khi hoán vị đặc trưng $j$ tại lần lặp thứ $k$.
- Tham số $K$ là tổng số lần lặp lại quá trình hoán vị ngẫu nhiên ($K = 30$).
- Nếu chỉ số RMSE tăng vọt sau khi xáo trộn, đặc trưng $j$ giữ vai trò tối quan trọng đối với khả năng dự báo của mô hình.

#### Phương pháp giải thích cộng tính Shapley (SHAP Values) - Công thức KaTeX
- Phương pháp SHAP là khung làm việc giải thích độc lập mô hình dựa trên lý thuyết trò chơi hợp tác Shapley (Lundberg and Lee, 2017, Lundberg et al., 2018).
- Giá trị SHAP định lượng mức đóng góp cận biên của từng biến đặc trưng vào giá trị dự báo đầu ra.
- Giá trị SHAP của biến đặc trưng $i$ đối với mẫu đầu vào $x$ được tính theo công thức:
  $$\phi_i(f, x) = \sum_{S \subseteq S_{\text{all}} \setminus \{i\}} \frac{|S|! \, (M - |S| - 1)!}{M!} [f_x(S \cup \{i\}) - f_x(S)]$$
- Trong công thức trên, $\phi_i(f, x)$ là giá trị đóng góp SHAP của biến đặc trưng $i$.
- Ký hiệu $S_{\text{all}}$ đại diện cho tập hợp tất cả $M$ biến đặc trưng đầu vào ($M = 11$).
- Ký hiệu $S$ là một tập con các biến đặc trưng không chứa biến $i$ ($S \subseteq S_{\text{all}} \setminus \{i\}$).
- Ký hiệu $|S|$ biểu thị số lượng phần tử có trong tập hợp con $S$.
- Ký hiệu $M$ là tổng số lượng biến đặc trưng đầu vào ($M = 11$).
- Phân thức $\frac{|S|! \, (M - |S| - 1)!}{M!}$ là trọng số tổ hợp xác suất công bằng của liên minh đặc trưng $S$.
- Biểu thức $f_x(S \cup \{i\})$ là giá trị dự báo của mô hình khi tập đặc trưng có mặt biến $i$.
- Biểu thức $f_x(S)$ là giá trị dự báo của mô hình khi tập đặc trưng vắng mặt biến $i$.
- Hiệu số $[f_x(S \cup \{i\}) - f_x(S)]$ phản ánh mức đóng góp cận biên thuần túy của biến $i$ vào liên minh $S$.

#### Cơ chế chuẩn hóa điểm xếp hạng (Ensemble Ranking Score) từ 1 đến M
- Các chỉ số độ quan trọng từ Gini, Permutation và SHAP khác biệt hoàn toàn về nguyên lý toán học và thang đo giá trị.
- Sự khác biệt về thang đo ngăn cản việc so sánh trực tiếp hoặc tính toán trung bình giá trị thô giữa ba phương pháp.
- Nhóm tác giả đề xuất chỉ số điểm xếp hạng (ranking score metric) để chuẩn hóa độ quan trọng đặc trưng (Zheng et al., 2023).
- Giá trị độ quan trọng của từng phương pháp được sắp xếp theo thứ tự tăng dần.
- Mỗi biến đặc trưng nhận một điểm thứ hạng số nguyên tương ứng với vị trí xuất hiện trong danh sách sắp xếp.
- Biến đặc trưng có độ quan trọng thấp nhất nhận điểm số nhỏ nhất là $1$.
- Biến đặc trưng có độ quan trọng thấp thứ hai nhận điểm số là $2$.
- Biến đặc trưng có độ quan trọng cao nhất nhận điểm số tối đa bằng tổng số biến đặc trưng là $M$ ($M = 11$).
- Thang điểm chuẩn hóa từ $1$ đến $M$ tạo lập hệ quy chiếu thống nhất giữa các phương pháp diễn giải khác nhau.
- Điểm xếp hạng tổ hợp cung cấp góc nhìn toàn diện và loại bỏ hoàn toàn các sai lệch chủ quan của từng phương pháp riêng lẻ.

## Chương 3: Kết quả Thực nghiệm và Phân tích Hiệu năng

### 3.1 Hiệu năng vượt trội của AutoML so với Deep Learning trong mô hình hóa AnMBR
#### So sánh định lượng hiệu năng dự đoán (AutoML vs FCN, CNN, DenseNet - Bảng 1)
- AutoML dùng tập dữ liệu 185 mẫu từ nghiên cứu Li et al. (2022).
- Tập đặc trưng gồm 6 biến: $T\text{-R}$, $T\text{-in}$, $T\text{-env}$, $\text{pH-in}$, $\text{COD-in}$, $\text{flux}$.
- Biến mục tiêu là hiệu suất loại bỏ COD ($\text{COD-re}$, đơn vị $\%$).
- Tỉ lệ phân chia dữ liệu gồm 166 mẫu huấn luyện và 19 mẫu kiểm thử (9:1).
- Mô hình FCN ghi nhận $\text{RMSE} = 6.29\%$ và $\text{MAE} = 5.71\%$.
- Mô hình FCN đạt $\text{MAPE} = 6.49\%$ và $R^2 = -1.19$.
- Mô hình CNN ghi nhận $\text{RMSE} = 5.98\%$ và $\text{MAE} = 5.34\%$.
- Mô hình CNN đạt $\text{MAPE} = 6.02\%$ và $R^2 = -0.97$.
- Mô hình DenseNet ghi nhận $\text{RMSE} = 4.69\%$ và $\text{MAE} = 4.34\%$.
- Mô hình DenseNet đạt $\text{MAPE} = 4.93\%$ và $R^2 = -0.21$.
- Trên tập kiểm thử của Li et al. (2022), AutoML đạt $\text{RMSE} = 3.09\%$.
- AutoML đạt $\text{MAE} = 2.76\%$, $\text{MAPE} = 3.11\%$ và $R^2 = 0.47$.
- Qua kiểm định chéo 10 lần (10-fold CV), AutoML đạt $\text{RMSE} = 2.47\%$.
- Khoảng tin cậy $95\%$ của RMSE là $[2.14\%, 2.81\%]$ (biên độ $\pm 0.33\%$).
- Chỉ số $\text{MAE}$ trung bình đạt $1.90\%$ với khoảng tin cậy $[1.68\%, 2.11\%]$.
- Chỉ số $\text{MAPE}$ trung bình đạt $2.19\%$ với khoảng tin cậy $[1.93\%, 2.46\%]$.
- Hệ số $R^2$ trung bình đạt $0.44$ với khoảng tin cậy $[0.22, 0.65]$.
- Biên độ hẹp $\pm 0.33\%$ chứng minh AutoML có độ bền vững cao.

#### Phân tích nguyên nhân thất bại của Deep Learning và ưu thế của mô hình cây trên dữ liệu bảng nhỏ
- Công thức tính hệ số xác định:
  $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
- Giá trị $R^2 < 0$ xuất hiện khi tổng bình phương sai số vượt quá phương sai dữ liệu.
- Các mô hình Deep Learning dự đoán kém hơn giá trị trung bình $\bar{y}$.
- Hiện tượng quá khớp nảy sinh do số lượng trọng số lớn trên mẫu nhỏ ($n = 185$).
- Dữ liệu thiếu các biến đo lường động học làm giảm độ khái quát của Deep Learning.
- Cấu trúc mạng nơ-ron không phù hợp với dữ liệu bảng có chiều không gian nhỏ.
- Thư viện FLAML chọn các mô hình cây: Random Forest, Extra Trees, XGBoost, LightGBM, CatBoost.
- Mô hình cây phân chia không gian đặc trưng bằng các mặt cắt trực giao.
- Thuật toán cây không cần chuẩn hóa dữ liệu hay biến đổi phi tuyến phức tạp.
- Cấu trúc cây ngăn chặn hiện tượng bão hòa gradient trên dữ liệu bảng nhỏ.
- Phương pháp CFO bắt đầu từ mô hình nhỏ và tăng dần độ phức tạp.
- Thuật toán BlendSearch kết hợp tìm kiếm toàn cục và tối ưu cục bộ trong 300 giây.
- Giá trị $\text{RMSE} = 3.09\%$ của AutoML thấp hơn độ lệch chuẩn AnMBR ($3.5\% - 5.0\%$).
- Độ chính xác của AutoML đáp ứng tốt yêu cầu mô phỏng động học AnMBR.

#### Đánh giá tính nhất quán và độ ổn định dự đoán qua phân tích Bland-Altman (Hình 3)
- Phương pháp Bland-Altman định lượng độ tương đồng giữa giá trị thực ($y$) và dự đoán ($\hat{y}$).
- Sai khác giữa hai giá trị tính theo công thức:
  $$d_i = y_i - \hat{y}_i$$
- Sai khác trung bình biểu diễn độ lệch:
  $$\bar{d} = \frac{1}{n} \sum_{i=1}^n d_i$$
- Giới hạn thỏa thuận $95\%$ (LoA):
  $$\text{LoA} = [\bar{d} - 1.96 \times s_d, \quad \bar{d} + 1.96 \times s_d]$$
  trong đó $s_d$ là độ lệch chuẩn của các sai khác $d_i$.
- Giới hạn thỏa thuận rộng phản ánh tính nhất quán kém giữa mô hình và thực tế.
- Các mô hình Deep Learning thể hiện dải thỏa thuận rất rộng trên Hình 3.
- Sai số Deep Learning giảm dần khi giá trị trung bình tăng lên (hiệu ứng phễu).
- Deep Learning mất ổn định ở vùng hiệu suất COD thấp.
- AutoML có dải thỏa thuận hẹp hơn và sai số phân bố đồng đều (Hình 3a).
- Sai số của AutoML phân tán ngẫu nhiên qua toàn bộ dải giá trị trung bình.
- Đại đa số điểm dữ liệu của AutoML nằm trong khoảng tin cậy $95\%$.
- Tất cả mô hình đều ghi nhận sai khác trung bình dương ($\bar{d} > 0$).
- Độ lệch dương cho thấy mô hình có xu hướng dự đoán thấp hơn thực tế.
- Xu hướng này do mất cân bằng phân phối giữa tập huấn luyện và kiểm thử.
- Mô hình làm mịn nhiễu đo lường và dao động sinh học tức thời.

### 3.2 Tác động nâng cao hiệu năng khi bổ sung thời gian vận hành (OD)
#### Giả thuyết khoa học và vai trò biến đại diện (proxy) của ngày vận hành OD
- Hiệu suất AnMBR phụ thuộc vào cấu trúc và hoạt tính của quần thể vi sinh vật.
- Đo đạc vi sinh vật tốn chi phí cao và mất nhiều thời gian.
- Tần suất lấy mẫu vi sinh thấp cản trở mô hình hóa học máy.
- Nhóm tác giả giả thuyết ngày vận hành (OD) tương quan với động học sinh học.
- Biến OD (50 đến 414 ngày) đóng vai trò biến đại diện (surrogate variable).
- OD phản ánh quá trình thích nghi của bùn kỵ khí và màng sinh học.
- OD phản ánh biến đổi đặc tính bề mặt màng và tích tụ chất bẩn.
- Trục thời gian OD giúp mô hình học các hành vi phi dừng của hệ phản ứng.

#### Cải thiện định lượng khi tích hợp OD vào tập đặc trưng nền tảng ($R^2$, RMSE)
- Tập nền tảng gồm 6 biến: $T\text{-R}$, $T\text{-in}$, $T\text{-env}$, $\text{pH-in}$, $\text{COD-in}$, $\text{flux}$.
- Khi tích hợp OD, hệ số $R^2$ trung bình tăng từ $0.44$ lên $0.55$.
- Mức tăng $R^2$ tương ứng mức cải thiện $+25.0\%$ theo Hình 4 và Hình S1.
- Sai số $\text{RMSE}$ trung bình giảm từ $2.47\%$ xuống $2.20\%$ (giảm $-10.9\%$).
- Khoảng tin cậy $95\%$ của các chỉ số đều thu hẹp rõ rệt.
- Kết quả khẳng định mô hình tiếp thu hiệu quả thông tin từ biến OD.
- Mô hình nắm bắt chính xác quy luật biến thiên COD theo từng pha vận hành.

#### Kiểm định nguy cơ rò rỉ dữ liệu (Data Leakage) và giới hạn ngoại suy của mô hình cây
- Phân tích tương quan Spearman đánh giá liên hệ giữa OD và nhãn $\text{COD-re}$.
- Kết quả ghi nhận mối tương quan rất yếu giữa OD và $\text{COD-re}$.
- Mối tương quan yếu loại trừ nguy cơ rò rỉ dữ liệu từ thời gian sang nhãn.
- Mô hình học được động học phi tuyến, không ghi nhớ chỉ mục thời gian đơn thuần.
- Mô hình cây phân chia không gian bằng các mặt cắt trực giao từng đoạn.
- Giá trị dự đoán tại mỗi nút lá là một hằng số cố định.
- Mô hình cây không thể ngoại suy ngoài phạm vi huấn luyện ($\text{OD} > 414\text{ ngày}$).
- Dự đoán cho các ngày ngoài ngưỡng huấn luyện sẽ bão hòa tại hằng số biên.
- Người vận hành cần hiệu chuẩn lại mô hình khi hệ thống bước sang chu kỳ mới.

#### Tác động hạn chế của các thông số vật lý - sinh học khác (ORP, HRT, MLSS, MLVSS)
- Nghiên cứu khảo sát thêm 4 thông số: $\text{ORP}$, $\text{HRT}$, $\text{MLSS}$, $\text{MLVSS}$.
- Khi dùng cả 5 biến (OD, ORP, HRT, MLSS, MLVSS), hiệu năng tương đương chỉ có OD.
- Mô hình chứa các thông số trên mà thiếu OD không đem lại cải thiện đáng kể.
- Phân tích Bland-Altman cho thấy biến OD thu hẹp dải sai số quanh mốc 0 (Hình 5).
- Bổ sung ORP, HRT, MLSS và MLVSS không làm giảm thêm khoảng thỏa thuận.
- Tần suất đo tuần của MLSS và MLVSS làm mờ tín hiệu thực nghiệm qua nội suy.
- Tỉ số tín hiệu trên nhiễu thấp làm lu mờ mối liên hệ sinh học.
- Hiện tượng cộng tuyến đa biến khiến thông tin bị trùng lặp với tập cơ sở.
- Kết quả khẳng định tầm quan trọng của việc chọn lọc đặc trưng chặt chẽ.

### 3.3 Tác động nghịch lý của thể tích dữ liệu đến hiệu năng dự đoán
#### Thiết kế 3 kịch bản xác thực quy mô dữ liệu (M1T1, M2T1, M2T2)
- Quan niệm phổ biến giả định tăng kích thước dữ liệu luôn tăng hiệu năng mô hình.
- Dữ liệu thực nghiệm môi trường thường nhỏ do giới hạn chi phí và không gian.
- Dữ liệu thực nghiệm dễ bị nhiễu bởi sai số đo và thao tác con người.
- Việc so sánh tập dữ liệu nhỏ chất lượng cao với tập lớn chứa nhiễu là vấn đề lớn.
- Tập dữ liệu gốc $M_1$ gồm 185 mẫu trong khoảng ngày 50 đến 414.
- Tập dữ liệu mở rộng $M_2$ gồm 320 mẫu trong khoảng ngày 7 đến 546.
- Kịch bản $M_1T_1$: 10-fold CV trên $M_1$, kiểm thử trên các tập con $T_1$ từ $M_1$.
- Kịch bản $M_2T_1$: Thêm 135 mẫu vào tập huấn luyện, kiểm thử trên cùng tập $T_1$.
- Kịch bản $M_2T_2$: 10-fold CV tiêu chuẩn trên toàn bộ 320 mẫu của tập $M_2$.
- Thiết kế $M_2T_1$ giúp đánh giá việc mở rộng dữ liệu trên cùng chuẩn kiểm thử.

#### Hiện tượng suy giảm hiệu năng khi mở rộng dữ liệu huấn luyện (Hình 6)
- So sánh $M_1T_1$ và $M_2T_1$ cho thấy thêm dữ liệu làm giảm hệ số $R^2$.
- Các sai số $\text{RMSE}$, $\text{MAE}$, $\text{MAPE}$ đều tăng khi thêm 135 mẫu huấn luyện.
- So sánh $M_1T_1$ và $M_2T_2$ cho thấy sai số tăng vọt trên toàn dải $M_2$.
- Kịch bản $M_2T_2$ cho hiệu năng dự đoán kém nhất trong cả ba phương án (Hình 6).
- Kết quả xác lập nghịch lý: Thêm dữ liệu thực nghiệm không giúp cải thiện mô hình.

#### Cơ chế dịch chuyển phân phối dữ liệu (Distribution Shift) và suy giảm tương quan Spearman
- Tương quan Spearman giữa $M_1$ và $M_2$ được minh họa tại Hình S3 và S4.
- Đặc trưng trong tập $M_2$ có tương quan với COD thấp hơn so với trong $M_1$.
- Mức độ liên quan của dữ liệu quyết định trực tiếp độ chính xác của mô hình.
- Dịch chuyển phân phối phát sinh do thay đổi dòng vào hoặc trạng thái sinh học.
- 135 mẫu bổ sung thuộc ngày 7-49 và ngày 415-546 mang nhiều biến động ngoại cảnh.
- Giai đoạn khởi động có hệ vi sinh chưa ổn định, gây sai lệch quy luật chuyển hóa.
- Tác hại của dịch chuyển phân phối vượt xa lợi ích từ việc tăng số lượng mẫu.
- Hiệu năng giảm sút phản ánh việc mô hình đã thu nhận dữ liệu không liên quan.

#### Bài học cốt lõi: Ưu tiên chất lượng và tính đặc thù ngữ cảnh hơn số lượng dữ liệu
- Chuyên gia cần đánh giá kỹ nguồn gốc và chất lượng dữ liệu trước khi mô hình hóa.
- Tăng thể tích dữ liệu mà bỏ qua tính không đồng nhất sẽ làm giảm độ chính xác.
- Kỹ thuật dữ liệu cần ưu tiên chất lượng và tính đặc thù ngữ cảnh của mẫu.
- Nghiên cứu tương lai cần phát triển kỹ thuật thích ứng miền để xử lý sai lệch phân phối.

## Chương 4: Phân tích Tầm quan trọng Đặc trưng, Giới hạn và Kết luận

### 4.1 Phân tích độ quan trọng đặc trưng bằng phương pháp kết hợp (Ensemble Ranking Score)
#### Vị thế chi phối của nồng độ COD đầu vào (COD-in) và vai trò cảnh báo sớm
- Đặc trưng $COD\text{-in}$ giữ vị trí số một trong mọi mô hình và phương pháp giải thích (Hình 7).
- Giá trị $COD\text{-in}$ phản ánh trực tiếp tải nạp hữu cơ (OLR). Biến này đo lường nồng độ chất ô nhiễm vào bể AnMBR.
- Quá trình phân hủy kỵ khí phụ thuộc vào nồng độ cơ chất nạp. Nồng độ này duy trì hoạt tính trao đổi chất của sinh khối.
- Đặc trưng $COD\text{-in}$ đóng vai trò tín hiệu cảnh báo sớm (warning signal) đáng tin cậy cho dự đoán hiệu suất loại bỏ $COD\text{-re}$.
- Khi cảm biến phát hiện nồng độ $COD\text{-in}$ tăng vọt, hệ thống điều khiển tự động giảm lưu lượng nạp ($Q_{\text{in}}$).
- Việc giảm lưu lượng nạp làm tăng thời gian lưu thủy lực ($HRT$). Vi sinh vật có thêm thời gian để phân hủy cơ chất hữu cơ.

#### Vai trò nổi bật của ngày vận hành (OD) phản ánh động học phi tĩnh
- Biến $OD$ giữ vị trí quan trọng thứ hai khi đưa vào mô hình (Hình 7(c–g)). Thứ hạng này xuất hiện trên toàn bộ các cấu hình.
- Biến $OD$ đóng vai trò đại diện thời gian (time-proxy variable) cho động học phi tĩnh (non-stationary dynamics) của hệ AnMBR dài hạn.
- Sự tích lũy lớp bánh bùn (cake layer) và tắc nghẽn màng (membrane fouling) gia tăng liên tục theo thời gian vận hành.
- Quần xã vi sinh vật kỵ khí trải qua quá trình thích nghi liên tục. Cấu trúc sinh khối biến đổi theo số ngày vận hành thực tế.
- Giám sát vận hành AnMBR không thể chỉ dựa vào các chỉ số cảm biến tức thời (instantaneous sensor readings).
- Kỹ sư vận hành phải tích hợp lịch trình bảo dưỡng màng và sục rửa định kỳ phụ thuộc thời gian tích lũy ($OD$).

#### Sự biến thiên thứ hạng giữa các phương pháp giải thích (Tree-based, Permutation, SHAP)
- Ba phương pháp cho thấy sai khác thứ hạng rõ rệt (Hình 7(b, d, f, h)). Sự phân hóa này tập trung ở các đặc trưng bậc trung.
- Độ quan trọng Gini (Tree-based method) đo lường mức giảm độ tinh khiết chuẩn hóa trên các điểm rẽ nhánh cây quyết định.
- Độ quan trọng hoán vị (Permutation Importance) đo mức suy giảm hiệu năng $RMSE$ qua $K = 30$ lần xáo trộn ngẫu nhiên:
  $$i_j = s - \frac{1}{K} \sum_{k=1}^K s_{k,j}$$
- Ở đây, $s$ là điểm sai số gốc ($RMSE$). Giá trị $s_{k,j}$ là sai số sau khi hoán vị đặc trưng $j$ tại lần lặp $k$.
- Phương pháp SHAP (Shapley Additive exPlanations) tính toán đóng góp biên trung bình theo lý thuyết trò chơi hợp tác:
  $$\phi_i(f, x) = \sum_{S \subseteq S_{\text{all}} \setminus \{i\}} \frac{|S|!(M - |S| - 1)!}{M!} [f_x(S \cup \{i\}) - f_x(S)]$$
- Ở đây, $M$ là tổng số biến đầu vào, $S$ là tập con các biến không chứa $i$, và $|S|$ là kích thước tập con.
- Đối với mô hình không có $OD$ huấn luyện trên tập gốc, nhiệt độ môi trường ($T\text{-env}$) xếp thứ hai (Hình 7(a)).
- Khi huấn luyện cùng dữ liệu bổ sung, chỉ số $pH\text{-in}$ lại vươn lên thành đặc trưng quan trọng thứ hai (Hình 7(e)).
- Các đặc trưng môi trường như $T\text{-env}$, $T\text{-in}$, và $pH\text{-in}$ thể hiện mức độ đóng góp thấp hơn nhiều so với $COD\text{-in}$.
- Khung điểm xếp hạng kết hợp (Ensemble Ranking Score) chuẩn hóa thứ tự từ $1$ (ít quan trọng nhất) đến $M$ (quan trọng nhất):
  $$R_j = \sum_{m \in \{\text{Tree, Perm, SHAP}\}} \text{Rank}_m(j)$$
- Điểm xếp hạng kết hợp giải quyết triệt để sự thiếu nhất quán giữa các tiên đề toán học riêng lẻ.

#### Tác động làm xáo trộn thứ tự đặc trưng khi thêm dữ liệu nhiễu (M2)
- Huấn luyện với tập dữ liệu mở rộng M2 (7–546 ngày, 320 mẫu) làm biến động mạnh thứ bậc đặc trưng.
- Kết quả giải thích của mô hình M2 (Hình 7(h)) sai lệch mạnh so với mô hình gốc (Hình 7(f)).
- Tương quan Spearman khẳng định các đặc trưng trong tập M2 ít liên kết với $COD\text{-re}$ (Hình S3 và S4).
- Tập M2 mang theo nhiễu từ các đợt vận hành không đồng nhất. Dữ liệu này gây ra hiện tượng dịch chuyển phân phối (distribution shift).
- Nhiễu ngẫu nhiên làm biến dạng cấu trúc phân nhánh cây và làm sai lệch giá trị Shapley biên.
- Kết quả này củng cố phát hiện ở Mục 3.3. Dữ liệu mở rộng M2 làm giảm độ chuẩn xác của mô hình học máy.

#### Ý nghĩa kỹ thuật và ứng dụng trong tự động hóa kiểm soát vận hành AnMBR
- Kết quả xếp hạng đặc trưng cho phép phân tầng mức độ ưu tiên của các biến điều khiển trong thực tế công nghệ.
- Thiết lập cơ chế kiểm soát phản hồi hai vòng lặp (dual-loop feedback control architecture):
  - Vòng lặp phản hồi nhanh (Fast response loop): Giám sát liên tục nồng độ $COD\text{-in}$ để điều chỉnh kịp thời tải lượng nạp hữu cơ.
  - Vòng lặp phản hồi chậm (Slow supervisory loop): Lập kế hoạch rửa ngược (backwash), sục khí biogas và ngâm hóa chất dựa trên biến $OD$.
- Tối ưu chi phí quan trắc. Đơn vị vận hành có thể giảm bớt các cảm biến thứ cấp có đóng góp dự báo thấp.
- Mô hình giúp đảm bảo hệ thống màng AnMBR vận hành an toàn. Hệ thống ngăn ngừa tắc nghẽn màng sớm và ổn định dòng ra xử lý nước thải.

### 4.2 Giới hạn nghiên cứu và định hướng phát triển tương lai
#### Tính chất chỉ dấu của kết quả so sánh trong thiết lập thực nghiệm
- Mô hình AutoML vượt trội so với các mạng nơ-ron sâu (FCN, CNN, DenseNet) trên cùng tỷ lệ chia dữ liệu cố định (9:1).
- Kết quả so sánh này mang tính chất chỉ dấu (indicative) trong phạm vi thiết lập thực nghiệm cụ thể của nghiên cứu.
- Các nhà nghiên cứu không nên coi kết quả này là sự vượt trội tuyệt đối trên mọi kịch bản và kiến trúc khác.
- Mô hình học máy dạng cây (Tree-based ML) gặp rào cản ngoại suy (extrapolation limitation) khi giá trị đầu vào vượt ngoài dải huấn luyện.
- Mô hình cây dự đoán kém chính xác khi $OD > 414$ ngày. Mô hình cũng giảm độ tin cậy khi $COD\text{-in}$ vượt ngưỡng cực đại.

#### Ý nghĩa thống kê của các biến sinh khối (MLSS/MLVSS) so với cơ chế vi sinh
- Hai biến đặc trưng $MLSS$ và $MLVSS$ thể hiện mức độ đóng góp rất thấp vào hiệu năng mô hình học máy.
- Đóng góp thấp này chỉ phản ánh mối tương quan thống kê trên tập dữ liệu khảo sát hiện hành.
- Người vận hành không được diễn giải kết quả này thành kết luận về mặt cơ chế vật lý hoặc sinh học kỵ khí.
- Về mặt cơ chế sinh hóa, nồng độ bùn hoạt tính kỵ khí ($MLVSS$) giữ vai trò trung tâm phân hủy chất hữu cơ.
- Biến sinh khối xếp hạng thấp do tần suất phân tích thưa thớt (đo hàng tuần). Dải biến động thực tế của bùn cũng rất hẹp.
- Sai số tích lũy trong quy trình sấy cân phòng thí nghiệm làm suy giảm tín hiệu tương quan của biến sinh khối.

#### Bài học về tính nhất quán dữ liệu thay vì số lượng thuần túy
- Hiệu năng mô hình giảm sút khi tăng từ 185 lên 320 mẫu. Hiện tượng này đem lại bài học đắt giá về chất lượng dữ liệu.
- Quy mô dữ liệu lớn không đồng nghĩa với độ chính xác cao nếu dữ liệu thiếu tính đồng nhất ngữ cảnh vận hành.
- Hiện tượng dịch chuyển phân phối (distribution shift) giữa các giai đoạn thí nghiệm gây tổn hại nghiêm trọng cho giải thuật học máy.
- Quy trình chuẩn bị dữ liệu (data curation) cần ưu tiên độ tin cậy và tính nhất quán hơn việc gộp dữ liệu bừa bãi.
- Kỹ sư môi trường cần kiểm soát chặt chẽ điều kiện vận hành trước khi kết hợp dữ liệu từ nhiều nguồn khác nhau.

#### Nhu cầu chuyển đổi từ ước lượng điểm sang mô hình hóa xác suất (Probabilistic ML)
- Mô hình hiện tại chỉ cung cấp các ước lượng điểm tất định (deterministic point estimates) cho giá trị $COD\text{-re}$.
- Dự đoán điểm đơn lẻ bỏ qua độ bất định cố hữu. Hệ phản ứng sinh học kỵ khí luôn có động học dao động phức tạp.
- Các nghiên cứu tương lai cần tích hợp các hướng tiếp cận học máy xác suất (Probabilistic Machine Learning).
- Phương pháp hồi quy lượng vị (Quantile Regression), mạng Bayes (Bayesian Neural Networks) hoặc Conformal Prediction cần được nghiên cứu áp dụng.
- Mô hình xác suất cung cấp khoảng dự đoán (prediction intervals). Kỹ thuật này định lượng độ bất định và giúp ra quyết định an toàn.

### 4.3 Kết luận tổng quát và đóng góp khoa học
#### Tổng kết hiệu năng vượt trội và tính khả thi của FLAML AutoML
- Công trình giải quyết thành công rào cản chuyên môn khoa học dữ liệu cho kỹ sư vận hành xử lý nước thải.
- Khung FLAML AutoML chứng minh tính khả thi vượt trội trong việc xây dựng mô hình dự đoán hiệu suất AnMBR chính xác.
- Mô hình AutoML họ cây đảo ngược hoàn toàn $R^2$ âm của các mạng học sâu trước đây, nâng $R^2$ từ âm lên $+0.47$.
- Khi bổ sung biến thời gian vận hành $OD$, hệ số xác định $R^2$ tiếp tục tăng lên mức $0.55$.
- Mô hình đạt các chỉ số sai số rất thấp: $RMSE = 3.09\%$, $MAE = 2.76\%$, và $MAPE = 3.11\%$.
- Ngân sách thời gian tối ưu hóa rất tiết kiệm. Quá trình chỉ mất 300 giây nhờ hai thuật toán CFO và BlendSearch.
- Phân tích Bland-Altman xác nhận độ ổn định cao với hầu hết các sai số nằm gọn trong khoảng giới hạn thỏa thuận 95%.

#### Khuyến nghị thực tiễn cho nghiên cứu xử lý nước thải quy mô phòng thí nghiệm và pilot
- Triển khai khung FLAML AutoML làm công cụ tiêu chuẩn cho mô hình hóa các bài toán xử lý nước thải dữ liệu mẫu nhỏ.
- Khuyến nghị đưa biến thời gian vận hành tích lũy ($OD$) vào danh mục biến bắt buộc khi quan trắc bể phản ứng màng.
- Áp dụng khung Ensemble Ranking Score để phân tích độ quan trọng đặc trưng, tránh các sai lệch từ một giải thuật đơn lẻ.
- Tận dụng quy trình nghiên cứu triệt tiêu (Ablation study) tự động của AutoML để chọn lọc tập đặc trưng tối giản và hiệu quả.
- Tái định hướng đầu tư cảm biến: Tập trung vào cảm biến giám sát liên tục $COD\text{-in}$ và kiểm soát lịch bảo trì theo $OD$.

### 4.4 Thông tin bổ trợ và Đóng góp tác giả
#### Đóng góp tác giả theo chuẩn CRediT
- Tác giả Junjie Yu:
  - Soạn thảo bản thảo ban đầu (Writing – original draft).
  - Trực quan hóa dữ liệu và đồ thị (Visualization).
  - Lập trình và thử nghiệm phần mềm (Software).
  - Thực hiện điều tra thực nghiệm (Investigation).
- Tác giả Zhonghua Zheng:
  - Rà soát và biên tập chuyên môn (Writing – review & editing).
  - Cung cấp và điều phối tài nguyên nghiên cứu (Resources).
  - Xây dựng phương pháp luận nghiên cứu (Methodology).
  - Thực hiện điều tra thực nghiệm (Investigation).
- Tác giả Jialing Ni:
  - Rà soát và biên tập bản thảo (Writing – review & editing).
  - Đóng góp tài nguyên nghiên cứu (Resources).
- Tác giả Jiayuan Ji:
  - Định hướng và khởi xướng ý tưởng nghiên cứu (Conceptualization).
  - Phát triển phương pháp luận (Methodology).
  - Quản trị và kiểm tra chất lượng dữ liệu (Data curation).
  - Thu nhận các nguồn tài trợ nghiên cứu (Funding acquisition).
  - Viết bản thảo gốc cùng rà soát biên tập (Writing – original draft, review & editing).
  - Thực hiện điều tra thực nghiệm (Investigation).

#### Tuyên bố xung đột lợi ích, tài trợ nghiên cứu và dữ liệu bổ sung
- Tuyên bố xung đột lợi ích: Nhóm tác giả tuyên bố không có xung đột lợi ích. Không có quan hệ tài chính hoặc cá nhân nào ảnh hưởng đến bài báo.
- Tài trợ từ Quỹ Xúc tiến Khoa học Nhật Bản: Quỹ JSPS KAKENHI tài trợ cho nghiên cứu này theo Mã hợp đồng JP24K17380.
- Tài trợ xây dựng cơ sở dữ liệu: Quỹ JIC Foundation tài trợ một phần việc xây dựng dữ liệu qua Mã số 2022-7.
- Hỗ trợ nguồn lực học thuật: Đại học Manchester cấp quỹ khởi động nghiên cứu cho tác giả Zhonghua Zheng.
- Hỗ trợ biên tập ngôn ngữ: Công ty Editage thực hiện hiệu đính tiếng Anh chuyên môn cho bài viết.
- Dữ liệu bổ trợ trực tuyến (Appendix A): Tài liệu bổ trợ được lưu trữ trực tuyến tại địa chỉ https://doi.org/10.1016/j.jenvman.2026.128801.
- Tính khả dụng của dữ liệu (Data availability): Nhóm nghiên cứu không có quyền chia sẻ công khai bộ dữ liệu gốc. Quy định bảo mật dự án không cho phép công bố dữ liệu này.
