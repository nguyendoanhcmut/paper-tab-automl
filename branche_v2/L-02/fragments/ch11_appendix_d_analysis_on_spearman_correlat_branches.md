## Appendix D: Analysis on Spearman Correlation

* **Động cơ và vai trò của tương quan Spearman trong SymboLLM-FE:**
  * SymboLLM-FE sử dụng hệ số tương quan hạng Spearman ($\rho_s$) làm tiêu chuẩn định lượng tiên quyết để sắp xếp mức độ quan trọng biên của các đặc trưng ban đầu trước khi đưa vào cơ chế cửa sổ mở rộng - trượt (expanding-sliding window).
  * Mục tiêu của phụ lục: Cung cấp nền tảng toán học chặt chẽ của tương quan Spearman và kiểm chứng bằng thực nghiệm tính nhất quán của nó khi so sánh với các độ đo tầm quan trọng đặc trưng phổ biến khác.

### D.1 Spearman Correlation

* **Định nghĩa và bản chất toán học của hệ số tương quan Spearman:**
  * Hệ số tương quan Spearman ($\rho_s$, Spearman Rank Correlation Coefficient - SCC) định lượng mối quan hệ đơn điệu (monotonic relationship) giữa một đặc trưng đầu vào $X$ và biến mục tiêu $Y$ thông qua thứ tự xếp hạng (rank orders) của các giá trị quan sát.
  * Về mặt bản chất, tương quan Spearman chính là hệ số tương quan tuyến tính Pearson được tính toán trên các biến đã được chuyển đổi sang dạng thứ hạng (ranked variables).
  * Miền giá trị xác định: $\rho_s \in [-1, 1]$.

* **Công thức tổng quát tính tương quan Spearman (tổng quát cho trường hợp có thứ hạng đồng hạng):**
  * Đối với tập dữ liệu tổng quát (bao gồm cả trường hợp có các giá trị đồng hạng - tied ranks), $\rho_s$ được xác định theo công thức hiệp phương sai của các biến thứ hạng:
    $$\rho_s = \frac{\operatorname{cov}(\operatorname{rg}_X, \operatorname{rg}_Y)}{\sigma_{\operatorname{rg}_X} \sigma_{\operatorname{rg}_Y}} = \frac{\mathbb{E}\left[(\operatorname{rg}_X - \mu_{\operatorname{rg}_X})(\operatorname{rg}_Y - \mu_{\operatorname{rg}_Y})\right]}{\sigma_{\operatorname{rg}_X} \sigma_{\operatorname{rg}_Y}} \quad (5)$$
  * Trong đó:
    * $\operatorname{rg}_X$ và $\operatorname{rg}_Y$ biểu thị các vector giá trị thứ hạng tương ứng của hai biến số $X$ và $Y$.
    * $\operatorname{cov}(\operatorname{rg}_X, \operatorname{rg}_Y)$ là hiệp phương sai giữa thứ hạng của $X$ và thứ hạng của $Y$.
    * $\sigma_{\operatorname{rg}_X}$ và $\sigma_{\operatorname{rg}_Y}$ là độ lệch chuẩn (standard deviations) của các giá trị thứ hạng tương ứng.
    * $\mu_{\operatorname{rg}_X}$ và $\mu_{\operatorname{rg}_Y}$ là kỳ vọng toán học (giá trị trung bình) của thứ hạng $\operatorname{rg}_X$ và $\operatorname{rg}_Y$.

* **Công thức đơn giản hóa khi không có giá trị đồng hạng (no tied ranks):**
  * Trong trường hợp tất cả các giá trị quan sát đều phân biệt (không có hai phần tử nào trùng thứ hạng), hệ số tương quan Spearman có thể được tính toán trực tiếp và nhanh chóng qua hiệu số thứ hạng:
    $$\rho_s = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)} \quad (6)$$
  * Trong đó:
    * $n$ biểu thị tổng số lượng mẫu quan sát trong tập dữ liệu.
    * $d_i = \operatorname{rg}(X_i) - \operatorname{rg}(Y_i)$ là hiệu số giữa thứ hạng của giá trị $X_i$ và thứ hạng của giá trị $Y_i$ tại quan sát thứ $i$.

