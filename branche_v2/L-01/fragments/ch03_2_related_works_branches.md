## 2 Related Works

* **Kỹ thuật đặc trưng (Feature Engineering):**
  * Kỹ thuật đặc trưng liên quan đến việc tạo ra các đặc trưng có ý nghĩa từ dữ liệu thô nhằm cải thiện hiệu năng dự đoán (predictive performance) (Hollmann et al., 2024).
  * Sự phức tạp ngày càng tăng của các tập dữ liệu đã thúc đẩy việc tự động hóa kỹ thuật đặc trưng nhằm giảm thiểu công sức thủ công và tối ưu hóa việc khám phá đặc trưng.
  * Các phương pháp kỹ thuật đặc trưng tự động truyền thống bao gồm:
    * Khám phá dựa trên cây (tree-based exploration).
    * Liệt kê phép biến đổi (transformation enumeration).
    * Các phương pháp dựa trên học máy (learning-based methods) (Khurana et al., 2016; Kanter & Veeramachaneni, 2015; Nargesian et al., 2017; Zhang et al., 2023).
  * Hạn chế của các phương pháp truyền thống: thường không tận dụng được tri thức miền (domain knowledge) cho việc khám phá đặc trưng.
  * Ưu thế của mô hình ngôn ngữ lớn (LLMs): rất phù hợp cho các tác vụ dự đoán trên dữ liệu dạng bảng (tabular prediction tasks) nhờ vào khả năng hiểu biết ngữ cảnh miền từ trước (prior contextual domain understanding).

* **LLMs và tối ưu hóa (LLMs and Optimization):**
  * Những tiến bộ trong LLMs đã chứng minh khả năng thích ứng với các tác vụ mới thông qua kỹ thuật tạo câu nhắc (prompt engineering) và học theo ngữ cảnh (in-context learning) mà không cần huấn luyện lại mô hình (Brown et al., 2020; Wei et al., 2022).
  * Thách thức của LLMs: kết quả đầu ra có thể không nhất quán hoặc sai lệch thực tế (inconsistent or factually incorrect) (Madaan et al., 2024; Zhu et al., 2023), thúc đẩy các nghiên cứu về cơ chế tinh chỉnh hoặc ổn định các thế hệ sinh (refine or stabilize generations).
  * Khung làm việc kết hợp LLM với bộ đánh giá (evaluators) theo cơ chế lặp hoặc tiến hóa (iterative or evolutionary frameworks):
    * Tận dụng phản hồi (feedback), đột biến (mutation), và lai ghép (crossover) để dẫn dắt quá trình tìm kiếm giải pháp (Lehman et al., 2023; Wu et al., 2024; Meyerson et al., 2024).
    * Đạt được nhiều tiến bộ trong:
      * Tối ưu hóa câu nhắc (prompt optimization) (Yang et al., 2024b; Guo et al., 2024).
      * Tìm kiếm kiến trúc mạng nơ-ron (neural architecture search - NAS) (Zheng et al., 2023; Chen et al., 2023).
      * Khám phá phương pháp suy nghiệm toán học (mathematical heuristic discovery) (Romera-Paredes et al., 2024).
      * Hồi quy ký hiệu (symbolic regression) (Shojaee et al., 2025).
  * Định vị của khung làm việc LLM-FE: hiện thực hóa LLMs như các bộ tối ưu hóa tiến hóa (evolutionary optimizers), kết hợp tri thức tiên nghiệm phong phú với quy trình tinh chỉnh dựa trên dữ liệu có hệ thống (systematic, data-driven refinement) để khám phá các đặc trưng tinh gọn và đạt hiệu năng cao.

* **LLMs cho học trên dữ liệu bảng (LLMs for Tabular Learning):**
  * Việc áp dụng LLM cho dữ liệu có cấu trúc (structured data) thường dựa trên:
    * Chuyển đổi bảng thành biểu diễn văn bản (textual representations) (Dinh et al., 2022; Hegselmann et al., 2023; Wang et al., 2023).
    * Điều chỉnh chiến lược phân tách từ (tokenization) và tiền huấn luyện (pre-training) nhằm tăng độ bền vững trên dữ liệu bảng (Yan et al., 2024).
  * Trong tác vụ dự đoán trên dữ liệu bảng cụ thể:
    * LLM được sử dụng trong mô hình tinh chỉnh (fine-tuning) và học ít mẫu theo ngữ cảnh (few-shot in-context paradigms) (Hegselmann et al., 2023; Nam et al., 2023).
    * LLM được ứng dụng trực tiếp trong kỹ thuật đặc trưng:
      * FeatLLM (Han et al., 2024): tạo ra các quy tắc nhị phân (binary rules).
      * CAAFE (Hollmann et al., 2024): khai thác mô tả tác vụ để tạo ra các đặc trưng theo ngữ cảnh (contextual features).
      * OCTree (Nam et al., 2024): cải thiện đặc trưng lặp đi lặp lại thông qua suy luận cây quyết định (decision tree reasoning).
  * Hạn chế của các phương pháp tiếp cận hiện có: thường phụ thuộc vào việc tinh chỉnh tăng dần trên một ứng viên duy nhất (incremental refinement of a single candidate).
  * Giải pháp đột phá của LLM-FE:
    * Duy trì một tập hợp đa dạng các chương trình triển vọng (diverse pool of promising programs).
    * Áp dụng tìm kiếm tiến hóa (evolutionary search) để duyệt không gian đặc trưng hiệu quả.
    * Tận dụng đột biến (mutation) và lai ghép (crossover) để phát hiện các phép biến đổi vừa dựa trên dữ liệu vừa có khả năng diễn giải (interpretable and data-driven transformations).
    * Thiết kế này cho phép khám phá các đặc trưng không chỉ có năng lực dự đoán cao mà còn có thể diễn giải bởi con người, kết nối khoảng cách giữa suy luận dựa trên tri thức miền (domain-informed reasoning) và tối ưu hóa.
    * Phụ lục A (Appendix A) minh họa chi tiết thêm về sự khác biệt định tính giữa LLM-FE và các phương pháp đối chuẩn (baseline methods).
