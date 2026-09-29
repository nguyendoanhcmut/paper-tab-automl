# Dự đoán khả giải liều lượng chất keo tụ trong nhà máy xử lý nước cấp dựa trên học máy tự động (AutoML) và phương pháp SHAP

## 1. Tổng quan và Phương pháp nghiên cứu

### 1.1 Thông tin xuất bản và Tóm tắt công trình

#### 1.1.1 Siêu dữ liệu bài báo và Tác giả
- Tiêu đề công trình: Interpretable prediction of coagulant dosage in drinking water treatment plant based on automated machine learning and SHAP method.
- Danh sách tác giả: Liyan Feng, Ying Zhang, Xiaoting Wei, Mengyuan Wang, Zhiguang Niu, Chenchen Wang.
- Tác giả liên hệ: Ying Zhang (yzhang_n@tju.edu.cn) và Chenchen Wang (wcc12122008@163.com).
- Cơ quan chủ quản: Trường Khoa học & Kỹ thuật Môi trường thuộc Đại học Thiên Tân, Trường Kỹ thuật Môi trường & Đô thị thuộc Đại học Thành Kiến Thiên Tân, Phòng thí nghiệm Trọng điểm Khoa học và Công nghệ Nước Thiên Tân, Công ty TNHH Cấp nước TEDA Kim Liên Thiên Tân.
- Thông tin xuất bản: Tạp chí Journal of Water Process Engineering, Tập 75, Năm 2025, Mã bài báo 107925, Nhà xuất bản Elsevier.
- Lịch sử bài báo: Tạp chí nhận bản thảo ngày 25 tháng 01 năm 2025. Tác giả nộp bản sửa đổi ngày 01 tháng 05 năm 2025. Ban biên tập chấp nhận đăng ngày 09 tháng 05 năm 2025. Bài báo xuất bản trực tuyến ngày 15 tháng 05 năm 2025.
- Chỉ số định danh: Mã định danh số $\text{DOI: } 10.1016/\text{j.jwpe.2025.107925}$. Mã chuẩn quốc tế $\text{ISSN: } 2214-7144$.
- Từ khóa chuyên ngành: Automated machine learning, SHAP interpretability, Random Forest, Coagulant, Water treatment.

#### 1.1.2 Tóm tắt nghiên cứu và Các chỉ số định lượng then chốt
- Mục tiêu nghiên cứu: Nghiên cứu xây dựng mô hình dự đoán chính xác liều lượng hóa chất keo tụ trong nhà máy xử lý nước cấp (DWTP) bằng học máy tự động (AutoML). Nghiên cứu tích hợp phương pháp SHAP nhằm loại bỏ tính chất hộp đen và nâng cao tính minh bạch khi ra quyết định.
- Hiệu năng vượt trội của mô hình Random Forest (RF): Mô hình RF do AutoML tối ưu hóa đạt hiệu năng vượt trội so với mô hình cây tăng cường độ dốc (GBT) đơn lẻ tốt nhất. Mô hình đạt chỉ số $\text{RMSE} = 0.89\text{ mg/L}$, giảm $37\%$. Mô hình đạt chỉ số $\text{MAE} = 0.47\text{ mg/L}$, giảm $52\%$. Mô hình đạt hệ số xác định $R^2 = 0.96$, tăng $5\%$.
- Tiết kiệm chi phí và hóa chất định lượng: Mô hình RF cắt giảm $10.25\%$ tổng lượng hóa chất keo tụ tiêu thụ mỗi năm.
- Định mức tiết kiệm cho nguồn nước Sông Dương Tử: Tiết kiệm $222\text{ kg/ngày}$ hóa chất PACl. Giá trị tiết kiệm chi phí tương đương $180.7\text{ Nhân dân tệ/ngày}$.
- Định mức tiết kiệm cho nguồn nước Sông Loan Hà: Tiết kiệm $225\text{ kg/ngày}$ hóa chất PACl. Giá trị tiết kiệm chi phí tương đương $183.2\text{ Nhân dân tệ/ngày}$.
- Kiểm soát ổn định chất lượng nước sau xử lý: Mô hình duy trì độ đục và pH đầu ra ổn định hơn so với phương thức vận hành thủ công.
- Nhận diện các biến động lực then chốt: Phân tích SHAP xác định độ dẫn điện ($\text{EC-RW}$), nitơ amoni ($\text{NH}_3\text{-N-RW}$), nhu cầu oxy hóa học ($\text{CODMn-RW}$) và nhiệt độ nước thô ($\text{T-RW}$) là các yếu tố chi phối mạnh nhất đến liều lượng châm PACl. Liều lượng PACl tác động trực tiếp và rõ nét nhất lên pH nước sau xử lý ($\text{pH-TW}$).

### 1.2 Bối cảnh nghiên cứu và Khoảng trống công nghệ

#### 1.2.1 Thách thức trong vận hành định liều keo tụ tại DWTP
- Mục tiêu giảm phát thải carbon: Ngành xử lý nước đối mặt với áp lực tiêu thụ năng lượng và phát thải khí nhà kính ngày càng gia tăng. Quá trình tối ưu hóa các công đoạn truyền thống nhằm đạt mục tiêu xanh và ít carbon gặp nhiều giới hạn kỹ thuật và kinh tế.
- Giới hạn kinh tế kỹ thuật của các công nghệ xử lý nâng cao: Phương pháp hấp phụ gặp khó khăn lớn trong việc hoàn nguyên vật liệu. Quá trình khoáng hóa sâu bằng quang xúc tác bị hạn chế bởi hiệu suất lượng tử. Xúc tác vi sóng đạt hiệu suất cao nhưng đòi hỏi chi phí đầu tư thiết bị rất lớn.
- Chi phí vận hành công đoạn keo tụ: Keo tụ là mắt xích cốt lõi trong dây chuyền xử lý nước cấp. Chi phí hóa chất keo tụ chiếm tỷ trọng lớn trong tổng chi phí sản xuất của các nhà máy nước.
- Đặc tính động học phức tạp: Quá trình keo tụ phụ thuộc vào nhiều biến số đầu vào như nhiệt độ nước, độ đục, pH và độ kiềm. Hệ thống phản ứng phi tuyến tính mạnh và chịu ảnh hưởng liên tục từ các nhiễu động thời gian thực.
- Hạn chế của các mô hình kinh nghiệm: Mô hình kinh nghiệm truyền thống không thể cân bằng đồng thời độ chính xác châm hóa chất và hiệu quả tiết kiệm năng lượng. Việc xác định liều lượng keo tụ tối ưu dựa trên biến động chất lượng nước thô và tiêu chuẩn nước sạch đầu ra giữ vai trò quyết định.

#### 1.2.2 Hạn chế của các phương pháp định liều truyền thống
- Thiếu sót của phương pháp vận hành thủ công: Vận hành thủ công phụ thuộc hoàn toàn vào trực giác và kinh nghiệm của công nhân. Thao tác này có tính chủ quan cao và dẫn đến tình trạng châm thừa hóa chất liên tục. Cách thức này không thể thích ứng với quy mô sản xuất công nghiệp lớn, gây mất ổn định chất lượng nước và tạo độ trễ điều khiển nghiêm trọng.
- Rào cản của mô hình cơ chế hóa lý: Mô hình động học cơ chế gặp khó khăn trong việc mô tả đầy đủ các phản ứng hóa học phức tạp và mối quan hệ phi tuyến giữa các hạt keo. Sự phụ thuộc vào nhiều giả định đơn giản hóa làm giảm khả năng ứng dụng thực tế tại nhà máy.
- Hạn chế của các mô hình học máy truyền thống: Mô hình học máy dựa trên dữ liệu có thể học mối quan hệ phi tuyến từ tập dữ liệu giới hạn. Tuy nhiên, các kiến trúc hiện có bộc lộ nhiều điểm nghẽn về khả năng hội tụ và tính tổng quát hóa.
- Mô hình DL-MV: Phương pháp học sâu đa biến (DL-MV) phụ thuộc nặng nề vào quá trình tinh chỉnh thủ công để đạt độ chính xác cao.
- Mô hình PSO-SVR: Thuật toán tối ưu hóa bầy đàn kết hợp máy vector hỗ trợ (PSO-SVR) đòi hỏi kỹ sư thiết lập trước các tham số tìm kiếm tĩnh.
- Mô hình GA-RF: Thuật toán di truyền kết hợp rừng ngẫu nhiên (GA-RF) sở hữu kiến trúc đóng cứng, kém linh hoạt và tiêu tốn tài nguyên tính toán lớn.
- Hai nút thắt kỹ thuật cốt lõi: Các phương pháp truyền thống phụ thuộc vào sự can thiệp thủ công của con người nên không thể tự động thích ứng với biến động chất lượng nước. Các phương pháp này tuân theo một khuôn mẫu tối ưu hóa đơn lẻ và thiếu cơ chế hiệp đồng động, làm hạn chế hiệu suất dự đoán và độ bền vững.

#### 1.2.3 Tiềm năng của AutoML và Nhu cầu minh bạch hóa với SHAP
- Cơ chế của học máy tự động (AutoML): AutoML tự động hóa toàn bộ đường ống máy học bao gồm tiền xử lý đặc trưng, lựa chọn thuật toán và tối ưu hóa siêu tham số. AutoML cắt giảm tối đa sự can thiệp của con người và giảm thiểu chi phí phát triển mô hình.
- Nền tảng phân tán TPOT: Công cụ tối ưu hóa đường ống dựa trên cây (TPOT) sử dụng lập trình di truyền để tự động sàng lọc các kiến trúc mô hình tối ưu.
- Thành tựu thực nghiệm của TPOT: TPOT cải thiện độ chính xác từ $15\%$ đến $20\%$ trên tập dữ liệu chất lượng nước 50 chiều mà không cần giảm chiều đặc trưng. TPOT vượt qua các mô hình học máy truyền thống $1.4\%$ trong nhiệm vụ phân loại chất lượng nước hồ.
- Khung H2O trong công nghệ môi trường: Khung H2O dự đoán chính xác quá trình loại bỏ chất dinh dưỡng sinh học trong xử lý nước thải.
- Khoảng trống nghiên cứu keo tụ: AutoML chưa từng được áp dụng để dự đoán liều lượng hóa chất keo tụ trong các nhà máy nước cấp công nghiệp.
- Nút thắt hộp đen trong ứng dụng công nghiệp: Các mô hình học máy tiên tiến hoạt động như những hộp đen bí ẩn. Bản chất này làm mất tính minh bạch và cản trở việc triển khai thực tế tại các nhà máy xử lý nước cấp, nơi yêu cầu độ tin cậy và an toàn vận hành cao.
- Phương pháp giải thích SHAP: Lý thuyết giải thích phụ gia Shapley (SHAP) do Lundberg và Lee phát triển dựa trên lý thuyết trò chơi hợp tác. SHAP định lượng đóng góp biên của từng biến đặc trưng đối với kết quả dự đoán. SHAP cung cấp góc nhìn toàn cục và phân tích cục bộ để làm rõ các hiệu ứng tương tác.
- Mục tiêu đột phá của đề tài: Đề tài lần đầu tiên kết hợp khung AutoML và phương pháp giải thích SHAP nhằm dự đoán liều lượng châm PACl. Hệ thống kết hợp dữ liệu vận hành thời gian thực và lịch sử để kiểm soát chính xác công đoạn keo tụ, đảm bảo tiêu chuẩn nước cấp sạch và tiết kiệm chi phí.

### 1.3 Thu thập dữ liệu và Quy trình tiền xử lý thực nghiệm

#### 1.3.1 Hiện trường nhà máy và Thuộc tính nguồn nước
- Địa điểm nghiên cứu: Nhà máy xử lý nước cấp DWTP tọa lạc tại thành phố Thiên Tân, Trung Quốc.
- Nguồn nước thô hai nguồn luân phiên: Nhà máy tiếp nhận nguồn nước từ hai lưu vực khác nhau nhằm thích ứng theo mùa.
- Nguồn nước Sông Loan Hà: Nước chuyển đổi từ tỉnh Hà Bắc, cung cấp cho nhà máy trong 3 tháng mùa đông (tháng 12, tháng 1 và tháng 2 hàng năm).
- Nguồn nước Sông Dương Tử: Nước lấy từ Hồ chứa Đan Giang Khẩu thuộc tỉnh Hồ Bắc, cung cấp cho nhà máy trong 9 tháng còn lại (từ tháng 3 đến tháng 11 hàng năm).
- Công suất thiết kế của DWTP: Công suất xử lý nước sạch đạt $17.5\text{ vạn tấn/ngày}$ ($17.5\text{ wt/d} = 175{,}000\text{ m}^3/\text{ngày}$).
- Thời gian lưu nước thủy lực (HRT): Giá trị HRT duy trì ổn định ở mức $25.56\text{ phút}$.
- Quy trình công nghệ tại nhà máy: Dây chuyền xử lý gồm công đoạn tiền xử lý, công đoạn xử lý truyền thống tăng cường, công đoạn khử trùng kết hợp tia cực tím (UV) và clo.
- Chế độ định lượng hóa chất kép: Nhà máy sử dụng song song hai loại chất keo tụ là sắt clorua ($\text{FeCl}_3$) và polyaluminum clorua ($\text{PACl}$).
- Vị trí châm hóa chất: $\text{FeCl}_3$ được châm trong giai đoạn tiền xử lý. $\text{PACl}$ được định lượng trong giai đoạn khuấy trộn phối phản ứng.
- Cơ sở chọn biến mục tiêu: Hoạt động thực tế tại nhà máy và đánh giá của chuyên gia vận hành cho thấy liều lượng của hai chất keo tụ có giá trị tương đương nhau. Độ chênh lệch liều lượng tối đa không vượt quá $5\text{ mg/L}$. Do đó, nghiên cứu lựa chọn liều lượng $\text{PACl}$ làm biến mục tiêu duy nhất ($Y$) để xây dựng mô hình dự đoán.

