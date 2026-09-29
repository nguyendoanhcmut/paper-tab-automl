---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Khung Trí Tuệ Nhân Tạo Có Thể Diễn Giải Định Nghĩa Vùng Vận Hành MBR Xử Lý Nước Thải Bán Dẫn (An Interpretable AI Framework for Defining MBR Operational Basin)

## 1. Giới thiệu (Introduction)

### 1.1. Bối cảnh tiêu thụ nước siêu tinh khiết và đặc thù nước thải bán dẫn
- Ngành sản xuất chất bán dẫn tiêu thụ lượng nước siêu tinh khiết (UPW) rất lớn. Định mức tiêu thụ dao động từ $1400$ đến $4200\text{ L/cm}^2$ diện tích tấm wafer.
- Quy trình thu nhỏ kích thước vi mạch đòi hỏi tăng độ sạch của nước cấp. Quy trình này cũng làm tăng tải lượng ô nhiễm trong nước thải phát sinh.
- Dòng thải bán dẫn chứa ba nhóm ô nhiễm chính:
  - Hợp chất hữu cơ từ dung dịch chất bóc tách quang khắc (photoresist stripper), dung dịch hiện ảnh và dung môi.
  - Hợp chất ion từ công đoạn ăn mòn hóa học và làm sạch bề mặt tấm bán dẫn.
  - Hạt keo mài mòn từ công đoạn mài phẳng hóa học - cơ học (CMP).
- Nước thải yêu cầu hệ thống xử lý đa rào cản. Mỗi công đoạn đơn vị phải vận hành ổn định để bảo vệ các công trình phía sau.

### 1.2. Cấu hình màng sợi rỗng PVDF MBR và vai trò tiền xử lý cho hệ thống RO
- Bể sinh học màng (MBR) ngập nước tích hợp xử lý sinh học và tách pha màng. MBR thay thế hoàn toàn bể lắng thứ cấp.
- Module màng sợi rỗng làm từ vật liệu polyvinylidene fluoride (PVDF). Màng UF đặt trực tiếp trong bùn hoạt tính để hút nước trong qua màng.
- Màng UF giữ lại vi khuẩn, chất rắn lơ lửng và chất hữu cơ có khối lượng phân tử lớn. Nước thấm qua màng có chất lượng cao và không phụ thuộc vào chỉ số lắng của bùn.
- Hệ thống MBR đóng vai trò tiền xử lý trực tiếp trước công đoạn khử khoáng bằng màng thẩm thấu ngược (RO).
- Nước thấm UF quyết định trực tiếp tốc độ hình thành tắc nghẽn trên màng RO phía sau.
- Cấu hình MBR cho phép vận hành ở nồng độ chất rắn lơ lửng trong hỗn dịch bùn (MLSS) cao. Hệ thống tách rời thời gian lưu bùn (SRT) khỏi thời gian lưu thủy lực (HRT).
- Tách rời SRT và HRT làm giàu các chủng vi khuẩn nitrat hóa sinh trưởng chậm. Quá trình này giúp nâng cao hiệu suất loại bỏ chất dinh dưỡng.

### 1.3. Cơ chế tắc nghẽn màng trong chế độ hiếu khí kéo dài
- Tắc nghẽn màng MBR chịu sự chi phối của hỗn hợp phức tạp. Hỗn hợp này gồm sinh khối vi sinh, chất polymer ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP).
- Nước thải bán dẫn tạo ra cơ chế tắc nghẽn khác biệt hoàn toàn so với nước thải sinh hoạt đô thị:
  - Chất hữu cơ khó phân hủy sinh học (chất bóc tách, dung môi, chất tạo phức) hấp phụ chọn lọc lên bề mặt PVDF. Lớp hấp phụ này tạo liên kết bám dính rất khó phục hồi.
  - Hạt mài silica siêu mịn kích thước dưới micromet từ nước thải CMP xâm nhập vào bánh bùn. Các hạt này tạo ra lớp bùn nén chặt có độ rỗng cực thấp.
  - Tải trọng hữu cơ và nitơ biến động đột ngột theo chu kỳ sản xuất mẻ của nhà máy bán dẫn. Tải trọng này không tuân theo quy luật sinh hoạt ngày đêm.
- Dòng thải chứa hàm lượng nitơ cao nhưng thiếu hụt carbon hữu cơ cho quá trình khử nitrat. Người vận hành phải châm bổ sung dung dịch glucose (Glu).
- Tốc độ châm glucose liên kết trực tiếp tỷ lệ carbon trên nitơ (C/N) với tốc độ tích tụ màng sinh học.
- Nhà máy phải duy trì chế độ hiếu khí kéo dài (extended aeration) với giá trị SRT rất cao ($43.3 - 108.3\text{ ngày}$).
- Các kinh nghiệm vận hành MBR ở mức SRT ngắn truyền thống hoàn toàn mất hiệu lực trong điều kiện này. Hệ thống tạo ra bề mặt phản ứng phi tuyến tính phức tạp.

### 1.4. Giới hạn của các nghiên cứu học máy MBR truyền thống
- Các thuật toán học máy gồm ANN, RF, GBDT, XGBoost và LSTM.
- Các công bố trước đây báo cáo độ chính xác cao với hệ số xác định $R^2 \ge 0.90 - 0.97$. Ba hạn chế lớn cản trở việc triển khai thực tế:
  - Hầu hết nghiên cứu thực hiện trên mô hình phòng thí nghiệm hoặc pilot nhân tạo. Các mô hình này không phản ánh biến động thực tế từ chu kỳ sản xuất và suy thoái màng.
  - Phần lớn nghiên cứu coi mô hình là hộp đen bí ẩn. Mô hình không giải thích tương tác giữa các biến quá trình. Điều này làm giảm độ tin cậy của người vận hành.
  - Chuỗi dữ liệu SCADA đo theo giờ có tính tự tương quan thời gian rất mạnh. Cách chia ngẫu nhiên truyền thống đưa các điểm dữ liệu lân cận vào cả tập huấn luyện và kiểm định.
- Hiện tượng rò rỉ dữ liệu qua tự tương quan làm sai lệch kết quả. Độ chính xác công bố không phản ánh đúng năng lực dự báo trên điều kiện vận hành mới.

### 1.5. Khoảng trống tri thức và khung AI giải thích đa mô hình
- Khoảng trống thứ nhất nằm ở năng lực diễn giải đa mô hình. Các phương pháp SHAP trước đây chỉ áp dụng cho một mô hình đơn lẻ trên dải thông số hẹp.
- Thuật toán khác nhau gán mức quan trọng khác nhau cho cùng một biến đầu vào. Cần phân tích SHAP trên toàn bộ 16 mô hình để loại bỏ độ lệch thuật toán.
- Khoảng trống thứ hai là sự dịch chuyển từ dự đoán điểm sang xác định vùng vận hành an toàn (operational basin).
- Các thuật toán tối ưu hóa điểm đơn lẻ không phản ánh biên độ bền vững của hệ thống. Đồng thời, các biến vận hành liên kết chặt chẽ qua các ràng buộc thủy lực và sinh học.
- Khung nghiên cứu áp dụng kỹ thuật lấy mẫu trên đa tạp thực tế (manifold-constrained resampling). Phương pháp này đảm bảo chỉ khảo sát các trạng thái nhà máy có thể đạt được.
- Khung AI sử dụng 4593 bản ghi SCADA theo giờ trong 306 ngày tại Asan. Mô hình dự báo đồng thời ba biến: TMP, Flow và Level.

## 2. Mô hình và phương pháp: Thiết lập hệ thống và dữ liệu vận hành

### 2.1. Mô tả hệ thống MBR thực tế và thu thập dữ liệu SCADA
#### 2.1.1. Quy mô công trình và thông số module màng sợi rỗng
- Công trình thu gom và xử lý nước thải sản xuất bán dẫn đặt tại thành phố Asan, Hàn Quốc. Công suất thiết kế đạt $1125\text{ m}^3/\text{h}$.
- Hệ thống lọc màng UF gồm 9700 module màng sợi rỗng PVDF do hãng SUEZ sản xuất.
- Tổng diện tích bề mặt màng hoạt động đạt $329800\text{ m}^2$. Kích thước lỗ màng danh định nằm trong dải siêu lọc để loại bỏ triệt để hạt keo.

#### 2.1.2. Cấu trúc sinh học A-O-A-O và thể tích các đơn nguyên
- Hệ sinh học gồm chuỗi bể thiếu khí - hiếu khí (A-O-A-O) nối tiếp. Cấu hình này khử đồng thời chất hữu cơ và nitơ.
- Thể tích làm việc thực tế của các đơn nguyên:
  - Tổng thể tích vùng thiếu khí (Anoxic zones): $3841\text{ m}^3$.
  - Tổng thể tích vùng hiếu khí (Oxic zones): $8604\text{ m}^3$.
  - Thể tích bể điều chỉnh pH: $376\text{ m}^3$.
  - Thể tích bể màng ngập nước (Membrane tank): $1437\text{ m}^3$.
- Thời gian lưu thủy lực HRT trong nghiên cứu tính riêng cho vùng hiếu khí. Hệ thống SCADA ghi nhận HRT như một biến ảo (virtual parameter) với giá trị trung bình $7.33\text{ h}$.

#### 2.1.3. Chuỗi dữ liệu SCADA và tiêu chí loại trừ chu kỳ rửa CIP
- Dữ liệu thu thập liên tục từ ngày 01 tháng 01 năm 2025 đến ngày 03 tháng 11 năm 2025 (306 ngày vận hành).
- Hệ thống SCADA ghi nhận dữ liệu gốc tại chu kỳ 5 phút. Dữ liệu sau đó gộp thành trung bình 1 giờ.
- Chu kỳ rửa hóa học tại chỗ (CIP) gồm rửa duy trì (MC) và rửa phục hồi (RC). Toàn bộ dữ liệu trong các chu kỳ này bị loại bỏ vì không phản ánh quá trình tắc nghẽn thông thường.
- Tập dữ liệu sạch cuối cùng gồm 4593 bản ghi theo giờ. Biến thiên dài hạn được xem là sự trôi dạt vận hành do lão hóa màng và lịch sử rửa màng.

### 2.2. Thông số quá trình và phạm vi vận hành
#### 2.2.1. Bảy biến đầu vào kiểm soát sinh học và thủy lực
- Lưu lượng châm glucose ($\text{Glu}$): đại diện cho nguồn carbon bổ sung. Phạm vi vận hành đạt $0.165 - 2.258\text{ L/min}$.
- Nồng độ bùn lơ lửng ($\text{MLSS}$): kiểm soát động học bánh bùn. Dải vận hành đạt $4275 - 8173\text{ mg/L}$.
- Lưu lượng khí sục màng ($\text{Air}$): tạo lực cắt thủy lực làm bong tróc bánh bùn. Dải cấp khí đạt $3375 - 7157\text{ m}^3/\text{h}$.
- Tỷ lệ thức ăn trên vi sinh ($\text{F/M}$): điều hòa sản sinh EPS. Dải vận hành đạt $0.016 - 0.038\text{ ngày}^{-1}$.
- Tỷ lệ carbon trên nitơ ($\text{C/N}$): đo lường dưới dạng $\text{TOC/TN}$. Dải biến thiên đạt $4.80 - 17.52$.
- Thời gian lưu thủy lực hiếu khí ($\text{HRT}$): kiểm soát thời gian phản ứng. Dải giá trị đạt $5.1 - 8.3\text{ h}$.
- Thời gian lưu bùn ($\text{SRT}$): quyết định tuổi bùn và lượng SMP. Dải vận hành đạt $43.3 - 108.3\text{ ngày}$.

#### 2.2.2. Ba biến trạng thái mục tiêu đầu ra
- Áp suất xuyên màng ($\text{TMP}$): chỉ thị chính mức độ tắc nghẽn. Dải áp suất chân không đạt $3.2 - 39.7\text{ kPa}$ ($-0.462\text{ đến }-0.034\text{ bar}$).
- Lưu lượng nước thấm ($\text{Flow}$): đo lường sản lượng lọc. Tổng lưu lượng trạm đạt $250 - 1125\text{ m}^3/\text{h}$ ($0.618 - 2.289\text{ m}^3/\text{min}$ mỗi nhánh).
- Mức nước bể màng ($\text{Level}$): biến tích hợp phản ánh cân bằng thủy lực. Dải đo đạt $1.8 - 3.6\text{ m}$ ($64.005\% - 73.942\%$).

#### 2.2.3. Thống kê mô tả và miền giá trị vận hành thực tế
- Bảng thống kê 4593 mẫu đo đạc SCADA trong 306 ngày liên tục:
  - $\text{Glu}$: giá trị trung bình $0.6775\text{ L/min}$, độ lệch chuẩn $0.1807\text{ L/min}$, khoảng biến thiên thực tế $[0.4027, 1.3515]\text{ L/min}$.
  - $\text{MLSS}$: giá trị trung bình $4889.5\text{ mg/L}$, độ lệch chuẩn $1075.2\text{ mg/L}$, khoảng biến thiên thực tế $[1919.4, 7628.8]\text{ mg/L}$.
  - $\text{Air}$: giá trị trung bình $5945.7\text{ m}^3/\text{h}$, độ lệch chuẩn $534.5\text{ m}^3/\text{h}$, khoảng biến thiên thực tế $[4469.1, 7268.3]\text{ m}^3/\text{h}$.
  - $\text{F/M}$: giá trị trung bình $0.0275\text{ ngày}^{-1}$, độ lệch chuẩn $0.0078\text{ ngày}^{-1}$, khoảng biến thiên thực tế $[0.0118, 0.0658]\text{ ngày}^{-1}$.
  - $\text{C/N}$: giá trị trung bình $9.4314$, độ lệch chuẩn $2.2581$, khoảng biến thiên thực tế $[4.8040, 17.5029]$.
  - $\text{HRT}$: giá trị trung bình $7.3346\text{ h}$, độ lệch chuẩn $0.7947\text{ h}$, khoảng biến thiên thực tế $[5.8738, 11.0411]\text{ h}$.
  - $\text{SRT}$: giá trị trung bình $87.828\text{ ngày}$, độ lệch chuẩn $14.564\text{ ngày}$, khoảng biến thiên thực tế $[43.323, 108.333]\text{ ngày}$.
  - $\text{TMP}$: giá trị trung bình $-0.122\text{ bar}$, độ lệch chuẩn $0.090\text{ bar}$, khoảng biến thiên thực tế $[-0.462, -0.034]\text{ bar}$.
  - $\text{Flow}$: giá trị trung bình $1.817\text{ m}^3/\text{min}$, độ lệch chuẩn $0.257\text{ m}^3/\text{min}$, khoảng biến thiên thực tế $[0.618, 2.289]\text{ m}^3/\text{min}$.
  - $\text{Level}$: giá trị trung bình $65.774\%$, độ lệch chuẩn $1.114\%$, khoảng biến thiên thực tế $[64.005\%, 73.942\%]$.

### 2.3. Tiền xử lý và chuẩn hóa dữ liệu
#### 2.3.1. Khử nhiễu ngoại lai cảm biến và xử lý dữ liệu khuyết thiếu
- Dữ liệu thô từ hệ thống SCADA trải qua quy trình kiểm soát chất lượng nghiêm ngặt.
- Loại bỏ ngoại lai cơ học và lỗi cảm biến bằng khoảng tứ phân vị (IQR) và ngưỡng Z-score.
- Dữ liệu khuyết thiếu do mất tín hiệu được xử lý bằng nội suy thời gian cục bộ.

#### 2.3.2. Chuẩn hóa Z-score độc lập ngăn ngừa rò rỉ thông tin
- Chuẩn hóa Z-score đưa tất cả biến về phân phối có giá trị trung bình bằng 0 và phương sai bằng 1:
  $$z = \frac{x - \mu_{\text{train}}}{\sigma_{\text{train}}}$$
