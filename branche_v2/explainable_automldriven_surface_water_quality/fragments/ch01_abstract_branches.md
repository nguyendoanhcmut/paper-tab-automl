## Abstract

- **Thách thức kép trong quan trắc và phân loại chất lượng nước mặt**:
  - Chi phí quan trắc cao khi đo đạc đầy đủ các chỉ tiêu theo quy chuẩn.
  - Quy trình xây dựng học máy truyền thống tốn nhiều thời gian và công sức chuyên gia.
- **Khung làm việc tự động và có thể giải thích (Explainable AutoML)**:
  - Khung làm việc Auto-sklearn tự động hóa toàn bộ quy trình lựa chọn mô hình và tối ưu siêu tham số.
  - Phân tích SHAP định lượng mức độ đóng góp của từng chỉ tiêu để giảm thiểu số lượng thông số cần đo.
- **Hiệu năng phân loại vượt bậc của Auto-sklearn**:
  - Dữ liệu thu thập từ các lưu vực sông chính tại Trung Quốc.
  - Auto-sklearn đạt hiệu năng trung bình cao nhất với chỉ số Weighted $\text{F1} = 0.9633 \pm 0.0027$ nhờ cấu trúc ensemble tối ưu.
  - Mô hình duy trì độ ổn định cao qua hai sơ đồ kiểm định nghiêm ngặt theo thời gian và không gian.
- **Sàng lọc bộ chỉ số then chốt bằng Kernel SHAP**:
  - Xác định $3$ chỉ số then chốt trên quy mô toàn quốc gồm $\text{COD}_{\text{Mn}}$, $\text{TP}$ và $\text{DO}$.
  - Mô hình Auto-sklearn sử dụng $3$ chỉ số này đạt Weighted $\text{F1} = 0.9205 \pm 0.0097$.
  - Mô hình $3$ chỉ số thể hiện độ chính xác cao hơn rõ rệt so với phương pháp đánh giá đơn nhân tố truyền thống trên tất cả các cấp nước.
  - Hiệu năng cải thiện tương đối $18.9\%$ đối với nước ô nhiễm nghiêm trọng (Cấp WV).
- **Tính dị biệt theo không gian giữa các lưu vực**:
  - Phần lớn lưu vực đồng nhất với bộ $3$ chỉ số toàn quốc ($\text{COD}_{\text{Mn}}$, $\text{TP}$, $\text{DO}$).
  - Hai lưu vực phía Bắc (Tùng Liêu và Hoàng Hà) đòi hỏi bổ sung thêm chỉ số $\text{NH}_3\text{-N}$.
