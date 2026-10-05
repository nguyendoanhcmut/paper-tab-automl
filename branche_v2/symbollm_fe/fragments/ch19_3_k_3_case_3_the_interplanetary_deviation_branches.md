### K.3 Case 3: The Interplanetary Deviation Risk Index

* Hồi quy ký hiệu (Symbolic regression) thăm dò các tương tác giữa biến $X_1$ (`HomePlanet` - hành tinh quê hương) và $X_4$ (`Destination` - hành tinh đích đến) thông qua các số hạng nhân (multiplicative terms) như $\text{mul}(X_4, X_1)$:
  * Phép nhân hai mã phân loại (categorical codes), ví dụ: $\text{“Earth”} \times \text{“TRAPPIST-1e”} = 3$, tạo ra một sản phẩm giả số học (numerical artifact) hoàn toàn không có ý nghĩa vật lý (devoid of physical meaning).
  * Người đọc không thể diễn giải được tích số của hai mã hành tinh được mã hóa nhãn (label-encoded product) thực sự đại diện cho điều gì trong thế giới thực.
* Mô hình ngôn ngữ lớn (LLM) tạo ra biến đặc trưng $X_4 - X_1$, là một hiệu có hướng (directed difference) nắm bắt mối quan hệ định hướng giữa điểm xuất phát và điểm đến:
  * Phần chú giải (annotation) của LLM định hình đặc trưng này phản ánh mức độ mã hóa đích đến vượt qua mã hóa hành tinh quê hương, điều có ý nghĩa sống còn khi các biến có tác động trái chiều (opposing effects) lên phân loại nhãn mục tiêu.
* Ý nghĩa vật lý trong bối cảnh hành trình tàu không gian (Spaceship scenario):
  * Khi $\text{Destination} \neq \text{HomePlanet}$, hành khách bước vào một hành trình du hành liên hành tinh (interplanetary journey) với thời gian di chuyển dài hơn, rủi ro môi trường chưa quen thuộc và hỗ trợ hậu cần phức tạp hơn.
  * Độ lớn của $X_4 - X_1$ mã hóa khoảng cách hành khách đã rời xa hành tinh quê hương; độ lệch càng lớn ngụ ý các đích đến càng xa xôi với xác suất sống sót (survival probabilities) bị thay đổi mang tính hệ thống.
  * Quan trọng nhất, hiệu số bảo toàn tính định hướng (preserves directionality): phân biệt rõ giữa việc di chuyển hướng tới một điểm đến an toàn hơn so với một điểm đến nguy hiểm hơn, một đặc tính hoàn toàn vắng mặt trong số hạng nhân $\text{mul}(X_4, X_1)$.
* Bước tiến về khả năng diễn giải (interpretability):
  * Khả năng diễn giải chuyển biến từ "tích số của các mã phân loại" (a product of categorical codes) thành "độ lệch rủi ro tương đối của hành trình du hành liên hành tinh" (the relative risk deviation of interplanetary travel).

#### Bài tập tình huống: Case 3: The Interplanetary Deviation Risk Index

* **Đề bài**:
  * Phân tích biểu thức tương tác giữa hai biến phân loại $X_1$ (`HomePlanet`) và $X_4$ (`Destination`) do hồi quy ký hiệu tạo ra trong bài toán Spaceship Titanic. Chỉ ra lý do vì sao biểu thức nhân $\text{mul}(X_4, X_1)$ không thể diễn giải được, và giải thích cơ chế LLM chuyển đổi công thức này thành hiệu có hướng $X_4 - X_1$ để thiết lập chỉ số rủi ro du hành liên hành tinh.
* **Dữ kiện**:
  * Tập dữ liệu: Spaceship Titanic (bài toán phân loại nhị phân dự đoán hành khách sống sót/bị vận chuyển trong sự cố không gian).
  * Biến đầu vào:
    * $X_1$: Hành tinh quê hương (`HomePlanet`), mã hóa dạng phân loại số (categorical label encoding).
    * $X_4$: Hành tinh đích đến (`Destination`), mã hóa dạng phân loại số (categorical label encoding).
  * Ví dụ mã hóa trong nguồn: $\text{“Earth”} \times \text{“TRAPPIST-1e”} = 3$.
  * Biểu thức gốc từ hồi quy ký hiệu (Symbolic Regression): $\text{mul}(X_4, X_1)$.
