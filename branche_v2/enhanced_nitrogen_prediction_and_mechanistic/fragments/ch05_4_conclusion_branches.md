## 4 Conclusion

- Kết luận tổng quan về hiệu quả của khung học máy có thể giải thích trong xử lý nước thải mặn bằng MBR:
  - Nghiên cứu ứng dụng thành công khung học máy kết hợp giải thích SHAP để dự đoán nồng độ nitơ đầu ra trong hệ thống MBR.
  - Thuật toán CatBoost đạt hiệu năng cao nhất với $R^2 = 0.88$ ($RMSE = 4.27\ \text{mg/L}$) cho $NH_4^+\text{-N}_{out}$ và $R^2 = 0.91$ ($RMSE = 4.35\ \text{mg/L}$) cho $TN_{out}$.
  - So với mô hình LightGBM tốt thứ hai, CatBoost tăng hệ số $R^2$ thêm $9\%\text{–}10\%$ và giảm sai số $RMSE$ từ $14\%\text{–}16\%$.
- Khám phá cơ chế sinh hóa học và xây dựng giải pháp điều khiển quy trình thực tế:
  - Phân tích SHAP xác nhận độ mặn là yếu tố chi phối mạnh mẽ nhất làm suy giảm hiệu quả xử lý sinh học.
  - Nồng độ muối cao làm bất hoạt các enzyme nitrat hóa đồng thời gây gián đoạn quá trình khử nitrat qua cạnh tranh chuyển hóa cacbon.
  - Hiệu suất khử $COD_{eff}$ và nồng độ $DO$ giữ vai trò điều hòa chính đối với quần xã vi sinh vật bùn hoạt tính.
  - Nhiệt độ dòng vào trực tiếp điều biến động học enzyme của các chủng vi khuẩn khử nitrat ưa nhiệt.
  - Đồ thị phụ thuộc một phần PDP xác định các ngưỡng chuyển đổi phi tuyến quan trọng của độ mặn và tỷ lệ $C/N$.
  - Kết quả cung cấp căn cứ định lượng để thiết lập các biện pháp can thiệp kỹ thuật như kiểm soát độ mặn, châm bổ sung nguồn cacbon và tối ưu sục khí.
  - Mô hình học máy có thể giải thích tạo cầu nối giữa dự đoán định lượng và hiểu biết cơ chế, hỗ trợ vận hành thông minh và giảm chi phí xử lý.
