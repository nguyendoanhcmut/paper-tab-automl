## 3. Methodology

- SIGMA bao gồm ba bước xử lý chính:
  - (1) Phân nhóm đặc trưng dựa trên SHAP (SHAP-based Feature Grouping).
  - (2) Sinh đặc trưng nội nhóm và liên nhóm (Intra-Group and Cross-Group Generation).
  - (3) Áp dụng EXIT để kiểm soát kích thước ngữ cảnh (Applying EXIT to control context size).
- Quy trình tổng thể của SIGMA được hình thức hóa chi tiết trong Algorithm 1.

### Algorithm 1: SIGMA Workflow

- **Yêu cầu đầu vào (Require)**:
  - Các tập phân chia dữ liệu: $(\mathcal{D}_{tr}, \mathcal{D}_{va}, \mathcal{D}_{te})$ tương ứng với tập huấn luyện (training split), tập kiểm định (validation split) và tập kiểm thử (test split).
  - Mô hình ngôn ngữ lớn (Large Language Model - LLM): $\mathcal{L}$.
  - Bộ phân loại hạ nguồn (downstream classifier): $\mathcal{C}$.
  - Số bước tối đa (max steps): $T$.
  - Mức độ nhiễu (noise level): $\eta$.
  - Ngưỡng kiên nhẫn (patience): $P$.
- **Khởi tạo trạng thái ban đầu**:
  - Trích xuất ma trận đặc trưng từ các tập dữ liệu: $(X_{tr}, X_{va}, X_{te}) \leftarrow \text{Extract}(D_{tr}, D_{va}, D_{te})$.
  - Đánh giá hiệu năng ban đầu của bộ phân loại: $s^* \leftarrow \text{Eval}(\mathcal{C}, X_{tr}, X_{va})$.
  - Khởi tạo tập hợp các mặt nạ che đặc trưng (mask set): $B \leftarrow \emptyset$.
  - Khởi tạo tập hợp các thao tác bị cấm (failed operations history): $H_{op} \leftarrow \emptyset$.
  - Khởi tạo bộ đếm số bước thất bại liên tiếp: $k_{fail} \leftarrow 0$.
- **Vòng lặp tối ưu hóa đặc trưng** ($\text{for } t \leftarrow 1 \text{ to } T \text{ do}$):
  - Phân nhóm đặc trưng bằng SHAP với mức nhiễu $\eta$:
    $$(G_{top}, G_{use}, G_{weak}) \leftarrow \text{SHAP-based feature grouping}(\mathcal{C}, X_{tr}, \eta)$$
  - Kiểm tra điều kiện giải phóng mặt nạ theo ngưỡng kiên nhẫn:
    - Nếu $k_{fail} \ge P$: giải phóng toàn bộ mặt nạ che và thiết lập lại bộ đếm thất bại:
      $$B \leftarrow \emptyset, \quad k_{fail} \leftarrow 0$$
    - Ngược lại ($k_{fail} < P$): loại bỏ các mặt nạ đã hết hạn khỏi tập $B$ (`Remove expired masks from B`).
  - Lọc không gian đặc trưng khả dụng: loại bỏ toàn bộ các đặc trưng đang bị che trong $B$ khỏi ba nhóm $(G_{top}, G_{use}, G_{weak})$.
  - Xây dựng prompt cho LLM:
    $$P_t \leftarrow \text{BuildPrompt}(G, H_{op}, s^*)$$
    trong đó $G = \{G_{top}, G_{use}, G_{weak}\}$.
  - Sinh ứng viên đặc trưng nội nhóm và liên nhóm:
    $$\Phi_t \leftarrow \text{Intra/cross-group generations with } \mathcal{L}(P_t), (X_{tr}, X_{va}, X_{te})$$
  - Đánh giá các ứng viên đặc trưng ($\phi \in \Phi_t$):
    - Khởi tạo tập ứng viên đạt hiệu quả cải thiện: $A \leftarrow \emptyset$.
    - Đo lường hiệu năng của từng ứng viên trên tập kiểm định:
      $$s_\phi \leftarrow \text{Eval}\left(\mathcal{C}, \text{Concat}[X_{tr}, \phi(X_{tr})], \text{Concat}[X_{va}, \phi(X_{va})]\right)$$
    - Cập nhật ứng viên cải thiện vào tập $A$: nếu $s_\phi > s^*$, gán $A \leftarrow A \cup \{(\phi, s_\phi)\}$.
  - Cập nhật không gian đặc trưng và lịch sử thao tác:
    - Trường hợp có ứng viên thành công ($A \ne \emptyset$):
      - Lựa chọn biến đổi đặc trưng tối ưu: $(\phi^*, s^*) \leftarrow \arg\max_{(\phi, s_\phi) \in A} s_\phi$.
      - Nối đặc trưng mới được chấp nhận vào dữ liệu: $X \leftarrow \text{Concat}[X, \phi^*(X)]$ với mọi $X \in \{X_{tr}, X_{va}, X_{te}\}$.
      - Áp dụng mặt nạ che lên các đặc trưng nguồn đã dùng và đặt lại bộ đếm thất bại:
        $$B \leftarrow B \cup \text{Mask}(\text{ExtractSourceFeatures}(\phi^*)), \quad k_{fail} \leftarrow 0$$
    - Trường hợp không có ứng viên thành công ($A = \emptyset$):
      - Bổ sung các thao tác thất bại vào tập cấm: $H_{op} \leftarrow H_{op} \cup \text{ExtractOperations}(\Phi_t)$.
      - Tăng bộ đếm thất bại liên tiếp: $k_{fail} \leftarrow k_{fail} + 1$.
