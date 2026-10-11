## Abstract

* **Dữ liệu dạng bảng (tabular data) thiếu sức mạnh phân biệt (discriminative power) cần thiết cho mô hình hóa hiệu năng cao:**
  * Là định dạng dữ liệu cốt lõi trong học máy (machine learning), dữ liệu dạng bảng thường thiếu sức mạnh phân biệt do tính giàu thông tin của đặc trưng (feature informativeness) chưa đủ.
  * Kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE) khắc phục hạn chế này bằng cách tự động hóa quá trình sinh đặc trưng (feature generation) và chọn lọc đặc trưng (feature selection), đảm bảo đồng thời hiệu năng mô hình (model performance) và hiệu quả vận hành (operational efficiency).

* **Hạn chế cố hữu của các phương pháp AutoFE hiện nay:**
  * AutoFE truyền thống (traditional AutoFE) thường tạo ra các đặc trưng có khả năng diễn giải kém (poor interpretability) do phụ thuộc vào các phép biến đổi toán học mù quáng (blind mathematical transformations).
  * AutoFE dựa trên mô hình ngôn ngữ lớn (large language models - LLM-based AutoFE) đòi hỏi nhiều vòng lặp tốn kém (costly multi-round iterations) để sinh ra các đặc trưng có độ hữu dụng cao (high-utility features) nhằm cải thiện hiệu năng mô hình một cách hiệu quả.
  * LLM-based AutoFE chịu thêm rủi ro cố hữu về thiên kiến (bias) và ảo giác (hallucination).

* **Phương pháp đề xuất: SymboLLM-FE (kết hợp hồi quy ký hiệu và LLM cho kỹ thuật đặc trưng):**
  * Kết hợp hồi quy ký hiệu (symbolic regression) với LLM cho kỹ thuật đặc trưng nhằm giải quyết đồng thời các thách thức trên.
  * Cơ chế hai giai đoạn:
    * Trích xuất các công thức toán học có tính biểu đạt cao và tương quan mạnh với mục tiêu thông qua symbolic regression để nâng cao hiệu năng mô hình.
    * Tinh chỉnh (refine) các công thức này bằng LLM với tri thức tiên nghiệm phong phú (rich prior knowledge) để bảo đảm khả năng diễn giải (interpretability).

* **Kết quả thực nghiệm và giải quyết thách thức kép:**
  * Kết quả thực nghiệm trên $6$ tập dữ liệu thực tế (real-world datasets) và $4$ cuộc thi Kaggle (Kaggle competitions) chứng minh SymboLLM-FE vượt trội hơn các phương pháp AutoFE hiện có.
  * Giải quyết thách thức kép gồm khả năng diễn giải kém và số lượng vòng lặp lớn nhờ cơ chế tinh chỉnh LLM dựa trên tiên nghiệm thống kê (statistical prior-grounded LLM refinement mechanism).
  * Giảm chi phí vận hành với số lượng lượt gọi LLM chỉ ở mức một chữ số (single-digit LLM calls).