* **Ý nghĩa định lượng của các khoảng giá trị hệ số tương quan Spearman:**
  * **Trường hợp $\rho_s = 0$:** Biểu thị không tồn tại bất kỳ mối quan hệ đơn điệu (no monotonic relationship) nào giữa đặc trưng $X$ và biến mục tiêu $Y$.
  * **Trường hợp tương quan dương ($0 < \rho_s \le 1$):** Biểu thị mối quan hệ đồng biến đơn điệu, nghĩa là khi giá trị của $X$ tăng lên, giá trị của $Y$ cũng có xu hướng tăng theo. Khi $\rho_s = 1$, mối quan hệ đơn điệu tăng là tuyệt đối hoàn hảo.
  * **Trường hợp tương quan âm ($-1 \le \rho_s < 0$):** Biểu thị mối quan hệ nghịch biến đơn điệu, nghĩa là khi giá trị của $X$ tăng lên, giá trị của $Y$ có xu hướng giảm đi. Khi $\rho_s = -1$, mối quan hệ đơn điệu giảm là tuyệt đối hoàn hảo.
  * **Độ lớn tuyệt đối $|\rho_s|$:** Giá trị $|\rho_s|$ càng tiệm cận về $1$ thì mối quan hệ đơn điệu giữa hai biến càng mạnh mẽ, thể hiện độ quan trọng biên của đặc trưng đối với biến mục tiêu càng cao.

* **Ưu điểm tính toán và tính kháng nhiễu thống kê:**
  * **Phi tham số (Non-parametric):** Không phụ thuộc vào giả định phân phối chuẩn của dữ liệu, hoạt động ổn định trên các phân phối lệch (skewed distributions) và dữ liệu dạng bảng không đồng nhất.
  * **Bền vững trước điểm dị biệt (Robust to outliers):** Do chỉ phụ thuộc vào trật tự tương đối thay vì độ lớn khoảng cách số học tuyệt đối, các giá trị ngoại lai cực trị không làm sai lệch nghiêm trọng kết quả đánh giá.
  * **Bắt quan hệ phi tuyến tính đơn điệu (Nonlinear monotonic dependencies):** Khắc phục triệt để nhược điểm của tương quan tuyến tính Pearson, cho phép nhận diện các quan hệ hàm mũ, logarit hoặc đa thức đơn điệu.
  * **Hiệu quả tính toán vượt trội:** Độ phức tạp tính toán chỉ ở mức $O(n \log n)$ (chi phí sắp xếp thứ hạng), cực kỳ nhanh và tối ưu hóa thời gian thực thi so với việc huấn luyện mô hình học máy phức tạp.

### D.2 Comparison with Other Feature Importance Metrics

* **Phương pháp luận đánh giá tính nhất quán thứ hạng bằng hệ số Kendall's $\tau$:**
  * Để xác định độ tin cậy của tương quan Spearman trong việc phản ánh tầm quan trọng đặc trưng, nghiên cứu tiến hành đo lường mức độ đồng thuận thứ hạng giữa các phương pháp thông qua hệ số tương quan hạng Kendall ($\tau$, Kendall’s rank correlation coefficient).
  * Công thức xác định hệ số Kendall's $\tau$ dựa trên tỷ lệ giữa các cặp thứ hạng đồng thuận ($C$, concordant pairs) và nghịch đảo ($D$, discordant pairs) giữa hai danh sách xếp hạng đặc trưng:
    $$\tau = \frac{C - D}{\frac{1}{2} m (m - 1)}$$
    với $m$ là tổng số lượng đặc trưng được xếp hạng.
  * Điểm $\tau$ càng cao chứng tỏ thứ hạng đặc trưng do phương pháp đó đưa ra càng có sự nhất quán và tương thích bền vững (robust alignment) với tất cả các phương pháp đánh giá khác.

