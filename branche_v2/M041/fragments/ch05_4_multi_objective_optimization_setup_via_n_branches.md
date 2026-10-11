### Multi-objective optimization setup via NSGA-II

* **Mục tiêu và nguyên lý của giải thuật di truyền sắp xếp không bị chi phối II (Non-dominated Sorting Genetic Algorithm II - NSGA-II)**:
    * **Mục đích tối ưu hóa**: Xác định các điều kiện vận hành tối ưu nhằm đồng thời cực đại hóa hiệu quả loại bỏ các chất dinh dưỡng (nutrient removal) trong hệ thống MBR.
    * **Đặc tính đa mục tiêu (Multi-objective optimization)**: Khác với phương pháp tối ưu hóa đơn mục tiêu (single-objective optimization) chỉ tìm một nghiệm cực trị cục bộ hoặc toàn cục, NSGA-II tạo ra một tập hợp các giải pháp tối ưu được gọi là mặt trước Pareto (Pareto Front).
    * **Bản chất của mặt trước Pareto (Pareto Front)**: Đại diện cho sự thỏa hiệp tối ưu nhất (best trade-offs) giữa các mục tiêu xung đột nhau (conflicting objectives), khi việc cải thiện một mục tiêu bắt buộc phải đánh đổi bằng sự suy giảm của mục tiêu còn lại.
    * **Cơ chế hoạt động cốt lõi của NSGA-II**:
        * **Sắp xếp không bị chi phối (Non-dominated sorting)**: Phân tầng các cá thể trong quần thể thành các bậc Pareto (Pareto fronts/ranks) dựa trên quan hệ chi phối; một giải pháp được coi là không bị chi phối nếu không có giải pháp nào khác tốt hơn nó ở tất cả các mục tiêu.
        * **Khoảng cách tập trung (Crowding distance)**: Ước lượng mật độ xung quanh từng giải pháp trên biên Pareto nhằm duy trì tính đa dạng sinh học (diversity preservation) của quần thể mà không cần tham số chia sẻ (niching/sharing parameter) định lượng trước.
        * **Bảo toàn độ ưu tú (Elitism)**: Ghép đôi quần thể cha mẹ và con cái ($2N$) trước khi chọn lọc, đảm bảo các cá thể xuất sắc nhất qua các thế hệ không bị mất đi.
* **Thiết lập bài toán tối ưu hóa (Problem Formulation)**:
    * Bài toán tối ưu hóa được xây dựng gồm $3$ biến quyết định (decision variables) và $2$ hàm mục tiêu (objective functions).
    * **Biến quyết định (Decision Variables)**: Không gian tìm kiếm (search space) bị giới hạn nghiêm ngặt bởi các biên của thiết kế thực nghiệm (experimental design boundaries):
        * Thời gian vận hành (Time): $0 \le \text{Time} \le 20$ (ngày / days).
        * Độ $\text{pH}$: $6 \le \text{pH} \le 9$.
        * Tổng cacbon hữu cơ (Total Organic Carbon - TOC): $40 \le \text{TOC} \le 120$ (mg/L).
    * **Hàm mục tiêu và hàm thích nghi (Objective / Fitness Functions)**: Các phương trình hồi quy đa thức (regression equations) thu được từ mô hình phương pháp bề mặt đáp ứng (Response Surface Methodology - RSM) được sử dụng trực tiếp làm các hàm thích nghi:
        * **Mục tiêu 1 (Objective 1)**: Cực đại hóa hiệu suất loại bỏ nitơ amoniac (Ammonia Nitrogen Removal Efficiency, $\%$), sử dụng các phương trình hồi quy RSM (Eqs. 2 và 6).
        * **Mục tiêu 2 (Objective 2)**: Cực đại hóa hiệu suất loại bỏ phosphat (Phosphate Removal Efficiency, $\%$), sử dụng các phương trình hồi quy RSM (Eqs. 4 và 8).
* **Cấu hình tham số thuật toán (Algorithm Parameters)**:
    * Các thông số vận hành của thuật toán NSGA-II được thiết lập nhằm đảm bảo khả năng hội tụ bền vững và chính xác (robust convergence):
        * **Quy mô quần thể (Population Size)**: $100$ cá thể.
        * **Số thế hệ tối đa (Maximum Generations)**: $200$ thế hệ.
        * **Xác suất lai ghép (Crossover Probability)**: $0.9$ ($90\%$).
        * **Xác suất đột biến (Mutation Probability)**: $0.1$ ($10\%$).
        * **Toán tử chọn lọc (Selection Operator)**: Chọn lọc giải đấu (Tournament Selection), cho phép chọn cá thể tốt hơn dựa trên bậc Pareto và khoảng cách tập trung.
* **Khả năng ứng dụng và hỗ trợ ra quyết định (Decision-making implications)**:
    * Tập nghiệm tối ưu Pareto (Pareto optimal set) cung cấp cho các nhà quản lý và kỹ sư vận hành một dải rộng các điều kiện vận hành khả thi.
    * Cho phép tính linh hoạt cao trong việc điều chỉnh chế độ công nghệ tùy theo yêu cầu cụ thể của từng kịch bản nước thải (wastewater scenario)—ưu tiên xử lý triệt để nitơ amoniac hay phosphat tùy thuộc vào quy chuẩn xả thải tại địa phương.
