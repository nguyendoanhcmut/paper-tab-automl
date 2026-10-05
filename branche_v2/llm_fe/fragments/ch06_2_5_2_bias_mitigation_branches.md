### 5.2 Bias Mitigation

- **Thiên lệch cố hữu của LLM về phía các toán tử toán học đơn giản (Pronounced bias toward simple operators)**:
  - Khi được yêu cầu sinh các biến đổi đặc trưng (feature transformations), các mô hình ngôn ngữ lớn (LLMs - Large Language Models) bộc lộ thiên lệch rõ nét về một tập hẹp các toán tử số học đơn giản như phép cộng (`add` / addition), phép trừ (`subtract` / subtraction), và giá trị tuyệt đối (`abs` / absolute value) (Küken et al., 2024).
  - *Nguồn gốc thiên lệch*: Xuất phát từ kho ngữ liệu tiền huấn luyện (pretraining corpora), nơi các quy luật đơn giản chiếm thế áp đảo và trở thành các chiến lược sinh mặc định (default strategies).
  - *Hệ quả của quy trình ngây thơ (naive pipelines)*: Các pipeline kỹ thuật đặc trưng dựa trên LLM ngây thơ thường tạo ra các phép biến đổi lặp lại, độ phức tạp thấp (low-complexity transformations), thất bại trong việc khai thác không gian kết hợp phong phú (richer compositional space) của các toán tử dữ liệu bảng thực sự có ý nghĩa.

- **Minh chứng thực nghiệm về thiên lệch toán tử trong các phương pháp cơ sở (Empirical operator bias in baselines)**:
  - Phương pháp CAAFE bộc lộ xu hướng ưu tiên cực đoan các phép biến đổi cơ bản: riêng hai toán tử nhân (`multiply`) và chia (`divide`) đã chiếm tới $75\%$ tổng số toán tử được tạo ra.
  - Mô hình LLM cơ sở (Base LLM) cũng tập trung gần như toàn bộ vào các phép tính cộng, trừ, nhân, chia và trị tuyệt đối, hoàn toàn vắng bóng các phép biến đổi bậc cao.
  - **Hình 4.** Tần suất sử dụng toán tử kỹ thuật đặc trưng giữa các mô hình
    - <img src="assets/fig_04_p9_vector.png" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - LLM-FE hóa giải thiên lệch toán tử đơn giản, khám phá đa dạng các phép biến đổi phức hợp và phi tuyến tính.
    - **Từ đâu mà thấy được**
      - Trục hoành biểu diễn các toán tử, trục tung là tần suất ($0.0 - 0.5$); CAAFE chiếm tới $75\%$ cho `divide` (~$0.51$) và `multiply` (~$0.24$), Base LLM chỉ dùng số học cơ bản, trong khi LLM-FE phân bổ đáng kể sang `residual`, `sigmoid`, `groupbythenmean`, `groupbythenmin`, và `groupbythenmax`.

- **Năng lực khám phá các phép biến đổi tinh vi thông qua tinh chỉnh tiến hóa (Evolutionary refinement)**:
  - Bất chấp thiên lệch cố hữu nêu trên, LLM-FE thường xuyên tìm ra và duy trì các biến đổi đặc trưng tinh vi (sophisticated feature transformations) nhờ cơ chế tinh chỉnh tiến hóa (evolutionary refinement).
  - Các toán tử bậc cao xuất hiện với tần suất vượt trội trong khuôn khổ tiến hóa của LLM-FE so với việc sinh trực tiếp từ LLM đơn lẻ:
    - Nhóm toán tử gom nhóm tổng hợp (`groupbythenmean`, `groupbythenmin`, `groupbythenmax`): Khai thác cấu trúc tổng hợp (aggregation structure) và biến thiên có điều kiện theo lớp (class-conditional variation).
    - Nhóm toán tử phi tuyến và phần dư (`residual`, `sigmoid`): Mô hình hóa các mối quan hệ phi tuyến tính (nonlinear relationships) phức tạp mà các phép tính số học đơn giản không thể biểu diễn được.

- **Cơ chế ba tác động của tìm kiếm tiến hóa nhằm triệt tiêu thiên lệch (Threefold evolutionary mechanism)**:
  - Cơ chế tìm kiếm tiến hóa (evolutionary search mechanism) của LLM-FE chủ động đối trọng và hóa giải xu hướng đơn giản hóa quá mức của LLM thông qua ba nguyên lý:
    1. **Thúc đẩy tính đa dạng (promoting diversity)**: Mở rộng diện bao phủ không gian tìm kiếm toán tử.
    2. **Đánh giá dựa trên hiệu năng thực nghiệm (empirical performance)**: Kiểm định biến đổi trực tiếp trên dữ liệu thực tế thay vì dựa vào phán đoán chủ quan.
    3. **Tinh chỉnh lặp các đặc trưng ứng viên (iteratively refining candidate features)**: Chọn lọc và tiến hóa liên tục các biến đổi có chất lượng cao.

- **Tác động kép của LLM-FE đối với chất lượng đặc trưng**:
  - LLM-FE không chỉ làm giảm nguy cơ ghi nhớ vẹt (memorization) mà còn giảm thiểu hiệu quả thiên lệch lựa chọn toán tử (operator-selection bias).
  - Cho phép tự động phát hiện các đặc trưng giàu tính biểu đạt (expressive) và gắn liền với tri thức miền (domain-relevant) mà các phương pháp gợi ý trực tiếp thông thường (naive prompting) hiếm khi có thể chạm tới.
