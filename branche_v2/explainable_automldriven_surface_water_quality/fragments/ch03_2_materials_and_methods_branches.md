## 2 Materials and methods

### 2.1 Study area and water quality dataset

- **Nguồn dữ liệu và phạm vi không gian**:
  - Dữ liệu thu thập từ Trung tâm Giám sát Môi trường Quốc gia Trung Quốc (CNEMC).
  - Phạm vi gồm $9$ lưu vực sông lớn: Nội địa (Continental), Hải Hà (Hai), Hoài Hà (Huai), Châu Giang (Pearl), Tùng Liêu (Song-Liao), Đông Nam (Southeast), Tây Nam (Southwest), Trường Giang (Yangtze) và Hoàng Hà (Yellow).
  - Thu thập từ khoảng $1900$ trạm quan trắc tự động trong giai đoạn từ tháng 1 năm 2021 đến tháng 6 năm 2024 với tần suất đo $4\text{ h/lần}$.
- **Lựa chọn $9$ chỉ tiêu chất lượng nước then chốt**:
  - Mạng lưới quan trắc online theo dõi $11$ chỉ tiêu thông dụng ban đầu.
  - Loại bỏ hai chỉ tiêu gồm diệp lục a ($\text{Chl-a}$) và mật độ tảo do tỷ lệ khuyết thiếu dữ liệu vượt quá $70\%$.
  - Giữ lại $9$ chỉ tiêu đo đạc ổn định: nhiệt độ nước ($\text{WT}$, $^\circ\text{C}$), $\text{pH}$, oxy hòa tan ($\text{DO}$, $\text{mg/L}$), độ dẫn điện ($\text{EC}$, $\mu\text{S/cm}$), nhu cầu oxy hóa học theo pemanganat ($\text{COD}_{\text{Mn}}$, $\text{mg/L}$), nitơ amoni ($\text{NH}_3\text{-N}$, $\text{mg/L}$), tổng photpho ($\text{TP}$, $\text{mg/L}$), tổng nitơ ($\text{TN}$, $\text{mg/L}$) và độ đục ($\text{NTU}$).
- **Quy chuẩn phân loại chất lượng nước mặt**:
  - Áp dụng Tiêu chuẩn Chất lượng Môi trường Nước mặt Quốc gia Trung Quốc (GB3838-2002).
  - Nước được xếp vào $6$ cấp từ tốt đến xấu nhất: Cấp I, Cấp II, Cấp III, Cấp IV, Cấp V và Cấp kém V ($\text{WV}$).
  - Cấp chất lượng nước chính thức được xác định bằng phương pháp đánh giá đơn nhân tố (Single-factor evaluation method).
- **Chiến lược lấy mẫu phân tầng (Stratified Sampling)**:
  - Tập dữ liệu sạch quy mô lớn có tổng cộng $n = 10,159,876$ bản ghi quan trắc.
  - Trích xuất tập con gồm $50,000$ mẫu bằng phương pháp lấy mẫu ngẫu nhiên phân tầng để tối ưu tốc độ tính toán và kiểm soát phương sai mô hình.
  - Lặp lại quy trình lấy mẫu $5$ lần độc lập với các hạt ngẫu nhiên (random seeds): 42, 123, 777, 1024 và 2048.
  - Phân tích tương quan Spearman khẳng định không có hiện tượng đa cộng tuyến nghiêm trọng giữa $9$ chỉ tiêu.

### 2.2 Model development and validation strategies

- **Đầu vào và đầu ra của mô hình**:
  - Đầu vào gồm $9$ biến đặc trưng hóa lý ($\text{WT}$, $\text{pH}$, $\text{DO}$, $\text{EC}$, $\text{COD}_{\text{Mn}}$, $\text{NH}_3\text{-N}$, $\text{TP}$, $\text{TN}$, $\text{NTU}$).
  - Đầu ra là biến mục tiêu phân loại đa lớp gồm $6$ cấp nước ($\text{I}$ đến $\text{WV}$).
- **Ba sơ đồ kiểm định hiệu năng nghiêm ngặt**:
  - *Kiểm định phân chia ngẫu nhiên phân tầng (Stratified random split)*: Chia tập $50,000$ mẫu thành $80\%$ tập huấn luyện ($n = 40,000$) và $20\%$ tập kiểm thử ($n = 10,000$), lặp lại $5$ lần độc lập.
  - *Kiểm định giữ lại theo thời gian (Temporal hold-out validation)*: Phân tách toàn bộ dữ liệu dựa trên mốc thời điểm $\text{2024-01-01 00:00:00}$; tập huấn luyện ($n = 40,000$) lấy trước mốc thời gian và tập kiểm thử ($n = 10,000$) lấy sau mốc thời gian.
  - *Kiểm định giữ lại theo không gian (Spatial hold-out validation)*: Áp dụng phương pháp loại từng lưu vực (leave-one-basin-out) qua $9$ vòng lặp; mỗi vòng lấy $8$ lưu vực để huấn luyện ($n = 40,000$) và lưu vực còn lại để kiểm thử ($n = 10,000$).
