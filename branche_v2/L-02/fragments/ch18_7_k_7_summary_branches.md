### K.7 Summary

* **Khuôn mẫu nhất quán (consistent pattern) xuyên suốt các trường hợp nghiên cứu**:
  * Một khuôn mẫu nhất quán nổi lên xuyên suốt tất cả các trường hợp (across all cases).
* **Vai trò của hồi quy biểu tượng (symbolic regression - SR)**:
  * Khám phá các mẫu tương tác phi tuyến (nonlinear interaction patterns) mà kỹ thuật trích chọn đặc trưng thủ công (manual feature engineering) thường bỏ sót.
  * Trả lời câu hỏi về cấu trúc toán học mà dữ liệu hàm chứa (what mathematical structure the data contains).
* **Vai trò tiếp nối của mô hình ngôn ngữ lớn (large language model - LLM)**:
  * Đưa tri thức miền (domain knowledge), bối cảnh vận hành (operational context), và cơ sở lý thuyết (theoretical grounding) vào phân tích.
  * Trả lời câu hỏi tại sao cấu trúc toán học đó lại tồn tại (why that structure exists) và cấu trúc đó mang ý nghĩa gì trong miền ứng dụng (what it means in the application domain).
* **Sự phân công lao động (division of labor) giữa SR và LLM**:
  * Phân định vai trò cốt lõi: hồi quy biểu tượng đảm nhiệm khám phá mẫu (pattern discovery), trong khi LLM đảm nhiệm chú giải ngữ nghĩa (semantic annotation).
  * Chuyển đổi kỹ thuật trích chọn đặc trưng tự động (automated feature engineering) từ một quy trình hộp đen mờ đục (opaque, black-box procedure) thành một quy trình có thể diễn giải và đáng tin cậy (interpretable and trustworthy process).
* **Bản chất và giá trị của các đặc trưng thu được**:
  * Các đặc trưng không chỉ dừng lại ở việc đạt hiệu quả về mặt số học (numerically effective).
  * Các đặc trưng mang theo những diễn giải thuyết minh (narratives) mà các chuyên gia chuyên ngành (domain experts) có thể đánh giá, kiểm chứng và tích hợp trực tiếp vào các mô hình khái niệm (conceptual models) về các hiện tượng cơ sở (underlying phenomena).
