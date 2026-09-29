## Chương 3: Kết quả Thực nghiệm và Phân tích Hiệu năng

### 3.1 Hiệu năng vượt trội của AutoML so với Deep Learning trong mô hình hóa AnMBR

#### So sánh định lượng hiệu năng dự đoán (AutoML vs FCN, CNN, DenseNet - Bảng 1)
- AutoML dùng tập dữ liệu 185 mẫu từ nghiên cứu Li et al. (2022).
- Tập đặc trưng gồm 6 biến: $T\text{-R}$, $T\text{-in}$, $T\text{-env}$, $\text{pH-in}$, $\text{COD-in}$, $\text{flux}$.
- Biến mục tiêu là hiệu suất loại bỏ COD ($\text{COD-re}$, đơn vị $\%$).
- Tỉ lệ phân chia dữ liệu gồm 166 mẫu huấn luyện và 19 mẫu kiểm thử (9:1).
- Mô hình FCN ghi nhận $\text{RMSE} = 6.29\%$ và $\text{MAE} = 5.71\%$.
- Mô hình FCN đạt $\text{MAPE} = 6.49\%$ và $R^2 = -1.19$.
- Mô hình CNN ghi nhận $\text{RMSE} = 5.98\%$ và $\text{MAE} = 5.34\%$.
- Mô hình CNN đạt $\text{MAPE} = 6.02\%$ và $R^2 = -0.97$.
- Mô hình DenseNet ghi nhận $\text{RMSE} = 4.69\%$ và $\text{MAE} = 4.34\%$.
- Mô hình DenseNet đạt $\text{MAPE} = 4.93\%$ và $R^2 = -0.21$.
- Trên tập kiểm thử của Li et al. (2022), AutoML đạt $\text{RMSE} = 3.09\%$.
- AutoML đạt $\text{MAE} = 2.76\%$, $\text{MAPE} = 3.11\%$ và $R^2 = 0.47$.
- Qua kiểm định chéo 10 lần (10-fold CV), AutoML đạt $\text{RMSE} = 2.47\%$.
- Khoảng tin cậy $95\%$ của RMSE là $[2.14\%, 2.81\%]$ (biên độ $\pm 0.33\%$).
- Chỉ số $\text{MAE}$ trung bình đạt $1.90\%$ với khoảng tin cậy $[1.68\%, 2.11\%]$.
- Chỉ số $\text{MAPE}$ trung bình đạt $2.19\%$ với khoảng tin cậy $[1.93\%, 2.46\%]$.
- Hệ số $R^2$ trung bình đạt $0.44$ với khoảng tin cậy $[0.22, 0.65]$.
- Biên độ hẹp $\pm 0.33\%$ chứng minh AutoML có độ bền vững cao.

#### Phân tích nguyên nhân thất bại của Deep Learning và ưu thế của mô hình cây trên dữ liệu bảng nhỏ
- Công thức tính hệ số xác định:
  $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
- Giá trị $R^2 < 0$ xuất hiện khi tổng bình phương sai số vượt quá phương sai dữ liệu.
- Các mô hình Deep Learning dự đoán kém hơn giá trị trung bình $\bar{y}$.
- Hiện tượng quá khớp nảy sinh do số lượng trọng số lớn trên mẫu nhỏ ($n = 185$).
- Dữ liệu thiếu các biến đo lường động học làm giảm độ khái quát của Deep Learning.
- Cấu trúc mạng nơ-ron không phù hợp với dữ liệu bảng có chiều không gian nhỏ.
- Thư viện FLAML chọn các mô hình cây: Random Forest, Extra Trees, XGBoost, LightGBM, CatBoost.
- Mô hình cây phân chia không gian đặc trưng bằng các mặt cắt trực giao.
- Thuật toán cây không cần chuẩn hóa dữ liệu hay biến đổi phi tuyến phức tạp.
- Cấu trúc cây ngăn chặn hiện tượng bão hòa gradient trên dữ liệu bảng nhỏ.
- Phương pháp CFO bắt đầu từ mô hình nhỏ và tăng dần độ phức tạp.
- Thuật toán BlendSearch kết hợp tìm kiếm toàn cục và tối ưu cục bộ trong 300 giây.
- Giá trị $\text{RMSE} = 3.09\%$ của AutoML thấp hơn độ lệch chuẩn AnMBR ($3.5\% - 5.0\%$).
- Độ chính xác của AutoML đáp ứng tốt yêu cầu mô phỏng động học AnMBR.

#### Đánh giá tính nhất quán và độ ổn định dự đoán qua phân tích Bland-Altman (Hình 3)
- Phương pháp Bland-Altman định lượng độ tương đồng giữa giá trị thực ($y$) và dự đoán ($\hat{y}$).
- Sai khác giữa hai giá trị tính theo công thức:
  $$d_i = y_i - \hat{y}_i$$
