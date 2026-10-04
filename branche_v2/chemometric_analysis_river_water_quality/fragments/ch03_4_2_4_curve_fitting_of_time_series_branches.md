### 2.4. Curve fitting of time series

- Phân tích thành phần chính (PCA - Principal Component Analysis) trên Dataset 1 thể hiện quy luật biến thiên có dạng chu kỳ (periodic form) đối với các giá trị điểm số (scores).
  - Các giá trị điểm số đại diện cho chất lượng nước tại các mốc thời gian khác nhau $t_i$ theo từng giờ (on hourly basis).
  - Dữ liệu chuỗi thời gian của các điểm số được giả định cấu thành từ hai thành phần:
    - Tín hiệu thời gian hữu ích $y$ (useful temporal signal): phản ánh xu hướng biến đổi chung (general trend) của chất lượng nước trong toàn bộ chu kỳ quan trắc đối với từng thành phần chính (principal components).
    - Thành phần nhiễu (noise): tương ứng với các sự kiện chất lượng nước không phụ thuộc vào chu kỳ thời gian (non-time dependent periodic events) hoặc các giá trị ngoại lai cực trị (extreme values) (Deng và Wang, 2017).
  - Tín hiệu hữu ích $y$ được biểu diễn toán học dưới dạng một hàm chu kỳ liên tục (continuous periodic function) xác định trên một khoảng thời gian cụ thể (certain time interval).
  - Các biến động giá trị chất lượng nước không được hàm chu kỳ liên tục này giải thích đều được xem là nhiễu (noise).
- Bản chất chu kỳ của các giá trị điểm số (được xem như tín hiệu chu kỳ $g(x)$) được mô hình hóa thông qua phương pháp xấp xỉ chuỗi Fourier (Fourier series approximation) (Mueller-Warrant et al., 2012).
  - Mô hình xấp xỉ chuỗi Fourier được thiết lập theo Phương trình (2):
    $$g(x) = a_0 + \sum_{i=1}^{n} \left( a_i \cdot \cos(i \cdot w \cdot x) + b_i \cdot \sin(i \cdot w \cdot x) \right) \tag{2}$$
  - Trong đó:
    - $a_0$: số hạng hằng số (hệ số chặn - intercept term) trong tập dữ liệu, tương ứng với số hạng cosin khi $i = 0$.
    - $w$: tần số cơ bản (fundamental frequency) của tín hiệu.
    - $n$: số lượng số hạng điều hòa (harmonics) trong chuỗi Fourier.
    - $x$: biến số thời gian biểu diễn chuỗi dữ liệu điểm số.
    - $a_i, b_i$: các hệ số Fourier của các số hạng điều hòa cosin và sin tương ứng tại bậc $i$.
    - Số lượng số hạng điều hòa bị giới hạn trong phạm vi $1 \le n \le 8$.
- Tiêu chí xác định mô hình khớp đường cong chuỗi thời gian tối ưu (best data fitting) kết hợp đánh giá trực quan và chỉ số thống kê.
  - Quá trình khớp dữ liệu tốt nhất đạt được thông qua quan sát trực quan (visual inspection).
  - Hệ số xác định ($R^2$ - determination coefficient) cao nhất được dùng làm thước đo đánh giá hiệu quả dự báo của phương trình đối với các giá trị điểm số.
