### 2.1 Data Acquisition and Preprocessing

#### 2.1.1 Study Site Characteristics
- Nghiên cứu thực hiện quan trắc tại hai nhà máy xử lý nước thải quy mô thực tế ở Queensland, Australia:
  - Nhà máy WWTP-A:
    - Công suất xử lý thiết kế đạt $20\text{ ML}\cdot\text{d}^{-1}$ ($20\text{ megalitres/day}$).
    - Áp dụng cấu hình khử dinh dưỡng sinh học (BNR - Biological Nutrient Removal) gồm vùng thiếu khí (anoxic) và hiếu khí (aerobic) nối tiếp, theo sau là bể lắng thứ cấp.
    - Vận hành máy sục khí cơ học bề mặt (surface aerators) trên 6 bể sinh học song song.
    - Mỗi bể gồm một vùng thiếu khí (ngăn 1) và một vùng hiếu khí chia 2 ngăn (ngăn 2 và 3); quan trắc chuyên sâu tại một bể sinh học đại diện.
  - Nhà máy WWTP-B:
    - Công suất xử lý thiết kế đạt $30\text{ ML}\cdot\text{d}^{-1}$.
    - Sử dụng quy trình 5 giai đoạn Bardenpho (five-stage Bardenpho process) trong bể phản ứng sinh học đa ngăn gồm 12 ngăn nối tiếp.
    - Cấu hình nối tiếp gồm các vùng kỵ khí (anaerobic), hiếu khí (aerobic), thiếu khí sau (post-anoxic) và tái hiếu khí (reaeration) trên các chuỗi xử lý song song.
    - Tạo lập môi trường oxy hóa khử phân tầng theo từng giai đoạn; chiến dịch quan trắc tập trung vào một chuỗi xử lý đại diện.

#### 2.1.2 Data Sets and Pretreatments
- Ba tập dữ liệu thực nghiệm được thu thập để đánh giá khung mô hình hóa (Bảng 1):
  - Tập dữ liệu A1 (WWTP-A):
    - Thời gian quan trắc từ ngày 25 tháng 5 năm 2024 đến ngày 16 tháng 8 năm 2024.
    - Giai đoạn tháng 5 đến tháng 7 năm 2024 dùng cho huấn luyện và kiểm định nội miền (in-distribution).
    - Giai đoạn từ ngày 9 đến ngày 16 tháng 8 năm 2024 là giai đoạn kiểm tra điều kiện dòng chảy cao ngoài phân phối (out-of-distribution high-flow).
    - Các thông số SCADA ghi nhận gồm: nồng độ $N_2O$ hòa tan, thông số bùn tuần hoàn ($\text{RAS\_CDE}$ và $\text{RAS\_F}$), chỉ số nitơ ($NH_4^+$, $NO_3^-$), công suất sục khí $\text{Aeration Power2}$, lưu lượng bùn thải $\text{WAS}$, lưu lượng dòng vào $\text{InflowRate}$, oxy hòa tan $\text{DO}$, trạng thái sục khí $\text{Aeration On/Off}$, amoni và nitrat trong nước sau lắng.
  - Tập dữ liệu A2 (WWTP-A):
    - Thu thập trong chiến dịch mùa hè từ ngày 5 đến ngày 15 tháng 12 năm 2024.
    - Đại diện cho điều kiện mùa vụ khác biệt nhằm kiểm tra tính tổng quát hóa theo thời gian.
  - Tập dữ liệu B1 (WWTP-B):
    - Thu thập trong chiến dịch quan trắc từ tháng 10 đến tháng 11 năm 2025.
    - Ghi nhận: lưu lượng dòng vào và bùn thải, lưu lượng bơm $\text{RAS}$, tốc độ bơm tuần hoàn nội bộ (chu kỳ A), lưu lượng khí sục tại các ngăn 1–3 và ngăn tái hiếu khí, nồng độ $\text{DO}$ các ngăn 1–3 và ngăn tái hiếu khí, $\text{pH}$ nước ra, nhiệt độ ngăn 1, amoni, nitrat và nồng độ $N_2O$ đo bằng cảm biến tại chỗ.
- Phương pháp tiền xử lý và đồng bộ hóa chuỗi thời gian:
  - Tái lấy mẫu (resampling) toàn bộ chuỗi dữ liệu SCADA về khoảng thời gian đồng nhất $15\text{ phút}$ bằng giá trị trung bình mỗi khung thời gian nhằm giảm chi phí tính toán và bảo đảm nắm bắt động học xử lý.
  - Dữ liệu lượng mưa theo giờ thu thập từ cổng CHRS (PERSIANN-CCS) tương ứng với lưu vực của từng nhà máy.
  - Áp dụng phương pháp nội suy tuyến tính (linear interpolation) để khớp dữ liệu mưa theo mốc thời gian $15\text{ phút}$ của hệ thống SCADA, phục vụ phân tích ảnh hưởng của mưa lên phát thải $N_2O$.

#### 2.1.3 Feature Engineering
- Xây dựng mô hình bùn hoạt tính kết hợp $N_2O$ (ASM-$N_2O$):
  - Mô hình Activated Sludge Model-$N_2O$ được hiệu chuẩn riêng cho từng hệ thống dựa trên dữ liệu 2 tuần đầu tiên.
  - Kiểm soát nghiêm ngặt hiện tượng rò rỉ dữ liệu (data leakage): dữ liệu hiệu chuẩn nằm trọn trong tập huấn luyện, không sử dụng dữ liệu từ tập kiểm định hay kiểm tra.
- Tích hợp con đường phản ứng sinh hóa và động học vi sinh:
  - Mô hình hóa cơ chế sinh $N_2O$ qua vi khuẩn oxy hóa amoni (AOB) theo Pocquet et al., gồm con đường nitrat hóa (NN - Nitrifier Nitrification) và khử nitrat của vi khuẩn nitrat hóa (ND - Nitrifier Denitrification).
  - Tích hợp mô hình khử nitrat dị dưỡng bốn bước của Hiatt và Grady.
  - Hiệu chuẩn độc lập cho WWTP-A và WWTP-B dựa trên dữ liệu biên dạng $\text{DO}$ và quá trình chuyển hóa các dạng nitơ.
- Trích xuất tập biến trạng thái sinh học bổ sung:
  - Nồng độ khí hòa tan: $N_2$ và $N_2O$.
  - Các dạng hợp chất nitơ hòa tan: $NH_4^+$, $NH_2OH$, $NO$, $NO_2^-$, $NO_3^-$.
  - Mức oxy hòa tan $\text{DO}$ và nồng độ cơ chất hữu cơ dễ phân hủy sinh học.
  - Nồng độ các nhóm sinh khối vi sinh: $X_{AOB}$, $X_H$ (vi khuẩn dị dưỡng), $X_I$ (chất trơ) và $X_{NOB}$ (vi khuẩn oxy hóa nitrit).
