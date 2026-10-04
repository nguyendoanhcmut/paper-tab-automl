## 5 Summary and prospect

- **Hiện trạng ứng dụng học máy trong MBR và ba thách thức cốt lõi**:
  - Các mô hình học máy (machine learning models), bao gồm mạng nơ-ron nhân tạo (ANN - Artificial Neural Networks), máy vector hỗ trợ (SVM - Support Vector Machines), và cây quyết định (decision trees), đã được ứng dụng để dự đoán hiệu năng lọc màng (membrane filtration performances) trong bioreactor màng (MBR - Membrane Bioreactors).
  - Nhiều mô hình đã được báo cáo là thể hiện hiệu năng khớp dữ liệu (fitting performance) và khả năng khái quát hóa (generalization ability) tương đối tốt.
  - Các tham số mô hình (model parameters) có thể được tối ưu hóa bằng các thuật toán tối ưu hóa thông minh (intelligent optimization algorithms) như thuật toán di truyền (GA - Genetic Algorithm) và tối ưu hóa bầy đàn (PSO - Particle Swarm Optimization) nhằm nâng cao khả năng dự đoán (predictability).
  - Việc ứng dụng phương pháp giải thích cộng tính Shapley (SHAP - SHapley Additive exPlanations) để giải thích các mô hình dự đoán MBR đã phát triển nhanh chóng (Aldrees et al., 2024a; Niu et al., 2024).
  - Các mô hình hiện tại đang đối mặt với các thách thức ở ba khía cạnh:
    - (a) Các đặc trưng đầu vào (input features) và chỉ số giám sát (monitoring indices) chưa đầy đủ.
    - (b) Khả năng giải thích (interpretability) và khả năng khái quát hóa (generalizability) của dự đoán mô hình còn hạn chế.
    - (c) Thiếu sự ứng dụng trong kiểm soát quy trình tự động (automated process control).
  - Tình trạng này đòi hỏi những tiến bộ xa hơn trong các kỹ thuật mô hình hóa (modeling techniques) và sự tích hợp sâu hơn của mô hình vào thế giới vật lý (physical world) (chẳng hạn như các hệ thống giám sát và điều khiển - monitoring and control systems).
  - Khuyến nghị khám phá các ràng buộc (constraints) và giải pháp nâng cao (enhancements) của học máy trong các ứng dụng kiểm chứng kỹ thuật MBR (engineering validation applications) ở bốn cấp độ (four levels): cấu thành các đặc trưng mô hình, giám sát trực tuyến các đặc trưng mô hình, ứng dụng hướng tới kiểm soát quy trình, cùng chia sẻ dữ liệu và khái quát hóa.

- **Cấp độ 1: Mở rộng và chuẩn hóa cấu thành đặc trưng mô hình (constitution of model features)**:
  - Các tham số đầu vào của mô hình (model input parameters) có thể được mở rộng nhằm đạt được mô tả chính xác và bao quát hơn về các đặc trưng then chốt:
    - Thay vì chỉ sử dụng các chỉ số thô truyền thống (conventional rough indices) để mô tả tắc nghẽn màng tổng thể (overall membrane fouling), các chỉ số cụ thể có thể được tinh chỉnh để mô tả chính xác hơn hành vi tắc nghẽn (fouling behavior) (ví dụ: tiềm năng tắc nghẽn [fouling potential] cho các giai đoạn tắc nghẽn cụ thể) và đặc tính của chất gây tắc nghẽn (foulant properties) (ví dụ: nồng độ polysaccharide, protein, chất mùn [humus concentrations] và các đặc trưng phân tử [molecular characteristics]).
    - Cần mở rộng hệ thống chỉ số hiện tại hướng tới việc bao phủ đầy đủ hơn các yếu tố tiềm năng.
    - Bổ sung trạng thái vận hành màng vào mô hình dự đoán hiệu quả loại bỏ chất ô nhiễm: Các mô hình trước đây về hiệu quả loại bỏ chất ô nhiễm (pollutant removal efficiency) ít chú ý hơn đến ảnh hưởng của trạng thái vận hành màng (áp suất xuyên màng $\text{TMP}$ - transmembrane pressure, thông lượng $\text{flux}$, độ thấm $\text{permeability}$, chỉ số tắc nghẽn biến đổi $\text{MFI}$ - modified fouling index, v.v.) và khả năng lưu giữ chất ô nhiễm tương ứng của màng (pollutant interception by the membrane).
    - Đưa chỉ số vận hành ($\text{OI}$ - operating index) vào mô hình dự đoán tắc nghẽn màng: Trong các mô hình dự đoán tắc nghẽn, $\text{MFI}$ và chỉ số tắc nghẽn kết hợp ($\text{CCI}$ - combined fouling index) thường xuyên được sử dụng làm tham số đầu vào, trong khi $\text{OI}$ (liên quan đến quá trình rửa ngược màng [backwash] và sục khí làm sạch màng [scouring]) vẫn chưa được đưa vào một cách thỏa đáng.
    - Tích hợp các tham số nồng độ truyền thống (traditional concentration parameters) với trạng thái màng (membrane status) và điều kiện vận hành (operating conditions) trong các mô hình tiếp theo.
    - Việc bổ sung các chỉ số giám sát chính xác và hoàn chỉnh này làm đặc trưng đầu vào sẽ tạo điều kiện thuận lợi cho việc ứng dụng học máy trong các quy trình MBR.