#### 1.3.2 Tập dữ liệu quan trắc và Phân chia dữ liệu
- Khung thời gian thu thập dữ liệu: Dữ liệu vận hành được ghi nhận liên tục theo chu kỳ hàng ngày từ tháng 10 năm 2022 đến tháng 5 năm 2024.
- Tổng số mẫu quan trắc: Toàn bộ tập dữ liệu gồm $N = 1339$ điểm quan trắc hoàn chỉnh.
- Phân chia tập dữ liệu: Tập dữ liệu được phân chia ngẫu nhiên thành hai phần độc lập theo tỷ lệ $8:2$.
- Tập huấn luyện (Training set): Gồm $1071\text{ mẫu}$, chiếm $80\%$ tổng dữ liệu, dùng để huấn luyện và tối ưu hóa siêu tham số mô hình.
- Tập kiểm thử (Test set): Gồm $268\text{ mẫu}$, chiếm $20\%$ tổng dữ liệu, dùng để đánh giá độc lập năng lực tổng quát hóa.
- Biến đặc trưng đầu vào dòng lưu lượng: Lưu lượng nước cấp đầu vào ($\text{WTR}$).
- Biến đặc trưng chất lượng nước thô (Raw Water - RW):
  - Nhiệt độ nước thô: $\text{T-RW}$ ($^\circ\text{C}$).
  - Độ kiềm toan nước thô: $\text{pH-RW}$.
  - Độ đục nước thô: $\text{NTU-RW}$ ($\text{NTU}$).
  - Độ dẫn điện nước thô: $\text{EC-RW}$ ($\mu\text{S/cm}$).
  - Chỉ số pemanganat biểu thị nhu cầu oxy hóa học: $\text{CODMn-RW}$ ($\text{mg/L}$).
  - Hàm lượng nitơ amoni trong nước thô: $\text{NH}_3\text{-N-RW}$ ($\text{mg/L}$).
- Biến đặc trưng chất lượng nước sau xử lý (Treated Water - TW):
  - Nhiệt độ nước sau xử lý: $\text{T-TW}$ ($^\circ\text{C}$).
  - Độ kiềm toan nước sau xử lý: $\text{pH-TW}$.
  - Độ đục nước sau xử lý: $\text{NTU-TW}$ ($\text{NTU}$).
  - Độ dẫn điện nước sau xử lý: $\text{EC-TW}$ ($\mu\text{S/cm}$).
  - Chỉ số pemanganat nước sau xử lý: $\text{CODMn-TW}$ ($\text{mg/L}$).
- Lưu ý đo đạc: Chỉ tiêu $\text{NH}_3\text{-N}$ chỉ được quan trắc trên nguồn nước thô và không đo trên dòng nước sau xử lý.

#### 1.3.3 Xử lý giá trị khuyết thiếu bằng thuật toán KNN
- Nguyên nhân phát sinh dữ liệu khuyết: Lỗi cảm biến đo đạc tại hiện trường và sự cố đột xuất của hệ thống cấp hóa chất gây ra các khoảng trống dữ liệu trong tập ghi nhận thô.
- Yêu cầu tiền xử lý: Tiền xử lý dữ liệu loại bỏ sai số đo, bảo toàn chất lượng quyết định và tăng cường độ tin cậy của thuật toán học máy.
- Thuật toán K láng giềng gần nhất (KNN): Nghiên cứu áp dụng mô hình ước lượng KNN để điền khuyết dữ liệu. KNN cân bằng giữa độ ổn định nội suy cục bộ và tính đại diện toàn cục của tập dữ liệu.
- Bảo toàn thông tin biến phi ngẫu nhiên: Thuật toán KNN bảo toàn cấu trúc dữ liệu tốt đối với các thông số quan trọng bị khuyết không ngẫu nhiên như nhiệt độ nước ($\text{T-RW}$) và nitơ amoni ($\text{NH}_3\text{-N-RW}$).
- Tối ưu hóa siêu tham số láng giềng $k$: Nghiên cứu thực hiện tìm kiếm dạng lưới (grid search) giá trị $k$ trong khoảng từ $k = 1$ đến $k = 10$.
- Tiêu chí đánh giá nội suy: Sai số bình phương trung bình ($\text{MSE}$) trên tập kiểm thử được sử dụng làm thước đo hiệu quả nội suy.
- Giá trị $k$ tối ưu: Kết quả thực nghiệm xác định $\text{MSE}$ đạt giá trị nhỏ nhất khi $k = 4$. Do đó, mô hình thiết lập cố định tham số nội suy $k = 4$.

#### 1.3.4 Lọc nhiễu chuỗi thời gian bằng Bộ lọc trung bình trượt
- Tác động tiêu cực của nhiễu dữ liệu: Nhiễu cảm biến và các sai số ngẫu nhiên thời gian thực làm biến dạng tín hiệu quan trắc, gây hiện tượng quá khớp cho các mô hình học sâu và mô hình cây.
- Cấu trúc bộ lọc trung bình trượt (Moving Average Filter): Nghiên cứu tích hợp bộ lọc trung bình trượt để làm mịn chuỗi tín hiệu và triệt tiêu các dao động ngẫu nhiên tần số cao.
- Thiết lập kích thước cửa sổ trượt: Kích thước cửa sổ lọc được xác định chính xác tại giá trị $n = 5$.
- Cơ sở xác định qua hàm tự tương quan (ACF): Kích thước cửa sổ $n = 5$ được lựa chọn dựa trên phân tích hàm tự tương quan ACF của chuỗi dữ liệu chu kỳ.
- Hiệu quả kỹ thuật: Cửa sổ $n = 5$ nắm bắt chính xác các biến động ngắn hạn thực tế của các thông số chất lượng nước, đồng thời ngăn chặn hiện tượng làm mịn quá mức dẫn đến suy giảm biên độ đỉnh giá trị (peak attenuation).

#### 1.3.5 Lọc đặc trưng dư thừa bằng Hệ số tương quan hạng Spearman
- Mục tiêu tinh giảm không gian đặc trưng: Việc đưa quá nhiều biến đầu vào có mức độ tương quan thấp hoặc trùng lặp sẽ làm tăng độ phức tạp tính toán và gây suy giảm khả năng tổng quát hóa của mô hình.
- Ưu thế của hệ số tương quan hạng Spearman ($r_s$): Hệ số tương quan Spearman không yêu cầu giả định phân phối chuẩn của dữ liệu. Phương pháp này có độ nhạy rất thấp trước các mối quan hệ phi tuyến phức tạp và các giá trị dị biệt (outliers).
- Công thức toán học tính hệ số tương quan hạng Spearman:
  $$r_s = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}$$
  Trong đó:
  - $n$ là tổng số cặp quan sát dữ liệu trong mẫu phân tích.
  - $d_i = \text{rg}(X_i) - \text{rg}(Y_i)$ biểu thị độ chênh lệch thứ hạng tương ứng giữa biến đầu vào thứ $i$ và biến đầu ra thứ $i$.
  - $\text{rg}(X_i)$ và $\text{rg}(Y_i)$ lần lượt là thứ hạng được gán cho các giá trị cụ thể của hai biến số.
- Cơ chế sàng lọc: Nghiên cứu phân tích ma trận tương quan giữa lưu lượng $\text{WTR}$, các chỉ số chất lượng nước thô, chất lượng nước sau xử lý và liều lượng keo tụ mục tiêu. Các đặc trưng có giá trị $r_s$ thấp bị loại bỏ để giảm số chiều đầu vào, nâng cao tốc độ tính toán và tăng cường tính ổn định của mô hình máy học.

### 1.4 Khung tối ưu hóa đường ống học máy tự động (AutoML TPOT)

#### 1.4.1 Cấu trúc nền tảng và Thư viện phụ thuộc
- Khái niệm AutoML: Học máy tự động là kỹ thuật sử dụng các thuật toán máy tính để tự động hóa toàn diện quy trình xây dựng đường ống phân tích dữ liệu. AutoML giải quyết tự động các bài toán kỹ thuật đặc trưng, lựa chọn thuật toán và tối ưu hóa siêu tham số.
- Công cụ TPOT (Tree-based Pipeline Optimization Tool): Nghiên cứu lựa chọn phiên bản mã nguồn mở TPOT 0.11.7 chạy trên nền ngôn ngữ Python 3.8.
- Nền tảng di truyền học lập trình (Genetic Programming - GP): TPOT ứng dụng lập trình di truyền dạng cây để tạo lập, biến đổi và tinh chỉnh các chuỗi quy trình xử lý dữ liệu phức tạp.
- Thư viện phụ thuộc cốt lõi: TPOT tích hợp khung thuật toán tiến hóa phân tán DEAP (Distributed Evolutionary Algorithms Framework) và nền tảng thuật toán Scikit-Learn phiên bản 1.0.2.
- Mô-đun mở rộng thuật toán: Hệ thống tích hợp các thuật toán tăng cường gradient tiên tiến như XGBoost để mở rộng không gian tìm kiếm mô hình.
- Tính mở của quy trình: Toàn bộ mã nguồn cấu hình đường ống học máy của TPOT được công khai minh bạch nhằm đảm bảo tính tái lập kết quả nghiên cứu.

#### 1.4.2 Cơ chế tiến hóa và Tối ưu hóa đa mục tiêu biên Pareto
- Mã hóa cây đường ống máy học (Tree-structured Pipeline Encoding): TPOT mô hình hóa các đường ống học máy dưới dạng các cấu trúc cây tiến hóa phân cấp. Mỗi nút lá biểu diễn các biến đầu vào hoặc toán tử tiền xử lý. Mỗi nút trung gian hoặc nút gốc biểu diễn các thuật toán mô hình hóa học máy.
- Không gian siêu tham số định sẵn: TPOT tích hợp hàng loạt thuật toán hồi quy từ Scikit-Learn với các miền siêu tham số được cấu hình sẵn. Cấu trúc này giúp cân bằng tối đa giữa hiệu quả tìm kiếm ngẫu nhiên và tốc độ hội tụ toán học.
- Tối ưu hóa đa mục tiêu biên Pareto (Pareto-optimal Frontier): TPOT không chỉ tối ưu hóa độ chính xác dự đoán mà còn đồng thời tối thiểu hóa độ phức tạp của cấu trúc cây mô hình. Cơ chế này loại bỏ các đường ống cồng kềnh, ưu tiên các mô hình tinh gọn và ngăn ngừa hiện tượng quá khớp (overfitting).
- Kiểm định chéo lặp 10-fold độc lập: Trong suốt chu trình tiến hóa di truyền, TPOT thực hiện kiểm định chéo lặp 10-fold cross-validation được chạy độc lập 3 lần riêng biệt. Quy trình kiểm định nghiêm ngặt này bảo đảm khả năng tổng quát hóa bền vững của mô hình trên các tập dữ liệu thực tế độc lập.

### 1.5 Phương pháp luận giải thích mô hình với SHAP

#### 1.5.1 Cơ sở lý thuyết trò chơi và Giá trị Shapley
- Nền tảng toán học của SHAP: Phương pháp SHAP (SHapley Additive exPlanations) do Lundberg và Lee đề xuất dựa trên nền tảng lý thuyết trò chơi hợp tác cổ điển.
- Nguyên lý giá trị Shapley: Mỗi biến đặc trưng đầu vào đóng vai trò như một người chơi trong một liên minh hợp tác. Giá trị Shapley phân bổ công bằng phần thưởng dự đoán cho từng biến dựa trên đóng góp biên kỳ vọng của nó trên mọi tập hợp con liên minh có thể tạo ra.
- Công thức toán học tổng quát tính giá trị Shapley:
  $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f(S \cup \{i\}) - f(S) \right]$$
  Trong đó:
  - $F$ là tập hợp chứa toàn bộ các đặc trưng đầu vào của mô hình.
  - $S$ là một tập hợp con bất kỳ của $F$ không chứa đặc trưng mục tiêu $i$ ($S \subseteq F \setminus \{i\}$).
  - $|S|$ là số lượng phần tử thuộc tập hợp con $S$.
  - $|F|$ là tổng số lượng biến đặc trưng đầu vào trong mô hình.
  - $f(S)$ là giá trị dự đoán của mô hình khi chỉ sử dụng tập hợp đặc trưng $S$.
  - $f(S \cup \{i\})$ là giá trị dự đoán của mô hình khi bổ sung thêm biến đặc trưng $i$ vào tập hợp $S$.
  - Biểu thức $f(S \cup \{i\}) - f(S)$ thể hiện đóng góp biên của đặc trưng $i$ đối với liên minh $S$.
- Tiên đề toán học thỏa mãn: Phương pháp đảm bảo 4 tính chất tiên đề cốt lõi gồm tính hiệu quả (Efficiency), tính đối xứng (Symmetry), tính người chơi vô thưởng vô phạt (Dummy player) và tính cộng dồn (Additivity).

