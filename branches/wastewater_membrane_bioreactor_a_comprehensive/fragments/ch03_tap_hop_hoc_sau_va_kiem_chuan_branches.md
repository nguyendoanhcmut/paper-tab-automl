# Cây Tri thức Chương 3 (Phần 2): Các Phương pháp Tập hợp, Học sâu, Giới hạn Dữ liệu và Kiểm chuẩn Thực nghiệm

## Chương 3 (Phần 2): Các Phương pháp Tập hợp, Học sâu, Giới hạn Dữ liệu và Kiểm chuẩn Thực nghiệm

### 3.3 Các phương pháp tập hợp và Học sâu trong mô hình hóa tắc nghẽn MBR

#### 3.3.1 Thuật toán Rừng ngẫu nhiên (Random Forest - RF) và Kỹ thuật đóng bao (Bagging)
- Bản chất và cơ chế đóng bao (Bootstrap Aggregating):
  - Thuật toán RF kết hợp dự đoán từ một tập hợp gồm nhiều cây quyết định độc lập.
  - Thuật toán huấn luyện mỗi cây trên một tập con dữ liệu ngẫu nhiên có hoàn lại từ tập dữ liệu gốc.
  - Tại mỗi nút phân nhánh, thuật toán chọn một tập con đặc trưng ngẫu nhiên thay vì quét toàn bộ biến đầu vào.
  - Cơ chế này giúp giảm phương sai (variance reduction) hiệu quả mà không làm tăng độ chệch (bias).
  - RF tạo ra khả năng chống quá khớp (overfitting resistance) vững chắc trước dữ liệu vận hành thực tế.
- Ưu thế kỹ thuật vượt trội trong dự đoán tắc nghẽn MBR:
  - RF xử lý đồng thời các biến đầu vào hỗn hợp, bao gồm cả biến liên tục và biến phân loại.
  - Mô hình có độ bền bỉ cao trước các điểm dữ liệu dị biệt (outliers) từ cảm biến SCADA.
  - RF cung cấp sẵn độ quan trọng của đặc trưng (built-in feature importance) mà không cần bước giải thích phụ trợ.
  - Độ quan trọng tính toán dựa trên mức giảm độ mờ Gini hoặc hoán vị ngẫu nhiên các đặc trưng đầu vào.
- Nghiên cứu kiểm chuẩn quy mô trạm thực của Kovacs et al. [26]:
  - Nghiên cứu thực hiện trên quy mô trạm xử lý nước thải đô thị thương mại đầy đủ (full-scale municipal WWTP).
  - Tập dữ liệu kiểm chuẩn chứa hơn 80.000 điểm mẫu đo đạc SCADA liên tục.
  - Mô hình RF đạt hệ số xác định vượt trội $R^2 = 0.927 - 0.996$ trên toàn bộ tập dữ liệu.
  - Sai số căn phương trung bình của RF đạt mức rất thấp $\text{RMSE} = 0.264 - 0.904\text{ kPa}$.
  - Nghiên cứu kiểm chứng mô hình qua bốn giai đoạn của chu kỳ lọc màng:
    - Giai đoạn tắc nghẽn ban đầu (initial fouling): hình thành lớp hấp phụ sinh học mỏng trên bề mặt màng.
    - Giai đoạn vận hành ổn định (stable operation): áp suất TMP tăng chậm và đồng đều theo thời gian.
    - Giai đoạn nén chặt bánh cặn muộn (late-stage compaction): áp suất TMP tăng vọt phi tuyến do bít tắc sâu.
    - Giai đoạn phục hồi sau rửa màng (post-cleaning recovery): đánh giá mức độ hoàn nguyên tính thấm của màng lọc.
- Giới hạn kỹ thuật và rào cản triển khai của RF:
  - Kích thước bộ nhớ RAM tăng tuyến tính theo số lượng cây quyết định trong cấu trúc tập hợp.
  - Yếu tố này cản trở việc nạp mô hình vào thiết bị cạnh (edge hardware) hoặc vi điều khiển thời gian thực.
  - Độ quan trọng đặc trưng từ RF mang tính toàn cục (global feature importance).
  - Giá trị toàn cục có thể che giấu các mối quan hệ phi tuyến cục bộ tại từng thời điểm.
  - Kỹ sư cần kết hợp thêm giá trị Shapley (SHAP) để giải thích chi tiết hành vi màng.

