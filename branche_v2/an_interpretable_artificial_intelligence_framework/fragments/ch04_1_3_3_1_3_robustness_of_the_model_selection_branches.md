#### 3.1.3. Robustness of the model selection to the validation design

- Đánh giá tính vững chắc của quy trình lựa chọn mô hình qua bốn thiết kế kiểm định độc lập (four independent validation designs):
  - Quyết định lựa chọn mô hình cho hồ sơ vận hành nhà máy quy mô đầy đủ (full-scale plant record) không thể chỉ dựa trên một phương án phân chia đơn lẻ, do đó Extra Trees được kiểm chứng qua $4$ thiết kế độc lập:
    - Phân chia ngẫu nhiên truyền thống $70/30$ (conventional random $70/30$ partition).
    - Thiết kế phân khối (blocked design): các khối thời gian liên tục được phân bổ thành từng đơn vị nguyên vẹn để bảo toàn phạm vi bao phủ của miền vận hành (operating envelope) trong khi vẫn tách biệt các giờ liền kề.
    - Phân chia tuần tự theo thời gian nghiêm ngặt (strictly chronological partition).
    - Phân tích kiểm định trên nhánh song song B độc lập (independent parallel B stream).
  - Extra Trees thể hiện tính ổn định cao và giữ vị trí dẫn đầu trong hầu hết các kịch bản thử nghiệm:
    - Extra Trees xếp hạng nhất ở $8$ trong số $9$ tổ hợp mô hình – thiết kế – mục tiêu (model–design–target combinations).
    - Xếp hạng nhất cho mọi biến mục tiêu dưới cả thiết kế phân chia ngẫu nhiên và thiết kế phân khối $24\text{ h}$ (24-h blocked designs) (Table S10).
  - Độ chính xác dưới thiết kế phân khối $24\text{ h}$ duy trì ở mức cao đối với hệ thống công nghiệp quy mô đầy đủ:
    - Đối với biến TMP: đạt $R^2 = 0.830$, tương ứng với $\text{RMSE} = 0.036\text{ bar}$ trên dải vận hành $0.43\text{ bar}$.
    - Sai số tuyệt đối trung bình ($\text{MAE}$) bằng $16.3\%$ khoảng tứ phân vị (interquartile range - IQR) của chuỗi đo thực tế.
- Đặc tính tự tương quan (autocorrelation) và tính ổn định của các kết luận công nghệ:
  - Do hồ sơ dữ liệu là chuỗi ghi nhận liên tục theo từng giờ nên có cấu trúc tự tương quan tự nhiên theo bản chất thu thập (autocorrelated by construction).
  - Các giá trị hiệu năng theo thiết kế phân khối (blocked) và ngẫu nhiên (random) được báo cáo song song xuyên suốt.
  - Cấu trúc phụ thuộc (dependence structure), kết quả chi tiết theo từng mô hình và hiện tượng phân kỳ giữa $R^2$ cùng sai số tuyệt đối khi kéo dài kích thước khối phân vùng được trình bày chi tiết tại Supplementary Section S6 và Fig. S17.
  - Tính ổn định của các kết luận công nghệ có ý nghĩa then chốt hơn độ chính xác tuyệt đối:
    - Thời gian lưu bùn (SRT) duy trì vị trí nhân tố tác động hàng đầu (first-ranked driver) đối với TMP và mực nước bể màng dưới cả $4$ phương thức huấn luyện: ngẫu nhiên, phân khối $24\text{ h}$, phân khối $168\text{ h}$ (168-h blocked) và tuần tự theo thời gian (chronological training).
    - Các kết luận về cơ chế quá trình công nghệ là đặc tính cố hữu của hồ sơ dữ liệu nhà máy (properties of the plant record) thay vì phụ thuộc vào bất kỳ phương án phân chia dữ liệu cụ thể nào.
- Phân tích phân chia theo thời gian (chronological partition) và lợi ích của cơ chế tái khớp định kỳ (periodic refitting):
  - Phương thức phân chia tuần tự theo thời gian thông thường phản ánh một kịch bản triển khai không thực tế trong vận hành: khớp mô hình một lần duy nhất trên $7$ tháng đầu tiên và giữ cố định (frozen model) để dự báo cho $4$ tháng tiếp theo.
  - Trong thực tế nhà máy, dữ liệu quan trắc mới theo từng giờ đều truyền về hệ thống lưu trữ (historian) trong vòng $1\text{ giờ}$, và việc khớp lại mô hình Extra Trees trên toàn bộ hồ sơ dữ liệu chỉ mất khoảng $1\text{ giây}$ ($~1\text{ s}$).
  - Khớp lại mô hình theo chu kỳ cố định trên toàn bộ dữ liệu tích lũy đến thời điểm đó, với mọi dự báo đều được thực hiện nghiêm ngặt trước mốc dữ liệu dùng để huấn luyện, giúp giải quyết triệt để vấn đề trôi dạt hiệu năng.
  - Độ chính xác ngoài thời gian (out-of-time accuracy) cải thiện đơn điệu khi chu kỳ làm mới mô hình được rút ngắn:
    - Khi khớp lại hàng ngày (daily refit), giá trị $R^2$ trên $30\%$ dữ liệu thời gian cuối cùng được giữ lại đạt $0.871$ cho TMP, $0.580$ cho mực nước và $0.574$ cho lưu lượng thấm (permeate flow).
    - TMP được dự đoán với sai số đạt $0.008\text{ bar}$, tương ứng mức giảm $80\%$ sai số so với mô hình cố định (Fig. S17D, Table S12).
  - Khả năng tổng quát hóa theo thời gian (temporal generalisation) được quyết định bởi lịch trình làm mới mô hình (refresh schedule) thay vì giới hạn nội tại của thuật toán.
  - Khuyến nghị triển khai công nghiệp cụ thể: thực hiện khớp lại mô hình trên dữ liệu tích lũy tối thiểu hàng tuần (weekly), và hàng ngày (daily) khi hệ thống kết nối historian cho phép tự động hóa mà không phát sinh chi phí tính toán.
