## 4 Experimental Setup

* LLM-FE được đánh giá trên một loạt các tập dữ liệu bảng (tabular datasets), bao gồm các tác vụ phân loại (classification) và hồi quy (regression).
* Phân tích thực nghiệm bao gồm các so sánh định lượng (quantitative comparisons) với các đường cơ sở (baselines) và các nghiên cứu triệt tiêu chi tiết (ablation studies).
* Phương pháp tiếp cận được đánh giá cụ thể bằng cách sử dụng $3$ mô hình dự đoán dạng bảng (tabular predictive models) đã biết với các kiến trúc riêng biệt:
  * XGBoost: một mô hình dựa trên cây (tree-based model) (Chen & Guestrin, 2016).
  * MLP: một mô hình mạng nơ-ron (neural model) (Gorishniy et al., 2021).
  * TabPFN (Hollmann et al., 2023): một mô hình nền tảng dựa trên transformer (transformer-based foundation model) (Vaswani et al., 2017).
* Các kết quả làm nổi bật khả năng của LLM-FE trong việc sinh ra các đặc trưng hiệu quả, giúp cải thiện một cách nhất quán hiệu năng của nhiều mô hình dự đoán khác nhau trên các tập dữ liệu.
