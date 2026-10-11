#### 3.4.3. Test set performance evaluation

* **Đánh giá trên tập kiểm tra độc lập (independent test set)**:
    * Các mô hình cuối cùng được huấn luyện lại trên toàn bộ tập dữ liệu huấn luyện với cấu hình siêu tham số đã tối ưu hóa, sau đó được kiểm định trên tập kiểm tra độc lập (phân chia ngẫu nhiên theo tỷ lệ $80:20$) nhằm xác định chính xác năng lực khái quát hóa thực tế.
    * Phép phân chia ngẫu nhiên $80:20$ đóng vai trò là cơ sở đánh giá chính cho năng lực nội suy trong phạm vi dữ liệu vận hành đã thu thập.

* **Đánh giá định lượng hiệu suất dự đoán COD và TMP trên tập kiểm tra độc lập (Bảng 2)**:
    * Hiệu suất dự đoán COD nước sau xử lý (effluent COD) đạt độ chuẩn xác cao trên cả ba mô hình:
        * Random Forest (RF) đạt hiệu suất ổn định nhất với hệ số xác định $R^2 = 0.96$, sai số toàn phương trung bình $\text{RMSE} = 331.50\text{ mg/L}$, và sai số tuyệt đối trung bình $\text{MAE} = 252.12\text{ mg/L}$.
        * Extreme Gradient Boosting (XGBoost) đạt $R^2 = 0.96$ tương đương với $\text{RMSE} = 351.76\text{ mg/L}$.
        * Mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) ghi nhận $R^2 = 0.90$ và $\text{RMSE} = 510.37\text{ mg/L}$.
    * Hiệu suất dự đoán áp suất xuyên màng (Transmembrane Pressure - TMP) thể hiện sự phân hóa rõ rệt giữa các mô hình:
        * RF duy trì kết quả tốt nhất với $R^2 = 0.88$, $\text{RMSE} = 3.86\text{ kPa}$, và $\text{MAE} = 2.47\text{ kPa}$.
        * XGBoost suy giảm năng lực khái quát hóa với $R^2 = 0.56$ và $\text{RMSE} = 7.50\text{ kPa}$.
        * ANN suy giảm năng lực khái quát hóa tương tự với $R^2 = 0.54$ và $\text{RMSE} = 7.59\text{ kPa}$.
    - **Bảng 2.** Hiệu suất dự báo COD và TMP trên tập kiểm tra
      - <img src="assets/table_02_p7.png" alt="Bảng 2" />
      - **Bảng này chứng minh điều gì**
        - RF đạt kết quả tốt nhất ở cả hai biến đầu ra, trong khi XGBoost và ANN suy giảm khả năng khái quát hóa đối với TMP ($R^2 \le 0.56$, $\text{RMSE} \ge 7.50\text{ kPa}$).
      - **Từ đâu mà thấy được**
        - Cột "Target Variable" và "Model": phân chia kết quả cho Effluent COD và TMP qua 3 mô hình (RF, XGBoost, ANN).
        - Cột "Test $R^2$" và "Test RMSE": ở Effluent COD cả 3 mô hình đạt $R^2 \ge 0.90$; ở TMP, RF đạt $R^2 = 0.88$ ($\text{RMSE} = 3.86\text{ kPa}$), so với XGBoost ($0.56$, $7.50\text{ kPa}$) và ANN ($0.54$, $7.59\text{ kPa}$).

* **Đánh giá trực quan qua đồ thị phân tán giữa giá trị dự đoán và giá trị thực tế (Hình 4)**:
    * Đối với dự đoán COD nước sau xử lý (Hình 4a–c):
        * Cả ba mô hình đều có các điểm dự đoán tập trung dày đặc xung quanh đường chuẩn $1:1$.
        * RF thể hiện tính ổn định cao nhất trên toàn dải nồng độ COD.
        * XGBoost xuất hiện độ lệch lớn hơn ở vùng COD cao, cho thấy độ ổn định suy giảm dưới điều kiện tải trọng cực biên.
        * ANN có độ phân tán rộng hơn, đặc biệt ở dải nồng độ trung bình đến cao, phản ánh độ nhạy thấp hơn trước các xu hướng phi tuyến; điều này phù hợp với các nghiên cứu chứng minh phương pháp hòa tấu dạng cây (ensemble tree-based methods) thường đạt kết quả ngang bằng hoặc tốt hơn ANN trong dự đoán COD/BOD ở hệ thống xử lý nước thải.
    * Đối với dự đoán TMP (Hình 4d–f):
        * Đồ thị phân tán của RF bám sát đường $1:1$ hơn rõ rệt so với XGBoost và ANN.
        * XGBoost khớp rất sát dữ liệu huấn luyện nhưng lệch xa trên tập kiểm tra, biểu hiện rõ hiện tượng quá khớp (overfitting) và giảm khả năng chuyển giao sang các quan sát mới.
        * ANN phân tán rải rác, phản ánh năng lực hạn chế trong việc nắm bắt đáp ứng TMP phi tuyến với tập dữ liệu hiện có.
    - **Hình 4.** Đồ thị phân tán dự đoán COD và TMP
      - <img src="assets/fig_04_p7.jpeg" alt="Hình 4" />
      - **Hình này chứng minh điều gì**
        - Cả ba mô hình đều dự đoán COD bám sát đường $1:1$; với TMP, RF duy trì độ tập trung sát đường $1:1$ trên tập kiểm tra, trong khi XGBoost và ANN phân tán rộng.
      - **Từ đâu mà thấy được**
        - Hàng trên (a–c): Điểm Train (xanh) và Test (hồng) của RF, XGBoost, ANN đều phân bố dọc sát đường nét đứt $1:1$ cho COD nước sau xử lý ($0\text{ - }6000\text{ mg/L}$).
        - Hàng dưới (d–f): Ở dự đoán TMP, panel (d) của RF có điểm Test bám sát đường $1:1$ ($-35\text{ đến }0\text{ kPa}$); panel (e) của XGBoost có điểm Test lệch xa đường chuẩn, panel (f) của ANN phân tán rộng.

