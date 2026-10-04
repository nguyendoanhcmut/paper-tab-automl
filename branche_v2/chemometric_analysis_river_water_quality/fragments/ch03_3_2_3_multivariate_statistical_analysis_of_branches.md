### 2.3. Multivariate statistical analysis of water quality parameters at the intake of the SJD DWTP using principal component analysis

- Cấu trúc bảng dữ liệu hai chiều (two-dimensional data tables) tích hợp số liệu từ cảm biến trực tuyến (on-line sensors) và phân tích phòng thí nghiệm (laboratory assays) phục vụ phân tích đa biến:
  - Số lượng lớn các mẫu đo được tạo ra đồng thời từ hệ thống cảm biến và xét nghiệm hóa nghiệm, hỗ trợ đánh giá các quy luật chất lượng nước sông tự nhiên và nhận diện các sự kiện bất thường nhằm cải tiến quy trình xử lý tại các nhà máy nước uống (DWTP - Drinking Water Treatment Plant).
  - Dữ liệu được lưu trữ dưới dạng ma trận hai chiều $\mathbf{D}$ kích thước $I \times J$:
    - Các hàng đại diện cho các quan trắc hoặc phép đo (observations/measurements), sắp xếp theo thời gian hoặc theo số hiệu mẫu.
    - Các cột đại diện cho các thông số hoặc biến số được đo lường (measured parameters/variables).
  - Cấu trúc ma trận hai chiều tương thích với các thuật toán thống kê đa biến (multivariate statistical methods) và hóa trắc lượng (chemometrics).

- Phân tích thành phần chính (PCA - Principal Component Analysis) mô hình hóa cấu trúc phương sai và các yếu tố ẩn chi phối chất lượng nguồn nước:
  - Phương pháp PCA (theo Jolliffe, 2002) là công cụ thống kê đa biến phổ biến trong phân tích dữ liệu môi trường.
  - Giả định cốt lõi của PCA: trong tập dữ liệu gốc tồn tại một số lượng nhỏ các nhân tố chi phối có ảnh hưởng lớn (dominant factors / components) đóng vai trò là nguồn biến thiên chính của hệ thống.
  - Các nhân tố này được gọi là yếu tố ẩn (hidden factors) vì không thể đo lường trực tiếp bằng một cảm biến đơn lẻ hoặc quan sát thực nghiệm riêng biệt.
  - Năng lực phân tích của PCA đối với dữ liệu quan trắc chất lượng nước:
    - Điều tra các quy luật và xu hướng biến thiên theo thời gian và theo mùa (temporal/seasonal patterns/trends).
    - Phân tích tác động khí tượng (meteorological patterns) và các xu hướng ô nhiễm (pollution trends).
    - Mô hình hóa mối quan hệ và tương tác phức tạp giữa nhiều thông số môi trường và các quan trắc mẫu.
    - Làm sáng tỏ các tiến trình bản chất ẩn sâu bên dưới hệ thống giám sát chất lượng nước tại trạm thu nước thô của nhà máy DWTP.

- Mô hình phân tích song tuyến tính (bilinear model) phân rã ma trận dữ liệu thành ma trận điểm số (scores), tải trọng (loadings) và phần dư (residuals):
  - Ma trận dữ liệu thực nghiệm ban đầu $\mathbf{D}$ được phân rã theo Phương trình (1):
    $$\mathbf{D} = \mathbf{T}\mathbf{P}^T + \mathbf{E}$$
    trong đó:
    - $\mathbf{D}$ là ma trận dữ liệu thực nghiệm ban đầu kích thước $I \times J$ ($I$ mẫu đo, $J$ biến số).
    - $\mathbf{T}$ là ma trận điểm số (scores matrix, kích thước $I \times K$), thực hiện ánh xạ các mẫu quan sát lên các thành phần chính.
    - $\mathbf{P}^T$ là chuyển vị của ma trận tải trọng (loadings matrix, kích thước $K \times J$), thực hiện ánh xạ các biến đo lường lên các trục thành phần chính.
    - $\mathbf{E}$ là ma trận phần dư (residuals matrix, kích thước $I \times J$), biểu diễn phần phương sai không được giải thích bởi mô hình (unexplained variance).
  - Hai ma trận $\mathbf{T}$ và $\mathbf{P}$ là các ma trận trực giao (orthogonal matrices), liên hệ trực tiếp với phép phân tích giá trị kỳ dị (SVD - Singular Value Decomposition) trên ma trận dữ liệu đã chuẩn hóa.

