## 1 Introduction

* **Bản chất và tầm quan trọng của dữ liệu dạng bảng (tabular data) trong các ứng dụng thực tế:**
  * Dữ liệu dạng bảng (tabular data) là định dạng dữ liệu có tính cấu trúc cao (highly structured data format), tổ chức thông tin theo hàng và cột (rows and columns) (Altman and Krzywinski, 2017):
    * Mỗi hàng biểu diễn một mẫu hoặc một thực thể độc lập (independent sample or instance).
    * Mỗi cột tương ứng với một đặc trưng hoặc thuộc tính cụ thể (specific feature or attribute) (Sahakyan et al., 2021).
  * Ứng dụng rộng rãi trong nhiều tác vụ quan trọng ở thế giới thực:
    * Lĩnh vực tài chính: hỗ trợ chấm điểm tín dụng (credit scoring) (West, 2000) và dự đoán thị trường chứng khoán (stock market prediction) (Zhu et al., 2021).
    * Lĩnh vực y tế: hỗ trợ chẩn đoán bệnh tật (disease diagnosis) (Yıldız and Kalayci, 2024) và phát triển dược phẩm (drug development) (Meijerink et al., 2020).
  * Hạn chế cố hữu của dữ liệu dạng bảng:
    * Thường bị thiếu hụt tính thông tin của đặc trưng (insufficient feature informativeness).
    * Chứa các tương tác bậc cao tiềm ẩn (implicit high-order interactions).
    * Những khoảng cách cố hữu này cản trở các mô hình hiểu hiệu quả cấu trúc dữ liệu cơ bản, dẫn đến hiệu năng dự đoán dưới mức tối ưu (suboptimal predictive performance) (Sayed et al., 2025; Cheng et al., 2025b; Gorishniy et al., 2021).

* **Vai trò của kỹ nghệ đặc trưng (feature engineering) và sự ra đời của AutoFE:**
  * Trước khi đưa vào dự đoán, kỹ nghệ đặc trưng (feature engineering) thường được áp dụng nhằm nâng cao mối quan hệ giữa các đặc trưng đầu vào và biến mục tiêu (target) thông qua các thao tác như sinh đặc trưng (feature generation) và chọn lọc đặc trưng (feature selection) (Ravishankar and Battineni, 2025).
  * Dữ liệu dạng bảng sau xử lý được đưa vào các mô hình xuôi dòng (downstream models) để tối ưu hóa hiệu năng dự đoán.
  * Trước đây, kỹ nghệ đặc trưng phụ thuộc chủ yếu vào việc xây dựng thủ công (manual construction) các đặc trưng chất lượng cao:
    * Quá trình này đòi hỏi nỗ lực lặp lại sâu rộng (extensive iterative efforts), làm tăng đáng kể chi phí nhân công (labour costs) (Susan and Tuteja, 2025).
  * Kỹ nghệ đặc trưng tự động (Automated Feature Engineering - AutoFE) nổi lên như một trọng tâm nghiên cứu thiết yếu trong các tác vụ học máy trên dữ liệu bảng.
  * Mục tiêu của AutoFE: tự động hóa và dùng thuật toán để khám phá, xây dựng các đặc trưng hiệu quả nhằm giảm bớt nỗ lực thủ công và nâng cao hiệu năng mô hình học máy (Khurana et al., 2016).

* **Hạn chế về khả năng diễn giải của các phương pháp AutoFE truyền thống (traditional AutoFE):**
  * Các phương pháp AutoFE truyền thống bao gồm: tối ưu hóa lai với tìm kiếm chùm tia (hybrid optimization with beam search) (Horn et al., 2019), cắt tỉa động (dynamic pruning) (Zhang et al., 2023b), và chọn lọc đặc trưng (feature selection) (Li et al., 2017; Cheng et al., 2025a).
  * Cơ chế sinh đặc trưng truyền thống dựa trên các quy tắc biến đổi định sẵn (predefined transformation rules), tìm kiếm vét cạn (exhaustive search), hoặc chiến lược dựa trên tối ưu hóa (optimization-based strategies).
  * Mặc dù có khả năng cải thiện hiệu năng mô hình, AutoFE truyền thống mắc phải hạn chế nghiêm trọng về khả năng diễn giải kém (poor interpretability):
    * Các đặc trưng sinh ra thường là những tổ hợp toán học phức tạp (complex mathematical compositions) hoàn toàn không có ý nghĩa ngữ nghĩa tường minh (devoid of explicit semantic meaning).
    * Tạo ra sự tách rời khỏi logic đặc thù miền mà con người có thể hiểu được (human-understandable domain-specific logic).
  * Tác hại nghiêm trọng trong các tình huống nhạy cảm như khai phá nhân tố (factor mining) (Wang et al., 2025, 2026):
    * Khả năng diễn giải là yêu cầu bắt buộc nhằm xác thực tính hợp lý kinh tế đằng sau các tín hiệu (validating the economic rationale behind signals), bảo đảm tuân thủ quy định pháp lý (regulatory compliance), và hỗ trợ chẩn đoán lỗi hiệu quả (effective error diagnosis).
    * Nếu thiếu logic suy luận rõ ràng, rất khó phân biệt giữa các mẫu hình dự đoán vững chắc (robust predictive patterns) và các tương quan giả tạo (spurious correlations), gây suy giảm niềm tin vào các quyết định của mô hình.

