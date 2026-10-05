### 3.2 Prompt Adaptation Memory

* **Nhu cầu thích ứng trực tuyến (online adaptation) của cơ chế đề xuất:**
  * Mặc dù tri thức tiền huấn luyện (pretrained knowledge) của mô hình ngôn ngữ lớn (LLM) cung cấp một tiên nghiệm (prior) mạnh mẽ cho các chương trình đặc trưng (feature programs), việc tìm kiếm hiệu quả đòi hỏi cơ chế đề xuất phải thích ứng trực tuyến với không gian tìm kiếm (landscape) đang biến chuyển của từng đảo (island).
  * Nếu không có sự thích ứng, LLM sẽ liên tục đề xuất các chương trình ở những vùng không gian đã được xác định là không hiệu quả, gây lãng phí ngân sách đánh giá (evaluation budget).
* **Định nghĩa Prompt Adaptation Memory (PAM) (Bộ nhớ thích ứng Prompt):**
  * PAM là một cơ chế nhẹ (lightweight) riêng cho từng đảo, liên tục định hình phân phối đề xuất (proposal distribution) của LLM từ kinh nghiệm tìm kiếm tích lũy mà không cần cập nhật bất kỳ tham số nào (without any parameter update).
  * PAM hoạt động thông qua ba quy tắc cập nhật phối hợp được áp dụng sau mỗi thế hệ (generation): cập nhật bộ nhớ prompt (prompt-memory update), cập nhật kho lưu trữ tinh hoa (elite archive update), và điều kiện hóa đề xuất (proposal conditioning).

#### 3.2.1 Prompt-memory Update

* **Phân loại tín hiệu ưu tiên và cần tránh từ cửa sổ lịch sử trượt:**
  * Ký hiệu $\mathcal{H}_i^+(t)$ và $\mathcal{H}_i^-(t)$ lần lượt là tập con các chương trình được chấp nhận (accepted) và bị từ chối (rejected) trong cửa sổ lịch sử trượt (sliding history window) $[t - W, t]$.
  * Các loại toán tử (operator types) tập trung nhiều trong các chương trình được chấp nhận sẽ được củng cố làm tín hiệu ưu tiên (*prefer signals*).
  * Các loại toán tử tập trung nhiều trong các chương trình bị từ chối sẽ được gắn cờ làm tín hiệu cần tránh (*avoid signals*).
* **Quy tắc cập nhật bộ nhớ prompt:**
  $$\rho_i^{(t+1)} = \text{Summarize}\left(\mathcal{H}_i^+(t), \mathcal{H}_i^-(t), \rho_i^{(t)}\right) \tag{8}$$
  * Trong đó, $\text{Summarize}(\cdot)$ là một lệnh gọi LLM để tạo ra một chuỗi ngôn ngữ tự nhiên cô đọng (ví dụ: *"prefer ratio features with lagged denominators, avoid log transforms of sparse columns"*).
  * Chuỗi ngôn ngữ tự nhiên này được thêm vào đầu (prepended) tất cả các prompt tiếp theo cho đảo $i$.

#### 3.2.2 Elite Archive Update

* **Cập nhật và cắt tỉa kho lưu trữ tinh hoa (Elite Archive Update):**
  * Sau mỗi thế hệ, kho lưu trữ $\mathcal{A}_i^{(t)}$ hợp nhất các chương trình mới được chấp nhận, xếp hạng lại theo $\hat{\Phi}$, và cắt tỉa về dung lượng tối đa $|\mathcal{A}|_{\max}$:
    $$\mathcal{A}_i^{(t+1)} = \text{TopK}\left(\mathcal{A}_i^{(t)} \cup \{p : a_t = 1\}, |\mathcal{A}|_{\max}, \hat{\Phi}\right) \tag{9}$$
* **Kiểm soát tính mới về cấu trúc (structural novelty):**
  * Các ứng viên có khoảng cách chỉnh sửa cây chuẩn hóa (normalized tree-edit distance) tới bất kỳ thành viên hiện có nào trong kho lưu trữ thấp hơn ngưỡng $\delta_{\min}$ sẽ bị loại bỏ trước khi chèn vào, nhằm đảm bảo tính mới về mặt cấu trúc.
* **Vai trò kép của kho lưu trữ:**
  * Kho lưu trữ vừa đóng vai trò là tập hợp mẫu minh họa theo ngữ cảnh (in-context demonstration pool) cho các đề xuất nội đảo (intra-island proposals).
  * Vừa đóng vai trò là nguồn ứng viên cho quá trình tổng hợp liên đảo (cross-island synthesis).

#### 3.2.3 Proposal Conditioning

* **Cơ chế điều kiện hóa ba thành phần (Three-way Proposal Conditioning):**
  * Mọi lệnh gọi LLM cho đảo $i$ tại thế hệ $t$ đều được điều kiện hóa theo:
    $$\text{Context}_i^{(t)} = \left(M, \rho_i^{(t)}, \text{Sample}\left(\mathcal{A}_i^{(t)}, n\right)\right) \tag{10}$$
  * Trong đó, $M$ neo giữ đề xuất vào tri thức miền (domain knowledge).
  * $\rho_i^{(t)}$ định hướng đề xuất bằng các sở thích tìm kiếm tích lũy (accumulated search preferences).
  * $\text{Sample}\left(\mathcal{A}_i^{(t)}, n\right)$ minh họa đề xuất bằng $m$ chương trình đạt điểm cao nhất được phát hiện cho đến nay.
* **Khép kín vòng lặp phản hồi (Feedback loop):**
  * Cơ chế điều kiện hóa ba thành phần này khép kín vòng lặp phản hồi đã giới thiệu: lịch sử định hình bộ nhớ, bộ nhớ định hướng các đề xuất, và các đề xuất được chấp nhận làm giàu thêm cho kho lưu trữ.
