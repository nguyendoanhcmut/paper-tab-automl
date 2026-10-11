## Appendix B: Prompt Design

* **Mục đích tài liệu hóa**: Phần này ghi lại toàn bộ hệ thống prompt của TOPOFE, được tổ chức và phân loại theo chức năng chuyên biệt (*organized by function*).

### B.1 Feature-Understanding Call

* **Mục tiêu của lời gọi hiểu đặc trưng (*Feature-Understanding Call*)**: Khởi tạo hiểu biết ngữ cảnh về bộ dữ liệu và tác vụ dự đoán trước khi tiến hành sinh chương trình kỹ thuật đặc trưng (*feature engineering program generation*).
* **Cấu trúc vai trò (`<Role>`)**:
  * Định vị mô hình là nhà khoa học làm việc trên tác vụ tạo chương trình kỹ thuật đặc trưng: *"You are an scientist working on feature engineering program generation."*
* **Đặc tả nhiệm vụ (`<Task>`)**:
  * Yêu cầu trước tiên phải hiểu các đặc trưng của bộ dữ liệu và nhiệm vụ học máy cần giải quyết.
  * Lập luận tường minh (*explicitly reason*) về mối quan hệ giữa các đặc trưng đầu vào và mục tiêu dự đoán (*prediction target*).
  * Giả định tất cả các đặc trưng đầu vào đều có thể sử dụng được; không loại trừ hoặc hạ thấp mức độ ưu tiên của bất kỳ cột nào (*do not exclude or de-prioritize any column*).
  * Đầu vào tác vụ gồm hai trường:
    * `Target: {task_description}`: Mô tả biến mục tiêu của bài toán.
    * `Columns: {comma-separated columns}`: Danh sách các cột đầu vào phân tách bằng dấu phẩy.
* **Quy cách định dạng đầu ra (`<Output>`)**:
  * Yêu cầu trả về các gạch đầu dòng súc tích (*concise bullets*) gồm ba nội dung:
    1. Các mối quan hệ tiềm năng giữa đặc trưng và mục tiêu dự đoán (chiều biến thiên / *direction*, tính phi tuyến / *nonlinearity*, ngưỡng / *thresholds*, hiệu ứng đơn điệu / *monotonic effects* khi hợp lý).
    2. Các tương tác, tỷ lệ (*ratios*) hoặc phép tổng hợp (*aggregations*) giữa các đặc trưng có khả năng nâng cao hiệu năng dự đoán mục tiêu.
    3. Ý tưởng biến đổi cụ thể (*concrete transformation ideas*) cho từng nhóm đặc trưng chính: dữ liệu số (*numeric*), dữ liệu phân loại (*categorical*), và dữ liệu hỗn hợp (*mixed*).

### B.2 Generation Context

* **Bản chất của ngữ cảnh sinh (*Generation Context*)**: Là thành phần prompt ngữ cảnh chung được đặt ở đầu (*prepended*) cho tất cả các bước khởi tạo (*initialize*), đột biến (*mutation*), lai ghép (*crossover*), và lai liên đảo (*hybrid*).
* **Đặc tả mục tiêu sinh (`<Objective>`)**:
  * Sứ mệnh cốt lõi (*Primary mission*): Trích xuất, biến đổi và chọn lọc các biến từ dữ liệu thô bằng cách sinh mã Python kỹ thuật đặc trưng dựa trên phân tích, giúp các mô hình học máy (*machine learning models*) đạt độ chính xác và hiệu quả cao hơn (*"extract, transform, and select variables from raw data by generating feature engineering Python codes based on the analysis, making machine learning models more accurate and efficient."*).
  * Mục tiêu sinh cụ thể (*Generation objective*): Tạo ra các đặc trưng được thiết kế nắm bắt đồng thời cả hai yếu tố:
    * Mối quan hệ giữa đặc trưng và mục tiêu (*feature-to-target relationships*).
    * Mối quan hệ giữa đặc trưng với đặc trưng liên quan đến việc dự đoán mục tiêu (*feature-to-feature relationships relevant to target prediction*).
  * Giới hạn ràng buộc: Tránh các phép biến đổi tùy tiện không gắn liền với tín hiệu hữu ích cho dự đoán mục tiêu (*avoid arbitrary transformations that are not tied to target-relevant signal*).
  * Yêu cầu chú thích: Bắt buộc mở đầu mã nguồn bằng một câu chuỗi tài liệu (*docstring*) ngắn gọn mô tả mục đích biến đổi (*transformation intent*).

