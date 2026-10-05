### 5.4 Feature Diversity

* **Mục tiêu và hệ thống độ đo đa dạng hình học bổ trợ (geometrically complementary diversity metrics)**:
  * Đánh giá chất lượng cấu trúc (structural quality) và độ phong phú thông tin (informational richness) của các tập đặc trưng kỹ thuật do từng phương pháp tạo ra thông qua hai độ đo bổ trợ hình học: MPOC và EffRank.
* **Mean Pairwise Output Correlation (MPOC) — Đo lường độ dư thừa cục bộ theo cặp (local pairwise redundancy)**:
  * MPOC được định nghĩa là giá trị tuyệt đối trung bình của hệ số tương quan hạng Spearman (Spearman rank correlation) giữa tất cả các cặp vector đầu ra trong tập đặc trưng kỹ thuật được chấp nhận $\Phi$:
    $$\text{MPOC}(\Phi) = \frac{2}{|\Phi|(|\Phi| - 1)} \sum_{i < j} |\rho_{\text{sp}}(\phi_i(X), \phi_j(X))|$$
    trong đó $\rho_{\text{sp}}$ ký hiệu hệ số tương quan hạng Spearman đánh giá trên tập huấn luyện (training set).
  * Ý nghĩa hình học: Giá trị MPOC càng thấp ($\downarrow$) biểu thị các đặc trưng được chấp nhận chứa ít thông tin dư thừa hơn, với các vector đầu ra trải rộng trên một không gian con lớn hơn của $\mathbb{R}^n$ thay vì sụp đổ (collapsing) thành một khối tương quan hạng thấp (low-rank correlated block).
* **Effective Rank (EffRank) — Đo lường độ bao phủ chiều toàn cục (global dimensional coverage)**:
  * EffRank đo lường độ bao phủ chiều toàn cục dựa trên phổ giá trị suy biến chuẩn hóa (normalized singular-value spectrum) của ma trận đặc trưng kỹ thuật:
    $$\text{EffRank}(\Phi) = \exp \left( - \sum_{k=1}^r \tilde{\sigma}_k \log \tilde{\sigma}_k \right), \quad \text{với } \tilde{\sigma}_k = \frac{\sigma_k}{\sum_{j=1}^r \sigma_j}$$
    trong đó $\{\sigma_k\}_{k=1}^r$ là các giá trị suy biến (singular values).
  * Chuẩn hóa: Báo cáo EffRank được chuẩn hóa theo kích thước tập đặc trưng $|\Phi|$ để đảm bảo tính so sánh công bằng giữa các phương pháp có số lượng đặc trưng được chấp nhận khác nhau.
  * Ý nghĩa hình học: Giá trị EffRank càng cao ($\uparrow$) biểu thị độ bao phủ rộng hơn của các hướng đặc trưng độc lập (independent feature directions).
* **Kết quả thực nghiệm về độ đa dạng đặc trưng (Table 5)**:
  * Bảng 5 so sánh MPOC và Effective Rank trung bình trên tất cả các tập dữ liệu phân loại (classification) và hồi quy (regression) giữa các phương pháp:

| Method | Classification: MPOC $\downarrow$ | Classification: EffRank $\uparrow$ | Regression: MPOC $\downarrow$ | Regression: EffRank $\uparrow$ |
| :--- | :---: | :---: | :---: | :---: |
| OpenFE | 0.421 | 0.480 | 0.378 | 0.448 |
| AutoFeat | 0.513 | 0.330 | 0.486 | 0.309 |
| FeatLLM | 0.581 | 0.394 | 0.462 | 0.389 |
| CAAFE | 0.479 | 0.567 | 0.382 | 0.412 |
| LLMFE | 0.309 | 0.699 | 0.320 | 0.631 |
| TOPOFE | **0.261** | **0.832** | **0.232** | **0.680** |

* **Tính tối ưu đồng thời (joint optimality) của TOPOFE**:
  * TOPOFE đạt MPOC thấp nhất ($0.261$ trên classification, $0.232$ trên regression) và EffRank cao nhất ($0.832$ trên classification, $0.680$ trên regression) trên cả hai bài toán phân loại và hồi quy.
  * Thiết lập tính tối ưu đồng thời trong việc vừa triệt tiêu độ dư thừa (redundancy suppression) vừa tối đa hóa độ bao phủ không gian con (subspace coverage) mà không phương pháp cạnh tranh nào đạt được.
* **Phân tích cơ chế của các chế độ thất bại (mechanistically distinct failure modes) ở các phương pháp đối chuẩn**:
  * **AutoFeat**: Đạt MPOC cao nhất và EffRank thấp nhất do quá trình liệt kê đa thức (polynomial enumeration) sinh ra các đặc trưng có tương quan đơn điệu mạnh mẽ, làm phổ giá trị suy biến sụp đổ vào một vài hướng chi phối.
  * **FeatLLM**: Chịu mức MPOC cao và EffRank thấp do hiện tượng gom cụm theo chủ đề (thematic clustering) của các đề xuất LLM phi trạng thái (stateless LLM proposals) — tuy mạch lạc về mặt ngữ nghĩa nhưng lại dư thừa về mặt thông tin.
  * **CAAFE và OpenFE**: Nằm ở chế độ trung gian (intermediate regime), nơi cơ chế phản hồi lặp (iterative feedback) và feature boosting phần nào triệt tiêu được dư thừa nhưng vẫn bị giới hạn trong một ngữ pháp toán tử đơn lẻ (single operator grammar), ngăn cản đạt EffRank cao.
  * **LLM-FE**: Có cải thiện đáng kể nhưng bị giới hạn bởi các đảo đồng nhất, bất khả tri về ngữ pháp (homogeneous, grammar-agnostic islands), khiến ma trận đặc trưng bị cô đọng trong một không gian con toán tử đơn nhất không phân hóa.
* **Cơ chế kiến trúc tạo nên ưu thế vượt trội của TOPOFE**:
  * **Bộ lọc dư thừa rõ ràng trong quá trình tìm kiếm (explicit within-search redundancy filter)**: Ngăn chặn các cụm tương quan tích lũy, trực tiếp kéo giảm MPOC.
  * **Lược đồ họ không đồng nhất kết hợp tổng hợp lai chéo họ (heterogeneous family schema & cross-family hybrid synthesis)**: Nhập khẩu các mẫu cấu trúc trực giao (structurally orthogonal templates) từ các đảo tiền thân vào ngữ pháp mục tiêu, trực tiếp gia tăng EffRank.
  * Sự kết hợp của hai cơ chế bổ trợ này tạo nên dấu ấn hình học (geometric signature) minh chứng cho tính ưu việt về mặt kiến trúc của TOPOFE.
