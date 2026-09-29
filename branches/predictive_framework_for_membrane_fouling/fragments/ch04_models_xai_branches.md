## 2.4 - 2.5. Các mô hình dự đoán và Khung giải thích AI (Models & Explainable AI)

### 2.4. Các mô hình dự đoán hiện tượng tắc màng (Predictive Models for Membrane Fouling)

#### 2.4.1. Các mô hình thống kê tuyến tính (Statistical Regression Models)
- Vai trò của mô hình thống kê: Nghiên cứu dùng các mô hình hồi quy thống kê để nắm bắt các mối quan hệ tuyến tính giữa các đặc trưng đầu vào và thông số mục tiêu.
- Bản chất phương pháp: Các mô hình này thiết lập chuẩn cơ sở (baseline) so sánh trước khi triển khai các thuật toán học máy phi tuyến phức tạp.
- Mô hình Hồi quy tuyến tính đa biến (Multiple Linear Regression):
  - Biểu diễn toán học chuẩn tắc (Phương trình 3):
    $$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$
  - Thành phần công thức: $Y$ là biến phụ thuộc mục tiêu ($\text{TMP}$ hoặc $\text{Spec. Flux}$). $X_j$ ($j = 1, \dots, p$) đại diện cho các biến độc lập đầu vào.
  - Hệ số hồi quy: $\beta_0$ là hệ số chặn (intercept). $\beta_j$ biểu thị trọng số đóng góp tuyến tính của biến $X_j$.
  - Thành phần sai số: $\epsilon$ là sai số ngẫu nhiên thỏa mãn phân phối chuẩn với kỳ vọng bằng $0$.
  - Giả định cơ bản: Mô hình giả định mối quan hệ cố định, hoàn toàn tuyến tính giữa các yếu tố vận hành sinh học và tốc độ tắc nghẽn màng.
  - Hạn chế thực tiễn: Hệ thống MBR có tương tác vi sinh và thủy lực rất phức tạp. Mô hình tuyến tính đơn giản không phản ánh được động học tắc nghẽn phi tuyến.
- Mô hình Hồi quy Lasso (Least Absolute Shrinkage and Selection Operator):
  - Khái niệm: Lasso kết hợp mô hình hồi quy tuyến tính với kỹ thuật điều chuẩn (regularization) bằng chuẩn $L_1$.
  - Hàm mục tiêu tối ưu hóa (Phương trình 4):
    $$\min_{\beta} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p |\beta_j|$$
  - Cơ chế hình phạt chuẩn $L_1$: Thành phần $\lambda \sum_{j=1}^p |\beta_j|$ áp đặt hình phạt tỷ lệ thuận với giá trị tuyệt đối của các hệ số hồi quy.
  - Vai trò siêu tham số $\lambda$: Hệ số $\lambda \ge 0$ kiểm soát cường độ điều chuẩn. Khi $\lambda$ tăng, mô hình co mạnh các trọng số về gần $0$.
  - Khả năng chọn lọc đặc trưng tự động (Feature Selection): Hình phạt $L_1$ có dạng hình học góc nhọn tại các trục tọa độ. Đặc tính này triệt tiêu hoàn toàn một số hệ số $\beta_j$ về đúng bằng $0$.
  - Kiểm soát hiện tượng quá khớp (Overfitting): Việc loại bỏ các biến dư thừa giúp đơn giản hóa mô hình và giảm thiểu nguy cơ học thuộc lòng nhiễu dữ liệu.
  - Hạn chế trên dữ liệu tương quan cao: Khi các thông số MBR có tương quan mạnh, Lasso có xu hướng chọn ngẫu nhiên một biến và triệt tiêu các biến còn lại.
