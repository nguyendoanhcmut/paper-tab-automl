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
  1. Rừng ngẫu nhiên (Random Forest - RF) đóng gói tập hợp các cây quyết định độc lập (Breiman, 2001).
  2. Cây cực kỳ ngẫu nhiên (Extra Trees / Extremely Randomized Trees) ngẫu nhiên hóa triệt để ngưỡng phân tách (Geurts et al., 2006).
  3. XGBoost triển khai hệ thống tăng cường độ dốc cây có khả năng mở rộng quy mô cao (Chen and Guestrin, 2016).
  4. LightGBM tối ưu hóa cây tăng cường độ dốc bằng chiến lược phát triển cây theo lá hiệu năng cao (Ke et al., 2017).
  5. CatBoost thực thi thuật toán tăng cường độ dốc với cơ chế xử lý biến phân loại và giảm thiểu dịch chuyển mục tiêu (Dorogush et al., 2018).

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
