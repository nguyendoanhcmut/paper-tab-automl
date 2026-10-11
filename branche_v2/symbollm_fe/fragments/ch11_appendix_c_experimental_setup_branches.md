## Appendix C Experimental Setup

- Phụ lục này trình bày chi tiết về thiết lập thực nghiệm (experimental setup) của SymboLLM-FE, bao gồm các tập dữ liệu chuẩn đối sánh (benchmark datasets), các mô hình đường cơ sở xuôi dòng (downstream baselines), các phương pháp tự động hóa kỹ thuật đặc trưng (AutoFE - Automated Feature Engineering) so sánh, các số đo đánh giá (evaluation metrics), cấu hình phần cứng huấn luyện (training settings) và tính khả lặp (reproducibility).

### C.1 Datasets

- Nghiên cứu lựa chọn nhiều tập dữ liệu đáng tin cậy và mã nguồn mở (open-source and reliable datasets) từ OpenML và Kaggle.
- Các tập dữ liệu này bao quát 3 tác vụ học máy chính:
  - Phân loại nhị phân (binary classification).
  - Phân loại đa lớp (multi-class classification).
  - Hồi quy (regression).
- Phạm vi dữ liệu trải rộng trên nhiều lĩnh vực ứng dụng thực tế khác nhau như tài chính (finance) và chăm sóc sức khỏe (healthcare).
- Thông tin tổng quan của các tập dữ liệu được sử dụng được trình bày chi tiết trong Bảng 7 (Table 7).
- Danh sách tổng quan các tập dữ liệu thực nghiệm theo Table 7 (Datasets used in this paper):

| Dataset | Type | Samples | Features |
| :--- | :--- | :--- | :--- |
| Credit-g | Binary Classification | 1,000 | 20 |
| Spaceship | Binary Classification | 2,000 | 13 |
| Cmc | Multi-class Classification | 1,473 | 9 |
| Academic | Multi-class Classification | 4424 | 36 |
| Ailerons | Regression | 12,250 | 33 |
| Tesla | Regression | 6,906 | 8 |

- Đặc tả chi tiết từng tập dữ liệu:
  - **Credit-g**:
    - Credit-g bao gồm 1,000 bản ghi với 20 thuộc tính phân loại/ký hiệu (categorical/symbolic attributes) do Giáo sư Hofmann (Prof. Hofmann) chuẩn bị.
    - Trong tập dữ liệu này, mỗi bản ghi đại diện cho một khách hàng vay tín dụng từ ngân hàng.
    - Mỗi cá nhân được phân loại là có rủi ro tín dụng tốt (good) hoặc xấu (bad) dựa trên tập hợp các thuộc tính.
    - Mục tiêu dự đoán là xác định xem rủi ro tín dụng của khách hàng là tốt hay xấu.
    - Tập dữ liệu có sẵn tại: `https://www.openml.org/search?type=data&sort=runs&id=31&status=active`.
  - **Cmc**:
    - Cmc là tập dữ liệu phân loại có giám sát (supervised classification) dự đoán biện pháp tránh thai được sử dụng (contraceptive method used, gồm 3 danh mục) dựa trên đặc điểm nhân khẩu học cá nhân của phụ nữ đã kết hôn.
    - Tập dữ liệu bao gồm 1,473 mẫu và 9 thuộc tính, thường được sử dụng rộng rãi để đánh giá các thuật toán phân loại.
    - Tập dữ liệu có sẵn tại: `https://www.openml.org/search?type=data&sort=runs&id=23&status=active`.
  - **Ailerons**:
    - Ailerons là tập dữ liệu hồi quy giải quyết bài toán điều khiển máy bay F16 (F16 aircraft control problem), dự đoán hành động điều khiển tác động lên cánh tà (ailerons) dựa trên các thuộc tính trạng thái bay của máy bay.
    - Tập dữ liệu chứa 12,250 mẫu và 33 đặc trưng (features), xuất phát từ một bài toán điều khiển hàng không vũ trụ trong thực tế (real aerospace control problem).
    - Tập dữ liệu có sẵn tại: `https://www.openml.org/search?type=data&sort=runs&id=296&status=active`.
  - **Spaceship**:
    - Spaceship là tập dữ liệu cuộc thi Kaggle cấp độ nhập môn (beginner-level) lấy bối cảnh năm 2912, trong đó một tàu vũ trụ chở gần 13,000 hành khách va chạm với một dị thường không-thời gian (space-time anomaly), khiến gần một nửa số hành khách bị dịch chuyển sang chiều không gian khác.
    - Tập dữ liệu chứa khoảng 2,000 bản ghi hành khách với các đặc trưng bao gồm hành tinh quê hương (home planet), trạng thái ngủ đông (cryo-sleep status), số cabin, điểm đến và lịch sử chi tiêu cá nhân.
    - Mục tiêu là dự đoán liệu hành khách có bị dịch chuyển (transported) hay không.
    - Tập dữ liệu có sẵn tại: `https://www.kaggle.com/competitions/spaceship-titanic`.
  - **Academic**:
    - Tập dữ liệu Academic, có nguồn gốc từ Kaggle, được thiết kế chuyên biệt để dự đoán kết quả học tập của sinh viên (student outcomes).
    - Tập dữ liệu chứa dữ liệu nhân khẩu học (demographic), kinh tế - xã hội (socio-economic) và dữ liệu đăng ký nhập học (academic enrollment data) được sử dụng để phân loại sinh viên thành các nhóm như "thành công trong học tập" ("academic success") hoặc "bỏ học" ("dropout").
    - Cung cấp góc nhìn định hướng kết quả (outcome-oriented perspective) sâu sát hơn về kết quả học tập của người học.
    - Tập dữ liệu có sẵn tại: `https://www.kaggle.com/datasets/missionjee/students-dropout-and-academic-success-dataset`.
  - **Tesla**:
    - Tập dữ liệu Tesla, có nguồn gốc từ Kaggle, chứa dữ liệu giá cổ phiếu lịch sử hàng ngày (historical daily stock price data) của tập đoàn Tesla Inc. (TSLA).
    - Các đặc trưng điển hình bao gồm Open (giá mở cửa), High (giá cao nhất), Low (giá thấp nhất), Close (giá đóng cửa), Adjusted Close (giá đóng cửa điều chỉnh), và Volume (khối lượng giao dịch).
    - Tập dữ liệu thường được sử dụng cho bài toán dự báo chuỗi thời gian (time series forecasting) về biến động giá cổ phiếu.
    - Tập dữ liệu có sẵn tại: `https://www.kaggle.com/datasets/guillemservera/tesla-stock-data`.

