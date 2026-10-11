## 5 Experiments

### 5.1 Experimental Setup

* **Tuyển chọn và phân loại các tập dữ liệu thực nghiệm (Datasets):**
  * Các tập dữ liệu được chọn lọc đa dạng từ hai nguồn mã nguồn mở và chuẩn mực là OpenML và Kaggle nhằm bảo đảm tính tin cậy và khách quan.
  * Ba nhóm tác vụ dự đoán chính (three primary tasks):
    * Phân loại nhị phân (binary classification).
    * Phân loại đa lớp (multi-class classification).
    * Hồi quy (regression).
  * Lĩnh vực ứng dụng thực tế phong phú: bao quát nhiều lĩnh vực chuyên ngành như tài chính (finance), chăm sóc sức khỏe (healthcare), công nghiệp và giáo dục (thông tin chi tiết về các tập dữ liệu được cung cấp trong Phụ lục C.1 / Appendix C.1).
  * Các tập dữ liệu đại diện điển hình được sử dụng trong đánh giá hiệu năng gồm:
    * `Credit-g`: Tác vụ phân loại nhị phân rủi ro tín dụng tài chính ($1.000$ mẫu, $20$ đặc trưng).
    * `Spaceship` (Spaceship Titanic): Tác vụ phân loại nhị phân dự đoán hành khách dịch chuyển không gian ($8.693$ mẫu, $13$ đặc trưng).
    * `Cmc` (Contraceptive Method Choice): Tác vụ phân loại đa lớp lựa chọn biện pháp y tế ($1.473$ mẫu, $9$ đặc trưng).
    * `Academic`: Tác vụ phân loại đa lớp thành tích học thuật sinh viên ($4.424$ mẫu, $36$ đặc trưng).
    * `Ailerons`: Tác vụ hồi quy điều khiển hệ thống cánh lái máy bay ($13.750$ mẫu, $40$ đặc trưng).
    * `Tesla`: Tác vụ hồi quy biến động giá cổ phiếu ($1.692$ mẫu, $6$ đặc trưng).

* **Các mô hình hạ nguồn cơ sở (Downstream Baselines):**
  * Mục tiêu thẩm định: Chứng minh năng lực thích ứng (adaptability) và khả năng tổng quát hóa (generalization) của SymboLLM-FE trên nhiều họ kiến trúc học máy khác nhau.
  * Các mô hình dựa trên cây quyết định (tree-based models):
    * CatBoost (Prokhorenkova et al., 2018).
    * XGBoost (Chen và Guestrin, 2016).
  * Các mô hình học sâu cho dữ liệu bảng (deep learning models for tabular data):
    * MLP (Multi-Layer Perceptron) (Gorishniy et al., 2021).
    * TabPFN (Prior-Data Fitted Network) (Hollmann et al., 2025).
  * Chi tiết cấu hình thử nghiệm và lưới siêu tham số đầy đủ (full hyperparameter grids) của các mô hình hạ nguồn được trình bày tại Phụ lục C.2 (Appendix C.2, Bảng 8).

* **Các phương pháp AutoFE đối chuẩn (Comparison AutoFE Methods):**
  * Để kiểm chứng hiệu quả vượt trội, SymboLLM-FE được so sánh toàn diện với 2 nhóm phương pháp AutoFE tiên tiến (chi tiết cấu hình trong Phụ lục C.3):
    * Hai phương pháp AutoFE truyền thống (traditional AutoFE):
      * AutoFeat (Horn et al., 2019): Dựa trên tập toán tử toán học cố định và lựa chọn đặc trưng tuyến tính.
      * OpenFE (Zhang et al., 2023b): Tận dụng thuật toán tìm kiếm gia tăng và boosting cây để phát hiện đặc trưng mới.
    * Năm phương pháp AutoFE dựa trên LLM (LLM-based AutoFE):
      * LLM-SELECT (Jeong et al., 2024): Phương pháp lựa chọn đặc trưng dựa trên LLM.
      * CAAFE (Hollmann et al., 2023b): Sinh mã kỹ thuật đặc trưng bán tự động có giải thích ngữ nghĩa.
      * OcTree (Nam et al., 2024): Phương pháp tối ưu cây quyết định lặp qua LLM.
      * FEBP (Zou et al., 2026): Tối ưu hóa đặc trưng tiến hóa định hướng bởi LLM.
      * LLM-FE (Abhyankar et al., 2025): Tạo đặc trưng tự động bằng mô hình ngôn ngữ lớn qua không gian ngữ nghĩa thô.
      * LLM-RANK: Phương pháp xếp hạng và lựa chọn đặc trưng bằng LLM (không sinh thêm đặc trưng mới).

