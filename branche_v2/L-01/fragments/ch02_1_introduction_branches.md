## 1 Introduction

* **Định nghĩa và vai trò cốt lõi của kỹ thuật đặc trưng (feature engineering) trên dữ liệu dạng bảng (tabular data):**
  * Kỹ thuật đặc trưng (feature engineering) là quá trình chuyển đổi dữ liệu thô (raw data) thành các đặc trưng có ý nghĩa (meaningful features) cho các mô hình học máy (machine learning models), giữ vai trò then chốt trong việc cải thiện hiệu năng dự đoán (predictive performance), đặc biệt khi làm việc với dữ liệu dạng bảng (tabular data) (Domingos, $2012$).
  * Trong nhiều tác vụ dự đoán trên dữ liệu bảng, các đặc trưng được thiết kế tốt đã được chứng minh là tăng cường đáng kể hiệu năng của các mô hình dạng cây (tree-based models), thường vượt trội hơn các mô hình học sâu (deep learning models) vốn phụ thuộc vào các biểu diễn học được (learned representations) (Grinsztajn et al., $2022$).
  * Tuy nhiên, các tác vụ lấy dữ liệu làm trung tâm (data-centric tasks) như kỹ thuật đặc trưng là một trong những quy trình tiêu tốn nhiều thời gian và tài nguyên nhất trong quy trình học trên dữ liệu bảng (tabular learning workflow) (Anaconda, $2020$; Hollmann et al., $2024$).
  * Quy trình này đòi hỏi các chuyên gia và nhà khoa học dữ liệu (data scientists) phải khám phá nhiều tổ hợp khả dĩ trong không gian tổ hợp khổng lồ (vast combinatorial space) của các phép biến đổi đặc trưng.

* **Hạn chế của các phương pháp kỹ thuật đặc trưng cổ điển (classical feature engineering methods):**
  * Các phương pháp kỹ thuật đặc trưng cổ điển (Kanter & Veeramachaneni, $2015$; Khurana et al., $2016, 2018$; Horn et al., $2020$; Zhang et al., $2023$) xây dựng không gian tìm kiếm mở rộng gồm các thao tác xử lý đặc trưng, dựa vào nhiều kỹ thuật tìm kiếm và tối ưu hóa khác nhau để xác định các đặc trưng hiệu quả nhất.
  * Các không gian tìm kiếm này phần lớn bị ràng buộc bởi các phép biến đổi được xác định trước, thiết kế thủ công (predefined, manually designed transformations) và thường thất bại trong việc kết hợp tri thức miền (domain knowledge) (Zhang et al., $2023$).
  * Tri thức miền có thể đóng vai trò như một phân phối tiên nghiệm vô giá (invaluable prior) để xác định các phép biến đổi này, giúp giảm thiểu độ phức tạp và tạo ra các đặc trưng hiệu quả, có khả năng diễn giải cao hơn (interpretable and effective features) (Hollmann et al., $2024$).

* **Sự xuất hiện của Mô hình Ngôn ngữ Lớn (LLMs) và hạn chế của các phương pháp dựa trên LLM hiện hành:**
  * Các mô hình ngôn ngữ lớn (Large Language Models — LLMs) đã nổi lên như một giải pháp mạnh mẽ cho thách thức này nhờ sở hữu nguồn tri thức miền nhúng sâu rộng (extensive embedded domain knowledge) có thể khai thác cho kỹ thuật đặc trưng.
  * Mặc dù các hướng tiếp cận gần đây cho thấy kết quả khả quan trong việc kết hợp tri thức này vào tự động khám phá đặc trưng, các phương pháp dựa trên LLM hiện tại (Hollmann et al., $2024$; Han et al., $2024$) chủ yếu phụ thuộc vào kỹ thuật nhắc lệnh trực tiếp (direct prompting) hoặc điểm số kiểm định (validation scores) để định hướng sinh đặc trưng.
  * Những phương pháp này không tận dụng được các hiểu biết rút ra từ các thử nghiệm khám phá đặc trưng trước đó, do đó chưa thiết lập được mối liên kết có ý nghĩa giữa quá trình sinh đặc trưng (feature generation) và hiệu năng dựa trên dữ liệu (data-driven performance).

