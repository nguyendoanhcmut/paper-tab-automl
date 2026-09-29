## Chương 5: Ứng dụng kỹ thuật thực tiễn, Giới hạn nghiên cứu và Định hướng tương lai

### 5.1 Khuyến nghị kỹ thuật vận hành trạm xử lý nước thải dòng chính ứng dụng Anammox
#### 5.1.1 Đánh giá cấu hình công nghệ và đặc tính nguồn nước nạp
- Lựa chọn cấu hình bể phản ứng và dạng hình thái sinh khối:
  - Bể phản ứng dòng chảy liên tục (continuous flow reactor) vận hành với bùn hạt vi sinh vật (microbial aggregates) là giải pháp tối ưu nhất.
  - Cấu trúc bùn hạt Anammox duy trì mật độ sinh khối cao hơn cấu trúc bùn bông (floc).
  - Cấu hình này giúp hệ thống tiếp nhận và xử lý tải trọng ô nhiễm nitơ cao trong điều kiện dòng chảy biến động.
- Khoảng cách giữa thực nghiệm nước thải nhân tạo và nước thải đô thị:
  - Phần lớn nghiên cứu phòng thí nghiệm sử dụng nước thải nhân tạo với thành phần hóa lý đơn giản.
  - Nước thải đô thị thực tế có thành phần cơ chất phức tạp và nồng độ chất ô nhiễm dao động liên tục.
  - Sự khác biệt lớn này làm suy giảm ý nghĩa thực tế của các mô hình huấn luyện từ dữ liệu nước thải nhân tạo.
  - Kỹ sư vận hành cần hiệu chuẩn lại mô hình dự báo và thông số điều khiển dựa trên đặc tính nước thải thực tế tại hiện trường.
#### 5.1.2 Chiến lược kiểm soát theo phân loại quy trình Anammox (PNA so với PDA)
- Quy trình Nitrit hóa một phần kết hợp Anammox (PNA):
  - Quy trình PNA và quy trình PNA kết hợp PDA đạt hiệu suất khử TIN cao hơn quy trình PDA đơn lẻ.
  - Nồng độ nitơ dòng vào và dòng ra trong quy trình PNA có tương quan thuận rất mạnh, với hệ số tương quan đạt từ 0.55 đến 0.95.
  - Mức tương quan cao này chứng tỏ quy trình PNA rất nhạy cảm với biến động của dòng vào.
  - Hệ thống PNA đòi hỏi hệ thống giám sát liên tục và chiến lược điều khiển nghiêm ngặt hơn quy trình PDA.
- Quy trình Khử nitrat một phần kết hợp Anammox (PDA):
  - Quy trình PDA duy trì nồng độ nitơ dòng ra ổn định hơn trước các biến động tải trọng dòng vào.
  - Cấu hình phối hợp PNA và PDA giúp hệ thống vừa đạt hiệu suất khử nitơ cao, vừa tăng cường tính ổn định vận hành.
#### 5.1.3 Hướng dẫn định lượng chi tiết cho từng chỉ tiêu chất lượng dòng ra
- Kiểm soát nồng độ $\text{NH}_4^+$-N dòng ra:
  - Duy trì tỷ lệ $\text{C/N}$ nạp trong khoảng từ 2.72 đến 6.32.
  - Duy trì nồng độ TIN dòng vào trong dải từ 18.85 đến 87.76 mg/L.
  - Nồng độ $\text{NH}_4^+$-N dòng ra tăng vọt khi $\text{NH}_4^+$-N dòng vào vượt 62.32 mg/L hoặc TIN dòng vào vượt 91.08 mg/L.
  - Nước thải đô thị thông thường có nồng độ nitơ thấp hơn hai ngưỡng trên, rất thuận lợi cho công nghệ Anammox dòng chính.
- Kiểm soát nồng độ $\text{NO}_3^-$-N dòng ra:
  - Vi khuẩn Anammox sản sinh $\text{NO}_3^-$-N như một sản phẩm phụ của chu trình oxy hóa amoni kỵ khí.
  - Theo hệ số tỷ lượng phản ứng sinh hóa, Anammox tạo ra 0.26 mol $\text{NO}_3^-$-N khi oxy hóa 1 mol $\text{NH}_4^+$-N.
  - $\text{NO}_3^-$-N chiếm phần lớn nồng độ tổng nitơ vô cơ (TIN) trong dòng ra của trạm xử lý.
  - Vận hành hệ thống theo các ngưỡng định lượng sau để cực tiểu hóa $\text{NO}_3^-$-N dòng ra:
    - Nồng độ COD dòng vào: duy trì trong dải 200.42 – 305.91 mg/L.
    - Thời gian lưu thủy lực (HRT): duy trì $\text{HRT} < 9.95\text{ h}$ hoặc trong khoảng 11.50 – 12.54 h.
    - Nồng độ TIN dòng vào: duy trì trong dải 59.38 – 87.76 mg/L.
    - Tải trọng nạp nitơ (NLR): vận hành ở mức $\text{NLR} > 0.95\text{ kg N/m}^3\text{/d}$.
