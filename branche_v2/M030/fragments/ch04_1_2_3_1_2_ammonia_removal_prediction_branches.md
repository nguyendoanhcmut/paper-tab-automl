#### 3.1.2. Ammonia removal prediction

- Ứng dụng mô hình mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) để dự đoán hiệu suất loại bỏ amoni (ammonia removal) của hệ thống MBR từ tập các điều kiện đầu vào (input conditions).
- Mối tương quan giữa các giá trị thực tế đo đạc (real / measured values) và giá trị do mô hình dự đoán (predicted values) được thể hiện ở Fig. 8:
  - **Hình 8.** Dự đoán hiệu suất loại bỏ amoni bằng mô hình ANN
    - <img src="assets/fig_08_p10.jpeg" alt="Hình 8" />
    - **Hình này chứng minh điều gì**
      - Sai số dự đoán thấp và duy trì tương quan tuyến tính trên toàn dải loại bỏ amoni, dữ liệu tập trung nhiều nhất ở khoảng $30$–$60$.
    - **Từ đâu mà thấy được**
      - Ox: Real Ammonia Removal, thang đo $0$–$100$. Oy: Predicted Ammonia Removal, thang đo $0$–$100$.
      - Các điểm dữ liệu bám sát đường chéo đỏ $1:1$; góc phải dưới ghi nhận hệ số xác định $R^2 = 0.8679$.
  - Mô hình ANN đạt hiệu suất cao với các giá trị sai số tuyệt đối trung bình (Mean Absolute Error - $\text{MAE}$) và sai số toàn phương trung bình (Mean Squared Error - $\text{MSE}$) đều ở mức thấp.
  - Các kết quả dự báo đạt độ tin cậy và quyết đoán thỏa đáng (adequately assertive) với hệ số xác định $R^2 = 0.868$.
  - Mức sai số giữa giá trị dự đoán của mô hình và giá trị đo đạc thực tế là thấp, chứng minh mô hình ANN có hiệu quả cao trong việc nắm bắt và dự đoán hành vi loại bỏ amoni của MBR.
- Khả năng ứng dụng cho quan trắc trực tuyến (online monitoring):
  - Dù được xây dựng từ tập dữ liệu quan trắc ngoại tuyến (offline monitoring data), kết quả này chứng minh tiềm năng rõ rệt của mô hình ANN trong giám sát trực tuyến các hệ thống xử lý nước thải MBR.
  - Nhờ năng lực dự đoán cao, mô hình có thể dự báo các mẫu dữ liệu mới để đánh giá xem hệ thống có đang vận hành đúng kỳ vọng hay đang gặp phải sự cố vận hành (operating problem).
- Hỗ trợ ra quyết định và nâng cao hiệu quả vận hành theo thời gian thực (real-time operation):
  - Việc cung cấp dữ liệu kịp thời theo thời gian thực giúp hỗ trợ quá trình ra quyết định quyết đoán và chính xác hơn (more assertive decision-making).
  - Cải thiện công tác giám sát và kiểm soát quy trình xử lý, đóng góp vào việc vận hành hệ thống hiệu quả và tối ưu hơn.