- **Cấp độ 2: Phát triển giám sát trực tuyến các đặc trưng then chốt (online monitoring of model features)**:
  - Giám sát trực tuyến (online monitoring) các tham số then chốt đóng vai trò quyết định trong việc phát triển các mô hình "thông minh" (smart models) có khả năng phản ứng kịp thời với trạng thái vận hành theo thời gian thực của MBR:
    - Các hạng mục giám sát trực tuyến thông thường bao gồm nhiệt độ (temperature), $\text{pH}$, oxy hòa tan ($\text{DO}$ - dissolved oxygen), độ đục (turbidity), và nhu cầu oxy hóa học ($\text{COD}$ - chemical oxygen demand), v.v.
    - Các chỉ số thông thường này không đủ để cung cấp chi tiết chính xác về các chất ô nhiễm và chất gây tắc nghẽn (pollutants/foulants) phục vụ mô hình hóa.
    - $\text{COD}$ chỉ có thể phản ánh nồng độ tổng thể của chất hữu cơ (overall concentration of organic matter) mà không tiết lộ chi tiết về thành phần hóa học (chemical composition) và cấu trúc phân tử (molecular structure).
    - Các phép đo tỉ mỉ (elaborate measurements) trong phòng thí nghiệm về các đặc tính này thường tốn nhiều công sức (laborious), mất nhiều thời gian (time-consuming), và không phù hợp cho giám sát trực tuyến (unsuitable for online monitoring).
    - Các phương pháp quang phổ (spectroscopic methods) (như quang phổ tử ngoại - ultraviolet, khả kiến - visible, và huỳnh quang - fluorescence spectroscopy) mở ra những khả năng mới để phản ánh chi tiết phân tử theo thời gian thực (real-time reflection of molecular details).
    - Kỹ thuật quang phổ sở hữu ưu thế nhanh chóng (fast), độ nhạy cao (sensitive), và giàu thông tin (informative) để khám phá dấu vân tay phân tử (molecular fingerprints), đóng vai trò là nguồn bổ sung triển vọng cho hệ thống giám sát trực tuyến.
    - Kết hợp các chỉ số quang phổ trực tuyến (online spectral indicators) với trạng thái vận hành màng và các điều kiện điều khiển (control conditions) mang lại lợi ích lớn trong việc phát triển các mô hình thực sự có thể triển khai để kiểm soát quy trình (implementable for process control).

