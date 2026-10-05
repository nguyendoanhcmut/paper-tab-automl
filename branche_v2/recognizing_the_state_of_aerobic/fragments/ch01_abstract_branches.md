## Abstract

- Hệ thống màng sinh học bùn hạt hiếu khí dòng liên tục (AGS-MBR) là công nghệ xử lý nước thải bền vững và hiệu quả cao.
  - Bùn hạt hiếu khí (AGS) có dạng hình cầu hoặc hình elip, hình thành do vi sinh vật tự kết tụ trong điều kiện hiếu khí.
  - Bùn trải qua 4 giai đoạn chu kỳ sống liên tiếp: khởi tạo (initial), sinh trưởng (growth), trưởng thành (mature), và phân cắt (cleaved).
  - Việc nhận dạng và phân loại chính xác các giai đoạn này quyết định sự ổn định của hệ thống vận hành.
  - Các phương pháp giám sát thủ công trước đây tốn nhiều nhân công và dễ xảy ra sai sót chủ quan.
- Nghiên cứu ứng dụng trí tuệ nhân tạo xây dựng mô hình học máy dựa trên thuật toán YOLOv8 để phân loại và giám sát AGS tự động.
  - Tập dữ liệu thực nghiệm gồm 862 ảnh chụp hiển vi được gắn nhãn chính xác.
  - Mô hình đạt độ chính xác trung bình $mAP_{50}$ là $0.985$ tại ngưỡng giao cắt $IoU = 0.5$.
  - Chỉ số $mAP_{50-95}$ đạt $0.837$, xác nhận năng lực phân loại chuẩn xác cao trên tập kiểm tra.
- Phân tích cụm $t\text{-SNE}$ và tính diễn giải SHAP cung cấp bằng chứng định lượng về cơ chế nhận dạng của mô hình.
  - Phương pháp $t\text{-SNE}$ tách biệt rõ ràng các cụm đặc trưng hình thái theo từng giai đoạn sinh trưởng.
  - Phương pháp SHAP chỉ ra mô hình tập trung vào đặc trưng toàn cục của hạt nhỏ và đặc trưng đường viền của hạt lớn.
  - Cơ chế thống kê biến toàn cục hỗ trợ giám sát thời gian thực trạng thái bùn trong quy trình xử lý nước thải liên tục.
