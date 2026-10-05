## 1 Introduction

- **Bản chất và vị trí trọng yếu của Feature Engineering (FE - Kỹ thuật đặc trưng) trong pipeline học máy dạng bảng (tabular machine learning)**:
  - Feature engineering là quá trình biến đổi các biến thô (raw variables) thành các biểu diễn có khả năng dự đoán (predictive representations) nhằm bộc lộ cấu trúc tiềm ẩn (latent structure) của bài toán học máy [Dong and Liu, 2018].
  - FE là một trong những giai đoạn mang tính quyết định nhất nhưng lại ít có tính nguyên lý nhất (least principled) trong toàn bộ quy trình tabular ML pipeline.
  - Trong môi trường dữ liệu dạng bảng (tabular settings), nơi dữ liệu mang tính dị thể (heterogeneous), giàu ngữ nghĩa (semantically rich) và thường chứa đựng cấu trúc đặc thù theo miền (domain-specific structure), chất lượng của các feature được tạo ra thường quyết định hiệu năng mô hình nhiều hơn cả việc lựa chọn kiến trúc (architectural choices) hay tinh chỉnh siêu tham số (hyperparameter tuning) [Zhang et al., 2023a, Hollmann et al., 2023a].

- **Nhu cầu về tri thức ngữ nghĩa và giới hạn căn bản của các hệ thống AutoFE truyền thống (early AutoFE systems)**:
  - Việc xây dựng các đặc trưng có giá trị cao đòi hỏi nhiều hơn là việc liệt kê cú pháp đơn thuần (syntactic enumeration): các ví dụ điển hình như tỷ lệ rủi ro có ý nghĩa lâm sàng (clinically meaningful risk ratio), chỉ số biến động tài chính (financial volatility indicator), hoặc đặc trưng tần suất hành vi (behavioral frequency feature) đều đòi hỏi sự thấu hiểu sâu sắc về ý nghĩa biến số, cách các biến tương tác nhân quả (causally interact), và các phép biến đổi nào là hợp lệ về mặt ngữ nghĩa (semantically admissible).
  - Tri thức ngữ nghĩa (semantic knowledge) này nằm ngoài khả năng mã hóa của các thư viện toán tử cố định (fixed operator libraries).
  - Các hệ thống tạo đặc trưng tự động ban đầu (early automated feature engineering - AutoFE) đóng khung bài toán thành việc tìm kiếm trên một ngữ pháp biến đổi tiền định (predefined transformation grammar) [Olson and Moore, 2016, Horn et al., 2019, Zhang et al., 2023a].
  - Dù khả thi về mặt tính toán (tractable), công thức này bị giới hạn căn bản bởi năng lực biểu đạt của thư viện toán tử: các đặc trưng đòi hỏi suy luận ngữ nghĩa liên biến (cross-variable semantic reasoning) nằm ngoài không gian có thể tiếp cận được (reachable space) ngay từ khâu thiết kế.

- **Bước chuyển dịch mô thức từ LLM và khiếm khuyết cấu trúc của các phương pháp AutoFE dựa trên LLM hiện có**:
  - Sự xuất hiện của các mô hình ngôn ngữ lớn (LLMs - Large Language Models), nhờ được tiền huấn luyện trên các kho ngữ liệu khổng lồ (massive corpora) về văn bản khoa học, toán học và chuyên ngành, mang lại năng lực suy đoán (hypothesize) các phép biến đổi có ý nghĩa từ tên cột (column names), mô tả bài toán (task descriptions) và tri thức nền tảng (background knowledge).
  - Năng lực này chuyển dịch căn bản mô thức nghiên cứu từ lựa chọn toán tử cố định (fixed operator selection) sang tổng hợp chương trình đặc trưng kết thúc mở (open-ended feature program synthesis) [Hollmann et al., 2023a, Han et al., 2024].
  - Tuy nhiên, các phương pháp dựa trên LLM hiện tại mắc phải một khiếm khuyết cấu trúc nghiêm trọng: các đề xuất (proposals) được sinh ra từ các prompt tĩnh (static prompts) và không lưu giữ bộ nhớ về các đánh giá trước đó (no memory of prior evaluations), dẫn đến việc sinh lặp lại đề xuất (repeated proposals), không thích ứng được với các mẫu hình đặc thù của tập dữ liệu (dataset-specific patterns), và thiếu cơ chế tổng hợp các đặc trưng đòi hỏi toán tử từ nhiều họ biến đổi đồng thời (multiple transformation families simultaneously).

