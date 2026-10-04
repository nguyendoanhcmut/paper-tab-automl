### 6.2. XAI Integration in Digital Twin Decision Architecture

- **Tích hợp mô-đun XAI làm tầng hỗ trợ quyết định và minh bạch trong kiến trúc Digital Twin MBR**: Việc tích hợp các mô-đun trí tuệ nhân tạo có thể giải thích (Explainable Artificial Intelligence - XAI) làm tầng hỗ trợ ra quyết định và tăng cường tính minh bạch nằm giữa động cơ dự đoán (prediction engine) và các hành động kiểm soát hoặc con người ở hạ nguồn (downstream human or control actions) đại diện cho bước tiến kiến trúc trọng yếu của các bản sao kỹ thuật số (Digital Twin - DT) MBR có độ trưởng thành cao:
  - Cải thiện tính diễn giải (interpretability), độ tin cậy (trust) và khả năng ứng dụng trong vận hành thực tế (operational usability) [62, 63].
  - Định dạng hiển thị giải thích cho người vận hành:
    - Định dạng trực quan dễ hiểu: biểu đồ thác nước SHAP (SHAP waterfall chart) hoặc biểu đồ thanh xếp hạng đóng góp cục bộ (local ranked bar plot).
    - Định dạng văn bản tóm tắt định hướng người dùng (user-oriented summary text).
  - Mục đích thực tiễn: Cho phép người vận hành đánh giá tính hợp lý của dự đoán (prediction plausibility) dựa trên trạng thái quy trình hiện tại trước khi quyết định hành động [64].

