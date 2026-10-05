### 3.1 Model training and optimization

- Quy trình huấn luyện, tối ưu siêu tham số và so sánh đối chuẩn hiệu năng sáu thuật toán:
  - Khảo sát chi tiết năng lực mô phỏng động học nitơ của các mô hình trên tập dữ liệu thực nghiệm nước thải có độ mặn cao.
  - Sử dụng quá trình Gaussian kết hợp hàm tiếp thu để tìm kiếm điểm cấu hình tối ưu cho từng thuật toán.

#### 3.1.1 Hyperparameter optimization

- Tối ưu hóa siêu tham số bằng quá trình Gaussian thông qua hàm tiếp thu biên tin cậy dưới ($LCB$):
  - Hàm $LCB$ ($Lower\ Confidence\ Bound$) tối đa hóa mức cải thiện kỳ vọng của sai số $RMSE$ trong kiểm định chéo $10\text{-fold}$.
  - Không gian tìm kiếm được giới hạn theo các ràng buộc hóa lý và tính toán:
    - Tốc độ học ($learning\ rate$) trong khoảng $0.01\text{–}0.30$ để cân bằng tốc độ hội tụ và độ ổn định mô hình.
    - Độ sâu cây quyết định ($tree\ depth$) trong khoảng $3\text{–}20$ để kiểm soát độ phức tạp và chống quá khớp.
    - Hệ số chính quy hóa L2 trong khoảng $1\text{–}10$ nhằm triệt tiêu nhiễu dữ liệu do nồng độ muối cao.
  - Cấu hình tối ưu của CatBoost hội tụ tại độ sâu cây `depth = 8` và hệ số chính quy hóa `L2 = 3`.
  - Cấu hình tối ưu của LightGBM xác lập số lượng lá cây trong khoảng $20\text{–}50$, trong khi Random Forest chọn độ sâu từ $5\text{–}20$.
  - Thuật toán XGBoost sử dụng tỷ lệ lấy mẫu nhánh con ($subsampling$) từ $0.50\text{–}1.00$ để tăng độ bền vững trước dữ liệu thưa do lực ion.
  - Các cấu hình tối ưu hóa Bayes giúp giảm sai số $RMSE$ kiểm định từ $12\%\text{–}18\%$ so với cấu hình mặc định ban đầu.

#### 3.1.2 Model performance comparison

- Kết quả so sánh đối chuẩn hiệu năng của sáu thuật toán học máy trên tập kiểm tra độc lập:
  - Thuật toán CatBoost đạt hiệu năng cao nhất trên toàn bộ các chỉ tiêu đánh giá thống kê:
    - Dự đoán $NH_4^+\text{-N}_{out}$: đạt hệ số xác định $R^2 = 0.88$ và sai số $RMSE = 4.27\ \text{mg/L}$.
    - Dự đoán $TN_{out}$: đạt hệ số xác định $R^2 = 0.91$ và sai số $RMSE = 4.35\ \text{mg/L}$.
    - Điểm kiểm định chéo $10\text{-fold}$ của CatBoost đạt $R^2 = 0.78 \pm 0.09$ cho $NH_4^+\text{-N}$ và $0.86 \pm 0.06$ cho $TN$.
  - Thuật toán LightGBM xếp vị trí thứ hai:
    - Đạt $R^2 = 0.81$ và $RMSE = 4.97\ \text{mg/L}$ cho $NH_4^+\text{-N}_{out}$.
    - Đạt $R^2 = 0.82$ và $RMSE = 5.17\ \text{mg/L}$ cho $TN_{out}$.
  - So với LightGBM, mô hình CatBoost tăng chỉ số $R^2$ thêm $9\%$ đối với $NH_4^+\text{-N}$ và $10\%$ đối với $TN$.
  - CatBoost giảm sai số $RMSE$ tương ứng $14\%$ đối với $NH_4^+\text{-N}$ và $16\%$ đối với $TN$.
  - Bốn thuật toán còn lại cho hiệu năng thấp hơn (Bảng 1):
    - Random Forest ($RF$): $R^2 = 0.79$, $RMSE = 5.48\ \text{mg/L}$ ($NH_4^+$); $R^2 = 0.80$, $RMSE = 5.25\ \text{mg/L}$ ($TN$).
    - XGBoost: $R^2 = 0.71$, $RMSE = 5.85\ \text{mg/L}$ ($NH_4^+$); $R^2 = 0.76$, $RMSE = 5.20\ \text{mg/L}$ ($TN$).
    - GBDT: $R^2 = 0.68$, $RMSE = 6.10\ \text{mg/L}$ ($NH_4^+$); $R^2 = 0.71$, $RMSE = 5.71\ \text{mg/L}$ ($TN$).
    - AdaBoost: $R^2 = 0.54$, $RMSE = 7.66\ \text{mg/L}$ ($NH_4^+$); $R^2 = 0.63$, $RMSE = 6.50\ \text{mg/L}$ ($TN$).
  - Các kết quả định lượng khẳng định tính chuẩn xác và sự phù hợp của CatBoost trong mô phỏng động học nitơ nước thải mặn.
