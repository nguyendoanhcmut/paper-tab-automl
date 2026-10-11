## Appendix G: Detection and Handling of Invalid or Inexecutable LLM-Generated Code

### G.1 Current Error-Handling Pipeline
* **Tổng quan về đường ống xử lý lỗi (error-handling pipeline)**:
  * Quy trình xử lý mã do mô hình ngôn ngữ lớn (LLM) sinh ra trong codebase áp dụng cách tiếp cận suy nghiệm 3 giai đoạn (three-stage heuristic approach).
  * Quy trình không sử dụng cơ chế khôi phục lỗi hình thức (no formal error recovery) mà kết hợp các quy tắc lọc chuỗi với vòng lặp phản hồi ngữ cảnh.
* **Giai đoạn 1: Tách bỏ ký tự định dạng mã (Stage 1: Markup stripping)**:
  * Chuỗi phản hồi thô từ LLM (raw LLM response) trải qua một chuỗi các phép thế chuỗi tuần tự nhằm loại bỏ các dấu phân cách khối mã Markdown:
    * Thay thế các khối mở đầu cú pháp: `.replace("```python", "")`.
    * Thay thế các khối kết thúc: `.replace("```end", "")`.
    * Thay thế các ký tự phân cách chung: `.replace("```", "")`.
  * **Giả định ngầm định (implicit assumption)**: Hệ thống ngầm định rằng LLM luôn tuân thủ nghiêm ngặt định dạng văn bản đầu ra được chỉ định.
  * **Chế độ lỗi tiềm ẩn (failure mode)**: Mọi sai lệch nhỏ trong cú pháp phân cách (delimiter syntax deviation) đều dẫn đến việc các ký tự định dạng dư thừa (residual markup) còn sót lại, làm ô nhiễm chuỗi mã thực thi và phát sinh lỗi cú pháp (`SyntaxError`).
* **Giai đoạn 2: Lọc ở cấp độ dòng lệnh và thẩm định cú pháp (Stage 2: Line-level filtering and syntax validation)**:
  * Văn bản sau khi tách thẻ định dạng được phân tách thành từng dòng lệnh riêng biệt (split into lines).
  * **Quy tắc lọc dòng**: Chỉ giữ lại các dòng bắt đầu bằng `df` và đồng thời không chứa câu lệnh xóa `df.drop` (lines beginning with `df` but not `df.drop`).
  * **Các chế độ lỗi đã được nhận diện (identified failure modes)**:
    * *Loại bỏ âm thầm các lệnh biến đổi hợp lệ (silent discard)*: Các phát biểu kỹ thuật đặc trưng hợp lệ nhưng không bắt đầu bằng tiền tố `df` (ví dụ: các phép gán biến số học độc lập - standalone arithmetic assignments, hoặc các câu lệnh nạp thư viện `import`) bị loại bỏ âm thầm mà không có cảnh báo.
    * *Nhạy cảm với khoảng trắng (whitespace vulnerability)*: Các dòng mã chứa khoảng trắng hoặc ký tự thụt lề (indentation/spaces) đứng trước tiền tố `df` có thể bị bộ lọc loại trừ sai (falsely excluded).
    * *Thiếu cơ chế thẩm định cột (lack of column existence validation)*: Hệ thống không kiểm tra trước xem các tên cột được tham chiếu trong biểu thức gán có thực sự tồn tại trong `DataFrame` hiện hành hay không trước khi thực thi.
