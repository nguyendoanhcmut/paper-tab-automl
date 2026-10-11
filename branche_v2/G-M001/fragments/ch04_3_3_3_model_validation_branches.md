### 3.3. Model validation

* Quá trình kiểm chứng (validation) các mô hình mạng nơ-ron truyền thẳng (FFNN - Feedforward Neural Network) và mạng nơ-ron hàm cơ sở xuyên tâm (RBFNN - Radial Basis Function Neural Network) được xác nhận dựa trên tính hợp lệ của cả tập dữ liệu huấn luyện (training dataset) và tập dữ liệu kiểm tra (testing dataset).
  * Để đánh giá độ tin cậy và tính hợp lệ của các mô hình phát triển, đồ thị đầu ra thông lượng dòng thấm (permeate flux output plot) và đồ thị hồi quy (regression plot) được phân tích chi tiết.
  * Việc so sánh và đánh giá hiệu năng giữa các mô hình dựa trên $2$ tiêu chí định lượng then chốt:
    * Giá trị sai số toàn phương trung bình thấp nhất ($\text{MSE}$ - Mean Squared Error nhỏ nhất).
    * Hệ số tương quan cao nhất ($R$ - Correlation Coefficient lớn nhất).

#### Đánh giá và kiểm chứng các mô hình FFNN (FFNN Models Validation)

* Kết quả huấn luyện thông lượng dòng thấm cho các mô hình $\text{FFNN-1}$, $\text{FFNN-2}$, $\text{FFNN-3}$, $\text{FFNN-4}$ và $\text{FFNN-RSM}$ (Hình S7(a)–S7(f)) được thiết lập dựa trên tập siêu tham số tối ưu thu được từ các Mục 3.1.1, 3.2.1 và 3.2.2.
  * Tập dữ liệu dự báo của cả $5$ mô hình huấn luyện đều thể hiện xu hướng tương đồng cao với tập dữ liệu thực nghiệm đo đạc (actual / measured datasets).
  * Mô hình $\text{FFNN-2}$ đạt độ chính xác huấn luyện cao nhất với hệ số $R = 0{,}9881$ và $\text{MSE} = 0{,}0236$.
  * Độ chính xác của các mô hình huấn luyện còn lại xếp theo thứ tự giảm dần:
    * $\text{FFNN-RSM}$: $R = 0{,}9878$ và $\text{MSE} = 0{,}0243$.
    * $\text{FFNN-1}$: $R = 0{,}9877$ và $\text{MSE} = 0{,}0245$.
    * $\text{FFNN-4}$: $R = 0{,}9862$ và $\text{MSE} = 0{,}0274$.
    * $\text{FFNN-3}$: $R = 0{,}9837$ và $\text{MSE} = 0{,}0323$.
* Mô hình huấn luyện sau đó được kiểm chứng độc lập trên tập dữ liệu kiểm tra (testing dataset), đạt được sự phù hợp xuất sắc với dữ liệu thực tế trên toàn bộ $1.600$ điểm mẫu kiểm tra.
  * Mô hình $\text{FFNN-3}$ có độ lệch nhẹ (slight offset) so với thực nghiệm do giá trị $\text{MSE}$ cao hơn một chút so với các mô hình khác.
  * Tất cả các mô hình FFNN đều thể hiện năng lực dự báo vững cáp với các chỉ số $R$ và $\text{MSE}$ tương đương nhau trên tập kiểm tra:
    * Mô hình $\text{FFNN-2}$ đạt hiệu năng kiểm tra cao nhất với $R = 0{,}9871$ và $\text{MSE} = 0{,}0256$.
    * Mô hình $\text{FFNN-RSM}$ bám sát nút với $R = 0{,}9867$ và $\text{MSE} = 0{,}0264$.
    * Mô hình $\text{FFNN-1}$ đạt $R = 0{,}9865$ và $\text{MSE} = 0{,}0268$.
    * Mô hình $\text{FFNN-4}$ đạt $R = 0{,}9854$ và $\text{MSE} = 0{,}0290$.
    * Mô hình $\text{FFNN-3}$ đạt $R = 0{,}9827$ và $\text{MSE} = 0{,}0343$.
    * **Hình 8.** Thông lượng dòng thấm và đồ thị tương quan thực nghiệm - dự báo của các mô hình FFNN trên tập kiểm tra (testing dataset)
      * <img src="assets/fig_08_p19.jpeg" alt="Hình 8" />
      * **Hình này chứng minh điều gì**
        * Tất cả $5$ mô hình FFNN đều được kiểm chứng thành công trên tập kiểm tra (testing dataset) với độ chính xác cao và bám sát dữ liệu thực nghiệm; trong đó mô hình FFNN-2 đạt hiệu năng dự báo tốt nhất.
      * **Từ đâu mà thấy được**
        * Đồ thị chuỗi (a) cho thấy đường thông lượng dự báo của cả $5$ mô hình bám rất sát thực nghiệm qua $1.600$ điểm kiểm tra, trong đó FFNN-2 đạt $\text{MSE}$ thấp nhất ($0{,}0256$), tiếp theo là FFNN-RSM ($0{,}0264$), FFNN-1 ($0{,}0268$), FFNN-4 ($0{,}0290$) và FFNN-3 ($0{,}0343$ có độ lệch nhẹ).
        * Đồ thị tương quan (b)–(f) thể hiện các điểm dữ liệu phân bố tập trung cao dọc đường hồi quy tuyến tính với hệ số tương quan $R$ rất lớn: FFNN-2 đạt cao nhất ($R = 0{,}9871$; $R^2 = 0{,}9744$), kế tiếp là FFNN-RSM ($R = 0{,}9867$), FFNN-1 ($R = 0{,}9865$), FFNN-4 ($R = 0{,}9854$) và FFNN-3 ($R = 0{,}9827$).

