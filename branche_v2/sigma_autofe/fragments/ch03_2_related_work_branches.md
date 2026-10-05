## 2. Related Work

### Traditional AutoFE Methods

- Các phương pháp kỹ nghệ đặc trưng tự động truyền thống (Traditional AutoFE - Automated Feature Engineering) chủ yếu vận hành dựa trên khung làm việc mở rộng - thu gọn (expansion-reduction framework).
  - Quy trình cốt lõi gồm hai giai đoạn: sinh ra không gian các đặc trưng ứng viên (candidate feature generation) và tiến hành chọn lọc đặc trưng (feature selection) để giữ lại tập đặc trưng tối ưu nhất.
- Deep Feature Synthesis (DFS) (Kanter và Veeramachaneni, 2015) khai thác các đường dẫn quan hệ (relational paths) và các phép toán nguyên thủy toán học (mathematical primitives) nhằm tự động tạo các đặc trưng liên bảng (cross-table features):
  - Sau giai đoạn mở rộng đặc trưng liên bảng, DFS thực hiện chọn lọc những đặc trưng đạt hiệu năng dự báo tốt nhất.
  - Ưu điểm: Tự động hóa quá trình trích xuất đặc trưng có cấu trúc quan hệ phức tạp giữa nhiều bảng mà không cần thiết kế thủ công.
  - Hạn chế: Dễ dẫn đến bùng nổ số lượng đặc trưng khi cơ sở dữ liệu có nhiều quan hệ lồng nhau; phụ thuộc vào lược đồ quan hệ định sẵn.
- ExploreKit (Katz và cộng sự, 2016) đề xuất khung làm việc sinh các đặc trưng ứng viên bằng cách kết hợp tất cả các đặc trưng gốc (combining all original features):
  - Tiến hành đánh giá và chọn lọc đặc trưng thông qua một bộ phân loại xếp hạng (ranking classifier).
  - Ưu điểm: Khám phá có hệ thống không gian tương tác giữa các đặc trưng ban đầu bằng mô hình học máy để xếp hạng.
  - Hạn chế: Chi phí tính toán và bộ nhớ tăng nhanh theo hàm số mũ khi số lượng đặc trưng gốc tăng lên.
- AutoFeat (Horn và cộng sự, 2019) tích hợp các phép biến đổi đặc trưng phi tuyến tính (non-linear feature transformations) và sử dụng mô hình tuyến tính có chuẩn hóa $L_1$ ($L_1$-regularized linear model) để chọn lọc đặc trưng:
  - Nâng cao hiệu quả năng lực dự báo của các mô hình tuyến tính trong khi vẫn bảo toàn tính diễn giải (interpretability).
  - Ưu điểm: Cung cấp các đặc trưng phi tuyến toán học rõ ràng, giữ trọn tính minh bạch và khả năng giải thích của mô hình tuyến tính.
  - Hạn chế: Phạm vi biến đổi bị giới hạn trong các hàm phi tuyến tiền định; chưa nắm bắt toàn diện các tương tác phi tuyến bậc cao phức tạp giữa nhiều thuộc tính.
- Tính toán tiến hóa (Evolutionary Computation) (Bäck và Schwefel, 1996) và lập trình di truyền (Genetic Programming) (Espejo và cộng sự, 2009) được ứng dụng rộng rãi trong AutoFE truyền thống:
  - TPOT (Olson và Moore, 2016) ứng dụng lập trình di truyền để phối hợp các bộ chọn đặc trưng (feature selectors), bộ biến đổi (transformers) và bộ phân loại (classifiers):
    - Mục tiêu tối ưu hóa là cực đại hóa độ chính xác dự báo (predictive accuracy) của toàn bộ pipeline học máy.
    - Ưu điểm: Tự động tìm kiếm cấu trúc pipeline trích xuất đặc trưng và mô hình hóa tối ưu mà không cần giả định trước.
    - Hạn chế: Không gian tìm kiếm rộng lớn dẫn đến chi phí tính toán cực kỳ tốn kém và thời gian chạy lâu.
- AutoGluon (Erickson và cộng sự, 2020) xử lý các tương tác đặc trưng theo cách tiềm ẩn (implicitly):
  - Kiến trúc tích hợp cơ chế suy luận kiểu dữ liệu thông minh theo phân cấp (hierarchical intelligent type inference) cùng cấu trúc xếp chồng mô hình đa tầng (multi-stage model stacking architecture).
  - Ưu điểm: Hiệu năng thực nghiệm mạnh mẽ, tự động hóa toàn diện quy trình xử lý dữ liệu bảng mà không đòi hỏi tạo đặc trưng tường minh phức tạp.
  - Hạn chế: Thiếu các đặc trưng tương tác tường minh dẫn đến giảm tính minh bạch và khó khăn trong việc phân tích căn nguyên dữ liệu.
