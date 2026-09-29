## Chương 1: Giới thiệu và Bối cảnh Nghiên cứu AnMBR

### 1.1 Khủng hoảng tài nguyên nước và vị thế của công nghệ AnMBR
#### Bối cảnh khan hiếm nước toàn cầu và tái tạo tài nguyên từ nước thải
- Hoạt động của con người làm gia tăng ô nhiễm và suy kiệt nguồn nước ngọt tự nhiên. Hiện tượng này đe dọa nghiêm trọng an ninh lương thực và cân bằng sinh thái (Jury and Vaux, 2007).
- Tình trạng khan hiếm nước cản trở nguồn cấp nước sạch cho các đô thị trên toàn cầu.
- Ngành công nghiệp nước xác định nước thải là nguồn tài nguyên tái tạo bền vững (Winkler and van Loosdrecht, 2022).
- Quy trình bùn hoạt tính truyền thống giữ vai trò nòng cốt trong các trạm xử lý nước thải hiện hành (van Loosdrecht and Brdjanovic, 2014).
- Các nhà khoa học ưu tiên nghiên cứu các công nghệ thu hồi tài nguyên để thúc đẩy nền kinh tế tuần hoàn.

#### Nguyên lý tích hợp và ưu điểm kỹ thuật của AnMBR (anaerobic membrane bioreactor)
- AnMBR tích hợp trực tiếp quá trình phân hủy kỵ khí sinh học với module màng lọc tách sinh khối.
- Hệ thống này xử lý nước thải hiệu quả và tạo ra khí sinh học (biogas) giàu năng lượng (Krzeminski et al., 2017; Moideen et al., 2023).
- Chi phí vận hành của AnMBR thấp hơn đáng kể so với các hệ thống hiếu khí truyền thống (Ho and Sung, 2010; Pretel et al., 2015).
- AnMBR hạn chế tối đa lượng bùn thải dư thừa và nâng cao tiềm năng thu hồi năng lượng sạch (Robles et al., 2022).
- Quá trình khởi động hệ thống phản ứng kỵ khí diễn ra nhanh chóng (Robles et al., 2018).
- Dấu chân sinh thái và diện tích xây dựng của AnMBR nhỏ gọn hơn nhiều so với các công nghệ truyền thống.
- Công nghệ này đáp ứng mục tiêu giảm phát thải carbon và tái tạo tài nguyên bền vững.

### 1.2 Rào cản thực nghiệm và sự cần thiết của mô hình hóa định hướng dữ liệu
#### Thách thức tài nguyên và thời gian trong nghiên cứu thực nghiệm AnMBR
- Quá trình phát triển AnMBR chủ yếu dựa vào các thí nghiệm quy mô phòng thí nghiệm và thử nghiệm pilot (Q. Li et al., 2024; Z. Li et al., 2024; Ren et al., 2024).
- Việc vận hành hệ thống thực nghiệm tiêu tốn lượng lớn hóa chất và thuốc thử phân tích (Li et al., 2022).
- Hệ thống phản ứng đòi hỏi trang thiết bị kiểm soát chuyên dụng và nhân sự kỹ thuật cao.
- Các thí nghiệm sinh học kỵ khí kéo dài từ vài tháng đến nhiều năm để đạt trạng thái ổn định.
- Giới hạn không gian và kinh phí phòng thí nghiệm thu hẹp số lượng mẻ vận hành của bể phản ứng.
- Các rào cản thực nghiệm này làm chậm quá trình thương mại hóa và mở rộng quy mô AnMBR.

#### Tiềm năng của mô hình hóa học máy (Machine Learning - ML) trong tối ưu hóa vận hành
- Mô hình hóa dựa trên dữ liệu nổi lên như giải pháp đột phá cho công nghệ AnMBR (Li et al., 2022; Robles et al., 2018; Wang and Li, 2024).
- Các thuật toán học máy sử dụng thông số vận hành và chất lượng nước đầu vào để dự báo chất lượng nước đầu ra (Li et al., 2022; Mahanna et al., 2024; Pal et al., 2024).
- Mô hình nắm bắt chính xác các mối quan hệ phi tuyến phức tạp giữa dòng vào và dòng ra.
- Học máy cung cấp các hiểu biết sâu sắc giúp kỹ sư điều khiển và tối ưu hóa hiệu suất bể phản ứng.
- Mô phỏng thuật toán thay thế các thử nghiệm vật lý tốn kém bằng mức tiêu hao tài nguyên tối thiểu.
- Chuyên viên vận hành đánh giá được nhiều kịch bản công nghệ khác nhau mà không cần gián đoạn hệ thống thực tế.
- Giải pháp này hỗ trợ đắc lực việc thiết kế AnMBR trong điều kiện hạn chế về ngân sách thực nghiệm.

