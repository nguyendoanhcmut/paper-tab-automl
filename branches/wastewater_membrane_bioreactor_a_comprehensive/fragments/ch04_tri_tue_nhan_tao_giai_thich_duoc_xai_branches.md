## Chương 4: Trí tuệ Nhân tạo có thể Giải thích trong Hệ thống MBR (Explainable Artificial Intelligence in MBR Applications)

### 4.1 Yêu cầu bắt buộc về tính khả giải trong hệ thống nước có quản lý nghiêm ngặt

#### 4.1.1 Trách nhiệm pháp lý và an toàn môi trường trong vận hành MBR
- Rào cản triển khai Machine Learning (ML) trong ngành nước:
  - Ngành xử lý nước thải vận hành dưới các quy định môi trường pháp lý nghiêm ngặt.
  - Các hệ thống công nghiệp thông thường chấp nhận mô hình hộp đen khi mô hình giảm chi phí sản xuất.
  - Các nhà máy xử lý nước thải yêu cầu độ tin cậy tuyệt đối và khả năng giải trình nguyên nhân kỹ thuật trước các cơ quan quản lý nhà nước.
- Rủi ro pháp lý và an toàn vận hành:
  - Khuyến nghị giảm lưu lượng sục khí màng từ mô hình AI có thể gây hiện tượng tắc nghẽn màng không thể phục hồi (irreversible fouling).
  - Quyết định sai lầm của AI có thể làm gián đoạn quá trình lọc và gây vi phạm tiêu chuẩn xả thải ra nguồn tiếp nhận (permit violations).
  - Kỹ sư vận hành phải kiểm chứng tính hợp lý vật lý của mọi khuyến nghị điều khiển trong thời gian của ca trực (operating shift) [29, 51].
- Tiêu chuẩn chấp thuận mô hình điều khiển trong ngành nước:
  - Mô hình ML không chỉ cần độ chính xác dự báo cao.
  - Khuyến nghị điều khiển phải bảo đảm tính hợp lý kỹ thuật (engineering plausibility).
  - Hệ thống phải có khả năng lưu vết và lập tài liệu giải trình nguyên nhân cho từng quyết định (document decision rationale) [29].

#### 4.1.2 Rào cản tâm lý người vận hành và sự đánh đổi giữa hộp đen và hộp trắng
- Sự ngờ vực đối với mô hình hộp đen:
  - Người vận hành có tâm lý từ chối các chỉ thị tự động nếu không hiểu rõ mối liên hệ nhân quả vật lý.
  - Tâm lý e ngại rủi ro hình thành do hậu quả nghiêm trọng của các sự cố tràn bùn hoặc tắc nghẽn màng đột ngột.
- Luận điểm của Rudin về mô hình khả giải cố hữu:
  - Rudin [51] khẳng định các lĩnh vực ra quyết định tuần tự có rủi ro cao phải ưu tiên sử dụng mô hình có tính khả giải cố hữu (inherently interpretable models).
  - Phương pháp giải thích hậu kiểm (post-hoc explanations) có thể tạo ra ảo tưởng về tính minh bạch nếu mô hình xấp xỉ không khớp với thực tế.
- Giới hạn biểu diễn của mô hình hộp trắng trong MBR:
  - Động học tắc nghẽn màng trong MBR có tính phi tuyến mạnh, phụ thuộc nhiều biến trạng thái và biến thiên theo thời gian.
  - Các mô hình hộp trắng đơn giản (như hồi quy tuyến tính hoặc cây quyết định nông) không đủ năng lực biểu diễn để đạt độ chính xác cần thiết cho vận hành thực tế.
- Lựa chọn thực dụng từ XAI hậu kiểm:
  - Áp dụng các kỹ thuật XAI hậu kiểm (post-hoc XAI) trên các mô hình hộp đen hiệu năng cao (Random Forest, XGBoost, CatBoost, LSTM) là giải pháp thực tế nhất cho hệ thống MBR [48].
  - XAI tạo cầu nối giúp chuyên gia công nghệ đánh giá, kiểm chứng với quy luật động học bùn hoạt tính và thực thi hành động điều khiển kịp thời [29].

---

### 4.2 SHAP: Khung giải thích chủ đạo trong nghiên cứu MBR

