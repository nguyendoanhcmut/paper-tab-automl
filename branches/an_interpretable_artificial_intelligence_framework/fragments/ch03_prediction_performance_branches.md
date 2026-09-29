## 3.1. Hiệu suất dự đoán của mô hình học máy (Machine Learning Model Prediction Performance)

### 3.1.1. Hiệu suất dự đoán biến mục tiêu đầu ra (Output Prediction Performance)

#### 3.1.1.1. Phân cấp khả năng dự đoán và căn cứ lựa chọn biến mục tiêu
- Hệ thống MBR công nghiệp yêu cầu dự đoán chính xác ba biến mục tiêu vận hành cốt lõi: áp suất xuyên màng (TMP), lưu lượng nước thấm (Permeate Flow) và mức nước bể màng (Membrane Tank Level).
- Nghiên cứu chủ động loại bỏ chất lượng nước đầu ra (TOC nước thấm) khỏi danh sách biến mục tiêu hồi quy:
  - Thiết bị phân tích TOC trực tuyến có dải đo hẹp $0.03\text{--}1000\text{ ppb}$, thường xuyên vận hành sát ngưỡng phát hiện dưới ($0.03\text{ ppb}$).
  - Màng siêu lọc sợi rỗng (UF PVDF) giữ lại gần như toàn bộ chất rắn lơ lửng và chất hữu cơ phân tử lượng lớn. Tín hiệu đo chủ yếu chứa nhiễu thiết bị.
  - Chất lượng nước thấm trong MBR ngập nước phụ thuộc tính toàn vẹn cơ học của màng (hiện tượng đứt gãy sợi màng gây biến đổi bậc thang), không phải hàm liên tục của các thông số sinh học. Đây là bài toán giám sát tính toàn vẹn màng, không phải bài toán hồi quy liên tục.
  - Ba biến mục tiêu được chọn cho phép người vận hành chủ động điều phối và đánh đổi theo từng chu kỳ giờ.
- Benchmark đánh giá 16 thuật toán học máy thuộc 6 họ mô hình cấu trúc khác nhau:
  - Họ Tuyến tính (Linear): Hồi quy tuyến tính cổ điển (Linear Regression).
  - Họ Tuyến tính chính quy hóa (Regularized Linear): Ridge Regression, Lasso Regression, Elastic Net.
  - Họ Máy vectơ hỗ trợ (Support Vector Machine): SVR với nhân hàm bán kính RBF.
  - Họ Dựa trên cá thể (Instance-based): Thuật toán $k$ láng giềng gần nhất (KNN).
  - Họ Tập hợp cây (Ensemble Tree): Cây quyết định (Decision Tree), Rừng ngẫu nhiên (Random Forest), Cây ngẫu nhiên hóa cực độ (Extra Trees), Bagging, AdaBoost, Gradient Boosting, Hist Gradient Boosting, XGBoost, LightGBM.
  - Họ Mạng nơ-ron nhân tạo (Neural Network): Perceptron đa tầng (MLP).
- Phân cấp khả năng dự đoán hình thành rõ rệt theo trật tự vật lý: TMP đạt độ chính xác cao nhất, tiếp theo là lưu lượng nước thấm, cuối cùng là mức nước bể màng.