- Tối ưu hóa hiệu suất khử tổng nitơ vô cơ (TIN) tổng thể:
  - Duy trì nồng độ COD dòng vào ở mức thấp từ 168.78 đến 200.42 mg/L để đạt hiệu suất khử TIN cao nhất.
  - Phối hợp các cặp thông số TIN dòng vào và HRT theo chiến lược tương thích:
    - Cặp tương thích 1 (TIN thấp - HRT ngắn): nồng độ TIN dòng vào từ 71.54 đến 87.76 mg/L kết hợp $\text{HRT}$ ngắn từ 0.63 đến 6.84 h.
    - Cặp tương thích 2 (TIN cao - HRT dài): nồng độ TIN dòng vào $> 108.03\text{ mg/L}$ kết hợp $\text{HRT}$ dài từ 24.45 đến 26 h.
    - Tránh phối hợp cặp thông số không tương thích (như nạp TIN cao với HRT ngắn) vì sẽ làm suy giảm nghiêm trọng hiệu suất khử TIN.
- Nâng cao tốc độ loại bỏ nitơ Anammox (NARR):
  - Chỉ số NARR phản ánh trực tiếp hoạt tính chuyển hóa sinh học của quần thể vi khuẩn Anammox trong bể phản ứng.
  - NARR tăng rõ rệt khi tải trọng nạp nitơ tăng và thời gian lưu thủy lực giảm.
  - Thiết lập chế độ vận hành theo các ngưỡng sau để tối đa hóa chỉ số NARR:
    - Thời gian lưu thủy lực: duy trì $\text{HRT} < 7.36\text{ h}$.
    - Tải trọng nạp nitơ: duy trì $\text{NLR} > 1.28\text{ kg N/m}^3\text{/d}$ (đặc biệt hiệu quả khi $\text{NLR} > 2.18\text{ kg N/m}^3\text{/d}$).
    - Nồng độ TIN dòng vào: nạp ở mức $\text{TIN} > 176.89\text{ mg/L}$ (kết hợp $\text{TIN} > 176.94\text{ mg/L}$ và $\text{NO}_2^-\text{-N} > 18.78\text{ mg/L}$ cho phản ứng NARR cao nhất).
    - Nồng độ $\text{NO}_2^-$-N dòng vào: nạp ở mức $> 18.78\text{ mg/L}$.
    - Nồng độ $\text{NH}_4^+$-N dòng vào: nạp ở mức $> 152.61\text{ mg/L}$ (hoặc $> 148.53\text{ mg/L}$).
  - Đề xuất giải pháp kỹ thuật phối trộn nguồn nước:
    - Nước thải đô thị thực tế thường có nồng độ nitơ thấp hơn ngưỡng kích hoạt NARR tối đa.
    - Phối trộn nước thải đô thị với một tỷ lệ nước thải công nghiệp giàu nitơ để kích hoạt tối đa năng lực khử của vi khuẩn Anammox.

### 5.2 Các giới hạn tồn tại trong nghiên cứu mô hình hóa hiện tại
#### 5.2.1 Hiện tượng suy giảm độ chính xác dự đoán ở các chỉ tiêu nhạy cảm
- Đánh giá sai số trên các tập dữ liệu thực nghiệm:
  - Các mô hình học máy tối ưu từ AutoML đạt độ chính xác cao trên tập kiểm tra y văn, với $R^2$ từ 0.814 đến 0.993.
  - Độ chính xác dự đoán giảm nhẹ khi kiểm chứng trên tập dữ liệu thực nghiệm độc lập 185 mẫu của bể UASB:
    - Nồng độ $\text{NO}_2^-$-N dòng ra: mô hình GBM chỉ đạt $R^2 = 0.563$ ($\text{MAE} = 1.045\text{ mg/L}$).
    - Tốc độ phản ứng Anammox (NARR): mô hình Deep Learning chỉ đạt $R^2 = 0.677$ ($\text{MAE} = 0.013\text{ kg N/m}^3\text{/d}$).
    - Nồng độ $\text{NO}_3^-$-N dòng ra: mô hình XGBoost đạt $R^2 = 0.725$ ($\text{MAE} = 2.196\text{ mg/L}$).
