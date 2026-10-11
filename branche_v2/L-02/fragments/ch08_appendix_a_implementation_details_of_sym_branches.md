## Appendix A: Implementation Details of Symbolic Regression

* **Tổng quan triển khai hồi quy ký hiệu (symbolic regression) trong SymboLLM-FE:**
  * Cung cấp đặc tả kỹ thuật chi tiết về hồi quy ký hiệu được tích hợp trong khuôn khổ SymboLLM-FE nhằm tự động sinh công thức đặc trưng.
  * Thư viện nền tảng: Sử dụng thư viện `gplearn` (phiên bản v0.4.1), triển khai mô hình quy hoạch di truyền (Genetic Programming - GP).
  * Mục tiêu cốt lõi: Khám phá các biểu thức toán học có khả năng diễn giải cao (interpretable mathematical expressions) bằng cách tiến hóa một quần thể gồm các cây cú pháp (syntax trees, ký hiệu là $T$) dựa trên các cơ chế mô phỏng chọn lọc tự nhiên (natural selection).

### A.1 Algorithmic Framework

* **Mục tiêu tối ưu hóa và không gian tìm kiếm hàm toán học:**
  * Mục tiêu cốt lõi của hồi quy ký hiệu là duyệt qua không gian các hàm toán học để tìm biểu thức tối ưu $T^*$ nhằm cực tiểu hóa sai số dự đoán trên dữ liệu huấn luyện.
  * Ký hiệu toán học: Gọi $X_{\text{train}} \in \mathbb{R}^{N \times d}$ là ma trận đặc trưng huấn luyện và $y_{\text{train}} \in \mathbb{R}^N$ là vector nhãn mục tiêu cho tập con tương ứng.

* **Bốn giai đoạn lặp (four iterative phases) trong quy trình Lập trình Di truyền:**
  * **1. Khởi tạo quần thể (Population Initialization):**
    * Quần thể ban đầu $P_0$ gồm $P$ cá thể được khởi tạo ngẫu nhiên.
    * Mỗi cá thể trong $P_0$ là một cây cú pháp ngẫu nhiên $T_i$: các nút nội bộ (internal nodes) đại diện cho các toán tử hàm số (function operators), các nút lá (leaf nodes) đại diện cho đặc trưng đầu vào hoặc các hằng số tức thời (ephemeral constants).
  * **2. Đánh giá độ thích nghi (Fitness Evaluation):**
    * Với mỗi cá thể $T_i \in P_t$ tại thế hệ thứ $t$, tính sai số toàn phương trung bình (Mean Squared Error - MSE) trên tập huấn luyện làm điểm thích nghi thô $E(T_i)$.
    * Để hạn chế hiện tượng phình to kích thước (bloat), thành phần phạt độ phức tạp (parsimony penalty) được bổ sung, tạo thành điểm thích nghi hỗn hợp $\tilde{E}(T_i)$:
      $$\tilde{E}(T_i) = E(T_i) + \Omega \cdot \text{size}(T_i) \quad (4)$$
    * Trong đó $\text{size}(T_i)$ biểu thị số lượng nút trong cây cú pháp $T_i$, và $\Omega$ là hệ số tinh gọn (parsimony coefficient) điều chỉnh sự đánh đổi giữa độ chính xác (accuracy) và độ phức tạp (complexity).
  * **3. Các phép toán di truyền (Genetic Operations):**
    * Chọn lọc cá thể cha mẹ (parent selection) được thực hiện thông qua cơ chế chọn lọc giải đấu (tournament selection).
    * Các thế hệ con mới được sinh ra thông qua hai cơ chế chính:
      * Trao đổi cây con (Subtree Crossover): Với xác suất $p_{\text{crossover}}$ (hay $p_{\text{cx}}$), các cây con từ hai cá thể cha mẹ được tráo đổi cho nhau.
      * Đột biến (Mutation): Với phần xác suất còn lại, áp dụng đột biến điểm (point mutation), đột biến cây con (subtree mutation), hoặc tái sinh (reproduction) để duy trì tính đa dạng di truyền.
  * **4. Tiến hóa lặp (Iterative Evolution):**
    * Lặp lại bước 2 và bước 3 cho đến khi thỏa mãn các tiêu chí dừng (stopping criteria).
    * Cá thể tối ưu nhất $T^*$ từ quần thể cuối cùng được trích xuất làm quy tắc ký hiệu đạo xuất (derived symbolic rule).

