#### 2.3.4. Proposed ANN-RSM hyperparameter optimization method

- Phương pháp tối ưu hóa siêu tham số cho mạng nơ-ron nhân tạo dựa trên phương pháp bề mặt đáp ứng đề xuất (ANN-RSM HPO - proposed RSM-based ANN hyperparameter optimization method) bao gồm hai giai đoạn chính: phương pháp sàng lọc (screening method) và phương pháp tối ưu hóa bề mặt đáp ứng (RSM optimization method).

- **2.3.4.1. Phương pháp sàng lọc (Screening method):**
  - Quy trình sàng lọc ban đầu sử dụng mô hình thiết kế nhân tố toàn phần $2$ mức (two-level full factorial design model) với một số tập cấu hình siêu tham số:
    - Sơ đồ các bước sàng lọc sử dụng phương pháp nhân tố toàn phần $2$ mức được minh họa tại Hình S3 (Figure S3 trong tài liệu bổ sung Supplementary Material).
    - Tiếp cận này hỗ trợ xác định các phạm vi hoặc thang đo phù hợp (appropriate ranges or scales) cho quá trình tối ưu hóa RSM tiếp theo.
  - Mô hình bậc một (first-order model) sử dụng hàm đa thức (polynomial function) thường là đủ để xấp xỉ quá trình và được giả định có hành vi tương tự như mạng nơ-ron trong một vùng hoặc phạm vi nhỏ của bề mặt đáp ứng (response surface).
  - Phương trình mô hình bậc một được biểu diễn theo Phương trình ($8$):
    $$Y = b_0 + b_1 x_1 + b_2 x_2 + \dots + b_i x_i + \varepsilon \tag{8}$$
    trong đó:
    - $Y$ đại diện cho đáp ứng dự đoán (predicted response) hoặc biến phụ thuộc (dependent variable).
    - $x_i$ là các biến độc lập (independent variables).
    - $b_i$ là các hằng số (constants).
    - $\varepsilon$ (được ký hiệu là $1$ trong bản in) là số hạng sai số (error term).
  - Xác định miền bề mặt đáp ứng bằng nhiều thang đo siêu tham số:
    - Đánh giá $3$ thang đo siêu tham số khác nhau đối với mô hình FFNN và $2$ thang đo khác nhau đối với mô hình RBFNN (chi tiết tại Bảng S2 trong tài liệu bổ sung).
    - Thang đo siêu tham số thể hiện hiệu năng tốt nhất được lựa chọn cho quy trình tối ưu hóa RSM tiếp theo.
    - Kết quả sàng lọc các siêu tham số của FFNN và RBFNN ($2\text{LF-FFNN}$ và $2\text{LF-RBFNN}$) được trình bày trong Bảng S2.
  - Phân tích phương sai (ANOVA - Analysis of Variance) ở mức ý nghĩa $5\%$ ($\alpha = 0.05$) được sử dụng để xác định thiết kế thực nghiệm, diễn giải và phân tích dữ liệu huấn luyện:
    - Các chỉ số đánh giá của ANOVA bao gồm hệ số xác định ($R^2$), $R^2$ hiệu chỉnh ($R^2_{\mathrm{adj}}$), và $R^2$ dự đoán ($R^2_{\mathrm{pred}}$) nhằm đánh giá mức độ ý nghĩa của mô hình.
    - Biến đổi đáp ứng dự đoán nhằm đưa phân phối của biến đáp ứng về gần phân phối chuẩn (normal distribution).
    - Đồ thị Box-Cox (Box-Cox plot) được áp dụng để cải thiện độ khớp của mô hình với nhiều phép biến đổi khác nhau (Nazghelichi et al. $2011$):
      - $\lambda = -1$: hàm nghịch đảo (inverse).
      - $\lambda = -0.5$: hàm nghịch đảo căn bậc hai (inverse square root).
      - $\lambda = 0$: hàm logarit tự nhiên (natural log).
      - $\lambda = 0.5$: hàm căn bậc hai (square root).
      - $\lambda = 1$: hàm không biến đổi (no transformation).
  - Biểu đồ Pareto (Pareto chart) được áp dụng để minh họa thứ tự ý nghĩa thống kê của các yếu tố ảnh hưởng chính (main effects) và yếu tố tương tác (interaction effects), đồng thời so sánh giá trị tương đối của chúng:
    - Các yếu tố vượt qua đường tham chiếu (reference line) được xem là có ý nghĩa thống kê ở mức độ tin cậy $95\%$ ($t$-value).
    - Hình S4(a) chỉ ra rằng yếu tố chính là siêu tham số hàm huấn luyện ($E$) đóng góp ảnh hưởng lớn nhất đến giá trị sai số bình phương trung bình ($MSE$) của thuật toán $2\text{LF-FFNN-1}$, tiếp theo là động lượng ($C$), số lượng nơ-ron ($A$), và tốc độ học ($B$).
    - Các yếu tố tương tác ảnh hưởng đáng kể đến hiệu năng $MSE$ bao gồm: $AD$, $AE$, $AF$, $BC$, $BE$, $CD$, $CE$, $CF$, $DE$, $DF$, $EF$, $ACE$, $ADE$, $ADF$, $BCE$, và $ACDE$.
    - Hình S4(b) cho thấy số lượng nơ-ron có tác động đáng kể nhất đến hiệu năng $MSE$ của thuật toán $2\text{LF-RBFNN-2}$.
  - Kết quả ANOVA đối với việc lựa chọn thang đo siêu tham số:
    - Thiết lập dải giá trị của $2\text{LF-FFNN-1}$ đạt hiệu năng tốt nhất với $R^2 = 0.9534$, $R^2_{\mathrm{adj}} = 0.9247$, và $R^2_{\mathrm{pred}} = 0.8744$ khi sử dụng phép biến đổi nghịch đảo căn bậc hai để phát triển mô hình nhân tố bậc cao nhất.
    - Đối với các siêu tham số sàng lọc của $2\text{LF-RBFNN}$, phép biến đổi logarit tự nhiên được sử dụng để phát triển mô hình nhân tố $2$ mức cao nhất.
    - Kết quả ANOVA chứng minh $2\text{LF-RBFNN-2}$ tạo ra hiệu năng mô hình xuất sắc với $R^2 = 0.9898$, $R^2_{\mathrm{adj}} = 0.9847$, và $R^2_{\mathrm{pred}} = 0.9593$.
    - Thang đo và cấu hình siêu tham số của $2\text{LF-FFNN-1}$ và $2\text{LF-RBFNN-2}$ lần lượt được lựa chọn cho FFNN và RBFNN để thực hiện phương pháp tối ưu hóa bậc cao hơn bằng kỹ thuật RSM.