* **Các chỉ số đánh giá hiệu năng (Evaluation Metrics):**
  * Tác vụ phân loại (classification tasks):
    * Độ chính xác (Accuracy).
    * Diện tích dưới đường cong ROC (Area Under the Receiver Operating Characteristic Curve - ROC-AUC).
    * Điểm F1 (F1-score).
  * Tác vụ hồi quy (regression tasks):
    * Căn bậc hai sai số toàn phương trung bình (Root Mean Square Error - RMSE).
    * Sai số tuyệt đối trung bình (Mean Absolute Error - MAE).
    * Hệ số xác định R bình phương (R-squared - $R^2$).

### 5.2 Main Results

* **Hiệu năng vượt trội của SymboLLM-FE trên 6 tập dữ liệu chuẩn hóa với mô hình hạ nguồn TabPFN (Bảng 2):**
  * SymboLLM-FE đạt được sự cải thiện vượt bậc và có ý nghĩa thống kê (statistically significant improvements) so với tất cả các baseline:
    * Đạt mức tăng trưởng trung bình $1.23\%$ so với các phương pháp AutoFE truyền thống (traditional AutoFE).
    * Đạt độ chính xác cao hơn khoảng $1\%$ so với các phương pháp AutoFE dựa trên LLM (LLM-based AutoFE).
  * Phân tích chi tiết kết quả thực nghiệm trên từng tập dữ liệu (Bảng 2):
    * Tập dữ liệu `Credit-g` (Accuracy ↑):
      * Baseline (không AutoFE): $77.03 \pm 0.47\%$
      * AutoFeat: $77.83 \pm 1.43\%$
      * OpenFE: $76.50 \pm 3.34\%$
      * CAAFE: $78.00 \pm 0.71\%$ (hạng 1)
      * OcTree: $76.50 \pm 0.82\%$
      * FEBP: $77.50 \pm 0.41\%$ (hạng 2)
      * LLM-FE: $76.67 \pm 0.62\%$
      * LLM-RANK: $77.50 \pm 0.82\%$
      * SymboLLM-FE: $77.00 \pm 1.63\%$
    * Tập dữ liệu `Spaceship` (Accuracy ↑):
      * Baseline: $80.79 \pm 1.27\%$
      * AutoFeat: $80.76 \pm 1.17\%$
      * OpenFE: $80.30 \pm 1.00\%$
      * CAAFE: $80.99 \pm 1.00\%$ (hạng 2)
      * OcTree: $80.79 \pm 1.15\%$
      * FEBP: $80.85 \pm 1.29\%$
      * LLM-FE: $80.22 \pm 0.96\%$
      * LLM-RANK: $80.70 \pm 1.15\%$
      * SymboLLM-FE: $\mathbf{81.27 \pm 1.31\%}$ (hạng 1, tốt nhất)
    * Tập dữ liệu `Cmc` (Accuracy ↑):
      * Baseline: $57.85 \pm 0.89\%$
      * AutoFeat: $57.85 \pm 0.32\%$
      * OpenFE: $57.85 \pm 2.35\%$
      * CAAFE: $57.78 \pm 1.28\%$
      * OcTree: $57.85 \pm 1.52\%$
      * FEBP: $57.93 \pm 0.48\%$ (hạng 2)
      * LLM-FE: $57.29 \pm 2.20\%$
      * LLM-RANK: $57.74 \pm 0.85\%$
      * SymboLLM-FE: $\mathbf{57.97 \pm 0.73\%}$ (hạng 1, tốt nhất)
    * Tập dữ liệu `Academic` (Accuracy ↑):
      * Baseline: $77.33 \pm 0.67\%$
      * AutoFeat: $76.80 \pm 0.46\%$
      * OpenFE: $76.42 \pm 0.61\%$
      * CAAFE: $77.29 \pm 0.56\%$
      * OcTree: $77.33 \pm 0.70\%$
      * FEBP: $77.36 \pm 0.35\%$ (hạng 2)
      * LLM-FE: $76.42 \pm 0.61\%$
      * LLM-RANK: $77.25 \pm 0.19\%$
      * SymboLLM-FE: $\mathbf{77.89 \pm 0.23\%}$ (hạng 1, tốt nhất)
    * Tập dữ liệu `Ailerons` (RMSE ↓):
      * Baseline: $5.10 \pm 0.48$
      * AutoFeat: $5.04 \pm 0.45$
      * OpenFE: $5.26 \pm 0.49$
      * CAAFE: $5.03 \pm 0.46$ (hạng 2)
      * OcTree: $5.09 \pm 0.47$
      * FEBP: $5.08 \pm 0.48$
      * LLM-FE: $5.05 \pm 0.46$
      * LLM-RANK: $5.10 \pm 0.48$
      * SymboLLM-FE: $\mathbf{5.02 \pm 0.46}$ (hạng 1, tốt nhất)
    * Tập dữ liệu `Tesla` (RMSE ↓):
      * Baseline: $2.39 \pm 0.09$
      * AutoFeat: $2.38 \pm 0.00$
      * OpenFE: $2.18 \pm 0.06$ (hạng 2)
      * CAAFE: $2.66 \pm 0.09$
      * OcTree: $2.43 \pm 0.10$
      * FEBP: $2.41 \pm 0.08$
      * LLM-FE: $2.39 \pm 0.09$
      * LLM-RANK: $5.87 \pm 0.19$ (suy giảm hiệu năng trầm trọng)
      * SymboLLM-FE: $\mathbf{2.16 \pm 0.06}$ (hạng 1, tốt nhất)
  * **Bảng 2.** So sánh hiệu năng của SymboLLM-FE với các AutoFE trên 6 tập dữ liệu thực tế với TabPFN
    * <img src="assets/table_02_p7.png" alt="Bảng 2" />
    * **Bảng này chứng minh điều gì**
      * SymboLLM-FE đạt độ chính xác cao nhất hoặc nhì trên hầu hết các tập dữ liệu thực tế
    * **Từ đâu mà thấy được**
      * Các giá trị in đậm (best) và gạch chân (second best) ở hàng SymboLLM-FE trên 6 tập dữ liệu (Accuracy / RMSE)