#### 3.3.2 Các thuật toán Tăng cường độ dốc nâng cao (XGBoost, LightGBM, CatBoost)
- Nguyên lý hoạt động của phương pháp Gradient Boosting:
  - Thuật toán xây dựng tuần tự các cây quyết định để cực tiểu hóa hàm tổn thất tổng quát.
  - Mỗi cây quyết định mới tập trung học và bù trừ sai số dư (residuals) của toàn bộ các cây trước đó.
  - Phương pháp đạt tốc độ hội tụ nhanh và độ chính xác dự báo cao với các quan hệ phi tuyến phức tạp.
- Khung thuật toán XGBoost (Extreme Gradient Boosting):
  - Tích hợp số hạng chính quy hóa L1 và L2 trực tiếp vào hàm mục tiêu để kiểm soát độ phức tạp của cây:
    $$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2 + \alpha \sum_{j=1}^T |w_j|$$
  - Áp dụng khai triển Taylor bậc hai của hàm tổn thất giúp tính toán trọng số lá tối ưu nhanh và chính xác:
    $$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ l\left(y_i, \hat{y}_i^{(t-1)}\right) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$
    trong đó $g_i$ và $h_i$ lần lượt là đạo hàm bậc nhất và bậc hai của hàm tổn thất.
  - Tích hợp kỹ thuật phân nhánh theo cột (column subsampling) và tìm kiếm điểm chia song song trên vi xử lý đa nhân.
- Khung thuật toán LightGBM (Light Gradient Boosting Machine):
  - Sử dụng chiến lược phân nhánh theo lá (leaf-wise tree growth) với độ sâu giới hạn thay vì phân nhánh theo tầng.
  - Kỹ thuật lấy mẫu một phía theo gradient (GOSS) giữ lại các mẫu gradient lớn và lấy mẫu ngẫu nhiên các mẫu nhỏ.
  - Kỹ thuật bó đặc trưng loại trừ lẫn nhau (EFB) gom các biến thưa độc lập để giảm số chiều không gian đặc trưng.
  - Các kỹ thuật này giúp giảm mạnh thời gian huấn luyện và mức tiêu thụ tài nguyên tính toán trên dữ liệu lớn.
- Khung thuật toán CatBoost (Categorical Boosting) và Thực nghiệm kiểm chuẩn [49]:
  - Kỹ thuật Ordered Boosting ngăn ngừa rò rỉ dữ liệu mục tiêu khi xử lý dữ liệu chuỗi thời gian.
  - Tự động mã hóa biến phân loại và xử lý giá trị khuyết thiếu mà không cần các bước tiền xử lý thủ công phức tạp.
  - Nghiên cứu của tác giả áp dụng CatBoost kết hợp XAI cho trạm MBR công nghiệp chế biến thực phẩm (food-processing WWTP).
  - Dữ liệu vận hành thực tế tại cơ sở này chứa nhiều tạp âm và biến động tải trọng lớn.
  - Mô hình đạt hệ số xác định $R^2 = 0.8374$.
  - Phân tích XAI chỉ ra hai nhân tố chi phối tắc nghẽn màng hàng đầu là tỷ lệ tải trọng F/M và nồng độ chất rắn lơ lửng MLSS.

#### 3.3.3 Mạng nơ-ron hồi quy chuỗi thời gian (LSTM và GRU)
- Bản chất động học thời gian của áp suất qua màng TMP:
  - Quá trình tắc nghẽn màng MBR mang bản chất phụ thuộc chuỗi thời gian tích lũy (inherently time-dependent).
  - Trạng thái áp suất TMP hiện tại lưu giữ lịch sử tích lũy của các biến động dòng thấm (permeate flux excursions).
  - Áp suất TMP cũng phản ánh toàn bộ các chu kỳ sục khí gián đoạn và sức khỏe bùn vi sinh qua nhiều ngày trước đó.
  - Các mô hình học tĩnh truyền thống (như ANN truyền thẳng) xem các mẫu là độc lập, làm mất mát thông tin động học chuỗi.
