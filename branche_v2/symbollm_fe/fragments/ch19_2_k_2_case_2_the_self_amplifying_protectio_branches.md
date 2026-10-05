### K.2 Case 2: The Self-Amplifying Protection of CryoSleep

* Biểu thức phức hợp do hồi quy ký hiệu tạo ra (compound symbolic regression expression):
  * Hồi quy ký hiệu (symbolic regression) sinh ra công thức phức hợp $\text{add}(X_2, X_2) - \cos\left(\text{mul}(X_5, \text{mul}(X_5, X_2)) - \text{div}(0.974, X_3)\right)$, rút gọn thành $2X_2 - \cos\left(X_5^2 \cdot X_2 - \frac{0.974}{X_3}\right)$.
  * Biến $X_2$ là biến chỉ báo trạng thái ngủ đông (CryoSleep indicator), $X_5$ biểu diễn độ tuổi (Age), và $X_3$ là một hiệp biến trong tập dữ liệu Spaceship Titanic.
* Thách thức về tính diễn giải của biểu thức ký hiệu thô:
  * Biến $X_2$ xuất hiện lặp đi lặp lại nhiều lần trong biểu thức: được nhân đôi ($2X_2$), nhân với bình phương độ tuổi ($X_5^2 \cdot X_2$), và lồng bên trong hàm lượng giác $\cos$.
  * Với bản chất là một tập hợp gộp cơ học các phép toán số học (aggregation of arithmetic operations), biểu thức hoàn toàn không cung cấp bất kỳ trực giác nào giải thích vì sao $2X_2$ hay $X_5^2 \cdot X_2$ lại có ý nghĩa quan trọng đối với tác vụ phân loại (classification).
* LLM bóc tách số hạng tự tương tác và cấu trúc khuếch đại:
  * LLM trích xuất số hạng tự tương tác (self-interaction term) $X_2 \cdot \tan(X_2)$.
  * LLM ghi nhận sự hiện diện lặp lại của cấu trúc này trong nhiều quy tắc hồi quy ký hiệu liên quan đến $\text{sub}(\tan(X_2), \cos(\dots))$, đồng thời diễn giải nó như một hiệu ứng khuếch đại bậc hai (quadratic amplification effect).
* Diễn giải ngữ nghĩa dựa trên bối cảnh miền thực tế:
  * Ý nghĩa trong thế giới thực trở nên rõ ràng khi nhận diện CryoSleep ($X_2$) là một biến nhị phân (binary variable): hành khách ở trạng thái ngủ đông (cryogenic stasis) trải qua toàn bộ hành trình cách ly trong các kén bảo vệ (protected pods), hoàn toàn được che chắn khỏi sự phơi nhiễm trực tiếp với các sự cố thảm họa (disaster events).
  * Cấu trúc toán học $X_2 \cdot \tan(X_2)$ tạo ra một đặc trưng khuếch đại theo cấp số nhân (multiplicatively amplified) khi $X_2 = 1$; trạng thái ngủ đông không chỉ có ý nghĩa tự thân mà tầm quan trọng của nó còn được nhân lên gấp bội thông qua các tương tác với các hiệp biến khác như Age ($X_5$).
  * Biểu thức phản ánh chính xác thực tế vật lý: kén ngủ đông đóng vai trò như một màng chắn bảo vệ (protective barrier) có tác động mang tính nhân (multiplicative) thay vì tính cộng (additive).
  * Bước chuyển biến chất lượng về khả năng diễn giải: Chuyển đổi từ "sự xếp chồng cơ học của các số hạng bình phương" (mechanical stacking of squared terms) sang "hệ số nhân bảo vệ dạng nhân của trạng thái ngủ đông" (the multiplicative protection multiplier of cryogenic stasis).

#### Bài tập tình huống: The Self-Amplifying Protection of CryoSleep

* **Đề bài**:
  * Phân tích quá trình chuyển hóa biểu thức toán học thô thành đặc trưng có khả năng diễn giải ngữ nghĩa trong Case 2 (The Self-Amplifying Protection of CryoSleep) trên tập dữ liệu Spaceship Titanic theo khuôn khổ SymboLLM-FE:
    1. Xác định cấu trúc toán học của biểu thức thô do hồi quy ký hiệu sinh ra và phân tích nguyên nhân biểu thức gặp phải rào cản diễn giải hộp đen.
    2. Xác định thành phần đặc trưng tự tương tác do LLM trích xuất và cơ chế tác động của nó.
    3. Lý giải ý nghĩa vật lý và ngữ nghĩa miền thực tế của đặc trưng mới khi áp dụng cho biến nhị phân CryoSleep.
* **Dữ kiện**:
  * Tập dữ liệu nghiên cứu: Spaceship Titanic.
  * Biểu thức hồi quy ký hiệu thô: $\text{add}(X_2, X_2) - \cos\left(\text{mul}(X_5, \text{mul}(X_5, X_2)) - \text{div}(0.974, X_3)\right)$, tương đương $2X_2 - \cos\left(X_5^2 \cdot X_2 - \frac{0.974}{X_3}\right)$.
  * Ý nghĩa các biến đầu vào:
    * $X_2$: Biến chỉ báo trạng thái ngủ đông ($\text{CryoSleep}$ indicator), nhận giá trị nhị phân $X_2 \in \{0, 1\}$.
    * $X_5$: Độ tuổi hành khách ($\text{Age}$).
    * $X_3$: Hiệp biến trong bảng dữ liệu.
  * Nhiều quy tắc hồi quy ký hiệu có độ chính xác cao chứa mẫu biểu thức $\text{sub}(\tan(X_2), \cos(\dots))$.
