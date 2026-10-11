### 3.4 Computational Complexity

* **Chi phí tính toán của phương pháp tìm kiếm đặc trưng tiến hóa đơn quần thể chuẩn (standard single-population evolutionary feature search):**
  * Phương pháp tìm kiếm tiến hóa đơn quần thể chuẩn thực hiện đánh giá $n$ ứng viên trên mỗi thế hệ (evaluates $n$ candidates per generation).
  * Mỗi ứng viên tiêu tốn một chi phí đánh giá là $C_{\text{eval}}$ (each at cost $C_{\text{eval}}$).
  * Tổng chi phí tính toán qua $T$ thế hệ (total cost over $T$ generations) đạt mức tiệm cận:
    $$\mathcal{O}(T \cdot n \cdot C_{\text{eval}})$$

* **Phân bổ ứng viên và chi phí mỗi thế hệ trong TOPOFE:**
  * TOPOFE phân phối $n$ ứng viên trên $M$ đảo tiến hóa (distributes $n$ candidates across $M$ islands) thỏa mãn điều kiện bảo toàn tổng số lượng ứng viên:
    $$\sum_{i=1}^M n_i = n$$
    trong đó $n_i$ là số lượng ứng viên được phân bổ cho đảo thứ $i$.
  * Chi phí tính toán phát sinh trên mỗi thế hệ (per-generation cost) của TOPOFE được xác định bởi:
    $$\mathcal{O}\left(\sum_{i=1}^M n_i \cdot C_{\text{eval}} + |E_t| \cdot C_{\text{transfer}}\right) \quad (16)$$
  * Ý nghĩa các thành phần trong công thức (16):
    * $\sum_{i=1}^M n_i \cdot C_{\text{eval}}$ biểu thị tổng chi phí đánh giá nội đảo (intra-island evaluation cost) trên toàn bộ $M$ đảo trong một thế hệ.
    * $|E_t|$ là số lượng cạnh chuyển giao đang hoạt động (number of active transfer edges) tại thế hệ $t$.
    * $C_{\text{transfer}}$ là chi phí cho một lần gọi phép tổng hợp lai đơn lẻ (cost of a single hybrid synthesis call) thông qua mô hình ngôn ngữ lớn (LLM).

* **Hành vi tiệm cận dưới phân bổ cân bằng và tính không đáng kể của chi phí phụ trội chuyển giao:**
  * Dưới phân bổ cân bằng ($n_i \approx \frac{n}{M}$), chi phí mỗi thế hệ rút gọn về:
    $$\mathcal{O}(n \cdot C_{\text{eval}} + |E_t| \cdot C_{\text{transfer}})$$
    khớp hoàn toàn với đường cơ sở đơn quần thể (matches single-population baseline) ngoại trừ phần chi phí phụ trội chuyển giao (transfer overhead).
  * Chi phí phụ trội chuyển giao là không đáng kể (transfer overhead is negligible): do cơ chế chuyển giao được kích hoạt theo điều kiện bão hòa (saturation-triggered transfer) thay vì áp dụng liên tục ở mọi thế hệ, số lượng cạnh chuyển giao hoạt động $|E_t|$ duy trì ở mức rất nhỏ trong thực tế ($|E_t|$ remains small in practice).

* **Khả năng song song hóa (Parallelism) và mức tăng tốc thời gian thực tế (wall-clock speedup):**
  * Các lượt đánh giá trên từng đảo là độc lập lẫn nhau (island evaluations are mutually independent).
  * Tất cả $M$ đảo được thực thi song song đồng thời (all $M$ islands execute in parallel).
  * Thời gian thực tế trên mỗi thế hệ (wall-clock time per generation) giảm mạnh từ $\mathcal{O}(n \cdot C_{\text{eval}})$ xuống còn:
    $$\mathcal{O}\left(\max_i n_i \cdot C_{\text{eval}}\right)$$
  * Cơ chế thực thi song song đem lại tốc độ tăng tốc xấp xỉ $k$ lần (approximate $k$-fold speedup, với $k \approx M$) trong điều kiện phân vùng cân bằng ($n_i \approx \frac{n}{M}$).