- Sai khác trung bình biểu diễn độ lệch:
  $$\bar{d} = \frac{1}{n} \sum_{i=1}^n d_i$$
- Giới hạn thỏa thuận $95\%$ (LoA):
  $$\text{LoA} = [\bar{d} - 1.96 \times s_d, \quad \bar{d} + 1.96 \times s_d]$$
  trong đó $s_d$ là độ lệch chuẩn của các sai khác $d_i$.
- Giới hạn thỏa thuận rộng phản ánh tính nhất quán kém giữa mô hình và thực tế.
- Các mô hình Deep Learning thể hiện dải thỏa thuận rất rộng trên Hình 3.
- Sai số Deep Learning giảm dần khi giá trị trung bình tăng lên (hiệu ứng phễu).
- Deep Learning mất ổn định ở vùng hiệu suất COD thấp.
- AutoML có dải thỏa thuận hẹp hơn và sai số phân bố đồng đều (Hình 3a).
- Sai số của AutoML phân tán ngẫu nhiên qua toàn bộ dải giá trị trung bình.
- Đại đa số điểm dữ liệu của AutoML nằm trong khoảng tin cậy $95\%$.
- Tất cả mô hình đều ghi nhận sai khác trung bình dương ($\bar{d} > 0$).
- Độ lệch dương cho thấy mô hình có xu hướng dự đoán thấp hơn thực tế.
- Xu hướng này do mất cân bằng phân phối giữa tập huấn luyện và kiểm thử.
- Mô hình làm mịn nhiễu đo lường và dao động sinh học tức thời.

### 3.2 Tác động nâng cao hiệu năng khi bổ sung thời gian vận hành (OD)

#### Giả thuyết khoa học và vai trò biến đại diện (proxy) của ngày vận hành OD
- Hiệu suất AnMBR phụ thuộc vào cấu trúc và hoạt tính của quần thể vi sinh vật.
- Đo đạc vi sinh vật tốn chi phí cao và mất nhiều thời gian.
- Tần suất lấy mẫu vi sinh thấp cản trở mô hình hóa học máy.
- Nhóm tác giả giả thuyết ngày vận hành (OD) tương quan với động học sinh học.
- Biến OD (50 đến 414 ngày) đóng vai trò biến đại diện (surrogate variable).
- OD phản ánh quá trình thích nghi của bùn kỵ khí và màng sinh học.
- OD phản ánh biến đổi đặc tính bề mặt màng và tích tụ chất bẩn.
- Trục thời gian OD giúp mô hình học các hành vi phi dừng của hệ phản ứng.

#### Cải thiện định lượng khi tích hợp OD vào tập đặc trưng nền tảng ($R^2$, RMSE)
- Tập nền tảng gồm 6 biến: $T\text{-R}$, $T\text{-in}$, $T\text{-env}$, $\text{pH-in}$, $\text{COD-in}$, $\text{flux}$.
- Khi tích hợp OD, hệ số $R^2$ trung bình tăng từ $0.44$ lên $0.55$.
- Mức tăng $R^2$ tương ứng mức cải thiện $+25.0\%$ theo Hình 4 và Hình S1.
- Sai số $\text{RMSE}$ trung bình giảm từ $2.47\%$ xuống $2.20\%$ (giảm $-10.9\%$).
- Khoảng tin cậy $95\%$ của các chỉ số đều thu hẹp rõ rệt.
- Kết quả khẳng định mô hình tiếp thu hiệu quả thông tin từ biến OD.
- Mô hình nắm bắt chính xác quy luật biến thiên COD theo từng pha vận hành.

#### Kiểm định nguy cơ rò rỉ dữ liệu (Data Leakage) và giới hạn ngoại suy của mô hình cây
- Phân tích tương quan Spearman đánh giá liên hệ giữa OD và nhãn $\text{COD-re}$.
- Kết quả ghi nhận mối tương quan rất yếu giữa OD và $\text{COD-re}$.
- Mối tương quan yếu loại trừ nguy cơ rò rỉ dữ liệu từ thời gian sang nhãn.
- Mô hình học được động học phi tuyến, không ghi nhớ chỉ mục thời gian đơn thuần.
- Mô hình cây phân chia không gian bằng các mặt cắt trực giao từng đoạn.
- Giá trị dự đoán tại mỗi nút lá là một hằng số cố định.
- Mô hình cây không thể ngoại suy ngoài phạm vi huấn luyện ($\text{OD} > 414\text{ ngày}$).
- Dự đoán cho các ngày ngoài ngưỡng huấn luyện sẽ bão hòa tại hằng số biên.
- Người vận hành cần hiệu chuẩn lại mô hình khi hệ thống bước sang chu kỳ mới.