### B.3 Generation Rules

* **Vai trò chuyên gia (`<Role>`)**:
  * Định vị mô hình là nhà khoa học dữ liệu (*data scientist*) có kiến thức chuyên sâu về bộ dữ liệu được cung cấp.
  * Vai trò cụ thể là nhận diện và thiết kế các đặc trưng giàu thông tin nhằm giải quyết tác vụ `<Task>` một cách hiệu quả.
* **Bộ chỉ dẫn sinh mã (`<Instructions>`)**:
  * Chỉ trả về các dòng mã Python thuần túy (*Return Python code lines only*).
  * Đảm bảo mã nguồn hoàn toàn có thể thực thi được (*Ensure the code is executable*).
  * Viết phần thân (*BODY*) của hàm `generated_feature(df)`.
  * Không sử dụng các biến giữ chỗ hoặc tên chưa được định nghĩa (*placeholders/undefined names*) như `member1`, `feature1`, `x`, `y`.
  * Không tạo các dataframe mẫu hoặc thử nghiệm (*toy/sample dataframes*); chỉ thao tác trực tiếp trên `df` được truyền vào.
  * Tránh cung cấp bất kỳ mô tả hay văn bản giải thích bổ sung nào bên ngoài mã nguồn.
  * Sử dụng các lệnh gọi toán tử hợp lệ với đối số là chuỗi dữ liệu (*Series*) của dataframe.
  * Toán tử được phép áp dụng cho họ đặc trưng hiện tại được quy định qua biến `{family_guide}`.
  * Họ đặc trưng hiện tại được xác định bởi tham số `{family_name}`.

### B.4 Initialization Prompt

* **Mục tiêu của prompt khởi tạo (*Initialization Prompt*)**: Gieo mầm (*seeds*) cho từng đảo biến đổi bằng một chương trình đường cơ sở mạnh (*strong baseline program*).
* **Cấu trúc ghép nối prompt**:
  * Kết hợp ngữ cảnh sinh và quy tắc sinh theo mẫu: `{prompt_context}{generation_rules}`.
* **Nhiệm vụ sinh đặc trưng cơ sở**:
  * Tạo ra duy nhất MỘT (*Produce ONE*) chương trình đặc trưng ban đầu thuộc họ `{family_name}`.
  * Sử dụng ít nhất hai cột nguồn (*two source columns*), hoặc một phép tổng hợp theo trục `axis=1` trên nhiều cột (*aggregation across many columns*).
  * Dựa vững trên các ghi chú phân tích (*analysis notes*); bảo đảm đây là một chương trình đường cơ sở mạnh mẽ, độc lập (*strong, self-contained baseline*) cho họ toán tử này.

### B.5 Mutation Prompt

* **Mục tiêu của prompt đột biến (*Mutation Prompt*)**: Điều chỉnh, biến đổi một chương trình cha đơn lẻ (*single parent program*) có điều kiện hóa dựa trên các tín hiệu phản hồi từ bộ nhớ thích ứng PAM (*Prompt Adaptation Memory*).
* **Cấu trúc ngữ cảnh đầu vào**:
  * Ghép nối `{prompt_context}{generation_rules}` cùng các trường điều kiện:
    * `Family: {family_name}`: Xác định họ biến đổi đang xử lý.
    * `Parent program: {parent.code}`: Mã nguồn của chương trình cha cần đột biến.
    * `Preferred patterns (recently rewarded): {prefer}`: Các mẫu hình được ưu tiên (đã nhận thưởng gần đây).
    * `Avoid patterns (recently rejected/redundant): {avoid}`: Các mẫu hình cần tránh (bị từ chối hoặc dư thừa gần đây).