* **Tính ổn định trên các mô hình hạ nguồn khác (CatBoost, XGBoost, MLP):**
  * Các thử nghiệm diện rộng trong Phụ lục E (Bảng 10, 11 và 12) trên CatBoost, XGBoost và MLP nhất quán khẳng định lợi thế hiệu năng bền vững của SymboLLM-FE độc lập với kiến trúc phân loại/hồi quy hạ nguồn.

* **Hiệu năng kiểm chứng trên 4 cuộc thi Kaggle thực tế (Hình 3):**
  * Để thẩm định năng lực mô hình trong điều kiện thi đấu cạnh tranh thực tế, SymboLLM-FE được đánh giá trên 4 cuộc thi Kaggle:
    * `BNP` (BNP Paribas Cardif Claims Management - quản lý hồ sơ bảo hiểm).
    * `Obesity Risk` (ước tính mức độ rủi ro béo phì).
    * `House Prices` (dự đoán giá nhà đất).
    * `Manufacturing` (tối ưu hóa quy trình sản xuất công nghiệp).
  * Đo lường trên cả hai bảng xếp hạng: Private Leaderboard (dữ liệu ẩn) và Public Leaderboard (dữ liệu công khai).
  * Mô hình kết hợp `SymboLLM-FE + TabPFN` vượt trội một cách đồng nhất cả `vanilla TabPFN` (mô hình gốc không AutoFE) lẫn `OpenFE + TabPFN`.
  * Đạt mức cải thiện điểm số trung bình là $2.5\text{ pp}$ ($2.5$ điểm phần trăm / percentage points) trên các cuộc thi.
  * **Hình 3.** So sánh điểm số hiệu năng trên 4 cuộc thi Kaggle giữa SymboLLM-FE và các baseline
    * <img src="assets/fig_05_p7_vector.png" alt="Hình 3" />
    * **Hình này chứng minh điều gì**
      * SymboLLM-FE đạt kết quả tốt nhất trên cả bài toán phân loại và hồi quy Kaggle
    * **Từ đâu mà thấy được**
      * Trục Ox: 4 tập Kaggle; Trục Oy: Metric điểm số; Cột SymboLLM-FE vượt trội hoặc cạnh tranh top 1

