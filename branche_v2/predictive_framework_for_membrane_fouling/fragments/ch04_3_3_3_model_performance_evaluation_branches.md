### 3.3. Model Performance Evaluation

- Mục tiêu và thiết lập đánh giá hiệu năng mô hình dự báo áp suất xuyên màng ($\text{TMP}$) và độ thông lượng riêng ($\text{Spec. Flux}$):
  - Nhằm xác định độ chính xác dự báo (predictive accuracy) đối với $\text{TMP}$ và $\text{Spec. Flux}$, nhiều thuật toán học máy (machine learning) và mô hình thống kê (statistical models) được huấn luyện và kiểm định qua $4$ kịch bản vận hành thực nghiệm (Cases I–IV).
  - Các họ mô hình được đánh giá bao gồm các mô hình thống kê truyền thống (Linear Regression, Ridge, Lasso, ElasticNet) và các mô hình học máy tăng cường gradient (Gradient Boosting: XGBoost, CatBoost).
  - Bộ chỉ số định lượng sai số và độ khớp bao gồm hệ số xác định ($R^2$ / R-Squared), sai số tuyệt đối trung bình ($\text{MAE}$), sai số phần trăm tuyệt đối trung bình ($\text{MAPE}$), sai số bình phương trung bình ($\text{MSE}$) và căn bậc hai sai số bình phương trung bình ($\text{RMSE}$).

#### 3.3.1. Model Performance Based on Raw Data

- Hiệu năng dự báo áp suất xuyên màng không sử dụng thông số hiệu suất khử COD (Case I: $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSSs}$, $\text{DO}$, $\text{pH}$, $\text{Temp.} \rightarrow \text{TMP}$) (Table 4):
  - Các mô hình thống kê truyền thống thể hiện năng lực dự báo hạn chế với hệ số xác định $R^2 < 0.35$:
    - Linear Regression đạt $R^2 = 0.3439$, $\text{MAE} = 4.9834$, $\text{MAPE} = 0.1008$, $\text{MSE} = 35.6655$, $\text{RMSE} = 5.9721$.
    - Ridge Regression đạt $R^2 = 0.3168$, $\text{MAE} = 5.1590$, $\text{MAPE} = 0.1037$, $\text{MSE} = 37.1352$, $\text{RMSE} = 6.0939$.
    - Lasso Regression đạt $R^2 = 0.3396$, $\text{MAE} = 5.0665$, $\text{MAPE} = 0.1021$, $\text{MSE} = 35.8953$, $\text{RMSE} = 5.9913$.
    - ElasticNet Regression đạt $R^2 = 0.3292$, $\text{MAE} = 5.1052$, $\text{MAPE} = 0.1028$, $\text{MSE} = 36.4606$, $\text{RMSE} = 6.0383$.
  - Các mô hình tăng cường gradient đạt hiệu năng cao hơn đáng kể so với các mô hình thống kê tuyến tính:
    - XGBoost đạt $R^2 = 0.6769$, $\text{MAE} = 3.0784$, $\text{MAPE} = 0.0602$, $\text{MSE} = 17.5643$, $\text{RMSE} = 4.1910$.
    - CatBoost đạt hiệu năng cao nhất trong Case I với $R^2 = 0.7088$, $\text{MAE} = 2.9686$, $\text{MAPE} = 0.0591$, $\text{MSE} = 15.8281$ và $\text{RMSE} = 3.9785$ (mức thấp nhất trong tất cả các mô hình), chứng minh độ chính xác dự báo cao nhất trên tập dữ liệu thô.

| Model | R-Squared | MAE | MAPE | MSE | RMSE |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Linear | $0.3439$ | $4.9834$ | $0.1008$ | $35.6655$ | $5.9721$ |
| Ridge | $0.3168$ | $5.1590$ | $0.1037$ | $37.1352$ | $6.0939$ |
| Lasso | $0.3396$ | $5.0665$ | $0.1021$ | $35.8953$ | $5.9913$ |
| ElasticNet | $0.3292$ | $5.1052$ | $0.1028$ | $36.4606$ | $6.0383$ |
| XGBoost | $0.6769$ | $3.0784$ | $0.0602$ | $17.5643$ | $4.1910$ |
| CatBoost | $0.7088$ | $2.9686$ | $0.0591$ | $15.8281$ | $3.9785$ |

