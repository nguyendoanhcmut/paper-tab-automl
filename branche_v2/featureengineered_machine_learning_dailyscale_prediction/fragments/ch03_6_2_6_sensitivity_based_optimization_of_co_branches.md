### 2.6 Sensitivity-based optimization of coagulant dosing

- Mục tiêu của khung tối ưu hóa liều lượng châm chất keo tụ phèn sắt $Fe_2(SO_4)_3$ theo độ nhạy:
  - Đánh giá phản ứng động học của nồng độ photpho tổng ($T\text{-}P$) đầu ra khi thay đổi liều lượng châm hóa chất keo tụ.
  - Xác định ngưỡng liều lượng châm tối thiểu nhằm duy trì nồng độ photpho đầu ra luôn tuân thủ quy chuẩn xả thải khắt khe ($0.2\ \text{mg/L}$).
- Thiết lập kịch bản mô phỏng động học bằng hệ số nhân liều lượng ($m$):
  - Áp dụng hệ số nhân $m$ lên liều lượng châm phèn sắt cơ sở tại từng thời điểm $t$ để thiết lập các kịch bản vận hành thử nghiệm.
  - Tích hợp cấu trúc tự hồi quy (autoregressive simulation) để truyền lan tác động của việc điều chỉnh hóa chất qua chuỗi thời gian liên tục.
- Cơ chế cập nhật đệ quy các đặc trưng biến động ngắn hạn trong mô phỏng:
  - Các đặc trưng sai phân ngắn hạn ($\Delta T\text{-}P$) được tính toán lại tại mỗi bước dự báo dựa trên chính các giá trị dự đoán của mô hình ở các bước trước đó, thay vì dùng dữ liệu quan sát thực nghiệm.
  - Sơ đồ cập nhật đệ quy nắm bắt các phản hồi phi tuyến và tác động tích lũy dài hạn của hệ thống khi liều lượng hóa chất chệch khỏi trạng thái vận hành ban đầu.
  - Lượng hóa độ nhạy của chất lượng nước đầu ra trước từng mức độ châm phèn, phân định rõ vùng định lượng tối ưu giữa tiết kiệm hóa chất và an toàn xả thải.
