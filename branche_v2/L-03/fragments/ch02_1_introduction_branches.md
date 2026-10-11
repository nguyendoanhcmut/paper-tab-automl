## 1 Introduction

* Kỹ thuật đặc trưng (Feature Engineering - FE) là quá trình chuyển đổi các biến thô thành các biểu diễn có khả năng dự đoán nhằm làm lộ ra cấu trúc ẩn của một bài toán học máy [Dong and Liu, 2018]:
    * FE vẫn là một trong những giai đoạn có tầm ảnh hưởng lớn nhất nhưng lại ít mang tính nguyên lý nhất (least principled) trong quy trình học máy dạng bảng (tabular machine learning pipeline).
    * Trong các thiết lập dữ liệu dạng bảng, nơi dữ liệu mang tính không đồng nhất (heterogeneous), giàu ngữ nghĩa (semantically rich) và thường chứa đựng cấu trúc đặc thù theo miền (domain-specific structure), chất lượng của các đặc trưng được thiết kế thường quyết định hiệu năng của mô hình nhiều hơn so với các lựa chọn về mặt kiến trúc hay tinh chỉnh siêu tham số (hyperparameter tuning) [Zhang et al., 2023a, Hollmann et al., 2023a].
    * Xây dựng các đặc trưng có giá trị cao đòi hỏi nhiều hơn là sự liệt kê về mặt cú pháp (syntactic enumeration):
        * Ví dụ: một tỷ số rủi ro có ý nghĩa lâm sàng (clinically meaningful risk ratio), một chỉ báo biến động tài chính (financial volatility indicator), hoặc một đặc trưng tần suất hành vi (behavioral frequency feature) đòi hỏi sự thấu hiểu về ý nghĩa của các biến, cách chúng tương tác nhân quả (causally interact), và những phép biến đổi nào được chấp nhận về mặt ngữ nghĩa (semantically admissible).
        * Tri thức ngữ nghĩa này nằm ngoài phạm vi những gì các thư viện toán tử cố định (fixed operator libraries) có thể mã hóa.
* Quá trình chuyển dịch mô hình từ AutoFE cổ điển dựa trên ngữ pháp sang tổng hợp chương trình bằng mô hình ngôn ngữ lớn (LLM):
    * Các hệ thống kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE) ban đầu định dạng bài toán thành quá trình tìm kiếm trên một ngữ pháp biến đổi được định nghĩa trước (predefined transformation grammar) [Olson and Moore, 2016, Horn et al., 2019, Zhang et al., 2023a].
    * Dù khả thi về mặt tính toán (tractable), công thức hóa cổ điển bị giới hạn căn bản bởi năng lực biểu đạt của thư viện toán tử: các đặc trưng đòi hỏi suy luận ngữ nghĩa liên biến (cross-variable semantic reasoning) nằm ngoài không gian có thể tiếp cận được theo thiết kế (outside the reachable space by construction).
    * Sự xuất hiện của các mô hình ngôn ngữ lớn (Large Language Models - LLM) mang lại một năng lực khác biệt về chất:
        * Thông qua tiền huấn luyện trên các kho ngữ liệu khổng lồ về văn bản khoa học, toán học và chuyên ngành, LLM có thể giả định các phép biến đổi có ý nghĩa từ tên cột (column names), mô tả tác vụ (task descriptions) và tri thức nền tảng (background knowledge).
        * Năng lực này dịch chuyển mô hình một cách hiệu quả từ việc lựa chọn toán tử cố định sang tổng hợp chương trình đặc trưng mở (open-ended feature program synthesis) [Hollmann et al., 2023a, Han et al., 2024].
    * Khiếm khuyết cấu trúc nghiêm trọng của các phương pháp AutoFE dựa trên LLM hiện tại: các đề xuất được tạo ra từ câu nhắc tĩnh (static prompts) không có bộ nhớ về các lần đánh giá trước, dẫn đến việc lặp lại đề xuất, không thích ứng được với các mẫu hình đặc thù của bộ dữ liệu, và không có cơ chế tổng hợp các đặc trưng đòi hỏi đồng thời toán tử từ nhiều họ biến đổi (multiple transformation families).