* **Các mô hình áp dụng theo bản chất tác vụ học máy:**
  * Tác vụ hồi quy (regression tasks): Áp dụng mô hình `SymbolicRegressor`.
  * Tác vụ phân loại nhị phân (binary classification): Áp dụng mô hình `SymbolicClassifier`.

### A.2 Operator Set Configuration

* **Tập toán tử nguyên thủy gồm 14 toán tử và cơ chế bảo vệ (protection strategy):**
  * Định nghĩa tập hợp tinh tuyển gồm 14 toán tử nguyên thủy (primitive operators) nhằm cân bằng giữa năng lực biểu đạt (expressive power) và khả năng diễn giải (interpretability).
  * Tập toán tử bao gồm ba nhóm chức năng chính (threefold design rationale):
    * Toán tử số học cơ bản (`add`, `sub`, `mul`, `div`): Tạo bộ khung xương cốt lõi cho xấp xỉ hàm hữu tỉ (rational function approximation).
    * Hàm siêu việt (`sin`, `cos`, `tan`, `log`): Cho phép mô hình hóa các động lực tuần hoàn (periodic dynamics) và hàm mũ (exponential dynamics).
    * Toán tử từng đoạn (`max`, `min`, `abs`): Hỗ trợ biểu diễn logic dựa trên ngưỡng quyết định (threshold-based logic).
    * Bổ sung các toán tử đơn biến: Căn bậc hai (`sqrt`), nghịch đảo (`inv`), đổi dấu (`neg`).
  * Cơ chế bảo vệ số học (Protected Operations): Tất cả các toán tử được cấu hình bảo vệ nhằm trả về các giá trị an toàn mặc định (như $1$ hoặc $0$) khi gặp các trạng thái không xác định (như chia cho 0 hoặc logarit số không dương), bảo đảm mọi cây cú pháp $T$ đều là một hàm hợp lệ trên miền $\mathbb{R}^d$:
    * `add`: Toán tử 2 ngôi (arity 2), dạng $x + y$, không bảo vệ (None).
    * `sub`: Toán tử 2 ngôi (arity 2), dạng $x - y$, không bảo vệ (None).
    * `mul`: Toán tử 2 ngôi (arity 2), dạng $x \cdot y$, không bảo vệ (None).
    * `div`: Toán tử 2 ngôi (arity 2), dạng $x / y$, bảo vệ bằng cách trả về $1$ nếu $y = 0$.
    * `sqrt`: Toán tử 1 ngôi (arity 1), dạng $\sqrt{|x|}$, bảo vệ bằng cách lấy giá trị tuyệt đối của đầu vào ($|x|$).
    * `inv`: Toán tử 1 ngôi (arity 1), dạng $1 / x$, bảo vệ bằng cách trả về $0$ nếu $x = 0$.
    * `neg`: Toán tử 1 ngôi (arity 1), dạng $-x$, không bảo vệ (None).
    * `abs`: Toán tử 1 ngôi (arity 1), dạng $|x|$, không bảo vệ (None).
    * `max`: Toán tử 2 ngôi (arity 2), dạng $\max(x, y)$, không bảo vệ (None).
    * `min`: Toán tử 2 ngôi (arity 2), dạng $\min(x, y)$, không bảo vệ (None).
    * `sin`: Toán tử 1 ngôi (arity 1), dạng $\sin(x)$, không bảo vệ (None).
    * `cos`: Toán tử 1 ngôi (arity 1), dạng $\cos(x)$, không bảo vệ (None).
    * `tan`: Toán tử 1 ngôi (arity 1), dạng $\tan(x)$, không bảo vệ (None).
    * `log`: Toán tử 1 ngôi (arity 1), dạng $\ln |x|$, bảo vệ bằng cách trả về $0$ nếu $x = 0$.
  * **Bảng 5.** Tập toán tử hồi quy ký hiệu và các phép toán bảo vệ ổn định số học
    * <img src="assets/table_05_p12.png" alt="Bảng 5" />
    * **Bảng này chứng minh điều gì**
      * Các phép toán protected division, log, sqrt và inv tránh tràn số hoặc lỗi chia cho 0
    * **Từ đâu mà thấy được**
      * Cột Operator, Arity, Mathematical Definition và Protection Mechanism trong bảng

