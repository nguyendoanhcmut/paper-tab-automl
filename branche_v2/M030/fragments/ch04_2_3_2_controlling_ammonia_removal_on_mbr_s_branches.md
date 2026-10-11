### 3.2. Controlling ammonia removal on MBR systems

#### 3.2.1. Detecting low ammonia removal conditions

- Áp dụng mô hình MSPC-PCA (Multivariate Statistical Process Control - Phân tích thành phần chính để kiểm soát quá trình thống kê đa biến) trên cơ sở dữ liệu nhằm theo dõi hiệu suất MBR về khả năng loại bỏ amoni theo thời gian và phát hiện các sự kiện bất thường dẫn đến hiệu suất loại bỏ thấp:
  - Phương pháp chiếu PCA (Principal Component Analysis) giữ lại 3 thành phần chính (PC - Principal Components) dựa trên cả tiêu chuẩn Kaiser (Kaiser criterion) và kiểm định đồ thị lắng đọng (scree test).
  - Ba PC giữ lại giải thích hơn $50\ \%$ tổng biến thiên dữ liệu (data variation).
- Biểu đồ kiểm soát đa biến Hotelling $T^2$ và $Q$, cùng với giá trị phần trăm loại bỏ amoni của từng mẫu trong Giai đoạn II (Phase II), được thiết lập để theo dõi quá trình:
  - **Hình 9.** Phát hiện suy giảm hiệu suất loại bỏ amoni trong MBR
    - <img src="assets/fig_09_p10.jpeg" alt="Hình 9" />
    - **Hình này chứng minh điều gì**
      - Các chu kỳ suy giảm amoni (mẫu 358–362 và 385–405, rơi xuống thấp nhất $\sim 56\ \%$) trùng khớp đồng bộ với cụm vi phạm $\text{UCL}$ trên biểu đồ $Q$.
    - **Từ đâu mà thấy được**
      - Panel (a): Biểu đồ $T^2$ có đường $\text{UCL} \approx 9.5$; đa số điểm tại các mẫu 358–362 và 385–405 đều nằm dưới ngưỡng.
      - Panel (b): Biểu đồ $Q$ có đường $\text{UCL} \approx 18$; cụm chấm đỏ ($Q > \text{UCL}$, đỉnh $\sim 68$) bùng phát tại mẫu 358–362 và 385–405.
      - Panel (c): Biểu đồ hiệu suất có đường ngưỡng $90\ \%$; các chấm đỏ ($\text{Rem} < 90$) giảm sâu xuống $\sim 78\ \%$ và chạm đáy $\sim 56\ \%$ (mẫu $\sim 395$).
- Biểu đồ kiểm soát Hotelling $T^2$ thể hiện hiệu quả kém trong việc phát hiện điều kiện vận hành có hiệu suất loại bỏ amoni thấp:
  - Tỷ lệ phát hiện (detection rate) các mẫu có hiệu suất loại bỏ amoni dưới $90\ \%$ của biểu đồ $T^2$ chỉ đạt $11\ \%$.
  - Thống kê $T^2$ kiểm tra xem một quan trắc mới khi chiếu lên siêu phẳng của các PC (PC hyperplane) có nằm trong các giới hạn xác định bởi dữ liệu tham chiếu hay không.
  - Giá trị $T^2$ vượt quá giới hạn kiểm soát cho thấy quan trắc có giá trị bất thường ở một số biến ban đầu nhưng vẫn duy trì cấu trúc tương quan giữa các biến trong mô hình (được định danh là điểm ngoại lai bên trong mô hình PCA - outlier inside the PCA model) [53,72].
  - Tỷ lệ phát hiện thấp của $T^2$ có thể bắt nguồn từ sự phá vỡ cấu trúc tương quan của mô hình ở các mẫu nằm ngoài tầm kiểm soát (out-of-control samples).