- **Hạn chế của tìm kiếm tiến hóa kết hợp LLM và hiện tượng khóa chéo họ (Cross-Family Lock-in)**:
  - Các nỗ lực gần đây kết hợp LLM với tìm kiếm tiến hóa (evolutionary search) nhằm giảm bớt hạn chế trên bằng cách duy trì vùng đệm kinh nghiệm (experience buffer) chứa các chương trình đạt điểm cao làm ví dụ mẫu trong ngữ cảnh (in-context demonstrations) [Abhyankar et al., 2025, Gong et al., 2025].
  - Tuy vậy, các phương pháp này vẫn vận hành trên một quần thể đơn nhất không phân hóa (single undifferentiated population).
  - Không gian chương trình đặc trưng không hề đồng nhất (not homogeneous), mà cấu thành từ các họ biến đổi (transformation families) khác biệt về chất:
    - Tương tác số học (arithmetic interactions)
    - Tổng hợp thống kê (statistical aggregates)
    - Động học thời gian (temporal dynamics)
    - Mã hóa quan hệ (relational encodings)
    - Ánh xạ phi tuyến đơn biến (nonlinear univariate maps)
    - Mỗi họ mã hóa một thiên kiến quy nạp (inductive bias) khác nhau về cách thức tín hiệu dự đoán phát sinh.
  - Tìm kiếm quần thể đơn nhất bỏ qua cấu trúc này: khi một vài chương trình thành công từ một họ chiếm ưu thế làm bão hòa experience buffer, các đề xuất tiếp theo của LLM dần dần bị giam cầm (progressively confined) vào họ đó.
  - Hậu quả là các họ trực giao (orthogonal families) không được khám phá đầy đủ, và các kết hợp chéo họ (cross-family compositions) – vốn thường mang lại các đặc trưng có tính biểu đạt và bổ trợ mạnh nhất – trở nên không thể tiếp cận được về mặt cấu trúc (structurally unreachable).
  - Hiện tượng khóa chéo họ (cross-family lock-in) là phương thức thất bại trung tâm (central failure mode) của các phương pháp LLM-tiến hóa hiện hành, và chưa có nghiên cứu nào cung cấp cơ chế có nguyên lý để phát hiện hoặc khắc phục lỗi này.

- **Ba giới hạn dai dẳng mang tính liên đới trong y văn hiện tại (L1 - L3)**:
  - **(L1) Động học tìm kiếm đồng nhất (Homogeneous search dynamics)**: Tiến hóa quần thể đơn nhất bị suy thoái/thu hẹp vào một tập con hẹp các kiểu biến đổi, thiên lệch về các motif đạt hiệu năng cao ban đầu và mù quáng trước cấu trúc đa phương thức (multi-modal structure) của không gian chương trình.
  - **(L2) Truy vấn LLM không trạng thái (Stateless LLM querying)**: Quá trình sinh đặc trưng thiếu bộ nhớ bền vững (persistent memory) về lịch sử khám phá trước đó, cản trở sự thích ứng tích lũy (cumulative adaptation) theo các mẫu hình của từng tập dữ liệu cụ thể.
  - **(L3) Cấu trúc chuyển giao cứng nhắc (Rigid transfer structure)**: Khi sử dụng nhiều quần thể (multiple populations/islands), cơ chế di cư (migration) diễn ra theo chu kỳ cố định hoặc ngẫu nhiên, hoàn toàn không nhận biết được thời điểm chuyển giao có lợi và họ nguồn nào bổ trợ tốt nhất cho một đảo đích đang bị đình trệ (stagnating target island).

- **Khung phương pháp TOPOFE và ba nguyên lý trụ cột**:
  - TOPOFE mô hình hóa AutoFE thành bài toán tìm kiếm chương trình lấy cảm hứng từ tiến hóa đa đảo có cấu trúc đồ thị (graph-structured multi-island evolution).
  - **Nguyên lý 1 - Phân rã thiên kiến quy nạp (Inductive bias decomposition)**: Không gian chương trình được phân hoạch thành các họ biến đổi (transformation families) khác nhau; mỗi họ được gán cho một đảo chuyên biệt (dedicated island) nhằm tiến hóa các chương trình chuyên biệt dưới các prior của họ đó, bảo toàn tính đa dạng giữa các kiểu biến đổi ngay từ thiết kế.
  - **Nguyên lý 2 - Học tô-pô thích ứng (Adaptive topology learning)**: Thay vì sử dụng lịch trình di cư cố định hoặc heuristic, TOPOFE duy trì một đồ thị có hướng có trọng số (directed weighted graph) trên các đảo, trong đó trọng số cạnh được cập nhật trực tuyến (online) từ mức cải thiện chuyển giao chéo họ quan sát được thực tế, qua đó học một mô hình định hướng dữ liệu (data-driven model) về tính bổ trợ liên họ (inter-family complementarity).
  - **Nguyên lý 3 - Chuyển giao ngữ nghĩa qua tổng hợp LLM (Semantic transfer via LLM synthesis)**: Việc chuyển giao tri thức liên đảo không thực hiện bằng việc sao chép chương trình nguyên bản (copying programs), mà thông qua tổng hợp lai do LLM điều phối (LLM-mediated hybrid synthesis), trong đó các chương trình từ đảo nguồn và đảo đích được cùng đưa vào ngữ cảnh để LLM sinh ra một chương trình mới về mặt cấu tạo (compositionally novel program) kế thừa các yếu tố cấu trúc từ cả hai họ.

