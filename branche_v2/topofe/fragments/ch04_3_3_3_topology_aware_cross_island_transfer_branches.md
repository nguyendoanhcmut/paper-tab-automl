### 3.3 Topology-Aware Cross-Island Transfer

* Phân rã đa đảo (multi-island decomposition) ngăn ngừa sự bão hòa nội bộ họ biến đổi (within-family saturation), nhưng không thể tự mình khám phá các đặc trưng đòi hỏi sự kết hợp đồng thời các toán tử từ nhiều họ khác nhau:
  * Ví dụ đặc trưng $\frac{\text{rolling\_mean}(\text{sales}, 7)}{\text{lag}(\text{sales}, 3)}$ kết hợp toán tử chuỗi thời gian ($\mathcal{P}_3$) với toán tử số học ($\mathcal{P}_1$); không một họ đơn lẻ nào có thể tự sinh ra đặc trưng này.
  * Cơ chế chuyển giao tri thức xuyên đảo nhận biết topo (topology-aware cross-island transfer) được đề xuất nhằm phát hiện có hệ thống các tổ hợp liên họ (cross-family compositions) như vậy, xoay quanh ba câu hỏi cốt lõi: khi nào chuyển giao (phát hiện bão hòa), chuyển giao tới đâu / nhận từ đâu (lựa chọn đảo tiền thân), và chuyển giao cái gì (tổng hợp lai chéo đảo).
* Định nghĩa đồ thị topo (Definition 3 - Topology Graph):
  * Đồ thị topo $G(t) = (V, E, W(t))$ là một đồ thị có hướng có trọng số (directed weighted graph).
  * $V$ là tập hợp các đảo ($|V| = M$, tương ứng với $M$ họ biến đổi).
  * $E$ là tập hợp các cạnh chuyển giao có hướng giữa các đảo.
  * Trọng số $w_{j \to i}^{(t)} \in W(t)$ mã hóa độ hữu dụng quan sát được từ thực nghiệm (empirically observed utility) khi chuyển giao tri thức từ đảo $j$ sang đảo $i$ tính đến thế hệ $t$.
* Khởi tạo và cập nhật trọng số cạnh đồ thị topo:
  * Trọng số cạnh được khởi tạo đồng đều:
    $$w_{j \to i}^{(0)} = \frac{1}{M - 1} \quad \forall j \neq i$$
  * Trọng số được cập nhật trực tuyến (online update) sau mỗi sự kiện chuyển giao thông qua trung bình động hàm mũ (exponential moving average - EMA):
    $$w_{j \to i}^{(t+1)} = (1 - \alpha) w_{j \to i}^{(t)} + \alpha \Delta_{\text{cross}}^{(j \to i)}(t)$$
    trong đó $\alpha \in (0, 1)$ là hệ số suy giảm (decay coefficient), và $\Delta_{\text{cross}}^{(j \to i)}(t)$ là mức tăng độ thích nghi quan sát được (observed fitness gain) từ quá trình chuyển giao.
  * Cơ chế cập nhật này biến $G(t)$ thành một mô hình định hướng dữ liệu (data-driven model) liên tục tinh chỉnh sự bổ trợ xuyên họ (cross-family complementarity) trong suốt quá trình tìm kiếm.

#### 3.3.1 When to Transfer: Saturation Detection

* Một đảo được coi là bão hòa (saturated) khi đã cạn kiệt thông tin hữu ích có thể trích xuất dưới họ biến đổi hiện tại, khiến cho việc tìm kiếm cục bộ tiếp theo chỉ đem lại hiệu suất suy giảm dần (diminishing returns).
* Tiêu chuẩn phát hiện bão hòa hình thức (formal saturation criterion):
  * Đảo $i$ bị coi là bão hòa tại thế hệ $t$ nếu mức cải thiện biên kỳ vọng (expected marginal improvement) từ các đề xuất nội đảo rơi xuống dưới ngưỡng $\varepsilon > 0$ trong một cửa sổ trượt gồm $W$ thế hệ liên tiếp:
    $$\frac{1}{W} \sum_{\tau = t - W + 1}^{t} \Delta_i(\tau) \le \varepsilon$$
  * Đại lượng cải thiện biên thế hệ được định nghĩa bởi:
    $$\Delta_i(\tau) = \mathbb{E}[U_i^{\max}(\tau + 1) - U_i^{\max}(\tau)]$$
    trong đó $U_i^{\max}(\tau) = \max_{p \in \Pi_i^{(\tau)}} \hat{\Phi}(p)$ là điểm thích nghi tối đa của quần thể $\Pi_i^{(\tau)}$ tại thế hệ $\tau$.
