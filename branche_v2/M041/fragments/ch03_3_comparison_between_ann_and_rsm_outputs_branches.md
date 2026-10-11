### Comparison between ANN and RSM outputs

* **So sánh trực quan giữa dữ liệu thực nghiệm và kết quả mô hình hóa ANN và RSM (trang 10–11)**:
    * Hình 8 so sánh trực tiếp dữ liệu thực nghiệm phòng thí nghiệm (laboratory / actual data) với kết quả mô phỏng từ hai mô hình mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) và phương pháp bề mặt đáp ứng (Response Surface Methodology - RSM).
    * **Hiệu năng dự đoán nồng độ và hiệu suất loại bỏ Ammonia Nitrogen theo $\text{pH}$ (Hình 8a)**:
        * Các giá trị đầu ra của mô hình ANN thể hiện năng lực dự báo vượt trội (superior predictive capability) đối với dữ liệu thực nghiệm, đặc biệt rõ nét ở các giai đoạn ban đầu (initial stages) của từng xu hướng biến thiên cho cả hai thông số phụ thuộc: nồng độ Ammonia Nitrogen và hiệu suất loại bỏ (dựa trên $\text{pH}$).
    * **Mối quan hệ giữa nồng độ Phosphate và hiệu suất loại bỏ theo $\text{pH}$ (Hình 8b)**:
        * Biểu diễn tương quan giữa nồng độ Phosphate và hiệu suất khử dựa trên $\text{pH}$; ngoại trừ điểm dữ liệu ở khoảng giữa (middle data point) có độ lệch khỏi xu hướng chung, cả hai mô hình ANN và RSM đều thể hiện năng lực dự đoán mạnh mẽ đối với dữ liệu thực nghiệm.
    * **Độ chính xác vượt bậc của ANN đối với Ammonia Nitrogen theo $\text{TOC}$ (Hình 8c)**:
        * Mô hình ANN thể hiện hiệu năng xuất sắc khi dự đoán chính xác dữ liệu tại mọi điểm khảo sát (at all points).
        * Ngược lại, mô hình RSM gặp nhiều khó khăn trong việc dự báo chính xác dữ liệu thực nghiệm, đặc biệt ở các điểm dữ liệu ban đầu (initial points).
    * **Hiệu năng dự báo Phosphate và hiệu suất loại bỏ theo $\text{TOC}$ (Hình 8d)**:
        * Mặc dù cả hai mô hình đều có năng lực dự đoán bị hạn chế đối với dữ liệu phòng thí nghiệm ở một số vùng cục bộ, mô hình ANN vẫn thể hiện độ chuẩn xác vượt trội (superior accuracy) trong việc tái hiện tập dữ liệu thực nghiệm.
    * **Hình 8.** So sánh đầu ra ANN và RSM với dữ liệu thực nghiệm
      * <img src="assets/fig_09_p11.png" alt="Hình 8" />
      * **Hình này chứng minh điều gì**
        * Đường ANN bám sát dữ liệu thực nghiệm nồng độ và hiệu suất xử lý ammonia nitrogen lẫn phosphate theo pH và TOC.
      * **Từ đâu mà thấy được**
        * Ox: số thứ tự mẫu theo pH (a, b) hoặc TOC (c, d); Oy: nồng độ và hiệu suất xử lý.
        * Ký hiệu ANN (hình vuông) bám khít điểm thực nghiệm (hình tròn), trong khi đường RSM lệch tại các đỉnh cực trị.
* **Cơ chế sinh học và động thái $\text{pH}$ trong bioreactor vi tảo**:
    * Hoạt tính quang hợp (photosynthetic activity) của vi tảo có thể làm tăng rõ rệt giá trị $\text{pH}$ trong môi trường nuôi cấy do tiêu thụ $\text{CO}_2$ hòa tan.
    * Giá trị $\text{pH}$ quan sát được trong bioreactor vận hành liên tục (continuous bioreactor) thấp hơn so với trong quang phản ứng mẻ luân phiên (sequencing batch photoreactor - SBPR), phản ánh việc nuôi cấy vi tảo liên tục trong lò phản ứng hỗ trợ sự phát triển và sinh trưởng của chúng hiệu quả hơn.
    * Ngưỡng $\text{pH}$ tối ưu có sự khác biệt giữa các loài vi tảo khác nhau; trong đó sản lượng của vi tảo *Chlorella* trong photobioreactor xử lý nước thải ngành sữa (dairy effluent) đạt mức tối đa tại dải $\text{pH}$ từ $6.3\text{ -- }7.5$.
