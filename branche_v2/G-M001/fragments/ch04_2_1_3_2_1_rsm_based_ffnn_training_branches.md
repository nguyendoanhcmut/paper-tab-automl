#### 3.2.1. RSM-based FFNN training

* **Mô hình bậc hai và phép biến đổi Box-Cox cho biến đáp ứng $1/\text{MSE}$**:
  * Nghiên cứu lựa chọn mô hình bậc hai (quadratic model) để thiết lập hàm quan hệ giữa các siêu tham số đầu vào của mạng nơ-ron truyền thẳng (Feed-Forward Neural Network - FFNN) và biến đáp ứng sai số toàn phương trung bình (Mean Squared Error - MSE) ở đầu ra.
  * Phép biến đổi Box-Cox (Box-Cox transformation) được áp dụng với tham số $\alpha = 1$, chuyển đổi biến đáp ứng $\text{MSE}$ thành nghịch đảo sai số ($1/\text{MSE}$):
    * Phép biến đổi này đưa phân phối dữ liệu của biến đáp ứng tiệm cận gần hơn với phân phối chuẩn (normality) và tăng cường độ tương thích của mô hình hồi quy với dữ liệu thực nghiệm (Nazghelichi et al. 2011).
    * Việc nghịch đảo giá trị $\text{MSE}$ đặc biệt có lợi cho tập dữ liệu có giá trị số rất nhỏ, vì phép nghịch đảo chuyển đổi chỉ số thành giá trị có độ lớn cao hơn, cho phép thể hiện trực quan và hiệu quả hơn sự cải thiện hiệu năng huấn luyện mạng.
  * Bộ dữ liệu so sánh giữa đáp ứng $1/\text{MSE}$ thực nghiệm (actual) và dự đoán (predicted) dựa trên $120$ lượt chạy thử nghiệm (runs) với nhiều cấu hình siêu tham số khác nhau theo thiết kế tâm xoay hỗn hợp (Central Composite Design - CCD) được trình bày chi tiết tại Bảng S3 trong Tài liệu bổ sung (Supplementary Material).
  * Phương trình hồi quy theo các yếu tố mã hóa (coded factors) cho phép dự đoán giá trị đáp ứng tại các mức cụ thể của từng nhân tố:
    * Mức cao của các yếu tố được chuẩn hóa mã hóa thành $+1$, mức thấp được mã hóa thành $-1$.
    * Phương trình mã hóa cho phép đánh giá định lượng tầm ảnh hưởng tương đối giữa các yếu tố thông qua việc so sánh trực tiếp độ lớn và dấu của các hệ số hồi quy.
  * Mô hình hồi quy bậc hai theo các biến mã hóa cho $1/\text{MSE}$ của mô hình FFNN-RSM được biểu diễn tại Phương trình (15):
    $$\frac{1}{\text{MSE}} = 27.8796 + 4.7072 A + 1.9849 B - 2.5610 C + 1.0684 D - 11.5799 E - 2.3678 F - 1.0215 AB - 0.0688 AC - 0.3811 AD - 3.5479 AE + 3.1920 AF - 2.7498 BC - 0.5089 BD + 0.5671 BE - 0.1462 BF + 0.4303 CD - 2.7918 CE + 0.2225 CF + 1.0511 DE - 0.0169 DF + 0.0231 EF - 1.9888 A^2 - 1.8045 B^2 - 1.9809 C^2 + 0.3722 D^2 \quad (15)$$
    * Trong đó: các thông số $A, B, C, D, E$ và $F$ lần lượt đại diện cho các giá trị mã hóa của:
      * $A$: Số lượng nơ-ron trong tầng ẩn (number of neurons)
      * $B$: Tốc độ học (learning rate)
      * $C$: Hệ số xung lượng (momentum)
      * $D$: Số lượng epoch (number of epochs)
      * $E$: Hàm huấn luyện (training function)
      * $F$: Hàm kích hoạt (activation function)
    * Quy ước dấu: Hệ số dương ($+$) biểu thị tác động làm gia tăng giá trị đáp ứng $1/\text{MSE}$ (giảm $\text{MSE}$, cải thiện độ chính xác), hệ số âm ($-$) biểu thị tác động làm suy giảm đáp ứng.
    * Do giá trị $\text{MSE}$ của mạng nơ-ron vốn dĩ rất nhỏ, độ lớn tuyệt đối của các hệ số hồi quy trong phương trình là tương đối thấp (Podstawczyk et al. 2015).

