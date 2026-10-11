## 2 Preliminary

### 2.1 Feature Engineering (FE)

* **Định nghĩa tập dữ liệu bảng và không gian đặc trưng:**
  * Cho $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$ là một tập dữ liệu dạng bảng (tabular dataset) gồm $N$ cá thể (instances).
  * Mỗi cá thể được biểu diễn bởi một vector đặc trưng $d$ chiều: $\mathbf{x}_i \in \mathcal{X} \subseteq \mathbb{R}^d$.
  * Biến mục tiêu tương ứng là $y_i \in \mathcal{Y}$.
* **Siêu dữ liệu có cấu trúc $\mathcal{M}$ (structured metadata):**
  * Mỗi tập dữ liệu được đi kèm với siêu dữ liệu có cấu trúc $\mathcal{M} = \{\mathcal{M}_{\text{task}}, \mathcal{M}_{\text{feat}}\}$.
  * $\mathcal{M}_{\text{task}}$ mã hóa loại tác vụ học máy (task type).
  * $\mathcal{M}_{\text{feat}}$ mã hóa các bộ mô tả ngữ nghĩa cho từng đặc trưng riêng biệt (per-feature semantic descriptors).
* **Mô hình dự báo hạ nguồn và tối thiểu hóa rủi ro thực nghiệm (Empirical Risk Minimization - ERM):**
  * Xét một phép biến đổi đặc trưng $T : \mathcal{X} \rightarrow \tilde{\mathcal{X}}$.
  * Gọi $\mathcal{F}$ là lớp các mô hình dự báo hạ nguồn (class of downstream predictive models) và $\mathcal{L}$ là hàm mất mát phù hợp với tác vụ (task-appropriate loss function).
  * Mô hình hạ nguồn tối ưu $f_T^*$ thu được thông qua quá trình tối thiểu hóa rủi ro thực nghiệm trên phân chia tập huấn luyện $\{X_{\text{tr}}, y_{\text{tr}}\}$:
    $$f_T^* = \arg\min_{f \in \mathcal{F}} \mathcal{L}(f(T(X_{\text{tr}})), y_{\text{tr}}) \quad (1)$$
* **Mục tiêu của kỹ thuật đặc trưng (Feature Engineering objective):**
  * Mục tiêu của kỹ thuật đặc trưng là tìm kiếm phép biến đổi tối ưu $T^*$ nhằm tối đa hóa hiệu năng tổng quát hóa (generalization performance) trên tập dữ liệu kiểm định giữ lại (held-out validation data):
    $$T^* = \arg\max_{T} \mathbb{E}[\text{Perf}(f_T^*, T(X_{\text{val}}), y_{\text{val}})] \quad (2)$$
  * Trong đó $\text{Perf}$ là thước đo hiệu năng phù hợp với tác vụ (ví dụ: độ chính xác — accuracy).
* **Bản chất tối ưu hóa hai cấp (Bilevel optimization) và thách thức tìm kiếm:**
  * Bài toán thiết kế đặc trưng cấu thành một bài toán tối ưu hóa hai cấp (bilevel optimization):
    * Bài toán cấp trong (inner problem): khớp / huấn luyện mô hình $f$ dưới một phép biến đổi đặc trưng $T$ cố định.
    * Bài toán cấp ngoài (outer problem): tìm kiếm chính phép biến đổi đặc trưng tối ưu $T$.
  * Hàm mục tiêu cấp ngoài là phi khả vi (non-differentiable) đối với phép biến đổi $T$.
  * Mỗi lượt đánh giá đều đòi hỏi phải khớp lại mô hình $f$ từ đầu (re-fitting $f$ from scratch).
  * Do đó, các chiến lược tìm kiếm hiệu quả về mặt mẫu (sample-efficient search strategies) đóng vai trò thiết yếu.

### 2.2 AutoFE as LLM-guided Program Search

* **Cụ thể hóa không gian biến đổi $\mathcal{T}$ thành không gian chương trình đặc trưng:**
  * Không gian phép biến đổi $\mathcal{T}$ được cụ thể hóa thành không gian các chương trình đặc trưng thực thi được (executable feature programs) trên một thư viện toán tử hữu hạn có định kiểu (finite typed operator library) $\mathcal{O} = \{o_q\}_{q=1}^Q$.
  * Mỗi toán tử $o_q$ có bậc toán tử (arity — số lượng toán hạng) và nhãn kiểu xác định (type signature) (ví dụ: $+$, $-$, $\times$, $\div$, $\log$, $\exp$).