- OpenFE (Zhang và cộng sự, 2023) đề xuất chiến lược cắt tỉa hai giai đoạn (two-stage pruning strategy):
  - Nhận diện và sàng lọc hiệu quả các đặc trưng ứng viên chất lượng cao (high-quality candidate features) từ không gian ứng viên khổng lồ.
  - Ưu điểm: Tối ưu hóa đáng kể tốc độ và khả năng mở rộng (scalability) so với các giải pháp mở rộng - thu gọn truyền thống.
  - Hạn chế: Vẫn dựa trên các toán tử biến đổi được định nghĩa trước, không tận dụng được tri thức ngữ nghĩa của miền ứng dụng.

### LLM-based AutoFE Methods

- Các mô hình ngôn ngữ lớn (LLMs) xây dựng trên kiến trúc Transformer (Vaswani và cộng sự, 2017) sở hữu năng lực học theo ngữ cảnh (In-Context Learning - ICL) và khả năng suy luận mạnh mẽ (Guo và cộng sự, 2025), phù hợp với việc ứng dụng tri thức miền (domain knowledge).
- CAAFE (Hollmann và cộng sự, 2023) là phương pháp đầu tiên đề xuất tận dụng tri thức ngữ nghĩa tiên nghiệm (prior semantic knowledge) của LLM:
  - Tạo ra các đặc trưng có khả năng diễn giải (interpretable features) dựa trên các mô tả bằng văn bản (textual descriptions) của bảng dữ liệu và thuộc tính.
  - Ưu điểm: Tận dụng hiểu biết ngữ nghĩa sâu rộng của LLM để sinh ra các đặc trưng có ý nghĩa thực tế cao và kèm giải thích rõ ràng.
  - Hạn chế: Phụ thuộc tuyệt đối vào sự tồn tại của mô tả văn bản (metadata); mất hiệu lực khi dữ liệu bị ẩn danh hoặc thiếu thông tin ngữ cảnh.
- FeatLLM (Han và cộng sự, 2024) khai thác LLM để sinh các quy tắc (rules) chuyển đổi đặc trưng thành các chuỗi nhị phân (binary sequences):
  - Quá trình chuyển đổi dựa trên mô tả đặc trưng và các mẫu dữ liệu thực tế (feature descriptions and samples), giúp tăng cường hiệu quả học trên dữ liệu bảng trong kịch bản ít mẫu (few-shot tabular learning).
  - Ưu điểm: Thúc đẩy độ chính xác phân loại trong các bài toán dữ liệu bảng ít mẫu nhờ biểu diễn nhị phân dựa trên quy tắc ngữ nghĩa.
  - Hạn chế: Vẫn phụ thuộc vào mô tả đặc trưng; việc nhị phân hóa có thể làm thất thoát các sắc thái thông tin liên tục.
- Tích hợp LLM với các thuật toán tối ưu hóa:
  - LLM-FE (Abhyankar và cộng sự, 2025) kết hợp kỹ nghệ đặc trưng dựa trên LLM với tính toán tiến hóa (evolutionary computation):
    - LLM đóng vai trò hỗ trợ sinh và biến đổi đặc trưng trong quá trình tìm kiếm tiến hóa.
    - Ưu điểm: Kết hợp sự linh hoạt về mặt ngữ nghĩa của LLM với khả năng tìm kiếm tối ưu toàn cục của giải thuật tiến hóa.
    - Hạn chế: Tiêu tốn chi phí gọi mô hình lớn qua các thế hệ tiến hóa lặp đi lặp lại.
- Thách thức thực tế và giải pháp biểu diễn cây (Tree Expression):
  - Trong các bài toán thực tế, mô tả đặc trưng và thông tin tác vụ thường khó thu thập do các rào cản bảo mật và quyền riêng tư (privacy and security issues), đồng thời việc mở rộng đặc trưng làm gia tăng đột biến độ dài prompt (prompt length).
  - OCTree (Nam và cộng sự, 2024) đề xuất chỉ sử dụng biểu thức cây của các đặc trưng (tree expression of features) để sinh ra các đặc trưng mới, không cần dựa vào mô tả ngữ nghĩa.
  - Ưu điểm: Khắc phục sự phụ thuộc vào văn bản mô tả nhạy cảm và giảm thiểu độ dài ngữ cảnh đưa vào prompt.
  - Hạn chế: Bỏ qua lợi thế tri thức ngữ nghĩa của LLM, chỉ khai thác cú pháp cây biểu thức toán học/logic.
- Các quan ngại và định hướng khắc phục trong LLM-based AutoFE:
  - Khả năng ghi nhớ dữ liệu của LLM (LLMs' memory of datasets) (Zhang và cộng sự, 2024): Đặt ra lo ngại về tính khái quát thực sự khi LLM có thể đã nhìn thấy các bộ dữ liệu tiêu chuẩn trong quá trình tiền huấn luyện.
  - Thiên kiến ưu tiên các phép toán đơn giản (preference for generating simple operations) (Küken và cộng sự, 2024): LLM có xu hướng ưa chuộng tạo ra các phép toán cơ bản thay vì các phép biến đổi phức tạp cần thiết.
  - Li và cộng sự (2026) đề xuất giải pháp phân tách quy trình đề xuất phép toán biến đổi (transformation operation proposal) khỏi quy trình chọn lọc đặc trưng (selection processes) nhằm nâng cao độ tin cậy và hiệu năng.
