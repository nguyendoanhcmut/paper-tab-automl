### B.2 Baselines

* Nhóm tác giả triển khai và đánh giá nhiều phương pháp đường cơ sở kỹ thuật đặc trưng tiên tiến nhất (state-of-the-art feature engineering baselines), trải dài từ các phương pháp truyền thống (traditional methods) đến các phương pháp tiếp cận gần đây dựa trên mô hình ngôn ngữ lớn (recent LLM-based approaches), nhằm so sánh đối chuẩn với LLM-FE.
* Sau khi sinh các đặc trưng bằng từng phương pháp cơ sở, một đường ống tiền xử lý thống nhất (unified preprocessing pipeline) được áp dụng để chuẩn bị dữ liệu cho quá trình huấn luyện và đánh giá trên mô hình học máy (machine learning model).
* Các phương pháp đường cơ sở cụ thể được triển khai bao gồm:

#### FeatLLM

* **Nguyên lý hoạt động:**
  * FeatLLM sử dụng một LLM để sinh ra các quy tắc nhằm nhị phân hóa các đặc trưng (rules to binarize features).
  * Các đặc trưng nhị phân này sau đó được sử dụng làm đầu vào cho một mô hình đơn giản (simple model), chẳng hạn như mô hình hồi quy tuyến tính (linear regression).
* **Triển khai và hiệu chỉnh mô hình suy luận:**
  * Nhóm nghiên cứu tùy biến triển khai mã nguồn mở của FeatLLM (kho mã nguồn chính thức: `https://github.com/Sungwon-Han/FeatLLM`).
  * Đường ống thực thi được sửa đổi để sử dụng mô hình XGBoost cho tác vụ suy luận (inference).
* **Cấu hình dữ liệu và đảm bảo so sánh công bằng (fair comparison):**
  * Mô hình XGBoost được huấn luyện trên toàn bộ tập dữ liệu huấn luyện (entire training dataset).
  * LLM chỉ sử dụng một tập con gồm $10$ mẫu ($10$ samples) để sinh ra các đặc trưng nhị phân.
* **Cơ chế ghép nhóm (ensembling):**
  * Do FeatLLM sinh ra nhiều tập đặc trưng song song qua các lượt gọi LLM (parallel across LLM calls), kết quả được báo cáo thông qua việc ghép nhóm (ensemble) trên $3$ mẫu ($3$ samples) nhằm duy trì tính nhất quán khi so sánh với LLM-FE.

#### AutoFeat

* **Nguyên lý hoạt động:**
  * AutoFeat là một phương pháp tiếp cận kỹ thuật đặc trưng cổ điển (classical feature engineering approach).
  * Phương pháp sử dụng cơ chế lấy mẫu con đặc trưng lặp đi lặp lại (iterative feature subsampling) kết hợp với tìm kiếm chùm (beam search) để lựa chọn các đặc trưng mang nhiều thông tin (informative features).
* **Triển khai và cấu hình tham số:**
  * Nhóm tác giả sử dụng gói thư viện mã nguồn mở `autofeat` (kho mã nguồn: `https://github.com/cod3licious/autofeat.git`).
  * Toàn bộ các thiết lập tham số mặc định (default parameter settings) được giữ nguyên.
  * Các thiết lập tham số được tham chiếu trực tiếp từ các tệp ví dụ định dạng `.ipynb` được cung cấp trong kho lưu trữ chính thức của phương pháp.

#### CAAFE

* **Triển khai và thiết lập tham số:**
  * Nhóm tác giả sử dụng triển khai chính thức của CAAFE, đồng thời duy trì toàn bộ các thiết lập tham số theo đúng quy định trong kho lưu trữ gốc.
* **Phạm vi tác vụ và tiền xử lý dữ liệu:**
  * Kho lưu trữ của CAAFE được thiết kế chuyên biệt cho các tập dữ liệu phân loại (classification datasets).
  * Tuân theo quy trình công việc (workflow) của CAAFE, dữ liệu được tiền xử lý trước khi đưa vào mô hình dự đoán sau giai đoạn kỹ thuật đặc trưng.
* **Giới hạn về ghép nhóm (ensembling):**
  * Do CAAFE thực hiện quy trình tinh chỉnh đặc trưng tuần tự (sequential feature refinement) và chỉ tạo ra một giải pháp ứng viên độc lập duy nhất (single independent candidate solution), kỹ thuật ghép nhóm (ensembling) không thể áp dụng được (not applicable).

#### OCTree

* **Triển khai và chuẩn hóa hệ thống:**
  * Triển khai chính thức của OCTree được điều chỉnh nhằm giữ cho phần nạp dữ liệu (data loading) và phần khởi tạo mô hình (model initialization) dùng chung thống nhất với hệ thống thử nghiệm.
* **Giới hạn phạm vi tác vụ:**
  * OCTree chỉ được triển khai cho các tập dữ liệu phân loại (classification datasets), do mã nguồn chính thức bị giới hạn ở các tập dữ liệu phân loại.
  * Nhóm tác giả không tự ý chạy trên các tập dữ liệu hồi quy (regression datasets) nhằm tránh nguy cơ sai lệch trong quá trình triển khai (incorrect implementation).
* **Giới hạn về ghép nhóm (ensembling):**
  * Tương tự CAAFE, OCTree tuân theo quy trình tối ưu hóa tuần tự (sequential optimization procedure) và không sinh ra nhiều giải pháp độc lập, do đó không hỗ trợ kỹ thuật ghép nhóm (ensembling).

#### OpenFE

* **Nguyên lý hoạt động:**
  * OpenFE là một phương pháp kỹ thuật đặc trưng truyền thống tiên tiến nhất khác (state-of-the-art traditional feature engineering method).
  * Phương pháp tối ưu hóa không gian đặc trưng bằng cách sử dụng các thuật toán tăng cường đặc trưng (feature boosting) và cắt tỉa đặc trưng (pruning algorithms).
* **Triển khai và cấu hình tham số:**
  * Nhóm nghiên cứu sử dụng gói thư viện mã nguồn mở `openfe` với các thiết lập tham số tiêu chuẩn (standard parameter settings).