- Hiệu năng dự báo áp suất xuyên màng khi bổ sung thông số hiệu suất khử COD (Case II: $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSSs}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM} \rightarrow \text{TMP}$) (Table 5):
  - Việc bổ sung biến đặc trưng $\text{COD RM}$ mang lại mức cải thiện nhẹ cho hiệu năng tổng thể của các mô hình:
    - Linear Regression giữ nguyên giá trị: $R^2 = 0.3439$, $\text{MAE} = 4.9834$, $\text{MAPE} = 0.1008$, $\text{MSE} = 35.6655$, $\text{RMSE} = 5.9721$.
    - Ridge Regression cải thiện nhẹ lên $R^2 = 0.3457$, $\text{MAE} = 5.0564$, $\text{MAPE} = 0.1016$, $\text{MSE} = 35.5654$, $\text{RMSE} = 5.9637$.
    - Lasso Regression nâng lên $R^2 = 0.3769$, $\text{MAE} = 4.9247$, $\text{MAPE} = 0.0992$, $\text{MSE} = 33.8710$, $\text{RMSE} = 5.8199$.
    - ElasticNet Regression nâng lên $R^2 = 0.3563$, $\text{MAE} = 5.0050$, $\text{MAPE} = 0.1007$, $\text{MSE} = 34.9865$, $\text{RMSE} = 5.9149$.
    - XGBoost cải thiện $R^2$ từ $0.6769$ lên $0.6922$, với $\text{MAE} = 3.1245$, $\text{MAPE} = 0.0610$, $\text{MSE} = 16.7314$ và $\text{RMSE}$ giảm từ $4.1910$ xuống $4.0904$.
    - CatBoost duy trì vị trí mô hình dẫn đầu với $R^2 = 0.7059$, $\text{MAE} = 3.1014$, $\text{MAPE} = 0.0626$, $\text{MSE} = 15.9842$ và $\text{RMSE} = 3.9980$.
  - Mức độ thay đổi chỉ số $\text{RMSE}$ của CatBoost chỉ mang tính biên (từ $3.9785$ ở Case I sang $3.9980$ ở Case II), chứng minh $\text{COD RM}$ có đóng góp thông tin vào dự báo $\text{TMP}$ nhưng không làm gia tăng đột biến độ chính xác tổng thể đối với biến mục tiêu này.

| Model | R-Squared | MAE | MAPE | MSE | RMSE |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Linear | $0.3439$ | $4.9834$ | $0.1008$ | $35.6655$ | $5.9721$ |
| Ridge | $0.3457$ | $5.0564$ | $0.1016$ | $35.5654$ | $5.9637$ |
| Lasso | $0.3769$ | $4.9247$ | $0.0992$ | $33.8710$ | $5.8199$ |
| ElasticNet | $0.3563$ | $5.0050$ | $0.1007$ | $34.9865$ | $5.9149$ |
| XGBoost | $0.6922$ | $3.1245$ | $0.0610$ | $16.7314$ | $4.0904$ |
| CatBoost | $0.7059$ | $3.1014$ | $0.0626$ | $15.9842$ | $3.9980$ |