* **Đánh giá định lượng hiệu năng mô hình qua các chỉ số thống kê (Bảng 3)**:
    * Mặc dù Hình 8 minh họa trực quan sự trùng khớp chặt chẽ giữa thực nghiệm và mô hình, đánh giá định lượng cung cấp một sự so sánh khoa học và nghiêm ngặt hơn (rigorous comparison).
    * Căn cứ vào các chỉ số thống kê trong Bảng 3, mô hình ANN nhất quán vượt trội hơn mô hình RSM trên tất cả các biến đáp ứng (across all response variables).
    * **So sánh định lượng trên biến nồng độ Ammonia Nitrogen**:
        * Mô hình ANN đạt sai số toàn phương trung bình $\text{RMSE} = 0.189$ và sai số tuyệt đối trung bình $\text{MAE} = 0.142$.
        * Mức sai số này đại diện cho sự suy giảm sai số khoảng $41\%$ so với mô hình RSM ($\text{RMSE} = 0.324$, $\text{MAE} = 0.281$).
        * Hệ số xác định $R^2$ của ANN đạt $0.9979$, cao hơn rõ rệt so với $R^2 = 0.9733$ của mô hình RSM.
    * **So sánh định lượng trên biến nồng độ Phosphate**:
        * Mô hình ANN đạt sai số cực thấp với $\text{RMSE} = 0.166$ và $\text{MAE} = 0.118$.
        * Mô hình RSM ghi nhận sai số lớn hơn đáng kể với $\text{RMSE} = 0.251$ và $\text{MAE} = 0.215$.
        * Hệ số xác định $R^2$ của ANN đạt $0.9972$, vượt trội so với $R^2 = 0.9608$ của RSM.
    * **Bảng 3.** So sánh định lượng các chỉ số thống kê giữa ANN và RSM
      * <img src="assets/table_03_p18.png" alt="Bảng 3" />
      * **Bảng này chứng minh điều gì**
        * ANN đạt độ chuẩn xác dự báo vượt trội trên cả Ammonia nitrogen và Phosphate với $R^2 > 0.997$ và sai số giảm gần một nửa.
      * **Từ đâu mà thấy được**
        * Cột $R^2$: hàng ANN đạt $0.9979$ (Ammonia nitrogen) và $0.9972$ (Phosphate), cao hơn rõ rệt so với RSM ($0.9733$ và $0.9608$).
        * Cột RMSE và MAE: hàng ANN ghi nhận sai số thấp nhất ở cả hai biến, với RMSE $0.189$ / $0.166$ và MAE $0.142$ / $0.118$.
* **Phân tích phân bố sai số phần dư và ưu thế vượt trội của ANN phi tuyến so với RSM đa thức bậc hai (Hình 9)**:
    * Sự khác biệt về độ chuẩn xác dự báo giữa hai mô hình được trực quan hóa sâu sắc qua biểu đồ tần số sai số phần dư (residual error distribution histogram, $y_{\text{pred}} - y_{\text{exp}}$) trong Hình 9.
    * **Phân bố sai số của mô hình ANN**:
        * Sai số phần dư của ANN tuân theo phân bố chuẩn (normally distributed) và tập trung đỉnh nhọn cao độ quanh giá trị 0 (sharply peaked around zero).
        * Phân bố tập trung sát 0 chứng minh đa số tuyệt đối các dự đoán từ ANN chỉ có độ lệch tối thiểu so với giá trị thực nghiệm, hoàn toàn không có sai số cực biên.
    * **Hạn chế trong phân bố sai số của mô hình RSM**:
        * Ngược lại, phân bố sai số của RSM có độ phân tán rộng hơn nhiều (wider spread), tương ứng với độ lệch chuẩn cao hơn (higher standard deviation).
        * Độ phân tán rộng phản ánh các phương trình đa thức bậc hai (quadratic polynomial equations) của RSM gặp nhiều hạn chế và bất cập khi nắm bắt các dao động phi tuyến phức tạp (complex, non-linear fluctuations) vốn có trong quy trình xử lý nước thải sinh học.
    * **Kết luận về năng lực mô hình hóa hệ thống MBR**:
        * Toàn bộ bằng chứng thống kê và trực quan khẳng định cấu trúc kiến trúc ANN cung cấp sự xấp xỉ vượt trội (superior approximation) đối với hành vi vận hành phức tạp của hệ thống màng lọc sinh học vi tảo (MBR).
    * **Hình 9.** Biểu đồ tần số phân bố sai số (phần dư) giữa ANN và RSM
      * <img src="assets/fig_10_p12.png" alt="Hình 9" />
      * **Hình này chứng minh điều gì**
        * ANN có độ tin cậy vượt trội khi tập trung phần lớn dự báo sát sai số 0 và không có sai số cực biên.
      * **Từ đâu mà thấy được**
        * Trục $Oy$ biểu thị tần số mẫu; trục $Ox$ biểu diễn các khoảng sai số phần dư.
        * Đồ thị a (ANN): cột tâm sát mốc 0 đạt đỉnh cao nhất ($\approx 66$), phân bố dốc đứng và đối xứng.
        * Đồ thị b (RSM): đỉnh bị phân tách ($\approx 47$ và $55$), dải phân bố dàn trải và có ngoại lai ở rìa phải.
