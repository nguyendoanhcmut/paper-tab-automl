### 5.5 Topology Graph Specialization

- **Định nghĩa và mục tiêu của chỉ số TGSS (Topology Graph Specialization Score - Điểm chuyên biệt hóa đồ thị tô-pô)**:
  - Nhằm đánh giá định lượng liệu đồ thị tô-pô (topology graph) của TOPOFE có tích lũy được tri thức đặc thù theo tác vụ (task-specific knowledge) về tính hữu dụng chuyển giao liên họ (cross-family transfer utility) trong tiến trình tìm kiếm hay không.
  - Ma trận trọng số chuyển giao tại thế hệ $t$ được ký hiệu là $W^{(t)} \in \mathbb{R}^{M \times M}$, trong đó mỗi phần tử ngoài đường chéo (off-diagonal entry) $w_{j \to i}^{(t)} \in [-1, 1]$ mã hóa tính hữu dụng đã học (learned utility) của đảo $j$ với vai trò tiền thân (precursor) cho đảo bão hòa $i$ (saturated island $i$) và được cập nhật theo Eq. 11.
  - TGSS được định nghĩa là phương sai thực nghiệm (empirical variance) của các trọng số chuyển giao ngoài đường chéo:
    $$\text{TGSS}(t) = \frac{1}{M(M - 1)} \sum_{\substack{j,i=1 \\ j \neq i}}^M \left( w_{j \to i}^{(t)} - \bar{w}^{(t)} \right)^2 \quad (19)$$
  - Trọng số ngoài đường chéo trung bình (mean off-diagonal weight) được tính theo công thức:
    $$\bar{w}^{(t)} = \frac{1}{M(M - 1)} \sum_{\substack{j,i=1 \\ j \neq i}}^M w_{j \to i}^{(t)} \quad (20)$$

- **Bản chất định lượng và vai trò xác thực của chỉ số TGSS đối với cơ chế chuyển giao thích ứng**:
  - TGSS định lượng độ phân kỳ cấu trúc (structural divergence) của ma trận trọng số so với trạng thái khởi tạo đều (uniform initialization): $\text{TGSS}(0) = 0$ khi tất cả trọng số bằng nhau và tăng dần khi đồ thị hình thành các thiên hướng phân hóa (differentiated preferences) trên các cặp đảo.
  - Giá trị TGSS cao chứng minh đồ thị tô-pô đã xác định được các hướng chuyển giao đạt năng suất cao (strongly productive) và các hướng kém hiệu quả (strongly unproductive) đặc thù cho tác vụ, từ đó tập trung định tuyến chuyển giao (transfer routing) tương ứng.
  - Giá trị TGSS xấp xỉ 0 (near-zero TGSS) phản ánh mọi cặp đảo đều đem lại tính hữu dụng chuyển giao gần như tương đương nhau và đồ thị duy trì sát với tiên nghiệm không mang thông tin (uninformative prior).
  - TGSS đo lường trực tiếp liệu cơ chế tô-pô thích ứng (adaptive topology mechanism) có thực sự thu nạp tri thức đặc thù tác vụ hay không, tạo ra sự phân biệt căn bản giữa TOPOFE với các phương pháp chuyển giao cố định (fixed) hoặc ngẫu nhiên (random transfer).

- **Phân tích quỹ đạo tiến hóa của TGSS qua 10 thế hệ thực nghiệm (Hình 2)**:
  - Toàn bộ các tập dữ liệu classification và regression đều bắt đầu tại $\text{TGSS}(0) = 0$ và tăng trưởng đơn điệu (increase monotonically) qua 10 thế hệ ($t = 1 \dots 10$), khẳng định đồ thị tô-pô liên tục chuyên biệt hóa rời xa tiên nghiệm đều ban đầu khi các sự kiện chuyển giao tích lũy.
  - Xu hướng tăng đơn điệu này là điều kiện tiên quyết bắt buộc (necessary precondition) để cơ chế định tuyến thích ứng đem lại lợi thế vượt trội so với việc chọn ngẫu nhiên đảo tiền thân (random precursor selection).
  - **Hình 2.** Quỹ đạo TGSS trên toàn bộ các tập dữ liệu classification (trái) và regression (phải) qua 10 thế hệ (Figure 2: TGSS trajectories across all classification (left) and regression (right) datasets over 10 generations).
    - <img src="assets/fig_02_p13_vector.png" alt="Hình 2" />
    - **Hình này chứng minh điều gì**
      - Đồ thị tô-pô liên tục chuyên biệt hóa rời xa phân phối đều ban đầu theo hướng đơn điệu tăng khi tích lũy các sự kiện chuyển giao, đồng thời mức độ chuyên biệt hóa mang tính phụ thuộc chặt chẽ vào tập dữ liệu và bản chất tác vụ.
    - **Từ đâu mà thấy được**
      - Trục hoành biểu diễn thế hệ $t$ (1 đến 10), trục tung biểu diễn $\text{TGSS}(t)$; toàn bộ đường cong bắt đầu tại $0.00$; nhóm Regression (phải) đi ngang sau thế hệ 3–4, còn Classification (trái) tiếp tục dốc lên đến thế hệ 10; biên độ hội tụ phân tán rộng từ sát $0.00$ (`blood`, `tic-tac-toe`) tới đỉnh $0.22$ (`vehicle`) và $0.24$ (`forest-fires`).

