## 4 Experiments

* Thực nghiệm được thiết kế nhằm giải quyết $6$ câu hỏi nghiên cứu (Research Questions - RQ) cốt lõi:
  * **RQ1**: Liệu TOPOFE có vượt trội hơn các phương pháp AutoFE tiên tiến nhất (state-of-the-art AutoFE methods) trên các tác vụ học dữ liệu bảng và đặc tính bộ dữ liệu đa dạng không? (§5.1)
  * **RQ2**: Hiệu năng của TOPOFE có bền vững (robust) trước việc lựa chọn mô hình nền LLM (LLM backbone) với các mức năng lực khác nhau không? (§5.2)
  * **RQ3**: Các chương trình đặc trưng (feature programs) được TOPOFE phát hiện có khả năng chuyển giao (transferable) qua các mô hình dự đoán hạ nguồn có kiến trúc khác biệt vượt ra ngoài mô hình đánh giá lúc tìm kiếm không? (§5.3)
  * **RQ4**: TOPOFE có tạo ra các tập đặc trưng đa dạng hơn, độ dư thừa thấp hơn và bổ trợ thông tin tốt hơn so với các phương pháp cạnh tranh không? (§5.4)
  * **RQ5**: Đồ thị topo thích ứng (adaptive topology graph) có thu nhận được tri thức đặc thù tác vụ có ý nghĩa về độ hữu dụng chuyển giao liên họ (cross-family transfer utility) trong quá trình tìm kiếm không? (§5.5)
  * **RQ6**: Từng thành phần cấu thành TOPOFE đóng góp như thế nào vào hiệu năng tổng thể của phương pháp? (§5.6)

### Datasets

* Đánh giá thực nghiệm được thực hiện trên $29$ bộ dữ liệu bảng công khai (public tabular datasets) bao gồm $19$ tác vụ phân loại (classification tasks) và $10$ tác vụ hồi quy (regression tasks).
  * Nguồn dữ liệu được thu thập từ UCI Machine Learning Repository (Asuncion et al., $2007$), Kaggle, và OpenML (Vanschoren et al., $2014$), tuân thủ theo giao thức lựa chọn bộ dữ liệu của các nghiên cứu tiền nhiệm (Hollmann et al., Han et al., $2024$, Abhyankar et al., $2025$).
  * Bộ chuẩn đối sánh (benchmark) bao quát đa dạng tác vụ dự đoán, quy mô mẫu dữ liệu ($n_{\text{inst}} \in [315, 581012]$), số chiều đặc trưng ($n_{\text{feat}} \in [4, 279]$), cùng các kiểu đặc trưng không đồng nhất bao gồm biến số (numerical), biến phân loại (categorical), và biến thời gian (temporal variables).
  * Thống kê chi tiết về các bộ dữ liệu được trình bày tại Bảng 1 (Table 1) và Bảng 2 (Table 2).
* Mỗi bộ dữ liệu đi kèm với siêu dữ liệu có cấu trúc $\mathcal{M}$ (structured metadata) gồm phần mô tả cấp tác vụ (task-level descriptions) và các chú giải ngữ nghĩa trên từng đặc trưng (per-feature semantic annotations) dùng để điều kiện hóa quá trình sinh của LLM.
* Giao thức phân chia dữ liệu và đánh giá thực nghiệm:
  * Tất cả các bộ dữ liệu được phân chia cố định theo tỷ lệ tập huấn luyện / kiểm thử là $80/20$ (fixed $80/20$ train/test split).
  * Phân vùng huấn luyện (training partition) được sử dụng độc quyền cho việc tìm kiếm đặc trưng, kiểm định chéo (cross-validation), và khớp mô hình (model fitting).
  * Phân vùng kiểm thử (test partition) được giữ lại hoàn toàn phục vụ đánh giá khách quan cuối cùng (final unbiased evaluation).
  * Tất cả các thực nghiệm được lặp lại qua $5$ lượt chạy (five runs) với các hạt ngẫu nhiên (random seeds) và phân chia dữ liệu khác nhau; kết quả được báo cáo dưới dạng trung bình $\pm$ độ lệch chuẩn ($\text{mean} \pm \text{std}$).

### Baselines

