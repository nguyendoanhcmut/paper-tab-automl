### K.1 Case 1: The Abrupt Age Threshold Effect

* Biểu thức hồi quy ký hiệu thô được phát hiện trên tập dữ liệu Titanic:
  * Hồi quy ký hiệu (symbolic regression) đã khám phá ra công thức $\tan(-0.607 - \tan(X_5))$, trong đó $X_5$ biểu diễn độ tuổi của hành khách (passenger age).
* Thách thức về tính diễn giải của cấu trúc lượng giác lồng nhau:
  * Dưới góc độ toán học thuần túy, cấu trúc hợp lồng nhau $\tan(\tan(X_5))$ hoàn toàn mờ đục (deeply opaque).
  * Độc giả hoàn toàn có cơ sở chính đáng để hoài nghi: tại sao hàm tang của hàm tang của độ tuổi lại mang tín hiệu dự đoán (predictive signal)?
  * Biểu thức này thoạt nhìn mang đặc trưng điển hình của một tạo tác quá khớp (overfitted artifact) vốn thường khiến quy hoạch di truyền (genetic programming) bị chỉ trích.
* LLM cô lập thành phần hạt nhân và chú giải ngữ nghĩa miền:
  * LLM đã tách biệt và cô lập thành phần cốt lõi $\tan(X_5)$, đồng thời gán cho nó ngữ nghĩa chuyên ngành (domain semantics).
  * Phần chú giải (annotation) của LLM ghi nhận rằng $\tan(X_5)$ xuất hiện lặp đi lặp lại (recurrently appears) qua nhiều quy tắc đạt độ chính xác cao (multiple high-accuracy rules), khẳng định tầm quan trọng thực chất của nó trong việc nắm bắt các xu hướng phi tuyến (nonlinear trends).
  * Cơ sở lý luận (rationale) làm rõ thêm rằng hàm tang ($\tan$) có khả năng mô hình hóa các biến đổi tuần hoàn và các biến đổi dốc đứng (periodic and steep changes) trong mối quan hệ giữa độ tuổi và biến mục tiêu (target variable).
* Diễn giải ngữ nghĩa dựa trên tri thức miền trong bối cảnh thảm họa:
  * Trong bối cảnh thảm họa tàu không gian / tàu Titanic (spaceship disaster), tác động của độ tuổi lên khả năng sống sót (survival) hoàn toàn không mang tính tuyến tính (far from linear).
  * Trẻ vị thành niên (minors) có thể được ưu tiên cứu hộ (rescue priority), trong khi người cao tuổi (the elderly) có thể gặp bất lợi về khả năng di chuyển linh hoạt (mobility disadvantages).
  * Tồn tại một vùng chuyển tiếp sắc nét (sharp transition zone) ở độ tuổi trung niên (middle age), nơi xác suất sống sót thay đổi một cách đột ngột và kịch tính (survival probability changes dramatically).
  * Về mặt toán học, hàm tang ($\tan$) nắm bắt chính xác loại hành vi vượt ngưỡng (threshold-crossing behavior) này; đây chính là sự phản chiếu số học (numerical projection) của nguyên tắc cứu hộ "phụ nữ và trẻ em trước" (“women and children first” rescue doctrine) vào không gian đặc trưng (feature space).
* Bước nhảy vọt về tính diễn giải (leap in interpretability):
  * Tạo nên bước chuyển biến chất lượng từ "một hộp đen lượng giác lồng nhau" (“a nested trigonometric black box”) trở thành "hiệu ứng biến đổi dốc đứng của độ tuổi theo mức độ ưu tiên cứu hộ" (“the rescue-priority steep-change effect of age”).

#### Bài tập tình huống: Case 1: The Abrupt Age Threshold Effect

