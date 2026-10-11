### K.5 Case 5: The Fertility–Education Trade-Off in Contraceptive Choice

* **Tập dữ liệu thực nghiệm và công thức hồi quy biểu tượng ban đầu (Experimental dataset and raw symbolic regression formula)**:
  * **Tập dữ liệu khảo sát**: Tập dữ liệu Lựa chọn Biện pháp Tránh thai CMC (*Contraceptive Method Choice dataset*).
  * **Các biến số tham gia**:
    * $X_1$: Trình độ học vấn của người vợ (*wife's education level*).
    * $X_2$: Trình độ học vấn của người chồng (*husband's education*).
    * $X_3$: Số lượng con cái hiện có (*number of children*).
  * **Biểu thức toán học do hồi quy biểu tượng khởi tạo**: Hồi quy biểu tượng (*symbolic regression - SR*) tạo ra công thức lồng ghép phức tạp:
    $$\min(\min(\text{sub}(X_3, X_1), \cos(\tan(X_2))), \cos(\tan(X_2)))$$
    tương đương dạng rút gọn đại số:
    $$\min(X_3 - X_1, \cos(\tan(X_2)))$$
  * **Cấu trúc lồng ghép của biểu thức**:
    * Lồng ghép hiệu số học vấn - sinh đẻ $X_3 - X_1$ bên trong phép toán cực tiểu $\min$ cùng với thành phần lượng giác $\cos(\tan(X_2))$.
    * Số hạng $\cos(\tan(X_2))$ là một phép biến đổi lượng giác kép (*double trigonometric transformation*) tác động lên biến trình độ học vấn của người chồng.

* **Thách thức về khả năng diễn giải (Interpretability challenge)**:
  * **Sự vô nghĩa về mặt nhân khẩu học (*Defies demographic interpretation*)**:
    * Phép biến đổi lượng giác kép $\cos(\tan(X_2))$ đối với học vấn của người chồng hoàn toàn không thể giải thích hay biện minh được dưới bất kỳ lăng kính nhân khẩu học thực tế nào (*defies any demographic interpretation*).
    * Hành vi dao động tuần hoàn và tính phi tuyến cực đoan của hàm $\cos(\tan(\cdot))$ không phản ánh bất kỳ quy luật tự nhiên hay mối tương quan xã hội nào liên quan đến học vấn gia đình.
  * **Sự mờ đục trong tương tác đa biến**: Việc gộp chung số lượng con cái với biến đổi lượng giác của học vấn người chồng thông qua phép lấy cực tiểu $\min$ tạo thành một cấu trúc hộp đen toán học, làm triệt tiêu khả năng truy nguyên nguyên nhân xã hội học đằng sau quyết định kế hoạch hóa gia đình.

* **Các đặc trưng do LLM suy luận và đề xuất (LLM-inferred features)**:
  * **Bộ đặc trưng ứng viên do LLM đề xuất**: Mô hình ngôn ngữ lớn (*LLM*) suy luận và trích xuất các đặc trưng toán học tường minh, bao gồm:
    * $\min(X_3, X_1)$
    * $X_3 - X_1$
    * $\frac{X_3}{X_1 + 1}$
  * **Định khung khái niệm (*Conceptual framing*)**:
    * LLM định khung các đặc trưng mới như một chỉ số đánh đổi giữa mức sinh và học vấn (*fertility–education trade-off index*).
  * **Cơ chế biểu diễn của phép toán cực tiểu ($\min$)**:
    * Phép toán $\min$ được giải thích là cơ chế toán học nắm bắt yếu tố nào giữ vai trò áp đảo hoặc chi phối quá trình ra quyết định (*captures whichever factor dominates the decision*).

* **Diễn giải ngữ nghĩa bám sát miền tri thức xã hội học (Domain-grounded sociological interpretation)**:
  * **Cơ sở lý thuyết trong nghiên cứu lựa chọn biện pháp tránh thai (*Contraceptive choice research*)**:
    * Phụ nữ có học vấn cao hơn ($X_1$ cao) có xu hướng chủ động tiếp cận và áp dụng các biện pháp tránh thai hiện đại (*modern contraceptive methods*).
    * Số lượng con cái hiện có ($X_3$) phản ánh thái độ, nhu cầu và mong muốn đối với việc tiếp tục sinh con (*attitudes toward continued childbearing*).
  * **Ý nghĩa ngữ nghĩa trực tiếp của hiệu số $X_3 - X_1$**:
    * **Trường hợp mang giá trị dương ($X_3 - X_1 > 0$)**:
      * Số lượng con cái thực tế vượt quá mức mã hóa trình độ học vấn (*more children than the education encoding*).
      * Đặc trưng cho nhóm phụ nữ thuộc các hộ gia đình truyền thống (*traditional households*).
      * Nhóm này có xu hướng nghiêng về các biện pháp tránh thai vĩnh viễn hoặc dài hạn (*permanent or long-acting contraception*).
    * **Trường hợp mang giá trị âm ($X_3 - X_1 < 0$)**:
      * Trình độ học vấn tương đối cao hơn so với số con hiện có (*higher relative education*).
      * Tương ứng với nhóm phụ nữ có xu hướng ưu tiên các biện pháp tránh thai ngắn hạn hoặc phương pháp hiện đại (*short-acting or modern methods*).
  * **Bước tiến vượt bậc về tính tường minh ngữ nghĩa (*Interpretability advance*)**:
    * Thay thế hoàn toàn biểu thức tối nghĩa: "Hàm $\cos(\tan)$ của học vấn người chồng lồng ghép với số con" (*"cos(tan) of husband's education nested with child count"*).
    * Xác lập cơ chế nhân quả xã hội học chuẩn xác: "Cơ chế thay thế / đánh đổi giữa mức sinh và học vấn trong quá trình ra quyết định tránh thai" (*"the fertility–education substitution mechanism in contraceptive decision-making"*).
