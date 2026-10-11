### 3.2. HPO for the MLP and LSTM model

* Lịch sử thử nghiệm tối ưu hóa siêu tham số (hyperparameter optimization - HPO) và so sánh hiệu năng giữa hai mô hình Perceptron đa lớp (multilayer perceptron - MLP) và Mạng bộ nhớ ngắn-dài hạn (long short-term memory - LSTM) (Fig. 4(a), (b)):
  * Giá trị $R^2$ trên tập kiểm tra (test set) cao nhất:
    * Mô hình MLP đạt $R^2 = 0{,}9183$, xuất hiện ở lượt thử nghiệm thứ 789 (789th trial).
    * Mô hình LSTM đạt $R^2 = 0{,}8954$, xuất hiện ở lượt thử nghiệm thứ 210 (210th trial).
  * Phân bố giá trị $R^2$ và độ ổn định qua 1000 lượt thử nghiệm (1000 trials):
    * Phần lớn các tổ hợp siêu tham số của mô hình MLP đạt giá trị $R^2 > 0{,}75$.
    * Mô hình LSTM có phân bố các giá trị $R^2 > 0{,}50$ đồng đều hơn, tuy nhiên giá trị $R^2$ có xu hướng dao động quanh ngưỡng $0{,}75$ ở phần lớn các lượt thử nghiệm.
    * Mô hình MLP không chỉ thể hiện độ chính xác cực đại vượt trội mà còn duy trì kết quả nhất quán hơn trong toàn bộ 1000 lượt thử nghiệm, cho thấy mô hình MLP có độ ổn định cao hơn trong các giới hạn siêu tham số đã xác định.
    * Hiệu năng $R^2$ tổng thể của LSTM kém hơn và kém ổn định hơn so với MLP.
  * Hiện tượng giá trị $R^2$ âm trong hồi quy phi tuyến:
    * Giá trị $R^2$ thông thường không âm trong các mô hình hồi quy tuyến tính (linear regression).
    * Trong các mô hình hồi quy phi tuyến như mạng nơ-ron nhân tạo (artificial neural networks - ANN), độ chính xác thấp bắt nguồn từ hiệu năng mô hình kém sẽ dẫn đến giá trị $R^2$ âm (Spiess and Neumeyer, 2010).
    * Mô hình LSTM xuất hiện nhiều giá trị $R^2$ âm hơn so với mô hình MLP, chứng minh thêm rằng mô hình MLP đạt độ ổn định cao hơn.
  * **Hình 4.** Biến thiên giá trị $R^2$ trong lịch sử thử nghiệm tối ưu hóa siêu tham số (HPO) và mức độ quan trọng của các siêu tham số trong quy trình HPO.
    * <img src="assets/fig_04_p8.jpeg" alt="Hình 4" />
    * **Hình này chứng minh điều gì**
      * Optimizer chi phối vượt trội hiệu năng mô hình, đạt độ quan trọng 0.36 ở MLP và 0.52 ở LSTM.
      * Quá trình HPO đạt giá trị $R^2$ tiệm cận đỉnh (> 0.85) chỉ sau số ít lượt thử nghiệm ban đầu.
    * **Từ đâu mà thấy được**
      * (a), (b): Trục Ox Trial (0–1000), Oy $R^2$ (-1–1.0); đường Best Value đỏ nhanh chóng vượt 0.85 và đi ngang sát 1.0.
      * (c), (d): Trục Oy Hyperparameters, Ox Importance for Objective Value ($R^2$); Optimizer đứng đầu ở cả hai mô hình (0.36 và 0.52).

