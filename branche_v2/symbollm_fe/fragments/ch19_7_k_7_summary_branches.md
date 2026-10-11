### K.7 Summary

* Xuyên suốt toàn bộ năm trường hợp (five cases), một khuôn mẫu nhất quán (consistent pattern) được ghi nhận rõ nét:
  * Hồi quy ký hiệu (symbolic regression) đóng góp khả năng khám phá các mẫu tương tác phi tuyến (nonlinear interaction patterns) vốn thường bị bỏ sót bởi kỹ thuật đặc trưng thủ công (manual feature engineering), từ đó trả lời câu hỏi cấu trúc toán học nào (what mathematical structure) hiện diện trong dữ liệu.
  * LLM sau đó bổ sung tri thức miền (domain knowledge), bối cảnh vận hành (operational context) và cơ sở lý thuyết (theoretical grounding) nhằm trả lời câu hỏi vì sao cấu trúc đó tồn tại (why that structure exists) và ý nghĩa của nó là gì trong miền ứng dụng (what it means in the application domain).
* Sự phân công lao động (division of labor) này mang tính quyết định đối với quy trình:
  * Hồi quy ký hiệu đảm nhiệm việc khám phá khuôn mẫu (pattern discovery), trong khi LLM phụ trách chú giải ngữ nghĩa (semantic annotation).
  * Cơ chế kết hợp chuyển hóa kỹ thuật đặc trưng tự động (automated feature engineering) từ một quy trình hộp đen (black-box) mờ đục thành một quy trình có thể diễn giải và đáng tin cậy (interpretable and trustworthy process).
* Giá trị và khả năng tiếp nhận của các đặc trưng tạo ra:
  * Các đặc trưng kết quả không chỉ dừng lại ở việc đạt hiệu quả thuần túy về mặt số học (numerically effective).
  * Đặc trưng mang theo các diễn giải ngữ nghĩa (narratives) cho phép các chuyên gia miền (domain experts) có thể đánh giá, kiểm chứng và tích hợp vào các mô hình khái niệm (conceptual models) về các hiện tượng bản chất bên dưới.
