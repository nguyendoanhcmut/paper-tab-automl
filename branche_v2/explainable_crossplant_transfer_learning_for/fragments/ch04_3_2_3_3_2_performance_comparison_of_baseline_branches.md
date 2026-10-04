#### 3.3.2. Performance comparison of baseline model and transfer learning models

- **Thiết lập đánh giá đối chứng hiệu suất dự đoán trên nhà máy mục tiêu**: Hiệu suất dự đoán trên nhà máy mục tiêu (target plant) được đánh giá đối chứng giữa mô hình đường cơ sở (baseline model - được huấn luyện đặc thù chỉ dựa trên các tập dữ liệu thu thập tại chính nhà máy mục tiêu) cùng hai mô hình học chuyển giao (transfer learning) gồm LSTM-FT và XGBoost-FT (Hình 5(d)):
  - Cả hai mô hình chuyển giao đều áp dụng quy trình tinh chỉnh (fine-tuning) dựa trên tập dữ liệu hạn chế từ nhà máy mục tiêu sau khi đã được huấn luyện trước (pretrained) trên ba nhà máy nguồn.

- **Đặc điểm phân bố của tập mẫu kiểm tra theo các dải áp suất xuyên màng**: Các mẫu kiểm tra (testing samples) của nhà máy mục tiêu phân bố tập trung chủ yếu trong dải TMP (transmembrane pressure - áp suất xuyên màng) từ khoảng $19\text{--}21.5\text{ kPa}$:
  - Số lượng mẫu kiểm tra xuất hiện ít hơn ở dải giá trị TMP thấp hơn, dao động trong khoảng $15.5\text{--}18\text{ kPa}$.

- **Mức độ hội tụ quanh đường bình đẳng giữa các mô hình trên đồ thị phân tán**: Trong dải TMP hoạt động chính ($19\text{--}21.5\text{ kPa}$), mô hình LSTM-FT thể hiện sự phân cụm chặt chẽ nhất xung quanh đường bình đẳng (line of equality), phản ánh mức độ tương đồng cao nhất giữa các giá trị TMP dự đoán và giá trị TMP quan sát thực nghiệm:
  - Mô hình baseline ghi nhận các độ lệch ở mức vừa phải (moderate deviations) so với đường bình đẳng.
  - Ngược lại, XGBoost-FT thể hiện mức độ phân tán lớn nhất (largest scatter) và độ lệch rõ rệt nhất khỏi đường bình đẳng.
  - Sự phân bố phân tán này cho thấy học chuyển giao giúp cải thiện khả năng dự đoán tại nhà máy mục tiêu khi được triển khai với mạng nơ-ron hồi quy LSTM, trong khi cấu trúc XGBoost-FT không mang lại lợi thế hiệu suất nào trong thiết lập thực nghiệm hiện tại.

- **Định lượng cải thiện hiệu suất của mô hình LSTM-FT so với baseline model**: Các chỉ số sai số và độ chính xác định lượng phản ánh cùng xu hướng tương tự như biểu hiện trực quan trên đồ thị phân tán:
  - So với mô hình baseline, mô hình LSTM-FT giảm sai số căn quân phương (RMSE - Root Mean Square Error) từ $0.63\text{ kPa}$ xuống còn $0.50\text{ kPa}$, tương ứng với mức giảm $20.6\%$.
  - LSTM-FT giảm sai số tuyệt đối trung bình (MAE - Mean Absolute Error) từ $0.45\text{ kPa}$ xuống còn $0.33\text{ kPa}$, tương ứng với mức giảm $26.7\%$.
  - LSTM-FT nâng cao hệ số xác định ($R^2$) từ $0.82$ lên $0.89$.

- **Sự suy giảm hiệu suất dự đoán của mô hình XGBoost-FT so với baseline model**: Cấu trúc cây quyết định tăng cường gradient tinh chỉnh (XGBoost-FT) ghi nhận sự suy giảm chất lượng dự đoán rõ rệt so với mô hình đường cơ sở:
  - RMSE của XGBoost-FT tăng lên mức $0.96\text{ kPa}$ (so với $0.63\text{ kPa}$ của baseline).
  - MAE của XGBoost-FT tăng lên mức $0.81\text{ kPa}$ (so với $0.45\text{ kPa}$ của baseline).
  - Hệ số xác định $R^2$ của XGBoost-FT giảm xuống còn $0.58$ (so với $0.82$ của baseline).

- **Kết luận so sánh và định hướng nghiên cứu cơ chế tiếp theo**: Tổng hợp các kết quả thực nghiệm chỉ ra rằng mô hình LSTM-FT đạt hiệu suất dự đoán cao nhất trong điều kiện dữ liệu hạn chế tại nhà máy mục tiêu, cho kết quả tốt hơn cả mô hình baseline lẫn XGBoost-FT:
  - Do LSTM-FT thể hiện khả năng học chuyển giao hiệu quả nhất, các nội dung tiếp theo của nghiên cứu tập trung chuyên sâu vào mô hình LSTM-FT để phân tích và diễn giải cơ chế chuyển giao thông qua hai phương pháp LOFO (Leave-One-Feature-Out) và SHAP (SHapley Additive exPlanations).
