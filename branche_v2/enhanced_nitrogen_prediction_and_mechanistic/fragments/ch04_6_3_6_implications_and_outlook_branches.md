### 3.6 Implications and outlook

- Ý nghĩa thực tiễn đối với điều khiển quy trình công nghệ và tối ưu hóa vận hành nhà máy xử lý nước thải:
  - Khung mô hình CatBoost cải thiện đáng kể độ chính xác so với mô hình tốt thứ hai LightGBM ($9\%$ hệ số $R^2$ và $14\%$ sai số $RMSE$).
  - Phân tích SHAP phát hiện sự cạnh tranh cơ chất cacbon gay gắt khi hiệu suất khử $COD$ tăng cao, làm bỏ đói vi sinh vật tự dưỡng.
  - Phân tích thác nước SHAP chỉ ra rằng ở nhiệt độ dưới $20^\circ\text{C}$, hoạt tính enzyme Nar suy giảm mạnh theo quy luật Arrhenius.
  - Tác động suy giảm động học này giảm bớt khi nhiệt độ vượt mốc $25^\circ\text{C}$ nhờ quán tính nhiệt của sinh khối bùn hoạt tính.
  - Nghiên cứu đề xuất ngưỡng kiểm soát oxy hòa tan chính xác trong khoảng $0.5\text{–}1.2\ \text{mg/L}$ để cân bằng nitrat hóa và khử nitrat.
  - Mức khuyến nghị này tối ưu hơn các hướng dẫn sục khí chung chung trước đây, giúp tiết kiệm đáng kể chi phí điện năng máy thổi khí.
- Các giới hạn nghiên cứu hiện tại và định hướng phát triển trong tương lai:
  - Mô hình yêu cầu quy trình hiệu chuẩn mở rộng khi áp dụng cho các nguồn nước thải có thành phần hữu cơ phức tạp hoặc biến động độ mặn lớn.
  - Cần duy trì hệ thống quan trắc tự động liên tục các thông số môi trường để cung cấp dữ liệu đầu vào ổn định cho mô hình dự báo.
  - Nghiên cứu hiện tại tập trung chủ yếu vào nước thải mặn tổng hợp và cần kiểm chứng trên các hệ thống quy mô công nghiệp thực tế.
  - Các nghiên cứu tiếp theo cần tích hợp tác động đồng thời của các yếu tố gây độc hại khác như kim loại nặng hoặc chất ô nhiễm hữu cơ khó phân hủy.
  - Việc đưa thêm các thông số áp suất màng, chất hấp phụ và tốc độ bám bẩn màng sẽ giúp hoàn thiện chiến lược điều khiển tự động hóa.