#### 3.1.1.2. Hiệu suất dự đoán áp suất xuyên màng TMP
- Nhóm thuật toán tập hợp cây thể hiện ưu thế vượt trội tuyệt đối trên biến TMP với phân chia ngẫu nhiên ($70:30$ và $80:20$):
  - Thuật toán Extra Trees dẫn đầu toàn diện: $R^2 = 0.988$, $\text{RMSE} = 0.010\text{ bar}$ ($1.0\text{ kPa}$), $\text{MAE} = 0.005\text{ bar}$ ($0.5\text{ kPa}$), độ lệch tổng thể $\Delta R^2 = 0.012$.
  - Thuật toán Bagging đạt vị trí thứ hai: $R^2 = 0.978$, $\text{RMSE} = 0.014\text{ bar}$ ($1.4\text{ kPa}$), $\text{MAE} = 0.006\text{ bar}$ ($0.6\text{ kPa}$), $\Delta R^2 = 0.019$.
  - Thuật toán Random Forest đạt kết quả tương đương: $R^2 = 0.978$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.006\text{ bar}$, $\Delta R^2 = 0.019$.
  - Thuật toán LightGBM bám sát: $R^2 = 0.978$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.008\text{ bar}$, $\Delta R^2 = 0.015$.
  - Thuật toán XGBoost đạt độ chính xác cao: $R^2 = 0.977$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.007\text{ bar}$, $\Delta R^2 = 0.022$.
  - Toàn bộ 5 thuật toán tập hợp hàng đầu đều vượt ngưỡng $R^2 > 0.97$.
- Các thuật toán phi ensemble và phi tuyến đạt hiệu suất khả quan:
  - Hist Gradient Boosting đạt $R^2 = 0.976$, $\text{RMSE} = 0.014\text{ bar}$, $\text{MAE} = 0.008\text{ bar}$.
  - Thuật toán KNN đạt $R^2 = 0.969$, $\text{RMSE} = 0.016\text{ bar}$, $\text{MAE} = 0.007\text{ bar}$.
  - Mạng nơ-ron MLP đạt $R^2 = 0.951$, $\text{RMSE} = 0.020\text{ bar}$, $\text{MAE} = 0.011\text{ bar}$.
  - Decision Tree đơn lẻ đạt $R^2 = 0.942$, $\text{RMSE} = 0.022\text{ bar}$, $\text{MAE} = 0.010\text{ bar}$.
  - Gradient Boosting cơ bản đạt $R^2 = 0.937$, $\text{RMSE} = 0.023\text{ bar}$, $\text{MAE} = 0.014\text{ bar}$.
  - SVR nhân RBF đạt $R^2 = 0.893$, $\text{RMSE} = 0.030\text{ bar}$, $\text{MAE} = 0.016\text{ bar}$.
- Các thuật toán tuyến tính và tăng cường yếu thất bại nặng:
  - AdaBoost suy giảm độ chính xác rõ rệt: $R^2 = 0.781$, $\text{RMSE} = 0.042\text{ bar}$, $\text{MAE} = 0.037\text{ bar}$.
  - Linear Regression và Ridge Regression dừng lại ở $R^2 = 0.499$, $\text{RMSE} = 0.064\text{ bar}$, $\text{MAE} = 0.045\text{ bar}$.
  - Elastic Net đạt $R^2 = 0.480$, $\text{RMSE} = 0.065\text{ bar}$, $\text{MAE} = 0.046\text{ bar}$.
  - Lasso Regression đạt $R^2 = 0.440$, $\text{RMSE} = 0.068\text{ bar}$, $\text{MAE} = 0.049\text{ bar}$.
- Cơ chế vật lý củng cố độ chính xác cao của TMP:
  - TMP phản ánh điện trở tắc nghẽn màng lọc trong hệ thống MBR ngập nước.
  - Quá trình tích tụ tắc nghẽn diễn ra liên tục theo nồng độ MLSS, cường độ sục khí khuấy trộn bề mặt và các đặc tính bùn phụ thuộc thời gian lưu bùn (SRT).
  - Tất cả các biến số chi phối chính đều được thu thập trực tiếp và cung cấp đầy đủ vào mô hình học máy.
  - Tín hiệu áp suất hút đo ở phía nước thấm có độ ổn định cao và tỷ số tín hiệu trên nhiễu (SNR) lớn hơn so với cấu hình màng nén áp lực.

