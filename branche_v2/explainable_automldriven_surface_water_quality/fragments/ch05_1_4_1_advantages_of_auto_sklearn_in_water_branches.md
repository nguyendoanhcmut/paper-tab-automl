### 4.1 Advantages of Auto-sklearn in water quality classification

- **Ưu thế cấu trúc và hiệu năng của Auto-sklearn**:
  - Auto-sklearn đạt hiệu năng dẫn đầu so với các mô hình học máy truyền thống trên nhiều chỉ số đánh giá thực nghiệm (Bảng 1).
  - Tự động hóa việc dò tìm và tích hợp $7$ đường ống học máy (pipelines) bổ trợ lẫn nhau thành cụm mô hình ensemble thống nhất.
  - Về mặt lý thuyết, các mô hình học máy truyền thống đơn lẻ không thể vượt qua AutoML vì chúng chính là các thuật toán con nằm trong không gian tìm kiếm của Auto-sklearn.
  - Kết quả phù hợp với các cuộc thi AutoML quốc tế, nơi việc tinh chỉnh tham số thủ công của các nhà khoa học dữ liệu không thể vượt qua tối ưu hóa tự động.
- **Vai trò then chốt của thuật toán Rừng ngẫu nhiên (RF)**:
  - Mức độ cải thiện hiệu năng của Auto-sklearn so với mô hình RF đơn lẻ là tương đối khiêm tốn do cả $7$ pipeline trong ensemble đều tự động chọn RF làm bộ phân loại cốt lõi.
  - Việc hệ thống tự động ưu tiên RF khẳng định hiệu quả của cơ chế tìm kiếm và chứng minh các mô hình họ cây quyết định với độ phức tạp vừa phải rất tối ưu cho dữ liệu phân loại nước mặt.
- **Ý nghĩa thực tiễn đối với quản lý môi trường**:
  - Đề xuất ứng dụng trực tiếp các khung làm việc AutoML trong giám sát môi trường thay vì tốn công sức thử nghiệm thủ công từng thuật toán đơn lẻ.
  - Giúp các cơ quan quản lý tiết kiệm đáng kể thời gian và nhân lực chuyên gia trong khâu tiền xử lý và tối ưu hóa siêu tham số.
  - Rào cản về tài nguyên tính toán đang giảm dần nhờ sự phát triển của hạ tầng điện toán đám mây và máy tính hiệu năng cao.
