### 3.2 Prompt Adaptation Memory

* Vai trò của tri thức tiền huấn luyện (pretrained knowledge) của mô hình ngôn ngữ lớn (LLM):
  * Cung cấp một tiên nghiệm mạnh mẽ (strong prior) đối với các chương trình đặc trưng (feature programs).
* Thách thức trong quá trình tìm kiếm đặc trưng hiệu quả:
  * Đòi hỏi cơ chế đề xuất (proposal mechanism) phải thích ứng trực tuyến (adapt online) với địa hình cảnh quan đang biến đổi liên tục (evolving landscape) của từng đảo (island).
  * Nếu không có sự thích ứng trực tuyến, LLM sẽ lặp đi lặp lại việc đề xuất các chương trình trong những vùng không gian đã được xác định là không hiệu quả (unproductive regions), dẫn đến lãng phí nghiêm trọng ngân sách đánh giá (evaluation budget).
* Đề xuất cơ chế Bộ nhớ thích ứng prompt (Prompt Adaptation Memory - PAM):
  * PAM là một cơ chế gọn nhẹ trên từng đảo (lightweight per-island mechanism), liên tục định hình phân phối đề xuất (proposal distribution) của LLM dựa trên kinh nghiệm tìm kiếm tích lũy (accumulated search experience).
  * PAM vận hành hoàn toàn không cần bất kỳ sự cập nhật tham số mô hình nào (without any parameter update).
  * PAM hoạt động thông qua $3$ quy tắc cập nhật phối hợp chặt chẽ (coordinated update rules), được áp dụng sau mỗi thế hệ tìm kiếm (generation).

#### 3.2.1 Prompt-memory Update

* Định nghĩa tập hợp lịch sử trượt:
  * Ký hiệu $\mathcal{H}^+_i(t)$ và $\mathcal{H}^-_i(t)$ lần lượt là tập con các chương trình được chấp nhận (accepted subset) và tập con các chương trình bị từ chối (rejected subset) trong cửa sổ lịch sử trượt (sliding history window) $[t - W, t]$.
* Cơ chế hình thành tín hiệu định hướng:
  * Các loại toán tử (operator types) tập trung chủ yếu trong số các chương trình được chấp nhận ($\mathcal{H}^+_i(t)$) được củng cố thành các tín hiệu ưu tiên (prefer signals).
  * Các loại toán tử tập trung trong số các chương trình bị từ chối ($\mathcal{H}^-_i(t)$) được gắn cờ thành các tín hiệu cần tránh (avoid signals).
* Quy tắc cập nhật bộ nhớ prompt hình thức hóa:
  $$\rho^{(t+1)}_i = \text{Summarize}\left(\mathcal{H}^+_i(t), \mathcal{H}^-_i(t), \rho^{(t)}_i\right) \tag{8}$$
  * Trong đó:
    * $\rho^{(t)}_i$ là chuỗi bộ nhớ prompt của đảo $i$ tại thế hệ $t$.
    * $\rho^{(t+1)}_i$ là chuỗi bộ nhớ prompt của đảo $i$ được cập nhật cho thế hệ $t+1$.
    * $\text{Summarize}(\cdot)$ là một lệnh gọi LLM (LLM call) có nhiệm vụ tổng hợp và tạo ra một chuỗi ngôn ngữ tự nhiên cô đọng (compact natural-language string).
    * Ví dụ về chuỗi bộ nhớ được sinh ra: *"prefer ratio features with lagged denominators, avoid log transforms of sparse columns"* (ưu tiên các đặc trưng tỷ lệ có mẫu số trễ, tránh các phép biến đổi log trên các cột dữ liệu thưa).
    * Chuỗi ngôn ngữ tự nhiên này được gắn vào phần đầu (prepended) của tất cả các prompt tiếp theo dành cho đảo $i$.

#### 3.2.2 Elite Archive Update

* Quy trình cập nhật kho lưu trữ tinh hoa sau mỗi thế hệ:
  * Sau mỗi thế hệ $t$, kho lưu trữ tinh hoa $\mathcal{A}^{(t)}_i$ của đảo $i$ hợp nhất các chương trình mới được chấp nhận, xếp hạng lại theo hàm mục tiêu $\hat{\Phi}$, và cắt tỉa về dung lượng tối đa $|\mathcal{A}|_{\max}$.