- Cấu trúc và cơ chế cổng của mạng Bộ nhớ dài ngắn hạn (LSTM - Long Short-Term Memory) [20]:
  - Ô trạng thái bộ nhớ trung tâm ($C_t$) duy trì dòng thông tin xuyên suốt chuỗi thời gian, giải quyết triệt để lỗi mất gradient.
  - Cổng quên (forget gate $f_t$) dùng hàm sigmoid ($\sigma$) để quyết định tỷ lệ thông tin cũ cần loại bỏ:
    $$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$
  - Cổng đầu vào (input gate $i_t$) phối hợp với trạng thái ứng viên ($\tilde{C}_t$) để quyết định thông tin mới nạp vào ô nhớ:
    $$i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$$
    $$\tilde{C}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$$
  - Cập nhật ô trạng thái bộ nhớ tại thời điểm $t$:
    $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
  - Cổng đầu ra (output gate $o_t$) tính toán trạng thái ẩn ($h_t$) phát ra ngoài mạng:
    $$o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$$
    $$h_t = o_t \odot \tanh(C_t)$$
- Cấu trúc Đơn vị hồi quy cổng rút gọn (Gated Recurrent Unit - GRU):
  - Tích hợp cổng quên và cổng đầu vào thành một cổng cập nhật duy nhất ($z_t$):
    $$z_t = \sigma(W_z [h_{t-1}, x_t] + b_z)$$
  - Sử dụng cổng tái lập ($r_t$) để điều chỉnh mức độ phụ thuộc vào trạng thái ẩn trong quá khứ:
    $$r_t = \sigma(W_r [h_{t-1}, x_t] + b_r)$$
  - Tính toán trạng thái ẩn ứng viên ($\tilde{h}_t$) và trạng thái ẩn cập nhật ($h_t$):
    $$\tilde{h}_t = \tanh(W_h [r_t \odot h_{t-1}, x_t] + b_h)$$
    $$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
  - Giảm khoảng 25% số lượng tham số so với LSTM, tăng tốc độ hội tụ trên các tập dữ liệu có quy mô vừa phải.
- Kết quả kiểm chuẩn thực nghiệm của Kovacs et al. [26]:
  - Mô hình ANN và LSTM cho sai số RMSE tổng thể cao hơn Random Forest trên tập dữ liệu SCADA lịch sử tĩnh.
  - Tuy nhiên, LSTM thể hiện năng lực vượt trội tại giai đoạn nén chặt bánh cặn muộn (late-stage fouling compaction).
  - Tại giai đoạn này, chuỗi lịch sử của dòng thấm và áp suất TMP nắm giữ các đặc trưng dự báo cốt lõi cho bước nhảy áp suất.
- Thách thức kỹ thuật và Giới hạn tài nguyên tính toán của LSTM:
  - Đòi hỏi kích thước dữ liệu lớn, thông thường từ hàng nghìn đến hàng chục nghìn bước thời gian để tránh quá khớp.
  - Chi phí tính toán huấn luyện và suy luận cao vượt bậc so với các mô hình RF hoặc SVM.
  - Yếu tố này gây khó khăn khi triển khai trực tiếp trên các bộ điều khiển khả trình công nghiệp (PLC) hiện hữu tại trạm.

#### 3.3.4 Kiến trúc lai, Cơ chế Tự chú ý và Mạng chuyên dụng MBR-Net
- Kiến trúc tích hợp không - thời gian (CNN-LSTM Hybrid):
  - Các lớp tích chập không gian (1D hoặc 2D CNN) đóng vai trò bộ lọc trích xuất các đặc trưng tương quan không gian.
  - Bộ lọc không gian gom cụm tín hiệu từ nhiều cảm biến đo đạc đồng thời (DO, nhiệt độ, MLSS, lưu lượng).
  - Các lớp LSTM tiếp nhận véc-tơ đặc trưng không gian để học động học tiến triển theo thời gian (temporal dynamics).
  - Kiến trúc lai giúp giảm suy hao thông tin và nắm bắt tốt tương tác đa biến trong bể phản ứng màng.