- **Cấp độ 3: Thiết lập mô hình truyền thẳng phục vụ cảnh báo sớm và kiểm soát chủ động (application toward process control)**:
  - Các mô hình truyền thẳng (feedforward models) là yêu cầu thiết yếu nhằm hỗ trợ cảnh báo sớm (early warning) và kiểm soát chủ động (proactive control) các quy trình MBR:
    - Để tối ưu hóa vận hành MBR về mặt loại bỏ chất ô nhiễm và giảm thiểu tắc nghẽn, các hành động phòng ngừa (preventive actions) cần được thực hiện từ sớm thay vì chỉ phản ứng bị động sau khi các sự cố bất lợi (adverse events) xảy ra.
    - Các hệ thống MBR hiện tại vẫn đang thiếu cơ chế kiểm soát truyền thẳng (feedforward control).
    - Mặc dù hầu hết các mô hình đã chứng minh hiệu năng tương đối tốt trong việc mô phỏng các dữ kiện hiện có (simulating existing facts), khả năng dự đoán các xu hướng tương lai (future tendencies) của chúng vẫn chưa đầy đủ.
    - Việc kiểm soát tắc nghẽn thông minh theo cơ chế truyền thẳng (intelligent feedforward fouling control) vẫn chưa thể hiện thực hóa do các đặc trưng đầu vào chưa hoàn thiện và thiếu các mô hình dự đoán xu hướng.
    - Trong các nghiên cứu mô hình hóa tiếp theo, cần chú trọng đưa các chỉ số xu hướng (tendency indices) (ví dụ: tiềm năng tắc nghẽn [fouling potential]) làm đầu ra của mô hình, hoặc tích hợp các khái niệm chuỗi thời gian (time series concepts) để dự báo hiệu năng tương lai từ trạng thái vận hành hiện tại.
    - Kết quả dự đoán từ mô hình cần được ghép nối với một hệ thống điều khiển tự động (automatic control system) để chuyển hóa chúng thành ứng dụng thực tiễn.

- **Cấp độ 4: Xây dựng cơ sở dữ liệu mở dùng chung nhằm nâng cao tính giải thích và tính khái quát hóa (data sharing and generalization)**:
  - Một cơ sở dữ liệu chia sẻ rộng rãi (widely shared database) có thể được xây dựng nhằm nâng cao khả năng giải thích (interpretability) và khả năng khái quát hóa (generalizability) của các mô hình:
    - Khả năng giải thích của các mô hình "hộp đen" (black box models) vẫn là một vấn đề tồn tại kéo dài, và sự phức tạp của các quá trình vật lý, hóa học, sinh học trong hệ thống MBR đặt ra những yêu cầu và rào cản mới cho khả năng giải thích của các mô hình dự đoán.
    - Hiện tại, việc ứng dụng các phương pháp giải thích mô hình (model interpretation) và các mô hình học sâu (deep learning models) trong dự đoán MBR vẫn còn ở mức giới hạn.
    - Các phương pháp giải thích mô hình đa dạng, chẳng hạn như phân tích luật quyết định (decision rule analysis), so sánh hệ số tương quan (correlation coefficient comparison), phân tích yếu tố độ nhạy (sensitivity factor analysis), và $\text{SHAP}$, có thể hỗ trợ giải thích mô hình nhưng vẫn chưa được sử dụng đầy đủ.
    - Sự thiếu hụt các đặc trưng đầu vào khiến cho việc giải thích mô hình gắn với bản chất vật lý thực tế càng trở nên khó khăn hơn.
    - Để hỗ trợ một mô hình học sâu bền vững (deep learning model) có đủ đặc trưng đầu vào và khả năng khái quát hóa rộng rãi, một lượng lớn dữ liệu mang tính đại diện (representative data) là yếu tố mang tính quyết định, đòi hỏi khối lượng công việc đáng kể cho việc thu thập và tiền xử lý dữ liệu.
    - Nhằm giải quyết thách thức này, việc xây dựng một cơ sở dữ liệu mở tương tự như $\text{ImageNet}$ mang ý nghĩa to lớn, tạo điều kiện cho các nhà nghiên cứu chia sẻ dữ liệu và phát triển các mô hình dự đoán có độ khái quát hóa tốt hơn cùng phạm vi ứng dụng rộng rãi hơn nhờ tập dữ liệu thực nghiệm hoặc kỹ thuật quy mô lớn và đa dạng.