* **Quy trình hoàn chỉnh của Thuật toán 1: TOPOFE (Algorithm 1: TOPOFE):**
  * **Đầu vào (Input):**
    * Tập dữ liệu bảng $\mathcal{D}$ (tabular dataset).
    * Số lượng đảo $M$ (number of islands).
    * Tập các họ biến đổi đặc trưng $\{\mathcal{P}_i\}_{i=1}^M$ (transformation families).
    * Tổng ngân sách đánh giá $B$ (evaluation budget).
    * Kích thước cửa sổ trượt $W$ (sliding window size for saturation detection).
    * Ngưỡng phát hiện bão hòa $\varepsilon$ (saturation threshold).
    * Hệ số suy giảm/học $\alpha$ (decay rate).
  * **Đầu ra (Output):**
    * Tập đặc trưng tối ưu $S^*$ (optimal engineered feature set).
  * **Khởi tạo (Initialization):**
    * Đối với mỗi đảo $i = 1, \dots, M$:
      * Sinh quần thể ban đầu qua LLM: $\Pi_i^{(0)} \leftarrow \text{LLM-Seed}(\mathcal{P}_i, \mathcal{M})$ dựa trên họ biến đổi $\mathcal{P}_i$ và siêu dữ liệu $\mathcal{M}$.
      * Khởi tạo kho lưu trữ tinh hoa rỗng: $\mathcal{A}_i^{(0)} \leftarrow \emptyset$.
      * Khởi tạo bộ nhớ câu nhắc rỗng: $\rho_i^{(0)} \leftarrow \emptyset$.
    * Khởi tạo đồ thị topo $\mathcal{G}^{(0)}$ với trọng số cạnh chuyển giao ban đầu đồng nhất giữa tất cả các cặp đảo phân biệt:
      $$w_{j \to i}^{(0)} = \frac{1}{M - 1}, \quad \forall j \neq i$$
    * Khởi tạo chỉ số thế hệ $t \leftarrow 0$ và bộ đếm ngân sách đã sử dụng $b \leftarrow 0$.
  * **Vòng lặp tiến hóa chính (trong khi ngân sách $b < B$):**
    * **Tiến hóa nội đảo song song (Parallel intra-island evolution):**
      * Với mỗi đảo $i = 1, \dots, M$ thực hiện **song song (in parallel)**:
        * Đề xuất ứng viên biến đổi: $p' \leftarrow \text{LLM-Mutate/Crossover}(\mathcal{A}_i^{(t)}, \mathcal{M}, \rho_i^{(t)})$.
        * Đánh giá ứng viên: Tính toán độ thích nghi $\hat{\Phi}(p')$ và tăng bộ đếm ngân sách $b \leftarrow b + 1$.
        * Cập nhật trạng thái đảo: Cập nhật quần thể $\Pi_i^{(t+1)}$, kho tinh hoa $\mathcal{A}_i^{(t+1)}$, lịch sử đánh giá $\mathcal{H}_i^{(t+1)}$, và bộ nhớ prompt $\rho_i^{(t+1)}$ theo Eqs. (8) và (9).
    * **Chuyển giao liên đảo nhận biết topo (Topology-aware cross-island transfer):**
      * Duyệt qua từng đảo $i = 1, \dots, M$:
        * Kiểm tra bão hòa: Nếu $\text{Saturated}(i, W, \varepsilon)$ trả về True:
          * Lựa chọn đảo tiền thân (precursor island) tối ưu: $j^* \leftarrow \arg\max_{j \neq i} w_{j \to i}^{(t)}$.
          * Tổng hợp lai liên đảo qua LLM: $p' \leftarrow \text{LLM-HybridSynth}(\mathcal{A}_i^{(t)}, \mathcal{A}_{j^*}^{(t)}, \mathcal{M})$.
          * Đánh giá ứng viên lai: Tính toán $\hat{\Phi}(p')$ và tăng bộ đếm ngân sách $b \leftarrow b + 1$.
          * Cập nhật quần thể và kho tinh hoa của đảo đích: $\Pi_i^{(t+1)}, \mathcal{A}_i^{(t+1)}$.
          * Cập nhật trọng số topo trên cạnh $j^* \to i$ theo quy tắc làm mịn hàm mũ:
            $$w_{j^* \to i}^{(t+1)} \leftarrow (1 - \alpha) w_{j^* \to i}^{(t)} + \alpha \Delta_{\text{cross}}^{(j^* \to i)}(t)$$
    * Cập nhật thế hệ: $t \leftarrow t + 1$.
  * **Lựa chọn tập đặc trưng cuối cùng (Final feature selection):**
    * Trả về tập đặc trưng tối ưu $S^*$ bằng cách lựa chọn tham lam từ hợp của tất cả các kho tinh hoa:
      $$S^* \leftarrow \text{GreedySelect}\left(\bigcup_{i=1}^M \mathcal{A}_i^{(t)}, d_{\max}'\right)$$
      trong đó $d_{\max}'$ là số lượng đặc trưng tối đa được giữ lại.

* **Hiệu quả sử dụng mẫu (Sample Efficiency) và tốc độ hội tụ:**
  * Cơ chế chuyển giao kích hoạt khi bão hòa (saturation-triggered transfer) tập trung các lượt đánh giá oracle (oracle evaluations) vào các vùng có độ hữu dụng cao (high-utility regions) trong không gian tìm kiếm $\mathcal{P}$.
  * Quá trình này làm giảm đáng kể số lượng thế hệ $T$ cần thiết để hội tụ so với tìm kiếm tiến hóa đơn quần thể (single-population search).
  * TOPOFE đạt được độ phức tạp tiệm cận (asymptotic complexity) tương đương với đường cơ sở đơn quần thể, đồng thời vượt trội trên hai phương diện cốt lõi:
    * Cải thiện hiệu quả thời gian thực tế (wall-clock efficiency) nhờ khả năng thực thi song song giữa các đảo độc lập.
    * Đẩy nhanh tốc độ hội tụ (convergence speed) nhờ cơ chế khám phá liên họ có nguyên lý (principled cross-family exploration) kết hợp giữa đồ thị topo động và mô hình ngôn ngữ lớn.
