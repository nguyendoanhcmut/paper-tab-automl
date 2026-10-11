### 5.1 Efficiency Analysis

- **Tầm quan trọng của khâu đánh giá chất lượng đặc trưng trong các quy trình tự động (Role of Feature Evaluation in Pipelines)**:
  - Việc đánh giá chất lượng đặc trưng (feature quality) thông qua việc huấn luyện và kiểm định mô hình lặp đi lặp lại (repeated model training and validation) là thành phần cốt lõi của các đường ống kỹ thuật đặc trưng tự động (automated feature engineering pipelines).
  - Quy trình đánh giá lặp này được áp dụng chung cho cả các phương pháp truyền thống (classical methods) lẫn các phương pháp tiếp cận dựa trên mô hình ngôn ngữ lớn (LLM-based methods).

- **Thiết lập phần cứng và định nghĩa thời gian chạy thực nghiệm (Hardware Setup and Runtime Metrics)**:
  - Toàn bộ các phép đo thời gian chạy (runtime measurements) được thu thập trên một hệ thống phần cứng đồng nhất trang bị 4 GPU NVIDIA RTX8000 ($4\text{ NVIDIA RTX8000 GPUs}$).
  - **Định nghĩa thời gian chạy cho các phương pháp dựa trên LLM (LLM-based methods)**: Đo lường toàn bộ quy trình hoàn chỉnh từ thời điểm khởi động vòng lặp đầu tiên đến khi kết thúc vòng lặp cuối cùng, bao gồm:
    - Độ trễ gọi API của LLM (LLM API latency).
    - Thời gian thực thi chương trình biến đổi đặc trưng (feature program execution).
    - Thời gian huấn luyện mô hình học máy (model training).
  - **Định nghĩa thời gian chạy cho các phương pháp đối chuẩn cổ điển (Classical baselines)**: Tính toàn bộ thời gian của đường ống hoàn chỉnh từ khâu sinh đặc trưng (feature generation), chọn lọc đặc trưng (feature selection), đến khâu đánh giá đặc trưng (feature evaluation).

- **Tối ưu hóa hiệu năng tính toán trong thiết kế kiến trúc LLM-FE (Computational Efficiency in LLM-FE Design)**:
  - **Mô hình đa đảo không phát sinh phụ phí (Multiple evolutionary islands without overhead)**: Dù LLM-FE duy trì đồng thời nhiều đảo tiến hóa (multiple evolutionary islands), thiết kế này trong thực tế không hề gây thêm phụ phí tính toán (computational overhead).
  - **Chiến lược lấy mẫu đa đầu ra (Sampling multiple outputs per call)**: LLM-FE tiến hành lấy mẫu nhiều kết quả đầu ra trên mỗi lần gọi LLM, giúp giảm thiểu đáng kể tổng số lượng truy vấn API (reducing the number of API calls).

- **Phân tích biên Pareto về sự đánh đổi giữa hiệu năng và thời gian tính toán (Pareto Analysis: Time vs Performance)**:
  - Phân tích biên Pareto (Pareto analysis) được thực hiện trên nhóm các tập dữ liệu có quy mô lớn hơn từ Section 4.4, đối chiếu thời gian chạy (runtime tính bằng giây) và hiệu năng dự đoán (predictive performance / accuracy).
  - **Hình 3.** Phân tích Pareto đánh đổi giữa độ chính xác và thời gian tính toán
    - <img src="assets/fig_03_p8_vector.png" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - LLM-FE xác lập biên Pareto tối ưu, đạt hiệu năng dự đoán cao nhất với thời gian chạy cạnh tranh so với các đối chuẩn.
    - **Từ đâu mà thấy được**
      - Trục hoành Time ($0 - 700\text{ s}$), trục tung Performance ($0.83 - 0.86$): LLM-FE nằm trên đỉnh biên Pareto với accuracy cao nhất (~$0.862$) trong ~$120\text{ s}$, nhanh hơn nhiều so với CAAFE (~$400\text{ s}$, ~$0.852$) và OpenFE (~$685\text{ s}$, ~$0.848$), đồng thời vượt trội về độ chính xác so với OCTree (~$95\text{ s}$, ~$0.841$) và Base LLM (~$10\text{ s}$, ~$0.837$).
  - **Vị trí tối ưu nhất quán của LLM-FE**: Kết quả thực nghiệm chỉ ra rằng LLM-FE luôn nằm trên biên Pareto (Pareto frontier), đạt hiệu năng dự đoán cao hơn hẳn với thời gian chạy gần tương đương OCTree và thấp hơn rất nhiều so với CAAFE.
  - **So sánh tương quan với các phương pháp cạnh tranh**:
    - **CAAFE và OpenFE**: Đòi hỏi chi phí thời gian chạy rất lớn (substantially more runtime), trong đó CAAFE mất ~$400\text{ s}$ và OpenFE mất tới ~$685\text{ s}$.
    - **OCTree**: Thất bại trong việc bắt kịp mức độ chính xác của LLM-FE dù thời gian chạy tương đối ngắn (~$95\text{ s}$ so với ~$120\text{ s}$ của LLM-FE).
    - **Mô hình cơ sở (Base LLM)**: Dù tốn ít chi phí tính toán nhất (~$10\text{ s}$), Base LLM phải chịu mức thâm hụt hiệu năng dự đoán rất nặng nề (steep performance deficit, chỉ đạt ~$0.837$).

- **Đánh giá tổng thể về sự đánh đổi hiệu quả và hiệu năng (Overall Efficiency-Performance Trade-off)**:
  - LLM-FE mang lại tỷ lệ đánh đổi giữa hiệu quả tính toán và hiệu năng dự đoán tốt nhất (best efficiency–performance trade-off) trong số toàn bộ các phương pháp được thử nghiệm.
  - Phương pháp thiết lập kỷ lục hiệu năng dự đoán hiện đại (state-of-the-art predictive performance) trên các tập dữ liệu dạng bảng lớn và phức tạp mà không làm phát sinh chi phí tính toán dư thừa nào.