#### 3.1.1.3. Hiệu suất dự đoán lưu lượng nước sau lọc (Permeate Flow)
- Thứ hạng các thuật toán dự đoán lưu lượng thấm tương đồng với TMP nhưng chỉ số $R^2$ giảm nhẹ:
  - Extra Trees tiếp tục dẫn đầu: $R^2 = 0.933$, $\text{RMSE} = 0.066\text{ m}^3\text{/min}$ ($3.96\text{ m}^3\text{/h}$), $\text{MAE} = 0.052\text{ m}^3\text{/min}$ ($3.12\text{ m}^3\text{/h}$), $\Delta R^2 = 0.067$.
  - Thuật toán Bagging đứng thứ hai: $R^2 = 0.910$, $\text{RMSE} = 0.076\text{ m}^3\text{/min}$, $\text{MAE} = 0.059\text{ m}^3\text{/min}$, $\Delta R^2 = 0.076$.
  - Random Forest xếp thứ ba: $R^2 = 0.909$, $\text{RMSE} = 0.077\text{ m}^3\text{/min}$, $\text{MAE} = 0.059\text{ m}^3\text{/min}$, $\Delta R^2 = 0.076$.
  - XGBoost xếp thứ tư: $R^2 = 0.906$, $\text{RMSE} = 0.078\text{ m}^3\text{/min}$, $\text{MAE} = 0.061\text{ m}^3\text{/min}$, $\Delta R^2 = 0.081$.
  - Hist Gradient Boosting hoàn thành top năm: $R^2 = 0.899$, $\text{RMSE} = 0.081\text{ m}^3\text{/min}$, $\text{MAE} = 0.064\text{ m}^3\text{/min}$, $\Delta R^2 = 0.048$.
  - Các thuật toán kế tiếp: LightGBM ($R^2 = 0.898$), KNN ($R^2 = 0.894$), MLP ($R^2 = 0.861$), Gradient Boosting ($R^2 = 0.824$), Decision Tree ($R^2 = 0.785$), SVR ($R^2 = 0.771$).
  - Thuật toán kém hiệu quả: AdaBoost ($R^2 = 0.655$, $\text{RMSE} = 0.150\text{ m}^3\text{/min}$), Linear/Ridge Regression ($R^2 = 0.469$, $\text{RMSE} = 0.185\text{ m}^3\text{/min}$), Elastic Net ($R^2 = 0.435$), Lasso ($R^2 = 0.393$).
- Cơ chế kỹ thuật giải thích sự suy giảm độ chính xác so với TMP:
  - Lưu lượng thấm không chỉ phản ánh mức độ tắc nghẽn màng mà còn phụ thuộc điểm đặt lưu lượng của người vận hành, chu kỳ rửa ngược (backwash) định kỳ và các xung đột thủy lực ngắn hạn.
  - Dữ liệu trung bình theo giờ không thể phản ánh trọn vẹn các dao động thủy lực diễn ra ở quy mô phút.
  - Sục khí gián đoạn tạo ra lực xáo trộn tức thời khiến lưu lượng lọc dao động mạnh. Các đặc trưng sinh học và vận hành theo giờ không cung cấp đủ thông tin để mô hình giải quyết biến động vi mô này.

#### 3.1.1.4. Hiệu suất dự đoán mức nước bể màng (Membrane Tank Water Level)
- Mức nước bể màng là biến mục tiêu phức tạp nhất trong hệ thống:
  - Extra Trees duy trì vị trí số một: $R^2 = 0.908$, $\text{RMSE} = 0.341\%$, $\text{MAE} = 0.227\%$, $\Delta R^2 = 0.092$.
  - XGBoost xếp vị trí thứ hai: $R^2 = 0.843$, $\text{RMSE} = 0.444\%$, $\text{MAE} = 0.292\%$, $\Delta R^2 = 0.143$.
  - Nhóm thuật toán đạt $R^2 \approx 0.839$: Bagging ($R^2 = 0.839$, $\text{RMSE} = 0.450\%$), Random Forest ($R^2 = 0.839$, $\text{RMSE} = 0.450\%$), Hist Gradient Boosting ($R^2 = 0.839$, $\text{RMSE} = 0.450\%$).
  - LightGBM đạt $R^2 = 0.822$, $\text{RMSE} = 0.473\%$, $\text{MAE} = 0.321\%$.
  - Thuật toán KNN đạt $R^2 = 0.813$, $\text{RMSE} = 0.485\%$, $\text{MAE} = 0.298\%$.
  - Các họ mô hình khác suy giảm sâu: MLP ($R^2 = 0.756$), Gradient Boosting ($R^2 = 0.698$), Decision Tree ($R^2 = 0.650$), SVR ($R^2 = 0.498$), AdaBoost ($R^2 = 0.308$).
  - Nhóm tuyến tính hoàn toàn mất khả năng dự đoán: Linear Regression và Ridge Regression chỉ đạt $R^2 = 0.195$ ($\text{RMSE} = 1.006\%$), Elastic Net đạt $R^2 = 0.159$, Lasso đạt $R^2 = 0.117$.
