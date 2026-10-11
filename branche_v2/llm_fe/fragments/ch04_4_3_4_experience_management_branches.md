### 3.4 Experience Management

- **Mục tiêu và Vai trò của Quản lý Kinh nghiệm (Experience Management)**:
  - Khắc phục sự bế tắc tại các cực trị địa phương (local optima) và thúc đẩy việc khám phá các đặc trưng đa dạng (diverse feature discovery).
  - Ứng dụng cơ chế **quản lý kinh nghiệm tiến hóa đa quần thể (evolutionary multi-population experience management)** (minh họa tại Figure 1(d)) nhằm lưu trữ các chương trình khám phá đặc trưng (feature discovery programs) vào một cơ sở dữ liệu chuyên dụng.
  - Sử dụng các mẫu trích xuất từ cơ sở dữ liệu này để cấu trúc các ví dụ ngữ cảnh (in-context examples) cung cấp cho mô hình ngôn ngữ lớn (LLM - Large Language Model), từ đó hỗ trợ LLM sinh ra các biến đổi đặc trưng mới lạ.
  - Quy trình quản lý kinh nghiệm gồm hai thành phần cốt lõi:
    - **(i) Bộ nhớ đa quần thể (multi-population memory)**: Duy trì một bộ đệm bộ nhớ dài hạn (long-term memory buffer) chứa các chương trình đã đánh giá.
    - **(ii) Lấy mẫu từ bộ đệm bộ nhớ (sampling from memory buffer)**: Chọn lọc các chương trình tiêu biểu từ bộ đệm để xây dựng các mẫu minh họa ngữ cảnh (in-context example demonstrations).
  - Sau khi đánh giá các phép biến đổi đặc trưng tại vòng lặp (iteration) $t$, cặp phép biến đổi và điểm số $(T, s)$ được lưu trữ vào bộ đệm quần thể $P_t$ để tinh chỉnh quá trình tìm kiếm lặp qua từng thế hệ.

