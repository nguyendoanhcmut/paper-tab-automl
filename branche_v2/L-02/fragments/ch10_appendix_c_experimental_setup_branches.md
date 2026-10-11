## Appendix C: Experimental Setup

### C.1 Datasets

* **Tổng quan các tập dữ liệu thực nghiệm và phân loại tác vụ (Bảng 7):**
  * Lựa chọn đa dạng các tập dữ liệu mã nguồn mở và đáng tin cậy từ OpenML và Kaggle nhằm kiểm chứng toàn diện năng lực của SymboLLM-FE.
  * Các tập dữ liệu bao quát $3$ nhóm tác vụ học máy chính: phân loại nhị phân (binary classification), phân loại đa lớp (multi-class classification) và hồi quy (regression).
  * Miền ứng dụng trải rộng qua nhiều lĩnh vực thực tế khác nhau như tài chính (finance) và y tế/chăm sóc sức khỏe (healthcare).
  * Thông tin chi tiết về các tập dữ liệu được sử dụng được trình bày trong Bảng 7:
  * **Bảng 7.** Danh mục và đặc trưng của 10 tập dữ liệu benchmark và Kaggle
    * <img src="assets/table_07_p15.png" alt="Bảng 7" />
    * **Bảng này chứng minh điều gì**
      * Đa dạng quy mô mẫu từ hàng nghìn đến hàng vạn dòng và số lượng đặc trưng đa dạng
    * **Từ đâu mà thấy được**
      * Các cột Dataset, Task Type, # Samples, # Numerical Features, # Categorical Features

