### 2.1 Full-scale MBR plant and data collection

#### 2.1.1 Plant description and operational data source

- Hệ thống màng sinh học ($\text{MBR}$) quy mô thực tế được đặt tại Trạm xử lý nước thải công cộng "D" ở Hàn Quốc
  - Trạm xử lý có công suất thiết kế đạt mức $25.000\text{ m}^3/\text{ngày}$.
  - Dữ liệu vận hành thực tế được theo dõi và thu thập liên tục trong khoảng thời gian hơn 1 năm.
- Cơ sở dữ liệu bao gồm giá trị trung bình hàng ngày của các thông số chất lượng nước và vận hành
  - Các thông số chất lượng nước đo đạc bao gồm $\text{COD}$, $\text{TN}$ và $\text{TP}$ từ dòng đầu vào và các phân vùng xử lý.
  - Các thông số vận hành kỹ thuật bao gồm lưu lượng dòng chảy, chế độ sục khí và nhiệt độ vận hành.
  - Nồng độ chất ô nhiễm trung bình trong nước thải đầu vào ghi nhận: $\text{COD}$ đạt $15.50\text{ mg/L}$, $\text{TN}$ đạt $27.91\text{ mg/L}$ và $\text{TP}$ đạt $1.80\text{ mg/L}$.
  - Tập dữ liệu đầy đủ này được sử dụng làm cơ sở huấn luyện và kiểm định các mô hình học máy.

#### 2.1.2 Integrated MBR process configuration

- Đơn vị màng $\text{MBR}$ đóng vai trò phân tách pha rắn - lỏng và duy trì nồng độ bùn hoạt tính ($\text{MLSS}$) cao
  - Màng sinh học giữ lại toàn bộ sinh khối hoạt tính trong bể, tạo dòng nước sau lọc có chất lượng trong và ổn định.
  - Mục tiêu cốt lõi của cấu hình cải tiến là tối đa hóa hiệu suất khử $\text{TN}$ trong khi vẫn duy trì cân bằng xử lý $\text{TP}$ và $\text{COD}$.
- Cấu hình tổng thể tích hợp hai giải pháp kỹ thuật bổ trợ khắc phục mất cân bằng oxy và nhạy cảm nhiệt độ
  - Tích hợp bể chuyển đổi (swing-basin) để tăng cường quá trình nitrat hóa trong điều kiện mùa lạnh.
  - Bổ sung bể giảm oxy hòa tan ($\text{DO-R}$) nhằm ngăn chặn oxy hòa tan dư thừa xâm nhập vào vùng thiếu khí.
    - **Hình 1.** Sơ đồ cấu hình hệ thống phản ứng MBR tích hợp bể chuyển đổi và bể DO-R
      - <img src="assets/fig_01_p3.jpeg" alt="Hình 1" />
      - **Hình này chứng minh điều gì**
        - Sơ đồ chuỗi công nghệ kết hợp bể swing và bể DO-R khử đồng thời nitơ và photpho.
      - **Từ đâu mà thấy được**
        - Dòng bùn tuần hoàn từ bể MBR đi qua bể DO-R không sục khí trước khi hồi lưu anoxic.

#### 2.1.3 Process unit design and functional rationale

- Vùng kỵ khí (2.1.3.1 Anaerobic zone) là điểm khởi đầu thiết yếu cho chu trình giải phóng photpho
  - Điều kiện vận hành duy trì triệt để không có oxy hòa tan và không chứa nitrat.
  - Quần thể sinh vật tích lũy photpho ($\text{PAO}$) thủy phân polyphosphate nội bào để tạo năng lượng, giải phóng photphat hòa tan vào dung dịch.
  - Sự tích lũy cacbon hòa tan dễ phân hủy dưới dạng polyhydroxyalkanoate ($\text{PHA}$) trong tế bào $\text{PAO}$ làm giảm sự cạnh tranh cacbon đối với vi khuẩn khử nitrat ở vùng sau.
