## Appendix D Analysis on Spearman Correlation

### D.1 Spearman Correlation

* Tương quan Spearman (Spearman correlation) cung cấp tường minh hệ số tương quan giữa đặc trưng đầu vào (input feature) và biến mục tiêu (target variable) dựa trên thứ tự hạng (rank orders) của chúng.
  * Hệ số tương quan Spearman (Spearman correlation coefficient - SCC) định lượng mối quan hệ đơn điệu (monotonic relationship) giữa hai biến bằng cách tính toán tương quan Pearson (Pearson correlation) giữa các biến đã được xếp hạng (ranked variables).
  * Hệ số tương quan Spearman được xác định trong phạm vi $[-1, 1]$.
* Công thức tổng quát xác định hệ số tương quan Spearman $\rho_s$:
  * Hệ số $\rho_s$ được tính toán thông qua hiệp phương sai và độ lệch chuẩn của các giá trị hạng:
    $$\rho_s = \frac{\operatorname{cov}(\operatorname{rg}_X, \operatorname{rg}_Y)}{\sigma_{\operatorname{rg}_X} \sigma_{\operatorname{rg}_Y}} = \frac{\mathbb{E}[(\operatorname{rg}_X - \mu_{\operatorname{rg}_X})(\operatorname{rg}_Y - \mu_{\operatorname{rg}_Y})]}{\sigma_{\operatorname{rg}_X} \sigma_{\operatorname{rg}_Y}} \quad (5)$$
  * Trong đó:
    * $\operatorname{rg}_X$ và $\operatorname{rg}_Y$ biểu diễn các giá trị hạng (rank values) lần lượt của hai biến $X$ và $Y$.
    * $\operatorname{cov}(\operatorname{rg}_X, \operatorname{rg}_Y)$ ký hiệu hiệp phương sai (covariance) giữa chúng.
    * $\sigma_{\operatorname{rg}_X}$ và $\sigma_{\operatorname{rg}_Y}$ là độ lệch chuẩn (standard deviations) tương ứng của các biến hạng.
* Công thức tính toán tương quan Spearman trong trường hợp không có các hạng đồng hạng (no tied ranks):
  * Khi không xuất hiện các hạng bằng nhau (tied ranks), hệ số $\rho_s$ có thể được tính theo công thức:
    $$\rho_s = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)} \quad (6)$$
  * Trong đó:
    * $d_i$ là hiệu số giữa các thứ hạng của các giá trị tương ứng $X_i$ và $Y_i$.
    * $n$ là số lượng quan sát (number of observations).
* Ý nghĩa định lượng của hệ số tương quan Spearman ($\rho_s$):
  * Nếu $\rho_s = 0$: Biểu thị không có mối quan hệ đơn điệu (no monotonic relationship) giữa hai biến $X$ và $Y$.
  * Tương quan dương ($0 < \rho_s \le 1$): Ngụ ý rằng khi $X$ tăng, $Y$ cũng có xu hướng tăng theo.
  * Tương quan âm ($-1 \le \rho_s < 0$): Biểu thị rằng khi $X$ tăng, $Y$ có xu hướng giảm.
  * Độ lớn tuyệt đối $|\rho_s|$ càng gần $1$: Mối quan hệ đơn điệu giữa hai biến càng mạnh mẽ.

### D.2 Comparison with Other Feature Importance Metrics

* Đánh giá tính nhất quán của các xếp hạng độ quan trọng đặc trưng (feature importance rankings) qua hệ số $\tau$ của Kendall (Kendall’s $\tau$):
  * Bảng 9 (Table 9) thể hiện mức độ nhất quán giữa các phương pháp đo lường độ quan trọng đặc trưng gồm Pearson, SHAP, mutual information (thông tin tương hỗ) và Spearman:
    * Spearman: $\tau = 0.65$
    * Pearson: $\tau = 0.59$
    * SHAP: $\tau = 0.52$
    * Mutual Information: $\tau = 0.48$
* Cơ sở lựa chọn Spearman làm độ đo đánh giá chính (primary evaluation metric):
  * Spearman đạt điểm số nhất quán cao nhất ($\tau = 0.65$) trong tất cả các phương pháp ứng viên so sánh.
  * Điểm số này chứng minh xếp hạng độ quan trọng đặc trưng của Spearman đồng thuận và liên kết vững chắc nhất (aligns most robustly) với các độ đo khác.
  * Mức độ nhất quán vượt trội này khẳng định tương quan Spearman mang lại đánh giá đáng tin cậy nhất (most reliable assessment) về mức độ liên quan của đặc trưng (feature relevance) trong bối cảnh nghiên cứu.