- Giá trị trung bình $\mu_{\text{train}}$ và độ lệch chuẩn $\sigma_{\text{train}}$ tính toán tuyệt đối trên tập huấn luyện (training fold).
- Áp dụng trực tiếp tham số chuẩn hóa sang tập kiểm định. Cách làm này ngăn ngừa rò rỉ thông tin.
- Chuẩn hóa giữ nguyên hình dạng phân phối gốc. Các đặc trưng độ lệch, tính đa đỉnh và đuôi phân phối được bảo toàn.

#### 2.3.3. Bảo toàn tương quan tuyến tính giữa các biến quá trình
- Ma trận tương quan Pearson trước và sau chuẩn hóa hoàn toàn đồng nhất.
- Chuẩn hóa Z-score bảo toàn quan hệ phụ thuộc vật lý giữa các biến:
  - Quan hệ tỷ lệ nghịch rõ nét giữa áp suất xuyên màng TMP và lưu lượng Flow.
  - Quan hệ ràng buộc giữa mức nước bể màng Level và các thông số tải trọng sinh học.
  - Ràng buộc thủy lực kết hợp giữa HRT và SRT trong việc kiểm soát lưu lượng đầu ra.
- Biến trạng thái Level phản ánh cả động học thủy lực lẫn mức độ tích tụ bùn trong bể màng.

### 2.4. Phân chia tập dữ liệu và đánh giá độ bền vững mô hình
#### 2.4.1. Phân chia ngẫu nhiên và phân tích biến thiên đa phân vùng
- Phân chia ngẫu nhiên theo tỷ lệ $70/30$ ($3215$ mẫu học, $1378$ mẫu thử) và $80/20$ để đối sánh.
- Phân tích đa phân vùng (multi-split) thực hiện trên 20 phân vùng ngẫu nhiên độc lập.
- Tái huấn luyện 16 mô hình trên 20 phân vùng. Thao tác này giúp đo lường độ biến thiên kết quả.

#### 2.4.2. Phân chia theo khối thời gian khử tự tương quan
- Dữ liệu chuỗi thời gian SCADA theo giờ có mức độ tự tương quan rất cao. Phân chia ngẫu nhiên gây rò rỉ các mẫu lân cận vào tập kiểm tra.
- Áp dụng phân chia theo khối thời gian (blocked partition). Kích thước khối gồm $1\text{ h}$, $6\text{ h}$, $24\text{ h}$, $72\text{ h}$, $168\text{ h}$, $336\text{ h}$ và $720\text{ h}$.
- Các khối nguyên vẹn được phân bổ ngẫu nhiên để phá vỡ cấu trúc tự tương quan ngắn hạn giữa các giờ liền kề.
- Kỹ thuật này kiểm tra năng lực tổng quát hóa mô hình giữa các ngày vận hành khác nhau.

##

## 2. Mô hình và phương pháp (Models and Methods)

### 2.1. Mô tả hệ thống MBR thực tế và thu thập dữ liệu SCADA
#### 2.1.1. Quy mô công trình và thông số module màng sợi rỗng
- Công trình thu gom và xử lý nước thải sản xuất bán dẫn đặt tại thành phố Asan, Hàn Quốc. Công suất thiết kế đạt $1125\text{ m}^3/\text{h}$.
- Hệ thống lọc màng UF gồm 9700 module màng sợi rỗng PVDF do hãng SUEZ sản xuất.
- Tổng diện tích bề mặt màng hoạt động đạt $329800\text{ m}^2$. Kích thước lỗ màng danh định nằm trong dải siêu lọc để loại bỏ triệt để hạt keo.

#### 2.1.2. Cấu trúc sinh học A-O-A-O và thể tích các đơn nguyên
- Hệ sinh học gồm chuỗi bể thiếu khí - hiếu khí (A-O-A-O) nối tiếp. Cấu hình này khử đồng thời chất hữu cơ và nitơ.
- Thể tích làm việc thực tế của các đơn nguyên:
  - Tổng thể tích vùng thiếu khí (Anoxic zones): $3841\text{ m}^3$.
  - Tổng thể tích vùng hiếu khí (Oxic zones): $8604\text{ m}^3$.
  - Thể tích bể điều chỉnh pH: $376\text{ m}^3$.
  - Thể tích bể màng ngập nước (Membrane tank): $1437\text{ m}^3$.
- Thời gian lưu thủy lực HRT trong nghiên cứu tính riêng cho vùng hiếu khí. Hệ thống SCADA ghi nhận HRT như một biến ảo (virtual parameter) với giá trị trung bình $7.33\text{ h}$.

#### 2.1.3. Chuỗi dữ liệu SCADA và tiêu chí loại trừ chu kỳ rửa CIP
- Dữ liệu thu thập liên tục từ ngày 01 tháng 01 năm 2025 đến ngày 03 tháng 11 năm 2025 (306 ngày vận hành).
- Hệ thống SCADA ghi nhận dữ liệu gốc tại chu kỳ 5 phút. Dữ liệu sau đó gộp thành trung bình 1 giờ.
- Chu kỳ rửa hóa học tại chỗ (CIP) gồm rửa duy trì (MC) và rửa phục hồi (RC). Toàn bộ dữ liệu trong các chu kỳ này bị loại bỏ vì không phản ánh quá trình tắc nghẽn thông thường.
- Tập dữ liệu sạch cuối cùng gồm 4593 bản ghi theo giờ. Biến thiên dài hạn được xem là sự trôi dạt vận hành do lão hóa màng và lịch sử rửa màng.

### 2.2. Thông số quá trình và phạm vi vận hành
#### 2.2.1. Bảy biến đầu vào kiểm soát sinh học và thủy lực
- Lưu lượng châm glucose ($\text{Glu}$): đại diện cho nguồn carbon bổ sung. Phạm vi vận hành đạt $0.165 - 2.258\text{ L/min}$.
- Nồng độ bùn lơ lửng ($\text{MLSS}$): kiểm soát động học bánh bùn. Dải vận hành đạt $4275 - 8173\text{ mg/L}$.
- Lưu lượng khí sục màng ($\text{Air}$): tạo lực cắt thủy lực làm bong tróc bánh bùn. Dải cấp khí đạt $3375 - 7157\text{ m}^3/\text{h}$.
- Tỷ lệ thức ăn trên vi sinh ($\text{F/M}$): điều hòa sản sinh EPS. Dải vận hành đạt $0.016 - 0.038\text{ ngày}^{-1}$.
- Tỷ lệ carbon trên nitơ ($\text{C/N}$): đo lường dưới dạng $\text{TOC/TN}$. Dải biến thiên đạt $4.80 - 17.52$.
- Thời gian lưu thủy lực hiếu khí ($\text{HRT}$): kiểm soát thời gian phản ứng. Dải giá trị đạt $5.1 - 8.3\text{ h}$.
- Thời gian lưu bùn ($\text{SRT}$): quyết định tuổi bùn và lượng SMP. Dải vận hành đạt $43.3 - 108.3\text{ ngày}$.

#### 2.2.2. Ba biến trạng thái mục tiêu đầu ra
- Áp suất xuyên màng ($\text{TMP}$): chỉ thị chính mức độ tắc nghẽn. Dải áp suất chân không đạt $3.2 - 39.7\text{ kPa}$ ($-0.462\text{ đến }-0.034\text{ bar}$).
- Lưu lượng nước thấm ($\text{Flow}$): đo lường sản lượng lọc. Tổng lưu lượng trạm đạt $250 - 1125\text{ m}^3/\text{h}$ ($0.618 - 2.289\text{ m}^3/\text{min}$ mỗi nhánh).
- Mức nước bể màng ($\text{Level}$): biến tích hợp phản ánh cân bằng thủy lực. Dải đo đạt $1.8 - 3.6\text{ m}$ ($64.005\% - 73.942\%$).

#### 2.2.3. Thống kê mô tả và miền giá trị vận hành thực tế
- Bảng thống kê 4593 mẫu đo đạc SCADA trong 306 ngày liên tục:
  - $\text{Glu}$: giá trị trung bình $0.6775\text{ L/min}$, độ lệch chuẩn $0.1807\text{ L/min}$, khoảng biến thiên thực tế $[0.4027, 1.3515]\text{ L/min}$.
  - $\text{MLSS}$: giá trị trung bình $4889.5\text{ mg/L}$, độ lệch chuẩn $1075.2\text{ mg/L}$, khoảng biến thiên thực tế $[1919.4, 7628.8]\text{ mg/L}$.
  - $\text{Air}$: giá trị trung bình $5945.7\text{ m}^3/\text{h}$, độ lệch chuẩn $534.5\text{ m}^3/\text{h}$, khoảng biến thiên thực tế $[4469.1, 7268.3]\text{ m}^3/\text{h}$.
  - $\text{F/M}$: giá trị trung bình $0.0275\text{ ngày}^{-1}$, độ lệch chuẩn $0.0078\text{ ngày}^{-1}$, khoảng biến thiên thực tế $[0.0118, 0.0658]\text{ ngày}^{-1}$.
  - $\text{C/N}$: giá trị trung bình $9.4314$, độ lệch chuẩn $2.2581$, khoảng biến thiên thực tế $[4.8040, 17.5029]$.
  - $\text{HRT}$: giá trị trung bình $7.3346\text{ h}$, độ lệch chuẩn $0.7947\text{ h}$, khoảng biến thiên thực tế $[5.8738, 11.0411]\text{ h}$.
  - $\text{SRT}$: giá trị trung bình $87.828\text{ ngày}$, độ lệch chuẩn $14.564\text{ ngày}$, khoảng biến thiên thực tế $[43.323, 108.333]\text{ ngày}$.
  - $\text{TMP}$: giá trị trung bình $-0.122\text{ bar}$, độ lệch chuẩn $0.090\text{ bar}$, khoảng biến thiên thực tế $[-0.462, -0.034]\text{ bar}$.
  - $\text{Flow}$: giá trị trung bình $1.817\text{ m}^3/\text{min}$, độ lệch chuẩn $0.257\text{ m}^3/\text{min}$, khoảng biến thiên thực tế $[0.618, 2.289]\text{ m}^3/\text{min}$.
  - $\text{Level}$: giá trị trung bình $65.774\%$, độ lệch chuẩn $1.114\%$, khoảng biến thiên thực tế $[64.005\%, 73.942\%]$.

### 2.3. Tiền xử lý và chuẩn hóa dữ liệu
#### 2.3.1. Khử nhiễu ngoại lai cảm biến và xử lý dữ liệu khuyết thiếu
- Dữ liệu thô từ hệ thống SCADA trải qua quy trình kiểm soát chất lượng nghiêm ngặt.
- Loại bỏ ngoại lai cơ học và lỗi cảm biến bằng khoảng tứ phân vị (IQR) và ngưỡng Z-score.
- Dữ liệu khuyết thiếu do mất tín hiệu được xử lý bằng nội suy thời gian cục bộ.

#### 2.3.2. Chuẩn hóa Z-score độc lập ngăn ngừa rò rỉ thông tin
- Chuẩn hóa Z-score đưa tất cả biến về phân phối có giá trị trung bình bằng 0 và phương sai bằng 1:
  $$z = \frac{x - \mu_{\text{train}}}{\sigma_{\text{train}}}$$
- Giá trị trung bình $\mu_{\text{train}}$ và độ lệch chuẩn $\sigma_{\text{train}}$ tính toán tuyệt đối trên tập huấn luyện (training fold).
- Áp dụng trực tiếp tham số chuẩn hóa sang tập kiểm định. Cách làm này ngăn ngừa rò rỉ thông tin.
- Chuẩn hóa giữ nguyên hình dạng phân phối gốc. Các đặc trưng độ lệch, tính đa đỉnh và đuôi phân phối được bảo toàn.

#### 2.3.3. Bảo toàn tương quan tuyến tính giữa các biến quá trình
- Ma trận tương quan Pearson trước và sau chuẩn hóa hoàn toàn đồng nhất.
- Chuẩn hóa Z-score bảo toàn quan hệ phụ thuộc vật lý giữa các biến:
  - Quan hệ tỷ lệ nghịch rõ nét giữa áp suất xuyên màng TMP và lưu lượng Flow.
  - Quan hệ ràng buộc giữa mức nước bể màng Level và các thông số tải trọng sinh học.
  - Ràng buộc thủy lực kết hợp giữa HRT và SRT trong việc kiểm soát lưu lượng đầu ra.
- Biến trạng thái Level phản ánh cả động học thủy lực lẫn mức độ tích tụ bùn trong bể màng.

### 2.4. Phân chia tập dữ liệu và đánh giá độ bền vững mô hình
#### 2.4.1. Phân chia ngẫu nhiên và phân tích biến thiên đa phân vùng
- Phân chia ngẫu nhiên theo tỷ lệ $70/30$ ($3215$ mẫu học, $1378$ mẫu thử) và $80/20$ để đối sánh.
- Phân tích đa phân vùng (multi-split) thực hiện trên 20 phân vùng ngẫu nhiên độc lập.
- Tái huấn luyện 16 mô hình trên 20 phân vùng. Thao tác này giúp đo lường độ biến thiên kết quả.

#### 2.4.2. Phân chia theo khối thời gian khử tự tương quan
- Dữ liệu chuỗi thời gian SCADA theo giờ có mức độ tự tương quan rất cao. Phân chia ngẫu nhiên gây rò rỉ các mẫu lân cận vào tập kiểm tra.
- Áp dụng phân chia theo khối thời gian (blocked partition). Kích thước khối gồm $1\text{ h}$, $6\text{ h}$, $24\text{ h}$, $72\text{ h}$, $168\text{ h}$, $336\text{ h}$ và $720\text{ h}$.
- Các khối nguyên vẹn được phân bổ ngẫu nhiên để phá vỡ cấu trúc tự tương quan ngắn hạn giữa các giờ liền kề.
- Kỹ thuật này kiểm tra năng lực tổng quát hóa mô hình giữa các ngày vận hành khác nhau.

#### 2.4.3. Kiểm định ngoại suy thời gian và xác thực chéo trên nhánh màng B
- Phân vùng theo thời gian (chronological partition): huấn luyện trên $70\%$ đầu và kiểm định trên $30\%$ cuối.
- Phiên bản loại trừ (purged chronological partition) loại bỏ khoảng đệm 1 tuần tại ranh giới hai tập.
- Kiểm định ngoại suy thời gian trên 3-4 tháng dữ liệu mới. Quy trình kết hợp tái huấn luyện hàng ngày (daily refit).
- Xác thực chéo độc lập trên nhánh màng B (parallel B stream) với 4593 bản ghi theo giờ riêng biệt tại cùng nhà máy.
- Kiểm định mô hình của nhánh A trực tiếp trên nhánh màng B không cần tái huấn luyện.

### 2.5. Lựa chọn và huấn luyện mô hình học máy

#### 2.5.1. Khảo sát 16 thuật toán qua 6 họ mô hình và kiểm định giả thuyết cấu trúc
- Nghiên cứu khảo sát 16 thuật toán hồi quy thuộc 6 họ mô hình. Các mô hình dự đoán 3 biến trạng thái từ 7 thông số vận hành.
- Việc so sánh các họ mô hình là một kiểm định giả thuyết cấu trúc. Thí nghiệm kiểm tra bản chất quan hệ giữa sinh học và màng lọc:
  - Họ Tuyến tính (Linear Regression - OLS, 1 mô hình): Kiểm tra mối quan hệ cộng tính và đơn điệu giữa các thông số.
  - Họ Tuyến tính hiệu chỉnh (Ridge, Lasso, ElasticNet, 3 mô hình): Kiểm tra giả thuyết cộng tính. Mô hình đồng thời đánh giá tác động của đa cộng tuyến.
  - Họ Máy vector hỗ trợ (SVR nhân RBF, 1 mô hình): Kiểm tra khả năng biểu diễn của bề mặt phi tuyến trơn toàn cục.
  - Họ Dựa trên cá thể (K-Nearest Neighbors - KNN, 1 mô hình): Kiểm tra tính quy luật cục bộ trong không gian vận hành. Các điều kiện lân cận phải tạo ra phản ứng tương đồng.
  - Họ Tập hợp cây (Decision Tree, Random Forest, Extra Trees, Bagging, AdaBoost, Gradient Boosting, Hist Gradient Boosting, XGBoost, LightGBM, 9 mô hình).
  - Họ tập hợp cây kiểm tra tác động ngưỡng và tương tác phi tuyến. Đây là các đặc tính dự báo theo lý thuyết tắc nghẽn màng kinh điển.
  - Họ Mạng nơ-ron (MLP hai tầng ẩn, 1 mô hình): Kiểm tra đóng góp của biểu diễn phân cấp phi tuyến sâu.