- Nguyên nhân kỹ thuật dẫn đến sự suy giảm độ chính xác:
  - Sự khác biệt về điều kiện vận hành và cấu trúc cộng đồng vi sinh vật giữa tập huấn luyện y văn và thực nghiệm độc lập.
  - Các biến số đầu ra như $\text{NO}_2^-$-N, $\text{NO}_3^-$-N và NARR có độ nhạy rất cao với các biến động công nghệ.
  - Nitrit tồn tại như hợp chất trung gian không bền, nồng độ dao động mạnh và gây tích lũy sai số đo đạc qua các bước phản ứng.
- Đề xuất bổ sung biến số giám sát trực tuyến thời gian thực:
  - Nồng độ oxy hòa tan (DO) trong môi trường phản ứng.
  - Giá trị pH dung dịch.
  - Thế oxy hóa khử (ORP).
  - Nồng độ định lượng của các chất hữu cơ gây ức chế sinh học đặc thù.
#### 5.2.2 Hạn chế bản chất của chỉ số COD tổng trong mô tả chất hữu cơ phức tạp
- Thiếu hụt thông tin về cấu trúc hóa học phân tử:
  - Chỉ số COD tổng chỉ đo lượng oxy hóa học cần thiết để oxy hóa toàn bộ cơ chất hữu cơ.
  - COD không phân biệt được các dạng hợp chất hữu cơ và nhóm chức hóa học cấu thành.
  - Nước thải đô thị thực tế chứa nhiều hợp chất hữu cơ đa dạng với cấu trúc hóa học sai khác.
- Cơ chế tác động phân tử của các nhóm thế hữu cơ lên hệ sinh thái Anammox:
  - Nhóm thế alkyl và hydroxyl ($-\text{CH}_3, -\text{OH}$):
    - Làm thay đổi tính kỵ nước của bề mặt tế bào vi khuẩn.
    - Cản trở quá trình khuếch tán cơ chất qua màng tế bào.
    - Gây ảnh hưởng xấu đến độ bền liên kết và độ ổn định của bùn hạt vi sinh vật.
  - Nhóm thế halogen ($-\text{Cl}, -\text{F}$):
    - Đóng góp trực tiếp vào độc tính sinh học đối với hệ sinh thái bùn vi sinh.
    - Gây ức chế mạnh hoạt tính enzym trao đổi chất của vi khuẩn Anammox.
- Hạn chế đối với mô hình học máy:
  - Việc biểu diễn toàn bộ chất hữu cơ bằng một chỉ số COD duy nhất làm mất đi dữ liệu về các nhóm chất độc hại.
  - Các thuật toán học máy không thể nhận diện và học được cơ chế ức chế riêng biệt của từng hợp chất hữu cơ.
#### 5.2.3 Thiếu hụt quy mô dữ liệu hệ vi sinh vật và cấu trúc cộng đồng
- Bất cân xứng về dung lượng dữ liệu:
  - Cơ sở dữ liệu hiện tại tập trung chủ yếu vào các thông số vận hành hóa lý và thủy lực thông thường.
  - Dung lượng dữ liệu phân tích sinh học phân tử và giải trình tự gen vi sinh vật còn rất nhỏ.
- Hạn chế trong cách tiếp cận biến số vi sinh hiện tại:
  - Dữ liệu vi sinh vật mới chỉ được đưa vào dưới dạng một biến phân loại thô sơ về chi Anammox chiếm ưu thế.
  - Dữ liệu chưa nắm bắt được mối quan hệ hợp tác và cạnh tranh giữa Anammox với các vi sinh vật cộng sinh khác (AOB, NOB, vi khuẩn khử nitrat dị dưỡng).
- Định hướng nghiên cứu dữ liệu sinh học:
  - Cần xây dựng quy trình thu thập và chuẩn hóa dữ liệu giải trình tự cộng đồng vi sinh vật độ phân giải cao.
  - Sử dụng học máy để khai phá dữ liệu hệ gen nhằm cung cấp hiểu biết sâu sắc hơn về cơ chế sinh học trong hệ thống xử lý nước thải.

### 5.3 Định hướng phát triển Digital Twin kết hợp vi sinh vật học chính xác và Kết luận
#### 5.3.1 Khái niệm Digital Twin thông tin sinh học (Biology-informed Digital Twins)
- Kiến trúc mô phỏng bản sao số thế hệ mới:
  - Xây dựng bản sao kỹ thuật số tích hợp dữ liệu cảm biến công nghệ trực tuyến với dữ liệu dấu vân tay cộng đồng vi sinh vật độ phân giải cao (high-dimensional microbial community fingerprints).
  - Kết hợp thông tin đa tầng omics (genomics, transcriptomics, metabolomics) với các mô hình động học quá trình và thuật toán học máy.