* **Chi tiết thông số và đặc điểm của từng tập dữ liệu thực nghiệm:**
  * **Tập dữ liệu Credit-g:**
    * Tác vụ: Phân loại nhị phân (Binary Classification).
    * Quy mô: Chứa $1{,}000$ mẫu dữ liệu (entries/samples) cùng $20$ thuộc tính dạng phân loại / ký hiệu (categorical/symbolic attributes), được xây dựng và chuẩn bị bởi Giáo sư Hofmann (Prof. Hofmann).
    * Ý nghĩa thực tế: Mỗi mục đại diện cho một khách hàng vay vốn tín dụng từ ngân hàng, được phân loại có mức độ rủi ro tín dụng tốt (good credit risk) hoặc xấu (bad credit risk) dựa trên tập hợp các thuộc tính cá nhân và tài chính.
    * Biến mục tiêu: Xác định liệu mức tín dụng của khách hàng là tốt hay xấu (good or bad).
    * Nguồn dữ liệu: Công khai trên OpenML tại đường dẫn `https://www.openml.org/search?type=data&sort=runs&id=31&status=active` (ID: $31$).
  * **Tập dữ liệu Spaceship (Spaceship Titanic):**
    * Tác vụ: Phân loại nhị phân (Binary Classification).
    * Nguồn gốc: Tập dữ liệu thi đấu cấp độ cơ bản trên nền tảng Kaggle (beginner-level Kaggle competition dataset).
    * Bối cảnh: Đặt trong bối cảnh giả định năm $2912$, một phi thuyền chở gần $13{,}000$ hành khách va chạm với một dị thường không-thời gian (space-time anomaly), khiến gần một nửa số hành khách bị dịch chuyển sang không gian khác (transported to another dimension).
    * Quy mô: Chứa xấp xỉ $2{,}000$ bản ghi hành khách (passenger records) cùng $13$ đặc trưng (features).
    * Các đặc trưng tiêu biểu: Hành tinh xuất phát (home planet), trạng thái ngủ đông (cryo-sleep status), số hiệu buồng ngủ (cabin number), điểm đến (destination) và lịch sử chi tiêu cho các dịch vụ (spending records).
    * Biến mục tiêu: Dự đoán hành khách có bị chuyển dịch sang không gian khác hay không (`Transported`).
    * Nguồn dữ liệu: Công khai trên Kaggle tại đường dẫn `https://www.kaggle.com/competitions/spaceship-titanic`.
  * **Tập dữ liệu Cmc (Contraceptive Method Choice):**
    * Tác vụ: Phân loại đa lớp có giám sát (Supervised Multi-class Classification).
    * Quy mô: Gồm $1{,}473$ mẫu quan sát và $9$ thuộc tính (attributes/features).
    * Ý nghĩa thực tế: Dự đoán phương pháp tránh thai được lựa chọn sử dụng (gồm $3$ phân loại / danh mục) dựa trên các đặc điểm nhân khẩu và cá nhân của phụ nữ đã kết hôn.
    * Ứng dụng phổ biến: Thường xuyên được sử dụng làm bộ dữ liệu chuẩn mực để đánh giá các thuật toán phân loại trong học máy.
    * Nguồn dữ liệu: Công khai trên OpenML tại đường dẫn `https://www.openml.org/search?type=data&sort=runs&id=23&status=active` (ID: $23$).
  * **Tập dữ liệu Academic (Students Dropout and Academic Success):**
    * Tác vụ: Phân loại đa lớp (Multi-class Classification).
    * Nguồn gốc: Được thu thập và công khai trên nền tảng Kaggle.
    * Quy mô: Gồm $4{,}424$ mẫu quan sát và $36$ đặc trưng (features).
    * Thành phần dữ liệu: Chứa dữ liệu nhân khẩu học (demographic), điều kiện kinh tế - xã hội (socio-economic) và thông tin ghi danh học tập (academic enrollment data).
    * Biến mục tiêu: Dự đoán kết quả học tập của người học, phân loại sinh viên vào các danh mục như "thành công trong học tập" (academic success) hoặc "bỏ học" (dropout).
    * Góc nhìn ứng dụng: Cung cấp góc nhìn định hướng kết quả (outcome-oriented perspective) đối với thành tích và tiến độ học tập của sinh viên.
    * Nguồn dữ liệu: Công khai trên Kaggle tại đường dẫn `https://www.kaggle.com/datasets/missionjee/students-dropout-and-academic-success-dataset`.
  * **Tập dữ liệu Ailerons:**
    * Tác vụ: Hồi quy (Regression).
    * Nguồn gốc: Xuất phát từ bài toán điều khiển kỹ thuật hàng không vũ trụ thực tế (real aerospace control problem) trên máy bay tiêm kích F16.
    * Quy mô: Gồm $12{,}250$ mẫu dữ liệu và $33$ đặc trưng (features).
    * Biến mục tiêu: Dự đoán hành động điều khiển tác động lên các cánh tà điều hướng / cánh liệng (ailerons) dựa trên các thuộc tính trạng thái vận hành của máy bay.
    * Nguồn dữ liệu: Công khai trên OpenML tại đường dẫn `https://www.openml.org/search?type=data&sort=runs&id=296&status=active` (ID: $296$).
  * **Tập dữ liệu Tesla:**
    * Tác vụ: Hồi quy (Regression).
    * Nguồn gốc: Được lấy từ nền tảng Kaggle, chứa dữ liệu lịch sử giá cổ phiếu giao dịch hàng ngày của công ty Tesla Inc. (mã niêm yết: TSLA).
    * Quy mô: Gồm $6{,}906$ mẫu quan sát và $8$ đặc trưng (features).
    * Các đặc trưng tiêu biểu: Giá mở cửa (`Open`), giá cao nhất trong ngày (`High`), giá thấp nhất trong ngày (`Low`), giá đóng cửa (`Close`), giá đóng cửa điều chỉnh (`Adjusted Close`) và khối lượng giao dịch (`Volume`).
    * Ứng dụng: Thường được ứng dụng trong các bài toán dự báo chuỗi thời gian (time series forecasting) về biến động xu hướng giá cổ phiếu.
    * Nguồn dữ liệu: Công khai trên Kaggle tại đường dẫn `https://www.kaggle.com/datasets/guillemservera/tsla-stock-data`.

### C.2 Downstream Baselines

* **Lựa chọn mô hình đường cơ sở hạ nguồn (downstream baselines):**
  * Nhằm kiểm chứng năng lực tổng quát hóa (generalization) và khả năng thích ứng linh hoạt (adaptability) của SymboLLM-FE trên nhiều họ kiến trúc mô hình khác nhau, phương pháp được thử nghiệm và đánh giá trên cả các mô hình dựa trên cây (tree-based models) và các mô hình học sâu (deep learning models).
  * Đối với họ mô hình dựa trên cây (tree-based models): Lựa chọn CatBoost (Prokhorenkova et al., 2018) và XGBoost (Chen and Guestrin, 2016).
  * Đối với họ mô hình học sâu (deep learning models): Lựa chọn mạng Perceptron đa tầng (Multilayer Perceptron - MLP) (Gorishniy et al., 2021) và TabPFN (Hollmann et al., 2025).

