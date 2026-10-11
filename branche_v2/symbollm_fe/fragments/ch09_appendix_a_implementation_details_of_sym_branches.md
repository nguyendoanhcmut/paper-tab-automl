## Appendix A Implementation Details of Symbolic Regression

- Phụ lục này cung cấp đặc tả toàn diện về symbolic regression (hồi quy ký hiệu) được sử dụng trong framework SymboLLM-FE.
- SymboLLM-FE sử dụng thư viện `gplearn` (phiên bản v0.4.1)*, thư viện hiện thực hóa mô hình Genetic Programming (quy hoạch di truyền - GP).
  - *https://github.com/trevorstephens/gplearn
- Symbolic regression được thiết kế nhằm khám phá các biểu thức toán học có khả năng diễn giải (interpretable mathematical expressions) bằng cách tiến hóa một quần thể các cây cú pháp (syntax trees), ký hiệu là $T$, thông qua các cơ chế lấy cảm hứng từ chọn lọc tự nhiên (natural selection).

### A.1 Algorithmic Framework

- Mục tiêu cốt lõi của symbolic regression là tìm kiếm trong không gian các hàm số toán học một biểu thức $T^*$ giúp tối thiểu hóa sai số dự đoán trên dữ liệu huấn luyện.
  - Cho $X_{\text{train}} \in \mathbb{R}^{N \times d}$ là ma trận đặc trưng (feature matrix) và $y_{\text{train}} \in \mathbb{R}^N$ là vector mục tiêu (target vector) cho một tập con xác định.
- Quá trình Genetic Programming diễn ra thông qua 4 giai đoạn lặp (four iterative phases):
  - **1. Khởi tạo quần thể (Population Initialization)**: Một quần thể ban đầu $P_0$ có kích thước $P$ được tạo ra. Mỗi cá thể trong $P_0$ là một cây cú pháp ngẫu nhiên $T_i$, trong đó các nút nội bộ (internal nodes) đại diện cho các toán tử hàm (function operators) và các nút lá (leaf nodes) đại diện cho các đặc trưng đầu vào (input features) hoặc các hằng số tạm thời (ephemeral constants).
  - **2. Đánh giá độ thích nghi (Fitness Evaluation)**: Đối với mỗi cá thể $T_i \in P_t$ tại thế hệ $t$, tính toán sai số bình phương trung bình MSE trên tập huấn luyện làm điểm số thích nghi thô $E(T_i)$. Để giảm thiểu hiện tượng phình to cây (bloat), một hình phạt tinh gọn (parsimony penalty) được bổ sung, tạo ra điểm thích nghi tổng hợp $\tilde{E}(T_i)$:
    $$\tilde{E}(T_i) = E(T_i) + \Omega \cdot \text{size}(T_i) \quad (4)$$
    trong đó $\text{size}(T_i)$ biểu thị số lượng nút trong cây cú pháp $T_i$, và $\Omega$ là hệ số tinh gọn (parsimony coefficient) kiểm soát sự đánh đổi giữa độ chính xác và độ phức tạp.
  - **3. Các phép toán di truyền (Genetic Operations)**: Các cá thể cha mẹ được lựa chọn thông qua cơ chế chọn lọc giải đấu (tournament selection). Các cá thể con mới được sinh ra thông qua:
    - *Lai ghép cây con (Subtree Crossover)*: Với xác suất $p_{\text{crossover}}$, các cây con từ hai cá thể cha mẹ được hoán đổi cho nhau.
    - *Đột biến (Mutation)*: Với xác suất còn lại, áp dụng đột biến điểm (point mutation), đột biến cây con (subtree mutation), hoặc tái tạo (reproduction) để tạo sự đa dạng.
  - **4. Tiến hóa lặp (Iterative Evolution)**: Các bước 2 và 3 được lặp lại cho đến khi thỏa mãn các tiêu chí dừng (stopping criteria). Cá thể tốt nhất $T^*$ từ quần thể cuối cùng được trả về làm quy tắc ký hiệu phái sinh (derived symbolic rule).
- Bộ ước lượng cho từng loại tác vụ học máy:
  - Đối với các tác vụ hồi quy (regression tasks), framework sử dụng `SymbolicRegressor`.
  - Đối với các tác vụ phân loại nhị phân (binary classification), framework sử dụng `SymbolicClassifier`.

### A.2 Operator Set Configuration

- Để cân bằng giữa năng lực biểu diễn (expressive power) và tính khả giải (interpretability), nghiên cứu định nghĩa một tập hợp chọn lọc gồm 14 toán tử nguyên thủy (primitive operators).
  - Tập hợp này bao gồm các phép toán số học (arithmetic), hàm siêu việt (transcendental), và hàm phi tuyến từng đoạn (piecewise nonlinear).
  - Bảng 5 (Table 5) chi tiết hóa danh mục 14 toán tử và chiến lược bảo vệ an toàn tương ứng.
- Danh mục 14 toán tử nguyên thủy theo Table 5 (Symbolic regression operator set. Protected operations ensure numerical stability across the domain):