#### 1.5.2 Thuật toán Tree SHAP và Môi trường triển khai
- Các phân nhánh thuật toán SHAP: Hệ thống phương pháp luận gồm Kernel SHAP, Deep SHAP và Tree SHAP.
- Ưu thế vượt trội của Tree SHAP: Tree SHAP là thuật toán chuyên biệt hóa dành cho các mô hình học máy dựa trên cấu trúc cây quyết định (Decision Trees, Random Forest, Gradient Boosting). Thuật toán tối ưu hóa thời gian tính toán giá trị Shapley chính xác từ độ phức tạp hàm mũ $\mathcal{O}(T L 2^{|F|})$ xuống độ phức tạp đa thức $\mathcal{O}(T L D^2)$, trong đó $T$ là số lượng cây, $L$ là số lượng nút lá lớn nhất, và $D$ là độ sâu tối đa của cây.
- Môi trường lập trình thực thi: Nghiên cứu triển khai gói thư viện Tree SHAP chuyên dụng trên nền tảng ngôn ngữ Python phiên bản 3.9.

#### 1.5.3 Khung giải thích toàn cục (Global Interpretability)
- Tầm quan trọng đặc trưng trung bình tuyệt đối: Nghiên cứu tính toán giá trị trung bình của trị tuyệt đối các giá trị SHAP trên toàn bộ tập dữ liệu mẫu để đánh giá mức độ đóng góp tổng thể của từng biến số:
  $$I_j = \frac{1}{N} \sum_{k=1}^{N} |\phi_j^{(k)}|$$
  Trong đó:
  - $I_j$ là chỉ số tầm quan trọng toàn cục của biến đặc trưng thứ $j$.
  - $\phi_j^{(k)}$ là giá trị SHAP của biến đặc trưng $j$ tại quan sát mẫu thứ $k$.
  - $N$ là tổng số mẫu dữ liệu trong tập kiểm tra.
- Định lượng tổng tác động của môi trường: Phép cộng gộp các giá trị SHAP tuyệt đối trung bình của toàn bộ các chỉ tiêu chất lượng nước thô và lưu lượng phản ánh tổng mức độ ảnh hưởng của biến động ngoại cảnh lên chiến lược định liều keo tụ.
- Đồ thị phụ thuộc đặc trưng (SHAP Dependency Plots): Đồ thị thể hiện mối quan hệ biến thiên liên tục giữa giá trị số của một biến đặc trưng và giá trị SHAP tương ứng của nó. Đồ thị này trực quan hóa các phản ứng phi tuyến tính và bộc lộ các hiệu ứng tương tác hiệp đồng giữa hai biến số đối với liều lượng hóa chất keo tụ dự đoán.

#### 1.5.4 Khung giải thích cục bộ (Local Interpretability)
- Mục đích phân tích cục bộ: Phân tích cục bộ giải thích chi tiết cơ chế suy luận và tính toán liều lượng hóa chất cho từng trường hợp quan trắc cụ thể tại một thời điểm vận hành nhất định.
- Lựa chọn mẫu điển hình: Nghiên cứu chọn ra hai mẫu dữ liệu đại diện đặc trưng tương ứng với các điều kiện vận hành theo mùa khác nhau để phân tích sâu cơ chế nội tại.
- Biểu đồ thác nước (Waterfall Plot): Biểu đồ bắt đầu từ giá trị dự đoán cơ sở $\mathbb{E}[f(x)]$. Các thanh biểu diễn đóng góp của từng biến đặc trưng được cộng dồn hoặc trừ dần liên tiếp theo chiều dọc để đạt tới giá trị dự đoán liều lượng cuối cùng $f(x)$. Biểu đồ hiển thị rõ ràng hướng tác động tích cực (tăng liều) hoặc tiêu cực (giảm liều) của từng thông số tại thời điểm khảo sát.
- Biểu đồ quyết định (Decision Plot): Biểu đồ theo dõi trực quan đường cong tích lũy đóng góp của tất cả các biến đặc trưng từ đường đáy giá trị trung bình kỳ vọng hướng tới điểm dự đoán thực tế. Biểu đồ làm rõ cơ chế hội tụ quyết định và thứ tự đóng góp của các thông số vận hành trong trường hợp cụ thể.

### 1.6 Tiêu chí định lượng đánh giá hiệu năng mô hình

#### 1.6.1 Căn bậc hai sai số bình phương trung bình (RMSE)
- Định nghĩa toán học: Căn bậc hai sai số bình phương trung bình biểu thị độ phân tán và độ lệch chuẩn của các phần dư dự đoán mô hình.
- Công thức toán học KaTeX:
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$
  Trong đó:
  - $n$ là tổng số mẫu quan sát thực nghiệm trong tập đánh giá.
  - $y_i$ là giá trị thực tế quan sát của liều lượng keo tụ tại mẫu thứ $i$ ($\text{mg/L}$).
  - $\hat{y}_i$ là giá trị dự đoán tương ứng do mô hình học máy tính toán ($\text{mg/L}$).
- Bản chất thống kê và vai trò kỹ thuật: Do sử dụng phép bình phương sai số trước khi lấy căn, $\text{RMSE}$ đặc biệt nhạy cảm với các sai số có độ lớn cao và các giá trị ngoại lai dị biệt. Chỉ số $\text{RMSE}$ càng nhỏ phản ánh sai số dự đoán trung bình của mô hình càng thấp và độ tin cậy càng cao.

#### 1.6.2 Sai số tuyệt đối trung bình (MAE)
- Định nghĩa toán học: Sai số tuyệt đối trung bình đo lường khoảng cách tuyệt đối trung bình giữa các giá trị dự đoán của thuật toán và các giá trị thực tế quan sát được.
- Công thức toán học KaTeX:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
  Trong đó:
  - $n$ là tổng số điểm dữ liệu quan trắc trong tập kiểm thử.
  - $y_i$ là giá trị thực nghiệm của liều lượng châm hóa chất keo tụ ($\text{mg/L}$).
  - $\hat{y}_i$ là giá trị dự đoán tạo ra từ đường ống học máy ($\text{mg/L}$).
- Bản chất thống kê và vai trò kỹ thuật: Khác với $\text{RMSE}$, $\text{MAE}$ không phóng đại các sai số lớn mà biểu diễn trọng số đồng đều tuyến tính trên toàn bộ các phần dư. Chỉ số $\text{MAE}$ tiến sát về giá trị $0$ chứng minh mô hình có độ lệch dự đoán tuyến tính thấp và hoạt động rất ổn định trên thực địa.

#### 1.6.3 Hệ số xác định ($R^2$)
- Định nghĩa toán học: Hệ số xác định lượng hóa tỷ lệ phương sai của biến mục tiêu thực tế được giải thích thành công bởi các biến đặc trưng thông qua mô hình dự đoán.
- Công thức toán học KaTeX:
  $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
  Trong đó:
  - $n$ là tổng số quan sát trong tập dữ liệu.
  - $y_i$ là giá trị thực tế của liều lượng hóa chất châm tại điểm thứ $i$.
  - $\hat{y}_i$ là giá trị liều lượng hóa chất dự đoán từ mô hình.
  - $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ là giá trị trung bình số học của toàn bộ các quan sát liều lượng thực tế.
  - Tử số $\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$ là tổng bình phương các phần dư (Residual Sum of Squares - $\text{SS}_{\text{res}}$).
  - Mẫu số $\sum_{i=1}^{n} (y_i - \bar{y})^2$ là tổng bình phương tổng thể (Total Sum of Squares - $\text{SS}_{\text{tot}}$).
- Bản chất thống kê và vai trò kỹ thuật: Hệ số $R^2$ nhận giá trị tối đa bằng $1$. Giá trị $R^2$ càng tiệm cận $1$ phản ánh mức độ tương thích hoàn hảo giữa mô hình và dữ liệu thực tế, khẳng định sai số dự đoán rất nhỏ và độ bền vững của mô hình đạt mức tối ưu.

---

## 2. Đặc tính chất lượng nước và Hiệu năng mô hình AutoML

### 2.1 Phân tích dữ liệu chất lượng nước và lựa chọn đặc trưng

#### 2.1.1 Thống kê mô tả và mức độ phân tán của các thông số chất lượng nước
- Phân phối tần suất dữ liệu: Biểu đồ phân phối tần suất (Histogram) kết hợp đường cong khớp tần số biểu diễn mật độ xuất hiện của 1339 mẫu quan trắc.
- Chỉ số định lượng mức độ biến thiên dữ liệu: Hệ số biến thiên ($CV$, tính theo phần trăm) và độ lệch chuẩn ($SD$) lượng hóa độ phân tán của các đặc trưng:
  $$CV = \frac{SD}{\text{Mean}} \times 100\%$$
- Các thông số có độ biến thiên dữ liệu mạnh nhất trong tập dữ liệu:
  - Nhiệt độ nước thô ($\text{T-RW}$): Độ lệch chuẩn $SD = 9.37^\circ\text{C}$, hệ số biến thiên $CV = 62\%$.
  - Nồng độ nitơ amoniac nước thô ($\text{NH}_3\text{-N-RW}$): Độ lệch chuẩn $SD = 0.07\text{ mg/L}$, hệ số biến thiên $CV = 59\%$.
  - Độ đục nước thô ($\text{NTU-RW}$): Độ lệch chuẩn $SD = 2.58\text{ NTU}$, hệ số biến thiên $CV = 57\%$.
  - Nhiệt độ nước sạch sau xử lý ($\text{T-TW}$): Độ lệch chuẩn $SD = 8.77^\circ\text{C}$, hệ số biến thiên $CV = 54\%$.
- Các thông số có độ ổn định cao nhất trong toàn bộ chu trình xử lý:
  - Độ pH nước thô ($\text{pH-RW}$): Hệ số biến thiên $CV = 3\%$.
  - Độ pH nước sạch ($\text{pH-TW}$): Hệ số biến thiên $CV = 2\%$.
  - Độ dao động pH của nước thô và nước sạch duy trì ở mức tối thiểu xuyên suốt quá trình xử lý nước cấp.

#### 2.1.2 Quy luật biến thiên theo mùa và cơ chế lý hóa của quá trình keo tụ
- Tác động của chất lượng nước thô: Chất lượng nước thô quyết định trực tiếp độ an toàn của nguồn cấp nước sinh hoạt và nhu cầu tiêu hao chất keo tụ PACl.
- Quy luật biến thiên theo mùa của các chỉ số ô nhiễm: Nồng độ $\text{CODMn}$ và $\text{NH}_3\text{-N}$ thể hiện chu kỳ biến thiên rõ rệt giữa mùa hè và mùa đông.
- Cơ chế lý hóa trong giai đoạn mùa hè:
  - Nhiệt độ cao kết hợp lượng mưa lớn kích thích tảo sinh trưởng mạnh tại nguồn nước mặt.
  - Sinh khối tảo làm tăng vọt chỉ số pemanganat ($\text{CODMn-RW}$) và làm suy giảm chất lượng nước thô.
  - Nhiệt độ nước tăng làm giảm độ nhớt động lực học của môi trường nước.
  - Độ nhớt giảm thúc đẩy tốc độ khuếch tán và va chạm của các hạt keo tích điện trong dung dịch.
  - Hiệu ứng chuyển động nhiệt hỗ trợ tạo bông nhanh, qua đó làm giảm nhu cầu định liều hóa chất keo tụ.
- Cơ chế lý hóa trong giai đoạn mùa đông:
  - Nhiệt độ nước hạ thấp làm suy giảm độ tan và hệ số khuếch tán phân tử của chất keo tụ PACl.
  - Năng lượng hoạt hóa phản ứng tăng làm suy giảm tốc độ thủy phân của ion nhôm $\text{Al}^{3+}$.
  - Phản ứng tạo nhân bông keo diễn ra chậm chạp.
  - Bông cặn hình thành có cấu trúc xốp rỗng, hạt nhỏ mịn và tỷ trọng thấp khó lắng.
  - Người vận hành buộc phải tăng liều lượng châm PACl để đảm bảo hiệu quả lắng trong nước.
- Yêu cầu định liều chính xác: Nhà máy cần tính toán liều lượng PACl tối ưu dựa trên dữ liệu nước thô thời gian thực kết hợp biến động lịch sử.

#### 2.1.3 Ma trận tương quan hạng Spearman giữa các biến đầu vào và liều lượng PACl
- Nguyên lý đánh giá tương quan: Hệ số tương quan hạng Spearman ($r_s$) xác định mối quan hệ đơn điệu phi tuyến giữa các đặc trưng đầu vào và biến mục tiêu liều lượng PACl.
- Nhóm thông số tương quan mạnh với liều lượng châm PACl:
  - Nhiệt độ nước thô ($\text{T-RW}$): Hệ số $r_s = -0.71$. Nhiệt độ cao làm tăng tốc phản ứng thủy phân và giảm nhu cầu châm hóa chất.
  - Nồng độ nitơ amoniac nước thô ($\text{NH}_3\text{-N-RW}$): Hệ số $r_s = 0.87$. Hàm lượng ion amoni cao đòi hỏi tăng liều lượng PACl để keo tụ tạp chất.
  - Độ pH nước thô ($\text{pH-RW}$): Hệ số $r_s = -0.90$. Nước thô có tính kiềm cao hỗ trợ phản ứng trung hòa axit giải phóng từ PACl.
  - Lưu lượng nước xử lý của nhà máy ($\text{WTR}$): Hệ số $r_s = -0.68$. Lưu lượng dòng chảy thay đổi làm biến đổi thời gian lưu thủy lực trong bể keo tụ.