- Tiêu chí lựa chọn số lượng thành phần chính ($K$) và ý nghĩa vật lý của điểm số và tải trọng:
  - Số lượng thành phần chính được giữ lại trong mô hình PCA (tương ứng với các cột của $\mathbf{T}$ và các hàng của $\mathbf{P}^T$) được xác định dựa trên hai tiêu chuẩn:
    - a) Kích thước của các giá trị riêng (eigenvalues) gắn liền với từng thành phần chính.
    - b) Khả năng giải thích có ý nghĩa thực tế về mặt môi trường (meaningful environmental explanation) của các hồ sơ điểm số và tải trọng.
  - Chức năng biểu diễn của ma trận tải trọng $\mathbf{P}^T$ và ma trận điểm số $\mathbf{T}$:
    - Tải trọng $\mathbf{P}^T$ thể hiện các hồ sơ hóa lý (physicochemical profiles) của các thành phần chính, phản ánh trọng số đóng góp của từng thông số chất lượng nước vào mỗi trục thành phần.
    - Điểm số $\mathbf{T}$ biểu diễn hình chiếu của các mẫu quan sát lên các thành phần chính, cung cấp thông tin về phân bố thời gian (temporal distribution / time distribution) của các phép đo.
    - Phân bố thời gian của các điểm số bộc lộ các xu hướng tiềm ẩn, làm cơ sở để tiến hành phân tích chuỗi thời gian (time series analysis).

- Đồ thị phần dư Q (Q residuals chart) phát hiện các sự kiện ô nhiễm và xáo trộn bất thường tại trạm thu nước thô:
  - Nghiên cứu áp dụng biểu đồ phần dư Q để phát hiện các sự kiện bất thường (unusual events) tại trạm thu nước thô của nhà máy nước Sant Joan Despí (SJD DWTP).
  - Phần dư Q đo lường sự khác biệt giữa các giá trị đo thực tế và hình chiếu của chúng lên $K$ thành phần chính được giữ lại trong mô hình PCA theo dòng thời gian:
    $$Q_i = \mathbf{e}_i \mathbf{e}_i^T = \sum_{j=1}^{J} e_{ij}^2$$
    trong đó $\mathbf{e}_i$ là vectơ hàng thứ $i$ của ma trận phần dư $\mathbf{E}$ cho mẫu thứ $i$.
  - Giá trị phần dư Q phản ánh mức độ phù hợp của một phép đo cụ thể đối với mô hình PCA:
    - Các mẫu có giá trị phần dư lớn biểu thị rằng thông tin của mẫu không được giải thích tốt bởi mô hình chuẩn, được định danh là các sự kiện bất thường (unusual events / outlying events).
    - Khi chất lượng nước tại trạm thu ở trạng thái ổn định và được kiểm soát, giá trị phần dư Q duy trì ở mức thấp.

- Biểu đồ đóng góp Q (Q contribution plot) định danh các thông số chất lượng nước đóng góp chính vào sự kiện bất thường:
  - Khi một phép đo được đánh dấu là sự kiện bất thường (flagged as an event), biểu đồ đóng góp Q (theo Wise và Gallagher, 1996) được sử dụng để phân tích nguyên nhân.
  - Biểu đồ đóng góp Q biểu diễn một hàng $\mathbf{e}_i$ của ma trận phần dư $\mathbf{E}$ ứng với mẫu sự kiện được xem xét:
    - Đồ thị thể hiện mức độ đóng góp của từng biến số hoặc thông số vào giá trị Q tổng thể của mẫu đó.
    - Đóng góp của từng biến số giữ nguyên dấu đại số (retaining the sign of the contribution), cho biết thông số tăng cao hay suy giảm so với tương quan thông thường.
  - Phân tích trực quan đóng góp Q giúp xác định chính xác thông số nào đóng góp nhiều nhất vào tổng bình phương sai số phần dư (sum-squared residual error) của mẫu sự kiện (theo Wise và cộng sự, 1989).

- Giới hạn tin cậy thống kê (confidence limits) thiết lập ngưỡng ranh giới phát hiện sai lệch:
  - Các giới hạn tin cậy được tính toán để cung cấp giá trị ngưỡng phân định giữa điều kiện vận hành bình thường và điều kiện bất thường ngoại lai (regular/outlying conditions).
  - Trạng thái kiểm soát bình thường (in-control): khi chất lượng nước tại trạm thu nằm trong tầm kiểm soát, các giá trị phần dư Q dao động ở mức nhỏ bên trong các giới hạn tin cậy ($Q \le Q_{\text{threshold}}$).
  - Trạng thái bất thường ngoại lai (outlying events): các sự kiện bất thường hiển thị với giá trị phần dư Q vượt ra ngoài giới hạn tin cậy ($Q > Q_{\text{threshold}}$), đóng vai trò như công cụ cảnh báo sớm cho công tác vận hành nhà máy xử lý nước.