#### 4.2.1 Nền tảng lý thuyết trò chơi hợp tác và công thức giá trị Shapley
- Cơ sở lý thuyết của SHAP (SHapley Additive exPlanations):
  - Phương pháp SHAP [52] xây dựng trên nền tảng lý thuyết trò chơi hợp tác của Lloyd Shapley.
  - Phương pháp xem các biến đặc trưng đầu vào như các người chơi trong một liên minh cùng đóng góp vào giá trị dự báo cuối cùng.
  - SHAP là khung giải thích xuất hiện phổ biến nhất trong các công bố nghiên cứu về MBR [53].
- Công thức toán học tính giá trị Shapley:
  - Giá trị đóng góp biên kỳ vọng $\phi_i$ của đặc trưng $i$ được xác định theo công thức:
    $$\phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} (f(S \cup \{i\}) - f(S))$$
  - Trong đó:
    - $N$: Tập hợp toàn bộ các đặc trưng đầu vào của mô hình.
    - $S$: Tập con các đặc trưng không chứa đặc trưng $i$ ($S \subseteq N \setminus \{i\}$).
    - $|S|$: Số lượng đặc trưng có trong tập hợp liên minh $S$.
    - $|N|$: Tổng số lượng đặc trưng đầu vào.
    - $f(S)$: Giá trị dự báo của mô hình khi chỉ sử dụng tập hợp đặc trưng $S$.
    - $f(S \cup \{i\}) - f(S)$: Đóng góp biên (marginal contribution) của đặc trưng $i$ khi tham gia vào tập hợp liên minh $S$.
    - $\frac{|S|!(|N|-|S|-1)!}{|N|!}$: Trọng số hoán vị ngẫu nhiên của các tập liên minh.

#### 4.2.2 Bốn thuộc tính toán học tiên đề của SHAP
- Tiên đề 1: Tính hiệu quả (Efficiency / Local Accuracy):
  - Tổng các giá trị đóng góp SHAP bằng chênh lệch giữa giá trị dự báo thực tế $f(x)$ và giá trị kỳ vọng cơ sở $\mathbb{E}[f(X)]$:
    $$\sum_{i=1}^{|N|} \phi_i(x) = f(x) - \mathbb{E}[f(X)] = f(x) - \phi_0$$
  - Thuộc tính bảo đảm phân bổ đầy đủ 100% sai lệch dự báo cho các biến đầu vào, không làm thất thoát thông tin.
- Tiên đề 2: Tính đối xứng (Symmetry):
  - Nếu hai đặc trưng $i$ và $j$ có đóng góp biên tương đương vào mọi liên minh khả dĩ ($f(S \cup \{i\}) = f(S \cup \{j\})$ với mọi $S \subseteq N \setminus \{i, j\}$):
    $$\phi_i = \phi_j$$
  - Thuộc tính bảo đảm sự công bằng tuyệt đối giữa các biến có vai trò tương đương.
- Tiên đề 3: Biến vô hiệu (Dummy / Null player / Missingness):
  - Nếu một đặc trưng $i$ không làm thay đổi giá trị dự báo trong bất kỳ liên minh nào ($f(S \cup \{i\}) = f(S)$ với mọi $S \subseteq N \setminus \{i\}$):
    $$\phi_i = 0$$
  - Thuộc tính loại bỏ hoàn toàn tác động của các biến nhiễu hoặc các biến không mang thông tin phân biệt.
- Tiên đề 4: Tính cộng (Additivity):
  - Nếu mô hình tổng thể là tổng của hai mô hình thành phần độc lập ($f = f_1 + f_2$):
    $$\phi_i(f_1 + f_2) = \phi_i(f_1) + \phi_i(f_2)$$
  - Thuộc tính cho phép tính toán giải thích nhất quán trên các mô hình kết hợp nhóm (ensemble models) như Random Forest hoặc Gradient Boosting.

#### 4.2.3 Đột phá tính toán: TreeSHAP so với KernelSHAP trên hệ thống SCADA
- Giới hạn tính toán của KernelSHAP:
  - KernelSHAP áp dụng cho mọi loại mô hình (model-agnostic) bằng phương pháp lấy mẫu xấp xỉ không gian đặc trưng.
  - Độ phức tạp tính toán tăng theo hàm số mũ: $\mathcal{O}(2^{|F|})$, với $|F|$ là số biến đặc trưng đầu vào.
  - Thời gian tính toán kéo dài khiến KernelSHAP không thể đáp ứng yêu cầu giám sát trực tuyến theo thời gian thực.
