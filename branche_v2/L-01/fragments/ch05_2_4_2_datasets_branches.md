### 4.2 Datasets

* Các bộ dữ liệu được lựa chọn theo Hollmann et al. ($2024$) từ các công trình feature engineering (kỹ thuật đặc trưng) trước đây, bao gồm Han et al. ($2024$), Hollmann et al. ($2024$), và Zhang et al. ($2023$), có chứa thông tin mô tả đặc trưng (descriptive feature information).
* Tập dữ liệu phân tích bao gồm $19$ bộ dữ liệu phân loại (classification) và $10$ bộ dữ liệu hồi quy (regression), mỗi bộ đều chứa các đặc trưng hỗn hợp dạng phân loại (categorical) và dạng số (numerical).
    * Nghiên cứu bổ sung $8$ bộ dữ liệu phân loại quy mô lớn, số chiều cao (large-scale, high-dimensional classification datasets) nhằm đảm bảo việc đánh giá toàn diện.
    * Nguồn thu thập dữ liệu đến từ các kho lưu trữ machine learning uy tín, bao gồm OpenML (Vanschoren et al., $2014$; Feurer et al., $2021$), UCI Machine Learning Repository (Asuncion et al., $2007$), và Kaggle.
* Thử nghiệm được tiến hành trên $5$ bộ dữ liệu phân loại từ Hollmann et al. ($2024$) và Bordt et al. ($2024$) được phát hành sau mốc thời gian cắt dữ liệu huấn luyện của GPT vào tháng $9$ năm $2021$ (September $2021$ GPT training cutoff date).
* Mỗi bộ dữ liệu đi kèm với metadata (siêu dữ liệu), bao gồm mô tả bằng ngôn ngữ tự nhiên về tác vụ dự đoán và tên các đặc trưng mang tính mô tả (descriptive feature names).
* Quy trình phân chia và đánh giá dữ liệu:
    * Mỗi bộ dữ liệu được phân chia thành tập huấn luyện (train set) và tập kiểm thử (test set) theo tỷ lệ $80$-$20$ ($80$-$20$ split).
    * Theo Hollmann et al. ($2024$), tất cả các phương pháp được đánh giá qua $5$ lần lặp (iterations), mỗi lần sử dụng một random seed (hạt ngẫu nhiên) và các phân chia train-test riêng biệt.
    * Chi tiết cụ thể được trình bày tại Appendix C.