- Phân tích đối lập giữa Bagging và Boosting xác định giải pháp xử lý dữ liệu cảm biến công nghiệp:
  - Kỹ thuật Bagging (Extra Trees, Random Forest, Bagging) giảm phương sai. Kỹ thuật này làm mịn dao động ngẫu nhiên của cảm biến hiệu quả.
  - Kỹ thuật Boosting (XGBoost, LightGBM, CatBoost) giảm độ lệch tuần tự. Kỹ thuật này nhạy cảm hơn với dữ liệu nhiễu ngoại lai.
- Mô hình Extra Trees đạt độ chính xác cao nhất cho cả 3 mục tiêu. Mô hình này được chọn làm đại diện duy nhất cho phân tích tiếp theo.

#### 2.5.2. Tối ưu hóa siêu tham số bằng Bayesian Optimization qua FLAML
- Nghiên cứu tối ưu hóa siêu tham số bằng giải thuật Bayesian Optimization thông qua thư viện FLAML.
- Không gian tìm kiếm siêu tham số được định nghĩa trên các phân phối liên tục và rời rạc:
  - Số lượng cây quyết định ($n_{\text{estimators}}$): Khảo sát trong khoảng từ 50 đến 500 cây.
  - Độ sâu tối đa của cây ($max\_depth$): Khảo sát từ 3 đến 30 tầng hoặc không giới hạn độ sâu.
  - Số mẫu tối thiểu để phân tách nhánh ($min\_samples\_split$): Khảo sát từ 2 đến 20 mẫu.
  - Tỷ lệ đặc trưng ngẫu nhiên cho mỗi vết cắt ($max\_features$): Khảo sát liên tục từ 0.3 đến 1.0.
  - Tốc độ học ($learning\_rate$) cho các mô hình boosting: Tìm kiếm logarit trong khoảng $10^{-3}$ đến $0.3$.
- Hàm mục tiêu tối ưu hóa là cực tiểu hóa sai số căn bậc hai trung bình bình phương (RMSE) trên tập kiểm thực chéo.
- Giải thuật tìm kiếm Bayesian phân bổ tài nguyên tính toán hiệu quả. Giải thuật tập trung khai thác các vùng siêu tham số tiềm năng cao.

#### 2.5.3. Môi trường triển khai và cấu hình mô hình đại diện
- Toàn bộ quy trình huấn luyện và đánh giá thực hiện trên ngôn ngữ Python phiên bản 3.10.
- Các thư viện cốt lõi gồm NumPy, pandas, scikit-learn, XGBoost, LightGBM và SHAP.
- Mô hình Extra Trees đại diện sử dụng 100 cây quyết định ngẫu nhiên hóa cực độ.
- Thuật toán Extra Trees chọn các điểm cắt phân nhánh hoàn toàn ngẫu nhiên cho từng đặc trưng con.
- Cơ chế ngẫu nhiên hóa điểm cắt giúp giảm mạnh phương sai của mô hình. Cơ chế này không làm tăng độ lệch dự báo.
- Cấu hình thống nhất này bảo đảm tính nhất quán xuyên suốt cho cả ba biến mục tiêu: TMP, Flow và Level.

### 2.6. Phân tích khả năng diễn giải qua SHAP đa mô hình

#### 2.6.1. Khung lý thuyết giá trị Shapley và mô hình phụ gia cục bộ
- Phương pháp SHAP bắt nguồn từ lý thuyết trò chơi hợp tác của Lloyd Shapley (1953).
- Giá trị Shapley định lượng mức đóng góp biên công bằng của từng đặc trưng vào kết quả dự đoán của mô hình.
- Mô hình giải thích phụ gia cục bộ biểu diễn đầu ra $f(x)$ thành tổng tuyến tính của các giá trị phân bổ:
  $$f(x) = \phi_0 + \sum_{j=1}^M \phi_j(x)$$
  Trong đó:
  - $\phi_0 = \mathbb{E}[f(x)]$ là giá trị dự đoán kỳ vọng gốc trên tập dữ liệu nền.
  - $\phi_j(x)$ là giá trị Shapley của đặc trưng thứ $j$ đối với mẫu dữ liệu $x$.
  - $M$ là tổng số lượng đặc trưng đầu vào ($M = 7$).
- Công thức giải tích tính toán giá trị Shapley thỏa mãn tính công bằng cổ điển:
  $$\phi_j = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{j\}) - f_x(S) \right]$$
  Trong đó:
  - $F$ là tập hợp toàn bộ các đặc trưng đầu vào.
  - $S$ là tập hợp con các đặc trưng không chứa đặc trưng $j$.
  - $f_x(S)$ là giá trị dự báo kỳ vọng có điều kiện khi chỉ quan sát tập đặc trưng $S$.
- Phân tích SHAP thỏa mãn ba tiên đề toán học cốt lõi: Tính hiệu quả cục bộ, tính đối xứng và tính đơn điệu.

#### 2.6.2. Thuật toán TreeSHAP tối ưu so với KernelSHAP mô hình thay thế
- Nghiên cứu triển khai TreeSHAP cho 9 mô hình dạng cây và KernelSHAP cho 7 mô hình phi cây.
- Thuật toán TreeSHAP khai thác cấu trúc phân nhánh cây để tính toán chính xác kỳ vọng có điều kiện.
- Độ phức tạp tính toán của TreeSHAP đạt mức $O(TLD^2)$. Trong đó, $T$ là số cây, $L$ là số lá tối đa và $D$ là độ sâu tối đa.
- TreeSHAP xử lý tin cậy và chính xác cấu trúc tương quan mạnh giữa các biến vận hành thực tế.
- Thuật toán KernelSHAP là phương pháp xấp xỉ không phụ thuộc mô hình. Phương pháp này dùng hồi quy tuyến tính cục bộ có trọng số.
- Khi các biến đầu vào có tương quan mạnh, KernelSHAP dễ tạo ra các liên minh mẫu ngoài phân phối thực tế.
- Hiện tượng này dẫn đến việc phóng đại tầm quan trọng của các biến điều khiển ngắn hạn như sục khí.
- KernelSHAP đồng thời đánh giá thấp vai trò của các biến sinh học biến thiên chậm như SRT.
- Khung so sánh đa mô hình giúp phát hiện sai lệch thuật toán mà các phân tích mô hình đơn lẻ không thể nhận diện.

#### 2.6.3. Xây dựng 48 hồ sơ giải thích đặc trưng và phân tích tương tác
- Nghiên cứu thiết lập 48 hồ sơ diễn giải đặc trưng riêng biệt từ tổ hợp 16 thuật toán và 3 biến mục tiêu.
- Ba công cụ trực quan hóa định lượng được xây dựng cho từng tổ hợp mô hình và mục tiêu:
  - Biểu đồ bầy ong (Beeswarm plot): Thể hiện phân phối giá trị SHAP của từng mẫu và hướng tác động tăng hoặc giảm.
  - Giá trị SHAP tuyệt đối trung bình ($\text{mean}(|\text{SHAP}|)$): Xác định thứ hạng mức độ quan trọng toàn cục của 7 thông số.
  - Biểu đồ phụ thuộc (Dependence plot): Phản ánh tác động phi tuyến của từng biến và nhận diện các ngưỡng vận hành giới hạn.
- Phân tích tương tác đặc trưng bậc hai qua ma trận giá trị tương tác SHAP:
  $$\phi_{i,j} = \sum_{S \subseteq F \setminus \{i,j\}} \frac{|S|!(|F| - |S| - 2)!}{2(|F|!)} \left[ f_x(S \cup \{i,j\}) - f_x(S \cup \{i\}) - f_x(S \cup \{j\}) + f_x(S) \right]$$
- Giá trị này phân tách tác động độc lập của biến $i$ khỏi hiệu ứng hiệp đồng khi kết hợp cùng biến $j$.

#### 2.6.4. Ý nghĩa nhận thức luận giữa liên kết thống kê và cơ chế vật lý
- Giá trị SHAP định lượng mức độ liên kết thống kê trong phân phối dữ liệu huấn luyện SCADA.
- SHAP không chứng minh quan hệ nhân quả vật lý thực nghiệm nếu không có kiểm chứng thực nghiệm độc lập.
- Các diễn giải cơ chế được đối chiếu nghiêm ngặt với lý thuyết lọc màng, động học bùn hoạt tính và thủy lực MBR.
- Khung tiếp cận này loại bỏ các tương quan giả tạo và cung cấp cơ sở khoa học tin cậy cho người vận hành.

### 2.7. Xác định điều kiện vận hành tối ưu (Operational Basin)

#### 2.7.1. Định nghĩa không gian vận hành khả thi và ba tiêu chuẩn kỹ thuật đồng thời
- Không gian vận hành khả thi (Operational Basin) là tập hợp các trạng thái đáp ứng đồng thời 3 tiêu chí kỹ thuật:
  - Tiêu chí Áp suất xuyên màng: $\text{TMP} \le \text{TMP}_{\text{threshold}}$, với dải vận hành an toàn $-0.09\text{ bar} \le \text{TMP} \le -0.03\text{ bar}$.
  - Giới hạn này ngăn ngừa tắc nghẽn màng nghiêm trọng và bảo vệ cấu trúc sợi màng PVDF.
  - Tiêu chí Lưu lượng thấm: $\text{Flow} \ge \text{Flow}_{\text{design}}$, với dải sản lượng yêu cầu $1.5\text{ m}^3/\text{min} \le \text{Flow} \le 2.2\text{ m}^3/\text{min}$.
  - Tiêu chí này bảo đảm công suất xử lý nước thải liên tục cho nhà máy chế tạo bán dẫn.
  - Tiêu chí Mức nước bể màng: $\text{Level}_{\text{min}} \le \text{Level} \le \text{Level}_{\text{max}}$, với dải kiểm soát $65.0\% \le \text{Level} \le 67.0\%$.
  - Tiêu chí này duy trì cân bằng thủy lực, bảo đảm màng ngập nước và chống tràn bể màng.
- Điểm vận hành đạt mức khả thi khi cả 3 giá trị dự báo đồng thời thỏa mãn các ngưỡng trên.

#### 2.7.2. Phương pháp lấy mẫu tái lập ràng buộc theo đa tạp (Manifold-Constrained Resampling)
- Việc lấy mẫu độc lập từng biến trên dải biên độ tạo ra các điểm phi thực tế ngoài không gian hoạt động.
- Nghiên cứu áp dụng kỹ thuật lấy mẫu hạt nhân hiệp phương sai cục bộ bị ràng buộc bởi đa tạp:
  - Bước 1: Rút ngẫu nhiên đồng đều một mẫu giờ gốc ($\mathbf{x}_{\text{seed}}$) từ 4593 bản ghi thực tế của nhà máy.
  - Bước 2: Xác định $k = 30$ điểm lân cận gần nhất của mẫu gốc trong không gian đầu vào chuẩn hóa Z-score.
  - Bước 3: Tính toán ma trận hiệp phương sai cục bộ $\mathbf{\Sigma}_k$ từ 30 điểm lân cận này.
  - Bước 4: Tạo mẫu ứng viên bằng cách nhiễu loạn điểm gốc theo phân phối Gauss với hệ số băng thông $\gamma = 0.6$:
    $$\mathbf{x}_{\text{cand}} = \mathbf{x}_{\text{seed}} + \mathcal{N}\left(\mathbf{0}, \gamma^2 \mathbf{\Sigma}_k\right)$$
  - Bước 5: Áp dụng điều kiện loại bỏ kép để kiểm soát mẫu ứng viên:
    - Loại bỏ mẫu ứng viên nếu bất kỳ biến nào vượt ra ngoài khoảng giá trị biên quan sát thực tế.
    - Loại bỏ mẫu nếu khoảng cách đến điểm thực tế gần nhất vượt quá phân vị 99 ($d_{99} = 0.539$ đơn vị chuẩn).
- Quy trình tạo ra 500000 trạng thái vận hành ứng viên liên tục trên đa tạp dữ liệu thực tế.
- Khoảng cách trung vị đến điểm thực tế gần nhất của tập mẫu đạt $0.121$, tương đương khoảng cách $0.119$ giữa các giờ thực tế.
- Đặc tính này bảo đảm quá trình nội suy phản ánh trung thực các chế độ vận hành khả dĩ của nhà máy.

#### 2.7.3. Định lượng độ bất định dự báo từ tập hợp 100 cây quyết định
- Độ bất định dự báo được định lượng trực tiếp từ độ phân tán kết quả của 100 cây trong mô hình Extra Trees.
- Khoảng tin cậy $95\%$ của các giá trị dự báo đạt mức độ chuẩn xác cao:
  - Khoảng tin cậy của TMP đạt $\pm 0.008\text{ bar}$.
  - Khoảng tin cậy của Flow đạt $\pm 0.17\text{ m}^3/\text{min}$.
  - Khoảng tin cậy của Level đạt $\pm 0.71\%$.
- Biên độ bất định khuyến cáo người vận hành nên đặt điểm làm việc ở vùng lõi của không gian khả thi.
- Vận hành tại vùng lõi giúp hệ thống tránh rủi ro vi phạm ngưỡng do các dao động ngẫu nhiên ngắn hạn.
- Trong số 500000 trạng thái vận hành mô phỏng, có 207238 trạng thái ($41.4\%$) thỏa mãn đồng thời cả 3 mục tiêu.

#### 2.7.4. Tỷ lệ khả thi có điều kiện (CFR) và giao thức xác định dải khuyến nghị
- Nghiên cứu định nghĩa Tỷ lệ khả thi có điều kiện (Conditional Feasibility Rate - CFR) theo từng biến đầu vào:
  $$\text{CFR}(x) = P(\text{TMP, Flow, Level đạt chuẩn} \mid X = x)$$
- CFR phản ánh xác suất thành công thực tế thay vì mật độ mẫu biểu kiến tại các vùng nhà máy thường vận hành.
- Phân phối mật độ liên tục của các điểm khả thi được ước lượng bằng phương pháp Kernel Density Estimation (KDE):
  - Áp dụng nhân Gauss trơn để khắc phục sự phụ thuộc vào cách chia khoảng của biểu đồ tần số.
  - Độ rộng băng thông được xác định tự động theo quy tắc Scott: $h = n^{-1/(d+4)} \cdot \sigma$.
- Giao thức xác định dải vận hành tối ưu khuyến nghị:
  - Chia toàn bộ dải giá trị của từng thông số thành 10 phân vị (deciles).
  - Chọn dải tối ưu là chuỗi phân vị liên tục rộng nhất có tỷ lệ đạt chuẩn trong khoảng 5% so với mức tối đa.
  - Ràng buộc ngưỡng hỗ trợ thống kê tối thiểu với ít nhất 250 giờ vận hành thực tế đã ghi nhận.
- Bốn trên bảy thông số giữ nguyên cấu trúc dải hẹp, chứng minh sự tồn tại của các điểm tối ưu cục bộ sắc nét.

### 2.8. Chỉ số đánh giá hiệu suất

#### 2.8.1. Các chỉ số thống kê sai số hồi quy (RMSE, R², MAE)
- Nghiên cứu sử dụng 3 chỉ số thống kê bổ trợ để định lượng sai số dự báo của các thuật toán:
  - Căn bậc hai sai số bình phương trung bình (Root Mean Squared Error - RMSE):
    $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
    Chỉ số này phạt nặng các sai số dự báo lớn và nhạy cảm với các điểm ngoại lai cục bộ.
  - Hệ số xác định (Coefficient of Determination - $R^2$):
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
    Chỉ số này đo tỷ lệ phương sai được mô hình giải thích so với giá trị trung bình $\bar{y}$.
  - Sai số tuyệt đối trung bình (Mean Absolute Error - MAE):
    $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
    Chỉ số này đánh giá sai số tuyến tính trên cùng đơn vị đo vật lý của biến mục tiêu.
