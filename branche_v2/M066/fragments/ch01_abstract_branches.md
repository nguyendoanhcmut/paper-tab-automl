## Tóm tắt (Abstract)

* Ứng dụng machine learning (ML - học máy) hỗ trợ dự đoán các chỉ số hiệu năng then chốt trong quá trình xử lý nước thải, tạo điều kiện tối ưu hóa kiểm soát vận hành và giảm thiểu các thách thức kỹ thuật như hiện tượng nghẹt màng (membrane fouling).
* Nghiên cứu triển khai các phương pháp ML để đánh giá hiệu quả loại bỏ COD và hiện tượng nghẹt màng trong hệ thống bể phản ứng sinh học màng kỵ khí nhiệt độ trung bình (mesophilic AnMBR) xử lý nước rỉ rác trạm trung chuyển (transfer station landfill leachate) vận hành liên tục trong $120\text{ ngày}$.
  * Hệ thống AnMBR đạt hiệu suất loại bỏ COD $\ge 80\%$ ở tải trọng hữu cơ (OLR) $6.4\text{ kg COD/m}^3\cdot\text{d}$ và thời gian lưu thủy lực (HRT) $6.5\text{ ngày}$.
* Ba mô hình học máy bao gồm mạng nơ-ron nhân tạo (ANN), rừng ngẫu nhiên (RF) và extreme gradient boosting (XGBoost) được xây dựng để dự đoán COD dòng ra (effluent COD) và áp suất qua màng (TMP).
  * Mô hình RF đạt hiệu năng dự đoán cao nhất cho cả hai biến đầu ra:
    * Dự đoán effluent COD: $R^2 = 0.96$; $\text{RMSE} = 331.50\text{ mg/L}$.
    * Dự đoán TMP: $R^2 = 0.88$; $\text{RMSE} = 3.86\text{ kPa}$.
* Phân tích SHapley Additive exPlanations (SHAP) xác định các đặc trưng chi phối khả năng dự đoán của mô hình:
  * Đối với effluent COD: OLR, HRT và thế oxy hóa - khử (ORP) là các biến dự đoán chính gắn liền với mô hình.
  * Đối với TMP: $\text{NH}_4^+-\text{N}$ dòng ra, pH dòng ra và ORP đóng góp mạnh nhất vào kết quả dự đoán TMP.
* Kết quả chứng minh việc tích hợp vận hành AnMBR với mô hình dự đoán ML có khả năng giải thích (interpretable ML) mang lại các hiểu biết chẩn đoán hữu ích cho việc tối ưu hóa hiệu quả xử lý nước rỉ rác và quản lý nghẹt màng.
