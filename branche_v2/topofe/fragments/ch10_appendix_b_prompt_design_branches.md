## Appendix B Prompt Design

* **Mục đích tài liệu hóa của Phụ lục B**: Phụ lục này tài liệu hóa chi tiết toàn bộ các câu lệnh nhắc (prompts) của khung làm việc TOPOFE, được tổ chức và chuẩn hóa theo từng chức năng trong quy trình tiến hóa đặc trưng.
    * Hệ thống prompt được thiết kế theo kiến trúc mô-đun phân tầng: các thành phần ngữ cảnh chung (`Generation Context`) và quy tắc thực thi (`Generation Rules`) được dùng chung làm tiền tố cho toàn bộ các thao tác sinh mã khởi tạo, đột biến, lai ghép và lai ghép chéo giữa các đảo.

### B.1 Feature-Understanding Call

* **Mục tiêu của cuộc gọi thấu hiểu đặc trưng (`Feature-Understanding Call`)**: Phân tích sơ bộ ngữ cảnh bài toán và đặc trưng của tập dữ liệu trước khi thực hiện sinh mã chương trình kỹ thuật đặc trưng.
* **Định nghĩa vai trò (`<Role>`)**: Thiết lập vai trò cho mô hình ngôn ngữ lớn:
    * `"You are an scientist working on feature engineering program generation."` (Bạn là một nhà khoa học nghiên cứu về sinh chương trình kỹ thuật đặc trưng).
* **Nhiệm vụ trọng tâm (`<Task>`)**:
    * Mô hình phải thấu hiểu các đặc trưng của tập dữ liệu và bài toán học máy trước tiên.
    * Suy luận tường minh về mối quan hệ giữa các đặc trưng đầu vào và biến mục tiêu dự đoán (`prediction target`).
    * Giả định toàn bộ các đặc trưng đầu vào đều có thể sử dụng được (`usable`), nghiêm cấm loại trừ hoặc hạ thấp độ ưu tiên của bất kỳ cột dữ liệu nào.
    * Tham số biến mục tiêu: `Target: {task_description}`.
    * Tham số danh sách cột: `Columns: {comma-separated columns}`.
* **Cấu trúc đầu ra chuẩn hóa (`<Output>`)**: Yêu cầu trả về các gạch đầu dòng súc tích gồm 3 nội dung bắt buộc:
    * 1) Các mối quan hệ tiềm năng giữa đặc trưng và biến mục tiêu: chiều hướng tác động (direction), tính phi tuyến (nonlinearity), các ngưỡng giá trị (thresholds), và tác động đơn điệu (monotonic effects) khi hợp lý.
    * 2) Các tương tác, tỷ lệ, hoặc phép tổng hợp gom nhóm (`interactions/ratios/aggregations`) tiềm năng giữa các đặc trưng có khả năng cải thiện độ chính xác dự đoán mục tiêu.
    * 3) Ý tưởng biến đổi cụ thể (`concrete transformation ideas`) cho từng nhóm đặc trưng chính: dữ liệu số (numeric), dữ liệu phân loại (categorical), và dữ liệu hỗn hợp (mixed).

### B.2 Generation Context

* **Bản chất của ngữ cảnh sinh mã (`Generation Context`)**: Thành phần ngữ cảnh chia sẻ dùng chung (`{prompt_context}`), luôn được gắn vào trước (prepended) các prompt khởi tạo (`initialization`), đột biến (`mutation`), lai ghép (`crossover`), và lai ghép chéo giữa các đảo (`hybrid`).
* **Mục tiêu tổng quát (`<Objective>`)**:
    * Sứ mệnh cốt lõi (Primary mission): `"extract, transform, and select variables from raw data by generating feature engineering Python codes based on the analysis, making machine learning models more accurate and efficient."` (Trích xuất, biến đổi và chọn lọc các biến từ dữ liệu thô bằng cách sinh mã Python kỹ thuật đặc trưng dựa trên phân tích, giúp mô hình học máy chính xác và hiệu quả hơn).
    * Mục tiêu sinh mã song hành (Generation objective): Tạo ra các đặc trưng kỹ thuật nắm bắt đồng thời cả hai dạng quan hệ:
        * Mối quan hệ giữa đặc trưng với biến mục tiêu (`feature-to-target relationships`).
        * Mối quan hệ giữa các đặc trưng với nhau có liên quan đến việc dự đoán biến mục tiêu (`feature-to-feature relationships relevant to target prediction`).
    * Ràng buộc tín hiệu: Nghiêm cấm tạo ra các phép biến đổi tùy tiện không gắn liền với tín hiệu hữu ích cho bài toán dự đoán mục tiêu.
    * Quy ước tài liệu hóa mã nguồn: Bắt buộc mở đầu bằng một chuỗi tài liệu (docstring) ngắn gọn đúng một câu mô tả ý đồ biến đổi (`transformation intent`).