- Các chỉ số được tính toán độc lập trên từng phân vùng kiểm định để đánh giá tính khái quát hóa của mô hình.

#### 2.8.2. Đánh giá mức độ cải thiện xác suất qua tỷ số chênh (Odds Ratio)
- Tỷ số chênh (Odds Ratio - OR) đo lường mức tăng xác suất đạt chuẩn vận hành khi hệ thống nằm trong dải khuyến nghị:
  $$\text{OR} = \frac{P(\text{Khả thi} \mid \text{Trong dải}) / [1 - P(\text{Khả thi} \mid \text{Trong dải})]}{P(\text{Khả thi} \mid \text{Ngoài dải}) / [1 - P(\text{Khả thi} \mid \text{Ngoài dải})]}$$
- Phân tích tỷ số chênh lượng hóa hiệu quả can thiệp kỹ thuật so với mức vận hành nền 37.1% của toàn trạm:
  - Vận hành trong dải khuyến nghị nâng tỷ lệ đạt đồng thời cả 3 mục tiêu lên mức $61.9\% - 82.4\%$.
  - Trên tập dữ liệu kiểm định giữ lại 3 tháng độc lập, dải vận hành đạt tỷ lệ thành công 61.9% với $\text{OR} = 3.89$.
  - Giá trị $\text{OR} > 1$ chứng minh việc vận hành trong vùng khuyến nghị giúp tăng xác suất đạt chuẩn.

## 3. Kết quả và thảo luận (Results and Discussion)

### 3.1. Hiệu suất dự đoán của mô hình học máy (Machine Learning Model Prediction Performance)

#### 3.1.1. Hiệu suất dự đoán biến mục tiêu đầu ra (Output Prediction Performance)

- **3.1.1.1. Phân cấp khả năng dự đoán và căn cứ lựa chọn biến mục tiêu**:
- Hệ thống MBR công nghiệp yêu cầu dự đoán chính xác ba biến mục tiêu vận hành cốt lõi: áp suất xuyên màng (TMP), lưu lượng nước thấm (Permeate Flow) và mức nước bể màng (Membrane Tank Level).
- Nghiên cứu chủ động loại bỏ chất lượng nước đầu ra (TOC nước thấm) khỏi danh sách biến mục tiêu hồi quy:
  - Thiết bị phân tích TOC trực tuyến có dải đo hẹp $0.03\text{--}1000\text{ ppb}$, thường xuyên vận hành sát ngưỡng phát hiện dưới ($0.03\text{ ppb}$).
  - Màng siêu lọc sợi rỗng (UF PVDF) giữ lại gần như toàn bộ chất rắn lơ lửng và chất hữu cơ phân tử lượng lớn. Tín hiệu đo chủ yếu chứa nhiễu thiết bị.
  - Chất lượng nước thấm trong MBR ngập nước phụ thuộc tính toàn vẹn cơ học của màng (hiện tượng đứt gãy sợi màng gây biến đổi bậc thang), không phải hàm liên tục của các thông số sinh học. Đây là bài toán giám sát tính toàn vẹn màng, không phải bài toán hồi quy liên tục.
  - Ba biến mục tiêu được chọn cho phép người vận hành chủ động điều phối và đánh đổi theo từng chu kỳ giờ.
- Benchmark đánh giá 16 thuật toán học máy thuộc 6 họ mô hình cấu trúc khác nhau:
  - Họ Tuyến tính (Linear): Hồi quy tuyến tính cổ điển (Linear Regression).
  - Họ Tuyến tính chính quy hóa (Regularized Linear): Ridge Regression, Lasso Regression, Elastic Net.
  - Họ Máy vectơ hỗ trợ (Support Vector Machine): SVR với nhân hàm bán kính RBF.
  - Họ Dựa trên cá thể (Instance-based): Thuật toán $k$ láng giềng gần nhất (KNN).
  - Họ Tập hợp cây (Ensemble Tree): Cây quyết định (Decision Tree), Rừng ngẫu nhiên (Random Forest), Cây ngẫu nhiên hóa cực độ (Extra Trees), Bagging, AdaBoost, Gradient Boosting, Hist Gradient Boosting, XGBoost, LightGBM.
  - Họ Mạng nơ-ron nhân tạo (Neural Network): Perceptron đa tầng (MLP).
- Phân cấp khả năng dự đoán hình thành rõ rệt theo trật tự vật lý: TMP đạt độ chính xác cao nhất, tiếp theo là lưu lượng nước thấm, cuối cùng là mức nước bể màng.

- **3.1.1.2. Hiệu suất dự đoán áp suất xuyên màng TMP**:
- Nhóm thuật toán tập hợp cây thể hiện ưu thế vượt trội tuyệt đối trên biến TMP với phân chia ngẫu nhiên ($70:30$ và $80:20$):
  - Thuật toán Extra Trees dẫn đầu toàn diện: $R^2 = 0.988$, $\text{RMSE} = 0.010\text{ bar}$ ($1.0\text{ kPa}$), $\text{MAE} = 0.005\text{ bar}$ ($0.5\text{ kPa}$), độ lệch tổng thể $\Delta R^2 = 0.012$.
  - Thuật toán Bagging đạt vị trí thứ hai: $R^2 = 0.978$, $\text{RMSE} = 0.014\text{ bar}$ ($1.4\text{ kPa}$), $\text{MAE} = 0.006\text{ bar}$ ($0.6\text{ kPa}$), $\Delta R^2 = 0.019$.
  - Thuật toán Random Forest đạt kết quả tương đương: $R^2 = 0.978$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.006\text{ bar}$, $\Delta R^2 = 0.019$.
  - Thuật toán LightGBM bám sát: $R^2 = 0.978$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.008\text{ bar}$, $\Delta R^2 = 0.015$.
  - Thuật toán XGBoost đạt độ chính xác cao: $R^2 = 0.977$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.007\text{ bar}$, $\Delta R^2 = 0.022$.
  - Toàn bộ 5 thuật toán tập hợp hàng đầu đều vượt ngưỡng $R^2 > 0.97$.
- Các thuật toán phi ensemble và phi tuyến đạt hiệu suất khả quan:
  - Hist Gradient Boosting đạt $R^2 = 0.976$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.008\text{ bar}$.
  - Thuật toán KNN đạt $R^2 = 0.969$, $\text{RMSE} = 0.016\text{ bar}$, $\text{MAE} = 0.007\text{ bar}$.
  - Mạng nơ-ron MLP đạt $R^2 = 0.951$, $\text{RMSE} = 0.020\text{ bar}$, $\text{MAE} = 0.011\text{ bar}$.
  - Decision Tree đơn lẻ đạt $R^2 = 0.942$, $\text{RMSE} = 0.022\text{ bar}$, $\text{MAE} = 0.010\text{ bar}$.
  - Gradient Boosting cơ bản đạt $R^2 = 0.937$, $\text{RMSE} = 0.023\text{ bar}$, $\text{MAE} = 0.014\text{ bar}$.
  - SVR nhân RBF đạt $R^2 = 0.893$, $\text{RMSE} = 0.030\text{ bar}$, $\text{MAE} = 0.016\text{ bar}$.
- Các thuật toán tuyến tính và tăng cường yếu thất bại nặng:
  - AdaBoost suy giảm độ chính xác rõ rệt: $R^2 = 0.781$, $\text{RMSE} = 0.042\text{ bar}$, $\text{MAE} = 0.037\text{ bar}$.
  - Linear Regression và Ridge Regression dừng lại ở $R^2 = 0.499$, $\text{RMSE} = 0.064\text{ bar}$, $\text{MAE} = 0.045\text{ bar}$.
  - Elastic Net đạt $R^2 = 0.480$, $\text{RMSE} = 0.065\text{ bar}$, $\text{MAE} = 0.046\text{ bar}$.
  - Lasso Regression đạt $R^2 = 0.440$, $\text{RMSE} = 0.068\text{ bar}$, $\text{MAE} = 0.049\text{ bar}$.
- Cơ chế vật lý củng cố độ chính xác cao của TMP:
  - TMP phản ánh điện trở tắc nghẽn màng lọc trong hệ thống MBR ngập nước.
  - Quá trình tích tụ tắc nghẽn diễn ra liên tục theo nồng độ MLSS, cường độ sục khí khuấy trộn bề mặt và các đặc tính bùn phụ thuộc thời gian lưu bùn (SRT).
  - Tất cả các biến số chi phối chính đều được thu thập trực tiếp và cung cấp đầy đủ vào mô hình học máy.
  - Tín hiệu áp suất hút đo ở phía nước thấm có độ ổn định cao và tỷ số tín hiệu trên nhiễu (SNR) lớn hơn so với cấu hình màng nén áp lực.

- **3.1.1.3. Hiệu suất dự đoán lưu lượng nước sau lọc (Permeate Flow)**:
- Thứ hạng các thuật toán dự đoán lưu lượng thấm tương đồng với TMP nhưng chỉ số $R^2$ giảm nhẹ:
  - Extra Trees tiếp tục dẫn đầu: $R^2 = 0.933$, $\text{RMSE} = 0.066\text{ m}^3\text{/min}$ ($3.96\text{ m}^3\text{/h}$), $\text{MAE} = 0.052\text{ m}^3\text{/min}$ ($3.12\text{ m}^3\text{/h}$), $\Delta R^2 = 0.067$.
  - Thuật toán Bagging đứng thứ hai: $R^2 = 0.910$, $\text{RMSE} = 0.076\text{ m}^3\text{/min}$, $\text{MAE} = 0.059\text{ m}^3\text{/min}$, $\Delta R^2 = 0.076$.
  - Random Forest xếp thứ ba: $R^2 = 0.909$, $\text{RMSE} = 0.077\text{ m}^3\text{/min}$, $\text{MAE} = 0.059\text{ m}^3\text{/min}$, $\Delta R^2 = 0.076$.
  - XGBoost xếp thứ tư: $R^2 = 0.906$, $\text{RMSE} = 0.078\text{ m}^3\text{/min}$, $\text{MAE} = 0.061\text{ m}^3\text{/min}$, $\Delta R^2 = 0.081$.
  - Hist Gradient Boosting hoàn thành top năm: $R^2 = 0.899$, $\text{RMSE} = 0.081\text{ m}^3\text{/min}$, $\text{MAE} = 0.064\text{ m}^3\text{/min}$, $\Delta R^2 = 0.048$.
  - Các thuật toán kế tiếp: LightGBM ($R^2 = 0.898$), KNN ($R^2 = 0.894$), MLP ($R^2 = 0.861$), Gradient Boosting ($R^2 = 0.824$), Decision Tree ($R^2 = 0.785$), SVR ($R^2 = 0.771$).
  - Thuật toán kém hiệu quả: AdaBoost ($R^2 = 0.655$, $\text{RMSE} = 0.150\text{ m}^3\text{/min}$), Linear/Ridge Regression ($R^2 = 0.469$, $\text{RMSE} = 0.185\text{ m}^3\text{/min}$), Elastic Net ($R^2 = 0.435$), Lasso ($R^2 = 0.393$).
- Cơ chế kỹ thuật giải thích sự suy giảm độ chính xác so với TMP:
  - Lưu lượng thấm không chỉ phản ánh mức độ tắc nghẽn màng mà còn phụ thuộc điểm đặt lưu lượng của người vận hành, chu kỳ rửa ngược (backwash) định kỳ và các xung đột thủy lực ngắn hạn.
  - Dữ liệu trung bình theo giờ không thể phản ánh trọn vẹn các dao động thủy lực diễn ra ở quy mô phút.
  - Sục khí gián đoạn tạo ra lực xáo trộn tức thời khiến lưu lượng lọc dao động mạnh. Các đặc trưng sinh học và vận hành theo giờ không cung cấp đủ thông tin để mô hình giải quyết biến động vi mô này.

- **3.1.1.4. Hiệu suất dự đoán mức nước bể màng (Membrane Tank Water Level)**:
- Mức nước bể màng là biến mục tiêu phức tạp nhất trong hệ thống:
  - Extra Trees duy trì vị trí số một: $R^2 = 0.908$, $\text{RMSE} = 0.341\%$, $\text{MAE} = 0.227\%$, $\Delta R^2 = 0.092$.
  - XGBoost xếp vị trí thứ hai: $R^2 = 0.843$, $\text{RMSE} = 0.444\%$, $\text{MAE} = 0.292\%$, $\Delta R^2 = 0.143$.
  - Nhóm thuật toán đạt $R^2 \approx 0.839$: Bagging ($R^2 = 0.839$, $\text{RMSE} = 0.450\%$), Random Forest ($R^2 = 0.839$, $\text{RMSE} = 0.450\%$), Hist Gradient Boosting ($R^2 = 0.839$, $\text{RMSE} = 0.450\%$).
  - LightGBM đạt $R^2 = 0.822$, $\text{RMSE} = 0.473\%$, $\text{MAE} = 0.321\%$.
  - Thuật toán KNN đạt $R^2 = 0.813$, $\text{RMSE} = 0.485\%$, $\text{MAE} = 0.298\%$.
  - Các họ mô hình khác suy giảm sâu: MLP ($R^2 = 0.756$), Gradient Boosting ($R^2 = 0.698$), Decision Tree ($R^2 = 0.650$), SVR ($R^2 = 0.498$), AdaBoost ($R^2 = 0.308$).
  - Nhóm tuyến tính hoàn toàn mất khả năng dự đoán: Linear Regression và Ridge Regression chỉ đạt $R^2 = 0.195$ ($\text{RMSE} = 1.006\%$), Elastic Net đạt $R^2 = 0.159$, Lasso đạt $R^2 = 0.117$.
- Căn nguyên vật lý chi phối trật tự dự đoán:
  - TMP dễ dự đoán nhất ($R^2 = 0.988$) do tích lũy trở lực tắc nghẽn qua nhiều giờ đến nhiều ngày. Các biến điều khiển chính như SRT và MLSS biến thiên chậm và được đo đạc chính xác.
  - Lưu lượng nước thấm có mức độ dự đoán trung gian ($R^2 = 0.933$) vì phụ thuộc một phần vào trạng thái màng và một phần vào nhu cầu sản xuất, chu kỳ rửa ngược cùng dao động thủy lực ngắn hạn.
  - Mức nước bể màng khó dự đoán nhất ($R^2 = 0.908$) vì đây là trạng thái thủy lực phản ứng nhanh. Mức nước bị chi phối bởi cân bằng tức thời giữa lưu lượng nước cấp đầu vào, lưu lượng hút màng, tuần hoàn nội bộ, xả bùn dư và thuật toán bật tắt bơm theo mức nước. Các quá trình này diễn ra theo từng phút và không nằm trong tập biến đầu vào của mô hình.
- Giá trị ứng dụng thực tiễn:
  - Mô hình học máy phù hợp nhất cho việc lập kế hoạch kiểm soát TMP dài hạn. Ngược lại, mức nước bể màng cần được xử lý thông qua các cơ chế điều khiển nhanh.
  - Mặc dù vậy, sai số tuyệt đối của Extra Trees ($\text{MAE} = 0.227\%$) vẫn nằm sâu bên trong biên độ kiểm soát cho phép $2.0\%$ của nhà máy, đáp ứng yêu cầu vận hành thực tế.

---

#### 3.1.2. So sánh mô hình, tính nhất quán và kiểm định độc lập (Model Comparison, Consistency and Independent Validation)

- **3.1.2.1. Phân kỳ bản chất giữa mô hình tuyến tính và phi tuyến**:
- Kết quả thực nghiệm tạo ra khoảng cách lớn và có hệ thống giữa mô hình tuyến tính và phi tuyến trên cả ba biến mục tiêu:
  - Mô hình tuyến tính cổ điển (Linear Regression) và Ridge Regression chỉ đạt $R^2 = 0.499$ cho TMP, $0.469$ cho lưu lượng và $0.195$ cho mức nước bể màng.
  - Các biến thể chính quy hóa như Elastic Net ($R^2 = 0.480, 0.435, 0.159$) và Lasso ($R^2 = 0.440, 0.393, 0.117$) suy giảm thêm do hệ số phạt loại bỏ các thông số hồi quy có giá trị thông tin nhỏ.
  - Ngược lại, các mô hình ensemble hàng đầu đều vượt ngưỡng $R^2 > 0.90$ trên cả ba mục tiêu.