* **Khung làm việc đề xuất LLM-FE (Large Language Models for Automated Feature Engineering):**
  * Nghiên cứu đề xuất LLM-FE, một khung làm việc mới tích hợp năng lực của LLMs với các mô hình dự đoán dữ liệu bảng và tìm kiếm tiến hóa (evolutionary search) nhằm hỗ trợ tối ưu hóa đặc trưng hiệu quả (minh họa tại Figure $1$).
  * LLM-FE tuân theo một quy trình lặp để sinh và đánh giá giả thuyết về phép biến đổi đặc trưng, sử dụng hiệu năng của mô hình dự đoán bảng làm phần thưởng (reward) để thúc đẩy việc sinh các đặc trưng hiệu quả.
  * **Kiến trúc và quy trình $4$ bước của LLM-FE (Figure $1$):**
    * **(a) Sinh đặc trưng mới (New Feature Generation):**
      * Khởi đầu từ một chương trình biến đổi đặc trưng ban đầu (`modify_features_v0`), LLM-FE khai thác tri thức miền nhúng của LLMs bằng cách đưa vào các chi tiết đặc thù của tác vụ (task description), mô tả đặc trưng (feature descriptions), và một tập con các mẫu dữ liệu (data samples).
      * Tại mỗi vòng lặp, LLM đóng vai trò như một bộ tối ưu hóa tiến hóa được định hướng bởi tri thức (knowledge-guided evolutionary optimizer), tạo đột biến (mutating) trên các ví dụ về các chương trình biến đổi đặc trưng thành công trước đó (Meyerson et al., $2024$) để sinh ra các chương trình khám phá đặc trưng mới dưới dạng mã nguồn Python (`modify_features(df_in)`).
      * Các đặc trưng sinh ra mang tính diễn giải cao nhờ tri thức miền của LLM (ví dụ: tạo đặc trưng chỉ số kháng insulin $\text{insulin\_resistance} = \frac{\text{glucose} \times \text{insulin}}{405}$ và chỉ số tương tác tuổi - thể trọng $\text{age\_bmi} = \text{age} \times \text{bmi}$).
    * **(b) Kỹ thuật đặc trưng (Feature Engineering):**
      * Chương trình biến đổi đặc trưng được áp dụng trực tiếp lên tập dữ liệu thô ban đầu để tạo thành tập dữ liệu tăng cường (augmented dataset), bao gồm các đặc trưng mới được bổ sung và các cột thô không cần thiết được loại bỏ (ví dụ: loại bỏ cột `insulin` sau khi đã tính kháng insulin).
    * **(c) Đánh giá đặc trưng (Feature Evaluation):**
      * Tập dữ liệu tăng cường kèm các đặc trưng mới được dùng để huấn luyện mô hình dự đoán học máy (ML prediction model).
      * Hiệu năng của mô hình được đánh giá trên tập kiểm định giữ lại (held-out validation set) nhằm cung cấp phản hồi dựa trên dữ liệu (data-driven feedback) thông qua các điểm số kiểm định cụ thể (validation scores, ví dụ: $0.8034$, $0.8247$, $0.7964$, v.v.).
    * **(d) Quản lý kinh nghiệm (Experience Management):**
      * Duy trì một bộ đệm/bộ nhớ dài hạn (long-term memory buffer) lưu trữ các chương trình biến đổi đạt điểm số cao.
      * Ứng dụng kiến trúc tiến hóa đa đảo (multi-island evolution: Island $1$, Island $2$, ..., Island $k$) để duy trì tính đa dạng trong tìm kiếm.
      * Lấy mẫu từ bộ nhớ để cung cấp các ví dụ mẫu trong ngữ cảnh (in-context samples / demonstrations) cho câu nhắc tinh chỉnh lặp tiếp theo của LLM.

