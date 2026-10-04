## 8. Conclusions

- **Tổng kết cơ sở bằng chứng về ML, XAI và Digital Twin trong MBR**: Bài tổng quan đã tổng hợp bằng chứng từ các nguồn tài liệu bình duyệt về ứng dụng học máy (ML - Machine Learning), trí tuệ nhân tạo có thể giải thích (XAI - Explainable Artificial Intelligence), và bản sao số (DT - Digital Twin) trong xử lý nước thải bằng bể phản ứng sinh học màng (MBR - Membrane Bioreactor), giải quyết $4$ mục tiêu đánh giá cốt lõi đã đặt ra ở Phần 1:
  - Khái quát hóa tiến trình phát triển và các rào cản kỹ thuật của ML trong dự đoán tắc nghẽn màng.
  - Đánh giá vai trò minh bạch hóa và giải thích quyết định của các kỹ thuật XAI.
  - Phân tích hiệu quả và tiềm năng tối ưu hóa năng lượng sục khí bằng mô hình hóa và ML.
  - Làm rõ cấu trúc tích hợp, cấp độ trưởng thành và tiềm năng của hệ thống Digital Twin.

- **Sự trưởng thành của các mô hình ML dự đoán tắc nghẽn màng và áp suất qua màng TMP (Transmembrane Pressure)**:
  - **Mức độ chính xác của các kiến trúc ML**: Các phương pháp học kết hợp (ensemble methods, đặc biệt là Random Forest - RF) và các tiếp cận dựa trên kernel (kernel-based approaches, tiêu biểu là Least Squares Support Vector Machine - LSSVM) đạt hệ số xác định $R^2 = 0.85\text{--}0.99$ trên các hệ thống quy mô phòng thí nghiệm (laboratory), bán công nghiệp (pilot) và quy mô đầy đủ (full-scale).
  - **Hiệu năng so sánh với ANN**: Các mô hình ensemble và kernel-based liên tục đạt hiệu năng cao hơn (consistently outperforming) các cấu trúc mạng nơ-ron nhân tạo tiêu chuẩn (standard ANN architectures).
  - **Kiểm chứng quy mô đầy đủ bằng dữ liệu lịch sử**: Kết quả kiểm chứng RF ở quy mô đầy đủ trên hơn $80{,}000$ mẫu vận hành ($R^2 = 0.927\text{--}0.996$, sai số căn quân phương $\text{RMSE} = 0.264\text{--}0.904\text{ kPa}$) đại diện cho một kết quả kiểm chứng lịch sử (historical validation) mạnh mẽ.
  - **Giới hạn giữa kiểm chứng dữ liệu lưu trữ và triển khai vận hành thực tế**: Kiểm chứng lịch sử trên dữ liệu SCADA lưu trữ (archived SCADA data) không tương đương với kiểm chứng triển khai vận hành thực tế (operational deployment validation).
  - **Thách thức điều kiện trực tiếp (live conditions)**: Hiệu năng vòng kín (closed-loop performance) dưới các điều kiện vận hành trực tiếp — bao gồm hiện tượng trôi dạt cảm biến (sensor drift), nhiễu tín hiệu (noise), và độ trễ dữ liệu (data latency) — hiện vẫn chưa được chứng minh trên thực tế.
  - **Điều kiện tiên quyết trước khi triển khai**: Việc kiểm chứng đặc thù theo từng địa điểm (site-specific validation) và thiết lập các cơ chế bảo đảm quản trị (governance safeguards) vẫn là những điều kiện tiên quyết bắt buộc trước khi đưa mô hình vào các hệ thống giám sát MBR vận hành thực tế.

