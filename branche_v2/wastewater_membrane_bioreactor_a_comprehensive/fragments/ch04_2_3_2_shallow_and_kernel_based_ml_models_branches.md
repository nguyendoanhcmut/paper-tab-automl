### 3.2. Shallow and Kernel-Based ML Models

- **Tiêu chuẩn lựa chọn nghiên cứu và giới hạn so sánh đối chuẩn (benchmarking)**: Các công trình tổng quan trong phần này đáp ứng đầy đủ tiêu chí lựa chọn tại mục "Literature Search and Study Selection", gồm báo cáo tối thiểu một chỉ số hiệu suất định lượng và áp dụng phương pháp luận ML nguyên bản trên dữ liệu vận hành hoặc thực nghiệm MBR:
  - So sánh đối chuẩn trực tiếp giữa các nghiên cứu bị giới hạn bởi tính dị thể (heterogeneity) về biến mục tiêu (target variables), quy mô tập dữ liệu (dataset sizes) và điều kiện vận hành (operating conditions).
  - Các chỉ số hiệu suất cần được diễn giải trong phạm vi từng nghiên cứu cụ thể thay vì xem là bảng xếp hạng tuyệt đối (absolute rankings).

- **Mô hình mạng nơ-ron nhân tạo (ANN) trong dự đoán tắc nghẽn màng (fouling prediction)**: ANN là một trong những kiến trúc ML đầu tiên được áp dụng có hệ thống vào việc dự đoán hiện tượng nghẽn màng trong MBR:
  - Mirbagheri và cộng sự so sánh mạng perceptron đa tầng (Multilayer Perceptron - MLP) và mạng hàm cơ sở xuyên tâm (Radial Basis Function - RBF) để dự đoán áp suất xuyên màng (Transmembrane Pressure - TMP) và độ thấm (permeability) trong hệ MBR đặt ngập quy mô pilot (pilot-scale submerged MBR) [23]:
    - Các biến đầu vào gồm thời gian, $\text{TSS}$, $\text{COD}$, $\text{SRT}$ và $\text{MLSS}$ thu thập qua đợt vận hành thử nghiệm kéo dài $60\text{ ngày}$.
    - Cả hai kiến trúc đều cho kết quả dự đoán thỏa đáng; trong đó mạng RBF cho thấy tốc độ hội tụ nhanh hơn và giảm độ nhạy đối với các điều kiện trọng số ban đầu (initial weight conditions), hỗ trợ triển khai mô hình trực tuyến (online model deployment).
    - Nghiên cứu nhấn mạnh tầm quan trọng của việc lựa chọn biến đầu vào và đảm bảo tính đa dạng của dữ liệu huấn luyện đối với khả năng tổng quát hóa ngoài giai đoạn huấn luyện.
  - Schmitt và cộng sự phát triển mô hình ANN lan truyền ngược (backpropagation ANN) để dự đoán nghẽn màng trong hệ MBR thiếu khí - hiếu khí (anoxic-aerobic MBR) xử lý nước thải sinh hoạt [25]:
    - Mô hình đạt hệ số xác định $R^2 = 0.850$ trên tập dữ liệu kiểm tra độc lập (held-out test data).
    - Mức hiệu suất này phản ánh tính biến thiên cố hữu trong vận hành quy mô pilot và thách thức khi mô hình hóa động học tắc nghẽn bằng số lượng biến đầu vào hạn chế.