* **Phân tích sai số phần dư và đặc tính động học của tắc nghẽn màng (Residual analysis)**:
    * Quá trình tắc nghẽn màng diễn ra phức tạp, phi tuyến, động học và phụ thuộc thời gian, chi phối bởi hoạt tính sinh học, sự tích tụ chất nền polyme ngoại bào (Extracellular Polymeric Substances - EPS), sự hình thành lớp bánh bùn (cake layer) và tương tác hóa lý.
    * Phân tích sai số phần dư (residual analysis, Fig. S4d–f) xác nhận lại các quy luật quan sát được:
        * Phân bố phần dư của RF đối với TMP gọn nhất trong cả ba mô hình, dù vẫn còn sai lệch ở các mức TMP cao, phản ánh độ không chắc chắn gia tăng khi tắc nghẽn nghiêm trọng.
        * XGBoost thể hiện sai số phần dư lớn dù có kết quả huấn luyện tốt, chứng minh mô hình chỉ nắm bắt các dạng thức đặc thù của tập huấn luyện thay vì động học tắc nghẽn ổn định.
        * Sai số phần dư của ANN phân tán rộng, củng cố nhận định về khả năng khái quát hóa yếu đối với TMP.
    * Độ phân tán phần dư của TMP rộng hơn đáng kể so với COD nước sau xử lý, xác nhận dự báo tắc nghẽn mang tính bất định cao hơn so với dự báo COD; điều này đồng thuận với các nghiên cứu màng trước đây khi mô hình học máy hoạt động tốt ở điều kiện bình thường nhưng kém tin cậy khi tắc nghẽn phát triển đột ngột hoặc nghiêm trọng.

* **So sánh tổng thể giữa khả năng dự đoán COD và TMP**:
    * COD nước sau xử lý ($R^2 > 0.90$) dễ dự đoán hơn đáng kể so với TMP ($R^2 = 0.80\text{ -- }0.50$, thực tế các mô hình đạt $0.54\text{ -- }0.88$):
        * COD được điều khiển bởi động học tương đối xác định và phụ thuộc tải trọng (load-dependent kinetics).
        * TMP phản ánh cơ chế tắc nghẽn ngẫu nhiên (stochastic) và phi tuyến phức tạp chịu tác động tổng hòa của vi sinh vật, tích lũy EPS và điều kiện hóa lý.
    * RF là lựa chọn phù hợp nhất để giám sát COD nhờ tính ổn định và độ chính xác; trong khi ANN đem lại độ bền vững tương đối cho dự đoán TMP khi tải trọng biến thiên.
    * Sự suy giảm hiệu suất TMP của XGBoost nhấn mạnh tính thiết yếu của việc kiểm định trên tập kiểm tra độc lập đối với các mô hình phức tạp khi áp dụng cho tập dữ liệu môi trường có quy mô giới hạn.
    * Việc kết hợp đồ thị dự đoán - quan sát và phân tích sai số phần dư đem lại đánh giá đầy đủ cả về độ chuẩn xác lẫn độ tin cậy của mô hình.

* **Thử nghiệm ngoại suy theo chuỗi thời gian dưới điều kiện sốc tải (Chronological extrapolation test)**:
    * Phương pháp phân chia dữ liệu theo thời gian (chronological data splitting) được triển khai để kiểm tra khả năng ngoại suy trong điều kiện vận hành chưa từng thấy:
        * Dữ liệu từ Giai đoạn I và II (Phases I–II) gồm $103$ mẫu (sau khi làm sạch và căn chỉnh) được sử dụng để huấn luyện mô hình.
        * Dữ liệu từ Giai đoạn III (Phase III) gồm $16$ mẫu đóng vai trò tập kiểm tra độc lập đại diện cho điều kiện sốc tải (shock loading).
        * Thử nghiệm này được thực hiện riêng biệt nhằm đánh giá khả năng ngoại suy dưới sốc tải và tách rời khỏi kết quả phân chia ngẫu nhiên $80:20$.
    * Kết quả ngoại suy Phase III suy giảm nghiêm trọng so với phép phân chia ngẫu nhiên $80:20$ (Table S3):
        * Cả ba mô hình (RF, ANN và XGBoost) đều cho giá trị $R^2$ âm ($R^2 < 0$) khi dự đoán cả COD nước sau xử lý lẫn TMP ở Phase III.
        * Giá trị $R^2$ âm chứng minh các mô hình hoàn toàn không thể ngoại suy đáng tin cậy sang điều kiện sốc tải chưa từng quan sát, và hiệu quả dự đoán thực tế kém hơn cả phép ước lượng bằng giá trị trung bình đơn giản (mean-based prediction).
    * Kết luận: Hiệu suất cao đạt được từ phân chia ngẫu nhiên $80:20$ cần được hiểu đúng là năng lực nội suy mạnh mẽ (interpolation ability) bên trong miền vận hành đã quan sát, chứ không đồng nghĩa với khả năng ngoại suy ổn định (extrapolation capacity) trong các điều kiện biến động bất thường.