#### Đánh giá và kiểm chứng các mô hình RBFNN (RBFNN Models Validation)

* Trên tập dữ liệu huấn luyện (Hình S8(a)–S8(c)), cả mô hình RBFNN thông thường (conventional RBFNN) và mô hình RBFNN-RSM đều dự báo chính xác thông lượng dòng thấm của hệ thống lọc SMBR, trong đó mô hình thông thường nhỉnh hơn một chút:
  * Mô hình RBFNN thông thường đạt $R = 0{,}9882$ và $\text{MSE} = 0{,}0235$.
  * Mô hình RBFNN-RSM đạt $R = 0{,}9873$ và $\text{MSE} = 0{,}0253$.
* Mô hình kiểm tra của RBFNN thông thường được đối chiếu trực tiếp với RBFNN-RSM trên tập dữ liệu kiểm tra, chứng minh cả hai mô hình đều có năng lực dự báo tương đương với sai số $\text{MSE}$ gần như trùng khớp.
  * Mô hình RBFNN thông thường đạt hệ số tương quan $R = 0{,}9867$ và $\text{MSE} = 0{,}0265$.
  * Mô hình RBFNN-RSM đạt hệ số tương quan $R = 0{,}9857$ và $\text{MSE} = 0{,}0284$.
    * **Hình 9.** Thông lượng dòng thấm và đồ thị tương quan thực nghiệm - dự báo của các mô hình RBFNN trên tập kiểm tra (testing dataset)
      * <img src="assets/fig_09_p20.jpeg" alt="Hình 9" />
      * **Hình này chứng minh điều gì**
        * Cả mô hình RBFNN thông thường và RBFNN-RSM đều đạt độ chính xác dự báo rất cao và tương đương nhau trên tập dữ liệu kiểm tra, chứng minh cấu trúc tối ưu của RBFNN-RSM duy trì trọn vẹn hiệu năng dự báo.
      * **Từ đâu mà thấy được**
        * Đồ thị (a): Đường dự báo của RBFNN và RBFNN-RSM bám rất sát giá trị thực nghiệm qua toàn bộ $1.600$ mẫu kiểm tra với sai số toàn phương trung bình rất nhỏ ($\text{MSE} \approx 0{,}0264\text{--}0{,}0265$).
        * Đồ thị (b, c): Điểm dữ liệu phân bố tập trung cao dọc theo đường hồi quy tuyến tính với hệ số tương quan xuất sắc ($R = 0{,}9867$, $R^2 = 0{,}9734$ ở RBFNN; $R = 0{,}9857$, $R^2 = 0{,}9715$ ở RBFNN-RSM).

#### Tổng kết hiệu năng tổng thể và chi phí tính toán (Overall Performance & Computational Efficiency)