* **Thiết lập không gian tìm kiếm siêu tham số chuẩn hóa (Bảng 8):**
  * Nhằm đảm bảo tính công bằng trong đánh giá, không gian tìm kiếm dạng lưới của các siêu tham số chuẩn hóa cho cả mô hình cây và mô hình học sâu được quy định trong Bảng 8:
  * **Bảng 8.** Lưới siêu tham số tìm kiếm cho các mô hình dự báo hạ nguồn
    * <img src="assets/table_08_p16.png" alt="Bảng 8" />
    * **Bảng này chứng minh điều gì**
      * Quy chuẩn đánh giá công bằng qua việc điều chỉnh siêu tham số chuẩn cho CatBoost, XGBoost, MLP
    * **Từ đâu mà thấy được**
      * Chi tiết không gian tìm kiếm: learning_rate, max_depth, n_estimators, regularization

* **Cấu hình chi tiết của các lưới siêu tham số (Hyperparameter Grids):**
  * **Mô hình XGBoost:**
    * Tốc độ học (Learning Rate): $\{0.01, 0.1\}$
    * Chiều sâu tối đa của cây (Max. Depth): $\{1, 5, 9\}$
    * Số lượng cây ước lượng (N Estimators): $\{10{,}000, 20{,}000, 30{,}000\}$
    * Tỷ lệ lấy mẫu con của dữ liệu (Subsample): $\{0.5, 0.8, 1.0\}$
    * Tỷ lệ lấy mẫu đặc trưng theo cây (Colsample Bytree): $\{0.5, 0.8, 1.0\}$
    * Trọng số tối thiểu của nút lá (Min Child Weight): $\{1, 3, 5\}$
  * **Mô hình CatBoost:**
    * Tốc độ học (Learning Rate): $\{0.01, 0.05, 0.1\}$
    * Chiều sâu của cây (Depth): $\{4, 6, 8\}$
    * Số vòng lặp huấn luyện (Iterations): $\{500, 1{,}000, 2{,}000\}$
  * **Mô hình MLP (Multilayer Perceptron):**
    * Kích thước số chiều các lớp ẩn (D_layers): $\{1, 8, 64, 512\}$
    * Tỷ lệ Dropout: Phân phối đều $\text{Uniform}\{0.0, 0.5\}$
    * Tốc độ học (Learning Rate): Phân phối đều trên thang log $\text{Loguniform}\{e^{-5}, 0.01\}$
    * Hệ số suy giảm trọng số (Weight Decay): Phân phối đều trên thang log $\text{Loguniform}\{e^{-6}, 0.001\}$

* **Nguyên lý hoạt động và kiến trúc của các mô hình đối chuẩn hạ nguồn:**
  * **XGBoost (Extreme Gradient Boosting):**
    * Là mô hình học máy hiệu quả và linh hoạt (Chen and Guestrin, 2016), xây dựng tiệm tiến (incrementally) nhiều cây quyết định thông qua việc tối ưu hóa hàm mất mát (loss function).
    * Mỗi cây sau liên tục điều chỉnh và sửa chữa các sai số của cây liền trước để nâng cao bền vững năng lực dự báo của mô hình.
    * Tích hợp thuật toán tăng cường độ dốc (gradient boosting algorithm), huấn luyện lặp đi lặp lại các mô hình cây quyết định với mục tiêu cực tiểu hóa phần dư (residuals) và gia tăng độ chính xác dự báo.
  * **CatBoost:**
    * Là mô hình tăng cường độ dốc mạnh mẽ (Prokhorenkova et al., 2018), được thiết kế chuyên biệt để xử lý hiệu quả các biến đặc trưng phân loại (categorical features).
    * Ứng dụng kỹ thuật "Ordered Boosting" (tăng cường có thứ tự), tính toán gradient tuần tự nhằm ngăn chặn triệt để hiện tượng rò rỉ thông tin biến mục tiêu (target leakage) và duy trì tính độc lập của từng mẫu huấn luyện.
    * Áp dụng kỹ thuật mã hóa biến phân loại dựa trên mục tiêu ("Target-based Categorical Encoding"), chuyển đổi các biến phân loại thành các biểu diễn số dựa trên các thống kê phân phối của biến mục tiêu, giúp giảm bớt nhu cầu tiền xử lý thủ công phức tạp và cải thiện đáng kể hiệu năng mô hình.
  * **MLP (Multilayer Perceptron):**
    * Cấu trúc gồm nhiều tầng nơ-ron, trong đó mỗi tầng kết nối đầy đủ (fully connected) tới tầng tiếp theo (Gorishniy et al., 2021).
    * Bao gồm tối thiểu $3$ tầng: một tầng đầu vào (input layer), một hoặc nhiều tầng ẩn (hidden layers) và một tầng đầu ra (output layer).
    * Liên tục hiệu chỉnh các trọng số kết nối giữa các nơ-ron thông qua các phương pháp huấn luyện tiêu chuẩn như thuật toán lan truyền ngược (backpropagation algorithm) và giải thuật hạ độ dốc (gradient descent) để cực tiểu hóa sai số dự báo.
  * **TabPFN:**
    * Là kiến trúc mô hình dựa trên Transformer (Hollmann et al., 2023a; Grinsztajn et al., 2025) có khả năng xấp xỉ phân phối dự báo hậu nghiệm (posterior predictive distribution) cho dữ liệu dạng bảng.
    * Cho phép thực hiện phân loại có giám sát với tốc độ cực nhanh mà hoàn toàn không cần tinh chỉnh siêu tham số (no hyperparameter tuning).
    * Vận hành thông qua cơ chế học theo ngữ cảnh (in-context learning), tạo ra các dự đoán trực tiếp từ chuỗi dữ liệu có nhãn mà không yêu cầu bất kỳ bước cập nhật tham số nào thêm, đồng thời có thể tái sử dụng ngay cho các tác vụ hạ nguồn mà không cần trải qua bước huấn luyện lại (without retraining).

