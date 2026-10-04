### 3.5. Limitations and future perspectives

- AutoML thể hiện tiềm năng là một công cụ mô hình hóa hiệu quả cho hệ thống màng sinh học kỵ khí (anaerobic membrane bioreactor - AnMBR) trong điều kiện dữ liệu hạn chế, tuy nhiên nghiên cứu tồn tại một số hạn chế cần lưu ý:
  - Khả năng khái quát hóa của mô hình phụ thuộc vào thiết lập thực nghiệm cụ thể:
    - Mặc dù AutoML đạt hiệu năng cao hơn các mô hình trước đây theo cùng chiến lược phân chia dữ liệu cố định (identical fixed data split strategy), các kết quả này chỉ mang tính biểu thị (indicative) trong phạm vi thiết lập thực nghiệm riêng biệt.
    - Kết quả không khẳng định ưu thế tuyệt đối (not definitively superior) trên mọi mô hình và mọi kịch bản vận hành.
  - Giới hạn diễn giải về mức độ đóng góp của đặc trưng:
    - Việc một số đặc trưng nhất định như $\text{MLSS}$ (mixed liquor suspended solids) và $\text{MLVSS}$ (mixed liquor volatile suspended solids) đóng góp ít hơn vào mô hình phản ánh kết quả mô hình hóa, không phản ánh bản chất vật lý hay sinh học.
    - Các kết quả này đại diện cho độ quan trọng đặc trưng mang tính thống kê (statistical feature importance), không phải mối quan hệ nhân quả theo cơ chế (mechanistic causality).
  - Tác động của chất lượng dữ liệu và hiện tượng dịch chuyển phân phối:
    - Việc hiệu năng không cải thiện khi mở rộng sang tập dữ liệu lớn hơn không đồng nghĩa với việc dung lượng dữ liệu (data volume) là vô ích.
    - Kết quả nhấn mạnh tầm quan trọng cốt lõi của tính nhất quán (data consistency) và chất lượng dữ liệu thay vì số lượng đơn thuần.
    - Sự thay đổi hiệu năng phản ánh tác động của hiện tượng dịch chuyển phân phối (distribution shifts) trong các quá trình động học của AnMBR khi xử lý nước thải.
  - Bản chất tiền định của mô hình và định hướng tiếp cận xác suất:
    - Nghiên cứu hiện tại chỉ cung cấp các ước lượng điểm mang tính xác định (deterministic point estimates).
    - Các nghiên cứu tương lai có thể tích hợp các phương pháp tiếp cận xác suất (probabilistic approaches) nhằm hỗ trợ tốt hơn cho việc ra quyết định vận hành (operational decision-making).
    - Phương pháp xác suất cho phép thiết lập các khoảng dự đoán (prediction intervals) và định lượng độ bất định (uncertainty quantification), cung cấp thông tin bao quát hơn cho công tác mô hình hóa xử lý nước thải bằng phương pháp sinh học.
