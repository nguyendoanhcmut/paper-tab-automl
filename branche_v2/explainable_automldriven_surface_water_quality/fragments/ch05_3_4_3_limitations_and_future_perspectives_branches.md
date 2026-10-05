### 4.3 Limitations and future perspectives

- **Giới hạn về phạm vi chỉ tiêu và dữ liệu sinh học**:
  - Nghiên cứu chỉ tập trung vào $9$ chỉ tiêu thông dụng, chưa bao quát toàn bộ $24$ chỉ tiêu theo quy chuẩn quốc gia.
  - Các thông số ô nhiễm đặc thù như kim loại nặng, phenol bay hơi và dầu mỏ chưa được đưa vào mô hình do thiếu dữ liệu quan trắc tự động liên tục.
  - Các chỉ tiêu sinh học như diệp lục a và mật độ tảo bị loại trừ do tỷ lệ khuyết thiếu dữ liệu vượt quá $70\%$.
  - Nghiên cứu tương lai cần mở rộng thu thập dữ liệu đa tầng để đánh giá đầy đủ các khía cạnh sinh thái nguồn nước.
- **Thách thức khi khuyết thiếu dữ liệu thời gian thực**:
  - Mô hình yêu cầu phải có đầy đủ bộ $3$ chỉ số then chốt ($\text{COD}_{\text{Mn}}$, $\text{TP}$, $\text{DO}$) để thực hiện phân loại.
  - Sự cố hỏng hóc cảm biến hoặc mất kết nối truyền dữ liệu có thể làm gián đoạn khả năng dự báo của hệ thống.
  - Hướng nghiên cứu tiếp theo là kết hợp mô hình chuỗi thời gian (như RNN, Transformer) để bù khuyết số liệu lịch sử trước khi đưa vào bộ phân loại AutoML (mô hình hai giai đoạn).
- **Khả năng nhân rộng và định hướng chính sách**:
  - Cung cấp giải pháp định hướng dữ liệu giúp các cơ quan quản lý thiết kế mạng lưới quan trắc tối ưu về mặt kinh tế.
  - Tính linh hoạt cao khi cho phép điều chỉnh chỉ tiêu theo đặc thù lưu vực (như bổ sung $\text{NH}_3\text{-N}$ tại miền Bắc).
  - Khung làm việc hạ thấp rào cản kỹ thuật thuật toán, tạo tiền đề xây dựng hệ thống quản lý môi trường nước thông minh.
