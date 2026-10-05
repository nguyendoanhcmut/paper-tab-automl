### 2.2 Data collection and processing

- Thu thập dữ liệu chất lượng nước và xác định các biến đặc trưng hệ thống:
  - Chất lượng nước sau xử lý được đo đạc theo các quy trình tiêu chuẩn cho các hợp chất nitơ và hàm lượng hữu cơ.
  - Các thông số hiện trường như $DO$ và $pH$ được đo bằng thiết bị đo cầm tay HI98191 (Hanna Instruments, Ý).
  - Lưu lượng bơm nhu động được điều chỉnh để kiểm soát chính xác thời gian lưu nước thủy lực ($HRT$).
  - Bộ dữ liệu quan trắc hoàn chỉnh gồm $15$ thông số đặc trưng then chốt:
    - Hai biến mục tiêu đầu ra: amoni đầu ra ($NH_4^+\text{-N}_{out}$) và tổng nitơ đầu ra ($TN_{out}$).
    - Mười ba biến đầu vào: độ mặn ($salinity$), $DO$, $HRT$, $pH$, nhiệt độ ($Temp$), $COD_{in}$, $COD_{out}$, $NH_4^+\text{-N}_{in}$, $NO_2^-\text{-N}_{out}$, $NO_3^-\text{-N}_{out}$, tỷ lệ $C/N$, hiệu suất $COD_{eff}$ và hiệu suất $TN_{eff}$.
- Tiền xử lý dữ liệu thực nghiệm và phân chia tập dữ liệu huấn luyện:
  - Loại bỏ các mẫu trùng lặp và làm sạch tập dữ liệu để ngăn ngừa hiện tượng rò rỉ dữ liệu ($data\ leakage$).
  - Chuẩn hóa các biến đặc trưng đầu vào bằng các kỹ thuật biến đổi chuẩn của thư viện Scikit-learn.
  - Sử dụng phương pháp điểm Z ($Z\text{-score}$) để phát hiện điểm dị biệt và loại bỏ các giá trị ngoại lai vượt ngưỡng $3$.
  - Áp dụng kỹ thuật phân vị Winsor ($winsorization$) để chặn các giá trị nằm ngoài bách phân vị thứ $1$ và thứ $99$.
  - Tập dữ liệu tinh chế cuối cùng thu được tổng cộng $570$ mẫu thực nghiệm hoàn chỉnh.
  - Phân chia ngẫu nhiên dữ liệu với tỷ lệ $80\%$ dành cho tập huấn luyện và $20\%$ dành cho tập kiểm tra độc lập.
- Đánh giá tương quan Pearson tuyến tính giữa các biến:
  - Hệ số tương quan Pearson đối với $NH_4^+\text{-N}_{out}$ dao động trong dải hẹp từ $-0.05$ đến $0.22$.
  - Hệ số tương quan Pearson đối với $TN_{out}$ phân bố trong khoảng từ $-0.52$ đến $0.26$.
  - Mối liên hệ tuyến tính yếu giữa nồng độ nitơ đầu ra và các biến vận hành đòi hỏi phải sử dụng các thuật toán học máy phi tuyến.
