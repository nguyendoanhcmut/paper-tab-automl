## 6 Related Work

* **Tổng quan các hướng tiếp cận liên quan:**
  * TOPOFE kết nối và định vị sự đổi mới giữa ba lĩnh vực nghiên cứu chính:
    * Kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE).
    * Mô hình ngôn ngữ lớn cho học dữ liệu dạng bảng (LLMs for Tabular Data Learning).
    * Tìm kiếm tiến hóa có hướng dẫn bởi mô hình ngôn ngữ lớn (LLM-guided Evolutionary Search).

### 6.1 Automatic Feature Engineering

* **Tiến trình phát triển của Kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE):**
  * AutoFE đã tiến hóa qua ba mô hình lớn (three broad paradigms):
    * Phương pháp dựa trên tìm kiếm (Search-based methods).
    * Phương pháp dẫn dắt bởi LLM (LLM-guided methods).
    * Phương pháp tiến hóa kết hợp LLM (LLM-evolutionary methods).
* **Phương pháp dựa trên tìm kiếm (Search-based methods):**
  * *Bản chất mô hình hóa:* Xử lý việc xây dựng đặc trưng (feature construction) như một bài toán tối ưu hóa tổ hợp (combinatorial optimization problem).
  * *Các thuật toán tìm kiếm tiêu biểu:*
    * Lập trình di truyền (genetic programming) [Olson and Moore, 2016].
    * Tìm kiếm vét cạn (exhaustive search) [Horn et al., 2019].
    * Tìm kiếm tham lam (greedy search) [Zhang et al., 2023a].
  * *Hạn chế cốt lõi:*
    * Chi phí tính toán đắt đỏ (computationally expensive).
    * Bất khả tri miền dữ liệu và hoàn toàn thiếu vắng sự định hướng ngữ nghĩa (domain-agnostic without semantic guidance).
* **Phương pháp dẫn dắt bởi LLM (LLM-guided methods):**
  * *Cơ chế hoạt động:* Tận dụng các mô hình ngôn ngữ tiền huấn luyện (pretrained LMs) để đề xuất đặc trưng [Han et al., 2024; Ko et al., 2025; Nam et al., 2024] dựa trên mô tả nhiệm vụ (task descriptions) và siêu dữ liệu tập dữ liệu (dataset metadata) [Hollmann et al., 2023a].
  * *Các mở rộng suy luận tiên tiến gần đây:*
    * Áp dụng suy luận Cây suy nghĩ (Tree-of-Thought reasoning) [Zhang et al., 2025].
    * Khung làm việc đa tác tử (multi-agent frameworks) [Ouyang et al., 2025].
    * Các tác tử dựa trên ReAct (ReAct-based agents) [Burghardt et al., 2026] để định hướng quá trình khám phá đặc trưng (feature discovery).
  * *Hạn chế cốt lõi:*
    * Hoàn toàn phụ thuộc vào kỹ thuật nhắc lệnh thuần túy (rely on prompting).
    * Dẫn đến việc lặp lại các đề xuất đặc trưng (repeated proposals).
    * Không có khả năng thích ứng theo từng tập dữ liệu cụ thể (no dataset-specific adaptation).
    * Không hỗ trợ khả năng tổ hợp và liên kết giữa các họ biến đổi khác nhau (no cross-family composition).
* **Phương pháp tiến hóa kết hợp LLM (LLM-evolutionary methods):**
  * *Cơ chế hoạt động:* Kết hợp khả năng sinh chương trình của LLM (LLM-based generation) với tìm kiếm tiến hóa (evolutionary search) [Abhyankar et al., 2025; Gong et al., 2025; Batista, 2025].
  * *Ưu thế:* Đạt được sự cải tiến rõ rệt so với phương pháp nhắc lệnh tĩnh (static prompting).
  * *Hạn chế cốt lõi:*
    * Chỉ vận hành trên một quần thể đơn lẻ (single population) mà không có sự phân tách cấu trúc của không gian chương trình (without structural decomposition of the program space).
    * Ngăn cản quá trình lai ghép liên họ (precluding cross-family hybridization).
    * Khiến quá trình tìm kiếm dễ rơi vào bẫy hội tụ sớm (premature convergence) bên trong một họ biến đổi chiếm ưu thế (dominant transformation family).
* **Giải pháp khắc phục của TOPOFE:**
  * TOPOFE giải quyết trực tiếp các hạn chế trên thông qua ba cơ chế tích hợp:
    * Phân tách đa đảo (multi-island decomposition).
    * Bộ nhớ thích ứng prompt (prompt adaptation memory - PAM).
    * Chuyển giao tri thức liên họ theo định hướng của đồ thị tô pô (topology-guided cross-family transfer).

### 6.2 LLMs for Tabular Data Learning

* **Hai mô hình tiếp cận chính trong học trên dữ liệu dạng bảng (Tabular learning):**
  * Các tiến bộ gần đây trong học dữ liệu bảng đã hội tụ về hai mô hình chính (two main paradigms):
    * Mô hình nền tảng dạng bảng (Tabular foundation models).
    * Phương pháp dữ liệu bảng dựa trên LLM (LLM-based tabular methods).
