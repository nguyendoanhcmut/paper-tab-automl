## Abstract

- **Thách thức vận hành trong xử lý nước thải sản xuất bán dẫn**: Các hệ thống bể phản ứng sinh học màng quy mô thực tế (full-scale membrane bioreactors - MBR) xử lý nước thải sản xuất chất bán dẫn (semiconductor wastewater) vận hành dưới các điều kiện đặc thù mà các nghiên cứu quy mô phòng thí nghiệm (laboratory studies) hiếm khi tái tạo được:
  - Tải lượng hữu cơ và ion biến động (fluctuating organic and ionic loads) gắn liền với kế hoạch sản xuất.
  - Sự hiện diện của các dung môi đặc thù (specialty solvents) và tác nhân tạo phức (chelating agents) phát sinh từ các công đoạn bóc tách chất cản quang (photoresist stripping) và đánh bóng cơ hóa (CMP - chemical mechanical planarization).
  - Tuổi bùn kéo dài (extended sludge ages), nằm ngoài phạm vi các chế độ thời gian lưu bùn ngắn (short-SRT regimes) vốn là cơ sở của hầu hết các lý thuyết tắc nghẽn màng (fouling theory).
  - Người vận hành phải đồng thời kiểm soát áp suất xuyên màng ($TMP$ - transmembrane pressure), thông lượng nước sau lọc ($permeate\ throughput$) và cân bằng thủy lực ($hydraulic\ balance$), trong khi chưa có khung làm việc dựa trên dữ liệu ($data-driven\ framework$) nào xác định được các tổ hợp vận hành đạt được mục tiêu này một cách đáng tin cậy.

- **Khung học máy có thể giải thích để xác định lưu vực vận hành**: Khung học máy có thể giải thích được ($interpretable\ machine-learning\ framework$) được phát triển dựa trên $4593$ bản ghi SCADA theo giờ ($hourly\ SCADA\ records$) từ một hệ thống MBR công nghiệp công suất $1125\ \text{m}^3/\text{h}$ nhằm xác định lưu vực vận hành ($operational\ basin$):
  - Đánh giá đối chuẩn (benchmarked) $16$ thuật toán thuộc $6$ nhóm mô hình (families) cho $3$ biến mục tiêu: áp suất xuyên màng ($TMP$), lưu lượng nước sau lọc ($permeate\ flow$) và mức bể màng ($membrane-tank\ level$).

- **Hiệu năng và độ ổn định của mô hình Extra Trees**: Thuật toán Extra Trees đạt độ chính xác cao nhất cho tất cả các biến mục tiêu, với hệ số xác định lần lượt là $R^2 = 0.988$ (cho $TMP$), $R^2 = 0.933$ (cho $permeate\ flow$) và $R^2 = 0.908$ (cho $membrane-tank\ level$):
  - Duy trì vị trí thứ nhất (first rank) dưới các phương pháp kiểm định phân khối (blocked validation), kiểm định theo trình tự thời gian (chronological validation) và kiểm định chéo giữa các đơn nguyên (cross-train validation), bao gồm cả một chuỗi đơn nguyên vận hành song song độc lập (independent parallel train).
  - Khi được tái huấn luyện hàng ngày (refit daily), mô hình duy trì $R^2 = 0.871$ cho biến $TMP$ xuyên suốt giai đoạn kiểm tra ngoài khung thời gian (out-of-time period) kéo dài $4$ tháng.

- **Cơ chế tắc nghẽn màng qua phân tích khả năng giải thích SHAP**: Phân tích SHAP ($SHAP\ analysis$) xác định thời gian lưu bùn ($SRT$ - sludge retention time) là biến thúc đẩy chủ đạo ($dominant\ driver$):
  - Hiện tượng tắc nghẽn màng ($fouling$) gia tăng độ nghiêm trọng một cách đơn điệu ($worsening\ monotonically$) trên toàn bộ dải sục khí kéo dài ($extended-aeration\ range$) của nhà máy.

- **Bản đồ hóa tính khả thi vận hành và nâng cao tỷ lệ đạt mục tiêu**: Kỹ thuật lập bản đồ tính khả thi ($feasibility\ mapping$) bằng phương pháp tái lấy mẫu hiệp phương sai cục bộ ($local-covariance\ resampling$) được ràng buộc trên đa tạp vận hành đạt được ($attainable\ operating\ manifold$) của nhà máy xác định được $207,238$ trạng thái khả thi trong tổng số $500,000$ trạng thái được lấy mẫu:
  - Tính khả thi xác định từ mô hình bám sát độ đạt mục tiêu đo đạc thực tế qua $70$ phân nhóm (bins) với hệ số tương quan $r = 0.99$.
  - Vận hành bên trong các dải khuyến nghị (recommended bands) đáp ứng đồng thời cả $3$ mục tiêu trong $61\text{–}82\%$ thời gian vận hành, so với mức cơ sở chỉ đạt $37\%$ ($37\%\ \text{baseline}$).
  - Cửa sổ vận hành trích xuất từ $7$ tháng đầu tiên nâng tỷ lệ đạt mục tiêu lên $61.9\%$ trong $3$ tháng cuối cùng, tương ứng với tỷ số chênh ($odds\ ratio$) đạt $3.89$.

- **Giao thức kiểm soát thực thi và khả năng chuyển giao**: Khung làm việc thiết lập một giao thức điều khiển có tính thực thi ($actionable\ control\ protocol$) với các khoảng thông số vận hành khuyến nghị:
  - Thời gian lưu bùn ($SRT$): $43.2\text{–}72.2\ \text{ngày}$ ($43.2\text{–}72.2\ \text{days}$).
  - Thời gian lưu thủy lực ($HRT$): $5.9\text{–}6.4\ \text{h}$.
  - Nồng độ chất rắn lơ lửng trong bùn lỏng ($MLSS$): $5580\text{–}6138\ \text{mg/L}$.
  - Tỷ lệ thức ăn trên vi sinh vật ($F/M$): $0.023\text{–}0.025\ \text{day}^{-1}$.
  - Lưu lượng sục khí ($aeration$): $4868\text{–}5892\ \text{m}^3/\text{h}$.
  - Khung làm việc có khả năng chuyển giao ($transferable$) cho các hệ thống MBR công nghiệp khác thông qua việc tái huấn luyện đặc thù theo từng địa điểm ($site-specific\ retraining$).
