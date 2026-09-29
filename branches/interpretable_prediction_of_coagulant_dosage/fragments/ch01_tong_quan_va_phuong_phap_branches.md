## 1. Tổng quan và Phương pháp nghiên cứu

### 1.1 Thông tin xuất bản và Tóm tắt công trình

#### 1.1.1 Siêu dữ liệu bài báo và Tác giả
- Tiêu đề công trình: Interpretable prediction of coagulant dosage in drinking water treatment plant based on automated machine learning and SHAP method.
- Danh sách tác giả: Liyan Feng, Ying Zhang, Xiaoting Wei, Mengyuan Wang, Zhiguang Niu, Chenchen Wang.
- Tác giả liên hệ: Ying Zhang (yzhang_n@tju.edu.cn) và Chenchen Wang (wcc12122008@163.com).
- Cơ quan chủ quản: Trường Khoa học & Kỹ thuật Môi trường thuộc Đại học Thiên Tân; Trường Kỹ thuật Môi trường & Đô thị thuộc Đại học Thành Kiến Thiên Tân; Phòng thí nghiệm Trọng điểm Khoa học và Công nghệ Nước Thiên Tân; Công ty TNHH Cấp nước TEDA Kim Liên Thiên Tân.
- Thông tin xuất bản: Tạp chí Journal of Water Process Engineering, Tập 75, Năm 2025, Mã bài báo 107925, Nhà xuất bản Elsevier.
- Lịch sử bài báo: Tạp chí nhận bản thảo ngày 25 tháng 01 năm 2025. Tác giả nộp bản sửa đổi ngày 01 tháng 05 năm 2025. Ban biên tập chấp nhận đăng ngày 09 tháng 05 năm 2025. Bài báo xuất bản trực tuyến ngày 15 tháng 05 năm 2025.
- Chỉ số định danh: Mã định danh số $\text{DOI: } 10.1016/\text{j.jwpe.2025.107925}$. Mã chuẩn quốc tế $\text{ISSN: } 2214-7144$.
- Từ khóa chuyên ngành: Automated machine learning, SHAP interpretability, Random Forest, Coagulant, Water treatment.

#### 1.1.2 Tóm tắt nghiên cứu và Các chỉ số định lượng then chốt
- Mục tiêu nghiên cứu: Nghiên cứu xây dựng mô hình dự đoán chính xác liều lượng hóa chất keo tụ trong nhà máy xử lý nước cấp (DWTP) bằng học máy tự động (AutoML). Nghiên cứu tích hợp phương pháp SHAP nhằm loại bỏ tính chất hộp đen và nâng cao tính minh bạch khi ra quyết định.
- Hiệu năng vượt trội của mô hình Random Forest (RF): Mô hình RF do AutoML tối ưu hóa đạt hiệu năng vượt trội so với mô hình cây tăng cường độ dốc (GBT) đơn lẻ tốt nhất. Mô hình đạt chỉ số $\text{RMSE} = 0.89$, giảm $37\%$. Mô hình đạt chỉ số $\text{MAE} = 0.47$, giảm $52\%$. Mô hình đạt hệ số xác định $R^2 = 0.96$, tăng $5\%$.
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
