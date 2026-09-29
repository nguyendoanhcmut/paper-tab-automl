## Chương 6: Khung Kiến trúc Bản sao Số cho Hệ thống MBR

### 6.1 Kiến trúc, Các thành phần và Các bậc trưởng thành công nghệ của Bản sao Số

#### 6.1.1 Khái niệm nền tảng và Đặc trưng cốt lõi của Bản sao Số
- Khái niệm khởi nguồn:
  - Khái niệm Digital Twin (DT) do Grieves đưa ra lần đầu trong sản xuất công nghiệp [30].
  - Công nghệ này mở rộng sang hàng không vũ trụ, hạ tầng năng lượng và sản xuất thông minh [32].
- Ba thành phần cốt lõi của Digital Twin công nghiệp theo Fuller và cộng sự [31]:
  - Thực thể vật lý (Physical entity): Trang bị hệ thống cảm biến và cơ cấu chấp hành.
  - Thực thể ảo (Virtual entity): Mô phỏng thực thể vật lý trên các thang thời gian tương ứng.
  - Lớp kết nối dữ liệu (Data connection layer): Đồng bộ hóa trạng thái liên tục hai chiều giữa miền vật lý và miền ảo.
- Đặc trưng mô hình ảo đa độ trung thực (Multi-fidelity virtual entity) [33]:
  - Mô hình ảo kết hợp mô hình cơ chế vật lý có độ chính xác cao cho biến đổi chậm.
  - Mô hình ảo tích hợp mô hình học máy dữ liệu (ML) có tốc độ xử lý nhanh cho biến động vận hành.
  - Sự kết hợp này đảm bảo tính khả thi tính toán thời gian thực và độ chính xác dự báo.
- Mục tiêu giá trị gia tăng trong hệ thống MBR theo Wang và cộng sự:
  - Tác giả xác định quản lý tắc nghẽn màng MBR và tối ưu hóa sục khí là hai mục tiêu giá trị cao nhất.
  - Hệ thống giúp tiết kiệm năng lượng toàn trạm và nâng cao chất lượng nước sau xử lý.
  - Hệ thống tối ưu hóa đồng thời quá trình sinh học, quá trình lọc màng và định lượng hóa chất.

#### 6.1.2 Bốn lớp kiến trúc kỹ thuật của Bản sao Số MBR
- Lớp 1 - Lớp thực thể vật lý và cảm biến đo lường (Physical & Sensing Layer):
  - Mạng SCADA hiện hữu của trạm xử lý MBR.
  - Cảm biến trực tuyến thu nhận dữ liệu gồm oxy hòa tan ($DO$), độ đục, áp suất chuyển màng ($TMP$), lưu lượng thấm ($J$), nhiệt độ ($T$), lưu lượng khí sục ($Q_{air}$).
  - Cơ cấu chấp hành vật lý gồm máy thổi khí, bơm hút màng và các van điều tiết.
- Lớp 2 - Lớp truyền thông và tiền xử lý dữ liệu (Communication & Preprocessing Layer):
  - Đường ống dữ liệu thời gian thực truyền dữ liệu lên nền tảng đám mây hoặc máy chủ biên (Edge computing) [37, 61].
  - Mạng SCADA truyền dữ liệu cảm biến thô định kỳ mỗi $1\text{ phút}$ về cơ sở dữ liệu chuỗi thời gian.
  - Hệ thống tự động kiểm tra chất lượng dữ liệu, loại bỏ giá trị bất thường và điền khuyết thiếu bằng nội suy.
