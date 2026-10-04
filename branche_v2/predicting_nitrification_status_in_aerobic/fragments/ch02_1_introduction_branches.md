## 1. Introduction

- Nước xám (greywater) chiếm khoảng $70\%$ tổng lưu lượng nước thải sinh hoạt khu dân cư (residential sewage), với sản lượng dao động từ $20$ đến $220\text{ L}$ trên đầu người mỗi ngày ($20\text{--}220\text{ L/capita/day}$) (Shaikh and Ahammed, 2020).
  - Nước xám được định nghĩa là nước thải sinh hoạt không bao gồm nước thải từ bồn cầu (excluding toilet contributions).
  - Tái sử dụng nước xám tại chỗ (on-site reuse) là chiến lược thiết yếu nhằm bảo tồn tài nguyên nước (water conservation), cải thiện khả năng thích ứng của hệ thống cấp thoát nước đô thị (urban water resilience improvement) và phát triển đô thị bền vững (Liu et al., 2023; Maggiotto, 2022).

- Bể phản ứng sinh học màng (membrane bioreactors - $\text{MBRs}$) đóng vai trò công nghệ chủ đạo cho xử lý nước xám phân tán (decentralized treatment) nhờ diện tích xây dựng nhỏ gọn (compact footprint) và chất lượng nước đầu ra ổn định, đáp ứng tiêu chuẩn tái sử dụng (Gao et al., 2025).
  - Hệ thống $\text{MBR}$ kết hợp hiệp đồng giữa các quá trình sinh học—bao gồm quá trình oxy hóa dị dưỡng (heterotrophic oxidation) và quá trình nitrat hóa tự dưỡng (autotrophic nitrification)—với quá trình lọc màng (membrane filtration) để phân tách hiệu quả pha rắn (Boleydei and Vaneeckhaute, 2024).

- Quá trình nitrat hóa (nitrification) chuyển hóa ammonium ($\text{NH}_4^+\text{--N}$) thành nitrite ($\text{NO}_2^-\text{--N}$) và sau đó thành nitrate ($\text{NO}_3^-\text{--N}$), là mắt xích thiết yếu trong $\text{MBRs}$ nhằm đáp ứng các quy chuẩn tái sử dụng nước.
  - Các nhà máy xử lý tập trung (centralized plants) thường áp dụng chiến lược điều khiển vi tích phân tỷ lệ (proportional integral differential - $\text{PID}$) để duy trì điểm đặt oxy hòa tan (dissolved oxygen - $\text{DO}$) cố định (fixed setpoints).
  - Chiến lược $\text{PID}$ điểm đặt cố định thích ứng kém với dao động tải lượng dòng vào (influent fluctuations) và gây tổn hao chi phí năng lượng lớn (Gu et al., 2023).
  - Các hệ thống xử lý nước xám tại chỗ đối mặt với biên độ biến động tải lượng khuếch đại (amplified load variability):
    - Chu kỳ sử dụng theo ngày và theo mùa (daily/seasonal usage patterns) tạo ra các khoảng thời gian tải lượng thấp kéo dài xen kẽ các đỉnh tải nhọn đột biến (sharp peaks).
    - Đặc tính chất lượng nước biến động liên tục làm mất hiệu lực các tham số điều khiển kinh nghiệm (empirical control parameters) (DelaPaz-Ruíz et al., 2024; Hassan et al., 2024).
  - Dù thuật toán $\text{PID}$ có thể điều chỉnh van sục khí (aeration valves), các mục tiêu $\text{DO}$ tĩnh không đáp ứng kịp thời theo thời gian thực trước biến động tải lượng $\text{NH}_4^+\text{--N}$ (thiếu sự điều chỉnh động phụ thuộc tải $\text{NH}_4^+\text{--N}$) (Li et al., 2022; Shi et al., 2024).
  - Hệ thống $\text{PID}$ phụ thuộc vào các đầu dò $\text{DO}$ ngập trong bể (submerged $\text{DO}$ probes):
    - Đầu dò ngập nước trong $\text{MBRs}$ quy mô nhỏ dễ bị bám bẩn (fouling) và trôi dạt tín hiệu (drift) do sục khí liên tục và tích tụ bùn vi sinh.
    - Sự cố đầu dò làm suy giảm độ tin cậy của phép đo, dễ bị nhầm lẫn giữa hỏng hóc cảm biến và biến động tải lượng thực tế.

- Giám sát đáng tin cậy quá trình nitrat hóa là rào cản kỹ thuật lớn đối với $\text{MBRs}$ phân tán do hiệu quả xử lý dao động tiềm ẩn nguy cơ mất ổn định hệ thống ngay cả khi chất lượng nước sau xử lý vẫn đạt chuẩn (được ghi nhận trong thử nghiệm nghiên cứu).
  - Việc giám sát theo thời gian thực quá trình nitrat hóa nội tại bên trong $\text{MBRs}$—đặc biệt ở các kịch bản vận hành phân tán—chưa từng được giải quyết trong các công bố khoa học trước đó.
  - Các cảm biến thương mại đo trực tiếp $\text{NH}_4^+\text{--N}$, $\text{NO}_2^-\text{--N}$ và $\text{NO}_3^-\text{--N}$ không khả thi khi lắp đặt trong bể phản ứng:
    - Nồng độ bùn sinh học cao gây tắc bẩn nhanh, tăng gánh nặng bảo trì định kỳ và đội chi phí vận hành (Huang et al., 2024).
    - Hợp chất hữu cơ (organic matter), chất rắn lơ lửng (suspended solids) và nhiễu ion (ionic interference) làm sai lệch kết quả đo.
    - Độ trễ đáp ứng (response lags) của cảm biến không theo kịp động học phản ứng nitrat hóa diễn ra nhanh, cản trở điều khiển thời gian thực.

