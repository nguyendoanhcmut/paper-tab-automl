### 2.4 Data Acquisition and Pre-processing

- Cấu trúc tập dữ liệu thực nghiệm thu thập từ hệ SAnMBR
  - Tập dữ liệu bao gồm chính xác 189 điểm đo thực nghiệm độc lập thu thập qua 189 ngày vận hành liên tục
  - Tập dữ liệu đạt tính toàn vẹn cao, không tồn tại bất kỳ giá trị khuyết thiếu (no missing entries) hay quan sát bị lỗi
- Phân loại không gian biến đầu vào và biến mục tiêu đầu ra
  - Sáu biến độc lập đầu vào ($X$) đại diện cho các điều kiện vận hành thủy lực, cơ chất và tải độc:
    - Nồng độ $\text{COD}$ dòng vào ($\text{COD}_{\text{in}}$, đơn vị $\text{mg/L}$)
    - Tải trọng nạp chất hữu cơ ($\text{OLR}$, đơn vị $\text{g COD/m}^3\cdot\text{day}$)
    - Nồng độ tải sốc phenolic dòng vào ($\text{2,4-DCP}_{\text{in}}$, đơn vị $\text{mg/L}$)
    - Độ đục dòng vào ($\text{Turbidity}_{\text{in}}$, đơn vị $\text{NTU}$)
    - Nồng độ tổng chất rắn lơ lửng dòng vào ($\text{TSS}_{\text{in}}$, đơn vị $\text{g/L}$)
    - Giá trị thế ion hydro dòng vào ($\text{pH}_{\text{in}}$)
  - Biến phụ thuộc mục tiêu ($Y$) duy nhất là hiệu suất loại bỏ nhu cầu oxy hóa học ($\text{COD removal efficiency}$, đơn vị $\%$)
- Chiến lược phân chia dữ liệu huấn luyện và kiểm tra độc lập
  - Tập dữ liệu được phân chia ngẫu nhiên theo tỷ lệ $70/30$ chuẩn mực
  - Tập huấn luyện (training set) chiếm $70\%$ quy mô dữ liệu (xấp xỉ 132 mẫu) dùng để tối ưu hóa trọng số mô hình
  - Tập kiểm tra (testing set) chiếm $30\%$ quy mô dữ liệu (xấp xỉ 56 mẫu) hoàn toàn độc lập dùng để đánh giá năng lực tổng quát hóa
- Quy trình chuẩn hóa Min-Max tránh rò rỉ thông tin
  - Phân tách tập huấn luyện và kiểm tra được tiến hành nghiêm ngặt trước bước chuẩn hóa dữ liệu nhằm loại trừ rò rỉ thông tin (data leakage)
  - Các tham số cực trị ($X_{\min}$, $X_{\max}$) được tính toán thuần túy trên tập huấn luyện rồi áp dụng biến đổi cho cả hai tập dữ liệu
  - Áp dụng phương pháp chuẩn hóa Min-Max để ánh xạ miền giá trị của từng đặc trưng về đoạn $[0, 1]$ theo công thức:
    $$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$
  - Quá trình chuẩn hóa triệt tiêu sự chênh lệch độ lớn thang đo giữa các biến nồng độ ($\text{mg/L}$) và chỉ số $\text{pH}$, đảm bảo cân bằng trọng số khi tối ưu hóa