* **Tiềm năng và hai thách thức cốt lõi của AutoFE dựa trên mô hình ngôn ngữ lớn (LLM-based AutoFE):**
  * Tiềm năng của LLM-based AutoFE:
    * Sự phát triển của các LLM mang lại tiềm năng mới nhờ năng lực hiểu ngữ nghĩa (semantic understanding) (Hollmann et al., 2023b), suy luận logic (logical reasoning) (Zou et al., 2026), và dẫn hướng tri thức (knowledge guidance) (Nam et al., 2024).
    * Tận dụng tri thức tiên nghiệm phong phú (rich prior knowledge) và khả năng hiểu ngữ cảnh để tự động nhận diện mối quan hệ tiềm năng giữa các đặc trưng thô trong dữ liệu bảng, xây dựng các đặc trưng mới giàu tính diễn giải thông qua phép toán và quy tắc logic.
  * Hai thách thức cốt lõi mà LLM-based AutoFE phải đối mặt:
    * Thách thức 1: Việc sinh các đặc trưng nâng cao hiệu năng đòi hỏi các tương tác lặp lại sâu rộng với mô hình dự đoán xuôi dòng (extensive iterative interactions with downstream models) để xác thực và tinh chỉnh, dẫn đến chi phí tính toán cực lớn (prohibitive computational overhead) và khả năng mở rộng hạn chế (limited scalability) (Abhyankar et al., 2025).
    * Thách thức 2: Sự nhạy cảm cố hữu của LLM đối với ảo giác (hallucinations) và thiên kiến tiềm ẩn (implicit biases) có thể dẫn tới việc sinh ra các đặc trưng không hợp lệ về mặt ngữ nghĩa hoặc không công bằng (semantically invalid or unfair features), ảnh hưởng nghiêm trọng đến độ tin cậy và tính toàn vẹn dự đoán (predictive integrity) của mô hình (Cheng et al., 2026; Han et al., 2024).
  * Tóm lược sự đối lập giữa hai trường phái AutoFE: AutoFE truyền thống bị hạn chế bởi đặc trưng không thể diễn giải, trong khi LLM-based AutoFE gặp khó khăn vì chi phí lặp lại cao, ảo giác và thiên kiến. Nhu cầu cấp thiết là phát triển khung làm việc AutoFE hiệu quả cao, sinh đặc trưng vừa có tính diễn giải vừa mang lại bước nhảy vọt về hiệu năng.
  * **Hình 1.** So sánh cơ chế sinh đặc trưng và diễn giải giữa các phương pháp AutoFE
    * <img src="assets/fig_01_p2.jpeg" alt="Hình 1" />
    * **Hình này chứng minh điều gì**
      * SymboLLM-FE kết hợp hồi quy ký hiệu và LLM đạt cả độ chính xác cao và tính minh bạch diễn giải
    * **Từ đâu mà thấy được**
      * Sơ đồ 3 nhánh so sánh: AutoFE truyền thống (hộp đen), AutoFE dựa trên LLM (bất ổn định), và SymboLLM-FE (hồi quy ký hiệu định hướng LLM)
      * Nhánh truyền thống minh họa Blind Operator Stack với các toán tử (+, -, x, log, exp, sin, GroupByThenMean, Freq)