### C.2 Downstream Baselines

- Nhằm kiểm chứng năng lực tổng quát hóa (generalization) và khả năng thích ứng (adaptability) của SymboLLM-FE, nghiên cứu đánh giá mô hình trên nhiều mô hình dạng cây (tree-based models) và mô hình học sâu (deep learning models) đa dạng.
- Lựa chọn các mô hình baseline:
  - Đối với các mô hình dạng cây: lựa chọn CatBoost (Prokhorenkova et al., 2018) và XGBoost (Chen and Guestrin, 2016).
  - Đối với các mô hình học sâu: lựa chọn MLP (Gorishniy et al., 2021) và TabPFN (Hollmann et al., 2025).
- Lưới không gian tìm kiếm siêu tham số (hyperparameter grids) của các mô hình dạng cây và học sâu được cung cấp trong Bảng 8 (Table 8).
- Lưới siêu tham số của các mô hình đường cơ sở theo Table 8 (Hyperparameter grids of downstream baselines):

| Model | Hyperparameter | Values |
| :--- | :--- | :--- |
| XGBoost | Learning Rate | {0.01, 0.1} |
| XGBoost | Max. Depth | {1, 5, 9} |
| XGBoost | N Estimators | {10, 000, 20, 000, 30, 000} |
| XGBoost | Subsample | {0.5, 0.8, 1.0} |
| XGBoost | Colsample Bytree | {0.5, 0.8, 1.0} |
| XGBoost | Min Child Weight | {1, 3, 5} |
| CatBoost | Learning Rate | {0.01, 0.05, 0.1} |
| CatBoost | Depth | {4, 6, 8} |
| CatBoost | Iterations | {500, 1, 000, 2, 000} |
| MLP | D_layers | {1, 8, 64, 512} |
| MLP | Dropout | Uniform {0.0, 0.5} |
| MLP | Learning Rate | Loguniform{$e^{-5}$, 0.01} |
| MLP | Weight Decay | Loguniform{$e^{-6}$, 0.001} |

