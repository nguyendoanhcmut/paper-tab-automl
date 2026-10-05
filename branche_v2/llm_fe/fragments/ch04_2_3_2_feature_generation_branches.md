### 3.2 Sinh Đặc trưng (Feature Generation)

- **Tổng quan về bước sinh đặc trưng**:
  - Bước sinh đặc trưng sử dụng một Mô hình Ngôn ngữ Lớn (Large Language Model - LLM) để khởi tạo nhiều chương trình biến đổi đặc trưng mới (feature transformation programs) (được minh họa trực quan tại Figure 1(a)).
  - Quá trình này tận dụng tri thức tiền định (prior knowledge), khả năng suy luận (reasoning) và năng lực học trong ngữ cảnh (in-context learning) của mô hình để khám phá không gian đặc trưng (feature space) một cách hiệu quả.

#### 3.2.1 Prompt Đầu vào (Input Prompt)

- **Phương pháp luận thiết kế prompt có cấu trúc (Structured Prompting Methodology)**:
  - Nhằm hỗ trợ việc tạo ra các chương trình khám phá đặc trưng vừa hiệu quả vừa phù hợp với ngữ cảnh, nghiên cứu phát triển một phương pháp thiết kế prompt có cấu trúc chặt chẽ.
  - Prompt được thiết kế nhằm cung cấp toàn diện: thông tin đặc thù của dữ liệu (data-specific information), một chương trình biến đổi đặc trưng khởi đầu làm điểm xuất phát cho tiến hóa (initial feature transformation program), một hàm đánh giá (evaluation function), và một định dạng đầu ra được định nghĩa rõ ràng (xem thêm chi tiết tại Appendix B.1).
  - Prompt đầu vào $p$ bao gồm 4 thành phần then chốt:
