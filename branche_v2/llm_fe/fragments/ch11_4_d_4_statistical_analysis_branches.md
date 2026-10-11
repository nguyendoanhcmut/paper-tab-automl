### D.4 Phân tích thống kê (Statistical Analysis)

- **Mục tiêu và Thiết kế Kiểm định Thống kê (Test Setup & Directional Formulation)**:
  - Để đánh giá một cách chặt chẽ liệu kỹ thuật tạo đặc trưng (feature engineering - FE) có mang lại những cải thiện có ý nghĩa thống kê (statistically significant improvements) so với tập đặc trưng thô ban đầu (raw feature set) hay không, nghiên cứu tiến hành các kiểm định thứ hạng có dấu Wilcoxon một phía (one-tailed Wilcoxon signed-rank tests) nhằm so sánh đối đầu giữa LLM-FE và mô hình cơ sở XGBoost (`Base`).
  - **Lý do lựa chọn kiểm định một phía (One-tailed formulation)**: Thiết kế kiểm định một phía hoàn toàn phù hợp và chuẩn xác về mặt phương pháp luận vì giả thuyết nghiên cứu mang tính định hướng nghiêm ngặt (strictly directional hypothesis): kỹ thuật tạo đặc trưng phải nâng cao hiệu năng dự đoán (predictive performance) so với việc chỉ sử dụng các đặc trưng thô ban đầu, chứ không chỉ dừng ở việc kiểm tra sự khác biệt hai chiều.
  - **Quy trình ghép cặp và độ tin cậy thực nghiệm**:
    - Kiểm định được tiến hành dựa trên $25$ quan sát ghép đôi (paired observations) cho mỗi tập dữ liệu, thu thập từ $5$ hạt giống ngẫu nhiên (random seeds) khác nhau kết hợp cùng kỹ thuật kiểm định chéo $5$ lượt ($5$-fold cross-validation) ($5 \times 5 = 25$ lượt chạy độc lập).
    - Ngưỡng đánh giá sử dụng khoảng tin cậy 95% (95% confidence intervals).

- **Kết quả Kiểm định Định lượng Tổng thể**:
  - **Tác vụ Hồi quy (Regression tasks)**: LLM-FE đạt được sự cải thiện vượt trội có ý nghĩa thống kê trên toàn bộ $10/10$ tập dữ liệu hồi quy ($100\%$) với giá trị $p < 0.001$.
  - **Tác vụ Phân loại (Classification tasks)**: LLM-FE đạt được sự cải thiện có ý nghĩa thống kê trên $8/15$ tập dữ liệu ($p < 0.05$), đồng thời đạt mức cải thiện cận biên có ý nghĩa (marginally significant improvements) trên $2/15$ tập dữ liệu khác.
  - Tổng hợp lại, có tới $18/25$ tập dữ liệu thử nghiệm ($72\%$) ghi nhận sự vượt trội có ý nghĩa thống kê hoặc cải thiện cận biên rõ rệt so với mô hình cơ sở.

- **Kết quả Kiểm định Ý nghĩa Thống kê Wilcoxon Một phía (Table 14)**:
  - *Quy ước hiển thị*: **In đậm (bold)** biểu thị cải thiện có ý nghĩa thống kê ($p < 0.05$ cho phân loại, $p < 0.001$ cho hồi quy); <u>Gạch chân (underline)</u> biểu thị cải thiện có ý nghĩa cận biên (marginally significant); các giá trị được biểu diễn dưới dạng $\text{Mean} \pm \text{Std}$.

#### Tác vụ Phân loại (Classification Tasks — Accuracy ↑)

| Tập dữ liệu (Dataset) | Base (XGBoost) | LLM-FE | Mức ý nghĩa thống kê |
| :--- | :---: | :---: | :--- |
| `adult` | $0.872 \pm 0.002$ | $\mathbf{0.874 \pm 0.003}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `bank` | $0.906 \pm 0.002$ | $\mathbf{0.907 \pm 0.003}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `breast-w` | $0.955 \pm 0.014$ | $\mathbf{0.963 \pm 0.012}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `blood` | $0.747 \pm 0.023$ | $0.743 \pm 0.024$ | Không có ý nghĩa |
| `car` | $0.992 \pm 0.005$ | $\mathbf{0.998 \pm 0.004}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `cdc-diabetes` | $0.849 \pm 0.001$ | $\mathbf{0.849 \pm 0.001}$ | Có ý nghĩa thống kê ($p < 0.05$)* |
| `cmc` | $0.527 \pm 0.029$ | $0.527 \pm 0.024$ | Không có ý nghĩa |
| `communities` | $0.699 \pm 0.020$ | <u>$0.703 \pm 0.019$</u> | Cận biên có ý nghĩa (Marginal) |
| `covtype` | $0.871 \pm 0.002$ | $\mathbf{0.878 \pm 0.001}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `credit-g` | $0.754 \pm 0.028$ | <u>$0.758 \pm 0.027$</u> | Cận biên có ý nghĩa (Marginal) |
| `eucalyptus` | $0.659 \pm 0.029$ | $\mathbf{0.671 \pm 0.029}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `heart` | $0.861 \pm 0.022$ | $0.857 \pm 0.026$ | Không có ý nghĩa |
| `myocardial` | $0.785 \pm 0.025$ | $0.788 \pm 0.029$ | Không có ý nghĩa |
| `pc1` | $0.931 \pm 0.010$ | $\mathbf{0.937 \pm 0.008}$ | Có ý nghĩa thống kê ($p < 0.05$) |
| `vehicle` | $0.761 \pm 0.028$ | $0.767 \pm 0.030$ | Không có ý nghĩa |

