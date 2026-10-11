## Appendix A Comparison with LLM-based Baselines

* Mặc dù LLM-FE, CAAFE và OCTree đều tận dụng các mô hình ngôn ngữ lớn (Large Language Models — LLMs) cho kỹ thuật đặc trưng tự động (automated feature engineering), các phương pháp này có sự khác biệt căn bản trong cách thức khám phá và tinh chỉnh không gian đặc trưng (feature space).
* **Khám phá song song và đa đường (Parallel and Multi-Path Exploration):**
  * LLM-FE khám phá không gian đặc trưng một cách song song bằng cách tiến hóa đồng thời nhiều chương trình ứng viên (multiple candidate programs) trên nhiều đảo (across islands).
  * CAAFE và OCTree đều tuân theo quy trình tối ưu hóa đơn đường (single-path optimization process), trong đó LLM tinh chỉnh tăng dần từng ứng viên đơn lẻ hoặc từng quy tắc (rule) tại một thời điểm.
* **Bộ nhớ dựa trên quần thể (Population-Based Memory):**
  * Khác với CAAFE và OCTree, LLM-FE duy trì một bộ nhớ ngoài đa quần thể (multi-population external memory) lưu trữ các chương trình đặc trưng đa dạng và có hiệu năng cao qua các vòng lặp (iterations).
* **Thiết kế phản hồi và tinh chỉnh (Feedback and Refinement Design):**
  * LLM-FE áp dụng toán tử đột biến (mutation) và lai ghép (crossover) được định hướng bởi LLM (LLM-guided mutation and crossover) trên nhiều quần thể để thúc đẩy quá trình khám phá (exploration) và tái tổ hợp (recombination).
  * Ngược lại, OCTree dựa vào việc tinh chỉnh quy tắc từng bước (stepwise rule refinement) dựa trên thông tin phản hồi từ cây quyết định (decision-tree feedback).
  * CAAFE áp dụng phương pháp tinh chỉnh dựa trên câu nhắc (prompt-based refinement) mà không sử dụng các toán tử tiến hóa (evolutionary operators).
* **Tác động thực nghiệm (Empirical Impact):**
  * Chiến lược đa đảo (multi-island strategy) giúp giảm thiểu hiện tượng hội tụ sớm (premature convergence) bằng cách bảo tồn tính đa dạng giữa các đảo (preserving diversity across islands).
  * Cơ chế này mang lại mức cải thiện hiệu năng thực nghiệm nhất quán so với cả CAAFE và OCTree (được thể hiện tại Bảng 2 và Bảng 3 — Tables 2 and 3).
* **Độ phức tạp của đặc trưng (Feature Complexity):**
  * Các nghiên cứu trước đây (Küken et al., 2024) chỉ ra rằng các phương pháp dựa trên LLM thường có xu hướng thiên vị các toán tử đặc trưng đơn giản (simple feature operators).
  * Kết quả thực nghiệm tại Hình 4 (Figure 4) cho thấy LLM-FE giảm thiểu hiệu quả độ thiên lệch này (mitigates this bias):
    * Khoảng $45\%$ các đặc trưng được khám phá bởi LLM-FE đạt tiêu chuẩn đặc trưng phức tạp (complex features) theo định nghĩa của Küken et al. (2024).
    * Tỷ lệ đặc trưng phức tạp này là không đáng kể (negligible) đối với CAAFE và OCTree.
