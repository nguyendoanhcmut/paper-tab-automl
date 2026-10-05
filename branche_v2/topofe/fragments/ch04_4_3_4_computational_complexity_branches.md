### 3.4 Computational Complexity

* **Chi phí tính toán tiệm cận và so sánh với baseline đơn quần thể (Asymptotic Complexity & Baseline Comparison):**
  * Phương pháp tìm kiếm đặc trưng tiến hóa đơn quần thể tiêu chuẩn (standard single-population evolutionary feature search) đánh giá $n$ ứng viên (candidates) trong mỗi thế hệ (generation), với chi phí đánh giá mỗi ứng viên là $C_{\text{eval}}$, dẫn đến tổng chi phí tính toán qua $T$ thế hệ là $\mathcal{O}(T \cdot n \cdot C_{\text{eval}})$.
  * TOPOFE phân bổ $n$ ứng viên trên $M$ quần thể đảo (islands) với ràng buộc bảo toàn tổng số lượng ứng viên $\sum_{i=1}^M n_i = n$.
  * Chi phí tính toán trên mỗi thế hệ của TOPOFE được xác định bởi:
    $$\mathcal{O}\left(\sum_{i=1}^M n_i \cdot C_{\text{eval}} + |E_t| \cdot C_{\text{transfer}}\right) \tag{16}$$
    trong đó:
    * $|E_t|$ là số lượng cạnh chuyển giao đang hoạt động (number of active transfer edges) tại thế hệ $t$.
    * $C_{\text{transfer}}$ là chi phí cho một lệnh gọi tổng hợp lai ghép đơn lẻ (single hybrid synthesis call).
    * $C_{\text{eval}}$ là chi phí tính toán khi đánh giá độ thích nghi qua oracle $\hat{\Phi}$ trên mô hình học máy hạ nguồn.
  * Dưới giả định phân bổ cân bằng (balanced allocation, $n_i \approx n/M$), chi phí mỗi thế hệ rút gọn về:
    $$\mathcal{O}\left(n \cdot C_{\text{eval}} + |E_t| \cdot C_{\text{transfer}}\right)$$
    khớp hoàn toàn với độ phức tạp của baseline đơn quần thể ngoại trừ phần phụ phí chuyển giao (transfer overhead) $|E_t| \cdot C_{\text{transfer}}$.

* **Phân tích phụ phí chuyển giao và chi phí gọi API LLM (Transfer Overhead & LLM API Calls):**
  * Quá trình chuyển giao liên đảo không bị áp đặt theo lịch trình định kỳ cố định mà chỉ được kích hoạt khi phát hiện bão hòa thích ứng (saturation-triggered transfer).
  * Do đó, trong thực nghiệm, số lượng cạnh chuyển giao tích cực $|E_t|$ luôn duy trì ở mức rất nhỏ ($|E_t| \ll M$), khiến phụ phí chuyển giao $|E_t| \cdot C_{\text{transfer}}$ trở nên không đáng kể (negligible).
  * Chi phí gọi API mô hình ngôn ngữ lớn (LLM API cost) được phân định thành hai luồng rõ ràng:
    * *Đề xuất nội đảo (Intra-island proposals)*: Mỗi thế hệ phát sinh $n$ lượt gọi LLM cho các toán tử đột biến hoặc lai ghép ($\text{LLM-Mutate/Crossover}(\mathcal{A}_i^{(t)}, \mathcal{M}, \rho_i^{(t)})$).
    * *Tổng hợp lai liên đảo (Cross-island hybrid synthesis)*: Chỉ phát sinh $|E_t|$ lượt gọi $\text{LLM-HybridSynth}(\mathcal{A}_i^{(t)}, \mathcal{A}_{j^*}^{(t)}, \mathcal{M})$ khi có đảo thỏa mãn điều kiện bão hòa $\text{Saturated}(i, W, \varepsilon)$.

* **Tính song song hóa và giảm thời gian thực tế (Parallelism & Wall-clock Time):**
  * Các quá trình đánh giá ứng viên trên các đảo diễn ra hoàn toàn độc lập với nhau (mutually independent).
  * Toàn bộ $M$ đảo có thể thực thi song song đồng thời (parallel execution), giúp giảm thời gian đồng hồ thực tế (wall-clock time) trên mỗi thế hệ từ $\mathcal{O}(n \cdot C_{\text{eval}})$ xuống còn:
    $$\mathcal{O}\left(\max_i n_i \cdot C_{\text{eval}}\right)$$
  * Dưới phân vùng cân bằng ($n_i \approx n/M$), thời gian thực thi thực tế mỗi thế hệ giảm xuống $\mathcal{O}\left(\frac{n}{M} \cdot C_{\text{eval}}\right)$, mang lại mức tăng tốc xấp xỉ $k$ lần (approximate $k$-fold speedup, với $k \approx M$).

