## 2 Preliminary

### 2.1 Feature Engineering (FE)
- **Định nghĩa tập dữ liệu bảng và siêu dữ liệu cấu trúc**: Tập dữ liệu dạng bảng (tabular dataset) được biểu diễn dưới dạng $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$ gồm $N$ thực thể (instances), vector đặc trưng $d$-chiều $\mathbf{x}_i \in \mathcal{X} \subseteq \mathbb{R}^d$ và biến mục tiêu $y_i \in \mathcal{Y}$.
  - Mỗi tập dữ liệu đi kèm với siêu dữ liệu có cấu trúc (structured metadata) $\mathcal{M} = \{\mathcal{M}_{\text{task}}, \mathcal{M}_{\text{feat}}\}$, mã hóa loại tác vụ (task type) và các mô tả ngữ nghĩa cho từng đặc trưng (per-feature semantic descriptors).
- **Mô hình hạ nguồn tối ưu thông qua tối thiểu hóa rủi ro thực nghiệm**: Với một phép biến đổi đặc trưng (feature transformation) $\mathcal{T} : \mathcal{X} \to \tilde{\mathcal{X}}$, gọi $\mathcal{F}$ là lớp các mô hình dự đoán hạ nguồn (downstream predictive models) và $\mathcal{L}$ là hàm mất mát (loss function) tương ứng với tác vụ, mô hình hạ nguồn tối ưu $f^*_{\mathcal{T}}$ trên tập phân chia huấn luyện $\{\mathbf{X}_{\text{tr}}, \mathbf{y}_{\text{tr}}\}$ được xác định bằng tối thiểu hóa rủi ro thực nghiệm (empirical risk minimization - ERM):
  $$f^*_{\mathcal{T}} = \arg \min_{f \in \mathcal{F}} \mathcal{L}(f(\mathcal{T}(\mathbf{X}_{\text{tr}})), \mathbf{y}_{\text{tr}}) \tag{1}$$
- **Mục tiêu của kỹ thuật đặc trưng (Feature Engineering Objective)**: Mục tiêu của FE là tìm phép biến đổi tối ưu $\mathcal{T}^*$ nhằm cực đại hóa hiệu năng khái quát hóa (generalization performance) trên tập dữ liệu kiểm định giữ lại (held-out data):
  $$\mathcal{T}^* = \arg \max_{\mathcal{T}} \mathbb{E}\left[\text{Perf}(f^*_{\mathcal{T}}, \mathcal{T}(\mathbf{X}_{\text{val}}), \mathbf{y}_{\text{val}})\right] \tag{2}$$
  trong đó $\text{Perf}$ là thước đo hiệu năng phù hợp với tác vụ (ví dụ: accuracy).
- **Bản chất tối ưu hóa hai cấp (Bilevel Optimization) và thách thức tìm kiếm**:
  - Quá trình này cấu thành một bài toán tối ưu hóa hai cấp: bài toán cấp trong (inner problem) tối ưu hóa trọng số mô hình dưới một phép biến đổi cố định, trong khi bài toán cấp ngoài (outer problem) tìm kiếm chính phép biến đổi đó.
  - Mục tiêu cấp ngoài không khả vi (non-differentiable) đối với $\mathcal{T}$ và mỗi lượt đánh giá đều đòi hỏi phải huấn luyện lại mô hình $f$ từ đầu (re-fitting from scratch).
  - Do đó, các chiến lược tìm kiếm hiệu quả về số lượng mẫu (sample-efficient search strategies) đóng vai trò then chốt.

### 2.2 AutoFE as LLM-guided Program Search
- **Hiện thực hóa không gian biến đổi thành không gian chương trình đặc trưng khả thi**: Không gian biến đổi $\mathcal{T}$ được cụ thể hóa thành không gian các chương trình đặc trưng có thể thực thi (executable feature programs) trên một thư viện toán tử có định kiểu hữu hạn (finite typed operator library) $\mathcal{O} = \{o_q\}_{q=1}^Q$.
  - Mỗi toán tử $o_q$ có số lượng toán hạng (arity) và chữ ký kiểu (type signature) được chỉ định cụ thể (ví dụ: $+$, $-$, $\times$, $\div$, $\log$, $\exp$).