* **Định nghĩa chương trình đặc trưng $p \in \mathcal{P}$ và không gian chương trình $\mathcal{P}$:**
  * Một chương trình đặc trưng $p \in \mathcal{P}$ là một hàm bất kỳ $p : \mathcal{X} \rightarrow \mathbb{R}$ được tạo thành bằng cách kết hợp/hợp thành các toán tử từ thư viện $\mathcal{O}$ lên tới độ sâu giới hạn $L_{\max}$:
    $$\mathcal{P} := \left\{ p \mid p = o^{(L)} \circ \cdots \circ o^{(1)}, \, o^{(\ell)} \in \mathcal{O}, \, L \le L_{\max} \right\} \quad (3)$$
  * Mỗi chương trình $p \in \mathcal{P}$ được biểu diễn dưới dạng một hàm Python thực thi được (executable Python function).
* **Ma trận thiết kế biến đổi và mô hình hạ nguồn tối ưu tương ứng:**
  * Một tập đặc trưng $S \subseteq \mathcal{P}$ sinh ra một ma trận thiết kế biến đổi (transformed design matrix):
    $$T_S(X) = [p(X)]_{p \in S} \in \mathbb{R}^{N \times |S|}$$
  * Trong đó mỗi cột tương ứng với giá trị đầu ra của một chương trình đặc trưng $p \in S$.
  * Mô hình hạ nguồn tối ưu trên ma trận thiết kế biến đổi $T_S$ được xác định theo:
    $$f_S^* = \arg\min_{f \in \mathcal{F}} \mathcal{L}(f(T_S(X_{\text{tr}})), y_{\text{tr}}) \quad (4)$$
* **Công thức hóa AutoFE dưới dạng bài toán tìm kiếm chương trình tổ hợp (Combinatorial program search):**
  * Mục tiêu kỹ thuật đặc trưng tự động (AutoFE) được công thức hóa thành bài toán tìm kiếm chương trình mang tính tổ hợp:
    $$S^* = \arg\max_{S \subseteq \mathcal{P}} \mathbb{E}[\text{Perf}(f_S^*, T_S(X_{\text{val}}), y_{\text{val}})] \quad (5)$$
* **Tính bất khả thi của tìm kiếm bằng duyệt toàn bộ và đặc tính phi khả vi:**
  * Không gian tìm kiếm là bất khả thi để giải quyết bằng phương pháp liệt kê/duyệt toàn bộ (intractable by enumeration) vì kích thước không gian $|\mathcal{P}|$ tăng trưởng theo cấp siêu mũ (super-exponentially) theo độ sâu $L_{\max}$.
  * Mục tiêu tìm kiếm phi khả vi đối với cấu trúc chương trình rời rạc (discrete program structure).
* **Chi phí tính toán và ước lượng tín hiệu thích nghi (Fitness signal estimation):**
  * Mỗi lượt đánh giá tiêu tốn chi phí $\mathcal{O}(k_{\text{cv}} \cdot C_{\text{fit}}(N, |S|))$ dưới quy trình kiểm định chéo $k_{\text{cv}}$ nếp ($k_{\text{cv}}$-fold cross-validation).
  * Trong đó $C_{\text{fit}}(N, |S|)$ biểu thị chi phí huấn luyện mô hình trên $N$ thực thể và $|S|$ đặc trưng được thiết kế.
  * Tín hiệu độ thích nghi (fitness signal) $\hat{\Phi}(S)$ được ước lượng thông qua trung bình trên các nếp kiểm định:
    $$\hat{\Phi}(S) = \frac{1}{k_{\text{cv}}} \sum_{k=1}^{k_{\text{cv}}} \text{Perf}\left(f_{S,k}^*, T_S(X_{\text{val}}^k), y_{\text{val}}^k\right) \quad (6)$$
  * Trong đó $f_{S,k}^*$ được huấn luyện trên nếp huấn luyện thứ $k$ và được đánh giá trên nếp kiểm định giữ lại tương ứng $(X_{\text{val}}^k, y_{\text{val}}^k)$.
* **Vai trò của siêu dữ liệu $\mathcal{M}$ làm tiên nghiệm ngữ nghĩa cho LLM:**
  * Siêu dữ liệu $\mathcal{M}$ đóng vai trò ràng buộc không gian $\mathcal{P}$, chỉ cho phép các chương trình hợp lệ về mặt ngữ nghĩa (semantically valid programs).
  * Đồng thời, $\mathcal{M}$ cung cấp một phân phối tiên nghiệm bằng ngôn ngữ tự nhiên (natural-language prior) được khai thác trực tiếp bởi quá trình tổng hợp chương trình có sự định hướng của LLM (LLM-guided synthesis).