- Thử nghiệm giả thuyết có cấu trúc chứng minh cơ chế vận hành sinh học:
  - Thất bại của nhóm mô hình cộng tính tuyến tính cùng với thành công của thuật toán phân vùng đệ quy khẳng định mối quan hệ giữa sinh khối bùn và màng lọc bị chi phối bởi các ngưỡng giới hạn (thresholds) và tương tác phi tuyến (interactions).
  - Hiện tượng này hoàn toàn phù hợp với lý thuyết tắc nghẽn màng. Điện trở lớp bánh bùn tăng vọt phi tuyến khi vượt nồng độ MLSS tới hạn. Hiệu quả sục khí suy giảm dần khi vượt vận tốc xáo trộn tới hạn. Tỷ lệ F/M và SRT tương tác phi cộng tính lên trạng thái bùn.

- **3.1.2.2. So sánh giữa các họ thuật toán Ensemble và phi tuyến**:
- Trong họ Ensemble, các biến thể đóng bao ngẫu nhiên (Bagging, Random Forest, Extra Trees) luôn vượt trội hơn các mô hình tăng cường tuần tự (Sequential Boosting):
  - Tuy nhiên, XGBoost ($R^2 = 0.977$) và LightGBM ($R^2 = 0.978$) đạt hiệu suất tiệm cận Bagging trên biến TMP.
  - Ngược lại, AdaBoost thể hiện hiệu suất kém nhất trên mọi biến mục tiêu ($R^2 = 0.781$ cho TMP, $0.655$ cho lưu lượng, $0.308$ cho mức nước). Cơ chế gán trọng số thích nghi của AdaBoost rất nhạy cảm với dị thường cảm biến và nhiễu ngẫu nhiên trong dữ liệu SCADA công nghiệp.
  - Extra Trees vượt qua Random Forest nhờ kỹ thuật ngẫu nhiên hóa bổ sung các ngưỡng phân chia tại mỗi nút cây. Kỹ thuật này giúp giảm phương sai mô hình hiệu quả hơn khi xử lý tín hiệu cảm biến thực địa.
- Đánh giá các mô hình phi cây:
  - Thuật toán KNN đạt hiệu suất cao ($R^2 = 0.969$ cho TMP, $0.894$ cho lưu lượng, $0.813$ cho mức nước). Kết quả chứng minh phản ứng của màng lọc có tính quy luật trơn đều cục bộ trong không gian vận hành. Đặc tính này là tiền đề toán học giúp việc thiết lập không gian vận hành tối ưu trở nên khả thi và có ý nghĩa.
  - Cây quyết định đơn lẻ (Decision Tree) xảy ra hiện tượng quá khớp (overfitting) nghiêm trọng đối với biến mức nước bể màng: $R^2$ tập huấn luyện đạt $0.890$ nhưng giảm mạnh xuống $0.650$ trên tập kiểm tra độc lập.
  - Phân tích độ bền vững qua 20 lần phân chia ngẫu nhiên lặp lại xác nhận Extra Trees duy trì vị trí dẫn đầu với $R^2$ trung bình cao nhất cùng RMSE và MAE thấp nhất trên cả ba biến đầu ra.

- **3.1.2.3. Kiểm định độc lập trên nhánh màng song song B (Cross-Train Validation)**:
- Khả năng chuyển giao mô hình được kiểm định trên hệ thống màng độc lập gồm 4593 bản ghi theo giờ từ nhánh màng B song song trong cùng nhà máy:
  - Nhánh màng B vận hành dưới điều kiện dòng vào độc lập và có lịch sử tắc nghẽn màng riêng biệt so với nhánh màng A.
  - Mô hình Extra Trees được huấn luyện trên dữ liệu ban đầu và áp dụng trực tiếp lên nhánh màng B mà không cần tái huấn luyện trọng số.
- Kết quả kiểm định xuyên nhánh đạt độ chính xác cao:
  - Áp suất xuyên màng TMP: $R^2 = 0.996$, độ lệch chuẩn sai số đạt $0.014\text{ bar}$ ($1.4\text{ kPa}$).
  - Lưu lượng nước thấm: $R^2 = 0.980$, độ lệch chuẩn sai số đạt $0.052\text{ m}^3\text{/min}$.
  - Mức nước bể màng: $R^2 = 0.972$, độ lệch chuẩn sai số đạt $0.306\%$.
  - Sai số dự đoán trung bình trên cả ba biến mục tiêu đều tiệm cận giá trị 0.
- Đặc tính phân phối sai số của TMP:
  - Phân phối sai số TMP lệch phải nhẹ với hệ số bất đối xứng $\text{skewness} = 1.025$.
  - Hiện tượng này phản ánh xu hướng đánh giá thấp nhẹ giá trị TMP trong các tình huống tắc nghẽn nghiêm trọng cực đoan.
  - Về mặt kỹ thuật, xu hướng này mang tính bảo thủ an toàn vì kích hoạt chu kỳ rửa màng sớm hơn thời điểm tắc nghẽn thực tế, bảo vệ an toàn cho sợi màng.
- Khẳng định tính bất biến vật lý của mô hình:
  - Nhánh màng B chạy song song cùng khoảng thời gian lịch và dùng chung nguồn nước thải đầu vào. Kiểm định này xác lập khả năng chuyển giao xuyên nhánh màng thay vì chuyển giao theo thời gian.
  - Mô hình đã học được quy luật thủy lực và sinh học nền tảng, không bị phụ thuộc vào đặc tính cơ khí cục bộ của từng cụm module màng.

- **3.1.2.4. Tính nhất quán xếp hạng và căn cứ lựa chọn mô hình thống nhất**:
- Extra Trees chứng minh tính nhất quán vượt trội khi giữ vững vị trí số một trên cả ba biến mục tiêu (TMP, lưu lượng thấm, mức nước bể màng) qua toàn bộ các bài kiểm tra:
  - Dẫn đầu trên tập kiểm tra ngẫu nhiên ban đầu.
  - Dẫn đầu trong đánh giá độ bền vững 20 lần phân chia lặp lại.
  - Dẫn đầu trong kiểm định chuyển giao xuyên nhánh màng song song B.
- Nghiên cứu quyết định chọn duy nhất mô hình Extra Trees cho các phân tích khả năng diễn giải SHAP (Mục 3.2) và tối ưu hóa không gian vận hành (Mục 3.3).
- Việc dùng chung một cấu trúc mô hình cho cả ba biến mục tiêu đảm bảo tính nhất quán toán học của khung vận hành và giúp so sánh tầm quan trọng đặc trưng một cách đồng bộ.

---

#### 3.1.3. Độ bền vững của việc lựa chọn mô hình đối với thiết kế kiểm định (Robustness of Model Selection to Validation Design)

- **3.1.3.1. Đánh giá độ bền vững qua bốn thiết kế kiểm định độc lập**:
- Để ngăn ngừa sai lệch từ một phép chia dữ liệu duy nhất, nghiên cứu kiểm tra Extra Trees trên bốn thiết kế kiểm định độc lập:
  - Phân chia ngẫu nhiên truyền thống ($70:30$ và $80:20$).
  - Phân chia theo khối thời gian liên tục 24 giờ (Blocked partition 24-h).
  - Phân chia theo trình tự thời gian chặt chẽ (Chronological partition).
  - Kiểm định độc lập trên nhánh màng song song B.
- Kết quả khẳng định tính vững chắc của mô hình:
  - Extra Trees xếp hạng nhất trong 8 trên 9 tổ hợp mô hình - thiết kế - biến mục tiêu.
  - Extra Trees giữ vị trí số một tuyệt đối cho mọi biến mục tiêu dưới cả thiết kế ngẫu nhiên và thiết kế phân chia khối 24 giờ.
- Tính bất biến của kết luận công nghệ:
  - Thời gian lưu bùn (SRT) luôn duy trì vị trí tác nhân chi phối số một đối với TMP và mức bể màng trên toàn bộ các chế độ kiểm định: phân chia ngẫu nhiên, phân chia khối 24 giờ, phân chia khối 168 giờ (1 tuần), và phân chia theo trình tự thời gian.
  - Kết luận này chứng minh các phát hiện cơ chế là đặc tính vật lý khách quan của nhà máy MBR, không phải kết quả ngẫu nhiên của một phương pháp chia tập dữ liệu.

- **3.1.3.2. Kiểm định phân chia khối thời gian 24 giờ (Blocked Partition 24-h)**:
- Dữ liệu cảm biến SCADA thu thập theo từng giờ vốn có tính tự tương quan chuỗi thời gian cao. Thiết kế phân chia khối 24 giờ phân bổ các khối giờ liên tục làm đơn vị nguyên vẹn để kiểm soát rò rỉ thông tin lân cận.
- Extra Trees duy trì độ chính xác cao đối với hệ thống công nghiệp quy mô đầy đủ:
  - TMP đạt $R^2 = 0.830$, tương ứng $\text{RMSE} = 0.036\text{ bar}$ ($3.6\text{ kPa}$) trên tổng dải vận hành thực tế rộng $0.43\text{ bar}$.
  - Sai số tuyệt đối trung bình $\text{MAE}$ chỉ chiếm $16.3\%$ khoảng tứ phân vị (IQR) của chuỗi đo thực tế.
- Kết quả chứng minh mô hình học được động lực học thực chất của quá trình lọc màng, không đơn thuần dự đoán dựa vào hiện tượng tự tương quan giữa các giờ liền kề.

- **3.1.3.3. Kiểm định ngoại suy ngoài thời gian (Out-of-Time Chronological Validation)**:
- Kiểm định theo trình tự thời gian mô phỏng kịch bản triển khai trong thực tế sản xuất:
  - Kịch bản thông thường huấn luyện mô hình một lần trên 7 tháng đầu và áp dụng cố định (đóng băng mô hình) cho 4 tháng tiếp theo (120 ngày liên tục).
  - Mô hình đóng băng hoàn toàn thất bại do màng lọc bị lão hóa tự nhiên, bùn hoạt tính biến đổi theo mùa và xuất hiện hiện tượng trôi dạt phân phối dữ liệu (data drift).
- Tính khả thi về chi phí tính toán:
  - Mỗi bản ghi mới được cập nhật vào hệ thống lưu trữ SCADA Historian theo từng giờ.
  - Thời gian huấn luyện lại thuật toán Extra Trees trên toàn bộ tập dữ liệu lịch sử tích lũy chỉ mất khoảng $1\text{ giây}$.
  - Do đó, việc tái huấn luyện định kỳ hoàn toàn khả thi và không gây áp lực tài nguyên phần cứng.

- **3.1.3.4. Chiến lược tái huấn luyện định kỳ trong triển khai thực tế**:
- Hiệu suất ngoại suy ngoài thời gian cải thiện tăng dần đều khi rút ngắn chu kỳ tái huấn luyện mô hình.
- Hiệu quả của chiến lược tái huấn luyện hàng ngày (Daily Refit):
  - Áp dụng trên $30\%$ dữ liệu ngoài thời gian được giữ lại (4 tháng cuối), mô hình Extra Trees tái huấn luyện hàng ngày đạt:
    - TMP: $R^2 = 0.871$, sai số tuyệt đối giảm xuống $\text{RMSE} = 0.008\text{ bar}$ ($0.8\text{ kPa}$). Mức sai số này giảm $80\%$ so với mô hình đóng băng cố định.
    - Mức nước bể màng: $R^2 = 0.580$.
    - Lưu lượng nước thấm: $R^2 = 0.574$.
- Hàm ý triển khai công nghiệp:
  - Khả năng tổng quát hóa theo thời gian của mô hình học máy phụ thuộc vào lịch trình cập nhật dữ liệu, không phải giới hạn nội tại của thuật toán.
  - Khuyến nghị vận hành tiêu chuẩn: các nhà máy xử lý nước thải công nghiệp cần tái huấn luyện mô hình tối thiểu mỗi tuần một lần, và ưu tiên thiết lập chu kỳ tái huấn luyện hàng ngày tự động khi hệ thống SCADA Historian cho phép.

### 3.2. Phân tích khả năng diễn giải quá trình (Process Interpretability Analysis)

#### 3.2.1. Đồng thuận và phân kỳ tầm quan trọng đặc trưng giữa các mô hình (Consensus & Divergence)

- **3.2.1.1. Đồng thuận tuyệt đối về vai trò của thời gian lưu bùn (SRT)**:
- Phân tích 48 hồ sơ SHAP: Nghiên cứu áp dụng SHAP cho $16$ mô hình trên $3$ biến mục tiêu (TMP, lưu lượng thấm, mực nước bể màng). Tổng số hồ sơ tầm quan trọng đặc trưng đạt $48$ (Hình 6A1–3).
- Đồng thuận tuyệt đối về TMP: $100\%$ ($16/16$) mô hình trên $6$ họ thuật toán đều xếp thời gian lưu bùn (SRT) ở vị trí số một với điểm số nhất quán tuyệt đối ($1.00$). Tỷ trọng đóng góp SHAP của SRT chiếm trên $40\%\text{--}50\%$ tổng độ quan trọng.
- Đồng thuận về mực nước bể màng: $15/16$ mô hình xếp SRT ở vị trí số một với thứ hạng trung bình đạt $1.07 \pm 0.25$. Mô hình mạng perceptron đa tầng (MLP) là ngoại lệ duy nhất.
- Thứ hạng lưu lượng thấm: Thứ hạng của biến lưu lượng thấm phân tán hơn giữa các thuật toán. Thời gian lưu thủy lực (HRT) đứng đầu ở $7/16$ mô hình với thứ hạng trung bình $2.28 \pm 1.39$. Biến SRT đạt thứ hạng trung bình $4.67 \pm 1.89$.
- Bản chất nội tại của dữ liệu: Sự hội tụ này chứng minh vai trò chi phối của SRT là thuộc tính vật lý của dữ liệu vận hành. Kết quả không phụ thuộc vào thiên kiến quy nạp (inductive bias) của bất kỳ thuật toán riêng lẻ nào.
- Tính vững chắc qua kiểm định: SRT giữ vị trí số một cho TMP và mực nước dưới mọi cấu hình chia dữ liệu. Thứ hạng này bảo toàn trong các thử nghiệm Blocked 24 h, Blocked 168 h và kiểm định theo thời gian. Thứ hạng duy trì ổn định ngay cả khi độ chính xác dự báo suy giảm.

- **3.2.1.2. Phân kỳ mô hình và nguồn gốc sai lệch phương pháp luận**:
- Phân kỳ tại các biến thứ cấp: Các mô hình họ cây (Extra Trees, Random Forest, XGBoost) xếp tỷ lệ C/N ở vị trí cuối cùng đối với TMP. Ngược lại, các mô hình tuyến tính xếp C/N ở vị trí thứ ba hoặc cao hơn.
- Phân kỳ về lưu lượng sục khí: Lưu lượng sục khí đứng vị trí số một đối với lưu lượng thấm dưới phương pháp KernelSHAP. Biến này đứng thứ tư dưới phương pháp TreeSHAP.
- Cơ chế sai lệch của KernelSHAP: KernelSHAP ước tính giá trị Shapley qua các liên minh đặc trưng ngẫu nhiên. Phương pháp này phân bổ sai lệch khi các biến đầu vào có hiện tượng đa cộng tuyến.
- Cơ chế chính xác của TreeSHAP: TreeSHAP khai thác cấu trúc phân nhánh cây quyết định và phân bố điều kiện thực tế. Phương pháp này tính toán chính xác khi các biến có tương quan mạnh.
- Hiện tượng đồng biến giữa khí sục và HRT: Lưu lượng khí sục tăng cao trong các chu kỳ tải trọng lớn. Chu kỳ tải cao đồng thời nén ngắn thời gian lưu thủy lực HRT. KernelSHAP gộp một phần đóng góp của HRT vào lưu lượng khí.
- Lựa chọn mô hình chuẩn: Nghiên cứu sử dụng kết quả giải thích của Extra Trees làm chuẩn cho phân tích cơ chế vật lý.