### 5.3 Analysis of Generated Features

* **Mô hình kết hợp đột phá giữa Hồi quy biểu trưng và LLM (Novel Synergy Paradigm):**
  * SymboLLM-FE thiết lập một mô thức hoàn toàn mới (minh họa ở Hình 1) khi kết hợp chặt chẽ giữa Hồi quy biểu trưng (Symbolic Regression - SR), mô hình ngôn ngữ lớn (LLM) và bộ dự đoán hạ nguồn (downstream predictor).
  * Khắc phục triệt để hai nhược điểm cố hữu của các phương pháp tiền nhiệm:
    * Không phụ thuộc mù quáng vào các phép xếp chồng toán tử thuần túy (blind mathematical operator stacks) thiếu hiểu biết ngữ nghĩa như AutoFE truyền thống.
    * Không thả nổi việc tìm kiếm trong không gian ngữ nghĩa tự do không định hướng (unguided semantic spaces) dẫn tới hội tụ chậm hoặc không ổn định như LLM-based AutoFE thuần túy.

* **Định vị LLM như một bộ máy tinh chỉnh thay vì bộ sinh sơ cấp (Refinement Engine vs. Primary Generator):**
  * SymboLLM-FE tận dụng LLM như một công cụ tinh chỉnh (refinement engine) thay vì để LLM tự do sinh đặc trưng ngay từ đầu.
  * Bằng cách neo chặt đầu vào của LLM vào các hệ số tương quan thứ hạng Kendall $\tau_i$ và kho công thức biểu trưng $\mathcal{P}$ thu được từ giai đoạn 1, quá trình sinh đặc trưng được củng cố vững chắc trên nền tảng thực tại thống kê (grounded in statistical reality).
  * Khung làm việc vòng lặp khép kín (closed-loop framework) ràng buộc vai trò của LLM một cách nghiêm ngặt:
    * Tối ưu hóa việc triển khai mã nguồn (optimizing code implementation) của các biểu thức toán học.
    * Tích hợp logic quy nạp (inductive logic) dựa trên tri thức miền có sẵn để gán nhãn ngữ nghĩa có ý nghĩa thực tế.

* **Triệt tiêu hiện tượng ảo giác và loại bỏ đặc trưng giả mạo (Eliminating Hallucinations):**
  * Ngăn ngừa hoàn toàn nguy cơ sinh ra các đặc trưng ngụy tạo hoặc ảo giác (spurious or hallucinated features) vốn không có căn cứ toán học.
  * Tạo ra các đặc trưng có khả năng giải thích cao (highly interpretable features) cho con người, chẳng hạn như chỉ số điểm triệu chứng có trọng số (weighted symptom score) như `Infection_Exposure_Risk` trong Hình 1.

* **Cân bằng tối ưu giữa tính hiệu quả và năng lực dự đoán (Quantified Efficiency & Performance):**
  * Các lợi thế định lượng của SymboLLM-FE được khẳng định rõ nét trong Bảng 1:
    * Thiết lập mức cân bằng vượt bậc giữa hiệu quả chi phí và năng lực dự đoán, giành điểm số mô hình cao nhất toàn diện đạt $80.02$.
    * Chỉ cần sinh ra một tập đặc trưng cực kỳ cô đọng và tinh gọn gồm đúng $70$ đặc trưng mới (so với hàng trăm đến hàng nghìn đặc trưng phình to của OpenFE hay AutoFeat).
    * Giảm thiểu triệt để không gian tìm kiếm và chi phí hội tụ: toàn bộ quá trình chỉ cần vẻn vẹn $4$ lượt gọi API (API calls), hoàn tất quy trình với chi phí thời gian xuất sắc, chứng minh năng lực tính toán vượt trội song hành cùng khả năng diễn giải minh bạch.