* **Mô hình nền tảng dạng bảng (Tabular foundation models):**
  * *Mục tiêu theo đuổi:* Khả năng chuyển giao xuyên bảng (cross-table transferability) thông qua tiền huấn luyện quy mô lớn (large-scale pretraining).
  * *Các hướng nghiên cứu tiêu biểu:*
    * Xấp xỉ suy diễn Bayes (Bayesian inference approximation) thông qua Mạng khớp dữ liệu tiên nghiệm (Prior-Data Fitted Networks - TabPFN) [Hollmann et al., 2023b, 2025].
    * Mở rộng quy mô ở cấp độ kiến trúc (architecture-level scaling) phục vụ học trong ngữ cảnh (in-context learning) [Gardner et al., 2024; Arazi et al., 2026; Qu et al., 2025].
    * Suy diễn tăng cường truy xuất (retrieval-augmented inference) mà không cần tinh chỉnh mô hình theo tác vụ cụ thể (without task-specific fine-tuning) [Ma et al., 2025].
* **Phương pháp dữ liệu bảng dựa trên LLM (LLM-based tabular methods):**
  * *Cơ chế hoạt động:* Tái sử dụng (repurpose) các mô hình ngôn ngữ tiền huấn luyện (pretrained LMs) cho nhiều nhiệm vụ khác nhau:
    * Dự đoán với ít mẫu dữ liệu (few-shot prediction) [Hegselmann et al., 2023; Dinh et al., 2022].
    * Khái quát hóa ngữ nghĩa dựa trên siêu dữ liệu dạng văn bản (semantic generalization via textual metadata) [Ye et al., 2024a; Kim et al., 2024; Yan et al.].
    * Thực hiện các tác vụ phụ trợ (auxiliary tasks):
      * Tăng cường dữ liệu (data augmentation) [Zhang et al., 2023b; Borisov et al.].
      * Làm sạch dữ liệu (data cleaning) [Bendinelli et al.].
      * Sinh đặc trưng (feature generation) [Hollmann et al., 2023a].
* **Hạn chế chung và đóng góp của TOPOFE:**
  * Bất chấp các tiến bộ kể trên, các phương pháp hiện tại phần lớn vẫn phụ thuộc vào sự thích ứng trên từng tác vụ (per-task adaptation).
  * Thiếu các cơ chế tìm kiếm có nguyên tắc (principled search mechanisms) trên không gian đặc trưng (feature space).
  * TOPOFE được thiết kế chuyên biệt để cung cấp chính xác cơ chế tìm kiếm có nguyên tắc này.

### 6.3 LLM-guided Evolutionary Search

* **Tích hợp LLM làm toán tử tiến hóa (LLMs as evolutionary operators):**
  * Một khối lượng công trình nghiên cứu đang gia tăng nhanh chóng trong việc tích hợp LLM làm các toán tử tiến hóa trên nhiều lĩnh vực:
    * *Tối ưu hóa câu nhắc (prompt optimization):* [Guo et al., 2023; Fernando et al.; Suzgun et al., 2026; Agrawal et al.].
    * *Khám phá chương trình và thuật toán (program and algorithm discovery):* [Šurina et al.; Assumpção et al., 2025; Novikov et al., 2025; Sharma; Lange et al., 2025].
    * *Khám phá khoa học (scientific discovery):* [Shojaee et al.; Yang et al., 2025b; Chen et al., 2026; Abhyankar et al., 2026].
* **Động lực học quần thể trong các hệ thống tiến hóa dẫn dắt bởi LLM:**
  * Các hệ thống hiện tại có sự biến thiên chủ yếu ở động lực học quần thể (population dynamics):
    * Sử dụng MAP-Elites [Novikov et al., 2025].
    * Tiến hóa dựa trên mô hình đảo (island-based evolution) [Assumpção et al., 2025].
    * Tối ưu hóa trên biên Pareto (Pareto frontier optimization) [Agrawal et al.].
    * Chọn lọc định hướng bởi độ đa dạng (diversity-driven selection) [Sharma].
  * Các khung làm việc nâng cao hơn tích hợp:
    * Đồng tiến hóa và siêu phản xạ (co-evolution and meta-reflection) [Liu et al.; Ye et al., 2024b].
    * Tiến hóa tác tử lặp lại (iterative agent evolution) [Yuan et al., 2025; Shang et al.].
* **Hạn chế cốt lõi của các phương pháp hiện hữu và vai trò trung tâm của TOPOFE:**
  * Bất chấp tính hiệu quả của chúng, các phương pháp hiện tại vẫn đối xử với không gian tìm kiếm như một không gian đồng nhất về mặt cấu trúc (structurally uniform).
  * Hoàn toàn không tích hợp các cơ chế cốt lõi:
    * Phân tách ngữ nghĩa (semantic decomposition).
    * Điều kiện hóa đề xuất thích ứng theo tác vụ (task-adaptive proposal conditioning).
    * Chuyển giao tri thức được kích hoạt bởi sự bão hòa (saturation-triggered transfer).
  * Cả ba cơ chế trên đều là những thành phần trọng tâm, mang tính nền tảng của TOPOFE.