- Nhóm thông số tương quan trung bình với liều lượng châm PACl:
  - Độ đục nước thô ($\text{NTU-RW}$): Hệ số $r_s = 0.45$. Hạt lơ lửng tăng đòi hỏi thêm hóa chất keo tụ để vô hiệu hóa điện thế zeta.
  - Độ dẫn điện nước thô ($\text{EC-RW}$): Hệ số $r_s = 0.56$. Nồng độ ion hòa tan phản ánh tải lượng tạp chất vô cơ cần keo tụ.
  - Chỉ số pemanganat nước thô ($\text{CODMn-RW}$): Hệ số $r_s = 0.56$. Hợp chất hữu cơ tự nhiên tiêu tốn ion nhôm qua phản ứng phức chất.
  - Độ dẫn điện nước sạch ($\text{EC-TW}$): Hệ số $r_s = 0.43$. Chỉ số phản ánh dư lượng ion khoáng sau chu trình keo tụ.
  - Độ đục nước sạch ($\text{NTU-TW}$): Hệ số $r_s = -0.23$. Liều lượng keo tụ đầy đủ giúp hạ thấp độ đục nước đầu ra.
- Nhóm thông số tương quan rất yếu:
  - Chỉ số pemanganat nước sạch ($\text{CODMn-TW}$): Hệ số $r_s = 0.011$. Mức độ liên kết tuyến tính và phi tuyến với liều châm PACl gần như bằng không.

#### 2.1.4 Phân tích đa cộng tuyến và thiết lập bộ 9 đặc trưng tối ưu
- Nhận diện hiện tượng đa cộng tuyến nghiêm trọng:
  - Cặp biến độ dẫn điện nước thô ($\text{EC-RW}$) và nước sạch ($\text{EC-TW}$) có tương quan tuyến tính rất cao với $r_s = 0.98$.
  - Cặp biến chỉ số pemanganat nước thô ($\text{CODMn-RW}$) và nhiệt độ nước sạch ($\text{T-TW}$) có hệ số $r_s = 0.91$.
  - Cặp biến độ dẫn điện nước thô ($\text{EC-RW}$) và nhiệt độ nước sạch ($\text{T-TW}$) có hệ số nghịch đảo cực mạnh với $r_s = -0.95$.
- Giải pháp loại bỏ biến dư thừa:
  - Mô hình chỉ giữ lại một đại diện từ mỗi nhóm thông số có tương quan tương hỗ vượt ngưỡng kiểm soát.
  - Loại bỏ đặc trưng $\text{EC-TW}$ để tránh trùng lặp thông tin với $\text{EC-RW}$.
  - Loại bỏ đặc trưng $\text{T-TW}$ do hiện tượng đa cộng tuyến mạnh với cả $\text{CODMn-RW}$ và $\text{EC-RW}$.
  - Giữ lại hai đặc trưng chất lượng nước thô cốt lõi gồm $\text{EC-RW}$ và $\text{CODMn-RW}$.
- Không gian 9 đặc trưng đầu vào cuối cùng ($X$):
  1. $\text{WTR}$: Lưu lượng nước thô cấp vào nhà máy ($\text{vạn tấn/ngày}$).
  2. $\text{T-RW}$: Nhiệt độ nước thô đầu vào ($^\circ\text{C}$).
  3. $\text{pH-RW}$: Giá trị pH của nước thô.
  4. $\text{NH}_3\text{-N-RW}$: Nồng độ nitơ amoniac nước thô ($\text{mg/L}$).
  5. $\text{NTU-RW}$: Độ đục nguồn nước thô ($\text{NTU}$).
  6. $\text{EC-RW}$: Độ dẫn điện nước thô ($\mu\text{S/cm}$).
  7. $\text{CODMn-RW}$: Chỉ số pemanganat nước thô ($\text{mg/L}$).
  8. $\text{pH-TW}$: Giá trị pH mục tiêu của nước sạch sau xử lý.
  9. $\text{NTU-TW}$: Độ đục mục tiêu của nước sạch sau xử lý ($\text{NTU}$).
- Biến đầu ra mục tiêu ($Y$): Liều lượng châm chất keo tụ PACl ($\text{mg/L}$). Bộ đặc trưng mô phỏng tương tác phức hợp giữa nước thô, hóa chất và nước thành phẩm.

### 2.2 So sánh hiệu năng và tối ưu hóa mô hình

#### 2.2.1 Cấu hình siêu tham số tối ưu của các thuật toán học máy đối chuẩn
- Phạm vi thuật toán so chuẩn: Nghiên cứu đối chiếu hiệu năng giữa AutoML TPOT với 5 thuật toán máy học tiêu chuẩn:
  - Cây quyết định (Decision Tree - DT).
  - Hồi quy véctơ hỗ trợ (Support Vector Regression - SVR).
  - K láng giềng gần nhất (K-Nearest Neighbors - KNN).
  - Hồi quy tuyến tính (Linear Regression - LR).
  - Cây tăng cường độ dốc (Gradient Boosting Tree - GBT).
- Bảng siêu tham số tối ưu của các thuật toán cơ sở:

| Loại mô hình | Tập siêu tham số tối ưu (Optimal Hyperparameters) | Ý nghĩa kỹ thuật của cấu hình tham số |
| :--- | :--- | :--- |
| **DT** | `max_depth = 8`, `min_samples_split = 10`, `min_samples_leaf = 5`, `max_features = 0.5`, `random_state = 42` | Giới hạn chiều sâu cây ở mức 8 để giảm thiểu quá khớp. Yêu cầu tối thiểu 10 mẫu để tách nhánh và 5 mẫu tại mỗi lá. |
| **SVR** | `C = 1`, `epsilon = 10`, `gamma = 'scale'` | Trọng số phạt sai số $C = 1$. Vùng dung sai không phạt lỗi $\epsilon = 10$. Hệ số hạt nhân RBF tự động điều chỉnh theo nghịch đảo phương sai dữ liệu. |
| **KNN** | `n_neighbors = 15`, `p = 1`, `metric = 'minkowski'` | Sử dụng 15 điểm láng giềng gần nhất. Áp dụng chuẩn khoảng cách Manhattan ($p = 1$) thay vì chuẩn Euclidean để tính khoảng cách vector. |
| **LR** | `fit_intercept = True`, `normalize = True`, `positive = False` | Tính toán hệ số chặn độc lập. Chuẩn hóa biến số về cùng thang đo phân bố. Không ràng buộc dấu dương cho các trọng số. |
| **GBT** | `n_estimators = 150`, `learning_rate = 0.1`, `max_depth = 5`, `min_samples_split = 8`, `subsample = 0.8`, `max_features = 'sqrt'` | Kết hợp 150 cây tuần tự với tốc độ học $\eta = 0.1$. Lấy mẫu ngẫu nhiên 80% dữ liệu huấn luyện cho mỗi cây. Chọn ngẫu nhiên căn bậc hai số đặc trưng. |

- Cơ chế tối ưu hóa tự động của AutoML TPOT:
  - TPOT áp dụng giải thuật lập trình di truyền (Genetic Programming) trên khung thư viện DEAP.
  - Thuật toán tự động tìm kiếm đường ống (pipeline) xử lý học máy tối ưu nhất mà không cần can thiệp thủ công.
  - TPOT tự động chọn mô hình Rừng ngẫu nhiên (Random Forest - RF) làm thuật toán hồi quy tối ưu toàn cục.

#### 2.2.2 Đánh giá định lượng hiệu năng trên tập huấn luyện và kiểm thử
- Bảng so sánh hiệu năng chi tiết giữa các mô hình học máy:

| Loại mô hình | Tập huấn luyện: RMSE (mg/L) | Tập huấn luyện: MAE (mg/L) | Tập huấn luyện: $R^2$ | Tập kiểm thử: RMSE (mg/L) | Tập kiểm thử: MAE (mg/L) | Tập kiểm thử: $R^2$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **AutoML: RF** | **0.07** | **0.02** | **1.00** | **0.89** | **0.47** | **0.96** |
| **GBT** | 1.06 | 0.74 | 0.96 | 1.41 | 0.97 | 0.91 |
| **LR** | 1.68 | 1.21 | 0.89 | 1.81 | 1.34 | 0.84 |
| **DT** | 0.00 | 0.00 | 1.00 | 2.07 | 0.66 | 0.80 |
| **KNN** | 2.90 | 1.91 | 0.68 | 3.46 | 2.55 | 0.43 |
| **SVR** | 4.81 | 2.85 | 0.13 | 4.45 | 2.89 | 0.06 |

- Hiệu năng xuất sắc của mô hình AutoML RF:
  - Trên tập huấn luyện: Mô hình đạt $\text{RMSE} = 0.07\text{ mg/L}$, $\text{MAE} = 0.02\text{ mg/L}$ và hệ số xác định $R^2 = 1.00$.
  - Trên tập kiểm thử độc lập: Mô hình đạt $\text{RMSE} = 0.89\text{ mg/L}$ (kết quả kiểm định chéo đạt $0.95 \pm 0.11\text{ mg/L}$), $\text{MAE} = 0.47\text{ mg/L}$ ($0.47 \pm 0.83\text{ mg/L}$) và $R^2 = 0.96$.
  - Mô hình RF vượt trội hơn toàn bộ các thuật toán đối chuẩn còn lại trên mọi tiêu chuẩn sai số.

#### 2.2.3 Phân tích nguyên nhân chênh lệch hiệu năng và so sánh với nghiên cứu tiền nhiệm
- Cơ chế vượt trội của mô hình học kết hợp trong AutoML:
  - Giải thuật di truyền TPOT ưu tiên lựa chọn các cấu trúc tổ hợp cây (Ensemble Learning).
  - Mô hình tổ hợp thể hiện ưu thế vượt trội trên các bộ dữ liệu dạng bảng có kích thước vừa và nhỏ ($N = 1339$).
  - Thuật toán cân bằng hoàn hảo giữa độ chệch và phương sai (bias-variance balance), ngăn ngừa hiện tượng quá khớp dữ liệu.
- Phân tích nguyên nhân quá khớp của cây quyết định (DT):
  - Mô hình DT đạt kết quả tuyệt đối trên tập huấn luyện ($\text{RMSE} = 0.00\text{ mg/L}$, $R^2 = 1.00$).
  - Hiệu năng suy giảm mạnh trên tập kiểm thử ($\text{RMSE} = 2.07\text{ mg/L}$, $R^2 = 0.80$).
  - Thuật toán DT đơn lẻ ghi nhớ các điểm ngoại lai và nhiễu ngẫu nhiên thay vì học quy luật tổng quát của dữ liệu.
- Phân tích nguyên nhân thất bại của mô hình hồi quy véctơ hỗ trợ (SVR):
  - Mô hình SVR thể hiện sai số lớn nhất với $R^2 = 0.13$ ở tập huấn luyện và $R^2 = 0.06$ ở tập kiểm thử.
  - Thuật toán SVR cực kỳ nhạy cảm với việc tinh chỉnh bộ ba siêu tham số $C$, $\epsilon$ và $\gamma$.
  - Không gian quan hệ chất lượng nước chứa nhiều biến đổi phi tuyến đột ngột khiến siêu phẳng SVR không hội tụ tối ưu.
- So sánh đối chuẩn với mô hình CNN-GRU của Kim và cộng sự:
  - Nghiên cứu của Kim et al. ứng dụng mạng tích chập kết hợp cổng hồi quy (CNN-GRU) để dự đoán liều lượng PAC.
  - Mô hình CNN-GRU đạt hệ số $R^2 > 0.8$ trên cả hai tập dữ liệu huấn luyện và kiểm thử.
  - Hạn chế: Kiến trúc học sâu chuỗi thời gian không gian đưa vào độ phức tạp thừa thãi và gây dư thừa thông tin.
  - Các nhân tố chi phối chính của phản ứng keo tụ là các thuộc tính lý hóa tĩnh (pH, độ đục, nhiệt độ, độ dẫn điện) thay vì quy luật trễ thời gian.
- So sánh đối chuẩn với mô hình học sâu của Lin và cộng sự:
  - Nghiên cứu của Lin et al. ứng dụng mô hình học sâu (Deep Learning) để dự đoán chất keo tụ PAC và muối sulfate.
  - Mô hình của Lin et al. đạt sai số $\text{RMSE} = 3.55\text{ mg/L}$ và hệ số $R^2 = 0.94$.
  - Mô hình AutoML RF trong nghiên cứu này giảm mạnh sai số dự đoán ($\text{RMSE} = 0.89\text{ mg/L}$ so với $3.55\text{ mg/L}$) và nâng cao độ chính xác ($R^2 = 0.96$ so với $0.94$).

#### 2.2.4 Phân bố mật độ sai số và độ ổn định của mô hình AutoML RF
- Biểu đồ khớp dữ liệu thực nghiệm:
  - Đường dự báo của mô hình bám sát gần như trùng khớp với đường biến thiên thực tế của mẫu quan trắc.
  - Mô hình phản ứng nhạy bén trước các bước nhảy liều lượng châm đột biến mà không bị trễ pha.
- Biểu đồ mật độ phân tán (Scatter Density Plot):
  - Các cặp giá trị liều châm PACl thực tế và dự đoán phân bố dày đặc tập trung dọc theo đường chéo lý tưởng $y = x$.
  - Độ lệch hệ thống tiềm ẩn (systematic bias) của mô hình duy trì ở mức tối thiểu.
- Phân tích biên độ sai số kiểm thử:
  - Nồng độ chất rắn lơ lửng, hạt keo và tạp chất trong nguồn nước thô nhìn chung ở mức thấp.
  - Mức độ dao động của $\text{pH-RW}$ và $\text{NTU-RW}$ diễn ra rất hẹp giúp hệ thống keo tụ ổn định.
  - Đại đa số sai số tuyệt đối ghi nhận trên tập kiểm thử đều nằm dưới ngưỡng $20\text{ mg/L}$.