* Cơ chế phát hiện bão hòa tách rời hoàn toàn quá trình chuyển giao khỏi các lịch trình cố định (fixed schedules), chỉ kích hoạt giao tiếp xuyên đảo khi tìm kiếm cục bộ thực sự rơi vào trạng thái đình trệ (stagnation).

#### 3.3.2 Where to Transfer: Precursor Selection

* Khi đảo $i$ rơi vào trạng thái bão hòa, TOPOFE chọn một đảo tiền thân (precursor island / donor) $j^*$ có tri thức giàu tiềm năng nhất để giải tỏa bế tắc cho đảo $i$:
  $$j^* = \arg\max_{j \neq i} w_{j \to i}^{(t)}$$
  trường hợp hòa điểm (ties) được giải quyết ngẫu nhiên.
* Định tuyến chuyển giao thích ứng:
  * Theo thời gian tiến hóa, đồ thị $G(t)$ xác định các tuyến chuyển giao có độ hữu dụng cao bền vững (persistently high-utility transfer pathways, chẳng hạn: chuỗi thời gian $\to$ số học / temporal $\to$ arithmetic).
  * Việc nhận biết tuyến chuyển giao tối ưu giúp tập trung ngân sách tìm kiếm vào các tổ hợp liên họ mang lại năng suất cao nhất thay vì phân tán tài nguyên ngẫu nhiên.

#### 3.3.3 What to Transfer: Cross-Island Synthesis

* Khi đã xác định được đảo bão hòa $i$ và đảo tiền thân $j^*$, cơ chế tổng hợp chéo đảo (cross-island synthesis) tạo ra các chương trình lai ghép (hybrid programs) trong không gian hợp thành chung:
  $$\mathcal{P}_{i \leftarrow j^*} \subseteq \mathcal{P}_i \cup (\mathcal{P}_i \circ \mathcal{P}_{j^*})$$
  trong đó ký hiệu $\circ$ đại diện cho phép hợp thành ở cấp độ toán tử (operator-level composition).
* Cơ chế kích hoạt LLM (LLM prompting mechanism):
  * LLM nhận đầu vào gồm top-$m$ chương trình từ $\Pi_i^{(t)}$ đóng vai trò ngữ cảnh mục tiêu (target context).
  * top-$m$ chương trình từ $\Pi_{j^*}^{(t)}$ đóng vai trò ngữ cảnh nguồn / tài trợ (donor context).
  * Siêu dữ liệu tác vụ $\mathcal{M}$ (task metadata) mô tả đặc tính bộ dữ liệu và mục tiêu bài toán.
  * LLM sinh ra các chương trình mới tích hợp các thành phần cấu trúc từ $\mathcal{P}_{j^*}$ trong khi vẫn duy trì sự tương thích chặt chẽ với thiên kiến quy nạp (inductive bias) của $\mathcal{P}_i$.
* Bản chất của tổng hợp lai có LLM điều phối (LLM-mediated hybrid synthesis):
  * Khác biệt căn bản so với sao chép chương trình trực tiếp (direct program copying), phương pháp này tạo ra các chương trình nằm ngoài phạm vi có thể tiếp cận được của tìm kiếm nội đảo đơn lẻ.
* Vòng phản hồi cập nhật:
  * Các ứng viên được chấp nhận sẽ được bổ sung vào quần thể $\Pi_i^{(t)}$ và kho lưu trữ tinh hoa $\mathcal{A}_i^{(t)}$.
  * Mức cải thiện độ thích nghi thực tế quan sát được $\Delta_{\text{cross}}^{(j^* \to i)}(t)$ lập tức được dùng để cập nhật trọng số cạnh $w_{j^* \to i}^{(t)}$ theo công thức EMA (Phương trình 11).
  * Vòng phản hồi đảm bảo các quyết định định tuyến chuyển giao trong các thế hệ tiếp theo luôn phản ánh chính xác độ hữu dụng thực nghiệm của từng tuyến liên lạc.

#### 3.3.4 Unified Objective