- Mô hình Transformer và Cơ chế Tự chú ý (Self-Attention) [46]:
  - Loại bỏ hoàn toàn cấu trúc hồi quy tuần tự, tính toán trực tiếp mức độ tương quan giữa tất cả các bước thời gian:
    $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
  - Cơ chế tự chú ý đa đầu (Multi-Head Attention) nắm bắt đồng thời các mẫu động học ở các thang đo thời gian khác nhau.
  - Mô hình theo dõi cả chu kỳ sục khí ngắn hạn và chu kỳ lão hóa màng dài hạn.
  - Transformer thiết lập chuẩn mực độ chính xác cao nhất trong các bài toán dự báo chuỗi thời gian môi trường.
  - Mô hình mở ra định hướng nghiên cứu tiên phong cho dự đoán tắc nghẽn MBR nhưng chưa có công trình phản biện nào đánh giá hệ thống.
  - Điểm nghẽn chính nằm ở yêu cầu dữ liệu khổng lồ và chi phí tính toán tỷ lệ bậc hai với chiều dài chuỗi $O(T^2)$.
- Mạng học sâu chuyên dụng MBR-Net [50]:
  - Kiến trúc học sâu tùy biến tích hợp mạng lưới vạn vật kết nối công nghiệp (Industrial IoT).
  - Thực hiện nhiệm vụ dự báo trước một ngày (one-day-ahead forecasting) áp suất qua màng TMP trong thời gian thực.
  - Đạt hệ số xác định $R^2 > 0.87$ trên hai tập dữ liệu kiểm thử độc lập từ cùng một trạm xử lý đô thị quy mô đầy đủ.
- Các kỹ thuật nén mô hình phục vụ triển khai phần cứng biên (Edge AI):
  - Kỹ thuật cắt tỉa mô hình (Model Pruning): loại bỏ các liên kết nơ-ron dư thừa, giảm kích thước mạng mà vẫn giữ độ chính xác.
  - Lượng tử hóa mô hình (Quantization): chuyển đổi định dạng số thực 32-bit (FP32) sang số nguyên 8-bit (INT8), tiết kiệm 75% bộ nhớ.
  - Chưng cất tri thức (Knowledge Distillation): chuyển giao tri thức từ mạng giáo viên phức tạp sang mạng học sinh gọn nhẹ để nhúng vào vi điều khiển.

#### 3.3.5 Ứng dụng mô hình AI trong hệ thống MBR thẩm thấu (OMBR)
- Đặc thù công nghệ của hệ thống OMBR (Osmotic Membrane Bioreactor) [22]:
  - Hệ thống OMBR tích hợp quá trình xử lý sinh học bùn hoạt tính với màng thẩm thấu thuận (Forward Osmosis - FO).
  - Quá trình phân tách vận hành nhờ chênh lệch áp suất thẩm thấu ($\Delta \pi$) giữa nước thải và dung dịch rút nồng độ cao.
  - Động học màng chịu sự chi phối phức tạp từ hiện tượng phân cực nồng độ bên trong (ICP) và bên ngoài (ECP).
  - Quá trình lọc còn chịu ảnh hưởng bởi sự pha loãng dung dịch rút và hiện tượng dòng muối ngược (reverse salt flux - RSF).
- Mô hình hóa bằng AI của Viet và Jang [22]:
  - Nhóm tác giả áp dụng các kiến trúc AI để dự đoán hiệu năng hệ thống OMBR xử lý nước thải đô thị.
  - Thông số đầu vào gồm các chỉ tiêu hóa lý nước cấp: pH, độ dẫn điện, nồng độ amoni ($\text{NH}_4\text{-N}$), tổng nitơ (TN), và tổng cacbon hữu cơ (TOC).
  - Biến mục tiêu dự báo gồm thông lượng nước qua màng (water flux) và trở lực tắc nghẽn màng (fouling resistance).
  - Mô hình đạt hệ số xác định cao $R^2 = 0.92 - 0.98$.
  - Phương pháp hướng dữ liệu giải quyết trọn vẹn các bậc tự do phức tạp mà không cần giải hệ phương trình truyền khối FO phi tuyến cao.

