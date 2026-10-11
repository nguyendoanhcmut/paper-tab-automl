### K.1 Case 1: The Abrupt Age Threshold Effect

* **Công thức hồi quy ký hiệu thô và bối cảnh thực nghiệm (Raw symbolic regression formula & empirical context)**:
  * Trên tập dữ liệu Titanic (*Titanic dataset* - trong bối cảnh thảm họa tàu vũ trụ Spaceship Titanic), thuật toán hồi quy ký hiệu (*symbolic regression - SR*) đã phát hiện ra công thức:
    $$\tan(-0.607 - \tan(X_5))$$
  * Biến số đầu vào: $X_5$ đại diện cho độ tuổi của hành khách (*passenger age*).
* **Thách thức về khả năng diễn giải và nghi vấn tạo phẩm quá khớp (Interpretability challenge & overfitting artifact suspicion)**:
  * **Tính tối nghĩa về mặt toán học (*Mathematical opacity*)**: Dưới góc nhìn thuần túy toán học, phép hợp lồng nhau của hàm lượng giác $\tan(\tan(X_5))$ là một cấu trúc cực kỳ mờ đục và khó hiểu (*deeply opaque*).
  * **Hoài nghi về tín hiệu dự báo (*Predictive signal skepticism*)**: Người đọc hoàn toàn có lý do chính đáng để đặt câu hỏi: tại sao hàm tang của tang độ tuổi lại có thể chứa đựng tín hiệu dự báo (*carry predictive signal*) có ý nghĩa?
  * **Nguy cơ tạo phẩm quá khớp (*Overfitted artifact*)**: Biểu thức này mang dáng dấp của một tạo phẩm quá khớp (*overfitted artifact*) điển hình mà các phương pháp lập trình di truyền (*genetic programming - GP*) thường bị chỉ trích là dễ sinh ra.
* **Đặc trưng cốt lõi do LLM bóc tách và chú giải ngữ nghĩa (LLM-isolated core feature & domain semantics annotation)**:
  * **Cô lập thành phần cốt lõi (*Core component isolation*)**: Khác với công thức ban đầu phức tạp, mô hình ngôn ngữ lớn (*LLM*) đã bóc tách thành phần hạt nhân:
    $$\tan(X_5)$$
    đồng thời gán ngữ nghĩa miền tri thức (*domain semantics*) cho thành phần này.
  * **Sự xuất hiện lặp lại trong các quy tắc hiệu năng cao (*Recurrence across high-accuracy rules*)**: Lời chú giải (*annotation*) của LLM chỉ rõ rằng $\tan(X_5)$ xuất hiện lặp đi lặp lại một cách có hệ thống trong nhiều quy tắc có độ chính xác cao (*high-accuracy rules*), phản ánh tầm quan trọng thực chất (*genuine importance*) của đặc trưng trong việc nắm bắt các xu hướng phi tuyến tính (*nonlinear trends*).
  * **Cơ sở toán học của hàm tang (*Mathematical rationale of the tangent function*)**: Lời lý giải chỉ rõ rằng hàm tang ($\tan$) có khả năng mô hình hóa các biến đổi có tính chu kỳ và dốc đứng / biến đổi đột ngột (*periodic and steep changes*) trong mối quan hệ giữa độ tuổi hành khách ($X_5$) và biến mục tiêu sống sót (*target variable*).
* **Diễn giải ngữ nghĩa bám sát miền tri thức cứu hộ (Domain-grounded physical semantics & rescue doctrine)**:
  * **Quy luật phi tuyến của độ tuổi trong thảm họa tàu vũ trụ (*Nonlinear age dynamics in spaceship disaster*)**: Trong bối cảnh thảm họa tàu vũ trụ, tác động của độ tuổi lên khả năng sống sót hoàn toàn không mang tính tuyến tính (*far from linear*):
    * Trẻ vị thành niên / trẻ em (*minors*): Thường nhận được mức độ ưu tiên cứu nạn cao (*rescue priority*).
    * Người cao tuổi (*elderly*): Đối mặt với nhiều bất lợi về thể chất và khả năng di chuyển linh hoạt (*mobility disadvantages*).
    * Vùng chuyển tiếp đột ngột ở độ tuổi trung niên (*Sharp transition zone in middle age*): Tồn tại một vùng ngưỡng chuyển tiếp sắc nét ở độ tuổi trung niên, nơi xác suất sống sót biến thiên một cách kịch tính (*survival probability changes dramatically*).
  * **Hàm tang như một hình chiếu số học của nguyên tắc cứu hộ (*Numerical projection of rescue doctrine*)**:
    * Về mặt toán học, hàm $\tan$ với đặc tính tiệm cận dốc đứng mô tả chính xác hành vi vượt ngưỡng (*threshold-crossing behavior*) đột ngột này.
    * Về bản chất ngữ nghĩa, hàm số chính là hình chiếu số học (*numerical projection*) của nguyên tắc cứu nạn kinh điển "ưu tiên phụ nữ và trẻ em" (*"women and children first" rescue doctrine*) vào không gian đặc trưng (*feature space*).
* **Bước nhảy vọt về khả năng diễn giải mô hình (Interpretability leap)**:
  * Quá trình phân tích mang lại bước tiến nhảy vọt về tính minh bạch ngữ nghĩa:
    * Chuyển đổi từ "một hộp đen lượng giác lồng ghép tối nghĩa" (*a nested trigonometric black box*).
    * Thành "hiệu ứng biến đổi dốc đứng / đột ngột theo mức độ ưu tiên cứu hộ của độ tuổi" (*the rescue-priority steep-change effect of age*) có cơ sở logic và ý nghĩa thực tiễn vững chắc.
