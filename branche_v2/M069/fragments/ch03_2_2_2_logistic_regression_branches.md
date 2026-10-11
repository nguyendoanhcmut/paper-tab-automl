### 2.2. Logistic regression

* Mô hình hồi quy logistic (Logistic regression - LR) được sử dụng để phát triển các mô hình phân loại nhị phân (binary classification) nhằm ước tính xác suất vượt các ngưỡng nồng độ amoni dòng ra đã chọn ($\mathrm{NH}_4\text{--}\mathrm{N}_{\mathrm{eff}}$).
  * Với mỗi ngưỡng $m$, xác suất vượt ngưỡng $p_{\mathrm{NH}_4\text{--}\mathrm{N}_{\mathrm{eff}}}(m)$ ($p_m$) được xác định theo Công thức (1):
    $$p_{\mathrm{NH}_4\text{--}\mathrm{N}_{\mathrm{eff}}}(m) = \frac{\exp(X_m)}{1 + \exp(X_m)} \quad \text{cho } m = 1, 2, 3, \dots, n$$
  * Tỷ số chênh logarit (log-odds / hàm liên kết logit) tương ứng với hàm dự đoán tuyến tính $X_m$: $\ln\left(\frac{p_m}{1 - p_m}\right) = X_m$.
  * Hàm dự đoán tuyến tính $X_m$ được tính toán theo Công thức (2):
    $$X_m = \alpha_0 + \alpha_1 \cdot x_1 + \alpha_2 \cdot x_2 + \dots + \alpha_i \cdot x_i$$
  * Các hệ số hồi quy $\alpha_0, \dots, \alpha_i$ được ước lượng bằng phương pháp hợp lý cực đại (maximum likelihood).
* Các biến đầu vào mô hình $x_i$ gồm $11$ thông số: $\mathrm{NLR}$, $\mathrm{PLR}$, $\mathrm{SRT}$, $\mathrm{HRT}$, $F_{\mathrm{air}}$, $\mathrm{PAR}$, $\mathrm{PAR}_{\max}$, $\mathrm{DO}$, $\mathrm{DO}_{\max}$, $T$, và $T_{\max}$.
* Tám mô hình LR được xây dựng tương ứng với $8$ ngưỡng $\mathrm{NH}_4\text{--}\mathrm{N}_{\mathrm{eff}}$: $1{,}6$, $4{,}0$, $6{,}0$, $8{,}0$, $10{,}0$, $12{,}0$, $14{,}0$, và $16{,}0\text{ mg N}\cdot\text{L}^{-1}$.
  * Tập ngưỡng được lựa chọn và phân phối dữ liệu được hỗ trợ bởi hàm phân phối tích lũy thực nghiệm (empirical cumulative distribution function - CDF) (Fig. S2).
* Mô hình tương ứng với ngưỡng $\mathrm{NH}_4\text{--}\mathrm{N}_{\mathrm{eff}} = 1{,}6\text{ mg N}\cdot\text{L}^{-1}$ được sử dụng để ước tính xác suất tuân thủ giới hạn tái sử dụng nước theo quy chuẩn Ý (DM 185/2003), được định nghĩa là $p_{\mathrm{reuse}}$.
  * Việc áp dụng nhiều mô hình LR theo ngưỡng tuân theo sự điều chỉnh phương pháp luận từ cách tiếp cận logistic từng được áp dụng cho dự đoán khử màu [43], với đầy đủ chi tiết triển khai trong Phụ lục Thông tin (Mục S1).
  * Kết quả dự báo của mô hình LR được so sánh đối chiếu với các mô hình kinh điển như XGBoost và mạng perceptron đa tầng (Multilayer Perceptron - MLP) (Mục S2).
* Quy trình tiền xử lý dữ liệu nghiêm ngặt được thực hiện trước khi phát triển mô hình:
  * Các bản ghi không hoàn chỉnh chứa giá trị khuyết thiếu bị loại bỏ khỏi phân tích.
  * Dữ liệu đầu vào được chuẩn hóa min-max (min-max standardization) nhằm đảm bảo quy mô đồng nhất giữa các biến.
  * Sàng lọc sơ bộ điểm Z (Z-score pre-screening) được tiến hành nhằm xác định các ngoại lai và sai số đo lường tiềm ẩn:
    $$Z_i = \frac{x_i - \mu_i}{\sigma_i}$$
  * Tất cả các giá trị đều nằm trong ngưỡng chấp nhận ($Z_i = 0{,}01\text{--}2{,}95 < 3$; Bảng S2), chứng minh không có bằng chứng về sai số đo lường trong tập dữ liệu phân tích.
  * Phân phối thực nghiệm của dữ liệu đầu vào được đánh giá tự động bằng phần mềm XLSTAT; độ phù hợp giữa phân phối thực nghiệm và phân phối chuẩn lý thuyết được đánh giá thông qua kiểm định Kolmogorov-Smirnov với mức xác suất tới hạn $p = 0{,}05$ (Bảng S3).
  * Đối với các biến có phân phối lệch đáng kể so với phân phối chuẩn, phép biến đổi Box-Cox (Box-Cox transformation) được áp dụng trước khi tích hợp vào khung hồi quy logistic.