* **Yêu cầu kỹ thuật đối với phép đột biến**:
  * Đột biến chương trình cha thành một đặc trưng `{family_name}` khác biệt và mạnh hơn.
  * Thay đổi cấu trúc một cách thực chất (*meaningfully*): hoán đổi một toán tử, bổ sung một phép biến đổi ổn định hóa (*stabilizing transform*), hoặc đưa thêm một cột dữ liệu khác nhằm tránh việc đầu ra chỉ là phiên bản co giãn tỷ lệ (*rescaled version*) của chương trình cha.
* **Cơ chế dẫn đường từ bộ nhớ PAM**:
  * Các trường `{prefer}` và `{avoid}` được trích xuất trực tiếp từ vector bộ nhớ prompt $\rho_i(t)$ (*prompt-memory vector*).
  * Cung cấp chỉ dẫn định hướng tường minh thu được từ lịch sử tích lũy chấp nhận / từ chối (*accumulated accept/reject history*) của đảo thứ $i$ theo Phương trình (8) (Eq. 8).

### B.6 Crossover Prompt

* **Mục tiêu của prompt lai ghép (*Crossover Prompt*)**: Tổng hợp một chương trình con mới từ hai chương trình cha cùng thuộc một đảo biến đổi (*within the same island*).
* **Cấu trúc ngữ cảnh đầu vào**:
  * Ghép nối `{prompt_context}{generation_rules}` kèm thông tin hai cha:
    * `Family: {family_name}`: Họ biến đổi chung của cả hai cha.
    * `Parent A: {p1.code}`: Mã nguồn chương trình cha A.
    * `Parent B: {p2.code}`: Mã nguồn chương trình cha B.
* **Chỉ dẫn tổng hợp cấu trúc**:
  * Kết hợp ý tưởng cấu trúc hữu ích nhất từ mỗi cha thành một đặc trưng mới thuộc họ `{family_name}`.
  * Nghiêm cấm việc ghép nối nguyên văn (*verbatim*); phải tổng hợp thành một tín hiệu nhất quán, có khả năng cải thiện so với cả hai chương trình cha và duy trì độ dư thừa thấp (*low-redundancy*).

### B.7 Cross-Island Hybrid Synthesis Prompt

* **Cơ chế kích hoạt và không gian tìm kiếm**:
  * Được kích hoạt khi phát hiện trạng thái bão hòa (*saturation detection*) trên đảo đích.
  * Sinh các chương trình nằm trong không gian hợp thành chung $P_i \circ P_j$ (*joint composition space*).
* **Cấu trúc ngữ cảnh đầu vào**:
  * Ghép nối `{prompt_context}{generation_rules}` cùng đặc tả hai họ:
    * `TARGET FAMILY: {target.family_name}`: Họ đặc trưng của đảo đích.
    * `DONOR FAMILY: {donor.family_name}`: Họ đặc trưng của đảo cho (*donor*).
    * `Target parent (stay in this family’s style): {p_t.code}`: Chương trình cha của đảo đích (yêu cầu duy trì phong cách của họ đích).
    * `Donor parent (borrow ONE idea from a different family): {p_d.code}`: Chương trình cha của đảo cho (mượn MỘT ý tưởng từ họ khác).
* **Yêu cầu tổng hợp lai (*Hybrid Synthesis*)**:
  * Ngữ cảnh kích hoạt: Đảo đích đã rơi vào trạng thái đình trệ (*stagnated*).
  * Nhập khẩu duy nhất một ý tưởng cấu trúc hữu ích từ đảo cho: một toán tử (*operator*), một phép chuẩn hóa (*normalization*), hoặc một chiến lược gom nhóm (*grouping strategy*).
  * Tái diễn đạt (*re-express*) ý tưởng đó dưới dạng một đặc trưng thuộc họ đích `{target.family_name}`.
  * Không sao chép nguyên trạng bất kỳ cha nào; kết quả tạo ra phải bền vững (*robust*), phi tầm thường (*non-trivial*), và mới lạ về mặt cấu trúc (*structurally novel*) so với các đặc trưng hiện có của đảo đích.