### B.3 Generation Rules

* **Định nghĩa vai trò chuyên gia (`<Role>`)**:
    * `"You are a data scientist with expert knowledge about the provided dataset. Your role is to identify and engineer informative features to solve the <Task> effectively."` (Bạn là một nhà khoa học dữ liệu sở hữu tri thức chuyên gia về tập dữ liệu được cung cấp, có vai trò xác định và thiết kế các đặc trưng giàu thông tin nhằm giải quyết `<Task>` hiệu quả).
* **Các chỉ dẫn thực thi nghiêm ngặt (`<Instructions>`)**:
    * Chỉ trả về các dòng mã lệnh Python thuần túy (`Return Python code lines only`).
    * Đảm bảo mã nguồn hoàn toàn có thể thực thi được (`executable`).
    * Viết phần thân (BODY) của hàm có chữ ký: `generated_feature(df)`.
    * Tuyệt đối không sử dụng các biến giữ chỗ hoặc tên chưa được định nghĩa (chẳng hạn như `member1`, `feature1`, `x`, `y`).
    * Tuyệt đối không tạo các khung dữ liệu mẫu/giả lập (`toy/sample dataframes`); chỉ thao tác trực tiếp trên khung dữ liệu `df` được cung cấp.
    * Tránh cung cấp bất kỳ văn bản giải thích nào ngoài khối mã lệnh.
    * Sử dụng các lời gọi toán tử hợp lệ với các đối số là Series của dataframe.
* **Tham số ràng buộc toán tử theo họ**:
    * Danh mục toán tử hợp lệ cho họ đặc trưng: `Allowed operators for this family: {family_guide}`.
    * Tên họ đặc trưng hiện tại: `Current family: {family_name}`.

### B.4 Initialization Prompt

* **Chức năng của câu lệnh khởi tạo (`Initialization Prompt`)**: Gieo mầm (seeds) cho mỗi đảo tiến hóa một chương trình đường cơ sở mạnh mẽ (strong baseline program) thuộc họ đặc trưng tương ứng.
* **Cấu trúc mẫu câu lệnh khởi tạo**:
    * Ghép nối tiền tố ngữ cảnh và quy tắc: `{prompt_context}{generation_rules}`.
    * Lệnh yêu cầu sinh mã:
      ```text
      Produce ONE initial '{family_name}' feature program.
      Use at least two source columns, or an axis=1 aggregation across many columns.
      Ground it in the analysis notes; make it a strong, self-contained baseline for this family.
      ```
* **Các ràng buộc kỹ thuật của chương trình khởi tạo**:
    * Chỉ sinh duy nhất MỘT chương trình đặc trưng thuộc họ `{family_name}`.
    * Phải sử dụng tối thiểu hai cột nguồn, hoặc áp dụng một phép tổng hợp dọc theo trục `axis=1` trên nhiều cột dữ liệu.
    * Phải bám sát các ghi chú phân tích từ bước thấu hiểu đặc trưng; đảm bảo chương trình là một đường cơ sở mạnh mẽ, độc lập và tự khép kín (`self-contained baseline`).

### B.5 Mutation Prompt

* **Chức năng của câu lệnh đột biến (`Mutation Prompt`)**: Biến đổi một chương trình cha đơn lẻ thuộc cùng một đảo dưới sự điều hướng của tín hiệu bộ nhớ tăng cường PAM (Prompt-Augmented Memory).
* **Cấu trúc mẫu câu lệnh đột biến**:
    * Ghép nối tiền tố: `{prompt_context}{generation_rules}`.
    * Định danh họ đặc trưng: `Family: {family_name}`.
    * Mã nguồn của chương trình cha: `Parent program: {parent.code}`.
    * Mẫu cấu trúc được khuyến khích (vừa được thưởng gần đây): `Preferred patterns (recently rewarded): {prefer}`.
    * Mẫu cấu trúc cần tránh (bị loại bỏ hoặc dư thừa gần đây): `Avoid patterns (recently rejected/redundant): {avoid}`.
    * Chỉ thị đột biến cấu trúc:
      ```text
      Mutate the parent into a distinct, stronger '{family_name}' feature.
      Change its structure meaningfully: swap an operator, add a stabilizing transform,
      or bring in another column so the output is not merely a rescaled version of the parent.
      ```
