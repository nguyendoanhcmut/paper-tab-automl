## 4. Conclusions

- Phát triển thành công các mô hình mạng nơ-ron truyền thẳng (Feed-Forward Neural Network — FFNN) và mạng nơ-ron hàm cơ sở xuyên tâm (Radial Basis Function Neural Network — RBFNN) để dự đoán thông lượng thấm (permeate flux) của nước thải nhà máy chế biến dầu cọ (Palm Oil Mill Effluent — POME) trong quá trình lọc màng của hệ thống bể phản ứng sinh học màng ngập nước (Submerged Membrane Bioreactor — SMBR).
  - Mô hình kết hợp FFNN-RSM và RBFNN-RSM đề xuất được phát triển nhằm xác định các siêu tham số (hyperparameters) của mạng nơ-ron nhân tạo (Artificial Neural Network — ANN).
  - Các mô hình đề xuất được so sánh đối chuẩn với những mô hình thử nghiệm truyền thống thay đổi từng biến đơn lẻ tại một thời điểm (One-Variable-At-a-Time — OVAT), bao gồm FFNN-1, FFNN-2, FFNN-3, FFNN-4 và RBFNN.
  - Kết quả kiểm định mô hình (model validation) chứng minh độ tin cậy tốt (good validity) của cả mô hình huấn luyện (training) và mô hình kiểm tra (testing) trên toàn bộ các mô hình khảo sát.
  - Kết quả mô phỏng (simulation results) cho thấy độ chính xác hiệu năng tương đương (comparable performance accuracy) của các mô hình ANN-RSM đề xuất (FFNN-RSM và RBFNN-RSM) so với các mô hình ANN truyền thống (FFNN-1, FFNN-2, FFNN-3, FFNN-4 và RBFNN).

- Tối ưu hóa siêu tham số bằng phương pháp bề mặt đáp ứng (Response Surface Methodology — RSM) giúp cắt giảm vượt trội thời gian tính toán và số lần lặp thực nghiệm:
  - Tối ưu hóa siêu tham số ANN cho mô hình FFNN-RSM mang lại sự cải thiện về thời gian tính toán (computational time) khoảng $41\%$ và số lần lặp (number of repetitions) khoảng $50\%$ so với mô hình FFNN truyền thống (FFNN-1, FFNN-2, FFNN-3 và FFNN-4).
  - Mô hình RBFNN-RSM giúp nâng cao hiệu năng khi giảm thời gian tính toán tới $65\%$ và số lần lặp tới $64\%$ so với mô hình RBFNN truyền thống.
  - Lợi ích của RSM có được là nhờ áp dụng quy hoạch thực nghiệm (Design of Experiments — DoE), giúp đòi hỏi ít số lần lặp lại của quá trình huấn luyện hơn nhưng vẫn cung cấp được lượng thông tin rất lớn (huge sum of information).
  - Phương pháp RSM đã xác định thành công các siêu tham số tối ưu nhất cho cả hai mô hình FFNN và RBFNN.
  - Hơn nữa, RSM học được ý nghĩa thống kê và mối quan hệ giữa các siêu tham số ANN với giá trị sai số toàn phương trung bình (Mean Squared Error — $\text{MSE}$), ngay cả khi mô hình chứa các tham số hỗn hợp (mix parameters, bao gồm biến số định lượng — numerical và biến số phân loại — categorical).
  - Kỹ thuật ANN-RSM đề xuất chứng minh sự vượt trội rõ rệt so với các mô hình ANN truyền thống xét trên cả ba phương diện: số lần lặp lại, thời gian tính toán và năng lực ước lượng (estimation capabilities).

- Bảng 4 tổng hợp độ chính xác hiệu năng tổng thể của các mô hình mạng nơ-ron truyền thống và các mô hình tích hợp RSM:

**Table 4** | Overall performance accuracy of the FFNN conventional, FFNN RSM, RBFNN conventional, and RBFNN RSM models for the SMBR filtration system