- Mô hình Hồi quy Ridge (Ridge Regression):
  - Khái niệm: Hồi quy Ridge bổ sung thành phần điều chuẩn chuẩn $L_2$ vào hàm tổn thất bình phương tối thiểu thông thường.
  - Hàm mục tiêu tối ưu hóa (Phương trình 5):
    $$\min_{\beta} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2$$
  - Cơ chế hình phạt chuẩn $L_2$: Thành phần $\lambda \sum_{j=1}^p \beta_j^2$ xử phạt nặng các hệ số có giá trị biên độ lớn.
  - Ổn định nghiệm bài toán: Hình phạt $L_2$ thu nhỏ đều các hệ số $\beta_j$ nhưng không làm chúng triệt tiêu hoàn toàn về $0$.
  - Xử lý hiện tượng đa cộng tuyến (Multicollinearity): Các biến vận hành trong trạm MBR (như $MLSS$, $SV30$, $SVI$) thường có mức tương quan tuyến tính rất cao.
  - Giảm phương sai dự báo: Hồi quy Ridge tăng độ ổn định số học cho ma trận nghịch đảo nghịch đảo suy biến $(X^T X + \lambda I)^{-1}$. Mô hình giảm độ nhạy trước các biến động ngẫu nhiên trong dữ liệu đo đạc.
- Mô hình Hồi quy Elastic Net (Elastic Net Regression):
  - Khái niệm: Elastic Net tích hợp đồng thời hai kỹ thuật điều chuẩn chuẩn $L_1$ (Lasso) và chuẩn $L_2$ (Ridge).
  - Hàm mục tiêu tối ưu hóa (Phương trình 6):
    $$\min_{\beta} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \left[ \alpha \sum_{j=1}^p |\beta_j| + \frac{1 - \alpha}{2} \sum_{j=1}^p \beta_j^2 \right]$$
  - Ý nghĩa các tham số điều khiển:
    - $\lambda$: Tham số điều chỉnh tổng cường độ điều chuẩn cho toàn bộ mô hình.
    - $\alpha \in [0, 1]$: Tỷ lệ phân bổ trọng số giữa hình phạt $L_1$ và $L_2$.
    - Khi $\alpha = 1$, mô hình trở về dạng Hồi quy Lasso thuần túy.
    - Khi $\alpha = 0$, mô hình trở về dạng Hồi quy Ridge thuần túy.
  - Khắc phục nhược điểm của Lasso: Elastic Net hỗ trợ hiệu ứng nhóm (grouping effect). Khi một nhóm đặc trưng có tương quan chặt chẽ với nhau, mô hình giữ lại toàn bộ nhóm thay vì chỉ giữ ngẫu nhiên một biến.
  - Độ phù hợp dữ liệu: Elastic Net đặc biệt hiệu quả trên các tập dữ liệu có số lượng chiều lớn và tồn tại các liên kết tương quan phức tạp.

#### 2.4.2. Các mô hình học máy tăng cường độ dốc (Gradient Boosting Machine Learning Models)
- Vai trò của mô hình học máy dạng cây: Các thuật toán học máy giải quyết triệt để tính phi tuyến, sự trễ pha thời gian và các tương tác bậc cao trong quá trình tắc màng MBR.
- Mô hình XGBoost (eXtreme Gradient Boosting):
  - Khái niệm: XGBoost là thuật toán tăng cường cây quyết định tối ưu hóa cao. Thuật toán hỗ trợ xử lý song song và tăng tốc tính toán trên quy mô lớn.
  - Hàm mục tiêu tổng quát tại vòng lặp thứ $t$ (Phương trình 7):
    $$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t)}\right) + \sum_{k=1}^K \left( \gamma T_k + \frac{1}{2} \lambda \|\omega_k\|^2 \right)$$
  - Thành phần hàm mất mát: $l\left(y_i, \hat{y}_i^{(t)}\right)$ là hàm đo lường độ sai lệch giữa giá trị thực tế $y_i$ và giá trị dự đoán $\hat{y}_i^{(t)}$ ở vòng lặp thứ $t$.
  - Thành phần điều chuẩn cây: Đại lượng $\gamma T_k + \frac{1}{2} \lambda \|\omega_k\|^2$ kiểm soát trực tiếp độ phức tạp của từng cây quyết định thành phần $k$.
  - Ý nghĩa biến số cấu trúc cây: $T_k$ biểu thị tổng số lượng nút lá trên cây thứ $k$. Vector $\omega_k$ đại diện cho trọng số dự đoán tại các nút lá đó.
  - Tham số phạt độ phức tạp:
    - $\gamma$: Ngưỡng phạt tối thiểu trên mỗi nút lá mới tạo ra. Tham số này hỗ trợ quá trình cắt tỉa cành cây (pruning) để ngăn mở rộng cây quá mức.
    - $\lambda$: Hệ số phạt chuẩn $L_2$ trên trọng số các nút lá $\omega$. Tham số này làm mượt các dự báo cực đoan.
  - Tối ưu hóa chuỗi Taylor bậc hai: XGBoost khai triển chuỗi Taylor đến bậc hai cho hàm mất mát. Kỹ thuật này sử dụng cả đạo hàm bậc một (gradient $g_i$) và đạo hàm bậc hai (hessian $h_i$), giúp thuật toán hội tụ nhanh và chính xác hơn.
