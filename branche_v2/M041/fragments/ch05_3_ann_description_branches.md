### ANN description

* **Khái niệm và nền tảng của Mạng nơ-ron nhân tạo (Artificial Neural Network - ANN)**:
    * **Định nghĩa và nguyên lý sinh học**: ANN là mô hình điện toán mô phỏng theo cấu trúc và phương thức vận hành của các mạng nơ-ron sinh học (biological neural networks). Mạng bao gồm nhiều nơ-ron hay các đơn vị xử lý kết nối mạng (networked processing units) phối hợp với nhau nhằm giải quyết các bài toán kỹ thuật phức tạp.
    * **Kiến trúc Perceptron đa tầng (Multilayer Perceptron - MLP)**: Là một dạng mạng nơ-ron truyền thẳng (feedforward neural network) gồm nhiều tầng nơ-ron:
        * Lớp đầu vào (input layer): Tiếp nhận các biến hoặc đặc trưng đầu vào của bài toán.
        * Một hoặc nhiều lớp ẩn (one or more hidden layers): Thực hiện việc trích xuất đặc trưng và biến đổi phi tuyến không gian dữ liệu.
        * Lớp đầu ra (output layer): Tính toán và xuất ra các giá trị dự báo cuối cùng.
    * **Thuật toán lan truyền ngược (Backpropagation algorithm)**: MLP được huấn luyện thông qua kỹ thuật lan truyền ngược nhằm liên tục điều chỉnh các trọng số liên kết (connection weights) giữa các nơ-ron, cực tiểu hóa sai số giữa kết quả dự báo và dữ liệu thực tế quan sát được.
    * **Lợi thế tính toán trong kỹ thuật môi trường**: MLP là một trong những mạng nơ-ron sâu cơ bản nhất (basic deep neural networks), cho phép nắm bắt trọn vẹn động học phi tuyến mà không đòi hỏi chi phí tính toán quá cao (avoiding high processing demands) như các kiến trúc học sâu hiện đại phức tạp.

* **Cấu trúc kiến trúc và quy tắc thiết lập siêu tham số của mô hình MLP**:
    * **Số lượng lớp ẩn (Hidden layer count)**:
        * Là siêu tham số quan trọng cần được tinh chỉnh (hyperparameter tuning). Về mặt lý thuyết, mô hình MLP có thể thiết lập số lượng lớp ẩn tùy ý.
        * **Quy tắc kinh nghiệm (Rules of thumb)**: Bắt đầu cấu hình với $1$ lớp ẩn duy nhất và tăng dần số lớp cho đến khi hiệu năng mô hình trên tập kiểm định không còn được cải thiện.
        * **Kiểm định chéo (Cross-validation)**: Khuyến nghị sử dụng các phương pháp kiểm định chéo để tìm ra số lượng lớp ẩn tối ưu, đảm bảo tính tổng quát hóa tốt nhất.
    * **Số lượng nơ-ron trong lớp ẩn (Number of neurons in hidden layers)**:
        * Là siêu tham số quyết định trực tiếp dung lượng học tập (learning capacity) của mô hình.
        * **Quy tắc biên**: Lựa chọn số lượng nơ-ron nằm trong khoảng trung gian giữa kích thước của lớp đầu vào và lớp đầu ra.
        * **Quy tắc tỷ lệ hai phần ba**: Thiết lập số lượng nơ-ron bằng hai phần ba ($2/3$) tổng kích thước của lớp đầu vào và lớp đầu ra.
    * **Cấu trúc hoàn toàn kết nối (Fully connected architecture)**:
        * Sơ đồ dòng dữ liệu bắt đầu từ lớp đầu vào đại diện cho các thuộc tính đặc trưng.
        * Mỗi nơ-ron ở lớp đầu vào kết nối toàn phần tới mọi nơ-ron của lớp ẩn đầu tiên; mỗi liên kết mang một trọng số đại diện cho cường độ tương tác.
        * Quá trình truyền xuôi tiếp tục được lặp lại qua từng lớp ẩn liên tiếp cho đến khi tới lớp đầu ra.