* **Cơ chế nạp dữ liệu điều hướng từ bộ nhớ PAM**:
    * Hai trường `{prefer}` và `{avoid}` được trích xuất trực tiếp từ vector bộ nhớ câu lệnh $\rho_i^{(t)}$ của đảo thứ $i$ tại thế hệ $t$.
    * Cung cấp chỉ dẫn định hướng rõ ràng (explicit directional guidance) được rút ra từ lịch sử chấp nhận/từ chối tích lũy của đảo theo Công thức (8) ($Eq.\ 8$).
    * Buộc phép đột biến phải thay đổi cấu trúc cốt lõi (hoán đổi toán tử, thêm biến đổi ổn định hóa, hoặc bổ sung cột nguồn), ngăn chặn việc sinh ra các phiên bản chỉ co giãn tỷ lệ (rescaled version) tầm thường từ chương trình cha.

### B.6 Crossover Prompt

* **Chức năng của câu lệnh lai ghép (`Crossover Prompt`)**: Tổng hợp một chương trình con từ hai chương trình cha thuộc cùng một đảo tiến hóa.
* **Cấu trúc mẫu câu lệnh lai ghép**:
    * Ghép nối tiền tố: `{prompt_context}{generation_rules}`.
    * Định danh họ đặc trưng: `Family: {family_name}`.
    * Mã nguồn chương trình cha A: `Parent A: {p1.code}`.
    * Mã nguồn chương trình cha B: `Parent B: {p2.code}`.
    * Chỉ thị lai ghép cấu trúc:
      ```text
      Combine the most useful structural idea from each parent into one new '{family_name}' feature.
      Do not concatenate them verbatim; synthesize a coherent signal that improves on both and stays low-redundancy.
      ```
* **Yêu cầu đối với chương trình lai ghép**:
    * Kết hợp ý tưởng cấu trúc hữu ích nhất từ mỗi chương trình cha thành duy nhất một đặc trưng mới thuộc họ `{family_name}`.
    * Nghiêm cấm nối ghép mã nguồn nguyên văn (`verbatim concatenation`).
    * Bắt buộc phải tổng hợp thành một tín hiệu mạch lạc, vượt trội hơn cả hai chương trình cha ban đầu và duy trì mức độ dư thừa thấp (`low-redundancy`).

### B.7 Cross-Island Hybrid Synthesis Prompt

* **Chức năng và điều kiện kích hoạt**:
    * Được kích hoạt tự động khi cơ chế phát hiện bão hòa (saturation detection) ghi nhận một đảo tiến hóa bị đình trệ.
    * Thực hiện sinh các chương trình đặc trưng trong không gian hợp thành chung $\mathcal{P}_i \circ \mathcal{P}_j$ giữa đảo mục tiêu $i$ và đảo hiến tặng $j$.
* **Cấu trúc mẫu câu lệnh lai ghép đảo**:
    * Ghép nối tiền tố: `{prompt_context}{generation_rules}`.
    * Định danh hai họ đảo: `TARGET FAMILY: {target.family_name}` và `DONOR FAMILY: {donor.family_name}`.
    * Mã nguồn chương trình cha mục tiêu: `Target parent (stay in this family’s style): {p_t.code}` (yêu cầu duy trì phong cách của họ mục tiêu).
    * Mã nguồn chương trình cha hiến tặng: `Donor parent (borrow ONE idea from a different family): {p_d.code}` (vay mượn MỘT ý tưởng từ họ đặc trưng khác).
    * Chỉ thị tổng hợp lai đảo:
      ```text
      The target island has stagnated. Import a single useful structural idea from the donor -
      an operator, a normalization, or a grouping strategy, and re-express it as a '{target.family_name}' feature.
      Do not copy either parent. The result must be robust, non-trivial, and structurally novel
      relative to the target island’s existing features.
      ```
* **Các nguyên tắc tái biểu đạt cấu trúc**:
    * Nhập khẩu duy nhất một ý tưởng cấu trúc từ chương trình hiến tặng (chẳng hạn: một toán tử biến đổi, một kỹ thuật chuẩn hóa, hoặc một chiến lược gom nhóm).
    * Tái biểu đạt ý tưởng đó theo phong cách và cú pháp của họ đặc trưng mục tiêu (`{target.family_name}`).
    * Tuyệt đối không sao chép nguyên trạng từ bất kỳ chương trình cha nào.
    * Chương trình sinh ra phải đảm bảo tính bền vững (robust), phi tầm thường (non-trivial) và mới lạ về mặt cấu trúc (structurally novel) so với toàn bộ các đặc trưng hiện có của đảo mục tiêu.
