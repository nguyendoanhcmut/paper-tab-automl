### 3.2 Water quality classification performance and generalization

#### 3.2.1 Comparative performance of models

- **Đặc trưng phân bố không gian và tính đại diện của tập mẫu**:
  - Tập dữ liệu quan trắc phân tầng bảo toàn tỷ lệ giữa các cấp chất lượng nước và cơ cấu lưu vực so với tổng thể $10,159,876$ bản ghi.
  - **Hình 1.** Phân bố trạm quan trắc và cơ cấu dữ liệu phân tầng
    - <img src="assets/fig_01_p3.png" alt="Hình 1" />
    - **Hình này chứng minh điều gì**
      - Mạng lưới quan trắc bao phủ $9$ lưu vực sông lớn và tập mẫu phân tầng phản ánh trung thực phân bố cấp nước thực tế.
    - **Từ đâu mà thấy được**
      - Bản đồ (a) hiển thị vị trí các trạm quan trắc; biểu đồ (b) so sánh tần suất cấp nước trước và sau lấy mẫu; ma trận (c) biểu thị tương quan Spearman.
- **Phân tầng thứ bậc hiệu năng giữa các nhóm thuật toán**:
  - Dựa trên $5$ lượt chạy độc lập với phân chia ngẫu nhiên phân tầng, kiểm định Tukey HSD ($p < 0.05$) phân tách các mô hình thành các nhóm rõ rệt.
  - Nhóm dẫn đầu gồm Auto-sklearn, Rừng ngẫu nhiên ($\text{RF}$) và $\text{CatBoost}$ ($\text{CatB}$) không có sự khác biệt có ý nghĩa thống kê về mặt hiệu năng.
  - Auto-sklearn đạt giá trị trung bình cao nhất trên mọi tiêu chí với Precision đạt $0.9636 \pm 0.0027$, Recall đạt $0.9635 \pm 0.0027$, và Weighted $\text{F1}$ đạt $0.9633 \pm 0.0027$.
  - Phân tích chi tiết theo từng lớp (Table S7) chứng minh Auto-sklearn đạt điểm Macro F1 cao nhất trong toàn bộ các thuật toán thử nghiệm.
  - Độ lệch chuẩn rất nhỏ ($\pm 0.0027$) phản ánh tính hội tụ ổn định của quy trình tối ưu hóa Bayesian qua các lượt lấy mẫu độc lập.
  - Nhóm kế tiếp gồm Cây quyết định ($\text{DT}$ với Weighted $\text{F1} = 0.9566$), $\text{LightGBM}$ ($\text{LGBM}$ với Weighted $\text{F1} = 0.9560$) và $\text{XGBoost}$ ($\text{XGB}$ với Weighted $\text{F1} = 0.9545$).
  - Nhóm cuối bảng gồm $\text{KNN}$ (Weighted $\text{F1} = 0.8492 \pm 0.0023$) và Hồi quy Logistic ($\text{LR}$ với Weighted $\text{F1} = 0.6457 \pm 0.0026$), cho thấy mô hình tuyến tính không thể mô tả tốt dữ liệu này.
  - Khoảng cách hiệu năng lớn giữa nhóm mô hình cấu trúc cây và mô hình khoảng cách như KNN khẳng định tính phi tuyến cao của các ranh giới thủy hóa.
- **Độ chính xác phân loại cao trên các cấp nước trung gian**:
  - Auto-sklearn đạt độ chính xác $99.1\%$ cho Cấp I, $98.4\%$ cho Cấp II, đồng thời duy trì độ chính xác cao trên các cấp chuyển tiếp khó phân loại gồm Cấp III ($96.1\%$), Cấp IV ($91.0\%$) và Cấp V ($84.4\%$).
  - **Hình 4.** Ma trận nhầm lẫn so sánh giữa các thuật toán phân loại
    - <img src="assets/fig_04_p6.png" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Auto-sklearn phân loại đồng đều và chính xác trên mọi cấp nước, trong khi mô hình tuyến tính (LR) suy giảm mạnh ở các cấp nước ô nhiễm.
    - **Từ đâu mà thấy được**
      - So sánh đường chéo chính giữa Auto-sklearn (a) và LR (d), trong đó LR rơi xuống $53.3\%$ ở Cấp III, $30.8\%$ ở Cấp IV và $0\%$ ở Cấp V.
