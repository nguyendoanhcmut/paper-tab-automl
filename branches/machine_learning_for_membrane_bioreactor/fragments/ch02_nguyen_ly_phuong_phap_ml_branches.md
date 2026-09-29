## 2. Nguyên lý và Phương pháp Học máy trong MBR

### 2.1 Quy trình Xây dựng Mô hình Học máy Tổng quát

#### 2.1.1 Khung Quy trình Chuẩn hóa trong Nghiên cứu MBR
- **Định nghĩa học máy trong kỹ thuật môi trường**: Học máy xây dựng mô hình toán học từ dữ liệu thực nghiệm ("training data"). Mô hình đưa ra dự báo hoặc quyết định vận hành mà không cần giả định cơ chế tiên nghiệm hoặc lập trình quy tắc cố định.
- **Chuỗi quy trình chuẩn hóa gồm 7 bước liên tục**:
  1. **Thu thập dữ liệu (Data acquisition)**: Thu nhận dữ liệu cảm biến đo trực tuyến (áp suất xuyên màng TMP, lưu lượng thấm, nhiệt độ, oxy hòa tan DO, pH) và dữ liệu xét nghiệm phòng thí nghiệm (nồng độ bùn hoạt tính MLSS, nhu cầu oxy hóa học COD, tổng nitơ TN, tổng phospho TP, chất cao phân tử ngoại bào EPS, sản phẩm vi sinh hòa tan SMP).
  2. **Tiền xử lý dữ liệu (Data preprocessing)**: Làm sạch dữ liệu thô. Xử lý giá trị khuyết (missing values) bằng nội suy tuyến tính hoặc thuật toán KNN. Phát hiện và loại bỏ giá trị dị biệt (outliers) bằng phương pháp lọc thống kê ($3\sigma$ hoặc IQR). Chuẩn hóa thang đo đặc trưng về dải $[0, 1]$ bằng Min-Max Scaling hoặc đưa về phân phối chuẩn hóa bằng Z-score Scaling:
     $$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}, \quad z = \frac{x - \mu}{\sigma}$$
  3. **Phân chia tập dữ liệu (Dataset splitting)**: Chia tập dữ liệu thành ba phần độc lập gồm tập huấn luyện (Training set, 70%), tập kiểm định (Validation set, 15%) và tập kiểm tra (Testing set, 15%). Quy trình này ngăn chặn hiện tượng rò rỉ dữ liệu (data leakage).
  4. **Lựa chọn và huấn luyện mô hình (Model selection & training)**: Lựa chọn cấu trúc thuật toán phù hợp với kiểu bài toán (hồi quy thông lượng, phân loại tắc nghẽn màng, dự báo chuỗi thời gian). Mô hình học các trọng số tham số nội tại từ tập huấn luyện.
  5. **Tối ưu hóa siêu tham số (Hyperparameter optimization)**: Tinh chỉnh các tham số cấu trúc mô hình bằng kỹ thuật tìm kiếm lưới (Grid Search), tìm kiếm ngẫu nhiên (Random Search), kiểm định chéo $k$-fold ($k$-fold Cross-Validation), hoặc kết hợp các thuật toán tối ưu hóa thông minh (GA, PSO, GWO).
  6. **Đánh giá hiệu năng mô hình (Model evaluation)**: Đo lường độ chính xác và sai số trên tập kiểm tra độc lập bằng các chỉ số thống kê định lượng ($R^2$, RMSE, MAE, MAPE).
  7. **Triển khai và giám sát thực tế (Model deployment & monitoring)**: Tích hợp mô hình vào hệ thống điều khiển giám sát tự động SCADA của nhà máy MBR. Mô hình cảnh báo sớm tốc độ tắc nghẽn màng và tự động điều chỉnh chu kỳ rửa ngược hoặc lưu lượng sục khí.

#### 2.1.2 Phân loại Các Phương thức Học máy trong MBR
- **Học có giám sát (Supervised Learning)**:
  - **Bản chất**: Tập dữ liệu huấn luyện chứa cặp biến đầu vào và nhãn đích tương ứng: $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$.
  - **Bài toán hồi quy (Regression)**: Đầu ra $y$ là biến liên tục. Ứng dụng dự báo áp suất xuyên màng TMP, thông lượng lọc $J$, tốc độ tăng trở lực màng $dR/dt$, nồng độ COD và amoni trong nước sau xử lý.
  - **Bài toán phân loại (Classification)**: Đầu ra $y$ là nhãn rời rạc. Ứng dụng nhận diện các giai đoạn nghẹt màng (nghẹt thuận nghịch, nghẹt không thuận nghịch), phân loại chất bám bẩn (hữu cơ, vô cơ, sinh học), chẩn đoán lỗi thiết bị cảm biến.
- **Học không giám sát (Unsupervised Learning)**:
  - **Bản chất**: Tập dữ liệu chỉ chứa các biến đặc trưng đầu vào không có nhãn đích: $\mathcal{D} = \{x_i\}_{i=1}^N$.
  - **Phân cụm dữ liệu (Clustering)**: Gom nhóm các mẫu nước thải hoặc đặc tính bùn có tính chất tương đồng bằng thuật toán $k$-Means hoặc Phân cụm phân cấp (Hierarchical Clustering).
  - **Giảm số chiều (Dimensionality reduction)**: Nén dữ liệu nhiều chiều từ phổ huỳnh quang 3D-EEM hoặc ảnh hiển vi mà vẫn giữ lại phần lớn phương sai thông qua phân tích thành phần chính (PCA) hoặc t-SNE.
  - **Phát hiện dị biệt (Anomaly detection)**: Nhận diện các điểm vận hành bất thường hoặc hỏng hóc cảm biến dựa trên mật độ phân bố dữ liệu.