| Operator | Arity | Mathematical Form | Protection Strategy |
| :--- | :--- | :--- | :--- |
| `add` | 2 | $x + y$ | None |
| `sub` | 2 | $x - y$ | None |
| `mul` | 2 | $x \cdot y$ | None |
| `div` | 2 | $x / y$ | Returns 1 if $y = 0$ |
| `sqrt` | 1 | $\sqrt{\|x\|}$ | Absolute value input |
| `inv` | 1 | $1 / x$ | Returns 0 if $x = 0$ |
| `neg` | 1 | $-x$ | None |
| `abs` | 1 | $\|x\|$ | None |
| `max` | 2 | $\max(x, y)$ | None |
| `min` | 2 | $\min(x, y)$ | None |
| `sin` | 1 | $\sin(x)$ | None |
| `cos` | 1 | $\cos(x)$ | None |
| `tan` | 1 | $\tan(x)$ | None |
| `log` | 1 | $\ln \|x\|$ | Returns 0 if $x = 0$ |

- Cơ sở thiết kế (design rationale) của các toán tử nguyên thủy bao gồm 3 khía cạnh:
  - (i) Các toán tử số học cơ bản (`add`, `sub`, `mul`, `div`) đóng vai trò là khung xương cho xấp xỉ hàm hữu tỷ (rational function approximation).
  - (ii) Các hàm siêu việt (`sin`, `cos`, `tan`, `log`) cho phép mô hình hóa các động lực tuần hoàn và hàm mũ (periodic and exponential dynamics).
  - (iii) Các toán tử từng đoạn (`max`, `min`, `abs`) cho phép thiết lập logic dựa trên ngưỡng (threshold-based logic).
- Chiến lược bảo vệ điểm kỳ dị (Protection Strategy):
  - Quan trọng là tất cả các toán tử đều được bảo vệ (protected), nghĩa là chúng trả về các giá trị mặc định an toàn (ví dụ: 1 hoặc 0) khi gặp các trạng thái không xác định (chẳng hạn phép chia cho 0 hoặc logarit của 0).
  - Cơ chế này đảm bảo mọi cây cú pháp $T$ đều là một hàm hợp lệ xác định trên $\mathbb{R}^d$.

### A.3 Hyperparameter Configuration

- Các siêu tham số cho symbolic regression được cố định trên tất cả các thử nghiệm nhằm đảm bảo tính nhất quán.
  - Cấu hình này được tóm tắt trong Bảng 6 (Table 6), được lựa chọn nhằm tối đa hóa phạm vi bao phủ tìm kiếm trong khi vẫn duy trì tính khả thi về mặt tính toán.
- Cấu hình siêu tham số thực nghiệm theo Table 6 (Hyperparameter configuration for the symbolic regression):

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| Population Size ($P$) | 20,000 | Ensures genetic diversity in high-dimensional spaces. |
| Generations ($G_{\max}$) | 120 | Hard upper bound on evolution steps. |
| Stopping Criteria ($\tau$) | $10^{-4}$ | Early stopping threshold for MSE. |
| Tournament Size | 100 | Moderate-to-high selection pressure. |
| Crossover Probability ($p_{\text{cx}}$) | 0.9 | Promotes recombination of successful sub-expressions. |
| Random State | 42 | Ensures reproducibility. |

- Phân tích hiệu ứng của các tham số:
  - Quy mô quần thể lớn ($P = 20, 000$, tức 20,000) kết hợp với xác suất lai ghép cao ($p_{\text{cx}} = 0.9$) tạo điều kiện thuận lợi cho việc khám phá sâu rộng không gian nghiệm.
  - Kích thước giải đấu (tournament size) bằng 100 áp đặt áp lực chọn lọc mạnh (strong selection pressure), thúc đẩy quá trình hội tụ nhanh chóng về phía các vùng có độ thích nghi cao.

### A.4 Regularization and Bloat Control

- Hiện tượng phình to cây cú pháp (bloat) là thách thức phổ biến trong GP:
  - Kích thước của các cây cú pháp $T$ có xu hướng gia tăng quá mức mà không đem lại sự cải thiện tương ứng về độ thích nghi (fitness), dẫn đến quá khớp (overfitting) và làm giảm tính khả giải.
- Phương pháp kiểm soát phình to (Bloat control):
  - Thách thức này được giải quyết thông qua áp lực tinh gọn (parsimony pressure), chịu sự chi phối của hệ số $\Omega$ trong Eq. (1) [công thức composite fitness (4)].
- Quy trình tối ưu hóa hệ số $\Omega$:
  - Giá trị tối ưu cho $\Omega$ được xác định thông qua tìm kiếm lưới (grid search) trên tập hợp ứng viên $\{0.005, 0.01, 0.02, 0.03, 0.04, 0.05\}$ trên một tập con kiểm định (validation subset).
  - Giá trị giúp tối thiểu hóa căn bậc hai sai số bình phương trung bình (Root Mean Squared Error - RMSE) được chọn cho tất cả các thử nghiệm tiếp theo.
- Ý nghĩa phương pháp luận:
  - Cơ chế điều chuẩn này đảm bảo biểu thức tiến hóa $T^*$ tuân thủ nguyên lý dao cạo Occam (Occam’s razor), ưu tiên các cấu trúc đơn giản hơn khi hiệu năng dự đoán là tương đương.