- **Vai trò chi phối của phân tích SHAP trong việc xác định các biến dự đoán và cơ chế tắc nghẽn**:
  - **Các biến dự đoán chiếm ưu thế (dominant predictors)**: Các phân tích dựa trên SHAP (SHapley Additive exPlanations) trong các nghiên cứu MBR thường xuyên xác định nồng độ chất rắn lơ lửng trong bùn lỏng MLSS (Mixed Liquor Suspended Solids), thời gian lưu bùn SRT (Solids Retention Time), thời gian lưu thủy lực HRT (Hydraulic Retention Time), và cường độ sục khí (aeration intensity) là các biến dự đoán chi phối.
  - **Tính tương thích cơ chế và khả năng ứng dụng thực tế**: Các phát hiện từ SHAP đồng thời xác thực hiểu biết cơ chế (mechanistic understanding) và cung cấp cho người vận hành bằng chứng có thể hành động được (operator-actionable evidence) về những biến số quan trọng nhất đối với việc kiểm soát tắc nghẽn màng [17, 25, 42].
  - **Cơ sở lý thuyết và thực tiễn của SHAP**: Sự chiếm ưu thế của SHAP trong các công bố tích hợp XAI phản ánh cả nền tảng lý thuyết bắt nguồn từ lý thuyết trò chơi hợp tác (cooperative game theory) lẫn khả năng ứng dụng thực tế cho việc diễn giải kỹ thuật (engineering interpretation).

- **Hiệu quả tối ưu hóa năng lượng sục khí và khoảng trống nghiên cứu chuyên biệt cho ML**:
  - **Mốc chuẩn kiểm chứng từ các tiếp cận dựa trên mô hình và điều khiển hồi tiếp**: Các phương pháp tiếp cận dựa trên mô hình (model-based) và điều khiển hồi tiếp (feedback-control) đã xác nhận khả năng cắt giảm tới $20\%$ nhu cầu năng lượng sục khí tại các công trình MBR quy mô đầy đủ [59], thiết lập một mốc chuẩn đã được kiểm chứng (validated benchmark) cho việc kiểm soát dựa trên mô hình (model-informed control).
  - **Khoảng trống nghiên cứu then chốt về tối ưu hóa năng lượng bằng ML**: Các nghiên cứu minh chứng dành riêng cho việc tối ưu hóa năng lượng chuyên biệt bằng ML (dedicated ML-specific energy optimization demonstrations) vẫn còn hạn chế.
  - **Ý nghĩa đối với hiệu quả vận hành**: Sự thiếu hụt các thử nghiệm ML chuyên biệt này đại diện cho khoảng trống nghiên cứu có tác động trực tiếp và tức thì nhất (most immediately impactful research gap) đối với hiệu quả năng lượng vận hành thực tế.

- **Kiến trúc Digital Twin đa tầng và yêu cầu tích hợp XAI**:
  - **Cấu trúc tích hợp mô hình cơ chế và ML**: Các khung bản sao số (Digital Twin frameworks) tích hợp các mô hình thành phần cơ chế ASM (mechanistic Activated Sludge Models sub-models) với các hiệu chỉnh từ ML (ML corrections) cung cấp nền tảng kiến trúc cho quản lý MBR Cấp độ II dự đoán (Tier II predictive) và Cấp độ III chỉ định (Tier III prescriptive).
  - **Bắt buộc chức năng của mô-đun XAI**: Việc nhúng các mô-đun minh bạch quyết định XAI (XAI decision-transparency modules) trong kiến trúc DT là một yêu cầu chức năng bắt buộc (functional requirement), không đơn thuần là một tính năng mong muốn (not merely a desirable feature), nhằm tạo dựng niềm tin của người vận hành (operator trust) — yếu tố cần thiết cho việc điều khiển chỉ định tự chủ (autonomous prescriptive control).
  - **Ranh giới công nghệ hiện tại**: Cho đến nay chưa có bất kỳ triển khai MBR Cấp độ III nào ở quy mô đầy đủ tích hợp XAI được ghi nhận trong y văn, đánh dấu đây là ranh giới nghiên cứu hàng đầu (primary frontier) của lĩnh vực.

