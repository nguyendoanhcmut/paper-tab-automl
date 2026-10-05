### 4.1 Baselines

- **Tập hợp các phương pháp đối chuẩn (baselines) được đưa vào so sánh**:
  - LLM-FE được đánh giá so sánh trực tiếp với các phương pháp feature engineering (kỹ thuật đặc trưng) tiên tiến nhất (state-of-the-art).
  - Nhóm phương pháp truyền thống: Bao gồm OpenFE (Zhang et al., 2023) và AutoFeat (Horn et al., 2020).
  - Nhóm phương pháp dựa trên LLM (LLM-based methods): Bao gồm CAAFE (Hollmann et al., 2024), FeatLLM (Han et al., 2024), và OCTree (Nam et al., 2024).
- **Cấu hình mô hình dự đoán và mô hình ngôn ngữ lớn nền tảng mặc định**:
  - **Mô hình dự đoán dữ liệu dạng bảng mặc định (default tabular data prediction model)**: XGBoost được lựa chọn làm mô hình dự đoán mặc định cho toàn bộ các thử nghiệm so sánh với các baselines.
  - **LLM backbone (mô hình ngôn ngữ lớn nền tảng) mặc định**: GPT-3.5-Turbo được sử dụng làm mô hình nền tảng mặc định cho tất cả các phương pháp tiếp cận dựa trên LLM (Tables 2 và 3).
- **Thiết lập giao thức thực nghiệm đảm bảo tính công bằng (fair comparison)**:
  - **Ngân sách lấy mẫu cố định (fixed budget)**: Mọi phương pháp tiếp cận dựa trên LLM đều vận hành dưới một ngân sách giới hạn cố định là 20 LLM samples (mẫu sinh LLM).
  - **Không áp dụng điều kiện dừng**: Quá trình tìm kiếm không sử dụng early stopping (dừng sớm) hay bất kỳ convergence criterion (tiêu chí hội tụ) nào.
  - **Tiêu chuẩn kết quả báo cáo cuối cùng**: Điểm số được công bố đại diện cho best-scoring program (chương trình đạt điểm số cao nhất) được khám phá trong phạm vi ngân sách 20 mẫu này.
- **Tài liệu tham khảo chi tiết triển khai**: Appendix B.2 cung cấp thêm các chi tiết triển khai bổ sung (additional implementation details).