- **Học tăng cường (Reinforcement Learning - RL)**:
  - **Bản chất**: Tác tử học máy (Agent) tự động tương tác với môi trường bể phản ứng sinh học màng (Environment) theo cơ chế thử và sai thông qua Quá trình Quyết định Markov (Markov Decision Process - MDP).
  - **Cơ chế hoạt động**: Tại mỗi bước thời gian $t$, tác tử quan sát trạng thái hệ thống $s_t \in \mathcal{S}$ (TMP, DO, mực bùn), thực hiện hành động điều khiển $a_t \in \mathcal{A}$ (tốc độ bơm hút, cường độ sục khí bọt khí), và nhận tín hiệu phần thưởng $r_t \in \mathbb{R}$ (tiết kiệm năng lượng điện, kéo dài chu kỳ lọc).
  - **Mục tiêu**: Tối đa hóa tổng phần thưởng tích lũy có chiết khấu theo thời gian:
    $$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}, \quad \gamma \in [0, 1)$$

---

### 2.2 Các Thuật toán Học máy Cốt lõi

#### 2.2.1 Máy Vector Hỗ trợ (Support Vector Machine - SVM / SVR)
- **Nền tảng lý thuyết học thống kê**:
  - Do Vapnik phát triển dựa trên Nguyên lý Cực tiểu hóa Rủi ro Cấu trúc (Structural Risk Minimization - SRM).
  - Khác với mạng nơ-ron truyền thống áp dụng Nguyên lý Cực tiểu hóa Rủi ro Thực nghiệm (Empirical Risk Minimization - ERM), SRM tối ưu hóa đồng thời sai số huấn luyện và độ phức tạp mô hình. SRM kiểm soát cận trên của sai số khái quát hóa, giúp ngăn chặn hiện tượng quá khớp (overfitting).
- **Nguyên lý siêu phẳng phân tách và biên cực đại**:
  - Dữ liệu đầu vào được ánh xạ phi tuyến từ không gian gốc sang không gian đặc trưng Hilbert nhiều chiều qua hàm $\Phi(x)$.
  - Phương trình siêu phẳng hồi quy tuyến tính trong không gian đặc trưng:
    $$f(x) = \langle w, \Phi(x) \rangle + b$$
  - Khoảng cách hình học của dải biên bằng $\frac{2}{||w||}$. Việc cực đại hóa biên tương đương với bài toán cực tiểu hóa chuẩn Euclid $\frac{1}{2} ||w||^2$.
- **Hàm mất mát không nhạy cảm $\epsilon$ ($\epsilon$-insensitive loss function)**:
  - Mô hình chấp nhận sai số dự báo nằm trong dải ống độ rộng $\pm\epsilon$ xung quanh siêu phẳng:
    $$L_\epsilon(y, f(x)) = |y - f(x)|_\epsilon = \max(0, |y - f(x)| - \epsilon) = \begin{cases} 0, & \text{nếu } |y - f(x)| \le \epsilon \\ |y - f(x)| - \epsilon, & \text{ngược lại} \end{cases}$$
  - Các điểm dữ liệu nằm trong dải ống $\epsilon$ không tạo ra chi phí phạt sai số.
  - Các điểm dữ liệu nằm ngoài dải ống $\epsilon$ vi phạm biên và được đo lường bằng hai biến bù sai số $\xi_i, \xi_i^* \ge 0$.
- **Bài toán tối ưu hóa lồi SVR**:
  - Công thức bài toán gốc (Primal optimization problem):
    $$\min_{w, b, \xi, \xi^*} \frac{1}{2} ||w||^2 + C \sum_{i=1}^l (\xi_i + \xi_i^*)$$
    thỏa mãn các điều kiện ràng buộc:
    $$\begin{cases} y_i - \langle w, \Phi(x_i) \rangle - b \le \epsilon + \xi_i \\ \langle w, \Phi(x_i) \rangle + b - y_i \le \epsilon + \xi_i^* \\ \xi_i, \xi_i^* \ge 0, \quad \forall i = 1, \dots, l \end{cases}$$
  - Công thức bài toán đối ngẫu Lagrange (Dual formulation):
    $$\max_{\alpha, \alpha^*} -\frac{1}{2} \sum_{i,j=1}^l (\alpha_i - \alpha_i^*)(\alpha_j - \alpha_j^*) K(x_i, x_j) - \epsilon \sum_{i=1}^l (\alpha_i + \alpha_i^*) + \sum_{i=1}^l y_i (\alpha_i - \alpha_i^*)$$
    thỏa mãn:
    $$\sum_{i=1}^l (\alpha_i - \alpha_i^*) = 0 \quad \text{và} \quad 0 \le \alpha_i, \alpha_i^* \le C$$
  - Hàm dự báo cuối cùng chỉ phụ thuộc vào tích vô hướng giữa các điểm dữ liệu:
    $$f(x) = \sum_{i=1}^l (\alpha_i - \alpha_i^*) K(x_i, x) + b$$
  - Các điểm có $(\alpha_i - \alpha_i^*) \neq 0$ nằm tại hoặc ngoài biên dải $\epsilon$ đóng vai trò là các vector hỗ trợ (Support Vectors).
