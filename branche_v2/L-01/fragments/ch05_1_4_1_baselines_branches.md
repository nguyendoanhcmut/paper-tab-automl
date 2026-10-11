### 4.1 Baselines

* LLM-FE được đánh giá so sánh với các phương pháp tiếp cận feature engineering (kỹ thuật đặc trưng) tiên tiến (state-of-the-art):
  * Các phương pháp truyền thống bao gồm OpenFE (Zhang et al., $2023$) và AutoFeat (Horn et al., $2020$).
  * Các phương pháp dựa trên mô hình ngôn ngữ lớn (LLM-based methods) bao gồm CAAFE (Hollmann et al., $2024$), FeatLLM (Han et al., $2024$), và OCTree (Nam et al., $2024$).
* Cấu hình mặc định cho các mô hình dự đoán và mô hình nền tảng trong thực nghiệm so sánh:
  * XGBoost được sử dụng làm mô hình dự đoán dữ liệu dạng bảng mặc định (default tabular data prediction model) khi so sánh với các phương pháp đối chuẩn (baselines).
  * GPT-3.5-Turbo được sử dụng làm mô hình nền tảng LLM mặc định (default LLM backbone) cho tất cả các phương pháp tiếp cận dựa trên LLM (Bảng $2$ và Bảng $3$ / Tables $2$ and $3$).
* Thiết lập ngân sách nhằm đảm bảo tính so sánh công bằng (fair comparison):
  * Tất cả các phương pháp tiếp cận dựa trên LLM hoạt động dưới một ngân sách cố định gồm $20$ mẫu LLM ($20$ LLM samples), không áp dụng cơ chế dừng sớm (early stopping) hay tiêu chí hội tụ (convergence criterion).
  * Kết quả được báo cáo cuối cùng tương ứng với chương trình đạt điểm cao nhất (best-scoring program) được khám phá trong phạm vi ngân sách $20$ mẫu này.
* Các chi tiết cài đặt và triển khai bổ sung được trình bày tại Phụ lục B.2 (Appendix B.2).
