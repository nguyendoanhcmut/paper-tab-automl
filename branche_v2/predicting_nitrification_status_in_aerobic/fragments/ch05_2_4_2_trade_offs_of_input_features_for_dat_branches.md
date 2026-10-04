### 4.2. Trade-offs of input features for data-driven model structure

- Mô hình sử dụng các chỉ số chất lượng nước đầu ra (effluent quality) để đánh giá trạng thái nitrat hóa (nitrification status) đồng thời, thực chất là sử dụng dữ liệu lịch sử để dự đoán các điều kiện vận hành hiện tại.
  - Sự biến động của lưu lượng dòng vào (influent flow variations) ảnh hưởng đến thời gian lưu nước thủy lực (hydraulic retention time - $\text{HRT}$), tạo ra độ trễ thời gian giữa đầu vào và đầu ra (input-output time lags) có thể làm suy giảm độ chính xác của mô hình.
  - Việc tính đến động học dòng vào (inflow dynamics) là yếu tố then chốt, đặc biệt trong điều kiện phát sinh nước xám (greywater generation) có tính biến thiên rất cao (Pinto and Maheshwari, 2015).
  - Công tác thu thập dữ liệu trong tương lai cần giải quyết tính biến thiên của lưu lượng dòng vào nhằm cải thiện kết quả dự đoán, có tiềm năng áp dụng các mô hình phụ đặc thù theo lưu lượng (flow-specific sub-models).
- Lưu lượng cấp khí (air flow rate) được sử dụng làm biến đại diện (proxy) duy nhất cho oxy do xuất hiện các khoảng trống dữ liệu oxy hòa tan (dissolved oxygen - $\text{DO}$) kéo dài.
  - Hiện tượng không đồng nhất nồng độ $\text{DO}$ (DO heterogeneity) quan sát được trong thực tế chịu sự chi phối của động lực học chất lưu (fluid dynamics), hiệu quả truyền oxy không đồng đều (uneven oxygen transfer), gradient hoạt tính vi sinh (microbial activity gradients), và thiết kế bể phản ứng (reactor design) (Gillot and Héduit, 2000).
  - Cần bố trí hệ thống cảm biến $\text{DO}$ phân tán (distributed DO sensors) trong các nghiên cứu mô hình hóa tương lai để bảo đảm độ chính xác.
- Quá trình xây dựng cấu trúc mô hình dựa trên dữ liệu (data-driven model structure) đòi hỏi chiến lược lựa chọn đặc trưng đầu vào (strategic input feature selection) phù hợp.
  - Các đặc trưng đầu vào phải cân bằng giữa tương quan thống kê (statistical correlations) và mức độ phù hợp thực tiễn (practical relevance), do các tập dữ liệu mất cân bằng (imbalanced datasets) có thể làm sai lệch mối quan hệ giữa đầu vào và đầu ra.
  - Cần so sánh có hệ thống giữa các tổ hợp đặc trưng khác nhau, lưu ý rằng việc bổ sung thêm các biến đầu vào không bảo đảm gia tăng độ chính xác bất chấp các tương quan sẵn có (Linardatos et al., 2020; Reynaert et al., 2023).
- Độ ổn định và độ tin cậy của đặc trưng (feature stability and reliability) đóng vai trò quan trọng đối với khả năng vận hành thực tế:
  - Mô hình chỉ dựa trên các đầu vào chất lượng nước thuần túy có nguy cơ gặp sai lệch dài hạn (long-term bias) nếu thiếu quy trình bảo trì cảm biến nghiêm ngặt.
  - Sai số đo lường (measurement errors) và lịch trình hiệu chuẩn lại (recalibration schedules) cần được tích hợp trực tiếp vào thiết kế mô hình bền vững (robust model design).
  - Chi phí đầu tư cảm biến (sensor costs) cần được đưa vào tính toán trong hệ thống giám sát nhằm nâng cao tính ứng dụng thực tế và rút ngắn thời gian thu hồi vốn (payback periods).
