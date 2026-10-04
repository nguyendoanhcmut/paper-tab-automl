#### 2.2.3. Data preprocessing

- Quy trình làm sạch loại bỏ các mục dữ liệu không hoàn chỉnh từ chuỗi quan trắc dài hạn của hệ thống MBR kép (dual MBRs):
  - Tổng số dữ liệu thu thập ban đầu gồm $128$ bộ dữ liệu (datasets) trong thời gian $235$ ngày vận hành.
  - Loại bỏ $8$ mục dữ liệu không hoàn chỉnh (incomplete entries), giữ lại $120$ nhóm dữ liệu hợp lệ cho các phân tích tiếp theo.
- Bổ sung giá thể sinh học (biocarriers) trong Giai đoạn 3 (Phase 3) làm thay đổi tương quan thông số và tạo cơ sở kiểm thử liên kịch bản:
  - Giá thể sinh học được bổ sung vào một bể phản ứng trong Phase 3 để thúc đẩy quá trình khử nitrat (denitrification) (Fig. 1), dẫn đến sự biến đổi trong mối quan hệ giữa các thông số (parameter relationships).
  - Thiết lập tập kiểm tra độc lập (independent test group) gồm $23$ nhóm dữ liệu thu thập từ Phase 3 (có bổ sung giá thể) nhằm đánh giá khả năng áp dụng liên kịch bản (cross-scenario applicability).
  - Tập dữ liệu gồm $97$ nhóm không bổ sung giá thể (no-biocarrier data groups, chỉ chứa bùn hoạt tính / activated sludge only) được sử dụng để huấn luyện (training), xác thực (validation) và kiểm tra (testing) mô hình dự đoán trạng thái nitrat hóa (nitrification).
  - Cách tiếp cận này cho phép đánh giá năng lực dự đoán của mô hình khi chuyển đổi sang các điều kiện vận hành bị thay đổi (altered operational conditions).
- Điểm ngoại lai (outliers) được chủ động giữ lại nhằm kiểm tra độ bền vững của mô hình:
  - Hệ thống xử lý nước xám tại chỗ (onsite greywater systems) có đặc tính biến thiên tự nhiên cao ở dòng vào (inherent influent variability).
  - Giữ lại các giá trị ngoại lai giúp đánh giá độ bền vững (robustness) của mô hình trước các dao động vận hành (operational fluctuations), phản ánh sát động học thực tế (real-world dynamics).
