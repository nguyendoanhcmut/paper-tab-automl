## 4 Experimental Setup

- **Phạm vi và mục tiêu đánh giá thực nghiệm (Scope and Objectives of Experimental Evaluation)**:
  - LLM-FE được đánh giá trên một dải rộng các tập dữ liệu dạng bảng (tabular datasets), bao quát cả tác vụ phân loại (classification tasks) lẫn tác vụ hồi quy (regression tasks).
  - Khung phân tích thực nghiệm bao gồm:
    - Các phép so sánh định lượng (quantitative comparisons) đối chiếu với các phương pháp đối chuẩn (baselines).
    - Các nghiên cứu cắt bỏ chi tiết (detailed ablation studies) nhằm thẩm định đóng góp của từng thành phần trong phương pháp.

- **Các mô hình dự đoán dữ liệu bảng đại diện cho các họ kiến trúc khác biệt (Tabular Predictive Models Evaluated)**:
  - Phương pháp tiếp cận được thẩm định trên 3 mô hình dự đoán dữ liệu bảng tiêu biểu với các cấu trúc kiến trúc hoàn toàn riêng biệt:
    - **(1) XGBoost**: Mô hình dựa trên cấu trúc cây (tree-based model) (Chen & Guestrin, 2016).
    - **(2) MLP**: Mô hình mạng nơ-ron (neural model) (Gorishniy et al., 2021).
    - **(3) TabPFN**: Mô hình nền tảng dựa trên kiến trúc transformer (transformer-based foundation model) (Hollmann et al., 2023; Vaswani et al., 2017).

- **Hiệu quả tổng quan của các đặc trưng do LLM-FE sinh ra**:
  - Các kết quả thực nghiệm làm nổi bật năng lực của LLM-FE trong việc tự động kiến tạo các đặc trưng hiệu quả (effective features).
  - Các đặc trưng mới này cải thiện một cách nhất quán hiệu năng dự đoán trên nhiều họ mô hình và tập dữ liệu khác nhau.