#### 3.2.2. Diễn giải cơ chế của các nhân tố chi phối chính (Mechanistic Interpretation)

- **3.2.2.1. Nghịch lý SRT trong vùng vận hành hiếu khí kéo dài**:
- Dải vận hành SRT thực tế: Hệ thống MBR xử lý nước thải bán dẫn vận hành trong dải SRT từ $43.3$ đến $108.3\text{ ngày}$. Toàn bộ dải vận hành nằm trong chế độ hiếu khí kéo dài (extended-aeration).
- Phân bố giá trị SHAP của Extra Trees: Giá trị SHAP dương trong khoảng SRT $45\text{--}75\text{ ngày}$ (Hình 6B1, Hình S9). Giá trị SHAP giảm mạnh qua ngưỡng $90\text{ ngày}$. Chỉ số đạt mức $-0.3$ đến $-2.0$ tại dải $100\text{--}108\text{ ngày}$.
- Nghịch lý so với nước thải sinh hoạt: Y văn truyền thống xác định kéo dài SRT dưới $30\text{--}40\text{ ngày}$ giúp giảm tắc nghẽn màng. Cơ chế giảm tắc nhờ hô hấp nội bào tiêu thụ polymer ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP).
- Cạn kiệt lợi thế giảm SMP: Mức SRT thấp nhất tại nhà máy ($43.3\text{ ngày}$) đã vượt xa ngưỡng trên. Lợi ích phân hủy sinh học EPS và SMP đã cạn kiệt hoàn toàn.
- Suy giảm đơn điệu ở dải SRT siêu dài: Khi SRT tăng từ $45$ lên $108\text{ ngày}$, lưu lượng xả bùn giảm. Hiện tượng này làm tích tụ sinh khối và làm tăng nồng độ bùn hoạt tính (MLSS).

- **3.2.2.2. Cơ chế tích tụ sinh khối và chất rắn trơ bán dẫn đặc thù**:
- Gia tăng độ nhớt và tính nén của bánh bùn: Lượng bùn xả thấp làm tăng độ nhớt biểu kiến của hỗn dịch bùn. Lớp bánh bùn trên bề mặt màng dày hơn và có độ nén ép cao hơn.
- Áp đảo hiệu ứng hòa tan: Sự gia tăng độ nhớt và trở lực bánh bùn ($R_c$) áp đảo hoàn toàn lượng giảm nhỏ của SMP dư. Hiện tượng này làm áp suất xuyên màng TMP tăng vọt.
- Tích tụ hạt trơ và hóa chất quang khắc: SRT kéo dài giữ lại các hạt mài siêu mịn silica từ nước thải CMP. Bông bùn tích tụ hợp chất khó phân hủy từ chất quang khắc (photoresist) và dung dịch tẩy rửa.
- Hấp phụ chọn lọc lên màng PVDF: Các hợp chất kỵ nước khó phân hủy bám dính lên bề mặt màng sợi rỗng PVDF. Lớp bám tạo thành lớp cặn đặc chắc và khó loại bỏ bằng rửa thủy lực.
- Tác động lên lưu lượng và mực nước: Độ nhớt bùn cao làm tăng lực cản thủy lực nội tại, làm giảm lưu lượng thấm. Đồng thời, mực nước bể màng tăng đơn điệu theo thời gian lưu bùn SRT.

- **3.2.2.3. Vùng chuyển tiếp tới hạn tại ngưỡng 80–90 ngày**:
- Vùng chuyển tiếp phân tán rộng: Đồ thị phụ thuộc SHAP ghi nhận dải phân tán rộng trong khoảng SRT từ $80$ đến $90\text{ ngày}$.
- Trạng thái điều kiện hóa: Tại vùng $80\text{--}90\text{ ngày}$, tác động của SRT phụ thuộc mạnh vào các biến vận hành đi kèm. Các quyết định điều khiển vận hành quyết định trạng thái tắc nghẽn màng.
- Tương tác bậc hai HRT $\times$ SRT: Hệ số ghép cặp tương tác giữa HRT và SRT đạt giá trị $0.056$ (Hình S8B1).
- Cơ chế bù trừ tại HRT ngắn: Khi HRT ngắn, thông lượng nước qua bể lớn bù trừ một phần tác động tiêu cực của SRT cao.
- Cơ chế cộng gộp tiêu cực: Khi HRT vượt $9\text{ giờ}$ kết hợp với SRT trên $90\text{ ngày}$, hai yếu tố cộng gộp làm tăng vọt TMP.

#### 3.2.3. Tác động của thông số thủy lực và sục khí (Hydraulic & Aeration Effects)

- **3.2.3.1. Vai trò kiểm soát kép của thời gian lưu thủy lực (HRT)**:
- Thứ hạng của HRT: HRT đứng thứ hai đối với TMP ($2.33 \pm 0.47$) và đứng đầu đối với lưu lượng thấm trong các mô hình họ cây.
- Vai trò kiểm soát kép: HRT vừa kiểm soát tải trọng hữu cơ thể tích, vừa giới hạn công suất thủy lực của hệ thống.
- Dải tác động của HRT lên TMP: Mức HRT ngắn $6\text{--}7\text{ giờ}$ tạo đóng góp SHAP dương cho TMP. Đóng góp SHAP giảm đều khi HRT vượt $7\text{ giờ}$, đạt mức $-1.3$ đến $-2.2$ tại $10\text{--}11\text{ giờ}$.
- Ba cơ chế thực tế vận hành: Lý thuyết truyền thống cho rằng HRT ngắn để lại nhiều SMP dư gây tắc màng. Ba yếu tố vận hành thực tế tại nhà máy tạo nên kết quả ngược lại:
  1. Pha loãng nước thải: HRT ngắn xảy ra trong giai đoạn sản xuất bán dẫn cao điểm khi nước thải loãng hơn.
  2. Tích tụ sinh khối: Chu kỳ HRT dài trên $9\text{ giờ}$ trùng với giai đoạn giảm xả bùn, gây tích tụ sinh khối.
  3. Tần suất rửa màng: Hệ thống điều khiển tăng tần suất súc rửa ngược và chu kỳ nghỉ khi nhà máy chạy công suất cao.
- Đáp ứng phi đơn điệu của lưu lượng thấm: Lưu lượng thấm đạt cực đại tại khoảng HRT $6.5\text{--}7.5\text{ giờ}$. Khi vượt ngưỡng này, trần thủy lực giới hạn thông lượng tối đa do thể tích bể cố định ($HRT = V/Q$).

- **3.2.3.2. Cơ chế cắt thủy động lực và hiện tượng bão hòa sục khí**:
- Thứ hạng của lưu lượng khí sục: Khí sục đứng thứ hai đối với mực nước ($0.216$), thứ ba đối với lưu lượng, nhưng chỉ đứng thứ sáu đối với TMP ($0.063$).
- Cơ chế bất đối xứng: Khí sục tạo lực cắt thủy động lực trên bề mặt màng. Lực cắt chi phối trực tiếp các đại lượng thủy lực dòng chảy và mực nước.
- Giới hạn của lực cắt khí: Ngược lại, TMP còn chịu kiểm soát bởi hiện tượng nghẹt lỗ xốp sâu và hấp phụ hóa học mà lực cắt không thể bóc tách.
- Đáp ứng phi đơn điệu của TMP với khí sục: Khi lưu lượng khí dưới $5000\text{ m}^3\text{/h}$, lực cắt không đủ làm lớp bánh bùn phát triển mất kiểm soát. Tăng khí sục từ $3500$ lên $5000\text{ m}^3\text{/h}$ giúp giảm nhanh TMP.
- Phân nhánh và bão hòa trên $6500\text{ m}^3\text{/h}$: Khi vượt $6500\text{ m}^3\text{/h}$, đáp ứng chia nhánh và hiệu quả chống tắc nghẽn bị bão hòa hoàn toàn.
- Giới hạn vật lý của bánh bùn: Sục khí mạnh chỉ có tác dụng khi bánh bùn còn mềm và xốp. Khi SRT dài và MLSS cao đã nén chặt lớp bánh bùn, khí sục không còn hiệu quả.
- Tác hại của sục khí quá mức: Sục khí quá mức còn làm vỡ bông bùn thành các hạt keo mịn, gây tắc nghẽn sâu trong lỗ màng.
- Tương tác Air $\times$ SRT lên mực nước: Hệ số tương tác đạt $0.1318$ (giá trị ngoài đường chéo lớn nhất trong ma trận SHAP, Hình S8B3). Hiệu quả của sục khí tăng mạnh ở SRT ngắn nhưng suy giảm rõ rệt ở SRT dài.

- **3.2.3.3. Tương quan nghịch biểu kiến giữa sục khí và lưu lượng thấm**:
- Tương quan nghịch biểu kiến: Dữ liệu quan sát cho thấy lưu lượng khí sục có tương quan nghịch với lưu lượng thấm.
- Bản chất vận hành thực tế: Đây không phải là sự suy giảm thấm do lực cản vật lý. Trong hệ thống MBR chìm hút cưỡng bức, máy bơm hút quy định trực tiếp thông lượng thấm.
- Tương quan phản ánh logic điều khiển: Người vận hành duy trì khí sục thấp khi tải trọng thấp và màng chịu ít áp lực thủy lực. Họ tăng mạnh khí sục để ứng phó khi tải cao hoặc khi màng tắc nghẽn làm giảm lưu lượng.
- Khả năng phân tách của TreeSHAP: TreeSHAP gỡ bỏ tương quan nhiễu này, xếp khí sục ở vị trí thứ tư sau HRT, SRT và C/N.
- Bản chất dữ liệu quan sát: Hiện tượng này là minh chứng cho việc dữ liệu quan sát ghi nhận mối liên kết thống kê chứ không phải quan hệ nhân quả trực tiếp.

#### 3.2.4. Động lực sinh học thứ cấp (Secondary Biological Drivers)

- **3.2.4.1. Nồng độ bùn hoạt tính MLSS và trở lực bánh bùn**:
- Thứ hạng của MLSS: MLSS đứng thứ ba đối với TMP ($3.33 \pm 1.35$) và đứng thứ ba đối với mực nước ($3.87 \pm 1.15$).
- Đáp ứng chữ U ngược đối với TMP: Đóng góp SHAP xấp xỉ $0$ tại dải MLSS $2000\text{--}3000\text{ mg/L}$. Giá trị SHAP đạt cực đại tại khoảng $6000\text{--}6500\text{ mg/L}$. Chỉ số rơi mạnh xuống $-1.5$ khi MLSS vượt $7000\text{--}7500\text{ mg/L}$ do trở lực bánh bùn tăng đột biến.
- Quy luật trở lực bánh bùn: Kết quả phù hợp với định luật tăng gần bậc hai của trở lực bánh bùn theo MLSS trên màng PVDF ($R_c \propto \text{MLSS}^2$).
- Tương tác MLSS $\times$ SRT: Hệ số tương tác đạt giá trị $0.042$.
- Tác động khuếch đại ở SRT ngắn: Hiện tượng tắc bùn khuếch đại ở SRT ngắn vì bùn non chứa nhiều EPS làm tăng độ nén của bánh lọc.

- **3.2.4.2. Tỷ lệ thức ăn trên vi sinh F/M và quá trình tự phân hủy nội bào**:
- Thứ hạng của F/M: Tỷ lệ F/M đứng thứ tư đối với TMP.
- Vùng tối ưu của F/M đối với TMP: Đóng góp SHAP đạt đỉnh tại dải $0.030\text{--}0.035\text{ ngày}^{-1}$. Giá trị SHAP suy giảm ở mức F/M cao hơn do vi sinh vật sản sinh thừa SMP tạo lớp gel nhầy bám màng.
- Đáp ứng chữ U đối với mực nước: Mực nước bể màng tăng dốc đứng khi F/M vượt ngưỡng $0.05\text{ ngày}^{-1}$.
- Cơ chế tự phân hủy ở F/M thấp: Khi F/M giảm dưới $0.02\text{ ngày}^{-1}$, quần thể vi sinh vật thiếu chất dinh dưỡng. Hiện tượng hô hấp nội bào tự phân giải tế bào phóng thích SMP gây tắc nghẽn lỗ xốp màng nghiêm trọng.

- **3.2.4.3. Bổ sung Glucose và tỷ lệ C/N trong nước thải bán dẫn**:
- Thứ hạng và tác động của Glucose: Glucose đứng thứ năm đối với TMP với tác động gián tiếp thông qua MLSS và F/M.
- Nhu cầu châm nguồn carbon: Nước thải bán dẫn giàu nitơ nhưng thiếu hụt carbon hữu cơ cho quá trình khử nitrat sinh học.
- Liều lượng bổ sung Glucose: Châm thiếu glucose làm suy giảm sinh khối vi khuẩn khử nitrat. Châm thừa glucose kích thích vi sinh vật tiết màng nhầy keo tụ polymer ngoại bào (EPS), làm tăng áp suất TMP.
- Thứ hạng của tỷ lệ C/N: C/N đứng thứ bảy đối với TMP trong các mô hình họ cây. Đóng góp SHAP giảm đơn điệu từ giá trị dương ở C/N $5\text{--}7$ xuống $-0.3$ ở dải $14\text{--}16$.
- Cơ chế bất lợi của C/N cao: Môi trường giàu carbon thiếu nitơ kích thích vi sinh vật tiết nhiều polysaccharide trong EPS. Điều kiện này kích thích vi khuẩn dạng sợi phát triển, gây xốp bùn và làm suy giảm khả năng lọc.
- Phân kỳ giữa các họ mô hình: Mô hình tuyến tính xếp C/N ở vị trí thứ ba do hiện tượng đa cộng tuyến với MLSS và F/M. Phân tích đa mô hình giúp nhận diện sai lệch này.

#### 3.2.5. Cấu trúc tương tác và hàm ý phương pháp (Interaction Structure & Implications)

- **3.2.5.1. So sánh độ lệch phương pháp luận giữa TreeSHAP và KernelSHAP**:
- So sánh chín mô hình họ cây và bảy mô hình phi cây: So sánh phân bổ Shapley cho thấy sai lệch có hệ thống về hướng ước tính giữa TreeSHAP và KernelSHAP (Hình S8A).
- Đồng thuận trên mục tiêu TMP: Cả hai phương pháp cùng xác định SRT chiếm ưu thế tuyệt đối (TreeSHAP đạt $0.530$, KernelSHAP đạt $0.458$). Hai phương pháp cùng xếp HRT ở vị trí thứ hai với giá trị $0.143$. Biến MLSS có độ lệch lớn nhất giữa hai phương pháp ($0.144$ so với $0.109$).
- Phân kỳ lớn trên mục tiêu lưu lượng: KernelSHAP xếp khí sục ở vị trí thứ nhất ($0.243$). TreeSHAP xếp khí sục ở vị trí thứ tư ($0.150$), đứng sau HRT ($0.318$), C/N ($0.230$) và F/M ($0.160$).
- Đồng thuận trên mục tiêu mực nước: Cả hai phương pháp cho kết quả thống nhất cao đối với mực nước bể màng.
- Sai lệch hệ thống của KernelSHAP: KernelSHAP phóng đại vai trò của các biến vận hành ngắn hạn dễ điều chỉnh như khí sục. Đồng thời, KernelSHAP đánh giá thấp các biến sinh học biến thiên chậm nhưng chi phối kết quả như SRT và MLSS.
- Khuyến nghị phương pháp: Các nhà vận hành cần sử dụng TreeSHAP để định hướng kiểm soát và điều khiển quy trình MBR thực tế.