*\*Ghi chú về `cdc-diabetes`*: Dù giá trị trung bình làm tròn hiển thị tương đương ($0.849 \pm 0.001$), phép kiểm định cặp thứ hạng trên $25$ mẫu quan sát chi tiết cho thấy phân phối cải thiện có ý nghĩa thống kê ở mức $p < 0.05$.

#### Tác vụ Hồi quy (Regression Tasks — RMSE ↓)

| Tập dữ liệu (Dataset) [Hệ số tỉ lệ] | Base (XGBoost) | LLM-FE | Mức ý nghĩa thống kê |
| :--- | :---: | :---: | :--- |
| `forest-fires` $[10^0]$ | $1.649 \pm 0.116$ | $\mathbf{1.567 \pm 0.116}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `housing` $[10^4]$ | $4.801 \pm 0.118$ | $\mathbf{4.422 \pm 0.144}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `insurance` $[10^3]$ | $5.280 \pm 0.306$ | $\mathbf{5.117 \pm 0.353}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `bike` $[10^1]$ | $4.078 \pm 0.122$ | $\mathbf{3.976 \pm 0.137}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `wine` $[10^{-1}]$ | $6.370 \pm 0.190$ | $\mathbf{6.130 \pm 0.190}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `crab` $[10^0]$ | $2.309 \pm 0.092$ | $\mathbf{2.215 \pm 0.097}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `diamond` $[10^2]$ | $5.482 \pm 0.104$ | $\mathbf{5.365 \pm 0.131}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `airfoil_self_noise` $[10^0]$ | $1.547 \pm 0.127$ | $\mathbf{1.435 \pm 0.113}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `cpu_small` $[10^0]$ | $2.833 \pm 0.210$ | $\mathbf{2.718 \pm 0.219}$ | Có ý nghĩa thống kê ($p < 0.001$) |
| `plasma_retinol` $[10^2]$ | $2.336 \pm 0.238$ | $\mathbf{2.240 \pm 0.268}$ | Có ý nghĩa thống kê ($p < 0.001$) |

- **Ý nghĩa Thực nghiệm và Kết luận Khoa học**:
  - **Tính nhất quán xuyên suốt các bài toán hồi quy**: Việc $10/10$ tập dữ liệu hồi quy đều đạt cải thiện có ý nghĩa thống kê cao ($p < 0.001$) chứng minh rằng trong không gian biến liên tục, việc tạo lập các biến đặc trưng mới dưới sự dẫn dắt của LLM (LLM-guided feature engineering) hỗ trợ mô hình dự đoán nắm bắt rất hiệu quả các quan hệ phi tuyến tính phức tạp.
  - **Độ tin cậy trong các bài toán phân loại**: Mặc dù không phải tuyệt đối $100\%$ các tập dữ liệu đều cho thấy cải thiện mang ý nghĩa thống kê (có $5/15$ tập dữ liệu chưa vượt ngưỡng ý nghĩa thống kê), nhưng sự tăng trưởng ở $10/15$ tập dữ liệu (8 tập có ý nghĩa thống kê và 2 tập cận biên) là bằng chứng thực nghiệm vững chắc.
  - **Khẳng định giá trị thực sự của tri thức LLM**: Những kết quả trên khẳng định rằng kỹ thuật tạo đặc trưng do LLM định hướng đem lại những bước tiến triển có ý nghĩa bản chất so với không gian đặc trưng thô ban đầu (meaningful improvements over the raw feature space), bác bỏ giả thuyết rằng các cải thiện này chỉ xuất hiện ngẫu nhiên hoặc do hiện tượng quá khớp (overfitting) cục bộ.
