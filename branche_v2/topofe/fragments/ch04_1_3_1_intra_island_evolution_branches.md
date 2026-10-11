### 3.1 Intra-island Evolution

#### 3.1.1 Multi-island Decomposition

- Không gian chương trình đặc trưng $\mathcal{P}$ (feature program space) mang tính không đồng nhất (heterogeneous):
  - Các chương trình tự nhiên gom cụm thành các vùng mạch lạc về ngữ nghĩa tùy theo lớp toán tử được sử dụng, trong đó mỗi vùng mã hóa một thiên kiến quy nạp (inductive bias) riêng biệt về cách xây dựng tín hiệu dự đoán từ các đặc trưng thô.
- **Định nghĩa 1 (Họ biến đổi - Transformation Family)**: Họ biến đổi $\mathcal{P}_i \subseteq \mathcal{P}$ là tập con mạch lạc về mặt ngữ nghĩa gồm các chương trình đặc trưng cùng chia sẻ thiên kiến quy nạp về cách kiến tạo tín hiệu dự đoán từ đặc trưng thô, tức các chương trình áp dụng cùng một lớp phép toán nguyên thủy (primitive operations).
- Hệ thống xem xét 5 họ biến đổi kinh điển (canonical transformation families):
  - Tương tác số học (arithmetic interactions) $\mathcal{P}_1$: tích, tỉ số và hiệu (products, ratios, differences).
  - Tổng hợp thống kê (statistical aggregates) $\mathcal{P}_2$: trung bình theo nhóm, độ lệch chuẩn, số đếm và trung vị (group-level means, standard deviations, counts, medians).
  - Đặc trưng thời gian (temporal features) $\mathcal{P}_3$: độ trễ (lags), cửa sổ trượt (rolling windows) và trung bình động lũy thừa (exponential moving averages).
  - Mã hóa quan hệ (relational encodings) $\mathcal{P}_4$: đếm tần suất (frequency counts), mã hóa mục tiêu (target encodings) và biến đổi dựa trên thứ hạng (rank-based transforms).
  - Ánh xạ đơn biến phi tuyến (nonlinear univariate maps) $\mathcal{P}_5$: biến đổi logarit, hàm mũ, chia khoảng (binned) và đa thức (polynomial transformations).
- Các họ biến đổi tạo nên một phủ xấp xỉ (approximate cover) cho không gian tìm kiếm:
  - Các họ biến đổi có thể chồng lấn (tổng quát là $\mathcal{P}_i \cap \mathcal{P}_j \neq \emptyset$), song mỗi họ đại diện cho một vùng cấu trúc riêng biệt của $\mathcal{P}$.
  - Phân vùng có khả năng mở rộng cho các họ biến đổi bổ sung khi cần thiết.
  - Hợp các họ tạo thành một phủ xấp xỉ $\mathcal{P} \approx \bigcup_{i=1}^M \mathcal{P}_i$, phân rã không gian tìm kiếm nguyên khối thành $M$ không gian con được định kiểu ngữ nghĩa (semantically typed subspaces), cho phép áp dụng tìm kiếm chuyên biệt hóa.
- Quần thể tiến hóa đơn lẻ gặp hiện tượng bão hòa và kẹt vùng cục bộ:
  - Trong một quần thể tiến hóa đơn lẻ, các chương trình đạt điểm cao từ một họ thống trị sẽ nhanh chóng làm bão hòa bộ đệm trải nghiệm (experience buffer).
  - Sự bão hòa này giam hãm các đề xuất tiếp theo của LLM vào vùng lân cận của họ thống trị đó, khiến các họ trực giao (orthogonal families) vĩnh viễn không được khám phá.
  - TOPOFE giải quyết thách thức này thông qua phân rã đa đảo có cấu trúc (structured multi-island decomposition), phân bổ một phân quần thể chuyên biệt cho từng $\mathcal{P}_i$, giúp bảo toàn thiên kiến quy nạp riêng của từng họ và ngăn chặn việc một họ đơn lẻ độc chiếm ngân sách tìm kiếm.