### 5.4 Generalization of SymboLLM-FE

* **Khả năng thích ứng vượt trội qua các họ LLM backbone khác nhau (Bảng 3):**
  * Để kiểm tra tính tổng quát hóa của SymboLLM-FE, nghiên cứu đánh giá hiệu năng phân loại khi kết hợp các bộ dự đoán hạ nguồn (CatBoost và TabPFN) với ba mô hình ngôn ngữ lớn khác nhau: GPT-4, GPT-o1 và DeepSeek-R1.
  * Kết quả thực nghiệm cụ thể (Bảng 3):
    * Với mô hình hạ nguồn CatBoost:
      * GPT-4: Độ chính xác $75.41 \pm 0.51\%$
      * GPT-o1: Độ chính xác $78.21 \pm 0.20\%$ (cải thiện $+2.80\%$)
      * DeepSeek-R1: Độ chính xác $77.95 \pm 0.36\%$ (cải thiện $+2.54\%$)
    * Với mô hình hạ nguồn TabPFN:
      * GPT-4: Độ chính xác $76.83 \pm 0.42\%$
      * GPT-o1: Độ chính xác $78.58 \pm 0.39\%$ (cải thiện $+1.75\%$)
      * DeepSeek-R1: Độ chính xác $\mathbf{79.49 \pm 0.57\%}$ (đạt hiệu năng cao nhất toàn diện, cải thiện $+2.66\%$ so với GPT-4)
  * **Bảng 3.** So sánh hiệu năng của SymboLLM-FE với các mô hình hạ nguồn và backbone LLM khác nhau
    * <img src="assets/table_03_p8.png" alt="Bảng 3" />
    * **Bảng này chứng minh điều gì**
      * Tính tổng quát hóa cao của SymboLLM-FE qua các họ LLM (GPT-4o, DeepSeek, Qwen) và mô hình hạ nguồn
    * **Từ đâu mà thấy được**
      * Các chỉ số Accuracy và RMSE duy trì mức vượt trội ổn định bất kể backbone LLM được sử dụng

* **Mối quan hệ nhân quả giữa năng lực suy luận của LLM và chất lượng đặc trưng:**
  * Cả hai mô hình định hướng suy luận chuyên sâu (advanced reasoning models) là GPT-o1 và DeepSeek-R1 đều vượt trội rõ rệt so với GPT-4 tiêu chuẩn trên cả hai bộ phân loại hạ nguồn.
  * Phát hiện thực nghiệm này xác nhận: Hiệu quả kỹ thuật đặc trưng của SymboLLM-FE tỷ lệ thuận và gắn kết chặt chẽ với năng lực suy luận (reasoning capability) của LLM. Do đó, việc ứng dụng các mô hình LLM suy luận ngày càng mạnh mẽ sẽ tiếp tục nâng cao trực tiếp chất lượng đặc trưng tự động.

### 5.5 Estimation of Running Costs for SymboLLM-FE

* **Kiểm soát độ phức tạp không gian tìm kiếm đặc trưng (Computational Scalability):**
  * Phân tích hiệu năng toàn diện xác nhận tính khả thi mở rộng (computational scalability) của SymboLLM-FE.
  * Chiến lược cửa sổ mở rộng-trượt (expanding-sliding window) có định hướng tương quan thứ hạng Spearman thu hẹp thành công độ phức tạp tìm kiếm đặc trưng từ mức cấp số mũ $\mathcal{O}(2^n)$ xuống mức đa thức $\mathcal{O}(n^2)$.
  * Số lượng công thức ứng viên sinh ra tuân thủ nghiêm ngặt các giới hạn toán học lý thuyết đã thiết lập (Bảng 4).