#### 2.2.5 Tối ưu hóa liều lượng châm PACl theo nguồn nước và hiệu quả kinh tế
- Hạn chế của phương pháp định liều thủ công:
  - Người vận hành châm hóa chất theo kinh nghiệm cảm tính thường châm dư (over-dosing) để đảm bảo an toàn.
  - Thao tác thủ công gây lãng phí hóa chất nghiêm trọng và làm tăng nồng độ ion nhôm dư trong nước sinh hoạt.
- Thiết lập ngưỡng chất lượng nước sạch mục tiêu cho mô hình RF:
  - Nguồn nước mặt Sông Dương Tử (Yangtze River): Đặt chuẩn $\text{NTU-TW} = 0.2\text{ NTU}$, $\text{CODMn-TW} = 1.2\text{ mg/L}$, $\text{pH-TW} = 8.0$, $\text{NH}_3\text{-N-TW} = 0.01\text{ mg/L}$.
  - Nguồn nước mặt Sông Loan Hà (Luanhe River): Đặt chuẩn $\text{NTU-TW} = 0.3\text{ NTU}$, $\text{CODMn-TW} = 1.5\text{ mg/L}$, $\text{pH-TW} = 8.0$, $\text{NH}_3\text{-N-TW} = 0.01\text{ mg/L}$.
- Hiệu quả tối ưu hóa đối với nguồn nước Sông Dương Tử:
  - Chu kỳ khai thác: Kéo dài liên tục 9 tháng mỗi năm, từ tháng 3 đến tháng 11.
  - Đặc tính vận hành: Liều châm thủ công dao động từ $8$ đến $30\text{ mg/L}$.
  - Cơ chế keo tụ: Mùa xuân và mùa hè nhiệt độ cao làm PACl thủy phân nhanh. Vi tảo tích điện âm phát triển mạnh làm tăng nhu cầu hóa chất trung hòa điện tích.
  - Kết quả kiểm soát: Mô hình triệt tiêu lượng châm dư thừa theo kinh nghiệm, giảm mức tiêu hao $222\text{ kg PACl/ngày}$.
  - Giá trị kinh tế: Tiết kiệm chi phí hóa chất $180.7\text{ Nhân dân tệ (RMB)/ngày}$, tương đương giảm $11\%$ tổng lượng tiêu thụ PACl hàng năm của nguồn nước này.
- Hiệu quả tối ưu hóa đối với nguồn nước Sông Loan Hà:
  - Chu kỳ khai thác: Kéo dài 3 tháng mùa đông lạnh, từ tháng 12 đến tháng 2 năm sau.
  - Đặc tính vận hành: Liều châm thủ công dao động ở mức rất cao, từ $10$ đến $35\text{ mg/L}$.
  - Cơ chế keo tụ: Nhiệt độ nước mùa đông hạ thấp làm phản ứng thủy phân nhôm kém hoàn toàn. Bông cặn nhỏ và xốp nhẹ, kết hợp nguy cơ ô nhiễm nguồn phân bón nông nghiệp.
  - Kết quả kiểm soát: Mô hình triệt tiêu hiện tượng châm bù quá mức do tâm lý lo sợ nhiệt độ thấp, giảm mức tiêu hao $225\text{ kg PACl/ngày}$.
  - Giá trị kinh tế: Tiết kiệm chi phí hóa chất $183.2\text{ Nhân dân tệ (RMB)/ngày}$, tương đương giảm $8\%$ tổng lượng tiêu thụ PACl hàng năm của nguồn nước này.
- Lợi ích tổng hợp trên toàn nhà máy xử lý nước cấp:
  - Tỷ trọng phân bổ khai thác: Nguồn Sông Dương Tử chiếm $75\%$ thời gian ($9/12$ tháng). Nguồn Sông Loan Hà chiếm $25\%$ thời gian ($3/12$ tháng).
  - Tỷ lệ tiết kiệm bình quân gia quyền: Mô hình AutoML RF cắt giảm chính xác $10.25\%$ tổng khối lượng hóa chất keo tụ PACl cho toàn nhà máy trong một năm vận hành:
    $$\Delta_{\text{PACl}} = \left(11\% \times \frac{9}{12}\right) + \left(8\% \times \frac{3}{12}\right) = 8.25\% + 2.00\% = 10.25\%$$
  - Ý nghĩa kỹ thuật và môi trường: Mô hình đảm bảo chất lượng nước thành phẩm đạt chuẩn an toàn nghiêm ngặt. Hệ thống hạ thấp chi phí vận hành và giảm thiểu tác động xả thải hóa chất ra môi trường.

---

## 3. Giải thích mô hình bằng phương pháp SHAP và Cơ chế keo tụ

### 3.1 Phân tích tầm quan trọng và chiều hướng tác động của đặc trưng toàn cục

#### 3.1.1 Thứ bậc tầm quan trọng đặc trưng toàn cục (Global Feature Importance)
- Thứ tự xếp hạng tổng thể: Trục tung biểu diễn các đặc trưng xếp theo thứ tự giảm dần của giá trị SHAP trung bình tuyệt đối ($\text{mean}(|\text{SHAP value}|)$). Thứ bậc từ cao xuống thấp gồm: $\text{EC-RW} > \text{pH-TW} > \text{NH3-N-RW} > \text{CODMn-RW} > \text{T-RW} > \text{NTU-RW} > \text{WTR} > \text{NTU-TW} > \text{pH-RW}$.
- Độ lớn đóng góp dự đoán: Trục hoành biểu thị giá trị SHAP trung bình, phản ánh mức độ ảnh hưởng trung bình của từng đặc trưng lên đầu ra của mô hình. Giá trị SHAP càng lớn chứng tỏ đặc trưng đóng góp càng nhiều vào kết quả dự đoán.
- Nguyên lý vận hành nhà máy nước: Mô hình xây dựng dựa trên dữ liệu quan trắc thực tế của nhà máy xử lý nước. Quy trình vận hành tuân thủ nguyên lý liên tục điều chỉnh liều lượng hóa chất theo phẩm chất nước thô để giữ nước sạch ổn định.
- Mối liên hệ nhân quả trực tiếp: Quan hệ giữa liều lượng hóa chất và chất lượng nước sạch mang tính nhân quả trực tiếp. Tuy nhiên, khi liều lượng vượt quá một ngưỡng nhất định, tác động biên của hóa chất lên chất lượng nước sạch hầu như không đáng kể.
- Giá trị kinh nghiệm vận hành thực tiễn: Quan hệ giữa liều lượng hóa chất và chất lượng nước thô phản ánh tri thức thực nghiệm của kỹ sư vận hành. Người vận hành dựa vào kinh nghiệm và phẩm chất nước thô để đặt liều châm đạt chuẩn nước sạch.
- Phân hóa tầm quan trọng giữa nước thô và nước sạch: Nước thô biến động rất mạnh theo mùa và chế độ thủy văn. Ngược lại, chất lượng nước sạch đầu ra luôn duy trì ổn định nghiêm ngặt. Do đó, các chỉ số nước thô đóng vai trò quan trọng hơn các chỉ số nước sạch trong cấu trúc mô hình.

#### 3.1.2 Động lực học chiều hướng tác động đặc trưng (SHAP Summary Analysis)
- Cấu trúc biểu đồ tổng hợp: Mỗi điểm trên biểu đồ đại diện cho giá trị SHAP của một mẫu dữ liệu. Vị trí trên trục hoành thể hiện độ lớn và hướng tác động của giá trị SHAP.
- Mã màu biểu diễn giá trị gốc: Màu sắc thể hiện giá trị nguyên bản của đặc trưng. Màu đỏ đại diện cho giá trị thực tế cao. Màu xanh đại diện cho giá trị thực tế thấp.
- Nhóm biến thúc đẩy tăng liều châm ($\text{SHAP} > 0$): Các đặc trưng $\text{EC-RW}$, $\text{NH3-N-RW}$, $\text{CODMn-RW}$ và $\text{NTU-RW}$ phân bố điểm đỏ về phía bên phải trục $0$. Giá trị của các biến này càng cao sẽ thúc đẩy tăng liều châm PACl.
- Nhóm biến thúc đẩy giảm liều châm ($\text{SHAP} < 0$): Các đặc trưng $\text{pH-RW}$, $\text{T-RW}$ và $\text{WTR}$ thể hiện xu hướng ngược lại. Điểm đỏ phân bố về phía bên trái trục $0$. Giá trị các biến này càng cao sẽ làm giảm liều lượng chất keo tụ cần châm.
- Bản chất tác động của độ dẫn điện $\text{EC-RW}$: Giá trị $\text{EC-RW}$ cao biểu thị độ tinh khiết của nước thấp. Nguồn nước chứa nồng độ muối hòa tan, chất hữu cơ và ion kim loại cao.
- Cơ chế tác động điện tích của PACl: Cation nhôm trong PACl trung hòa điện tích bề mặt của các hạt lơ lửng và chất keo tích điện âm. Phản ứng này triệt tiêu lực đẩy tĩnh điện giữa các hạt và thúc đẩy quá trình kết tụ keo.
- Vai trò của lưu lượng xử lý nước ($\text{WTR}$): Giá trị $\text{WTR}$ cao tương ứng với giá trị SHAP thấp hơn. Điều này chỉ báo xu hướng giảm nhẹ liều lượng hóa chất tính trên một đơn vị thể tích khi trạm vận hành ở công suất cao.

### 3.2 Phân tích phụ thuộc biên và hiệu ứng ngưỡng phi tuyến của từng biến chất lượng nước

#### 3.2.1 Độ dẫn điện nước thô (EC-RW) và cơ chế nén lớp điện kép
- Ý nghĩa vật lý của $\text{EC-RW}$: Độ dẫn điện phản ánh tổng nồng độ các ion chất điện phân hòa tan trong nguồn nước thô tự nhiên.
- Dải tăng cường tuyến tính ($300\text{--}550\ \mu\text{S/cm}$): Trong khoảng từ $300\ \mu\text{S/cm}$ đến $550\ \mu\text{S/cm}$, $\text{EC-RW}$ duy trì mối quan hệ tăng cường gần như tuyến tính với liều lượng keo tụ.
- Hiệu ứng suy giảm biên ngoài khoảng tối ưu: Khi $\text{EC-RW} < 300\ \mu\text{S/cm}$ hoặc $\text{EC-RW} > 550\ \mu\text{S/cm}$, mối quan hệ chuyển sang xu hướng suy giảm biên (diminishing returns).
- Cơ chế nén lớp điện kép (Electric Double Layer Compression): Nồng độ ion chất điện giải cao làm gia tăng lực ion dung dịch. Lực ion cao nén mỏng bề dày lớp điện kép khuếch tán bao quanh các hạt keo, tạo điều kiện cho lực hút Van der Waals kéo các hạt dính kết lại với nhau.
- Tác động ức chế của pH thấp: Độ dẫn điện cao hỗ trợ nén lớp điện kép. Tuy nhiên, giá trị pH thấp sẽ ức chế quá trình hình thành kết tủa $\text{Al(OH)}_3$. Lúc này hệ thống đòi hỏi bổ sung liều châm PACl để bù trừ hiệu năng lắng.

#### 3.2.2 Hàm lượng Amoniac nước thô (NH3-N-RW) và cân bằng ion hóa
- Dạng tồn tại của Amoniac: Nitơ amoniac tồn tại đồng thời ở dạng amoniac tự do ($\text{NH}_3$) và ion amoni ($\text{NH}_4^+$). Tỷ lệ phân bố giữa hai dạng chất này chịu sự chi phối trực tiếp của giá trị pH và nhiệt độ nước.
- Khoảng tác động đồng biến tích cực ($0\text{--}0.2\ \text{mg/L}$): Trong phạm vi từ $0$ đến $0.2\ \text{mg/L}$, $\text{NH3-N-RW}$ tác động thuận chiều rõ rệt lên liều lượng châm PACl.
- Hiệu ứng bão hòa vượt ngưỡng $0.2\ \text{mg/L}$: Khi hàm lượng $\text{NH3-N-RW}$ vượt qua ngưỡng $0.2\ \text{mg/L}$, mối quan hệ đồng biến suy giảm độ dốc và đạt trạng thái bão hòa.
- Tương tác với nhiệt độ nước: Nhiệt độ cao thúc đẩy tốc độ thủy phân của chất keo tụ. Đồng thời, hàm lượng $\text{NH}_3\text{-N}$ thấp giúp giảm thiểu hiện tượng nhiễu cạnh tranh ion, cho phép kỹ sư vận hành điều chỉnh liều châm PACl chính xác theo kinh nghiệm chuyên môn.

#### 3.2.3 Nhu cầu oxy hóa học Permanganat nước thô (CODMn-RW) và cạnh tranh vị trí hoạt hóa
- Ý nghĩa chỉ số $\text{CODMn-RW}$: Chỉ số permanganat phản ánh tổng lượng chất hữu cơ tự nhiên và các hợp chất vô cơ có tính khử hiện diện trong khối nước.
- Vùng trơ dưới ngưỡng ($< 4\ \text{mg/L}$): Khi $\text{CODMn-RW} < 4\ \text{mg/L}$, giá trị SHAP duy trì gần trục $0$ và không xuất hiện tương quan rõ rệt với liều lượng hóa chất.
- Hiệu ứng ngưỡng đột biến trên $4\ \text{mg/L}$: Khi nồng độ $\text{CODMn-RW}$ vượt qua ngưỡng tới hạn $4\ \text{mg/L}$, giá trị SHAP tăng vọt theo chiều thẳng đứng.
- Cơ chế cạnh tranh vị trí hoạt hóa: Các phân tử chất hữu cơ hòa tan cạnh tranh trực tiếp vị trí hoạt hóa liên kết với ion $\text{Al}^{3+}$ và các polyme nhôm của PACl.
- Tiêu hao hóa chất do chất hữu cơ: Sự cạnh tranh vị trí hoạt hóa làm cạn kiệt lượng nhôm hữu hiệu dành cho kết tụ hạt cặn. Người vận hành bắt buộc phải tăng mạnh liều châm PACl để vô hiệu hóa lượng chất hữu cơ dư thừa này.