- Chi tiết nguyên lý hoạt động của từng mô hình đường cơ sở xuôi dòng:
  - **XGBoost**:
    - XGBoost (Chen and Guestrin, 2016) là mô hình học máy hiệu quả và linh hoạt, xây dựng tuần tự tăng dần nhiều cây quyết định bằng cách tối ưu hóa hàm mất mát (loss function).
    - Mỗi cây quyết định kế tiếp sửa đổi sai số của cây đứng trước nó để liên tục nâng cao hiệu năng dự đoán của mô hình.
    - XGBoost tích hợp thuật toán tăng cường độ dốc (gradient boosting algorithm), huấn luyện lặp đi lặp lại các mô hình dạng cây quyết định với mục tiêu giảm thiểu tối đa phần dư (residuals) và nâng cao độ chính xác dự đoán.
  - **CatBoost**:
    - CatBoost (Prokhorenkova et al., 2018) là mô hình dựa trên kỹ thuật boosting mạnh mẽ được thiết kế chuyên biệt để xử lý hiệu quả các đặc trưng phân loại (categorical features).
    - Mô hình sử dụng kỹ thuật "Ordered Boosting", tính toán gradient theo thứ tự tuần tự để triệt tiêu hiện tượng rò rỉ mục tiêu (target leakage) và bảo toàn tính độc lập của từng mẫu huấn luyện.
    - Đồng thời, CatBoost áp dụng kỹ thuật "Target-based Categorical Encoding", chuyển đổi các biến phân loại thành biểu diễn số học dựa trên các thống kê của biến mục tiêu, nhờ đó giảm bớt các bước tiền xử lý phức tạp và nâng cao hiệu năng của mô hình.
  - **MLP**:
    - Mạng nơ-ron nhiều lớp MLP (Multilayer Perceptron) bao gồm nhiều tầng nơ-ron, trong đó mỗi tầng được kết nối đầy đủ (fully connected) với tầng tiếp theo.
    - MLP bao gồm ít nhất 3 tầng: một tầng đầu vào (input layer), một hoặc nhiều tầng ẩn (hidden layers), và một tầng đầu ra (output layer).
    - Mô hình liên tục điều chỉnh các trọng số liên kết giữa các nơ-ron thông qua các phương pháp huấn luyện như thuật toán lan truyền ngược (backpropagation algorithm) và hạ độ dốc (gradient descent) để giảm thiểu sai số dự đoán.
  - **TabPFN**:
    - TabPFN (Hollmann et al., 2023a; Grinsztajn et al., 2025) là mô hình dựa trên kiến trúc Transformer xấp xỉ phân phối dự đoán hậu nghiệm (posterior predictive distribution) cho dữ liệu bảng.
    - Cho phép phân loại có giám sát cực kỳ nhanh chóng mà không cần bất kỳ bước tinh chỉnh siêu tham số nào (no hyperparameter tuning).
    - TabPFN thực hiện học trong ngữ cảnh (in-context learning), đưa ra dự đoán trực tiếp từ các chuỗi dữ liệu có nhãn mà không cần cập nhật thêm tham số mô hình, đồng thời có thể tái sử dụng ngay cho các tác vụ xuôi dòng mà không cần huấn luyện lại (without retraining).

### C.3 AutoFE

- Để chứng minh tính hiệu quả vượt trội của SymboLLM-FE, nghiên cứu so sánh đối chiếu với 2 phương pháp AutoFE truyền thống (traditional AutoFE) và 5 phương pháp AutoFE dựa trên mô hình ngôn ngữ lớn (LLM-based AutoFE):
  - Hai phương pháp AutoFE truyền thống bao gồm: AutoFeat (Horn et al., 2019) và OpenFE (Zhang et al., 2023b).
  - Năm phương pháp AutoFE dựa trên LLM bao gồm: CAAFE (Hollmann et al., 2023b), OcTree (Nam et al., 2024), FEBP (Zou et al., 2026), LLM-FE (Abhyankar et al., 2025) và LLM-RANK (Jeong et al., 2024).
- Đặc tả các phương pháp AutoFE truyền thống:
  - **AutoFeat**:
    - AutoFeat (Horn et al., 2019) tự động khám phá các đặc trưng hữu ích trong các hồ dữ liệu lớn (large data lakes) thông qua việc duyệt các đường dẫn kết nối bắc cầu nhiều bước (multi-hop transitive join paths).
    - Đánh giá năng lực dự đoán của đặc trưng bằng độ tương quan (correlation) và độ dư thừa (redundancy).
    - Tiến hành xếp hạng các đường dẫn kết nối mà không đòi hỏi huấn luyện mô hình, giúp đạt được tốc độ thực thi nhanh hơn đáng kể so với các phương pháp đường cơ sở.
  - **OpenFE**:
    - OpenFE (Zhang et al., 2023b) áp dụng khung làm việc mở rộng - thu gọn (expand-reduce framework) để sinh ra các đặc trưng ứng viên.
    - Đánh giá mức độ gia tăng hiệu năng của đặc trưng thông qua thuật toán FeatureBoost mà không cần huấn luyện lại toàn bộ mô hình.
    - Kết hợp cơ chế cắt tỉa hai giai đoạn (two-stage pruning) để chọn lọc đặc trưng hiệu quả, vượt qua hơn 99% các đội ngũ khoa học dữ liệu trong các cuộc thi Kaggle.