- Mô hình CatBoost (Category Boosting):
  - Khái niệm: CatBoost là thuật toán học máy tăng cường độ dốc phát triển bởi Yandex. Thuật toán tối ưu hóa vượt trội trên các tập dữ liệu dạng bảng (tabular data).
  - Hàm mục tiêu tổng quát (Phương trình 8):
    $$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t)}\right) + \sum_{k=1}^K \left( \gamma T_k + \frac{1}{2} \lambda \|\omega_k\|^2 \right) + R_{\text{ordered}}(D)$$
  - Thành phần điều chuẩn mở rộng $R_{\text{ordered}}(D)$: Đại lượng phạt này hình thành trực tiếp từ nguyên lý tăng cường có thứ tự (Ordered Boosting).
  - Kỹ thuật Ordered Boosting:
    - Cơ chế loại bỏ rò rỉ mục tiêu (Target Leakage): Các thuật toán boosting truyền thống dùng toàn bộ tập dữ liệu để tính gradient cho cây kế tiếp. Cách làm này tạo ra sự thiên lệch thông tin (prediction shift).
    - Nguyên lý thứ tự: CatBoost hoán vị ngẫu nhiên tập dữ liệu. Thuật toán tính toán gradient của mẫu dữ liệu hiện tại chỉ dựa trên các mẫu xuất hiện phía trước nó trong dãy thứ tự.
    - Loại bỏ sai lệch ước lượng gradient (Gradient Estimation Bias): Kỹ thuật này giúp mô hình không bị quá khớp trên dữ liệu huấn luyện, duy trì khả năng tổng quát hóa cao.
  - Cấu trúc cây quyết định đối xứng (Symmetric Trees / Oblivious Trees):
    - Cùng một tiêu chuẩn phân nhánh: CatBoost sử dụng cùng một điều kiện kiểm tra trên tất cả các nút tại cùng một tầng của cây quyết định.
    - Tốc độ suy luận cao: Cấu trúc cân đối cho phép biên dịch cây thành các chỉ mục nhị phân đơn giản, tăng tốc độ tính toán dự báo thời gian thực.
    - Tính kháng quá khớp vượt trội: Cây đối xứng đóng vai trò như một bộ điều chuẩn cấu trúc tự nhiên, ngăn ngừa các nhánh cây quá sâu và dị biệt.

#### 2.4.3. Quy trình làm việc và chiến lược kiểm soát quá khớp (Workflow & Overfitting Control)
- Quy trình học máy 4 giai đoạn khép kín:
  - Giai đoạn nạp dữ liệu đầu vào (Input): Tiếp nhận các đặc trưng vận hành đã qua tiền xử lý, gồm tỷ lệ $F/M$, nồng độ bùn $MLSS$, $DO$, $pH$, $Temp$, $SV30$, $SVI$, $COD\ RM$ và các biến trung bình trượt thời gian.
  - Giai đoạn huấn luyện thuật toán (Training): Tối ưu hóa lặp các cây quyết định, giảm thiểu sai số hồi quy đồng thời áp đặt các mức phạt chống quá khớp.
  - Giai đoạn phát sinh dự báo đầu ra (Output): Xuất dự đoán thông lượng riêng $\text{Spec. Flux} = \frac{\text{Flux}}{\text{TMP}}$, định lượng trực tiếp và tường minh mức độ suy giảm độ thấm của màng.
  - Giai đoạn diễn giải kết quả (Interpretation): Áp dụng giá trị Shapley từ SHAP để định lượng tỷ lệ đóng góp của từng thông số, cung cấp đòn bẩy điều khiển trực tiếp cho kỹ sư vận hành trạm.
