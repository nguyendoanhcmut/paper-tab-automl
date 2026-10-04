### 3.5. Limitations and future directions

- Hiệu năng dự đoán và độ bền vững của FLAML trên tập dữ liệu do [30] thu thập vẫn còn các hạn chế và hướng mở rộng nghiên cứu trong tương lai:
  - Khả năng thích ứng của khung mô hình hóa cần được đánh giá trên các không gian thông số vận hành rộng hơn (broader operational parameter spaces).
  - Hiệu năng mô hình cần được kiểm định bằng các tập dữ liệu độc lập bên ngoài (external datasets) thu thập từ các thiết lập thực nghiệm (experimental setups) khác nhau.
  - Phổ hợp chất nghiên cứu cần mở rộng sang các hợp chất PFAS (per- and polyfluoroalkyl substances) khác, bao gồm PFOS (perfluorooctane sulfonate) và các chất đồng ô nhiễm (co-contaminants), nhằm xác định khả năng tổng quát hóa (generalizability) trên các hệ thống xử lý đa dạng.
  - Phương pháp học chuyển giao (transfer learning methodologies) là hướng tiếp cận tiềm năng để khai thác hiệu quả tri thức từ mô hình hiện tại nhằm đẩy nhanh năng lực dự đoán trên các hệ thống điện hóa liên quan.
- Mở rộng khung phân tích sang tối ưu hóa đa mục tiêu tích hợp (integrated multi-objective optimization) nhằm nâng cao khả năng ứng dụng thực tế ngoài mục tiêu đơn lẻ là hiệu suất loại bỏ chất ô nhiễm (removal efficiency):
  - Tích hợp các chỉ số hiệu năng vận hành then chốt, bao gồm:
    - Các thước đo tiêu thụ năng lượng (energy consumption metrics).
    - Sự hình thành sản phẩm phụ (byproduct formation).
    - Sự đánh đổi tính toán (computational trade-offs) giữa tốc độ tối ưu hóa và hiệu năng mô hình cuối cùng.
  - Phát triển kiểm soát quá trình thích ứng thời gian thực (real-time adaptive process control):
    - Tích hợp FLAML với các công nghệ cảm biến tại chỗ (in situ sensing technologies) để thực hiện tối ưu hóa quá trình động (dynamic process optimization).
    - Cho phép điều chỉnh tức thời các thông số vận hành dựa trên phản hồi theo thời gian thực (real-time feedback).
- Nâng cao khả năng diễn giải (interpretability) và tinh chỉnh phương pháp luận mô hình:
  - Phát triển các khung mô hình hóa lai (hybrid modeling frameworks) kết hợp FLAML với các mô hình điện hóa dựa trên quy luật vật lý (physics-based electrochemical models) nhằm đạt mức độ diễn giải sâu hơn so với phân tích SHAP (SHapley Additive exPlanations) ban đầu.
  - Khám phá cơ chế xử lý biến phân loại tự nhiên (native categorical handling) bên trong các mô hình dạng cây (tree-based models) như một giải pháp thay thế tiềm năng cho phương pháp mã hóa one-hot (one-hot encoding).
  - Các định hướng nghiên cứu này củng cố tiềm năng của AutoML như một cách tiếp cận mang tính chuyển đổi cho các công nghệ xử lý môi trường bằng phương pháp điện hóa (environmental electrochemical remediation technologies).