* Giới hạn của việc kết hợp LLM với tìm kiếm tiến hóa và phương thức thất bại khóa chặt liên họ (Cross-family Lock-in):
    * Các nỗ lực gần đây kết hợp LLM với tìm kiếm tiến hóa (evolutionary search) giảm thiểu một phần hạn chế trên bằng cách duy trì một bộ đệm kinh nghiệm (experience buffer) gồm các chương trình đạt điểm số cao làm mẫu minh họa trong ngữ cảnh (in-context demonstrations) [Abhyankar et al., 2025, Gong et al., 2025].
    * Tuy nhiên, các phương pháp này vẫn vận hành trên một quần thể đơn nhất không phân hóa (single undifferentiated population).
    * Không gian chương trình đặc trưng không hề đồng nhất mà cấu thành từ các họ biến đổi (transformation families) khác biệt về chất:
        * Tương tác số học (arithmetic interactions),
        * Tập hợp thống kê (statistical aggregates),
        * Động học thời gian (temporal dynamics),
        * Mã hóa quan hệ (relational encodings),
        * Ánh xạ phi tuyến đơn biến (nonlinear univariate maps).
        * Mỗi họ mã hóa một thiên kiến quy nạp (inductive bias) khác nhau về nguồn gốc phát sinh tín hiệu dự đoán.
    * Tìm kiếm trên quần thể đơn nhất bỏ qua cấu trúc này:
        * Khi một vài chương trình thành công từ một họ thống trị làm bão hòa bộ đệm kinh nghiệm, các đề xuất tiếp theo của LLM dần dần bị giam cầm trong chính họ đó.
        * Các họ trực giao (orthogonal families) bị khám phá dưới mức tiềm năng.
        * Các cấu thành liên họ (cross-family compositions) — vốn thường mang lại những đặc trưng có tính biểu đạt cao nhất và bổ trợ tốt nhất — trở nên bất khả tiếp cận về mặt cấu trúc (structurally unreachable).
    * Sự khóa chặt liên họ (cross-family lock-in) là phương thức thất bại trung tâm (central failure mode) của các phương pháp LLM-tiến hóa hiện hành, và chưa có công trình nào cung cấp cơ chế có nguyên tắc để phát hiện hoặc hiệu chỉnh hiện tượng này.
* Ba hạn chế liên đới cố hữu trong y văn hiện tại (Three Interrelated Limitations):
    * $(\text{L1})$ Động lực tìm kiếm đồng nhất (Homogeneous search dynamics): Tiến hóa trên quần thể đơn nhất suy thoái vào một tập con hạn hẹp các loại biến đổi, bị thiên lệch về các mô-típ đạt hiệu năng cao ban đầu và mù quáng trước cấu trúc đa phương thức (multi-modal structure) của không gian chương trình.
    * $(\text{L2})$ Truy vấn LLM không trạng thái (Stateless LLM querying): Quá trình sinh đặc trưng thiếu bộ nhớ dai dẳng (persistent memory) về các thăm dò trước đó, ngăn cản sự thích ứng tích lũy (cumulative adaptation) đối với các mẫu hình đặc thù của bộ dữ liệu.
    * $(\text{L3})$ Cấu trúc chuyển giao cứng nhắc (Rigid transfer structure): Khi sử dụng nhiều quần thể, cơ chế di cư (migration) mang tính định kỳ hoặc ngẫu nhiên, không nhận biết được thời điểm chuyển giao mang lại lợi ích và họ nguồn nào bổ trợ tốt nhất cho một đảo đích đang rơi vào trạng thái trì trệ (stagnating target island).
