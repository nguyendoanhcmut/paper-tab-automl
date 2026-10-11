### 3.3 Topology-Aware Cross-Island Transfer

* **Giới hạn của phân rã đa đảo (multi-island decomposition) và nhu cầu chuyển giao liên họ:**
  * Phân rã đa đảo giúp ngăn ngừa hiện tượng bão hòa nội họ (within-family saturation), nhưng không thể tự khám phá các đặc trưng đòi hỏi sự kết hợp đồng thời của các toán tử từ nhiều họ khác nhau.
  * *Ví dụ minh chứng*: Đặc trưng $\frac{\text{rolling\_mean}(\text{sales}, 7)}{\text{lag}(\text{sales}, 3)}$ kết hợp các toán tử thời gian (temporal operators - $\mathcal{P}_3$) với các toán tử số học (arithmetic operators - $\mathcal{P}_1$), mà không một họ đơn lẻ nào có thể tự sinh ra được.
* **Cơ chế chuyển giao liên đảo nhận biết cấu trúc topo (topology-aware cross-island transfer):**
  * TOPOFE giới thiệu cơ chế chuyển giao liên đảo nhận biết cấu trúc topo nhằm khám phá một cách có hệ thống các cấu thành liên họ (cross-family compositions) như vậy.
  * Cơ chế được tổ chức xoay quanh ba câu hỏi cốt lõi:
    * Khi nào chuyển giao (phát hiện bão hòa - saturation detection)?
    * Chuyển giao từ đâu / tới đâu (lựa chọn đảo tiền thân/nguồn - precursor selection)?
    * Chuyển giao cái gì (tổng hợp lai - hybrid synthesis)?
* **Định nghĩa 3 (Đồ thị Topo - Topology Graph):**
  * Đồ thị topo $G(t) = (V, E, W(t))$ là một đồ thị có hướng có trọng số (directed weighted graph), trong đó:
    * $V$ là tập hợp các đảo (set of islands).
    * $E$ là tập hợp các cạnh chuyển giao có hướng (set of directed transfer edges).
    * $w_{j \to i}^{(t)} \in W(t)$ mã hóa độ hữu dụng quan sát được từ thực nghiệm (empirically observed utility) của việc chuyển giao tri thức từ đảo $j$ sang đảo $i$ tính đến thế hệ $t$.
* **Khởi tạo và quy tắc cập nhật trực tuyến trọng số cạnh:**
  * Trọng số cạnh được khởi tạo đồng nhất tại thế hệ $t = 0$:
    $$w_{j \to i}^{(0)} = \frac{1}{M - 1} \quad \text{với } j \ne i$$
    trong đó $M$ là tổng số đảo.
  * Trọng số cạnh được cập nhật trực tuyến (online) sau mỗi sự kiện chuyển giao thông qua trung bình trượt hàm mũ (EMA - Exponential Moving Average):
    $$w_{j \to i}^{(t+1)} = (1 - \alpha) w_{j \to i}^{(t)} + \alpha \Delta_{\text{cross}}^{(j \to i)}(t) \tag{11}$$
    trong đó:
    * $\alpha \in (0, 1)$ là hệ số suy giảm (decay coefficient).
    * $\Delta_{\text{cross}}^{(j \to i)}(t)$ là mức tăng độ thích nghi quan sát được (observed fitness gain) từ sự kiện chuyển giao tri thức từ đảo $j$ sang đảo $i$.
  * Quy tắc cập nhật này biến $G(t)$ thành một mô hình định hướng bởi dữ liệu (data-driven model) liên tục được tinh chỉnh về tính bổ trợ liên họ (cross-family complementarity), được cập nhật trực tuyến trong suốt quá trình tìm kiếm.

#### 3.3.1 When to Transfer: Saturation Detection

* **Định nghĩa trạng thái bão hòa (saturated island):**
  * Một đảo được coi là bão hòa khi nó đã khai thác cạn kiệt thông tin hữu ích có thể trích xuất được dưới họ biến đổi (transformation family) hiện tại của mình.
  * Khi đã bão hòa, việc tiếp tục tìm kiếm cục bộ nội đảo chỉ mang lại hiệu suất suy giảm dần (diminishing returns).