- **Phương pháp dựa trên hàm hạt nhân (kernel-based methods) và đối chuẩn các mô hình nông**: Các phương pháp kernel ánh xạ dữ liệu đầu vào lên không gian đặc trưng nhiều chiều hơn để học các ranh giới quyết định phi tuyến tính mà không cần kiến trúc học sâu, đạt hiệu suất cạnh tranh cao:
  - Hamedi và cộng sự thực hiện nghiên cứu đối chuẩn so sánh ANN-MLP, ANN kết hợp tối ưu hóa bầy đàn hạt (ANN-PSO), lập trình biểu thức gen (Gene Expression Programming - GEP) và máy vector hỗ trợ bình phương tối thiểu (Least-Squares Support Vector Machine - LSSVM) để dự đoán trở lực tắc nghẽn (fouling resistance) trong hệ MBR phòng thí nghiệm [42]:
    - LSSVM đạt hiệu suất cao nhất với $R^2 = 0.990$ và $\text{MSE} = 0.0002$, cao hơn đáng kể so với tất cả các biến thể ANN.
    - Phân tích độ nhạy (sensitivity analysis) chỉ ra thông lượng dòng thấm (permeate flux) và TMP là các biến đầu vào chi phối, hoàn toàn phù hợp với khung lý thuyết trở lực nối tiếp (resistance-in-series framework).
    - Kết quả chứng minh phân tích tầm quan trọng của đặc trưng trong ML có khả năng tái hiện thứ bậc các biến có ý nghĩa về mặt cơ chế vật lý.
  - Giwa và cộng sự áp dụng mô hình ANN cho hệ submerged MBR xử lý hỗn hợp nước thải công nghiệp và đô thị tại UAE [43]:
    - Các đặc tính của nước cấp (độ dẫn điện, $\text{pH}$, chất rắn lơ lửng) đóng vai trò là các biến dự đoán quan trọng đối với các thông số chất lượng nước đầu ra gồm $\text{COD}$, $\text{BOD}$ và độ đục (turbidity).
    - Hiệu suất của ANN phụ thuộc mang tính quyết định vào độ đa dạng của dữ liệu huấn luyện qua nhiều điều kiện tải khác nhau.
  - Nguyen và cộng sự áp dụng hồi quy cây quyết định (decision tree regression), hồi quy vector hỗ trợ (Support Vector Regression - SVR) và hồi quy tuyến tính (linear regression) để dự đoán TMP trong hệ MBR xử lý nước thải sinh hoạt [44]:
    - Hồi quy cây quyết định đạt $R^2 = 0.99$.
    - Kết quả này cần được đánh giá thận trọng do tập dữ liệu có kích thước nhỏ và chỉ thu thập tại một cơ sở duy nhất; giá trị $R^2$ cao nhiều khả năng phản ánh hiện tượng khớp vào cấu trúc nhiễu đặc thù của tập dữ liệu thay vì tạo ra mô hình fouling có khả năng khái quát hóa.

- **Thống kê xu hướng ứng dụng ML và khoảng trống nghiên cứu thực tiễn**: Khảo sát tổng hợp của Queiroz và cộng sự phân tích $57$ nghiên cứu ML về dự đoán hiệu suất MBR [45]:
  - Các mô hình ANN được ứng dụng trong $88\%$ các trường hợp nghiên cứu.
  - Báo cáo xác định khoảng trống nghiên cứu then chốt: chưa có nghiên cứu nào ứng dụng ML để dự đoán tuổi thọ màng (membrane lifespan) hoặc thời điểm thay thế màng (membrane replacement timing).
  - Khoảng trống nghiên cứu này có liên hệ trực tiếp đến hiệu quả kinh tế vận hành của các nhà máy xử lý nước.

- **Tổng kết từ các nghiên cứu khảo sát và vai trò của mô hình lai ML - cơ chế**: Các nghiên cứu tổng quan đã đánh giá có hệ thống thực trạng mô hình hóa ML trong lĩnh vực MBR:
  - Schmitt và Do tổng quan các hướng tiếp cận ML mô hình hóa tắc nghẽn màng MBR trên hơn $30$ nghiên cứu [24]:
    - Tính sẵn có và tính đại diện của dữ liệu là các rào cản chính hạn chế khả năng tổng quát hóa của mô hình.
    - Đề xuất các chiến dịch quan trắc liên tục dài hạn (long-duration continuous monitoring campaigns) là yêu cầu tối thiểu về tập dữ liệu để phát triển mô hình đáng tin cậy.
  - Shi và cộng sự đánh giá các ứng dụng ML trên phạm vi rộng hơn của các quá trình lọc màng [38]:
    - Các mô hình lai ML - cơ chế (hybrid ML–mechanistic models) — sử dụng các phương trình cơ chế để tính toán các đặc trưng đầu vào phái sinh (derived input features) trước khi đưa vào dự đoán ML — đạt hiệu suất cao hơn một cách nhất quán so với các phương pháp tiếp cận thuần túy hộp đen (black-box) trong các thử nghiệm kiểm định chéo (cross-validation).
    - Lợi thế của mô hình lai thể hiện rõ nét khi ngoại suy ra ngoài phạm vi vận hành của dữ liệu huấn luyện.