- Học máy (machine learning - $\text{ML}$) mở ra hướng tiếp cận dựa trên dữ liệu (data-driven solutions) cho phép giám sát quá trình nitrat hóa trong $\text{MBRs}$ thông qua các thông số chất lượng nước đầu ra (effluent water quality parameters) mà không cần sử dụng các đầu dò xâm lấn trong bể phản ứng (Van de Walle et al., 2023).
  - Phương pháp $\text{ML}$ cho phép giám sát nhanh, chi phí thấp, theo thời gian thực—tạo điều kiện can thiệp quy trình kịp thời và tăng cường độ an toàn vận hành (Bahramian et al., 2023).
  - So với các mô hình cơ chế (mechanistic models), $\text{ML}$ yêu cầu ít biến đầu vào hơn và giảm thiểu yêu cầu bảo trì, thích hợp với các trạm xử lý tại chỗ (Duarte et al., 2024).
  - Xử lý nước xám phục vụ tái sử dụng đòi hỏi sự chấp thuận khắt khe từ cơ quan quản lý và sự tin cậy của cộng đồng:
    - Các mô hình $\text{ML}$ có khả năng giải thích (interpretable $\text{ML}$) cung cấp cơ sở dự đoán minh bạch cho quyết định can thiệp của người vận hành và quá trình hiệu chỉnh mô hình (Allen et al., 2024).
    - Tính diễn giải giúp làm rõ các hạn chế trong chiến lược huấn luyện hiện hành và định hướng nâng cấp kiến trúc mô hình.

- Các nghiên cứu dự đoán dựa trên dữ liệu trước đây trong xử lý nước thải bằng $\text{MBR}$ tập trung vào chất lượng nước thải đầu ra, hiệu suất loại bỏ chất ô nhiễm mục tiêu và tắc nghẽn màng (membrane fouling) (Muniz de Queiroz et al., 2025; Shi et al., 2022; Zhong et al., 2022).
  - Việc phụ thuộc thuần túy vào giám sát chất lượng dòng thải đầu ra bộc lộ nhiều hạn chế vận hành:
    - Khả năng kiểm soát quy trình bị hạn chế, không cho phép can thiệp kịp thời khi phát sinh các sự cố vận hành bất thường.
    - Phương pháp đo dòng thải đòi hỏi nhiều nhân công (labor-intensive) và tiêu tốn thời gian (time-consuming).
    - Không có khả năng truy xuất các khiếm khuyết vận hành tiềm ẩn trước khi xảy ra vi phạm tiêu chuẩn xả thải (Moretti et al., 2024).
  - Ngược lại, giám sát quy trình theo thời gian thực (real-time process monitoring) tạo tiền đề cho điều khiển chủ động (proactive control), củng cố khả năng phục hồi của hệ thống (system resilience) và phát hiện sự cố sớm—yếu tố quyết định để duy trì chất lượng nước đồng nhất cho nhiều mục đích tái sử dụng.

- Nghiên cứu này hướng đến xây dựng mô hình $\text{ML}$ có khả năng giải thích nhằm giám sát quá trình nitrat hóa trong $\text{MBRs}$ dựa trên các thông số dòng ra, giảm thiểu độ phức tạp trong việc thu thập đặc trưng đầu vào thực tế.
  - Các đặc trưng đầu vào được sàng lọc theo ba tiêu chí: khả năng đo đạc trực tiếp (direct measurability), tính tương thích với cảm biến (sensor compatibility), và ý nghĩa vận hành (operational relevance).
  - Ba thuật toán có khả năng giải thích được đánh giá nhằm giảm thiểu nguy cơ quá khớp (overfitting) và cân bằng độ chệch - phương sai (bias-variance tradeoffs):
    - Hồi quy logistic (logistic regression - $\text{LR}$).
    - Rừng ngẫu nhiên (random forest - $\text{RF}$).
    - Extreme gradient boosting ($\text{XGB}$).
  - Chiến lược huấn luyện mô hình đặt ưu tiên vào độ ổn định vận hành thông qua việc tối đa hóa độ chính xác ($\text{precision}$), dựa trên tỷ lệ dương tính thật ($\text{TPR}$ / true positive rate) cao và tỷ lệ dương tính giả ($\text{FPR}$ / false positive rate) thấp, sử dụng dữ liệu từ hệ thống $\text{MBR}$ bùn lơ lửng (suspended-sludge $\text{MBR}$).
  - Phân tích $\text{SHAP}$ (SHapley Additive exPlanations), đánh giá độ quan trọng của đặc trưng (feature importance) và các phân tích cặp (pairwise assessments) được thực hiện nhằm làm rõ mối liên kết giữa các nhân tố với kết quả dự đoán, định hướng cải thiện mô hình.
  - Mô hình được kiểm chứng mở rộng trên hệ thống lai (hybrid system) tích hợp bùn lơ lửng với giá thể sinh học polyvinylidene fluoride ($\text{PVDF}$ biocarriers) thực hiện đồng thời quá trình nitrat hóa - khử nitrat (simultaneous nitrification-denitrification - $\text{SND}$), chứng minh khả năng áp dụng dự đoán xuyên kịch bản.
  - Một chiến lược điều khiển sục khí tự động (automated aeration control strategy) được đề xuất nhằm hiện thực hóa khung giám sát vào thực tiễn vận hành.
