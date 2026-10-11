### 3.5. Limitations and future prospects

* Quá trình dự đoán hiện tượng nghẹt màng (membrane fouling) dựa trên trí tuệ nhân tạo (artificial intelligence - AI) đã đạt được nhiều tiến bộ đáng kể, song việc ứng dụng thực tế công nghệ AI vào các quy trình màng vẫn đối mặt với nhiều rào cản kỹ thuật (Niu et al., 2022).
* Bể phản ứng sinh học màng kỵ khí (anaerobic membrane bioreactor - AnMBR) mang lại nhiều ưu điểm nổi bật, đặc biệt thích hợp để triển khai tại các quốc gia đang phát triển (Elmoutez et al., 2023):
  * Diện tích mặt bằng nhỏ gọn (compact footprint).
  * Hiệu quả xử lý nước thải cao.
  * Khả năng sản xuất nước tái sử dụng (reclaimed water production).
  * Tiềm năng thu hồi năng lượng (energy recovery).
  * Thách thức trung tâm cần giải quyết là ứng dụng công nghệ AI để giảm thiểu vấn đề nghẹt màng dai dẳng trong các hệ thống AnMBR xử lý nước thải đô thị (municipal wastewater treatment).
* Việc đưa công nghệ AI vào vận hành thực tế (operationalize) đòi hỏi phải giải quyết đồng thời nhiều yêu cầu thiết yếu về tài nguyên và hạ tầng (De-Arteaga et al., 2018):
  * Khả năng tiếp cận dữ liệu (data accessibility).
  * Năng lực tính toán phần cứng (computational capacity).
  * Tính sẵn có của hạ tầng mạng internet (internet availability).
  * Nguồn nhân lực chuyên môn hóa cao (specialized human resources).
  * Cần cân nhắc kỹ lưỡng bối cảnh áp dụng và nguồn lực sẵn có trong suốt giai đoạn phát triển lẫn giai đoạn triển khai công nghệ.
* Nghiên cứu hiện tại được thực hiện dựa trên quy mô thử nghiệm pilot (pilot-scale case investigation), đặt ra bài toán cân đối giữa hiệu năng và chi phí triển khai:
  * Quy mô thu thập dữ liệu (scale of data acquisition) và độ phức tạp của mô hình (model intricacy) đóng vai trò là thước đo tương đối về mức tiêu hao tài nguyên cần thiết cho việc phát triển và triển khai thực tế.
  * Kết quả so sánh giữa các mô hình s-MLP (simplified multi-layer perceptron), MLP (multi-layer perceptron) và LSTM (long short-term memory) nhấn mạnh sự cần thiết phải định hướng cân bằng giữa hiệu năng và chi phí (performance-cost nexus) phù hợp với từng kịch bản và nhu cầu vận hành cụ thể.
* Khả năng thích ứng (adaptability) cao của các mô hình mạng nơ-ron nhân tạo (artificial neural network - ANN) mở ra tiềm năng ứng dụng rộng rãi trong lĩnh vực kỹ thuật môi trường và xử lý nước thải:
  * Bên cạnh AnMBR, các mô hình ANN có khả năng tái hiệu chuẩn (recalibrated) và điều chỉnh linh hoạt để thích nghi với các kịch bản vận hành khác nhau.
  * Quy trình điều chỉnh mô hình sang bối cảnh mới đòi hỏi một phương pháp luận hoàn chỉnh:
    * Tái huấn luyện (retrained) mô hình bằng dữ liệu đặc thù của hệ thống xử lý nước thải mới.
    * Tinh chỉnh các kỹ thuật kỹ nghệ đặc trưng (feature engineering) nhằm bao quát các đặc tính riêng biệt của hệ thống mới.
    * Thực hiện kiểm chứng nghiêm ngặt (rigorous validation) để đảm bảo độ tin cậy (dependability) và độ chính xác (precision) trong môi trường mới.
    * Bổ sung các chỉ số đánh giá hiệu năng tùy biến (customized performance metrics) nhằm mang lại đánh giá đa chiều, sâu sắc về hiệu quả mô hình qua nhiều kịch bản vận hành đa dạng.
* Sự tiến bộ với tốc độ nhanh chóng của các công nghệ AI mở ra nhiều triển vọng nghiên cứu trong tương lai:
  * Tốc độ đổi mới của AI vượt xa các cải tiến công nghiệp truyền thống, đòi hỏi các phương pháp và mô hình dự đoán nghẹt màng phải không ngừng cải tiến và cập nhật.
  * Các hướng nghiên cứu tương lai cần liên tục tập trung vào:
    * Các kỹ thuật tối ưu hóa siêu tham số mới nổi (emerging hyperparameter optimization - HPO techniques).
    * Các mẫu hình mô hình hóa tiên tiến (novel modeling paradigms).
    * Các khung làm việc mới nhằm tăng cường khả năng giải thích của mô hình (frameworks for model interpretability).
  * Nhờ khả năng thích ứng và mở rộng (scalability) vốn có, các mô hình học máy (machine learning - ML) có tiềm năng mở rộng sang nhiều quy trình xử lý nước thải khác, với điều kiện thực hiện các điều chỉnh tham số phù hợp, thay thế tập dữ liệu tương thích, và hoàn thiện các chiến lược chỉ số đánh giá hiệu năng.
