### 3.2 Confusion matrix

- Ma trận nhầm lẫn chuẩn hóa định lượng tỷ lệ phân loại chính xác và nhầm lẫn biên giữa các lớp.
  - **Hình 4.** Kết quả chuẩn hóa các lớp đối tượng trong ma trận nhầm lẫn
    - <img src="assets/fig_04_p7.jpeg" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Đường chéo chính đạt độ chính xác từ 0.94 đến 0.97 cho cả 4 giai đoạn sinh trưởng bùn.
    - **Từ đâu mà thấy được**
      - Lưới ma trận $5 \times 5$ chuẩn hóa theo dòng thực tế:
      - IS đạt 0.97, GS đạt 0.96, MS đạt 0.94, CS đạt 0.97;
      - Ô nhầm lẫn ngoại đường chéo chỉ từ 0.02 đến 0.04 tại ranh giới kích thước hạt.
- Phân tích xác suất nhận dạng chính xác theo từng giai đoạn chu kỳ sống.
  - Lớp khởi tạo (IS) và lớp phân cắt (CS) đạt tỷ lệ phân loại chính xác cao nhất trong tập kiểm tra với giá trị $0.97$.
  - Tỷ lệ nhầm lẫn khoảng $0.03$ giữa IS/CS và GS xảy ra tại các ngưỡng giá trị chuyển tiếp khi kích thước hạt bùn tiệm cận nhau.
  - Lớp sinh trưởng (GS) đạt tỷ lệ nhận dạng đúng $0.96$, với khoảng $0.04$ mẫu bị phân loại nhầm sang CS do bề mặt cả hai nhóm đều có viền thô ráp.
  - Lớp trưởng thành (MS) đạt độ chính xác $0.94$, trong đó $0.02$ mẫu bị gán nhầm sang GS và $0.04$ mẫu bị gán nhầm sang CS do sự tương đồng kích thước hạt trước và sau pha trưởng thành.
- Đánh giá phân bố lỗi dự đoán đối với lớp nền (background).
  - Trong các trường hợp nền bị mô hình nhận diện nhầm thành đối tượng bùn, tỷ lệ phân bố giữa các giai đoạn tương ứng là $0.38$ (IS), $0.38$ (GS), $0.15$ (MS), và $0.08$ (CS).
  - Các hạt có kích thước lớn ở giai đoạn MS và CS chiếm diện tích ảnh hiển vi rộng hơn nên xác suất bị nhầm lẫn từ nền thấp hơn đáng kể.
  - So với môi trường nước tự nhiên trong mô hình YOLOv7 của Liu et al. (2023) vốn chịu nhiễu quang học lớn, quy trình chụp ảnh hiển vi trường sáng chuẩn hóa giúp giảm tối đa nhiễu nền.
