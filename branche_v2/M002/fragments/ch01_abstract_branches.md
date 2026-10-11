## Abstract

* **Bối cảnh và mục tiêu nghiên cứu**:
  * Việc định lượng tương tác liên bề mặt (interfacial interactions) giữ vai trò đặc biệt quan trọng do tương tác này trực tiếp quyết định khả năng bám dính của chất gây nghẹt (foulant adhesion) và toàn bộ tiến trình tắc nghẽn màng trong các bể phản ứng sinh học màng ($MBR$ - Membrane Bioreactors).
  * Nghiên cứu này phát triển mô hình mạng nơ-ron nhân tạo hàm cơ sở hướng tâm ($RBF\text{ }ANN$ - Radial Basis Function Artificial Neural Network) nhằm mục đích dự đoán các tương tác liên bề mặt trên bề mặt màng có độ nhám ngẫu nhiên (randomly rough membrane surface).

* **Phương pháp luận và bộ dữ liệu huấn luyện**:
  * Dữ liệu tương tác liên bề mặt được định lượng từ phương pháp tiếp cận $XDLVO$ mở rộng nâng cao (advanced extended Derjaguin–Landau–Verwey–Overbeek approach) được sử dụng làm tập mẫu huấn luyện ($training\text{ }samples$) cho các mạng $RBF$.
  * Mô hình kết hợp nền tảng lý thuyết tương tác bề mặt keo tụ $XDLVO$ với kỹ thuật học máy để mô phỏng hình học bề mặt gồ ghề bất quy tắc.

* **Hiệu quả tính toán và kết quả định lượng**:
  * Thời gian tiêu tốn cho tính toán ($computing\text{ }time\text{ }consumption$) đối với dự đoán bằng mạng $RBF$ chỉ bằng khoảng $1/50$ so với thời gian tính toán bằng phương pháp $XDLVO$ nâng cao trong cùng điều kiện khảo sát.
  * Tỉ lệ thời gian $1/50$ minh chứng cho hiệu suất vượt trội ($high\text{ }efficiency$) của phương pháp $RBF\text{ }ANN$, giải quyết điểm nghẽn về chi phí tính toán lớn của phương pháp số học cổ điển.
  * Độ chính xác tính toán ($calculation\text{ }accuracy$) của phương pháp đạt ngưỡng chấp nhận được, đảm bảo độ tin cậy của các kết quả phân tích tương tác.

* **Ý nghĩa khoa học và tiềm năng ứng dụng**:
  * Nghiên cứu thể hiện bước đột phá về phương pháp luận cơ bản liên quan đến cơ chế tắc nghẽn màng lọc sinh học.
  * Phương pháp $RBF\text{ }ANN$ đề xuất mở ra triển vọng ứng dụng rộng lớn trong nghiên cứu hiện tượng tắc nghẽn màng cũng như các hành vi liên bề mặt ($interface\text{ }behavior$).