* **Cơ chế tính toán toán học trong nơ-ron (Mathematical Formulation of Neuron Processing)**:
    * **Tính toán đầu vào nơ-ron (Neuron input calculation - Weighted sum)**:
        * Đối với một nơ-ron đơn lẻ trong mạng, tổng có trọng số của các đầu vào kết hợp với số hạng độ lệch (bias term) được xác định theo phương trình (11):
          $$Z = \sum_{i=1}^{n} (w_i \cdot x_i) + b \quad (11)$$
          Trong đó:
          * $Z$ (hoặc $z$): Tổng có trọng số của các tín hiệu đầu vào cộng với độ lệch bias.
          * $x_i$: Tín hiệu đầu vào thứ $i$ đưa vào nơ-ron.
          * $w_i$: Trọng số liên kết gắn liền với đầu vào $x_i$.
          * $b$: Số hạng độ lệch (bias term), đóng vai trò ngưỡng dịch chuyển cho hàm kích hoạt.
    * **Áp dụng hàm kích hoạt (Activation function transformation)**:
        * Hàm kích hoạt $f(z)$ được áp dụng trực tiếp lên tổng có trọng số $z$ theo phương trình (12):
          $$a = f(z) \quad (12)$$
          Trong đó $a$ là giá trị kích hoạt đầu ra của nơ-ron được truyền tiếp xuống lớp kế cận.
        * **Vai trò**: Đưa đặc tính phi tuyến (non-linearity) vào mạng nơ-ron, cho phép mô hình học và xấp xỉ các mối quan hệ động học và hóa sinh phức tạp.
    * **Tính toán đầu ra tại lớp đầu ra (Output layer computation)**:
        * Hàm kích hoạt của nơ-ron lớp đầu ra tạo ra giá trị dự đoán cuối cùng $y$ theo phương trình (13):
          $$y = f\left(\sum_{i=1}^{n} (w_i \cdot x_i) + b\right) \quad (13)$$
          Giá trị $y$ này biểu diễn đại lượng được mô hình mạng nơ-ron dự báo cho biến mục tiêu tương ứng.

* **Các hàm kích hoạt và phạm vi ứng dụng trong MLP**:
    * **Hàm kích hoạt cho lớp ẩn (Hidden layer activation functions)**:
        * **Hàm Hyperbolic Tangent Sigmoid ($\tanh$ / `tansig`)**: Ánh xạ bất kỳ giá trị đầu vào nào thành giá trị trong dải $[-1, 1]$. Tính đối xứng qua gốc tọa độ giúp quá trình tối ưu hóa lan truyền ngược hội tụ nhanh hơn.
        * **Hàm Sigmoid đối xứng / Logistic (`logsig`)**: Ánh xạ dần dần bất kỳ giá trị đầu vào nào thành giá trị thực trong khoảng $[0, 1]$.
        * **Hàm Rectified Linear Unit (ReLU)**: Hàm phi tuyến từng đoạn không trơn (non-smooth), ánh xạ mọi giá trị $< 0$ về $0$ và giữ nguyên giá trị đầu vào nếu $\ge 0$ ($f(z) = \max(0, z)$).
    * **Hàm kích hoạt cho lớp đầu ra (Output layer activation functions)**:
        * **Bài toán phân loại (Classification tasks)**: Thường sử dụng hàm Softmax để chuyển đổi các đầu ra thành phân phối xác suất.
        * **Bài toán hồi quy (Regression tasks)**: Thường sử dụng hàm tuyến tính đồng nhất (Identity function / linear / `purelin`), cho phép mô hình dự báo không bị giới hạn trong dải giá trị thực liên tục của các chỉ tiêu chất lượng nước thải.

