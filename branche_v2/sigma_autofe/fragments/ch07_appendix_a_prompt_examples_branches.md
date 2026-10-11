## Appendix A. Prompt Examples

- Khung mẫu prompt tổng thể (Listing 1: Overall Prompt Template) được thiết kế để chỉ dẫn mô hình ngôn ngữ lớn (LLM) thực hiện kỹ thuật đặc trưng hóa tự động (AutoFE):
  - Vai trò hệ thống (System role): Thiết lập LLM đóng vai trò là một chuyên gia khoa học dữ liệu (data science expert) với nhiệm vụ tối ưu hóa phân phối đặc trưng (optimizing feature distribution) nhằm cải thiện hiệu năng của mô hình phân loại `<CLS_MODEL>` trên bài toán phân loại `<N>` lớp (`<N>-class classification problem`).
  - Phân tích dữ liệu hiện tại (Current Data Analysis):
    - Tổ chức đặc trưng (Feature Organization): Chứa phần mô tả phân nhóm/gom nhóm đặc trưng (`<GROUPINGDESCRIPTION>`).
    - Định dạng đặc trưng (Format): Định rõ định dạng biểu diễn đặc trưng (`<FEATURE_FORMAT>`) cùng các khối thông tin đặc trưng chi tiết (`<FEATURE_BLOCKS>`).
  - Nhiệm vụ cần thực hiện (Your Task):
    - Yêu cầu sinh mã nguồn bắt buộc (Code Generation - Required): Chỉ dẫn LLM sinh ra đúng 2 hàm Python riêng biệt (`TWO separate Python functions`), mỗi hàm tạo ra đúng 1 đặc trưng mới duy nhất (`ONE new feature`).
    - Thông tin phép toán (`<OPERATIONS_INFO>`): Cung cấp thông tin và ràng buộc về các phép biến đổi toán học/thao tác đặc trưng được áp dụng.
    - Cấu trúc đặc tả từng hàm:
      - Hàm 1 (`Function 1: <FUNCTION_1_TITLE>`): Quy định mục đích cụ thể (`<FUNCTION_1_PURPOSE>`) và các yêu cầu triển khai (`<FUNCTION_1_REQUIREMENTS>`).
      - Hàm 2 (`Function 2: <FUNCTION_2_TITLE>`): Quy định mục đích cụ thể (`<FUNCTION_2_PURPOSE>`) và các yêu cầu triển khai (`<FUNCTION_2_REQUIREMENTS>`).
