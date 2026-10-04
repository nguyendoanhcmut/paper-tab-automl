### 2.6. Interpretability analysis through multi-model SHAP

- Phân tích SHAP (SHapley Additive exPlanations) được áp dụng trên toàn bộ $16$ mô hình và $3$ biến mục tiêu (targets), thiết lập $48$ hồ sơ khả năng diễn giải (interpretability profiles):
  - Khung phân tích đa mô hình (multi-model framework) làm sáng tỏ liệu các thuật toán khác nhau có đạt được sự đồng thuận về độ quan trọng của đặc trưng (feature importance) hay không.
  - Phân tích đa mô hình giúp phát hiện sai lệch phụ thuộc mô hình (model-dependent bias) mà các phân tích đơn mô hình (single-model analyses) không thể nhận diện được.
- Phân bổ thuật toán SHAP theo kiến trúc mô hình và các dạng đồ thị trực quan hóa:
  - TreeSHAP được áp dụng cho $9$ mô hình dựa trên cây (tree-based models).
  - KernelSHAP được áp dụng cho $7$ mô hình không dựa trên cây (non-tree models).
  - Biểu đồ bầy ong (beeswarm plots), giá trị SHAP tuyệt đối trung bình (mean absolute SHAP values) và biểu đồ phụ thuộc (dependence plots) được khởi tạo cho từng tổ hợp mô hình – mục tiêu (model–target combination).
- Bản chất thống kê của giá trị SHAP và giới hạn diễn giải cơ chế:
  - Do SHAP định lượng phần đóng góp của từng đặc trưng vào đầu ra dự báo của mô hình, giá trị này phản ánh mối liên hệ thống kê (association) bên trong phân phối dữ liệu huấn luyện (training distribution), chứ không phải quan hệ nhân quả vật lý đã được kiểm chứng (verified physical causation).
  - Các diễn giải cơ chế (mechanistic explanations) đưa ra tại Mục 3.2 là những diễn giải hợp lý về mặt vật lý (physically plausible) và nhất quán với y văn khoa học (literature-consistent interpretations), không phải các cơ chế đã được thực nghiệm chứng minh (demonstrated mechanisms).