* **Quy tắc áp dụng**:
  * Mục 4.1 (*Formula Construction by Symbolic Regression*): Hồi quy ký hiệu tìm kiếm không gian hàm bằng quy hoạch di truyền sử dụng các toán tử bảo vệ (protected operators), bao gồm toán tử nhân $\text{mul}$, nhưng chỉ tối ưu hóa tương quan số học mà không có tri thức ngữ nghĩa về kiểu biến.
  * Mục 4.2 (*Feature Generation via LLMs*): LLM hoạt động như bộ tích hợp tất định (deterministic integrator), tiếp nhận biểu thức ký hiệu ứng viên cùng ngữ cảnh ngữ nghĩa bảng dữ liệu để tái cấu trúc thành đặc trưng có khả năng diễn giải vật lý cao.
  * Mục H.1 (*Feature Traceability to Symbolic Regression Rules*): Đặc trưng sinh ra từ LLM duy trì tính truy xuất nguồn gốc toán học tới cặp biến tương tác do hồi quy ký hiệu đề xuất, đồng thời loại bỏ các sản phẩm giả số học vô nghĩa (numerical artifacts).
* **Lời giải**:
  * Bước 1: Nhận diện hạn chế và sản phẩm giả số học của công thức nhân $\text{mul}(X_4, X_1)$:
    * Phép nhân hai số nguyên mã hóa nhãn danh mục (ví dụ mã nhãn của Trái Đất nhân với mã nhãn của TRAPPIST-1e bằng 3) hoàn toàn không có cơ sở đại diện cho bất kỳ hiện tượng vật lý nào.
    * Phép nhân có tính chất giao hoán ($\text{mul}(X_4, X_1) = \text{mul}(X_1, X_4)$), khiến biểu thức hoàn toàn mất đi tính định hướng của lộ trình di chuyển (không phân biệt được giữa việc đi từ A đến B hay từ B đến A).
  * Bước 2: Tái cấu trúc thành hiệu có hướng thông qua LLM:
    * LLM đề xuất phép trừ $X_4 - X_1$ nhằm đo lường mức độ chênh lệch có hướng giữa mã hóa đích đến và hành tinh gốc.
    * Phép trừ này cho phép mô hình nắm bắt ảnh hưởng khi hai biến $X_1$ và $X_4$ có tác động trái chiều (opposing effects) lên xác suất mục tiêu.
  * Bước 3: Diễn giải ngữ nghĩa miền vật lý (Domain-grounded semantic interpretation):
    * Khi $\text{Destination} \neq \text{HomePlanet}$, hành khách rời bỏ thế giới quê hương để du hành liên hành tinh, gắn liền với thời gian bay dài hơn, hiểm họa không gian mới và yêu cầu hậu cần phức tạp.
    * Độ lớn $|X_4 - X_1|$ phản ánh khoảng cách độ lệch rời xa quê hương, tương ứng với sự dịch chuyển có hệ thống của xác suất sống sót.
    * Dấu của $X_4 - X_1$ bảo toàn tính định hướng (directionality), phân biệt rõ chiều di chuyển hướng tới một điểm đến an toàn hơn hay nguy hiểm hơn.
* **Kết quả**:
  * Biểu thức đặc trưng hoàn chỉnh: $X_4 - X_1$.
  * Tên gọi ngữ nghĩa: Chỉ số độ lệch rủi ro du hành liên hành tinh (The Interplanetary Deviation Risk Index).
  * Bước nhảy vọt về khả năng diễn giải: Chuyển hóa từ "tích số của các mã phân loại" thành "độ lệch rủi ro tương đối của hành trình du hành liên hành tinh".
* **Kiểm tra lại**:
  * Kiểm tra tính bảo toàn định hướng: $X_4 - X_1 \neq X_1 - X_4$, đảm bảo tính bất đối xứng giữa chiều đi và chiều về.
  * Kiểm tra tính khả thi tính toán: Biểu thức hợp lệ, xác định trên mọi mẫu dữ liệu có mã hóa hợp lệ của $X_1$ và $X_4$.
  * Kiểm tra tính nhất quán với mã nguồn và ngữ nghĩa bài báo: Khớp hoàn toàn với mô tả trong Phần K.3 về việc chuyển từ $\text{mul}(X_4, X_1)$ sang $X_4 - X_1$.