- **Chín khoảng trống nghiên cứu then chốt cần điều tra có hệ thống (nine critical research gaps)**:
  - **Bộ dữ liệu chuẩn đối sánh đa cơ sở (standardized multi-facility benchmark datasets)**: Xây dựng các tập dữ liệu chuẩn đối sánh được chuẩn hóa thu thập từ nhiều nhà máy xử lý khác nhau.
  - **Định lượng độ không đảm bảo đã hiệu chuẩn (calibrated uncertainty quantification)**: Ước tính độ không đảm bảo đã được hiệu chuẩn trong các dự đoán ML phục vụ vận hành thực tế.
  - **Bằng chứng triển khai Digital Twin quy mô đầy đủ (full-scale DT deployment evidence)**: Thu thập và chứng minh các bằng chứng triển khai DT trong điều kiện vận hành nhà máy thực tế.
  - **Tích hợp động công nghệ xác định đặc tính nước thải đầu vào (dynamic integration of influent characterization technology)**: Ứng dụng các công nghệ cảm biến và phân tích động đối với thành phần và lưu lượng dòng vào.
  - **Đánh giá thực nghiệm XAI theo khung quy chuẩn pháp lý (empirical evaluation of XAI within regulatory acceptance frameworks)**: Kiểm chứng thực nghiệm năng lực giải trình của XAI đáp ứng các yêu cầu chấp thuận pháp lý và giấy phép xả thải.
  - **Báo cáo minh bạch chi phí phát triển và tái huấn luyện mô hình (transparent reporting of ML model development and retraining costs)**: Minh bạch hóa các khoản chi phí liên quan đến việc thu thập dữ liệu, huấn luyện ban đầu, và duy trì tái huấn luyện định kỳ mô hình ML.
  - **Xây dựng năng lực nhân lực vận hành tại các đơn vị cấp thoát nước (workforce capacity building for DT and XAI operations at water utilities)**: Đào tạo kỹ năng chuyên môn cho đội ngũ kỹ sư và công nhân vận hành để tiếp nhận và sử dụng hệ thống DT và XAI.
  - **Đối sánh có hệ thống với các mốc cơ sở điều khiển truyền thống (systematic benchmarking of ML-based control against PID and fuzzy logic baselines)**: Thực hiện đánh giá đối chuẩn bài bản giữa các thuật toán điều khiển dựa trên ML với các bộ điều khiển PID (Proportional-Integral-Derivative) và logic mờ (fuzzy logic).
  - **Báo cáo dấu chân năng lượng tính toán của các mô hình học sâu (reporting of computational energy footprints for deep learning models)**: Minh bạch mức tiêu thụ năng lượng phục vụ tính toán và huấn luyện của các mô hình Deep Learning triển khai trong các hệ thống xử lý môi trường.

- **Lộ trình tương lai: Sự hội tụ hướng tới vận hành MBR thông minh và đáng tin cậy**:
  - **Lộ trình ngắn hạn triển vọng nhất (most promising near-term pathway)**: Sự hội tụ giữa dự đoán ML có thể giải thích (interpretable ML prediction), tính minh bạch từ XAI (XAI transparency), và mô phỏng bản sao số theo thời gian thực (real-time digital twin simulation) đại diện cho con đường ngắn hạn triển vọng nhất để đạt được vận hành MBR thông minh và đáng tin cậy.
  - **Yêu cầu đầu tư đồng bộ và liên tục**: Hiện thực hóa tầm nhìn này đòi hỏi sự đầu tư bền bỉ, có phối hợp vào:
    - Cơ sở hạ tầng dữ liệu mở (open data infrastructure).
    - Quy trình đường ống mô hình nhận biết độ không đảm bảo (uncertainty-aware model pipelines).
    - Quan hệ đối tác triển khai quy mô đầy đủ (full-scale deployment partnerships).
    - Sự tham gia gắn kết với các khuôn khổ pháp lý và quy chuẩn (engagement with regulatory frameworks).
  - **Hợp tác liên ngành bắt buộc**: Các đóng góp thiết yếu này phải đến từ hành động phối hợp chặt chẽ giữa $3$ cộng đồng: kỹ thuật xử lý nước (water engineering), khoa học dữ liệu (data science), và quản trị nguồn nước (water governance).

- **Thông tin bổ trợ và tuyên bố liên quan (Supplementary Materials & Statements)**:
  - **Tài liệu bổ trợ (Supplementary Materials)**: Bảng S1 (Table S1) cung cấp dữ liệu trích xuất cấp nghiên cứu (study-level data extraction) cho các công trình ML, XAI, và DT trên hệ thống MBR đã được tổng quan.
  - **Tài trợ (Funding)**: Nghiên cứu không nhận nguồn tài trợ từ bên ngoài.
  - **Tuyên bố về tính khả dụng của dữ liệu (Data Availability Statement)**: Không có dữ liệu mới nào được tạo ra hoặc phân tích trong nghiên cứu này.
  - **Xung đột lợi ích (Conflicts of Interest)**: Tác giả tuyên bố không có xung đột lợi ích.
