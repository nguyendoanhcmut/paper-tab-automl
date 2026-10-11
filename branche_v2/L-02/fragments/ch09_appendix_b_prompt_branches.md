## Appendix B: Prompt

* **Mục đích và vai trò của Phụ lục B (Appendix B: Prompt):**
  * Cung cấp mẫu câu lệnh (prompt template) hoàn chỉnh được sử dụng trong SymboLLM-FE để hướng dẫn mô hình ngôn ngữ lớn (LLM) sinh mã Python (`Python code`) thực hiện tinh chỉnh và tái cấu trúc đặc trưng (feature refinement and generation).
  * Prompt được thiết kế có cấu trúc chặt chẽ nhằm tích hợp tri thức tiên nghiệm thu được từ hồi quy ký hiệu (Symbolic Regressor) vào quá trình tạo mã đặc trưng, đảm bảo tính diễn giải (interpretability) và hiệu năng mô hình hạ nguồn.

* **Mô tả nhiệm vụ và vai trò hệ thống (Task Description):**
  * **Định vị vai trò (System Role):** LLM được giao vai trò là một chuyên gia khoa học dữ liệu (expert data scientist).
  * **Mục tiêu cốt lõi:** Cải thiện mô hình phân loại/hồi quy hạ nguồn (downstream classification/regression model) bằng cách sinh ra các đặc trưng mới hữu ích và loại bỏ các đặc trưng dư thừa (redundant features) hoặc gây nhiễu.
  * **Biến mục tiêu (Target Variable):** Biến mục tiêu được xác định là `class` (hoặc nhãn mục tiêu cụ thể của tác vụ).

* **Thông tin tập dữ liệu được tham số hóa trong prompt (Dataset Information):**
  * **Đặc trưng ban đầu:** Tập dữ liệu thô gồm $N$ cột, được đánh số và đặt tên theo quy chuẩn từ `X{0}` đến `X{N-1}`.
  * **Tác vụ hạ nguồn (Downstream Task):** Tham số hóa theo tác vụ cụ thể, nhận giá trị `{regression / classification}` (hồi quy hoặc phân loại).
  * **Thước đo đánh giá (Evaluation Metric):** Tham số hóa theo nhiệm vụ, nhận giá trị `{accuracy / RMSE}` (độ chính xác hoặc căn bậc hai sai số toàn phương trung bình).

* **Đưa tri thức tiên nghiệm từ bộ hồi quy ký hiệu vào ngữ cảnh (Prior Knowledge from Symbolic Regressor):**
  * **Bản chất tri thức tiên nghiệm:** Cung cấp danh sách các quy tắc ký hiệu (symbolic rules) được trích xuất tự động từ tập dữ liệu bởi Symbolic Regressor.
  * **Ý nghĩa toán học:** Mỗi quy tắc thể hiện cách biến mục tiêu có thể được xấp xỉ thông qua sự kết hợp của các tập con đặc trưng được chọn lọc.
  * **Độ đo định lượng kèm theo:** Đi kèm với mỗi công thức là sai số tuyệt đối trung bình (Mean Absolute Error - $\text{MAE}$), phản ánh hiệu năng xấp xỉ của mô hình Symbolic Regressor trên tập kiểm thử (test set) khi sử dụng công thức tương ứng.
  * **Định dạng bảng công thức cung cấp cho LLM:**
    * Cột 1: `Formula` (Công thức ký hiệu, biểu thị dưới dạng các biểu thức toán học `{rule1}`, `{rule2}`, ...).
    * Cột 2: `MAE` (Giá trị sai số tuyệt đối trung bình tương ứng `{mae1}`, `{mae2}`, ...).