### A.3 Hyperparameter Configuration

* **Thiết lập siêu tham số cố định cho hồi quy ký hiệu:**
  * Tất cả các siêu tham số của hồi quy ký hiệu được cố định xuyên suốt toàn bộ các thí nghiệm để bảo đảm tính nhất quán và khả năng so sánh khách quan.
  * Cấu hình được thiết kế nhằm tối đa hóa phạm vi bao phủ không gian tìm kiếm (search coverage) trong khi vẫn duy trì tính khả thi về mặt tài nguyên và thời gian tính toán (computational feasibility).
  * Chi tiết cấu hình siêu tham số và cơ sở lý giải:
    * Kích thước quần thể ($P$ - Population Size): $20{,}000$, bảo đảm tính đa dạng di truyền trong không gian dữ liệu nhiều chiều (high-dimensional spaces).
    * Số thế hệ tối đa ($G_{\max}$ - Generations): $120$, giới hạn chặn trên cứng cho số vòng lặp tiến hóa.
    * Tiêu chí dừng sớm ($\tau$ - Stopping Criteria): $10^{-4}$, ngưỡng dừng sớm dựa trên sai số MSE khi mô hình đạt độ khớp mong muốn.
    * Kích thước giải đấu (Tournament Size): $100$, tạo áp lực chọn lọc từ trung bình đến cao (moderate-to-high selection pressure), thúc đẩy quá trình hội tụ nhanh chóng về các vùng không gian có độ thích nghi cao.
    * Xác suất trao đổi chéo ($p_{\text{cx}}$ - Crossover Probability): $0{,}9$, thúc đẩy việc tái tổ hợp mạnh mẽ giữa các biểu thức con thành công.
    * Hạt giống ngẫu nhiên (Random State): $42$, bảo đảm tính tái lập hoàn toàn (reproducibility) của kết quả.
  * **Bảng 6.** Cấu hình siêu tham số của giải thuật hồi quy ký hiệu gplearn
    * <img src="assets/table_06_p13.png" alt="Bảng 6" />
    * **Bảng này chứng minh điều gì**
      * Thiết lập tham số chặt chẽ về quần thể, thế hệ, xác suất đột biến và parsimony coefficient
    * **Từ đâu mà thấy được**
      * Bảng liệt kê Parameter (population size, generations, parsimony_coefficient) và Value tương ứng

### A.4 Regularization and Bloat Control

* **Thách thức hiện tượng phình to cây cú pháp (bloat control) trong GP:**
  * Bloat là thách thức phổ biến trong quy hoạch di truyền khi kích thước của các cây cú pháp $T$ tăng lên quá mức mà không cải thiện tương ứng độ thích nghi (fitness).
  * Tác hại của bloat: Dẫn đến hiện tượng quá khớp (overfitting) và làm suy giảm nghiêm trọng khả năng diễn giải minh bạch (interpretability) của các đặc trưng sinh ra.

* **Kiểm soát thông qua áp lực tinh gọn (parsimony pressure) và tối ưu hóa hệ số $\Omega$:**
  * Sử dụng hệ số phạt độ phức tạp $\Omega$ trong hàm thích nghi $\tilde{E}(T_i) = E(T_i) + \Omega \cdot \text{size}(T_i)$ để kìm hãm sự bùng nổ kích thước cây.
  * Giá trị tối ưu của $\Omega$ được xác định thông qua tìm kiếm lưới (grid search) trên tập ứng viên $\{0{,}005; 0{,}01; 0{,}02; 0{,}03; 0{,}04; 0{,}05\}$ trên một tập con kiểm định (validation subset).
  * Giá trị $\Omega$ giúp cực tiểu hóa sai số căn bậc hai trung bình (Root Mean Squared Error - RMSE) trên tập kiểm định được chọn cố định cho toàn bộ các thực nghiệm sau đó.
  * Tuân thủ nguyên lý Dao cạo Occam (Occam’s razor): Cơ chế chính quy hóa này ưu tiên các cấu trúc công thức đơn giản, súc tích khi hiệu năng dự đoán giữa các biểu thức là tương đương.