- **Hàm nhân phi tuyến (Kernel Trick)**:
  - Hàm nhân RBF (Radial Basis Function - hàm nhân Gauss):
    $$K(x, x_i) = \exp(-\gamma ||x - x_i||^2) = \exp\left(-\frac{||x - x_i||^2}{2\sigma^2}\right)$$
  - RBF ánh xạ dữ liệu đầu vào vào không gian đặc trưng vô hạn chiều. Hàm nhân này xử lý hiệu quả các quan hệ phi tuyến phức tạp trong cơ chế nghẹt màng MBR.
- **Vai trò của hai siêu tham số then chốt**:
  - **Tham số phạt $C$ ($C > 0$)**: Cân bằng giữa độ phẳng của hàm hồi quy ($||w||^2$) và mức phạt cho các điểm vượt quá giới hạn sai số $\epsilon$. Giá trị $C$ quá lớn khiến mô hình quá khớp với dữ liệu nhiễu; giá trị $C$ quá nhỏ khiến mô hình bị thiếu khớp (underfitting).
  - **Hệ số nhân $\gamma$ ($\gamma = \frac{1}{2\sigma^2}$)**: Quyết định bán kính ảnh hưởng của từng vector hỗ trợ đơn lẻ. Giá trị $\gamma$ lớn tạo ra bề mặt quyết định cục bộ và uốn lượn; giá trị $\gamma$ nhỏ tạo ra bề mặt quyết định quá phẳng, mất khả năng nắm bắt dao động thực tế.
- **Phạm vi ứng dụng và đặc điểm thực nghiệm trong MBR**:
  - Ưu thế vượt trội khi mẫu dữ liệu nhỏ ($N < 125$ mẫu thực nghiệm) như đã chứng minh bởi Qian và cộng sự (2015).
  - Ứng dụng chính: Dự báo áp suất xuyên màng TMP, dự báo tổng trở lực màng $R_t$, nhận diện rò rỉ hệ thống đường ống, cảnh báo sớm ô nhiễm nguồn nước cấp (Liu et al., 2020a).
  - Hạn chế: Rất nhạy cảm với dữ liệu khuyết; độ phức tạp tính toán xấp xỉ $\mathcal{O}(N^3)$, không phù hợp khi số lượng mẫu dữ liệu quá lớn ($N > 10^5$).

#### 2.2.2 Mạng Nơ-ron Nhân tạo (Artificial Neural Network - ANN)
- **Kiến trúc ba tầng cơ bản**:
  - **Tầng vào (Input layer)**: Tiếp nhận các biến quá trình MBR (thời gian lưu bùn SRT, thời gian lưu nước HRT, nồng độ bùn MLSS, nhiệt độ, pH, DO, thông lượng).
  - **Tầng ẩn (Hidden layers)**: Thực hiện tính toán tổ hợp tuyến tính và biến đổi phi tuyến qua hàm kích hoạt. Số lượng tầng ẩn xác định độ sâu (depth), số nơ-ron trong một tầng xác định độ rộng (width) của mạng.
  - **Tầng ra (Output layer)**: Xuất kết quả dự báo (giá trị TMP tương lai, nồng độ chất lượng nước đầu ra, sản lượng khí sinh học methane).
- **Mô hình toán học của nơ-ron nhân tạo**:
  $$z = \sum_{j=1}^n w_j x_j + b = w^T x + b, \quad a = f(z)$$
  trong đó $w_j$ là trọng số liên kết, $b$ là độ lệch (bias), $f(\cdot)$ là hàm kích hoạt phi tuyến.
- **Các hàm kích hoạt thông dụng**:
  - Hàm Sigmoid (Logistic): $\sigma(z) = \frac{1}{1 + e^{-z}}$, xuất giá trị trong khoảng $(0, 1)$, dễ gây bão hòa và triệt tiêu đạo hàm khi $|z|$ lớn.
  - Hàm Tanh (Hyperbolic Tangent): $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$, xuất giá trị trong khoảng $(-1, 1)$, đối xứng qua gốc tọa độ.
  - Hàm ReLU (Rectified Linear Unit): $\text{ReLU}(z) = \max(0, z)$, giải quyết hiện tượng triệt tiêu đạo hàm đối với miền giá trị dương, tăng tốc độ hội tụ.
- **Mạng Perceptron Đa tầng (MLP) và Mạng Lan truyền Ngược Sai số (BPNN)**:
  - Lan truyền tiến: Dữ liệu tính toán từ tầng vào qua các tầng ẩn đến tầng ra.
  - Lan truyền ngược (Backpropagation): Sai số đầu ra được lan truyền ngược về từng tầng để tính đạo hàm riêng $\frac{\partial E}{\partial w_{ij}}$ dựa trên quy tắc chuỗi (chain rule).
  - Thuật toán Giảm độ dốc (Gradient Descent):
    $$w^{(t+1)} = w^{(t)} - \eta \nabla E(w^{(t)})$$
    với $\eta$ là tốc độ học (learning rate).
  - Thuật toán Levenberg-Marquardt (LM): Kết hợp giữa phương pháp Gradient Descent và phương pháp Gauss-Newton. Thuật toán LM sử dụng ma trận xấp xỉ Hessian để cập nhật trọng số:
    $$\Delta w = (J^T J + \mu I)^{-1} J^T e$$
    trong đó $J$ là ma trận Jacobian của các đạo hàm riêng sai số, $\mu$ là tham số điều chỉnh độ dốc giảm, $I$ là ma trận đơn vị, $e$ là vector sai số huấn luyện. Thuật toán LM tăng tốc độ hội tụ nhanh hơn hàng chục lần so với Gradient Descent cổ điển trên mạng quy mô nhỏ và vừa.