- Hiệu năng dự báo độ thông lượng riêng không sử dụng thông số hiệu suất khử COD (Case III: $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSSs}$, $\text{DO}$, $\text{pH}$, $\text{Temp.} \rightarrow \text{Spec. Flux}$) (Table 6):
  - Linear Regression đạt $R^2 = 0.6117$, cao hơn so với các biến thể điều chuẩn Ridge ($R^2 = 0.3951$), Lasso ($R^2 = 0.2497$) và ElasticNet ($R^2 = 0.3070$), cho thấy biến $\text{Spec. Flux}$ tồn tại mối quan hệ tuyến tính chặt chẽ hơn với các thông số vận hành đầu vào so với $\text{TMP}$:
    - Linear Regression đạt $\text{MAE} = 0.0068$, $\text{MAPE} = 0.1521$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0083$.
    - Ridge Regression đạt $\text{MAE} = 0.0084$, $\text{MAPE} = 0.1770$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0104$.
    - Lasso Regression đạt $\text{MAE} = 0.0094$, $\text{MAPE} = 0.1980$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0116$.
    - ElasticNet Regression đạt $\text{MAE} = 0.0090$, $\text{MAPE} = 0.1858$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0111$.
  - Các mô hình học máy thể hiện năng lực dự báo chính xác cao, trong đó CatBoost là mô hình đáng tin cậy nhất:
    - XGBoost đạt $R^2 = 0.5797$, $\text{MAE} = 0.0063$, $\text{MAPE} = 0.1347$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0087$.
    - CatBoost đạt $R^2 = 0.7317$, $\text{MAE} = 0.0058$, $\text{MAPE} = 0.1237$, $\text{MSE} = 0.0000$ và $\text{RMSE} = 0.0069$ (mức thấp nhất trong nhóm).

| Model | R-Squared | MAE | MAPE | MSE | RMSE |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Linear | $0.6117$ | $0.0068$ | $0.1521$ | $0.0001$ | $0.0083$ |
| Ridge | $0.3951$ | $0.0084$ | $0.1770$ | $0.0001$ | $0.0104$ |
| Lasso | $0.2497$ | $0.0094$ | $0.1980$ | $0.0001$ | $0.0116$ |
| ElasticNet | $0.3070$ | $0.0090$ | $0.1858$ | $0.0001$ | $0.0111$ |
| XGBoost | $0.5797$ | $0.0063$ | $0.1347$ | $0.0001$ | $0.0087$ |
| CatBoost | $0.7317$ | $0.0058$ | $0.1237$ | $0.0000$ | $0.0069$ |

- Hiệu năng dự báo độ thông lượng riêng khi tích hợp thông số hiệu suất khử COD (Case IV: $\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSSs}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM} \rightarrow \text{Spec. Flux}$) (Table 7):
  - Việc bổ sung biến đặc trưng $\text{COD RM}$ nâng cao hiệu năng trên toàn bộ các mô hình, đặc biệt là nhóm mô hình tăng cường gradient:
    - Linear Regression đạt $R^2 = 0.6200$, $\text{MAE} = 0.0068$, $\text{MAPE} = 0.1500$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0082$.
    - Ridge Regression tăng lên $R^2 = 0.4349$, $\text{MAE} = 0.0079$, $\text{MAPE} = 0.1685$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0100$.
    - Lasso Regression đạt $R^2 = 0.2513$, $\text{MAE} = 0.0094$, $\text{MAPE} = 0.1976$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0115$.
    - ElasticNet Regression đạt $R^2 = 0.3070$, $\text{MAE} = 0.0090$, $\text{MAPE} = 0.1858$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0111$.
    - XGBoost tăng lên $R^2 = 0.6555$, $\text{MAE} = 0.0059$, $\text{MAPE} = 0.1304$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0078$.
    - CatBoost đạt mức độ chính xác cao nhất với $R^2 = 0.7710$, $\text{MAE} = 0.0054$, $\text{MAPE} = 0.1149$, $\text{MSE} = 0.0000$ và $\text{RMSE} = 0.0064$ (thấp nhất trong toàn bộ các cấu hình).
  - Khẳng định vai trò của $\text{COD RM}$ và sự phù hợp của mô hình học kết hợp (ensemble learning):
    - Sự gia tăng rõ rệt về độ chính xác xác nhận $\text{COD RM}$ đóng góp quan trọng vào việc cải thiện dự báo $\text{Spec. Flux}$.
    - Kết quả này phù hợp với các nghiên cứu gần đây cho thấy các phương pháp tổ hợp (như gradient boosting) đạt hiệu năng cao hơn các mô hình truyền thống nhờ khả năng nắm bắt hiệu quả các tương tác phi tuyến (non-linear interactions) $[20]$.
    - Khung dự báo được phát triển đạt độ chính xác tương đương ($R^2 > 0.77$) trong khi sử dụng ít thông số đầu vào hơn đáng kể so với các tiếp cận tiêu tốn cảm biến thông thường (sensor-intensive approaches) $[27]$, chứng minh tính hiệu quả và khả năng ứng dụng thực tế cho các trạm MBR bị giới hạn nguồn lực cảm biến.
    - CatBoost duy trì vị thế dẫn đầu liên tục trên tất cả các mô hình và toàn bộ $4$ kịch bản dữ liệu thô.

