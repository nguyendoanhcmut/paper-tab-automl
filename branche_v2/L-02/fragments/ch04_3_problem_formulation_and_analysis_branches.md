## 3 Problem Formulation and Analysis

### 3.1 Problem Formulation

* **Mục tiêu hình thức của bài toán dự đoán dạng bảng (tabular prediction tasks):**
  * Mục tiêu cốt lõi là huấn luyện một mô hình học máy (machine learning model) $f : \mathcal{X} \to \mathcal{Y}$, trong đó $\mathcal{X}$ biểu diễn không gian đầu vào (input space) và $\mathcal{Y}$ biểu diễn không gian đầu ra (output space).
  * Tập hợp tất cả các đặc trưng trong không gian đầu vào $\mathcal{X}$ được định nghĩa là $C$.
  * Với không gian đầu vào $\mathcal{X}$ có số chiều là $n$ ($n$-dimensional), tập đặc trưng thông thường (ordinary feature set) được xác định là:
    $$C = \{c_1, c_2, \dots, c_n\}$$

* **Mục đích và cơ chế mở rộng số chiều của kỹ thuật đặc trưng (feature engineering):**
  * Kỹ thuật đặc trưng hướng đến việc mở rộng số chiều của không gian đầu vào $\mathcal{X}$ thông qua việc sinh ra $m$ đặc trưng mới dựa trên tập đặc trưng ban đầu $C$.
  * Tập đặc trưng mới sinh ra được ký hiệu là $C_{\text{new}}$:
    $$C_{\text{new}} = \{c_{n+1}, c_{n+2}, \dots, c_{n+m}\}$$
  * Sau khi thực hiện kỹ thuật đặc trưng, số chiều của không gian đầu vào $\mathcal{X}$ tăng từ $n$ lên $n + m$.
  * Hiệu năng $P$ của mô hình $f$ có thể được cải thiện trên tập đặc trưng mở rộng $S$, với $S = C \oplus C_{\text{new}}$ (trong đó $\oplus$ ký hiệu phép kết hợp/ghép nối tập hợp đặc trưng).

* **Mục tiêu tối ưu hóa của kỹ thuật đặc trưng tự động (AutoFE objective optimization):**
  * Mục tiêu là đạt được hiệu năng tối đa của mô hình $f$ bằng cách thay đổi và tối ưu hóa tập đặc trưng mới $C_{\text{new}}$ được sinh ra từ phương pháp AutoFE $g$:
    $$\max P_f(S) = \max P_f(C \oplus C_{\text{new}}) = \max P_f(C \oplus g(C)) \quad (1)$$
  * Ý nghĩa các thành phần trong công thức tối ưu hóa:
    * $g$ biểu diễn toán tử hoặc quy trình kỹ thuật đặc trưng tự động (AutoFE method/operator) ánh xạ từ tập đặc trưng gốc $C$ sang tập đặc trưng mới $C_{\text{new}} = g(C)$.
    * $P_f(\cdot)$ biểu thị hàm đánh giá đo lường hiệu năng của bộ dự đoán hạ nguồn (downstream predictor) $f$ khi được huấn luyện và suy luận trên tập đặc trưng được cung cấp.

### 3.2 Analysis

* **Sự phân đôi rõ rệt giữa AutoFE truyền thống và AutoFE dựa trên LLM (dichotomy between traditional and LLM-based AutoFE):**
  * Phân tích so sánh giữa các phương pháp AutoFE khác nhau trong Hình 1 (Figure 1) và Bảng 1 (Table 1) làm nổi bật sự đối lập rõ rệt giữa hai trường phái: AutoFE truyền thống (traditional AutoFE) và AutoFE dựa trên mô hình ngôn ngữ lớn (LLM-based AutoFE).
  * Sự phân cực này phản ánh các điểm nghẽn nghiêm trọng (critical bottlenecks) ở cả khía cạnh hiệu quả vận hành/tính toán (efficiency) và chất lượng đặc trưng (feature quality).

