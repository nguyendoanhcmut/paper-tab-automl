### 4.4 Results and Discussion

- **Hiệu năng vượt trội trên các tập dữ liệu phân loại (Classification Datasets - Table 2)**:
  - **Quy mô thực nghiệm**: LLM-FE được so sánh toàn diện với nhiều phương pháp feature engineering (kỹ thuật đặc trưng) đối chuẩn (baselines) trên $19$ classification datasets (tập dữ liệu phân loại).
  - **Cải thiện nhất quán so với mô hình cơ sở**: Kết quả thực nghiệm chứng minh LLM-FE liên tục cải thiện hiệu năng dự đoán (predictive performance) so với base model (mô hình cơ sở) sử dụng raw data (dữ liệu thô).
  - **Thứ hạng trung bình tối ưu với chi phí thấp**: LLM-FE đạt mean rank (thứ hạng trung bình) thấp nhất ($1.42$, đại diện cho hiệu năng tốt nhất so với Base $3.95$, AutoFeat $5.11$, OpenFE $3.63$, CAAFE $3.47$, FeatLLM $5.11$, OCTree $4.05$) với computational cost (chi phí tính toán) thấp hơn (chi tiết tại Section 5.1), khẳng định tính hiệu quả vượt trội trong việc thúc đẩy khám phá đặc trưng (feature discovery) so với các baselines dẫn đầu khác.

- **Hiệu năng vượt trội trên các tập dữ liệu hồi quy (Regression Datasets - Table 3)**:
  - **Mở rộng thực nghiệm sang bài toán hồi quy**: Để đánh giá sâu hơn hiệu quả của LLM-FE, các thực nghiệm được tiến hành trên $10$ regression datasets (tập dữ liệu hồi quy) với cùng các evaluation settings (thiết lập đánh giá) được áp dụng cho các tập dữ liệu phân loại.
  - **Giới hạn phạm vi so sánh đối chuẩn**: Do thiếu phần triển khai cho dữ liệu hồi quy trong các kho mã nguồn hiện có của các baseline dựa trên LLM (LLM-based baselines gồm CAAFE và FeatLLM), phạm vi so sánh trong Table 3 được giới hạn ở các phương pháp phi LLM (non-LLM methods gồm OpenFE & AutoFeat), base LLM (mô hình ngôn ngữ lớn cơ sở), và OCTree — những phương pháp đã được kiểm chứng trước đó trên các tác vụ hồi quy.
  - **Kết quả dẫn đầu vượt bậc**: LLM-FE vượt trội hơn toàn bộ các phương pháp đối chuẩn, đạt mean rank thấp nhất ($1.10$, so với OpenFE $2.80$, OCTree $3.70$, base LLM $4.40$, AutoFeat $4.45$, Base $4.55$) và thể hiện sự cải thiện nhất quán trên toàn bộ tất cả các tập dữ liệu.

- **Các phân tích thực nghiệm mở rộng và kiểm định thống kê (Appendix D)**:
  - **Kiểm định ý nghĩa thống kê**: Bổ sung Wilcoxon signed-rank tests (kiểm định hạng có dấu Wilcoxon) nhằm chứng minh ý nghĩa thống kê của mức độ cải thiện hiệu năng.
  - **Tác động của tối ưu hóa siêu tham số**: Phân tích ảnh hưởng của hyperparameter optimization (tối ưu hóa siêu tham số - HPO) đối với LLM-FE.
  - **Đánh giá trên các mô hình dự đoán thay thế**: Kiểm thử mở rộng với các mô hình dự đoán khác như CatBoost và Logistic Regression.

- **Khả năng chuyển giao và tính tổng quát hóa (Transferability and Generalizability)**:
  - **Khảo sát trên nhiều mô hình nền tảng**: Nghiên cứu sâu hơn về tính chuyển giao (transferability) và khả năng tổng quát hóa (generalizability) của các đặc trưng được khám phá qua nhiều LLM backbones (mô hình ngôn ngữ lớn nền tảng) khác nhau.
  - **Độ bền vững kiến trúc**: Kết quả khẳng định LLM-FE duy trì tính bền vững (robust) và hiệu quả cao dưới các cơ chế mô hình hóa và kiến trúc đa dạng.
