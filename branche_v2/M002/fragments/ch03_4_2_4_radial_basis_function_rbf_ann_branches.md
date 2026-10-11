### 2.4. Radial basis function (RBF) ANN

* **Khái niệm và đặc tính vượt trội của mạng nơ-ron nhân tạo hàm cơ sở xuyên tâm (Radial Basis Function Artificial Neural Network - RBF ANN):**
  * **Mô hình mạng nơ-ron nhân tạo (ANN):**
    * Mạng nơ-ron nhân tạo là một mô hình toán học phỏng sinh học mô phỏng theo cấu trúc liên kết khớp thần kinh (synaptic connections) của não bộ con người nhằm mục đích xử lý thông tin phi tuyến tính phức tạp.
    * Các ưu điểm vượt trội nổi bật của ANN trong tính toán kỹ thuật bao gồm khả năng tự học thích ứng (self-study), khả năng lưu trữ thông tin phân tán (storage), và năng lực tìm kiếm tối ưu hóa tốc độ cao (high-speed search capabilities) (Iliyas et al., 2013; Sreekanth et al., 2010).
    * Trong số các họ kiến trúc mạng nơ-ron nhân tạo, mô hình mạng truyền thẳng (feedforward neural networks) được ứng dụng rộng rãi và phổ biến nhất trong các bài toán kỹ thuật môi trường và công nghệ xử lý nước (Basheer and Hajmeer, 2000).
  * **Đặc tính ưu việt của mạng RBF ANN:**
    * Mạng nơ-ron hàm cơ sở xuyên tâm (RBF ANN) là một đại diện điển hình của mạng nơ-ron truyền thẳng, đã được chứng minh toán học là sở hữu năng lực xấp xỉ vạn năng (universal approximation ability) (Bakire et al., 2018; Dreiseitl and Ohno-Machado, 2002).
    * Khác biệt căn bản với các mạng perceptron đa tầng (MLP) truyền thống dùng thuật toán lan truyền ngược (backpropagation) vốn thường bị mắc kẹt tại các điểm cực tiểu cục bộ, RBF ANN hoàn toàn không gặp phải vấn đề bẫy cực tiểu địa phương (no local minimum problem) (Bakire et al., 2018; Dreiseitl and Ohno-Machado, 2002).
    * So với các mô hình mạng nơ-ron nhân tạo phức tạp khác, RBF ANN sở hữu cấu trúc mạng gọn gàng, đơn giản hơn (simpler structure) và thuật toán học tập hội tụ nhanh hơn vượt trội (faster learning algorithm) (Basheer and Hajmeer, 2000; Sreekanth et al., 2010).

* **Cấu trúc kiến trúc ba tầng của mô hình mạng RBF (Three-Layer Architecture of RBF Network Model):**
  * Mô hình mạng RBF điển hình sở hữu cấu trúc mạng truyền thẳng gồm ba tầng: tầng đầu vào (input layer), tầng ẩn (hidden layer) với các nơ-ron cơ sở xuyên tâm, và tầng đầu ra tuyến tính (output layer) (Fig. 1):
    * **Hình 1.** Kiến trúc mô hình mạng nơ-ron RBF ba tầng
      * <img src="assets/fig_01_p3.jpeg" alt="Hình 1" />
      * **Hình này chứng minh điều gì**
        * Liên kết đầy đủ một chiều từ các nút vào tới từng nút ẩn Gauss, sau đó kết hợp tuyến tính về một nút ra duy nhất.
      * **Từ đâu mà thấy được**
        * Luồng từ trái qua phải: nút vào (lam nhạt) phát mũi tên liền đến nút ẩn (cam) chứa đồ thị Gauss, rồi đường đứt nét hội tụ về nút ra "output layer".
  * **Cơ chế truyền dẫn và xử lý tín hiệu qua ba tầng mạng:**
    * **Tầng đầu vào (Input layer):**
      * Tiếp nhận một khối lượng lớn thông tin phi tuyến tính từ môi trường thực nghiệm. Tầng này bao gồm các nút thụ động, chỉ thực hiện chức năng tiếp nhận và kết nối truyền thẳng các giá trị của vectơ biến đầu vào đến tất cả các nút của tầng kế tiếp mà không thực hiện biến đổi số học nào.
      * Trong nghiên cứu này, biến đầu vào duy nhất đưa vào mạng là khoảng cách phân tách liên bề mặt $h$ (separation distance, biến thiên liên tục trong dải từ $0{,}158\text{ nm}$ đến $12\text{ nm}$).
    * **Tầng ẩn phi tuyến (Hidden layer):**
      * Chứa các nút nơ-ron cơ sở xuyên tâm thực hiện phép ánh xạ phi tuyến dữ liệu từ không gian đầu vào sang không gian đặc trưng ẩn có số chiều cao hơn.
      * Mỗi nơ-ron ở tầng ẩn sở hữu một đáp ứng cục bộ đối xứng xuyên tâm quanh một điểm tâm cố định.
      * Số lượng nút nơ-ron ở tầng ẩn của mạng RBF được thiết lập đồng nhất bằng đúng số lượng mẫu huấn luyện ($N_{\text{hidden}} = N_{\text{samples}}$).
    * **Tầng đầu ra tuyến tính (Output layer):**
      * Tiếp nhận các đáp ứng phi tuyến từ tầng ẩn và thực hiện phép kết hợp tuyến tính (linear combination) có trọng số để xuất ra kết quả dự đoán cuối cùng.
      * Trong nghiên cứu này, đầu ra của mạng là các giá trị năng lượng tương tác liên bề mặt ($U^{\text{LW}}$, $U^{\text{EL}}$, $U^{\text{AB}}$, hoặc $U^{\text{TOT}}$).