- Căn nguyên vật lý chi phối trật tự dự đoán:
  - TMP dễ dự đoán nhất ($R^2 = 0.988$) do tích lũy trở lực tắc nghẽn qua nhiều giờ đến nhiều ngày. Các biến điều khiển chính như SRT và MLSS biến thiên chậm và được đo đạc chính xác.
  - Lưu lượng nước thấm có mức độ dự đoán trung gian ($R^2 = 0.933$) vì phụ thuộc một phần vào trạng thái màng và một phần vào nhu cầu sản xuất, chu kỳ rửa ngược cùng dao động thủy lực ngắn hạn.
  - Mức nước bể màng khó dự đoán nhất ($R^2 = 0.908$) vì đây là trạng thái thủy lực phản ứng nhanh. Mức nước bị chi phối bởi cân bằng tức thời giữa lưu lượng nước cấp đầu vào, lưu lượng hút màng, tuần hoàn nội bộ, xả bùn dư và thuật toán bật tắt bơm theo mức nước. Các quá trình này diễn ra theo từng phút và không nằm trong tập biến đầu vào của mô hình.
- Giá trị ứng dụng thực tiễn:
  - Mô hình học máy phù hợp nhất cho việc lập kế hoạch kiểm soát TMP dài hạn. Ngược lại, mức nước bể màng cần được xử lý thông qua các cơ chế điều khiển nhanh.
  - Mặc dù vậy, sai số tuyệt đối của Extra Trees ($\text{MAE} = 0.227\%$) vẫn nằm sâu bên trong biên độ kiểm soát cho phép $2.0\%$ của nhà máy, đáp ứng yêu cầu vận hành thực tế.

---

### 3.1.2. So sánh mô hình, tính nhất quán và kiểm định độc lập (Model Comparison, Consistency and Independent Validation)

#### 3.1.2.1. Phân kỳ bản chất giữa mô hình tuyến tính và phi tuyến
- Kết quả thực nghiệm tạo ra khoảng cách lớn và có hệ thống giữa mô hình tuyến tính và phi tuyến trên cả ba biến mục tiêu:
  - Mô hình tuyến tính cổ điển (Linear Regression) và Ridge Regression chỉ đạt $R^2 = 0.499$ cho TMP, $0.469$ cho lưu lượng và $0.195$ cho mức nước bể màng.
  - Các biến thể chính quy hóa như Elastic Net ($R^2 = 0.480, 0.435, 0.159$) và Lasso ($R^2 = 0.440, 0.393, 0.117$) suy giảm thêm do hệ số phạt loại bỏ các thông số hồi quy có giá trị thông tin nhỏ.
  - Ngược lại, các mô hình ensemble hàng đầu đều vượt ngưỡng $R^2 > 0.90$ trên cả ba mục tiêu.