- Biểu đồ kiểm soát $Q$ (SPE - Squared Prediction Error) chứng minh khả năng phát hiện vượt trội đối với các điều kiện suy giảm hiệu suất loại bỏ amoni:
  - Thống kê $Q$ kiểm tra sự xuất hiện của các sự kiện mới làm quá trình dịch chuyển ra khỏi siêu phẳng được xác định bởi mô hình tham chiếu.
  - Biểu đồ $Q$ phát hiện được $54\ \%$ các trường hợp vận hành có tỷ lệ loại bỏ amoni dưới $90\ \%$ (nhận diện các điểm ngoại lai bên ngoài mô hình - outliers outside the model).
  - Độ nhạy phát hiện đạt $100\ \%$ đối với tất cả các điểm vận hành có hiệu suất loại bỏ amoni giảm xuống dưới $85\ %$.
  - Ý nghĩa đối với kiểm soát vận hành: Khả năng phát hiện sớm giúp ngăn ngừa hiệu suất loại bỏ amoni rơi xuống các mức cực kỳ thấp và định hướng thời điểm can thiệp thích hợp nhất vào hệ thống.
  - Tiềm năng nâng cao độ nhạy: Kết quả chỉ ra rằng với các hiệu chỉnh tốt hơn trong mô hình hoặc tập dữ liệu đầu vào mang tính đại diện cao hơn, tỷ lệ phát hiện các điều kiện có hiệu suất loại bỏ dưới $90\ \%$ có thể tiếp tục được nâng cao.
- Cả hai thống kê kiểm soát đều duy trì tỷ lệ báo động giả (false alarms) ở mức rất thấp:
  - Tỷ lệ báo động giả chỉ là $3\ \%$ ở biểu đồ $T^2$ và $1\ \%$ ở biểu đồ $Q$.
  - Các sai số này là tất yếu do xác suất thống kê định trước của phương pháp ($5\ \%$).
- Ứng dụng MSPC thông qua biểu đồ kiểm soát $Q$ là công cụ hữu ích cho việc giám sát và kiểm soát loại bỏ amoni trên hệ thống MBR:
  - Cho phép can thiệp phòng ngừa và quyết đoán hơn vào hệ thống khi phát hiện xu hướng suy giảm hiệu suất.
  - Tránh phát sinh các chi phí vận hành không cần thiết.
  - Nâng cao chất lượng nước sau xử lý và cải thiện hiệu quả tổng thể của MBR.

#### 3.2.2. Diagnosing low ammonia removal conditions

- Đồ thị đóng góp (contribution plot) dựa trên thống kê $Q$ được thiết lập nhằm điều tra các nguyên nhân dẫn đến hiệu suất loại bỏ amoni thấp trong quá trình giám sát vận hành MBR:
  - Do thống kê $Q$ vượt trội trong việc phát hiện vận hành loại bỏ amoni thấp, nó được lựa chọn để phân tích đóng góp biến.
  - Tương tự như phân tích độ nhạy, chỉ có 10 biến quan trọng nhất được hiển thị để đơn giản hóa đồ thị chẩn đoán:
  - **Hình 10.** Đồ thị đóng góp thống kê Q khi mất kiểm soát
    - <img src="assets/fig_10_p11.jpeg" alt="Hình 10" />
    - **Hình này chứng minh điều gì**
      - Ba thông số SRT, fCOD và temp luôn chiếm tỷ trọng đóng góp chủ đạo vào thống kê Q trên toàn bộ 25 mẫu quan trắc mất kiểm soát.
    - **Từ đâu mà thấy được**
      - Ox: mẫu quan trắc (Sample) $345$–$413$. Oy: tỷ lệ đóng góp (Contribution), thang đo $0\%$–$100\%$.
      - Ba dải màu dưới cùng gồm SRT (tím đậm, $\sim 15\text{--}22\%$), fCOD (tím nhạt, $\sim 15\text{--}20\%$) và temp (cam đậm, $\sim 13\text{--}18\%$), cộng dồn luôn vượt $50\%$ chiều cao mỗi cột.
