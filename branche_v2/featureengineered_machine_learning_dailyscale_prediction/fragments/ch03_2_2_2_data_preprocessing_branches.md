### 2.2 Data preprocessing

- Sàng lọc và loại bỏ dữ liệu ngoại lai bằng quy tắc ba độ lệch chuẩn ($3\sigma$):
  - Áp dụng trên toàn bộ các thông số vận hành và chỉ tiêu chất lượng nước trước khi huấn luyện mô hình.
  - Các bản ghi nằm ngoài khoảng $\pm 3\sigma$ quanh giá trị trung bình đại diện cho lỗi cảm biến, sự cố thiết bị hoặc xáo trộn vận hành cực đoan được loại bỏ để bảo đảm tính ổn định.
- Điền khuyết dữ liệu chuỗi thời gian bằng thuật toán MICE (Multivariate Imputation by Chained Equations):
  - Thuật toán mô hình hóa có điều kiện từng biến chứa giá trị khuyết $X_j$ dựa trên phân phối hồi quy phụ thuộc vào tất cả các biến còn lại $X_{-j}$:
    $$X_j^{\text{mis}} \sim f_j(X_{-j}; \theta_j)$$
  - Quá trình điền khuyết cập nhật lặp qua chuỗi phương trình liên hoàn:
    $$\hat{X}^{(t)} = F(\hat{X}^{(t-1)})$$
    trong đó $\hat{X}^{(t)}$ là ma trận dữ liệu được làm đầy tại vòng lặp $t$.
  - Thuật toán lặp đến khi hội tụ nhằm bảo toàn cấu trúc tương quan đa biến phức tạp giữa các yếu tố khí tượng, thủy lực và chất lượng nước.
- Đặc trưng thiết kế và vận hành trạm xử lý DAF quy mô thực:
  - Công suất thiết kế đạt $410{,}000\ \text{m}^3/\text{ngày}$ với quy trình sinh học Modified Ludzack–Ettinger (MLE).
  - Hệ thống tuyển nổi DAF đóng vai trò công đoạn xử lý hóa lý bậc ba cốt lõi nhằm khử photpho.
  - Hóa chất keo tụ sử dụng là phèn sắt ferric sulfate $Fe_2(SO_4)_3$.
  - Chu kỳ ra quyết định điều chỉnh hóa chất thực hiện theo ngày dựa trên kết quả phân tích phòng thí nghiệm trong chuỗi dữ liệu 3 năm ($N = 1{,}096\ \text{ngày}$).
- Chiến lược kỹ nghệ đặc trưng tích hợp tri thức cơ chế và động học vận hành thực tế:
  - Đặc trưng biến động ngắn hạn (short-term variation metrics): Tính toán sai phân nồng độ $T\text{-}P$ đầu ra tại các độ trễ 1 ngày ($\Delta T\text{-}P_{t-1}$), 2 ngày ($\Delta T\text{-}P_{t-2}$) và 3 ngày ($\Delta T\text{-}P_{t-3}$).
  - Các biến sai phân nắm bắt kịp thời chiều hướng và biên độ dao động nhanh do mưa rửa trôi, châm thiếu phèn cục bộ hoặc biến đổi đặc tính hạt bông cặn.
  - Nguyên tắc phòng ngừa rò rỉ dữ liệu (data leakage): Toàn bộ biến trễ và sai phân chỉ tính toán từ dữ liệu sẵn có trước thời điểm dự báo.
  - Đặc trưng cơ chế vận hành DAF: Tỷ lệ cấp khí trên lưu lượng nước vào ($\text{DAF\_A/F}$), lưu lượng châm phèn sắt $Fe_2(SO_4)_3$, lưu lượng vào DAF và lưu lượng tuần hoàn nội bộ (IRFR).
  - Đặc trưng môi trường và khí hậu bên ngoài: Nhiệt độ không khí, lượng mưa tích lũy và chỉ số tháng phản ánh biến thiên nhiệt độ ảnh hưởng tới động học keo tụ.
  - Đặc trưng chất lượng nước đầu vào: Nồng độ $T\text{-}P$ đầu vào và chất rắn lơ lửng ($\text{SS}$) đầu vào trực tiếp quyết định nhu cầu tiêu hao chất keo tụ.
