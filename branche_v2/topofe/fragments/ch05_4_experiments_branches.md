## 4 Experiments

- **Mục tiêu thực nghiệm và các câu hỏi nghiên cứu cốt lõi**: Quá trình đánh giá thực nghiệm của TOPOFE được thiết kế nhằm giải quyết $6$ câu hỏi nghiên cứu (Research Questions - RQ):
  - **$\text{RQ1}$ (Hiệu năng tổng thể)**: Liệu TOPOFE có vượt trội hơn các phương pháp kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE) tiên tiến nhất (State-of-the-art - SOTA) trên các tác vụ học máy dạng bảng và đặc tính dữ liệu đa dạng không (§5.1).
  - **$\text{RQ2}$ (Tính vững chắc trước mô hình nền tảng)**: Hiệu năng của TOPOFE có bền vững (robust) trước các lựa chọn mô hình ngôn ngữ lớn nền tảng (LLM backbone) với các mức năng lực khác nhau không (§5.2).
  - **$\text{RQ3}$ (Khả năng chuyển giao của chương trình đặc trưng)**: Các chương trình đặc trưng (feature programs) do TOPOFE khám phá có khả năng chuyển giao (transferable) qua các bộ dự đoán hạ nguồn (downstream predictors) có kiến trúc khác biệt ngoài mô hình đánh giá tại thời điểm tìm kiếm hay không (§5.3).
  - **$\text{RQ4}$ (Độ đa dạng và tính bổ trợ của đặc trưng)**: Liệu TOPOFE có tạo ra các tập đặc trưng đa dạng hơn, độ dư thừa thấp (low-redundancy) và có tính bổ trợ thông tin (informationally complementary) tốt hơn các phương pháp cạnh tranh không (§5.4).
  - **$\text{RQ5}$ (Tri thức cấu trúc tô-pô thích ứng)**: Đồ thị cấu trúc tô-pô thích ứng (adaptive topology graph) có học được tri thức đặc thù theo tác vụ (task-specific knowledge) có ý nghĩa về độ hữu dụng chuyển giao liên họ (cross-family transfer utility) trong quá trình tìm kiếm không (§5.5).
  - **$\text{RQ6}$ (Đóng góp của từng thành phần)**: Từng thành phần riêng lẻ cấu thành TOPOFE đóng góp như thế nào vào hiệu năng tổng thể của toàn bộ hệ thống (§5.6).

### Datasets

- **Quy mô và nguồn gốc tập dữ liệu chuẩn đối chuẩn (benchmark datasets)**: TOPOFE được đánh giá trên $29$ tập dữ liệu bảng công khai, bao gồm $19$ tác vụ phân loại (classification tasks) và $10$ tác vụ hồi quy (regression tasks).
  - Dữ liệu được thu thập từ ba nguồn chuẩn: Kho lưu trữ học máy UCI (UCI Machine Learning Repository), Kaggle, và OpenML, tuân thủ đúng giao thức lựa chọn tập dữ liệu từ các công trình trước.
- **Phạm vi đa dạng và đặc tính kỹ thuật của benchmark**:
  - Quy mô số lượng mẫu quan sát: $n_{\text{inst}} \in [315, 581012]$.
  - Chiều không gian đặc trưng ban đầu: $n_{\text{feat}} \in [4, 279]$.
  - Đa dạng kiểu dữ liệu không đồng nhất (heterogeneous feature types): bao gồm biến số (numerical), biến phân loại (categorical), và biến thời gian (temporal).
  - Thống kê chi tiết từng tập dữ liệu được ghi nhận toàn diện trong Bảng 1 và Bảng 2 của công trình.
- **Siêu dữ liệu có cấu trúc ($\mathcal{M}$)**: Mỗi tập dữ liệu được cung cấp siêu dữ liệu cấu trúc $\mathcal{M}$ gồm:
  - Bản mô tả mục tiêu cấp tác vụ (task-level descriptions).
  - Chú giải ngữ nghĩa chi tiết cho từng đặc trưng (per-feature semantic annotations), được dùng làm điều kiện ngữ cảnh dẫn đường cho quá trình sinh chương trình của LLM.
