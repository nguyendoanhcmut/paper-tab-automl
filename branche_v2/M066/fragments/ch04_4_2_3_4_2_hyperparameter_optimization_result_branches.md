#### 3.4.2. Hyperparameter optimization results

* Thiết lập và phương pháp tối ưu hóa siêu tham số:
  * Nhằm tối đa hóa độ chính xác dự đoán đồng thời ngăn ngừa hiện tượng quá khớp (overfitting), quá trình tối ưu hóa siêu tham số (hyperparameter optimization) được thực hiện bằng phương pháp tìm kiếm ngẫu nhiên (randomized search) kết hợp kiểm định chéo $5$ lượt ($5\text{-fold cross-validation - CV}$).
  * Phương pháp này khảo sát có hệ thống không gian siêu tham số để xác định các cấu hình tối ưu hóa hiệu suất tổng quát hóa (generalization performance).
  * Bảng 1 (Table 1) tóm tắt các siêu tham số được tối ưu hóa cùng điểm kiểm định chéo trung bình (mean cross-validation scores) tương ứng cho cả hai biến mục tiêu dự đoán:
    - **Bảng 1.** Siêu tham số tối ưu và hiệu suất kiểm định chéo
      - <img src="assets/table_01_p6.png" alt="Bảng 1" />
      - **Bảng này chứng minh điều gì**
        - Cung cấp cấu hình siêu tham số và kết quả CV ($R^2$, RMSE) của 3 mô hình cho COD và TMP.
      - **Từ đâu mà thấy được**
        - Cột "optimized hyperparameters" liệt kê các tham số tối ưu cho RF, XGBoost và ANN.
        - Cột "$\text{CV } R^2$" và "CV RMSE" ghi nhận RF đạt $R^2 = 0.94$ (COD); XGBoost đạt $R^2 = 0.69$, RF đạt $R^2 = 0.62$ (TMP).
* Kết quả kiểm định chéo đối với dự đoán $\text{COD}$ dòng ra (effluent COD prediction):
  * Rừng ngẫu nhiên ($\text{RF}$ - Random Forest) thể hiện độ ổn định cao hơn trong quá trình $\text{CV}$, đạt hệ số xác định cao nhất ($R^2 = 0{,}94$) và sai số căn phương phương sai trung bình thấp nhất ($\text{RMSE} = 396{,}65\text{ mg/L}$).
  * $\text{XGBoost}$ đạt hiệu suất tương đương với $\text{CV } R^2 = 0{,}92$.
  * Mạng nơ-ron nhân tạo ($\text{ANN}$ - artificial neural network) cho thấy độ biến thiên dự đoán lớn hơn và tính ổn định dự đoán tương đối thấp hơn ($\text{CV } R^2 = 0{,}87$).
* Kết quả kiểm định chéo đối với dự đoán $\text{TMP}$ (áp suất xuyên màng - transmembrane pressure):
  * $\text{XGBoost}$ đạt hiệu suất kiểm định chéo cao nhất trong không gian biến mục tiêu đã biến đổi (transformed target space), với $R^2 = 0{,}69$ và $\text{RMSE} = 0{,}54\text{ kPa}$.
  * $\text{RF}$ xếp kế tiếp với $R^2 = 0{,}62$ và $\text{RMSE} = 0{,}59\text{ kPa}$.
  * $\text{ANN}$ mang lại kết quả kiểm định chéo yếu hơn với $R^2 = 0{,}47$ và $\text{RMSE} = 0{,}73\text{ kPa}$.
* Đánh giá nguy cơ quá khớp và khả năng tổng quát hóa trong dự đoán $\text{TMP}$:
  * Hiệu suất của $\text{XGBoost}$ dấy lên lo ngại về nguy cơ tiềm ẩn quá khớp (overfitting) do độ phức tạp mô hình (model complexity) so với kích thước nhỏ của tập dữ liệu $\text{TMP}$.
  * Mặc dù $\text{XGBoost}$ đạt hiệu suất kiểm định chéo cao hơn một chút, $\text{RF}$ mang lại khả năng tổng quát hóa (generalization) tốt nhất cho bài toán dự đoán $\text{TMP}$.
