### 3.2 MICE-based interpolation of input and target features

- Cơ chế hồi quy lặp chuỗi đa biến của thuật toán MICE áp dụng cho chuỗi dữ liệu công nghệ môi trường:
  - MICE ước lượng tuần tự các giá trị khuyết thiếu qua các mô hình hồi quy lặp, cho phép từng biến chứa điểm khuyết được dự đoán tối ưu từ tất cả các biến quan sát còn lại.
  - Thuật toán thích ứng tối ưu với đặc tính phi tuyến và phụ thuộc lẫn nhau phức tạp giữa tải lượng thủy lực, nồng độ ô nhiễm đầu vào và điều kiện vận hành DAF.
- Tái tạo chuỗi dữ liệu chất lượng nước bảo đảm tính liên tục thời gian và động học quá trình:
  - Điểm khuyết thiếu ở $\text{SS}$ đầu vào và $T\text{-}P$ đầu vào (thường phát sinh trong các đợt đỉnh tải hoặc gián đoạn đo đạc phòng thí nghiệm) được khôi phục đồng nhất với phương sai của các mẫu lân cận.
  - Nồng độ $T\text{-}P$ đầu ra bị khuyết được làm đầy mượt mà dọc theo biến thiên chu kỳ ngày và mùa, không gây ra bước nhảy đột ngột hay mất cân bằng dữ liệu mục tiêu.
- Cơ sở khoa học và ưu thế của MICE so với các phương pháp nội suy truyền thống:
  - Phù hợp với các nghiên cứu quan trắc chất lượng nước (Dixneuf et al. 2021; Wang et al. 2024), xác nhận phương pháp đa biến duy trì tương quan hệ số cao hơn các kỹ thuật nội suy đơn biến cục bộ.
  - Khắc phục hạn chế của phương pháp điền giá trị trung bình hoặc nội suy tuyến tính vốn làm suy giảm phương sai và bóp méo phân phối xác suất.
  - Cung cấp tập dữ liệu đầu vào hoàn chỉnh, sạch và nhất quán thời gian cho các bước kỹ nghệ đặc trưng và huấn luyện mô hình học máy tiếp theo.
