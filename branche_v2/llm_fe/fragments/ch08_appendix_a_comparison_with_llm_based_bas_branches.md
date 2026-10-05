## Appendix A Comparison with LLM-based Baselines

- **Khái quát so sánh phương pháp luận giữa LLM-FE và các phương pháp đối chuẩn dựa trên LLM**:
  - Mặc dù LLM-FE cùng hai phương pháp đối chuẩn tiêu biểu là CAAFE và OCTree đều tận dụng các mô hình ngôn ngữ lớn (Large Language Models - LLMs) cho kỹ thuật tạo đặc trưng tự động (Automated Feature Engineering - AutoFE), chúng có sự khác biệt căn bản (differ fundamentally) về cơ chế khám phá (explore) và tinh chỉnh (refine) không gian đặc trưng (feature space).
  - Bài báo chỉ ra 5 điểm khác biệt phương pháp luận cốt lõi (key methodological differences) giữa LLM-FE và các phương pháp đối chuẩn dựa trên LLM tiền nhiệm: (i) Khám phá song song và đa đường dẫn, (ii) Bộ nhớ dựa trên quần thể, (iii) Thiết kế phản hồi và tinh chỉnh, (iv) Tác động thực nghiệm, và (v) Độ phức tạp của đặc trưng.

### 1. Khám phá Song song và Đa đường dẫn (Parallel and Multi-Path Exploration)

- **Cơ chế tiến hóa đa ứng viên song song qua các đảo của LLM-FE**:
  - LLM-FE tiến hành thăm dò không gian đặc trưng theo phương thức song song (in parallel) thông qua việc tiến hóa đồng thời nhiều chương trình ứng viên (evolving multiple candidate programs simultaneously) phân bố trên các đảo độc lập (across islands).
  - Mô hình đa đảo (multi-island model) cho phép duy trì song song các quỹ đạo tìm kiếm tách biệt, thúc đẩy tính đa dạng của giải pháp và ngăn ngừa việc toàn bộ quá trình tìm kiếm bị chi phối bởi một hướng phát triển cục bộ duy nhất.
- **Hạn chế của quy trình tối ưu hóa đơn đường dẫn ở CAAFE và OCTree**:
  - Cả CAAFE và OCTree đều tuân theo quy trình tối ưu hóa đơn đường dẫn (single-path optimization process).
  - Trong quy trình này, LLM chỉ tinh chỉnh tăng dần (incrementally refines) duy nhất một ứng viên (single candidate) hoặc một quy tắc (rule) tại một thời điểm.
  - Cách tiếp cận tuần tự đơn luồng này hạn chế đáng kể độ bao phủ của không gian tìm kiếm tổ hợp và làm gia tăng nguy cơ mắc kẹt trong không gian nghiệm cục bộ.

### 2. Bộ nhớ Dựa trên Quần thể (Population-Based Memory)

- **Kiến trúc bộ nhớ ngoài đa quần thể của LLM-FE**:
  - Khác biệt rõ rệt so với CAAFE và OCTree, LLM-FE duy trì một bộ nhớ ngoài đa quần thể (multi-population external memory).
  - Bộ nhớ này có nhiệm vụ lưu trữ các chương trình biến đổi đặc trưng đa dạng và đạt hiệu năng cao (diverse, high-performing feature programs) xuyên suốt các vòng lặp tiến hóa (iterations).
  - Các chương trình ưu tú trong bộ nhớ được cấu trúc và phân cụm để chọn lọc làm các mẫu minh họa theo ngữ cảnh (in-context demonstrations) hiệu quả cho LLM trong các vòng tiếp theo.
- **Sự thiếu vắng bộ nhớ quần thể ở các phương pháp đối chuẩn**:
  - Cả CAAFE và OCTree đều không sở hữu cơ chế bộ nhớ quần thể bên ngoài để lưu trữ đa dạng các ứng viên xuất sắc xuyên suốt chiều dài tối ưu hóa, làm giới hạn khả năng tích lũy và truyền thừa tri thức khám phá giữa các thế hệ.

### 3. Thiết kế Cơ chế Phản hồi và Tinh chỉnh (Feedback and Refinement Design)

