## 2.3. Preprocessing and Feature Engineering

- Tiền xử lý dữ liệu và kỹ thuật đặc trưng (preprocessing and feature engineering) được áp dụng nhằm nâng cao tính nhất quán của dữ liệu (data consistency) và cải thiện hiệu suất mô hình trong điều kiện vận hành thực địa không lý tưởng (non-ideal field conditions):
  - Phép co giãn mạnh mẽ (robust scaling) và các phép biến đổi trung bình trượt (moving average transformations) được lựa chọn để mô phỏng các điều kiện thực tế tại hiện trường, nơi chất lượng dữ liệu thường xuyên bị suy giảm (compromised).
  - Các kỹ thuật này bảo đảm độ bền vững (resilience) của mô hình trước các giá trị ngoại lai (outliers) và các khoảng trống dữ liệu theo thời gian (temporal gaps) — những yếu tố có tính chất sống còn đối với việc triển khai thực tế trong công nghiệp (industrial deployment).

### 2.3.1. Robust Scaling

- Phép co giãn mạnh mẽ (robust scaling) được triển khai nhằm chuẩn hóa tập dữ liệu (normalize the dataset) đồng thời hạn chế tối đa ảnh hưởng từ các giá trị cực trị (extreme values):
  - Khác biệt với các phương pháp chuẩn hóa tiêu chuẩn (standard normalization methods) vốn rất nhạy cảm với các giá trị ngoại lai (outliers), robust scaling định tâm dữ liệu theo giá trị trung vị (median) và co giãn theo khoảng tứ phân vị (interquartile range: $IQR = Q_3 - Q_1$).
  - Kỹ thuật này bảo đảm sự phân phối của các biến số có thang đo (scales) khác nhau duy trì được tính tương đồng và có thể so sánh trực tiếp với nhau.
- Phép biến đổi robust scaling được thực hiện theo Equation (1):
  $$x_{\text{robust scaled}} = \frac{x - \text{Median}}{Q_3 - Q_1} \tag{1}$$
  - $x$: giá trị ban đầu của đặc trưng trước khi chuẩn hóa.
  - $x_{\text{robust scaled}}$: giá trị đặc trưng thu được sau khi thực hiện biến đổi robust scaling.
  - $\text{Median}$: giá trị trung vị của phân phối đặc trưng (phân vị thứ $50$, $Q_2$), đóng vai trò tâm chuẩn hóa thay cho giá trị trung bình (mean) để triệt tiêu ảnh hưởng của ngoại lai.
  - $Q_3 - Q_1$: khoảng tứ phân vị ($IQR$), biểu thị độ biến thiên giữa phân vị thứ $75$ ($Q_3$) và phân vị thứ $25$ ($Q_1$), đóng vai trò là mẫu số co giãn bền vững.

### 2.3.2. Moving Average

- Hiện tượng trễ thời gian (time delay) giữa các đặc tính dòng vào (influent) và dòng ra (effluent) phát sinh do quá trình loại bỏ chất ô nhiễm trong hệ thống bể phản ứng sinh học màng (membrane bioreactor - MBR) đòi hỏi một khoảng thời gian xử lý nhất định:
  - Khái niệm độ trễ thời gian trong nghiên cứu này là một phương pháp kỹ thuật đặc trưng dựa trên dữ liệu (data-driven feature engineering method) nhằm tối ưu hóa việc ghép cặp dữ liệu đầu vào – đầu ra (input–output data pairing) cho huấn luyện mô hình học máy.
  - Phương pháp này không đóng vai trò đại diện trực tiếp cho thời gian lưu thủy lực (hydraulic retention time - HRT) hay độ trễ quá trình vật lý (physical process lag).
  - Cách tiếp cận tối ưu ghép cặp cho phép xác định cơ chế căn chỉnh theo thời gian hiệu quả nhất (effective temporal alignment) phục vụ dự đoán tắc nghẽn màng (fouling prediction) trong các điều kiện dữ liệu và vận hành cụ thể.
- Biến đổi trung bình trượt (moving average transformation) được áp dụng đồng loạt cho toàn bộ các đặc trưng nhằm tích hợp hành vi phụ thuộc thời gian (time-dependent behavior):
  - Nâng cao năng lực nắm bắt các xu hướng dài hạn (long-term trends) của mô hình học máy, đồng thời giảm thiểu tác động gây nhiễu từ các dao động ngắn hạn (short-term fluctuations).
  - Giảm thiểu ảnh hưởng của các giá trị cực trị (extreme values), mang lại hiệu quả đặc biệt rõ rệt đối với các tập dữ liệu có mức độ nhiễu cao (high noise levels).
- Giá trị biến đổi trung bình trượt $MA_t$ được tính toán theo Equation (2):
  $$MA_t = \frac{x_{n-t+1} + x_{n-t+2} + \dots + x_n}{t} = \frac{1}{t} \sum_{i=n-t+1}^{n} x_i \tag{2}$$
  - $MA_t$: giá trị trung bình trượt tính tại bước thời gian hiện tại $n$ ứng với kích thước cửa sổ thời gian trễ $t$.
  - $t$: khoảng thời gian trễ hoặc độ dài của cửa sổ trượt (time window / delay interval) dùng để gom nhóm các quan sát lịch sử.
  - $x_n$: giá trị đặc trưng ghi nhận tại thời điểm hiện tại $n$.
  - $x_{n-t+1}, x_{n-t+2}, \dots, x_n$: chuỗi $t$ giá trị quan sát liên tiếp được thu thập trong khoảng thời gian từ bước $n-t+1$ đến bước $n$.
  - $\frac{1}{t} \sum_{i=n-t+1}^{n} x_i$: biểu thức tổng quát của phép tính trung bình số học trên cửa sổ thời gian kích thước $t$.