* **Phân tích phương sai ANOVA cho mô hình bậc hai FFNN-RSM (Bảng 2)**:
  * Độ chính xác và độ tin cậy của mô hình hồi quy RSM được kiểm định thông qua phân tích phương sai (Analysis of Variance - ANOVA) trình bày tại Bảng 2.
  * Tiêu chuẩn ý nghĩa thống kê: Giá trị $p\text{-value} < 0.050$ xác nhận nhân tố hoặc tương tác có ảnh hưởng đáng kể đến quá trình dự đoán đáp ứng.
  * Các số hạng đạt mức ý nghĩa thống kê ($p < 0.050$) gồm: $A, B, C, E, F, AE, AF, BC$ và $CE$.
  * Thứ tự mức độ ảnh hưởng của các yếu tố chính:
    * Số hạng tuyến tính của hàm huấn luyện ($E$) có mức ý nghĩa vượt trội nhất với giá trị $F = 227.38$ và $p < 0.0001$.
    * Số lượng nơ-ron ($A$) là yếu tố quan trọng thứ hai với $F = 22.54$ và $p < 0.0001$.
    * Kế tiếp theo thứ tự giảm dần của mức ý nghĩa là hàm kích hoạt ($F$, $F = 9.51$, $p = 0.0027$), hệ số xung lượng ($C$, $F = 6.67$, $p = 0.0113$), và tốc độ học ($B$, $F = 4.01$, $p = 0.0482$).
    * Trái lại, số lượng epoch ($D$) thể hiện tác động không đáng kể đến biến đáp ứng với giá trị $F$ rất nhỏ ($1.16$) và $p = 0.2839$.
    * Các số hạng tương tác và bậc hai gồm $AB, AC, AD, BD, BE, BF, CD, CF, DE, DF, EF, A^2, B^2, C^2$ và $D^2$ đều có $p > 0.050$, khẳng định vai trò thứ yếu của chúng trong quá trình huấn luyện mạng FFNN.
  * **Bảng 2.** Phân tích phương sai (ANOVA) cho mô hình bậc hai siêu tham số FFNN:
    | Nguồn biến thiên (Source) | Tổng bình phương (Sum of squares) | Bậc tự do (df) | Trung bình bình phương (Mean square) | Giá trị F (F-value) | Giá trị p (p-Value) | Ghi chú (Remark) |
    | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
    | **Mô hình (Model)** | $22791.82$ | $25$ | $911.67$ | $12.88$ | $< 0.0001$ | Có ý nghĩa (Significant) |
    | $A$: Số nơ-ron (No. of neurons) | $1595.33$ | $1$ | $1595.33$ | $22.54$ | $< 0.0001$ | Có ý nghĩa (Significant) |
    | $B$: Tốc độ học (Learning rate) | $283.68$ | $1$ | $283.68$ | $4.01$ | $0.0482$ | Có ý nghĩa (Significant) |
    | $C$: Xung lượng (Momentum) | $472.24$ | $1$ | $472.24$ | $6.67$ | $0.0113$ | Có ý nghĩa (Significant) |
    | $D$: Số epoch (No. of epoch) | $82.19$ | $1$ | $82.19$ | $1.16$ | $0.2839$ | Không có ý nghĩa |
    | $E$: Hàm huấn luyện (Train. Func.) | $16091.19$ | $1$ | $16091.19$ | $227.38$ | $< 0.0001$ | Có ý nghĩa (Significant) |
    | $F$: Hàm kích hoạt (Activ. Func.) | $672.78$ | $1$ | $672.78$ | $9.51$ | $0.0027$ | Có ý nghĩa (Significant) |
    | $AB$ | $66.78$ | $1$ | $66.78$ | $0.9437$ | $0.3338$ | Không có ý nghĩa |
    | $AC$ | $0.3032$ | $1$ | $0.3032$ | $0.0043$ | $0.9480$ | Không có ý nghĩa |
    | $AD$ | $9.29$ | $1$ | $9.29$ | $0.1313$ | $0.7179$ | Không có ý nghĩa |
    | $AE$ | $906.33$ | $1$ | $906.33$ | $12.81$ | $0.0005$ | Có ý nghĩa (Significant) |
    | $AF$ | $733.12$ | $1$ | $733.12$ | $10.36$ | $0.0018$ | Có ý nghĩa (Significant) |
    | $BC$ | $483.92$ | $1$ | $483.92$ | $6.84$ | $0.0104$ | Có ý nghĩa (Significant) |
    | $BD$ | $16.57$ | $1$ | $16.57$ | $0.2342$ | $0.6295$ | Không có ý nghĩa |
    | $BE$ | $23.15$ | $1$ | $23.15$ | $0.3272$ | $0.5687$ | Không có ý nghĩa |
    | $BF$ | $1.54$ | $1$ | $1.54$ | $0.0217$ | $0.8831$ | Không có ý nghĩa |
    | $CD$ | $11.85$ | $1$ | $11.85$ | $0.1674$ | $0.6833$ | Không có ý nghĩa |
    | $CE$ | $561.16$ | $1$ | $561.16$ | $7.93$ | $0.0059$ | Có ý nghĩa (Significant) |
    | $CF$ | $3.57$ | $1$ | $3.57$ | $0.0504$ | $0.8229$ | Không có ý nghĩa |
    | $DE$ | $79.55$ | $1$ | $79.55$ | $1.12$ | $0.2918$ | Không có ý nghĩa |
    | $DF$ | $0.0205$ | $1$ | $0.0205$ | $0.0003$ | $0.9865$ | Không có ý nghĩa |
    | $EF$ | $0.0640$ | $1$ | $0.0640$ | $0.0009$ | $0.9761$ | Không có ý nghĩa |
    | $A^2$ | $40.99$ | $1$ | $40.99$ | $0.5792$ | $0.4485$ | Không có ý nghĩa |
    | $B^2$ | $33.75$ | $1$ | $33.75$ | $0.4769$ | $0.4915$ | Không có ý nghĩa |
    | $C^2$ | $40.67$ | $1$ | $40.67$ | $0.5746$ | $0.4503$ | Không có ý nghĩa |
    | $D^2$ | $1.44$ | $1$ | $1.44$ | $0.0203$ | $0.8870$ | Không có ý nghĩa |
    | Phần dư (Residual) | $6652.29$ | $94$ | $70.77$ | — | — | — |
    | Sai số thiếu khớp (Lack of fit) | $5019.59$ | $74$ | $67.83$ | $0.8309$ | $0.7237$ | Không có ý nghĩa (Not significant) |
    | Sai số thuần túy (Pure error) | $1632.70$ | $20$ | $81.64$ | — | — | — |
    | Tổng cộng hiệu chỉnh (Cor total) | $29444.12$ | $119$ | — | — | — | — |

