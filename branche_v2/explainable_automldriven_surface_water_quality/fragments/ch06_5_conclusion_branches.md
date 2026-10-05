## 5 Conclusion

- **Khẳng định tính hiệu quả của khung làm việc AutoML giải thích được**:
  - Tích hợp thành công Auto-sklearn với kỹ thuật giải thích mô hình Kernel SHAP phục vụ giám sát và phân loại chất lượng nước mặt quy mô lớn.
  - Auto-sklearn đạt hiệu năng dẫn đầu với Weighted $\text{F1} = 0.9633 \pm 0.0027$, vượt qua các mô hình học máy truyền thống và các thuật toán ensemble độc lập.
  - Mô hình duy trì độ ổn định vững chắc qua các sơ đồ kiểm định nghiêm ngặt theo thời gian và theo không gian địa lý.
- **Sàng lọc thành công bộ ba chỉ số quan trắc then chốt toàn quốc**:
  - Phân tích SHAP xác định $\text{COD}_{\text{Mn}}$, $\text{TP}$ và $\text{DO}$ là ba chỉ số quan trọng hàng đầu trong việc phân định các cấp chất lượng nước.
  - Mô hình Auto-sklearn sử dụng $3$ chỉ số đạt Weighted $\text{F1} = 0.9205 \pm 0.0097$, chính xác hơn nhiều so với phương pháp đánh giá đơn nhân tố truyền thống.
  - Mức cải thiện tương đối đạt $18.9\%$ đối với nguồn nước ô nhiễm nghiêm trọng (Cấp WV), giải quyết triệt để bài toán nhận diện nguy cơ ô nhiễm nặng.
- **Tính dị biệt theo không gian và bài học thực tiễn**:
  - Bảy trong số chín lưu vực sông lớn hoàn toàn tương thích với bộ chỉ số cốt lõi toàn quốc.
  - Hai lưu vực phía Bắc (Tùng Liêu và Hoàng Hà) đòi hỏi bổ sung $\text{NH}_3\text{-N}$ để phản ánh chính xác áp lực ô nhiễm nitơ do điều kiện thủy văn tải lượng cao và dòng chảy thấp.
  - Khung làm việc giải quyết đồng thời hai trở ngại lớn: loại bỏ sự phụ thuộc vào chuyên gia khi tinh chỉnh mô hình học máy, đồng thời cắt giảm chi phí vận hành mạng lưới quan trắc môi trường tại các quốc gia đang phát triển.