* Bảng 4 (Table 4) tổng kết toàn diện các chỉ số thống kê hiệu năng trên tập huấn luyện và tập kiểm tra cùng số lần chạy và thời gian tính toán của các mô hình:
  * $\text{FFNN-1}$ (cấu hình thông thường):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0245$, $\text{RMSE} = 0{,}1567$, $R = 0{,}9877$, $R^2 = 0{,}9754$; Số lần chạy: $60$, Thời gian: $59{,}58\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0268$, $\text{RMSE} = 0{,}1636$, $R = 0{,}9865$, $R^2 = 0{,}9731$.
  * $\text{FFNN-2}$ (cấu hình thông thường có độ chính xác cao nhất):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0236$, $\text{RMSE} = 0{,}1535$, $R = 0{,}9881$, $R^2 = 0{,}9764$; Số lần chạy: $60$, Thời gian: $57{,}68\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0256$, $\text{RMSE} = 0{,}1600$, $R = 0{,}9871$, $R^2 = 0{,}9744$.
  * $\text{FFNN-3}$ (cấu hình thông thường):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0323$, $\text{RMSE} = 0{,}1797$, $R = 0{,}9837$, $R^2 = 0{,}9677$; Số lần chạy: $60$, Thời gian: $72{,}95\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0343$, $\text{RMSE} = 0{,}1851$, $R = 0{,}9827$, $R^2 = 0{,}9656$.
  * $\text{FFNN-4}$ (cấu hình thông thường):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0274$, $\text{RMSE} = 0{,}1654$, $R = 0{,}9862$, $R^2 = 0{,}9726$; Số lần chạy: $60$, Thời gian: $63{,}03\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0290$, $\text{RMSE} = 0{,}1703$, $R = 0{,}9854$, $R^2 = 0{,}9709$.
  * $\text{FFNN-RSM}$ (tối ưu hóa bằng phương pháp bề mặt đáp ứng):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0243$, $\text{RMSE} = 0{,}1559$, $R = 0{,}9878$, $R^2 = 0{,}9757$; Số lần chạy: $120$, Thời gian: $150{,}38\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0264$, $\text{RMSE} = 0{,}1624$, $R = 0{,}9867$, $R^2 = 0{,}9736$; Tổng số lần chạy: $120$, Tổng thời gian: $150{,}38\text{ s}$.
  * $\text{RBFNN}$ thông thường (cấu hình conventional):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0235$, $\text{RMSE} = 0{,}1533$, $R = 0{,}9882$, $R^2 = 0{,}9765$; Số lần chạy: $36$, Thời gian: $269{,}02\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0265$, $\text{RMSE} = 0{,}1628$, $R = 0{,}9867$, $R^2 = 0{,}9734$; Tổng số lần chạy: $36$, Tổng thời gian: $269{,}02\text{ s}$.
  * $\text{RBFNN-RSM}$ (tối ưu hóa bằng RSM):
    * Tập huấn luyện (Training): $\text{MSE} = 0{,}0253$, $\text{RMSE} = 0{,}1589$, $R = 0{,}9873$, $R^2 = 0{,}9747$; Số lần chạy: $13$, Thời gian: $93{,}82\text{ s}$.
    * Tập kiểm tra (Testing): $\text{MSE} = 0{,}0284$, $\text{RMSE} = 0{,}1686$, $R = 0{,}9857$, $R^2 = 0{,}9715$; Tổng số lần chạy: $13$, Tổng thời gian: $98{,}82\text{ s}$.
* Phương pháp tối ưu hóa siêu tham số đề xuất $\text{ANN-RSM}$ chứng minh ưu thế vượt bậc về thời gian và số lượt lặp tính toán so với phương pháp thử sai đơn biến truyền thống (OVAT - One-Variable-at-a-Time):
  * Đối với họ mô hình FFNN: phương pháp OVAT yêu cầu $60$ lần chạy cho mỗi mô hình (tổng cộng $240$ lần chạy cho $4$ mô hình $\text{FFNN-1}$ đến $\text{FFNN-4}$) với tổng thời gian tính toán lên tới $253{,}24\text{ s}$ ($59{,}58\text{ s}$ cho $\text{FFNN-1}$, $57{,}68\text{ s}$ cho $\text{FFNN-2}$, $72{,}95\text{ s}$ cho $\text{FFNN-3}$, và $63{,}03\text{ s}$ cho $\text{FFNN-4}$). Ngược lại, $\text{FFNN-RSM}$ chỉ cần duy nhất $120$ lần chạy trong $150{,}38\text{ s}$, cắt giảm $40{,}6\%$ thời gian tính toán và giảm một nửa số lượng phép thử.
  * Đối với họ mô hình RBFNN: mô hình $\text{RBFNN-RSM}$ chỉ cần $13$ lần chạy trong $98{,}82\text{ s}$, giảm mạnh so với $\text{RBFNN}$ thông thường đòi hỏi tới $36$ lần chạy trong $269{,}02\text{ s}$, tiết kiệm đến $63{,}3\%$ thời gian tính toán và giảm $63{,}9\%$ số lần chạy.