* **Khung làm việc SymboLLM-FE và quy trình hợp tác hai giai đoạn:**
  * SymboLLM-FE là khung làm việc mới kết hợp hồi quy ký hiệu (symbolic regression) và LLM để sinh ra các đặc trưng toán học có khả năng diễn giải, nâng cao hiệu năng mô hình dự đoán.
  * Quy trình hợp tác hai giai đoạn (two-stage collaborative pipeline):
    * Giai đoạn 1 (Thu hẹp không gian và kiến tạo công thức ứng viên): Áp dụng chiến lược cửa sổ trượt mở rộng (expanding-sliding window strategy) dựa trên phân tích tương quan Spearman (Spearman correlation analysis) giúp giảm không gian tìm kiếm từ hàm mũ $\mathcal{O}(2^n)$ xuống đa thức $\mathcal{O}(n^2)$, cho phép hồi quy ký hiệu sinh ra các công thức ứng viên tường minh, có cơ sở toán học chặt chẽ.
    * Giai đoạn 2 (Tiêm tri thức tiên nghiệm và tinh chỉnh mã thực thi): Tận dụng LLM để tiêm tri thức tiên nghiệm đặc thù miền (domain-specific priors) vào các công thức toán học vốn mờ mịt, chuyển đổi chúng thành mã nguồn thực thi có ý nghĩa ngữ nghĩa thông qua chuỗi suy luận (chain-of-thought reasoning).
    * Vòng lặp tinh chỉnh lặp lại vừa xác thực độ hữu dụng của đặc trưng thông qua hiệu năng bộ dự đoán xuôi dòng, vừa bảo đảm căn chỉnh với logic nghiệp vụ, đạt được sự cân bằng vững chắc giữa khám phá đặc trưng hiệu năng cao và tính minh bạch có thể diễn giải cho con người.
  * So sánh định lượng hiệu quả hiệu năng và chi phí tính toán giữa các phương pháp AutoFE:
    * AutoFE truyền thống (không gọi LLM): AutoFeat sinh $2$ đặc trưng, đạt điểm $79.75$; OpenFE sinh $1436$ đặc trưng, đạt điểm $79.53$.
    * AutoFE dựa trên LLM: CAAFE sinh $30$ đặc trưng với $10$ lượt gọi API, đạt điểm $79.94$; OcTree sinh $50$ đặc trưng với $50$ lượt gọi API, đạt điểm $79.52$; FEBP sinh $200$ đặc trưng với $29$ lượt gọi API, đạt điểm $79.36$; LLM-FE sinh $30$ đặc trưng với $35$ lượt gọi API, đạt điểm $79.59$; LLM-RANK là bộ chọn đặc trưng nên không sinh đặc trưng mới, tốn $7$ lượt gọi API, đạt điểm $78.86$.
    * SymboLLM-FE sinh $70$ đặc trưng, đạt điểm số cao nhất là $80.02$ với chỉ $4$ lượt gọi API LLM (single-digit calls).
  * **Bảng 1.** Phân tích so sánh hiệu quả hiệu năng và chi phí tính toán giữa các phương pháp AutoFE
    * <img src="assets/table_01_p3.png" alt="Bảng 1" />
    * **Bảng này chứng minh điều gì**
      * SymboLLM-FE cân bằng giữa hiệu năng cao, khả năng diễn giải tốt và chi phí gọi LLM thấp
    * **Từ đâu mà thấy được**
      * Các cột so sánh đặc tính: Feature Generation, Interpretability, LLM Call Overhead và Performance trên bảng

* **Tóm tắt bốn đóng góp chính của bài báo:**
  * Thực hiện phân tích thực nghiệm và chỉ ra rằng AutoFE truyền thống chịu hạn chế về tính diễn giải không đầy đủ, trong khi LLM-based AutoFE gặp trở ngại lớn về thử nghiệm lặp lại sâu rộng, ảo giác và thiên kiến tiềm ẩn.
  * Đề xuất SymboLLM-FE giải quyết các thách thức của AutoFE hiện nay thông qua việc tận dụng hồi quy ký hiệu để khai phá các đặc trưng tăng cường hiệu năng, sau đó tinh chỉnh bằng LLM để nâng cao khả năng diễn giải.
  * Đánh giá toàn diện trên $6$ tập dữ liệu thế giới thực và $4$ cuộc thi Kaggle chứng minh hiệu năng vượt trội và khả năng tổng quát hóa của SymboLLM-FE so với các phương pháp AutoFE hiện nay.
  * SymboLLM-FE giải quyết đồng thời thách thức kép về tính diễn giải kém và gánh nặng thử nghiệm lặp lại bằng cơ chế tinh chỉnh LLM dựa trên tiên nghiệm thống kê (statistical prior-grounded LLM refinement mechanism) với số lượt gọi LLM chỉ ở mức một chữ số (single-digit LLM calls).
