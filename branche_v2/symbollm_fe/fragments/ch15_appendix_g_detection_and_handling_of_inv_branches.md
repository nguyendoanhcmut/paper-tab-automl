## Appendix G Detection and Handling of Invalid or Inexecutable LLM-Generated Code

### G.1 Current Error-Handling Pipeline

- Đường ống xử lý mã nguồn do LLM tạo ra (LLM code processing pipeline) trong cơ sở mã (codebase) áp dụng phương pháp tiếp cận heuristic 3 giai đoạn (three-stage heuristic approach), không có cơ chế phục hồi lỗi hình thức (formal error recovery):
  - **Giai đoạn 1 (Stage 1) - Loại bỏ định dạng đánh dấu (Markup stripping):**
    - Phản hồi thô từ LLM (raw LLM response) trải qua một chuỗi các thao tác thay thế chuỗi ký tự (`replace("```python", "")`, `replace("```end", "")`, `replace("```", "")`, v.v.) nhằm loại bỏ các ký tự phân tách khối mã Markdown (markdown code-block delimiters).
    - Phương pháp tiếp cận này giả định ngầm định về sự tuân thủ nghiêm ngặt đối với định dạng đầu ra quy định (prescribed output format); bất kỳ sự sai lệch nào về cú pháp ký tự phân tách (delimiter syntax) đều khiến phần đánh dấu dư thừa (residual markup) làm nhiễm bẩn mã nguồn có thể thực thi (executable code).
  - **Giai đoạn 2 (Stage 2) - Lọc ở cấp độ dòng (Line-level filtering):**
    - Văn bản đã loại bỏ đánh dấu được tách thành từng dòng, và chỉ những dòng bắt đầu bằng `df` mà không phải là `df.drop` mới được giữ lại.
    - Bộ lọc này mang nhiều dạng lỗi đã biết (known failure modes):
      - *(i)* Các câu lệnh kỹ thuật đặc trưng hợp lệ (legitimate feature-engineering statements) không bắt đầu bằng `df` (ví dụ: các phép gán số học độc lập - standalone arithmetic assignments, câu lệnh nhập thư viện - `import` statements) bị âm thầm loại bỏ (silently discarded).
      - *(ii)* Các dòng có khoảng trắng (whitespace) đứng trước tiền tố `df` có thể bị loại trừ sai (falsely excluded).
      - *(iii)* Hoàn toàn không có bước xác thực (no validation) để kiểm tra xem các tên cột được tham chiếu (referenced column names) có tồn tại trong DataFrame hiện tại hay không.
  - **Giai đoạn 3 (Stage 3) - Thực thi mạnh mẽ kèm phản hồi lỗi (Robust execution with error feedback):**
    - Chuỗi mã nguồn sau khi lọc được thực thi bên trong một khối `try–except`.
    - Trường hợp thực thi thành công: Kết quả được ghi nhận (captured).
    - Trường hợp phát sinh ngoại lệ (ví dụ: lỗi cú pháp - syntactic errors, biến chưa được định nghĩa - undefined variables, hoặc ngoại lệ khi chạy - runtime exceptions): Thông báo lỗi cụ thể và vết ngăn xếp (traceback) sẽ được bắt giữ lại.
    - Cơ chế tự sửa lỗi (self-correction): Thông tin lỗi này được tự động cung cấp ngược lại cho LLM dưới dạng ngữ cảnh (context), thúc đẩy mô hình phân tích nguyên nhân lỗi và tạo lại mã nguồn đã sửa (regenerate corrected code), nhờ đó ngăn chặn việc đứt gãy đường ống xử lý (pipeline termination) và kích hoạt khả năng tự sửa lỗi (self-correction).

### G.2 Accepted Feature Ratio and Empirical Failure Rate

- Tỷ lệ chấp nhận và độ tin cậy thực nghiệm của các thành phần sinh đặc trưng:
  - Hồi quy ký hiệu (Symbolic regression) đạt tỷ lệ chấp nhận $100\%$ (100% acceptance rate), luôn mang lại các cột dự đoán hợp lệ về mặt số học (numerically valid prediction columns) cho mỗi lần khớp mô hình (fit).
  - Song song với đó, mã nguồn do LLM tạo ra thể hiện tỷ lệ thành công vững chắc (robust success rate) đạt $92.6\%$ trong các đánh giá quy mô lớn (large-scale evaluations).
  - Kết quả này phản ánh độ tin cậy cao (high reliability) trong việc sản sinh logic kỹ thuật đặc trưng có thể thực thi mà không đòi hỏi can thiệp thủ công sâu rộng (extensive manual intervention).
- Phân tích thống kê chi tiết theo Table 13 (Statistical analysis of ablation study results):
  - Thống kê chi tiết kết quả kiểm định thống kê và độ ổn định của các biến thể trong nghiên cứu cắt bỏ (ablation study variants):
    - **Baseline**: Độ chính xác (Accuracy) $75.81$, độ lệch chuẩn (Std) $\pm 0.45$, khoảng tin cậy $95\%$ (95% Confidence Interval) $[74.93, 76.69]$, giá trị $p$ ($p$-value so với Ours) $< 0.001$, có ý nghĩa thống kê (Significant: Yes).
    - **w/oSP** (loại bỏ sắp xếp trước đặc trưng theo tương quan Spearman): Độ chính xác $76.07$, độ lệch chuẩn $\pm 0.51$, khoảng tin cậy $95\%$ $[75.07, 77.07]$, giá trị $p < 0.001$, có ý nghĩa thống kê (Significant: Yes).
    - **w/oES** (loại bỏ cơ chế cửa sổ mở rộng - trượt): Độ chính xác $75.92$, độ lệch chuẩn $\pm 0.58$, khoảng tin cậy $95\%$ $[74.78, 77.06]$, giá trị $p < 0.001$, có ý nghĩa thống kê (Significant: Yes).
    - **w/oLLM** (loại bỏ sinh đặc trưng bằng LLM): Độ chính xác $76.84$, độ lệch chuẩn $\pm 0.41$, khoảng tin cậy $95\%$ $[76.03, 77.65]$, giá trị $p = 0.0142$, có ý nghĩa thống kê (Significant: Yes).
    - **Ours** (SymboLLM-FE đầy đủ): Độ chính xác cao nhất đạt $77.16$, độ lệch chuẩn $\pm 0.34$, khoảng tin cậy $95\%$ $[76.49, 77.83]$, không cần tính giá trị $p$ đối chiếu.

| Variants | Accuracy | Std | 95% Confidence Interval | p-value (vs. Ours) | Significant? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Baseline | $75.81$ | $\pm 0.45$ | $[74.93, 76.69]$ | $< 0.001$ | Yes |
| w/oSP | $76.07$ | $\pm 0.51$ | $[75.07, 77.07]$ | $< 0.001$ | Yes |
| w/oES | $75.92$ | $\pm 0.58$ | $[74.78, 77.06]$ | $< 0.001$ | Yes |
| w/oLLM | $76.84$ | $\pm 0.41$ | $[76.03, 77.65]$ | $0.0142$ | Yes |
| Ours | $\mathbf{77.16}$ | $\pm 0.34$ | $[76.49, 77.83]$ | - | - |