### 3.4 Giới hạn tập dữ liệu, Nguy cơ quá khớp và Khả năng tổng quát hóa liên cơ sở

#### 3.4.1 Cạm bẫy dữ liệu đơn trạm (Single-Site Trap) và Quy mô mẫu hạn chế
- Hiện tượng phụ thuộc vào dữ liệu đơn cơ sở trong y văn:
  - Đa số các nghiên cứu ML trong lĩnh vực MBR (hơn 85%) chỉ huấn luyện và kiểm chuẩn mô hình trên một cơ sở duy nhất.
  - Các tập dữ liệu phần lớn có quy mô phòng thí nghiệm hoặc mô hình pilot với kích thước từ vài trăm đến vài nghìn mẫu đo.
  - Nghiên cứu của Kovacs et al. [26] là ngoại lệ duy nhất ghi nhận tập dữ liệu quy mô trạm thực đô thị với hơn 80.000 mẫu SCADA.
- Nguy cơ quá khớp ẩn danh sau điểm số $R^2$ cao:
  - Các giá trị hệ số xác định rất cao trong phòng thí nghiệm (như $R^2 = 0.990$ của LSSVM [42] hay $R^2 = 0.92 - 0.98$ của OMBR [22]) cần được nhìn nhận thận trọng.
  - Khi huấn luyện và kiểm thử trên một chiến dịch vận hành đơn lẻ, điểm số $R^2$ cao phản ánh việc mô hình học thuộc cấu trúc nhiễu riêng biệt.
  - Mô hình cũng học thuộc tính tự tương quan thời gian của chiến dịch đó thay vì nắm bắt quy luật động học tổng quát.
  - Mô hình sẽ suy giảm độ chính xác nghiêm trọng khi đối mặt với điều kiện vận hành biến động ngoài thực địa.

#### 3.4.2 Lỗi rò rỉ thời gian (Data Leakage) và Chiến lược phân chia dữ liệu chuẩn xác
- Cơ chế phát sinh lỗi rò rỉ dữ liệu thời gian (Temporal Data Leakage):
  - Hầu hết các công trình nghiên cứu áp dụng kỹ thuật phân chia ngẫu nhiên tập huấn luyện và kiểm thử (random train-test split).
  - Phân chia ngẫu nhiên vi phạm nghiêm trọng tính đơn điệu thời gian của dữ liệu chuỗi quan trắc.
  - Thông tin ở các bước thời gian tương lai rò rỉ trực tiếp vào tập huấn luyện của quá khứ.
  - Lỗi rò rỉ này dẫn đến các chỉ số đánh giá ($R^2$, RMSE) lạc quan giả tạo, che giấu sự kém ổn định của mô hình.
- Khung tiêu chuẩn kiểm chuẩn chuỗi thời gian bắt buộc:
  - Bắt buộc áp dụng phương pháp kiểm chuẩn chéo phân khối theo thời gian (k-fold cross-validation with temporal blocking).
  - Người nghiên cứu cũng có thể dùng phương pháp kiểm chuẩn cửa sổ thời gian mở rộng (expanding window temporal split).
  - Các khối kiểm thử phải luôn nằm hoàn toàn phía sau các khối huấn luyện theo trục thời gian thực.
  - Cần báo cáo đường cong học tập (learning curves) biểu diễn sai số mô hình theo kích thước tập mẫu huấn luyện.
  - Bắt buộc đánh giá khả năng tổng quát hóa trên các giai đoạn vận hành độc lập về thời gian trước khi triển khai thực tế.

