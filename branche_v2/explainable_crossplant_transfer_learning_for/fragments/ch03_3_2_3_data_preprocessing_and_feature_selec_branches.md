### 2.3. Data preprocessing and feature selection

- Dữ liệu thô được tiền xử lý tuần tự qua các bước xử lý ngoại lai (outlier treatment), nội suy giá trị thiếu (missing-value imputation) và chuẩn hóa điểm z (z-score standardization) nhằm bảo đảm phát triển mô hình tin cậy:
  - Xử lý ngoại lai và nội suy giá trị thiếu được thực hiện đầu tiên trên các tập dữ liệu thô (Text S2).
  - Chuẩn hóa điểm z ($z$-score standardization) được áp dụng trong quá trình tiền xử lý để đưa các biến về thang đo có thể so sánh được và ngăn các biến có khoảng giá trị số lớn hơn chi phối quá trình huấn luyện mô hình (Text S3).
  - Bộ chuẩn hóa ($scaler$) chỉ được khớp (fitted) trên tập dữ liệu huấn luyện (training data), và đầu ra của mô hình được biến đổi ngược (inverse-transformed) về thang đo gốc sau khi hoàn thành huấn luyện.
- Áp suất xuyên màng ngày tiếp theo (next-day $TMP$) là mục tiêu dự đoán cuối cùng của nghiên cứu, trong khi vi sai $TMP$ ($\text{d}TMP$) chỉ được dùng làm mục tiêu huấn luyện trung gian:
  - Biến $\text{d}TMP$ đóng vai trò mục tiêu huấn luyện trung gian (intermediate training target) nhằm giảm thiểu tính không dừng (non-stationarity) và cải thiện khả năng so sánh kết quả đầu ra giữa các nhà máy $[33, 34]$.
  - So với các giá trị $TMP$ thô, biến $\text{d}TMP$ làm giảm sự khác biệt về mức độ $TMP$ giữa các nhà máy và tạo ra các phân phối tập trung quanh giá trị $0$ hơn (Hình S3 / Fig. S3).
  - Các giá trị $\text{d}TMP$ dự đoán sau đó được cộng vào $TMP$ ngày hiện tại (current-day $TMP$) để tái cấu trúc $TMP$ ngày tiếp theo (next-day $TMP$) phục vụ đánh giá mô hình và trình bày kết quả.
- Phân tích thành phần chính liên hợp (joint principal component analysis - joint $PCA$) được tiến hành để đánh giá độ sai lệch phân phối và vùng chồng lấn giữa miền nguồn và miền đích:
  - Joint $PCA$ được thực hiện bằng cách sử dụng tập hợp các biến đầu vào kết hợp cùng với $\text{d}TMP$ nhằm đánh giá sự sai khác phân phối (distribution discrepancy) và độ chồng lấn (overlap) giữa nguồn và đích liên quan đến học chuyển giao (transfer learning).
  - Khối biến đầu vào (input block) và khối biến đầu ra (output block) được chuẩn hóa riêng biệt và được gán trọng số tổng thể bằng nhau (Text S4).
- Phân tích tương quan Pearson (Pearson correlation analysis) đóng vai trò bước sàng lọc sơ bộ thô (coarse pre-screening step) để kiểm soát số chiều thực dụng dựa trên tỷ lệ kích thước mẫu trên số đặc trưng:
  - Tỷ lệ kích thước mẫu trên số đặc trưng (sample-size-to-feature ratio - $SFR$) là chỉ số quan trọng phản ánh mức độ phù hợp của độ phức tạp mô hình đối với kích thước tập dữ liệu cho trước.
  - Trong mô hình hóa với tập mẫu nhỏ (small-sample modeling), tỷ lệ $SFR > 10$ thường được coi là ngưỡng mong muốn $[35]$.
  - Bước sàng lọc ban đầu bằng phân tích tương quan Pearson (Text S5) được thực hiện đối chiếu với $TMP$ thay vì $\text{d}TMP$ do mục tiêu dự đoán cuối cùng vẫn là next-day $TMP$.
  - Quy trình này đồng thời xem xét mối liên kết giữa đặc trưng với biến mục tiêu (feature–target association) và tính cộng tuyến giữa các đặc trưng (inter-feature collinearity).
  - Phân tích tương quan này chỉ đóng vai trò quy trình kiểm soát số chiều mang tính thực dụng (pragmatic dimensionality-control procedure), không phải là đánh giá dứt khoát về mức độ liên quan dự đoán phi tuyến (nonlinear predictive relevance).