- **Định hướng tương lai về tích hợp đa chiều và đổi mới kiến trúc mô hình (future trajectory and model innovation)**:
  - Quỹ đạo tương lai của học máy trong MBR bao hàm nhiều chiều không gian:
    - Giám sát các đặc trưng đa chiều (multidimensional features) có tiềm năng trực tuyến.
    - Trích xuất chi tiết phân tử dựa trên quang phổ (spectral-driven molecular details).
    - Tích hợp hệ thống điều khiển thông minh dựa trên các mô hình cảnh báo thời gian thực (real-time warning models).
    - Thiết lập các hệ thống dữ liệu mở và dùng chung.
  - Đổi mới mô hình (model innovation) là một phương hướng đáng chú ý:
    - Các phương pháp trí tuệ nhân tạo tiên tiến (AI methods), chẳng hạn như học tăng cường có thể giải thích (explainable reinforcement learning) (Yu et al., 2023) và các mô hình lớn (large models) dựa trên khung kiến trúc $\text{Transformer}$ hoặc đa phương thức (multimodality) (Vasu et al., 2023), đã chứng minh tiềm năng đáng kể trong một số lĩnh vực, bao gồm viễn thám (remote sensing) (Sun et al., 2023), dự đoán sớm không - thời gian (spatio-temporal early prediction) (Wei et al., 2024), và nhận diện vật thể $3\text{D}$ ($3\text{D}$ object detection) (Li et al., 2024b).
    - Các nhà nghiên cứu cần xem xét các mô hình tiên tiến nhưng tinh gọn (simple models) như $\text{KAN}$ (Kolmogorov-Arnold Network với các hàm kích hoạt có thể học được trên các trọng số thay vì sử dụng các hàm kích hoạt cố định trên các nơ-ron) (Liu et al., 2024), và $\text{xLSTM}$ (extended LSTM với cơ chế cổng hàm mũ [exponential gating] cùng cấu trúc bộ nhớ cải tiến [enhanced memory structures]) (Beck et al., 2024).
    - Việc kết hợp các phương pháp luận tích hợp tri thức vật lý (physics-informed), nhận biết vật lý (physics-aware), hoặc dẫn dắt bởi dữ liệu và tri thức (data-knowledge driven methodologies) cũng có thể cải thiện hiệu năng mô hình và/hoặc khả năng giải thích (Nguyen et al., 2023; Li et al., 2024a; Wang et al., 2024a).
    - Các mô hình và phương pháp mới này vẫn chưa được khai thác nhiều trong lĩnh vực quản lý nước và kỹ thuật xử lý nước thải (water management and wastewater engineering); khuyến nghị các nhà nghiên cứu MBR hướng sự chú ý vào các hướng tiếp cận tiên tiến này.
    - Lĩnh vực xử lý nước có thể hưởng lợi từ sự truyền cảm hứng liên ngành hoặc xuyên ngành (interdisciplinary or cross-disciplinary inspiration) từ các kỹ thuật học máy đã ứng dụng trong vật liệu, sinh học, y học và viễn thám, qua đó nâng cao hiệu quả các phương pháp tiếp cận hiện hữu trong xử lý nước.
    - Việc lập hồ sơ đặc tính của các kiểu dữ liệu (profiling of data types), mục tiêu giải pháp (solution goals), và yêu cầu ứng dụng (application requirements) sẽ tạo điều kiện thuận lợi cho việc lựa chọn và tối ưu hóa mô hình.
    - Khám phá mở rộng về các ứng dụng tiềm năng của các thuật toán tối ưu hóa thông minh (intelligent optimization algorithms, còn gọi là thuật toán metaheuristic), học máy tự động ($\text{AutoML}$ - Automated Machine Learning), và trí tuệ nhân tạo có thể giải thích ($\text{XAI}$ - Explainable Artificial Intelligence) trong các quy trình MBR có thể thúc đẩy sự phát triển của các mô hình hiệu quả phục vụ dự đoán và giải thích quy trình.
