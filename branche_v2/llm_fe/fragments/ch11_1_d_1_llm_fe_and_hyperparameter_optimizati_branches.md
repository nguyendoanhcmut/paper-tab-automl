### D.1 LLM-FE và Tối ưu hóa Siêu tham số (Hyperparameter Optimization - HPO)

- **Mục tiêu nghiên cứu**:
  - Đánh giá tác động thực nghiệm của kỹ thuật tối ưu hóa siêu tham số (Hyperparameter Optimization - HPO) đối với phương pháp LLM-FE.
  - Kiểm tra xem liệu các cải tiến hiệu năng mà LLM-FE mang lại từ kỹ thuật đặc trưng (Feature Engineering - FE) dựa trên mô hình ngôn ngữ lớn (Large Language Models - LLMs) có mang tính độc lập và bổ trợ hay sẽ bị triệt tiêu khi các mô hình cơ sở được tinh chỉnh siêu tham số tối ưu.

- **Thiết lập thực nghiệm**:
  - **Mô hình đánh giá**: Thử nghiệm trên hai cấu trúc mô hình đại diện cho hai trường phái học máy trên dữ liệu bảng:
    - XGBoost: Đại diện cho họ mô hình cây quyết định tăng cường gradient (Gradient Boosted Decision Trees - GBDT).
    - Multilayer Perceptron (MLP): Mạng nơ-ron truyền thẳng đa tầng (multilayer perceptron) đại diện cho mô hình học sâu (deep learning).
  - **Tập dữ liệu thử nghiệm**: Đánh giá trên $5$ tập dữ liệu phân loại (classification datasets) có độ khó cao, nơi các mô hình cơ sở ban đầu đạt độ chính xác (accuracy) dưới $0.8$ ($< 0.8$), gồm: `eucalyptus`, `credit-g`, `cmc`, `blood-transfusion`, và `vehicle`.
  - **Giao thức và công cụ tối ưu hóa**:
    - Quá trình tối ưu hóa được triển khai thông qua thư viện Optuna (Akiba et al., 2019).
    - Thiết lập $100$ lượt thử nghiệm (trials) với cơ chế lấy mẫu ngẫu nhiên (random sampling) trên nhiều phép phân chia dữ liệu (dataset splits).
    - Toàn bộ các mô hình MLP được huấn luyện tối đa $100$ chu kỳ (epochs) kết hợp kỹ thuật dừng sớm (early stopping), giữ lại điểm lưu mô hình (checkpoint) đạt điểm số cao nhất trên tập kiểm định (validation score).

#### Không gian Tìm kiếm Siêu tham số (Hyperparameter Search Spaces)

- **Cơ sở xây dựng**:
  - Không gian tìm kiếm siêu tham số được kế thừa chặt chẽ từ các nghiên cứu đối chuẩn chuẩn mực trên dữ liệu dạng bảng (Grinsztajn et al., 2022; Gorishniy et al., 2021).

- **Không gian siêu tham số của XGBoost (Bảng 7)**:
  - Chi tiết phân phối tìm kiếm của $10$ siêu tham số cốt lõi trong XGBoost:

  | Siêu tham số (Parameter) | Phân phối (Distribution) | Miền giá trị & Diễn giải |
  | :--- | :--- | :--- |
  | `Max depth` | $\text{UniformInt}[1, 11]$ | Độ sâu tối đa của từng cây quyết định |
  | `Num estimators` | $\text{UniformInt}[100, 6100, 200]$ | Số lượng cây ước lượng (bước nhảy $200$) |
  | `Min child weight` | $\text{LogUniformInt}[1, 1\text{e}2]$ | Trọng số cá thể tối thiểu tại một nút lá con |
  | `Subsample` | $\text{Uniform}[0.5, 1]$ | Tỷ lệ lấy mẫu ngẫu nhiên của tập dữ liệu huấn luyện |
  | `Learning rate` | $\text{LogUniform}[1\text{e}-5, 0.7]$ | Tốc độ học (shrinkage factor) |
  | `Col sample by level` | $\text{Uniform}[0.5, 1]$ | Tỷ lệ lấy mẫu đặc trưng cho mỗi cấp độ phân nhánh |
  | `Col sample by tree` | $\text{Uniform}[0.5, 1]$ | Tỷ lệ lấy mẫu đặc trưng cho mỗi cây |
  | `Gamma` | $\text{LogUniform}[1\text{e}-8, 7]$ | Mức giảm độ mất mát tối thiểu để tiếp tục phân nhánh |
  | `Lambda` | $\text{LogUniform}[1, 4]$ | Hệ số chính quy hóa L2 (L2 regularization) |
  | `Alpha` | $\text{LogUniform}[1\text{e}-8, 1\text{e}2]$ | Hệ số chính quy hóa L1 (L1 regularization) |