- **Mạng Nơ-ron Hàm Cơ sở Xuyên tâm (RBFNN)**:
  - Cấu trúc ba tầng: Tầng vào, một tầng ẩn phi tuyến duy nhất dùng hàm cơ sở đối xứng tâm, và một tầng ra tuyến tính.
  - Hàm kích hoạt Gaussian tại nơ-ron ẩn thứ $j$:
    $$\phi_j(x) = \exp\left(-\frac{||x - c_j||^2}{2\sigma_j^2}\right)$$
    với $c_j$ là vector tâm và $\sigma_j$ là độ rộng của hàm Gaussian.
  - Tầng ra tính toán tổng tuyến tính:
    $$y = \sum_{j=1}^m w_j \phi_j(x) + b$$
  - Ưu thế: Khả năng xấp xỉ tối ưu cục bộ, không gặp vấn đề kẹt cực trị địa phương như BPNN, tốc độ huấn luyện nhanh do có thể xác định tâm bằng $k$-means và xác định trọng số tầng ra bằng giải hệ phương trình tuyến tính.
- **Mạng Nơ-ron Tích chập (Convolutional Neural Network - CNN)**:
  - Kiến trúc chuyên biệt xử lý dữ liệu lưới không gian và hình ảnh:
    1. **Lớp tích chập (Convolutional layer)**: Quét các bộ lọc (kernels) qua ma trận đầu vào để tính tích chập hai chiều:
       $$S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(i-m, j-n) K(m, n)$$
    2. **Lớp gộp (Pooling layer)**: Sử dụng Max-pooling hoặc Average-pooling để giảm kích thước không gian đặc trưng, giảm tải số lượng tham số và tăng tính bất biến với phép dịch chuyển.
    3. **Lớp kết nối đầy đủ (Fully connected layer)**: Tổng hợp các đặc trưng bậc cao thành giá trị đầu ra.
  - Các cấu trúc cải tiến tiêu biểu: GoogLeNet, DenseNet, ResNet (Wide Residual Networks), CNN hai kênh (dual-channel CNN).
  - Ứng dụng trong MBR: Trích xuất đặc trưng hình thái bề mặt màng từ ảnh hiển vi điện tử quét (SEM) hoặc kính hiển vi lực nguyên tử (AFM); nhận diện mẫu huỳnh quang từ ma trận phổ huỳnh quang kích thích - phát xạ (EEM) để định lượng thành phần protein-like và humic-like gây nghẹt màng (Ma et al., 2023).
- **Mạng Nơ-ron Hồi quy (RNN) và Mạng Bộ nhớ Ngắn-Dài hạn (LSTM)**:
  - RNN truyền thống lưu trạng thái ẩn qua bước thời gian: $h_t = \tanh(W x_t + U h_{t-1} + b)$. RNN thường gặp hiện tượng tiêu biến đạo hàm (vanishing gradient) khi chuỗi thời gian dài.
  - Mạng LSTM khắc phục triệt để bằng cấu trúc tế bào nhớ (Cell State $C_t$) kết hợp cơ chế ba cổng điều khiển:
    1. **Cổng quên (Forget gate)**: Quyết định tỷ lệ loại bỏ thông tin cũ từ trạng thái tế bào trước:
       $$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
    2. **Cổng vào (Input gate)**: Quyết định lượng thông tin mới được nạp vào tế bào nhớ:
       $$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
       $$\tilde{C}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$$
    3. **Cập nhật trạng thái tế bào (Cell state update)**: Kết hợp thông tin giữ lại và thông tin nạp mới:
       $$C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$$
    4. **Cổng ra (Output gate)**: Quyết định giá trị trạng thái ẩn xuất ra ngoài:
       $$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$
       $$h_t = o_t * \tanh(C_t)$$
  - Ứng dụng trong MBR: Dự báo chuỗi thời gian áp suất TMP động học nhiều bước thời gian tiếp theo, dự báo sự suy giảm thông lượng thấm và dự báo động học sinh khí biogas trong bể phản ứng sinh học màng kỵ khí (AnMBR).
- **Mạng Nơ-ron Wavelet (WNN)**:
  - Thay thế hàm kích hoạt truyền thống bằng hàm wavelet (như Morlet wavelet):
    $$\psi_{a, b}(x) = \frac{1}{\sqrt{|a|}} \psi\left(\frac{x - b}{a}\right)$$
  - Ưu thế: Khả năng phân tích cục bộ đồng thời cả miền thời gian và miền tần số; tốc độ hội tụ nhanh hơn MLP truyền thống và hạn chế tối đa nguy cơ rơi vào cực tiểu cục bộ.
