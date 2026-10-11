## 1. Introduction

* Phú dưỡng (eutrophication) là dạng ô nhiễm nguồn nước do tích tụ dinh dưỡng (nutrient-based water pollution), bắt nguồn chủ yếu từ sự xả thải các hợp chất chứa nitơ (nitrogen compounds) và phốt pho (phosphorus compounds) phát sinh từ các quá trình tự nhiên hoặc nhân tạo (anthropogenic processes):
  * Các nguồn phát thải nhân tạo chính dẫn đến phú dưỡng bao gồm hoạt động canh tác nông nghiệp (agricultural sites), quá trình đốt nhiên liệu hóa thạch (fossil fuel combustion), các trạm xử lý nước thải (wastewater treatment), và dòng chảy tràn đô thị khi có mưa bão (stormwater runoff from urban areas).
  * Tác động môi trường nghiêm trọng của phú dưỡng gồm làm thay đổi vị (taste), mùi (odor), màu sắc (color), độ đục (opacity) của nguồn nước tự nhiên, đồng thời dẫn đến suy thoái đa dạng sinh học (biodiversity degradation) và làm cạn kiệt nguồn oxy hòa tan trong các thủy vực (depletion of oxygen in water resources).
  * Việc loại bỏ triệt để các chất dinh dưỡng khỏi các dòng thải là lĩnh vực nghiên cứu cấp thiết nhằm bảo vệ tài nguyên nước mặt.

* Đánh giá các công nghệ loại bỏ chất dinh dưỡng hiện hành và ưu thế của bể phản ứng màng tích hợp:
  * Các công nghệ sinh học (biological), hóa học (chemical), và công nghệ màng (membrane technologies) đã được áp dụng rộng rãi để xử lý dinh dưỡng trong nước thải:
    * Phương pháp sinh học truyền thống không thể đáp ứng ổn định các tiêu chuẩn xả thải khắt khe đối với tổng nitơ ($\text{TN}$ - total nitrogen) và tổng phốt pho ($\text{TP}$ - total phosphorus).
    * Phương pháp xử lý hóa học làm gia tăng đáng kể lượng bùn thải phát sinh (sludge production), kéo theo chi phí xử lý và chôn lấp bùn tốn kém.
  * Phương pháp màng kết hợp với các quá trình hóa học và sinh học là giải pháp giàu triển vọng, giúp nâng cao tính khả thi về mặt kỹ thuật lẫn kinh tế (technical and economic feasibility) của toàn bộ hệ thống.
  * Bể phản ứng sinh học màng (MBR - membrane bioreactors) là lựa chọn tối ưu cho mục tiêu tái sử dụng nước (potable reuse) nhờ giảm dấu chân sinh thái / diện tích mặt bằng (ecological footprint), hiệu quả khử mầm bệnh cao (pathogen reduction), và chi phí đầu tư ban đầu hợp lý (low capital costs).
  * Hệ thống bể phản ứng sinh học màng kỵ khí - thiếu khí - hiếu khí ($\text{A}^2\text{O-MBR}$ - anaerobic-anoxic-oxic membrane bioreactor) đạt hiệu suất vượt trội nhờ áp dụng hiệu quả quy trình nạp dòng phân đoạn thiếu khí - hiếu khí (step-feed anoxic-oxic process) trong việc loại bỏ đồng thời nitơ và phốt pho.
  * Việc bổ sung các giá thể nhựa lơ lửng (floating plastic carriers) kết hợp quy trình nạp phân đoạn thiếu khí - hiếu khí trong các ngăn hiếu khí mang lại tiềm năng nâng cấp, cải tạo lớn cho các nhà máy xử lý nước thải hiện hữu.
  * Mục tiêu nền tảng là khảo sát toàn diện hệ thống $\text{A}^2\text{O-MBR}$ xử lý dinh dưỡng tại trạm xử lý nước thải quy mô thực tế (full-scale wastewater treatment plant).

* Thách thức trong tối ưu hóa vận hành và giới hạn của các phương pháp mô hình hóa truyền thống:
  * Hiệu suất loại bỏ dinh dưỡng của hệ thống $\text{A}^2\text{O-MBR}$ chịu sự chi phối phức tạp bởi các điều kiện vận hành (operating conditions) và đặc tính dòng vào (influent characteristics).
  * Kỹ thuật mô hình hóa từng yếu tố đơn lẻ tại một thời điểm (OFAT - one-factor-at-a-time modeling technique) thường được dùng để tối ưu hóa và kiểm soát các hệ thống xử lý nước thải:
    * Việc triển khai hàng loạt thí nghiệm kiểm chứng trong phòng thí nghiệm (laboratory experiments) theo các phương pháp mô hình hóa thông thường/động học truyền thống (ASM) rất tốn kém chi phí (expensive) và tiêu tốn nhiều thời gian (time-consuming).
    * Các phương pháp mô hình hóa giải tích/cơ học cổ điển không thể mô phỏng chính xác các cơ chế sinh học - hóa lý phi tuyến cực kỳ phức tạp bên trong hệ thống $\text{A}^2\text{O-MBR}$.

