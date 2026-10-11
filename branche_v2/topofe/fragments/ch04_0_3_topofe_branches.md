## 3 TOPOFE

- **Thách thức tìm kiếm chương trình tổ hợp (Combinatorial Program Search)**:
  - Dựa trên các tiền đề được thiết lập tại § 2.2, không gian tìm kiếm chương trình tổ hợp $\mathcal{P}$ là bất khả thi đối với các phương pháp duyệt vét cạn (enumeration) và không thể tiếp cận bằng các phương pháp dựa trên đạo hàm/gradient (gradient-based methods).
  - Quá trình này đòi hỏi một cơ chế đề xuất được dẫn đường bởi mô hình ngôn ngữ lớn (LLM-guided proposal mechanism) thỏa mãn đồng thời ba điều kiện cốt lõi:
    1. *Sinh chương trình hợp lệ và có ý nghĩa ngữ nghĩa*: Khả năng tạo ra các chương trình biến đổi hợp lệ về mặt cú pháp và có ý nghĩa về mặt ngữ nghĩa trên không gian toán tử không đồng nhất (heterogeneous operator space) mà không cần vét cạn toàn bộ không gian.
    2. *Khai thác tri thức miền đặc thù*: Tận dụng tri thức miền trong siêu dữ liệu $\mathcal{M}$ (task-specific domain knowledge) để tạo thiên kiến tìm kiếm hướng tới các biến đổi khả thi và đầy triển vọng (promising and admissible transformations).
    3. *Hỗ trợ đa dạng chế độ đề xuất qua giao diện thống nhất*: Cung cấp một giao diện hợp nhất hỗ trợ nhiều chế độ đề xuất khác nhau, cho phép song hành giữa việc khai thác sâu (exploitation) các chương trình chất lượng cao đã biết và thăm dò mở rộng (exploration) các vùng không gian chưa được khám phá trong $\mathcal{P}$.
- **Kiến trúc tổng thể TOPOFE (Topology-Aware Program Optimization for Feature Engineering)**:
  - TOPOFE tổ chức quy trình tìm kiếm chương trình cho AutoFE dưới sự dẫn dắt của LLM thông qua ba thành phần phối hợp chặt chẽ:
    1. *Phân rã đa đảo (Multi-island decomposition)* (§3.1): Phân chia không gian chương trình $\mathcal{P}$ thành $M$ họ biến đổi mạch lạc về ngữ nghĩa (semantically coherent transformation families), mỗi họ được khám phá bởi một đảo chuyên trách nhằm ngăn chặn hiện tượng hội tụ sớm vào một họ duy nhất (premature convergence).
    2. *Bộ nhớ thích ứng Prompt (Prompt Adaptation Memory)* (§3.2): Duy trì trạng thái tìm kiếm cục bộ cho từng đảo để liên tục điều chỉnh các prompt đề xuất của LLM dựa trên lịch sử chấp nhận/từ chối (accept/reject history) đã tích lũy mà không cần cập nhật bất kỳ trọng số tham số nào.
    3. *Cơ chế chuyển giao liên đảo nhận biết cấu trúc liên kết (Topology-aware cross-island transfer)* (§3.3): Điều phối luồng tri thức giữa các đảo thông qua một đồ thị có hướng được học (learned directed graph), kích hoạt quá trình tổng hợp lai (hybrid synthesis) từ các họ bổ trợ khi tìm kiếm cục bộ chạm ngưỡng bão hòa.
  - Sự kết hợp của ba thành phần này thiết lập trạng thái cân bằng giữa khai thác chuyên sâu trong từng họ biến đổi và thăm dò có cấu trúc trên toàn bộ không gian biến đổi; toàn bộ quy trình được khái quát trong Hình 1 và tóm tắt chi tiết trong Thuật toán 1 (Algorithm 1).
  - **Hình 1.** Tổng quan kiến trúc hệ thống TOPOFE (Overview of TOPOFE).
    - <img src="assets/fig_01_p4.png" alt="Hình 1" />
    - **Hình này chứng minh điều gì**
      - TOPOFE phân rã không gian AutoFE thành các đảo họ biến đổi, kết hợp tiến hóa cục bộ dẫn dắt bởi LLM, phát hiện bão hòa thích ứng, tổng hợp liên đảo dựa trên cấu trúc liên kết và chọn lọc lưu trữ để nâng cao hiệu năng dự đoán tabular.
    - **Từ đâu mà thấy được**
      - Sơ đồ tương tác liên hoàn: Dữ liệu bảng + Prompts phân chia vào 5 đảo (Arithmetic, Aggregate, Temporal, Relational, Non-linear); vòng lặp Intra-Island Evolution (Population, LLM Variation, Eval, Selection); khối Saturation Detection với điểm $Sat_i$; khối Prompt Adaptation Memory (Prefer/Avoid, Global Archival); và khối Topology-learning & Transfer kết nối đường ống Downstream Evaluation (XGBoost, TabPFN, CatBoost).