- **Định nghĩa không gian chương trình đặc trưng $\mathcal{P}$**: Một chương trình đặc trưng $p \in \mathcal{P}$ là một hàm bất kỳ $p : \mathcal{X} \to \mathbb{R}$ được tạo thành bằng cách hợp thành (composing) các toán tử từ $\mathcal{O}$ với độ sâu bị chặn $L_{\max}$:
  $$\mathcal{P} := \left\{ p \mid p = o^{(L)} \circ \dots \circ o^{(1)}, \; o^{(\ell)} \in \mathcal{O}, \; L \le L_{\max} \right\} \tag{3}$$
  - Mỗi chương trình $p \in \mathcal{P}$ được biểu diễn dưới dạng một hàm Python có thể thực thi (executable Python function).
- **Ma trận thiết kế biến đổi và mô hình hạ nguồn tương ứng**: Một tập hợp đặc trưng $S \subseteq \mathcal{P}$ cảm sinh một ma trận thiết kế biến đổi (transformed design matrix):
  $$\mathcal{T}_S(\mathbf{X}) = [p(\mathbf{X})]_{p \in S} \in \mathbb{R}^{N \times |S|} \tag{4}$$
  trong đó mỗi cột tương ứng với đầu ra của một chương trình đặc trưng.
  - Mô hình hạ nguồn tối ưu tương ứng $f^*_S$ là:
    $$f^*_S = \arg \min_{f \in \mathcal{F}} \mathcal{L}(f(\mathcal{T}_S(\mathbf{X}_{\text{tr}})), \mathbf{y}_{\text{tr}})$$
- **Công thức hóa AutoFE thành bài toán tìm kiếm chương trình tổ hợp (Combinatorial Program Search)**:
  $$S^* = \arg \max_{S \subseteq \mathcal{P}} \mathbb{E}\left[\text{Perf}(f^*_S, \mathcal{T}_S(\mathbf{X}_{\text{val}}), \mathbf{y}_{\text{val}})\right] \tag{5}$$
- **Độ phức tạp và tính bất khả thi khi duyệt vét cạn**:
  - Không gian tìm kiếm không thể duyệt vét cạn (intractable by enumeration) vì kích thước $|\mathcal{P}|$ tăng trưởng theo cấp siêu hàm mũ (super-exponentially) theo độ sâu $L_{\max}$.
  - Mục tiêu không khả vi (non-differentiable) đối với cấu trúc rời rạc của chương trình.
  - Mỗi lượt đánh giá gánh chịu chi phí tính toán $\mathcal{O}(k_{\text{cv}} \cdot C_{\text{fit}}(N, |S|))$ dưới quy trình kiểm định chéo $k_{\text{cv}}$-fold ($k_{\text{cv}}$-fold cross-validation), với $C_{\text{fit}}(N, |S|)$ biểu diễn chi phí huấn luyện trên $N$ mẫu dữ liệu và $|S|$ đặc trưng được tạo ra.
- **Tín hiệu độ thích nghi (Fitness Signal)**: Tín hiệu đánh giá độ thích nghi $\hat{\Phi}(S)$ được ước lượng thông qua kiểm định chéo $k_{\text{cv}}$-fold:
  $$\hat{\Phi}(S) = \frac{1}{k_{\text{cv}}} \sum_{k=1}^{k_{\text{cv}}} \text{Perf}\left(f^*_{S,k}, \mathcal{T}_S(\mathbf{X}_{\text{val}}^k), \mathbf{y}_{\text{val}}^k\right) \tag{6}$$
  trong đó $f^*_{S,k}$ được huấn luyện trên fold huấn luyện thứ $k$ và đánh giá trên fold kiểm định giữ lại tương ứng $\mathbf{X}_{\text{val}}^k, \mathbf{y}_{\text{val}}^k$.
- **Vai trò của siêu dữ liệu $\mathcal{M}$ đối với tổng hợp có LLM định hướng**:
  - Siêu dữ liệu $\mathcal{M}$ giới hạn không gian $\mathcal{P}$ trong phạm vi các chương trình hợp lệ về mặt ngữ nghĩa (semantically valid programs).
  - Cung cấp tiên nghiệm ngôn ngữ tự nhiên (natural-language prior) được khai thác trực tiếp bởi quá trình tổng hợp có LLM định hướng (LLM-guided synthesis).
