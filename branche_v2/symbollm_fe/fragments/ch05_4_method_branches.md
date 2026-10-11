## 4 Method

- **Mô hình lai SymboLLM-FE**: SymboLLM-FE khắc phục các hạn chế của AutoFE hiện nay bằng cách kết hợp hiệp đồng giữa hồi quy ký hiệu (Symbolic Regression) và các mô hình ngôn ngữ lớn (Large Language Models - LLMs):
  - Hồi quy ký hiệu xuất sắc trong việc khám phá hiệu quả các công thức toán học tường minh (explicit mathematical formulas), vừa nhẹ về chi phí tính toán (computationally lightweight) vừa đáp ứng nhu cầu tạo ra các đặc trưng giúp nâng cao hiệu năng.
  - LLMs đóng vai trò bổ trợ bằng cách tận dụng tri thức sâu rộng để tinh chỉnh và tối ưu hóa các công thức ký hiệu ứng viên này.
  - Bằng cách đưa vào các tiên nghiệm đặc thù của miền (domain-specific priors), LLMs chuyển hóa các công thức toán học mờ đục (opaque mathematical formulas), đồng thời tăng cường khả năng diễn giải (interpretability) thông qua giải thích bằng ngôn ngữ tự nhiên và bảo đảm sự phù hợp với logic kinh doanh (business logic).
  - Mô hình lai này thu hẹp hiệu quả khoảng cách giữa tính hữu hiệu (efficacy) và khả năng diễn giải (interpretability).
  - **Hình 2.** Tổng quan kiến trúc SymboLLM-FE, bao gồm Xây dựng Công thức bằng Hồi quy Ký hiệu, Sinh Đặc trưng qua LLMs và mô hình dự đoán xuôi dòng
    - <img src="assets/fig_02_p5.png" alt="Hình 2" />
    - **Hình này chứng minh điều gì**
      - Quy trình hai giai đoạn kết hợp hồi quy ký hiệu và LLMs: Hồi quy ký hiệu trích xuất công thức toán học từ các tập con đặc trưng tạo bởi cửa sổ mở rộng - trượt; LLMs tinh chỉnh mã nguồn Python pandas và lặp tối ưu dựa trên điểm kiểm định của bộ dự đoán xuôi dòng.
    - **Từ đâu mà thấy được**
      - Sơ đồ gồm hai khối: khối trái thực hiện sắp xếp thứ tự đặc trưng Spearman, tạo tập con bằng cửa sổ Expanding và Sliding qua Symbolic Regression tạo Formulas; khối phải nhận Prompt/Background, dùng LLMs sinh Features, huấn luyện Predictor lấy Validation Score lặp tối ưu, cuối cùng Feature Merge và Predict ra Test Score.
- **Phân chia tập dữ liệu (Dataset Split)**: SymboLLM-FE tuân thủ nghiêm ngặt giao thức huấn luyện theo từng fold (fold-wise training protocol) trong khuôn khổ kiểm định chéo (cross-validation framework):
  - Tập huấn luyện (training set) chỉ được sử dụng duy nhất cho giai đoạn Xây dựng Công thức bằng Hồi quy Ký hiệu (Formula Construction by Symbolic Regression), hỗ trợ toàn bộ pipeline từ sắp xếp lại thứ tự đặc trưng dựa trên tương quan Spearman, tạo tập con bằng cửa sổ mở rộng - trượt cho đến khớp các mô hình ký hiệu.
  - Tập kiểm định (validation set) đóng vai trò là môi trường phản hồi (feedback environment) cho giai đoạn Sinh Đặc trưng qua LLMs (Feature Generation via LLMs):
    - Tập kiểm định được cách ly hoàn toàn khỏi quy trình hồi quy ký hiệu trước đó, nhưng được sử dụng tích cực để tính điểm kiểm định (validation scores) nhằm dẫn đường cho vòng lặp tổng hợp mã nguồn lặp (iterative code synthesis), khai phá quy tắc (rule mining) và tối ưu hóa đặc trưng của LLM.
    - Tập kiểm định chỉ được sử dụng duy nhất cho việc tinh chỉnh siêu tham số (hyperparameter tuning) nhằm ngăn chặn triệt để hiện tượng rò rỉ dữ liệu (data leakage).
  - Tập kiểm thử (test set) chỉ được giữ lại duy nhất cho bước đánh giá xuôi dòng cuối cùng trên tập đặc trưng đã hợp nhất (merged feature set) nhằm lượng giá hiệu năng mô hình:
    - Kiến trúc và tham số của mô hình xuôi dòng (downstream model architecture and parameters) được giữ cố định và độc lập với quy trình đánh giá trên tập kiểm thử, đảm bảo không có bất kỳ thông tin nào từ pha kiểm định vô tình ảnh hưởng đến đánh giá hiệu năng cuối cùng.