* Mục tiêu tối ưu hóa hợp nhất của TOPOFE đồng thời cân bằng giữa hiệu năng dự đoán (predictive performance), tính bổ trợ đặc trưng (feature complementarity), độ ổn định (stability), và hiệu quả chi phí tính toán (computational efficiency):
  * Gọi $\mathcal{A} = \bigcup_{i=1}^M \mathcal{A}_i$ là kho lưu trữ ứng viên gộp (pooled candidate archive) thu thập từ tất cả $M$ kho lưu trữ tinh hoa của các đảo.
  * Tập đặc trưng kỹ thuật hóa cuối cùng $S^* \subseteq \mathcal{A}$ được tuyển chọn thông qua cơ chế chọn lọc nhận biết độ dư thừa (redundancy-aware selection) dưới ràng buộc lực lượng $|S^*| \le d'_{\max}$.
* Hàm mục tiêu toàn cục (Global Optimization Objective):
  $$\max_{\{\Pi_i\}, G, S^* \subseteq \mathcal{A}} \mathbb{E}[\text{Perf}(f_{S^*}^*, T_{S^*}(X_{\text{val}}), y_{\text{val}})] - \lambda_1 \text{Redundancy}(S^*) + \lambda_2 \text{Stability}(S^*) - \lambda_3 \text{Cost}(B)$$
  $$\text{s.t.} \quad |S^*| \le d'_{\max}$$
* Diễn giải các thành phần trong hàm mục tiêu:
  * **Hiệu năng dự đoán ($\text{Perf}$)**: Đánh giá khả năng tổng quát hóa hạ nguồn của mô hình dự đoán $f_{S^*}^*$ được huấn luyện trên tập đặc trưng đã biến đổi $T_{S^*}(X_{\text{val}})$.
  * **Hình phạt dư thừa ($\text{Redundancy}(S)$)**: Ngăn chặn các chương trình đặc trưng có tương quan quá cao:
    $$\text{Redundancy}(S) = \frac{1}{|S|(|S| - 1)} \sum_{p \neq p' \in S} |\text{Corr}(p(X), p'(X))|$$
    trong đó $\text{Corr}(\cdot, \cdot)$ biểu thị hệ số tương quan hạng Spearman (Spearman rank correlation) tính trên đầu ra của đặc trưng. Công thức loại trừ tự tương quan và chỉ phạt độ dư thừa theo từng cặp giữa các chương trình đặc trưng phân biệt.
  * **Độ ổn định ($\text{Stability}(S)$)**: Đo lường nghịch đảo phương sai của ước lượng độ thích nghi $\hat{\Phi}(S)$ qua các fold kiểm định chéo (cross-validation folds), khuyến khích các tập đặc trưng duy trì hiệu năng nhất quán trên các phân vùng huấn luyện - kiểm định khác nhau.
  * **Chi phí tính toán ($\text{Cost}(B)$)**: Đại diện cho tổng ngân sách đánh giá oracle tiêu thụ trong suốt quá trình tìm kiếm.
  * **Hệ số điều hòa $\lambda_1, \lambda_2, \lambda_3 \ge 0$**: Kiểm soát sự đánh đổi đa mục tiêu giữa độ chính xác dự đoán, tính đa dạng đặc trưng, độ vững chắc và hiệu quả tài nguyên.
* Cơ chế chọn lọc đặc trưng tham lam sau tìm kiếm (Post-Search Greedy Feature Selection):
  * Sau khi kết thúc quá trình tìm kiếm, tập đặc trưng cuối cùng $S^*$ được kiến tạo bằng cách duyệt tham lam các chương trình điểm cao từ $\mathcal{A}$ theo thứ tự giảm dần của hiệu năng kiểm định.
  * Bất kỳ ứng viên nào có độ tương quan tuyệt đối với một đặc trưng đã được chọn vượt quá ngưỡng định trước $\tau_{\text{red}}$ đều bị loại bỏ, bảo đảm tính bổ trợ tối đa trong tập $S^*$.