* TOPOFE được đối chuẩn so sánh với $6$ phương pháp AutoFE tiên tiến nhất (SOTA AutoFE methods) thuộc $3$ nhóm chính:
  * (i) Các phương pháp cổ điển (classical methods): OpenFE (Zhang et al., $2023\text{a}$) và AutoFeat (Horn et al., $2019$).
  * (ii) Các phương pháp dựa trên LLM (LLM-based methods): CAAFE (Hollmann et al., $2023\text{a}$), FeatLLM (Han et al., $2024$), và OCTree (Nam et al., $2024$).
  * (iii) Tìm kiếm tiến hóa dẫn dắt bởi LLM (LLM-guided evolutionary search): LLM-FE (Abhyankar et al., $2025$), phương pháp đối chuẩn cơ sở có mối liên hệ mật thiết nhất khi cùng chia sẻ kiến trúc tiến hóa đa quần thể (multi-population evolutionary architecture).
* Kiểm soát điều kiện thử nghiệm công bằng: Tất cả các phương pháp dựa trên LLM đều sử dụng chung một mô hình nền (backbone model) và cùng cấu hình sinh (generation settings) như TOPOFE để đảm bảo việc so sánh có kiểm soát (controlled comparison).

### Evaluation Protocol

* Tiêu chuẩn đo lường hiệu năng:
  * Hiệu năng phân loại được đo bằng độ chính xác (accuracy $\uparrow$).
  * Hiệu năng hồi quy được đo bằng căn bậc hai sai số toàn phương trung bình (Root Mean Square Error - RMSE $\downarrow$).
* Quy trình đánh giá đặc trưng gồm hai giai đoạn (two-stage feature evaluation procedure):
  * Giai đoạn 1: Với tập đặc trưng ứng viên $S$, thực thi từng chương trình $p \in S$ trên dữ liệu huấn luyện để xây dựng biểu diễn tăng cường $T_S(X_{\text{tr}})$.
  * Giai đoạn 2: Huấn luyện bộ dự đoán hạ nguồn $f_S^*$ trên tập huấn luyện tăng cường và đánh giá tín hiệu độ thích nghi $\hat{\Phi}(S)$ trên tập kiểm định giữ lại qua kiểm định chéo phân tầng 5 lượt (5-fold stratified cross-validation) theo định nghĩa tại Công thức (6).
* Bộ dự đoán hạ nguồn mặc định:
  * XGBoost được sử dụng làm bộ dự đoán hạ nguồn mặc định (default downstream predictor) cho tất cả các phương pháp để đảm bảo so sánh công bằng.
  * Các phương pháp áp dụng đồng nhất giao thức huấn luyện/kiểm định, ngân sách đánh giá (evaluation budgets), và cấu hình mô hình (model configurations), trừ khi có quy định khác rõ ràng.

### Implementation Details

* Triển khai mô hình nền LLM và tham số sinh:
  * Tất cả các phương pháp dựa trên LLM được triển khai với ba mô hình nền (backbone models): Qwen3-8B (Yang et al., $2025\text{a}$), Qwen2.5-Coder (Hui et al., $2024$), và GPT-4o-mini (Hurst et al., $2024$).
  * Nhiệt độ lấy mẫu (sampling temperature) được đặt là $\tau = 0.8$ cho tất cả các lượt gọi sinh LLM, trừ khi có chỉ định khác.
* Thiết lập hệ thống đảo tiến hóa của TOPOFE:
  * Khởi tạo $M = 5$ đảo chuyên biệt hóa theo họ biến đổi (family-specialised islands) tương ứng với 5 họ biến đổi chuẩn tắc xác định tại §3.1: tương tác số học ($P_1$), tổng hợp thống kê ($P_2$), đặc trưng thời gian ($P_3$), mã hóa quan hệ ($P_4$), và ánh xạ phi tuyến đơn biến ($P_5$).
  * Tại mỗi thế hệ, mỗi lượt gọi LLM sinh ra $b = 3$ chương trình đặc trưng ứng viên (candidate feature programs) dưới dạng các hàm Python thực thi được (executable Python functions).
