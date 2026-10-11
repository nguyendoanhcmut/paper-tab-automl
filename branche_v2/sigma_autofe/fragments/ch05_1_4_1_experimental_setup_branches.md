### 4.1. Experimental Setup

- **Tập dữ liệu thực nghiệm (Datasets)**:
  - Sử dụng $16$ bộ dữ liệu phân loại dạng bảng công khai (public tabular classification datasets) được kế thừa từ các nghiên cứu trước đây (Hollmann et al., 2023; Nam et al., 2024).
  - Toàn bộ các tập dữ liệu đều được thu thập từ hai nguồn chuẩn là OpenML (Feurer et al., 2021) và Kaggle (Banachewicz and Massaron, 2022).
  - Giới hạn kích thước mẫu: Mỗi bộ dữ liệu được giới hạn tối đa $50,000$ mẫu (samples) nhằm kiểm soát chi phí tính toán.
  - Phân chia dữ liệu (Data split): Dữ liệu được phân chia thành tập huấn luyện (training set) và tập kiểm tra (test set) theo tỷ lệ $8:2$ ($80\%$ huấn luyện, $20\%$ kiểm tra).
  - Lặp lại thực nghiệm: Quá trình phân chia dữ liệu được thực hiện $3$ lần độc lập với các seed ngẫu nhiên khác nhau (random seeds) nhằm tăng cường độ tin cậy và độ vững chắc của kết quả.

- **Thang đo đánh giá (Evaluation Metrics)**:
  - Áp dụng F1-score làm thang đo đánh giá chính (primary evaluation metric).
  - Chỉ số này cung cấp một đánh giá cân bằng và toàn diện về hiệu năng mô hình (balanced assessment of model performance), đặc biệt thích hợp với dữ liệu phân loại thực tế có thể bị mất cân bằng lớp.

- **Các phương pháp cơ sở đối chuẩn (Baselines)**:
  - Mô hình hạ nguồn (Downstream model): Lựa chọn XGBoost (Chen and Guestrin, 2016) làm mô hình học máy hạ nguồn thống nhất để đánh giá chất lượng của tập đặc trưng sinh ra.
  - Các phương pháp cơ sở dựa trên mô hình ngôn ngữ lớn (LLM-based baselines):
    - CAAFE (Hollmann et al., 2023): Phương pháp tiếp cận dựa trên ngữ nghĩa (semantic-based approach), tận dụng các bản mô tả văn bản chi tiết về đặc trưng để chỉ dẫn sinh đặc trưng.
    - OCTree (Nam et al., 2024): Phương pháp tiếp cận phi ngữ nghĩa (non-semantic generation), sử dụng các biểu thức cấu trúc cây của không gian đặc trưng (tree-structured expressions of feature space) làm thông tin quỹ đạo (trajectory information).
  - Các phương pháp cơ sở AutoFE truyền thống (Traditional AutoFE baselines):
    - So sánh với ba phương pháp đại diện tiêu biểu gồm DFS (Deep Feature Synthesis), OpenFE, và AutoFeat.
    - Các phương pháp truyền thống này hoạt động dựa trên các quy tắc biến đổi định trước (predefined transformation rules) và thực hiện sinh đặc trưng thông qua tìm kiếm vét cạn (exhaustive search) trên không gian toán tử.