- Bốn chiến lược kiểm soát hiện tượng quá khớp (Overfitting Prevention Strategies):
  - Kiểm định chéo 5 phần (5-Fold Cross-Validation):
    - Phân chia dữ liệu: Chia ngẫu nhiên tập huấn luyện thành $5$ phần có kích thước tương đương nhau.
    - Vòng lặp thẩm định: Huấn luyện mô hình trên $4$ phần và đánh giá hiệu năng trên phần còn lại. Lặp lại quá trình $5$ lần để lấy sai số trung bình.
    - Mục đích: Đảm bảo ước lượng khách quan hiệu năng mô hình trên tập dữ liệu nhỏ $194$ mẫu, tránh hiện tượng thiên vị do cách chia tập dữ liệu đơn lẻ.
  - Dừng huấn luyện sớm (Early Stopping):
    - Áp dụng trên CatBoost và XGBoost: Theo dõi liên tục giá trị hàm mất mát (loss) trên tập dữ liệu kiểm định qua từng vòng lặp tăng cường (boosting iteration).
    - Ngưỡng dừng: Tự động ngừng quá trình huấn luyện khi sai số kiểm định không còn cải thiện sau một số chu kỳ quy định trước.
    - Hiệu quả: Ngăn chặn cây thuật toán tiếp tục phân nhánh học thuộc lòng các nhiễu đo lường ngẫu nhiên trong pha huấn luyện cuối.
  - Tinh chỉnh siêu tham số bằng tìm kiếm lưới (Grid Search):
    - Quét không gian tham số: Tự động hóa đánh giá toàn diện các tổ hợp siêu tham số quan trọng gồm độ sâu cây (tree depth), tốc độ học (learning rate) và các hệ số điều chuẩn $\lambda$, $\gamma$.
    - Lựa chọn tối ưu: Chọn cấu hình siêu tham số đạt điểm số kiểm định chéo cao nhất để huấn luyện mô hình hoàn thiện.
  - Giới hạn độ phức tạp cấu trúc mô hình (Model Complexity Control):
    - Giới hạn độ sâu tối đa của cây (Max Tree Depth): Thiết lập trần độ sâu cho các cây quyết định, ngăn việc hình thành các mẫu kết hợp quá chuyên biệt.
    - Ràng buộc trọng số nút lá tối thiểu (Min Child Weight): Đòi hỏi một số lượng mẫu tối thiểu nhất định tại mỗi nút con trước khi thực hiện phân nhánh tiếp theo.

### 2.5. Khung Trí tuệ nhân tạo có thể giải thích (Explainable AI - XAI Framework)

#### 2.5.1. Phân tích độ quan trọng của đặc trưng (Feature Importance Analysis)
- Mục tiêu triển khai XAI: Mở rộng tính minh bạch của các mô hình học máy dạng hộp đen (black box). XAI giúp kỹ sư hiểu rõ cơ chế chi phối sự suy giảm thông lượng riêng và gia tăng áp suất xuyên màng.
- Phương pháp Độ quan trọng tích hợp (Built-in Feature Importance):
  - Cơ chế tính toán nội tại: Phương pháp này dựa trên cấu trúc các cây quyết định đã được huấn luyện trong mô hình tăng cường độ dốc.
  - Tiêu chí đánh giá: Đo lường tổng mức suy giảm độ vẩn đục hoặc mức cải thiện hàm mất mát (loss reduction) khi một biến được chọn để phân chia nút lá trên toàn bộ các cây.
  - Hạn chế: Phương pháp tích hợp thường thiên vị các đặc trưng liên tục có nhiều giá trị phân nhánh hoặc các biến có tương quan cao.