- **Giao thức phân chia dữ liệu và tính lặp lại thực nghiệm**:
  - Dữ liệu được phân chia cố định theo tỷ lệ $80/20$ giữa tập huấn luyện (train split) và tập kiểm thử (test split).
  - Tập huấn luyện ($80\%$) được sử dụng độc quyền cho quá trình tìm kiếm đặc trưng, kiểm định chéo (cross-validation), và huấn luyện tham số mô hình (model fitting).
  - Tập kiểm thử ($20\%$) được giữ lại độc lập (held out) hoàn toàn cho việc đánh giá khách quan cuối cùng (final unbiased evaluation).
  - Mọi thực nghiệm đều được lặp lại qua $5$ lượt chạy độc lập với các hạt giống ngẫu nhiên (random seeds) và phép phân chia dữ liệu khác nhau; kết quả báo cáo dưới dạng giá trị trung bình kèm độ lệch chuẩn ($\text{mean} \pm \text{standard deviation}$).

### Baselines

- **Các phương pháp đối chuẩn (baselines) tiên tiến**: TOPOFE được so sánh toàn diện với $6$ phương pháp AutoFE tiên tiến nhất (SOTA AutoFE methods), phân bổ trên $3$ nhóm chính:
  - **Nhóm phương pháp cổ điển (Classical methods)**: OpenFE và AutoFeat.
  - **Nhóm phương pháp dựa trên LLM (LLM-based methods)**: CAAFE, FeatLLM, và OCTree.
  - **Nhóm tìm kiếm tiến hóa dẫn đường bởi LLM (LLM-guided evolutionary search)**: LLM-FE — phương pháp đối chuẩn cơ sở có mối liên hệ gần gũi nhất khi cùng chia sẻ kiến trúc tiến hóa đa quần thể (multi-population evolutionary architecture).
- **Kiểm soát điều kiện thực nghiệm đối chuẩn**: Tất cả các phương pháp dựa trên LLM đều sử dụng cùng mô hình nền tảng (backbone model) và cùng thiết lập tham số sinh như TOPOFE nhằm đảm bảo môi trường so sánh có đối chứng nghiêm ngặt và công bằng.

### Evaluation Protocol

- **Thước đo đánh giá hiệu năng (Performance metrics)**:
  - Tác vụ phân loại: đo lường bằng độ chính xác (Accuracy $\uparrow$, càng cao càng tốt).
  - Tác vụ hồi quy: đo lường bằng sai số bình phương trung bình căn (Root Mean Square Error - $\text{RMSE} \downarrow$, càng thấp càng tốt).
- **Quy trình đánh giá đặc trưng hai giai đoạn (Two-stage feature evaluation procedure)**:
  - **Giai đoạn 1 (Xây dựng biểu diễn tăng cường)**: Đối với mỗi tập đặc trưng ứng viên $S$, thực thi từng chương trình biến đổi $p \in S$ trên tập dữ liệu huấn luyện để hình thành không gian biểu diễn tăng cường $T_S(X_{\text{tr}})$.
  - **Giai đoạn 2 (Đánh giá tín hiệu độ phù hợp)**: Huấn luyện một mô hình dự đoán hạ nguồn $f^*_S$ trên tập dữ liệu huấn luyện đã tăng cường, sau đó ước lượng tín hiệu độ phù hợp (fitness signal) $\hat{\Phi}(S)$ trên tập kiểm định độc lập thông qua kiểm định chéo phân tầng 5 lần ($5$-fold stratified cross-validation) theo Phương trình (6).
- **Bộ dự đoán hạ nguồn mặc định**: XGBoost được chọn làm bộ dự đoán hạ nguồn mặc định cho tất cả các phương pháp với cùng giao thức huấn luyện/kiểm định, cùng ngân sách đánh giá (evaluation budgets), và cùng cấu hình mô hình để đảm bảo tính so sánh tương quan chuẩn mực.

### Implementation Details

- **Mô hình ngôn ngữ nền tảng và tham số lấy mẫu**:
  - Ba mô hình nền tảng được triển khai cho tất cả các phương pháp dựa trên LLM: Qwen3-8B, Qwen2.5-Coder, và GPT-4o-mini.
  - Nhiệt độ lấy mẫu (sampling temperature) được thiết lập cố định ở mức $\tau = 0.8$ cho mọi lượt gọi sinh mã của LLM (trừ khi có ghi chú riêng).
- **Cấu hình các đảo chuyên hóa (Family-specialised islands)**:
  - Khởi tạo $M = 5$ đảo chuyên hóa tương ứng với $5$ họ toán tử biến đổi kinh điển (§3.1): tương tác số học (arithmetic interactions - $\mathcal{P}_1$), tập hợp thống kê (statistical aggregates - $\mathcal{P}_2$), đặc trưng chuỗi thời gian (temporal features - $\mathcal{P}_3$), mã hóa quan hệ (relational encodings - $\mathcal{P}_4$), và ánh xạ phi tuyến đơn biến (nonlinear univariate maps - $\mathcal{P}_5$).
  - Tại mỗi thế hệ, mỗi lượt gọi LLM sinh ra $b = 3$ chương trình đặc trưng ứng viên dưới dạng hàm Python có thể thực thi độc lập.
