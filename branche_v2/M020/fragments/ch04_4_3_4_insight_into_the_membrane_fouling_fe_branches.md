### 3.4. Insight into the membrane fouling features and the interpretability of the model

* **Nguyên lý khung diễn giải SHAP và mối liên kết giữa độ quan trọng đặc trưng với giải thích toàn cục (global interpretability)**:
  * Khung phân tích $\text{SHAP}$ (SHapley Additive exPlanations) đóng vai trò là phương pháp chặt chẽ nhằm làm sáng tỏ ảnh hưởng của từng đặc trưng riêng lẻ (individual features) lên kết quả dự đoán của các mô hình học máy (ML models).
  * Bắt nguồn từ các nguyên lý của lý thuyết trò chơi hợp tác (cooperative game theory), các giá trị $\text{SHAP}$ cung cấp một thước đo thống nhất (unified metric) để đánh giá tầm quan trọng của đặc trưng, đảm bảo phân bổ đóng góp công bằng (equitable allocation of attribution) giữa các biến số đầu vào được xem xét (Gramegna and Giudici, 2021).
  * Trong bối cảnh tính khả giải thích của học máy, khái niệm tầm quan trọng của đặc trưng (feature importance) liên kết mật thiết với khái niệm giải thích toàn cục (global interpretability):
    * Trong khi độ quan trọng đặc trưng phản ánh đóng góp của từng biến số vào các dự đoán cụ thể, dạng tổng hợp (aggregate form) của nó trên nhiều cá thể/mẫu dữ liệu giúp mô tả hành vi tổng quát của mô hình, từ đó thiết lập khả năng giải thích toàn cục.
    * Bằng cách tính toán giá trị $\text{SHAP}$ cho từng biến số, mức đóng góp trung bình của chúng vào kết quả dự đoán của mô hình trên toàn bộ các tổ hợp đặc trưng khả dĩ được xác định đầy đủ.
    * Giá trị $\text{SHAP}$ càng cao biểu thị mức độ ý nghĩa và đóng góp càng lớn đối với kết quả dự đoán của mô hình.

* **Thứ bậc tầm quan trọng của các đặc trưng và tác động định hướng toàn cục đến dự đoán TMP (Fig. 6)**:
  * Đánh giá giá trị $\text{SHAP}$ tuyệt đối trung bình (mean absolute SHAP values) trên $7$ đặc trưng đầu vào xác lập thứ tự chi phối đối với biến động áp suất xuyên màng ($\text{TMP}$):
    $$\text{Flux} > \text{OLR} > \text{Temperature} > \text{MLSS} > \text{EPSp} > \text{EPSc} > \text{SS}$$
  * Thông lượng ($\text{Flux}$) là yếu tố chi phối mạnh mẽ nhất trong việc dự đoán các dao động của $\text{TMP}$, tiếp theo là tải trọng hữu cơ ($\text{OLR}$), nhiệt độ ($\text{Temperature}$), $\text{MLSS}$, $\text{EPSp}$, $\text{EPSc}$ và chất rắn lơ lửng ($\text{SS}$).
  * Hệ thống $\text{AnMBR}$ quy mô pilot lớn kết hợp bể phản ứng khuấy trộn hoàn toàn liên tục (continuously stirred tank reactor - CSTR) và mô-đun màng, trong đó biến động thời gian lưu thủy lực ($\text{HRT}$) và điều kiện tải trọng nạp ($\text{loading rate}$) phụ thuộc trực tiếp vào sự biến thiên của thông lượng ($\text{flux}$).
  * Do đó, tải trọng nạp cao hơn đi kèm với thông lượng cao hơn có xu hướng gây ra tình trạng tắc nghẽn màng nghiêm trọng hơn, hoàn toàn phù hợp với cơ chế lý thuyết cho thấy $\text{flux}$ ảnh hưởng trực tiếp đến tốc độ tắc nghẽn màng (He et al., 2017).
  * Trái ngược với giải thích toàn cục tập trung vào hành vi trên toàn bộ không gian dữ liệu, giải thích cục bộ (local interpretability) đi sâu giải thích các dự đoán riêng lẻ trên từng mẫu kiểm tra và cho phép phát hiện các điểm ngoại lai được dự đoán (predicted outliers).
  * Biến thiên của $\text{Flux}$ và $\text{OLR}$ tạo ra tác động phân tán rộng hơn (more diffused impact) trong phân bố giá trị $\text{SHAP}$, chứng tỏ sự thay đổi của hai thông số này giúp phân biệt rõ rệt hơn mức độ tắc nghẽn màng so với các yếu tố khác.
  * Ngược lại, $\text{Temperature}$, $\text{MLSS}$, $\text{EPSp}$, $\text{EPSc}$ và $\text{SS}$ thể hiện mức độ phân biệt giá trị $\text{SHAP}$ thấp hơn trên các mẫu kiểm tra, cho thấy mức đóng góp tối thiểu vào việc phân hóa dự đoán tắc nghẽn màng.
  * Biểu đồ phân tán $\text{SHAP}$ làm rõ cả độ lớn tác động (magnitude of impact) lẫn chiều hướng tác động (direction: dương hoặc âm): $\text{Flux}$ và $\text{OLR}$ thể hiện cả tác động dương lẫn âm với biên độ biến thiên mạnh (giá trị thực nghiệm cao đẩy $\text{TMP}$ tăng mạnh, giá trị thấp kéo $\text{TMP}$ giảm).
  * **Hình 6.** Tầm quan trọng và tác động của đặc trưng lên mô hình MLP
    * <img src="assets/fig_06_p11.jpeg" alt="Hình 6" />
    * **Hình này chứng minh điều gì**
      * $\text{Flux}$ ($\approx 2{,}2$) và $\text{OLR}$ ($\approx 1{,}8$) chi phối áp đảo dự đoán $\text{TMP}$; giá trị $\text{Flux}$ và $\text{OLR}$ cao làm tăng mạnh $\text{TMP}$, trong khi nhiệt độ cao làm giảm $\text{TMP}$.
    * **Từ đâu mà thấy được**
      * Panel (a) Biểu đồ thanh: Trục hoành biểu diễn $\text{Mean}(|\text{SHAP value}|)$ trong thang đo $0{,}0\text{--}2{,}5$; $\text{Flux}$ đạt giá trị cao nhất ($\approx 2{,}2$), $\text{OLR}$ đứng thứ hai ($\approx 1{,}8$), vượt xa nhóm $\text{Temperature}$ ($\approx 0{,}65$), $\text{MLSS}$ ($\approx 0{,}63$) và các biến sinh học $\text{EPSp}$, $\text{EPSc}$, $\text{SS}$ ($< 0{,}6$).
      * Panel (b) Biểu đồ chấm phân tán SHAP (dot plot): Trục hoành biểu diễn $\text{SHAP value}$ (dải $-5$ đến $8$ quanh trục chuẩn $0$); điểm đỏ (giá trị đặc trưng cao) của $\text{Flux}$ và $\text{OLR}$ phân tán mạnh sang phía dương ($> 6\text{--}8$), $\text{Temperature}$ phân tán sang phía âm (đạt $-2$), trong khi các biến sinh học co cụm sát vạch $0$.

