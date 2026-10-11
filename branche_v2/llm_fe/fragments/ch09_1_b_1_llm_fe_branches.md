### B.1 LLM-FE

#### Feature Generation (Sinh đặc trưng)

- **Cấu trúc prompt đầu vào tiêu chuẩn**: Đối với tập dữ liệu `balance-scale`, prompt (lời nhắc) bắt đầu bằng các chỉ dẫn chung (general instructions), tiếp theo là thông tin chi tiết đặc thù của tập dữ liệu bao gồm mô tả tác vụ (task descriptions), mô tả đặc trưng (feature descriptions), và một tập con các quan sát dữ liệu được tuần tự hóa (serialized data instances) diễn đạt bằng ngôn ngữ tự nhiên.
  - Ngữ cảnh có cấu trúc này cho phép mô hình tận dụng tri thức miền (domain knowledge) để đề xuất các giả thuyết có ý nghĩa ngữ nghĩa và ngữ cảnh cho các chương trình tối ưu hóa đặc trưng mới.
  - Chi tiết về chất lượng của các đặc trưng được tạo ra được trình bày cụ thể trong Phụ lục 5.2 (Appendix 5.2).
  - **Hình 9.** Cấu trúc prompt mẫu cho tập dữ liệu balance-scale
    - <img src="assets/fig_08_p17_vector.png" alt="Hình 9" />
    - **Hình này chứng minh điều gì**
      - Minh họa trực quan 5 khối cấu trúc thành phần của prompt giúp LLM sinh mã biến đổi đặc trưng hợp lệ và tối ưu.
    - **Từ đâu mà thấy được**
      - 5 khối nhãn đỏ: Chỉ dẫn (Instruction), Đặc tả tập dữ liệu (Dataset Specification), Hàm đánh giá (Evaluation Function), Ví dụ mẫu (In-Context Example), và Hàm cần hoàn thiện (Function to Complete).
- **Chiến lược đa dạng hóa prompt và giảm thiểu thiên lệch toán tử**: Nhằm tạo sự đa dạng trong kỹ thuật nhắc lệnh (prompting diversity), quy trình lấy mẫu ngẫu nhiên giữa phương pháp tiếp cận tiêu chuẩn và một bộ chỉ dẫn thay thế (alternative set of instructions).
  - Bộ chỉ dẫn thay thế khuyến khích LLM khai phá dải rộng các toán tử từ OpenFE (Zhang et al., 2023), khắc phục hạn chế cố hữu của các LLM trước đây vốn có xu hướng thiên lệch chuộng các toán tử đơn giản (Küken et al., 2024).
  - **Hình 8.** Chỉ dẫn thay thế định hướng dùng toán tử phức tạp
    - <img src="assets/fig_07_p16_vector.png" alt="Hình 8" />
    - **Hình này chứng minh điều gì**
      - Thiết kế prompt ép buộc LLM không sử dụng phép tính số học cơ bản mà phải tập trung vào các toán tử nâng cao từ OpenFE.
    - **Từ đâu mà thấy được**
      - Các thẻ cấu trúc: `<Role>` định vị chuyên gia dữ liệu, `<Instructions>` cấm phép tính cộng trừ nhân chia, và danh mục `<Operators>` phân loại chi tiết các toán tử phức tạp.

#### Data-Driven Evaluation (Đánh giá dựa trên dữ liệu)

- **Lấy mẫu đầu ra từ LLM**: Sau khi truyền prompt vào LLM, hệ thống tiến hành lấy mẫu $b = 3$ đầu ra (outputs).
- **Cấu hình nhiệt độ sinh mã**: Dựa trên các thí nghiệm sơ bộ, tham số nhiệt độ sinh mã của LLM được thiết lập ở mức $t = 0.8$.
  - Mức nhiệt độ này giúp cân bằng giữa tính sáng tạo khám phá (exploration) và sự tuân thủ các ràng buộc bài toán cũng như khai thác tri thức sẵn có (exploitation).
- **Quy trình biến đổi dữ liệu thực nghiệm**: Các đoạn mã sinh ra từ LLM được áp dụng trực tiếp để biến đổi các đặc trưng thông qua hàm `modify_features(inputs)` (như minh họa tại Hình 9(c)).
  - Tập đặc trưng sau khi sửa đổi được đưa vào mô hình dự đoán (prediction model) để huấn luyện và tính toán điểm số kiểm định (validation score) tương ứng.