- **Ba chức năng vận hành cốt lõi của tầng XAI trong kiến trúc điều khiển MBR hỗ trợ Digital Twin**:
  - Cung cấp dấu vết kiểm toán cận thời gian thực (near-real-time audit trail): Ghi nhật ký bối cảnh giải thích đi kèm các khuyến nghị do mô hình đưa ra, nâng cao tính truy xuất nguồn gốc (traceability), trách nhiệm giải trình (accountability) và hỗ trợ rà soát sau sự việc (post hoc review) trong kiểm toán nội bộ, đánh giá tuân thủ và thanh tra quy chuẩn pháp lý [65].
  - Kích hoạt quyền ghi đè có cơ sở của người vận hành (informed operator override):
    - Thay vì chấp nhận hoặc từ chối thụ động khuyến nghị từ ML, người vận hành sử dụng phân bổ đóng góp SHAP (SHAP attribution) để xác định chính xác biến số cụ thể nào đang dẫn dắt dự đoán.
    - Đánh giá các biến dẫn dắt phản ánh trạng thái quy trình thực tế hay là sai số đo lường (measurement artefact), thiết lập sự giám sát có hiểu biết của con người thay vì từ chối mù quáng [17, 66].
  - Cảnh báo trôi dạt khái niệm có thể diễn giải (interpretable warning signals of concept drift): Những biến đổi rõ rệt trong quy luật giải thích, như sự thay đổi trong phân bố xếp hạng SHAP (marked changes in SHAP ranking distributions), cảnh báo hiện tượng trôi dạt khái niệm hoặc vận hành ngoài phạm vi quen thuộc của mô hình (outside the model's familiar regime), từ đó kích hoạt con người rà soát trước khi tiếp tục điều khiển tự động [48, 67].

- **Luồng dữ liệu và quyết định năm giai đoạn trong Digital Twin MBR Cấp độ II/III tích hợp XAI**: Cấu trúc luồng xử lý khép kín bảo đảm XAI được nhúng về mặt cấu trúc vào luồng quyết định (decision pipeline) thay vì hoạt động như một mô-đun hậu nghiệm tùy chọn (optional post-hoc module):
  - Giai đoạn 1 (Thu nhận và tiền xử lý dữ liệu cảm biến): Các luồng dữ liệu cảm biến thô gồm oxy hòa tan (dissolved oxygen - $\text{DO}$), áp suất xuyên màng (transmembrane pressure - $\text{TMP}$), thông lượng nước thấm (permeate flux), độ đục (turbidity), nhiệt độ (temperature) và lưu lượng sục khí màng (membrane aeration flow rate) được truyền từ nhà máy vật lý qua hệ thống $\text{SCADA}$ theo chu kỳ $1\text{ phút}$ ($1\text{-minute intervals}$) về tầng dữ liệu DT; tại đây dữ liệu được kiểm tra chất lượng, điền khuyết bằng phương pháp nội suy (gap-filled by interpolation) và lưu trữ trong cơ sở dữ liệu chuỗi thời gian (time-series database).
  - Giai đoạn 2 (Động cơ dự đoán ML): Động cơ dự đoán ML đã huấn luyện — như mô hình Random Forest hoặc Long Short-Term Memory ($\text{LSTM}$) cho dự báo $\text{TMP}$, và Gradient Boosting cho ước tính chất lượng nước đầu ra (effluent quality) — tạo ra dự báo trước từ $12\text{ đến }72\text{ h}$ ($12\text{ to }72\text{ h ahead}$) dựa trên lịch sử cảm biến hiện tại và gần đây.
  - Giai đoạn 3 (Mô-đun giải thích SHAP theo thời gian thực): Tính toán giá trị gán đóng góp cho từng đặc trưng (per-feature attribution values) cho mỗi dự đoán theo thời gian thực (real time), tạo biểu đồ đóng góp có xếp hạng (ranked contribution plot) xác định biến quy trình nào đang chi phối dự báo hiện tại và biên độ chi phối cụ thể.
  - Giai đoạn 4 (Bảng điều khiển trực quan cho người vận hành): Dự đoán và giải thích SHAP được trình bày đồng thời trên bảng điều khiển trực quan (interpretable operator dashboard), hỗ trợ con người rà soát có cơ sở trước khi thực thi bất kỳ hành động điều khiển nào.
  - Giai đoạn 5 (Tầng điều khiển và lưu vết kiểm toán): Khuyến nghị được chấp thuận chuyển sang tầng điều khiển (control layer) để điều chỉnh điểm đặt sục khí (aeration setpoints), mục tiêu thông lượng (flux targets) hoặc lịch làm sạch màng (cleaning schedules) theo yêu cầu; đồng thời dự đoán cùng giải thích tự động lưu vào dấu vết kiểm toán (audit trail) phục vụ truy xuất quy chuẩn pháp lý và rà soát sau sự kiện.

- **Tính diễn giải là yêu cầu thiết kế nền tảng cho Digital Twin công nghiệp đáng tin cậy**:
  - Tao và cộng sự [32] cùng Barricelli và cộng sự [33] xác định tính diễn giải (interpretability) là yêu cầu thiết kế cơ bản cho DT công nghiệp đáng tin cậy.
  - Những khuyến nghị mô hình không được giải thích trong điều kiện quy trình mới lạ, dù chính xác về mặt định lượng, vẫn bị những người vận hành thận trọng ghi đè một cách có hệ thống (systematically overridden by conservative operators), làm triệt tiêu giá trị vận hành của DT.
  - Tích hợp XAI vào kiến trúc DT là yêu cầu chức năng thiết yếu để xây dựng niềm tin của người vận hành, điều kiện tiên quyết để chuyển từ vận hành khuyến nghị Cấp độ II (Tier II advisory) sang vận hành kê toa Cấp độ III (Tier III prescriptive).
  - Sự kết hợp giữa dự đoán ML, tính minh bạch XAI và kiểm tra tính nhất quán bằng mô hình cơ chế (mechanistic model consistency checking) trong một kiến trúc DT thống nhất cấu thành khung làm việc hoàn chỉnh nhất cho vận hành MBR thông minh ở trình độ công nghệ hiện nay [37].

- **Đặc tính năng lực và triển khai của ba cấp độ trưởng thành Digital Twin (Bảng 5)**: Hệ thống phân loại gồm Cấp độ I (Mô tả), Cấp độ II (Dự đoán) và Cấp độ III (Kê toa) phản ánh sự gia tăng về độ phức tạp và yêu cầu dữ liệu [5, 15, 24, 26, 33, 36, 37]:
  - Bảng 5. Các cấp độ trưởng thành của Digital Twin cho hệ thống MBR cùng đặc tính năng lực và triển khai:
    - Cấp độ I — Mô tả (Tier I — Descriptive): Năng lực giám sát thời gian thực, bảng điều khiển trực quan, quản lý cảnh báo (real-time monitoring, dashboards, alarm management); yêu cầu dữ liệu $\text{SCADA}$ và cảm biến trực tuyến (online sensors); độ phức tạp triển khai Thấp (Low); tình trạng đã triển khai thương mại tại các công trình thực tế (commercially deployed) [5, 15].
    - Cấp độ II — Dự đoán (Tier II — Predictive): Năng lực dự báo $\text{TMP}$, dự đoán chất lượng nước đầu ra, phát hiện sự cố trước từ $12\text{ đến }72\text{ h}$ ($12\text{–}72\text{ h ahead}$); yêu cầu dữ liệu $\text{SCADA}$, phân tích phòng thí nghiệm (lab analytics) và mô hình ML đã huấn luyện (trained ML); độ phức tạp triển khai Trung bình (Medium); tình trạng đã xác thực trong mô phỏng và dữ liệu quy mô thực (validated in simulation and full-scale data) [24, 26, 36].
    - Cấp độ III — Kê toa (Tier III — Prescriptive): Năng lực tối ưu hóa tự động vòng kín (closed-loop autonomous optimization), thử nghiệm kịch bản giả định "what-if" (what-if scenario testing), biện minh quyết định bằng XAI (XAI decision justification); yêu cầu dữ liệu DT đầy đủ, cơ cấu chấp hành (actuators), XAI và xác thực an toàn (safety validation); độ phức tạp triển khai Cao (High); tình trạng chưa ghi nhận triển khai ở quy mô đầy đủ trong tài liệu MBR (no full-scale MBR deployment documented) [33, 37].

- **Tình trạng bằng chứng thực nghiệm của ba cấp độ trưởng thành Digital Twin**:
  - Cấp độ I đã triển khai thương mại ở quy mô đầy đủ tại các công trình đô thị và công nghiệp trên toàn thế giới [5, 15], đại diện cho công nghệ vận hành đã được kiểm chứng (validated operational technology).
  - Cấp độ II được chứng minh qua mô phỏng $\text{BSM-MBR}$ [36] và xác thực trên bộ dữ liệu $\text{SCADA}$ quy mô đầy đủ (Kovacs và cộng sự, $2022$ [26]), nhưng chưa vận hành liên tục như một hệ thống khuyến nghị vòng kín trong nhà máy chính thức (commissioned plant); tình trạng bằng chứng dừng ở mức xác thực từ mô phỏng đến dữ liệu quy mô thực (simulation-to-full-scale data validation).
  - Cấp độ III dừng ở giai đoạn đề xuất khái niệm và kiến trúc: Chưa có triển khai MBR quy mô thực tế nào kết hợp kiểm soát kê toa Tier III và biện minh quyết định XAI được ghi nhận trong y văn bình duyệt tính đến tháng $12\text{ năm }2025$.
  - Bước chuyển dịch từ Tier II sang Tier III đại diện cho ranh giới công nghệ chính của lĩnh vực, gắn liền trực tiếp với các khoảng trống nghiên cứu tại Mục 7.

- **Bản đồ nhiệt tổng hợp định tính mức độ trưởng thành nghiên cứu các ứng dụng MBR thông minh**:
  - Tiêu chí đánh giá gồm $3$ yếu tố: khối lượng bằng chứng bình duyệt hiện có, khả năng xác thực vận hành ở quy mô thực tế, và mức độ ghi nhận triển khai trong các công trình xử lý nước đã vận hành chính thức.
  - Bốn mức đánh giá định tính: Cao (`High` - nền tảng bằng chứng đáng kể từ nhiều nghiên cứu độc lập với kết quả nhất quán), Trung bình (`Moderate` - nền tảng bằng chứng đang hình thành có xác thực pilot hoặc quy mô thực), Mới nổi (`Emerging` - lĩnh vực được thừa nhận nhưng bằng chứng giới hạn ở đề xuất khái niệm, mô phỏng hoặc quy mô phòng thí nghiệm), và Thấp (`Low` - không ghi nhận bằng chứng bình duyệt trong tìm kiếm có cấu trúc).

- **Phân hóa mức độ trưởng thành giữa năng lực dự đoán thuật toán và độ sẵn sàng triển khai thực tế trong hệ thống MBR**:
  - **Hình 3.** Bản đồ nhiệt mức độ trưởng thành nghiên cứu MBR thông minh
    - <img src="assets/fig_04_p19.jpeg" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - Thể hiện sự chênh lệch lớn giữa năng lực dự đoán thuật toán và độ sẵn sàng ứng dụng thực tế trên các mảng nghiệp vụ MBR.
    - **Từ đâu mà thấy được**
      - Trục hoành (5 chiều triển khai): Evidence base, Predictive maturity, Interpretability integration, Full-scale validation, Deployment readiness.
      - Trục tung (5 lĩnh vực ứng dụng): Fouling prediction, Energy optimization, Effluent quality estimation, XAI-supported interpretation, Digital twin deployment.
      - Thang màu 4 mức: High (vàng), Moderate (xanh lục), Emerging (xanh lam), Low (tím); Fouling prediction đạt High ở 2 cột đầu, trong khi Digital twin deployment có 2 ô Low và 1 ô Moderate.
      - Lưu ý: hình ghi ô Interpretability integration của Digital twin deployment là Moderate, văn bản ghi Emerging hoặc Low trên cả 5 chiều.

- **Ba quy luật phân bố mức độ trưởng thành phản ánh các khoảng trống công nghệ then chốt**:
  - Dự đoán bám bẩn (fouling prediction) sở hữu nền tảng bằng chứng và độ trưởng thành dự đoán cao nhất (đều xếp hạng `High`), phản ánh khối lượng nghiên cứu ML dồi dào; tuy nhiên tích hợp khả năng giải thích, xác thực quy mô thực và độ sẵn sàng triển khai đều ở mức `Emerging`, cho thấy năng lực dự đoán vượt xa ứng dụng thực tế.
  - Diễn giải hỗ trợ bởi XAI (XAI-supported interpretation) đạt mức `High` ở chiều tích hợp khả năng giải thích, nhưng xác thực quy mô thực ở mức `Low` và độ sẵn sàng triển khai ở mức `Emerging`, khẳng định XAI trong MBR chủ yếu vẫn là nghiên cứu học thuật.
  - Triển khai Digital Twin (digital twin deployment) có mức trưởng thành tổng thể thấp nhất với các đánh giá `Emerging` hoặc `Low` trên tất cả $5$ chiều (hình ghi chiều Interpretability integration đạt `Moderate`), phản ánh sự vắng bóng của các triển khai vận hành quy mô thực trong y văn bình duyệt.
  - Mỗi ô có mức độ trưởng thành thấp ánh xạ trực tiếp đến một hoặc nhiều khoảng trống trong số $9$ khoảng trống nghiên cứu tại Mục 7, định hình lộ trình trực quan cho việc ưu tiên nguồn lực đầu tư nghiên cứu.