- **2.3.4.2. Phương pháp tối ưu hóa siêu tham số bằng RSM (RSM hyperparameters optimization method):**
  - Phương pháp bề mặt đáp ứng (RSM - Response Surface Methodology) là một quy trình tuần tự được sử dụng để khớp mô hình bậc hai (second-order model), hoạt động hiệu quả trong việc mô hình hóa độ cong xung quanh các vùng tiềm năng.
  - **i. Nhập dữ liệu (Data Insertion):**
    - Các bước tổng thể của việc nhập dữ liệu tương tự như Hình S2 (trong tài liệu bổ sung).
    - Đối với mô hình FFNN, $6$ siêu tham số được xem xét:
      - $4$ biến số dạng số (numerical variables): số lượng nơ-ron (number of neurons), tốc độ học (learning rate), động lượng (momentum), và số lượng epoch (number of epochs).
      - $2$ yếu tố phân loại (categorical components): hàm huấn luyện (training function) và hàm kích hoạt (activation function).
    - Đối với mô hình RBFNN, $2$ biến số dạng số được xem xét: số lượng nơ-ron (number of neurons) và độ trải rộng (spreads).
    - Mức thấp nhất và cao nhất của các biến được mã hóa tương ứng là $-1$ và $+1$, bao gồm các điểm trục hình sao (axial star points) tại $-\alpha$ và $+\alpha$:
      - $\alpha$ là khoảng cách của các điểm trục tính từ tâm giúp thiết kế có tính chất quay tròn (rotatable).
      - Giá trị $\alpha$ được thiết lập bằng $1$ (thiết kế tâm mặt - face centred).
    - Tổng số tổ hợp thực nghiệm được tính toán dựa trên khái niệm thiết kế tâm xoay hỗn hợp (CCD - Central Composite Design) theo Phương trình ($9$):
      $$N_{\mathrm{runs}} = 2^k + 2k + n_0 \tag{9}$$
      trong đó:
      - $k$ là số lượng yếu tố (chỉ tính yếu tố dạng số - numerical factors).
      - $n_0$ là số lượng thí nghiệm (tinh chỉnh) lặp lại tại điểm tâm (centre point).
      - $2^k$ là số điểm nhân tố (factorial points).
      - $2k$ là số điểm trục (axial points).
    - Thiết lập số lượng thí nghiệm cụ thể cho hai mạng:
      - Đối với FFNN: với $4$ yếu tố dạng số ($k = 4$) và $n_0 = 6$. Do nghiên cứu bao gồm $2$ yếu tố phân loại với $2$ mức—hàm huấn luyện (`trainlm` và `traingdm`) và hàm kích hoạt (`tansig` và `ReLu`)—số lượng thí nghiệm lặp lại tại điểm nhân tố, điểm trục và điểm tâm được nhân đôi cho từng yếu tố phân loại ($2^4_{\mathrm{trainlm}} = 16$, $2^4_{\mathrm{traingdm}} = 16$; $2^4_{\mathrm{tansig}} = 16$, $2^4_{\mathrm{ReLu}} = 16$; $2k_{\mathrm{trainlm}} = 8$, $2k_{\mathrm{traingdm}} = 8$; $2k_{\mathrm{tansig}} = 8$, $2k_{\mathrm{ReLu}} = 8$; $n_{0,\mathrm{trainlm}} = 6$, $n_{0,\mathrm{traingdm}} = 6$; $n_{0,\mathrm{tansig}} = 6$, $n_{0,\mathrm{ReLu}} = 6$).
      - Đối với RBFNN: với $2$ yếu tố dạng số (số lượng nơ-ron và độ rộng spread), $k = 2$ và $n_0 = 5$. Số lượng thí nghiệm lặp lại tại điểm nhân tố, điểm trục và điểm tâm lần lượt là $4$, $4$, và $5$.
      - Tổng số lượt chạy (runs) cần thiết cho FFNN và RBFNN lần lượt là $120$ và $13$.
    - Ma trận gồm $120$ thí nghiệm cho FFNN và $13$ thí nghiệm cho RBFNN được tạo ra bằng gói phần mềm Design-Expert phiên bản 12.0.
    - Bảng S3 và Bảng S4 trình bày ma trận thiết kế hoàn chỉnh của các thí nghiệm được thực hiện và kết quả $MSE$ thu được tương ứng cho FFNN và RBFNN.
    - Các điểm tâm được sử dụng để xác định sai số thực nghiệm (experimental error) và độ lặp lại (reproducibility) của dữ liệu.
  - **ii. Biến đổi dữ liệu (Data Transformation):**
    - Đáp ứng dự đoán được biến đổi nhằm đưa phân phối của biến đáp ứng về gần phân phối chuẩn.
    - Đồ thị Box-Cox được áp dụng để cải thiện độ khớp của mô hình với các phép biến đổi ($\lambda = -1$, $\lambda = -0.5$, $\lambda = 0$, $\lambda = 0.5$, và $\lambda = 1$), đại diện tương ứng cho các hàm nghịch đảo, nghịch đảo căn bậc hai, logarit tự nhiên, căn bậc hai, và không biến đổi (Nazghelichi et al. $2011$).
  - **iii. Lựa chọn mô hình (Model Selection):**
    - Mô hình bậc hai (quadratic models) được thiết lập bằng phương pháp bình phương tối thiểu (least squares method) nhằm mô tả hành vi động của quá trình mạng nơ-ron.
    - Đối với $k$ yếu tố, mô hình bậc hai được sử dụng theo Phương trình ($10$) (Ogunjiofor & Ayodele $2023$):
      $$Y = b_0 + \sum_{i=1}^{k} b_i x_i + \sum_{i=1}^{k} b_{ii} x_i^2 + \sum_{i=1}^{k-1} \sum_{j=i+1}^{k} b_{ij} x_i x_j + \varepsilon \tag{10}$$
      trong đó:
      - $Y$ là đáp ứng dự đoán (predicted response).
      - $x_i$ và $x_j$ là các biến yếu tố (factors).
      - $b_i$ và $b_j$ là các hằng số.
      - $\varepsilon$ (được ký hiệu là $1$ trong bản in) là số hạng sai số (error term).
      - $b_0$ là số hạng chặn (intercept term).
      - $b_i$ là số hạng tuyến tính (linear term).
      - $b_{ii}$ và $b_{jj}$ là các số hạng bình phương (squared terms).
      - $b_{ij}$ là số hạng tương tác (interaction term) giữa các biến.
  - **iv. Phân tích ANOVA, đồ thị chẩn đoán và đồ thị mô hình (ANOVA, Diagnostic Plot, and Model Graph):**
    - Độ chính xác của mô hình RSM được xác định bằng phân tích ANOVA và đồ thị chẩn đoán (diagnostic plot).
    - Các tiêu chí đánh giá của ANOVA bao gồm hệ số xác định ($R^2$), $R^2$ hiệu chỉnh ($R^2_{\mathrm{adj}}$), $R^2$ dự đoán ($R^2_{\mathrm{pred}}$), độ chính xác thỏa đáng (adequate precision), giá trị $F$ ($F$-value), và giá trị $p$ ($p$-value) dùng để đánh giá mức độ ý nghĩa của mô hình.
    - Hệ số kiểm định thống kê $F$-value được sử dụng để đánh giá mức độ ý nghĩa của mô hình ở mức độ tin cậy $95\%$ (Nourbakhsh et al. $2014$).
    - Giá trị $p$-value đóng vai trò là công cụ bảo đảm tầm quan trọng của từng hệ số ở mức ý nghĩa xác định:
      - Giá trị $p < 0.050$ thể hiện mức ý nghĩa cao nhất và đóng góp lớn vào biến đáp ứng.
      - Giá trị $p$-value càng nhỏ thì hệ số tương ứng càng có ý nghĩa thống kê cao.
      - Các giá trị $p > 0.050$ có ý nghĩa thống kê thấp hơn.
    - Phân tích phần dư (residuals analysis) được thực hiện để chẩn đoán tính thỏa đáng và độ tin cậy của mô hình.
    - Đồ thị bề mặt đáp ứng và các yếu tố tương tác thu được từ đồ thị mô hình (model graph) của phần mềm Design-Expert phiên bản 12.0.
  - **v. Thiết lập mục tiêu và giá trị tối ưu (Set the Goal and Optimum Value):**
    - Trong giai đoạn tối ưu hóa bằng số (numerical optimization phase), có $5$ khả năng thiết lập mục tiêu để xây dựng chỉ số mức độ mong muốn (desirability indices) bao gồm: 'tối đa hóa' ('maximize'), 'tối thiểu hóa' ('minimize'), 'mục tiêu' ('target'), 'trong khoảng' ('in range'), và 'bằng' ('equal to').
    - Thang đo mức độ mong muốn dao động từ $0$ đến $1$ cho bất kỳ đáp ứng nào:
      - Giá trị bằng $1$ đại diện cho trường hợp lý tưởng.
      - Giá trị bằng $0$ biểu thị một hoặc nhiều đáp ứng nằm ngoài giới hạn mong muốn.
    - Phương pháp RSM đề xuất một vài tập hợp giải pháp cấu hình siêu tham số, xếp theo thứ tự từ kết quả mong muốn nhất đến kết quả kém mong muốn nhất.
  - Phương pháp luận chi tiết về việc phát triển quy trình ANN-RSM đề xuất được minh họa trong Hình 3:
    * **Hình 3.** Quy trình tổng thể của phương pháp tinh chỉnh siêu tham số ANN-RSM đề xuất
      * <img src="assets/fig_03_p10.jpeg" alt="Hình 3" />
      * **Hình này chứng minh điều gì**
        * Quy trình đề xuất chuẩn hóa việc tối ưu siêu tham số ANN qua 3 giai đoạn khép kín: chuẩn bị dữ liệu, tối ưu hóa bằng RSM với DOE (sàng lọc 2 mức và CCD), và thẩm định độc lập có cơ chế phản hồi lặp theo độ thỏa dụng (desirability).
      * **Từ đâu mà thấy được**
        * Khối màu xanh lá (Data collection and preprocessing): Dữ liệu sau tiền xử lý được chia ngẫu nhiên thành 60% huấn luyện (Ttraining) cấp cho RSM và 40% kiểm định (Ttesting) đưa tới bước đánh giá.
        * Khối màu cam (Proposed ANN-RSM Hyperparameter optimization): Tiến hành sàng lọc 2 mức (2-level factorial), bổ sung điểm thực nghiệm CCD, kiểm định ANOVA/chẩn đoán (có vòng lặp cải thiện) và đề xuất nghiệm tối ưu theo hàm desirability.
        * Khối màu xanh dương (Model validation): Mạng được huấn luyện lại và kiểm tra; nhánh "No" tại "Test model good?" tạo vòng lặp quay lại nhận giải pháp tiếp theo từ RSM cho đến khi chọn được mô hình tối ưu nhất.