- Thuật toán TreeSHAP tối ưu hóa:
  - TreeSHAP tối ưu hóa riêng cho các mô hình cấu trúc cây (Decision Trees, Random Forest, XGBoost, CatBoost, LightGBM).
  - Thuật toán duyệt đệ quy qua các nhánh cây để theo dõi tỷ lệ mẫu đi qua các nút phân chia.
  - Độ phức tạp tính toán giảm xuống mức đa thức:
    $$\mathcal{O}(T \cdot L \cdot D^2)$$
  - Trong đó:
    - $T$: Tổng số lượng cây quyết định trong mô hình ensemble.
    - $L$: Số lượng lá tối đa trên mỗi cây.
    - $D$: Độ sâu tối đa của cây (thường $D \le 10$).
- Ý nghĩa triển khai SCADA thời gian thực:
  - TreeSHAP tạo ra giải thích định lượng trong vài mili-giây đến vài giây.
  - Tốc độ tính toán đáp ứng trọn vẹn chu kỳ quét dữ liệu của hệ thống SCADA tại nhà máy xử lý nước thải.
  - Hệ thống cho phép hiển thị tức thời nguyên nhân gây rủi ro tắc màng trên màn hình giám sát HMI của người vận hành.

#### 4.2.4 Phân tích SHAP cục bộ và toàn cục trong chẩn đoán suy giảm thông lượng
- Các công cụ trực quan hóa SHAP đa cấp:
  - Biểu đồ tóm tắt (Summary plot / Beeswarm plot): Thể hiện mức độ quan trọng toàn cục và hướng tác động (dương hoặc âm) của từng biến trên toàn bộ tập dữ liệu.
  - Biểu đồ phụ thuộc (Dependence plot): Thể hiện mối quan hệ phi tuyến giữa giá trị thực tế của một biến với giá trị SHAP, tích hợp tương tác với biến thứ hai.
  - Biểu đồ lực đẩy / Thác nước (Force plot / Waterfall plot): Phân tích nguyên nhân cho từng dự báo cục bộ riêng biệt, thể hiện sự giằng co giữa lực làm tăng rủi ro và lực làm giảm rủi ro.
- Kịch bản chẩn đoán cảnh báo tăng TMP trong 4 giờ tại nhà máy MBR đô thị:
  - Mô hình Random Forest cảnh báo áp suất xuyên màng (TMP) sẽ vượt ngưỡng vận hành trong vòng 4 giờ tới.
  - Phân tích Waterfall plot bóc tách đóng góp cụ thể của 4 biến quá trình:
    - $\text{MLSS} = +2.1\text{ kPa}$: Nồng độ bùn hoạt tính gần chạm ngưỡng trên, là nguyên nhân rủi ro hàng đầu.
    - $\text{HRT} = +1.4\text{ kPa}$: Thời gian lưu nước ngắn làm gia tăng tải trọng hữu cơ nạp vào bề mặt màng.
    - Cường độ sục khí (Aeration intensity) $= -0.8\text{ kPa}$: Tác động cắt thủy lực của bọt khí đang kìm hãm một phần tốc độ tắc nghẽn.
    - Lưu lượng nước đầu vào (Feed flow rate) $= +0.6\text{ kPa}$: Dòng vào dâng cao tạo áp lực ép chặt các hạt cặn lên bề mặt màng.
  - Tính hợp lý của quyết định vận hành:
    - Tổng giá trị SHAP cân bằng chính xác với mức tăng TMP dự báo (+3.3 kPa), thỏa mãn tính hiệu quả cục bộ.
    - Kỹ sư vận hành lập tức điều chỉnh tăng lưu lượng khí sục màng và kích hoạt sớm chu kỳ ngâm nghỉ (relaxation cycle).
    - Giải pháp dựa trực tiếp trên các biến đo SCADA quen thuộc, không đòi hỏi kiến thức chuyên sâu về ML [17, 25, 42].
- Cảnh báo hiện tượng rò rỉ dữ liệu (Data Leakage) và quá khớp (Overfitting):
  - Biểu đồ xếp hạng toàn cục phát hiện các biến phi vật lý (ví dụ: nhãn thời gian SCADA timestamp) có giá trị SHAP cao bất thường.
  - Tín hiệu này cảnh báo hiện tượng rò rỉ dữ liệu hoặc mô hình học mối tương quan giả (spurious correlations), giúp hiệu chỉnh tập dữ liệu trước khi triển khai thực tế [17, 53].