#### 3.4.3 Động học bùn vi sinh, Trôi dạt khái niệm (Concept Drift) và Thách thức vận hành vòng kín
- Cơ chế trôi dạt khái niệm trong hệ thống MBR thực địa:
  - Mối quan hệ thống kê giữa các biến vận hành đầu vào và áp suất TMP biến đổi liên tục theo thời gian thực.
  - Biến động nhiệt độ theo mùa ảnh hưởng sâu sắc đến độ nhớt của bùn lỏng và hoạt tính sinh học của vi sinh vật.
  - Các đợt xả thải công nghiệp đột ngột làm thay đổi tải trọng hữu cơ và nồng độ chất polyme ngoại bào EPS/SMP trong bể sinh học.
  - Quá trình lão hóa màng không thể phục hồi làm suy giảm vĩnh viễn cấu trúc lỗ rỗng và làm tăng trở lực nội tại ($R_m$).
- Khoảng cách giữa kiểm chứng SCADA lịch sử và Vận hành vòng kín (Closed-Loop Operational Deployment):
  - Việc kiểm chứng thành công trên dữ liệu SCADA lịch sử chỉ xác nhận mô hình tái tạo được các quy luật quá khứ trên một cơ sở tĩnh.
  - Vận hành vòng kín thời gian thực đòi hỏi mô hình phải hoạt động ổn định trước nhiều yếu tố bất định thực địa.
  - Các yếu tố này bao gồm hiện tượng trôi dạt cảm biến đo (sensor drift), nhiễu tín hiệu đo đạc, và độ trễ truyền dữ liệu mạng.
  - Hệ thống cũng phải ứng phó với sự cố hỏng hóc thiết bị cơ khí đột xuất trong quá trình vận hành liên tục.
  - Mô hình học máy bắt buộc phải trải qua quá trình kiểm thử trực tiếp trong điều kiện vòng kín trước khi giao quyền điều khiển tự động.

#### 3.4.4 Khả năng tổng quát hóa liên cơ sở (Cross-Site Generalization), Học chuyển giao và Thích ứng miền
- Thách thức suy giảm hiệu năng liên cơ sở (Cross-Site Performance Degradation):
  - Mô hình học máy huấn luyện tại một trạm MBR nguồn thường suy giảm độ chính xác nghiêm trọng khi áp dụng cho trạm MBR đích thứ hai.
  - Sự suy giảm này bắt nguồn từ hiện tượng lệch phân phối dữ liệu (dataset shift / domain shift).
  - Nguyên nhân xuất phát từ sự khác biệt về hình học mô-đun màng, chế độ thủy lực sục khí, và thành phần hóa lý nước thải.
  - Sự khác biệt về hệ sinh thái vi sinh vật bùn hoạt tính giữa các vùng địa lý cũng gây ra độ lệch lớn.
- Giải pháp Học chuyển giao (Transfer Learning):
  - Huấn luyện trước mô hình nền tảng trên tập dữ liệu SCADA phong phú từ một trạm nguồn quy mô lớn.
  - Đóng băng các tầng trích xuất đặc trưng cơ sở và tinh chỉnh các tầng đầu ra bằng một lượng dữ liệu nhỏ tại trạm đích mới.
- Giải pháp Thích ứng miền (Domain Adaptation):
  - Áp dụng các thuật toán tối ưu hóa nhằm cực tiểu hóa khoảng cách phân phối xác suất giữa không gian đặc trưng nguồn và đích.
  - Cả hai phương pháp đã chứng minh hiệu quả trong kỹ thuật môi trường tổng quát [17, 47] và là hướng nghiên cứu trọng tâm cho MBR.

#### 3.4.5 Bảng tổng hợp đối sánh kiểm chuẩn và Đánh giá rủi ro sai lệch (Bảng 1 và Bảng 2)
- Khung tiêu chí đánh giá mức độ rủi ro sai lệch (Bias Risk Evaluation Framework):
  - Đánh giá dựa trên hướng dẫn chuẩn mực kiểm chuẩn ML trong kỹ thuật môi trường [28, 48] và phản biện chuyên gia.
  - Mức rủi ro CAO (HIGH BIAS RISK): Nghiên cứu không có kiểm chuẩn ngoại kiểm độc lập và kích thước tập dữ liệu nhỏ hơn 500 mẫu.
  - Mức rủi ro TRUNG BÌNH (MODERATE BIAS RISK): Tập dữ liệu có kích thước lớn nhưng chỉ kiểm chuẩn trong phạm vi một cơ sở duy nhất.
  - Mức rủi ro THẤP (LOW BIAS RISK): Mô hình được kiểm chứng trên tối thiểu hai tập dữ liệu kiểm thử độc lập từ các trạm vận hành thực tế.
