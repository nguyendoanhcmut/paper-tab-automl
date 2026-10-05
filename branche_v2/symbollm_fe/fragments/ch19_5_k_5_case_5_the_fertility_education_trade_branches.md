### K.5 Case 5: The Fertility-Education Trade-Off in Contraceptive Choice

* Biểu thức hồi quy ký hiệu thô được sinh ra trên tập dữ liệu CMC (Contraceptive Method Choice dataset):
  * Cấu trúc toán học: $\min(\min(\text{sub}(X_3, X_1), \cos(\tan(X_2))), \cos(\tan(X_2)))$.
  * Ý nghĩa các biến thành phần:
    * $X_1$: Trình độ học vấn của người vợ (wife’s education level).
    * $X_2$: Trình độ học vấn của người chồng (husband’s education).
    * $X_3$: Số lượng con cái (number of children).
  * Biểu thức thực hiện lồng ghép hiệu số $X_3 - X_1$ bên trong phép toán $\min$ cùng với thành phần $\cos(\tan(X_2))$.
* Thách thức về tính diễn giải (interpretability challenge) của công thức ký hiệu:
  * Biểu thức $\cos(\tan(X_2))$ là một phép biến đổi lượng giác kép (double trigonometric transformation) áp dụng trên trình độ học vấn của người chồng.
  * Phép biến đổi này hoàn toàn không thể lý giải được theo bất kỳ nguyên lý nhân khẩu học hay xã hội học nào (defies any demographic interpretation).
* Mô hình ngôn ngữ lớn (LLM) suy luận và tinh chỉnh thành các đặc trưng có ý nghĩa thực tế:
  * LLM trích xuất các dạng đặc trưng cô đọng từ cấu trúc tín hiệu cốt lõi: $\min(X_3, X_1)$, $X_3 - X_1$, hoặc $\frac{X_3}{X_1 + 1}$.
  * Các đặc trưng này được định hình dưới dạng "chỉ số đánh đổi giữa sinh sản và học vấn" (fertility–education trade-off index).
* Nền tảng xã hội học vững chắc (sociologically grounded meaning) của đặc trưng tinh chỉnh:
  * Trong các nghiên cứu về lựa chọn biện pháp tránh thai (contraceptive choice research):
    * Phụ nữ có học vấn cao hơn ($X_1$) có xu hướng lựa chọn và áp dụng các biện pháp tránh thai hiện đại (modern contraceptive methods).
    * Số lượng con hiện có ($X_3$) phản ánh thái độ đối với việc tiếp tục sinh sản (attitudes toward continued childbearing).
  * Ý nghĩa trực tiếp của hiệu số $X_3 - X_1$:
    * Giá trị dương ($X_3 - X_1 > 0$, số con nhiều hơn mức mã hóa học vấn) đặc trưng cho nhóm phụ nữ từ các hộ gia đình truyền thống (traditional households), có xu hướng nghiêng về các biện pháp tránh thai dài hạn hoặc vĩnh viễn (permanent or long-acting contraception).
    * Giá trị âm ($X_3 - X_1 < 0$, học vấn tương đối cao hơn) tương ứng với nhóm phụ nữ có xu hướng ưu tiên các biện pháp tránh thai hiện đại hoặc ngắn hạn (short-acting or modern methods).
  * Phép toán $\min$ giúp nắm bắt nhân tố nào chiếm ưu thế và chi phối quyết định (captures whichever factor dominates the decision).
* Bước chuyển biến mô thức về khả năng diễn giải:
  * Chuyển hóa từ biểu thức mờ đục: “$\cos(\tan)$ của trình độ học vấn người chồng lồng với số con” (cos(tan) of husband’s education nested with child count).
  * Thành cơ chế ngữ nghĩa minh bạch: “cơ chế thay thế giữa sinh sản và học vấn trong việc ra quyết định tránh thai” (the fertility–education substitution mechanism in contraceptive decision-making).

#### Bài tập tình huống: Case 5: The Fertility-Education Trade-Off in Contraceptive Choice

* **Đề bài**:
  * Phân tích biểu thức hồi quy ký hiệu $\min(\min(\text{sub}(X_3, X_1), \cos(\tan(X_2))), \cos(\tan(X_2)))$ được sinh ra trên tập dữ liệu CMC (Contraceptive Method Choice). Giải thích lý do vì sao thành phần biến đổi lượng giác kép $\cos(\tan(X_2))$ đối với học vấn người chồng là không thể diễn giải được về mặt nhân khẩu học, và trình bày cơ chế LLM tinh chỉnh biểu thức này thành các đặc trưng có ý nghĩa xã hội học (như $X_3 - X_1$, $\min(X_3, X_1)$, hoặc $\frac{X_3}{X_1 + 1}$) nhằm định lượng cơ chế đánh đổi giữa sinh sản và học vấn trong quyết định tránh thai.
* **Dữ kiện**:
  * Tập dữ liệu: CMC (Contraceptive Method Choice dataset).
  * Các biến đầu vào trong biểu thức:
    * $X_1$: Trình độ học vấn của người vợ (`wife's education level`).
    * $X_2$: Trình độ học vấn của người chồng (`husband's education`).
    * $X_3$: Số lượng con cái hiện có (`number of children`).
  * Biểu thức hồi quy ký hiệu ban đầu: $\min(\min(\text{sub}(X_3, X_1), \cos(\tan(X_2))), \cos(\tan(X_2)))$.
  * Các đặc trưng do LLM suy luận đề xuất: $\min(X_3, X_1)$, $X_3 - X_1$, hoặc $\frac{X_3}{X_1 + 1}$.