* **Hiện tượng quá khớp và các chiến lược kiểm soát (Overfitting & Regularization)**:
    * **Bản chất của hiện tượng quá khớp (Overfitting)**:
        * Xảy ra khi mô hình đạt độ chính xác quá cao trên tập huấn luyện (training data) nhưng hoạt động rất kém trên tập dữ liệu mới chưa từng thấy (fresh/unseen data).
        * Nguyên nhân do mô hình quá phức tạp so với lượng dữ liệu huấn luyện có sẵn, dẫn tới việc mạng ghi nhớ (memorize) các điểm dữ liệu cụ thể và nhiễu ngẫu nhiên thay vì học các quy luật quy nạp bản chất (underlying patterns).
    * **Kỹ thuật điều chuẩn (Regularization techniques - L1 & L2)**:
        * Bổ sung một số hạng phạt (penalty term) vào hàm mất mát (loss function) nhằm khuyến khích mô hình duy trì các giá trị trọng số nhỏ hơn.
        * Giúp đơn giản hóa cấu trúc mô hình và kiểm soát độ phức tạp hiệu quả.
    * **Điều chuẩn loại bỏ nơ-ron (Dropout regularization)**:
        * Trong quá trình huấn luyện, kỹ thuật dropout loại bỏ ngẫu nhiên một tỷ lệ nơ-ron trong mạng ở mỗi lượt lặp.
        * Thúc đẩy mô hình hình thành các đặc trưng bền vững (robust features) và ngăn ngừa hiện tượng phụ thuộc quá mức vào bất kỳ một nơ-ron đơn lẻ nào.
    * **Phát hiện quá khớp qua kiểm định chéo (Cross-validation)**:
        * Đánh giá song song hiệu năng của mô hình trên cả tập huấn luyện và tập kiểm định. Hiện tượng quá khớp được xác nhận khi sai số trên tập kiểm định tăng cao rõ rệt so với sai số trên tập huấn luyện.

* **Chiến lược phân chia tập dữ liệu và Thuật toán huấn luyện Levenberg-Marquardt**:
    * **Phân chia tập dữ liệu (Dataset partitioning - 70/15/15)**:
        * **Tập huấn luyện (Training set - 70%)**: Dùng để tính toán gradient và trực tiếp cập nhật các trọng số liên kết và độ lệch ($w, b$) của mô hình mạng.
        * **Tập kiểm định (Validation set - 15%)**: Dùng để theo dõi độc lập độ chính xác trong quá trình huấn luyện, ngăn ngừa hiện tượng quá khớp thông qua cơ chế giám sát sai số.
        * **Tập kiểm tra (Testing set - 15%)**: Hoàn toàn độc lập, không tham gia vào quá trình tối ưu hóa trọng số hay lựa chọn mô hình, dùng để đánh giá năng lực tổng quát hóa khách quan trên dữ liệu thực tế.
    * **Thuật toán huấn luyện Levenberg-Marquardt (LM backpropagation)**:
        * Là thuật toán tối ưu hóa bậc hai dựa trên xấp xỉ ma trận Hessian ($H \approx J^T J + \mu I$, với $J$ là ma trận Jacobian của sai số).
        * Kết hợp linh hoạt giữa tốc độ hội tụ nhanh vượt trội của phương pháp Gauss-Newton (khi gần điểm cực tiểu) và tính ổn định bền vững của phương pháp hạ độ dốc (gradient descent - khi ở xa điểm cực tiểu).
        * Được xem là giải thuật huấn luyện chuẩn mực có hiệu quả cao nhất cho các mạng MLP quy mô vừa và nhỏ trong mô hình hóa kỹ thuật môi trường.
    * **Tiêu chí dừng và kỹ thuật dừng sớm (Stopping criteria & Early Stopping)**:
        * **Dừng sớm dựa trên kiểm định (Validation checks / Early Stopping)**: Quá trình huấn luyện tự động dừng lại khi sai số trên tập kiểm định liên tiếp không giảm trong $6$ epoch kiểm tra (validation checks fail = 6); các trọng số tối ưu tại epoch có sai số kiểm định nhỏ nhất được lưu trữ lại nhằm triệt tiêu hoàn toàn quá khớp.
        * **Các ngưỡng dừng bổ sung**: Đạt số chu kỳ tối đa (maximum epochs), gradient sai số giảm xuống dưới ngưỡng cực tiểu cho phép, hoặc tham số suy giảm $\mu$ vượt ngưỡng tối đa ($\mu_{\max}$).