* **Tiến trình ra quyết định và cơ chế nhận biết trạng thái vận hành của mô hình MLP (Fig. 7)**:
  * Biểu đồ quyết định (decision plot) thể hiện khả năng giải thích cục bộ của mô hình $\text{MLP}$ thông qua việc tái hiện tiến trình tích lũy ra quyết định cho từng mẫu thuộc tập kiểm tra:
    * Đường thẳng đứng màu đen ở trung tâm biểu đồ đại diện cho giá trị cơ sở (fundamental value/base value) của mô hình, được xác định là giá trị $\text{TMP}$ trung bình ($\approx 6\text{ kPa}$).
    * Mỗi đường biểu diễn phản ánh quỹ đạo dự đoán của một mẫu thử nghiệm cụ thể; chuyển động lệch sang trái hoặc sang phải khi đi qua từng đặc trưng thể hiện đặc trưng đó kéo giảm hay làm tăng giá trị đầu ra so với mức trung bình.
    * Bắt đầu từ đáy biểu đồ, đường dự đoán mô tả cách thức mô hình $\text{MLP}$ tích lũy đóng góp từ mức $\text{TMP}$ trung bình ban đầu để đạt tới giá trị đầu ra dự đoán cuối cùng ở đỉnh đồ thị.
    * Dao động ngang (horizontal oscillation) càng lớn sau khi đi qua tác động của một đặc trưng biểu thị mức độ ảnh hưởng càng mạnh của đặc trưng đó đối với kết quả dự đoán.
  * Đồng nhất với kết quả phân tích giải thích toàn cục, ba biến số đầu tiên ($\text{Temperature}$, $\text{OLR}$ và $\text{Flux}$) làm biến đổi sâu sắc nhất đường dự báo, trong khi $\text{SS}$, $\text{EPSc}$, $\text{EPSp}$ và $\text{MLSS}$ hầu như không làm chệch quỹ đạo khỏi giá trị trung bình ban đầu.
  * Về mặt lý thuyết cơ chế, ảnh hưởng của $\text{OLR}$ và $\text{Flux}$ lên đường dự đoán phải cùng hướng (đồng biến, in the same direction):
    * Xu hướng đồng biến này hoàn toàn phù hợp và nhất quán khi mô hình dự đoán ở các giai đoạn tắc nghẽn màng nghiêm trọng tương ứng với các giá trị $\text{TMP}$ cao ($> 10\text{--}20\text{ kPa}$).
    * Tuy nhiên, ở vùng $\text{TMP}$ thấp tương ứng với giai đoạn vận hành ổn định (steady portion of operation), tác động của $\text{OLR}$ và $\text{Flux}$ lên $\text{TMP}$ lại bộc lộ tính chất đối kháng nhất định (exhibited some antagonism).
    * Hiện tượng này chứng minh mô hình $\text{MLP}$ có khả năng phân biệt thành công giữa giai đoạn vận hành ổn định và giai đoạn tắc nghẽn màng nghiêm trọng, đồng thời sở hữu hành vi dự đoán tùy biến riêng biệt (tailored prediction behavior) thích ứng cho từng giai đoạn vận hành.
  * Khả năng phân hóa này gợi mở hướng nghiên cứu tương lai: có thể chia tách các mô hình dự đoán chuyên biệt cho từng giai đoạn tải nạp khác nhau của hệ thống $\text{AnMBR}$ nhằm nâng cao hơn nữa hiệu năng dự báo.
  * **Hình 7.** Quá trình ra quyết định dự đoán TMP của mô hình MLP
    * <img src="assets/fig_07_p12.jpeg" alt="Hình 7" />
    * **Hình này chứng minh điều gì**
      * Quỹ đạo dự đoán phân kỳ mạnh nhất khi đi qua các đặc trưng $\text{Temperature}$, $\text{OLR}$ và $\text{Flux}$; các biến $\text{SS}$, $\text{EPSc}$, $\text{EPSp}$ và $\text{MLSS}$ hầu như không làm chệch mức $\text{TMP}$ trung bình.
    * **Từ đâu mà thấy được**
      * Trục hoành $Ox$: Giá trị đầu ra của mô hình ($\text{Model output value}$), dải từ $-5$ đến $20$. Trục tung $Oy$: $7$ biến đầu vào tích lũy từ đáy lên gồm $\text{SS}$, $\text{EPSc}$, $\text{EPSp}$, $\text{MLSS}$, $\text{Temp}$, $\text{OLR}$, $\text{Flux}$.
      * Đường thẳng đứng màu đen ở trung tâm đồ thị (mốc $\approx 6$) đại diện giá trị $\text{TMP}$ trung bình xuất phát tại đáy.
      * Các đường tích lũy tản rộng dần từ $\text{Temp}$ lên $\text{Flux}$ thành hai dải rõ rệt: dải màu xanh lam hạ thấp ($< 5\text{ kPa}$) và dải màu đỏ hồng tăng cao ($> 10$ đến $> 20\text{ kPa}$).

