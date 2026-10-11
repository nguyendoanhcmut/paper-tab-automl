## 4 Proposed Method: SymboLLM-FE

* **Khái niệm và động lực cốt lõi**: SymboLLM-FE là một mô hình lai (hybrid paradigm) kết hợp hiệp đồng giữa hồi quy biểu trưng (Symbolic Regression - SR) và mô hình ngôn ngữ lớn (Large Language Models - LLMs) nhằm giải quyết triệt để các hạn chế của các phương pháp kỹ nghệ đặc trưng tự động (Automated Feature Engineering - AutoFE) hiện hành:
  * **Thế mạnh của Hồi quy biểu trưng**: SR vượt trội trong việc khám phá hiệu quả các công thức toán học tường minh (explicit mathematical formulas), có chi phí tính toán nhẹ (computationally lightweight), đồng thời trực tiếp đáp ứng nhu cầu tạo ra các đặc trưng nâng cao hiệu năng mô hình.
  * **Thế mạnh bổ trợ của LLM**: LLM tận dụng tri thức sâu rộng để tinh chỉnh và tối ưu hóa các công thức biểu trưng ứng viên này. Bằng cách tích hợp các tiền nghiệm đặc thù miền (domain-specific priors), LLM biến đổi các công thức toán học trừu tượng, nâng cao tính minh bạch thông qua giải thích bằng ngôn ngữ tự nhiên, đồng thời bảo đảm sự phù hợp với logic nghiệp vụ (business logic).
  * **Cầu nối hiệu năng và khả năng diễn giải**: Khung tích hợp SymboLLM-FE thu hẹp hiệu quả khoảng cách giữa hiệu năng dự báo (efficacy) và khả năng diễn giải (interpretability).
  * Chi tiết toàn bộ quy trình của SymboLLM-FE được trực quan hóa trong Hình 2:
    * **Hình 2.** Tổng quan kiến trúc SymboLLM-FE qua hai giai đoạn xây dựng công thức và sinh đặc trưng
      * <img src="assets/fig_02_p5.png" alt="Hình 2" />
      * **Hình này chứng minh điều gì**
        * Quy trình khép kín từ xếp hạng Spearman, cửa sổ trượt, giải thuật di truyền gplearn đến tinh chỉnh LLM và mô hình hạ nguồn
      * **Từ đâu mà thấy được**
        * Luồng xử lý từ trái qua phải: Formula Construction by Symbolic Regression liên kết sang Feature Generation via LLMs
* **Giao thức phân chia tập dữ liệu (Dataset Split Protocol)**: SymboLLM-FE tuân thủ nghiêm ngặt giao thức huấn luyện theo từng nếp (fold-wise training protocol) trong khuôn khổ kiểm định chéo (cross-validation framework) nhằm ngăn ngừa rò rỉ dữ liệu (data leakage):
  * **Tập huấn luyện (Training Set)**: Được sử dụng độc quyền cho giai đoạn Xây dựng công thức bằng Hồi quy biểu trưng (Formula Construction by Symbolic Regression), hỗ trợ toàn bộ chuỗi xử lý từ tái sắp xếp đặc trưng dựa trên hệ số tương quan Spearman, sinh tập con đặc trưng theo cơ chế mở rộng - trượt cửa sổ, cho đến việc khớp các mô hình biểu trưng.
  * **Tập thẩm định (Validation Set)**: Đóng vai trò là môi trường phản hồi (feedback environment) cho giai đoạn Sinh đặc trưng thông qua LLM (Feature Generation via LLMs). Tập này hoàn toàn độc lập và cách ly khỏi giai đoạn xây dựng công thức SR, nhưng được tích cực sử dụng để tính toán điểm số thẩm định (validation score) nhằm dẫn dắt vòng lặp tổng hợp mã nguồn, khai phá quy tắc và tinh chỉnh đặc trưng của LLM. Ngoài ra, tập thẩm định chỉ được dùng cho việc tinh chỉnh siêu tham số (hyperparameter tuning).
  * **Tập kiểm thử (Test Set)**: Được bảo lưu duy nhất cho bước đánh giá cuối cùng của mô hình dự báo hạ nguồn (downstream predictor) trên tập đặc trưng đã hợp nhất ($C_{\text{final}}$) để đánh giá năng lực mô hình. Kiến trúc mô hình hạ nguồn và các tham số được cố định hoàn toàn, độc lập với quá trình đánh giá kiểm thử, bảo đảm không có bất kỳ thông tin nào từ pha thẩm định làm sai lệch kết quả đánh giá hiệu năng sau cùng.

### 4.1 Formula Construction by Symbolic Regression