* **Chỉ dẫn thực thi và tư duy phân tích cho LLM (Instructions):**
  * **Yêu cầu phân tích tổng thể:** LLM phải cân nhắc toàn diện các công thức và hiệu năng ($\text{MAE}$) của chúng, vận dụng tối đa tri thức chuyên gia sẵn có để đề xuất các đặc trưng mới giúp nâng cao hiệu năng mô hình.
  * **Nguyên tắc không chuyển đổi máy móc:** Các đặc trưng mới có thể được dẫn xuất trực tiếp từ các công thức ký hiệu, nhưng LLM tuyệt đối **không được** chuyển đổi một cách đơn giản hay sao chép toàn bộ các công thức (must not simply convert all formulas).
  * **Phân tích tương quan chỉnh thể:** LLM bắt buộc phải phân tích toàn diện tất cả các công thức trong mối tương quan chỉnh thể (holistic analysis) và kiểm tra kỹ lưỡng mối quan hệ tương hỗ giữa các đặc trưng (relationships between features) trước khi quyết định tạo mới hoặc loại bỏ.

* **Yêu cầu kỹ thuật về mã nguồn (Code Requirements):**
  * **Ngôn ngữ thực thi:** LLM phải viết mã nguồn Python để tạo thêm các cột đặc trưng mới và tùy chọn loại bỏ các cột dư thừa/gây hại.
  * **Cơ chế đánh giá mã:** Mã nguồn sinh ra sẽ được tự động thực thi và đánh giá trên một tập kiểm định độc lập (holdout set) dựa trên độ chính xác (`accuracy`) hoặc $\text{RMSE}$.
  * **Quy ước đặt tên cột nghiêm ngặt (Naming Convention):**
    * Tên cột mới bắt buộc phải tuân theo sơ đồ đặt tên tuần tự hiện có của tập dữ liệu.
    * Nếu cột hiện có cuối cùng là `X{k}`, cột mới đầu tiên bắt buộc phải đặt tên là `X{k+1}`, cột tiếp theo là `X{k+2}`, và tiếp tục tăng dần tuần tự.
  * **Định dạng chuẩn hóa cho thao tác thêm cột (Format for Adding Columns):**
    * Mỗi thao tác tạo cột mới phải đi kèm khối chú thích (comment block) bắt buộc gồm 3 thành phần:
      * `# Feature name: new_feature_name` (Tên mô tả của đặc trưng mới).
      * `# Reason: why this feature is proposed` (Lý do đề xuất đặc trưng này).
      * `# Usefulness: how it helps classify Class according to given rules` (Độ hữu dụng: giải thích cách đặc trưng hỗ trợ phân loại hoặc dự đoán biến mục tiêu dựa trên các quy tắc đã cho).
    * Cú pháp tính toán:
      ```python
      # Feature name: new_feature_name
      # Reason: why this feature is proposed
      # Usefulness: how it helps classify Class according to given rules
      df['Xnext_index'] = ... # computation using existing columns
      ```
  * **Định dạng chuẩn hóa cho thao tác loại bỏ cột (Format for Dropping Columns):**
    * Mỗi cột bị loại bỏ phải có lời giải thích cụ thể về lý do:
      * `# Explanation: why this column is redundant or harmful` (Giải thích tại sao cột này bị dư thừa hoặc gây hại cho mô hình).
    * Cú pháp loại bỏ trực tiếp trên DataFrame:
      ```python
      # Explanation: why this column is redundant or harmful
      df.drop(columns=['Xcol_index'], inplace=True)
      ```
  * **Quy tắc thực thi khối mã (Code Block Rules):**
    * Mỗi khối mã phải bắt đầu bằng cú pháp ````python` và kết thúc bằng ````.
    * Tính kế thừa dữ liệu: Các cột mới được thêm vào hoàn toàn có thể được sử dụng làm biến đầu vào cho các khối mã hoặc phép tính tiếp theo.
    * Tính bất khả dụng sau khi xóa: Các cột đã bị loại bỏ (`dropped columns`) sẽ không còn tồn tại để sử dụng trong các bước tính toán sau.

* **Quy cách định dạng đầu ra (Output Format):**
  * LLM được yêu cầu tạo ra một hoặc nhiều khối mã Python hoàn chỉnh, tuân thủ chính xác tất cả các ràng buộc về cú pháp, chú thích giải thích và quy tắc đặt tên đã nêu.
