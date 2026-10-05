## Appendix B Prompt

- Phần phụ lục cung cấp mẫu câu lệnh (prompt templates) chuẩn hóa dùng cho sinh mã nguồn (code generation) trong khuôn khổ SymboLLM-FE.
- Cấu trúc chi tiết của mẫu câu lệnh dùng cho sinh mã nguồn (`Prompt used for Code Generation`):
  - Khai báo vai trò và nhiệm vụ (`Task Description`):
    - Mô hình ngôn ngữ lớn (LLM) được chỉ định đóng vai trò chuyên gia khoa học dữ liệu (expert data scientist) với nhiệm vụ cải thiện mô hình phân loại xuôi dòng (downstream classification model) bằng cách sinh các đặc trưng mới và loại bỏ các đặc trưng dư thừa.
    - Biến mục tiêu (target variable) được thiết lập cố định là `class`.
    - Nguyên văn chỉ dẫn: *"You are an expert data scientist tasked with improving a downstream classification model by generating new features and dropping redundant ones. The target variable is ‘class‘."*
  - Thông tin bộ dữ liệu (`Dataset Information`):
    - Bộ dữ liệu gốc có $N$ cột, được đặt tên tuần tự từ `X{0}` đến `X{N-1}` (*"The raw dataset has {N} columns named from ‘X{0}‘ to ‘X{N-1}‘"*).
    - Nhiệm vụ xuôi dòng (downstream task) được xác định là `{regression / classification}` (hồi quy hoặc phân loại), đi kèm thước đo đánh giá tương ứng là `{accuracy / RMSE}` (*"The downstream task is {regression / classification}, and the evaluation metric is {accuracy / RMSE}"*).
  - Tri thức tiên nghiệm từ bộ hồi quy ký hiệu (`Prior Knowledge from Symbolic Regressor`):
    - Cung cấp bảng quy tắc ký hiệu rút ra từ bộ dữ liệu, biểu diễn cách xấp xỉ biến mục tiêu bằng việc kết hợp các tập con đặc trưng chọn lọc.
    - Chỉ số sai số tuyệt đối trung bình (Mean Absolute Error - MAE) thể hiện hiệu năng của mô hình hồi quy ký hiệu trên tập kiểm tra ứng với từng công thức tương ứng (*"The MAE indicates the performance of the Symbolic Regressor model on the test set using the corresponding formula"*).
    - Cấu trúc bảng quy tắc gồm hai cột `Formula` và `MAE`:
      | Formula | MAE |
      | :--- | :--- |
      | `{rule1}` | `{mae1}` |
      | `{rule2}` | `{mae2}` |
      | `...` | `...` |
  - Chỉ dẫn chiến lược sinh đặc trưng (`Instructions`):
    - LLM được yêu cầu xem xét bao quát các công thức toán học cùng mức độ hiệu năng tương ứng của chúng, tận dụng tri thức tiên nghiệm để đề xuất các đặc trưng mới giúp nâng cao hiệu năng mô hình (*"Please consider these formulas and their performance comprehensively. Make full use of your prior knowledge to propose new features that can further improve the model’s performance"*).
    - Các đặc trưng mới có thể được dẫn xuất trực tiếp từ các công thức toán học bên dưới, nhưng LLM tuyệt đối không được chuyển đổi đơn thuần toàn bộ các công thức (*"New features can be directly derived from the formulas below, but you should **not** simply convert all formulas"*).
    - Thay vào đó, LLM bắt buộc phải phân tích tổng thể tất cả các công thức và kiểm tra mối liên hệ tương hỗ giữa các đặc trưng (*"Instead, you must analyze all formulas holistically and examine the relationships between the features"*).
  - Yêu cầu kỹ thuật đối với mã nguồn sinh ra (`Code Requirements`):
    - LLM viết mã Python để tạo thêm các cột và tùy chọn loại bỏ các cột dư thừa; mã nguồn được đánh giá trên tập kiểm tra giữ lại (holdout set) dựa trên độ chính xác (`accuracy`).
    - Quy ước đặt tên biến (`Naming Convention`): Tên cột mới bắt buộc phải tuân theo quy ước đặt tên hiện có; nếu cột cuối cùng hiện tại là `X{k}`, cột mới đầu tiên phải được đặt tên là `X{k+1}`, kế tiếp là `X{k+2}`, và tiếp diễn tương tự (*"New column names must follow the existing naming scheme. If the last existing column is ‘X{k}‘, the first new column should be named ‘X{k+1}‘, then ‘X{k+2}‘, and so on"*).
    - Định dạng khi thêm cột (`Format for Adding Columns`): Mỗi cột tạo mới bắt buộc phải kèm khối chú thích gồm ba trường thông tin: tên đặc trưng (`Feature name`), lý do đề xuất (`Reason`), và mức độ hữu dụng (`Usefulness`) trong việc phân loại Class theo các quy tắc đã cho:
      ```python
      # Feature name: new_feature_name
      # Reason: why this feature is proposed
      # Usefulness: how it helps classify Class according to given rules
      df['Xnext_index'] = ... # computation using existing columns
      ```
    - Định dạng khi loại bỏ cột (`Format for Dropping Columns`): Mỗi thao tác loại bỏ cột bắt buộc phải kèm lời giải thích lý do vì sao cột đó là dư thừa hoặc gây hại:
      ```python
      # Explanation: why this column is redundant or harmful
      df.drop(columns=['Xcol_index'], inplace=True)
      ```
    - Quy tắc định dạng khối mã (`Code Block Rules`):
      - Mỗi khối mã bắt đầu bằng cú pháp ` ```python ` và kết thúc bằng ` ``` ` (*"Each code block starts with ‘ ```python ‘ and ends with ‘```‘"*).
      - Các cột mới tạo có thể được tái sử dụng trong các khối mã tiếp theo (*"Added columns can be used in subsequent code blocks"*).
      - Các cột đã bị loại bỏ sẽ không còn khả dụng (*"Dropped columns are no longer available"*).
  - Định dạng đầu ra mong muốn (`Output`):
    - LLM xuất ra một hoặc nhiều khối mã nguồn thực thi độc lập tuân thủ nghiêm ngặt định dạng quy định ở trên (*"Generate one or more code blocks following the above format"*).
