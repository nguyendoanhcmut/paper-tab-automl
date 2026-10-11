### 5.4 Memorization in Feature Engineering

- **Mối lo ngại về hiện tượng ghi nhớ dữ liệu trong các mô hình ngôn ngữ lớn**:
  - Các công trình nghiên cứu gần đây chỉ ra rằng các mô hình ngôn ngữ lớn (LLMs - Large Language Models) có thể vô tình ghi nhớ dữ liệu huấn luyện (unintentionally memorize data) dưới một số điều kiện nhất định (Carlini et al., 2021; Bordt et al., 2024).
  - Hiện tượng này dấy lên mối lo ngại về việc liệu những cải thiện hiệu năng đạt được từ LLM là kết quả của năng lực suy luận thực chất (genuine LLM reasoning) hay chỉ đơn thuần là sự tái hiện lại các mẫu dữ liệu trong tập huấn luyện (recalling training examples).
- **Thiết lập thực nghiệm kiểm chứng hiện tượng ghi nhớ (Experimental Setup)**:
  - Để thăm dò và làm rõ vấn đề này, các tác giả thực hiện đánh giá mô hình XGBoost ở hai trường hợp: không có LLM-FE (Base) và có kết hợp LLM-FE, sử dụng GPT-3.5-Turbo làm mô hình nền tảng.
  - **Tập dữ liệu từ Bordt et al. (2024)**: Các tập dữ liệu này được xây dựng một cách tường minh nhằm phát hiện hiện tượng ghi nhớ (explicitly constructed to detect memorization) và đã được xác nhận là hoàn toàn không xuất hiện trong quá trình tiền huấn luyện (model pretraining) của mô hình.
  - **Tập dữ liệu từ Hollmann et al. (2024)**: Được phát hành sau mốc thời gian giới hạn dữ liệu huấn luyện (training cutoff date) tháng 9/2021 của GPT và được cung cấp trên Kaggle với các phép chia tập dữ liệu ẩn (hidden splits), khiến cho khả năng mô hình từng tiếp xúc với dữ liệu trong giai đoạn tiền huấn luyện (pretraining exposure) gần như không thể xảy ra.
- **Kết quả thực nghiệm trên năm tập dữ liệu phân loại (Table 4)**:
  - Hiệu năng phân loại (độ chính xác kèm độ lệch chuẩn qua các lần chạy) của mô hình XGBoost khi không có (Base) và có LLM-FE:

| Dataset | Base | LLM-FE |
| :--- | :---: | :---: |
| kidney-stones | $0.761 \pm 0.024$ | $0.761 \pm 0.027$ |
| health-insurance | $0.756 \pm 0.001$ | $0.759 \pm 0.001$ |
| pharyngitis | $0.655 \pm 0.008$ | $0.660 \pm 0.023$ |
| fico | $0.715 \pm 0.006$ | $0.719 \pm 0.009$ |
| acs-income | $0.807 \pm 0.002$ | $0.809 \pm 0.003$ |

  - **Mức tăng hiệu năng khiêm tốn nhưng nhất quán**: Như thể hiện trong Table 4, LLM-FE mang lại mức cải thiện hiệu năng khiêm tốn nhưng nhất quán (modest but consistent performance gains) trên toàn bộ năm tập dữ liệu được thử nghiệm.
  - **Sự tương phản với các bộ sinh đặc trưng ngây thơ**: Kết quả này tạo nên sự tương phản rõ rệt với các bộ sinh đặc trưng LLM ngây thơ (naive LLM feature generators) - vốn có xu hướng vô tình bị quá khớp (overfit) hoặc tạo ra các mối quan hệ ảo giác về miền dữ liệu (hallucinate domain relationships).
- **Cơ chế tinh chỉnh tiến hóa đóng vai trò là màng lọc bảo vệ (Evolutionary Refinement as Safeguard)**:
  - Thay vì chỉ dựa vào các đầu ra thô (raw outputs) của LLM, LLM-FE tiến hành chọn lọc (selects), làm đột biến (mutates) và đánh giá (evaluates) lặp đi lặp lại các đặc trưng ứng viên dựa trên hiệu năng thực tế của mô hình hạ nguồn (downstream model performance).
  - Quy trình này đóng vai trò như một bộ lọc (filter), triệt tiêu có hệ thống các tạo tác bắt nguồn từ hiện tượng ghi nhớ (memorization-driven artifacts) và thúc đẩy các đặc trưng có khả năng tổng quát hóa (generalize) qua các vòng đánh giá lặp lại.
  - **Kết luận và định hướng nghiên cứu tương lai**: Mặc dù hiện tượng ghi nhớ vẫn là một rủi ro trọng yếu trong các quy trình làm việc trên dữ liệu dạng bảng có sự tham gia của LLM (LLM-driven tabular workflows), các kết quả thực nghiệm chỉ ra rằng quá trình tinh chỉnh tiến hóa (evolutionary refinement) cung cấp một cơ chế bảo vệ hữu hiệu (effective safeguard), đồng thời nhấn mạnh nhu cầu xây dựng các bộ đo chuẩn (benchmarks) trong tương lai để cô lập và kiểm thử áp lực (isolate and stress-test) đối với những hành vi này.