- Chức năng giám sát và cảnh báo thông minh:
  - Nhận diện sớm các dấu hiệu suy thoái hệ vi sinh vật (suy giảm AOB, bùng phát vi khuẩn NOB, mất cân bằng bùn hạt).
  - Tự động điều chỉnh các thông số vận hành (lưu lượng khí cấp, HRT, tỷ lệ tuần hoàn bùn, dòng nạp cơ chất) trước khi xảy ra hiện tượng suy giảm chất lượng nước dòng ra.
#### 5.3.2 Chuyển đổi mô hình sang quản lý chính xác hệ vi sinh vật (Precision Microbiome Management)
- Dịch chuyển mô thức vận hành công nghệ:
  - Dịch chuyển từ phương thức điều khiển thủy lực theo kinh nghiệm truyền thống (empirical hydraulic control) sang quản lý chính xác hệ vi sinh vật (precision microbiome management).
  - Vận hành trạm xử lý dựa trên nguyên tắc chủ động kiến tạo vi môi trường tối ưu cho vi khuẩn Anammox và vi sinh vật cộng sinh.
- Chiến lược tối ưu hóa đa yếu tố (multifactor optimization):
  - Áp dụng các thuật toán học máy để khai phá các mối quan hệ ẩn giữa biến số hệ vi sinh vật và hiệu quả xử lý thực tế.
  - Đảm bảo trạm xử lý nước thải đô thị dòng chính vận hành liên tục, ổn định và đạt hiệu suất xử lý nitơ cao nhất.
#### 5.3.3 Kết luận toàn diện của công trình nghiên cứu
- Ưu thế công nghệ qua khai phá dữ liệu lớn:
  - Phân tích dữ liệu lớn khẳng định bể phản ứng dòng liên tục sử dụng bùn hạt Anammox có năng lực xử lý vượt trội đối với tải trọng nitơ cao.
  - Quy trình PNA có độ nhạy nạp cao hơn, trong khi quy trình phối hợp PNA và PDA đạt hiệu suất khử TIN tối ưu.
- Hiệu năng xuất sắc của nền tảng AutoML:
  - Thuật toán AutoML tự động hóa quy trình xây dựng các mô hình dự báo hiệu năng cao cho toàn bộ các chỉ tiêu chất lượng dòng ra chính.
  - Các mô hình dựa trên thuật toán tăng cường độ dốc (GBM và XGBoost) đạt độ chính xác dự báo cao nhất:
    - Tập kiểm tra y văn: $R^2 = 0.814\text{ – }0.993$.
    - Tập thực nghiệm kiểm chứng độc lập 185 mẫu UASB: $R^2 = 0.725\text{ – }0.945$ đối với các chỉ tiêu nồng độ nitơ dòng ra.
  - Kết quả chứng minh khả năng tổng quát hóa xuất sắc của các mô hình trên các tập dữ liệu độc lập chưa từng thấy trong quá trình huấn luyện.
- Ý nghĩa kỹ thuật của phân tích giải thích mô hình (PDP):
  - Phân tích 1D PDP và 2D PDP xác lập các ngưỡng vận hành định lượng tin cậy cho kỹ thuật môi trường:
    - Kiểm soát $\text{NH}_4^+$-N dòng ra: tỷ lệ $\text{C/N}$ từ 2.72 đến 6.32, nồng độ TIN dòng vào từ 18.85 đến 87.76 mg/L.
    - Cực tiểu hóa $\text{NO}_3^-$-N dòng ra: nồng độ COD dòng vào từ 200.42 đến 305.91 mg/L, $\text{NLR} > 0.95\text{ kg N/m}^3\text{/d}$, $\text{HRT} < 9.95\text{ h}$ hoặc trong khoảng 11.50 – 12.54 h.
    - Tối ưu hóa hiệu suất khử TIN: nồng độ COD dòng vào từ 168.78 đến 200.42 mg/L, ghép nối TIN thấp (71.54 – 87.76 mg/L) với HRT ngắn (0.63 – 6.84 h).
    - Thúc đẩy tốc độ Anammox NARR: duy trì $\text{HRT} < 7.36\text{ h}$, $\text{NLR} > 1.28\text{ kg N/m}^3\text{/d}$ và TIN dòng vào $> 176.89\text{ mg/L}$.
  - Các khuyến nghị kỹ thuật giải quyết căn bản bài toán mất ổn định trong vận hành công nghệ Anammox xử lý nước thải đô thị dòng chính.
