### ANN modeling results

* **Nguồn dữ liệu thực nghiệm và các biến số mô hình (Experimental dataset source and model variables)**:
    * Dữ liệu thực nghiệm được kế thừa từ công trình của Ding et al. [26] dùng cho mô hình hóa mạng nơ-ron nhân tạo (artificial neural network - ANN).
    * **Các biến phụ thuộc (Dependent factors / output targets)**:
        * Nồng độ nitơ amoniac (ammonia nitrogen concentration).
        * Nồng độ phosphat (phosphate concentration).
        * Hiệu suất loại bỏ (removal efficiency) của cả nitơ amoniac và phosphat.
    * **Các biến độc lập (Independent variables / model inputs)**:
        * Thời gian vận hành (Time).
        * Độ $\text{pH}$.
        * Nồng độ tổng carbon hữu cơ (Total Organic Carbon - TOC concentration).

* **Chiến lược lựa chọn cấu trúc mạng nơ-ron tối ưu (Optimal ANN architecture selection strategy)**:
    * Tô-pô tối ưu (optimal topology) của các mô hình ANN được xác định thông qua quy trình thử - sai có hệ thống (trial-and-error procedure).
    * Số lượng nơ-ron trong lớp ẩn (number of neurons in the hidden layer) được khảo sát và biến thiên lặp lại từng bước từ $1$ đến $20$ nơ-ron (iteratively varied from 1 to 20).
    * **Tiêu chí lựa chọn cấu trúc tối ưu**: Cấu trúc kiến trúc đạt giá trị sai số toàn phương trung bình thấp nhất trên tập kiểm định (lowest mean squared error - MSE on the validation set) được lựa chọn làm mô hình khớp tốt nhất (best-fit architecture).

* **Các thông số kiến trúc và độ chính xác tối ưu của các mô hình ANN (Optimal ANN architectures and accuracy parameters)**:
    * Kết quả cấu trúc tối ưu và các thông số độ chính xác cho từng biến phụ thuộc được chi tiết hóa trong Bảng 1:
        * **Mô hình nitơ amoniac dựa trên dữ liệu $\text{pH}$ (Ammonia nitrogen based on pH data)**:
            * Cấu trúc mạng (Structure): $[2\ 5]$ ($2$ nơ-ron ở lớp ẩn thứ nhất và $5$ nơ-ron ở lớp ẩn thứ hai).
            * Hàm kích hoạt chuyển tiếp (Transfer function): kết hợp [Logsigmoid Tansigmoid].
            * Hệ số tương quan (Correlation coefficient): $R = 0.99743$.
            * Sai số toàn phương trung bình: $\text{MSE} = 2.04\times 10^{-2}$ ($2.04\text{E-}02$).
        * **Mô hình nitơ amoniac dựa trên dữ liệu TOC (Ammonia nitrogen based on TOC data)**:
            * Cấu trúc mạng: $[2\ 4]$ ($2$ nơ-ron và $4$ nơ-ron ở các lớp ẩn).
            * Hàm kích hoạt chuyển tiếp: [Logsigmoid Logsigmoid].
            * Hệ số tương quan: $R = 0.99791$.
            * Sai số toàn phương trung bình: $\text{MSE} = 3.57\times 10^{-2}$ ($3.57\text{E-}02$).
        * **Mô hình phosphat dựa trên dữ liệu $\text{pH}$ (Phosphate based on pH data)**:
            * Cấu trúc mạng: $[3\ 3]$ ($3$ nơ-ron và $3$ nơ-ron ở các lớp ẩn).
            * Hàm kích hoạt chuyển tiếp: [Tansigmoid Logsigmoid].
            * Hệ số tương quan: $R = 0.99647$.
            * Sai số toàn phương trung bình: $\text{MSE} = 1.36\times 10^{-2}$ ($1.36\text{E-}02$).
        * **Mô hình phosphat dựa trên dữ liệu TOC (Phosphate based on TOC data)**:
            * Cấu trúc mạng: $[5\ 2]$ ($5$ nơ-ron và $2$ nơ-ron ở các lớp ẩn).
            * Hàm kích hoạt chuyển tiếp: [Tansigmoid Logsigmoid].
            * Hệ số tương quan: $R = 0.99722$.
            * Sai số toàn phương trung bình: $\text{MSE} = 2.75\times 10^{-2}$ ($2.75\text{E-}02$).
    * **Bảng 1.** Cấu trúc tối ưu và thông số độ chính xác của mạng ANN
        * <img src="assets/table_01_p9.png" alt="Bảng 1" />
        * **Bảng này chứng minh điều gì**
            * Mô hình ANN đạt cấu trúc tối ưu với 2 lớp ẩn (từ $[2\ 4]$ đến $[5\ 2]$ nơ-ron) kết hợp hàm Logsigmoid/Tansigmoid cho các biến Ammonia nitrogen và Phosphate.
        * **Từ đâu mà thấy được**
            * Cột "Structure" và "Transfer function" thể hiện số nơ-ron lớp ẩn và hàm kích hoạt tương ứng cho từng biến mô phỏng.
            * Cột "$R$" ghi nhận giá trị tương quan cao cho cả 4 mô hình, từ $0.99647$ (dòng 3) đến $0.99791$ (dòng 2).
