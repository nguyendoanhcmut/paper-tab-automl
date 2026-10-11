### 5.3 Impact of Domain Knowledge and Evolutionary Refinement

- **Lợi ích định tính của việc tích hợp tri thức miền trong kỹ thuật đặc trưng (Qualitative benefits of domain knowledge)**:
  - Phân tích định tính (Figure 7) đối chiếu rõ nét giữa hai hướng tiếp cận trên tập dữ liệu y sinh: kỹ thuật đặc trưng không có tri thức miền (w/o domain knowledge - Figure 7(a)) và LLM-FE được định hướng bởi tri thức chuyên biệt theo miền (domain-specific insights - Figure 7(b)).
  - *Hạn chế của biến thể không có tri thức miền (domain-agnostic variant)*: Tên các đặc trưng bị ẩn danh hóa thành ký hiệu trừu tượng ($C_1, C_2, C_3$); mô hình tạo ra các phép biến đổi tùy tiện (arbitrary transformations) như lấy căn bậc hai tích của hai biến ($C_{10} = \sqrt{C_1 \times C_3}$) và loại bỏ đặc trưng $C_2$ mà không có lý giải xác đáng, dẫn tới các đầu ra không thể diễn giải được (uninterpretable outputs).
  - *Ưu thế vượt trội của LLM-FE*: Khai thác kho tri thức miền nội tại (embedded domain knowledge) của LLM để suy luận logic (Thought) và sinh ra các đặc trưng có khả năng diễn giải cao (interpretable) cùng ý nghĩa lâm sàng thực tế (clinically meaningful features):
    - Tạo đặc trưng tỷ lệ Insulin / Glucose (`insulin_glucose_ratio` = $\text{Insulin} / \text{Glucose}$) nhằm phản ánh trạng thái chuyển hóa (metabolic state) của cơ thể.
    - Tạo đặc trưng tỷ lệ BMI / Tuổi (`bmi_age_ratio` = $\text{BMI} / \text{Age}$) đóng vai trò chỉ số đánh giá rủi ro mắc bệnh tiểu đường (diabetes risk) tiềm ẩn.

- **Minh chứng định lượng về tác động vượt trội của tri thức miền đối với độ chính xác mô hình (Quantitative impact of domain knowledge)**:
  - Kết quả so sánh định lượng trên cùng tập dữ liệu (Figure 5) khẳng định việc tích hợp tri thức miền giúp LLM-FE tối ưu hóa độ chính xác (accuracy) vượt bậc:
    - LLM-FE đạt độ chính xác cao nhất ($\approx 0.746$), vượt trội hơn hẳn cả mô hình cơ sở (Base model, $\approx 0.732$) lẫn biến thể LLM-FE không có tri thức miền (LLM-FE w/o domain knowledge, đạt $0.735$).
  - **Hình 5.** Tác động định lượng của tri thức miền lên độ chính xác mô hình
    - <img src="assets/fig_05_p10_vector.png" alt="Hình 5" />
    - **Hình này chứng minh điều gì**
      - LLM-FE tích hợp tri thức miền tối ưu hóa độ chính xác vượt trội so với mô hình cơ sở và biến thể thiếu tri thức miền.
    - **Từ đâu mà thấy được**
      - Biểu đồ cột biểu diễn Accuracy: mô hình Base đạt ~0.732, LLM-FE không có tri thức miền đạt 0.735, trong khi LLM-FE đầy đủ bứt phá lên ~0.746.

- **Phân tích quỹ đạo hiệu năng và vai trò của cơ chế tinh chỉnh tiến hóa (Evolutionary refinement trajectory)**:
  - Khảo sát quỹ đạo độ chính xác kiểm định (validation accuracy trajectory) qua $20$ vòng lặp (iterations) (Figure 6) chứng minh cơ chế tinh chỉnh tiến hóa (evolutionary refinement) là yếu tố quyết định để duy trì đà tối ưu:
    - *Biến thể không có tinh chỉnh tiến hóa (LLM-FE w/o evolutionary refinement)*: Đạt cải thiện sớm ở các vòng đầu (tăng từ $\approx 0.7513$ lên $\approx 0.7561$ tại vòng $3$), nhưng ngay sau đó đi ngang hoàn toàn (quickly plateaus), phản ánh việc mô hình bị kẹt sớm tại điểm cực trị địa phương (local optimum).
    - *LLM-FE với tinh chỉnh tiến hóa đầy đủ*: Liên tục duy trì đà tăng trưởng qua các thế hệ; thực hiện bước nhảy vọt tại vòng $10$ ($\approx 0.7643$) và tiếp tục tối ưu đạt đỉnh $\approx 0.7660$ ở vòng $19$.
  - **Hình 6.** Phân tích quỹ đạo hiệu năng kiểm định qua các vòng lặp tiến hóa
    - <img src="assets/fig_06_p10_vector.png" alt="Hình 6" />
    - **Hình này chứng minh điều gì**
      - Cơ chế tinh chỉnh tiến hóa giúp LLM-FE liên tục thoát khỏi cực trị địa phương để nâng cao hiệu năng qua các thế hệ.
    - **Từ đâu mà thấy được**
      - Trục hoành là Iterations (0-20), trục tung là Validation Accuracy: biến thể w/o Evolutionary Refinement đi ngang tại 0.7561 từ vòng 3, trong khi LLM-FE nhảy vọt ở vòng 10 (~0.7643) và đạt đỉnh ~0.7660 ở vòng 19.

- **Cơ chế vượt qua cực trị địa phương để tối ưu hóa hiệu quả (Escaping local optima)**:
  - Cơ chế tìm kiếm tiến hóa kết hợp vòng lặp phản hồi dựa trên dữ liệu thực nghiệm (data-driven feedback) trao cho LLM-FE khả năng thoát khỏi các điểm cực trị địa phương (local optima) mà các phương pháp tạo đặc trưng tĩnh hoặc tối ưu một lần không thể vượt qua.
  - Các phân tích thực nghiệm chi tiết và mở rộng được cung cấp thêm tại Phụ lục E (Appendix E).