- Đặc tả các phương pháp AutoFE dựa trên LLM:
  - **CAAFE**:
    - CAAFE (Hollmann et al., 2023b) kết hợp sức mạnh của LLM với các bộ dự đoán dữ liệu bảng (tabular predictors).
    - Lặp đi lặp lại việc sinh mã nguồn Python cùng với các lời giải thích bằng văn bản để xây dựng các đặc trưng mới dựa trên mô tả tập dữ liệu, giúp cải thiện hiệu năng dự đoán trên nhiều bộ dữ liệu khác nhau.
  - **OcTree**:
    - OCTree (Nam et al., 2024) tận dụng tính khả giải bằng ngôn ngữ tự nhiên (natural language interpretability) của cây quyết định.
    - Phản hồi tri thức tích lũy từ các thử nghiệm trước đó trở lại cho LLM dưới dạng thông tin suy luận ngôn ngữ (linguistic reasoning information).
    - Cải tiến lặp lại các quy tắc tạo đặc trưng mà không cần phải xác định thủ công không gian tìm kiếm.
  - **FEBP**:
    - FEBP (Zou et al., 2026) khai thác triệt để thông tin ngữ nghĩa của tập dữ liệu.
    - Cho phép LLM tối ưu hóa lặp quá trình xây dựng đặc trưng dựa trên các đặc trưng mẫu có hiệu năng cao nhất (best-performing exemplar features) thông qua học trong ngữ cảnh (in-context learning), đồng thời cung cấp giải thích ngữ nghĩa rõ ràng.
  - **LLM-FE**:
    - LLM-FE (Abhyankar et al., 2025) hình thức hóa kỹ thuật đặc trưng dưới dạng bài toán tìm kiếm chương trình (program search problem).
    - LLM đóng vai trò là các bộ tối ưu hóa tiến hóa được định hướng bởi tri thức (knowledge-guided evolutionary optimizers), tiến hành đột biến các phép biến đổi đặc trưng thành công để tạo ra các đặc trưng mới.
    - Kết hợp cùng bộ nhớ động (dynamic memory) phục vụ quá trình tối ưu hóa lặp, hỗ trợ đồng thời cả tác vụ phân loại lẫn hồi quy.
  - **LLM-RANK**:
    - LLM-RANK (Jeong et al., 2024) chỉ yêu cầu thông tin về tên đặc trưng và phần mô tả bài toán.
    - Sử dụng kỹ thuật gợi ý không mẫu (zero-shot prompting) để khai thác điểm số quan trọng dạng số hoặc thứ hạng đặc trưng từ LLM, từ đó xác định các đặc trưng có giá trị dự đoán cao nhất.
    - Phương pháp này đặc biệt hữu dụng trong các lĩnh vực có chi phí thu thập dữ liệu đắt đỏ.

### C.4 Evaluation Metrics

- Đối với các tác vụ phân loại (classification tasks), nghiên cứu kiểm tra các thước đo hiệu năng bao gồm Độ chính xác (Accuracy) và F1-score.
- Đối với các tác vụ hồi quy (regression tasks), nghiên cứu áp dụng thước đo Căn bậc hai sai số bình phương trung bình (Root Mean Square Error - RMSE) và Hệ số xác định $R^2$ (R-squared).

### C.5 Training Settings

- Các mô hình học sâu (deep learning models) được huấn luyện trên card đồ họa NVIDIA 4090 GPU.
- Các mô hình dạng cây (tree-based models) được huấn luyện trên vi xử lý AMD Ryzen 5 7500F 6-Core Processor.
- Tất cả các kết quả thực nghiệm được báo cáo dưới dạng giá trị trung bình trên ba hạt giống ngẫu nhiên khác nhau (three different random seeds) nhằm bảo đảm tính tin cậy về mặt thống kê.

### C.6 Reproducibility

- Để bảo đảm tính khả lặp (reproducibility), nhóm tác giả đã công bố toàn bộ mã nguồn hoàn chỉnh của nghiên cứu.
- Mã nguồn bao gồm bản hiện thực SymboLLM-FE, các cấu hình hồi quy ký hiệu (symbolic regression configurations), và các bản mẫu lời nhắc cho LLM (LLM prompt templates).
- Toàn bộ được lưu trữ trong kho mã nguồn GitHub công khai tại: `LAMDA-NeSy/SymboLLM-FE`.
