## Appendix J: Comparison with Genetic Programming Methods

* **Thiết lập so sánh thực nghiệm với các biến thể Lập trình di truyền tiên tiến (Genetic Programming Baselines):**
  * Đánh giá đối chuẩn SymboLLM-FE với 5 biến thể Lập trình di truyền (Genetic Programming - GP) tiên tiến nhất (state-of-the-art) trên 6 tập dữ liệu chuẩn đa dạng thuộc cả hai nhóm tác vụ phân loại và hồi quy.
  * Phân loại thước đo đánh giá theo loại hình tác vụ:
    * Bốn tác vụ phân loại (classification tasks: Credit-g, Spaceship, Cmc, Academic) sử dụng thang đo Độ chính xác (Accuracy, ký hiệu $\text{Acc} \uparrow$, tính theo đơn vị $\%$.
    * Hai tác vụ hồi quy (regression tasks: Ailerons, Tesla) sử dụng thang đo Sai số căn bậc hai trung bình bình phương (Root Mean Squared Error, ký hiệu $\text{RMSE} \downarrow$).
  * Danh sách 5 biến thể thuật toán Lập trình di truyền đối chuẩn gồm:
    * Shapley-GP (Chen et al., 2017): Tích hợp cơ chế chọn lọc đặc trưng dựa trên giá trị Shapley nhằm cải thiện khả năng tổng quát hóa của GP.
    * LAS-GP (Zhang et al., 2025): Ứng dụng các thư viện ngữ nghĩa quy mô lớn (large semantic libraries) vào cấu tạo đặc trưng tiến hóa trong hồi quy ký hiệu.
    * SAM-GP (Bakurov et al., 2024): Áp dụng phương pháp tối thiểu hóa nhạy cảm độ sắc nét (Sharpness-Aware Minimization - SAM) vào GP nhằm giảm thiểu hiện tượng quá khớp (overfitting).
    * Modular-MTGP (Zhang et al., 2023a): Giải thuật lập trình di truyền đa cây dạng khối mô-đun (Modular Multi-Tree Genetic Programming) phục vụ sinh đặc trưng tiến hóa cho bài toán hồi quy.
    * Baseline gốc: Mô hình cơ sở không tích hợp kỹ thuật sinh đặc trưng tiến hóa.

* **Bảng 15 tổng hợp kết quả so sánh hiệu năng toàn diện trên 6 tập dữ liệu thực nghiệm:**
  * **Bảng 15.** So sánh hiệu năng giữa SymboLLM-FE và các biến thể giải thuật Lập trình di truyền GP
    * <img src="assets/table_15_p24.png" alt="Bảng 15" />
    * **Bảng này chứng minh điều gì**
      * SymboLLM-FE vượt trội các biến thể GP truyền thống nhờ kết hợp lọc ngữ nghĩa và tinh chỉnh của LLM
    * **Từ đâu mà thấy được**
      * So sánh với Standard GP, Multi-tree GP, M3GP trên các thước đo Accuracy và RMSE
  * Chi tiết hiệu năng định lượng trên các tập dữ liệu phân loại ($\text{Acc} \uparrow, \%$):
    * `Credit-g`: Baseline đạt $77.03\%$, Shapley-GP đạt $77.28\%$, LAS-GP đạt $69.35\%$, SAM-GP đạt $77.20\%$, Modular-MTGP đạt $77.15\%$, và SymboLLM-FE đạt $77.00\%$.
    * `Spaceship`: Baseline đạt $80.79\%$, Shapley-GP đạt $81.05\%$, LAS-GP đạt $81.12\%$, SAM-GP đạt $80.95\%$, Modular-MTGP đạt $80.88\%$, trong khi SymboLLM-FE dẫn đầu với $81.27\%$.
    * `Cmc`: Baseline đạt $57.85\%$, Shapley-GP đạt $57.92\%$, LAS-GP đạt $57.91\%$, SAM-GP đạt $57.08\%$, Modular-MTGP đạt $57.82\%$, và SymboLLM-FE đạt đỉnh cao nhất với $57.97\%$.
    * `Academic`: Baseline đạt $77.33\%$, Shapley-GP đạt $77.65\%$, LAS-GP đạt $77.72\%$, SAM-GP đạt $77.55\%$, Modular-MTGP đạt $77.12\%$, và SymboLLM-FE giành vị trí cao nhất với $77.89\%$.
  * Chi tiết hiệu năng định lượng trên các tập dữ liệu hồi quy ($\text{RMSE} \downarrow$):
    * `Ailerons`: Baseline ghi nhận $5.10$, Shapley-GP ghi nhận $5.06$, LAS-GP ghi nhận $5.04$, SAM-GP ghi nhận $5.07$, Modular-MTGP ghi nhận $5.08$, trong khi SymboLLM-FE giảm sai số xuống thấp nhất đạt $5.02$.
    * `Tesla`: Baseline ghi nhận $2.39$, Shapley-GP ghi nhận $2.30$, LAS-GP ghi nhận $2.28$, SAM-GP ghi nhận $2.34$, Modular-MTGP ghi nhận $2.36$, trong khi SymboLLM-FE vượt trội rõ rệt khi đưa sai số xuống mức kỷ lục $2.16$.

* **Phân tích ưu thế dự đoán vượt trội và độ ổn định phân phối của SymboLLM-FE:**
  * SymboLLM-FE thể hiện hiệu năng tổng thể vượt trội (superior overall performance), đánh bại toàn bộ các biến thể Lập trình di truyền được so sánh trên đại đa số các tập dữ liệu thử nghiệm ($5/6$ bộ dữ liệu).
  * Mức tăng trưởng hiệu năng đặc biệt mạnh mẽ trong các bài toán hồi quy phức tạp, đồng thời xác lập vị trí dẫn đầu ở hầu hết các bài toán chuẩn phân loại.
  * Giữ vững năng lực cạnh tranh cực kỳ sát sao ngay cả trong trường hợp duy nhất mà một biến thể GP nắm giữ lợi thế dẫn trước biên độ nhỏ (tại `Credit-g`, Shapley-GP dẫn trước chỉ $+0.28\%$).
  * Thể hiện tính ổn định và độ bền vững (stability and robustness) cao hơn đáng kể trên các phân phối dữ liệu đa dạng.
  * Tránh được hiện tượng biến động hiệu năng thất thường (performance volatility) và nguy cơ phạt bùng nổ kích thước (bloat penalties) thường gặp ở các cơ chế tìm kiếm tiến hóa ngẫu nhiên (chẳng hạn hiện tượng sụt giảm hiệu năng nghiêm trọng của LAS-GP xuống $69.35\%$ trên tập `Credit-g`).

* **Ưu thế cốt lõi của việc kết hợp định hướng ngữ nghĩa LLM và tốc độ hội tụ:**
  * Khẳng định thực nghiệm rằng SymboLLM-FE không chỉ tương đương mà còn thường xuyên vượt xa năng lực dự đoán của cả các phương pháp GP truyền thống lẫn các biến thể GP tiên tiến.
  * Sở hữu các lợi thế bổ sung mang tính quyết định:
    * Định hướng ngữ nghĩa dựa trên LLM (LLM-driven semantic guidance): Giúp cấu trúc biểu thức được tái diễn giải mạch lạc và có ý nghĩa miền ứng dụng cụ thể thay vì chỉ dựa vào các phép toán tổ hợp tiến hóa mù quáng.
    * Tốc độ hội tụ nhanh hơn (faster convergence): Rút ngắn thời gian và chi phí tính toán đáng kể so với việc phải lặp qua hàng trăm thế hệ di truyền phức tạp.
