## Abstract

* **Bối cảnh và thách thức vận hành**: Hiện tượng tắc nghẽn màng (membrane fouling) là trở ngại hàng đầu hạn chế việc ứng dụng của bể phản ứng sinh học màng kỵ khí (anaerobic membrane bioreactors - AnMBR) trong xử lý nước thải đô thị (municipal wastewater treatment).
  * Xử lý nước thải hiệu quả đóng vai trò nền tảng trong việc duy trì tính bền vững môi trường, đòi hỏi các giải pháp dự báo và kiểm soát tắc nghẽn chính xác.
  * Nghiên cứu ứng dụng các bước tiến đột phá về năng lực tính toán và thuật toán học máy (machine learning) nhằm giải quyết bài toán dự đoán tắc nghẽn màng.

* **Cơ sở dữ liệu thực nghiệm và điều kiện vận hành**: Mô hình được xây dựng dựa trên bộ dữ liệu vận hành liên tục kéo dài 525 ngày từ hệ thống AnMBR quy mô pilot lớn (large pilot-scale AnMBR) xử lý nước thải đô thị thực (real municipal wastewater).
  * Hệ thống phản ánh trung thực diễn biến thực tế khi vận hành dưới các biến động điều kiện vận hành đáng kể (substantial variations in operating conditions) trong suốt 525 ngày.

* **Kiến trúc mô hình học máy và tập đặc trưng**: Dự đoán hồi quy (regression prediction) được hiện thực hóa thông qua hai kiến trúc mạng nơ-ron nhân tạo: Perceptron đa lớp (multilayer perceptron - MLP) và Mạng bộ nhớ ngắn-dài hạn (long short-term memory - LSTM).
  * **Đặc trưng đầu vào (input features)**: Mô hình tích hợp 6 thông số vận hành và hóa sinh then chốt:
    * Tải trọng hữu cơ (organic loading rate - OLR).
    * Nồng độ chất rắn lơ lửng (suspended solids concentration - SS).
    * Nồng độ protein trong các chất polyme ngoại bào (protein concentration in extracellular polymeric substances - $\text{EPS}_p$).
    * Nồng độ polysaccharide trong các chất polyme ngoại bào (polysaccharide concentration in extracellular polymeric substances - $\text{EPS}_c$).
    * Nhiệt độ bể phản ứng (reactor temperature).
    * Thông lượng màng (flux).
  * **Mục tiêu dự đoán đầu ra (prediction target output)**: Áp suất xuyên màng (transmembrane pressure - TMP).

* **Hiệu suất dự đoán và tối ưu hóa siêu tham số**: Quá trình tối ưu hóa siêu tham số (hyperparameter optimization) đóng vai trò đặc biệt quan trọng trong việc thiết lập mô hình và nâng cao độ chính xác dự đoán hồi quy.
  * Cả hai mô hình MLP và LSTM đều dự đoán thành công diễn biến tắc nghẽn màng trên hệ thống AnMBR quy mô pilot lớn.
  * Độ chính xác dự đoán hồi quy đạt hệ số xác định vượt trội: $R^2 > 0.91$.

* **Phân tích khả năng giải thích của mô hình (Model Interpretability)**: Áp dụng công nghệ phân tích khả năng giải thích mô hình nhằm hỗ trợ thấu hiểu cơ chế dự đoán và khắc phục nhược điểm "hộp đen" của học máy.
  * Tính hợp lý (rationality) và tính hữu dụng thực tiễn (utility) của mô hình MLP trong dự đoán tắc nghẽn màng AnMBR quy mô lớn được chứng minh ở cả hai cấp độ:
    * Cấp độ toàn cục (global level).
    * Cấp độ cục bộ (local level).

* **Ý nghĩa khoa học và thực tiễn**: Nghiên cứu mang lại bước tiến phương pháp luận quan trọng, khẳng định tầm quan trọng của việc kết hợp kỹ thuật môi trường (environmental engineering) với tiến bộ tính toán (computational advancements) để giải quyết các thách thức môi trường cấp bách.
