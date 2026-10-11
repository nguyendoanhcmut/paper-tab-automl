### 3.3. Regression models for membrane fouling prediction

* **Thiết lập mô hình hồi quy và phân chia tập dữ liệu vận hành**:
    * Các mô hình hồi quy dự đoán dựa trên mạng nơ-ron truyền thẳng nhiều tầng (Multilayer Perceptron - MLP) và mạng nơ-ron hồi quy có bộ nhớ dài-ngắn hạn (Long Short-Term Memory - LSTM) được xây dựng dựa trên kết quả tối ưu hóa siêu tham số (Hyperparameter Optimization - HPO).
    * Toàn bộ tập dữ liệu $525$ ngày vận hành của hệ thống AnMBR được phân chia thành tập huấn luyện (training set) và tập kiểm tra (testing set) theo tỷ lệ $9:1$:
        * Tập huấn luyện bao gồm $472$ ngày dữ liệu, được huấn luyện qua $1000$ epoch với kích thước lô (batch size) là $32$.
        * Tập kiểm tra độc lập bao gồm $53$ ngày dữ liệu được dùng để đánh giá năng lực dự đoán thực tế của các mô hình đã huấn luyện.

* **Đặc tính suy giảm và hành vi dao động của hàm mất mát MSE trong quá trình huấn luyện (Hình 5a, b)**:
    * Diễn biến hàm mất mát sai số toàn phương trung bình (Mean Squared Error - MSE) trong suốt $1000$ epoch huấn luyện:
        * Đường cong mất mát MSE của mô hình MLP và LSTM giảm dần về các giá trị ổn định lần lượt là xấp xỉ $4.5$ (khoảng $4.9$ trên đồ thị) đối với MLP và $8.8$ đối với LSTM.
        * Việc đạt đến trạng thái ổn định khẳng định $1000$ epoch là số lượng chu kỳ huấn luyện hoàn toàn phù hợp cho cả hai cấu trúc mạng.
    * Phân tích hành vi dao động (oscillatory pattern) của hàm mất mát MSE trong quá trình tiệm cận giá trị cực tiểu (minimum):
        * Hàm MSE không suy giảm đơn điệu (not monotonically decrease) mà xuất hiện các đợt dao động với sự tăng và giảm giá trị xen kẽ.
        * Hiện tượng dao động phản ánh tác động đồng thời của nhiều yếu tố kỹ thuật:
            * Tốc độ học (learning rate): quy định mức điều chỉnh các tham số (trọng số weights và độ lệch bias) sau mỗi vòng lặp; nếu tốc độ học quá lớn, mô hình có thể nhảy vượt qua điểm tối ưu lý tưởng (overshoot) và gây dao động đường cong mất mát.
            * Tỷ lệ ngắt kết nối nơ-ron (dropout rate): tỷ lệ dropout cao đưa vào lượng lớn nhiễu ngẫu nhiên trong quá trình huấn luyện, có thể cản trở sự hội tụ trơn tru của mô hình và gây khó khăn tạm thời trong việc đạt nghiệm ổn định.
            * Độ phức tạp nội tại và tính không lồi (non-convexity) của bề mặt mất mát (loss landscape; Fort and Jastrzebski, 2019).
        * Mặc dù có dao động cục bộ, đường cong MSE của cả MLP và LSTM đều thể hiện xu hướng hội tụ mạnh mẽ (strong convergence), chứng minh tính xác đáng của việc lựa chọn siêu tham số từ HPO và bảo đảm độ chính xác của cấu trúc mô hình.
    * **Hình 5.** Dự đoán TMP và mất mát MSE của MLP và LSTM
        * <img src="assets/fig_05_p10.jpeg" alt="Hình 5" />
        * **Hình này chứng minh điều gì**
            * MLP hội tụ MSE huấn luyện thấp hơn (~$4.5$ so với ~$8.8$) và bám sát TMP thực nghiệm hơn LSTM.
        * **Từ đâu mà thấy được**
            * (a), (b): Trục Ox là Epochs ($0$–$1000$), Oy là Loss MSE; đường loss MLP (a) giảm về ~$4.5$ (khoảng $4.9$ trên đồ thị), LSTM (b) giảm về ~$8.8$.
            * (c), (d): Trục Ox là Test samples, Oy là TMP ($0$–$30\text{ kPa}$); Predicted TMP (xanh) của MLP khớp Actual TMP (cam) chặt chẽ hơn LSTM.