* **Đánh giá độ tương thích, độ chính xác thống kê và phân tích phần dư**:
  * Kiểm định sai số thiếu khớp (Lack-of-fit test): Kết quả kiểm định đạt giá trị $F = 0.8309$ và $p = 0.7237$ ($> 0.050$), xác nhận sai số thiếu khớp không có ý nghĩa thống kê, chứng minh mô hình bậc hai hoàn toàn tương thích và khớp chuẩn xác với dữ liệu thực nghiệm.
  * Các hệ số đánh giá độ khớp (Determination coefficient - $R^2$):
    * Theo hướng dẫn thực hành của Elfghi (2016), mức $R^2 \ge 0.75$ được khuyến nghị để bảo đảm phản ánh chính xác độ lệch tổng thể của dữ liệu thực nghiệm so với giá trị trung bình.
    * Các hệ số đo lường thực tế gồm $R^2 = 0.7741$, $R^2_{\text{adj}} = 0.7140$ (hệ số xác định hiệu chỉnh), và $R^2_{\text{pred}} = 0.6309$ (hệ số xác định dự đoán), chứng minh mức độ tương đồng chặt chẽ giữa giá trị nghịch đảo MSE thực nghiệm và giá trị dự báo từ mô hình hồi quy.
  * Độ chính xác thích hợp (Adequate precision): Đạt mức $13.2814$, vượt xa ngưỡng chuẩn tối thiểu là $4$, xác nhận tỷ số tín hiệu trên nhiễu (signal-to-noise ratio) đạt mức tin cậy cao để mô hình điều hướng không gian thiết kế.
  * Sự khác biệt về mức ý nghĩa của số epoch ($D$) giữa hai phương pháp:
    * Trong phương pháp thiết kế nhân tố hai mức (two-level factorial, Hình S3(a)), số epoch từng thể hiện ý nghĩa thống kê thông qua các tương tác hai yếu tố.
    * Trong phương pháp bề mặt đáp ứng RSM, số epoch lại được ước lượng là không có ý nghĩa ($p = 0.2839$).
    * Nguyên nhân là trong RSM, mức ý nghĩa của tham số được đánh giá thông qua kiểm định thống kê trên hệ số hồi quy; do hệ số hồi quy của số epoch không khác biệt có ý nghĩa so với $0$, tham số này được xác định là không có ý nghĩa thống kê.
  * Phân tích phần dư (Residuals analysis) kiểm chứng tính thỏa đáng và độ tin cậy của mô hình:
    * Đồ thị xác suất chuẩn so với phần dư student hóa (Hình S5(a)): Các điểm dữ liệu nằm bám sát trên một đường thẳng, xác nhận các sai số tuân theo phân phối chuẩn với phương sai không đổi (Pashaei et al. 2023).
    * Đồ thị kiểm định giả thuyết phương sai không đổi (Hình S5(b)): Các điểm phần dư student hóa ngoại (externally studentized residuals) phân bố ngẫu nhiên đồng đều ở cả phía trên và phía dưới trục hoành trong dải $[-3.6612, +3.6612]$.
    * Cả kiểm định ANOVA lẫn phân tích phần dư đều chứng minh mô hình hồi quy đạt tính hợp lệ khoa học cao.