- Thử nghiệm giả thuyết có cấu trúc chứng minh cơ chế vận hành sinh học:
  - Thất bại của nhóm mô hình cộng tính tuyến tính cùng với thành công của thuật toán phân vùng đệ quy khẳng định mối quan hệ giữa sinh khối bùn và màng lọc bị chi phối bởi các ngưỡng giới hạn (thresholds) và tương tác phi tuyến (interactions).
  - Hiện tượng này hoàn toàn phù hợp với lý thuyết tắc nghẽn màng. Điện trở lớp bánh bùn tăng vọt phi tuyến khi vượt nồng độ MLSS tới hạn. Hiệu quả sục khí suy giảm dần khi vượt vận tốc xáo trộn tới hạn. Tỷ lệ F/M và SRT tương tác phi cộng tính lên trạng thái bùn.

#### 3.1.2.2. So sánh giữa các họ thuật toán Ensemble và phi tuyến
- Trong họ Ensemble, các biến thể đóng bao ngẫu nhiên (Bagging, Random Forest, Extra Trees) luôn vượt trội hơn các mô hình tăng cường tuần tự (Sequential Boosting):
  - Tuy nhiên, XGBoost ($R^2 = 0.977$) và LightGBM ($R^2 = 0.978$) đạt hiệu suất tiệm cận Bagging trên biến TMP.
  - Ngược lại, AdaBoost thể hiện hiệu suất kém nhất trên mọi biến mục tiêu ($R^2 = 0.781$ cho TMP, $0.655$ cho lưu lượng, $0.308$ cho mức nước). Cơ chế gán trọng số thích nghi của AdaBoost rất nhạy cảm với dị thường cảm biến và nhiễu ngẫu nhiên trong dữ liệu SCADA công nghiệp.
  - Extra Trees vượt qua Random Forest nhờ kỹ thuật ngẫu nhiên hóa bổ sung các ngưỡng phân chia tại mỗi nút cây. Kỹ thuật này giúp giảm phương sai mô hình hiệu quả hơn khi xử lý tín hiệu cảm biến thực địa.
- Đánh giá các mô hình phi cây:
  - Thuật toán KNN đạt hiệu suất cao ($R^2 = 0.969$ cho TMP, $0.894$ cho lưu lượng, $0.813$ cho mức nước). Kết quả chứng minh phản ứng của màng lọc có tính quy luật trơn đều cục bộ trong không gian vận hành. Đặc tính này là tiền đề toán học giúp việc thiết lập không gian vận hành tối ưu trở nên khả thi và có ý nghĩa.
  - Cây quyết định đơn lẻ (Decision Tree) xảy ra hiện tượng quá khớp (overfitting) nghiêm trọng đối với biến mức nước bể màng: $R^2$ tập huấn luyện đạt $0.890$ nhưng giảm mạnh xuống $0.650$ trên tập kiểm tra độc lập.
  - Phân tích độ bền vững qua 20 lần phân chia ngẫu nhiên lặp lại xác nhận Extra Trees duy trì vị trí dẫn đầu với $R^2$ trung bình cao nhất cùng RMSE và MAE thấp nhất trên cả ba biến đầu ra.

#### 3.1.2.3. Kiểm định độc lập trên nhánh màng song song B (Cross-Train Validation)
- Khả năng chuyển giao mô hình được kiểm định trên hệ thống màng độc lập gồm 4593 bản ghi theo giờ từ nhánh màng B song song trong cùng nhà máy:
  - Nhánh màng B vận hành dưới điều kiện dòng vào độc lập và có lịch sử tắc nghẽn màng riêng biệt so với nhánh màng A.
  - Mô hình Extra Trees được huấn luyện trên dữ liệu ban đầu và áp dụng trực tiếp lên nhánh màng B mà không cần tái huấn luyện trọng số.
- Kết quả kiểm định xuyên nhánh đạt độ chính xác cao:
  - Áp suất xuyên màng TMP: $R^2 = 0.996$, độ lệch chuẩn sai số đạt $0.014\text{ bar}$ ($1.4\text{ kPa}$).
  - Lưu lượng nước thấm: $R^2 = 0.980$, độ lệch chuẩn sai số đạt $0.052\text{ m}^3\text{/min}$.
  - Mức nước bể màng: $R^2 = 0.972$, độ lệch chuẩn sai số đạt $0.306\%$.
  - Sai số dự đoán trung bình trên cả ba biến mục tiêu đều tiệm cận giá trị 0.