* **Tính khả thi triển khai trong ứng dụng thực tế và tự động hóa rửa màng**:
  * Dưới góc độ ứng dụng kỹ thuật thực tế, để hiện thực hóa việc rửa màng tự động (automatic membrane cleaning), các thông số đầu vào được lựa chọn phải là những biến số có thể thu thập trực tiếp từ cảm biến (directly obtained from sensors), thay vì phụ thuộc vào các chỉ tiêu đòi hỏi lấy mẫu và phân tích thủ công trong phòng thí nghiệm.
  * Kết quả phân tích tính khả giải thích chỉ ra rằng $\text{Flux}$, $\text{OLR}$ (liên hệ trực tiếp với nồng độ $\text{COD}$), nhiệt độ ($\text{Temperature}$) và $\text{MLSS}$ là những đặc trưng quan trọng nhất đối với mô hình dự đoán.
  * Cả bốn thông số then chốt này đều có thể được thu thập hoàn toàn và liên tục bằng các cảm biến trực tuyến (sensors solely).
  * Do đó, mô hình $\text{MLP}$ được phát triển trong nghiên cứu này hoàn toàn phù hợp và có tính khả thi cao khi ứng dụng vào hệ thống điều khiển tự động hóa trong thực tế.

* **Ý nghĩa đối sánh giữa khả năng giải thích toàn cục và cục bộ trong quản lý tắc nghẽn màng**:
  * Giải thích toàn cục (global interpretability) mang lại cái nhìn toàn diện về hành vi tổng thể của mô hình trên toàn bộ tập dữ liệu, làm nổi bật các biến số chi phối cốt lõi. Điều này củng cố niềm tin của các bên liên quan (stakeholders) vào năng lực khái quát hóa của mô hình và đảm bảo mô hình vận hành phù hợp với các nguyên lý khoa học đã xác lập.
  * Ngược lại, giải thích cục bộ (local interpretability) tập trung làm sáng tỏ căn nguyên suy luận đằng sau từng kết quả dự đoán riêng lẻ. Trong bối cảnh tắc nghẽn màng, những hiểu biết chi tiết ở mức độ hạt mịn này (granular insights) mang tính sống còn, đóng vai trò định hướng thiết thực cho công tác bảo trì (maintenance), phòng ngừa sớm (prevention) và đề xuất các điều chỉnh hệ thống kịp thời (potential system modifications).
