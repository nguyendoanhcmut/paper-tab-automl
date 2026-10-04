### 4.3. LIME, Partial Dependence Plots, and Gradient-Based Methods

- **Phương pháp LIME (Local Interpretable Model-agnostic Explanations)**: LIME tạo ra các mô hình đại diện tuyến tính cục bộ (locally linear surrogate models) xung quanh từng dự đoán đơn lẻ bằng cách làm nhiễu (perturbing) các đặc trưng đầu vào và quan sát tác động đối với đầu ra của mô hình [27].
  - **Quy trình xây dựng mô hình đại diện cục bộ**: Đối với mỗi dự đoán cần giải thích, LIME lấy mẫu trong một vùng lân cận (neighborhood) xung quanh điểm dữ liệu đầu vào, gán trọng số cho các mẫu dựa trên khoảng cách (proximity) đến đầu vào gốc, và khớp một mô hình giải thích đơn giản (thường là hồi quy tuyến tính - linear regression hoặc cây quyết định nông - shallow decision tree) với các đầu ra được lấy mẫu.
  - **Giải thích hành vi mô hình hộp đen**: Các hệ số của mô hình đại diện cục bộ này đóng vai trò giải thích hành vi cục bộ của mô hình hộp đen (black-box model).
  - **Hiệu quả tính toán (computational efficiency)**: Lời giải thích có thể được tạo ra trong vài mili giây, phù hợp để tích hợp vào các bảng điều khiển vận hành thời gian thực (real-time operational dashboards) nơi độ trễ giải thích (explanation latency) là một yếu tố ràng buộc kỹ thuật.
  - **Hạn chế về tính thiếu nhất quán (inconsistency)**: Các giải thích cho các đầu vào tương tự nhau có thể biến thiên đáng kể do tác động của quá trình lấy mẫu ngẫu nhiên (random sampling), đồng thời việc lựa chọn bán kính vùng lân cận (neighborhood radius) ảnh hưởng trực tiếp đến độ ổn định của lời giải thích.
  - **Hiện trạng ứng dụng và khoảng trống nghiên cứu trong MBR**: Ứng dụng LIME chuyên biệt cho các mô hình tắc nghẽn màng (fouling) và kiểm soát quy trình MBR là một lĩnh vực mới nổi với số lượng nghiên cứu được bình duyệt (peer-reviewed) còn hạn chế; việc so sánh có hệ thống về hiệu năng giữa LIME và SHAP trong bối cảnh MBR là một khoảng trống cần nghiên cứu trong tương lai.

- **Biểu đồ phụ thuộc một phần (PDP) và đường kỳ vọng điều kiện cá thể (ICE)**: Biểu đồ PDP (Partial Dependence Plots) và đường cong ICE (Individual Conditional Expectation) cung cấp khả năng trực quan hóa toàn cục (global visualization) về mối quan hệ cận biên (marginal relationship) giữa từng đặc trưng đầu vào riêng lẻ và các dự đoán của mô hình [48].
  - **Đặc tính của biểu đồ PDP**: PDP biểu diễn đầu ra kỳ vọng của mô hình dưới dạng hàm số của một đặc trưng mục tiêu, được tính cận biên hóa (marginalized) trên toàn bộ phân phối của tất cả các đặc trưng còn lại.
  - **Đặc tính phân tách của đường cong ICE**: Đường cong ICE phân rã mối quan hệ này bằng cách hiển thị quan hệ phản ứng cho từng mẫu dữ liệu riêng biệt, làm sáng tỏ tính không đồng nhất (heterogeneity) trong hiệu ứng đặc trưng vốn bị che khuất trong giá trị trung bình của PDP.
  - **Phân tích ngưỡng nồng độ MLSS trong hệ MBR**: Phân tích PDP đối với nồng độ chất rắn lơ lửng trong bùn lỏng (MLSS concentration) trong các ứng dụng MBR phát hiện quy luật ngưỡng phi tuyến (non-linear threshold pattern):
    - Tốc độ tắc nghẽn màng (fouling rates) duy trì tương đối ổn định khi nồng độ MLSS dưới mức $10\text{--}12\ \text{g/L}$.
    - Tốc độ tắc nghẽn gia tăng dốc đứng khi MLSS vượt quá ngưỡng $10\text{--}12\ \text{g/L}$, phù hợp với hiện tượng chuyển pha quan sát được từ thực nghiệm từ động học huyền phù loãng (dilute suspension dynamics) sang hành vi bùn nhớt phi-Newton (viscous, non-Newtonian sludge behavior) trên ngưỡng nồng độ này.
  - **Biến thiên ngưỡng động học theo ICE**: Phân tích ICE chỉ ra thêm rằng ngưỡng nồng độ này dịch chuyển phụ thuộc vào nhiệt độ (temperature) và thời gian lưu bùn (SRT / Solids Retention Time):
    - Phản ánh các biến thiên theo mùa và theo điều kiện vận hành của khả năng lọc bùn (sludge filterability).
    - Làm phức tạp hóa việc áp dụng chiến lược điều khiển theo điểm đặt cố định (fixed-setpoint control) [48].

