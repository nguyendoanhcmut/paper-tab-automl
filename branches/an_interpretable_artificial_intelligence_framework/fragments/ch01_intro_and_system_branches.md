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

#### 2.4.3. Kiểm định ngoại suy thời gian và xác thực chéo trên nhánh màng B
- Phân vùng theo thời gian (chronological partition): huấn luyện trên $70\%$ đầu và kiểm định trên $30\%$ cuối.
- Phiên bản loại trừ (purged chronological partition) loại bỏ khoảng đệm 1 tuần tại ranh giới hai tập.
- Kiểm định ngoại suy thời gian trên 3-4 tháng dữ liệu mới. Quy trình kết hợp tái huấn luyện hàng ngày (daily refit).
- Xác thực chéo độc lập trên nhánh màng B (parallel B stream) với 4593 bản ghi theo giờ riêng biệt tại cùng nhà máy.
- Kiểm định mô hình của nhánh A trực tiếp trên nhánh màng B không cần tái huấn luyện.