* **Đánh giá hiệu năng dự đoán áp suất qua màng (TMP) trên tập kiểm tra độc lập và kiểm soát quá khớp (Hình 5c, d)**:
    * Kết quả so sánh giữa giá trị dự đoán và giá trị thực tế của áp suất qua màng (Transmembrane Pressure - TMP) trên cùng tập kiểm tra $53$ ngày được thể hiện chi tiết tại Fig. 5 (c) cho MLP và Fig. 5 (d) cho LSTM.
    * Đánh giá định lượng qua hệ số xác định ($R^2$):
        * Trên tập kiểm tra độc lập: mô hình MLP đạt $R^2 = 0.9183$, trong khi mô hình LSTM đạt $R^2 = 0.8954$.
        * Trên tập dữ liệu huấn luyện: mô hình MLP đạt $R^2 = 0.9322$, trong khi LSTM đạt $R^2 = 0.9249$.
        * Giá trị dự đoán của cả hai mô hình đều có độ tương đồng và ăn khớp rất cao (good agreement) với giá trị thực nghiệm của TMP.
    * Phân tích nguyên nhân $R^2$ tập huấn luyện cao hơn nhẹ so với tập kiểm tra:
        * Kích thước mẫu của tập huấn luyện lớn hơn nhiều ($472$ ngày so với $53$ ngày), dẫn đến các ước lượng hiệu năng mang tính ổn định và tối ưu hơn.
        * Sự khác biệt nhỏ về phân bố dữ liệu giữa tập huấn luyện và tập kiểm tra thực tế.
        * Mức chênh lệch rất nhỏ giữa hai tập ($0.9322$ so với $0.9183$ ở MLP; $0.9249$ so với $0.8954$ ở LSTM) chứng minh hiện tượng quá khớp (overfitting) đã được khống chế và phòng tránh một cách hiệu quả.
    * Đánh giá sai số qua căn bậc hai sai số toàn phương trung bình (Root Mean Square Error - RMSE):
        * Đơn vị đo lường của RMSE được giữ nguyên theo đơn vị của TMP đầu ra là $\text{kPa}$.
        * Trên tập kiểm tra: MLP ghi nhận $\text{RMSE} = 2.408\text{ kPa}$, trong khi LSTM ghi nhận $\text{RMSE} = 3.098\text{ kPa}$.
        * Trên tập huấn luyện: MLP đạt $\text{RMSE} = 2.176\text{ kPa}$, LSTM đạt $\text{RMSE} = 2.898\text{ kPa}$.
        * Mức sai số RMSE phản ánh độ lệch trung bình giữa giá trị dự đoán và giá trị thực tế dao động quanh mức $3\text{ kPa}$ TMP.
        * Xét trong toàn bộ dải phân bố TMP thực tế của hệ thống AnMBR (dao động rộng từ xấp xỉ $0$ đến $25\text{ kPa}$), mức sai số RMSE này là hoàn toàn chấp nhận được đối với bài toán dự báo tắc nghẽn màng nhằm phục vụ công tác lập kế hoạch làm sạch màng (membrane cleaning).

