## Abstract

* **Ứng dụng của Large Language Models (LLMs) trong Automated Feature Engineering (AutoFE - Kỹ thuật tạo đặc trưng tự động)**:
  * Các nghiên cứu gần đây khai thác LLM để nâng cao hiệu quả của AutoFE thông qua việc sử dụng mô tả ngữ nghĩa (semantic descriptions) và kỹ thuật nhắc dựa trên quỹ đạo (trajectory-based prompting).
* **Hai thách thức cốt lõi hạn chế khả năng ứng dụng và mở rộng quy mô trong tối ưu hóa dài hạn (long-horizon optimization)**:
  * *Thiếu siêu dữ liệu ngữ nghĩa*: Siêu dữ liệu ngữ nghĩa (semantic metadata) không có sẵn trong nhiều bối cảnh thực tế.
  * *Hạn chế của việc tích lũy quỹ đạo và cửa sổ ngữ cảnh (context window)*: Tích lũy quỹ đạo làm tăng nguy cơ vượt quá giới hạn cửa sổ ngữ cảnh; ngược lại, nếu thiếu thông tin quỹ đạo, quá trình sinh đặc trưng trở nên bất ổn định, dễ rơi vào cực trị địa phương (local optima) và gây ra tỷ lệ trùng lặp đặc trưng sinh ra cao (high duplicate rate).
* **Khung tối ưu hóa SIGMA (SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE)**:
  * Đề xuất khung tối ưu hóa với ngữ cảnh không đổi (scalable constant-context optimization framework) giải quyết đồng thời hai thách thức trên mà không cần siêu dữ liệu.
  * *Tín hiệu nhận biết tác vụ bằng giá trị SHAP (SHAP values)*: SIGMA khai thác các giá trị SHAP để cung cấp tín hiệu nhận biết tác vụ (task-aware signals), định hướng quá trình sinh đặc trưng theo nhóm (group feature generation) thay cho thông tin ngữ nghĩa.
  * *Cơ chế quỹ đạo ngầm định qua đặc trưng bộc lộ EXIT (EXposed-feature Implicit Trajectory)*: Sử dụng các đặc trưng được phơi bày trực tiếp trong prompt (exposed features) để đại diện ngầm định cho quỹ đạo mà không cần lưu trữ toàn bộ lịch sử các bước trước.
* **Kết quả thực nghiệm**:
  * *Hiệu năng và độ dài ngữ cảnh*: SIGMA đạt hiệu năng tương đương với các mô hình cơ sở LLM tiên tiến nhất (SOTA - state-of-the-art) trong khi duy trì độ dài prompt gần như không đổi.
  * *Khả năng kiểm soát trùng lặp*: Cơ chế EXIT giảm đáng kể tỷ lệ trùng lặp của các đặc trưng được tạo ra từ $37.2\%$ xuống còn $6.8\%$.
  * *Hiệu quả sử dụng đặc trưng*: Đạt hiệu năng ngang ngửa SOTA truyền thống chỉ với trung bình $5.4$ đặc trưng, thể hiện mức tăng đáng kể về hiệu quả khai thác và sử dụng đặc trưng.
* **Keywords (Từ khóa)**: Automated Feature Engineering, LLM, Tabular Machine Learning, AutoML.