* **Đề bài**:
  * Phân tích quá trình chuyển hóa biểu thức toán học mờ đục $\tan(-0.607 - \tan(X_5))$ (với $X_5$ biểu diễn độ tuổi hành khách) thành đặc trưng có khả năng giải thích ngữ nghĩa trong Case 1 (The Abrupt Age Threshold Effect) theo khuôn khổ SymboLLM-FE:
    1. Xác định công thức thô do hồi quy ký hiệu tạo ra và làm rõ thách thức diễn giải khiến biểu thức dễ bị coi là tạo tác quá khớp.
    2. Giải thích cơ chế LLM cô lập thành phần cốt lõi dựa trên các quy tắc hồi quy ký hiệu có độ chính xác cao.
    3. Phân tích đặc tính toán học của hàm $\tan$ và làm sáng tỏ ý nghĩa vật lý - xã hội của đặc trưng trong việc mô hình hóa vùng chuyển tiếp ưu tiên cứu hộ theo độ tuổi.
* **Dữ kiện**:
  * Tập dữ liệu nghiên cứu: Spaceship Titanic / Titanic dataset.
  * Biểu thức hồi quy ký hiệu thô: $\tan(-0.607 - \tan(X_5))$.
  * Biến đầu vào: $X_5$ biểu diễn độ tuổi hành khách ($\text{Age}$).
  * Nghi vấn ban đầu: Phép lồng lượng giác $\tan(\tan(X_5))$ mờ đục, mang đặc trưng của tạo tác quá khớp (overfitted artifact) trong quy hoạch di truyền.
  * Tín hiệu thực nghiệm từ quy trình SR: Thành phần $\tan(X_5)$ xuất hiện lặp đi lặp lại trong nhiều quy tắc đạt độ chính xác cao (multiple high-accuracy rules).
  * Bối cảnh thực tế: Thảm họa cứu hộ khẩn cấp với sự phân tầng sống sót phi tuyến theo độ tuổi (trẻ em được ưu tiên cứu hộ, người già hạn chế vận động, trung niên là vùng chuyển tiếp).
* **Quy tắc áp dụng**:
  * *Mục 4.1 Formula Construction by Symbolic Regression*: Tìm kiếm các công thức toán học giải tích tối ưu thông qua quy hoạch di truyền sử dụng tập toán tử bảo vệ (protected operators), bao gồm toán tử $\tan$.
  * *Mục 4.2 Feature Generation via LLMs*: LLM hoạt động như bộ tích hợp tất định (deterministic integrator), loại bỏ cấu trúc lồng mờ đục, cô lập thành phần hạt nhân và tích hợp tri thức miền để chú giải ngữ nghĩa.
  * *Mục H.1 Feature Traceability to Symbolic Regression Rules*: Đảm bảo đặc trưng sinh ra có thể truy vết nguồn gốc 100% từ các quy tắc hồi quy ký hiệu hợp lệ, loại trừ nguy cơ sinh ảo giác (hallucination).
  * *Đặc tính toán học của hàm $\tan$*: Khả năng mô hình hóa các thay đổi dốc đứng (steep changes) và hành vi vượt ngưỡng cục bộ (threshold-crossing behavior) tại các điểm ranh giới.
  * *Nguyên lý cứu hộ trong thảm họa*: Học thuyết "phụ nữ và trẻ em trước" (“women and children first” rescue doctrine) tạo ra mối liên hệ phi tuyến mạnh giữa tuổi tác và xác suất sống sót.