- Đặc tính phân phối sai số của TMP:
  - Phân phối sai số TMP lệch phải nhẹ với hệ số bất đối xứng $\text{skewness} = 1.025$.
  - Hiện tượng này phản ánh xu hướng đánh giá thấp nhẹ giá trị TMP trong các tình huống tắc nghẽn nghiêm trọng cực đoan.
  - Về mặt kỹ thuật, xu hướng này mang tính bảo thủ an toàn vì kích hoạt chu kỳ rửa màng sớm hơn thời điểm tắc nghẽn thực tế, bảo vệ an toàn cho sợi màng.
- Khẳng định tính bất biến vật lý của mô hình:
  - Nhánh màng B chạy song song cùng khoảng thời gian lịch và dùng chung nguồn nước thải đầu vào. Kiểm định này xác lập khả năng chuyển giao xuyên nhánh màng thay vì chuyển giao theo thời gian.
  - Mô hình đã học được quy luật thủy lực và sinh học nền tảng, không bị phụ thuộc vào đặc tính cơ khí cục bộ của từng cụm module màng.

#### 3.1.2.4. Tính nhất quán xếp hạng và căn cứ lựa chọn mô hình thống nhất
- Extra Trees chứng minh tính nhất quán vượt trội khi giữ vững vị trí số một trên cả ba biến mục tiêu (TMP, lưu lượng thấm, mức nước bể màng) qua toàn bộ các bài kiểm tra:
  - Dẫn đầu trên tập kiểm tra ngẫu nhiên ban đầu.
  - Dẫn đầu trong đánh giá độ bền vững 20 lần phân chia lặp lại.
  - Dẫn đầu trong kiểm định chuyển giao xuyên nhánh màng song song B.
- Nghiên cứu quyết định chọn duy nhất mô hình Extra Trees cho các phân tích khả năng diễn giải SHAP (Mục 3.2) và tối ưu hóa không gian vận hành (Mục 3.3).
- Việc dùng chung một cấu trúc mô hình cho cả ba biến mục tiêu đảm bảo tính nhất quán toán học của khung vận hành và giúp so sánh tầm quan trọng đặc trưng một cách đồng bộ.

---

### 3.1.3. Độ bền vững của việc lựa chọn mô hình đối với thiết kế kiểm định (Robustness of Model Selection to Validation Design)

#### 3.1.3.1. Đánh giá độ bền vững qua bốn thiết kế kiểm định độc lập
- Để ngăn ngừa sai lệch từ một phép chia dữ liệu duy nhất, nghiên cứu kiểm tra Extra Trees trên bốn thiết kế kiểm định độc lập:
  - Phân chia ngẫu nhiên truyền thống ($70:30$ và $80:20$).
  - Phân chia theo khối thời gian liên tục 24 giờ (Blocked partition 24-h).
  - Phân chia theo trình tự thời gian chặt chẽ (Chronological partition).
  - Kiểm định độc lập trên nhánh màng song song B.
- Kết quả khẳng định tính vững chắc của mô hình:
  - Extra Trees xếp hạng nhất trong 8 trên 9 tổ hợp mô hình - thiết kế - biến mục tiêu.
  - Extra Trees giữ vị trí số một tuyệt đối cho mọi biến mục tiêu dưới cả thiết kế ngẫu nhiên và thiết kế phân chia khối 24 giờ.
- Tính bất biến của kết luận công nghệ:
  - Thời gian lưu bùn (SRT) luôn duy trì vị trí tác nhân chi phối số một đối với TMP và mức bể màng trên toàn bộ các chế độ kiểm định: phân chia ngẫu nhiên, phân chia khối 24 giờ, phân chia khối 168 giờ (1 tuần), và phân chia theo trình tự thời gian.
  - Kết luận này chứng minh các phát hiện cơ chế là đặc tính vật lý khách quan của nhà máy MBR, không phải kết quả ngẫu nhiên của một phương pháp chia tập dữ liệu.