- Phương pháp Độ quan trọng hoán vị (Permutation Feature Importance):
  - Nguyên lý đánh giá độc lập: Phương pháp đo lường tầm quan trọng của đặc trưng trực tiếp trên tập dữ liệu kiểm tra độc lập.
  - Quy trình xáo trộn giá trị: Hoán vị ngẫu nhiên các giá trị của một đặc trưng khảo sát duy nhất, trong khi giữ nguyên giá trị của tất cả các đặc trưng khác.
  - Đo lường mức sụt giảm hiệu năng: So sánh sự thay đổi của chỉ số sai số (mức tăng RMSE hoặc mức giảm $R^2$) trước và sau khi xáo trộn giá trị đặc trưng.
  - Bản chất đánh giá: Nếu việc hoán vị một biến làm sai số mô hình tăng vọt, biến đó giữ vai trò cốt lõi trong khả năng dự báo. Ngược lại, nếu sai số biến đổi không đáng kể, mô hình không phụ thuộc vào biến đó.
- Phân tích thực nghiệm so sánh trên mô hình CatBoost:
  - Vị thế thống trị của biến trung bình trượt $F/M\_MA5$: Biến $F/M\_MA5$ đạt tỷ lệ quan trọng cao nhất ở cả ba thước đo phân tích (Built-in đạt $22.65\%$, Permutation đạt $33.70\%$, SHAP đạt $26.17\%$).
  - Bảng tổng hợp mức đóng góp thực nghiệm của các đặc trưng (Bảng 10):
    - $F/M\_MA5$: Built-in $22.65\%$; Permutation $33.70\%$; SHAP $26.17\%$.
    - $F/M$: Built-in $12.05\%$; Permutation $16.19\%$; SHAP $13.23\%$.
    - $MLSS$: Built-in $9.22\%$; Permutation $12.18\%$; SHAP $10.04\%$.
    - $pH\_MA5$: Built-in $9.16\%$; Permutation $11.03\%$; SHAP $7.19\%$.
    - $DO$: Built-in $4.26\%$; Permutation $0.82\%$; SHAP $7.06\%$.
    - $Temp$: Built-in $5.18\%$; Permutation $3.70\%$; SHAP $6.19\%$.
    - $Temp\_MA5$: Built-in $4.55\%$; Permutation $6.71\%$; SHAP $4.95\%$.
    - $COD\ RM$: Built-in $6.79\%$; Permutation $1.64\%$; SHAP $4.16\%$.
    - $DO\_MA5$: Built-in $2.93\%$; Permutation $1.51\%$; SHAP $3.38\%$.
    - $SV30$: Built-in $2.55\%$; Permutation $1.39\%$; SHAP $3.21\%$.
    - $MLSS\_MA5$: Built-in $3.56\%$; Permutation $2.37\%$; SHAP $3.05\%$.
    - $SV30\_MA5$: Built-in $5.30\%$; Permutation $3.28\%$; SHAP $3.04\%$.
    - $pH$: Built-in $3.92\%$; Permutation $2.06\%$; SHAP $2.96\%$.
    - $SVI$: Built-in $3.40\%$; Permutation $2.16\%$; SHAP $2.83\%$.
    - $SVI\_MA5$: Built-in $4.47\%$; Permutation $1.25\%$; SHAP $2.54\%$.
  - Đối chiếu giữa Built-in và Permutation (Hình 6): Khi loại bỏ thông tin từ $F/M\_MA5$, mô hình CatBoost chịu sự suy giảm hiệu năng nghiêm trọng nhất. Các biến $MLSS$, $pH\_MA5$ và $Temp$ cũng xác nhận tầm ảnh hưởng rõ rệt đến độ ổn định thủy lực màng.

#### 2.5.2. Phương pháp giải thích phụ gia Shapley (Shapley Additive Explanations - SHAP)
- Nền tảng lý thuyết trò chơi hợp tác (Cooperative Game Theory):
  - Nguồn gốc lý thuyết: Kỹ thuật SHAP phát triển từ lý thuyết giá trị Shapley do nhà toán học Lloyd Shapley đề xuất năm 1953.
  - Phân bổ phần thưởng công bằng: Trong bối cảnh học máy, dự đoán của mô hình là tổng tiền thưởng chung của một liên minh. Các đặc trưng đầu vào đóng vai trò là những người chơi hợp tác để tạo nên dự đoán đó.