* Xếp hạng mức độ quan trọng của các siêu tham số đối với giá trị $R^2$ trong quy trình HPO (Fig. 4(c), (d) và Table 4):
  * Khi chuẩn hóa tổng tỷ lệ đóng góp (overall contribution rate) của tất cả các siêu tham số bằng $1$, bộ tối ưu hóa (optimizer) đóng vai trò đóng góp lớn nhất ở cả hai mô hình:
    * Đạt mức $0{,}36$ ở mô hình MLP.
    * Đạt mức $0{,}52$ ở mô hình LSTM.
  * Thứ hạng và mức độ đóng góp của các siêu tham số đối với mô hình MLP:
    * 1. Bộ tối ưu hóa (optimizer): đóng góp $0{,}36$ (lớn nhất).
    * 2. Hàm mất mát (loss function): đóng góp $0{,}19$ (đứng thứ hai sau optimizer).
    * 3. Tốc độ học (learning rate): đóng góp $0{,}17$ (xếp thứ ba).
    * 4. Hàm kích hoạt của lớp ẩn thứ nhất (activation function of 1st hidden layer): đóng góp $0{,}15$ (xếp thứ tư).
    * 5. Tỷ lệ loại bỏ nơ-ron ngẫu nhiên (dropout rate): đóng góp $0{,}05$.
    * 6. Số lượng nơ-ron (number of neurons): đóng góp $0{,}03$.
    * 7. Suy giảm trọng số (weight decay): đóng góp $0{,}03$.
    * 8. Số lớp ẩn (number of hidden layers): đóng góp $0{,}02$.
  * Thứ hạng và mức độ đóng góp của các siêu tham số đối với mô hình LSTM:
    * 1. Bộ tối ưu hóa (optimizer): đóng góp $0{,}52$ (chi phối áp đảo).
    * 2. Số lớp ẩn (number of hidden layers): xếp thứ hai với tỷ lệ đóng góp $0{,}15$.
    * 3. Hàm mất mát (loss function): xếp thứ ba với tỷ lệ đóng góp $0{,}12$.
    * 4. Số lượng nơ-ron (number of neurons): xếp thứ tư với tỷ lệ đóng góp $0{,}10$.
    * 5. Tỷ lệ loại bỏ nơ-ron ngẫu nhiên (dropout rate): đóng góp $0{,}03$.
    * 6. Số đơn vị LSTM (number of LSTM units): đóng góp $0{,}03$ (chỉ áp dụng riêng cho mô hình LSTM).
    * 7. Tốc độ học (learning rate): đóng góp $0{,}02$.
    * 8. Suy giảm trọng số (weight decay): đóng góp $0{,}02$.
    * 9. Hàm kích hoạt (activation functions): xếp cuối cùng với tỷ lệ đóng góp $0{,}01$.
  * Vai trò cơ chế của bộ tối ưu hóa (optimizer) trong mạng nơ-ron nhân tạo:
    * Trong mạng nơ-ron (NNs), optimizer điều khiển quá trình hiệu chỉnh các tham số của mô hình xuyên suốt quá trình huấn luyện nhằm tối thiểu hóa hàm mất mát (loss) hoặc tối đa hóa độ chính xác mô hình.
    * Optimizer quyết định trực tiếp phương thức tính toán gradient và cơ chế cập nhật trọng số mô hình.
    * Tham số optimizer có tác động chi phối mạnh nhất đến hành vi hội tụ (convergence behavior), năng lực tổng quát hóa (generalizability), và hiệu năng tổng thể của các mô hình ANN.
  * **Bảng 4.** Độ quan trọng của siêu tham số trong MLP và LSTM.
    * <img src="assets/table_04_p8.png" alt="Bảng 4" />
    * **Bảng này chứng minh điều gì**
      * Optimizers chi phối hiệu năng lớn nhất ở cả hai mô hình ($0.36$ ở MLP và $0.52$ ở LSTM), định hình quá trình hội tụ và tối ưu trọng số.
      * Yếu tố ảnh hưởng kế tiếp phân hóa: MLP phụ thuộc hàm mất mát ($0.19$), còn LSTM phụ thuộc số lớp ẩn ($0.15$).
    * **Từ đâu mà thấy được**
      * Cột "Optimizers" có giá trị lớn nhất trên cả 2 dòng: MLP đạt $0.36$ và LSTM đạt $0.52$.
      * Giá trị thấp nhất nằm ở cột "Number of hidden layers" đối với MLP ($0.02$) và "Activation functions" đối với LSTM ($0.01$).