#### 4.2.5 Khám phá quy luật vật lý và động học nén bánh cặn qua SHAP chuỗi thời gian
- Kiểm chứng thực nghiệm trên quy mô thực (Full-scale MBR):
  - Nghiên cứu của Liang et al. [49]: Ứng dụng mô hình CatBoost kết hợp XAI cho hệ thống MBR xử lý nước thải chế biến thực phẩm.
  - Độ chính xác mô hình: Đạt hệ số xác định $R^2 = 0.8374$.
  - Phát hiện thuộc tính chi phối: Tỷ lệ thức ăn trên vi sinh vật ($F/M$) và nồng độ $\text{MLSS}$ là hai nhân tố chi phối chính đến tốc độ tắc nghẽn màng, hoàn toàn phù hợp với cơ chế sinh học phân hủy chất nền.
- Kiểm chứng trên hệ thống màng thẩm thấu xuôi (OMBR):
  - Nghiên cứu của Viet và Jang [22]: Ứng dụng mô hình dự báo AI trên hệ thống Osmotic MBR (OMBR).
  - Độ chính xác mô hình: Đạt $R^2 = 0.92\text{--}0.98$ cho dự báo thông lượng nước và trở lực tắc màng.
  - Quy luật vật lý thu nhận: Nồng độ dung dịch rút (draw solution concentration), pH nước đầu vào và độ dẫn điện (conductivity) là các biến chi phối chính, khớp với nguyên lý động lực áp suất thẩm thấu.
- Giám sát chẩn đoán bất thường từ dữ liệu SCADA:
  - Nghiên cứu của Newhart et al. [17]: Xây dựng khung giám sát dựa trên dữ liệu cho quản lý vận hành MBR.
  - Các mô hình ML huấn luyện trên dòng dữ liệu cảm biến SCADA thông thường phát hiện sớm các rối loạn quá trình trước khi xuất hiện suy giảm hiệu năng đo đếm được.
  - Nghiên cứu xác định các biến cảm biến giàu thông tin nhất để ước lượng trạng thái vận hành màng.
- Phát hiện sớm hiện tượng nén bánh cặn qua tiến hóa SHAP theo thời gian:
  - Khi màng bước vào chu kỳ lọc, giá trị SHAP của điểm đặt thông lượng và $\text{MLSS}$ tăng dần đơn điệu, phản ánh sự tích tụ liên tục của trở lực bánh cặn ($R_c$).
  - Giá trị SHAP âm của cường độ sục khí ban đầu lớn nhưng sau đó suy giảm dần hoặc đi vào vùng bão hòa.
  - Cơ chế vật lý: Lớp bùn chuyển đổi từ dạng cặn xốp dễ bóc tách bằng lực cắt khí sang lớp gel nén chặt (compacted gel layer) bám dính cao.
  - Ứng dụng chẩn đoán: Theo dõi đường cong SHAP động cung cấp chỉ báo sớm về điểm chuyển tiếp nghẹt màng nguy kịch, giúp rửa màng chủ động trước khi TMP chạm ngưỡng làm sạch [17, 53].

---

### 4.3 LIME, Đồ thị phụ thuộc một phần (PDP) và Các phương pháp dựa trên Gradient

#### 4.3.1 Mô hình giải thích cục bộ thay thế LIME
- Cơ chế hoạt động của LIME (Local Interpretable Model-agnostic Explanations):
  - LIME [27] tạo một mô hình thay thế cục bộ (local surrogate model) có cấu trúc tuyến tính đơn giản xung quanh điểm dự báo cụ thể $x$.
  - Phương pháp tạo ra các mẫu nhiễu (perturbations) trong vùng lân cận, gán trọng số theo khoảng cách tới $x$ và tối ưu hóa hàm mục tiêu:
    $$\xi(x) = \arg\min_{g \in G} \mathcal{L}(f, g, \pi_x) + \Omega(g)$$
  - Trong đó:
    - $f$: Mô hình hộp đen ban đầu cần giải thích.
    - $g \in G$: Mô hình giải thích cục bộ đơn giản (hồi quy tuyến tính hoặc cây quyết định nông).
    - $\pi_x(z)$: Hàm trọng số khoảng cách lân cận giữa mẫu nhiễu $z$ và điểm mẫu $x$.
    - $\mathcal{L}(f, g, \pi_x)$: Độ sai lệch cục bộ giữa dự báo của $f$ và mô hình giải thích $g$.
    - $\Omega(g)$: Tham số ràng buộc độ phức tạp của mô hình giải thích $g$.