- Lớp 3 - Lớp lõi mô hình hóa thứ bậc (Hierarchical Modeling Layer):
  - Phân mô hình cơ chế sinh học: Ứng dụng mô hình bùn hoạt tính ASM1 hoặc ASM2d để mô phỏng động học sinh học [34, 35].
  - Phân mô hình cơ chế màng: Ứng dụng mô hình trở lực nối tiếp (Resistance-in-series) để phân tích cơ chế tắc nghẽn [36].
  - Phân mô hình học máy: Ứng dụng mô hình Random Forest hoặc LSTM để dự báo động thái TMP [22, 26].
  - Phân mô hình chất lượng nước: Ứng dụng mô hình Gradient Boosting để dự báo nồng độ ô nhiễm nước đầu ra.
  - Mô-đun giải thích tính năng: Ứng dụng thuật toán SHAP để tính toán mức độ đóng góp thuộc tính thời gian thực [53].
  - Phân mô hình cân bằng năng lượng: Mô phỏng tiêu thụ điện năng của hệ thống sục khí và bơm [14, 56].
- Lớp 4 - Lớp giao diện vận hành và điều khiển chấp hành (Interface & Actuation Control Layer):
  - Bảng điều khiển giao diện người vận hành (Operator Dashboard) hiển thị trực quan dự báo và giải thích SHAP.
  - Hệ thống cung cấp cơ chế phê duyệt hoặc ghi đè quyết định từ nhân viên vận hành (Human-in-the-loop).
  - Vòng điều khiển gửi tín hiệu cài đặt ngược về SCADA để điều chỉnh van thổi khí, bơm màng hoặc chu trình rửa màng CIP.

#### 6.1.3 Ba bậc trưởng thành công nghệ (Maturity Tiers) và Hiện trạng triển khai
- Bậc I - Bản sao số mô tả (Tier I: Descriptive DT):
  - Năng lực: Giám sát trạng thái trạm theo thời gian thực, bảng điều khiển cảm biến, quản lý cảnh báo ngưỡng vượt, phân tích xu hướng lịch sử.
  - Yêu cầu dữ liệu: Dữ liệu mạng SCADA và các cảm biến đo trực tuyến.
  - Độ phức tạp triển khai: Thấp (Low).
  - Hiện trạng ứng dụng MBR: Đã thương mại hóa và ứng dụng phổ biến tại nhiều nhà máy MBR quy mô thực tế [5, 15].
  - Minh chứng kỹ thuật: Rodríguez-Alonso và cộng sự triển khai nền tảng vi dịch vụ trên kiến trúc điện toán biên cho toàn bộ trạm xử lý [61].
- Bậc II - Bản sao số dự đoán (Tier II: Predictive DT):
  - Năng lực: Dự báo trước $12 - 72\text{ h}$ quỹ đạo áp suất TMP, suy giảm lưu lượng thấm, chất lượng nước đầu ra và nhu cầu điện năng.
  - Chuyển đổi vận hành: Giúp người vận hành đưa ra quyết định chủ động thay vì phản ứng thụ động sau sự cố.
  - Yêu cầu dữ liệu: Dữ liệu SCADA kết hợp số liệu phân tích phòng thí nghiệm và mô hình ML đã huấn luyện.
  - Độ phức tạp triển khai: Trung bình (Medium).
  - Hiện trạng ứng dụng MBR: Đã xác thực trên mô phỏng BSM-MBR [24, 36] và kiểm chứng độc lập trên dữ liệu SCADA quy mô thực tế (Kovacs et al., 2022 [26]). Trạm thực tế chưa đưa vào vận hành cố vấn vòng kín liên tục.
- Bậc III - Bản sao số kê đơn và Tự trị (Tier III: Prescriptive DT):
  - Năng lực: Tối ưu hóa đa mục tiêu vòng kín tự trị (Closed-loop autonomous optimization), kiểm thử kịch bản giả định (What-if scenario testing), giải trình quyết định điều khiển bằng XAI.
  - Hành động thực thi: Tự động điều chỉnh điểm đặt sục khí ($DO$, $Q_{air}$), điều khiển lưu lượng thấm ($J$) và tự động lập lịch làm sạch màng CIP.
  - Cơ chế an toàn: Mô phỏng vòng kín đánh giá trước hệ quả điều khiển trước khi tác động lên hệ thống vật lý.
  - Yêu cầu dữ liệu: Bản sao số toàn diện kết hợp cơ cấu chấp hành tự động, mô-đun XAI và lớp thẩm định an toàn.
  - Độ phức tạp triển khai: Cao (High).
  - Hiện trạng ứng dụng MBR: Đang ở giai đoạn đề xuất kiến trúc lý thuyết. Chưa có công bố nào triển khai Bậc III kèm XAI trên trạm MBR quy mô thực tế tính đến tháng 12 năm 2025 [33, 37].
