## Abstract

* **Phương pháp tiếp cận dựa trên dữ liệu cho quản lý tài nguyên nước**:
  * Đề xuất khung mô hình hồi quy logistic (logistic regression -- LR) nhằm dự đoán nồng độ nitơ amoni trong dòng thải ($NH_4\text{-}N_{eff}$) và đánh giá tính phù hợp để tái sử dụng nước (water reuse suitability).
  * Đối tượng nghiên cứu là hệ thống bể phản ứng quang sinh học màng ngoài trời (outdoor membrane photobioreactor -- MPBR) quy mô pilot có dung tích $470\text{ L}$ (vận hành tại Valencia, Tây Ban Nha).
  * MPBR đóng vai trò là công đoạn xử lý bậc ba (tertiary treatment) để loại bỏ chất dinh dưỡng từ dòng thải của bể phản ứng sinh học màng kỵ khí (anaerobic membrane bioreactor -- AnMBR).
  * AnMBR đảm nhiệm loại bỏ chất hữu cơ bậc một (primary organic matter removal) từ nước thải sinh hoạt đô thị (municipal wastewater).
* **Đánh giá xác suất tuân thủ quy chuẩn tái sử dụng nước nghiêm ngặt**:
  * Khung mô hình ước tính xác suất tuân thủ quy định tái sử dụng nghiêm ngặt của Ý và Liên minh Châu Âu (EU).
  * Ngưỡng nồng độ nitơ amoni quy định trong nước tái sử dụng là $NH_4\text{-}N_{eff} < 1.6\text{ mg N/L}$ ($1.6\text{ mg N}\cdot\text{L}^{-1}$).
* **Xây dựng mô hình và các biến số đầu vào**:
  * Phát triển $8$ mô hình hồi quy logistic nhị phân (binary LR models) dựa trên tập dữ liệu vận hành ngoài trời liên tục trong $1.5\text{ năm}$ ($230\text{ mẫu}$ đo lường thực nghiệm).
  * Các biến đầu vào được xác định tường minh, bao gồm $4$ thông số vận hành chính cùng các yếu tố môi trường và sinh học:
    * Thông số vận hành: thời gian lưu chất rắn (solids retention time -- $\text{SRT}$), thời gian lưu thủy lực (hydraulic retention time -- $\text{HRT}$), lưu lượng sục khí (aeration flowrate -- $F_{air}$), và tải trọng nitơ (nitrogen loading rate -- $\text{NLR}$).
    * Yếu tố môi trường và sinh học: bức xạ ánh sáng khả dụng (light availability), nhiệt độ (temperature), nồng độ oxy hòa tan (dissolved oxygen -- $\text{DO}$), và các chỉ thị sinh khối vi tảo (microalgal biomass indicators).
  * Ứng dụng các phương pháp phân tích hỗ trợ:
    * Phân tích độ nhạy cục bộ (local sensitivity analysis -- LSA) và độ nhạy toàn cục Sobol để lượng hóa mức độ ảnh hưởng của các biến vận hành đến khả năng tuân thủ.
    * Phân cụm K-means (K-means clustering) để phân nhóm các kịch bản và điều kiện vận hành tối ưu.
* **Chiến lược điều khiển nâng cao và kết quả mô phỏng tính toán (in-silico projections)**:
  * Mô phỏng chiến lược điều khiển nâng cao nhằm tối ưu hóa đồng thời $4$ thông số vận hành ($\text{SRT}$, $\text{HRT}$, $F_{air}$, $\text{NLR}$).
  * Kết quả dự báo tính toán chứng minh ưu thế thực tiễn vượt trội so với các điều kiện vận hành cố định (fixed operating conditions):
    * Nâng cao hiệu quả xử lý amoni: nồng độ $NH_4\text{-}N_{eff}$ giảm từ $12\%$ đến $50\%$ ($12\text{--}50\%$).
    * Giảm nhu cầu cấp khí màng: lưu lượng khí sục $F_{air}$ giảm từ $32\%$ đến $38\%$ ($32\text{--}38\%$).
    * Tiết kiệm điện năng tiêu thụ cho sục khí: giảm từ $25\%$ đến $30\%$ ($25\text{--}30\%$), tương ứng giảm mức tiêu thụ năng lượng từ $0.369\text{ kWh/m}^3$ xuống còn $0.260\text{--}0.277\text{ kWh/m}^3$.
    * Gia tăng sản lượng nước tái sử dụng: tỷ lệ mẫu đạt chuẩn tăng thêm từ $5\%$ đến $67\%$ ($5\text{--}67\%$), sản xuất lên tới $750\text{ L}$ nước tái sử dụng đạt chuẩn trên mỗi $\text{m}^3$ nước thải xử lý ($750\text{ L/m}^3$).
* **Tiềm năng ứng dụng và tích hợp hệ thống**:
  * Khung mô hình cung cấp công cụ hỗ trợ ra quyết định giám sát (supervisory decision-making).
  * Có khả năng tích hợp trực tiếp vào hệ thống giám sát điều khiển và thu thập dữ liệu (SCADA) hiện hữu của các nhà máy xử lý nước.
  * Duy trì cấu trúc phân tích giải tích minh bạch và dễ diễn giải (transparent analytical structure).