* **Hình thức hóa toán học cho điều kiện phát hiện bão hòa:**
  * Đảo $i$ rơi vào trạng thái bão hòa tại thế hệ $t$ nếu mức cải thiện biên kỳ vọng (expected marginal improvement) từ các đề xuất nội đảo giảm xuống dưới ngưỡng $\varepsilon > 0$ trong một cửa sổ trượt gồm $W$ thế hệ liên tiếp:
    $$\frac{1}{W} \sum_{\tau=t-W+1}^{t} \Delta_i(\tau) \le \varepsilon \tag{12}$$
    trong đó:
    * $\Delta_i(\tau) = \mathbb{E}[U_i^{\max}(\tau + 1) - U_i^{\max}(\tau)]$ là mức cải thiện độ thích nghi kỳ vọng giữa thế hệ $\tau$ và $\tau+1$.
    * $U_i^{\max}(\tau) = \max_{p \in \Pi_i^{(\tau)}} \hat{\Phi}(p)$ biểu thị điểm thích nghi cao nhất trong quần thể chương trình $\Pi_i^{(\tau)}$ của đảo $i$ tại thế hệ $\tau$, với $\hat{\Phi}(p)$ là ước lượng độ thích nghi của chương trình đặc trưng $p$.
* **Ý nghĩa cơ chế của phát hiện bão hòa:**
  * Cơ chế phát hiện bão hòa tách rời (decouples) việc chuyển giao tri thức khỏi các lịch trình cố định (fixed schedules).
  * Chỉ kích hoạt giao tiếp liên đảo khi quá trình tìm kiếm cục bộ thực sự rơi vào trạng thái đình trệ (genuinely stagnated).

#### 3.3.2 Where to Transfer: Precursor Selection

* **Tiêu chí lựa chọn đảo tiền thân / đảo cho tặng (precursor / donor island):**
  * Khi đảo $i$ rơi vào trạng thái bão hòa, TOPOFE chọn một đảo tiền thân $j^*$, đóng vai trò là bên cho tặng (donor) mà tri thức của nó có khả năng cao nhất giúp giải tỏa tình trạng đình trệ của đảo $i$:
    $$j^* = \arg\max_{j \ne i} w_{j \to i}^{(t)} \tag{13}$$
  * Các trường hợp hòa điểm (ties) được phân định ngẫu nhiên (broken at random).
* **Định hướng ngân sách tìm kiếm theo đồ thị topo:**
  * Theo thời gian tìm kiếm, đồ thị $G(t)$ tự động nhận diện các lộ trình chuyển giao có độ hữu dụng cao bền vững (persistently high-utility transfer pathways) (ví dụ: chuyển giao từ toán tử thời gian $\to$ toán tử số học / temporal $\to$ arithmetic).
  * Việc này giúp tập trung ngân sách tìm kiếm (search budget) vào các cấu thành liên họ mang lại hiệu quả cao (productive cross-family compositions).

#### 3.3.3 What to Transfer: Cross-Island Synthesis

* **Không gian thành phần chung (joint composition space):**
  * Cho trước đảo bị bão hòa $i$ và đảo tiền thân $j^*$, quá trình tổng hợp liên đảo sinh ra các chương trình lai (hybrid programs) trong không gian thành phần chung:
    $$\mathcal{P}_{i \leftarrow j^*} \subseteq \mathcal{P}_i \cup (\mathcal{P}_i \circ \mathcal{P}_{j^*}) \tag{14}$$
    trong đó $\circ$ ký hiệu phép kết hợp ở cấp độ toán tử (operator-level composition).
* **Cơ chế điều phối nhắc lệnh cho LLM (LLM-prompted hybrid synthesis):**
  * Mô hình ngôn ngữ lớn (LLM) được cung cấp prompt chứa:
    * Top-$m$ chương trình từ quần thể $\Pi_i^{(t)}$ làm ngữ cảnh đích (target context).
    * Top-$m$ chương trình từ quần thể $\Pi_{j^*}^{(t)}$ làm ngữ cảnh cho tặng (donor context).
    * Siêu dữ liệu tác vụ (task metadata) $\mathcal{M}$.
  * LLM sinh ra các chương trình mới tích hợp các phần tử cấu trúc từ họ $\mathcal{P}_{j^*}$, trong khi vẫn duy trì tính nhất quán với thiên kiến quy nạp (inductive bias) của họ đích $\mathcal{P}_i$.
* **Điểm khác biệt căn bản so với sao chép trực tiếp:**
  * Tổng hợp lai do LLM làm trung gian (LLM-mediated hybrid synthesis) khác biệt căn bản so với việc sao chép chương trình trực tiếp (direct program copying).
  * Cơ chế này cho phép sinh ra các chương trình nằm ngoài tầm với nếu chỉ thực hiện tìm kiếm nội đảo đơn thuần (unreachable by intra-island search alone).
* **Cập nhật quần thể và phản hồi độ hữu dụng:**
  * Các chương trình ứng viên được chấp nhận sẽ được cập nhật vào quần thể $\Pi_i^{(t)}$ và kho lưu trữ $\mathcal{A}_i^{(t)}$.
  * Mức tăng độ thích nghi thực nghiệm quan sát được sẽ cập nhật trọng số cạnh $w_{j^* \to i}^{(t)}$ thông qua Phương trình (11).
  * Đảm bảo rằng các quyết định định tuyến chuyển giao trong tương lai phản ánh chính xác độ hữu dụng thực nghiệm của lộ trình chuyển giao này.