#### Tác động hạn chế của các thông số vật lý - sinh học khác (ORP, HRT, MLSS, MLVSS)
- Nghiên cứu khảo sát thêm 4 thông số: $\text{ORP}$, $\text{HRT}$, $\text{MLSS}$, $\text{MLVSS}$.
- Khi dùng cả 5 biến (OD, ORP, HRT, MLSS, MLVSS), hiệu năng tương đương chỉ có OD.
- Mô hình chứa các thông số trên mà thiếu OD không đem lại cải thiện đáng kể.
- Phân tích Bland-Altman cho thấy biến OD thu hẹp dải sai số quanh mốc 0 (Hình 5).
- Bổ sung ORP, HRT, MLSS và MLVSS không làm giảm thêm khoảng thỏa thuận.
- Tần suất đo tuần của MLSS và MLVSS làm mờ tín hiệu thực nghiệm qua nội suy.
- Tỉ số tín hiệu trên nhiễu thấp làm lu mờ mối liên hệ sinh học.
- Hiện tượng cộng tuyến đa biến khiến thông tin bị trùng lặp với tập cơ sở.
- Kết quả khẳng định tầm quan trọng của việc chọn lọc đặc trưng chặt chẽ.

### 3.3 Tác động nghịch lý của thể tích dữ liệu đến hiệu năng dự đoán

#### Thiết kế 3 kịch bản xác thực quy mô dữ liệu (M1T1, M2T1, M2T2)
- Quan niệm phổ biến giả định tăng kích thước dữ liệu luôn tăng hiệu năng mô hình.
- Dữ liệu thực nghiệm môi trường thường nhỏ do giới hạn chi phí và không gian.
- Dữ liệu thực nghiệm dễ bị nhiễu bởi sai số đo và thao tác con người.
- Việc so sánh tập dữ liệu nhỏ chất lượng cao với tập lớn chứa nhiễu là vấn đề lớn.
- Tập dữ liệu gốc $M_1$ gồm 185 mẫu trong khoảng ngày 50 đến 414.
- Tập dữ liệu mở rộng $M_2$ gồm 320 mẫu trong khoảng ngày 7 đến 546.
- Kịch bản $M_1T_1$: 10-fold CV trên $M_1$, kiểm thử trên các tập con $T_1$ từ $M_1$.
- Kịch bản $M_2T_1$: Thêm 135 mẫu vào tập huấn luyện, kiểm thử trên cùng tập $T_1$.
- Kịch bản $M_2T_2$: 10-fold CV tiêu chuẩn trên toàn bộ 320 mẫu của tập $M_2$.
- Thiết kế $M_2T_1$ giúp đánh giá việc mở rộng dữ liệu trên cùng chuẩn kiểm thử.

#### Hiện tượng suy giảm hiệu năng khi mở rộng dữ liệu huấn luyện (Hình 6)
- So sánh $M_1T_1$ và $M_2T_1$ cho thấy thêm dữ liệu làm giảm hệ số $R^2$.
- Các sai số $\text{RMSE}$, $\text{MAE}$, $\text{MAPE}$ đều tăng khi thêm 135 mẫu huấn luyện.
- So sánh $M_1T_1$ và $M_2T_2$ cho thấy sai số tăng vọt trên toàn dải $M_2$.
- Kịch bản $M_2T_2$ cho hiệu năng dự đoán kém nhất trong cả ba phương án (Hình 6).
- Kết quả xác lập nghịch lý: Thêm dữ liệu thực nghiệm không giúp cải thiện mô hình.

#### Cơ chế dịch chuyển phân phối dữ liệu (Distribution Shift) và suy giảm tương quan Spearman
- Tương quan Spearman giữa $M_1$ và $M_2$ được minh họa tại Hình S3 và S4.
- Đặc trưng trong tập $M_2$ có tương quan với COD thấp hơn so với trong $M_1$.
- Mức độ liên quan của dữ liệu quyết định trực tiếp độ chính xác của mô hình.
- Dịch chuyển phân phối phát sinh do thay đổi dòng vào hoặc trạng thái sinh học.
- 135 mẫu bổ sung thuộc ngày 7-49 và ngày 415-546 mang nhiều biến động ngoại cảnh.
- Giai đoạn khởi động có hệ vi sinh chưa ổn định, gây sai lệch quy luật chuyển hóa.
- Tác hại của dịch chuyển phân phối vượt xa lợi ích từ việc tăng số lượng mẫu.
- Hiệu năng giảm sút phản ánh việc mô hình đã thu nhận dữ liệu không liên quan.

#### Bài học cốt lõi: Ưu tiên chất lượng và tính đặc thù ngữ cảnh hơn số lượng dữ liệu
- Chuyên gia cần đánh giá kỹ nguồn gốc và chất lượng dữ liệu trước khi mô hình hóa.
- Tăng thể tích dữ liệu mà bỏ qua tính không đồng nhất sẽ làm giảm độ chính xác.
- Kỹ thuật dữ liệu cần ưu tiên chất lượng và tính đặc thù ngữ cảnh của mẫu.
- Nghiên cứu tương lai cần phát triển kỹ thuật thích ứng miền để xử lý sai lệch phân phối.