- **Cơ chế đột biến và lai ghép được LLM dẫn dắt trong LLM-FE**:
  - LLM-FE áp dụng các toán tử đột biến (mutation) và lai ghép (crossover) được dẫn dắt bởi LLM (LLM-guided operators) trên nhiều quần thể để thúc đẩy đồng thời cả hai quá trình thăm dò (exploration) và tái tổ hợp (recombination).
  - Cơ chế này cho phép LLM vừa đề xuất các biến đổi mới lạ, vừa kết hợp có chọn lọc các khối cấu trúc đặc trưng thành công từ nhiều chương trình giải pháp khác nhau.
- **Cơ chế tinh chỉnh quy tắc từng bước của OCTree**:
  - Ngược lại, OCTree dựa vào việc tinh chỉnh quy tắc từng bước (stepwise rule refinement) được định hướng bởi phản hồi từ cây quyết định (decision-tree feedback).
  - Phương pháp này chủ yếu điều chỉnh các điều kiện rẽ nhánh và ngưỡng phân chia của cây thay vì tái tổ hợp các biểu thức đặc trưng độc lập.
- **Cơ chế tinh chỉnh dựa trên câu lệnh nhắc của CAAFE**:
  - CAAFE sử dụng cơ chế tinh chỉnh dựa trên câu lệnh nhắc (prompt-based refinement) mà hoàn toàn không tích hợp các toán tử tiến hóa (evolutionary operators).
  - Việc cải tiến đặc trưng phụ thuộc đơn thuần vào việc viết lại prompt lặp đi lặp lại mà không có sự hỗ trợ của các phép toán tiến hóa cấu trúc.

### 4. Tác động Thực nghiệm (Empirical Impact)

- **Bảo toàn tính đa dạng và hạn chế hội tụ sớm**:
  - Chiến lược đa đảo (multi-island strategy) giúp giảm thiểu hiện tượng hội tụ sớm (premature convergence) bằng cách bảo toàn tính đa dạng (preserving diversity) giữa các quần thể đảo.
  - Điều này đảm bảo quá trình tìm kiếm không bị đình trệ ở các giải pháp tối ưu cục bộ kém chất lượng.
- **Thành quả vượt trội nhất quán trên dữ liệu thực nghiệm**:
  - Nhờ duy trì tính đa dạng và tái tổ hợp hiệu quả, LLM-FE đạt được các bước cải thiện thực nghiệm nhất quán (consistent empirical gains) so với cả CAAFE và OCTree.
  - Các kết quả định lượng vượt trội này được chứng minh cụ thể trong Bảng 2 và Bảng 3 (Tables 2 and 3) trên cả các tác vụ phân loại và hồi quy.

### 5. Độ phức tạp của Đặc trưng (Feature Complexity)

- **Hiện tượng thiên lệch về toán tử đơn giản trong y văn trước đây**:
  - Nghiên cứu của Küken et al. (2024) đã chứng minh rằng các phương pháp kỹ thuật đặc trưng dựa trên LLM thường có xu hướng thiên lệch mạnh mẽ về phía các toán tử đơn giản (favor simple feature operators), chỉ giới hạn ở các phép toán số học cơ bản.
- **Khả năng khắc phục thiên lệch toán tử của LLM-FE**:
  - Các kết quả thực nghiệm trình bày tại Hình 4 (Figure 4) khẳng định LLM-FE hóa giải thành công sự thiên lệch này:
    - Xấp xỉ $45\%$ các đặc trưng do LLM-FE phát hiện đạt tiêu chuẩn xếp loại là đặc trưng phức tạp (complex features) theo định nghĩa của Küken et al. (2024) (chẳng hạn như các toán tử phi tuyến và tổng hợp nhóm: `groupbythenmean`, `groupbythenmin`, `groupbythenmax`, `residual`, `sigmoid`).
    - Ngược lại, tỷ lệ đặc trưng phức tạp được tạo ra bởi CAAFE và OCTree là không đáng kể (negligible), cho thấy hai phương pháp này hầu như không thể thoát khỏi xu hướng lựa chọn toán tử tầm thường.
