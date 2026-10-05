### 2.4 Hyperparameter optimization

- Tối ưu hóa siêu tham số mô hình Rừng ngẫu nhiên ($\text{RF}$) qua tìm kiếm lưới kết hợp kiểm định chéo
  - Cấu hình siêu tham số tối ưu được xác lập chặt chẽ:
    - Số lượng cây quyết định: `n_estimators = 500`.
    - Số mẫu tối thiểu để phân tách một nút: `min_samples_split = 2`.
    - Số mẫu tối thiểu tại một nút lá: `min_samples_leaf = 1`.
    - Số lượng đặc trưng tối đa khi phân nhánh: `max_features = 'log2'`.
    - Độ sâu tối đa của cây: `max_depth = None` (phát triển tự nhiên đến khi các lá thuần nhất).
    - Hạt giống ngẫu nhiên: `random_state = 42` và sử dụng toàn bộ tài nguyên luồng tính toán: `n_jobs = -1`.
- Quy trình điều chỉnh siêu tham số cho mạng nơ-ron sâu ($\text{DNN}$)
  - Thực hiện thử nghiệm đa dạng các tổ hợp số lượng nơ-ron trong các lớp ẩn và tỷ lệ ngắt kết nối (`dropout rate`).
  - Huấn luyện mô hình qua nhiều chu kỳ (epochs) bằng thuật toán hạ gradient theo lô (batch gradient descent).
  - Lựa chọn cấu trúc tối ưu dựa trên hàm mất mát kiểm định (validation loss) nhằm đảm bảo sự so sánh công bằng giữa hai phương pháp tiếp cận.