- **Cơ chế điều phối tìm kiếm và bộ nhớ thích ứng của TOPOFE**:
  - **Tiêu chí bão hòa (Saturation criterion)**: Chuyển giao chéo họ được kích hoạt bởi tiêu chí bão hòa dựa trên ước lượng cửa sổ trượt (sliding-window estimate) về mức cải thiện biên (marginal improvement) của từng đảo nhằm phát hiện chính xác thời điểm tìm kiếm cục bộ đã thực sự cạn kiệt vùng hiệu quả.
  - Cơ chế này tách biệt việc chuyển giao khỏi số lượt sinh theo thời gian (wall-clock generation count), đảm bảo ngân sách đánh giá (evaluation budget) được chuyển hướng sang khám phá chéo họ đúng vào thời điểm có giá trị nhất.
  - **Bộ nhớ thích ứng Prompt (Prompt Adaptation Memory)**: Duy trì lịch sử chấp nhận/bác bỏ (accept/reject history) cho từng đảo kèm theo bản tóm tắt ngắn gọn bằng ngôn ngữ tự nhiên về các mẫu hình biến đổi ưa chuộng và cần tránh, được đưa vào mỗi lần gọi LLM.
  - Cơ chế bộ nhớ này cho phép thích ứng tích lũy theo từng tập dữ liệu cụ thể trong suốt quá trình tìm kiếm mà không yêu cầu cập nhật tham số mô hình (without parameter update).

- **Tóm tắt bốn đóng góp chính của nghiên cứu (Key Contributions)**:
  - **(i) Định thức nhận biết tô-pô (Topology-aware formulation)**: Mô hình hóa AutoFE dưới dạng tìm kiếm chương trình đa đảo cấu trúc đồ thị, phân hoạch không gian đặc trưng thành các đảo chuyên môn hóa theo họ và thay thế cơ chế di cư heuristic bằng đồ thị tô-pô có hướng được học với trọng số cạnh mã hóa độ hữu dụng chuyển giao chéo họ (cross-family transfer utility) quan sát được thực nghiệm, cập nhật trực tuyến qua quy tắc kiểu bandit (bandit-style rule).
  - **(ii) Chuyển giao thích ứng kích hoạt theo độ bão hòa (Saturation-triggered adaptive transfer)**: Đề xuất tiêu chí bão hòa dựa trên độ hữu dụng để kích hoạt chuyển giao liên đảo khi tìm kiếm cục bộ cạn kiệt, kết hợp cùng Prompt Adaptation Memory tích lũy mẫu chương trình được chấp nhận và loại bỏ nhằm thích ứng tích lũy đặc thù theo tập dữ liệu mà không cần cập nhật tham số.
  - **(iii) Khung đánh giá có nguyên lý (Principled evaluation framework)**: Giới thiệu $3$ thước đo được thiết kế chuyên biệt:
    - Tương quan đầu ra theo cặp trung bình (Mean Pairwise Output Correlation) và Hạng hiệu dụng (Effective Rank): Cùng nhau định tính và định lượng độ dư thừa đặc trưng (feature redundancy) và độ bao phủ không gian con biểu diễn (subspace coverage).
    - Điểm chuyên biệt hóa đồ thị tô-pô (Topology Graph Specialisation Score): Định lượng mức độ mà đồ thị tô-pô tiếp thu tri thức chuyển giao chéo họ đặc thù cho từng tác vụ trong suốt quá trình tìm kiếm.
  - **(iv) Kiểm chứng thực nghiệm toàn diện (Empirical validation)**: Trên $29$ tập dữ liệu, chứng minh TOPOFE vượt trội nhất quán so với đa số các baseline AutoFE cổ điển và dựa trên LLM, sản sinh các tập đặc trưng có độ dư thừa thấp hơn và độ bao phủ cao hơn, đồng thời duy trì hiệu năng ổn định trên nhiều mô hình dự đoán hạ nguồn (downstream predictors) và các LLM backbone có năng lực khác nhau.