- Xu hướng công bố khoa học trong ngành nước:
  - Khảo sát 147 nghiên cứu từ năm 2015 đến tháng 5 năm 2025 cho thấy số lượng bài báo Digital Twin tăng từ 1 bài (năm 2015) lên 41 bài (năm 2024) [60].
  - Trong 147 nghiên cứu trên có 41 nghiên cứu tập trung vào xử lý nước thải.
  - Công nghệ đang chuyển biến rõ rệt từ nghiên cứu ý niệm sang các khung kiến trúc triển khai có cấu trúc.

### 6.2 Tích hợp XAI vào Kiến trúc Ra quyết định của Bản sao Số

#### 6.2.1 Vai trò then chốt của XAI trong hệ thống Bản sao Số
- Cầu nối minh bạch và hỗ trợ ra quyết định:
  - XAI tạo thành lớp trung gian minh bạch giữa công cụ dự báo ML và quyết định điều khiển downstream [62, 63].
  - XAI cung cấp định dạng trực quan dễ hiểu gồm biểu đồ thác nước SHAP (SHAP waterfall chart), biểu đồ thanh xếp hạng thuộc tính cục bộ (Ranked bar plot) hoặc tóm tắt văn bản [64].
  - Người vận hành đánh giá tính hợp lý của dự báo dựa trên hiện trạng công nghệ trước khi thực thi lệnh [64].
- Ba chức năng vận hành cốt lõi của XAI trong kiến trúc Digital Twin:
  - Tạo nhật ký kiểm toán gần thời gian thực (Near-real-time audit trail):
    - Hệ thống lưu lại bối cảnh giải thích đi kèm từng khuyến nghị điều khiển của mô hình.
    - Chức năng này nâng cao tính truy xuất nguồn gốc, trách nhiệm giải trình và phục vụ rà soát hậu kiểm trong các đợt kiểm tra quy định [65].
  - Hỗ trợ người vận hành ghi đè có căn cứ khoa học (Informed operator override):
    - Người vận hành không tiếp nhận hoặc bác bỏ mù quáng khuyến nghị của mô hình ML.
    - Giá trị SHAP chỉ rõ biến quy trình nào đang thúc đẩy dự báo áp suất TMP hoặc chất lượng nước.
    - Người vận hành phân biệt chính xác giữa biến động công nghệ thực tế và tín hiệu giả tạo do lỗi cảm biến đo (Measurement artefact) [17, 66].
  - Cảnh báo sớm hiện tượng trôi dạt khái niệm (Concept drift warning):
    - Sự dịch chuyển bất thường trong phân phối xếp hạng SHAP báo hiệu trôi dạt dữ liệu hoặc trạng thái vận hành nằm ngoài vùng học của mô hình [48, 67].
    - Tín hiệu này kích hoạt người vận hành kiểm tra thủ công trước khi hệ thống tiếp tục điều khiển tự động.
- Yêu cầu chức năng bắt buộc để xây dựng niềm tin:
  - Tao và cộng sự [32] cùng Barricelli và cộng sự [33] xác định khả năng giải thích là yêu cầu thiết kế bắt buộc cho Digital Twin công nghiệp đáng tin cậy.
  - Nhân viên vận hành thường ghi đè và từ chối các khuyến nghị khó hiểu khi gặp điều kiện vận hành mới, làm triệt tiêu giá trị của bản sao số.
  - XAI là điều kiện chức năng tiên quyết để xây dựng niềm tin cho việc chuyển đổi từ Bậc II (Dự đoán) sang Bậc III (Kê đơn tự trị) [37].

