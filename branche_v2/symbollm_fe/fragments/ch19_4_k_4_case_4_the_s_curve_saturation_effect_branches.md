### K.4 Case 4: The S-Curve Saturation Effect of Cabin Position

* Hồi quy ký hiệu (Symbolic regression) nhúng biến $X_3$ (mã định danh cabin / Cabin identifier) vào trong một biểu thức lượng giác lồng nhau (nested trigonometric expression):
  * Biểu thức hồi quy ký hiệu tạo ra là $\text{add}(X_3, X_3) - \cos\left(\text{div}\left(\text{mul}(X_1, -0.149), X_4\right)\right)$, tương đương $2X_3 - \cos\left(\frac{-0.149 X_1}{X_4}\right)$.
  * Biểu thức kết hợp $X_3$ cùng với $X_1$ (`HomePlanet` - hành tinh quê hương) và $X_4$ (`Destination` - hành tinh đích đến) bên trong một phép chia lấy cosin.
* Thách thức về tính diễn giải do hiện tượng vướng víu đa biến (Multi-variable entanglement interpretability challenge):
  * Sự vướng víu giữa nhiều biến số (multi-variable entanglement) khiến việc cô lập và diễn giải phần đóng góp độc lập của riêng biến Cabin ($X_3$) trở nên gần như bất khả thi.
* Mô hình ngôn ngữ lớn (LLM) suy dẫn và kiến tạo đặc trưng tự tương tác $X_3 \cdot (1 - X_3)$:
  * Quá trình suy dẫn được lấy cảm hứng từ việc đơn giản hóa biểu thức $\text{add}(X_3, \text{sub}(X_3, 0.641))$ thành dạng tuyến tính $2X_3 - 0.641$, sau đó được LLM mở rộng thành một số hạng tự tương tác (self-interaction term) $X_3 \cdot (1 - X_3)$ để biểu diễn tính chất phi tuyến (nonlinear representation).
  * Phần chú giải ngữ nghĩa (semantic annotation) của LLM mô tả đây là một tương tác đường cong chữ S (S-curve interaction) có khả năng mô hình hóa các hiệu ứng bão hòa (saturation effects) và các hành vi ngưỡng (threshold behaviors).
* Nền tảng diễn giải ngữ nghĩa gắn liền với miền bài toán (Domain-grounded semantic interpretation):
  * Dạng hàm parabol $X_3(1 - X_3)$ đạt đỉnh cực đại tại $X_3 = 0.5$ và suy giảm dần về $0$ ở cả hai đầu cực trị ($X_3 \to 0$ và $X_3 \to 1$).
  * Hình dạng hàm số nắm bắt thanh lịch giả thuyết rằng các cabin ở khu vực giữa tàu (mid-ship cabins) — tức những vị trí gần nhất với các khoang thoát hiểm (escape pods) cùng các tiện ích và cơ sở vật chất trọng yếu (critical facilities) — mang lại mức độ an toàn cao nhất.
  * Ngược lại, các cabin nằm ở hai đầu con tàu (gần khu vực động cơ ở đuôi tàu hoặc ở mũi tàu / near the engines or the bow) phải chịu mức độ rủi ro tăng cao (elevated risk).
* Bước chuyển dịch căn bản về khả năng diễn giải (Interpretability transition):
  * Cấu trúc mới thay thế biểu thức mờ đục "Cabin lồng trong hàm cosin cùng HomePlanet và Destination" bằng một khái niệm vật lý trực quan và sáng tỏ: "đường cong an toàn hình chữ S của vị trí cabin vật lý" (the S-shaped safety curve of physical cabin position).

#### Bài tập tình huống: Case 4: The S-Curve Saturation Effect of Cabin Position

* **Đề bài**:
  * Phân tích biểu thức lượng giác lồng nhau chứa mã vị trí cabin $X_3$ (`Cabin`) cùng các biến $X_1$ (`HomePlanet`) và $X_4$ (`Destination`) do hồi quy ký hiệu tạo ra trong bài toán Spaceship Titanic. Chỉ ra thách thức diễn giải do hiện tượng vướng víu đa biến (multi-variable entanglement), và trình bày từng bước cách LLM chuyển đổi, đơn giản hóa cấu trúc này thành số hạng tự tương tác dạng parabol $X_3 \cdot (1 - X_3)$ để mô hình hóa hiệu ứng bão hòa đường cong chữ S (S-curve saturation effect) phản ánh mức độ an toàn theo vị trí vật lý của cabin trên tàu.