* Quy trình thuật toán tổng thể TOPOFE (Algorithm 1 Details):
  * **Đầu vào (Input)**: Bộ dữ liệu $\mathcal{D}$, không gian tác vụ và siêu dữ liệu $\mathcal{M}$, $M$ họ biến đổi $\{\mathcal{P}_i\}_{i=1}^M$, ngân sách đánh giá $B$, kích thước cửa sổ trượt $W$, ngưỡng bão hòa $\varepsilon$, hệ số suy giảm $\alpha$, giới hạn đặc trưng $d'_{\max}$, ngưỡng tương quan $\tau_{\text{red}}$.
  * **Khởi tạo (Initialization)**:
    * Với mỗi đảo $i = 1, \dots, M$: khởi tạo quần thể hạt giống $\Pi_i^{(0)} \leftarrow \text{LLM-Seed}(\mathcal{P}_i, \mathcal{M})$; kho lưu trữ tinh hoa $\mathcal{A}_i^{(0)} \leftarrow \emptyset$; bộ nhớ thích nghi prompt $\rho_i^{(0)} \leftarrow \emptyset$.
    * Khởi tạo ma trận trọng số đồ thị topo $G^{(0)}$ với $w_{j \to i}^{(0)} = \frac{1}{M - 1}$ với mọi $j \neq i$.
    * Đặt chỉ số thế hệ $t \leftarrow 0$, số lượng đánh giá đã dùng $b \leftarrow 0$.
  * **Vòng lặp tiến hóa và chuyển giao (while $b < B$)**:
    1. *Tiến hóa nội đảo song song (Parallel Intra-island Evolution)*:
       * Với mỗi đảo $i = 1, \dots, M$ đồng thời thực hiện:
         * Đề xuất ứng viên thông qua đột biến hoặc lai ghép: $p' \leftarrow \text{LLM-Mutate/Crossover}(\mathcal{A}_i^{(t)}, \mathcal{M}, \rho_i^{(t)})$.
         * Đánh giá độ thích nghi $\hat{\Phi}(p')$; cập nhật ngân sách $b \leftarrow b + 1$.
         * Cập nhật quần thể $\Pi_i^{(t+1)}$, kho lưu trữ $\mathcal{A}_i^{(t+1)}$, lịch sử $\mathcal{H}_i^{(t+1)}$ và bộ nhớ prompt $\rho_i^{(t+1)}$.
    2. *Phát hiện bão hòa và chuyển giao nhận biết topo (Topology-Aware Transfer)*:
       * Với mỗi đảo $i = 1, \dots, M$:
         * Kiểm tra điều kiện bão hòa $\text{Saturated}(i, W, \varepsilon)$ theo cửa sổ trượt $W$ và ngưỡng $\varepsilon$.
         * Nếu đảo $i$ bão hòa:
           * Chọn đảo tiền thân $j^* \leftarrow \arg\max_{j \neq i} w_{j \to i}^{(t)}$.
           * Tổng hợp chương trình lai ghép liên đảo: $p' \leftarrow \text{LLM-HybridSynth}(\mathcal{A}_i^{(t)}, \mathcal{A}_{j^*}^{(t)}, \mathcal{M})$.
           * Đánh giá $\hat{\Phi}(p')$; cập nhật ngân sách $b \leftarrow b + 1$.
           * Bổ sung ứng viên hợp lệ vào $\Pi_i^{(t+1)}$ và $\mathcal{A}_i^{(t+1)}$.
           * Cập nhật trọng số thích ứng của tuyến chuyển giao: $w_{j^* \to i}^{(t+1)} \leftarrow (1 - \alpha) w_{j^* \to i}^{(t)} + \alpha \Delta_{\text{cross}}^{(j^* \to i)}(t)$.
    3. Tăng biến đếm thế hệ $t \leftarrow t + 1$.
  * **Lựa chọn tập đặc trưng đầu ra (Output Selection)**:
    * Trả về $S^* \leftarrow \text{GreedySelect}\left(\bigcup_{i=1}^M \mathcal{A}_i^{(t)}, d'_{\max}, \tau_{\text{red}}\right)$.
* Hiệu quả mẫu và hội tụ (Sample Efficiency & Convergence):
  * Việc chỉ kích hoạt chuyển giao khi phát hiện bão hòa giúp tập trung các đánh giá oracle vào các vùng có độ hữu dụng cao trong không gian $\mathcal{P}$, giảm mạnh số thế hệ $T$ cần thiết để hội tụ so với tìm kiếm đơn quần thể thông thường.
  * TOPOFE đạt độ phức tạp tiệm cận tương đương với phương pháp đơn quần thể nhưng vượt trội về thời gian thực thi nhờ tính song song tự nhiên giữa các đảo và tăng tốc hội tụ nhờ khám phá liên họ có cấu trúc topo dẫn đường.