- **Tổng kết ứng dụng ANN trong MBR**:
  - Dự báo chất lượng nước đầu ra (COD, $\text{NH}_4^+$-N) và sản lượng khí sinh học methane (Li et al., 2022).
  - Dự báo thông lượng lọc và tỷ lệ phục hồi thông lượng sau rửa màng (Zhao et al., 2020).
  - Phân loại cơ chế nghẹt màng (Shi et al., 2022).
  - Thách thức: Mô hình dạng "hộp đen" (black-box), khó diễn giải cơ chế hóa lý trực tiếp, đòi hỏi cấu hình mạng phức tạp và có nguy cơ quá khớp khi dữ liệu nhỏ.

#### 2.2.3 Cây Quyết định và Học kết hợp (Decision Tree & Ensemble Learning)
- **Cây Quyết định Phân loại và Hồi quy (CART)**:
  - Cấu trúc dạng cây phân cấp nhị phân gồm nút gốc (root node), nút nội bộ (internal nodes) và nút lá (leaf nodes). Mỗi nút nội bộ thực hiện một phép kiểm tra logic dạng if-then trên một thuộc tính đầu vào đơn lẻ.
  - **Tiêu chuẩn phân tách cho bài toán phân loại**:
    - Chỉ số bất thuần Gini (Gini Impurity):
      $$\text{Gini}(D) = 1 - \sum_{k=1}^K p_k^2$$
      với $p_k$ là tỷ lệ mẫu thuộc lớp $k$ trong tập dữ liệu $D$. Thuật toán chọn thuộc tính phân tách tối đa hóa độ giảm chỉ số Gini: $\Delta \text{Gini} = \text{Gini}(D) - \frac{|D_1|}{|D|} \text{Gini}(D_1) - \frac{|D_2|}{|D|} \text{Gini}(D_2)$.
    - Độ hỗn loạn thông tin (Entropy):
      $$H(D) = -\sum_{k=1}^K p_k \log_2(p_k)$$
  - **Tiêu chuẩn phân tách cho bài toán hồi quy**:
    - Cực tiểu hóa tổng bình phương sai số (MSE reduction):
      $$\min_{j, s} \left[ \sum_{x_i \in R_1(j, s)} (y_i - c_1)^2 + \sum_{x_i \in R_2(j, s)} (y_i - c_2)^2 \right]$$
      trong đó $j$ là biến phân tách, $s$ là điểm ngưỡng cắt, $c_1, c_2$ là trung bình giá trị đích tại hai vùng không gian con $R_1$ và $R_2$.
  - Ưu nhược điểm: Mô hình có tính minh bạch cao, dễ diễn giải trực quan cho kỹ sư vận hành. Tuy nhiên, một cây quyết định đơn lẻ rất dễ bị quá khớp (overfitting) và kém ổn định trước nhiễu nhỏ trong dữ liệu. Khắc phục bằng kỹ thuật cắt tỉa cành (pruning) và kiểm định chéo (cross-validation).
