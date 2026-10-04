## Abstract

- Học máy (ML - machine learning) là hướng tiếp cận tiềm năng cho mô hình hóa bể phản ứng sinh học màng kỵ khí (AnMBR - anaerobic membrane bioreactor), nhưng độ phức tạp kỹ thuật gây khó khăn cho các nhà nghiên cứu thiếu chuyên môn ML sâu:
  - Thách thức cốt lõi nằm ở khâu lựa chọn mô hình (model selection) và tối ưu hóa siêu tham số (hyperparameter optimization).
- Nghiên cứu ứng dụng học máy tự động (AutoML - automated machine learning) để mô hình hóa quá trình loại bỏ nhu cầu oxy hóa học (COD - chemical oxygen demand) trong AnMBR xử lý nước thải đô thị (municipal wastewater).
- Mô hình AutoML đạt hiệu suất dự đoán cao hơn các mô hình mạng nơ-ron sâu (deep neural models) từng được công bố trước đó:
  - Sai số phần trăm tuyệt đối trung bình (MAPE - mean absolute percentage error) đạt $3.11\,\%$.
- Đánh giá tác động của việc mở rộng tập đặc trưng (feature set expansion) và gia tăng lượng dữ liệu đối với hiệu suất mô hình:
  - Các đặc trưng về thời gian vận hành (operation time) giúp cải thiện hiệu suất mô hình hóa.
  - Việc bổ sung thêm dữ liệu không đóng góp đáng kể vào hiệu quả mô hình hóa bằng ML.
- Phân tích độ quan trọng đặc trưng dạng tổ hợp (ensemble feature importance) xác định nồng độ COD trong dòng vào (influent COD concentration) là biến quan trọng nhất để dự đoán hiệu quả loại bỏ COD.
- Kết quả khẳng định hiệu quả thực tế của AutoML trong mô hình hóa AnMBR và cung cấp cơ sở phương pháp luận cho việc xây dựng mô hình các quy trình xử lý nước thải dựa trên các tập dữ liệu nhỏ (small datasets).