#### 3.2.4 Độ đục nước thô (NTU-RW) và hiện tượng nghịch đảo độ đục cực thấp
- Xu hướng đồng biến tổng thể: Thông thường, độ đục nước thô có tác động thúc đẩy dương đối với liều châm. Châm thêm lượng chất keo tụ phù hợp sẽ thúc đẩy các hạt cặn liên kết và lắng nhanh.
- Hiện tượng nghịch đảo ở độ đục cực thấp ($\text{NTU-RW} < 2\ \text{NTU}$): Khi $\text{NTU-RW}$ giảm xuống dưới $2\ \text{NTU}$, giá trị SHAP bất ngờ đảo chiều tăng lên.
- Giới hạn khuếch tán và bắt giữ cặn (Diffusion Limitations): Trong điều kiện nước có độ đục cực thấp, các hạt keo phân tán quá thưa thớt trong thể tích nước. Khoảng cách lớn làm hạn chế tần suất va chạm nhiệt và giảm khả năng bắt giữ cặn của các bông hydroxit nhôm sau thủy phân.
- Bù trừ bằng cơ chế keo tụ quét (Sweep Coagulation): Kỹ sư vận hành bắt buộc phải tăng liều châm PACl để bù đắp các giới hạn khuếch tán và đảm bảo quá trình trung hòa điện tích diễn ra triệt để. Liều châm cao tạo ra mạng lưới kết tủa hydroxit nhôm dày đặc để quét sạch các hạt cặn phân tán.
- Hiện tượng tạo màng bao bọc của chất hữu cơ: Trong nguồn nước có đồng thời $\text{CODMn}$ cao và độ đục cao, các phân tử chất hữu cơ bao bọc xung quanh các hạt keo khoáng. Lớp màng hữu cơ này tạo thành hàng rào cản trở tĩnh điện và không gian. Nhà máy cần bổ sung thêm PACl để tăng cường trung hòa điện tích và phá vỡ lớp vỏ hữu cơ bảo vệ.

#### 3.2.5 Giá trị pH nước thô (pH-RW) và tương tác tĩnh điện trong môi trường kiềm yếu
- Vùng pH kiềm yếu thuận lợi ($8.0\text{--}8.4$): Trong khoảng $\text{pH-RW}$ từ $8.0$ đến $8.4$, liều lượng chất keo tụ yêu cầu giảm dần khi giá trị pH tăng lên.
- Tương tác điện tích trái dấu tối ưu: Môi trường kiềm yếu tạo điều kiện cho các dạng thủy phân mang điện tích dương của PACl tương tác tĩnh điện mạnh mẽ với các hạt tạp chất tích điện âm.
- Hiệu năng keo tụ vượt trội: Sự chênh lệch điện tích tối ưu giúp PACl thể hiện các đặc tính keo tụ vượt trội trong môi trường kiềm nhẹ. Lượng hóa chất cần thiết để loại bỏ cặn bẩn giảm xuống mức tối thiểu.

#### 3.2.6 Nhiệt độ nước thô (T-RW) và động học nhiệt - độ nhớt môi trường
- Xu hướng tác động âm của nhiệt độ: Nhiệt độ nước thô thể hiện ảnh hưởng nghịch đảo đối với liều lượng châm PACl. Nước càng lạnh đòi hỏi liều lượng hóa chất châm vào càng lớn.
- Trở lực cơ học do độ nhớt tăng cao: Nhiệt độ nước suy giảm làm tăng độ nhớt động học của môi trường lỏng. Độ nhớt cao cản trở trực tiếp chuyển động nhiệt Brown tự do của các hạt lơ lửng trong nước.
- Kìm hãm va chạm và kết tụ bông keo: Chuyển động hạt bị kìm hãm làm giảm xác suất va chạm hiệu dụng giữa các hạt keo, gây bất lợi cho sự ổn định và phát triển của các khối bông cặn.
- Đặc tính thu nhiệt của phản ứng thủy phân: Quá trình thủy phân muối nhôm PACl là phản ứng thu nhiệt ($\Delta H > 0$). Nhiệt độ thấp làm chậm đáng kể tốc độ phản ứng thủy phân và làm chậm quá trình hình thành kết tủa $\text{Al(OH)}_3$.
- Yêu cầu bù trừ liều lượng: Người vận hành bắt buộc phải tăng cường liều châm PACl trong mùa lạnh để bù đắp sự suy giảm động học phản ứng và đạt hiệu quả keo tụ mong muốn.

#### 3.2.7 Giá trị pH nước sạch (pH-TW) và phản ứng giải phóng ion H+
- Dải phân bố tập trung hẹp ($7.6\text{--}7.8$): Các giá trị $\text{pH-TW}$ của nước sau xử lý tập trung chủ yếu trong một dải hẹp từ $7.6$ đến $7.8$.
- Tương quan tuyến tính âm rõ rệt: Giữa $\text{pH-TW}$ và lượng chất keo tụ châm vào tồn tại mối tương quan tuyến tính nghịch đảo rất mạnh mẽ.
- Cơ chế giải phóng ion $\text{H}^+$: Phản ứng thủy phân của PACl giải phóng các ion $\text{H}^+$ vào nguồn nước:
  $$\text{Al}^{3+} + 3\text{H}_2\text{O} \rightleftharpoons \text{Al(OH)}_3\downarrow + 3\text{H}^+$$
  Sự gia tăng ion $\text{H}^+$ tự do trung hòa bớt độ kiềm của nước và làm giảm trực tiếp giá trị pH của nước sạch đầu ra.

#### 3.2.8 Độ đục nước sạch (NTU-TW) và lưu lượng xử lý nước (WTR)
- Thiếu vắng quan hệ tuyến tính của $\text{NTU-TW}$: Kết quả quan sát không ghi nhận bất kỳ mối liên hệ tuyến tính rõ rệt nào giữa liều châm PACl và độ đục nước sạch $\text{NTU-TW}$.
- Cơ chế kiểm soát vận hành thực tế: Giá trị $\text{NTU-TW}$ chịu tác động đồng thời của chất lượng nước thô và liều châm hóa chất. Khi $\text{NTU-RW}$ tăng cao, người vận hành chủ động tăng liều PACl để giữ $\text{NTU-TW}$ ổn định đạt chuẩn cấp nước.
- Biên độ biến động tối thiểu của nước sạch: Nước sạch xuất xưởng từ nhà máy luôn duy trì độ đục ở mức rất thấp và ổn định với phương sai cực nhỏ. Do đó, $\text{NTU-TW}$ có mức độ ảnh hưởng rất thấp đến việc dự đoán liều lượng.
- Đặc trưng lưu lượng nước xử lý ($\text{WTR}$): Đại lượng $\text{WTR}$ nằm ở vị trí thứ 7 về tầm quan trọng. Giá trị $\text{WTR}$ tăng gắn liền với giá trị SHAP âm nhẹ, phản ánh hiệu ứng tối ưu hóa thủy lực khi lưu lượng nước qua trạm xử lý ổn định ở mức cao.

### 3.3 Cơ chế keo tụ nâng cao và hiện tượng bảo vệ keo (Colloidal Protection)

#### 3.3.1 Trung hòa điện tích và cầu nối hấp phụ của PACl
- Hai cơ chế phản ứng cốt lõi: Hiệu quả xử lý của chất keo tụ Polyaluminum Chloride (PACl) phụ thuộc chủ yếu vào cơ chế trung hòa điện tích (charge neutralization) và cầu nối hấp phụ (adsorption bridging).
- Trung hòa điện tích bề mặt hạt keo: Khi hòa tan vào nước với liều lượng tối ưu, PACl nhanh chóng thủy phân thành các ion polyme nhôm mang điện tích dương cao. Các ion này hấp phụ lên bề mặt các hạt keo mang điện tích âm, đưa điện thế bề mặt về trạng thái trung hòa.
- Cầu nối hấp phụ tạo bông cặn lớn: Các chuỗi polyme nhôm mạch dài hoạt động như những cầu nối hóa lý liên kết các vi hạt keo riêng lẻ lại với nhau. Quá trình tạo cầu nối hình thành nên các khối bông cặn kích thước lớn có trọng lượng riêng cao và dễ dàng lắng đọng.

#### 3.3.2 Hiện tượng bảo vệ keo khi châm thừa hóa chất và suy giảm hiệu suất
- Hiện tượng bảo vệ keo (Colloidal Protection): Việc châm hóa chất PACl vượt quá ngưỡng bão hòa sẽ kích hoạt hiện tượng bảo vệ keo, làm suy giảm nghiêm trọng hiệu quả xử lý.
- Hấp phụ quá mức các ion dương: Lượng ion nhôm hydroxit tích điện dương dư thừa tiếp tục bám dính dày đặc lên bề mặt các hạt keo đã được trung hòa điện tích.
- Hiện tượng đảo dấu điện thế bề mặt: Sự tích tụ ion dương quá mức dẫn đến hiện tượng đảo dấu điện tích bề mặt hạt keo từ âm sang dương ($\zeta > 0$).
- Biến đổi tính chất bề mặt từ kỵ nước thành ưa nước: Các hạt keo vốn có tính kỵ nước (hydrophobic) bị chuyển hóa thành các hạt keo ưa nước (hydrophilic) do lớp vỏ hydrat hóa bao bọc xung quanh.
- Hiện tượng tái ổn định keo (Restabilization): Lực đẩy tĩnh điện dương giữa các hạt keo tái xuất hiện và ngăn cản quá trình kết tụ. Các hạt keo bị tái ổn định và phân tán trở lại vào trong nước, làm giảm khả năng lắng đọng của bông cặn và kéo tụt hiệu quả khử độ đục của bể lắng.

#### 3.3.3 Rủi ro nồng độ nhôm dư hòa tan đối với an toàn cấp nước
- Nguy cơ từ việc châm thừa để chỉnh pH: Việc châm dư hóa chất PACl nhằm hạ thấp pH nước sạch đạt chuẩn sẽ gây hiện tượng tái ổn định keo và làm giảm hiệu suất keo tụ.
- Gia tăng nồng độ nhôm dư hòa tan: Châm hóa chất quá liều làm tăng lượng nhôm hòa tan tồn dư trong nước sau lắng, đe dọa trực tiếp đến tính an toàn và chất lượng nước sạch cung cấp cho người tiêu dùng.
- Tác hại của nhôm hòa tan đối với sức khỏe: Hàm lượng ion nhôm vượt ngưỡng cho phép có nguy cơ gây tích tụ sinh học và ảnh hưởng xấu đến hệ thần kinh con người.
- Gia tăng lượng bùn nhôm phát thải: Dư thừa PACl tạo ra lượng bùn hydroxit nhôm lớn. Khối lượng bùn thải tăng cao gây áp lực chi phí cho công tác xử lý và lưu trữ bùn thải nguy hại tại trạm xử lý.

### 3.4 Đánh giá độ tin cậy mô hình AutoML và ưu thế vượt trội của phương pháp SHAP

#### 3.4.1 Kiểm định nguy cơ quá khớp (Overfitting) trong chuỗi TPOT
- Rủi ro lý thuyết của hệ thống AutoML: Hệ thống AutoML (TPOT) có nguy cơ đối mặt với hiện tượng quá khớp (overfitting) trong quá trình tự động tìm kiếm đường ống tối ưu và điều chỉnh siêu tham số.
- Đánh giá thực nghiệm qua hệ số xác định $R^2$: Mặc dù mô hình đạt hệ số xác định hoàn hảo $R^2 = 1.00$ trên tập huấn luyện (training set), kết quả kiểm định chéo lặp lại và kiểm tra trên tập kiểm tra độc lập (testing set) vẫn duy trì giá trị rất cao $R^2 = 0.96$.
- Tính khái quát hóa của mô hình tối ưu: Sự thống nhất cao giữa kết quả kiểm định chéo và tập kiểm tra độc lập khẳng định mô hình TPOT được kiểm soát tốt và không xảy ra hiện tượng quá khớp dữ liệu.

#### 3.4.2 Năng lực bóc tách tương tác phi tuyến và hành vi ngưỡng của Tree SHAP
- Giới hạn của các mô hình tuyến tính cổ điển: Các phương pháp phân tích thống kê tuyến tính truyền thống không thể nắm bắt được các quy luật tác động phi tuyến phức tạp trong quy trình keo tụ.
- Nhận diện chính xác hành vi phản ứng ngưỡng: Phương pháp SHAP đã bóc tách thành công hành vi phản ứng ngưỡng của các thông số then chốt, tiêu biểu là bước nhảy tại mốc $4\ \text{mg/L}$ của $\text{CODMn-RW}$ và ngưỡng $2\ \text{NTU}$ của $\text{NTU-RW}$.
- Nâng cao tính giải thích và độ tin cậy: Tree SHAP vượt qua ranh giới thống kê tuyến tính, cung cấp cơ sở khoa học vững chắc giúp kỹ sư hiểu rõ cơ chế vận hành nội tại của mô hình học máy.