### C.3 AutoFE

* **Phân loại các phương pháp kỹ thuật đặc trưng tự động (AutoFE) đối chuẩn:**
  * Để minh chứng tính hiệu quả vượt trội của SymboLLM-FE, nghiên cứu so sánh đối chiếu với $2$ phương pháp AutoFE truyền thống và $5$ phương pháp AutoFE dựa trên LLM tiên tiến nhất:
    * AutoFE truyền thống: AutoFeat (Horn et al., 2019) và OpenFE (Zhang et al., 2023b).
    * AutoFE dựa trên LLM (LLM-based AutoFE): CAAFE (Hollmann et al., 2023b), OcTree (Nam et al., 2024), FEBP (Zou et al., 2026), LLM-FE (Abhyankar et al., 2025) và LLM-RANK (Jeong et al., 2024).

* **Cơ chế hoạt động của các phương pháp AutoFE truyền thống:**
  * **AutoFeat (Horn et al., 2019):**
    * Tự động phát hiện các đặc trưng trong các hồ dữ liệu lớn (data lakes) bằng cách khám phá các đường dẫn kết nối bắc cầu đa chặng (multi-hop transitive join paths).
    * Đánh giá sức mạnh dự báo của các đặc trưng dựa trên độ tương quan (correlation) và độ dư thừa (redundancy).
    * Xếp hạng các đường dẫn kết nối mà không cần huấn luyện mô hình dự báo, mang lại tốc độ xử lý nhanh hơn nhiều lần (significant times speedup) so với các phương pháp đường cơ sở thông thường.
  * **OpenFE (Zhang et al., 2023b):**
    * Áp dụng khung làm việc mở rộng - thu gọn (expand-reduce framework) để sinh ra tập hợp đặc trưng ứng viên (candidate features).
    * Đánh giá mức độ gia tăng hiệu năng của đặc trưng thông qua giải thuật FeatureBoost mà không đòi hỏi phải huấn luyện lại toàn bộ mô hình.
    * Kết hợp cơ chế cắt tỉa hai giai đoạn (two-stage pruning) để chọn lọc đặc trưng với hiệu suất cao, đạt thành tích vượt trội hơn $99\%$ các đội ngũ khoa học dữ liệu trong các cuộc thi cạnh tranh Kaggle.