* **So sánh đa tiêu chí giữa các cấu trúc mô hình (Adjusted $R^2$, MAE, MedAE)**:
    * Đánh giá qua hệ số xác định hiệu chỉnh (Adjusted $R^2$):
        * Mô hình MLP đạt Adjusted $R^2 = 0.9056$, vượt trội hơn đáng kể so với mô hình MLP đơn giản không qua HPO tối ưu đầy đủ (Simple MLP hay s-MLP, Adjusted $R^2 = 0.8055$) và mô hình LSTM (Adjusted $R^2 = 0.8791$) khi hiệu chỉnh theo số lượng biến dự báo (predictors) sử dụng.
    * Đánh giá qua sai số tuyệt đối trung bình (Mean Absolute Error - MAE):
        * Mô hình MLP đạt sai số trung bình thấp nhất với $\text{MAE} = 1.509$, vượt trội rõ rệt về độ chính xác dự đoán so với s-MLP ($\text{MAE} = 2.243$) và LSTM ($\text{MAE} = 1.878$).
    * Đánh giá qua sai số tuyệt đối trung vị (Median Absolute Error - MedAE):
        * Mô hình LSTM đạt sai số trung vị thấp hơn với $\text{MedAE} = 0.8400$, so với MLP đạt $\text{MedAE} = 0.9190$ và s-MLP đạt $\text{MedAE} = 1.748$.
        * Giá trị MedAE thấp hơn của LSTM gợi ý rằng LSTM có thể đem lại độ chính xác dự đoán đồng đều và nhất quán hơn trên phân bố trung vị của tập dữ liệu.
    * Phân tích bản chất thống kê giữa các chỉ số và tác động của điểm ngoại lai (outliers):
        * Một mô hình có thể ghi nhận giá trị $R^2$ cao hơn nhưng đồng thời lại có MedAE lớn hơn nếu mô hình đó nhạy cảm hơn trước các điểm ngoại lai (outliers); các điểm ngoại lai tác động bất cân xứng lên sai số trung bình (mean error) so với sai số trung vị (median error).
        * Quá trình đánh giá và lựa chọn mô hình đòi hỏi phải tổng hòa cả các thước đo xu hướng tập trung (central tendency) lẫn các thước đo độ phân tán sai số (error dispersion), gắn liền với mục đích ứng dụng thực tiễn cụ thể.
        * Tổng thể các chỉ số xác nhận MLP luôn mang lại các kết quả dự đoán chuẩn xác nhất một cách ổn định; LSTM có hiệu năng cao hơn s-MLP nhưng nhìn chung xếp sau MLP (ngoại trừ MedAE); s-MLP là mô hình có độ chính xác thấp nhất.
        * Nhờ giảm thiểu ảnh hưởng của các điểm ngoại lai cực biên, MedAE cung cấp góc nhìn bổ trợ tin cậy và khách quan hơn bên cạnh MAE.