* Tiềm năng và ứng dụng thực tiễn của các công cụ học máy (ML - machine learning) trong xử lý nước thải:
  * Các công cụ học máy có năng lực vượt bậc trong việc giải quyết các khó khăn mà phương pháp mô hình hóa truyền thống gặp phải.
  * Mạng nơ-ron nhân tạo ($\text{ANN}$ - artificial neural network) mô hình hóa hiệu quả các hệ thống xử lý nước thải sinh học phi tuyến và phức tạp (complex and non-linear biological wastewater treatment systems) so với các kỹ thuật giải tích thông thường.
  * Bằng chứng thực nghiệm từ các nghiên cứu trước đây khẳng định hiệu quả của học máy trong nhiều lĩnh vực kỹ thuật môi trường:
    * Mô phỏng hệ thống xử lý nước thải để loại bỏ kim loại nặng, cũng như mô hình hóa sự hấp phụ kim loại nặng trong đất và các thủy vực tự nhiên.
    * Theo dõi hiệu suất loại bỏ dinh dưỡng của dòng chảy triều trong đất ngập nước kiến tạo (tidal flow in constructed wetlands) và quá trình nitrat hóa bán phần (partial nitrification process) thông qua mô hình $\text{ANN}$.
    * Tối ưu hóa quá trình sản xuất axit hypocloro ($\text{HClO}$ - hypochlorous acid) nhờ kết hợp $\text{ANN}$ với phương pháp bề mặt đáp ứng ($\text{RSM}$ - response surface methodology).
    * Dự đoán chính xác khả năng loại bỏ đồng ($\text{Cu}$) qua quá trình hấp phụ bằng $\text{ANN}$ và dự đoán mức độ ô nhiễm kim loại nặng bằng mô hình học kết hợp (ensemble model).
    * Sử dụng $\text{ANN}$ trong quá trình siêu lọc tăng cường micelle (MEUF - micellar-enhanced ultrafiltration) để nâng cao độ chính xác dự đoán loại bỏ ion kim loại nặng.
    * Tích hợp $\text{ANN}$ với giải thuật di truyền ($\text{GA}$ - genetic algorithms) để tối ưu hóa quá trình sinh khí sinh học (biogas) và khí metan ($\text{CH}_4$) trong mô hình pilot bể phản ứng bùn kỵ khí dòng chảy ngược ($\text{UASB}$ - up-flow anaerobic sludge blanket).
    * Theo dõi quá trình loại bỏ dinh dưỡng trong bể $\text{MBR}$ tăng cường điện trường (electrically enhanced MBR) nhằm xác lập mối tương quan với các thông số đầu vào.
    * Dự đoán nhu cầu oxy hóa học ($\text{COD}$ - chemical oxygen demand) trong hệ sinh học đa bậc xử lý nước thải nhà máy lọc dầu (petroleum refinery wastewater).
    * Ứng dụng máy vector hỗ trợ ($\text{SVM}$ - support vector machine) kết hợp giải thuật di truyền gia tốc ($\text{AGA}$ - accelerating genetic algorithm) tối ưu hóa hệ thống $\text{A}^2\text{O}$ quy mô thực tế để loại bỏ dinh dưỡng.
    * Ứng dụng thuật toán học tăng cường $\text{Q-learning}$ nhằm tối đa hóa hiệu quả loại bỏ phốt pho sinh học tăng cường (EBPR) thông qua chiến lược kiểm soát đáp ứng đặc tính dòng vào (influent response control approach).

* Đánh giá hạn chế của nghiên cứu ứng dụng mô hình $\text{LSTM}$ trên hệ thống $\text{A}^2\text{O-MBR}$ trước đây:
  * Mô hình bộ nhớ ngắn hạn dài ($\text{LSTM}$ - long short-term memory) từng được áp dụng để dự đoán hiệu suất loại bỏ dinh dưỡng của trạm $\text{A}^2\text{O-MBR}$ thực tế dựa trên mối liên hệ giữa các biến:
    * Tập biến đầu vào bao gồm oxy hòa tan ($\text{DO}$ - dissolved oxygen), thế oxy hóa - khử ($\text{ORP}$ - oxidation-reduction potential), chất rắn lơ lửng bùn lỏng ($\text{MLSS}$ - mixed liquor suspended solids), tổng cacbon hữu cơ ($\text{TOC}$ - total organic carbon), tổng nitơ ($\text{TN}$), tổng phốt pho ($\text{TP}$), $\text{COD}$, amoni ($\text{NH}_4$), và chất rắn lơ lửng ($\text{SS}$ - suspended solids).
    * Mô hình $\text{LSTM}$ dự đoán đồng thời cả ba thành phần dinh dưỡng đầu ra ($\text{NH}_4$, $\text{TN}$, $\text{TP}$) trong một kiến trúc mô hình duy nhất (single model).
    * Việc đánh giá hiệu năng mô hình $\text{LSTM}$ chỉ dựa vào hai chỉ số thống kê đơn lẻ: sai số bình phương trung bình ($\text{MSE}$ - mean-square-error) và tỷ số giữa $\text{RMSE}$ trên độ lệch chuẩn của dữ liệu quan sát ($\text{RSR}$ - root-MSE-observation standard deviation ratio).
  * Hai khoảng trống nghiên cứu cốt lõi chưa được giải quyết trong các công bố trước:
    * Khoảng trống 1: Chưa phân tách để khảo sát độc lập ảnh hưởng của các điều kiện vận hành (operating conditions) so với ảnh hưởng của các đặc tính nước thải đầu vào (influent characteristics) đối với khả năng loại bỏ từng chất dinh dưỡng riêng biệt ($\text{NH}_4$, $\text{TN}$, $\text{TP}$).
    * Khoảng trống 2: Thiếu sự nghiên cứu so sánh đối chứng liên mô hình (comparative study) với các cấu trúc học máy tiên tiến khác, đồng thời việc kiểm định mô hình mới chỉ dừng lại ở các thước đo hiệu năng hạn chế.