* **Hàm kích hoạt cơ sở xuyên tâm Gauss và công thức toán học đầu ra (Gaussian Activation Function and Network Output Formulation):**
  * **Hàm kích hoạt Gauss (Gaussian activation function):**
    * Mặc dù có nhiều dạng hàm cơ sở xuyên tâm khả dĩ cho các nơ-ron tầng ẩn, hàm Gauss là hàm kích hoạt thông dụng và hiệu quả nhất (Dreiseitl and Ohno-Machado, 2002), được xác định theo phương trình (11):
      $$\phi_i(x) = \exp\left( -\frac{\|x - c_i\|^2}{2\sigma_i^2} \right) \quad (11)$$
      hoặc được viết gọn dưới dạng hàm khoảng cách vô hướng xuyên tâm $r = \|x - c_i\|$:
      $$\phi(r) = \exp\left( -\frac{r^2}{2\sigma^2} \right)$$
      trong đó:
      * $x$ là vectơ tín hiệu đầu vào đưa vào mạng nơ-ron.
      * $c_i$ là tọa độ tâm (center) của nút RBF thứ $i$.
      * $\sigma_i$ là độ rộng hay độ phân tán (spread / width parameter) của hàm cơ sở Gauss tại nút RBF thứ $i$.
      * $\|x - c_i\|$ là chuẩn khoảng cách Euclid (Euclidean norm) giữa điểm đầu vào $x$ và tâm $c_i$. Giá trị hàm kích hoạt $\phi_i(x)$ đạt cực đại bằng $1$ khi khoảng cách $r = \|x - c_i\| = 0$ và suy giảm đơn điệu về $0$ khi khoảng cách tăng dần ra xa tâm.
  * **Tính toán kết quả đầu ra tại tầng đầu ra (Output layer linear combination):**
    * Giá trị đầu ra của mạng ($y$) được sinh ra từ tổ hợp tuyến tính giữa các giá trị hàm kích hoạt của tầng ẩn nhân với vectơ trọng số của tầng đầu ra $\omega$ (Sreekanth et al., 2010), mô tả theo phương trình (12):
      $$y = \sum_{i=0}^n \omega_i \phi_i \quad (12)$$
      trong đó:
      * $\omega_i$ là giá trị trọng số liên kết (joint weighted value) tương ứng của hàm cơ sở thứ $i$.
      * $n$ là tổng số nút nơ-ron hàm cơ sở trong tầng ẩn.
      * Số hạng $i = 0$ đại diện cho trọng số độ lệch hằng số (bias weight $\omega_0$ với $\phi_0 = 1$).