* **Dữ kiện**:
  * Tập dữ liệu: Spaceship Titanic (bài toán phân loại nhị phân dự đoán hành khách được cứu thoát an toàn hay bị vận chuyển/mất tích trong sự cố không gian).
  * Các biến đầu vào liên quan:
    * $X_3$: Mã định danh vị trí cabin (`Cabin identifier`), được chuẩn hóa theo tọa độ số trong khoảng $[0, 1]$.
    * $X_1$: Hành tinh quê hương (`HomePlanet`), biến phân loại dạng số (categorical label encoding).
    * $X_4$: Hành tinh đích đến (`Destination`), biến phân loại dạng số (categorical label encoding).
  * Biểu thức hồi quy ký hiệu ban đầu (Raw Symbolic Regression expression):
    $$\text{add}(X_3, X_3) - \cos\left(\text{div}\left(\text{mul}(X_1, -0.149), X_4\right)\right)$$
    hay tương đương:
    $$2X_3 - \cos\left(\frac{-0.149 X_1}{X_4}\right)$$
  * Biểu thức trung gian tạo cảm hứng: $\text{add}(X_3, \text{sub}(X_3, 0.641)) = 2X_3 - 0.641$.
  * Biểu thức đặc trưng do LLM suy dẫn: $X_3 \cdot (1 - X_3)$.
* **Quy tắc áp dụng**:
  * Mục 4.1 (*Formula Construction by Symbolic Regression*): Hồi quy ký hiệu tìm kiếm không gian hàm bằng quy hoạch di truyền (GP) với 14 toán tử bảo vệ (bao gồm $\text{add}, \text{sub}, \text{mul}, \text{div}, \cos, \dots$). Thuật toán tập trung tối ưu hóa tương quan số học mà không có tri thức ngữ nghĩa về kiểu biến, thường dẫn đến các cấu trúc toán học vướng víu đa biến và không thể giải thích.
  * Mục 4.2 (*Feature Generation via LLMs*): LLM hoạt động như một bộ tích hợp tất định (deterministic integrator) và bộ lọc ngữ nghĩa có tri thức chuyên ngành. LLM phân tích các biểu thức ký hiệu ứng viên, loại bỏ các thành phần nhiễu không tương thích về mặt vật lý và tái cấu trúc thành đặc trưng có khả năng diễn giải ngữ nghĩa cao.
  * Mục H.1 (*Feature Traceability to Symbolic Regression Rules*): Mọi đặc trưng sinh ra từ LLM duy trì tính truy xuất nguồn gốc (traceability) toán học từ biến cốt lõi do hồi quy ký hiệu đề xuất, chuyển hóa từ biểu thức tuyến tính sang dạng tự tương tác phi tuyến có ý nghĩa thực nghiệm.