- Vùng thiếu khí (2.1.3.2 Anoxic zone) là vị trí phản ứng chính của quá trình khử nitrat tổng thể
  - Môi trường phản ứng đặc trưng bởi sự vắng mặt của $\text{DO}$ cùng với sự hiện diện của nitrat ($\text{NO}_3^-$) và nitrit ($\text{NO}_2^-$).
  - Vi khuẩn dị dưỡng tùy nghi sử dụng các dạng nitơ oxy hóa làm chất nhận electron cuối cùng thay thế cho oxy tự do.
  - Quá trình khử sinh hóa chuyển hóa tuần tự từ nitrat sang nitrit ($\text{NO}_2^-$), oxit nitric ($\text{NO}$), oxit đinitơ ($\text{N}_2\text{O}$) và khí nitơ vô hại ($\text{N}_2$).
  - Nồng độ oxy xâm nhập phải được giữ ở mức tối thiểu để tránh ức chế các enzyme khử nitrat đặc hiệu.
- Bể chuyển đổi (2.1.3.3 Swing basin) hoạt động như một vùng đệm linh hoạt cho quá trình nitrat hóa
  - Khả năng chuyển đổi luân phiên giữa chế độ thiếu khí và hiếu khí thông qua việc bật hoặc tắt hệ thống sục khí.
  - Trong mùa đông lạnh, vận hành chế độ hiếu khí giúp mở rộng thể tích sục khí hiệu dụng và kéo dài thời gian lưu thủy lực ($\text{HRT}$).
  - Sự ổn định quá trình nitrat hóa ngăn ngừa amoni tích tụ trong nước sau xử lý và giảm bớt nhu cầu bổ sung nguồn cacbon ngoại sinh.
  - Quá trình chuyển hóa amoni hoàn chỉnh hạn chế sự cạnh tranh oxy giữa vi khuẩn nitrat hóa và vi khuẩn $\text{PAO}$, hỗ trợ gián tiếp cho việc hấp thu photpho.
- Vùng hiếu khí và ngăn màng MBR (2.1.3.4 Aerobic zone and MBR) duy trì hai quá trình sinh học song song
  - Sục khí liên tục thúc đẩy vi khuẩn tự dưỡng chuyển hóa amoni ($\text{NH}_4^+$) thành nitrat ($\text{NO}_3^-$) qua bước trung gian nitrit.
  - Nguồn năng lượng $\text{PHA}$ tích lũy được vi khuẩn $\text{PAO}$ sử dụng để hấp thu lượng lớn photphat từ hỗn hợp bùn, lưu trữ dưới dạng hạt polyphosphate nội bào.
- Bể giảm oxy hòa tan (2.1.3.5 DO reduction basin) loại bỏ oxy hòa tan dư thừa khỏi dòng bùn hồi lưu
  - Bể phản ứng chuyên biệt không cấp khí được lắp đặt ngay sau vùng hiếu khí và ngăn màng $\text{MBR}$.
  - Vi sinh vật thực hiện quá trình hô hấp nội bào trong điều kiện thiếu cacbon ngoại sinh để tiêu thụ lượng $\text{DO}$ còn tồn dư.
  - Ngăn ngừa hiện tượng ngộ độc oxy trong vùng thiếu khí, tạo điều kiện thuận lợi nhất cho quá trình khử nitrat đạt hiệu suất cao.
  - Môi trường không chứa $\text{DO}$ bảo vệ hoạt tính giải phóng photpho của vi khuẩn $\text{PAO}$ khi hồi lưu về ngăn trước.
- Hệ thống phân dòng bùn hồi lưu từng bậc (2.1.3.6 Return sludge step-feed system) kiểm soát linh hoạt dòng mang nitrat
  - Thiết kế các đường ống tuần hoàn độc lập cho phép điều chỉnh lưu lượng bùn đưa về vùng kỵ khí hoặc vùng chuyển đổi/thiếu khí.
  - Khả năng tinh chỉnh lưu lượng bùn giúp tối ưu hóa nồng độ cơ chất và thời gian tiếp xúc của các chủng vi sinh vật.
- Đường tắt dòng nước thải đầu vào (2.1.3.7 Influent bypass - Line 4) khắc phục hiện tượng thiếu hụt cacbon
  - Cơ chế cho phép dẫn trực tiếp một phần nước thải thô giàu $\text{COD}$ dễ phân hủy (như axit béo bay hơi) vào thẳng vùng thiếu khí.
  - Đường tắt được kích hoạt khi hiệu suất khử nitrat giảm sút nhằm bổ sung chất cho electron cho vi khuẩn khử nitrat mà không qua ngăn kỵ khí.