- Biểu thức toán học chuẩn tắc của giá trị Shapley (Phương trình 9):
  $$\phi_i(f) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(n - |S| - 1)!}{n!} [f_x(S \cup \{i\}) - f_x(S)]$$
  - Ý nghĩa các thành phần công thức:
    - $\phi_i(f)$: Giá trị Shapley biểu thị đóng góp biên trung bình của đặc trưng thứ $i$ vào kết quả đầu ra của mô hình $f$.
    - $N$: Tập hợp chứa toàn bộ $n$ đặc trưng đầu vào của mô hình ($|N| = n$).
    - $S$: Tập con bất kỳ gồm các đặc trưng được chọn, thỏa mãn điều kiện không chứa đặc trưng $i$ ($S \subseteq N \setminus \{i\}$).
    - $|S|$: Số lượng các phần tử hiện diện trong tập con $S$.
    - $f_x(S)$: Giá trị dự đoán của mô hình khi chỉ sử dụng nhóm đặc trưng trong tập $S$.
    - $f_x(S \cup \{i\}) - f_x(S)$: Đóng góp biên (marginal contribution) của đặc trưng $i$ khi tham gia vào tập hợp liên minh $S$.
    - Hệ số tổ hợp $\frac{|S|!(n - |S| - 1)!}{n!}$: Trọng số chuẩn hóa dựa trên xác suất xuất hiện của liên minh $S$ qua tất cả các thứ tự hoán vị có thể có của tập đặc trưng $N$.
- Bốn tiên đề toán học cốt lõi bảo đảm tính công bằng:
  - Tiên đề Hiệu quả và Tính cộng dồn (Efficiency / Additivity): Tổng tất cả các giá trị Shapley $\phi_i$ của các đặc trưng bằng đúng độ chênh lệch giữa dự đoán mô hình $f(x)$ và giá trị dự đoán trung bình toàn cục $\mathbb{E}[f(x)]$:
    $$\sum_{i=1}^n \phi_i = f(x) - \mathbb{E}[f(x)]$$
  - Tiên đề Đối xứng (Symmetry): Nếu hai đặc trưng $i$ và $j$ mang lại mức đóng góp biên hoàn toàn bằng nhau cho mọi liên minh $S$ khả dĩ ($f_x(S \cup \{i\}) = f_x(S \cup \{j\})$ với mọi $S$), giá trị Shapley của hai đặc trưng đó phải bằng nhau ($\phi_i = \phi_j$).
  - Tiên đề Người chơi vô giá trị (Dummy / Null Player): Nếu đặc trưng $i$ không làm thay đổi giá trị dự đoán trên mọi liên minh ($f_x(S \cup \{i\}) = f_x(S)$ với mọi $S$), giá trị Shapley của đặc trưng đó bắt buộc phải bằng $0$ ($\phi_i = 0$).
  - Tiên đề Tính nhất quán (Monotonicity / Consistency): Nếu mô hình thay đổi khiến đóng góp biên của đặc trưng $i$ tăng lên hoặc giữ nguyên đối với mọi liên minh $S$, giá trị Shapley của đặc trưng $i$ không được phép sụt giảm.