#### 6.2.2 Quy trình làm việc 5 giai đoạn tích hợp XAI (Hình 3 / Luồng quyết định)
- Giai đoạn 1 - Thu thập và tiền xử lý luồng dữ liệu SCADA thời gian thực:
  - Thu nhận luồng dữ liệu cảm biến thô từ trạm vật lý qua mạng SCADA theo chu kỳ $1\text{ phút}$.
  - Các thông số gồm $DO$, $TMP$, lưu lượng thấm $J$, độ đục, nhiệt độ và lưu lượng khí sục màng $Q_{air}$.
  - Dữ liệu được kiểm tra chất lượng, xử lý ngoại lai, nội suy điền giá trị khuyết thiếu và lưu trữ vào cơ sở dữ liệu chuỗi thời gian.
- Giai đoạn 2 - Dự báo trạng thái hệ thống bằng động cơ ML:
  - Động cơ ML tiếp nhận dữ liệu cảm biến thời gian thực và chuỗi dữ liệu lịch sử gần nhất.
  - Mô hình Random Forest hoặc LSTM dự báo quỹ đạo TMP trước $12 - 72\text{ h}$.
  - Mô hình Gradient Boosting ước tính nồng độ các chất ô nhiễm trong dòng nước đầu ra.
- Giai đoạn 3 - Tính toán giá trị giải thích thuộc tính bằng mô-đun SHAP:
  - Mô-đun SHAP tính toán giá trị đóng góp của từng biến số cho từng dự báo theo thời gian thực.
  - Hệ thống xuất biểu đồ đóng góp có xếp hạng thứ tự, xác định rõ mức độ và chiều hướng tác động của từng thông số vận hành lên kết quả dự báo.
- Giai đoạn 4 - Hiển thị trực quan trên bảng điều khiển giao diện người vận hành:
  - Bảng điều khiển hiển thị đồng thời giá trị dự báo và biểu đồ giải thích SHAP tương ứng.
  - Người vận hành xem xét, đánh giá cơ sở kỹ thuật và phê duyệt khuyến nghị trước khi kích hoạt hành động điều khiển.
- Giai đoạn 5 - Thực thi điều khiển và lưu vết nhật ký kiểm toán tự động:
  - Lệnh điều khiển được chuyển đến lớp chấp hành để điều chỉnh điểm đặt sục khí, lưu lượng bơm hút hoặc chu trình rửa màng CIP.
  - Hệ thống tự động ghi giá trị dự báo kèm toàn bộ giá trị giải thích SHAP vào nhật ký kiểm toán nhằm phục vụ thanh tra quy định và rà soát kỹ thuật sau vận hành.
  - Kiến trúc này đảm bảo XAI gắn liền vào cấu trúc ra quyết định, không phải mô-đun gắn thêm tùy chọn.

#### 6.2.3 Bảng so sánh các bậc trưởng thành và Bản đồ nhiệt mức độ trưởng thành nghiên cứu (Bảng 5 và Hình 3)
- Bảng tổng hợp các bậc trưởng thành Digital Twin trong hệ thống MBR (Bảng 5 trong bài báo):
  - Bậc I (Mô tả - Descriptive):
    - Năng lực vận hành: Giám sát thời gian thực, bảng điều khiển trực quan, quản lý hệ thống cảnh báo.
    - Yêu cầu dữ liệu: Dữ liệu mạng SCADA và các cảm biến đo trực tuyến.
    - Độ phức tạp kỹ thuật: Thấp (Low).
    - Trạng thái nghiên cứu: Đã triển khai thương mại rộng rãi trên quy mô thực tế [5, 15].
  - Bậc II (Dự đoán - Predictive):
    - Năng lực vận hành: Dự báo TMP, dự đoán chất lượng nước đầu ra, phát hiện sự cố trước $12 - 72\text{ h}$.
    - Yêu cầu dữ liệu: SCADA kết hợp số liệu phân tích phòng thí nghiệm và mô hình ML đã huấn luyện.
    - Độ phức tạp kỹ thuật: Trung bình (Medium).
    - Trạng thái nghiên cứu: Đã xác thực trên mô phỏng và dữ liệu trạm quy mô đầy đủ [24, 26, 36].
  - Bậc III (Kê đơn và Tự trị - Prescriptive):
    - Năng lực vận hành: Tối ưu hóa tự trị vòng kín, thử nghiệm kịch bản giả định (What-if), giải trình quyết định bằng XAI.
    - Yêu cầu dữ liệu: Bản sao số đầy đủ kết hợp cơ cấu chấp hành, mô-đun XAI và lớp thẩm định an toàn.
    - Độ phức tạp kỹ thuật: Cao (High).
    - Trạng thái nghiên cứu: Chưa có công bố triển khai trên trạm MBR quy mô thực tế trong tài liệu bình duyệt [33, 37].