### 3.5 Giải thích cục bộ cho các mẫu thực nghiệm vận hành điển hình (Local Explanations)

#### 3.5.1 Mẫu mùa đông nguồn nước Sông Loan Hà: Điều kiện liều cao cực trị
- Thời điểm thu mẫu và nguồn nước thô: Mẫu thử nghiệm được thu thập vào tháng 2 trong điều kiện mùa đông lạnh giá, với nguồn nước thô khai thác trực tiếp từ Sông Loan Hà (Luanhe River).
- Mức liều châm dự đoán vượt ngưỡng: Mô hình dự đoán mức liều châm PACl lên tới $34.9\ \text{mg/L}$, cao hơn rất nhiều so với giá trị kỳ vọng trung bình của tập kiểm tra ($14.5\ \text{mg/L}$).
- Điều kiện chất lượng nước thô mùa đông:
  - Nhiệt độ nước thô rất thấp: $\text{T-RW} = 3.8\ ^\circ\text{C}$ (gây cản trở động học thủy phân).
  - Nhu cầu oxy hóa học cao vượt ngưỡng: $\text{CODMn-RW} = 5.46\ \text{mg/L}$ (vượt xa ngưỡng tới hạn $4\ \text{mg/L}$).
  - Độ dẫn điện rất cao: $\text{EC-RW} = 600.6\ \mu\text{S/cm}$ (vượt ngưỡng bão hòa $550\ \mu\text{S/cm}$).
  - Hàm lượng amoniac cao: $\text{NH3-N-RW} = 0.36\ \text{mg/L}$ (vượt ngưỡng tác động mạnh $0.2\ \text{mg/L}$).
  - Độ đục nước thô ở mức trung bình: $\text{NTU-RW} = 7.19\ \text{NTU}$.

#### 3.5.2 Phân tích Waterfall Plot và Decision Plot mẫu mùa đông
- Phân tích biểu đồ thác nước: Biểu đồ thể hiện chi tiết quá trình dịch chuyển từ giá trị kỳ vọng cơ sở $\mathbb{E}[f(x)] = 14.5\ \text{mg/L}$ lên giá trị dự đoán cuối cùng $f(x) = 34.9\ \text{mg/L}$.
- Tác nhân chi phối hàng đầu $\text{CODMn-RW}$: Nồng độ $\text{CODMn-RW} = 5.46\ \text{mg/L}$ vượt ngưỡng $4\ \text{mg/L}$ tạo ra bước nhảy SHAP dương lớn nhất, đóng vai trò nhân tố chủ chốt kéo tăng mạnh liều lượng dự đoán.
- Đóng góp cộng dồn của các đặc trưng đồng biến: Các biến $\text{EC-RW}$, $\text{NTU-RW}$ và $\text{NH3-N-RW}$ đều duy trì giá trị $\text{SHAP} > 0$, hiệp đồng đẩy mức liều châm lên cao.
- Đóng góp không đáng kể của pH và lưu lượng: Mức độ đóng góp của hai đặc trưng $\text{pH-RW}$ và $\text{WTR}$ đối với mẫu này gần như bằng $0$.
- Phân tích biểu đồ quyết định: Biểu đồ biểu diễn trực quan quỹ đạo tích lũy của từng đặc trưng vượt qua mức trung bình $14.5\ \text{mg/L}$ để đạt giá trị xuất ra $34.9\ \text{mg/L}$.
- Tính hợp lý theo tri thức chuyên gia: Dựa trên đánh giá tổng thể về chất lượng nước thô khắc nghiệt mùa đông, quyết định tăng vọt liều châm PACl hoàn toàn phù hợp với kinh nghiệm vận hành thực tiễn của nhà máy.

#### 3.5.3 Mẫu mùa hè nguồn nước Sông Dương Tử: Điều kiện liều thấp tối ưu
- Thời điểm thu mẫu và nguồn nước thô: Mẫu thử nghiệm được thu thập vào tháng 5 trong điều kiện mùa hè ấm áp, với nguồn nước thô khai thác từ Sông Dương Tử (Yangtze River).
- Mức liều châm dự đoán dưới trung bình: Mô hình dự đoán mức liều châm PACl chỉ đạt $8.57\ \text{mg/L}$, thấp hơn rõ rệt so với giá trị kỳ vọng trung bình ($14.5\ \text{mg/L}$).
- Điều kiện chất lượng nước thuận lợi mùa hè:
  - Nhiệt độ nước thô ấm áp: $\text{T-RW} = 22.34\ ^\circ\text{C}$ (nhiệt độ thuận lợi cho phản ứng thủy phân).
  - Độ dẫn điện nước thô thấp: $\text{EC-RW} = 290.2\ \mu\text{S/cm}$ (dưới ngưỡng tối thiểu $300\ \mu\text{S/cm}$).
  - Hàm lượng chất hữu cơ rất thấp: $\text{CODMn-RW} = 2.6\ \text{mg/L}$ (thấp hơn nhiều so với ngưỡng phản ứng $4\ \text{mg/L}$).
  - Giá trị pH nước thô kiềm nhẹ: $\text{pH-RW} = 8.15$ (môi trường kiềm tối ưu cho PACl).
  - Giá trị pH nước sạch sau xử lý: $\text{pH-TW} = 7.906$.

#### 3.5.4 Phân tích Waterfall Plot và Decision Plot mẫu mùa hè
- Phân tích biểu đồ thác nước: Biểu đồ minh họa bước dịch chuyển làm sụt giảm liều châm từ giá trị kỳ vọng $14.5\ \text{mg/L}$ xuống mức $8.57\ \text{mg/L}$.
- Vai trò kéo giảm chi phối của $\text{pH-TW}$: Đặc trưng $\text{pH-TW} = 7.906$ tạo ra tác động tiêu cực mạnh nhất lên liều lượng dự đoán. Mức châm PACl thấp sẽ bảo đảm không giải phóng quá nhiều ion $\text{H}^+$, duy trì pH nước sạch ở mức cao.
- Sự đồng thuận kéo giảm liều của các yếu tố nước thô: Các đặc trưng $\text{T-RW} = 22.34\ ^\circ\text{C}$, $\text{EC-RW} = 290.2\ \mu\text{S/cm}$ và $\text{CODMn-RW} = 2.6\ \text{mg/L}$ đều có giá trị SHAP mang dấu âm đồng nhất.
- Đóng góp mờ nhạt của amoniac và lưu lượng: Sự đóng góp của $\text{NH3-N-RW}$ và $\text{WTR}$ vào sai khác dự đoán không đáng kể.
- Phân tích biểu đồ quyết định: Biểu đồ minh họa chi tiết cách thức các đặc trưng đồng loạt bẻ lái dự đoán dịch chuyển về phía dưới mức trung bình $14.5\ \text{mg/L}$, ấn định kết quả tại $8.57\ \text{mg/L}$.
- Phù hợp kinh nghiệm vận hành thực tiễn: Khi chất lượng nước thô sạch, nhiệt độ ấm và ít chất hữu cơ, quyết định chủ động cắt giảm liều lượng châm PACl xuống dưới mức trung bình là hoàn toàn chính xác và khoa học.

### 3.6 Hàm ý kỹ thuật vận hành và định hướng công nghệ keo tụ bền vững

#### 3.6.1 Hỗ trợ quyết định vận hành chính xác và tiết giảm hóa chất tại DWTP
- Tối ưu hóa kiểm soát liều châm: Mô hình xây dựng trong nghiên cứu này tối ưu hóa việc định lượng hóa chất keo tụ, cho phép châm hóa chất chính xác tại các nhà máy xử lý nước.
- Hạn chế lạm dụng hóa chất: Kiểm soát tự động giúp giảm thiểu đáng kể tình trạng lạm dụng hóa chất quá liều trong quá trình keo tụ cặn bẩn.
- Nâng cao tính minh bạch cho hệ thống: Việc ứng dụng phương pháp giải thích SHAP giúp vạch rõ các yếu tố cốt lõi và quy luật tác động chi phối mức tiêu hao chất keo tụ.
- Hỗ trợ kỹ sư ra quyết định chuẩn xác: Các đồ thị giải thích trực quan giúp nhân viên vận hành nhà máy đưa ra các quyết định điều hành khoa học và hợp lý hơn, vừa tránh châm dư hóa chất vừa bảo đảm chất lượng nước sạch đầu ra.

#### 3.6.2 Tích hợp công nghệ tiền xử lý và chất keo tụ sinh học thân thiện môi trường
- Giảm thiểu tác động môi trường trong thực tế: Để giảm thiểu các tác động tiêu cực đến môi trường do việc sử dụng hóa chất keo tụ, nhà máy cần tiếp tục cải tiến các giải pháp công nghệ bổ trợ.
- Tích hợp các quy trình tiền xử lý: Kết hợp mô hình dự đoán liều lượng với các quy trình tiền xử lý như tiền clo hóa (pre-chlorination) hoặc hấp phụ bằng than hoạt tính để giảm thiểu nhu cầu tiêu thụ chất keo tụ.
- Phát triển chất keo tụ sinh học xanh: Đẩy mạnh nghiên cứu và ứng dụng các chất keo tụ sinh học có nguồn gốc tự nhiên và bền vững (như chitosan, chất tạo bông vi sinh vật).
- Khai thác công nghệ quang xúc tác tiên tiến: Ứng dụng công nghệ quang xúc tác để phân hủy chất ô nhiễm hữu cơ trước khi vào bể keo tụ.
- Giảm thiểu phụ thuộc tài nguyên và rủi ro bùn thải: Ứng dụng công nghệ mới giúp giảm sự phụ thuộc vào các nguồn tài nguyên không tái tạo, đồng thời triệt tiêu các rủi ro môi trường do cặn hóa chất và sản phẩm phụ (như bùn hydroxit nhôm) gây ra.

---

## 4. Kết luận và Định hướng ứng dụng thực tế

### 4.1 Kết luận nghiên cứu cốt lõi

#### 4.1.1 Hiệu năng vượt trội và tính thích ứng của mô hình AutoML RF
- Độ chính xác dự báo tổng thể: Mô hình Rừng ngẫu nhiên (RF) do khung TPOT AutoML tối ưu đạt hệ số xác định $R^2 = 0.96$ trên tập kiểm thử độc lập gồm 268 mẫu.
- Chỉ số sai số thực nghiệm mức thấp: Mô hình ghi nhận sai số toàn phương trung bình $\text{RMSE} = 0.89\text{ mg/L}$ và sai số tuyệt đối trung bình $\text{MAE} = 0.47\text{ mg/L}$.
- Ưu thế chu kỳ phát triển thuật toán: Khung AutoML tự động hóa hoàn toàn các khâu tiền xử lý, chọn mô hình và tinh chỉnh siêu tham số. Quy trình này rút ngắn đáng kể thời gian phát triển so với các phương pháp lập trình thủ công truyền thống.
- Vượt trội so với các thuật toán nền tảng: Mô hình RF tối ưu vượt xa hiệu năng của Cây tăng cường độ dốc (GBT với $R^2 = 0.91$), Hồi quy tuyến tính (LR với $R^2 = 0.84$), Cây quyết định (DT với $R^2 = 0.80$), K láng giềng gần nhất (KNN với $R^2 = 0.43$) và Hồi quy vector hỗ trợ (SVR với $R^2 = 0.06$).
- Công cụ điều khiển định lượng tin cậy: Kết quả nghiên cứu chứng minh mô hình RF là công cụ tính toán hiệu quả cao để dự báo và tự động hóa quy trình châm chất keo tụ trong các nhà máy xử lý nước cấp (DWTP).

#### 4.1.2 Minh bạch hóa cơ chế keo tụ thông qua lý thuyết SHAP
- Thứ tự phân cấp tầm quan trọng đặc trưng: Khi độ đục nước thô ($\text{NTU-RW}$) duy trì ở mức thấp và ổn định, độ dẫn điện ($\text{EC-RW}$) trở thành yếu tố chi phối mạnh nhất đến liều lượng châm PACl.
- Trật tự ảnh hưởng của các thông số kế tiếp: Mức độ ảnh hưởng giảm dần theo thứ tự từ nồng độ amoniac ($\text{NH}_3\text{-N-RW}$), nhu cầu oxy hóa học pemanganat ($\text{CODMn-RW}$), nhiệt độ nước thô ($\text{T-RW}$) đến lưu lượng nước xử lý ($\text{WTR}$).
- Cơ chế giải thích cục bộ trực quan: Biểu đồ thác nước (waterfall plot) và biểu đồ quyết định (decision plot) định lượng chính xác mức độ tăng hoặc giảm liều lượng châm chất keo tụ so với giá trị kỳ vọng nền của từng mẫu kiểm thử.
- Mối liên hệ hóa lý của chỉ số pH: Độ pH nước sau keo tụ ($\text{pH-TW}$) có mối liên hệ nghịch đảo tuyến tính với liều lượng keo tụ do ion $\text{Al}^{3+}$ thủy phân giải phóng các ion $\text{H}^+$.
- Nhận diện ngưỡng đáp ứng bão hòa: Phân tích phụ thuộc biên SHAP xác định khoảng biến thiên nhạy cảm của $\text{EC-RW}$ nằm trong vùng $300\text{ đến }550\ \mu\text{S/cm}$ và điểm bùng phát nhu cầu hóa chất khi $\text{CODMn-RW}$ vượt ngưỡng $4\text{ mg/L}$.

