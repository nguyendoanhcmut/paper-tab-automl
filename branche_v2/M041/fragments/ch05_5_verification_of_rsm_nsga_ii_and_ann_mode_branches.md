### Verification of RSM, NSGA-II, and ANN models

* **Mục tiêu và khuôn khổ kiểm chứng mô hình (Model Verification Framework)**:
    * **Đánh giá nghiêm ngặt độ chuẩn xác dự báo (Predictive Accuracy)**: Để đánh giá toàn diện và khắt khe năng lực dự báo của các mô hình bề mặt đáp ứng (Response Surface Methodology - RSM) và mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) đã phát triển, nghiên cứu áp dụng các chỉ số thống kê định lượng chuyên sâu thay vì chỉ dựa vào hệ số xác định ($R^2$).
    * **Sự cần thiết của việc mở rộng các chỉ số đánh giá**: Mặc dù hệ số xác định $R^2$ phản ánh mức độ tương quan xu hướng giữa dữ liệu dự đoán và thực nghiệm, chỉ số này có thể bị thổi phồng hoặc không phản ánh được biên độ sai số tuyệt đối; do đó, việc kết hợp các chỉ số sai số trung bình là bắt buộc để khẳng định độ tin cậy trong kỹ thuật môi trường.
    * **Kiểm định sự phù hợp của mô hình trong hệ thống MBR vi tảo**: Xác nhận khả năng mô phỏng chính xác quá trình loại bỏ các chất dinh dưỡng (nitơ amoniac và phosphat) trong bể phản ứng sinh học màng vi tảo (*microalgae membrane bioreactor* - MBR), nơi diễn ra đồng thời nhiều tương tác sinh hóa và thủy động học phức tạp.

* **Các chỉ số thống kê đánh giá sai số và công thức toán học (Statistical Evaluation Metrics)**:
    * **Căn bậc hai sai số toàn phương trung bình (Root Mean Square Error - RMSE)**:
        * **Định nghĩa và ý nghĩa vật lý**: RMSE lượng hóa độ lệch căn bậc hai trung bình giữa các giá trị dự đoán ($y_{\text{pred}}$) và dữ liệu thực nghiệm thực tế ($y_{\text{exp}}$). Do áp dụng phép tính bình phương sai số trước khi lấy trung bình, RMSE đặc biệt nhạy cảm với các sai số lớn (outliers) và phạt nặng các độ lệch dự báo bất thường.
        * **Công thức toán học (Phương trình 16)**:
          $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{\text{exp}} - y_{\text{pred}})^2} \quad (16)$$
          Trong đó:
          * $n$: Tổng số điểm dữ liệu thực nghiệm quan sát ($n = 44$).
          * $y_{\text{exp}}$: Giá trị thực nghiệm đo đạc thực tế tại mẫu thứ $i$.
          * $y_{\text{pred}}$: Giá trị dự báo tương ứng thu được từ mô hình (RSM hoặc ANN) tại mẫu thứ $i$.
    * **Sai số tuyệt đối trung bình (Mean Absolute Error - MAE)**:
        * **Định nghĩa và đặc tính thống kê**: MAE lượng hóa giá trị trung bình số học của tất cả các sai số tuyệt đối giữa giá trị thực nghiệm và giá trị dự báo. Không giống như RMSE, MAE gán trọng số tuyến tính đồng đều cho mọi mức sai lệch, phản ánh độ lớn sai số điển hình mà không phóng đại ảnh hưởng của các giá trị ngoại lai.
        * **Công thức toán học (Phương trình 17)**:
          $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{exp}} - y_{\text{pred}}| \quad (17)$$
          Trong đó:
          * $n$: Số lượng mẫu quan sát trong tập dữ liệu.
          * $|y_{\text{exp}} - y_{\text{pred}}|$: Độ lệch tuyệt đối giữa giá trị thực nghiệm và giá trị dự báo tại mẫu thứ $i$.
    * **Hệ số xác định (Coefficient of Determination - $R^2$)**:
        * **Ý nghĩa thống kê**: Đo lường tỷ lệ phần trăm tổng phương sai của biến phụ thuộc được giải thích bởi mô hình toán học (RSM hoặc ANN), biểu thị mức độ phù hợp tổng thể giữa đường cong dự báo và phân bố thực nghiệm:
          $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_{\text{exp}} - y_{\text{pred}})^2}{\sum_{i=1}^{n} (y_{\text{exp}} - \bar{y}_{\text{exp}})^2}$$
          Trong đó $\bar{y}_{\text{exp}}$ là giá trị trung bình thực nghiệm ($\bar{y}_{\text{exp}} = \frac{1}{n} \sum_{i=1}^{n} y_{\text{exp}}$).
        * **Tiêu chuẩn đánh giá**: Giá trị $R^2$ nằm trong dải $[0, 1]$; giá trị càng tiệm cận $1.0$ càng khẳng định mức độ ăn khớp lý tưởng của mô hình đối với dữ liệu thực nghiệm.
    * **Kiểm định giả thuyết thống kê (Statistical Hypothesis Testing)**:
        * **Bác bỏ giả thuyết không ($H_0$)**: Thông qua phân tích phương sai (ANOVA), giả thuyết không cho rằng "mô hình không có khả năng dự báo và sai số quan sát được chỉ do ngẫu nhiên" bị bác bỏ với mức ý nghĩa cao ($P < 0.0001$).
        * **Ngưỡng chấp nhận mô hình**: Cả hai mô hình RSM và ANN đều vượt qua ngưỡng kiểm định khắt khe với hệ số $R^2 > 0.95$, xác nhận cả hai cách tiếp cận đều có ý nghĩa thống kê thực chất và đủ năng lực mô phỏng động học của bioreactor.

