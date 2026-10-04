## 2 Materials and methods

### 2.1 Data acquisition and preprocessing
- Dữ liệu nghiên cứu thu thập từ nhà máy xử lý nước uống (DWTP - Drinking Water Treatment Plant) tại Thiên Tân (Tianjin), Trung Quốc.
  - Nhà máy tiếp nhận nguồn nước thô từ hai nguồn chính theo chu kỳ hàng năm:
    - Sông Loan Hà (Luanhe River): cấp nước vào tháng 12, tháng 1 và tháng 2 hàng năm, chuyển dòng từ tỉnh Hà Bắc (Hebei).
    - Sông Dương Tử (Yangtze River): cấp nước từ tháng 3 đến tháng 11 hàng năm, bắt nguồn từ hồ chứa Đan Giang Khẩu (Danjiangkou Reservoir) thuộc tỉnh Hồ Bắc (Hubei).
  - Quy trình công nghệ xử lý nước gồm tiền xử lý (pre-treatment), xử lý truyền thống tăng cường (enhanced conventional treatment), và khử trùng kết hợp tia cực tím (ultraviolet - UV) cùng clo (chlorine disinfection).
  - Công suất xử lý nước danh định hàng ngày của nhà máy đạt $17.5\text{ wt/d}$ ($17.5 \times 10^4\,\text{m}^3/\text{d}$).
  - Thời gian lưu nước thủy lực (hydraulic retention time - HRT) vận hành tương đối ổn định ở mức $25.56\text{ min}$.
  - Nhà máy sử dụng hai loại hóa chất keo tụ trong dây chuyền:
    - Sắt(III) clorua (ferric chloride) châm tại giai đoạn tiền xử lý.
    - Polyaluminum chloride (PACl) châm tại giai đoạn hòa trộn (blending stage).
- Tập dữ liệu quan trắc gồm $1339$ điểm dữ liệu được thu thập hàng ngày trong giai đoạn từ tháng 10 năm 2022 (October 2022) đến tháng 5 năm 2024 (May 2024).
  - Dữ liệu được phân chia ngẫu nhiên thành tập huấn luyện (training set) gồm $1071$ mẫu và tập kiểm tra (test set) gồm $268$ mẫu theo tỷ lệ $8:2$.
  - Tập biến đặc trưng đầu vào gồm lưu lượng dòng vào (WTR - water treatment rate) cùng các chỉ số chất lượng nước thô (RW - raw water) và nước sau xử lý (TW - treated water):
    - Nhiệt độ nước ($T$).
    - Độ kiềm/axit ($\text{pH}$).
    - Độ đục ($\text{NTU}$).
    - Độ dẫn điện ($\text{EC}$).
    - Nhu cầu oxy hóa học permanganat ($\text{COD}_{\text{Mn}}$).
    - Nitơ amoni ($\text{NH}_3\text{-N}$) chỉ thu thập riêng cho nguồn nước thô (RW).
  - Lượng hóa chất châm thực tế của hai chất keo tụ tương đương nhau với mức sai lệch tối đa không vượt quá $5\text{ mg/L}$.
  - Nghiên cứu chọn PACl làm biến mục tiêu duy nhất để mô phỏng chính xác quá trình định lượng chất keo tụ.
- Tiền xử lý dữ liệu loại bỏ sai số đo đạc và sự cố hệ thống châm hóa chất để nâng cao độ tin cậy.
  - Mô hình ước lượng K láng giềng gần nhất (KNN - K-nearest neighbor) với $k = 4$ xử lý các giá trị khuyết thiếu (missing values).
    - Thuật toán KNN cân bằng giữa độ ổn định nội suy và tính đại diện toàn cục.
    - Thuật toán bảo toàn dữ liệu hiệu quả cho các thông số khuyết không ngẫu nhiên như nhiệt độ nước và nitơ amoni.
    - Quá trình tìm kiếm lưới (grid search) trong dải $k = 1\text{--}10$ sử dụng sai số toàn phương trung bình (MSE - mean square error) làm tiêu chí tối ưu.
    - Kết quả đánh giá cho thấy chỉ số MSE đạt giá trị nhỏ nhất trên tập kiểm tra tại cấu hình $k = 4$.
  - Bộ lọc trung bình trượt (moving average filter) với kích thước cửa sổ $n = 5$ làm giảm nhiễu và sai số ngẫu nhiên.
    - Tham số $n = 5$ được xác định thông qua phân tích hàm tự tương quan (ACF - autocorrelation function).
    - Cửa sổ này bắt trọn các biến động ngắn hạn của chỉ số chất lượng nước, đồng thời tránh hiện tượng làm mịn quá mức gây suy giảm đỉnh dữ liệu.
- Phương pháp hệ số tương quan thứ hạng Spearman ($r_s$) đánh giá mối liên hệ giữa các biến đặc trưng và liều lượng châm chất keo tụ.
  - Hệ số tương quan Spearman có độ nhạy thấp đối với quan hệ phi tuyến và các điểm dị biệt (outliers).
  - Loại bỏ các đặc trưng có tương quan thấp giúp giảm chiều dữ liệu đầu vào, nâng cao hiệu quả vận hành và năng lực tổng quát hóa của mô hình qua quy trình tích hợp gồm tiền xử lý, AutoML và giải thích SHAP.
  - **Hình 1.** Sơ đồ phương pháp luận mô hình hóa hoàn chỉnh.
    - <img src="assets/fig_01_p3.jpeg" alt="Hình 1" />
    - **Hình này chứng minh điều gì**
      - Kỹ thuật đặc trưng (Feature engineering) kết nối dữ liệu tiền xử lý vào quy trình huấn luyện AutoML và hậu giải thích SHAP.
    - **Từ đâu mà thấy được**
      - Luồng chính từ trái qua phải: Data Collection $\rightarrow$ Data Preprocessing $\rightarrow$ AutoML Model ($80\,\%$ Train, $20\,\%$ Test, $3$ lần 10-fold CV) $\rightarrow$ Output (Coagulant-dosage).
      - Khối giải thích phía dưới: mũi tên từ Coagulant-dosage dẫn sang Explanation (SHAP) gồm Global interpretation, Partial interpretation và Partial Dependency.