- Bảng 3 (Table 3) tổng hợp hiệu năng trên tập kiểm tra (test set performance) của $16$ mô hình học máy trên ba biến mục tiêu (TMP, lưu lượng permeate flow, mực nước bể màng membrane tank water level), xếp hạng theo giá trị $R^2$ trung bình trên các mục tiêu (các giá trị tốt nhất trong từng cột được gạch chân trong tài liệu gốc):

| Mô hình (Model) | TMP $R^2$ | TMP RMSE (bar) | TMP MAE (bar) | TMP $\Delta R^2$ | Flow $R^2$ | Flow RMSE ($\text{m}^3/\text{min}$) | Flow MAE ($\text{m}^3/\text{min}$) | Flow $\Delta R^2$ | Level $R^2$ | Level RMSE (%) | Level MAE (%) | Level $\Delta R^2$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Extra Trees | 0.988 | 0.010 | 0.005 | 0.012 | 0.933 | 0.066 | 0.052 | 0.067 | 0.908 | 0.341 | 0.227 | 0.092 |
| Bagging | 0.978 | 0.014 | 0.006 | 0.019 | 0.910 | 0.076 | 0.059 | 0.076 | 0.839 | 0.450 | 0.282 | 0.140 |
| Random Forest | 0.978 | 0.014 | 0.006 | 0.019 | 0.909 | 0.077 | 0.059 | 0.076 | 0.839 | 0.450 | 0.282 | 0.140 |
| XGBoost | 0.977 | 0.014 | 0.007 | 0.022 | 0.906 | 0.078 | 0.061 | 0.081 | 0.843 | 0.444 | 0.292 | 0.143 |
| LightGBM | 0.978 | 0.014 | 0.008 | 0.015 | 0.898 | 0.081 | 0.063 | 0.048 | 0.822 | 0.473 | 0.321 | 0.109 |
| Hist Grad. Boost. | 0.976 | 0.014 | 0.008 | 0.016 | 0.899 | 0.081 | 0.064 | 0.048 | 0.839 | 0.450 | 0.312 | 0.094 |
| KNN | 0.969 | 0.016 | 0.007 | 0.011 | 0.894 | 0.083 | 0.063 | 0.036 | 0.813 | 0.485 | 0.298 | 0.062 |
| MLP Neural Net. | 0.951 | 0.020 | 0.011 | 0.003 | 0.861 | 0.095 | 0.074 | 0.022 | 0.756 | 0.554 | 0.387 | 0.015 |
| Decision Tree | 0.942 | 0.022 | 0.010 | 0.042 | 0.785 | 0.118 | 0.086 | 0.096 | 0.650 | 0.663 | 0.383 | 0.240 |
| GBoosting | 0.937 | 0.023 | 0.014 | 0.011 | 0.824 | 0.107 | 0.084 | 0.024 | 0.698 | 0.616 | 0.437 | 0.059 |
| SVR | 0.893 | 0.030 | 0.016 | -0.005 | 0.771 | 0.122 | 0.092 | 0.004 | 0.498 | 0.794 | 0.458 | 0.034 |
| AdaBoost | 0.781 | 0.042 | 0.037 | 0.002 | 0.655 | 0.150 | 0.120 | 0.023 | 0.308 | 0.932 | 0.796 | -0.020 |
| Lin Regression | 0.499 | 0.064 | 0.045 | 0.015 | 0.469 | 0.185 | 0.147 | 0.010 | 0.195 | 1.006 | 0.696 | 0.001 |
| Rid Regression | 0.499 | 0.064 | 0.045 | 0.015 | 0.469 | 0.185 | 0.147 | 0.010 | 0.195 | 1.006 | 0.696 | 0.001 |
| ElasticNet | 0.480 | 0.065 | 0.046 | 0.005 | 0.435 | 0.192 | 0.151 | 0.008 | 0.159 | 1.028 | 0.735 | -0.001 |
| Las Regression | 0.440 | 0.068 | 0.049 | 0.000 | 0.393 | 0.199 | 0.158 | 0.007 | 0.117 | 1.053 | 0.767 | -0.002 |