- **Cấu trúc khung câu lệnh (Prompt structure)**: Mỗi câu lệnh nhắc LLM bao gồm $4$ thành phần chuẩn tắc:
  - Siêu dữ liệu cấp tác vụ $\mathcal{M}_{\text{task}}$: tóm tắt mục tiêu dự đoán và biến đích cần dự báo.
  - Siêu dữ liệu cấp đặc trưng $\mathcal{M}_{\text{feat}}$: tên đặc trưng, kiểu giá trị, và mô tả ngữ nghĩa cô đọng trong một câu, kèm theo các giá trị phân loại tiêu biểu cho các biến hạng mục.
  - Mẫu minh họa trong ngữ cảnh (in-context demonstrations): trích xuất trực tiếp từ kho lưu trữ tinh hoa của đảo $\mathcal{A}_i^{(t)}$, đóng vai trò mẫu chương trình chất lượng cao làm tiền đề cho quá trình đột biến (mutation), lai ghép (crossover), hoặc tổng hợp lai ghép (hybrid synthesis).
  - Quy cách định dạng đầu ra nghiêm ngặt: ràng buộc sinh hàm biến đổi đặc trưng bằng Python hợp lệ cú pháp.
  - Ngữ cảnh bổ trợ: Bổ sung một lượng nhỏ các mẫu quan sát huấn luyện đã được tuần tự hóa kèm nhãn thực tế làm ngữ cảnh tác vụ cho LLM.
- **Quy trình thẩm định chương trình có hệ thống (Systematic validation)**:
  - Mọi chương trình được sinh ra đều phải trải qua kiểm tra cú pháp (syntax checking), xác thực tính nhất quán về kiểu dữ liệu (type consistency verification), bộ lọc an toàn số học (numerical-safety filtering, như chống chia cho 0 và ngăn tràn số), cùng kiểm tra tính tương thích siêu dữ liệu trước khi đưa vào bước đánh giá độ phù hợp.
- **Tham số bộ nhớ tăng cường theo prompt (Prompt-Augmented Memory - PAM)**:
  - Độ dài cửa sổ lịch sử trượt (sliding history window): $W = 5$ thế hệ.
  - Chuỗi bộ nhớ prompt được cập nhật sau mỗi thế hệ qua một lượt gọi LLM tóm tắt, có điều kiện hóa dựa trên lịch sử thành công $\mathcal{H}_i^+(t)$ và lịch sử thất bại $\mathcal{H}_i^-(t)$.
- **Tham số kho lưu trữ tinh hoa (Elite archive)**:
  - Sức chứa tối đa: $|\mathcal{A}|_{\max} = 20$ chương trình cho mỗi đảo.
  - Đảm bảo tính mới về mặt cấu trúc (structural novelty): áp dụng ngưỡng khoảng cách chỉnh sửa cây chuẩn hóa (normalized tree-edit distance threshold) tối thiểu $\delta_{\min} = 0.1$.
- **Tham số đồ thị cấu trúc tô-pô (Topology graph)**:
  - Hệ số suy giảm trung bình động lũy thừa (exponential moving average decay coefficient): $\alpha = 0.3$.
  - Ngưỡng phát hiện bão hòa (saturation threshold): $\varepsilon = 0.01$ trên cửa sổ trượt gồm $W = 5$ thế hệ liên tiếp.
- **Hệ số hàm mục tiêu thống nhất (Unified objective, Eq. 15)**:
  - Hệ số phạt độ dư thừa: $\lambda_1 = 0.3$.
  - Trọng số độ ổn định: $\lambda_2 = 0.1$.
  - Trọng số chi phí tính toán: $\lambda_3 = 0.1$.
- **Hợp nhất tập đặc trưng cuối cùng (Final feature assembly)**:
  - Sau khi kết thúc quá trình tìm kiếm, các chương trình tinh hoa từ toàn bộ kho lưu trữ của các đảo được gộp chung.
  - Thực hiện thuật toán chọn lọc tham lam theo thứ hạng điểm kiểm định (greedy validation-score-ranked selection) để chọn tối đa $5$ chương trình không dư thừa.
  - Loại bỏ các chương trình ứng viên có hệ số tương quan Spearman tuyệt đối (absolute Spearman correlation) vượt ngưỡng $\tau_{\text{red}} = 0.9$ so với bất kỳ đặc trưng nào đã được chọn trước đó.