* **Lời giải**:
  * *Bước 1: Phân tích cấu trúc biểu thức thô và thách thức diễn giải*:
    * Biểu thức $\tan(-0.607 - \tan(X_5))$ chứa phép hợp lồng lượng giác $\tan(\tan(X_5))$.
    * Dưới góc nhìn toán học thuần túy, việc lấy tang hai lần của tuổi không mang lại bất kỳ ý nghĩa trực quan nào; biểu thức không giải thích được cơ chế dự đoán và dễ bị đánh giá là một tạo tác quá khớp do quy hoạch di truyền sinh ra khi tối ưu số học thuần túy.
  * *Bước 2: Cô lập thành phần cốt lõi nhờ quan sát thực nghiệm qua LLM*:
    * LLM phân tích các quy tắc sinh ra và nhận diện thành phần $\tan(X_5)$ xuất hiện lặp đi lặp lại qua nhiều quy tắc đạt độ chính xác cao.
    * LLM loại bỏ lớp lồng toán học dư thừa và hằng số dịch chuyển $(-0.607)$, cô lập $\tan(X_5)$ thành thành phần hạt nhân chịu trách nhiệm mang tín hiệu dự đoán phi tuyến thực chất.
  * *Bước 3: Phân tích cơ sở toán học của hàm tang ($\tan$)*:
    * Hàm $\tan(x)$ có đạo hàm $\tan'(x) = 1 + \tan^2(x)$, thể hiện tốc độ biến thiên tăng vọt và độ dốc cực lớn khi tiến gần các điểm kỳ dị.
    * Nhờ đặc tính này, hàm tang là công cụ toán học lý tưởng để mô hình hóa các bước nhảy vọt đột ngột (steep changes) và các trạng thái chuyển pha sắc nét, vượt trội hơn so với các hàm tuyến tính hay đa thức bậc thấp.
  * *Bước 4: Ánh xạ tri thức miền và giải thích hiện tượng vượt ngưỡng cứu hộ*:
    * Trong thảm họa, mối quan hệ giữa tuổi và khả năng sống sót phân hóa thành ba nhóm rõ rệt:
      * Nhóm trẻ em / vị thành niên ($\text{minors}$): Nhận được sự bảo vệ và mức ưu tiên cứu hộ cao nhất.
      * Nhóm người cao tuổi ($\text{elderly}$): Gặp bất lợi về khả năng di chuyển linh hoạt trong môi trường nguy hiểm.
      * Vùng chuyển tiếp sắc nét ở tuổi trung niên ($\text{sharp transition zone in middle age}$): Ranh giới nơi xác suất sống sót giảm mạnh và đột ngột.
    * Do đó, $\tan(X_5)$ chính là phép chiếu số học (numerical projection) của nguyên tắc "phụ nữ và trẻ em trước" vào không gian đặc trưng, phản ánh chính xác hành vi vượt ngưỡng tuổi.
  * *Bước 5: Xác lập bước nhảy vọt về tính diễn giải (Interpretability leap)*:
    * Biến đổi hoàn toàn nhận thức về đặc trưng: từ "hộp đen lượng giác lồng nhau" (“a nested trigonometric black box”) thành "hiệu ứng biến đổi dốc đứng của độ tuổi theo mức độ ưu tiên cứu hộ" (“the rescue-priority steep-change effect of age”).
* **Kết quả**:
  * Thành phần đặc trưng được cô lập và giải thích: $\tan(X_5)$ (hàm tang biểu diễn độ dốc vượt ngưỡng tuổi).
  * Tên gọi ngữ nghĩa: Hiệu ứng ngưỡng tuổi đột ngột (The Abrupt Age Threshold Effect).
  * Bước chuyển đổi định tính: Chuyển từ công thức mờ đục bị nghi ngờ quá khớp thành tri thức đặc trưng có căn cứ khoa học và cơ sở nhân học vững chắc.
* **Kiểm tra lại**:
  * Tính hợp lệ toán học: Hàm $\tan(X_5)$ mô hình hóa chính xác tính phi tuyến cục bộ và hành vi dốc đứng tại ngưỡng chuyển tiếp.
  * Khả năng truy xuất nguồn gốc: Đặc trưng bắt nguồn trực tiếp từ các quy tắc hồi quy ký hiệu có độ chính xác cao, loại bỏ hoàn toàn ảo giác.
  * Tính nhất quán với văn bản gốc: Khớp 100% với biểu thức $\tan(-0.607 - \tan(X_5))$, biến $X_5$ ($\text{Age}$), học thuyết "women and children first" và bước nhảy vọt diễn giải được trình bày trong Mục K.1 của bài báo.