* Hiệu năng mô hình được đánh giá toàn diện thông qua $6$ chỉ số phân loại: độ chính xác (accuracy - ACC), độ nhạy / độ thu hồi (sensitivity/recall - SENS), độ đặc hiệu (specificity - SPEC), độ chuẩn xác (precision - Prec), diện tích dưới đường cong ROC (ROC-AUC), và điểm F1 (F1-score).
  * Việc tuân thủ ngưỡng $\mathrm{NH}_4\text{--}\mathrm{N}$ được định nghĩa là lớp dương tính (positive class).
  * SENS đại diện cho tỷ lệ các quan sát tuân thủ được phân loại chính xác, trong khi SPEC đại diện cho tỷ lệ các quan sát không tuân thủ được phân loại chính xác.
  * Prec định lượng tỷ lệ các quan sát được dự đoán tuân thủ mà trên thực nghiệm có tuân thủ, trong khi F1-score là trung bình điều hòa của Prec và SENS/recall.
  * ROC-AUC đánh giá năng lực của mô hình trong việc phân biệt giữa các quan sát tuân thủ và không tuân thủ trên toàn bộ dải ngưỡng xác suất.
  * Các công thức tính toán các chỉ số này được cung cấp trong Phụ lục Thông tin (Mục S1).
  * Khoảng tin cậy $95\%$ được xác định cho tất cả các chỉ số hiệu năng (SENS, SPEC, Prec, ACC, và F1-score) nhằm củng cố độ vững chắc của kết quả.
* Tập dữ liệu lựa chọn bao gồm tổng cộng $230$ đợt đo (measurement episodes):
  * Phương pháp lấy mẫu ngẫu nhiên phân tầng (stratified random sampling) được áp dụng trên dữ liệu từ $4$ giai đoạn vận hành ($1\text{--}4$) nhằm đảm bảo mô hình có khả năng khái quát hóa qua mọi biến động theo mùa và chế độ vận hành.
  * Dữ liệu từ bốn giai đoạn vận hành gồm $210$ đợt đo với dải nồng độ $\mathrm{NH}_4\text{--}\mathrm{N}_{\mathrm{eff}}$ biến thiên rộng, chia theo tỷ lệ $80\%$ dùng cho huấn luyện (training) và $20\%$ dùng cho kiểm tra (testing) trong mỗi giai đoạn:
    * Giai đoạn 1 (tháng 11/2016 – tháng 01/2017, $37\text{ ngày}$ vận hành): $\mathrm{SRT} = 4{,}5 \pm 0{,}2\text{ ngày}$, $\mathrm{HRT} = 1{,}5 \pm 0{,}10\text{ ngày}$, $F_{\mathrm{air}} = 0{,}23 \pm 0{,}01\text{ vvm}$, $\mathrm{NLR} = 15{,}8 \pm 8{,}2\text{ g N}\cdot\text{d}^{-1}$ (nghiên cứu ảnh hưởng của đường truyền ánh sáng lên hiệu suất quang hợp [36]).
    * Giai đoạn 2 (tháng 01/2017 – tháng 03/2017, $36\text{ ngày}$ vận hành): $\mathrm{SRT} = 4{,}5\text{--}6\text{ ngày}$, $\mathrm{HRT} = 1{,}5 \pm 0{,}10\text{ ngày}$, $F_{\mathrm{air}} = 0{,}23 \pm 0{,}00\text{ vvm}$, $\mathrm{NLR} = 13{,}0 \pm 2{,}8\text{ g N}\cdot\text{d}^{-1}$ (tối ưu hóa SRT/HRT để loại bỏ dinh dưỡng bằng vi tảo [36]).
    * Giai đoạn 3 (tháng 08/2017 – tháng 09/2017, $28\text{ ngày}$ vận hành): $\mathrm{SRT} = 3 \pm 0{,}1\text{ ngày}$, $\mathrm{HRT} = 1{,}25 \pm 0{,}10\text{ ngày}$, $F_{\mathrm{air}} = 0{,}24 \pm 0{,}03\text{ vvm}$, $\mathrm{NLR} = 16{,}0 \pm 2{,}4\text{ g N}\cdot\text{d}^{-1}$ (tối ưu hóa SRT/HRT để loại bỏ dinh dưỡng bằng vi tảo [36]).
    * Giai đoạn 4 (tháng 02/2018 – tháng 05/2018, $89\text{ ngày}$ vận hành): $\mathrm{SRT} = 2{,}5\text{--}4{,}5\text{ ngày}$, $\mathrm{HRT} = 1{,}25 \pm 0{,}10\text{ ngày}$, $F_{\mathrm{air}} = 0{,}22 \pm 0{,}04\text{ vvm}$, $\mathrm{NLR} = 20{,}5 \pm 5{,}1\text{ g N}\cdot\text{d}^{-1}$ (ảnh hưởng của SRT lên sự cạnh tranh giữa vi tảo và vi khuẩn oxy hóa amoni AOB [37]).
  * Quá trình huấn luyện và kiểm định mô hình sử dụng kiểm định chéo 10 lần (10-fold cross-validation) để giảm thiểu độ không đảm bảo và ngăn ngừa quá khớp (overfitting).
  * Bước xác thực bên ngoài độc lập (external verification) bổ sung được tiến hành trên tập con dự phòng gồm $20$ đợt đo độc lập đại diện cho phương sai lớn về chất lượng nước dòng ra ($\mathrm{NH}_4\text{--}\mathrm{N} = 1{,}6\text{--}32\text{ mg N/L}$).
  * Ngưỡng cắt phân loại (classification cut-offs) cho xác suất $p_m$ được tối ưu hóa riêng cho từng ngưỡng (thay vì cố định giá trị $p = 0{,}50$) nhằm cải thiện độ khớp của mô hình theo thông lệ trong y văn [44].

