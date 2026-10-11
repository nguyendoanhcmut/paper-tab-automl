### 3.1 Intra-island Evolution

#### 3.1.1 Multi-island Decomposition

* **Tính không đồng nhất của không gian chương trình đặc trưng $\mathcal{P}$ (heterogeneity of feature program space):**
  * Không gian chương trình đặc trưng $\mathcal{P}$ không đồng nhất (not homogeneous).
  * Các chương trình cụm lại một cách tự nhiên thành các vùng mạch lạc về mặt ngữ nghĩa (semantically coherent regions) dựa theo lớp toán tử (class of operations) mà chúng áp dụng.
  * Mỗi vùng mã hóa một thiên kiến quy nạp (inductive bias) riêng biệt về cách thức tín hiệu dự đoán (predictive signal) được kiến tạo từ các đặc trưng thô (raw features).
* **Định nghĩa 1 — Họ biến đổi (Definition 1: Transformation Family):**
  * Một họ biến đổi (transformation family) $\mathcal{P}_i \subseteq \mathcal{P}$ là một tập con mạch lạc về ngữ nghĩa gồm các chương trình đặc trưng cùng chia sẻ một thiên kiến quy nạp về cách kiến tạo tín hiệu dự đoán từ các đặc trưng thô, tức là các chương trình áp dụng cùng một lớp toán tử nguyên thủy (primitive operations).
* **Năm họ biến đổi chuẩn tắc (five canonical transformation families):**
  * Tương tác số học (arithmetic interactions) $\mathcal{P}_1$: bao gồm các phép nhân (products), tỷ số (ratios), và hiệu (differences).
  * Tập hợp thống kê (statistical aggregates) $\mathcal{P}_2$: bao gồm trung bình mức nhóm (group-level means), độ lệch chuẩn (standard deviations), số lượng đếm (counts), và trung vị (medians).
  * Đặc trưng thời gian (temporal features) $\mathcal{P}_3$: bao gồm các độ trễ (lags), cửa sổ trượt (rolling windows), và trung bình động lũy thừa (exponential moving averages).
  * Mã hóa quan hệ (relational encodings) $\mathcal{P}_4$: bao gồm đếm tần suất (frequency counts), mã hóa mục tiêu (target encodings), và các phép biến đổi dựa trên thứ hạng (rank-based transforms).
  * Ánh xạ đơn biến phi tuyến (nonlinear univariate maps) $\mathcal{P}_5$: bao gồm các phép biến đổi logarit (logarithmic), hàm mũ (exponential), phân nhóm/rời rạc hóa (binned), và đa thức (polynomial transformations).
* **Mối quan hệ giao thoa và sự phân tách của các họ biến đổi:**
  * Các họ biến đổi có thể giao thoa lẫn nhau (tức là $\mathcal{P}_i \cap \mathcal{P}_j \neq \emptyset$ nói chung), nhưng mỗi họ đại diện cho một vùng phân biệt về mặt cấu trúc trong $\mathcal{P}$.
  * Phép phân chia này có thể mở rộng (extensible) cho các họ biến đổi bổ sung khi cần thiết.
  * Cùng nhau, các họ biến đổi tạo thành một phủ xấp xỉ (approximate cover):
    $$\mathcal{P} \approx \bigcup_{i=1}^M \mathcal{P}_i$$
    qua đó phân rã không gian tìm kiếm đơn khối (monolithic search space) thành $M$ không gian con được định kiểu ngữ nghĩa (semantically typed subspaces), mỗi không gian con thích ứng cho việc tìm kiếm chuyên biệt (specialized search).
* **Hạn chế của quần thể tiến hóa đơn lẻ và giải pháp phân tách đa đảo của TOPOFE:**
  * Trong một quần thể tiến hóa đơn lẻ (single evolutionary population), các chương trình đạt điểm cao từ một họ thống trị sẽ nhanh chóng làm bão hòa bộ đệm kinh nghiệm (experience buffer).
  * Sự bão hòa này giam cầm các đề xuất tiếp theo của LLM vào vùng lân cận của họ thống trị đó, khiến các họ trực giao (orthogonal families) vĩnh viễn không được khám phá.
  * TOPOFE giải quyết vấn đề này thông qua phân tách đa đảo có cấu trúc (structured multi-island decomposition), phân bổ một quần thể con chuyên biệt (dedicated subpopulation) cho từng $\mathcal{P}_i$, giúp bảo toàn các thiên kiến quy nạp đặc thù của từng họ và ngăn chặn bất kỳ họ đơn lẻ nào độc chiếm ngân sách tìm kiếm (search budget).
* **Định nghĩa 2 — Đảo tiến hóa (Definition 2: Island):**
  * Đảo thứ $i$ tại thế hệ $t$ là một bộ giá trị (tuple):
    $$I_i^{(t)} = (\Pi_i^{(t)}, \mathcal{A}_i, \mathcal{H}_i^{(t)}, \rho_i^{(t)})$$
    trong đó:
    * (i) $\Pi_i^{(t)} \subset \mathcal{P}_i$ là quần thể hiện tại (current population) gồm tối đa $n_{\max}$ chương trình đặc trưng, được xếp hạng theo độ thích nghi (fitness) $\hat{\Phi}$.
    * (ii) $\mathcal{A}_i \subset \mathcal{P}_i$ là kho lưu trữ tinh hoa dài hạn (long-term archive of elite programs) được phát hiện bởi đảo $i$.
    * (iii) $\mathcal{H}_i^{(t)}$ là lịch sử chấp nhận/từ chối (accept/reject history) được dùng để thích ứng câu nhắc đột biến (mutation prompt).
    * (iv) $\rho_i^{(t)} \in \mathbb{R}^s$ là một vector bộ nhớ câu nhắc (prompt-memory vector) mã hóa tín hiệu cô đọng dạng "ưu tiên/tránh né" ("prefer/avoid") bắt nguồn từ $\mathcal{H}_i^{(t)}$.
