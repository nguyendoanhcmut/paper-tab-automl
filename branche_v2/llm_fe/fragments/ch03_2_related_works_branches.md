## 2 Related Works

### Kỹ thuật đặc trưng (Feature Engineering)
- **Bản chất và mục tiêu của Feature Engineering**: Feature engineering (kỹ thuật đặc trưng) là quá trình tạo ra các đặc trưng có ý nghĩa từ raw data (dữ liệu thô) nhằm nâng cao predictive performance (hiệu năng dự đoán) của mô hình học máy (Hollmann et al., 2024).
- **Nhu cầu tự động hóa**: Độ phức tạp ngày càng gia tăng của các tập dữ liệu đã thúc đẩy sự phát triển của automated feature engineering (kỹ thuật đặc trưng tự động) nhằm cắt giảm công sức thủ công và tối ưu hóa quá trình khám phá đặc trưng.
- **Các phương pháp truyền thống**: Các kỹ thuật tự động hóa truyền thống chủ yếu bao gồm:
  - Tree-based exploration (thám hiểm dựa trên cây)
  - Transformation enumeration (liệt kê phép biến đổi toán tử)
  - Learning-based methods (các phương pháp dựa trên học máy) (Khurana et al., 2016; Kanter & Veeramachaneni, 2015; Nargesian et al., 2017; Zhang et al., 2023).
- **Rào cản của phương pháp truyền thống và tiềm năng của LLM**: Các phương pháp tiếp cận truyền thống thường thất bại trong việc tận dụng domain knowledge (tri thức miền) để phát hiện đặc trưng mới. Ngược lại, Large Language Models (LLMs - các mô hình ngôn ngữ lớn) lại đặc biệt phù hợp cho các bài toán tabular prediction (dự đoán trên dữ liệu dạng bảng) nhờ sở hữu prior contextual domain understanding (hiểu biết ngữ cảnh miền tiên nghiệm) phong phú.

### LLM và Tối ưu hóa (LLMs and Optimization)
- **Khả năng thích ứng không cần huấn luyện lại**: Những bước tiến của LLM chứng minh chúng có thể thích ứng linh hoạt với các tác vụ mới lạ thông qua prompt engineering (kỹ nghệ câu nhắc) và in-context learning (học trong ngữ cảnh) mà không đòi hỏi huấn luyện lại mô hình (Brown et al., 2020; Wei et al., 2022).
- **Hạn chế về tính ổn định và tính chính xác**: Đầu ra của LLM vẫn thường gặp hiện tượng thiếu nhất quán hoặc sai lệch về mặt thực tế (factually incorrect) (Madaan et al., 2024; Zhu et al., 2023), đặt ra yêu cầu cấp thiết về các cơ chế giúp tinh chỉnh (refine) hoặc ổn định hóa kết quả sinh ra.
- **Kết hợp LLM với khung làm việc tiến hóa (Evolutionary Frameworks)**: Một làn sóng nghiên cứu đang phát triển mạnh mẽ đã kết hợp LLM với các bộ đánh giá (evaluators) trong các khuôn khổ lặp hoặc tiến hóa, sử dụng feedback (phản hồi), mutation (đột biến), và crossover (lai ghép) để dẫn đường cho không gian tìm kiếm giải pháp (Lehman et al., 2023; Wu et al., 2024; Meyerson et al., 2024).
- **Các lĩnh vực ứng dụng thành công**: Mô hình tiếp cận này đã đạt được nhiều đột phá trong:
  - Prompt optimization (tối ưu hóa câu nhắc) (Yang et al., 2024b; Guo et al., 2024)
  - Neural architecture search (NAS - tìm kiếm kiến trúc mạng nơ-ron) (Zheng et al., 2023; Chen et al., 2023)
  - Mathematical heuristic discovery (khám phá thuật toán phỏng đoán/heuristic toán học) (Romera-Paredes et al., 2024)
  - Symbolic regression (hồi quy tượng trưng) (Shojaee et al., 2025).
- **Định vị của LLM-FE**: Kế thừa và phát triển định hướng này, khung làm việc LLM-FE hiện thực hóa LLM dưới vai trò là các evolutionary optimizers (bộ tối ưu hóa tiến hóa), kết hợp tri thức tiên nghiệm sâu rộng của mô hình với quy trình tinh chỉnh có hệ thống dựa trên dữ liệu (data-driven refinement) để khám phá các đặc trưng vừa cô đọng (compact), vừa đạt hiệu năng vượt trội.

### LLM cho Học trên dữ liệu bảng (LLMs for Tabular Learning)
- **Tiếp cận LLM trên dữ liệu có cấu trúc**: Việc áp dụng LLM cho structured data (dữ liệu có cấu trúc) thường dựa vào hai hướng chính:
  - Chuyển đổi bảng biểu thành textual representations (biểu diễn dạng văn bản) (Dinh et al., 2022; Hegselmann et al., 2023; Wang et al., 2023).
  - Tùy biến chiến lược tokenization (phân đoạn từ) và pre-training (tiền huấn luyện) chuyên biệt để nâng cao độ bền vững trên dữ liệu bảng (Yan et al., 2024).
- **Ứng dụng trong dự đoán và kỹ thuật đặc trưng trên dữ liệu bảng**:
  - LLM được triển khai dưới các mô hình fine-tuning (tinh chỉnh) hoặc few-shot in-context learning (Hegselmann et al., 2023; Nam et al., 2023).
  - Trực tiếp thực hiện kỹ thuật đặc trưng: FeatLLM sinh các binary rules (luật nhị phân) (Han et al., 2024); CAAFE tận dụng bản mô tả tác vụ để sinh các đặc trưng theo ngữ cảnh (Hollmann et al., 2024); OCTree tinh chỉnh lặp các đặc trưng thông qua suy luận cây quyết định (decision tree reasoning) (Nam et al., 2024).
- **Điểm nghẽn của các phương pháp đi trước**: Các phương pháp trên chủ yếu dựa vào việc tinh chỉnh tăng dần trên một ứng viên duy nhất (incremental refinement of a single candidate), dễ dẫn đến bế tắc cục bộ và hạn chế không gian tìm kiếm.
- **Cơ chế đột phá của LLM-FE**:
  - LLM-FE duy trì một diverse pool (bể chứa đa dạng) các chương trình biến đổi tiềm năng.
  - Sử dụng evolutionary search (tìm kiếm tiến hóa) để duyệt qua feature space (không gian đặc trưng) một cách hiệu quả.
  - Tận dụng mutation (đột biến) và crossover (lai ghép) để khai phá các phép biến đổi vừa có căn cứ dữ liệu (data-driven) vừa có khả năng diễn giải cao (interpretable transformations).
- **Giá trị cốt lõi**: Thiết kế này giúp phát hiện các đặc trưng không chỉ cải thiện độ chính xác dự đoán mà còn hoàn toàn dễ hiểu đối với con người, thu hẹp khoảng cách giữa domain-informed reasoning (suy luận dựa trên tri thức miền) và quá trình tối ưu hóa thực nghiệm. Phụ lục A (Appendix A) phân tích rõ hơn sự khác biệt định tính giữa LLM-FE và các phương pháp baseline.