- **Ràng buộc tài nguyên và cơ chế kiểm soát chất lượng**: Quá trình đánh giá được kiểm soát nghiêm ngặt với giới hạn thời gian thực thi $T = 30\text{ s}$ và giới hạn bộ nhớ $M = 2\text{ GB}$.
  - Các chương trình vượt quá một trong hai ngưỡng giới hạn này sẽ bị loại trực tiếp (disqualified) và gán điểm số là `None`.
  - Cơ chế này đảm bảo tiến độ tìm kiếm diễn ra đúng thời hạn và tối ưu hóa hiệu quả sử dụng tài nguyên phần cứng.

#### Memory Management (Quản lý bộ nhớ)

- **Kiến trúc bộ đệm đa đảo độc lập (Islands Model)**: Áp dụng mô hình các đảo ('islands' model) phỏng theo Cranmer (2023), Shojaee et al. (2025), và Romera-Paredes et al. (2024), các giả thuyết sinh ra cùng điểm số đánh giá được lưu trữ trong một bộ đệm bộ nhớ (memory buffer) gồm $m = 3$ đảo tiến hóa độc lập.
  - Mỗi đảo được khởi tạo bằng một chương trình biến đổi đặc trưng đơn giản đặc thù cho tập dữ liệu (ví dụ: hàm `def modify_features_v0()` trong Hình 9(d)).
  - Trong mỗi vòng lặp, các giả thuyết mới và chỉ số kiểm định tương ứng chỉ được tích hợp vào đảo nếu chúng đạt điểm số vượt qua kỷ lục tốt nhất hiện tại của đảo đó.
- **Phân cụm chương trình dựa trên chữ ký (Signature-Based Clustering)**: Bên trong từng đảo, các chương trình khám phá đặc trưng được phân cụm dựa trên chữ ký (signature) được đặc trưng bởi chính điểm số kiểm định (validation score) của chúng.
  - Các chương trình biến đổi đặc trưng cho ra điểm số giống hệt nhau sẽ được gom lại thành các cụm riêng biệt (distinct clusters).
  - Phương pháp phân cụm này giúp bảo tồn tính đa dạng (preserve diversity) của quần thể bằng cách duy trì các chương trình có đặc tính hiệu năng khác nhau cùng tồn tại.
- **Cơ chế chọn mẫu in-context qua phân phối Boltzmann**: Mô hình đảo được khai thác trực tiếp để xây dựng prompt cho LLM; sau khi cập nhật mẫu prompt ban đầu với thông tin tập dữ liệu, các ví dụ minh họa ngữ cảnh (in-context demonstrations) được tích hợp từ bộ đệm:
  - Chọn ngẫu nhiên một trong $m$ đảo hiện có.
  - Trong đảo đã chọn, tiến hành lấy mẫu $k = 3$ chương trình đóng vai trò làm mẫu ví dụ minh họa in-context.
  - Để lấy mẫu chương trình, trước tiên hệ thống chọn cụm dựa trên chữ ký bằng chiến lược chọn lọc Boltzmann (Boltzmann selection strategy; De La Maza & Tidor, 1992), ưu tiên các cụm có điểm số cao hơn.
- **Xác suất chọn cụm và tham số làm nguội**: Gọi $s_i$ là điểm số của cụm thứ $i$, xác suất $P_i$ để chọn cụm thứ $i$ được xác định theo công thức:
  $$P_i = \frac{\exp\left(\frac{s_i}{\tau_c}\right)}{\sum_i \exp\left(\frac{s_i}{\tau_c}\right)}$$
  trong đó tham số nhiệt độ $\tau_c$ được điều chỉnh động theo công thức:
  $$\tau_c = T_0\left(1 - \frac{u \bmod N}{N}\right)$$
  - $\tau_c$ là tham số nhiệt độ (temperature parameter).
  - $u$ là số lượng chương trình hiện tại trên đảo.
  - $T_0 = 0.1$ và $N = 10{,}000$ là các siêu tham số (hyperparameters).
  - Sau khi một cụm được chọn theo phân phối xác suất trên, các chương trình cụ thể sẽ được lấy mẫu trực tiếp từ cụm đó.
