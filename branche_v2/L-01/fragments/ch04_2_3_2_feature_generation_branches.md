### 3.2 Feature Generation

* Bước sinh đặc trưng (feature generation step) sử dụng một mô hình ngôn ngữ lớn (LLM - Large Language Model) để tạo ra nhiều chương trình biến đổi đặc trưng (feature transformation programs) mới, tận dụng tri thức tiên nghiệm (prior knowledge), năng lực suy luận (reasoning) và khả năng học trong ngữ cảnh (in-context learning) của mô hình nhằm khám phá không gian đặc trưng (feature space) một cách hiệu quả (minh họa tại Figure $1\text{(a)}$).

#### 3.2.1 Input Prompt

* Phương pháp nhắc lệnh có cấu trúc (structured prompting methodology) được phát triển nhằm tạo điều kiện thuận lợi cho việc tạo ra các chương trình khám phá đặc trưng (feature discovery programs) hiệu quả và phù hợp với ngữ cảnh.
  * Prompt được thiết kế để cung cấp: thông tin toàn diện đặc thù cho dữ liệu (comprehensive data-specific information), một chương trình biến đổi đặc trưng ban đầu làm điểm khởi đầu cho tiến hóa (evolution starting point), một hàm đánh giá (evaluation function), và một định dạng đầu ra được xác định rõ ràng (well-defined output format, xem chi tiết tại Appendix B.1).
  * Prompt đầu vào $p$ bao gồm các phần tử cốt lõi sau:
    * **Chỉ dẫn (Instruction)**:
      * LLM được giao nhiệm vụ tìm kiếm các đặc trưng phù hợp nhất để giúp giải quyết tác vụ cho trước.
      * Tác vụ nhấn mạnh việc sử dụng tri thức tiên nghiệm (prior knowledge) của LLM về miền dữ liệu (domain) của tập dữ liệu để sinh đặc trưng.
      * LLM được chỉ dẫn rõ ràng để sinh các đặc trưng mới lạ (novel features) và cung cấp lập luận từng bước (step-by-step reasoning) rõ ràng về mức độ liên quan của chúng đối với tác vụ dự đoán (prediction task).
      * Do các LLM có xu hướng sinh ra các đặc trưng đơn giản (simple features), nhóm tác giả chỉ dẫn cụ thể cho LLM sinh ra các đặc trưng phức tạp (complex features).
    * **Đặc tả tập dữ liệu (Dataset Specification)**:
      * Sau khi cung cấp chỉ dẫn, LLM được cung cấp thông tin đặc thù của tập dữ liệu từ siêu dữ liệu (metadata) $M$.
      * Thông tin này bao gồm mô tả chi tiết về tác vụ hạ nguồn dự kiến (intended downstream task), cùng với tên các đặc trưng $C$ và các mô tả tương ứng của chúng.
      * Cung cấp một số lượng giới hạn các mẫu đại diện từ tập dữ liệu dạng bảng (tabular dataset).
      * Nhằm cải thiện khả năng diễn giải dữ liệu hiệu quả, áp dụng phương pháp tuần tự hóa (serialization approach) từ các nghiên cứu trước (Dinh et al., 2022; Hegselmann et al., 2023; Han et al., 2024):
        $$\text{Serialize}(x_i, y_i, C) = \text{‘If } c_1 \text{ is } x_i^1, \dots, c_d \text{ is } x_i^d \text{. Then Result is } y_i\text{’} \tag{3}$$
      * Việc cung cấp các chi tiết đặc thù của tập dữ liệu giúp định hướng mô hình ngôn ngữ tập trung vào các đặc trưng thích hợp nhất theo ngữ cảnh, trực tiếp hỗ trợ tập dữ liệu và mục tiêu tác vụ.
    * **Hàm đánh giá (Evaluation Function)**:
      * Hàm đánh giá được tích hợp trực tiếp vào prompt, định hướng mô hình ngôn ngữ sinh ra các chương trình biến đổi đặc trưng phù hợp với các mục tiêu hiệu năng (performance objectives).
      * Các chương trình này làm giàu (augment) tập dữ liệu gốc bằng các đặc trưng mới; các đặc trưng này được đánh giá dựa trên hiệu năng của một mô hình dự đoán được huấn luyện trên dữ liệu đã làm giàu (augmented data).
      * Điểm số đánh giá của mô hình trên tập kiểm định làm giàu (augmented validation set) đóng vai trò là chỉ số đo lường chất lượng đặc trưng.
      * Bằng cách đưa hàm đánh giá vào prompt, LLM sinh ra các chương trình vốn dĩ đã phù hợp với các tiêu chí hiệu năng mong muốn.
    * **Minh họa trong ngữ cảnh (In-Context Demonstration)**:
      * Lấy mẫu $k$ minh họa có hiệu năng cao nhất từ các vòng lặp trước, cho phép LLM kế thừa và phát triển từ các đầu ra thành công.
      * Tương tác lặp lại giữa các kết quả đầu ra sinh của LLM và phản hồi của bộ đánh giá (evaluator), được định hướng bởi các ví dụ này, tạo điều kiện thuận lợi cho một quy trình tinh chỉnh có hệ thống (systematic refinement process).
      * Qua từng vòng lặp, LLM tiến bộ dần các đầu ra của mình bằng cách tận dụng các khuôn mẫu (patterns) và hiểu biết sâu sắc (insights) được xác định từ các minh họa thành công trước đó.

#### 3.2.2 Feature Sampling

* Tại mỗi vòng lặp $t$, prompt $p_t$ được xây dựng bằng cách lấy mẫu vòng lặp trước làm đầu vào cho LLM $\pi_\theta$, tạo ra đầu ra $T_1, \dots, T_b = \pi_\theta(p_t)$ đại diện cho một tập gồm $b$ chương trình được lấy mẫu.
* Nhằm thúc đẩy tính đa dạng và duy trì sự cân bằng giữa khám phá (exploration - tính sáng tạo) và khai thác (exploitation - tri thức tiên nghiệm), phương pháp lấy mẫu ngẫu nhiên dựa trên nhiệt độ (stochastic temperature-based sampling) được áp dụng.
* Kiểm tra tính thực thi và lọc chương trình:
  * Mỗi phép biến đổi đặc trưng được lấy mẫu ($T_i$) đều được thực thi trước khi đánh giá nhằm loại bỏ các chương trình dễ phát sinh lỗi (error-prone programs).
  * Cơ chế này đảm bảo chỉ các chương trình biến đổi đặc trưng hợp lệ và thực thi được (valid, executable) mới được đưa vào đường ống tối ưu hóa (optimization pipeline).
  * Nhằm đảm bảo hiệu quả tính toán (computational efficiency), một ngưỡng thời gian thực thi tối đa (maximum execution time threshold) được áp dụng; bất kỳ chương trình nào vượt quá ngưỡng này đều bị loại bỏ.