- **Chỉ dẫn (Instruction)**:
  - LLM được giao nhiệm vụ tìm kiếm các đặc trưng phù hợp nhất để hỗ trợ giải quyết tác vụ cho trước.
  - Tác vụ nhấn mạnh việc khai thác tri thức tiền định của LLM về miền dữ liệu (dataset's domain) để tạo ra các đặc trưng.
  - LLM được chỉ dẫn rõ ràng phải tạo ra các đặc trưng mới lạ (novel features) và cung cấp lập luận từng bước (step-by-step reasoning) minh bạch về mức độ liên quan của chúng đối với tác vụ dự đoán.
  - Do LLM thường có xu hướng thiên lệch tạo ra các đặc trưng đơn giản, prompt chỉ dẫn đặc biệt yêu cầu LLM phải sinh ra các đặc trưng phức tạp (complex features).
- **Đặc tả Tập dữ liệu (Dataset Specification)**:
  - Sau phần chỉ dẫn, LLM được cung cấp thông tin đặc thù của tập dữ liệu trích xuất từ siêu dữ liệu (metadata) $M$.
  - Thông tin này bao gồm mô tả chi tiết về tác vụ hạ nguồn dự kiến (downstream task), đi kèm danh sách tên các đặc trưng $C$ và các phần mô tả tương ứng của từng thuộc tính.
  - Ngoài ra, một số lượng giới hạn các mẫu dữ liệu đại diện từ tập dữ liệu dạng bảng cũng được cung cấp trong prompt.
  - Để nâng cao khả năng diễn giải dữ liệu hiệu quả của mô hình, phương pháp áp dụng kỹ thuật tuần tự hóa (serialization approach) tương tự các nghiên cứu trước (Dinh et al., 2022; Hegselmann et al., 2023; Han et al., 2024):
    $$\text{Serialize}(x_i, y_i, C) = \text{‘If } c_1 \text{ is } x_i^1, \dots, c_d \text{ is } x_i^d. \text{ Then Result is } y_i\text{’} \tag{3}$$
  - Việc cung cấp các chi tiết đặc thù của tập dữ liệu giúp định hướng mô hình ngôn ngữ tập trung vào các đặc trưng thích hợp nhất về mặt ngữ cảnh, trực tiếp hỗ trợ tập dữ liệu và mục tiêu tác vụ.
- **Hàm Đánh giá (Evaluation Function)**:
  - Hàm đánh giá được tích hợp trực tiếp vào prompt để dẫn dắt mô hình ngôn ngữ sinh ra các chương trình biến đổi đặc trưng bám sát các mục tiêu hiệu năng (performance objectives).
  - Các chương trình này thực hiện tăng cường tập dữ liệu gốc bằng các đặc trưng mới; chất lượng của chúng được đánh giá dựa trên hiệu năng của một mô hình dự đoán được huấn luyện trên dữ liệu tăng cường đó.
  - Điểm số đánh giá của mô hình trên tập kiểm định tăng cường (augmented validation set) đóng vai trò là thước đo chất lượng đặc trưng.
  - Nhờ việc nhúng hàm đánh giá vào prompt, LLM có thể sinh ra các chương trình vốn dĩ đã tương thích chặt chẽ với các tiêu chí hiệu năng mong muốn.
- **Mẫu Minh họa theo Ngữ cảnh (In-Context Demonstration)**:
  - Cụ thể, phương pháp lấy mẫu $k$ mẫu minh họa có hiệu năng cao nhất từ các vòng lặp trước đó, cho phép LLM kế thừa và phát triển từ các kết quả thành công.
  - Sự tương tác lặp đi lặp lại giữa đầu ra sinh của LLM và phản hồi từ bộ đánh giá (được định hướng bởi các ví dụ này) tạo điều kiện thuận lợi cho một quy trình tinh chỉnh có hệ thống (systematic refinement process).
  - Qua từng vòng lặp, LLM liên tục cải thiện chất lượng đầu ra bằng cách tận dụng các quy luật (patterns) và tri thức sâu sắc (insights) đã được đúc kết từ những mẫu minh họa thành công trước đó.

#### 3.2.2 Lấy Mẫu Đặc trưng (Feature Sampling)

- **Quy trình sinh và lấy mẫu chương trình tại mỗi vòng lặp**:
  - Tại mỗi vòng lặp $t$, prompt $p_t$ được xây dựng bằng cách lấy mẫu từ vòng lặp trước đó để làm đầu vào cho LLM $\pi_\theta$, từ đó tạo ra đầu ra $T_1, \dots, T_b = \pi_\theta(p_t)$ đại diện cho một tập hợp gồm $b$ chương trình được lấy mẫu.
- **Cân bằng giữa khám phá (exploration) và khai thác (exploitation)**:
  - Nhằm thúc đẩy tính đa dạng và duy trì sự cân bằng tối ưu giữa khám phá (exploration / tính sáng tạo) và khai thác (exploitation / tri thức tiền định), phương pháp áp dụng cơ chế lấy mẫu ngẫu nhiên dựa trên nhiệt độ (stochastic temperature-based sampling).
- **Lọc và kiểm tra tính khả thi trước đánh giá**:
  - Mỗi phép biến đổi đặc trưng được lấy mẫu ($T_i$) đều phải trải qua bước thực thi thử nghiệm trước khi tiến hành đánh giá nhằm loại bỏ các chương trình dễ phát sinh lỗi (error-prone programs).
  - Cơ chế này đảm bảo chỉ những chương trình biến đổi đặc trưng hợp lệ, có khả năng thực thi mới được xem xét trong đường ống tối ưu hóa (optimization pipeline).
- **Kiểm soát chi phí tính toán (Computational Efficiency)**:
  - Để đảm bảo hiệu quả về mặt tài nguyên tính toán, một ngưỡng thời gian thực thi tối đa (maximum execution time threshold) được áp dụng nghiêm ngặt; bất kỳ chương trình nào chạy vượt quá ngưỡng thời gian này đều bị loại bỏ ngay lập tức.