* **Phân tích đồ thị nhiễu loạn và tương tác siêu tham số (Hình 6)**:
  * Đồ thị nhiễu loạn (Perturbation plot) giữ vai trò then chốt trong việc phân tích cách biến đáp ứng ($1/\text{MSE}$) thay đổi khi điều chỉnh từng nhân tố rời khỏi điểm tham chiếu chuẩn (reference point), trong điều kiện các nhân tố còn lại được cố định tại giá trị tham chiếu:
    * Khảo sát so sánh tác động của tất cả các yếu tố định lượng gồm số lượng nơ-ron ($A$), tốc độ học ($B$), hệ số xung lượng ($C$), và số epoch ($D$) tại điểm tham chiếu; trong khi các yếu tố phân loại gồm hàm huấn luyện và hàm kích hoạt được cố định tương ứng tại `trainlm` và `ReLu`.
    * Biến đáp ứng $1/\text{MSE}$ biến thiên nghịch đảo so với sai số $\text{MSE}$, theo đó mục tiêu tối ưu hóa đòi hỏi giá trị $1/\text{MSE}$ phải đạt mức cực đại càng cao càng tốt.
  * Đồ thị nhiễu loạn và phân tích tương tác khẳng định số lượng nơ-ron có ảnh hưởng vượt trội nhất đến $1/\text{MSE}$, tiếp theo là tương tác mạnh giữa learning rate và momentum, trong khi số epoch hầu như không ảnh hưởng đáng kể:
    * **Hình 6.** Đồ thị phân tích ảnh hưởng và tương tác của các siêu tham số đến giá trị nghịch đảo sai số ($1/\text{MSE}$) của mô hình FFNN: (a) Đồ thị nhiễu loạn (perturbation plot), (b) Đồ thị một yếu tố số epoch, (c) Đồ thị bề mặt đáp ứng 3D tương tác giữa learning rate và momentum, (d) Đồ thị đường mức (contour plot) của learning rate và momentum
      * <img src="assets/fig_06_p15.jpeg" alt="Hình 6" />
      * **Hình này chứng minh điều gì**
        * Số lượng nơ-ron (yếu tố $A$) là yếu tố chi phối mạnh nhất đến $1/\text{MSE}$, đồng thời learning rate (tốc độ học, $B$) và momentum (động lượng, $C$) có tương tác phi tuyến rõ rệt, trong khi số epoch ($D$) hầu như không ảnh hưởng.
      * **Từ đâu mà thấy được**
        * Đồ thị nhiễu loạn (a) và đơn yếu tố (b): Yếu tố $A$ có độ dốc lớn nhất đưa $1/\text{MSE}$ từ $< 25$ tại $-1{,}000$ lên $> 46$ tại $+1{,}000$ (mức mã hóa), trong khi đường $D$ gần như nằm ngang phẳng quanh mức $37$ suốt dải $100\text{--}300\text{ epoch}$.
        * Đồ thị $3\text{D}$ (c) và đường mức (d): Tương tác giữa $B$ và $C$ tạo bề mặt vòm cong với các đường elip đồng tâm, đạt cực đại $1/\text{MSE} > 37{,}3$ trong khoảng learning rate $0{,}25\text{--}0{,}31$ và momentum $0{,}68\text{--}0{,}80$, vượt trội so với vùng giá trị thấp $< 30$.
  * Phân tích đồ thị đơn biến số epoch (Hình 6(b)):
    * Đường biểu diễn gần như đi ngang phẳng xác nhận số lượng epoch hầu như không chi phối giá trị $1/\text{MSE}$.
    * Số epoch thấp biểu thị tốc độ huấn luyện nhanh hơn do đòi hỏi ít vòng lặp hơn để đạt sự hội tụ; hiện tượng này diễn ra do quá trình huấn luyện tự động dừng ngay khi sai số đạt mức cực tiểu, thường xuất hiện trước khi chạm đến giới hạn số epoch thiết lập (Salam et al. 2021).
    * Kết quả này hoàn toàn nhất quán với kết quả mô phỏng theo phương pháp truyền thống ở Mục 3.1.1 (Hình 4(d)), tại đó mọi mô hình FFNN đều tạo ra các giá trị MSE thấp với sự biến thiên xu hướng là không đáng kể.
  * Phân tích tương tác giữa tốc độ học (learning rate) và hệ số xung lượng (momentum) qua đồ thị 3D và đồ thị đường mức (Hình 6(c) và 6(d)):
    * Biểu đồ bề mặt đáp ứng ba chiều ($3\text{D}$) và đồ thị đường mức hai chiều ($2\text{D}$) mô tả mối liên hệ tương hỗ giữa $1/\text{MSE}$ với hai yếu tố kết hợp là tốc độ học và hệ số xung lượng; trong đó vùng màu xanh lam chỉ thị các giá trị $1/\text{MSE}$ cao nhất.
    * Giá trị $1/\text{MSE}$ tăng lên rõ rệt khi đồng thời tăng tốc độ học và hệ số xung lượng, thể hiện một đường cong lý tưởng giữa hai tham số này nhờ hiệu ứng tương tác hiệp đồng giúp gia tốc quá trình học tập của mạng (accelerated learning).
    * Đường cong phản ứng duy trì dạng tuyến tính nếu tốc độ học quá thấp, và chuyển sang dạng đường cong hàm mũ nghịch đảo khi tốc độ học ở mức cao.
    * Tuy nhiên, tốc độ học quá cao có thể khiến hàm mất mát suy giảm quá nhanh và làm mô hình rơi vào bẫy điểm cực tiểu cục bộ (local minima).
    * Vùng đạt giá trị $1/\text{MSE}$ cực đại tối ưu được ghi nhận trong khoảng tốc độ học từ $0.13$ đến $0.31$ và hệ số xung lượng trong dải $0.6$–$0.84$.