| Model | R-Squared | MAE | MAPE | MSE | RMSE |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Linear | $0.6200$ | $0.0068$ | $0.1500$ | $0.0001$ | $0.0082$ |
| Ridge | $0.4349$ | $0.0079$ | $0.1685$ | $0.0001$ | $0.0100$ |
| Lasso | $0.2513$ | $0.0094$ | $0.1976$ | $0.0001$ | $0.0115$ |
| ElasticNet | $0.3070$ | $0.0090$ | $0.1858$ | $0.0001$ | $0.0111$ |
| XGBoost | $0.6555$ | $0.0059$ | $0.1304$ | $0.0001$ | $0.0078$ |
| CatBoost | $0.7710$ | $0.0054$ | $0.1149$ | $0.0000$ | $0.0064$ |

- Tổng kết so sánh hiệu năng trên tập dữ liệu thô:
  - Các mô hình tăng cường gradient (XGBoost và CatBoost) liên tục đạt kết quả cao hơn các mô hình thống kê truyền thống trên toàn bộ các phép đo.
  - CatBoost thể hiện tính ổn định cao nhất và đạt hiệu năng dẫn đầu trong mọi trường hợp kiểm thử.
  - Việc đưa thêm thông số $\text{COD RM}$ nâng cao độ chính xác dự báo rõ rệt đối với $\text{Spec. Flux}$, phản ánh tính liên quan mật thiết của đại lượng này đối với động học tắc nghẽn màng (membrane fouling dynamics).
  - Khung dự báo đề xuất, kết hợp kỹ thuật trích chọn đặc trưng nâng cao và AI có khả năng giải thích (explainable AI / XAI), chứng minh hiệu quả trong việc nắm bắt các cơ chế tắc nghẽn phức tạp và xếp hạng ưu tiên các thông số vận hành trọng yếu cho bài toán dự báo $\text{Spec. Flux}$ ở quy mô thực tế.

#### 3.3.2. Enhanced Model Performance with Robust Scaling and Moving Average

- Áp dụng các kỹ thuật tiền xử lý dữ liệu nâng cao trên Case IV ($\text{F/M}$, $\text{SV30}$, $\text{SVI}$, $\text{MLSSs}$, $\text{DO}$, $\text{pH}$, $\text{Temp.}$, $\text{COD RM} \rightarrow \text{Spec. Flux}$):
  - Kỹ thuật chuẩn hóa mạnh (Robust Scaling) và kỹ thuật trung bình trượt (Moving Average) được áp dụng nhằm nâng cao độ chính xác và tính ổn định của các mô hình dự báo.
  - Tác động từng bước của hai kỹ thuật tiền xử lý đặc trưng này được định lượng lần lượt tại Bảng 8 (Table 8) và Bảng 9 (Table 9).