- **Mô hình Đa Quần thể Đảo (Multi-Population 'Island' Model)**:
  - Để tiến hóa quần thể chương trình một cách hiệu quả, LLM-FE áp dụng mô hình đa quần thể lấy cảm hứng từ mô hình đảo ('island' model) (Cranmer, 2023; Romera-Paredes et al., 2024; Shojaee et al., 2025).
  - Quần thể chương trình được phân chia thành $m$ đảo độc lập (independent islands):
    - Mỗi đảo đều có quyền truy cập vào toàn bộ tập đặc trưng gốc (original feature set) ban đầu, nhưng thực hiện tiến hóa hoàn toàn riêng biệt.
    - Mỗi đảo được khởi tạo bằng một bản sao của ví dụ mẫu ban đầu từ người dùng (user's initial example, xem Figure 9(d)).
  - Cho phép khám phá song song (parallel exploration) không gian đặc trưng, giảm thiểu nguy cơ mắc kẹt trong các giải pháp dưới mức tối ưu (suboptimal solutions).
  - Quy trình chọn đảo và cập nhật nghiệm:
    - Tại mỗi vòng lặp $t$, hệ thống chọn ngẫu nhiên một trong số $m$ đảo và lấy mẫu các chương trình từ bộ đệm bộ nhớ của đảo đó để cập nhật prompt với các ví dụ ngữ cảnh mới.
    - Đánh giá $b$ mẫu đặc trưng mới sinh; nếu điểm số $s_j$ của mẫu mới vượt qua điểm số tốt nhất hiện tại, cặp đặc trưng - điểm số $(T_j, s_j)$ sẽ được nạp bổ sung vào chính hòn đảo đã dùng để lấy mẫu ví dụ ngữ cảnh.

- **Phân cụm theo Chữ ký Chương trình (Program Signature Clustering) và Chọn lọc Boltzmann (Boltzmann Sampling)**:
  - **Bảo toàn tính đa dạng quần thể (Preserving Diversity)**: Để đảm bảo các chương trình có đặc tính hiệu năng khác nhau cùng được duy trì trong bộ đệm, các chương trình trong mỗi đảo được phân cụm dựa trên **chữ ký chương trình (program signature)**, định nghĩa bởi điểm hiệu năng kiểm định (validation performance score) $s$.
    - Cụ thể: các chương trình biến đổi đặc trưng tạo ra điểm kiểm định giống hệt nhau sẽ được gộp chung vào cùng một cụm (cluster).
  - **Quy trình lấy mẫu hai giai đoạn (Two-step sampling mechanism)** (theo Romera-Paredes et al., 2024; Shojaee et al., 2025):
    - Giai đoạn 1: Lấy mẫu từ một trong số $m$ đảo khả dụng.
    - Giai đoạn 2: Lấy mẫu $k$ chương trình từ đảo đã chọn để tạo các ví dụ ngữ cảnh $k$-shot ($k$-shot in-context examples) cho LLM (chi tiết tại Appendix B.1).
  - **Cơ chế chọn lọc cụm Boltzmann (Boltzmann cluster selection)** (De La Maza & Tidor, 1992):
    - Gán xác suất lựa chọn cao hơn cho các cụm có điểm số trung bình cao hơn theo phân phối xác suất dựa trên điểm số:
      $$P_i = \frac{\exp(s_i / \tau_c)}{\sum_i \exp(s_i / \tau_c)}$$
      trong đó:
      - $s_i$ biểu thị điểm số trung bình (mean score) của cụm thứ $i$.
      - $\tau_c$ là tham số nhiệt độ (temperature parameter).
    - Tham số nhiệt độ $\tau_c$ kiểm soát sự đánh đổi giữa khám phá và khai thác (exploration–exploitation trade-off):
      - $\tau_c$ thấp: tập trung phần lớn khối lượng xác suất vào cụm có điểm số cao nhất (khai thác - exploitation).
      - $\tau_c$ cao: phân bổ khối lượng xác suất đồng đều hơn giữa các cụm (khám phá - exploration).
  - Các chương trình biến đổi đặc trưng được lấy mẫu từ bộ đệm bộ nhớ sau đó được ghép vào prompt làm ví dụ ngữ cảnh để định hướng LLM sinh ra các biến đổi đặc trưng hiệu quả hơn (chi tiết chiến lược quản lý bộ nhớ, quy trình phân cụm và cơ chế lấy mẫu được trình bày tại Appendix B.1).

- **Thuật toán Khung LLM-FE (Algorithm 1: LLM-FE Pseudocode)**:
  - Cấu trúc giả mã quy trình tìm kiếm tiến hóa của LLM-FE:
    ```text
    Algorithm 1 LLM-FE
    Require: Dataset D, Metadata M, Iterations T, Model f, LLM π_θ, Metric E
     1: P_0 ← BufferInit()
     2: T*, s* ← null, -∞
     3: p ← UpdatePrompt(D, M)
     4: for t = 1 to T do
     5:     p_t ← p + P_{t-1}.topk()
     6:     {T_j}_{j=1}^b ← π_θ(p_t)
     7:     for j = 1 to b do
     8:         s_j ← FeatureScore(f, T_j, D, E)
     9:         if s_j > s* then
    10:             T*, s* ← T_j, s_j
    11:         end if
    12:         P_t ← UpdateBuffer(P_{t-1}, Tj, sj)
    13:     end for
    14: end for
    15: return T*, s*
    ```
  - **Chi tiết các bước thực thi tuần tự của thuật toán**:
    - **Bước 1 (Khởi tạo - Initialization)**:
      - Gọi hàm `BufferInit()` để khởi tạo bộ đệm bộ nhớ $P_0$ với quần thể ban đầu chứa một phép biến đổi đặc trưng đơn giản, đóng vai trò điểm xuất phát cho tìm kiếm tiến hóa các chương trình biến đổi đặc trưng ở các bước kế tiếp.
      - Thiết lập nghiệm tối ưu ban đầu $T^* \leftarrow \text{null}$, điểm số tối ưu $s^* \leftarrow -\infty$.
      - Xây dựng prompt cơ sở $p \leftarrow \text{UpdatePrompt}(D, M)$ dựa trên tập dữ liệu $D$ và siêu dữ liệu $M$.
    - **Bước 2 (Vòng lặp tiến hóa - Evolutionary loop qua $t = 1 \dots T$)**:
      - Áp dụng hàm `topk()` để lấy mẫu $k$ ví dụ in-context từ quần thể thế hệ trước $P_{t-1}$, cập nhật prompt: $p_t \leftarrow p + P_{t-1}.\text{topk}()$.
      - Truy vấn mô hình ngôn ngữ lớn $\pi_\theta(p_t)$ bằng prompt đã cập nhật để lấy mẫu $b$ chương trình biến đổi đặc trưng mới $\{T_j\}_{j=1}^b$.
      - Với từng chương trình ứng viên $T_j$ ($j = 1 \dots b$):
        - Đánh giá chất lượng bằng hàm `FeatureScore(f, T_j, D, E)` theo quy trình Đánh giá Dựa trên Dữ liệu (Section 3.3).
        - Nếu điểm số $s_j$ vượt trội hơn kỷ lục hiện tại $s^*$, cập nhật nghiệm tốt nhất: $T^* \leftarrow T_j$ và $s^* \leftarrow s_j$.
        - Cập nhật bộ đệm bộ nhớ thông qua `UpdateBuffer(P_{t-1}, Tj, sj)` để hình thành quần thể thế hệ $P_t$.
    - **Bước 3 (Trả về kết quả tối ưu - Return optimal solution)**:
      - Sau khi hoàn thành $T$ vòng lặp tiến hóa, thuật toán trả về chương trình đạt điểm cao nhất $T^*$ từ $P_t$ cùng điểm số tương ứng $s^*$ làm giải pháp tối ưu tìm được cho bài toán.

- **Cơ chế Tiến hóa Ngầm định qua Gợi ý Ngữ cảnh (Implicit Evolution via Prompt-Conditioned Generation)**:
  - LLM-FE sử dụng cơ chế tìm kiếm lặp (iterative search) để hoàn thiện và nâng cao chất lượng các chương trình bằng cách khai thác tối đa năng lực của LLM.
  - Thông qua việc học hỏi từ kho kinh nghiệm liên tục tiến hóa trong bộ đệm, LLM tự định hướng không gian tìm kiếm về phía các giải pháp hiệu quả cao.
  - **Khác biệt bản chất so với các thuật toán tiến hóa cổ điển (classical evolutionary algorithms)**:
    - Thuật toán tiến hóa cổ điển: áp dụng các toán tử đột biến (mutation) hoặc lai ghép (crossover) một cách tường minh (explicit).
    - LLM-FE: thực hiện quá trình tiến hóa một cách ngầm định (implicitly) thông qua cơ chế sinh có điều kiện định hướng bởi prompt (prompt-conditioned generation).
    - Các chương trình thành công ở các thế hệ trước, khi được đưa vào prompt dưới dạng các ví dụ in-context, sẽ định hướng LLM tự động tạo ra các biến thể cải tiến của từng chương trình đơn lẻ cũng như lai ghép, kết hợp các đặc trưng ưu việt từ nhiều chương trình khác nhau.