* **Quy tắc áp dụng**:
  * Mục 4.1 (*Formula Construction by Symbolic Regression*): Hồi quy ký hiệu thông qua quy hoạch di truyền sử dụng tập các toán tử bảo vệ (protected operators) để tìm kiếm không gian hàm tối ưu hóa tương quan số học, nhưng dễ tạo ra các phép biến đổi lượng giác phi ngữ nghĩa lồng ghép phức tạp.
  * Mục 4.2 (*Feature Generation via LLMs*): LLM hoạt động như bộ tích hợp tất định và bộ lọc ngữ nghĩa miền, phát hiện cấu trúc tín hiệu then chốt ($X_3 - X_1$), loại bỏ các thành phần lượng giác nhân tạo không thể giải thích ($\cos(\tan(X_2))$), và thiết lập chỉ số có cơ sở lý thuyết nhân khẩu học.
  * Mục H.1 & H.2 (*Feature Traceability & Hallucination Mitigation*): Tinh chỉnh của LLM bảo toàn mối quan hệ phụ thuộc giữa các biến tương tác từ công thức gốc nhưng cải thiện căn bản tính trung thực toán học và khả năng diễn giải chuyên môn.
* **Lời giải**:
  * Bước 1: Nhận diện hạn chế và thành phần giả số học của công thức hồi quy ký hiệu thô:
    * Biểu thức gốc lồng ghép hiệu số $\text{sub}(X_3, X_1) = X_3 - X_1$ vào hai phép toán $\min$ liên tiếp với $\cos(\tan(X_2))$.
    * Trình độ học vấn của người chồng ($X_2$) là một biến định lượng thứ bậc. Việc áp dụng liên tiếp các hàm lượng giác tuần hoàn tang ($\tan$) và cô-sin ($\cos$) tạo ra dao động số học kỳ dị, hoàn toàn không có bất kỳ ý nghĩa nhân khẩu học hay kinh tế - xã hội học nào trong thực tế (defies any demographic interpretation).
  * Bước 2: Tái cấu trúc thành đặc trưng đánh đổi ngữ nghĩa thông qua LLM:
    * LLM nhận diện mối tương tác cốt lõi giữa học vấn của người vợ ($X_1$) và số lượng con cái ($X_3$).
    * LLM đề xuất ba biến thể đặc trưng tinh chỉnh có cơ sở toán học và ngữ nghĩa rõ ràng:
      1. Hiệu số trực tiếp: $X_3 - X_1$.
      2. Mức trần tương quan: $\min(X_3, X_1)$.
      3. Tỷ số chuẩn hóa tránh chia cho 0: $\frac{X_3}{X_1 + 1}$.
  * Bước 3: Diễn giải ngữ nghĩa dựa trên cơ sở xã hội học (Sociologically grounded semantic interpretation):
    * Trong nghiên cứu lựa chọn tránh thai, học vấn của phụ nữ ($X_1$) tỷ lệ thuận với xu hướng áp dụng các biện pháp tránh thai hiện đại, trong khi số con hiện có ($X_3$) phản ánh thái độ đối với việc tiếp tục sinh sản.
    * Ý nghĩa của hiệu số $X_3 - X_1$:
      * Giá trị dương ($X_3 - X_1 > 0$): Phụ nữ có số con nhiều hơn mức mã hóa học vấn thuộc các hộ gia đình truyền thống, có xu hướng nghiêng về biện pháp tránh thai dài hạn hoặc vĩnh viễn nhằm chấm dứt sinh đẻ.
      * Giá trị âm ($X_3 - X_1 < 0$): Phụ nữ có học vấn tương đối cao hơn so với số con ưu tiên các biện pháp tránh thai ngắn hạn hoặc hiện đại để chủ động kế hoạch hóa gia đình.
    * Phép toán $\min$ nắm bắt nhân tố nào chiếm ưu thế và chi phối quyết định lựa chọn.
* **Kết quả**:
  * Biểu thức đặc trưng hoàn chỉnh: $X_3 - X_1$ (hoặc các biến thể $\min(X_3, X_1)$, $\frac{X_3}{X_1 + 1}$).
  * Tên gọi ngữ nghĩa: Chỉ số đánh đổi sinh sản - học vấn (Fertility–Education Trade-Off Index) / Cơ chế thay thế sinh sản - học vấn trong việc ra quyết định tránh thai (Fertility–Education Substitution Mechanism in Contraceptive Decision-Making).
  * Bước nhảy vọt về tính diễn giải: Chuyển hóa từ “$\cos(\tan)$ của học vấn người chồng lồng ghép với số con” thành “cơ chế thay thế giữa sinh sản và học vấn trong việc ra quyết định tránh thai”.
* **Kiểm tra lại**:
  * Kiểm tra tính xác định và ổn định số học: Các biểu thức $X_3 - X_1$, $\min(X_3, X_1)$ và $\frac{X_3}{X_1 + 1}$ xác định hợp lệ trên toàn bộ miền dữ liệu CMC (với $X_1 \ge 0 \Rightarrow X_1 + 1 > 0$, tránh triệt để lỗi chia cho 0).
  * Kiểm tra loại bỏ thành phần mờ đục: Đã loại bỏ hoàn toàn biểu thức lượng giác vô nghĩa $\cos(\tan(X_2))$.
  * Kiểm tra tính trung thực với nguồn: Khớp hoàn toàn với nội dung chi tiết trong Phần K.5 về biến $X_1, X_2, X_3$, công thức gốc, các biến thể đề xuất và phân tích xã hội học.