### 4.1 Formula Construction by Symbolic Regression

- **Quy trình tổng thể**: SymboLLM-FE khởi đầu bằng việc xây dựng nhiều tập con đặc trưng đầu vào thông qua hệ số tương quan Spearman (Spearman correlation) (De Winter et al., 2016) kết hợp phương pháp tiếp cận cửa sổ mở rộng - trượt (expanding-sliding window approach), sau đó áp dụng mô hình hồi quy ký hiệu riêng biệt lên từng tập con để suy dẫn các công thức toán học có khả năng diễn giải, nắm bắt các mối quan hệ có ý nghĩa với biến mục tiêu (target).
- **Lấy mẫu tập đặc trưng (Feature Set Sampling)**:
  - Với tập đặc trưng $C$ gồm $n$ đặc trưng, tổng số tập con đặc trưng phi rỗng là $2^n - 1$.
  - Việc áp dụng hồi quy ký hiệu lên mọi tập con sẽ dẫn đến độ phức tạp tính toán hàm mũ $\mathcal{O}(2^n)$, đòi hỏi chiến lược lấy mẫu nhằm tối ưu hiệu quả tính toán trong khi vẫn bảo toàn năng lực biểu diễn của đặc trưng.
  - Sắp xếp thứ tự đặc trưng bằng tương quan Spearman:
    - Đánh giá tầm quan trọng của các đặc trưng trong $C$ bằng phân tích hệ số tương quan Spearman, sau đó sắp xếp tăng đơn điệu (monotonic ascending sorting) theo hệ số tương quan để thu được chuỗi đặc trưng có thứ tự $C' = \{c'_1, c'_2, \dots, c'_n\}$ thỏa mãn:
      $$\phi_{c'_1} \le \phi_{c'_2} \le \dots \le \phi_{c'_n}$$
      trong đó $\phi_{c'_i}$ ký hiệu hệ số tương quan Spearman giữa đặc trưng $c'_i$ và biến mục tiêu.
    - Tương quan Spearman được chọn làm tiêu chí định lượng tầm quan trọng đặc trưng vì có khả năng định lượng bền vững hơn các phụ thuộc phi tuyến (nonlinear dependencies) giữa đặc trưng và mục tiêu so với tương quan Pearson, cung cấp phép đo chính xác hơn về tầm quan trọng biên của đặc trưng (marginal feature importance) (Cheng et al., 2025b; Phụ lục D kiểm chứng thực nghiệm tương quan thống kê giữa chỉ số này và các tiêu chí khác).
  - Phương pháp cửa sổ mở rộng - trượt động (Dynamic Expanding-Sliding Window):
    - Khởi tạo với kích thước cửa sổ ban đầu $k = \lfloor n/2 \rfloor$.
    - Pha mở rộng (Expanding Phase): Kích thước cửa sổ $k$ tăng dần từ $\lfloor n/2 \rfloor$ đến $n$ với bước nhảy đơn vị ($+1$).
    - Pha trượt (Sliding Phase): Với mỗi kích thước cửa sổ $k$ cố định, cửa sổ trượt sang phải với bước nhảy từng đặc trưng đơn lẻ để sinh ra các tập con đặc trưng khác nhau (ví dụ khi $k = \lfloor n/2 \rfloor$, các tập con sinh ra gồm $\{\{c'_1, \dots, c'_{\lfloor n/2 \rfloor}\}, \{c'_2, \dots, c'_{\lfloor n/2 \rfloor + 1}\}, \dots\}$).
    - Tổng số tập con đặc trưng đầu vào ứng viên $|S|$ được chặn trên bởi tổng cấp số cộng:
      $$\sum_{k=\lfloor n/2 \rfloor}^n (n - k + 1) = \sum_{m=1}^{\lceil n/2 \rceil + 1} m = \begin{cases} \frac{(n + 2)(n + 4)}{8}, & \text{nếu } n \text{ chẵn} \\ \frac{(n + 3)(n + 5)}{8}, & \text{nếu } n \text{ lẻ} \end{cases} \tag{2}$$
    - Phương trình (2) chứng minh phương pháp cửa sổ mở rộng - trượt giảm thiểu tổng số tập con đặc trưng từ độ phức tạp hàm mũ $\mathcal{O}(2^n)$ xuống độ phức tạp đa thức $\mathcal{O}(n^2)$.
- **Sinh công thức (Formula Generating)**:
  - Với mỗi tập con $S_i$ ($i \in [1, |S|]$) sinh ra từ phương pháp cửa sổ mở rộng - trượt, huấn luyện một mô hình hồi quy ký hiệu và sinh ra công thức biểu diễn (ví dụ có dạng $\text{add}(\text{mul}(c_1, c_2), c_3)$) từ $S_i$ đến mục tiêu làm đặc trưng mới (chi tiết về hồi quy ký hiệu được trình bày tại Phụ lục A).
  - Sau quá trình huấn luyện và xây dựng có hệ thống, thiết lập kho lưu trữ đặc trưng dựa trên công thức (formula-based feature repository) $\mathcal{R}$ gồm $|S|$ bộ ba:
    $$\mathcal{R} = \{(S_i, P_f(S_i), \tau_i)\}_{i=1}^{|S|} \tag{3}$$
    trong đó mỗi bộ ba gồm:
    1. Tập con đặc trưng đầu vào $S_i$.
    2. Hiệu năng hồi quy ký hiệu $P$ của mô hình ký hiệu $f$ đã huấn luyện trên $S_i$ (ký hiệu $P_f(S_i)$).
    3. Công thức toán học $\tau_i$ ánh xạ từ $S_i$ đến mục tiêu.

### 4.2 Feature Generation via LLMs

- **Quy trình tinh chỉnh đa giai đoạn**: SymboLLM-FE triển khai một pipeline tinh chỉnh đa giai đoạn (multi-stage refinement pipeline) thông qua LLMs và các mô hình dự đoán xuôi dòng (downstream predictors) dựa trên kho lưu trữ $\mathcal{R}$ để tạo ra các đặc trưng chất lượng cao.
- **Sinh mã nguồn định hướng bởi LLM (LLM-guided Code Generation)**:
  - Đầu vào cung cấp cho LLMs được xây dựng bằng cách chuyển đổi từng công thức $\tau \in \mathcal{R}$ thành mô tả ngôn ngữ tự nhiên tương ứng, nối ghép với thông tin bối cảnh tập dữ liệu có cấu trúc (structured dataset background information) và prompt sinh mã nguồn.
  - LLMs sinh mã nguồn kỹ thuật đặc trưng có thể thực thi trực tiếp dưới định dạng Python pandas thông qua cơ chế lập luận chuỗi suy nghĩ (Chain-of-Thought reasoning - CoT) (Wei et al., 2022).
- **Kiểm thực hiệu năng bộ dự đoán xuôi dòng (Downstream Predictor Performance Validation)**:
  - Mã nguồn được sinh ra được thực thi để tạo tập đặc trưng mở rộng $C_{\text{new}}$ và làm giàu tập dữ liệu gốc $C$:
    $$C_{\text{final}} = C \oplus C_{\text{new}}$$
  - Tiếp theo, một mô hình dự đoán xuôi dòng được huấn luyện trên $C_{\text{final}}$ để thu thập kết quả hiệu năng tương ứng.
- **Tinh chỉnh đặc trưng lặp (Iterative Feature Refinement)**:
  - Hiệu năng của mô hình dự đoán, cùng với các đặc trưng đã sử dụng và mã nguồn sinh tương ứng, được đưa ngược lại cho LLMs để phục vụ tối ưu hóa lặp và tinh chỉnh đặc trưng.
  - Vòng lặp phản hồi này tiếp diễn cho đến khi mô hình dự đoán đạt được mức hiệu năng tối ưu tương đối trên tập đặc trưng mở rộng.
- **Cơ chế kiểm soát đặc trưng và khử dư thừa nghiêm ngặt (Rigorous Feature Control and De-redundancy Mechanisms)**:
  - Quản lý ngân sách đặc trưng (Feature budget management): Tự động cắt tỉa động (dynamically prune) các đặc trưng làm suy giảm hiệu năng trên tập kiểm định thông qua phản hồi từ mô hình dự đoán xuôi dòng, tạo ra một tập đặc trưng tinh chỉnh cô đọng, tránh hiệu quả lời nguyền số chiều (curse of dimensionality) so với các phương pháp cơ sở.
  - Khử dư thừa (Redundancy elimination) thông qua các ràng buộc độc lập với prompt:
    - Bản mẫu prompt (template) bắt buộc thực thi thao tác loại bỏ đặc trưng tường minh có giải trình (explicit feature dropping with justification).
    - LLM đóng vai trò là bộ lọc ngữ nghĩa (semantic filter) để nhận diện tính tương đương toán học giữa các công thức hồi quy ký hiệu và các đặc trưng gốc, loại bỏ triệt để hiện tượng đa cộng tuyến (multicollinearity).
  - Triệt tiêu nhiễu và hạn chế quá khớp (Suppress noise and overfitting):
    - Áp đặt số hạng phạt độ phức tạp (parsimony penalty) theo nguyên lý Dao cạo Ockham (Occam's razor) ở giai đoạn hồi quy ký hiệu.
    - Giới hạn nghiêm ngặt các thao tác của LLM trong không gian con đã được xác thực thống kê (statistically validated subspace), qua đó loại bỏ hoàn toàn hiện tượng ảo giác (hallucination), bảo đảm tính vững chắc (robustness) và độ cô đọng (compactness) của tập đặc trưng cuối cùng.