- **Kết quả đầu ra**:
  - Trả về tập các đặc trưng đã được tăng cường: $(X_{tr}, X_{va}, X_{te})$.

### 3.1. Feature Groups

- Các đặc trưng ban đầu được chia thành các nhóm dựa trên giá trị SHAP (SHAP values) tương ứng của chúng:
  - Thay vì áp dụng tỷ lệ chia cố định (ví dụ $33\%$ số đặc trưng cho mỗi nhóm), phương pháp đưa vào một ngưỡng động (threshold) thông qua việc bổ sung một đặc trưng nhiễu (noise feature).
  - Một cột nhiễu Gaussian (Gaussian noise column) được thêm vào tập đặc trưng ban đầu trước khi tính toán giá trị SHAP cho toàn bộ các đặc trưng cùng cột nhiễu.
  - Chuẩn hóa min-max (min-max normalization) được áp dụng tại giai đoạn này để đưa các đặc trưng về cùng thang đo, giúp chúng có thể so sánh trực tiếp với đặc trưng nhiễu.
- Giá trị SHAP của cột nhiễu đóng vai trò là ngưỡng phân chia đặc trưng thành ba nhóm riêng biệt:
  - **Nhóm top ($G_{top}$)**:
    - Bao gồm các đặc trưng có giá trị SHAP xếp hạng trong top $10\%$ cao nhất (yêu cầu tối thiểu ít nhất 2 đặc trưng).
    - Đây là những đặc trưng quan trọng nhất đối với kết quả dự đoán của mô hình.
  - **Nhóm yếu (weak group - $G_{weak}$)**:
    - Bao gồm toàn bộ các đặc trưng có giá trị SHAP thấp hơn ngưỡng của đặc trưng nhiễu.
  - **Nhóm hữu ích (useful group - $G_{use}$)**:
    - Bao gồm các đặc trưng còn lại (nằm giữa ngưỡng của đặc trưng nhiễu và top $10\%$).
- Động lực và lợi ích của việc phân nhóm dựa trên ngưỡng nhiễu Gaussian:
  - Giúp điều chỉnh sự chú ý (attention) của LLM đối với không gian đặc trưng hiện tại theo đặc thù của từng tập dữ liệu:
    - Nếu sử dụng tỷ lệ phân chia cố định, LLM sẽ phân bổ mức độ chú ý cố định cho mỗi nhóm trên tất cả các tập dữ liệu.
    - Tuy nhiên, mỗi tập dữ liệu đều mang các đặc tính nội tại riêng biệt; ví dụ trong một số trường hợp, phần lớn các đặc trưng có độ quan trọng thấp hơn nhiễu, trong khi ở các trường hợp khác, toàn bộ các đặc trưng đều quan trọng hơn nhiễu.
    - Nhóm nào chứa càng nhiều đặc trưng thì LLM sẽ càng dành nhiều sự chú ý cho nhóm đó.
  - Việc đưa đặc trưng nhiễu vào định hướng LLM sinh các đặc trưng mới phù hợp với các đặc tính nội tại (intrinsic characteristics) của tập dữ liệu đích.
  - Chiến lược phân nhóm là điều kiện tiên quyết và mang lại lợi ích trực tiếp cho chiến lược EXIT.

### 3.2. Intra-Group and Cross-Group Generation

- Prompt của LLM được xây dựng dựa trên các nhóm đặc trưng đã phân loại nhằm sinh ra các đặc trưng mới:
  - Cấu trúc prompt chi tiết tuân theo mẫu được cung cấp tại Appendix A.
  - Thay vì chỉ sinh duy nhất 1 đặc trưng ở mỗi bước, hệ thống yêu cầu LLM đồng thời tạo ra:
    - 1 đặc trưng nội nhóm (intra-group feature).
    - 1 đặc trưng liên nhóm (cross-group feature).