- Bảng 1: Phân tích so sánh toàn diện các nghiên cứu ML trong dự đoán tắc nghẽn MBR:

| Thuật toán ML | Biến mục tiêu | Quy mô trạm | $R^2$ tốt nhất | Kích thước tập dữ liệu ước tính | Kiểm chuẩn ngoại kiểm | Sai số RMSE / MSE | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ANN (MLP + RBF) | TMP / Độ thấm (TMP / permeability) | Quy mô thử nghiệm (Pilot) | Đạt yêu cầu (không công bố số liệu) | Không báo cáo (chiến dịch 60 ngày) | Không có (phân chia train-test) | Không báo cáo | [23] |
| ANN (Lan truyền ngược) | TMP, AO-MBR | Quy mô thử nghiệm (Pilot) | 0.850 | Không báo cáo (quy mô pilot) | Không có (phân chia train-test) | Không báo cáo | [25] |
| LSSVM (tối ưu nhất) | Trở lực tắc nghẽn (Fouling resistance) | Phòng thí nghiệm (Lab) | 0.990 | Không báo cáo (quy mô lab) | Không có (phân chia train-test) | $\text{MSE} = 0.0002$ | [42] |
| ANN-MLP | Trở lực tắc nghẽn (Fouling resistance) | Phòng thí nghiệm (Lab) | Thấp hơn LSSVM | Không báo cáo (quy mô lab) | Không có (phân chia train-test) | Lớn hơn LSSVM | [42] |
| Mô hình AI (OMBR) | Thông lượng nước + Trở lực tắc nghẽn | Phòng thí nghiệm (Lab) | 0.92–0.98 | Không báo cáo (lab OMBR) | Không có (phân chia train-test) | Đã báo cáo | [22] |
| Random Forest (tối ưu nhất) | TMP, trạm đô thị thương mại | Quy mô trạm thực (Full-scale) | 0.927–0.996 | >80.000 mẫu quan trắc | Không có (trạm đơn lẻ) | $\text{RMSE} = 0.264 - 0.904\text{ kPa}$ | [26] |
| LSTM | TMP, trạm đô thị thương mại | Quy mô trạm thực (Full-scale) | Thấp hơn RF (không báo cáo số cụ thể) | >80.000 mẫu quan trắc | Không có (trạm đơn lẻ) | Cao hơn RF | [26] |
| ANN | TMP, trạm đô thị thương mại | Quy mô trạm thực (Full-scale) | Thấp hơn RF (không báo cáo số cụ thể) | >80.000 mẫu quan trắc | Không có (trạm đơn lẻ) | Cao hơn RF | [26] |

- Bảng 2: So sánh phản biện các thuật toán ML chính yếu và Đánh giá rủi ro sai lệch:

| Thuật toán | Phân nhóm thuật toán | Điểm mạnh chính | Hạn chế cốt lõi | $R^2$ tốt nhất | Mức độ rủi ro sai lệch (Bias Risk) | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ANN (MLP + RBF) | Mạng ANN nông (Shallow ANN) | Tốc độ hội tụ nhanh. Xử lý tốt mối quan hệ phi tuyến giữa đầu vào và đầu ra. | Không báo cáo giá trị định lượng $R^2$. Khả năng tổng quát hóa chưa được kiểm chứng. | Không báo cáo | CAO (HIGH)¹ | [23] |
| ANN (Lan truyền ngược) | Mạng ANN nông (Shallow ANN) | Kiến trúc kinh điển đã thiết lập. Tính thực tế cao cho quy mô pilot. | Chỉ đạt $R^2 = 0.850$. Độ chính xác trung bình. Thiếu định lượng độ bất định. | 0.850 | CAO (HIGH)¹ | [24] |
| LSSVM | Dựa trên hạt nhân (Kernel-based) | Đạt $R^2$ cao nhất ở quy mô phòng thí nghiệm (0.99). Bền vững trên dữ liệu nhỏ. Tích hợp phân tích độ nhạy. | Không mở rộng được cho tập dữ liệu lớn. Thiếu năng lực mô hình hóa chuỗi thời gian. | 0.990 | CAO (HIGH)² | [42] |
| Mô hình AI (OMBR) | Đa dạng cấu trúc (Various) | Nắm bắt chính xác động lực áp suất thẩm thấu dẫn động. $R^2 = 0.92 - 0.98$. | Dữ liệu phòng thí nghiệm nhỏ. Chỉ kiểm chứng một cơ sở duy nhất. Không có kiểm chuẩn ngoại kiểm. | 0.92–0.98 | CAO (HIGH)¹ | [22] |
| Random Forest | Học tập hợp (Ensemble) | Độ chính xác cao nhất ở quy mô đầy đủ. Kháng ngoại lai tốt. Tích hợp độ quan trọng đặc trưng. Xử lý dữ liệu hỗn hợp. | Tốn nhiều bộ nhớ RAM. Độ quan trọng biến chỉ mang tính toàn cục. Chỉ kiểm chuẩn trên một trạm đơn lẻ. | 0.927–0.996 | TRUNG BÌNH (MODERATE)³ | [26] |
| LSTM | Học sâu (Mạng RNN) | Nắm bắt quan hệ phụ thuộc động học thời gian dài hạn. Tối ưu cho chuỗi thời gian TMP. | Đòi hỏi tập dữ liệu lớn. Chi phí tính toán cao. Độ chính xác kém hơn RF trong cùng nghiên cứu. | Thấp hơn RF | TRUNG BÌNH (MODERATE)³ | [26] |
| CatBoost + XAI | Tăng cường độ dốc (Gradient boosting) | Hiệu năng dự báo cao ở quy mô thực tế. XAI nhận diện rõ các nhân tố chi phối chính (F/M, MLSS). | Chỉ đạt $R^2$ trung bình (0.8374) trên dữ liệu công nghiệp nhiều tạp âm. Chỉ kiểm chứng một trạm thực phẩm duy nhất. | 0.8374 | TRUNG BÌNH (MODERATE)³ | [49] |
| MBR-Net (tùy biến) | Học sâu chuyên dụng (Deep learning) | Tích hợp IoT thời gian thực. $R^2 > 0.87$ trên hai tập kiểm thử độc lập. Hỗ trợ dự báo trước một ngày. | Phụ thuộc tính sẵn sàng của dữ liệu. Chỉ kiểm chứng trên một loại hình cơ sở. | >0.87 | THẤP (LOW)⁴ | [50] |

- Các ghi chú kỹ thuật giải trình mức độ rủi ro sai lệch:
  - Ghi chú 1: Mức độ rủi ro sai lệch phân loại theo tiêu chí Người phản biện 2. Mức Cao xảy ra khi nghiên cứu không có ngoại kiểm và dữ liệu dưới 500 mẫu. Mức Trung bình xảy ra khi dữ liệu lớn nhưng chỉ kiểm chuẩn đơn trạm. Mức Thấp đạt được khi kiểm chứng trên từ hai tập kiểm thử độc lập trở lên.
  - Ghi chú 2: Mô hình LSSVM chỉ huấn luyện trên dữ liệu phòng thí nghiệm. Số lượng mẫu không công bố nhưng phù hợp ngưỡng dưới 500 mẫu của các thí nghiệm ngắn ngày.
  - Ghi chú 3: Kiểm chuẩn thực hiện tại một trạm đô thị hoặc trạm công nghiệp duy nhất. Nghiên cứu chưa thực hiện kiểm chuẩn chéo liên cơ sở.
  - Ghi chú 4: Mô hình MBR-Net kiểm chứng trên hai tập kiểm thử độc lập từ cùng một trạm quy mô đầy đủ. Khả năng tổng quát hóa liên cơ sở giữa các trạm khác nhau cần tiếp tục nghiên cứu thêm.