* **Quy tắc áp dụng**:
  * *Mục 4.1 Formula Construction by Symbolic Regression*: Sử dụng quy hoạch di truyền để tìm kiếm các công thức toán học giải tích tối ưu gắn với nhãn mục tiêu.
  * *Mục 4.2 Feature Generation via LLMs*: LLM đóng vai trò bộ tích hợp tất định (deterministic integrator), loại bỏ các phép toán ghép nối cơ học dư thừa và tích hợp tri thức tiên nghiệm về miền dữ liệu bảng để trích xuất đặc trưng cốt lõi.
  * *Mục H.1 Feature Traceability to Symbolic Regression Rules*: Đảm bảo khả năng truy xuất nguồn gốc đặc trưng trực tiếp từ các quy tắc hồi quy ký hiệu đã được xác thực thống kê, loại trừ triệt để nguy cơ sinh ảo giác (hallucination).
  * *Nguyên lý miền thực tế (Physical Domain Reality)*: Trạng thái ngủ đông trong kén bảo vệ tạo ra rào cản cách ly vật lý, khiến tác động bảo vệ mang bản chất nhân (multiplicative) thay vì cộng (additive).
* **Lời giải**:
  * *Bước 1: Phân tích thách thức về tính diễn giải của công thức thô*:
    * Trong biểu thức $2X_2 - \cos\left(X_5^2 \cdot X_2 - \frac{0.974}{X_3}\right)$, biến $X_2$ xuất hiện rải rác: được nhân đôi ($2X_2$), nhân với bình phương độ tuổi ($X_5^2 \cdot X_2$), và đặt bên trong hàm lượng giác $\cos(\dots)$.
    * Biểu thức này mang tính chất ghép nối số học cơ học (mechanical stacking of arithmetic operations); nó không giải thích được lý do thực tế vì sao $2X_2$ hay $X_5^2 \cdot X_2$ lại có giá trị phân biệt đối với xác suất vận chuyển của hành khách.
  * *Bước 2: Bóc tách cấu trúc đặc trưng tự tương tác qua LLM*:
    * Dựa trên các quy tắc hồi quy ký hiệu lặp lại chứa $\text{sub}(\tan(X_2), \cos(\dots))$, LLM cô lập số hạng tự tương tác (self-interaction term):
      $$f(X_2) = X_2 \cdot \tan(X_2)$$
    * LLM xác định đây là cơ chế khuếch đại bậc hai (quadratic amplification effect) phản ánh tương tác phi tuyến thực sự.
  * *Bước 3: Gắn ngữ nghĩa miền thực tế và phân tích hành vi toán học*:
    * Xét bản chất nhị phân $X_2 \in \{0, 1\}$:
      * Khi $X_2 = 0$ (không ngủ đông): $X_2 \cdot \tan(X_2) = 0 \cdot \tan(0) = 0$; hành khách đối mặt trực tiếp với môi trường nguy hiểm ngoài kén.
      * Khi $X_2 = 1$ (ở trạng thái ngủ đông): $X_2 \cdot \tan(X_2) = 1 \cdot \tan(1) \approx 1.5574$; đặc trưng được kích hoạt và khuếch đại phi tuyến theo cấp số nhân ($> 1$).
    * Trong bối cảnh thảm họa không gian, kén ngủ đông cách ly hoàn toàn hành khách khỏi rủi ro, đóng vai trò như một màng chắn bảo vệ có hiệu ứng mang tính nhân (multiplicative barrier) hơn là cộng (additive), đồng thời điều chỉnh tác động của các hiệp biến khác như Age ($X_5$).
* **Kết quả**:
  * Đặc trưng trích xuất: $X_2 \cdot \tan(X_2)$ (số hạng tự tương tác khuếch đại của $\text{CryoSleep}$).
  * Bước chuyển đổi định tính: Chuyển từ "sự xếp chồng cơ học của các số hạng bình phương" (mechanical stacking of squared terms) sang "hệ số nhân bảo vệ dạng nhân của trạng thái ngủ đông" (the multiplicative protection multiplier of cryogenic stasis).
  * Giá trị thực tiễn: Cung cấp đặc trưng toán học sáng tỏ, vừa nâng cao năng lực phân loại vừa mang tính diễn giải rõ ràng dựa trên cơ sở vật lý.
* **Kiểm tra lại**:
  * Tính hợp lệ toán học: Với $X_2 \in \{0, 1\}$, hàm $\tan(X_2)$ hoàn toàn xác định tại $0$ và $1$ radian ($1 \text{ rad} \approx 57.3^\circ < 90^\circ = \frac{\pi}{2}$), không gặp điểm kỳ dị.
  * Khả năng truy xuất nguồn gốc: Đặc trưng bắt nguồn trực tiếp từ biểu thức của quy hoạch di truyền $\text{sub}(\tan(X_2), \cos(\dots))$, tuân thủ cơ chế tích hợp tất định và không bị ảo giác.
  * Phù hợp với trực giác bài toán: Phản ánh trung thực thuộc tính quan trọng bậc nhất của tập dữ liệu Spaceship Titanic trong việc dự đoán tỷ lệ an toàn của hành khách.