* **So sánh định lượng hiệu năng giữa mô hình RSM và ANN (đối chiếu Bảng 3 tại mục 3.3)**:
    * **Chi tiết các chỉ số thống kê so sánh đối chứng giữa hai mô hình**:
      | Biến mục tiêu (*Target Variable*) | Mô hình (*Model*) | $R^2$ | RMSE | MAE |
      | :--- | :--- | :--- | :--- | :--- |
      | Nitơ amoniac (*Ammonia nitrogen*) | RSM | $0.9733$ | $0.324$ | $0.281$ |
      | Nitơ amoniac (*Ammonia nitrogen*) | ANN | $0.9979$ | $0.189$ | $0.142$ |
      | Photphat (*Phosphate*) | RSM | $0.9608$ | $0.251$ | $0.215$ |
      | Photphat (*Phosphate*) | ANN | $0.9972$ | $0.166$ | $0.118$ |
    * **Phân tích so sánh chi tiết giữa RSM và ANN**:
      * **Độ chính xác trên biến Nitơ amoniac (Ammonia nitrogen)**:
        * Mô hình RSM đạt $R^2 = 0.9733$, $\text{RMSE} = 0.324$, và $\text{MAE} = 0.281$.
        * Mô hình ANN đạt $R^2 = 0.9979$, $\text{RMSE} = 0.189$, và $\text{MAE} = 0.142$.
        * Sai số RMSE của ANN giảm $41.7\%$ và MAE giảm $49.5\%$ so với RSM, thể hiện sự cải thiện vượt bậc về độ chuẩn xác tại từng điểm đo.
      * **Độ chính xác trên biến Photphat (Phosphate)**:
        * Mô hình RSM đạt $R^2 = 0.9608$, $\text{RMSE} = 0.251$, và $\text{MAE} = 0.215$.
        * Mô hình ANN đạt $R^2 = 0.9972$, $\text{RMSE} = 0.166$, và $\text{MAE} = 0.118$.
        * Sai số RMSE của ANN giảm $33.9\%$ và MAE giảm $45.1\%$ so với RSM.
      * **Đánh giá ưu thế vượt trội của phương pháp mạng nơ-ron (ANN superiority)**:
        * Dù cả hai mô hình đều có năng lực dự báo thỏa đáng ($R^2 > 0.95$), ANN thể hiện độ chính xác vượt trội (superior precision) với các giá trị RMSE và MAE thấp hơn rõ rệt trên toàn bộ các biến phản ứng mục tiêu.
        * Kết quả này khẳng định cấu trúc phi tuyến với các hàm kích hoạt đối xứng nhiều tầng của ANN thích hợp vượt trội trong việc nắm bắt bản chất động sinh học phi tuyến phức tạp (*non-linear complexities*) của hệ thống MBR vi tảo so với các phương trình hồi quy đa thức giới hạn của RSM.

* **Kiểm chứng vai trò tích hợp của thuật toán NSGA-II trong chuỗi mô hình hóa**:
    * **Kết nối giữa mô hình hồi quy và giải thuật di truyền**: Thuật toán di truyền sắp xếp không bị chi phối II (NSGA-II) sử dụng trực tiếp các phương trình toán học thực nghiệm từ RSM làm các hàm thích nghi (fitness functions) để tìm kiếm không gian nghiệm tối ưu.
    * **Xác thực tập nghiệm tối ưu Pareto (Pareto Optimal Verification)**:
        * NSGA-II giải quyết xung đột cố hữu giữa hai mục tiêu: cực đại hóa hiệu quả loại bỏ nitơ amoniac và cực đại hóa hiệu quả loại bỏ phosphat.
        * Các nghiệm trên mặt trước Pareto được kiểm chứng chéo với các miền biên vật lý thực nghiệm và dự báo ANN, đảm bảo các chế độ vận hành đề xuất hoàn toàn khả thi và không bị trôi dạt vào các vùng bất ổn định của bể sinh học màng vi tảo.