- Phân tích bản đồ nhiệt mức độ trưởng thành nghiên cứu (Research Maturity Heat Map - Hình 3):
  - Ba tiêu chí đánh giá mức độ trưởng thành:
    - Khối lượng bằng chứng từ các tài liệu được bình duyệt đồng nghiệp (Peer-reviewed evidence volume).
    - Mức độ sẵn có của các kiểm chứng vận hành trên quy mô thực tế (Full-scale operational validation).
    - Mức độ triển khai thực tế tại các cơ sở xử lý nước đang hoạt động (Documented deployment in commissioned facilities).
  - Bốn cấp độ đánh giá định tính:
    - Cao (High): Cơ sở bằng chứng vững chắc, nhiều nghiên cứu độc lập cho kết quả nhất quán.
    - Vừa (Moderate): Cơ sở bằng chứng đang phát triển, có một số kiểm chứng trên pilot hoặc quy mô thực tế.
    - Mới xuất hiện (Emerging): Lĩnh vực được công nhận, bằng chứng mới dừng ở đề xuất khái niệm, mô phỏng hoặc thử nghiệm phòng thí nghiệm.
    - Thấp (Low): Không tìm thấy bằng chứng bình duyệt trong các đợt tìm kiếm có cấu trúc.
  - Ba quy luật chính rút ra từ bản đồ nhiệt Hình 3:
    - Quy luật 1 - Dự báo tắc nghẽn màng (Fouling prediction): Đạt mức Cao (High) về cơ sở bằng chứng và năng lực dự báo mô hình. Mức độ tích hợp khả năng giải thích XAI, kiểm chứng quy mô đầy đủ và mức độ sẵn sàng triển khai đều ở mức Mới xuất hiện (Emerging). Năng lực dự báo bằng ML đang phát triển vượt xa khả năng triển khai thực tế.
    - Quy luật 2 - Diễn giải hỗ trợ bởi XAI (XAI-supported interpretation): Đạt mức Cao (High) về tích hợp khả năng giải thích. Tuy nhiên kiểm chứng quy mô đầy đủ ở mức Thấp (Low) và mức độ sẵn sàng triển khai ở mức Mới xuất hiện (Emerging). Ứng dụng XAI trong hệ thống MBR hiện nay phần lớn vẫn là nghiên cứu học thuật.
    - Quy luật 3 - Triển khai Bản sao số (Digital Twin deployment): Thể hiện mức độ trưởng thành thấp nhất trong các lĩnh vực, đạt xếp hạng Mới xuất hiện (Emerging) hoặc Thấp (Low) trên toàn bộ 5 khía cạnh. Chưa có trạm MBR quy mô thực tế nào vận hành bản sao số được công bố trong tài liệu bình duyệt.
  - Ý nghĩa định hướng nghiên cứu: Các ô có mức độ trưởng thành thấp liên kết trực tiếp với 9 khoảng trống nghiên cứu được phân tích trong Chương 7, tạo lộ trình ưu tiên cho các nghiên cứu tiếp theo.