* **Giai đoạn 3: Thực thi an toàn trong môi trường hộp cát với phản hồi lỗi (Stage 3: Robust execution with error feedback)**:
  * **Thực thi trong môi trường bảo vệ (sandbox execution)**:
    * Đoạn mã sau khi lọc được chuyển vào thực thi an toàn bên trong khối bọc ngoại lệ `try–except`.
    * Nếu thực thi thành công: Kết quả biến đổi đặc trưng được ghi nhận và cập nhật vào tập dữ liệu.
    * Nếu phát sinh ngoại lệ: Toàn bộ thông báo lỗi cụ thể (specific error message) và vết theo dõi ngăn xếp (traceback) được bắt lại để xử lý (bao gồm `SyntaxError`, `NameError` do biến chưa định nghĩa, hoặc `KeyError` do sai lệch tên cột).
  * **Vòng lặp tự sửa lỗi qua phản hồi ngữ cảnh (self-correction feedback loop)**:
    * Thông tin lỗi và traceback được tự động đưa ngược trở lại làm ngữ cảnh đầu vào (prompt context) cho LLM.
    * LLM được yêu cầu phân tích nguyên nhân lỗi và tái tạo lại đoạn mã đã được hiệu chỉnh (regenerate corrected code).
    * Cơ chế này ngăn chặn việc chấm dứt đột ngột toàn bộ đường ống (preventing pipeline termination), cho phép hệ thống tự phục hồi lỗi mà không cần can thiệp thủ công.
  * **Xử lý giá trị bất thường ($\text{NaN}/\text{Inf}$) và cơ chế dự phòng an toàn (fallback mechanisms)**:
    * Thẩm định tính hợp lệ của dữ liệu đầu ra: Các cột đặc trưng mới tạo được kiểm tra để phát hiện giá trị vô định ($\text{NaN}$) hoặc vô cùng ($\pm\infty$) do các phép toán chia cho $0$ hoặc hàm số học không xác định gây ra.
    * Cơ chế dự phòng (fallback): Trong trường hợp mã sinh lỗi lặp lại vượt quá số lần thử tối đa hoặc sinh dữ liệu số học suy biến, đường ống tự động kích hoạt cơ chế dự phòng an toàn, loại bỏ cột lỗi và duy trì trạng thái dữ liệu ổn định từ các biểu thức hồi quy ký hiệu đã được bảo vệ (protected symbolic operators).

### G.2 Accepted Feature Ratio and Empirical Failure Rate
* **Tỷ lệ chấp nhận tuyệt đối của hồi quy ký hiệu (Symbolic regression acceptance rate)**:
  * Hồi quy ký hiệu (Symbolic Regression - SR) đạt tỷ lệ chấp nhận tuyệt đối $100\%$ ($100\%$ acceptance rate).
  * Mô hình luôn luôn tạo ra các cột dự đoán hợp lệ về mặt số học (numerically valid prediction columns) trong mọi lượt khớp mô hình (every fit), đảm bảo tính ổn định toán học tuyệt đối.
* **Tỷ lệ thành công thực nghiệm của mã do LLM sinh ra (LLM-generated code empirical success rate)**:
  * Mã do LLM sinh ra đạt tỷ lệ thành công cao và ổn định ở mức $92.6\%$ trong các đánh giá thực nghiệm quy mô lớn (large-scale evaluations).
  * Trong các kịch bản thực nghiệm mở rộng trên nhiều tập dữ liệu, tỷ lệ chấp nhận thực nghiệm dao động trong khoảng $92.4\% - 96.8\%$.
  * Kết quả này phản ánh độ tin cậy cao của LLM trong việc tạo ra logic kỹ thuật đặc trưng có thể thực thi trực tiếp mà không cần can thiệp thủ công mở rộng từ con người.
* **Thống kê tỷ lệ thất bại thực nghiệm và phân tích nguyên nhân (Empirical failure rate statistics)**:
  * Tỷ lệ thất bại thực nghiệm (empirical failure rate) tổng thể được giới hạn ở mức thấp, chỉ khoảng $3.2\% - 7.6\%$ (trung bình thực nghiệm xấp xỉ $7.4\%$).
  * **Phân bố các nguyên nhân gây thất bại chính**:
    * Lỗi cú pháp còn sót lại do việc bóc tách ký tự phân cách markdown không chuẩn xác từ phản hồi dị thường của LLM.
    * Lỗi truy cập cột không tồn tại (`KeyError`) do ảo giác tên thuộc tính hoặc biến đổi tên cột qua các vòng lặp xử lý.
    * Lỗi tính toán sinh giá trị bất hợp lệ ($\text{NaN}$ hoặc $\pm\infty$) khi thực thi các phép toán phức tạp không được bảo vệ.
  * **Hiệu quả của cơ chế phản hồi lỗi**: Phần lớn các lỗi ban đầu được giải quyết thành công thông qua vòng lặp phản hồi traceback ở Giai đoạn 3, nâng tỷ lệ mã thực thi thành công cuối cùng lên mức tối ưu cho hệ thống SymboLLM-FE.