### 1.3 Thách thức cốt lõi khi ứng dụng học máy trong AnMBR
#### Tính không đồng nhất cao của hệ thống sinh học AnMBR
- Hệ thống AnMBR thể hiện tính không đồng nhất rất lớn giữa các công trình xử lý nước thải.
- Cấu trúc quần thể vi sinh vật thay đổi liên tục theo điều kiện cấp cơ chất và nhiệt độ vận hành.
- Cấu hình thiết bị và đặc tính nước thải đầu vào biến động mạnh theo thời gian.
- Kích thước lỗ màng trong AnMBR làm biến đổi nồng độ COD dòng ra và cấu trúc hệ vi sinh (Ji et al., 2020).
- Biến động vi sinh ảnh hưởng trực tiếp đến chất lượng nước đầu ra và hiệu suất sinh khí sinh học.
- Tính không đồng nhất cao ngăn cản việc áp dụng một mô hình tổng quát chung cho nhiều hệ phản ứng.
- Kỹ sư phải hiệu chỉnh mô hình riêng biệt cho từng cấu hình lò phản ứng cụ thể.

#### Rào cản chuyên môn kỹ thuật trong lựa chọn thuật toán và tinh chỉnh siêu tham số
- Quy trình phát triển mô hình học máy bao gồm nhiều tác vụ phức tạp (He et al., 2021; Karmaker et al., 2021).
- Chuyên gia phải sàng lọc và lựa chọn thuật toán phù hợp nhất trong số hàng loạt thuật toán ứng viên.
- Công việc tinh chỉnh siêu tham số đòi hỏi kiến thức toán học sâu rộng và chi phí tính toán lớn.
- Kỹ sư ngành nước thường thiếu chuyên môn chuyên sâu về khoa học dữ liệu và trí tuệ nhân tạo.
- Sự thiếu hụt nhân lực liên ngành cản trở việc ứng dụng học máy trong thực tế vận hành MBR (Lai et al., 2024).

### 1.4 Giải pháp học máy tự động (AutoML) và mục tiêu công trình
#### Khái niệm và tiềm năng dân chủ hóa công nghệ của AutoML (FLAML)
- AutoML tự động hóa các tác vụ lặp lại trong toàn bộ đường ống học máy (Truong et al., 2019).
- Hệ thống tự động thực hiện việc tuyển chọn thuật toán và tối ưu hóa siêu tham số.
- AutoML giảm thiểu đáng kể rào cản kỹ thuật và rút ngắn thời gian xây dựng mô hình dự báo.
- Nền tảng tự động này thúc đẩy mạnh mẽ quá trình triển khai học máy vào thực tiễn ngành nước (Lai et al., 2024).
- AutoML giúp dân chủ hóa công nghệ mô hình hóa cho các chuyên gia môi trường không chuyên về ML (Li et al., 2021).
- Người dùng có thể nhanh chóng làm chủ công nghệ dữ liệu để cải tiến hiệu quả vận hành AnMBR.

#### Các mục tiêu nghiên cứu cốt lõi của bài báo
- Nghiên cứu áp dụng khung làm việc AutoML (thư viện FLAML) để mô hình hóa động học phi tuyến của AnMBR xử lý nước thải sinh hoạt.
- Tác vụ trọng tâm tập trung vào dự báo chính xác nồng độ và hiệu suất loại bỏ COD dòng ra.
- Công trình đánh giá định lượng tác động của việc mở rộng tập đặc trưng vận hành đối với chất lượng mô hình.
- Nhóm nghiên cứu khảo sát ảnh hưởng của kích thước tập dữ liệu huấn luyện nhỏ đối với độ chính xác thuật toán.
- Công trình đối sánh hiệu năng của AutoML với các mạng nơ-ron sâu tiên tiến gồm FCN, CNN và DenseNet.
- AutoML đạt sai số phần trăm tuyệt đối trung bình (MAPE) ở mức $3.11\%$, vượt trội hơn các mô hình học sâu.
- Nghiên cứu phát triển khung diễn giải xếp hạng đặc trưng tổ hợp để giải thích cơ chế dự báo của AutoML.
- Kết quả xếp hạng xác định nồng độ COD dòng vào là đặc trưng chi phối mạnh nhất đến hiệu suất loại bỏ COD.
- Phát hiện của bài báo mở rộng tiềm năng ứng dụng AutoML cho các hệ thống xử lý nước thải có tập dữ liệu nhỏ.