* **So sánh định lượng hiệu năng mô hình dự đoán và đối chiếu toàn diện với y văn (Bảng 5)**:
    * Kết quả hiệu năng của các mô hình trong nghiên cứu này và so sánh với các công trình công bố trước đây được tổng hợp chi tiết tại Bảng 5:
        * Nghiên cứu này (This study):
            * Simple MLP (AnMBR $5000\text{ L}$, nước thải đô thị thực tế, HPO bằng Optuna, $525$ mẫu): Tập huấn luyện đạt $R^2 = 0.8622$, $\text{RMSE} = 3.897\text{ kPa}$; Tập kiểm tra đạt $R^2 = 0.8317$, $\text{RMSE} = 4.156\text{ kPa}$, Adjusted $R^2 = 0.8055$, $\text{MAE} = 2.243$, $\text{MedAE} = 1.748$.
            * MLP (AnMBR $5000\text{ L}$, nước thải đô thị thực tế, HPO bằng Optuna, $525$ mẫu): Tập huấn luyện đạt $R^2 = 0.9322$, $\text{RMSE} = 2.176\text{ kPa}$; Tập kiểm tra đạt $R^2 = 0.9183$, $\text{RMSE} = 2.408\text{ kPa}$, Adjusted $R^2 = 0.9056$, $\text{MAE} = 1.509$, $\text{MedAE} = 0.9190$.
            * LSTM (AnMBR $5000\text{ L}$, nước thải đô thị thực tế, HPO bằng Optuna, $525$ mẫu): Tập huấn luyện đạt $R^2 = 0.9249$, $\text{RMSE} = 2.898\text{ kPa}$; Tập kiểm tra đạt $R^2 = 0.8954$, $\text{RMSE} = 3.098\text{ kPa}$, Adjusted $R^2 = 0.8791$, $\text{MAE} = 1.878$, $\text{MedAE} = 0.8400$.
        * Schmitt et al. (2018): Mô hình MLP trên hệ thống AO-MBR ($50\text{ L}$), xử lý nước thải sinh hoạt thực tế, không thực hiện HPO, kích thước mẫu $938$, đạt $R^2 = 0.85$ và $\text{RMSE} = 0.099\text{ cm Hg}$.
        * Yao et al. (2022): Mô hình MLP trên hệ thống AnMBR ($20\text{ L}$), xử lý thành phần hữu cơ của nước rỉ rác sinh hoạt, HPO bằng thuật toán di truyền (Genetic Algorithm - GA), kích thước mẫu $102$, sai số tương đối (Relative error) = $3.57\%$.
        * Viet và Jang (2021): Mô hình MLP trên hệ thống màng thẩm thấu (OMBR, quy mô $1\text{ L}$), xử lý nước thải, tối ưu bằng thử sai (Trial-and-error), kích thước mẫu $100$, đạt $R^2 > 0.9$.
        * Shim et al. (2021): Mô hình LSTM trên hệ thống lọc nano (Nanofiltration), nước cấp muối tổng hợp, không HPO, kích thước mẫu $1420$, đạt $R^2 = 0.97$.
        * Kovacs et al. (2022): So sánh RF, MLP, LSTM trên bể MBR quy mô thực tế công suất $60,000\text{ m}^3\text{/ngày}$, nước thải đô thị thực, áp dụng phân tích độ bất định (Uncertainty analysis), kích thước mẫu lớn $83,823$, đạt $R^2 > 0.92$.
        * Mirbagheri et al. (2015): Mô hình MLP và mạng hàm xuyên tâm (RBF) trên bể MBR, nước thải đô thị thực, HPO bằng GA, kích thước mẫu $60$, đạt $R^2 = 0.98$.
        * Liu et al. (2020): Mô hình máy vector hỗ trợ (SVM) trên hệ thống AnMBR, nước thải sinh hoạt, áp dụng kiểm định chéo 5 lần (Five-fold cross-validation) kết hợp tìm kiếm siêu tham số, kích thước mẫu $190$, đạt $R^2 = 0.9995$ và $\text{RMSE} = 1.70 \times 10^{-7}$.
    * **Bảng 5.** So sánh hiệu năng mô hình dự đoán với y văn
        * <img src="assets/table_05_p9.png" alt="Bảng 5" />
        * **Bảng này chứng minh điều gì**
            * Mô hình MLP đạt hiệu năng kiểm tra tốt nhất ($R^2 = 0.9183$, $\text{RMSE} = 2.408\text{ kPa}$), tương đương mức $R^2 > 0.90$ của các nghiên cứu MBR khác.
        * **Từ đâu mà thấy được**
            * Hàng "This study", cột "Model performance": MLP đạt $R^2 = 0.9183$ (tập test), cao hơn Simple MLP ($R^2 = 0.8317$) và LSTM ($R^2 = 0.8954$).
            * Cột "Model performance" các hàng y văn: giá trị cao nhất là Liu et al. ($R^2 = 0.9995$), thấp nhất là Schmitt et al. ($R^2 = 0.85$).