- Phân tích biểu đồ tóm tắt SHAP (SHAP Summary Plot - Hình 7):
  - Cách thức hiển thị: Mỗi điểm trên biểu đồ đại diện cho một mẫu quan sát trong bộ dữ liệu kiểm tra.
  - Tọa độ trục hoành: Vị trí của điểm trên trục ngang thể hiện giá trị SHAP ($\phi_i$). Điểm nằm về phía bên phải làm tăng giá trị $\text{Spec. Flux}$, điểm nằm về bên trái kéo giảm giá trị này.
  - Thang dải màu sắc: Thể hiện độ lớn thực tế của đặc trưng (màu đỏ chỉ giá trị đặc trưng cao, màu xanh lam chỉ giá trị đặc trưng thấp).
  - Tác động động học của tỷ lệ $F/M\_MA5$ và $F/M$:
    - Các điểm màu đỏ ($F/M\_MA5$ ở mức cao) phân bố lệch về phía bên phải, đóng góp tích cực vào việc gia tăng thông lượng riêng $\text{Spec. Flux}$.
    - Các điểm màu xanh lam ($F/M\_MA5$ ở mức thấp) dồn mạnh về phía âm bên trái, kéo tụt độ thấm và thúc đẩy hiện tượng tắc màng.
  - Tác động của nồng độ sinh khối $MLSS$:
    - Giá trị $MLSS$ cao (màu đỏ) nằm ở phía dương, duy trì thông lượng ổn định nhờ khả năng xử lý sinh học tốt.
    - Nồng độ bùn quá thấp (màu xanh lam) tương quan với sự suy giảm thông lượng thấm qua màng.
  - Ảnh hưởng của thông số $pH\_MA5$: Các điểm màu xanh lam (độ pH thấp) kéo giá trị dự đoán về phía âm, làm tăng nguy cơ tắc màng nghiêm trọng.
  - Ảnh hưởng của nhiệt độ nước thải ($Temp$): Giá trị nhiệt độ cao hơn hỗ trợ cải thiện và ổn định thông lượng lọc màng.

#### 2.5.3. Ý nghĩa vận hành thực tế và tối ưu hóa hệ thống MBR (Operational Implications for MBR Optimization)
- Chuyển dịch từ giám sát thụ động sang kiểm soát chủ động: Khung mô hình XAI giúp trạm xử lý không chỉ thụ động chờ đợi tín hiệu cảnh báo áp suất $\text{TMP}$ tăng vọt. Vận hành viên có thể can thiệp sớm vào quá trình sinh học trước khi tắc màng diễn ra.
- Xác thực khoa học giữa AI và cơ chế hóa - sinh học:
  - Khung XAI định lượng hai yếu tố chi phối lớn nhất là tỷ lệ $F/M$ và nồng độ $MLSS$ (tổng tỷ lệ đóng góp vượt $25\%$).
  - Kết quả này hoàn toàn nhất quán với các mô hình cơ chế truyền thống, chứng minh rằng $F/M$ và $MLSS$ là các tác nhân gốc rễ chi phối độ nhớt của bùn và tốc độ hình thành lớp bánh bùn (cake layer) trên bề mặt màng.
- Cơ sở khoa học để thiết lập đòn bẩy vận hành trạm MBR:
  - Kiểm soát tỷ lệ $F/M$: Điều chỉnh lưu lượng cơ chất nạp vào ngăn hiếu khí nhằm tránh rơi vào vùng $F/M$ quá thấp gây bài tiết polyme ngoại bào (EPS) và sản phẩm vi sinh vật hòa tan (SMP).
  - Duy trì nồng độ bùn $MLSS$ tối ưu: Quản lý nồng độ bùn trong phạm vi thích hợp ($7000 - 8500\text{ mg/L}$) để cân bằng giữa hiệu suất xử lý nước và lực cản thủy lực màng.
  - Điều chỉnh độ pH và nhiệt độ: Khống chế dải pH trung bình trượt để bảo tồn hoạt tính vi sinh và ngăn cản muối vô cơ kết tủa trên bề mặt màng lọc.
- Tính khả thi kinh tế cho các nhà máy quy mô công nghiệp:
  - Khung dự đoán chỉ sử dụng các thông số đo đạc thường quy sẵn có tại các trạm xử lý nước thải.
  - Không cần lắp đặt các đầu đo trực tuyến đắt tiền và khó bảo trì trong môi trường bùn nồng độ cao. Mô hình giúp giảm thiểu chi phí đầu tư thiết bị quan trắc chuyên dụng.
- Khả năng mở rộng và chuyển giao công nghệ (Scalability):
  - Phương pháp kết hợp biến trung bình trượt thời gian, chuẩn hóa thang đo Robust Scaling và thuật toán CatBoost có thể chuyển giao linh hoạt cho các công nghệ lọc màng khác như màng thẩm thấu ngược (RO) hoặc siêu lọc công nghiệp (UF).
  - Nền tảng XAI mang lại độ tin cậy toán học vững chắc, mở đường cho việc tích hợp mô hình vào các hệ thống điều khiển tự động hóa thích ứng theo thời gian thực.