- Bản chất và mục tiêu của việc sinh đặc trưng nội nhóm (intra-group generation):
  - Tập trung vào phép biến đổi đặc trưng sâu (deep feature transformation) hoặc tương tác đa đặc trưng (multi-feature interaction) nhằm phát hiện các mẫu tiềm ẩn (hidden patterns) giữa các đặc trưng trong cùng một nhóm.
  - Mục đích chính là củng cố và cải thiện các tín hiệu vốn đã có sức ảnh hưởng mạnh (already influential signals).
- Bản chất và mục tiêu của việc sinh đặc trưng liên nhóm (cross-group generation):
  - Tập trung vào việc xây dựng tính hiệp đồng (synergy building) bằng cách bắc cầu liên kết giữa các đặc trưng có tầm quan trọng cao với các tín hiệu yếu hơn.
  - Mục đích chính là cải thiện và nâng cao chất lượng của các tín hiệu yếu (weak signals).
- Cơ chế đánh giá và chấp nhận đặc trưng:
  - Cả hai đặc trưng sinh ra đều được đưa vào đánh giá độc lập bởi mô hình phân loại hạ nguồn.
  - Chỉ đặc trưng mang lại sự cải thiện tích cực lớn nhất (most positive improvement) và vượt qua ngưỡng điểm hiện tại ($s_\phi > s^*$) mới được chấp nhận bổ sung vào tập dữ liệu.

### 3.3. EXposed-feature Implicit Trajectory (EXIT)

- Nguyên lý và động lực đề xuất EXIT (EXposed-feature Implicit Trajectory):
  - Khi lược bỏ quỹ đạo tìm kiếm tường minh (explicit trajectory) trong prompt, LLM có xu hướng rất cao tạo ra các đặc trưng bị trùng lặp (duplicated features).
  - EXIT được xây dựng dựa trên nguyên lý: thông tin được truyền tải không chỉ qua sự hiện diện của các tín hiệu tường minh, mà còn thông qua sự lược bỏ có tính chiến lược (strategic omission) của chúng.
- Cơ chế che giấu đặc trưng lộ diện (Masking exposed features):
  - Tại mỗi bước, toàn bộ các đặc trưng được chọn $f_{sel}$ dùng để sinh đặc trưng mới đều được theo dõi và che giấu (masked) khỏi prompt trong một số bước kế tiếp.
  - Khoảng thời gian che giấu (masking intervals) được phân tầng dựa trên độ quan trọng và chức năng của từng nhóm đặc trưng:
    - Nhóm `top`: do mang nhiều thông tin hơn và có khả năng hưởng lợi cao hơn từ các tương tác tiếp theo, nhóm này được gán khoảng thời gian che giấu ngắn nhất là 20 bước ($20$ steps).
    - Nhóm `useful`: có khoảng thời gian che giấu là 21 bước ($21$ steps).
    - Nhóm `weak`: có khoảng thời gian che giấu dài nhất là 22 bước ($22$ steps).
- Cơ chế đặt lại và giải phóng đặc trưng khi bế tắc (Reset mechanism):
  - Để ngăn LLM bị mắc kẹt trong các cực trị địa phương (local optima), EXIT kích hoạt thiết lập lại không gian đặc trưng bị che khi không có bất kỳ đặc trưng nào được chấp nhận trong $P = 5$ bước liên tiếp (ngưỡng kiên nhẫn $P = 5$).
  - Khi cơ chế này được kích hoạt, toàn bộ các đặc trưng đang bị đóng băng (frozen features) sẽ được khôi phục trạng thái khả dụng hoàn toàn ($B \leftarrow \emptyset$, $k_{fail} \leftarrow 0$).
- Cơ chế theo dõi và kiểm soát thao tác biến đổi (Operation tracking & restriction):
  - Hệ thống ghi nhận các thao tác biến đổi đã thực hiện và tạm thời ngăn LLM sử dụng 2 thao tác có tần suất xuất hiện cao nhất (two most frequent operations) trong prompt, nhằm phá vỡ thói quen liên tục chọn cùng các thao tác cố định của LLM trên một tập dữ liệu.
  - Cơ chế cấm chỉ áp dụng có chọn lọc: chỉ các thao tác gắn liền với các lượt sinh thất bại (failed generations) mới bị theo dõi và tạm thời cấm đưa vào prompt.
  - Thao tác hiệu quả được duy trì: nếu một thao tác liên tục cải thiện hiệu năng mô hình, thao tác đó được xác định là phù hợp với tập dữ liệu và được giữ lại để tiếp tục sử dụng (rewarded accordingly).
- Bản chất tối ưu hóa của quỹ đạo ngầm định:
  - Thông tin quỹ đạo tìm kiếm được đóng gói ngầm định (implicitly encapsulated) bên trong tập hợp các đặc trưng được để lộ (exposed features), thay vì phải duy trì một bản ghi lịch sử tối ưu hóa tường minh tiêu tốn nhiều token ngữ cảnh (explicit, token-heavy record).