- Ưu điểm và nhược điểm kỹ thuật của LIME:
  - Ưu điểm: Tốc độ tính toán nhanh trong phạm vi mili-giây, độc lập hoàn toàn với cấu trúc mô hình gốc.
  - Nhược điểm: Tính bất ổn định cao do phụ thuộc vào thuật toán lấy mẫu ngẫu nhiên. Hai lần chạy cùng một mẫu có thể cho ra hệ số khác nhau. Phương pháp nhạy cảm với việc chọn bán kính vùng lân cận (kernel width) [27, 55].
  - Khoảng trống nghiên cứu: Chưa có nhiều công trình so sánh định lượng có hệ thống giữa LIME và SHAP trong bối cảnh kiểm soát tắc nghẽn MBR.

#### 4.3.2 Đồ thị phụ thuộc một phần (PDP) và Đường cong kỳ vọng điều kiện cá thể (ICE)
- Khái niệm và công thức tính PDP:
  - PDP [48] trực quan hóa tác động biên trung bình của một hoặc hai biến mục tiêu $x_S$ lên đầu ra dự báo của mô hình:
    $$\hat{f}_S(x_S) = \frac{1}{n} \sum_{i=1}^n f(x_S, x_C^{(i)})$$
  - Trong đó $x_C$ là tập hợp tất cả các đặc trưng còn lại trong tập dữ liệu $n$ mẫu quan trắc.
- Phân tích đường cong ICE (Individual Conditional Expectation):
  - ICE bóc tách chi tiết tác động biên cho từng cá thể mẫu riêng biệt, tránh hiện tượng triệt tiêu dị biệt do lấy trung bình của PDP.
- Phát hiện ngưỡng chuyển tiếp phi Newton của bùn hoạt tính:
  - Đường cong PDP cho thấy khi $\text{MLSS} < 10\text{--}12\text{ g/L}$, tốc độ gia tăng TMP duy trì ở mức thấp và ổn định (đặc trưng của huyền phù loãng).
  - Khi $\text{MLSS} \ge 10\text{--}12\text{ g/L}$, đường cong PDP dốc đứng đột ngột, phản ánh quá trình bùn chuyển pha sang chất lỏng phi Newton có độ nhớt cao.
  - Đường cong ICE chỉ ra ngưỡng chuyển tiếp này bị dịch chuyển bởi nhiệt độ nước thải ($T$) và tuổi bùn (SRT), giải thích tại sao các điểm đặt cố định truyền thống thường thất bại theo mùa [48].

#### 4.3.3 Các phương pháp phân bổ thuộc tính dựa trên Gradient cho mô hình chuỗi thời gian sâu
- Cơ chế đạo hàm đồ thị tính toán:
  - Các phương pháp phân bổ dựa trên gradient (Vanilla Gradients, Integrated Gradients, Guided Backpropagation, Grad-CAM) đo lường độ nhạy của đầu ra thông qua vi phân giải tích của đồ thị tính toán nơ-ron [28, 54].
  - Áp dụng trên các kiến trúc mạng học sâu chuỗi thời gian như LSTM hoặc mạng tích hợp Convolutional-LSTM trong xử lý nước.
- Kỹ thuật Grad-CAM cho mạng nơ-ron tích chập (CNN):
  - Grad-CAM (Gradient-weighted Class Activation Mapping) sử dụng gradient của điểm số dự báo chảy vào lớp tích chập cuối cùng để tạo bản đồ nhiệt trực quan.
  - Trong chẩn đoán MBR, Grad-CAM định vị các vùng không gian hoặc các dải phổ tín hiệu cảm biến rung động, áp suất mang dấu hiệu tắc nghẽn cục bộ.
