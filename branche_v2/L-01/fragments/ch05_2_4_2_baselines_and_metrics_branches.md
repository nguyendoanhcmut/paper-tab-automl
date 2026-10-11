### 4.2 Baselines and Metrics

* Lựa chọn tập dữ liệu theo quy trình của Hollmann et al. ($2024$) từ các nghiên cứu kỹ thuật đặc trưng (feature engineering) trước đó, bao gồm Han et al. ($2024$), Hollmann et al. ($2024$), và Zhang et al. ($2023$).
    * Tiêu chí lựa chọn: Các tập dữ liệu bắt buộc phải đi kèm thông tin mô tả đặc trưng (descriptive feature information).
* Cấu trúc và quy mô tập dữ liệu phân tích thực nghiệm:
    * Tập dữ liệu phân tích ban đầu bao gồm $19$ tập dữ liệu phân loại (classification datasets) và $10$ tập dữ liệu hồi quy (regression datasets).
    * Đặc tính thuộc tính: Tất cả các tập dữ liệu đều chứa hỗn hợp các đặc trưng dạng phân loại (categorical features) và dạng số (numerical features).
    * Tập dữ liệu mở rộng: Bổ sung thêm $8$ tập dữ liệu phân loại quy mô lớn, số chiều cao (large-scale, high-dimensional classification datasets) để bảo đảm việc đánh giá toàn diện (comprehensive evaluation).
* Nguồn gốc thu thập dữ liệu từ các kho lưu trữ học máy (machine learning repositories) đã được kiểm chứng:
    * OpenML (Vanschoren et al., $2014$; Feurer et al., $2021$).
    * UCI Machine Learning Repository (Asuncion et al., $2007$).
    * Kaggle.
* Kiểm định khả năng phòng ngừa rò rỉ dữ liệu (data leakage) sau mốc huấn luyện của mô hình nền tảng:
    * Thực nghiệm trên $5$ tập dữ liệu phân loại từ Hollmann et al. ($2024$) và Bordt et al. ($2024$).
    * Các tập dữ liệu này đều được phát hành sau thời điểm giới hạn dữ liệu huấn luyện (training cutoff date) của GPT vào tháng $9$ năm $2021$ (September $2021$).
* Siêu dữ liệu (metadata) đi kèm với mỗi tập dữ liệu:
    * Bản mô tả bằng ngôn ngữ tự nhiên về tác vụ dự đoán (natural-language description of the prediction task).
    * Tên các đặc trưng mang tính mô tả rõ ràng (descriptive feature names).
* Giao thức phân chia dữ liệu và quy trình đánh giá thực nghiệm (data partitioning and evaluation protocol):
    * Phân chia tập dữ liệu: Mỗi tập dữ liệu được phân chia thành tập huấn luyện (train set) và tập kiểm thử (test set) theo tỷ lệ $80$-$20$ ($80$-$20$ split).
    * Quy trình đánh giá lặp lại: Theo Hollmann et al. ($2024$), tất cả các phương pháp đều được đánh giá qua $5$ lần lặp (iterations).
    * Đảm bảo tính ngẫu nhiên: Mỗi lần lặp sử dụng một hạt ngẫu nhiên phân biệt (distinct random seed) cùng các tập phân chia train-test khác nhau.
    * Thông tin chi tiết về từng tập dữ liệu được trình bày tại Phụ lục C (Appendix C).
