### 2.2. Preprocessing data

- **Quy trình tiền xử lý dữ liệu (data preprocessing)**: Chuẩn hóa dữ liệu (data normalization) và phân chia dữ liệu (data division) được thực hiện trước khi phát triển mô hình mạng nơ-ron (neural network model).
- **Chuẩn hóa dữ liệu (data normalization)**:
  - Do dữ liệu đầu vào của hệ thống SMBR (Submerged Membrane Bioreactor) bao gồm các biến có độ lớn (magnitudes) và thang đo (scales) khác nhau, toàn bộ tập dữ liệu được co giãn (scaled) về phạm vi $0\text{--}1$.
  - Mục đích chuẩn hóa:
    - Ngăn ngừa tình trạng các dữ liệu đầu vào gốc có giá trị lớn chi phối/áp đảo nghiệm giải thuật (dominance of large original input data in the solution).
    - Giảm thiểu các thách thức về mặt số học (numerical challenges) trong quá trình tính toán (Kumar $2011$).
  - Công thức chuẩn hóa (Equation $(2)$):
    $$X_0 = \frac{y_i - y_{\min}}{y_{\max} - y_{\min}} \quad (2)$$
    - $X_0$: Giá trị sau chuẩn hóa (scaled value).
    - $y_i$: Giá trị thực tế thứ $i$ của dữ liệu ($i^{\text{th}}$ actual value of the data).
    - $y_{\max}$: Giá trị lớn nhất của dữ liệu (maximum value of the data).
    - $y_{\min}$: Giá trị nhỏ nhất của dữ liệu (minimum value of the data).
- **Phân chia dữ liệu (data division)**:
  - Nhằm đánh giá tính khả thi của mô hình dự đoán (predictive model), toàn bộ dữ liệu được phân chia ngẫu nhiên (randomly divided) thành hai phần: tập dữ liệu huấn luyện ($T_{\text{training}}$ / training dataset) chiếm $60\%$ và tập dữ liệu kiểm thử ($T_{\text{testing}}$ / testing dataset) chiếm $40\%$.
  - Tập dữ liệu huấn luyện ($T_{\text{training}}$):
    - Được sử dụng để huấn luyện mạng (network training) và đánh giá mô hình.
    - Dùng để tinh chỉnh siêu tham số (hyperparameter tuning) và đánh giá hiệu năng mạng (network performance).
    - Quy trình tinh chỉnh siêu tham số được lặp lại $3$ lần, tính sai số toàn phương trung bình (MSE - Mean Squared Error) trung bình, từ đó lựa chọn bộ siêu tham số mang lại MSE tối thiểu (minimum MSE).
  - Tập dữ liệu kiểm thử ($T_{\text{testing}}$):
    - Được sử dụng để kiểm định/xác thực hiệu năng mạng (validate network performance).
    - Cung cấp một ước lượng khách quan, không thiên vị (unbiased estimate) về hiệu năng của mô hình trên dữ liệu chưa từng thấy (unseen data).