* Cơ sở lý thuyết của các mô hình học máy được lựa chọn nghiên cứu:
  * Mạng nơ-ron nhiều tầng ($\text{MLP}$ - multilayer perceptron):
    * Là dạng kiến trúc mạng nơ-ron truyền thẳng (feed-forward neural network) tiêu chuẩn, trong đó luồng dữ liệu truyền theo chiều xuôi từ tầng đầu vào (input layer) qua các tầng ẩn (hidden layers) đến tầng đầu ra (output layer).
    * Được ứng dụng chủ đạo trong các bài toán dự đoán chuỗi và xấp xỉ hàm phi tuyến phức tạp.
  * Thuật toán tăng cường gradient cực đại ($\text{XGBoost}$ - extreme gradient boosting):
    * Sở hữu nhiều tính năng vượt trội về tinh chỉnh siêu tham số mô hình (model tuning), tối ưu hóa môi trường tính toán song song, và nâng cấp thuật toán nền tảng.
    * Hỗ trợ cơ chế tinh chỉnh sâu kết hợp bổ sung các số hạng điều chuẩn (regularization parameters) giúp ngăn ngừa hiện tượng quá khớp (overfitting).
    * Khả năng thực thi ba dạng thuật toán tăng cường gradient (GB - gradient boosting) chủ đạo: tăng cường gradient tiêu chuẩn (GB), tăng cường gradient có điều chuẩn (regularized GB), và tăng cường gradient ngẫu nhiên (stochastic GB).

* Đóng góp mới và mục tiêu cụ thể của nghiên cứu:
  * Tính mới khoa học: Đây là nghiên cứu tiên phong áp dụng mô hình $\text{XGBoost}$ và $\text{MLP}$ để mô phỏng và dự đoán hiệu suất loại bỏ dinh dưỡng trên hệ thống $\text{A}^2\text{O-MBR}$ quy mô thực tế.
  * Thiết kế nghiên cứu đa kịch bản (multiple input scenarios): Thiết lập 9 kịch bản phân tách (kết hợp các nhóm biến đặc tính nước vào và điều kiện vận hành) để đánh giá tầm quan trọng của việc lựa chọn đặc trưng (feature selection), từ đó nâng cao năng lực học máy trong việc dự đoán từng chất dinh dưỡng riêng rẽ.
  * Ba mục tiêu nghiên cứu cụ thể:
    * Mục tiêu (i): Phát triển các mô hình $\text{XGBoost}$ và $\text{MLP}$ để dự đoán chính xác hiệu suất loại bỏ từng chất dinh dưỡng ($\text{NH}_4$, $\text{TN}$, $\text{TP}$) dưới các kịch bản đầu vào và đầu ra khác nhau.
    * Mục tiêu (ii): Kiểm định và đánh giá toàn diện hiệu năng của các mô hình $\text{XGBoost}$ và $\text{MLP}$ dựa trên hệ thống các chỉ số thống kê chuẩn hóa gồm hệ số xác định ($R^2$), sai số toàn phương trung bình ($\text{RMSE}$ - root mean square error), sai số tuyệt đối trung bình ($\text{MAE}$ - mean absolute error), và sai số phần trăm tuyệt đối trung bình ($\text{MAPE}$ - mean absolute percentage error).
    * Mục tiêu (iii): So sánh đối chứng hiệu năng giữa $\text{XGBoost}$, $\text{MLP}$ và mô hình $\text{LSTM}$ được công bố trước đó nhằm xác định mô hình tối ưu nhất cho bài toán quan trắc và dự đoán loại bỏ dinh dưỡng tại trạm xử lý nước thải $\text{A}^2\text{O-MBR}$ quy mô thực tế.