* Cấu trúc prompt đầu vào cho LLM gồm 4 thành phần:
  * (i) Siêu dữ liệu cấp tác vụ $\mathcal{M}_{\text{task}}$ tóm tắt mục tiêu dự đoán và biến mục tiêu (target variable).
  * (ii) Siêu dữ liệu cấp đặc trưng $\mathcal{M}_{\text{feat}}$ gồm tên đặc trưng, kiểu giá trị, và mô tả ngữ nghĩa một câu, kèm theo các giá trị danh mục tiêu biểu đối với biến phân loại.
  * (iii) Trực quan hóa mẫu trong ngữ cảnh (in-context demonstrations) trích xuất từ kho lưu trữ tinh hoa của đảo $\mathcal{A}_i^{(t)}$, cung cấp các chương trình chất lượng cao đã phát hiện trước đó làm hình mẫu cho quá trình đột biến (mutation), lai ghép (crossover), hoặc tổng hợp lai (hybrid synthesis).
  * (iv) Đặc tả định dạng đầu ra nghiêm ngặt (strict output format specification) yêu cầu một hàm biến đổi đặc trưng Python hợp lệ về mặt cú pháp.
  * Bổ sung ngữ cảnh tác vụ: Một số lượng nhỏ các mẫu huấn luyện tuần tự hóa kèm nhãn thực tế (serialized training instances with ground-truth labels) được đưa vào ngữ cảnh tác vụ theo Dinh et al. ($2022$) và Han et al. ($2024$).
* Quy trình kiểm định hệ thống chương trình:
  * Tất cả các chương trình do LLM sinh ra đều trải qua quy trình kiểm định hệ thống (systematic validation) trước khi đánh giá độ thích nghi, bao gồm: kiểm tra cú pháp (syntax checking), xác minh tính nhất quán kiểu (type consistency verification), lọc an toàn số học (numerical-safety filtering, ví dụ: chốt chặn chia cho 0 và tràn số), và kiểm tra tính nhất quán với siêu dữ liệu (metadata-consistency checks).
* Tham số cấu hình bộ nhớ thích ứng prompt PAM (Prompt Adaptation Memory):
  * Cửa sổ lịch sử trượt (sliding history window) được thiết lập ở mức $W = 5$ thế hệ.
  * Chuỗi bộ nhớ prompt (prompt-memory string) được cập nhật sau mỗi thế hệ thông qua một lượt gọi tóm tắt LLM có điều kiện trên tập thành công $\mathcal{H}_i^+(t)$ và tập thất bại $\mathcal{H}_i^-(t)$.
  * Dung lượng kho lưu trữ tinh hoa (elite archive capacity): $|\mathcal{A}|_{\max} = 20$ chương trình cho mỗi đảo.
  * Tính mới cấu trúc (structural novelty) được thực thi nghiêm ngặt qua ngưỡng khoảng cách chỉnh sửa cây chuẩn hóa (normalized tree-edit distance threshold): $\delta_{\min} = 0.1$.
* Tham số cấu hình đồ thị topo và hàm mục tiêu hợp nhất:
  * Hệ số suy giảm trung bình động lũy thừa (exponential moving average decay coefficient): $\alpha = 0.3$.
  * Ngưỡng bão hòa (saturation threshold): $\varepsilon = 0.01$ trên cửa sổ trượt $W = 5$ thế hệ liên tiếp.
  * Các trọng số trong hàm mục tiêu hợp nhất (unified objective, Công thức 15):
    * Hệ số phạt dư thừa (redundancy penalty coefficient): $\lambda_1 = 0.3$.
    * Trọng số độ ổn định (stability weight): $\lambda_2 = 0.1$.
    * Trọng số chi phí tính toán (cost weight): $\lambda_3 = 0.1$.
* Quy trình lắp ráp tập đặc trưng cuối cùng (final feature set assembly):
  * Sau khi kết thúc tìm kiếm, tập đặc trưng cuối cùng được tổng hợp bằng cách gom chung các chương trình tinh hoa từ kho lưu trữ của tất cả các đảo.
  * Lựa chọn tối đa $5$ chương trình không dư thừa thông qua thuật toán tham lam xếp hạng theo điểm kiểm định (greedy validation-score-ranked selection).
  * Loại bỏ các ứng viên có hệ số tương quan Spearman tuyệt đối (absolute Spearman correlation) với bất kỳ đặc trưng nào đã được chọn trước đó vượt quá ngưỡng $\tau_{\text{red}} = 0.9$.