#### 3.3.4 Unified Objective

* **Mục tiêu tối ưu hóa đa tiêu chí đồng thời:**
  * Hàm mục tiêu toàn diện của TOPOFE tối ưu hóa đồng thời bốn yếu tố: hiệu năng dự đoán (predictive performance), tính bổ trợ đặc trưng (feature complementarity), độ ổn định (stability), và hiệu quả tính toán (computational efficiency).
* **Kho ứng viên gộp và ràng buộc lực lượng:**
  * Đặt $\mathcal{A} = \bigcup_{i=1}^M \mathcal{A}_i$ là kho lưu trữ ứng viên gộp (pooled candidate archive) tập hợp từ các kho lưu trữ thành phần của tất cả các đảo.
  * Tập đặc trưng kỹ thuật cuối cùng $S^* \subseteq \mathcal{A}$ được lựa chọn thông qua cơ chế chọn lọc nhận biết độ dư thừa (redundancy-aware selection) dưới ràng buộc lực lượng (cardinality constraint):
    $$|S^*| \le d'_{\max}$$
* **Hình thức hóa toán học của hàm mục tiêu hợp nhất:**
  * Bài toán tối ưu hóa được định nghĩa như sau:
    $$\max_{\{\Pi_i\}, G, S^* \subseteq \mathcal{A}} \mathbb{E}[\text{Perf}(f^*_{S^*}, T_{S^*}(X_{\text{val}}), y_{\text{val}})] - \lambda_1 \text{Redundancy}(S^*) + \lambda_2 \text{Stability}(S^*) - \lambda_3 \text{Cost}(B) \tag{15}$$
    thỏa mãn điều kiện:
    $$|S^*| \le d'_{\max}$$
* **Chi tiết các thành phần trong hàm mục tiêu:**
  * **Số hạng hiệu năng dự đoán (Predictive term)**:
    * $\mathbb{E}[\text{Perf}(f^*_{S^*}, T_{S^*}(X_{\text{val}}), y_{\text{val}})]$ đánh giá hiệu năng khái quát hóa hạ nguồn (downstream generalization performance) của mô hình $f^*$ được huấn luyện trên tập đặc trưng kỹ thuật $S^*$.
  * **Số hạng phạt độ dư thừa (Redundancy penalty)**:
    * Ngăn chặn các chương trình đặc trưng có tương quan cao với nhau:
      $$\text{Redundancy}(S) = \frac{1}{|S|(|S|-1)} \sum_{p \ne p' \in S} |\text{Corr}(p(X), p'(X))|$$
    * $\text{Corr}(\cdot, \cdot)$ biểu thị hệ số tương quan thứ hạng Spearman (Spearman rank correlation) được tính toán trên các đầu ra đặc trưng (feature outputs).
    * Công thức này loại trừ tương quan bản thân (self-correlations) và chỉ phạt độ dư thừa từng cặp (pairwise redundancy) giữa các chương trình đặc trưng phân biệt.
  * **Số hạng độ ổn định (Stability term)**:
    * $\text{Stability}(S)$ đo lường nghịch đảo phương sai (inverse variance) của ước lượng độ thích nghi $\hat{\Phi}(S)$ qua các fold kiểm định chéo (cross-validation folds).
    * Khuyến khích các tập đặc trưng duy trì hiệu năng nhất quán dưới các phân vùng tập huấn luyện - kiểm định (train-validation partitions) khác nhau.
  * **Số hạng chi phí tính toán (Computational cost term)**:
    * $\text{Cost}(B)$ biểu thị tổng ngân sách đánh giá kiểm thử qua hàm mục tiêu chuẩn (total oracle evaluation budget) bị tiêu tốn trong suốt quá trình tìm kiếm.
  * **Các siêu tham số đánh đổi (Trade-off hyperparameters)**:
    * Các hệ số $\lambda_1, \lambda_2, \lambda_3 \ge 0$ kiểm soát sự đánh đổi giữa độ chính xác dự đoán, độ đa dạng đặc trưng, độ vững chắc (robustness), và hiệu quả tính toán.
* **Quy trình hậu xử lý xây dựng tập đặc trưng cuối cùng (post-search feature selection):**
  * Sau khi kết thúc tìm kiếm, tập đặc trưng cuối cùng được xây dựng bằng cách chọn tham lam (greedily selecting) các chương trình điểm cao từ $\mathcal{A}$ theo thứ tự giảm dần của hiệu năng kiểm định (validation performance).
  * Đồng thời loại bỏ các ứng viên có tương quan tuyệt đối với bất kỳ đặc trưng nào đã được chọn trước đó vượt quá ngưỡng định trước $\tau_{\text{red}}$.