| Model | Training MSE | Training RMSE | Training R | Training $R^2$ | Testing MSE | Testing RMSE | Testing R | Testing $R^2$ | No. of run | Computational time (sec) | Total no. of run | Total computational time (sec) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| FFNN-1 | $0.0245$ | $0.1567$ | $0.9877$ | $0.9754$ | $0.0268$ | $0.1636$ | $0.9865$ | $0.9731$ | $60$ | $59.58$ | $240$ | $253.24$ |
| FFNN-2 | $0.0236$ | $0.1535$ | $0.9881$ | $0.9764$ | $0.0256$ | $0.1600$ | $0.9871$ | $0.9744$ | $60$ | $57.68$ | — | — |
| FFNN-3 | $0.0323$ | $0.1797$ | $0.9837$ | $0.9677$ | $0.0343$ | $0.1851$ | $0.9827$ | $0.9656$ | $60$ | $72.95$ | — | — |
| FFNN-4 | $0.0274$ | $0.1654$ | $0.9862$ | $0.9726$ | $0.0290$ | $0.1703$ | $0.9854$ | $0.9709$ | $60$ | $63.03$ | — | — |
| FFNN-RSM | $0.0243$ | $0.1559$ | $0.9878$ | $0.9757$ | $0.0264$ | $0.1624$ | $0.9867$ | $0.9736$ | $120$ | $150.38$ | $120$ | $150.38$ |
| RBFNN | $0.0235$ | $0.1533$ | $0.9882$ | $0.9765$ | $0.0265$ | $0.1628$ | $0.9867$ | $0.9734$ | $36$ | $269.02$ | $36$ | $269.02$ |
| RBFNN-RSM | $0.0253$ | $0.1589$ | $0.9873$ | $0.9747$ | $0.0284$ | $0.1686$ | $0.9857$ | $0.9715$ | $13$ | $93.82$ | $13$ | $98.82$ |

  - Các quan sát chi tiết từ Bảng 4:
    - Nhóm mô hình FFNN truyền thống (FFNN-1 đến FFNN-4): Đạt sai số huấn luyện $\text{MSE}$ trong khoảng $0.0236$ – $0.0323$, $\text{RMSE}$ từ $0.1535$ – $0.1797$, $R$ từ $0.9837$ – $0.9881$, $R^2$ từ $0.9677$ – $0.9764$; sai số kiểm thử $\text{MSE}$ trong khoảng $0.0256$ – $0.0343$, $\text{RMSE}$ từ $0.1600$ – $0.1851$, $R$ từ $0.9827$ – $0.9871$, $R^2$ từ $0.9656$ – $0.9744$. Mỗi cấu hình đòi hỏi $60$ lần chạy với thời gian tính toán từ $57.68\text{ s}$ đến $72.95\text{ s}$, dẫn đến tổng cộng $240$ lần chạy và tiêu tốn $253.24\text{ s}$.
    - Mô hình FFNN-RSM: Đạt độ chính xác huấn luyện $\text{MSE} = 0.0243$, $\text{RMSE} = 0.1559$, $R = 0.9878$, $R^2 = 0.9757$ và kiểm thử $\text{MSE} = 0.0264$, $\text{RMSE} = 0.1624$, $R = 0.9867$, $R^2 = 0.9736$. Toàn bộ quy trình chỉ cần $120$ lần chạy với tổng thời gian tính toán là $150.38\text{ s}$ (tiết kiệm gần $41\%$ thời gian và $50\%$ số lần lặp so với tổng chu trình của FFNN truyền thống).
    - Mô hình RBFNN truyền thống: Đạt kết quả huấn luyện $\text{MSE} = 0.0235$, $\text{RMSE} = 0.1533$, $R = 0.9882$, $R^2 = 0.9765$ và kiểm thử $\text{MSE} = 0.0265$, $\text{RMSE} = 0.1628$, $R = 0.9867$, $R^2 = 0.9734$. Cần $36$ lần chạy với thời gian tính toán lên tới $269.02\text{ s}$.
    - Mô hình RBFNN-RSM: Đạt kết quả huấn luyện $\text{MSE} = 0.0253$, $\text{RMSE} = 0.1589$, $R = 0.9873$, $R^2 = 0.9747$ và kiểm thử $\text{MSE} = 0.0284$, $\text{RMSE} = 0.1686$, $R = 0.9857$, $R^2 = 0.9715$. Số lần chạy được rút gọn tối đa xuống chỉ còn $13$ lần ($93.82\text{ s}$ thời gian chạy, tổng thời gian tính toán $98.82\text{ s}$), giúp giảm tương ứng $64\%$ số lần lặp và $65\%$ (tính theo thời gian chạy $93.82\text{ s}$ so với $269.02\text{ s}$) thời gian tính toán.

