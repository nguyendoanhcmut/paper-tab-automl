## Abstract

* Kỹ thuật đặc trưng tự động (automated feature engineering) đóng vai trò then chốt trong việc cải thiện hiệu năng mô hình dự đoán cho các nhiệm vụ học trên dữ liệu dạng bảng (tabular learning tasks).
* Các phương pháp kỹ thuật đặc trưng tự động truyền thống bị hạn chế do phụ thuộc vào các phép biến đổi được xác định trước (pre-defined transformations) trong các không gian tìm kiếm (search spaces) cố định, được thiết kế thủ công, và thường bỏ qua tri thức miền (domain knowledge).
* Các tiến bộ gần đây sử dụng mô hình ngôn ngữ lớn (Large Language Models - LLMs) đã cho phép tích hợp tri thức miền vào quy trình kỹ thuật đặc trưng.
* Tuy nhiên, các phương pháp tiếp cận dựa trên LLM hiện tại còn tồn tại hạn chế:
  * Sử dụng kỹ thuật nhắc lệnh trực tiếp (direct prompting) hoặc chỉ dựa hoàn toàn vào điểm đánh giá/kiểm định (validation scores) để lựa chọn đặc trưng (feature selection).
  * Không tận dụng được tri thức/hiểu biết (insights) rút ra từ các thử nghiệm khám phá đặc trưng trước đó.
  * Không thiết lập được lập luận có ý nghĩa (meaningful reasoning) giữa việc tạo đặc trưng (feature generation) và hiệu năng dựa trên dữ liệu (data-driven performance).
* Để giải quyết các thách thức này, nghiên cứu đề xuất LLM-FE, một khung làm việc (framework) mới kết hợp tìm kiếm tiến hóa (evolutionary search) với tri thức miền và năng lực suy luận (reasoning capabilities) của LLMs nhằm tự động khám phá các đặc trưng hiệu quả cho các nhiệm vụ học trên dữ liệu dạng bảng.
* LLM-FE mô hình hóa kỹ thuật đặc trưng thành bài toán tìm kiếm chương trình (program search problem):
  * LLMs liên tục đề xuất các chương trình biến đổi đặc trưng (feature transformation programs) mới theo phương thức lặp.
  * Phản hồi dựa trên dữ liệu (data-driven feedback) định hướng quá trình tìm kiếm.
* Các kết quả thực nghiệm chứng minh LLM-FE liên tục vượt trội so với các phương pháp cơ sở tiên tiến nhất (state-of-the-art baselines), đồng thời thể hiện khả năng tổng quát hóa (generalizability) trên nhiều mô hình, nhiệm vụ và tập dữ liệu đa dạng.
* Mã nguồn của phương pháp được công khai tại: https://github.com/nikhilsab/LLMFE.