- Công thức Integrated Gradients (IG):
  - Tính tích phân gradient dọc theo đường nối từ điểm tham chiếu đường cơ sở $x'$ đến đầu vào $x$:
    $$\text{IG}_i(x) = (x_i - x'_i) \times \int_{0}^{1} \frac{\partial f(x' + \alpha (x - x'))}{\partial x_i} d\alpha$$
- Khám phá cửa sổ thời gian quyết định tắc nghẽn MBR:
  - Bản đồ phân bổ gradient trên mô hình LSTM xác định các bước thời gian mang thông tin quyết định cao nhất đối với giá trị TMP hiện tại.
  - Cửa sổ thời gian then chốt nằm trong khoảng $2\text{--}8\text{ giờ}$ ngay trước thời điểm xuất hiện bước nhảy TMP.
  - Cơ chế vật lý: Đây là thang thời gian đặc trưng của quá trình tích tụ các chất ngoại bào (EPS/SMP), tạo mầm bánh cặn và nén chặt cấu trúc màng, cung cấp cơ sở định lịch rửa ngược và sục khí [28].

#### 4.3.4 Bảng 2: So sánh toàn diện các phương pháp XAI trong hệ thống MBR
(Tổng hợp đối chiếu từ Table 3 trong tài liệu gốc và các bằng chứng thực nghiệm vận hành MBR)

| Phương pháp XAI | Phạm vi giải thích | Loại mô hình tương thích | Độ phức tạp tính toán | Bằng chứng thực nghiệm trong MBR / Xử lý nước | Ưu điểm cốt lõi | Nhược điểm và Hạn chế |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SHAP** (Shapley Additive exPlanations) | Cục bộ + Toàn cục (Local & Global) | Độc lập mô hình (Model-agnostic). Tối ưu hóa trên mô hình Cây (Tree-based) | Trung bình - Cao (KernelSHAP: $\mathcal{O}(2^{|F|})$. TreeSHAP: $\mathcal{O}(T \cdot L \cdot D^2)$) | Liang et al. ($R^2 = 0.8374$), Viet & Jang ($R^2 = 0.92\text{--}0.98$), Newhart et al. [17, 22, 49, 53] | Nền tảng lý thuyết trò chơi toán học vững chắc. Thỏa mãn 4 tiên đề. Tính cộng cục bộ chính xác. Phát hiện động học nén bánh cặn. | Tốn kém tài nguyên tính toán đối với dữ liệu lớn nếu không dùng mô hình dạng cây. Đòi hỏi giả định độc lập biến nền. |
| **LIME** (Local Interpretable Model-agnostic Explanations) | Cục bộ (Local) | Độc lập mô hình (Model-agnostic) | Thấp - Trung bình (Vài mili-giây trên mẫu đơn lẻ) | Phát hiện bất thường cảm biến SCADA, phân loại suy thoái chất lượng nước [27, 55] | Tốc độ trích xuất cực nhanh. Phù hợp bảng điều khiển vận hành thời gian thực. Trực quan qua hệ số tuyến tính. | Kết quả bất ổn định do lấy mẫu ngẫu nhiên nhiễu. Nhạy cảm cao với bán kính vùng lân cận. Không cung cấp bức tranh toàn cục. |
| **PDP / ICE** (Partial Dependence / Individual Conditional Expectation) | Toàn cục (PDP) + Bóc tách cá thể (ICE) | Độc lập mô hình (Model-agnostic) | Thấp ($\mathcal{O}(n \cdot K)$ với $K$ điểm lưới khảo sát) | Nhận diện ngưỡng chuyển tiếp nồng độ bùn $\text{MLSS} = 10\text{--}12\text{ g/L}$, phân tích đường cong vận hành [48] | Trực quan hóa trực tiếp mối quan hệ phi tuyến. Nhận diện các điểm uốn vật lý. ICE chỉ ra sự biến thiên theo nhiệt độ và SRT. | Giả định tính độc lập giữa các biến khảo sát và các biến còn lại. Bỏ qua tương tác phức tạp đa biến trên không gian cao chiều. |
| **Integrated Gradients** (và Grad-CAM / Gradient) | Cục bộ theo chuỗi thời gian và không gian (Temporal / Spatial Local) | Mạng nơ-ron khả vi (Deep Neural Networks, LSTM, CNN-LSTM) | Thấp (Tính đạo hàm giải tích trên đồ thị tính toán) | Dự báo TMP bằng LSTM, xác định cửa sổ trễ quyết định $2\text{--}8\text{ giờ}$ trước khi tắc nghẽn [28, 54] | Nắm bắt chính xác động học trễ chuỗi thời gian. Giải tích trực tiếp trên đồ thị mạng. Tính toán nhanh trên GPU. | Chỉ áp dụng cho các cấu trúc mạng nơ-ron khả vi. Nhạy cảm với việc định nghĩa điểm cơ sở tham chiếu (baseline). |
| **ANCHORS** | Cục bộ dạng luật (Rule-based Local) | Độc lập mô hình (Model-agnostic) | Cao (Tìm kiếm tổ hợp không gian trạng thái) | Trích xuất luật if-then trong nghiên cứu lý thuyết vận hành MBR [27] | Cung cấp các điều kiện biên rõ ràng, dễ hiểu cho người vận hành không chuyên tin học. Độ bao phủ và độ chính xác cao. | Chi phí tính toán tìm kiếm luật cao. Khó biểu diễn cho các biến số liên tục có biến thiên phức tạp trong xử lý nước. |