* **Các chỉ số đánh giá hiệu năng mô hình (Performance Evaluation Metrics)**:
    * **Sai số toàn phương trung bình (Mean Squared Error - MSE)**:
        * Là hàm mất mát tiêu chuẩn trong huấn luyện và đánh giá MLP, đo lường sai khác bình phương trung bình giữa giá trị thực nghiệm và giá trị dự báo theo phương trình (14):
          $$\text{MSE} = \frac{1}{n} \sum (y - a)^2 \quad (14)$$
          Trong đó:
          * $n$: Cỡ mẫu quan sát (sample size).
          * $y$: Giá trị thực tế thu được từ thực nghiệm.
          * $a$: Giá trị dự đoán bởi mạng nơ-ron.
          * $\text{Sum}$: Tổng bình phương sai số trên toàn bộ tập dữ liệu mẫu.
    * **Hệ số xác định ($R^2$ / R-squared)**:
        * Đo lường mức độ phù hợp của mô hình đối với dữ liệu thực nghiệm, dao động trong dải từ $0$ đến $1$ ($1$ đại diện cho sự trùng khớp tuyệt đối) theo phương trình (15):
          $$R^2 = 1 - \frac{\sum (y - a)^2}{\sum (y - \bar{y})^2} \quad (15)$$
          Trong đó:
          * $y$: Giá trị đầu ra thực tế.
          * $a$: Giá trị đầu ra dự đoán.
          * $\bar{y}$ ($\text{mean}(y)$): Giá trị trung bình cộng của các đầu ra thực tế quan sát được.

* **Thiết lập mô hình ANN trong nghiên cứu cụ thể này**:
    * **Nguồn dữ liệu thực nghiệm**: Mô hình MLP được xây dựng và huấn luyện dựa trên $44$ điểm dữ liệu thực nghiệm nuôi cấy liên tục vi tảo *Platymonas helgolandica tsingtaoensis* trong hệ thống MBR xử lý nước thải nuôi trồng thủy sản từ nghiên cứu của Yi Ding et al.
    * **Các biến đầu vào ($3$ thông số vận hành)**:
        * Thời gian vận hành ($\text{Time}$, đơn vị: ngày / days).
        * Độ $\text{pH}$.
        * Nồng độ tổng carbon hữu cơ đầu vào ($\text{TOC}$, đơn vị: mg/L).
    * **Các biến đầu ra ($4$ chỉ tiêu xử lý chất dinh dưỡng)**:
        * Nồng độ amonia nitơ ($\text{NH}_4^+\text{-N}$) và hiệu suất loại bỏ amonia nitơ ($\%$).
        * Nồng độ phosphat ($\text{PO}_4^{3-}$) và hiệu suất loại bỏ phosphat ($\%$).
    * **Cấu hình hàm kích hoạt và thuật toán trong nghiên cứu**:
        * Lớp ẩn: Sử dụng hàm kích hoạt hyperbolic tangent sigmoid (`tansig`) nhằm nắm bắt trọn vẹn bản chất phi tuyến phức tạp trong quá trình hấp thụ dinh dưỡng của vi tảo.
        * Lớp đầu ra: Sử dụng hàm kích hoạt tuyến tính đồng nhất (`purelin`) để thực hiện tác vụ hồi quy liên tục cho các chỉ số nồng độ và hiệu suất.
        * Giải thuật huấn luyện: Áp dụng thuật toán Levenberg-Marquardt (LM) với chiến lược chia dữ liệu $70/15/15$ và cơ chế Early Stopping để ngăn chặn quá khớp, sử dụng $\text{MSE}$ và $R^2$ làm thước đo định lượng chính xác độ tin cậy của mô hình.
