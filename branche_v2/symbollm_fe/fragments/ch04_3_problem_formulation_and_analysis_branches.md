## 3 Problem Formulation and Analysis

### 3.1 Problem Formulation

- Mục tiêu hình thức của các tác vụ dự đoán trên dữ liệu bảng (tabular prediction tasks) là huấn luyện một mô hình học máy (machine learning model) $f : X \rightarrow Y$, trong đó $X$ là không gian đầu vào (input space) và $Y$ là không gian đầu ra (output space).
  - Tập hợp các đặc trưng trong $X$ được định nghĩa là $C$.
  - Đối với không gian $X$ có $n$ chiều ($n$-dimensional), tập đặc trưng thông thường là $C = \{c_1, c_2, \dots, c_n\}$.
- Kỹ thuật đặc trưng (feature engineering) nhằm mục đích mở rộng số chiều của $X$ bằng cách tạo ra $m$ đặc trưng mới dựa trên $C$, tức là tập đặc trưng mới $C_{\text{new}} = \{c_{n+1}, c_{n+2}, \dots, c_{n+m}\}$.
  - Sau kỹ thuật đặc trưng, số chiều của $X$ tăng từ $n$ lên $n + m$.
  - Hiệu năng (performance) $P$ của $f$ có thể được cải thiện trên tập đặc trưng mới $S$.
- Mục tiêu là đạt được giá trị cực đại của hiệu năng $f$, bằng cách thay đổi $C_{\text{new}}$ được sinh ra bởi bộ AutoFE (Automated Feature Engineering - kỹ thuật đặc trưng tự động) $g$:
  $$\max P_f(S) = \max P_f(C \oplus C_{\text{new}}) = \max P_f(C \oplus g(C)) \quad (1)$$
  - Trong đó, $S = C \oplus C_{\text{new}} = C \oplus g(C)$ biểu diễn tập đặc trưng sau khi ghép nối các đặc trưng ban đầu với các đặc trưng do $g$ sinh ra.

### 3.2 Analysis

- Phân tích so sánh các phương pháp AutoFE khác nhau trong Figure 1 và Table 1 bộc lộ một sự phân đôi rõ rệt (dichotomy) giữa AutoFE truyền thống (traditional AutoFE) và AutoFE dựa trên LLM (LLM-based AutoFE), làm nổi bật các điểm nghẽn then chốt ở cả hiệu suất (efficiency) lẫn chất lượng đặc trưng (feature quality).
- AutoFE truyền thống bị giới hạn nghiêm ngặt bởi các đặc trưng không thể diễn giải (uninterpretable features):
  - Phương pháp này phụ thuộc vào một chồng toán tử mù (blind operator stack) để kết hợp các cột dữ liệu thô về mặt toán học mà không có sự hiểu biết ngữ nghĩa (semantic understanding).
  - Quá trình này sinh ra một tập đặc trưng quá lớn (excessively large feature set).
  - Các đặc trưng mới sinh ra thiếu nền tảng ngữ nghĩa (semantic grounding) và ý nghĩa vật lý (physical meaning), không cung cấp được các hiểu biết hữu ích (actionable insights) cho việc thu thập đặc trưng trong tương lai.
  - Các đặc trưng này mang lại khả năng tổng quát hóa kém đối với các tác vụ xuôi dòng (downstream tasks) do tính diễn giải (interpretability) của các đặc trưng được sinh ra bị tổn hại nghiêm trọng.
- AutoFE dựa trên LLM đảm bảo tính diễn giải ngữ nghĩa nhờ tận dụng tri thức nền tảng của tác vụ (task background knowledge), nhưng gặp trở ngại với chi phí lặp cao (high iteration costs) như thể hiện trong Table 1:
  - Việc chỉ dựa hoàn toàn vào LLM để sinh đặc trưng thường xuyên tạo ra các đặc trưng tuy mạch lạc về mặt ngữ nghĩa và phù hợp với miền dữ liệu nhưng lại thiếu năng lực phân biệt mạnh mẽ (robust discriminative power).
  - Các phương pháp như OcTree đòi hỏi xấp xỉ 50 vòng lặp (rounds) để hội tụ, cho thấy các đặc trưng do AutoFE dựa trên LLM sinh ra cần trải qua nhiều vòng kiểm chứng thử-sai (trial-and-error validation) và liên tục tinh chỉnh để nâng cao hiệu năng của mô hình xuôi dòng.
  - Tính bất định nội tại (intrinsic uncertainty) này buộc phải diễn ra tương tác lặp đi lặp lại trên diện rộng với các bộ dự đoán xuôi dòng (downstream predictors), dẫn đến sự bùng nổ nghiêm trọng về cả số vòng lặp lẫn chi phí thời gian tính toán (computational time costs).
  - Hơn nữa, các phương pháp AutoFE dựa trên LLM tiên tiến này vốn dĩ vẫn dễ bị ảnh hưởng bởi hiện tượng ảo giác nghiêm trọng (severe hallucinations) và thiên kiến tiềm ẩn (implicit biases), có thể dẫn đến việc suy giảm hiệu năng mô hình.
- Các phát hiện trên làm nổi bật rõ rệt những hạn chế cốt lõi của AutoFE truyền thống và AutoFE dựa trên LLM hiện nay, nhấn mạnh nhu cầu cấp thiết về một khung làm việc AutoFE tối ưu hóa hơn:
  - Khung làm việc cần có khả năng vượt qua chi phí lặp cao của LLM và bản chất khó diễn giải của các phép kết hợp toán học truyền thống.
  - Mục tiêu là tạo ra các đặc trưng đồng thời vừa có khả năng diễn giải (interpretable) vừa đạt hiệu quả dự đoán cao (predictively effective).