#### 2.2.1. Measurement-uncertainty and applicability-domain analysis

* Độ vững chắc (robustness) của mô hình LR trước độ không đảm bảo đo lường được đánh giá đối với $3$ biến môi trường và quá trình: oxy hòa tan ($\mathrm{DO}$), bức xạ quang hợp hoạt dụng ($\mathrm{PAR}$), và nhiệt độ ($T$).
  * Ba biến này được khảo sát riêng lẻ và đồng thời trong kịch bản kết hợp $T\text{--}\mathrm{DO}\text{--}\mathrm{PAR}$, trong khi các biến đầu vào còn lại được cố định tại giá trị trung bình của chúng.
  * Độ không đảm bảo đo lường được mô phỏng thông qua các giá trị đầu vào tuân theo phân phối chuẩn:
    $$x_i^* \sim \mathcal{N}\left(\mu_i, \sigma_i^2\right)$$
    trong đó $\mu_i$ là giá trị trung bình danh định của biến đầu vào được đánh giá, và độ lệch chuẩn $\sigma_i$ được thiết lập lần lượt bằng $5\%$, $10\%$, $15\%$, $20\%$, hoặc $25\%$ của giá trị trung bình $\mu_i$.
  * Đối với mỗi kịch bản, $10000$ lượt mô phỏng lấy mẫu (sampling simulations) được thực hiện để tạo lập phân phối thực nghiệm của xác suất dự đoán tuân thủ ngưỡng $\mathrm{NH}_4\text{--}\mathrm{N} < 1{,}6\text{ mg N}\cdot\text{L}^{-1}$.
  * Độ vững chắc được định lượng thông qua xác suất dự đoán trung bình ($\mu_p$), độ lệch chuẩn của xác suất ($\sigma_p$), và hệ số biến thiên:
    $$\mathrm{CV}_p = \frac{\sigma_p}{\mu_p}$$
* Miền áp dụng của mô hình (applicability domain) được xác định bởi các khoảng giá trị của các biến dự đoán biểu diễn trong tập dữ liệu phát triển mô hình.
  * Mọi dự đoán thực hiện khi một hoặc nhiều biến đầu vào rơi ra ngoài các khoảng giá trị này được coi là phép ngoại suy (extrapolations).
  * Các dự đoán ngoại suy không được giả định là duy trì được hiệu năng đã quan sát trong quá trình kiểm định mô hình.