- **Giao thức thực nghiệm (Experimental Protocol)**:
  - Loại bỏ thông tin ngữ nghĩa (Metadata-free setting): Đối với SIGMA và các phương pháp kỹ thuật đặc trưng truyền thống, toàn bộ thông tin ngữ nghĩa được loại bỏ bằng cách ẩn tên đặc trưng (masking feature names) và mã hóa các giá trị (encoding values), đảm bảo tất cả các phương pháp vận hành hoàn toàn không có quyền truy cập vào mô tả ngữ nghĩa.
  - Không gian toán tử chia sẻ (Shared operation space): Nhằm loại bỏ các khác biệt bắt nguồn từ định nghĩa phép biến đổi giữa các phương pháp, một không gian toán tử chung được thiết lập thống nhất bao gồm:
    - Các phép toán số học cơ bản (basic arithmetic operations): phép cộng (`addition`), phép trừ (`subtraction`), phép nhân (`multiplication`), và phép chia (`division`).
    - Các phép biến đổi đơn nguyên phổ biến (common unary transformations): logarit tự nhiên (`logarithm`), căn bậc hai (`square root`), và giá trị tuyệt đối (`absolute value`).
    - Tương tác đặc trưng đơn giản (simple feature interactions): tỷ số giữa các đặc trưng (`ratios`).
  - Giao thức cho các baseline dựa trên LLM:
    - Tuân theo cấu hình cài đặt gốc từ tác giả của từng phương pháp.
    - Để hạn chế biến động hiệu năng gây ra bởi tham số nhiệt độ (temperature parameter) và các chiến lược lấy mẫu (sampling strategies), mỗi phương pháp AutoFE dựa trên LLM được lặp lại $3$ lần độc lập.
    - Ngân sách sinh đặc trưng (Generation budget): Được cố định ở mức $50$ đặc trưng (50 features), tính theo tổng số đặc trưng được sinh ra (generated features) chứ không phải số đặc trưng được chấp nhận (accepted features).
  - Đánh giá sự đánh đổi giữa hiệu năng dự đoán và ngân sách đặc trưng:
    - Trong thực tế, việc tạo ra số lượng lớn đặc trưng sẽ gây khó khăn cho việc diễn giải mô hình và đòi hỏi chi phí bảo trì hệ thống rất lớn (huge maintenance costs).
    - Do đó, hiệu quả sử dụng đặc trưng (feature-efficiency) của SIGMA được đối chiếu trực tiếp với AutoFE truyền thống bằng cách khảo sát biến thiên theo ngân sách đặc trưng $K$ (varying feature budget $K$).

- **Chi tiết triển khai kỹ thuật (Implementation Details)**:
  - Triển khai và suy luận LLM: Nhằm đáp ứng mục tiêu ứng dụng thực tế, các LLM được triển khai thông qua thư viện vLLM (Kwon et al., 2023) để đảm bảo tốc độ suy luận hiệu quả và khả năng mở rộng cao (scalable inference).
  - Mô hình nền tảng mặc định và khảo sát mở rộng:
    - Mô hình xương sống mặc định (Default backbone): `Qwen3-4B-Instruct` (cụ thể là `Qwen3-4B-Instruct-2507`, mô hình dày cỡ nhỏ - small dense model) được sử dụng cho toàn bộ các so sánh chính.
    - Các mô hình khảo sát mở rộng: Nghiên cứu cũng đánh giá khả năng tổng quát hóa trên các mô hình khác bao gồm `Qwen3-Coder-Next` (tổng $80\text{ tỷ}$ tham số, kích hoạt $3\text{ tỷ}$ tham số theo cấu trúc MoE) và `Llama3.1-70B` (mô hình dày cỡ lớn - large dense model).
  - Tối ưu hóa mô hình hạ nguồn: Sử dụng phiên bản hỗ trợ GPU của XGBoost (Mitchell and Frank, 2017) nhằm triệt tiêu điểm nghẽn hiệu năng tính toán trên CPU (CPU bottleneck).
  - Cấu hình chi tiết của các baseline (theo Phụ lục B):
    - `AutoFeat`: Sử dụng thư viện Python chính thức với số bước sinh đặc trưng `feateng_steps = 2` và số lần chạy chọn lọc đặc trưng `featsel_runs = 3`.
    - `DFS`: Sử dụng thư viện Python chính thức với các primitive chuyển đổi `trans_primitives = ['add_numeric', 'subtract_numeric', 'multiply_numeric', 'divide_numeric', 'natural_logarithm', 'square_root', 'absolute']` và độ sâu tối đa `max_depth = 2`.
    - `OpenFE`: Sử dụng thư viện Python chính thức với các tham số mặc định (default parameters).
    - `CAAFE`: Sử dụng bản cài đặt Python chính thức kết hợp với XGBoost để bảo đảm so sánh công bằng.
    - `OCTree`: Sử dụng mã nguồn Python chính thức được cung cấp bởi tác giả.
