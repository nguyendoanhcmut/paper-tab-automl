## Tóm tắt (Abstract)

- **Vai trò của Kỹ thuật Đặc trưng Tự động (Automated Feature Engineering - AutoFE)**:
  - Kỹ thuật đặc trưng tự động đóng vai trò then chốt trong việc cải thiện hiệu năng của mô hình dự đoán (predictive model performance) đối với các tác vụ học máy trên dữ liệu bảng (tabular learning tasks).

- **Hạn chế của các phương pháp AutoFE truyền thống**:
  - Phụ thuộc vào các phép biến đổi tiền định (pre-defined transformations) bên trong các không gian tìm kiếm (search spaces) cố định, được thiết kế thủ công.
  - Thường xuyên bỏ qua tri thức miền (domain knowledge) về ngữ nghĩa thực tế của các thuộc tính dữ liệu.

- **Thách thức của các phương pháp ứng dụng Mô hình Ngôn ngữ Lớn (Large Language Models - LLMs) hiện nay**:
  - *Cơ hội*: Các bước tiến gần đây của LLMs đã cho phép tích hợp tri thức miền phong phú vào quy trình kỹ thuật đặc trưng.
  - *Hạn chế tồn đọng*: Các giải pháp dựa trên LLM hiện thời chủ yếu áp dụng cơ chế gợi ý trực tiếp (direct prompting) hoặc chỉ dựa đơn thuần vào điểm kiểm định (validation scores) để chọn lọc đặc trưng (feature selection).
  - *Hệ quả*: Thất bại trong việc khai thác tri thức tích lũy (insights) từ các thử nghiệm khám phá đặc trưng trước đó, đồng thời chưa thiết lập được lập luận suy diễn có ý nghĩa (meaningful reasoning) liên kết giữa quá trình sinh đặc trưng và hiệu năng thực nghiệm định hướng bởi dữ liệu (data-driven performance).

- **Đề xuất Khung làm việc LLM-FE**:
  - Giới thiệu **LLM-FE**, một khung làm việc mới lạ kết hợp giữa tìm kiếm tiến hóa (evolutionary search) với tri thức miền và năng lực suy luận (reasoning capabilities) của LLM nhằm tự động phát hiện các đặc trưng hiệu quả cho dữ liệu dạng bảng.
  - **Mô hình hóa bài toán**: LLM-FE thiết lập bài toán kỹ thuật đặc trưng dưới dạng bài toán tìm kiếm chương trình (program search problem).
  - **Cơ chế vận hành**: LLM đề xuất lặp đi lặp lại các chương trình biến đổi đặc trưng mới (feature transformation programs), trong khi phản hồi dựa trên dữ liệu (data-driven feedback) đóng vai trò định hướng toàn bộ không gian tìm kiếm.

- **Kết quả Thực nghiệm và Tính Tổng quát hóa (Generalizability)**:
  - Các kết quả thực nghiệm chứng minh LLM-FE vượt trội nhất quán so với các phương pháp cơ sở hiện đại nhất (state-of-the-art baselines).
  - Khẳng định khả năng tổng quát hóa mạnh mẽ trên nhiều kiến trúc mô hình, tác vụ học máy và tập dữ liệu đa dạng.

- **Tính khả dụng của mã nguồn**:
  - Mã nguồn hoàn chỉnh của nghiên cứu được công khai tại: [https://github.com/nikhilsab/LLMFE](https://github.com/nikhilsab/LLMFE).