* **Định lượng thời gian chạy thực tế và tài nguyên API theo từng tập dữ liệu (Bảng 4):**
  * Thời gian chạy cục bộ tỷ lệ tuyến tính với số lượng công thức và quy mô tập dữ liệu ở giai đoạn 1 (Hồi quy biểu trưng - SR):
    * `Credit-g`: Sinh $66$ công thức SR, thời gian chạy SR là $4.23\text{ phút}$, thực hiện $3$ lượt gọi LLM, tiêu tốn $2.331\text{ tokens}$ mỗi lượt gọi.
    * `Spaceship`: Sinh $36$ công thức SR, thời gian chạy SR là $2.01\text{ phút}$, thực hiện $4$ lượt gọi LLM, tiêu tốn $1.201\text{ tokens}$ mỗi lượt gọi.
    * `Cmc`: Sinh $21$ công thức SR, thời gian chạy SR là $0.89\text{ phút}$, thực hiện $3$ lượt gọi LLM, tiêu tốn $1.159\text{ tokens}$ mỗi lượt gọi.
    * `Academic`: Sinh $190$ công thức SR, thời gian chạy SR là $25.34\text{ phút}$, thực hiện $4$ lượt gọi LLM, tiêu tốn $3.587\text{ tokens}$ mỗi lượt gọi.
    * `Ailerons`: Sinh $171$ công thức SR, thời gian chạy SR là $30.24\text{ phút}$, thực hiện $5$ lượt gọi LLM, tiêu tốn $3.250\text{ tokens}$ mỗi lượt gọi.
    * `Tesla`: Sinh $15$ công thức SR, thời gian chạy SR là $2.54\text{ phút}$, thực hiện $2$ lượt gọi LLM, tiêu tốn $1.147\text{ tokens}$ mỗi lượt gọi.
  * **Bảng 4.** Các chỉ số vận hành và chi phí tính toán của SymboLLM-FE
    * <img src="assets/table_04_p8.png" alt="Bảng 4" />
    * **Bảng này chứng minh điều gì**
      * Chi phí thời gian và số lần gọi LLM của SymboLLM-FE cực kỳ tiết kiệm so với các phương pháp LLM-based thuần
    * **Từ đâu mà thấy được**
      * Cột SR time, LLM calls và tổng chi phí tính toán được liệt kê chi tiết theo từng tập dữ liệu
      * Số lượt gọi LLM chỉ 2–5 lần (1147–3587 tokens), thời gian SR từ 0.89 phút (Cmc) đến 30.24 phút (Ailerons)

* **Hiệu quả vượt bậc của cơ chế lọc ngữ nghĩa giai đoạn hai:**
  * Bằng cách hoạt động như một bộ lọc ngữ nghĩa (semantic filter) có chọn lọc thay vì bộ sinh văn bản mở vô định, LLM duy trì số lượt gọi API ổn định quanh mức xấp xỉ $4$ lượt gọi (dao động từ $2$ đến $5$ lượt gọi) trên tất cả các tác vụ thực nghiệm, hoàn toàn không phụ thuộc vào số chiều dữ liệu ban đầu.
  * Tổng lượng token tiêu thụ được tách rời (decoupled) khỏi kích thước mẫu của tập dữ liệu, chỉ mở rộng phụ thuộc vào ngữ cảnh tác vụ (task context) và dung lượng của kho lưu trữ công thức biểu trưng.

* **Ưu thế chi phí và thời gian so với các phương pháp LLM-AutoFE khác:**
  * Kiến trúc tối giản hai giai đoạn cho phép SymboLLM-FE vượt trội hoàn toàn các phương pháp AutoFE dựa trên LLM khác về tốc độ và chi phí, đơn cử như FEBP (tốn đến $43.71\text{ phút}$ theo Zou et al., 2026), mang lại hiệu quả chi phí tối ưu trong triển khai thực tế.

### 5.6 Ablation Study