- **Định nghĩa 2 (Đảo - Island)**: Đảo thứ $i$ tại thế hệ $t$ là một bộ bốn (tuple) $I_i^{(t)} = (\Pi_i^{(t)}, \mathcal{A}_i, \mathcal{H}_i^{(t)}, \rho_i^{(t)})$:
  - $\Pi_i^{(t)} \subset \mathcal{P}_i$: quần thể hiện tại gồm tối đa $n_{\max}$ chương trình đặc trưng, được xếp hạng theo độ thích nghi $\hat{\Phi}$ (fitness).
  - $\mathcal{A}_i \subset \mathcal{P}_i$: kho lưu trữ dài hạn (long-term archive) lưu giữ các chương trình tinh hoa (elite programs) do đảo $i$ phát hiện.
  - $\mathcal{H}_i^{(t)}$: lịch sử chấp nhận/từ chối (accept/reject history) dùng để điều chỉnh prompt đột biến.
  - $\rho_i^{(t)} \in \mathbb{R}^s$: vector bộ nhớ prompt (prompt-memory vector) mã hóa tín hiệu cô đọng dạng "ưu tiên/tránh" ("prefer/avoid") suy xuất từ $\mathcal{H}_i^{(t)}$.
- Bốn thành phần cùng duy trì toàn bộ trạng thái tìm kiếm của đảo:
  - $\Pi_i^{(t)}$ dẫn dắt quá trình tìm kiếm cục bộ (local search).
  - $\mathcal{A}_i^{(t)}$ tích lũy các phát hiện tốt nhất và đóng vai trò làm tập mẫu minh họa ngữ cảnh (in-context demonstration pool) cho các đề xuất của LLM.
  - $\mathcal{H}_i^{(t)}$ cung cấp tín hiệu thô cho việc thích ứng prompt (prompt adaptation).
  - $\rho_i^{(t)}$ chuyển hóa tín hiệu đó thành chỉ dẫn bằng ngôn ngữ tự nhiên được đưa vào mọi lệnh gọi LLM.

#### 3.1.2 LLM-guided Intra-island Evolution (Specialized Exploration)

- Tiến hóa độc lập trong từng đảo tại mỗi thế hệ $t$:
  - Đảo $i$ tiến hóa quần thể độc lập thông qua 2 toán tử có LLM định hướng (LLM-guided operators), cả hai đều phụ thuộc vào ngữ cảnh siêu dữ liệu $\mathcal{M}$ (metadata context) của đảo và vector bộ nhớ prompt $\rho_i^{(t)}$.
- Hai toán tử tiến hóa định hướng bởi LLM:
  - **Đột biến (Mutation)**: Lấy mẫu một chương trình cha đơn lẻ $p \sim \Pi_i^{(t)}$ với xác suất tỉ lệ thuận với độ thích nghi $\hat{\Phi}(p)$ và prompt LLM sinh ra chương trình biến đổi $p' \in \mathcal{P}_i$ cải thiện so với $p$ đồng thời tuân thủ các tín hiệu mã hóa trong $\rho_i^{(t)}$.
  - **Lai ghép (Crossover)**: Lấy mẫu hai chương trình cha $(p_a, p_b) \sim \Pi_i^{(t)}$ và đưa vào làm mẫu minh họa trong ngữ cảnh (in-context demonstrations); LLM sau đó được prompt để tổng hợp một chương trình con $p' \in \mathcal{P}_i$ kết hợp các yếu tố cấu thành từ cả hai cha mẹ.
- Quy trình kiểm định và đánh giá độ thích nghi thống nhất (unified validation and fitness pipeline):
  - Mỗi ứng viên $p'$ được kiểm tra tính hợp lệ cú pháp (syntactic validity) và tính chấp nhận được về ngữ nghĩa (semantic admissibility) dưới ngữ cảnh $\mathcal{M}$.
  - Ứng viên sau đó được đánh giá qua oracle $\hat{\Phi}$.
  - Quần thể $\Pi_i^{(t+1)}$ giữ lại top-$n_{\max}$ chương trình có độ thích nghi cao nhất.
  - Kho lưu trữ $\mathcal{A}_i^{(t)}$ và vector bộ nhớ $\rho_i^{(t)}$ được cập nhật theo các quy tắc xác định trong §3.2.

#### 3.1.3 Global Objective

- Mục tiêu toàn cục tập hợp tập đặc trưng cuối cùng bằng cách gom các chương trình tinh hoa từ tất cả các đảo:
  $$S^* = \arg \max_{S \subseteq \bigcup_i \mathcal{A}_i} \hat{\Phi}(S), \quad \text{s.t. } |S| \le d'_{\max}, \quad \sum_{i=1}^K |\Pi_i^{(t)}| \le B \quad (7)$$
  trong đó $B$ là ngân sách đánh giá tổng cộng (total evaluation budget).
- Yêu cầu tín hiệu dự đoán không dư thừa (non-redundant predictive signal):
  - Mỗi chương trình được giữ lại trong tập nghiệm $S^*$ đều phải đóng góp tín hiệu dự đoán không dư thừa:
    $$\hat{\Phi}(\{p\} \mid S^* \setminus \{p\}) > 0 \quad \forall p \in S^*$$