#### 3.1.3.2. Kiểm định phân chia khối thời gian 24 giờ (Blocked Partition 24-h)
- Dữ liệu cảm biến SCADA thu thập theo từng giờ vốn có tính tự tương quan chuỗi thời gian cao. Thiết kế phân chia khối 24 giờ phân bổ các khối giờ liên tục làm đơn vị nguyên vẹn để kiểm soát rò rỉ thông tin lân cận.
- Extra Trees duy trì độ chính xác cao đối với hệ thống công nghiệp quy mô đầy đủ:
  - TMP đạt $R^2 = 0.830$, tương ứng $\text{RMSE} = 0.036\text{ bar}$ ($3.6\text{ kPa}$) trên tổng dải vận hành thực tế rộng $0.43\text{ bar}$.
  - Sai số tuyệt đối trung bình $\text{MAE}$ chỉ chiếm $16.3\%$ khoảng tứ phân vị (IQR) của chuỗi đo thực tế.
- Kết quả chứng minh mô hình học được động lực học thực chất của quá trình lọc màng, không đơn thuần dự đoán dựa vào hiện tượng tự tương quan giữa các giờ liền kề.

#### 3.1.3.3. Kiểm định ngoại suy ngoài thời gian (Out-of-Time Chronological Validation)
- Kiểm định theo trình tự thời gian mô phỏng kịch bản triển khai trong thực tế sản xuất:
  - Kịch bản thông thường huấn luyện mô hình một lần trên 7 tháng đầu và áp dụng cố định (đóng băng mô hình) cho 4 tháng tiếp theo (120 ngày liên tục).
  - Mô hình đóng băng hoàn toàn thất bại do màng lọc bị lão hóa tự nhiên, bùn hoạt tính biến đổi theo mùa và xuất hiện hiện tượng trôi dạt phân phối dữ liệu (data drift).
- Tính khả thi về chi phí tính toán:
  - Mỗi bản ghi mới được cập nhật vào hệ thống lưu trữ SCADA Historian theo từng giờ.
  - Thời gian huấn luyện lại thuật toán Extra Trees trên toàn bộ tập dữ liệu lịch sử tích lũy chỉ mất khoảng $1\text{ giây}$.
  - Do đó, việc tái huấn luyện định kỳ hoàn toàn khả thi và không gây áp lực tài nguyên phần cứng.

#### 3.1.3.4. Chiến lược tái huấn luyện định kỳ trong triển khai thực tế
- Hiệu suất ngoại suy ngoài thời gian cải thiện tăng dần đều khi rút ngắn chu kỳ tái huấn luyện mô hình.
- Hiệu quả của chiến lược tái huấn luyện hàng ngày (Daily Refit):
  - Áp dụng trên $30\%$ dữ liệu ngoài thời gian được giữ lại (4 tháng cuối), mô hình Extra Trees tái huấn luyện hàng ngày đạt:
    - TMP: $R^2 = 0.871$, sai số tuyệt đối giảm xuống $\text{RMSE} = 0.008\text{ bar}$ ($0.8\text{ kPa}$). Mức sai số này giảm $80\%$ so với mô hình đóng băng cố định.
    - Mức nước bể màng: $R^2 = 0.580$.
    - Lưu lượng nước thấm: $R^2 = 0.574$.
- Hàm ý triển khai công nghiệp:
  - Khả năng tổng quát hóa theo thời gian của mô hình học máy phụ thuộc vào lịch trình cập nhật dữ liệu, không phải giới hạn nội tại của thuật toán.
  - Khuyến nghị vận hành tiêu chuẩn: các nhà máy xử lý nước thải công nghiệp cần tái huấn luyện mô hình tối thiểu mỗi tuần một lần, và ưu tiên thiết lập chu kỳ tái huấn luyện hàng ngày tự động khi hệ thống SCADA Historian cho phép.