* **So sánh chi tiết với các tiêu chí độ đo tầm quan trọng đặc trưng khác:**
  * **Hệ số tương quan tuyến tính Pearson (Pearson Correlation Coefficient, $r$):**
    * Định nghĩa toán học: $r = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^n (X_i - \bar{X})^2 \sum_{i=1}^n (Y_i - \bar{Y})^2}}$.
    * Đặc điểm và hạn chế: Chỉ nắm bắt được mối quan hệ tuyến tính nghiêm ngặt; rất nhạy cảm với các điểm dị biệt và giả định dữ liệu tuân theo phân phối chuẩn.
    * Điểm nhất quán Kendall's $\tau$: Đạt mức $\tau = 0.59$, đứng thứ hai nhưng kém hơn Spearman do bỏ sót các phụ thuộc phi tuyến.
  * **Giá trị SHAP (SHapley Additive exPlanations):**
    * Định nghĩa toán học: Dựa trên lý thuyết trò chơi hợp tác để tính đóng góp biên trung bình của đặc trưng qua mọi tập con đặc trưng:
      $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} [f(S \cup \{i\}) - f(S)]$$
    * Đặc điểm và hạn chế: Có khả năng giải thích cục bộ và toàn cục tinh vi trên mô hình phi tuyến, nhưng chi phí tính toán bùng nổ theo cấp số nhân ($O(2^{|F|})$), đòi hỏi huấn luyện mô hình dự báo nền tảng và dễ biến thiên theo siêu tham số mô hình.
    * Điểm nhất quán Kendall's $\tau$: Đạt mức $\tau = 0.52$.
  * **Thông tin tương hỗ (Mutual Information - MI):**
    * Định nghĩa toán học: Đo lường độ phụ thuộc thông tin tổng quát thông qua entropy thông tin Shannon:
      $$I(X; Y) = \iint p(x, y) \log \frac{p(x, y)}{p(x)p(y)} \, dx \, dy$$
    * Đặc điểm và hạn chế: Mặc dù có khả năng nắm bắt mọi dạng phụ thuộc phi tuyến tính (kể cả phi đơn điệu), nhưng ước lượng MI trên mẫu hữu hạn phụ thuộc nặng nề vào kỹ thuật phân chia giỏ (binning) hoặc ước lượng mật độ hạt nhân (KDE), dẫn đến độ chệch lớn và độ ổn định thứ hạng kém.
    * Điểm nhất quán Kendall's $\tau$: Đạt mức $\tau = 0.48$ (mức thấp nhất trong bốn phương pháp).
  * **Độ quan trọng đặc trưng dựa trên cây và hoán vị (Tree-based & Permutation Feature Importance):**
    * Đánh giá qua độ suy giảm tạp chất trung bình (Mean Decrease Impurity - MDI) hoặc suy giảm hiệu năng khi hoán vị mẫu (Permutation Importance). Thường bị thiên lệch đối với các biến có số lượng giá trị duy nhất lớn (high-cardinality) và phụ thuộc chặt chẽ vào cấu trúc của từng họ mô hình cây cụ thể.

* **Kết quả thực nghiệm định lượng về tính nhất quán thứ hạng độ quan trọng đặc trưng:**
  * Bảng 9 tổng hợp điểm số nhất quán thứ hạng Kendall's $\tau$ giữa các phương pháp đánh giá độ quan trọng đặc trưng trên các tập dữ liệu thực nghiệm:
  * **Bảng 9.** Tính nhất quán thứ hạng độ quan trọng đặc trưng đo bằng Kendall's τ
    * <img src="assets/table_09_p17.png" alt="Bảng 9" />
    * **Bảng này chứng minh điều gì**
      * Thứ hạng tương quan Spearman có độ đồng thuận rất cao với các độ đo phức tạp khác
    * **Từ đâu mà thấy được**
      * Giá trị hệ số tương quan hạng Kendall's tau giữa Spearman và SHAP / Permutation Importance trên các tập dữ liệu
  * Phân tích chi tiết kết quả định lượng:
    * Hệ số tương quan Spearman đạt điểm nhất quán cao nhất trong tất cả các ứng viên với $\tau = 0.65$.
    * Xếp hạng nhất quán tổng thể theo thứ tự giảm dần: $\text{Spearman} \; (\tau = 0.65) > \text{Pearson} \; (\tau = 0.59) > \text{SHAP} \; (\tau = 0.52) > \text{Mutual Information} \; (\tau = 0.48)$.
    * Khoảng cách vượt trội: Spearman vượt hơn Pearson $+0.06$, vượt hơn SHAP $+0.13$, và vượt hơn Mutual Information $+0.17$ về độ đồng thuận thứ hạng.

* **Lý do lựa chọn tương quan Spearman làm độ đo tiên quyết trong SymboLLM-FE:**
  * **Độ tin cậy và sự đồng thuận cao nhất (Superior Agreement):** Điểm số $\tau = 0.65$ khẳng định thứ hạng của Spearman phản ánh mức độ liên quan của đặc trưng (feature relevance) một cách đáng tin cậy và ổn định nhất, không bị thiên lệch bởi cấu trúc mô hình hay ước lượng mật độ.
  * **Cân bằng tối ưu giữa độ chính xác và chi phí tính toán:** Trong khi các phương pháp như SHAP đòi hỏi chi phí tính toán khổng lồ và phụ thuộc mô hình hạ nguồn, Spearman cho phép tiền xử lý và xếp thứ tự toàn bộ đặc trưng trong thời gian $O(n \log n)$ mà vẫn đạt độ đồng thuận vượt trội.
  * **Hiệu quả thực tế trong quy trình SymboLLM-FE:** Việc xếp thứ tự đặc trưng theo Spearman cho phép thuật toán cửa sổ mở rộng - trượt ưu tiên kết hợp các đặc trưng có độ liên quan cao nhất trước, vừa thu hẹp không gian tìm kiếm từ $O(2^n)$ xuống cấp độ đa thức $O(n^2)$, vừa tối ưu hóa chất lượng công thức ký hiệu cho bước sinh đặc trưng tiếp theo của LLM.