### 2.2 Automated machine learning
- Học máy tự động (AutoML - Automated Machine Learning) tự động hóa quy trình xây dựng mô hình thuật toán.
  - AutoML thực hiện kỹ thuật tạo đặc trưng (feature engineering), lựa chọn thuật toán (algorithm selection), và tối ưu hóa siêu tham số (hyperparameter optimization).
  - Mục tiêu cốt lõi của AutoML là giảm can thiệp thủ công của con người và cải thiện hiệu suất mô hình.
- Công cụ tối ưu hóa đường ống dựa trên cây (TPOT - Tree-based Pipeline Optimization Tool) tự động xây dựng mô hình.
  - TPOT là thư viện AutoML mã nguồn mở bằng Python (phiên bản 0.11.7) vận hành dựa trên thuật toán lập trình di truyền (genetic programming).
  - TPOT phụ thuộc vào các thư viện nền tảng gồm Scikit-Learn (phiên bản 1.0.2), DEAP (Distributed Evolutionary Algorithms Framework), và các mở rộng như XGBoost.
  - Mô hình thực thi trong môi trường Python 3.8 với toàn bộ mã nguồn cấu hình mở.
- Khung làm việc TPOT áp dụng ba cơ chế cốt lõi để tối ưu hóa pipeline học máy:
  - Tối ưu hóa lặp dựa trên mã hóa cấu trúc cây của giải thuật lập trình di truyền.
  - Tích hợp đa thuật toán của Scikit-Learn cùng không gian siêu tham số xác định trước để cân bằng hiệu quả tìm kiếm.
  - Sàng lọc pipeline tối ưu Pareto (Pareto-optimal pipeline) bằng kiểm định chéo 10 lần (10-fold cross-validation), lặp lại độc lập $3$ lần để bảo đảm khả năng tổng quát hóa.

### 2.3 SHAP interpretability method
- Hệ phương pháp SHAP (Shapley Additive exPlanations) gồm ba nhánh chính: Kernel SHAP, Deep SHAP, và Tree SHAP.
- Nghiên cứu sử dụng gói Tree SHAP trong môi trường Python 3.9 để phân tích tầm quan trọng, sự phụ thuộc và tương tác giữa các đặc trưng.
  - Các thư viện Python và chức năng tương ứng được tổng hợp tại Bảng 1:
    - Sklearn (phiên bản 1.5.0): xử lý dữ liệu, phân chia tập mẫu, đánh giá mô hình và kiểm định chéo.
    - Scipy (phiên bản 1.13.1): phân tích tương quan Spearman.
    - Seaborn (phiên bản 0.13.2): trực quan hóa thống kê dữ liệu.
    - TPOT (phiên bản 0.11.7 / 0.12.2): thiết lập mô hình hồi quy TPOT Regressor.
    - SHAP (phiên bản 0.45.1): diễn giải mô hình và trực quan hóa dữ liệu.
    - Matplotlib (phiên bản 3.9.0): vẽ đồ thị kỹ thuật.
- Giá trị SHAP tuyệt đối trung bình định lượng tầm quan trọng của các yếu tố ảnh hưởng đến liều lượng châm chất keo tụ.
  - Tổng các giá trị SHAP tuyệt đối trung bình của toàn bộ thông số môi trường đo lường tác động kết hợp của chúng lên chiến lược châm hóa chất.
  - Biểu đồ phụ thuộc SHAP (SHAP dependency plots) thể hiện tương tác giữa các đặc trưng và đóng góp chung vào dự đoán liều lượng keo tụ.
  - Hai mẫu điển hình được chọn để lập biểu đồ giải thích cục bộ, biểu đồ thác nước (waterfall plots) và biểu đồ quyết định (decision plots) nhằm làm sáng tỏ cơ chế ra quyết định của mô hình.

### 2.4 Model evaluation
- Ba chỉ số đánh giá gồm RMSE, MAE và $R^2$ kiểm tra độ tin cậy và độ chính xác của các mô hình dự đoán.
- Sai số căn bậc hai trung bình (RMSE - Root Mean Square Error) đo lường độ chênh lệch giữa giá trị dự đoán và giá trị thực tế:
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$
  - Chỉ số RMSE nhạy cảm với các điểm dị biệt (outliers) và định lượng quy mô trung bình của sai số dự đoán.
- Sai số tuyệt đối trung bình (MAE - Mean Absolute Error) phản ánh khoảng cách sai số trung bình giữa dự đoán và thực tế:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
  - Giá trị MAE càng tiến gần $0$ thể hiện hiệu suất mô hình càng tốt.
- Hệ số xác định ($R^2$ - Coefficient of Determination) định lượng mức độ phù hợp giữa mô hình dự đoán và dữ liệu thực nghiệm:
  $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
  - Giá trị $R^2$ tiến gần $1$ chứng minh tương quan chặt chẽ giữa biến phụ thuộc và các biến độc lập, sai số dự đoán nhỏ và mô hình đạt độ vững chắc cao.