* **Cơ chế hoạt động của các phương pháp AutoFE dựa trên mô hình ngôn ngữ lớn (LLM-based AutoFE):**
  * **CAAFE (Hollmann et al., 2023b):**
    * Kết hợp các mô hình ngôn ngữ lớn (LLMs) với các bộ dự báo dữ liệu dạng bảng.
    * Sinh mã nguồn Python (Python code) và các phần giải thích văn bản (textual explanations) một cách lặp đi lặp lại để tạo các đặc trưng mới dựa trên mô tả ngữ nghĩa của tập dữ liệu, giúp cải thiện hiệu năng dự báo trên nhiều tập dữ liệu đa dạng.
  * **OcTree (Nam et al., 2024):**
    * Khai thác triệt để khả năng diễn giải bằng ngôn ngữ tự nhiên vốn có của các cây quyết định (decision trees).
    * Phản hồi ngược các tri thức thu được từ các thực nghiệm trước đó về cho LLM dưới dạng thông tin suy luận ngôn ngữ (linguistic reasoning information).
    * Cải tiến lặp các quy tắc sinh đặc trưng mà không đòi hỏi người dùng phải định nghĩa không gian tìm kiếm một cách thủ công.
  * **FEBP (Zou et al., 2026):**
    * Tận dụng đầy đủ thông tin ngữ nghĩa của tập dữ liệu.
    * Cho phép LLM tối ưu hóa lặp quá trình xây dựng đặc trưng dựa trên các đặc trưng mẫu đạt hiệu năng cao nhất (best-performing exemplar features) thông qua cơ chế học theo ngữ cảnh (in-context learning), đồng thời cung cấp các giải thích ngữ nghĩa rõ ràng.
  * **LLM-FE (Abhyankar et al., 2025):**
    * Hình thức hóa kỹ thuật đặc trưng như một bài toán tìm kiếm chương trình (program search problem).
    * Sử dụng LLM như các bộ tối ưu hóa tiến hóa có định hướng tri thức (knowledge-guided evolutionary optimizers), thực hiện đột biến (mutate) các phép biến đổi đặc trưng đã thành công để tạo ra các đặc trưng mới.
    * Kết hợp với bộ nhớ động (dynamic memory) cho quá trình tối ưu hóa lặp, hỗ trợ đồng thời cho cả tác vụ phân loại và tác vụ hồi quy.
  * **LLM-RANK (Jeong et al., 2024):**
    * Chỉ yêu cầu thông tin về tên các đặc trưng (feature names) và phần mô tả tác vụ (task descriptions).
    * Sử dụng kỹ thuật gợi ý không cần mẫu (zero-shot prompting) để trích xuất điểm số quan trọng định lượng hoặc thứ hạng đặc trưng trực tiếp từ LLM.
    * Nhận diện và chọn lọc các đặc trưng có tính dự báo mạnh nhất, chứng minh giá trị đặc biệt trong các lĩnh vực có chi phí thu thập dữ liệu đắt đỏ.

### C.4 Evaluation Metrics

* **Chỉ số đánh giá cho các tác vụ phân loại (Classification Tasks):**
  * Độ chính xác (Accuracy): Tỷ lệ các mẫu được dự đoán đúng phân lớp trên tổng số mẫu đánh giá.
  * Điểm F1 (F1-score): Trung bình điều hòa giữa độ chuẩn xác (Precision) và độ thu hồi (Recall), đánh giá năng lực phân loại toàn diện và công bằng khi dữ liệu mất cân bằng phân bố lớp.
* **Chỉ số đánh giá cho các tác vụ hồi quy (Regression Tasks):**
  * Căn bậc hai sai số bình phương trung bình (Root Mean Square Error - RMSE): Đo lường độ lệch chuẩn của các phần dư dự báo, nhạy cảm với các sai số lớn: $\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}$.
  * Hệ số xác định (R-squared / $R^2$): Tỷ lệ phương sai của biến mục tiêu được giải thích bởi mô hình so với mức phương sai tổng thể: $R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$.

### C.5 Training Settings

* **Cấu hình phần cứng thực nghiệm (Hardware Specifications):**
  * Huấn luyện mô hình học sâu (Deep learning models): Được thực hiện trên một bộ vi xử lý đồ họa GPU NVIDIA GeForce RTX 4090.
  * Huấn luyện mô hình dựa trên cây (Tree-based models): Được thực hiện trên bộ vi xử lý máy tính AMD Ryzen 5 7500F 6 lõi (AMD Ryzen 5 7500F 6-Core Processor).
* **Quy chuẩn độ tin cậy thống kê (Statistical Reliability):**
  * Toàn bộ các kết quả thực nghiệm được báo cáo dưới dạng giá trị trung bình cộng thu được từ $3$ hạt giống ngẫu nhiên độc lập khác nhau (average of three different random seeds) nhằm loại bỏ sự sai lệch do ngẫu nhiên và đảm bảo độ tin cậy thống kê chuẩn xác.

### C.6 Reproducibility

* **Công khai mã nguồn mở và khả năng tái lập (Reproducibility):**
  * Nhằm đảm bảo khả năng tái lập hoàn toàn của các kết quả nghiên cứu, toàn bộ mã nguồn thực nghiệm đã được công khai trên kho lưu trữ GitHub chính thức tại địa chỉ: `LAMDA-NeSy/SymboLLM-FE`.
  * Các thành phần tài nguyên được phát hành bao gồm:
    * Bản hiện thực đầy đủ của khung làm việc SymboLLM-FE (SymboLLM-FE implementation).
    * Toàn bộ các cấu hình hồi quy ký hiệu (symbolic regression configurations).
    * Các mẫu câu nhắc cho mô hình ngôn ngữ lớn (LLM prompt templates) được áp dụng trong toàn bộ quy trình sinh và tinh chỉnh đặc trưng.