- **Ba quy luật cốt lõi (three patterns) rút ra từ phân tích liên kết toàn diện trên 29 tập dữ liệu**:
  - *Quy luật 1: Phương sai liên tập dữ liệu đáng kể khi hội tụ (Substantial inter-dataset variance at convergence)*:
    - Giá trị TGSS khi hội tụ trải rộng trong dải $[0.00, 0.22]$ đối với classification và $[0.04, 0.24]$ đối với regression, xác nhận mức độ cấu trúc hữu dụng liên họ có thể học được là thuộc tính phụ thuộc thực chất vào từng tập dữ liệu (genuinely dataset-dependent) thay vì là đặc tính thuật toán cố định (fixed algorithmic property).
    - Kết quả này chứng minh tính đúng đắn trong thiết kế thích ứng của TOPOFE: một cấu trúc tô-pô cố định (fixed topology) sẽ dưới mức tối ưu (suboptimal) cho mọi tập dữ liệu, trong khi đồ thị học được sẽ tự thích nghi linh hoạt theo cấu trúc hữu dụng liên họ riêng biệt của từng bài toán.
  - *Quy luật 2: TGSS là chỉ báo dự đoán thực tiễn (predictive indicator) cho mức độ hữu ích của chuyển giao liên họ*:
    - Các tập dữ liệu duy trì TGSS xấp xỉ 0 xuyên suốt quá trình chạy, tiêu biểu là `tic-tac-toe` và `blood` (classification), chính xác là những bài toán mà ưu thế hiệu năng của TOPOFE so với các baseline đơn họ (single-family baselines) ở mức nhỏ nhất.
    - Mối tương quan này xác lập TGSS như một chỉ báo dự đoán hữu ích trong thực tiễn để nhận biết thời điểm chuyển giao liên họ đem lại lợi ích rõ rệt.
    - Ngược lại, các tập như `vehicle` (classification, $\text{TGSS} \approx 0.22$) và `forest-fires` (regression, $\text{TGSS} \approx 0.24$) đạt mức chuyên biệt hóa cao nhất; hoàn toàn tương thích với các tương tác đặc trưng không đồng nhất (heterogeneous feature interactions) trải rộng qua nhiều họ toán tử (operator families), sản sinh tính hữu dụng phân hóa sâu sắc giữa các cặp đảo.
  - *Quy luật 3: Sự bất đối xứng trong động lực học đạt điểm bình nguyên (plateau asymmetry) giữa regression và classification*:
    - Các tập dữ liệu regression thể hiện hành vi chững lại sớm hơn (faster early plateau behavior), với phần lớn đường cong bắt đầu đi ngang sau thế hệ 3–4, trong khi các đường cong classification duy trì đà tăng trưởng liên tục qua thế hệ 10.
    - Sự bất đối xứng này phản ánh tín hiệu độ thích nghi (fitness signals) của bài toán hồi quy mượt mà và ổn định hơn (smoother and more stable), giúp quy tắc cập nhật kiểu bandit (bandit-style update rule) đạt được các ước lượng trọng số tin cậy chỉ sau ít lượt thử nghiệm chuyển giao (fewer transfer trials).
    - Trái lại, các tác vụ classification sở hữu không gian địa hình hữu dụng nhiễu hơn (noisier utility landscapes), đòi hỏi lấy mẫu chuyển giao kéo dài (sustained transfer sampling) để phân giải rõ các khác biệt hữu dụng liên họ; quan sát này gợi mở định hướng lập lịch ngân sách chuyển giao đặc thù theo loại tác vụ (task-type-specific transfer budget scheduling) trong các nghiên cứu tương lai.