- **Không gian siêu tham số của MLP (Bảng 8)**:
  - Chi tiết phân phối tìm kiếm của $7$ siêu tham số kiến trúc và huấn luyện trong MLP:

  | Siêu tham số (Parameter) | Phân phối (Distribution) | Miền giá trị & Diễn giải |
  | :--- | :--- | :--- |
  | `Num layers` | $\text{UniformInt}[1, 8]$ | Số lượng tầng ẩn (hidden layers) |
  | `Layer size` | $\text{UniformInt}[16, 1024]$ | Số lượng đơn vị nơ-ron trên mỗi tầng ẩn |
  | `Dropout` | $\text{Uniform}[0, 0.5]$ | Tỷ lệ loại bỏ nơ-ron ngẫu nhiên chống quá khớp |
  | `Learning rate` | $\text{LogUniform}[1\text{e}-5, 1\text{e}-2]$ | Tốc độ học của thuật toán tối ưu hóa |
  | `Category embedding size` | $\text{UniformInt}[64, 512]$ | Số chiều không gian nhúng của biến phân loại |
  | `Learning rate scheduler` | $\{\text{True}, \text{False}\}$ | Cơ chế điều chỉnh lịch trình tốc độ học |
  | `Batch size` | $\{256, 512, 1024\}$ | Kích thước lô huấn luyện (mini-batch size) |

#### Kết quả So sánh và Phân tích Thực nghiệm

- **So sánh độ chính xác phân loại sau HPO (Bảng 9)**:
  - Đánh giá hiệu năng giữa mô hình cơ sở (Base), OpenFE và LLM-FE sau khi áp dụng HPO trên cả hai mô hình XGBoost và MLP (giá trị in đậm thể hiện hiệu năng tốt nhất):

  | Tập dữ liệu (Dataset) | XGBoost: Base | XGBoost: OpenFE | XGBoost: LLM-FE | MLP: Base | MLP: OpenFE | MLP: LLM-FE |
  | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
  | `eucalyptus` | $0.681 \pm 0.029$ | **$0.687 \pm 0.017$** | $0.678 \pm 0.020$ | $0.501 \pm 0.041$ | $0.376 \pm 0.080$ | **$0.506 \pm 0.028$** |
  | `credit-g` | $0.746 \pm 0.023$ | $0.754 \pm 0.019$ | **$0.755 \pm 0.020$** | $0.689 \pm 0.032$ | $0.643 \pm 0.047$ | **$0.693 \pm 0.028$** |
  | `cmc` | $0.552 \pm 0.030$ | $0.551 \pm 0.013$ | **$0.560 \pm 0.030$** | **$0.572 \pm 0.024$** | $0.491 \pm 0.023$ | $0.567 \pm 0.027$ |
  | `blood-transfusion` | $0.790 \pm 0.010$ | $0.777 \pm 0.016$ | **$0.791 \pm 0.011$** | $0.616 \pm 0.182$ | **$0.746 \pm 0.031$** | $0.705 \pm 0.078$ |
  | `vehicle` | $0.760 \pm 0.016$ | **$0.810 \pm 0.016$** | $0.780 \pm 0.022$ | $0.637 \pm 0.095$ | $0.396 \pm 0.043$ | **$0.694 \pm 0.039$** |

- **Phân tích kết quả và nhận định khoa học**:
  - **Tác động nhất quán của HPO**: Quá trình tối ưu hóa siêu tham số liên tục cải thiện hiệu năng dự đoán trên tất cả các tập dữ liệu đối với mô hình Base gốc, khẳng định tầm quan trọng của HPO trong đường ống học máy chuẩn.
  - **Lợi thế vượt trội của LLM-FE sau tinh chỉnh HPO**:
    - Ngay cả khi tất cả các mô hình đã được hưởng lợi tối đa từ quá trình HPO chuyên sâu, phương pháp đề xuất LLM-FE vẫn mang lại mức tăng trưởng hiệu năng bổ sung (further gains), vượt trội hơn cả mô hình Base và phương pháp tiên tiến OpenFE trên $3/5$ tập dữ liệu ở cả hai lớp mô hình:
      - *Mô hình XGBoost*: LLM-FE thiết lập hiệu năng cao nhất trên `credit-g` ($0.755 \pm 0.020$), `cmc` ($0.560 \pm 0.030$) và `blood-transfusion` ($0.791 \pm 0.011$).
      - *Mô hình MLP*: LLM-FE đạt vị trí dẫn đầu trên `eucalyptus` ($0.506 \pm 0.028$), `credit-g` ($0.693 \pm 0.028$) và `vehicle` ($0.694 \pm 0.039$).
  - **Tính chất bổ trợ và độc lập của LLM-FE**:
    - Các kết quả thực nghiệm chỉ ra rằng HPO và LLM-FE giải quyết hai khía cạnh tối ưu hóa trực giao (orthogonal) trong học máy: trong khi HPO tinh chỉnh cách mô hình khai thác không gian tham số, LLM-FE tái cấu trúc và làm giàu chính không gian biểu diễn đặc trưng (feature representation space).
    - Do đó, LLM-FE mang lại những nâng cấp căn bản, có tính chất bổ trợ thực chất và hoàn toàn độc lập với việc tinh chỉnh siêu tham số, điều mà các kỹ thuật HPO đơn thuần không thể tạo ra được.
