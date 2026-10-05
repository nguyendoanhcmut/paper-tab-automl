## 4 Conclusions

- Tổng kết hiệu năng nhận dạng và phân loại chu kỳ sống bùn hạt của mô hình YOLOv8.
  - Nghiên cứu đã xây dựng thành công giải pháp học máy dựa trên YOLOv8 để nhận diện tự động 4 giai đoạn chu kỳ sống của bùn hạt hiếu khí (AGS).
  - Mô hình đạt độ chính xác trung bình $mAP_{50} = 0.985$ và $mAP_{50-95} = 0.837$, khẳng định độ tin cậy và tính ổn định cao.
  - Phân tích không gian $t\text{-SNE}$ chứng minh sự tách biệt rõ nét của các cụm đặc trưng hình thái qua từng giai đoạn sinh trưởng.
  - Phương pháp diễn giải SHAP làm rõ cơ chế phân loại: tập trung vào đặc trưng toàn cục ở hạt nhỏ và đường viền ở hạt lớn.
- Khả năng giám sát thời gian thực và chức năng thống kê quần thể hạt bùn.
  - Sự kết hợp giữa cơ chế biến toàn cục và mô-đun chú ý SimAM nâng cao tốc độ xử lý với thời gian toàn trình chỉ $14.2\text{--}15.6\text{ ms}$ cho mỗi ảnh.
  - Chức năng đếm hạt tự động theo mẻ phản ánh trực tiếp trạng thái phân bố sinh khối trong bể sinh học MBR dòng liên tục.
- Khuyến nghị ứng dụng thực tiễn và định hướng mở rộng công nghệ.
  - Đối với các hệ thống nuôi cấy gián đoạn theo mẻ (SBR), khuyến nghị tái huấn luyện mô hình trên dữ liệu tương thích và tùy biến cấu trúc mạng.
  - Việc chuyển hóa kết quả chẩn đoán từ AI thành quyết định điều khiển vận hành cần kết hợp linh hoạt với kinh nghiệm thực nghiệm và các biến số công nghệ khác.
  - Nghiên cứu mở ra công cụ hỗ trợ kỹ thuật đáng tin cậy cho công tác quản lý và tối ưu hóa hệ thống xử lý nước thải tiên tiến.