#### Addressing model robustness and overfitting

* **Thách thức tập dữ liệu giới hạn và sự cần thiết của kiểm soát quá khớp (Small dataset challenge and overfitting control)**:
    * Do kích thước tập dữ liệu thực nghiệm bị hạn chế (chỉ gồm $44$ điểm dữ liệu thực nghiệm), các biện pháp kỹ thuật đặc thù đã được thiết lập để đảm bảo khả năng diễn giải mô hình (model interpretability) và chủ động ngăn chặn hiện tượng quá khớp (overfitting).

* **Cơ chế điều chuẩn dừng sớm trong tiến trình huấn luyện (Early Stopping regularization mechanism)**:
    * Chiến lược giảm thiểu quá khớp chính (primary mitigation strategy) là áp dụng kỹ thuật điều chuẩn dừng sớm (Early Stopping regularization).
    * Trong suốt tiến trình huấn luyện lặp (iterative training process), chỉ số $\text{MSE}$ của tập con kiểm định (Validation subset, chiếm $15\%$ dữ liệu) liên tục được theo dõi trực tiếp.
    * Thuật toán huấn luyện được cấu hình tự động dừng (halt automatically) nếu sai số trên tập kiểm định không được cải thiện trong $6$ epoch liên tiếp ($6$ consecutive epochs).
    * Cơ chế này đảm bảo mạng nơ-ron tiếp thu và học được các quy luật xu hướng chung tiềm ẩn (underlying general trends) thay vì ghi nhớ nhiễu ngẫu nhiên (memorizing noise) trong tập huấn luyện.

* **Thuật toán tối ưu hóa trọng số Levenberg-Marquardt (Levenberg-Marquardt backpropagation weight optimization)**:
    * Thuật toán lan truyền ngược Levenberg-Marquardt (LM backpropagation algorithm) được lựa chọn cho bài toán tối ưu hóa trọng số mạng.
    * Thuật toán LM được biết đến rộng rãi với tham số tắt dần (damping parameter, $\mu$), đóng vai trò cung cấp cơ chế điều chuẩn tự nhiên (natural regularization) thông qua việc luân chuyển linh hoạt giữa phương pháp hạ gradient (Gradient Descent) và phương pháp Gauss-Newton.
    * Đặc tính này giúp thuật toán LM đạt độ ổn định tính toán rất cao (highly stable), đặc biệt phù hợp và hiệu quả đối với các tập dữ liệu có kích thước nhỏ [1].