* **Vai trò của bốn thành phần trong việc duy trì trạng thái tìm kiếm hoàn chỉnh của đảo:**
  * $\Pi_i^{(t)}$ dẫn dắt việc tìm kiếm cục bộ (local search).
  * $\mathcal{A}_i^{(t)}$ tích lũy những phát hiện tốt nhất và đóng vai trò làm nhóm mẫu thị phạm theo ngữ cảnh (in-context demonstration pool) cho các đề xuất của LLM.
  * $\mathcal{H}_i^{(t)}$ cung cấp tín hiệu thô (raw signal) cho quá trình thích ứng câu nhắc (prompt adaptation).
  * $\rho_i^{(t)}$ chuyển dịch tín hiệu đó thành hướng dẫn bằng ngôn ngữ tự nhiên (natural-language guidance) được chèn vào mỗi lượt gọi LLM.

#### 3.1.2 LLM-guided Intra-island Evolution (Specialized Exploration)

* **Quy trình tiến hóa độc lập tại mỗi thế hệ $t$:**
  * Tại mỗi thế hệ $t$, đảo $i$ tiến hóa quần thể của mình một cách độc lập thông qua hai toán tử do LLM dẫn dắt, cả hai đều phụ thuộc có điều kiện vào ngữ cảnh siêu dữ liệu $\mathcal{M}$ (metadata context) của đảo và bộ nhớ câu nhắc $\rho_i^{(t)}$:
* **Toán tử đột biến (Mutation operator):**
  * Lấy mẫu một chương trình cha mẹ đơn lẻ $p \sim \Pi_i^{(t)}$ với xác suất tỷ lệ thuận với độ thích nghi $\hat{\Phi}(p)$.
  * Nhắc (prompt) LLM tạo ra một chương trình đã biến đổi $p' \in \mathcal{P}_i$ nhằm cải thiện dựa trên $p$ đồng thời tuân thủ các tín hiệu được mã hóa trong $\rho_i^{(t)}$.
* **Toán tử lai ghép (Crossover operator):**
  * Lấy mẫu hai chương trình cha mẹ $(p_a, p_b) \sim \Pi_i^{(t)}$ và trình bày chúng dưới dạng các mẫu thị phạm theo ngữ cảnh (in-context demonstrations).
  * LLM sau đó được nhắc để tổng hợp một chương trình con $p' \in \mathcal{P}_i$ kết hợp các yếu tố cấu thành (compositional elements) từ cả hai chương trình cha mẹ.
* **Quy trình kiểm định và đánh giá độ thích nghi thống nhất (unified validation and fitness pipeline):**
  * Cả hai toán tử đều đi qua một quy trình kiểm định và thích ứng thống nhất: mỗi ứng viên $p'$ được kiểm tra tính hợp lệ cú pháp (syntactic validity) và khả năng chấp nhận ngữ nghĩa (semantic admissibility) dưới $\mathcal{M}$.
  * Sau đó ứng viên được đánh giá thông qua hàm oracle $\hat{\Phi}$.
  * Quần thể $\Pi_i^{(t+1)}$ giữ lại top-$n_{\max}$ chương trình có độ thích nghi cao nhất.
  * Kho lưu trữ tinh hoa $\mathcal{A}_i^{(t)}$ và bộ nhớ câu nhắc $\rho_i^{(t)}$ được cập nhật theo các quy tắc xác định trong mục §3.2.

#### 3.1.3 Global Objective

* **Tổng hợp tập đặc trưng cuối cùng từ tinh hoa của tất cả các đảo:**
  * Hệ thống đa đảo tập hợp tập đặc trưng cuối cùng bằng cách gộp (pooling) các chương trình tinh hoa từ tất cả các đảo:
    $$S^* = \arg\max_{S \subseteq \bigcup_{i} \mathcal{A}_i} \hat{\Phi}(S), \quad (7)$$
    thỏa mãn các điều kiện ràng buộc:
    $$|S| \le d'_{\max}, \quad \sum_{i=1}^K |\Pi_i^{(t)}| \le B,$$
    trong đó:
    * $B$ là tổng ngân sách đánh giá (total evaluation budget).
    * $d'_{\max}$ là số lượng đặc trưng tối đa được chọn.
    * $K$ là tổng số đảo (tương ứng với số lượng họ biến đổi).
* **Yêu cầu đóng góp tín hiệu dự đoán không dư thừa (non-redundant predictive signal):**
  * Mỗi chương trình $p$ được giữ lại trong tập đặc trưng tối ưu $S^*$ bắt buộc phải đóng góp tín hiệu dự đoán không dư thừa:
    $$\hat{\Phi}(\{p\} \mid S^* \setminus \{p\}) > 0, \quad \forall p \in S^*.$$