- **Rừng Ngẫu nhiên (Random Forest - RF)**:
  - Hoạt động dựa trên cơ chế kết hợp Đóng bao (Bagging - Bootstrap Aggregating).
  - Thuật toán rút mẫu ngẫu nhiên có hoàn lại (bootstrap sampling) để tạo ra $B$ tập dữ liệu huấn luyện con độc lập từ tập dữ liệu gốc.
  - Áp dụng phương pháp Không gian con Ngẫu nhiên (Random Subspace Method): Tại mỗi nút phân nhánh của mỗi cây, chỉ chọn ngẫu nhiên một tập con gồm $m$ thuộc tính (thường $m \approx \sqrt{p}$ đối với phân loại hoặc $m \approx p/3$ đối với hồi quy) trong tổng số $p$ thuộc tính đầu vào để tìm điểm cắt tối ưu.
  - Đầu ra tổng hợp:
    $$\hat{y}_{\text{RF}} = \frac{1}{B} \sum_{b=1}^B T_b(x)$$
  - Cơ chế giảm phương sai: Việc lấy mẫu ngẫu nhiên và chọn tập đặc trưng con giúp giảm đáng kể hệ số tương quan giữa các cây thành phần. Phương sai của mô hình tổ hợp giảm theo công thức:
    $$\text{Var}(\bar{X}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$
    khi số cây $B$ tăng và độ tương quan $\rho$ giảm, phương sai mô hình tiệm cận về $\rho \sigma^2$, giúp chống quá khớp vượt trội.
  - Cung cấp đánh giá tầm quan trọng của đặc trưng (Feature Importance) dựa trên độ giảm chỉ số Gini trung bình hoặc mức tăng sai số ngoài bao (Out-Of-Bag - OOB error) khi xáo trộn giá trị đặc trưng.
- **Cây Quyết định Tăng cường Độ dốc (GBDT) và XGBoost**:
  - **Cơ chế Tăng cường (Boosting)**: Xây dựng tuần tự các mô hình học yếu (base learners). Cây quyết định mới được huấn luyện để dự báo và bù đắp sai số phần dư (residuals) của toàn bộ các cây xây dựng trước đó:
    $$f_m(x) = f_{m-1}(x) + \eta h_m(x)$$
    với $h_m(x)$ là cây ước lượng phần dư và $\eta$ là tốc độ co hẹp (shrinkage / learning rate).
  - **Thuật toán XGBoost (eXtreme Gradient Boosting)**:
    - Mở rộng hàm mục tiêu bằng khai triển Taylor bậc hai quanh giá trị dự báo hiện tại $\hat{y}_i^{(t-1)}$:
      $$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$
      trong đó $g_i$ và $h_i$ là đạo hàm bậc một (gradient) và đạo hàm bậc hai (Hessian) của hàm mất mát:
      $$g_i = \frac{\partial l(y_i, \hat{y}^{(t-1)})}{\partial \hat{y}^{(t-1)}}, \quad h_i = \frac{\partial^2 l(y_i, \hat{y}^{(t-1)})}{\partial (\hat{y}^{(t-1)})^2}$$
    - Hàm phạt kiểm soát độ phức tạp cấu trúc cây $\Omega(f_t)$:
      $$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
      với $T$ là số lượng nút lá, $w_j$ là điểm trọng số tại lá thứ $j$, $\gamma$ là hệ số phạt bổ sung nút lá mới, $\lambda$ là hệ số chính quy hóa chuẩn $L_2$ trên trọng số lá.
    - Điểm trọng số tối ưu tại nút lá $j$:
      $$w_j^* = -\frac{G_j}{H_j + \lambda}, \quad G_j = \sum_{i \in I_j} g_i, \quad H_j = \sum_{i \in I_j} h_i$$
    - Công thức tính độ lợi phân tách (Split Gain) tại mỗi nút:
      $$\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$
      nếu $\text{Gain} \le 0$, thuật toán dừng phân nhánh (tự động cắt tỉa).
  - Ưu thế vượt bậc: Tính toán phân tán song song, tự động xử lý giá trị khuyết, chính quy hóa bậc hai chống quá khớp hiệu quả, độ chính xác dự báo cao nhất trong các bảng dữ liệu vận hành.
- **Ứng dụng cây quyết định và học kết hợp trong MBR**:
  - Dự báo chất lượng nước đầu ra nhà máy MBR (Zhuang et al., 2021).
  - Dự báo suy giảm thông lượng lọc (Li et al., 2020).
  - Hỗ trợ ra quyết định vận hành và đánh giá độ quan trọng của các thông số điều khiển (Jiang et al., 2021).

#### 2.2.4 Thuật toán k Láng giềng Gần nhất (KNN)
- **Nguyên lý học lười (Lazy learning / Instance-based learning)**:
  - Thuật toán không xây dựng hàm ánh xạ toàn cục trong pha huấn luyện. Quá trình học thực chất là việc lưu trữ toàn bộ tập dữ liệu mẫu vào bộ nhớ.
  - Phép tính dự báo chỉ bắt đầu khi nhận được một điểm truy vấn mới $x_{\text{query}}$.
- **Đo lường khoảng cách trong không gian đặc trưng**:
  - Khoảng cách Euclid (Euclidean distance):
    $$d(x, y) = \sqrt{\sum_{i=1}^p (x_i - y_i)^2} = ||x - y||_2$$
  - Khoảng cách Manhattan: $d(x, y) = \sum_{i=1}^p |x_i - y_i|$.
  - Khoảng cách Minkowski tổng quát: $d(x, y) = \left( \sum_{i=1}^p |x_i - y_i|^q \right)^{1/q}$.
- **Cơ chế ra quyết định dự báo**:
  - Tìm tập hợp $N_k(x)$ chứa $k$ điểm dữ liệu mẫu có khoảng cách ngắn nhất đến $x$.
  - Bài toán phân loại: Bỏ phiếu theo đa số:
    $$y = \arg\max_{c} \sum_{i \in N_k(x)} I(y_i = c)$$
  - Bài toán hồi quy: Tính trung bình có trọng số nghịch đảo khoảng cách:
    $$\hat{y} = \frac{\sum_{i \in N_k(x)} w_i y_i}{\sum_{i \in N_k(x)} w_i}, \quad w_i = \frac{1}{d(x, x_i) + \varepsilon}$$
- **Đặc tính kỹ thuật và hạn chế**:
  - Ưu điểm: Đơn vị thuật toán đơn giản; không yêu cầu giả định phân phối xác suất tiên nghiệm; không nhạy với nhiễu cục bộ khi chọn $k$ hợp lý.
  - Nhược điểm: Độ phức tạp tính toán và bộ nhớ lớn ở pha suy luận $\mathcal{O}(N \cdot p)$; rất nhạy cảm với thang đo đặc trưng (bắt buộc phải chuẩn hóa dữ liệu trước); hiệu năng suy giảm nghiêm trọng khi số chiều đặc trưng lớn (hiện tượng lời nguyền số chiều - curse of dimensionality).
- **Ứng dụng trong MBR**:
  - Sàng lọc và loại bỏ giá trị ngoại lai của dữ liệu cảm biến MBR (Table 1).
  - Giám sát chất lượng nước và hỗ trợ điều khiển hệ thống xử lý nước thải (Uddin et al., 2023; Xu et al., 2022).

#### 2.2.5 Các Phương pháp Học máy Khác (Other ML Methods)
- **Hồi quy Tuyến tính Đa biến (Multiple Linear Regression - MLR)**:
  - Mô hình tham số biểu diễn quan hệ tuyến tính:
    $$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p + \epsilon$$
  - Ước lượng vector hệ số $\beta$ bằng phương pháp Bình phương Tối thiểu Thông thường (Ordinary Least Squares - OLS):
    $$\hat{\beta} = (X^T X)^{-1} X^T y$$
  - Đóng vai trò là mô hình mốc chuẩn (baseline) để so sánh hiệu năng với các thuật toán học máy phi tuyến phức tạp trong MBR.
- **Hồi quy Phi tuyến (Nonlinear Regression)**:
  - Khớp các phương trình bán thực nghiệm hoặc phương trình vật lý (mô hình điện trở lọc màng Darcy, mô hình các cơ chế nghẹt màng Hermia: nghẹt hoàn toàn, nghẹt trung gian, nghẹt tiêu chuẩn, hình thành bánh bùn) vào dữ liệu thông qua giải thuật Gauss-Newton hoặc Levenberg-Marquardt.
- **Thuật toán Naive Bayes**:
  - Dựa trên Định lý Xác suất Bayes và giả định độc lập có điều kiện giữa các biến đặc trưng:
    $$P(y|x_1, \dots, x_p) = \frac{P(y) \prod_{j=1}^p P(x_j|y)}{P(x_1, \dots, x_p)}$$
  - Tốc độ huấn luyện và phân loại tức thời, sử dụng tốt trong phân loại nhị phân trạng thái vận hành màng (bình thường / tắc nghẽn nghiêm trọng).
- **Học Tăng cường Nâng cao (Advanced Reinforcement Learning - RL)**:
  - Áp dụng các thuật toán Deep Q-Network (DQN) hoặc Actor-Critic (DDPG, PPO) để điều khiển liên tục hệ thống MBR.
  - Ứng dụng: Tự động hóa quá trình loại bỏ phospho sinh học (Mohammadi et al., 2024), tối ưu hóa lưu lượng sục khí định kỳ, giảm thiểu điện năng tiêu thụ từ 15% đến 30% mà vẫn đảm bảo độ bền của màng.
- **Mô hình Nền tảng và Mô hình Lớn (Foundation & Large Models)**:
  - Các mạng nơ-ron quy mô tham số khổng lồ (hàng tỷ tham số), được tiền huấn luyện trên lượng dữ liệu lớn và có khả năng giải quyết đa nhiệm.
  - Ứng dụng: Dự báo xu hướng biến đổi khí hậu ảnh hưởng đến nguồn nước cấp, mô hình hóa phát thải khí nhà kính methane toàn cầu từ các công trình xử lý sinh học (Rouet-Leduc & Hulbert, 2024), phát triển trợ lý ảo hỗ trợ vận hành hệ thống MBR.
- **Học máy Tự động (Automated Machine Learning - AutoML)**:
  - Tự động hóa toàn diện chu trình học máy: Tiền xử lý dữ liệu $\rightarrow$ Trích xuất và chọn lọc đặc trưng $\rightarrow$ Tìm kiếm cấu trúc mô hình tối ưu $\rightarrow$ Tối ưu siêu tham số $\rightarrow$ Tích hợp mô hình (Salehin et al., 2024).
  - Giảm thiểu nhu cầu can thiệp thủ công của chuyên gia dữ liệu, nâng cao tốc độ triển khai mô hình học máy trong dự báo chất lượng nước và kiểm soát MBR (Senthil Kumar et al., 2024).

#### 2.2.6 Các Thuật toán Tối ưu hóa Thông minh Liên quan (Related Optimization Algorithms)
- **Hệ Logic Mờ (Fuzzy Logic) và Mạng Nơ-ron Mờ (FNN)**:
  - Logic mờ mô phỏng tư duy định tính của con người bằng cách gán cho mỗi biến một giá trị chân lý thuộc đoạn $[0, 1]$ thông qua hàm thuộc tính (membership functions: hình tam giác, hình thang, hàm Gauss).
  - Cấu trúc hệ mờ gồm 4 khối: Khối mờ hóa (Fuzzification) $\rightarrow$ Khối cơ sở luật If-Then $\rightarrow$ Động cơ suy luận mờ (Mamdani hoặc Sugeno) $\rightarrow$ Khối giải mờ (Defuzzification).
  - Mạng nơ-ron mờ (Fuzzy Neural Network - FNN): Kết hợp khả năng diễn giải bằng quy tắc mờ của Logic mờ với năng lực tự học từ dữ liệu của ANN. FNN sinh ra cơ sở tri thức chuyên gia từ dữ liệu vận hành có độ bất định và nhiễu lớn trong hệ thống MBR (de Campos Souza, 2020).
- **Phương pháp Mô phỏng Monte Carlo**:
  - Phương pháp tính toán số học dựa trên lý thuyết xác suất và Định lý Số lớn (Law of Large Numbers):
    $$\bar{X}_N = \frac{1}{N} \sum_{i=1}^N f(X_i) \xrightarrow{P} \mathbb{E}[f(X)]$$
  - Cơ chế: Thực hiện lấy mẫu ngẫu nhiên hàng nghìn đến hàng triệu lần từ các phân phối xác suất của biến đầu vào (nhiệt độ nước, chất lượng nước thải đầu vào dao động) để mô phỏng phân phối độ bất định của đầu ra (tuổi thọ màng, chi phí vận hành).
  - Kết hợp với học tăng cường (như thuật toán tìm kiếm cây Monte Carlo - MCTS trong AlphaGo, Silver et al., 2016) nhằm tăng cường năng lực ra quyết định điều khiển tối ưu trong điều kiện thiếu dữ liệu chính xác.
- **Giải thuật Di truyền (Genetic Algorithm - GA)**:
  - Thuật toán tìm kiếm ngẫu nhiên mô phỏng quá trình tiến hóa sinh học tự nhiên của Darwin (Katoch et al., 2021).
  - **Mã hóa cá thể**: Các siêu tham số (như cặp $[C, \gamma]$ của SVM hoặc số nơ-ron tầng ẩn và tốc độ học của ANN) được mã hóa thành chuỗi nhiễm sắc thể (dạng nhị phân hoặc vector số thực).
  - **Hàm thích nghi (Fitness function)**: Định nghĩa dựa trên sai số của mô hình học máy, ví dụ: $\text{Fitness} = \frac{1}{\text{RMSE} + \epsilon}$ hoặc $\text{Fitness} = R^2$.
  - **Các toán tử tiến hóa cốt lõi**:
    1. **Toán tử chọn lọc (Selection)**: Lựa chọn các cá thể có độ thích nghi cao vào quần thể sinh sản qua cơ chế Bánh xe Roulette (Roulette Wheel Selection) hoặc Chọn lọc Giải đấu (Tournament Selection).
    2. **Toán tử lai ghép (Crossover)**: Trao đổi đoạn gen giữa hai nhiễm sắc thể cha mẹ với xác suất lai ghép $P_c \in [0.6, 0.9]$ để sinh ra các cá thể con mới.
    3. **Toán tử đột biến (Mutation)**: Biến đổi ngẫu nhiên một hoặc nhiều gen trong nhiễm sắc thể với xác suất đột biến nhỏ $P_m \in [0.001, 0.05]$. Toán tử này duy trì tính đa dạng di truyền của quần thể và ngăn ngừa bầy rơi vào cực tiểu cục bộ.
- **Tối ưu hóa Bầy đàn (Particle Swarm Optimization - PSO)**:
  - Mô phỏng hành vi di chuyển tìm mồi có tính xã hội của đàn chim hoặc đàn cá (Eberhart & Kennedy).
  - Mỗi hạt trong bầy đại diện cho một nghiệm siêu tham số trong không gian tìm kiếm đa chiều. Hạt sở hữu vị trí hiện tại $x_i^t$ và vector vận tốc $v_i^t$.
  - **Công thức cập nhật vận tốc và vị trí**:
    $$v_{i}^{t+1} = w v_i^t + c_1 r_1 (pbest_i - x_i^t) + c_2 r_2 (gbest - x_i^t)$$
    $$x_i^{t+1} = x_i^t + v_i^{t+1}$$
    trong đó:
    - $w$: Hệ số quán tính (inertia weight), điều khiển khả năng cân bằng giữa thăm dò toàn cục (exploration) và khai thác cục bộ (exploitation).
    - $c_1$: Hệ số học tập nhận thức cá nhân (cognitive parameter), thúc đẩy hạt quay lại vị trí tốt nhất trong lịch sử bản thân $pbest_i$.
    - $c_2$: Hệ số học tập xã hội (social parameter), hướng hạt di chuyển về phía vị trí tốt nhất của toàn bộ bầy $gbest$.
    - $r_1, r_2$: Các số ngẫu nhiên phân bố đều trong khoảng $[0, 1]$.
  - Ưu thế: Cấu trúc toán học đơn giản, dễ cài đặt, không cần tính toán ma trận đạo hàm, tốc độ hội tụ nhanh hơn GA trong tối ưu siêu tham số SVR và ANN.
- **Thuật toán Đàn dơi (Bat Algorithm - BA) và Tối ưu Sói xám (Grey Wolf Optimizer - GWO)**:
  - **Thuật toán Đàn dơi (BA)**: Do Yang (2010) phát triển, mô phỏng hành vi định vị bằng tiếng vang (echolocation) của dơi. Thuật toán điều chỉnh tần số phát xung $f_i = f_{\min} + (f_{\max} - f_{\min})\beta$, cập nhật vận tốc và vị trí, đồng thời kiểm soát độ to âm thanh $A_i$ và tỷ lệ phát xung $r_i$ để hội tụ về nghiệm tối ưu.
  - **Tối ưu Sói xám (GWO)**: Do Mirjalili và cộng sự (2014) phát triển, mô phỏng thứ bậc xã hội nghiêm ngặt của loài sói xám gồm 4 cấp bậc: sói đầu đàn alpha ($\alpha$), sói cố vấn beta ($\beta$), sói chấp hành delta ($\delta$), và bầy sói cấp dưới omega ($\omega$). Thuật toán mô phỏng 3 giai đoạn săn mồi: theo dõi/bao vây con mồi, rượt đuổi, và tấn công con mồi theo hướng dẫn của bộ ba $\alpha, \beta, \delta$.
  - **Hiệu quả thực nghiệm**: Việc lai ghép các thuật toán metaheuristic (GA, PSO, BA, GWO) với các mô hình học máy (SVM, ANN, RF) giúp nâng cao hệ số xác định $R^2$ từ 5% đến 20%, đồng thời giảm sai số RMSE từ 15% đến 40% so với phương pháp thử-sai thủ công trong dự báo hiện tượng nghẹt màng MBR.