- **Các phương pháp quy gán dựa trên gradient (Gradient-based attribution methods)**: Được phát triển ban đầu cho học sâu (deep learning) trong thị giác máy tính và xử lý ngôn ngữ tự nhiên, các phương pháp này định lượng độ nhạy của đầu ra mô hình đối với các biến động đầu vào thông qua việc lấy vi phân giải tích (analytically differentiating) đồ thị tính toán (computational graph) [28,54].
  - **Các biến thể gradient trong giám sát hệ thống nước**: Các phương pháp gồm vanilla gradients, gradients tích hợp (integrated gradients - tính trung bình gradient dọc theo đường dẫn từ đường cơ sở tham chiếu baseline đến đầu vào thực tế), và guided backpropagation đã được ứng dụng cho các kiến trúc mạng nơ-ron chuỗi thời gian như LSTM và mô hình lai tích chập - tuần hoàn (convolutional-recurrent hybrids).
  - **Xác định bước thời gian nhạy cảm đối với dự đoán TMP trong MBR**: Đối với bài toán dự đoán áp suất xuyên màng (TMP / Transmembrane Pressure) bằng mô hình LSTM, bản đồ quy gán gradient (gradient attribution maps) định vị các bước thời gian mang lượng thông tin dự đoán cao nhất cho trạng thái TMP hiện tại:
    - Khoảng thời gian đóng góp thông tin cao nhất thường tương ứng với giai đoạn $2\text{--}8\ \text{h}$ ngay trước cửa sổ dự đoán (prediction window).
    - Cung cấp hiểu biết về thang thời gian đặc trưng (characteristic timescales) của quá trình hình thành và nén chặt lớp bánh bùn (cake layer formation and consolidation), phục vụ công tác lập lịch bảo trì màng [28].
  - **Tiềm năng nghiên cứu**: Ứng dụng các phương pháp quy gán gradient trong các mô hình học sâu chuyên biệt cho MBR đại diện cho một hướng nghiên cứu tiên phong với tiềm năng ứng dụng thực tế đáng kể.

- **Đặc tính và ứng dụng của các phương pháp XAI trong MBR và xử lý nước (Bảng 3)**: Bảng 3 tổng kết 5 phương pháp XAI chủ đạo được nhận diện trong các y văn nghiên cứu MBR và xử lý nước liên quan, so sánh chi tiết theo phạm vi giải thích, tính tương thích mô hình, chi phí tính toán và phạm vi ứng dụng [17,27,28,48,53,54,55]:
  - **SHAP**:
    - Phạm vi giải thích (Explanation Scope): Cục bộ và toàn cục (Local + Global).
    - Khả năng tương thích mô hình (Model Compatibility): Bất khả tri mô hình (Model-agnostic).
    - Chi phí tính toán (Comp. Cost): Trung bình đến cao (Medium–High).
    - Ứng dụng trong MBR và xử lý nước: Dự đoán tắc nghẽn màng (fouling prediction), tối ưu hóa năng lượng (energy optimization), dự đoán chất lượng nước đầu ra (effluent quality) [17,53].
  - **LIME**:
    - Phạm vi giải thích (Explanation Scope): Cục bộ (Local).
    - Khả năng tương thích mô hình (Model Compatibility): Bất khả tri mô hình (Model-agnostic).
    - Chi phí tính toán (Comp. Cost): Thấp đến trung bình (Low–Medium).
    - Ứng dụng trong MBR và xử lý nước: Phát hiện bất thường (anomaly detection), phân loại chất lượng nước (water quality classification) [27,55].
  - **PDP/ICE**:
    - Phạm vi giải thích (Explanation Scope): Toàn cục (Global).
    - Khả năng tương thích mô hình (Model Compatibility): Bất khả tri mô hình (Model-agnostic).
    - Chi phí tính toán (Comp. Cost): Thấp (Low).
    - Ứng dụng trong MBR và xử lý nước: Xác định ngưỡng đặc trưng (feature threshold identification), phân tích đường cong vận hành (operating curve analysis) [48].
  - **Integrated Gradients**:
    - Phạm vi giải thích (Explanation Scope): Cục bộ theo thời gian (Local (temporal)).
    - Khả năng tương thích mô hình (Model Compatibility): Mạng nơ-ron (Neural networks).
    - Chi phí tính toán (Comp. Cost): Thấp (Low).
    - Ứng dụng trong MBR và xử lý nước: Dự báo tắc nghẽn màng bằng mô hình LSTM (LSTM fouling forecasting), quy gán thuộc tính thời gian (temporal attribution) [28,54].
  - **ANCHORS**:
    - Phạm vi giải thích (Explanation Scope): Cục bộ dựa trên tập luật (Local (rule-based)).
    - Khả năng tương thích mô hình (Model Compatibility): Bất khả tri mô hình (Model-agnostic).
    - Chi phí tính toán (Comp. Cost): Cao (High).
    - Ứng dụng trong MBR và xử lý nước: Nghiên cứu khái niệm: trích xuất quy tắc vận hành (Conceptual: operational rule extraction) [27].

- **Mối liên hệ giữa khả năng giải thích của XAI và bài toán tối ưu hóa năng lượng trong MBR**: Trong khi các phương pháp XAI giải quyết rào cản về tính minh bạch để thúc đẩy triển khai ML, bài toán vận hành song hành cấp thiết trong các hệ thống MBR là hiệu quả sử dụng năng lượng:
  - **Chi phí năng lượng sục khí**: Năng lượng sục khí dùng cho mục đích thổi rửa bề mặt màng (membrane scouring) và xử lý sinh học (biological treatment) chiếm tỷ trọng tiêu hao năng lượng chi phối lớn nhất trong hệ thống MBR.
  - **Vai trò của mô hình hóa ML**: Hoạt động tối ưu hóa quá trình sục khí phụ thuộc vào các mối quan hệ phi tuyến phức tạp trong quy trình mà các mô hình ML có khả năng nắm bắt thích hợp.
  - **Mục tiêu nghiên cứu chuyển tiếp**: Cần kiểm chứng cơ sở bằng chứng cho bài toán tối ưu hóa năng lượng điều khiển bằng ML và thiết lập các điểm chuẩn (benchmarks) rõ ràng làm thước đo cho các tiến bộ công nghệ tiếp theo.
