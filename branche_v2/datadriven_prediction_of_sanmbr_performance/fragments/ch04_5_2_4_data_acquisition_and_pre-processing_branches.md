### 2.4 Data Acquisition and Pre-processing

- **Thu thập dữ liệu và kỹ thuật tiền xử lý đặc trưng**:
  - Tập dữ liệu gồm $189$ mẫu dữ liệu hàng ngày đại diện cho toàn bộ chu kỳ thử nghiệm.
  - $6$ biến đầu vào được lựa chọn: COD đầu vào ($COD_{in}$), nồng độ $2,4	ext{-DCP}$, pH, độ đục đầu vào, $OLR$, và thời gian vận hành ($Time$).
  - Loại bỏ các điểm ngoại lai ($outliers$) dựa trên khoảng tứ phân vị ($IQR$) và điền khuyết bằng nội suy tuyến tính.