* Công thức cập nhật kho lưu trữ tinh hoa:
  $$\mathcal{A}^{(t+1)}_i = \text{TopK}\left(\mathcal{A}^{(t)}_i \cup \{p : a_t = 1\}, |\mathcal{A}|_{\max}, \hat{\Phi}\right) \tag{9}$$
  * Trong đó:
    * $\mathcal{A}^{(t)}_i$ là kho lưu trữ tinh hoa hiện tại của đảo $i$ ở thế hệ $t$.
    * $\{p : a_t = 1\}$ là tập hợp các chương trình ứng viên $p$ mới được chấp nhận tại thế hệ $t$ ($a_t = 1$).
    * $|\mathcal{A}|_{\max}$ là dung lượng giới hạn tối đa của kho lưu trữ (archive capacity).
    * $\hat{\Phi}$ là hàm mục tiêu dùng để đánh giá và xếp hạng độ ưu tú của các chương trình đặc trưng.
    * $\text{TopK}(\cdot)$ là toán tử chọn ra $K$ chương trình có điểm số cao nhất theo hàm đánh giá $\hat{\Phi}$.
* Điều kiện sàng lọc tính mới về mặt cấu trúc (structural novelty):
  * Các chương trình ứng viên có khoảng cách chỉnh sửa cây chuẩn hóa (normalized tree-edit distance) tới bất kỳ thành viên hiện hữu nào trong kho lưu trữ nhỏ hơn ngưỡng $\delta_{\min}$ sẽ bị loại bỏ trước khi chèn vào kho.
  * Tiêu chí này bắt buộc đảm bảo tính mới về mặt cấu trúc (enforcing structural novelty) cho tập hợp các chương trình đặc trưng tinh hoa.
* Vai trò kép của kho lưu trữ tinh hoa:
  * Đóng vai trò là tập biểu diễn mẫu trong ngữ cảnh (in-context demonstration pool) phục vụ cho các đề xuất tiến hóa nội đảo (intra-island proposals).
  * Đóng vai trò là nguồn ứng viên (candidate source) cung cấp đầu vào cho quá trình tổng hợp liên đảo (cross-island synthesis).

#### 3.2.3 Proposal Conditioning

* Điều kiện hóa ngữ cảnh cho các lệnh gọi LLM:
  * Mọi lệnh gọi LLM cho đảo $i$ tại thế hệ $t$ đều được điều kiện hóa trên bộ ba ngữ cảnh $\text{Context}^{(t)}_i$:
    $$\text{Context}^{(t)}_i = \left\langle \mathcal{M}, \rho^{(t)}_i, \text{Sample}\left(\mathcal{A}^{(t)}_i, n\right) \right\rangle \tag{10}$$
    * Trong đó:
      * $\mathcal{M}$ neo giữ đề xuất trong tri thức miền (domain knowledge) của tập dữ liệu.
      * $\rho^{(t)}_i$ định hướng đề xuất bằng các sở thích tìm kiếm tích lũy (accumulated search preferences) từ bộ nhớ prompt.
      * $\text{Sample}\left(\mathcal{A}^{(t)}_i, n\right)$ minh họa đề xuất thông qua các chương trình đạt điểm cao nhất được phát hiện cho đến nay (nguồn văn bản nêu lấy mẫu $n$ chương trình và minh họa bằng $m$ chương trình có điểm số cao nhất).
* Cơ chế khép kín vòng lặp phản hồi (closed feedback loop):
  * Việc điều kiện hóa ba chiều này hoàn tất và khép kín vòng lặp phản hồi trong tìm kiếm tiến hóa:
    * Lịch sử định hình bộ nhớ (history shapes memory): các quyết định chấp nhận/từ chối trong cửa sổ trượt cập nhật nên bộ nhớ prompt $\rho^{(t)}_i$.
    * Bộ nhớ định hướng đề xuất (memory steers proposals): chuỗi $\rho^{(t)}_i$ dẫn dắt và uốn nắn phân phối đề xuất của LLM.
    * Đề xuất được chấp nhận làm phong phú kho lưu trữ (accepted proposals enrich the archive): các ứng viên thành công tiếp tục được bổ sung vào $\mathcal{A}^{(t)}_i$.