- **3.2.5.2. Ma trận tương tác bậc hai và yêu cầu tối ưu hóa đa biến**:
- Cặp tương tác HRT $\times$ SRT: Hệ số ghép nối đạt $0.056$ đối với TMP và đạt $0.0510$ đối với lưu lượng thấm (Hình S8).
- Cặp tương tác MLSS $\times$ SRT: Hệ số ghép nối đạt $0.042$ đối với mục tiêu TMP.
- Cặp tương tác Air $\times$ SRT: Hệ số ghép nối đạt $0.1318$ đối với mục tiêu mực nước bể màng. Đây là giá trị ghép cặp tương tác ngoài đường chéo lớn nhất trong toàn bộ nghiên cứu.
- Bản chất phi cộng gộp: Các mối tương quan phi tuyến chứng minh phương pháp tối ưu hóa đơn biến độc lập sẽ thất bại.
- Yêu cầu kiểm soát đồng thời: Vận hành trạm MBR bắt buộc phải tối ưu hóa đồng thời toàn bộ bảy thông số đầu vào. Phần 3.3 triển khai phương pháp tối ưu hóa đa mục tiêu dựa trên nền tảng tương tác này.

### 3.3. Điều kiện vận hành tối ưu cho MBR xử lý nước thải bán dẫn (Operational Basin)

#### 3.3.1. Từ tầm quan trọng đặc trưng đến không gian vận hành khả thi

- **Giới hạn của SHAP và nguyên lý ánh xạ không gian khả thi**:
- Phân tích SHAP xác lập sự đồng thuận trên 16 thuật toán về chiều tác động của các thông số. SRT chi phối áp suất hút xuyên màng TMP theo hướng đơn điệu. HRT thiết lập trần thủy lực cho lưu lượng nước thấm. Lưu lượng sục khí Air tác động phi tuyến lên TMP với lợi nhuận giảm dần.
- Phân tích SHAP không thể chỉ ra tổ hợp thông số đầu vào để đạt đồng thời cả ba mục tiêu. Phương pháp này cũng không phát hiện được xung đột ràng buộc giữa các biến.
- Khung phương pháp luận giải quyết khoảng trống này bằng cách chuyển đổi độ quan trọng đặc trưng thành dải biên vận hành định lượng. Mô hình Extra Trees ánh xạ không gian khả thi trên đa tạp dữ liệu thực nghiệm.
- Ba tiêu chuẩn ràng buộc vận hành đồng thời gồm:
  - Áp suất hút xuyên màng: $\text{TMP} \in [-0.09, -0.03]\text{ bar}$.
  - Lưu lượng nước thấm lọc qua màng: $Q_{\text{permeate}} \in [1.5, 2.2]\text{ m}^3/\text{min}$.
  - Mức chất lỏng trong bể chứa cụm màng: $H_{\text{tank}} \in [65.0\%, 67.0\%]$.

- **Kỹ thuật lấy mẫu trên đa tạp thực tế (Manifold-Constrained Resampling)**:
- Kỹ thuật lấy mẫu hạt nhân hiệp phương sai cục bộ tạo ra $500{,}000$ trạng thái vận hành ứng viên trên đa tạp dữ liệu thực nghiệm.
- Thuật toán xác định $207{,}238$ trạng thái khả thi, chiếm tỷ lệ $41.4\%$ tổng số mẫu kiểm tra.
- Độ phân tán tập hợp trên 100 cây quyết định Extra Trees xác lập khoảng tin cậy $95\%$:
  - Sai số TMP đạt $\pm 0.008\text{ bar}$.
  - Sai số lưu lượng nước thấm đạt $\pm 0.17\text{ m}^3/\text{min}$.
  - Sai số mức chất lỏng bể màng đạt $\pm 0.71\%$.
- Hệ thống khuyến nghị vận hành sâu bên trong không gian khả thi thay vì vùng biên để phòng ngừa rủi ro vi phạm thủy lực.
- Khoảng cách láng giềng gần nhất trung vị từ điểm mẫu đến dữ liệu thực nghiệm đạt $0.121$ đơn vị chuẩn hóa. Khoảng cách này tương đương giá trị $0.119$ giữa các giờ vận hành thực tế.
- Mọi trạng thái dự báo đều là phép nội suy hợp lý trong không gian nhà máy từng trải qua. Các khuyến nghị đảm bảo tính khả thi vật lý tuyệt đối.
- Cửa sổ vận hành được xếp hạng theo tỷ lệ khả thi có điều kiện (Conditional Feasibility Rate). Phương pháp này ưu tiên vùng trạm đạt hiệu suất cao nhất thay vì vùng trạm lưu lại nhiều thời gian nhất.

- **Cấu trúc tương quan phi tuyến và tương tác giữa các biến vận hành**:
- Không gian vận hành khả thi tạo thành cấu trúc dải hẹp tương quan phi tuyến, không phải hình hộp chữ nhật độc lập.
- Quan hệ đối nghịch trực tiếp xuất hiện giữa MLSS và F/M với hệ số tương quan Pearson $r = -0.791$.
- Quan hệ đồng biến tạo thành dải dốc tăng dần xuất hiện giữa C/N và HRT.
- Giao điểm các dải khuyến nghị đơn lẻ thuộc vùng xác suất cao ($60\% - 100\%$) trong 20 trên 21 cặp biến. Hiệu suất này vượt trội so với mức nền $37.1\%$ của toàn hệ thống.
- Cặp biến SRT và HRT tạo ra tương tác phi cộng gộp duy nhất:
  - Khi xét riêng lẻ, dải tối ưu của SRT ($43.2 - 72.2\text{ ngày}$) và HRT ($5.875 - 6.381\text{ h}$) mang lại tỷ lệ đạt mục tiêu lần lượt là $77.0\%$ và $82.4\%$.
  - Khi kết hợp đồng thời hai dải tối ưu đơn lẻ, hệ thống chỉ ghi nhận 35 giờ vận hành thực tế. Tỷ lệ đạt mục tiêu giảm xuống còn $34.3\%$, thấp hơn mức nền $37.1\%$.
  - Cơ chế kỹ thuật: Khi duy trì SRT trong dải $43.2 - 72.2\text{ ngày}$, trạm thực tế hoạt động ở HRT $6.2 - 7.5\text{ h}$. Dải HRT ngắn $5.9 - 6.4\text{ h}$ chỉ xuất hiện khi tuổi bùn đạt $72 - 108\text{ ngày}$.
  - HRT ngắn đòi hỏi thông lượng nước cao. Việc duy trì thông lượng cao ở tuổi bùn thấp đòi hỏi tốc độ xả bùn hoạt tính (WAS) vượt quá giới hạn thiết bị trạm.
  - Quy tắc điều khiển: Người vận hành không cài đặt SRT và HRT độc lập. Cần cố định biến chậm SRT trước, sau đó xác định HRT phụ thuộc theo SRT.

---

#### 3.3.2. Cấu trúc mật độ của các vùng khả thi (Feasible Windows)

- **Đòn bẩy sinh học và trần thủy lực của hệ thống**:
- Mức nền cơ sở của toàn hệ thống đạt tỷ lệ thỏa mãn đồng thời cả ba mục tiêu là $37.1\%$ ($1703$ trên $4593\text{ giờ}$ SCADA).
- HRT là đòn bẩy thủy lực nhạy nhất của hệ thống:
  - Tỷ lệ khả thi đạt đỉnh $82.8\%$ theo mô hình và $82.4\%$ theo dữ liệu thực tế trong dải $5.88 - 6.38\text{ h}$.
  - Tỷ lệ khả thi giảm đơn điệu về $0\%$ khi $\text{HRT} > 7.95\text{ h}$ trên cả mô hình lẫn số đo thực tế.
  - Cơ chế trần thủy lực: Với thể tích bể hiếu khí cố định ($8604\text{ m}^3$), giá trị $\text{HRT} > 8\text{ h}$ tương ứng với lưu lượng đầu vào quá thấp. Hệ thống không thể đạt mục tiêu lưu lượng nước thấm tối thiểu $1.5\text{ m}^3/\text{min}$.
- SRT chi phối trực tiếp áp suất TMP và tốc độ bám bẩn màng:
  - Tỷ lệ đạt mục tiêu đạt $77.0\%$ trong dải $43.2 - 72.2\text{ ngày}$, so với $32.3\%$ ngoài dải ($p < 0.001$).
  - Tỷ lệ đạt mục tiêu giảm liên tục theo tuổi bùn: $74.5\%$ ($77 - 84\text{ ngày}$), $59.0\%$ ($84 - 86\text{ ngày}$), $18.7\%$ ($87 - 92\text{ ngày}$) và $0\%$ ($> 108\text{ ngày}$).
  - Khuyến nghị vận hành: Giữ SRT dưới $85\text{ ngày}$ và duy trì trong dải mục tiêu $43.2 - 72.2\text{ ngày}$.
  - Ba nguồn bằng chứng độc lập cùng khẳng định dải tối ưu của SRT. Các bằng chứng gồm đồng thuận SHAP trên 16 mô hình, bề mặt khả thi đa tạp và số liệu đo thực tế trạm.

- **Bảng thông số vận hành khuyến nghị theo tỷ lệ đạt mục tiêu**:
- Dưới đây là các dải thông số vận hành tối ưu nhằm đạt đồng thời ba mục tiêu hiệu suất:

| Thông số | Đơn vị | Dải quan sát thực tế | Dải khuyến nghị (dựa trên tỷ lệ) | Tỷ lệ đạt mục tiêu trong / ngoài dải (%) | Hướng dẫn vận hành và hiệu quả kiểm định giữ lại |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SRT** | ngày | $43.3 - 108.4$ | $43.2 - 72.2$ | $77.0 \text{ / } 32.3$ | Giữ dưới $85\text{ ngày}$. Hướng tới $43.2 - 72.2\text{ ngày}$. Tỷ lệ đạt giảm xuống $< 20\%$ khi $> 87\text{ ngày}$. Mức tăng chuyển giao giữ lại ngoài thời gian đạt $+22.7\text{ pp}$. |
| **HRT** | h | $5.875 - 11.042$ | $5.875 - 6.381$ | $82.4 \text{ / } 32.1$ | Vận hành trong dải $5.9 - 6.4\text{ h}$. Tỷ lệ đạt giảm về $0\%$ khi $> 7.95\text{ h}$ do trần thủy lực giới hạn lưu lượng nước thấm. |
| **Air** | $\text{m}^3/\text{h}$ | $4470 - 7272$ | $4868 - 5892$ | $61.1 \text{ / } 34.4$ | Giữ trong dải $4868 - 5892\text{ m}^3/\text{h}$. Cung cấp đủ lực cắt bề mặt cho TMP mà không rơi vào chế độ sục khí phản ứng quá mức khi tải cao. |
| **MLSS** | mg/L | $1918 - 7630$ | $5580 - 6138$ | $67.6 \text{ / } 29.5$ | Vận hành trong dải $5580 - 6138\text{ mg/L}$. Đạt mức tăng chuyển giao ngoài thời gian cao nhất trong các đòn bẩy ($+30.9\text{ pp}$). |
| **C/N** | – | $4.80 - 17.52$ | $4.80 - 7.51$ | $55.0 \text{ / } 32.6$ | Biến giám sát, không phải điểm đặt cố định. Dải thuận lợi $4.80 - 7.51$ (vai phụ $11.3 - 12.9$ đạt $50.5\%$). Cần tái ước lượng định kỳ theo lịch xả bán dẫn. |
| **F/M** | $\text{ngày}^{-1}$ | $0.0117 - 0.0658$ | $0.0233 - 0.0252$ | $68.3 \text{ / } 33.5$ | Giữ dưới $\approx 0.03\text{ ngày}^{-1}$. Tăng xả bùn WAS đón đầu các chu kỳ xả thải hữu cơ cao. Chuyển giao ngoài thời gian tăng $+15.7\text{ pp}$. |
| **Glu** | L/min | $0.402 - 1.352$ | $0.705 - 1.352$ | $59.8 \text{ / } 31.3$ | Đòn bẩy có điều kiện, châm để duy trì cân bằng C/N. Không phải mục tiêu tối ưu hóa độc lập. |

- **Động lực học sục khí và nồng độ sinh khối**:
- Lưu lượng sục khí Air tối ưu hóa ứng suất cắt bề mặt màng:
  - Tỷ lệ đạt mục tiêu cao nhất đạt $61.1\%$ trong dải $4868 - 5892\text{ m}^3/\text{h}$. Tỷ lệ này giảm xuống $17.2\%$ khi khí sục vượt $6356\text{ m}^3/\text{h}$.
  - Áp suất TMP đạt điểm tối ưu tại dải khí sục $5500 - 6000\text{ m}^3/\text{h}$, nơi ứng suất cắt duy trì tính linh động của bánh bùn. Khí sục cao hơn không mang lại lợi ích giảm TMP.
  - Tương quan âm giữa khí sục và lưu lượng nước thấm đạt $r = -0.410$. Mối tương quan này xuất phát từ logic điều khiển khi tải cao, không do suy giảm thủy lực.
- Nồng độ bùn hoạt tính MLSS quyết định trở lực dòng thấm:
  - Tỷ lệ đạt mục tiêu tạo đường cong chữ U ngược: tăng từ $3.9\%$ ($< 3590\text{ mg/L}$) lên cực đại $67.6\%$ ($5580 - 6138\text{ mg/L}$ với $918\text{ giờ}$ ghi nhận), sau đó giảm xuống $25.1\%$ ($> 6138\text{ mg/L}$).
  - MLSS thấp làm giảm hiệu quả xử lý sinh học. MLSS cao làm tăng độ nhớt bùn và gây tắc nghẽn màng nghiêm trọng.
- Tải trọng hữu cơ F/M chi phối lớp gel sinh học:
  - Tỷ lệ đạt mục tiêu đạt cực đại $68.3\%$ trong dải $0.0233 - 0.0252\text{ ngày}^{-1}$, so với $15.0\%$ khi $\text{F/M} > 0.0373\text{ ngày}^{-1}$.
  - F/M cao kích thích vi sinh vật tiết các sản phẩm vi sinh hòa tan (SMP), đẩy nhanh quá trình bám bẩn lớp gel trên màng sợi rỗng.
  - Hướng dẫn vận hành: Khống chế $\text{F/M} < 0.03\text{ ngày}^{-1}$. Chủ động xả bùn khi hệ thống quản lý sản xuất báo trước chu kỳ xả thải hữu cơ cao.
- Tỷ lệ C/N và lưu lượng châm glucose Glu phản ánh chế độ xả thải hóa chất:
  - Tỷ lệ đạt mục tiêu của C/N đạt đỉnh $55.0\%$ tại dải $4.80 - 7.51$ và đỉnh phụ $50.5\%$ tại dải $11.3 - 12.9$. Cấu trúc hai đỉnh tương ứng với nước thải bóc tách photoresist giàu carbon và nước rửa khắc axit giàu nitơ.
  - Glucose đóng vai trò nguồn carbon ngoại sinh để ổn định C/N (dải tối ưu $0.705 - 1.352\text{ L/min}$, đạt $59.8\%$), tương quan rất yếu với F/M.

- **Kiểm chứng định lượng giữa dự báo mô hình và dữ liệu thực tế**:
- Mô hình được kiểm chứng đối đầu trên 70 khoảng bin phân vị thập phân (deciles) của 7 thông số đầu vào.
- Hệ số tương quan Pearson giữa tỷ lệ dự báo và tỷ lệ thực đo đạt $r = 0.988$ ($p = 9 \times 10^{-57}$).
- Hệ số tương quan hạng Spearman đạt $\rho = 0.984$.
- Độ lệch tuyệt đối trung bình (MAD) giữa dự báo và thực tế đạt $4.3$ điểm phần trăm.
- Sai số lạc quan hệ thống rất nhỏ, chỉ $+4.2$ điểm phần trăm. Hệ số tương quan trên từng biến dao động trong khoảng $r = 0.96 - 0.998$.
- Kết quả khẳng định mô hình tái lập chính xác tần suất đạt mục tiêu của trạm thực tế mà không cần căn chỉnh tham số.

---

#### 3.3.3. Kiểm định cửa sổ vận hành trên giai đoạn dữ liệu giữ lại (Out-of-Time Validation)