- Đánh giá tác động của kỹ thuật chuẩn hóa mạnh (Robust Scaling) đối với hiệu năng mô hình (Table 8):
  - Robust Scaling được triển khai trước tiên nhằm giảm thiểu tác động của các giá trị ngoại lai (extreme values / outliers) và tăng cường độ ổn định cho mô hình:
    - Biến đổi dữ liệu này mang lại sự gia tăng rõ nét về hiệu năng, đặc biệt đối với các mô hình tăng cường gradient phi tuyến.
    - CatBoost đạt hiệu năng cao nhất với $R^2 = 0.7969$ (tăng từ $0.7710$) và $\text{RMSE} = 0.0060$ (giảm từ $0.0064$), cùng $\text{MAE} = 0.0050$, $\text{MAPE} = 0.1074$, $\text{MSE} = 0.0000$, chứng minh khả năng tổng quát hóa vững chắc.
    - XGBoost duy trì hệ số xác định $R^2 = 0.6555$, $\text{MAE} = 0.0059$, $\text{MAPE} = 0.1304$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0078$, giữ được tính ổn định dù độ chính xác thấp hơn CatBoost.
    - Linear Regression và Ridge Regression có mức cải thiện vừa phải, đạt $R^2$ xấp xỉ $0.63$: Linear Regression đạt $R^2 = 0.6344$, $\text{MAE} = 0.0066$, $\text{MAPE} = 0.1477$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0081$; Ridge Regression đạt $R^2 = 0.6356$, $\text{MAE} = 0.0066$, $\text{MAPE} = 0.1478$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0081$.
    - ElasticNet Regression và Lasso Regression tiếp tục ghi nhận kết quả kém khi mô hình hóa các quan hệ phức tạp: ElasticNet đạt $R^2 = 0.2953$, $\text{MAE} = 0.0095$, $\text{MAPE} = 0.2077$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0112$; Lasso Regression suy giảm về $R^2 = -0.0048$, $\text{MAE} = 0.0112$, $\text{MAPE} = 0.2392$, $\text{MSE} = 0.0002$, $\text{RMSE} = 0.0134$.

| Model | R-Squared | MAE | MAPE | MSE | RMSE |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Linear | $0.6344$ | $0.0066$ | $0.1477$ | $0.0001$ | $0.0081$ |
| Ridge | $0.6356$ | $0.0066$ | $0.1478$ | $0.0001$ | $0.0081$ |
| Lasso | $-0.0048$ | $0.0112$ | $0.2392$ | $0.0002$ | $0.0134$ |
| ElasticNet | $0.2953$ | $0.0095$ | $0.2077$ | $0.0001$ | $0.0112$ |
| XGBoost | $0.6555$ | $0.0059$ | $0.1304$ | $0.0001$ | $0.0078$ |
| CatBoost | $0.7969$ | $0.0050$ | $0.1074$ | $0.0000$ | $0.0060$ |

- Tích hợp phụ thuộc chuỗi thời gian bằng kỹ thuật trung bình trượt $5\text{ ngày}$ (5-day Moving Average) (Table 9):
  - Do hiện tượng tắc nghẽn màng diễn tiến mang tính tích lũy dần theo thời gian (cumulatively over time), cửa sổ trung bình trượt $5\text{ ngày}$ (5-day moving average, văn bản gốc ghi "5 says") được bổ sung nhằm tích hợp các phụ thuộc thời gian (temporal dependencies) vào mô hình dự báo:
    - Cửa sổ $5\text{ ngày}$ được xác định là tối ưu (như mô tả tại Mục 3.2.2) thông qua việc đánh giá có hệ thống các chu kỳ dịch chuyển ngày khác nhau cho từng đặc trưng đầu vào trong phạm vi $1\text{ tuần}$ và so sánh hiệu năng qua $R^2$ và $\text{RMSE}$; cấu hình đạt độ chính xác cao nhất được chọn áp dụng.
  - Tác động làm mượt và thu nhận xu hướng lịch sử mang lại bước cải thiện hiệu năng then chốt:
    - CatBoost đạt hiệu năng nâng cao rõ rệt, vươn tới $R^2 = 0.8374$ và giảm $\text{RMSE}$ xuống $0.0054$, cùng $\text{MAE} = 0.0042$, $\text{MAPE} = 0.0863$, $\text{MSE} = 0.0000$, làm nổi bật tính hữu hiệu của việc tích hợp xu hướng lịch sử.
    - Phát hiện này củng cố các kết luận từ nghiên cứu trước $[12]$ về tác động tích lũy của điều kiện vận hành lên quá trình tắc nghẽn màng.
    - Trong khi các mô hình thống kê trước đây gặp trở ngại khi xử lý sự phụ thuộc thời gian $[14]$, giải pháp trung bình trượt trong nghiên cứu này giải quyết trực tiếp động học tắc nghẽn có độ trễ thời gian (time-delayed fouling dynamics), mang lại mức gia tăng $> 10\%$ về giá trị $R^2$ so với các mô hình chạy trên dữ liệu thô.
    - XGBoost tăng mạnh độ chính xác, đạt $R^2 = 0.7404$, $\text{MAE} = 0.0055$, $\text{MAPE} = 0.1168$, $\text{MSE} = 0.0000$, $\text{RMSE} = 0.0068$, hưởng lợi trực tiếp từ hiệu ứng làm mượt nhiễu (smoothing effect) của trung bình trượt.
    - Linear Regression và Ridge Regression cũng cho thấy sự cải thiện đồng đều, đạt $R^2$ xấp xỉ $0.66$ (Linear: $R^2 = 0.6623$, $\text{MAE} = 0.0065$, $\text{MAPE} = 0.1445$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0078$; Ridge: $R^2 = 0.6617$, $\text{MAE} = 0.0065$, $\text{MAPE} = 0.1460$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0078$), chứng tỏ trung bình trượt đóng góp vào biểu diễn đặc trưng ổn định hơn ngay cả trên các cấu trúc mô hình đơn giản.
    - Lasso Regression và ElasticNet giữ nguyên xu hướng hiệu năng thấp: Lasso đạt $R^2 = -0.0048$, $\text{MAE} = 0.0112$, $\text{MAPE} = 0.2392$, $\text{MSE} = 0.0002$, $\text{RMSE} = 0.0134$; ElasticNet đạt $R^2 = 0.3145$, $\text{MAE} = 0.0093$, $\text{MAPE} = 0.2022$, $\text{MSE} = 0.0001$, $\text{RMSE} = 0.0110$.