* **Cấu trúc thực thi hoàn chỉnh của Thuật toán TOPOFE (Algorithm 1: TOPOFE):**
  * **Đầu vào (Input)**:
    * Bộ dữ liệu dạng bảng $\mathcal{D}$.
    * Số lượng quần thể đảo $M$.
    * Phân hoạch ngữ nghĩa của không gian chương trình thành $M$ họ biến đổi $\{\mathcal{P}_i\}_{i=1}^M$.
    * Tổng ngân sách đánh giá (evaluation budget) $B$.
    * Kích thước cửa sổ trượt (sliding window size) $W$ dùng để phát hiện bão hòa.
    * Ngưỡng cải thiện bão hòa $\varepsilon$.
    * Hệ số suy giảm (decay coefficient) $\alpha$ trong cập nhật trọng số đồ thị tô-pô.
  * **Đầu ra (Output)**: Tập đặc trưng tối ưu được chọn $\mathcal{S}^*$.
  * **Quy trình thực thi chi tiết**:
    1. *Khởi tạo (Initialization - Dòng 1–3)*:
       * Với mỗi đảo $i = 1, \dots, M$: khởi tạo quần thể hạt giống $\Pi_i^{(0)} \leftarrow \text{LLM-Seed}(\mathcal{P}_i, \mathcal{M})$; thiết lập kho lưu trữ tinh hoa rỗng $\mathcal{A}_i^{(0)} \leftarrow \emptyset$; thiết lập bộ nhớ prompt rỗng $\rho_i^{(0)} \leftarrow \emptyset$.
       * Khởi tạo đồ thị tô-pô có hướng $\mathcal{G}^{(0)}$ với trọng số phân phối đều: $w_{j \to i}^{(0)} = \frac{1}{M - 1}$ với mọi $j \neq i$.
       * Khởi tạo chỉ số thế hệ $t \leftarrow 0$ và số lượt đánh giá đã dùng $b \leftarrow 0$.
    2. *Vòng lặp tiến hóa và chuyển giao có ràng buộc ngân sách (Dòng 4–13, `while b < B`)*:
       * *Tiến hóa nội đảo song song (Parallel intra-island evolution)*:
         * Với mỗi đảo $i = 1, \dots, M$ đồng thời thực hiện song song:
           * Sinh ứng viên mới: $p' \leftarrow \text{LLM-Mutate/Crossover}(\mathcal{A}_i^{(t)}, \mathcal{M}, \rho_i^{(t)})$.
           * Đánh giá độ thích nghi: tính $\hat{\Phi}(p')$ và tăng biến đếm ngân sách $b \leftarrow b + 1$.
           * Cập nhật trạng thái đảo: cập nhật quần thể $\Pi_i^{(t+1)}$, kho lưu trữ tinh hoa $\mathcal{A}_i^{(t+1)}$, lịch sử chấp nhận/từ chối $\mathcal{H}_i^{(t+1)}$, và bộ nhớ thích ứng prompt $\rho_i^{(t+1)}$ thông qua các Phương trình (8) và (9).
       * *Phát hiện bão hòa và chuyển giao liên đảo (Saturation detection & cross-island transfer)*:
         * Với mỗi đảo $i = 1, \dots, M$:
           * Kiểm tra điều kiện bão hòa: $\text{Saturated}(i, W, \varepsilon)$.
           * Nếu thỏa mãn bão hòa:
             * Chọn đảo tiền thân có độ hữu dụng cao nhất: $j^* \leftarrow \arg\max_{j \neq i} w_{j \to i}^{(t)}$.
             * Tổng hợp ứng viên lai ghép liên đảo: $p' \leftarrow \text{LLM-HybridSynth}(\mathcal{A}_i^{(t)}, \mathcal{A}_{j^*}^{(t)}, \mathcal{M})$.
             * Đánh giá ứng viên lai: tính $\hat{\Phi}(p')$ và tăng biến đếm ngân sách $b \leftarrow b + 1$.
             * Cập nhật $\Pi_i^{(t+1)}$ và $\mathcal{A}_i^{(t+1)}$ với ứng viên được chấp nhận.
             * Cập nhật trực tuyến trọng số cạnh chuyển giao trên đồ thị tô-pô bằng trung bình động hàm mũ (EMA):
               $$w_{j^* \to i}^{(t+1)} \leftarrow (1 - \alpha) w_{j^* \to i}^{(t)} + \alpha \Delta_{\text{cross}}^{(j^* \to i)}(t)$$
       * Tăng bước thế hệ: $t \leftarrow t + 1$.
    3. *Lựa chọn đặc trưng hậu tìm kiếm (Post-search feature selection - Dòng 14)*:
       * Tuyển chọn tập đặc trưng cuối cùng thông qua thuật toán chọn tham lam từ hợp kho tinh hoa của tất cả các đảo:
         $$\mathcal{S}^* \leftarrow \text{GreedySelect}\left(\bigcup_{i=1}^M \mathcal{A}_i^{(t)}, d_{\max}'\right)$$
         với ràng buộc số lượng đặc trưng tối đa $d_{\max}'$.

* **Hiệu quả mẫu và tốc độ hội tụ (Sample Efficiency & Convergence Speed):**
  * Cơ chế chuyển giao kích hoạt theo điểm bão hòa (saturation-triggered transfer) tập trung các lượt đánh giá oracle đắt đỏ vào các vùng có độ hữu dụng cao (high-utility regions) trong không gian chương trình $\mathcal{P}$, thay vì dàn trải ngân sách ngẫu nhiên hoặc tiếp tục khai thác các vùng đã bão hòa.
  * Nhờ đó, số lượng thế hệ $T$ cần thiết để hội tụ giảm đáng kể so với phương pháp tìm kiếm đơn quần thể thông thường.
  * TOPOFE đạt được độ phức tạp tiệm cận tương đương với baseline, đồng thời tối ưu hóa song song hai khía cạnh:
    * *Thời gian thực tế (wall-clock efficiency)*: Được rút ngắn đáng kể nhờ khả năng thực thi song song tự nhiên giữa các đảo.
    * *Tốc độ hội tụ (convergence speed)*: Được gia tốc mạnh mẽ nhờ cơ chế thăm dò liên họ có nguyên lý (principled cross-family exploration) được dẫn dắt bởi đồ thị tô-pô động.