#### 4.1.3 Hiệu quả kinh tế, năng lượng và tối ưu hóa vận hành
- Tiết kiệm hóa chất nguồn Sông Dương Tử: Mô hình giúp cắt giảm $222\text{ kg PACl/ngày}$, tương đương giảm $11\%$ tổng lượng chất keo tụ tiêu thụ và tiết kiệm $180.7\text{ Nhân dân tệ/ngày}$ chi phí vận hành.
- Tiết kiệm hóa chất nguồn Sông Loan Hà: Mô hình giúp cắt giảm $225\text{ kg PACl/ngày}$, tương ứng giảm $8\%$ hóa chất châm vào và tiết kiệm $183.2\text{ Nhân dân tệ/ngày}$ chi phí thực tế.
- Tỷ lệ tiết kiệm bình quân gia quyền cả năm: Tính theo chu kỳ cấp nước luân phiên thực tế (Sông Dương Tử chiếm phần lớn thời gian, Sông Loan Hà cấp vào mùa đông), nhà máy giảm $10.25\%$ lượng hóa chất PACl hàng năm.
- Giảm thiểu rủi ro định liều quá mức: Mô hình loại bỏ sai số do thao tác theo thói quen của công nhân vận hành, ngăn ngừa triệt để hiện tượng hạt keo bị tái ổn định điện tích (colloidal restabilization).
- Đảm bảo chất lượng nước sau xử lý: Độ đục nước đầu ra ($\text{NTU-TW}$) luôn duy trì ổn định dưới ngưỡng tiêu chuẩn quốc gia, khẳng định việc giảm liều lượng không gây tổn hại đến chất lượng nước thành phẩm.

### 4.2 Khuyến nghị kỹ thuật xanh và giải pháp giảm thiểu tác động môi trường

#### 4.2.1 Tích hợp liên hoàn quy trình tiền xử lý và hấp phụ nâng cao
- Kết hợp quy trình tiền clo hóa (pre-chlorination): Tích hợp thuật toán dự báo với khâu châm clo sơ bộ giúp oxy hóa các hợp chất hữu cơ hòa tan phức tạp và phá vỡ liên kết chelate kim loại - hữu cơ.
- Hấp phụ than hoạt tính dạng hạt hoặc bột: Bố trí công đoạn hấp phụ than hoạt tính trước bể keo tụ để hấp phụ chọn lọc các tiền chất hữu cơ khó phân hủy và các chất gây mùi.
- Hiệu ứng cộng hưởng làm suy giảm nhu cầu keo tụ: Quá trình oxy hóa sơ bộ kết hợp hấp phụ than giúp hạ thấp nồng độ $\text{CODMn-RW}$, tạo điều kiện giảm mạnh liều lượng chất keo tụ vô cơ PACl châm vào hệ thống.
- Tối ưu hóa điều khiển đa quy trình: Các nhà máy nên xây dựng hệ thống điều khiển liên hoàn giữa liều lượng chất oxy hóa, vật liệu hấp phụ và hóa chất keo tụ nhằm tối đa hóa hiệu quả loại bỏ chất ô nhiễm hữu cơ vi lượng.

#### 4.2.2 Phát triển chất keo tụ sinh học bền vững và công nghệ xúc tác mới
- Nghiên cứu chất tạo bông sinh học có nguồn gốc tự nhiên: Ứng dụng chitosan, tinh bột biến tính hoặc chất tạo bông vi sinh vật để thay thế một phần hoặc toàn bộ chất keo tụ gốc nhôm.
- Cơ chế keo tụ bổ trợ của phân tử chitosan: Cấu trúc phân tử mang mật độ điện tích dương cao và chuỗi mạch polymer dài của chitosan kích hoạt cơ chế bắc cầu hạt keo hiệu quả, tăng kích thước bông cặn và tốc độ lắng trong điều kiện nước lạnh.
- Giảm phụ thuộc tài nguyên khoáng sản không tái tạo: Khai thác chất keo tụ hữu cơ sinh học giúp giảm sự lệ thuộc vào quặng bauxite và giảm lượng hóa chất vô cơ tiêu thụ trong ngành cấp nước.
- Ứng dụng công nghệ quang xúc tác tiên tiến: Tích hợp vật liệu quang xúc tác mới như composite aerogel MIL-53(Fe)/graphene hoặc cấu trúc dị thể dưới ánh sáng khả kiến nhằm khoáng hóa triệt để kháng sinh và chất ô nhiễm hữu cơ khó xử lý.

#### 4.2.3 Kiểm soát rủi ro tồn dư nhôm hòa tan và quản lý bùn thải nhôm hydroxit
- Loại bỏ nguy cơ tồn dư nhôm hòa tan ($\text{Al}_{\text{res}}$): Nồng độ ion nhôm hòa tan vượt mức tiêu chuẩn trong nước sạch có thể gây độc tính thần kinh cho người sử dụng và tạo cặn kết tủa thứ cấp làm tắc nghẽn đường ống phân phối.
- Cắt giảm phát sinh bùn nhôm hydroxit ($\text{Al(OH)}_3$): Việc tiết kiệm $10.25\%$ lượng PACl châm vào giúp giảm trực tiếp khối lượng kết tủa $\text{Al(OH)}_3$ dạng keo xốp cồng kềnh tích tụ tại đáy bể lắng.
- Tối ưu chi phí xử lý và khử nước bùn: Khối lượng bùn phát sinh thấp hơn giúp giảm áp lực vận hành của sân phơi bùn, tiết kiệm năng lượng cho máy ép bùn và giảm tiêu hao hóa chất polymer trợ lắng bùn.
- Thúc đẩy kinh tế tuần hoàn từ phụ phẩm bùn thải: Bùn lắng chứa nhôm hydroxit sau khi nung xử lý nhiệt có thể tái sinh thành hạt vật liệu hấp phụ để loại bỏ asen ($\text{As(V)}$) hoặc tái sử dụng làm nguyên liệu chế tạo vật liệu xây dựng.

### 4.3 Phần thông tin bổ trợ và Tuyên bố trách nhiệm khoa học

#### 4.3.1 Phân công đóng góp của các tác giả theo tiêu chuẩn CRediT
- Liyan Feng: Trực tiếp đảm nhiệm các vai trò Conceptualization, Methodology, Software, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization, Supervision, Validation, Resources, Project administration.
- Ying Zhang: Đảm nhiệm các khâu Resources, Project administration, Methodology, Investigation, Funding acquisition, Data curation.
- Xiaoting Wei: Đảm nhiệm các vai trò Writing – original draft, Visualization, Supervision, Software.
- Mengyuan Wang: Đảm nhiệm các công việc Visualization, Validation, Software, Resources, Project administration.
- Zhiguang Niu: Đảm nhiệm các vai trò Resources, Project administration, Methodology, Investigation, Data curation.
- Chenchen Wang: Đảm nhiệm các vai trò Writing – review & editing, Visualization, Supervision, Software, Project administration.

#### 4.3.2 Tuyên bố xung đột lợi ích và tính khả dụng của dữ liệu
- Tuyên bố xung đột lợi ích (Declaration of competing interest): Nhóm tác giả khẳng định không có bất kỳ lợi ích tài chính cạnh tranh hoặc quan hệ cá nhân nào làm ảnh hưởng đến các kết quả và kết luận trong bài báo.
- Khả năng tiếp cận dữ liệu (Data availability): Toàn bộ dữ liệu quan trắc chất lượng nước và vận hành thực tế sẽ được nhóm tác giả cung cấp khi có yêu cầu hợp lý.

#### 4.3.3 Nguồn tài trợ và Lời cảm ơn đơn vị thực địa
- Nguồn tài trợ từ đề tài trọng điểm quốc gia: Nghiên cứu nhận hỗ trợ kinh phí từ National Key Research and Development Programme của Trung Quốc theo mã đề tài 2022YFC3203803.
- Nguồn tài trợ từ quỹ khoa học địa phương: Công trình được tài trợ bởi Department of Science and Technology of Fujian Province thông qua đề tài mang mã số 2022J01522.
- Tri ân doanh nghiệp hỗ trợ dữ liệu: Các tác giả gửi lời cảm ơn sâu sắc đến Công ty Cấp nước TEDA Thiên Tân (Tianjin TEDA Water Industry Co., Ltd.) vì đã hỗ trợ kỹ thuật và cung cấp toàn bộ chuỗi dữ liệu vận hành thực địa.

### 4.4 Tổng hợp các tài liệu tham khảo cốt lõi làm nền tảng lý thuyết

#### 4.4.1 Nền tảng thuật toán AutoML và Khung giải thích mô hình SHAP
- Thuật toán tối ưu đường ống học máy TPOT: Olson và cộng sự (2016) công bố công cụ TPOT sử dụng lập trình di truyền trên nền scikit-learn để tự động hóa toàn bộ quy trình thiết kế và tối ưu đường ống học máy.
- Đánh giá tổng quan các hệ thống AutoML hiện đại: Baratchi và cộng sự (2024), Eldeeb và cộng sự (2024) tổng hợp các bước phát triển của AutoML và phân tích thực nghiệm so sánh các khung AutoML phổ biến.
- Ứng dụng AutoML trong phân tích chất lượng nước: Venkata Vara Prasad và cộng sự (2021), Luo và cộng sự (2023) ứng dụng AutoML để tự động hóa phân tích chất lượng nước và dự báo hiệu quả xử lý dinh dưỡng sinh học trong nhà máy nước thải.
- Cơ sở lý thuyết trò chơi của phương pháp SHAP: Lundberg và Lee (2017) thiết lập khung giải thích mô hình thống nhất dựa trên giá trị phân bổ Shapley trong lý thuyết trò chơi hợp tác.
- Chuẩn hóa lựa chọn đặc trưng bằng SHAP: Hancock và cộng sự (2025) chuẩn hóa phương pháp lựa chọn đặc trưng độc lập với mô hình bằng cách ứng dụng phân tích giá trị SHAP.
- Ứng dụng XAI giải mã quá trình xử lý nước: Li và cộng sự (2024), Makumbura và cộng sự (2024), Park và cộng sự (2022) kết hợp mô hình học sâu và học máy quần thể với SHAP để dự báo và giải thích các chỉ số chất lượng dòng ra.

#### 4.4.2 Cơ chế keo tụ bằng muối kim loại và Mô hình hóa định liều trong DWTP
- Động học keo tụ bằng muối kim loại thủy phân: Duan và Gregory (2003) giải thích chi tiết các cơ chế trung hòa điện tích, kết tủa bẫy cặn và động học thủy phân phức tạp của các ion muối kim loại như nhôm và sắt.
- Dự báo liều lượng keo tụ bằng mô hình chuỗi thời gian sâu: Lin, Kim và cộng sự (2023, 2024) phát triển mô hình mạng chú ý đồ thị đa biến (GAT) và so sánh mạng nơ-ron nhân tạo với mạng nơ-ron sâu trong việc dự đoán liều lượng chất keo tụ trên tập dữ liệu vận hành lớn.
- Kết hợp mạng Elman và Rừng ngẫu nhiên: Wang và cộng sự (2023) ứng dụng thành công mạng nơ-ron hồi quy Elman kết hợp với mô hình Rừng ngẫu nhiên để dự đoán đồng thời liều chất keo tụ và độ đục nước sau lắng.
- Tối ưu hóa phản ứng keo tụ bằng phương pháp bề mặt đáp ứng: Ji và cộng sự (2024) áp dụng phương pháp bề mặt đáp ứng (RSM) để xác định các thông số vận hành tối ưu cho quá trình keo tụ bằng Poly-aluminum Chloride.
- Điều khiển dự báo đa mô hình cho quy trình keo tụ: Bello và cộng sự (2014) thiết kế hệ thống điều khiển dự báo dựa trên nhiều mô hình (MMPC) để kiểm soát tự động liều hóa chất châm vào trong nhà máy xử lý nước cấp.

#### 4.4.3 Kỹ thuật keo tụ nước độ đục thấp, Polyme sinh học và Quản lý phụ phẩm
- Cơ chế keo tụ nước nhiệt độ thấp và độ đục thấp: Zhang và cộng sự (2018), Liu và cộng sự (2019) nghiên cứu tăng cường keo tụ cho nguồn nước mặt độ đục thấp thông qua việc điều chỉnh độ kiềm (basicity) của PACl và sử dụng chitosan làm chất trợ keo tụ.
- Hợp chất keo tụ composite sinh học: El Foulani và cộng sự (2023) so sánh hiệu năng của chất keo tụ hỗn hợp PACl-chitosan và PACl-sodium alginate trong việc loại bỏ chất bẩn ở nguồn nước hồ chứa.
- Bột hạt tự nhiên làm chất tạo bông thân thiện môi trường: Vunain và cộng sự (2019) đánh giá hiệu quả tạo bông và khả năng giảm thiểu mầm bệnh của bột hạt chùm ngây (*Moringa oleifera*).
- Tái sử dụng bùn thải nhôm hydroxit nung: Kim và cộng sự (2023) nghiên cứu tác động của nhiệt độ nung lên khả năng hấp phụ của các hạt chế tạo từ bùn thải PACl để loại bỏ asen ($\text{As(V)}$) khỏi môi trường nước.
- Công nghệ xúc tác phân hủy ô nhiễm hữu cơ: Luo và cộng sự (2025), Yang và cộng sự (2025) tổng hợp các vật liệu xúc tác mới mở ra triển vọng kết hợp với công đoạn xử lý keo tụ để bảo vệ môi trường nước bền vững.