* Kết quả kiểm chứng thực nghiệm tại Bảng 4 củng cố trọn vẹn kết quả phân tích phương sai ANOVA ở Bảng 3 (Table 3 | Analysis of variance for the RBFNN hyperparameters quadratic model):
  * Phân tích ANOVA ở Bảng 3 đã chứng minh tính có ý nghĩa thống kê cực kỳ cao của mô hình toàn phương tối ưu hóa siêu tham số RBFNN ($F\text{-value} = 21.809{,}26$, giá trị $p < 0{,}0001$, hệ số xác định $R^2 = 0{,}9999$).
  * Sự tương đồng về độ chính xác dự báo kiểm tra giữa $\text{RBFNN-RSM}$ ($R = 0{,}9857$, $\text{MSE} = 0{,}0284$) và RBFNN thông thường ($R = 0{,}9867$, $\text{MSE} = 0{,}0265$) khẳng định rằng mô hình hồi quy bậc hai từ Bảng 3 xác định chính xác điểm cực tiểu thực sự mà không làm suy giảm hiệu năng dự báo thực tế.

#### Thảo luận so sánh cơ chế tính toán và thuật toán (Mechanism & Algorithm Discussion)

* Mô hình RBFNN đòi hỏi thời gian tính toán nhiều hơn đáng kể so với FFNN ($269{,}02\text{ s}$ so với khoảng $57\text{--}73\text{ s}$ ở mô hình thông thường), hoàn toàn nhất quán với các phát hiện nghiên cứu trước đây (Yang 2023).
  * Nguyên nhân xuất phát từ việc RBFNN cần số lượng nơ-ron lớn hơn, tạo ra nhiều bậc tự do hơn cho quá trình điều chỉnh trọng số (weight adjustment) và hệ quả là làm gia tăng thời gian tính toán (Nazghelichi et al. 2011).
* Độ chính xác hiệu năng của FFNN ghi nhận nhỉnh hơn một chút so với RBFNN ($R = 0{,}9871$ ở $\text{FFNN-2}$ so với $R = 0{,}9867$ ở RBFNN thông thường).
  * Phát hiện này trái ngược với các kết quả do Yang (2023) báo cáo khi dự báo hiệu năng trong hệ thống chưng cất màng (membrane distillation).
* Sự kết hợp giữa thuật toán huấn luyện Levenberg–Marquardt (`trainlm`) và hàm kích hoạt đơn vị tuyến tính chỉnh lưu (`ReLU`) trong FFNN được chứng minh là cấu hình tối ưu cho dự báo thông lượng dòng thấm màng SMBR, vừa giảm thời gian tính toán vừa duy trì độ chính xác rất cao:
  * Thuật toán Levenberg–Marquardt tạo điều kiện đẩy nhanh tốc độ hội tụ của quá trình huấn luyện với giá trị $\text{MSE}$ thấp hơn (Ibrahim & Wahab 2022).
  * Hàm kích hoạt `ReLU` thể hiện hiệu năng huấn luyện vượt trội so với các hàm kích hoạt phi tuyến truyền thống (Rasamoelina et al. 2020).
* Kỹ thuật tích hợp $\text{ANN-RSM}$ nổi lên như một phương pháp tối ưu hóa siêu tham số có hệ thống (systematic), vượt trội (superior) và nhanh hơn (faster) so với phương pháp thử sai đơn biến OVAT truyền thống:
  * Phương pháp đề xuất giảm mạnh số lần lặp thí nghiệm cần thiết để xác định siêu tham số tối ưu, rút ngắn đáng kể thời gian phát triển mô hình học máy.
  * Đây là giải pháp thay thế hoàn toàn khả thi và hiệu quả cho kỹ thuật OVAT, mở ra tiềm năng ứng dụng trực tiếp trong việc phát triển hệ thống điều khiển tự động nhằm nâng cao hiệu quả vận hành màng trong xử lý nước thải.