* **Phân tích nguyên nhân chênh lệch hệ số xác định $R^2$ so với các nghiên cứu trước đây**:
    * Hệ số xác định của nghiên cứu này ($R^2 = 0.9183$ trên tập kiểm tra) thấp hơn một chút so với một số nghiên cứu tiền nhiệm ghi nhận $R^2 > 0.95$ (Liu et al., 2020; Mirbagheri et al., 2015; Shim et al., 2021; Yao et al., 2022). Nguyên nhân được làm sáng tỏ qua ba khía cạnh chính:
        1. Tính phức tạp của cơ chế tắc nghẽn màng trong AnMBR: Trong các hệ thống MBR sử dụng màng vi lọc (microfiltration), cơ chế tắc nghẽn màng của AnMBR phức tạp hơn nhiều so với hệ thống MBR hiếu khí truyền thống (Dvořák et al., 2016); đồng thời sự khác biệt lớn trong việc lựa chọn các đặc trưng đầu vào dẫn đến sự biến thiên về độ chính xác khi huấn luyện và dự đoán bằng cùng một loại mạng nơ-ron nhân tạo.
        2. Dữ liệu vận hành thực tế dài hạn và dải biến thiên TMP rộng lớn: Các mô hình trong nghiên cứu này được xây dựng hoàn toàn dựa trên dữ liệu vận hành dài hạn ($525$ ngày) của một bể phản ứng quy mô pilot lớn ($5000\text{ L}$); số lượng mẫu dữ liệu và biên độ biến động của các thông số lớn hơn nhiều so với các nghiên cứu quy mô phòng thí nghiệm trước đây. Giá trị TMP trong tập kiểm tra trải rộng từ mức dưới $5\text{ kPa}$ (giai đoạn vận hành ổn định) đến gần $25\text{ kPa}$ (sau khi xảy ra tắc nghẽn màng nghiêm trọng).
        3. Kỹ thuật điều chuẩn chống quá khớp (Regularization): Cả MLP và LSTM đều được áp dụng kỹ thuật điều chuẩn L2 (L2 regularization / weight decay) cùng với dropout; kết hợp với lượng dữ liệu phong phú, điều này bảo đảm mô hình không bị hiện tượng quá khớp (overfitting) như ở các nghiên cứu có tập dữ liệu nhỏ.
    * Ý nghĩa khoa học: Đây là lần đầu tiên mô hình mạng nơ-ron nhân tạo (ANN) được triển khai thành công để dự đoán tắc nghẽn màng trong vận hành dài hạn của hệ thống AnMBR quy mô lớn xử lý nước thải đô thị thực tế với độ chính xác tin cậy, đảm bảo năng lực tổng quát hóa (generalizability) và thiết lập một chuẩn đối sánh (benchmark) vững chắc cho các hệ thống AnMBR tương lai.

* **Đánh giá chi phí tính toán và lựa chọn mô hình tối ưu cho hệ thống AnMBR**:
    * Thời gian tính toán (không bao gồm thời gian thực hiện HPO):
        * Mô hình s-MLP và MLP hoàn thành tính toán trên cùng tập dữ liệu chỉ trong vòng chưa đầy $1$ phút ($< 1\text{ min}$).
        * Mô hình LSTM đòi hỏi thời gian tính toán trong vòng $2$ phút ($< 2\text{ min}$).
    * Đánh giá và lựa chọn mô hình thích hợp:
        * Mô hình MLP đạt độ chính xác cao nhất (thể hiện qua $R^2$ cao nhất và RMSE thấp nhất); mức độ phức tạp vừa phải cùng mức tiêu thụ tài nguyên tính toán thấp khiến MLP trở thành mô hình phù hợp nhất để dự đoán tắc nghẽn màng trong hệ thống AnMBR của nghiên cứu này.
        * Mô hình Simple MLP (s-MLP) tuy tiết kiệm thời gian và tài nguyên phần cứng nhưng độ chính xác kém hơn nhiều so với các mô hình khác ($R^2 = 0.8317$, $\text{RMSE} = 4.156\text{ kPa}$).
        * Mô hình LSTM có độ phức tạp thuật toán cao, đòi hỏi tài nguyên và thời gian tính toán vượt trội, trong khi độ chính xác $R^2$ ($0.8954$) và RMSE ($3.098\text{ kPa}$) lại kém hơn MLP, khiến LSTM không phải là lựa chọn tối ưu cho việc dự đoán tắc nghẽn màng trong điều kiện nghiên cứu này.
