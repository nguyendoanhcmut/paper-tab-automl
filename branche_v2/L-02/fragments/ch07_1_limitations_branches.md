### Limitations

* **Chi phí thời gian tính toán lớn trên các tập dữ liệu nhiều chiều (High-dimensionality computational time overhead):**
  * Dù SymboLLM-FE đã triển khai $2$ cơ chế chiến lược (two strategic mechanisms) nhằm đảm bảo khả năng mở rộng (scalability) trên các tập dữ liệu có số chiều cao (high-dimensional datasets), phương pháp vẫn phát sinh chi phí thời gian quá mức cho phép (prohibitive time overhead).
  * Chi phí tính toán và thời gian thực thi lớn gây cản trở và hạn chế tính khả thi của phương pháp trong các kịch bản chịu ràng buộc nghiêm ngặt về tài nguyên tính toán (resource-constrained scenarios) hoặc các ứng dụng đòi hỏi xử lý thời gian thực (real-time scenarios).

* **Chiến lược tạo tập con bỏ sót tương tác cộng hưởng giữa các biến không liền kề (Non-adjacent feature interactions):**
  * Chiến lược xây dựng tập con đặc trưng (subset construction strategy) sắp xếp các biến đặc trưng theo thứ tự độ quan trọng giảm dần (descending order of importance) và sử dụng một cửa sổ trượt liên tục (continuous sliding window).
  * Quy trình này có thể thất bại trong việc nắm bắt các hiệu ứng cộng hưởng (synergistic effects) giữa các biến không nằm ở vị trí liền kề nhau:
    * Cụ thể, khi hai hoặc nhiều đặc trưng có tương quan ngầm định (implicitly correlated features) không được xếp ở các vị trí liên tiếp trong bảng xếp hạng độ quan trọng, đóng góp dự đoán chung (joint predictive contribution) của chúng có nguy cơ bị bỏ sót hoàn toàn.
    * Sự phân tách về mặt vị trí trong danh sách sắp xếp ngăn cản thuật toán hồi quy ký hiệu (symbolic regression) kết hợp các biến này vào chung một không gian tìm kiếm công thức đặc trưng mới.

* **Thách thức thích ứng và chuyển giao giữa các miền dữ liệu (Domain transfer and adaptation challenges):**
  * Cấu trúc tương quan giữa các biến và thứ tự ưu tiên của đặc trưng phụ thuộc chặt chẽ vào phân phối dữ liệu cụ thể, tạo ra thách thức lớn khi chuyển giao mô hình sang các miền dữ liệu mới (domain transfer challenges).
  * Trong các miền dữ liệu bị dịch chuyển phân phối (domain shift) hoặc các tập dữ liệu bị mã hóa/ẩn danh (anonymized features) thiếu ngữ cảnh ngữ nghĩa tự nhiên, khả năng liên kết tri thức tiên nghiệm của LLM và việc phân nhóm đặc trưng dựa trên độ quan trọng cố định có thể suy giảm hiệu quả tối ưu hóa đặc trưng.