* **Thiết lập thực nghiệm nghiên cứu cắt bỏ (Ablation Study Setup):**
  * Để định lượng chặt chẽ sự đóng góp riêng biệt của từng mô-đun trong SymboLLM-FE và chứng minh tính thiết yếu không thể lược bỏ của chúng, nghiên cứu tiến hành phân tích cắt bỏ toàn diện trên nhiều tập dữ liệu với các hạt giống ngẫu nhiên độc lập (independent random seeds).
  * Ba biến thể được đánh giá bằng cách loại bỏ có hệ thống các thành phần cốt lõi:
    * `w/o SP.` (without Spearman pre-sorting): Loại bỏ mô-đun tiền sắp xếp đặc trưng dựa trên giá trị tương quan Spearman.
    * `w/o ES.` (without Expanding-Sliding window): Loại bỏ cơ chế cửa sổ mở rộng-trượt, thay bằng lấy mẫu ngẫu nhiên.
    * `w/o LLM` (without LLM-guided feature generation): Loại bỏ hoàn toàn sự tham gia tinh chỉnh và tổng hợp mã của mô hình ngôn ngữ lớn, chỉ giữ lại các công thức biểu trưng thô.
    * `Baseline`: Mô hình cơ sở không áp dụng kỹ thuật sinh đặc trưng tự động.
    * `Ours`: Khung làm việc SymboLLM-FE hoàn chỉnh tích hợp đầy đủ cả ba thành phần.

* **Kết quả định lượng đóng góp của từng thành phần (Hình 4):**
  * So sánh độ chính xác trung bình (Accuracy %) giữa các biến thể:
    * `Baseline`: $75.81\%$
    * `w/o SP.`: $76.07\%$
    * `w/o ES.`: $75.92\%$
    * `w/o LLM`: $76.84\%$
    * `Ours` (SymboLLM-FE đầy đủ): $\mathbf{77.16\%}$
  * **Hình 4.** Nghiên cứu cắt bỏ định lượng đóng góp của tiền sắp xếp Spearman, cửa sổ trượt và LLM
    * <img src="assets/fig_06_p9_vector.png" alt="Hình 4" />
    * **Hình này chứng minh điều gì**
      * Cả ba thành phần SP, ES và LLM đều đóng góp thiết yếu vào hiệu năng tổng thể của SymboLLM-FE
    * **Từ đâu mà thấy được**
      * Biểu đồ cột so sánh các biến thể w/o SP, w/o ES, w/o LLM với bản đầy đủ SymboLLM-FE
      * Cột Ours đạt 77.16% Accuracy, vượt trội w/o LLM (76.84%), w/o SP (76.07%), w/o ES (75.92%) và Baseline (75.81%)

* **Phân tích vai trò chuyên biệt của từng mô-đun:**
  * Vai trò của tiền sắp xếp Spearman (`SP.`):
    * Việc loại bỏ `SP.` khiến độ chính xác giảm từ $77.16\%$ xuống $76.07\%$ (giảm $1.09\%$).
    * Chứng minh rằng việc ưu tiên các đặc trưng có tương quan cao với nhãn mục tiêu giúp thiết lập không gian tìm kiếm định hướng hiệu quả hơn rất nhiều so với việc chọn lọc đặc trưng ngẫu nhiên.
  * Vai trò của cơ chế cửa sổ mở rộng-trượt (`ES.`):
    * Việc loại bỏ `ES.` gây ra sự sụt giảm hiệu năng mạnh nhất trong các thành phần, từ $77.16\%$ xuống $75.92\%$ (giảm $1.24\%$, gần như rơi về mức Baseline $75.81\%$).
    * Khẳng định cơ chế cửa sổ có cấu trúc là nhân tố cốt lõi giúp bao quát và nắm bắt các tương tác đặc trưng bậc cao (high-order feature interactions) mà các phương pháp lấy mẫu ngẫu nhiên bỏ lỡ; qua đó xác thực chiến lược giảm độ phức tạp tính toán mà không làm tổn hại đến chất lượng đặc trưng sinh ra.
  * Vai trò của tinh chỉnh LLM (`LLM`):
    * Khi loại bỏ `LLM`, hiệu năng sụt giảm từ $77.16\%$ xuống $76.84\%$ (giảm $0.32\%$).
    * Xác nhận rằng các công thức biểu trưng thô từ SR thường mắc phải sự dư thừa hoặc triển khai mã chưa tối ưu; sự hiện diện của LLM đóng vai trò như một bộ tích hợp ngữ nghĩa then chốt (critical semantic integrator), tối ưu hóa hiệu quả thực thi mã và phối hợp logic các quy tắc để nâng cao khả năng tổng quát hóa của tập đặc trưng mới.