- Định hướng nghiên cứu mở rộng và triển vọng ứng dụng:
  - Mặc dù nghiên cứu chứng minh tính khả thi của phương pháp ANN-RSM đề xuất trong việc tối ưu hóa siêu tham số ANN cho quá trình thông lượng thấm của hệ thống SMBR, việc tiếp tục nghiên cứu sâu rộng hơn về phương pháp luận này vẫn là yêu cầu thiết yếu.
  - Cần khám phá thêm các hàm huấn luyện thay thế (alternative training functions), chẳng hạn như thuật toán điều chuẩn Bayes (Bayesian Regularization — BR) và thuật toán hạ độ dốc liên hợp theo tỷ lệ (Scaled Conjugate Gradient).
  - Khảo sát các hàm kích hoạt (activation functions) đa dạng khác như logsig, hàm đơn vị tuyến tính hàm mũ theo tỷ lệ (Scaled Exponential Linear Unit — SELU) và hàm đơn vị tuyến tính chỉnh lưu rò rỉ (Leaky Rectified Linear Unit — Leaky ReLU).
  - Phương pháp luận được trình bày trong nghiên cứu này cần được nhân rộng không chỉ cho các mô hình học máy (Machine Learning — ML) khác mà còn đối với nhiều lĩnh vực xử lý nước thải đa dạng khác nhau.
  - Việc mở rộng phạm vi ứng dụng sẽ đóng góp vào sự hiểu biết toàn diện về khả năng khái quát hóa (generalizability) cũng như tính hiệu quả của phương pháp đề xuất qua các bối cảnh khác nhau.
  - Ngoài ra, sự cải tiến quan trọng này có thể được ứng dụng trong tương lai để phát triển các hệ thống điều khiển nhằm nâng cao hiệu quả vận hành màng lọc.

- Lời cảm ơn, Tuyên bố dữ liệu và Xung đột lợi ích (Acknowledgements, Data Availability Statement, Conflict of Interest):
  - Lời cảm ơn (Acknowledgements): Công trình nghiên cứu này được tài trợ một phần bởi Quỹ Nghiên cứu Đại học Tác động Cao của Universiti Teknologi Malaysia (UTMHI, mã số $Q.J130000.2451.08G74$) và Bộ Giáo dục Đại học Malaysia (Ministry of Higher Education) theo Đề án Tài trợ Nghiên cứu Nguyên mẫu (Prototype Research Grant Scheme — PRGS/1/2019/TK04/UTM/02/3).
  - Tuyên bố về tính khả dụng của dữ liệu (Data Availability Statement): Dữ liệu không thể công khai trực tiếp cho cộng đồng; bạn đọc có thể liên hệ với tác giả chịu trách nhiệm liên lạc (corresponding author) để biết thêm chi tiết.
  - Xung đột lợi ích (Conflict of Interest): Các tác giả tuyên bố không có xung đột lợi ích.
