### 3.5 Implications

- Ba kết luận khoa học cốt lõi từ nghiên cứu:
  - Thứ nhất, lựa chọn đặc trưng định hướng tri thức (KBFS) khắc phục triệt để hạn chế tổng quát hóa ngoại suy mà các mô hình học sâu phức tạp không thể giải quyết.
  - Thứ hai, chất lượng không gian đầu vào là yếu tố quyết định hiệu năng mô hình trong điều kiện dữ liệu mẫu nhỏ và số chiều cao, ưu thế hơn so với việc chỉ tăng độ phức tạp kiến trúc.
  - Thứ ba, khung LLM-RAG là giải pháp tự động hóa khả thi, mang lại hiệu năng dự đoán cạnh tranh mà không phụ thuộc vào sự can thiệp trực tiếp của chuyên gia con người.
- Vai trò của lựa chọn đặc trưng trong kỹ thuật môi trường và đối sánh liên ngành:
  - Lựa chọn đặc trưng đóng vai trò trung tâm trong nhiều lĩnh vực kỹ thuật từ tin sinh học hệ gen, xử lý ngôn ngữ tự nhiên đến chẩn đoán hình ảnh và tài chính.
  - Trong ngành nước thải, đa số các nghiên cứu học máy áp dụng lựa chọn đặc trưng thiếu hệ thống và chưa đánh giá đúng tầm quan trọng của việc thanh lọc biến.
  - Thực nghiệm cho thấy cắt giảm $2/3$ số biến đầu vào không chỉ nâng hệ số $R^2$ thêm $10–20\%$ mà còn cắt giảm $50\%$ thời gian tính toán của mô hình vận hành.
- Đóng góp phương pháp luận và khả năng mở rộng:
  - Kết hợp chặt chẽ giữa nguyên lý sinh hóa và tương quan thực nghiệm để xây dựng mô hình nhận biết quá trình (process-aware model) có độ bền vững cao.
  - Tiên phong ứng dụng kỹ thuật LLM-RAG vào quy trình lựa chọn đặc trưng trong kỹ thuật xử lý nước thải, mở rộng bộ công cụ phương pháp luận cho ngành kỹ thuật môi trường.
  - Khung phương pháp có khả năng chuyển giao trực tiếp sang các bài toán môi trường khác có dữ liệu thưa, số chiều cao và cấu trúc cơ chế sinh hóa phức tạp.
- Ba giới hạn nội tại và định hướng phát triển tương lai:
  - Hạn chế 1: Nghiên cứu hiện tại chủ yếu đánh giá đóng góp đơn lẻ của từng đặc trưng lên biến mục tiêu; các nghiên cứu tiếp theo cần phát triển thuật toán nhận biết tương tác đa biến (interaction-aware feature selection).
  - Hạn chế 2: Trọng số kết hợp $1:1$ giữa tương quan thống kê và điểm cơ chế mang tính cân bằng thực dụng; tỷ lệ này cần được điều chỉnh linh hoạt tùy thuộc vào độ tin cậy của dữ liệu quan trắc và mức độ hiểu biết cơ chế lý thuyết.
  - Hạn chế 3: Bản chất rời rạc của dữ liệu thực nghiệm khiến ranh giới ngoại suy an toàn (safe extrapolation bounds) chưa được xác định rõ ràng, đòi hỏi các đợt quan trắc rộng hơn để định hình phạm vi ứng dụng tin cậy.