* **Hạn chế nghiêm ngặt của AutoFE truyền thống về khả năng diễn giải đặc trưng:**
  * AutoFE truyền thống bị giới hạn nghiêm ngặt bởi các đặc trưng không thể diễn giải (strictly limited by uninterpretable features - minh họa trong Hình 1).
  * Cơ chế xếp chồng toán tử mù quáng:
    * Phụ thuộc vào việc xếp chồng toán tử mù quáng (blind operator stack) để thực hiện kết hợp toán học các cột thô (mathematically combine raw columns) mà hoàn toàn không có hiểu biết về mặt ngữ nghĩa (without semantic understanding).
    * Quá trình này tạo ra một tập đặc trưng phình to quá mức (excessively large feature set).
  * Thiếu hụt nền tảng ngữ nghĩa và giá trị sử dụng thực tiễn:
    * Các đặc trưng mới sinh ra thiếu nền tảng ngữ nghĩa (lack semantic grounding) và không mang ý nghĩa vật lý (physical meaning).
    * Thất bại trong việc cung cấp các thông tin chi tiết có thể hành động (actionable insights) nhằm phục vụ công tác thu thập đặc trưng trong tương lai (future feature acquisition).
    * Khả năng tổng quát hóa (generalization) sang các tác vụ hạ nguồn (downstream tasks) rất kém do khả năng diễn giải của các đặc trưng sinh ra bị tổn hại nghiêm trọng.

* **Điểm nghẽn chi phí vòng lặp và rủi ro nội tại của AutoFE dựa trên LLM:**
  * Mặc dù LLM-based AutoFE bảo đảm khả năng diễn giải ngữ nghĩa (semantic interpretability) nhờ khai thác tri thức nền tảng của tác vụ (task background knowledge), phương pháp này phải đối mặt với chi phí vòng lặp rất lớn (high iteration costs - thể hiện qua Bảng 1).
  * Đặc trưng thiếu sức mạnh phân biệt mạnh mẽ:
    * Việc phụ thuộc hoàn toàn vào LLM để sinh đặc trưng thường tạo ra các đặc trưng có tính mạch lạc về mặt ngữ nghĩa (semantically coherent) và phù hợp với miền bài toán (domain-relevant), nhưng lại thiếu sức mạnh phân biệt mạnh mẽ (lack robust discriminative power).
    * Minh chứng thực nghiệm: các phương pháp như OcTree đòi hỏi khoảng $50$ vòng lặp (rounds) để hội tụ, cho thấy các đặc trưng do LLM-based AutoFE tạo ra bắt buộc phải trải qua nhiều vòng thử-sai (trial-and-error validation) và liên tục tinh chỉnh (continuous refinement) mới có thể cải thiện được hiệu năng mô hình hạ nguồn.
  * Chi phí tính toán bùng nổ và rủi ro ảo giác:
    * Tính bất định nội tại (intrinsic uncertainty) buộc hệ thống phải duy trì các tương tác lặp đi lặp lại trên diện rộng với các bộ dự đoán hạ nguồn (downstream predictors), dẫn đến sự gia tăng đột biến không thể chấp nhận được (prohibitive surge) về cả số vòng lặp lẫn chi phí thời gian tính toán (computational time costs).
    * Các phương pháp LLM-based AutoFE tiên tiến này vẫn nhạy cảm cố hữu với hiện tượng ảo giác nghiêm trọng (severe hallucinations) và thiên kiến ngầm ẩn (implicit biases), có thể dẫn tới sự sụt giảm hiệu năng của mô hình.

* **Nhu cầu cấp thiết về một khung làm việc AutoFE tối ưu hóa:**
  * Những phát hiện so sánh trên làm sáng tỏ các hạn chế cốt lõi của cả AutoFE truyền thống và AutoFE dựa trên LLM hiện tại.
  * Nhấn mạnh nhu cầu cấp thiết về một khung làm việc AutoFE tối ưu hơn có khả năng:
    * Loại bỏ gánh nặng chi phí vòng lặp khổng lồ của các LLM (bypass the high iteration overhead of LLMs).
    * Vượt qua bản chất không thể diễn giải của các phép kết hợp toán học truyền thống (bypass the uninterpretable nature of traditional mathematical combinations).
    * Hướng tới mục tiêu sinh ra các đặc trưng vừa có khả năng diễn giải vừa mang lại hiệu quả dự đoán cao (simultaneously interpretable and predictively effective).