- **Nguyên tắc báo cáo số liệu**:
  - Mọi chỉ số định lượng đều được trình bày dưới dạng giá trị trung bình kèm độ lệch chuẩn ($\text{mean} \pm \text{SD}$).

### 2.3 Traditional and automated machine learning

- **Quy trình học máy truyền thống**:
  - Chuẩn hóa các biến đặc trưng đầu vào bằng phương pháp chuẩn hóa Z-score ($\mu = 0, \sigma = 1$).
  - Sử dụng tối ưu hóa Bayesian dựa trên quá trình Gaussian (Gaussian process-based Bayesian optimization) để dò tìm siêu tham số.
- **Khung làm việc AutoML (Auto-sklearn 0.15.0)**:
  - Tiếp nhận dữ liệu thô trực tiếp mà không cần can thiệp tiền xử lý thủ công.
  - Kết hợp ba cơ chế: học siêu dữ liệu (meta-learning) để khởi tạo không gian tìm kiếm, tối ưu hóa Bayesian để tìm pipeline tối ưu, và xây dựng mô hình ensemble sau tìm kiếm.
  - Áp dụng kiểm định chéo $5$ lớp phân tầng ($5\text{-fold stratified cross-validation}$) trong suốt quá trình huấn luyện nhằm chống mất cân bằng lớp.
- **Danh mục thuật toán đối chứng**:
  - Các mô hình học máy truyền thống: Hồi quy Logistic ($\text{LR}$), k láng giềng gần nhất ($\text{KNN}$), Cây quyết định ($\text{DT}$), Rừng ngẫu nhiên ($\text{RF}$).
  - Các mô hình ensemble tiên tiến: $\text{CatBoost}$ ($\text{CatB}$), $\text{LightGBM}$ ($\text{LGBM}$), $\text{XGBoost}$ ($\text{XGB}$).
  - Nền tảng thực thi xây dựng trên ngôn ngữ Python phiên bản 3.8.13.

### 2.4 Model evaluation metrics

- **Bộ tiêu chí đánh giá đa chiều**:
  - Sử dụng các chỉ số phân loại đa lớp: Độ chính xác ($\text{Precision}$), Độ thu hồi ($\text{Recall}$), và Điểm F1 có trọng số ($\text{Weighted F1}$).
  - Chỉ số $\text{Weighted F1}$ đóng vai trò tiêu chí chính để phản ánh trung thực hiệu năng khi dữ liệu bị mất cân bằng lớp.
  - Sử dụng ma trận nhầm lẫn ($\text{confusion matrix}$) để quan sát chi tiết tỷ lệ phân loại đúng và nhầm lẫn giữa từng cặp cấp nước.
  - Đường cong đặc trưng hoạt động của bộ thu ($\text{ROC}$) và diện tích dưới đường cong ($\text{AUC}$) đánh giá năng lực phân biệt tổng thể.

### 2.5 Explanation of Auto-sklearn

- **Nguyên lý giải thích mô hình bằng Kernel SHAP**:
  - Áp dụng phương pháp giá trị giải thích phụ gia Shapley ($\text{SHAP}$) dựa trên lý thuyết trò chơi hợp tác.
  - Độ chính xác dự đoán cao của mô hình là điều kiện tiên quyết để việc giải thích đặc trưng mang ý nghĩa tin cậy.
  - Kernel SHAP là phương pháp phi mô hình (model-agnostic), đặc biệt thích hợp cho các mô hình ensemble không đồng nhất được tạo ra bởi Auto-sklearn.
- **Công thức toán học tính giá trị Shapley**:
  - Giá trị Shapley $\phi_i$ của chỉ số thứ $i$ được tính theo công thức:
    $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(M - |S| - 1)!}{M!} [f_x(S \cup \{i\}) - f_x(S)]$$
  - Trong đó $F$ là tập hợp tất cả các đặc trưng, $M$ là tổng số lượng đặc trưng ($M = 9$).
  - $S$ là tập con các đặc trưng không chứa đặc trưng $i$.
  - Biểu thức $f_x(S) = \mathbb{E}[f(x)|x_S]$ biểu thị giá trị dự đoán kỳ vọng của mô hình khi chỉ biết tập đặc trưng $S$.
  - Kernel SHAP ước lượng các giá trị này thông qua hồi quy tuyến tính cục bộ có trọng số trên các liên minh đặc trưng được lấy mẫu.