- **Sự sụp đổ hiệu năng của các mô hình tuyến tính trên các cấp ô nhiễm**:
  - Mô hình Hồi quy Logistic (LR) hoàn toàn bất lực trong việc nhận diện nguồn nước ô nhiễm Cấp V với độ chính xác rơi về mức $0\%$.
  - Hạn chế cấu trúc của các siêu phẳng tuyến tính khiến mô hình đơn giản không thể phân tách các vùng biên giới nồng độ đan xen phức tạp.
- **Năng lực phân biệt tổng thể qua diện tích dưới đường cong ROC**:
  - Auto-sklearn đạt diện tích dưới đường cong trung bình vĩ mô cao nhất $\text{MA-AUC} = 0.9963$, xếp trên RF ($\text{MA-AUC} = 0.9961$) và CatB ($\text{MA-AUC} = 0.9960$).
  - **Hình 5.** Đường cong ROC và giá trị AUC của các thuật toán
    - <img src="assets/fig_05_p6.png" alt="Hình 5" />
    - **Hình này chứng minh điều gì**
      - Cụm mô hình Auto-sklearn đạt năng lực phân biệt tối đa trên tất cả các lớp ranh giới so với các mô hình đơn lẻ.
    - **Từ đâu mà thấy được**
      - Đồ thị (a) của Auto-sklearn có đường cong áp sát góc trên bên trái cho mọi cấp nước; đồ thị (d) của LR suy giảm rõ rệt ở Cấp III ($\text{AUC} = 0.8257$) và Cấp IV ($\text{AUC} = 0.8762$).
- **Độ suy giảm phân biệt của mô hình cơ sở tại vùng ranh giới**:
  - Mô hình LR biểu hiện điểm yếu lớn nhất tại Cấp III ($\text{AUC} = 0.8257$) và Cấp IV ($\text{AUC} = 0.8762$), làm suy giảm giá trị MA-AUC xuống mức $0.9027$.
  - Kết quả so sánh đối chuẩn chứng minh AutoML tự động tạo lập giải pháp tối ưu mà không phụ thuộc vào kinh nghiệm thủ công của chuyên viên.

#### 3.2.2 Generalization assessment with temporal and spatial validation

- **Đánh giá độ ổn định dự báo theo thời gian (Temporal Validation)**:
  - Kiểm định trên chuỗi dữ liệu chưa từng thấy sau mốc ngày 01 tháng 01 năm 2024 nhằm ngăn ngừa rò rỉ dữ liệu chuỗi thời gian.
  - Điểm Weighted $\text{F1}$ của Auto-sklearn đạt $0.9627 \pm 0.0005$, không suy giảm có ý nghĩa thống kê so với phân chia ngẫu nhiên ($0.9633 \pm 0.0027$).
  - Kết quả khẳng định các mô hình học được quy luật chất lượng nước ổn định, bền vững qua các chu kỳ mùa và thời gian.
- **Đánh giá năng lực tổng quát hóa theo không gian (Spatial Validation)**:
  - Áp dụng kỹ thuật kiểm định chéo loại từng lưu vực (leave-one-basin-out) trên $9$ lưu vực thủy văn độc lập.
  - Điểm Weighted $\text{F1}$ trung bình của Auto-sklearn vẫn duy trì ở mức cao $0.9675 \pm 0.0154$.
  - Độ lệch chuẩn tăng đáng kể từ $0.0027$ lên $0.0154$ là bằng chứng định lượng rõ nét cho tính dị biệt theo vùng miền của môi trường nước.
  - Thứ bậc tương đối giữa các thuật toán không hề thay đổi: Auto-sklearn và các mô hình ensemble luôn duy trì vị trí dẫn đầu tại tất cả các lưu vực kiểm định.