| Model | R-Squared | MAE | MAPE | MSE | RMSE |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Linear | $0.6623$ | $0.0065$ | $0.1445$ | $0.0001$ | $0.0078$ |
| Ridge | $0.6617$ | $0.0065$ | $0.1460$ | $0.0001$ | $0.0078$ |
| Lasso | $-0.0048$ | $0.0112$ | $0.2392$ | $0.0002$ | $0.0134$ |
| ElasticNet | $0.3145$ | $0.0093$ | $0.2022$ | $0.0001$ | $0.0110$ |
| XGBoost | $0.7404$ | $0.0055$ | $0.1168$ | $0.0000$ | $0.0068$ |
| CatBoost | $0.8374$ | $0.0042$ | $0.0863$ | $0.0000$ | $0.0054$ |

- Đánh giá tổng hợp cơ chế kỹ thuật đặc trưng và luận cứ phương pháp luận trên dữ liệu thực địa:
  - Chuẩn hóa mạnh (Robust Scaling) nâng cao hiệu năng mô hình thông qua cơ chế triệt tiêu ảnh hưởng của các giá trị cực trị, tạo lợi thế đặc biệt rõ nét cho các mô hình học máy phi tuyến.
  - Trung bình trượt (Moving Average) gia tăng độ chính xác nhờ thu nhận sát thực bản chất phụ thuộc thời gian và tính chất tích lũy dần của lớp tắc nghẽn màng.
  - Luận cứ về tính không khả dụng của kiểm định thống kê cổ điển: Do toàn bộ các mô hình đều được huấn luyện và kiểm thử trên cùng một tập dữ liệu chuỗi thời gian vận hành thực tế từ một trạm MBR quy mô công nghiệp duy nhất, các kiểm định thống kê truyền thống như t-test hay khoảng tin cậy (confidence intervals) — vốn tiền giả định các mẫu lấy lặp độc lập (independent repeated samples) — không thể áp dụng được về mặt lý thuyết trong bối cảnh này.
  - Định hướng so sánh mô hình tập trung vào tính nhất quán của hiệu năng dự báo và khả năng diễn giải cơ chế dưới các điều kiện vận hành thực tế, thay vì dựa vào ý nghĩa thống kê từ việc lấy mẫu ngẫu nhiên lặp lại.
  - CatBoost thể hiện hiệu năng cao ổn định và bền vững, có khả năng xử lý vững chắc các tương tác phi tuyến phức tạp trong hệ thống MBR; sự cải thiện đồng thời của XGBoost tái khẳng định tầm quan trọng quyết định của kỹ thuật xử lý đặc trưng (feature engineering) trong bài toán dự báo tắc nghẽn màng.