- **Thiết kế kiểm định theo chuỗi thời gian độc lập**:
- Nghiên cứu kiểm tra năng lực suy rộng của cửa sổ vận hành trên giai đoạn dữ liệu thời gian tương lai chưa từng được học.
- Chuỗi dữ liệu SCADA 306 ngày được chia theo thời gian nghiêm ngặt. Tập huấn luyện gồm $70\%$ dữ liệu đầu (tháng 1 đến 7) để xác lập cửa sổ vận hành. Tập kiểm định độc lập gồm $30\%$ dữ liệu sau (tháng 8 đến 10/11).
- Quá trình kiểm định đánh giá trực tiếp tần suất đạt mục tiêu thực tế của trạm, độc lập hoàn toàn với sai số mô hình học máy.
- Cửa sổ vận hành rút ra từ 7 tháng đầu đặt điều kiện ưu tiên hàng đầu cho $\text{SRT} \le 84.5\text{ ngày}$ kết hợp với điều chỉnh thứ cấp của HRT.

- **Hiệu quả cải thiện tỷ lệ đạt mục tiêu và độ tin cậy thống kê**:
- Trạm ghi nhận 415 giờ vận hành rơi vào bên trong cửa sổ khuyến nghị trong giai đoạn giữ lại.
- Tỷ lệ đạt đồng thời cả ba tiêu chí hiệu suất bên trong cửa sổ đạt $61.9\%$, vượt trội so với mức nền $39.3\%$ ngoài cửa sổ ($37.1\%$ toàn trạm).
- Tỷ số chênh lệch khả năng đạt mục tiêu đạt $\text{Odds Ratio} = 3.89$ với mức ý nghĩa thống kê cao (kiểm định chính xác Fisher $p = 3 \times 10^{-29}$).
- Hiệu quả chuyển giao độc lập của từng biến điều khiển sinh học trên dữ liệu giữ lại:
  - Nồng độ bùn hoạt tính MLSS tăng $+30.9$ điểm phần trăm (mức tăng cao nhất trong các đòn bẩy).
  - Thời gian lưu bùn SRT tăng $+22.7$ điểm phần trăm.
  - Tải trọng hữu cơ F/M tăng $+15.7$ điểm phần trăm.
- Ba biến kiểm soát sinh học (SRT, MLSS, F/M) có chu kỳ can thiệp từ vài giờ đến vài ngày. Các biến này đạt độ bền vững chuyển giao cao nhất và giữ vai trò trung tâm trong giao thức vận hành.

---

#### 3.3.4. Sự dịch chuyển tầm quan trọng đặc trưng và hàm ý kiểm soát thời gian thực

- **Hiện tượng dịch chuyển thứ hạng SHAP trong vùng khả thi**:
- Việc giới hạn không gian phân tích SHAP vào bên trong vùng khả thi làm thay đổi đáng kể thứ hạng quan trọng của các đặc trưng.
- Nguyên nhân: Các điều kiện vận hành cực đoan gây hại ($\text{SRT} > 100\text{ ngày}$, $\text{MLSS} > 7500\text{ mg/L}$, $\text{HRT} > 10\text{ h}$) đã bị loại bỏ hoàn toàn bởi các ràng buộc đầu ra.
- Khi loại bỏ các điều kiện cực đoan, các nguồn biến động ngắn hạn trở thành yếu tố chi phối chính.
- Mức độ quan trọng của tỷ lệ F/M đối với mức chất lỏng bể màng tăng vọt $87\%$, nhảy từ vị trí thứ 5 lên vị trí thứ 4.
- Trong toàn bộ dữ liệu, giá trị SRT và MLSS cực hạn chi phối phương sai mức nước. Hiện tượng này che khuất tác động ngắn hạn của tải lượng hữu cơ.
- Trong vùng khả thi, khi SRT và MLSS duy trì ở mức an toàn, F/M trở thành động lực chính dẫn dắt dao động mức bể màng theo từng giờ.

- **Chiến lược kiểm soát ba cấp tốc độ cho mức bể màng**:
- Dao động của F/M phản ánh trực tiếp chu kỳ xả thải theo mẻ của các công đoạn chế tạo linh kiện bán dẫn.
- Mức độ quan trọng của MLSS đối với mức nước bể màng cũng tăng đồng thời, định hình ba đòn bẩy điều khiển phản ứng nhanh:
  - **Tốc độ châm glucose Glu (thời gian phản ứng: vài phút)**: Ổn định tỷ lệ dinh dưỡng và kiểm soát tải hữu cơ tức thời.
  - **Lưu lượng xả bùn hoạt tính WAS (thời gian phản ứng: vài giờ)**: Điều chỉnh mật độ sinh khối và giải phóng thể tích bùn.
  - **Điều chỉnh F/M qua bể điều hòa lưu lượng (thời gian phản ứng: vài giờ)**: Giảm đỉnh nồng độ hữu cơ cấp vào bể phản ứng sinh học.
- Ba đòn bẩy thời gian thực giúp khống chế mức nước bể màng dưới ngưỡng an toàn $67.0\%$ khi sản xuất cao điểm. Người vận hành không cần chờ chu kỳ điều chỉnh SRT kéo dài nhiều tuần.
- Thứ hạng của C/N cũng tăng lên đối với TMP và lưu lượng nước thấm. C/N đóng vai trò thông số giám sát động cần tái ước lượng định kỳ theo tiến độ sản xuất của xưởng đúc wafer.
- Khuyến nghị vận hành đạt sự hội tụ từ ba nguồn chứng cứ. Các chứng cứ gồm đồng thuận SHAP trên 16 mô hình, bề mặt khả thi đa tạp và số đo thực tế SCADA.

---

### 3.4. So sánh và triển vọng (Comparison & Perspectives)

#### 3.4.1. Hiệu suất dự đoán

- **Đối sánh hiệu năng với các nghiên cứu MBR tiền nhiệm**:
- Các nghiên cứu học máy MBR trước đây chủ yếu tập trung vào nước thải sinh hoạt hoặc đô thị ở quy mô phòng thí nghiệm và quy mô pilot. Các công trình trước thường chỉ dự báo một biến mục tiêu đơn lẻ như TMP hoặc lưu lượng nước thấm:
  - Mô hình MLP và LSTM dự báo TMP cho trạm pilot AnMBR xử lý nước thải đô thị đạt $R^2 > 0.91$ [68].
  - Rừng ngẫu nhiên (Random Forest) dự báo tắc nghẽn màng trong trạm AnMBR đạt $R^2 = 0.906$ [69].
  - Hệ suy luận mờ thích ứng nơ-ron (ANFIS) dự báo lưu lượng nước thấm trong MBR thẩm thấu đạt $R^2 = 0.9755 - 0.9861$ [70].
- Nghiên cứu triển khai Extra Trees trên hệ thống MBR công nghiệp quy mô $1125\text{ m}^3/\text{h}$ với $4593\text{ giờ}$ SCADA thực tế. Nguồn thải bán dẫn có biến động tải lượng rất lớn.
- Mô hình giải quyết đồng thời ba biến đầu ra phụ thuộc lẫn nhau, phản ánh chân thực động lực học vận hành thực tế.

- **Tác động của cấu trúc phân vùng dữ liệu lên độ chính xác**:
- Dưới thiết kế phân vùng ngẫu nhiên (Random Partition) tương đương các nghiên cứu trước, Extra Trees đạt độ chính xác cao:
  - Áp suất hút xuyên màng TMP đạt $R^2 = 0.988$.
  - Lưu lượng nước thấm qua màng đạt $R^2 = 0.933$.
  - Mức chất lỏng bể chứa màng đạt $R^2 = 0.908$.
- Dưới thiết kế phân vùng khối 24 giờ (24-h Blocked Partition) nhằm loại bỏ rò rỉ dữ liệu do tự tương quan chuỗi thời gian:
  - TMP đạt $R^2 = 0.830$.
  - Lưu lượng nước thấm đạt $R^2 = 0.788$.
  - Mức chất lỏng bể màng đạt $R^2 = 0.564$.
- Việc công bố song song cả hai sơ đồ phân vùng đảm bảo tính minh bạch học thuật khi so sánh với tài liệu tiền nhiệm. Mô hình tập hợp Extra Trees đạt hiệu năng xuất sắc trên ba mục tiêu mà không chịu gánh nặng tính toán lớn của mạng nơ-ron tái hồi RNN/LSTM.

---

#### 3.4.2. Tiếp cận tối ưu hóa

- **Khác biệt giữa tối ưu hóa tham số mô hình và tối ưu hóa vận hành**:
- Phần lớn tài liệu MBR học máy dùng thuật ngữ "tối ưu hóa" để chỉ việc tinh chỉnh siêu tham số mô hình hoặc tìm kiếm kiến trúc mạng (AutoML).
- Nghiên cứu [71] từng áp dụng thuật toán di truyền (GA) để tìm điều kiện vận hành. Tuy nhiên công trình đó chỉ giải quyết bài toán đơn mục tiêu nhằm giảm tắc màng.
- Đây là nghiên cứu đầu tiên tối ưu hóa điều kiện vận hành đa mục tiêu trên đa tạp dữ liệu thực tế cho MBR. Phương pháp đáp ứng đồng thời cả ba tiêu chuẩn hiệu suất.

- **Bản đồ xác suất liên tục so với thuật toán tối ưu hóa điểm đơn lẻ**:
- Thuật toán GA hoặc tối ưu hóa bầy đàn (PSO) truyền thống chỉ tìm ra một điểm vận hành đơn lẻ mang tính cục bộ. Điểm này rất nhạy cảm với sai số mô hình và không cung cấp biên độ dung sai an toàn.
- Phương pháp lập bản đồ vùng vận hành khả thi tạo ra bề mặt xác suất có điều kiện liên tục trên $207{,}238$ trạng thái thực tế.
- Bề mặt xác suất giúp người vận hành nhận diện các vùng có khả năng chống chịu cao trước các biến động tải lượng thường nhật.
- Không gian khả thi cần được lấy mẫu trên đa tạp kết hợp thực tế thay vì quét độc lập từng chiều biên. Khuyến nghị vận hành phải được xếp hạng theo tỷ lệ đạt mục tiêu có điều kiện thay vì mật độ mẫu.

- **Phân biệt ranh giới khả thi kỹ thuật và vùng lõi đạt mục tiêu cao**:
- Ranh giới khả thi toán học rộng hơn rất nhiều so với vùng vận hành an toàn thực tế:
  - Vùng bao khả thi của SRT mở rộng tới trên $95\text{ ngày}$, nhưng tỷ lệ đạt mục tiêu thực tế trên $87\text{ ngày}$ giảm xuống dưới $20\%$.
  - Vùng bao khả thi của HRT kéo dài đến $7.65\text{ h}$, nhưng tỷ lệ đạt mục tiêu thực tế trên $7.95\text{ h}$ rơi về $0\%$.
  - Vùng bao khả thi của F/M kéo dài đến $0.037\text{ ngày}^{-1}$, nhưng tỷ lệ đạt mục tiêu thực tế trên ngưỡng này chỉ còn $15.0\%$.
- Phân tích thỏa mãn ràng buộc thông thường dễ hướng người vận hành đến các điểm biên có rủi ro vi phạm cao. Việc xếp hạng theo tỷ lệ đạt mục tiêu thiết lập ranh giới an toàn thực chất, bảo vệ hệ thống trước sự cố công nghệ.

---

#### 3.4.3. Triển vọng và chiến lược tương lai

- **Khả năng chuyển giao công nghệ và giá trị thực tiễn**:
- Mô hình huấn luyện trên dữ liệu SCADA lịch sử hỗ trợ chỉ dẫn vận hành trực tiếp. Trạm không cần phân tích hóa lý bổ sung trong phòng thí nghiệm.
- Khung phân tích SHAP hai ngữ cảnh so sánh toàn bộ dữ liệu với vùng khả thi. Phương pháp này giúp phát hiện các biến điều khiển phản ứng nhanh cho quy trình công nghiệp đa đầu ra.
- Quy trình vận hành được xếp hạng theo bằng chứng thực nghiệm rõ ràng. Mỗi khuyến nghị đều đi kèm tỷ lệ đạt mục tiêu thực tế và chứng minh hiệu quả trên tập dữ liệu giữ lại độc lập.

- **Ranh giới áp dụng và định hướng phát triển thực nghiệm**:
- Nghiên cứu xác lập bốn ranh giới kỹ thuật cần lưu ý:
  - **Bản chất dữ liệu**: Kết quả dựa trên dữ liệu quan sát SCADA lịch sử, chưa qua thử nghiệm đối chứng ngẫu nhiên (Randomized Controlled Trial).
  - **Tính đặc thù trạm**: Mô hình xây dựng cho một nhà máy duy nhất với cấu hình màng sợi rỗng PVDF UF. Phương pháp luận có thể chuyển giao toàn diện, nhưng các dải số định lượng cần hiệu chỉnh theo từng trạm.
  - **Miền nội suy đa tạp**: Mô hình chỉ hoạt động tin cậy trong không gian dữ liệu trạm từng trải qua. Cần bổ sung các biến đầu vào triển vọng gồm tuổi thọ màng, lịch sử rửa hóa chất CIP và độ dẫn điện dòng thải.
  - **Bản chất của SHAP**: Giá trị SHAP định lượng mối liên kết thống kê trên phân phối dữ liệu, không chứng minh quan hệ nhân quả vật lý tuyệt đối. Việc xác nhận cơ chế đòi hỏi mổ xẻ màng (autopsy), đo thế zeta và phân đoạn hữu cơ dịch lọc.
- Định hướng tiếp theo: Triển khai thử nghiệm lâm sàng luân phiên chiến lược điều khiển giữa hai nhánh màng UF song song có chung nước đầu vào. Tích hợp mô hình vào Bản sao số (Digital Twin) và Hệ thống hỗ trợ ra quyết định thời gian thực (Real-time DSS).

---

## 4. Kết luận (Conclusion)

### 4.1. Đóng góp cốt lõi của khung AI giải thích được
- Nghiên cứu xây dựng khung AI giải thích đa mô hình đầu tiên cho trạm MBR bán dẫn quy mô $1125\text{ m}^3/\text{h}$. Khung AI định nghĩa thành công không gian vận hành tối ưu.
- Extra Trees đạt độ chính xác và tính ổn định cao trên cả ba biến mục tiêu phụ thuộc lẫn nhau. Kết quả gồm TMP ($R^2 = 0.988$), lưu lượng thấm ($R^2 = 0.933$) và mức bể màng ($R^2 = 0.908$).
- Phân vùng khối 24 giờ chứng minh năng lực tổng quát hóa của Extra Trees. Thuật toán khắc phục triệt để hiện tượng tự tương quan chuỗi thời gian công nghiệp.

### 4.2. Khám phá cơ chế vật lý và ý nghĩa thực tiễn cho vận hành MBR
- **Cơ chế tắc màng đơn điệu của SRT trong chế độ hiếu khí kéo dài**: 16 thuật toán SHAP xác nhận tăng SRT làm tích tụ sinh khối trơ. Quá trình này làm tăng độ nhớt bùn và nén chặt bánh bùn ($R^2 = 0.988$). Kết quả bác bỏ quan niệm truyền thống cho rằng tuổi bùn cao giúp giảm tắc nghẽn màng.
- **Xác lập bản đồ không gian khả thi trên đa tạp dữ liệu thực nghiệm**: Phương pháp xác lập dải thông số vận hành hành động được. Việc tuân thủ dải khuyến nghị nâng tỷ lệ đạt mục tiêu từ mức nền $37.1\%$ lên tới $82.4\%$.
- **Kiểm chứng độc lập trên dữ liệu tương lai giữ lại**: Tỷ lệ đạt mục tiêu thực tế trong cửa sổ đạt $61.9\%$ so với $39.3\%$ ngoài cửa sổ. Tỷ số chênh lệch đạt $\text{Odds Ratio} = 3.89$ ($p < 0.001$).
- **Duy trì độ chính xác ngoại suy dài hạn**: Tái huấn luyện mô hình hàng ngày duy trì sai số dự báo TMP trong phạm vi $\pm 0.008\text{ bar}$. Hệ số xác định đạt $R^2 = 0.871$ sau 4 tháng kiểm định ngoại suy liên tục.
- **Chuyển dịch tư duy quản lý màng**: Khung phương pháp luận ưu tiên tính giải thích quy trình. Bản đồ khả thi phân tầng thực nghiệm thay thế việc chỉ theo đuổi độ chính xác danh nghĩa trên dữ liệu tự tương quan.