* **Đánh giá độ bền vững và năng lực tổng quát hóa của mô hình ANN (Model robustness and generalization performance)**:
    * Sự đồng nhất và nhất quán cao của các giá trị hệ số xác định $R^2$ trên toàn bộ các tập dữ liệu chứng minh năng lực mô hình:
        * Tập huấn luyện (Training dataset): $R^2 > 0.99$.
        * Tập kiểm định (Validation dataset): $R^2 > 0.99$.
        * Tập kiểm tra (Testing dataset): $R^2 > 0.9$.
    * Độ ổn định nhất quán này (được trình bày chi tiết trong Bảng 1 và trực quan hóa trong Hình 6) khẳng định mô hình ANN đã đạt được khả năng tổng quát hóa mạnh mẽ (strong generalization capabilities) đối với dữ liệu mới chưa từng thấy (unseen data).
    * **Đối sánh giữa dữ liệu thực nghiệm và đầu ra ANN về nồng độ**:
        * Dữ liệu thực nghiệm (đường màu tím) và đầu ra mô hình ANN (đường màu xanh lá) của nồng độ nitơ amoniac và phosphat nằm rất gần nhau, thể hiện xu thế tương đồng.
        * Các đường huấn luyện (đường màu cam), kiểm tra (đường màu xanh lá) và kiểm định (đường màu đỏ) phản ánh chính xác hiệu năng qua từng pha: đường huấn luyện cho thấy mô hình khớp rất tốt dữ liệu học, trong khi đường kiểm tra và kiểm định xác nhận khả năng tổng quát hóa xuất sắc.
        * Một số sai lệch nhỏ còn tồn tại giữa dữ liệu thực nghiệm và đầu ra ANN phản ánh các giới hạn tiềm ẩn của mô hình hoặc từ điều kiện thiết kế thực nghiệm (limitations of model or experimental setup).
    * **Hình 6.** Đối sánh nồng độ thực nghiệm và đầu ra ANN cho Amonia và Phosphate
        * <img src="assets/fig_07_p9.png" alt="Hình 6" />
        * **Hình này chứng minh điều gì**
            * Đầu ra ANN mô phỏng chính xác các bước nhảy nồng độ của Ammonia Nitrogen ($2 - 16\text{ mg/L}$) và Phosphate ($0.2 - 3.1\text{ mg/L}$).
        * **Từ đâu mà thấy được**
            * Ox: số mẫu theo pH ($0 - 45$) hoặc theo TOC ($0 - 35$). Oy: nồng độ Ammonia ($0 - 22\text{ mg/L}$) và Phosphate ($-0.5 - 4.5\text{ mg/L}$).
            * Đường ANN Output (màu tím) nối trùng khít qua từng điểm Experimental Data (vuông xanh) trên cả 4 đồ thị (a)–(d).

* **Dự báo hiệu suất loại bỏ chất ô nhiễm bằng mô hình ANN (Removal efficiency prediction by ANN model)**:
    * Đồ thị trong Hình 7 biểu diễn đầu ra của mô hình ANN và dữ liệu thực nghiệm đối với hiệu suất loại bỏ nitơ amoniac và phosphat:
        * Mặc dù dữ liệu thực nghiệm củng cố và hỗ trợ mạnh mẽ cho mô hình, chúng không xác định rõ xu thế của dữ liệu đầu ra xuyên suốt toàn bộ pha kiểm định và pha kiểm tra.
        * Tuy nhiên, mô hình ANN vẫn dự báo chính xác các điểm giá trị mục tiêu (accurately predicted the target points) trên toàn dải hiệu suất loại bỏ.
    * **Hình 7.** Đối sánh hiệu suất khử thực nghiệm và đầu ra ANN cho Amonia và Phosphate
        * <img src="assets/fig_08_p10.png" alt="Hình 7" />
        * **Hình này chứng minh điều gì**
            * Đường cong ANN bám sát dữ liệu thực nghiệm qua toàn bộ các dao động cực đại và cực tiểu ($0 - 90\%$).
        * **Từ đâu mà thấy được**
            * Ox: Thứ tự dữ liệu theo pH ($0 - 45$) hoặc TOC ($0 - 35$); Oy: Hiệu suất loại bỏ ($0 - 100\%$).
            * Đồ thị (a)–(d): Đường hồng (ANN Output) đi qua chính xác các điểm thực nghiệm (vuông xanh).
            * Cả ba tập Train, Test và Validation đều phân bố trùng khít với đường mô phỏng ANN.