* **Tối ưu hóa số và bộ siêu tham số tối ưu cho mô hình FFNN-RSM**:
  * Ba siêu tham số gồm số lượng nơ-ron, tốc độ học và hệ số xung lượng đóng vai trò cốt lõi chi phối giá trị $1/\text{MSE}$, hoàn toàn phù hợp với kết quả kiểm định mô hình hồi quy ANOVA.
  * Quy trình tối ưu hóa số (numerical optimization) được thực hiện thông qua phần mềm Design-Expert:
    * Tiêu chí tối ưu cho toàn bộ các yếu tố siêu tham số được đặt ở chế độ "trong khoảng" ('in range').
    * Tiêu chí cho biến đáp ứng $\text{MSE}$ được thiết lập ở chế độ "cực tiểu hóa" ('minimum').
  * Các giá trị siêu tham số tối ưu được đề xuất bởi RSM với hàm độ mong muốn (desirability value) đạt mức tuyệt đối bằng $1$ bao gồm:
    * Số lượng nơ-ron trong tầng ẩn: $15$ ($A = 15$)
    * Tốc độ học (learning rate): $0.23$ ($B = 0.23$)
    * Hệ số xung lượng (momentum): $0.65$ ($C = 0.65$)
    * Số epoch: $287$ ($D = 287$)
    * Hàm huấn luyện: `trainlm` (thuật toán Levenberg-Marquardt)
    * Hàm kích hoạt: `ReLu` (Rectified Linear Unit)
  * Bộ thông số tối ưu tối hảo này được áp dụng trực tiếp cho mô hình FFNN nhằm dự đoán động học thông lượng dòng thấm (permeate flux) trong hệ thống SMBR xử lý nước thải POME.