* **So sánh đối chuẩn toàn diện giữa LLM-FE và các phương pháp kỹ thuật đặc trưng hiện có (Table $1$):**
  * Các phương pháp truyền thống thiếu tính thích ứng và sự hiểu biết ngữ cảnh sâu sắc, trong khi các phương pháp dựa trên LLM trước đây chỉ sinh các đặc trưng đơn giản (Küken et al., $2024$) hoặc dùng phản hồi để tinh chỉnh lặp chỉ một quy tắc đơn lẻ.
  * Ngược lại, LLM-FE hỗ trợ đồng thời cả $4$ khía cạnh cốt lõi nhờ kết hợp tri thức miền từ LLM và tối ưu hóa định hướng phản hồi:
    1. Tri thức miền (Domain Knowledge).
    2. Định hướng bằng phản hồi (Feedback Driven).
    3. Đặc trưng phức tạp (Complex Features).
    4. Tinh chỉnh đa đặc trưng (Multi-Feature Refinement).
  * **Bảng so sánh chi tiết các phương pháp (Table $1$):**
    * AutoFeat (Horn et al., $2020$): Domain Knowledge: ✗; Feedback Driven: ✗; Complex Features: ✓; Multi-Feature Refinement: ✗.
    * OpenFE (Zhang et al., $2023$): Domain Knowledge: ✗; Feedback Driven: ✗; Complex Features: ✓; Multi-Feature Refinement: ✗.
    * FeatLLM (Han et al., $2024$): Domain Knowledge: ✓; Feedback Driven: ✗; Complex Features: ✗; Multi-Feature Refinement: ✗.
    * CAAFE (Hollmann et al., $2024$): Domain Knowledge: ✓; Feedback Driven: ✓; Complex Features: ✗; Multi-Feature Refinement: ✗.
    * OCTree (Nam et al., $2024$): Domain Knowledge: ✓; Feedback Driven: ✓; Complex Features: ✗; Multi-Feature Refinement: ✗.
    * **LLM-FE (Đề xuất)**: Domain Knowledge: ✓; Feedback Driven: ✓; Complex Features: ✓; Multi-Feature Refinement: ✓.

* **Thiết lập thực nghiệm và hiệu năng khái quát hóa:**
  * LLM-FE được đánh giá thực nghiệm với hai mô hình nền LLM gồm Llama-3.1-8B-Instruct (Dubey et al., $2024$) và GPT-3.5-Turbo (OpenAI, $2023$).
  * Đánh giá bao trùm trên cả các tác vụ phân loại (classification) và hồi quy (regression) trên các tập dữ liệu dạng bảng đa dạng.
  * LLM-FE liên tục vượt trội hơn các phương pháp kỹ thuật đặc trưng tiên tiến nhất, xác định các đặc trưng phù hợp ngữ cảnh giúp tăng cường hiệu năng hạ nguồn.
  * Những cải thiện rõ rệt được ghi nhận trên các mô hình dạng bảng phổ biến gồm XGBoost (Chen & Guestrin, $2016$), TabPFN (Hollmann et al., $2023$), và MLP (Gorishniy et al., $2021$), nhấn mạnh tầm quan trọng của tìm kiếm tiến hóa trong việc đạt được kết quả vượt trội.

* **Các đóng góp chính của nghiên cứu (Major Contributions):**
  * **Đóng góp 1 — Khung làm việc LLM-FE:** Giới thiệu LLM-FE, một khung làm việc mới mô hình hóa kỹ thuật đặc trưng thành bài toán tối ưu hóa tiến hóa dưới sự định hướng của LLM, tích hợp chặt chẽ tri thức miền, đánh giá dựa trên dữ liệu, và bộ nhớ dài hạn phục vụ quá trình tinh chỉnh lặp.
  * **Đóng góp 2 — Hiệu năng vượt trội và tính khái quát hóa:** Kết quả thực nghiệm chứng minh tính hiệu quả của LLM-FE, thể hiện khả năng vượt trội so với các mô hình cơ sở tiên tiến nhất, đồng thời thể hiện khả năng khái quát hóa cao trên nhiều bộ dự đoán (predictors: XGBoost, TabPFN, MLP) và nhiều nền tảng LLM khác nhau.
  * **Đóng góp 3 — Phân tích loại trừ thành phần (Ablation Study):** Thông qua một nghiên cứu loại trừ toàn diện, công trình làm nổi bật vai trò cốt lõi của $4$ yếu tố: tri thức miền (domain knowledge), tìm kiếm tiến hóa (evolutionary search), phản hồi dựa trên dữ liệu (data-driven feedback), và các mẫu dữ liệu (data samples) trong việc dẫn dắt LLM khám phá không gian đặc trưng một cách hiệu quả và khám phá các đặc trưng có tác động lớn nhất.