* **Quy trình huấn luyện hai bước, thuật toán bình phương tối thiểu trực giao (OLS) và tối ưu hóa trọng số:**
  * **Hai bước huấn luyện tổng quát của RBF ANN:**
    * Trước khi đưa vào sử dụng để dự báo thực tế, mạng RBF ANN phải trải qua quy trình huấn luyện gồm hai giai đoạn độc lập:
      * **Bước 1 - Lựa chọn tâm (Center selection):** Tuyển chọn các tâm đại diện từ tập dữ liệu huấn luyện hoặc thực hiện kỹ thuật phân cụm (clustering) không giám sát trên dữ liệu huấn luyện để thiết lập các vị trí tâm $c_i$.
      * **Bước 2 - Ước lượng trọng số tuyến tính (Weight estimation):** Sử dụng phương pháp bình phương tối thiểu thông thường (ordinary least squares) để ước lượng tối ưu vectơ trọng số $\omega$ của tầng đầu ra.
  * **Kỹ thuật bình phương tối thiểu trực giao (Orthogonal Least Squares - OLS):**
    * Chiến lược học tập phổ biến và hiệu quả nhất để lựa chọn các tâm RBF là chiến lược chọn tâm tự tổ chức (self-organized centre selection).
    * Kỹ thuật bình phương tối thiểu trực giao (OLS), một phương pháp tự tổ chức nổi tiếng đề xuất bởi Bianchini et al. (1995), được ứng dụng trong nghiên cứu này để lựa chọn các tâm RBF.
    * Kỹ thuật OLS tích hợp thuật toán trực giao hóa Gram–Schmidt (Gram–Schmidt algorithm) nhằm lựa chọn và cập nhật các tâm một cách có chọn lọc và tối ưu (Iliyas et al., 2013). Thuật toán Gram–Schmidt biến đổi tập hợp các vectơ hàm cơ sở thành các vectơ trực giao độc lập tuyến tính, giúp định lượng chính xác mức đóng góp riêng biệt của từng tâm ứng viên vào tỷ lệ suy giảm phương sai sai số, loại bỏ hoàn toàn hiện tượng đa cộng tuyến và dư thừa nơ-ron.
  * **Thích ứng trọng số theo quy trình hạ độ dốc (Adaptive gradient descent):**
    * Bằng cách kết hợp kỹ thuật OLS, các trọng số liên kết có thể được điều chỉnh tối ưu thông qua quy trình hạ độ dốc thích ứng (adaptive gradient descent procedure) (Chen et al., 1991).
  * **Hàm tổn thất / hàm chi phí (Cost function / loss function):**
    * Các giá trị tham số tối ưu của mạng nơ-ron được xác định khi chúng cực tiểu hóa hàm mục tiêu sai số toàn phương (cost function $J$), biểu diễn theo phương trình (13):
      $$J = \min \sum_{i=1}^Q |Y_i - y_i|^2 \quad (13)$$
      trong đó:
      * $Q$ là số lượng mẫu trong tập dữ liệu huấn luyện (training pattern number).
      * $Y_i$ là giá trị đầu ra do mạng nơ-ron RBF tính toán/dự đoán (network output).
      * $y_i$ là giá trị đầu ra mục tiêu mong muốn (desired target output) lấy từ tập dữ liệu tính toán chuẩn.

* **Thiết lập mô hình hóa tương tác liên bề mặt và công thức đánh giá sai số tương đối (Model Configuration and Relative Error Formulation):**
  * **Thiết lập tập dữ liệu huấn luyện và kiểm tra:**
    * Chuỗi dữ liệu định lượng năng lượng tương tác liên bề mặt thu nhận từ phương pháp XDLVO nâng cao (advanced XDLVO approach) được phân chia thành tập huấn luyện (training set) và tập kiểm tra (test set) cho mạng nơ-ron RBF.
    * Các điểm dữ liệu XDLVO nâng cao được chọn lọc để huấn luyện mạng RBF, sau đó mô hình mạng RBF đã được huấn luyện tối ưu được triển khai để dự đoán các đường cong năng lượng tương tác liên bề mặt tại các khoảng cách phân tách $h$ khác nhau.
    * Số lượng nút nơ-ron ở tầng ẩn của mạng RBF được thiết lập đồng nhất bằng đúng số lượng mẫu huấn luyện ($N_{\text{hidden}} = N_{\text{samples}}$, với các quy mô khảo sát cụ thể là $5$, $10$, $15$, và $20$ mẫu).
  * **Biến đầu vào và đầu ra của bài toán:**
    * **Vectơ đầu vào:** Khoảng cách phân tách $h$ (separation distance) giữa hạt bùn hoạt tính dạng hạt và bề mặt màng PVDF nhám ngẫu nhiên ($0{,}158\text{ nm} \le h \le 12\text{ nm}$).
    * **Vectơ đầu ra:** Các thành phần năng lượng tương tác liên bề mặt cục bộ gồm tương tác phân tán Lifshitz–van der Waals ($U^{\text{LW}}$), tương tác lớp điện kép tĩnh điện ($U^{\text{EL}}$), tương tác phân cực axit–bazơ Lewis ($U^{\text{AB}}$), và tổng năng lượng tương tác liên bề mặt ($U^{\text{TOT}}$).
  * **Công thức định lượng sai số tương đối (Relative error $R$):**
    * Sai số tương đối $R$ của giá trị đầu ra dự đoán từ mạng nơ-ron được đánh giá theo phương trình (14):
      $$R = \frac{Y - y}{Y} \quad (14)$$
      trong đó:
      * $Y$ là giá trị năng lượng tương tác do mạng nơ-ron RBF dự đoán (network output, tương ứng $U_{\text{pred}}$).
      * $y$ là giá trị năng lượng tương tác tính toán chuẩn từ phương pháp XDLVO nâng cao (calculation value of the advanced XDLVO approach, tương ứng $U_{\text{calc}}$).
    * Trong lý thuyết sai số mô hình hồi quy, công thức tính sai số tương đối còn được biểu diễn quy chuẩn so với giá trị tính toán lý thuyết:
      $$R = \frac{U_{\text{pred}} - U_{\text{calc}}}{U_{\text{calc}}}$$
      Chỉ số sai số tương đối $R$ này là tiêu chí cốt lõi để đánh giá độ chính xác, độ tin cậy và mức độ tiệm cận của mạng RBF đối với các đường cong năng lượng tương tác bề mặt màng thực tế.
