### B.2 Baselines

- **Tổng quan về thiết lập đối chuẩn (Baseline setup)**:
  - Nghiên cứu triển khai và đánh giá nhiều phương pháp đối chuẩn (baselines) kỹ thuật đặc trưng (feature engineering) tiên tiến nhất (state-of-the-art), bao phủ từ các phương pháp truyền thống đến các cách tiếp cận dựa trên mô hình ngôn ngữ lớn (LLM-based approaches) gần đây, nhằm so sánh toàn diện với LLM-FE.
  - **Đường ống tiền xử lý hợp nhất (Unified preprocessing pipeline)**: Sau khi sinh đặc trưng với từng phương pháp đối chuẩn, một đường ống tiền xử lý thống nhất được áp dụng để chuẩn bị dữ liệu cho quá trình huấn luyện và đánh giá trên mô hình học máy (machine learning model).

#### FeatLLM

- **Nguyên lý hoạt động cơ sở**:
  - FeatLLM sử dụng một LLM để sinh ra các quy tắc nhằm nhị phân hóa đặc trưng (binarize features), sau đó các đặc trưng này được đưa vào làm đầu vào cho một mô hình đơn giản, chẳng hạn như hồi quy tuyến tính (linear regression).
- **Điều chỉnh triển khai và mô hình suy luận**:
  - Nghiên cứu kế thừa và tùy biến bản triển khai mã nguồn mở của FeatLLM ([https://github.com/Sungwon-Han/FeatLLM](https://github.com/Sungwon-Han/FeatLLM)), điều chỉnh đường ống (pipeline) để sử dụng mô hình XGBoost cho pha suy luận (inference).
- **Giao thức so sánh công bằng (Fair comparison protocol)**:
  - Để đảm bảo tính công bằng với các phương pháp khác, mô hình XGBoost được huấn luyện trên toàn bộ tập dữ liệu huấn luyện (entire training dataset), trong khi LLM chỉ sử dụng một tập con gồm 10 mẫu ($10$ samples) để sinh ra các đặc trưng nhị phân.
- **Cơ chế tập hợp (Ensemble)**:
  - Do FeatLLM sinh ra song song nhiều tập đặc trưng qua các lượt gọi LLM, kết quả báo cáo cuối cùng được tổng hợp (ensemble) qua 3 mẫu ($3$ samples) nhằm duy trì tính nhất quán tuyệt đối với LLM-FE.

#### AutoFeat

- **Nguyên lý hoạt động cơ sở**:
  - AutoFeat là một phương pháp kỹ thuật đặc trưng cổ điển (classical feature engineering approach), vận hành dựa trên cơ chế lấy mẫu con đặc trưng lặp (iterative feature subsampling) kết hợp với tìm kiếm chùm tia (beam search) để chọn lọc các đặc trưng chứa nhiều thông tin hữu ích (informative features).
- **Cấu hình triển khai**:
  - Sử dụng gói mã nguồn mở `autofeat` chính thức ([https://github.com/cod3licious/autofeat.git](https://github.com/cod3licious/autofeat.git)).
  - Toàn bộ các thiết lập tham số mặc định (default parameter settings) được giữ nguyên, tham chiếu trực tiếp theo các tệp ví dụ `.ipynb` được cung cấp trong kho lưu trữ chính thức của tác giả.

#### CAAFE

- **Triển khai và phạm vi bài toán áp dụng**:
  - Sử dụng bản triển khai chính thức của CAAFE, duy trì nguyên vẹn toàn bộ các thiết lập tham số theo đúng quy định trong kho lưu trữ gốc.
  - Kho lưu trữ của CAAFE vốn được thiết kế chuyên biệt cho các tập dữ liệu phân loại (classification datasets).
- **Đường ống xử lý dữ liệu**:
  - Tuân thủ quy trình làm việc (workflow) của tác giả gốc, dữ liệu được tiền xử lý trước khi nạp vào mô hình dự đoán sau pha kỹ thuật đặc trưng.
- **Khả năng tổng hợp nghiệm (Ensembling)**:
  - Do CAAFE áp dụng cơ chế tinh chỉnh đặc trưng tuần tự (sequential feature refinement) và chỉ tạo ra duy nhất một giải pháp ứng viên độc lập (single independent candidate solution), nên kỹ thuật ensemble không thể áp dụng được cho phương pháp này.

#### OCTree

- **Tùy biến triển khai và thống nhất đường ống**:
  - Bản triển khai chính thức của OCTree được điều chỉnh để đồng bộ hóa và giữ chung phần nạp dữ liệu (data loading) cũng như khởi tạo mô hình (model initialization) với quy trình thử nghiệm tổng thể.
- **Giới hạn trên tác vụ phân loại**:
  - OCTree chỉ được triển khai đánh giá trên các tập dữ liệu phân loại (classification datasets), do bản triển khai chính thức bị giới hạn ở các bài toán phân loại và việc tự ý mở rộng cho bài toán hồi quy (regression datasets) có thể dẫn tới sai lệch trong triển khai.
- **Tính chất giải pháp đơn lẻ**:
  - Tương tự CAAFE, OCTree tuân theo một quy trình tối ưu hóa tuần tự (sequential optimization procedure) và không tạo ra nhiều nghiệm độc lập phục vụ cho việc kết hợp ensemble.

#### OpenFE

- **Nguyên lý hoạt động cơ sở**:
  - OpenFE là phương pháp kỹ thuật đặc trưng truyền thống hiện đại nhất (state-of-the-art traditional feature engineering method), ứng dụng các thuật toán boosting đặc trưng (feature boosting) và cắt tỉa đặc trưng (pruning algorithms) để tìm kiếm các đặc trưng tổ hợp hiệu quả.
- **Cấu hình triển khai**:
  - Sử dụng gói mã nguồn mở `openfe` chính thức với các thiết lập tham số tiêu chuẩn (standard parameter settings).