* Phương pháp luận tối ưu hóa siêu tham số (HPO) và so sánh các thuật toán tìm kiếm:
  * Thuật toán ước lượng Parzen theo cấu trúc cây (Tree-structured Parzen Estimator - TPE) và ý nghĩa của HPO:
    * Nghiên cứu sử dụng thuật toán TPE để tìm kiếm tổ hợp siêu tham số tối đa hóa giá trị mục tiêu $R^2$ trong không gian giới hạn siêu tham số cho trước.
    * HPO cải thiện đáng kể độ chính xác của mô hình và hiệu quả của quy trình phát triển, mang ý nghĩa quan trọng trong việc thiết lập mô hình dự đoán tắc nghẽn màng của hệ thống AnMBR quy mô lớn.
    * HPO là một bước đi có giá trị bất kể mục tiêu cụ thể của nghiên cứu, nhờ khả năng thúc đẩy quá trình xây dựng mô hình chính xác hơn, mạnh mẽ hơn (robust), và đáng tin cậy hơn (reliable).
    * Mục tiêu chính của HPO là nâng cao độ chính xác dự đoán; quan trọng hơn nữa, mô hình sau tối ưu hóa có thể tận dụng hiệu quả các mối tương quan giữa các đặc trưng đầu vào (input features) và biến phản ứng (response variable) (Zhu et al., 2023).
  * So sánh các phương pháp tối ưu hóa siêu tham số khác nhau:
    * Framework Optuna cung cấp giải pháp tiếp cận tự động hóa tinh vi.
    * Phương pháp thử và sai (trial-and-error) (Viet and Jang, 2021): các cấu hình siêu tham số được chọn lựa thủ công và đánh giá hiệu năng; phương pháp tuy đơn giản và đôi khi đạt kết quả thỏa đáng nhưng đòi hỏi nhiều thời gian cùng tài nguyên tính toán hơn với mức độ bảo đảm tối ưu hóa thấp hơn.
    * Thuật toán di truyền (Genetic Algorithms - GA) (Yao et al., 2022): mô phỏng quá trình chọn lọc tự nhiên để tìm kiếm tổ hợp tối ưu; phương pháp mô phỏng sinh học này mã hóa siêu tham số thành các gen và tiến hóa chúng qua các thế hệ dựa trên hàm thích nghi (fitness function, thông thường là điểm số kiểm định mô hình).
    * Tìm kiếm theo lưới (Grid Search): tìm kiếm vét cạn qua tập hợp các siêu tham số được định nghĩa trước.
    * Tìm kiếm ngẫu nhiên (Random Search): lấy mẫu ngẫu nhiên các thiết lập siêu tham số từ các phân phối xác định.
    * Mỗi phương pháp đều sở hữu ưu điểm và giới hạn riêng, phù hợp với các dạng bài toán và ràng buộc tài nguyên tính toán khác nhau.

* Chi phí tính toán, nền tảng phần cứng và sự đánh đổi thực tiễn (computational costs and practical trade-offs):
  * Cấu hình phần cứng và thời gian thực thi HPO:
    * Toàn bộ quá trình mô hình hóa tính toán trong nghiên cứu được thực hiện trên CPU Intel Core i5-1135G7 với tốc độ xung nhịp $2{,}40\text{ GHz}$.
    * Thời gian cần thiết để hoàn thành quy trình HPO với 1000 lượt thử nghiệm (1000 trials) trong các điều kiện đồng nhất:
      * Mô hình MLP: xấp xỉ $7\text{ giờ}$ ($7\text{ h}$).
      * Mô hình LSTM: xấp xỉ $12\text{ giờ}$ ($12\text{ h}$) — đòi hỏi thời gian tính toán kéo dài nhất do độ phức tạp cố hữu của các đơn vị LSTM (inherent complexity of LSTM units).
      * Mô hình MLP đơn giản hóa (simplified MLP - s-MLP): xấp xỉ $3\text{ giờ}$ ($3\text{ h}$) — nhờ kiến trúc thô sơ nên tiêu tốn ít thời gian tính toán nhất; tuy nhiên độ chính xác $R^2$ cực đại chỉ đạt $0{,}8317$, kém hơn đáng kể so với các mô hình dự đoán tắc nghẽn màng khác được tổng hợp trong Table 5.
  * Cân nhắc đánh đổi thực tiễn khi triển khai HPO:
    * Về mặt lý thuyết, việc gia tăng số lượng lượt thử nghiệm có thể làm tăng xác suất đạt được cấu hình siêu tham số tối ưu.
    * Mặc dù vậy, lợi thế này phải được cân nhắc và cân bằng với các ràng buộc thực tế, bao gồm hạn chế về tài nguyên tính toán và chi phí thời gian.
    * Do đó, việc triển khai HPO trong thực tế phát triển mô hình cần được đánh giá thỏa đáng, xét đồng thời cả yêu cầu về hiệu năng dự đoán lẫn chi phí tính toán liên quan trong bối cảnh và khu vực ứng dụng cụ thể.