* **Bài toán lấy mẫu tập con đặc trưng (Feature Set Sampling)**:
  * Cho tập đặc trưng ban đầu $C$ gồm $n$ đặc trưng, tổng số tập con đặc trưng không rỗng khả dĩ là $2^n - 1$.
  * Áp dụng hồi quy biểu trưng lên toàn bộ các tập con sẽ dẫn đến bùng nổ tổ hợp với độ phức tạp tính toán hàm mũ $\mathcal{O}(2^n)$, hoàn toàn bất khả thi trên thực tế.
  * Nhằm tối ưu hóa hiệu quả tính toán trong khi vẫn bảo toàn năng lực biểu diễn đặc trưng, SymboLLM-FE đề xuất chiến lược kết hợp đặc trưng dựa trên phân tích hệ số tương quan Spearman kết hợp cơ chế cửa sổ mở rộng - trượt (expanding-sliding window approach).
* **Định lượng độ quan trọng và tái sắp xếp đặc trưng theo tương quan Spearman**:
  * Đánh giá độ quan trọng của từng đặc trưng trong $C$ thông qua hệ số tương quan hạng Spearman $\phi_{c_i}$ với biến mục tiêu.
  * Ưu thế của tương quan Spearman: So với các chỉ số khác như tương quan Pearson, hệ số tương quan Spearman định lượng bền vững hơn các mối quan hệ phi tuyến đơn điệu giữa đặc trưng và biến mục tiêu, cung cấp phép đo chính xác hơn về độ quan trọng biên (marginal feature importance) của đặc trưng (được kiểm chứng tính tương quan thống kê qua hệ số Kendall's $\tau$ trong Phụ lục D).
  * Sắp xếp đơn điệu tăng dần (Monotonic Ascending Sorting): Các đặc trưng được sắp xếp lại theo thứ tự tăng dần của hệ số tương quan, tạo thành chuỗi đặc trưng có thứ tự $C' = (c'_1, c'_2, \dots, c'_n)$ thỏa mãn:
    $$\phi_{c'_1} \le \phi_{c'_2} \le \dots \le \phi_{c'_n}$$
    trong đó $\phi_{c'_i}$ biểu thị hệ số tương quan Spearman giữa đặc trưng $c'_i$ và biến mục tiêu.
* **Cơ chế Cửa sổ Mở rộng - Trượt động (Dynamic Expanding-Sliding Window Approach)**:
  * Nhằm duy trì chất lượng công thức đồng thời kiểm soát hiệu quả số lượng đặc trưng sinh ra, phương pháp tiếp cận khởi tạo kích thước cửa sổ tại $k = \lfloor n/2 \rfloor$ và vận hành qua hai pha cốt lõi:
    * **Pha mở rộng (Expanding Phase)**: Kích thước cửa sổ $k$ tăng dần từ $\lfloor n/2 \rfloor$ đến $n$ với bước nhảy đơn vị ($\Delta k = 1$).
    * **Pha trượt (Sliding Phase)**: Ứng với mỗi kích thước cửa sổ $k$ cố định, cửa sổ trượt sang phải theo từng bước đơn đặc trưng ($\Delta s = 1$) để tạo ra các tập con đặc trưng khác nhau. Ví dụ, khi $k = \lfloor n/2 \rfloor$, các tập con sinh ra lần lượt là $\{c'_1, \dots, c'_{\lfloor n/2 \rfloor}\}$, $\{c'_2, \dots, c'_{\lfloor n/2 \rfloor + 1}\}, \dots$
  * **Giảm thiểu độ phức tạp tính toán từ hàm mũ về bậc đa thức**:
    * Tổng số tập con đặc trưng ứng viên $S$ sinh ra từ phương pháp mở rộng - trượt bị chặn trên bởi tổng của một cấp số cộng:
      $$\sum_{k=\lfloor n/2 \rfloor}^{n} (n - k + 1) = \sum_{m=1}^{\lceil n/2 \rceil + 1} m = \begin{cases} \frac{(n + 2)(n + 4)}{8}, & \text{nếu } n \text{ chẵn} \\ \frac{(n + 3)(n + 5)}{8}, & \text{nếu } n \text{ lẻ} \end{cases} \quad (2)$$
    * Cơ chế này làm giảm tổng số tập con đặc trưng cần xem xét từ cấp số mũ $\mathcal{O}(2^n)$ xuống cấp số đa thức $\mathcal{O}(n^2)$, cắt giảm mạnh mẽ chi phí tính toán trong khi vẫn đảm bảo độ bao phủ các tổ hợp đặc trưng quan trọng nhất.
* **Sinh công thức toán học biểu trưng (Formula Generating)**:
  * Với mỗi tập con đặc trưng $S_i$ ($i \in [1, |S|]$) sinh ra từ cơ chế cửa sổ, một mô hình hồi quy biểu trưng độc lập (sử dụng giải thuật di truyền Genetic Programming qua thư viện `gplearn`) được huấn luyện để sinh ra một công thức toán học tường minh biểu diễn mối quan hệ từ $S_i$ đến biến mục tiêu, đóng vai trò là một đặc trưng mới (ví dụ dạng $\text{add}(\text{mul}(c_1, c_2), c_3)$).
  * Khuôn khổ giải thuật di truyền (Genetic Programming Framework):
    * Quần thể ban đầu gồm các cây cú pháp ngẫu nhiên $T_i$ với kích thước quần thể $P = 20{,}000$, số thế hệ $G_{\max} = 120$, áp lực chọn lọc qua đấu loại (tournament size = 100), xác suất lai ghép cây con $p_{\text{cx}} = 0.9$.
    * Tập 14 toán tử nguyên thủy được bảo vệ (protected operators) chống lỗi toán học: cộng (`add`), trừ (`sub`), nhân (`mul`), chia an toàn (`div`), căn bậc hai an toàn (`sqrt`), nghịch đảo an toàn (`inv`), phủ định (`neg`), giá trị tuyệt đối (`abs`), cực đại (`max`), cực tiểu (`min`), và các hàm lượng giác/siêu việt (`sin`, `cos`, `tan`, `log`).
  * Hàm độ thích nghi kết hợp hệ số tiết chế (Fitness Function with Parsimony Penalty):
    * Độ thích nghi thô $E(T_i)$ được đo bằng sai số toàn phương trung bình (MSE) trên tập huấn luyện.
    * Để ngăn ngừa hiện tượng phình to cây cú pháp (bloat) gây quá khớp và làm giảm khả năng diễn giải, hàm độ thích nghi tổng hợp $\tilde{E}(T_i)$ áp dụng hình phạt tiết chế (parsimony penalty) tuân theo nguyên lý dao cạo Occam:
      $$\tilde{E}(T_i) = E(T_i) + \Omega \cdot \text{size}(T_i) \quad (4)$$
      trong đó $\text{size}(T_i)$ biểu thị số lượng nút trong cây cú pháp $T_i$, và $\Omega$ là hệ số tiết chế (parsimony coefficient) kiểm soát sự cân bằng giữa độ chính xác dự báo và độ phức tạp biểu thức (được tìm kiếm lưới tối ưu trên tập $\{0.005, 0.01, 0.02, 0.03, 0.04, 0.05\}$).
  * Kho lưu trữ đặc trưng dạng công thức (Formula-based Feature Repository $R$):
    * Sau quá trình huấn luyện hệ thống, một kho lưu trữ đặc trưng $R$ được thiết lập gồm $|S|$ bộ ba:
      $$R = \{(S_i, P_f(S_i), \tau_i)\}_{i=1}^{|S|} \quad (3)$$
      trong đó mỗi bộ ba thành phần bao gồm:
      1. Tập con đặc trưng đầu vào $S_i$.
      2. Hiệu năng mô hình biểu trưng $P_f(S_i)$ của mô hình $f$ đã huấn luyện trên $S_i$ (ví dụ đo bằng MAE hoặc MSE).
      3. Công thức toán học biểu trưng $\tau_i$ biểu diễn ánh xạ từ $S_i$ sang biến mục tiêu.

### 4.2 Feature Generation via LLMs

* **Quy trình tinh chỉnh và sinh đặc trưng đa giai đoạn**: SymboLLM-FE triển khai chuỗi xử lý tinh chỉnh nhiều chặng kết hợp LLM và mô hình dự báo hạ nguồn dựa trên kho công thức $R$ để kiến tạo tập đặc trưng chất lượng cao.
* **Sinh mã nguồn định hướng bởi LLM (LLM-guided Code Generation)**:
  * Cấu trúc thông tin đầu vào (Prompt) cho LLM:
    * Chuyển đổi từng công thức toán học $\tau_i \in R$ thành mô tả tương ứng bằng ngôn ngữ tự nhiên.
    * Ghép nối cùng thông tin bối cảnh có cấu trúc của tập dữ liệu (tên các cột từ $X_0$ đến $X_{N-1}$, loại tác vụ học máy regression hoặc classification, thang đo đánh giá accuracy hoặc RMSE).
    * Bảng tri thức tiền nghiệm (Prior Knowledge) chứa các công thức biểu trưng rút ra cùng chỉ số sai số tuyệt đối trung bình (MAE) tương ứng của mô hình hồi quy biểu trưng trên tập kiểm tra nội bộ.
    * Lời nhắc định hướng sinh mã nguồn (code-generation prompt).
  * Cơ chế suy luận chuỗi tư duy (Chain-of-Thought - CoT Reasoning):
    * LLM phân tích toàn diện và sâu sắc các công thức toán học cùng mối quan hệ tương hỗ giữa các đặc trưng, tuyệt đối không chuyển đổi cơ học toàn bộ công thức mà chọn lọc các tổ hợp có ý nghĩa ngữ nghĩa.
    * LLM tự động sinh ra mã nguồn kỹ nghệ đặc trưng có thể thực thi trực tiếp bằng thư viện Python `pandas`.
  * Định dạng yêu cầu mã nguồn trong Prompt:
    * **Định dạng thêm cột mới**: Mỗi cột mới được tạo phải kèm theo khối chú thích giải thích rõ ràng gồm: tên đặc trưng (`# Feature name:`), lý do đề xuất (`# Reason:`), và mức độ hữu dụng đối với bài toán (`# Usefulness:`), tuân thủ quy ước đặt tên tăng dần ($X_{k+1}, X_{k+2}, \dots$).
    * **Định dạng loại bỏ cột dư thừa**: Mỗi cột bị loại bỏ phải có dòng giải thích nguyên nhân (`# Explanation:` vì sao cột đó dư thừa hoặc gây hại) trước khi gọi hàm loại bỏ `df.drop(columns=[...], inplace=True)`.
* **Thẩm định hiệu năng bằng Mô hình dự báo hạ nguồn (Downstream Predictor Performance Validation)**:
  * Mã nguồn sinh ra được thực thi để tạo ra tập đặc trưng tăng cường $C_{\text{new}}$ và làm giàu tập dữ liệu gốc $C$:
    $$C_{\text{final}} = C \oplus C_{\text{new}}$$
  * Huấn luyện mô hình dự báo hạ nguồn (chẳng hạn như TabPFN, LightGBM, CatBoost, XGBoost, hoặc MLP) trên tập đặc trưng mở rộng $C_{\text{final}}$ và ghi nhận điểm số hiệu năng thẩm định (Validation Score) thu được.
* **Vòng lặp tinh chỉnh đặc trưng lặp (Iterative Feature Refinement)**:
  * Điểm số hiệu năng thẩm định của mô hình dự báo, đi kèm danh sách các đặc trưng đã sử dụng và mã nguồn sinh tương ứng, được đưa ngược lại vào ngữ cảnh của LLM để thực hiện vòng lặp tối ưu hóa và tinh chỉnh đặc trưng.
  * Quá trình phản hồi - hiệu chỉnh này diễn ra lặp đi lặp lại cho đến khi mô hình dự báo hạ nguồn đạt được mức hiệu năng tương đối tối ưu trên tập đặc trưng mở rộng.
* **Cơ chế chọn lọc đặc trưng, khử dư thừa và triệt tiêu ảo giác**:
  * **Quản lý ngân sách đặc trưng (Feature Budget Management)**: Dựa trên phản hồi từ mô hình dự báo hạ nguồn, SymboLLM-FE chủ động cắt tỉa động các đặc trưng làm suy giảm hiệu năng thẩm định, tạo ra một tập đặc trưng tinh gọn, tránh được lời nguyền số chiều (curse of dimensionality) vốn là điểm yếu của các phương pháp AutoFE thông thường.
  * **Khử dư thừa và loại bỏ hiện tượng đa cộng tuyến (Redundancy Elimination)**:
    * Khuôn mẫu prompt áp đặt ràng buộc loại bỏ đặc trưng tường minh đi kèm lý do giải thích.
    * LLM đóng vai trò như một bộ lọc ngữ nghĩa (semantic filter) thông minh, nhận diện sự tương đương về mặt toán học giữa các công thức hồi quy biểu trưng và các đặc trưng ban đầu, nhờ đó loại trừ triệt để hiện tượng đa cộng tuyến (multicollinearity).
  * **Khống chế nhiễu và triệt tiêu ảo giác (Noise Suppression & Hallucination Elimination)**:
    * Hình phạt tiết chế (parsimony penalty) $\Omega \cdot \text{size}(T_i)$ ở giai đoạn hồi quy biểu trưng giúp loại bỏ các cấu trúc biểu thức rườm rà không cần thiết theo nguyên lý dao cạo Occam.
    * Việc giới hạn nghiêm ngặt các thao tác của LLM trong không gian con đã được kiểm chứng thống kê bởi các công thức biểu trưng (statistically validated subspace) giúp loại bỏ hoàn toàn hiện tượng sinh đặc trưng ảo giác vô căn cứ của LLM, bảo đảm tính bền vững (robustness) và độ cô đọng (compactness) của tập đặc trưng cuối cùng.