* **Lời giải**:
  * Bước 1: Nhận diện hiện tượng vướng víu đa biến và hạn chế của biểu thức hồi quy ký hiệu ban đầu:
    * Biểu thức $\text{add}(X_3, X_3) - \cos\left(\frac{-0.149 X_1}{X_4}\right)$ kết hợp biến vị trí cabin $X_3$ với tỷ số giữa hai mã phân loại hành tinh $X_1$ và $X_4$ bên trong hàm cosin.
    * Sự lồng ghép tùy tiện giữa một biến không gian vật lý ($X_3$) với các mã phân loại hành trình ($X_1, X_4$) thông qua hàm lượng giác tuần hoàn tạo ra hiện tượng vướng víu đa biến (multi-variable entanglement).
    * Hậu quả là người nghiên cứu không thể cô lập hay diễn giải được tác động biên (marginal contribution) độc lập của riêng vị trí cabin đối với nguy cơ gặp nạn của hành khách.
  * Bước 2: Quá trình tinh chỉnh và suy dẫn số hạng tự tương tác của LLM:
    * LLM nhận diện cấu trúc tuyến tính của biến cabin từ nhánh biểu thức $\text{add}(X_3, \text{sub}(X_3, 0.641))$, vốn được rút gọn trực tiếp thành $2X_3 - 0.641$.
    * Thay vì giữ nguyên dạng đơn thức tuyến tính hoặc biểu thức lượng giác nhiễu với các biến hành tinh, LLM mở rộng $X_3$ thành số hạng tự tương tác phi tuyến (self-interaction term): $X_3 \cdot (1 - X_3)$.
    * Về mặt toán học, hàm số $f(X_3) = X_3(1 - X_3) = X_3 - X_3^2$ là một hàm bậc hai đối xứng (parabolic form):
      * Đạt giá trị cực đại tại trung tâm: khi $X_3 = 0.5$, ta có $f(0.5) = 0.5 \cdot (1 - 0.5) = 0.25$.
      * Suy giảm dần về $0$ tại hai biên: $\lim_{X_3 \to 0} f(X_3) = 0$ và $\lim_{X_3 \to 1} f(X_3) = 0$.
  * Bước 3: Diễn giải ngữ nghĩa miền vật lý và mô hình hóa đường cong an toàn chữ S:
    * Trong cấu trúc không gian của con tàu vũ trụ, tọa độ cabin $X_3 \in [0, 1]$ biểu diễn vị trí vật lý từ đầu này đến đầu kia của con tàu (từ mũi tàu đến đuôi tàu).
    * Các cabin ở khu vực giữa tàu ($X_3 \approx 0.5$, mid-ship) nằm ở vị trí thuận lợi nhất: gần nhất với các khoang thoát hiểm (escape pods) và các cơ sở vận hành huyết mạch (critical facilities), do đó mang lại mức độ an toàn cao nhất khi sự cố xảy ra.
    * Ngược lại, các cabin nằm ở hai đầu mút của con tàu (khu vực mũi tàu hoặc khu vực đuôi tàu gần động cơ phản lực) phải chịu mức độ rủi ro tăng cao do khoảng cách di tản xa và nguy cơ va chạm/cháy nổ lớn.
    * Chú giải của LLM xác lập đặc trưng này như một hàm bão hòa dạng đường cong chữ S / vòm an toàn (S-curve saturation / threshold behavior), phản ánh trung thực quy luật vật lý của miền ứng dụng.
* **Kết quả**:
  * Biểu thức đặc trưng hoàn chỉnh: $X_3 \cdot (1 - X_3)$.
  * Tên gọi ngữ nghĩa: Hiệu ứng bão hòa đường cong chữ S của vị trí Cabin (The S-Curve Saturation Effect of Cabin Position).
  * Bước chuyển biến diễn giải: Chuyển hóa từ biểu thức mờ đục "Cabin lồng trong hàm cosin cùng HomePlanet và Destination" thành "đường cong an toàn hình chữ S của vị trí cabin vật lý".
* **Kiểm tra lại**:
  * Kiểm tra tính chất cực trị: Lấy đạo hàm bậc nhất $f'(X_3) = 1 - 2X_3 = 0 \iff X_3 = 0.5$; đạo hàm bậc hai $f''(X_3) = -2 < 0$, khẳng định hàm số đạt cực đại toàn cục tại $X_3 = 0.5$.
  * Kiểm tra tính chất biên: $f(0) = 0(1 - 0) = 0$ và $f(1) = 1(1 - 1) = 0$, xác nhận tính đối xứng và suy giảm đều về hai đầu con tàu.
  * Kiểm tra tính khả thi và độ phức tạp: Biểu thức đơn giản hóa tối đa, xác định trên toàn bộ miền giá trị của $X_3$, loại bỏ hoàn toàn nguy cơ chia cho 0 hoặc điểm kỳ dị của hàm cosin/div, tính toán với độ phức tạp $O(1)$.
  * Kiểm tra tính nhất quán với tài liệu nguồn: Nội dung bám sát nguyên văn Phần K.4 về nguồn gốc biểu thức $\text{add}(X_3, X_3) - \cos(\dots)$, cảm hứng từ $2X_3 - 0.641$, và diễn giải vật lý về mid-ship cabins và escape pods.