* Khung làm việc TOPOFE mô hình hóa kỹ thuật đặc trưng thành tìm kiếm chương trình tiến hóa đa đảo cấu trúc đồ thị:
    * TOPOFE dựa trên ba nguyên lý thiết kế nền tảng:
        * Phân tách thiên kiến quy nạp (Inductive bias decomposition): Không gian chương trình được phân vùng thành các họ biến đổi khác nhau, mỗi họ được gán cho một đảo chuyên dụng (dedicated island) nhằm tiến hóa các chương trình chuyên biệt hóa dưới các tiên nghiệm riêng theo họ, bảo toàn tính đa dạng trên các loại biến đổi theo thiết kế.
        * Học topo thích ứng (Adaptive topology learning): Thay vì sử dụng lịch trình di cư cố định hoặc suy nghiệm (heuristic), TOPOFE duy trì một đồ thị có hướng có trọng số trên các đảo, trong đó trọng số cạnh được cập nhật trực tuyến từ mức cải thiện chuyển giao liên họ quan sát được từ thực nghiệm, học một mô hình định hướng dữ liệu về tính bổ trợ giữa các họ.
        * Chuyển giao ngữ nghĩa qua tổng hợp LLM (Semantic transfer via LLM synthesis): Chuyển giao tri thức liên đảo không được thực hiện bằng cách sao chép chương trình, mà thông qua tổng hợp lai (hybrid synthesis) do LLM điều phối, trong đó các chương trình từ đảo nguồn và đảo đích được cùng trình bày làm ngữ cảnh, và LLM sinh ra một chương trình mới về mặt cấu thành kế thừa các phần tử cấu trúc từ cả hai họ.
    * Tiêu chí bão hòa (Saturation criterion):
        * Chuyển giao được kích hoạt bởi tiêu chí bão hòa — một ước lượng cửa sổ trượt (sliding-window estimate) về mức cải thiện biên (marginal improvement) của từng đảo nhằm phát hiện khi nào tìm kiếm cục bộ đã thực sự cạn kiệt vùng hữu ích.
        * Tiêu chí này tách rời việc chuyển giao khỏi số lượng thế hệ tính theo thời gian thực (wall-clock generation count) và đảm bảo ngân sách đánh giá được hướng vào thăm dò liên họ chính xác vào thời điểm có giá trị cao nhất.
    * Bộ nhớ thích ứng câu nhắc (Prompt Adaptation Memory - PAM):
        * Duy trì lịch sử chấp nhận/từ chối trên từng đảo và một bản tóm tắt ngắn gọn bằng ngôn ngữ tự nhiên về các mẫu biến đổi được ưu tiên và cần tránh, được đưa vào mỗi lệnh gọi LLM.
        * Thành phần này cho phép thích ứng tích lũy, đặc thù theo bộ dữ liệu trong toàn bộ quá trình tìm kiếm mà không cần bất kỳ sự cập nhật tham số nào (without any parameter update).
* Bốn đóng góp chính của nghiên cứu:
    * (i) Công thức hóa nhận biết cấu trúc topo (Topology-aware formulation): Định dạng AutoFE thành bài toán tìm kiếm chương trình đa đảo cấu trúc đồ thị, phân vùng không gian đặc trưng thành các đảo chuyên biệt hóa theo từng họ và thay thế cơ chế di cư suy nghiệm bằng một đồ thị topo có hướng học được, có trọng số cạnh mã hóa độ hữu dụng chuyển giao liên họ quan sát được trên thực nghiệm và cập nhật trực tuyến thông qua quy tắc kiểu bandit (bandit-style rule).
    * (ii) Chuyển giao thích ứng kích hoạt bởi độ bão hòa (Saturation-triggered adaptive transfer): Giới thiệu tiêu chí bão hòa dựa trên độ hữu dụng để kích hoạt chuyển giao liên đảo khi tìm kiếm cục bộ cạn kiệt; kết hợp thành phần Prompt Adaptation Memory tích lũy các mẫu chương trình được chấp nhận và từ chối trên từng đảo, cho phép thích ứng tích lũy theo bộ dữ liệu trong suốt quá trình tìm kiếm mà không cần cập nhật tham số.
    * (iii) Khung đánh giá có nguyên tắc (Principled evaluation framework): Giới thiệu ba độ đo chuyên dụng:
        * Hệ số tương quan đầu ra từng cặp trung bình (Mean Pairwise Output Correlation - $\text{MPOC}$) và Hạng hiệu dụng (Effective Rank - $\text{EffRank}$): cùng mô tả mức độ dư thừa đặc trưng và độ bao phủ không gian con (subspace coverage).
        * Điểm chuyên biệt hóa đồ thị topo (Topology Graph Specialisation Score - $\text{TGSS}$): định lượng mức độ đồ thị topo tiếp thu tri thức chuyển giao liên họ đặc thù theo tác vụ trong quá trình tìm kiếm.
    * (iv) Xác thực thực nghiệm toàn diện (Empirical validation): Trên $29$ bộ dữ liệu, chứng minh TOPOFE vượt trội nhất quán so với phần lớn các baseline AutoFE cổ điển và dựa trên LLM, tạo ra các tập đặc trưng có độ dư thừa thấp hơn và độ bao phủ cao hơn, đồng thời hiệu năng duy trì tính ổn định qua nhiều mô hình dự đoán hạ nguồn và các mô hình nền LLM có năng lực khác nhau.