- Ba biến số đóng góp lớn nhất vào các giá trị vượt ngưỡng của thống kê $Q$ là nồng độ COD dòng vào (fCOD - influent COD), thời gian lưu bùn (SRT - Sludge Retention Time) và nhiệt độ (temperature - temp):
  - Ba biến này có ảnh hưởng mạnh nhất đến sự suy giảm loại bỏ amoni, củng cố và đồng thuận với các kết quả thu được từ mô hình PCA và mạng nơ-ron nhân tạo (ANN - Artificial Neural Network).
  - Kết quả khẳng định vai trò quyết định của tỷ lệ C/N (C/N ratio) đối với quá trình kiểm soát loại bỏ amoni.
  - Nhấn mạnh tầm quan trọng của việc duy trì hệ thống vận hành ở nhiệt độ và SRT phù hợp: giá trị COD đầu vào cao kết hợp với SRT ngắn và nhiệt độ thấp là những nguyên nhân phổ biến nhất gây ra sự suy giảm tỷ lệ loại bỏ amoni trong MBR.
- Nghiên cứu sự phối hợp giữa các yếu tố vận hành để tìm điểm cân bằng là điều cần thiết trong thực tế kỹ thuật:
  - Trong thực tế vận hành, không phải lúc nào cũng có thể duy trì đồng thời tất cả các thông số trong phạm vi mong muốn.
  - Nghiên cứu của Stewart et al. [73] trên hai chuỗi xử lý loại bỏ chất dinh dưỡng sinh học (BNR - Biological Nutrient Removal) quy mô pilot cho thấy việc tăng SRT trong giai đoạn nhiệt độ nước lạnh giúp bù đắp và duy trì hiệu suất loại bỏ amoni.
- Áp dụng kiểm định thống kê phi tham số Wilcoxon-Mann-Whitney [74] ở mức ý nghĩa 1 % (hình ghi p < 0.01%) để kiểm tra xem giá trị trung vị của các biến gồm hiệu suất loại bỏ amoni, nhiệt độ, SRT và COD dòng vào có khác biệt đáng kể giữa trạng thái vận hành trong kiểm soát (in-control) và ngoài kiểm soát (out-of-control) hay không:
  - **Hình 11.** Kiểm định Wilcoxon-Mann-Whitney cho hai trạng thái vận hành
    - <img src="assets/fig_11_p11.jpeg" alt="Hình 11" />
    - **Hình này chứng minh điều gì**
      - Hiệu suất khử amoni và nhiệt độ giảm rõ rệt khi mất kiểm soát, củng cố sự phân tách trên cả 4 biến.
    - **Từ đâu mà thấy được**
      - Panels A, C: Khử amoni giảm từ trung vị $\sim 97\ \%$ xuống $\sim 88\ \%$; nhiệt độ giảm từ $\sim 29.5\ ^\circ\text{C}$ xuống $\sim 25\ ^\circ\text{C}$.
      - Panels B, D: SRT bị ghìm ở mức đáy $30\text{ d}$; COD đầu vào tăng từ trung vị $\sim 420\text{ mg/L}$ lên $\sim 610\text{ mg/L}$ (ngoại lai $> 1200\text{ mg/L}$).
      - Lưu ý: hình ghi p < 0.01%, văn bản ghi 1 %.
- Kết quả kiểm định giả thuyết (các giá trị $p\text{-value}$ chi tiết được trình bày trong Phụ lục A) xác nhận tính phân tách có ý nghĩa thống kê giữa hai trạng thái vận hành:
  - Giá trị của hiệu suất loại bỏ amoni, nhiệt độ và SRT ở trạng thái mất kiểm soát (out-of-control) thấp hơn rõ rệt và có ý nghĩa thống kê so với trạng thái kiểm soát (in-control).
  - Giá trị nồng độ COD dòng vào ở trạng thái mất kiểm soát cao hơn rõ rệt và có ý nghĩa thống kê so với trạng thái kiểm soát.
  - Kết quả kiểm định khẳng định và củng cố vững chắc các kết luận chẩn đoán rút ra từ phân tích thành phần chính, mô hình mạng nơ-ron và đồ thị đóng góp của thống kê $Q$.
