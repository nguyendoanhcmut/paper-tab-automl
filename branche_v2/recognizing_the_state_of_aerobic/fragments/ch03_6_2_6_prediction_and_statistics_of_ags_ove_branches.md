### 2.6 Prediction and statistics of AGS over its life-cycle

- Kiểm chứng độc lập năng lực tổng quát hóa mô hình trên hệ thống MBR mới.
  - Mô hình đã tối ưu được nạp từ tệp điểm kiểm tra (checkpoint) để thực hiện suy luận trên các ảnh hiển vi mới.
  - Thu thập dữ liệu ảnh từ một hệ thống MBR độc lập khác trong suốt chu kỳ sống của bùn để thẩm định tính tổng quát.
  - Dữ liệu độc lập gồm 7 lô thực nghiệm với hơn 50 ảnh mỗi lô, mang lại tổng cộng 362 điểm dữ liệu hợp lệ.
- Cơ chế lọc trùng lặp và thống kê định lượng phân bố hạt bùn tự động.
  - Thiết lập ngưỡng giao cắt $IoU = 0.7$ để chọn lọc hộp bao tối ưu trong các vùng ứng viên có mức độ chồng lấn cao.
  - Sử dụng biến toàn cục để đếm và lưu trữ số lượng cá thể bùn theo từng phân lớp cho mỗi ảnh đầu vào.
  - Tích lũy số liệu thống kê tự động theo từng mẻ xử lý qua các vòng lặp để theo dõi biến động quần thể hạt.
  - Cung cấp công cụ định lượng hỗ trợ kỹ sư vận hành giám sát trực tiếp trạng thái bùn trong quy trình thực tế.
