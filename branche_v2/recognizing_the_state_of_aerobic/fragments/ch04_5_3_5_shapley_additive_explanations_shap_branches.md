### 3.5 SHapley additive exPlanations (SHAP)

- Bản đồ nhiệt SHAP giải thích cơ chế gán trọng số đặc trưng hình thái theo kích thước hạt.
  - **Hình 7.** Phân tích tính diễn giải đặc trưng SHAP cho toàn bộ các lớp
    - <img src="assets/fig_07_p9.jpeg" alt="Hình 7" />
    - **Hình này chứng minh điều gì**
      - Mô hình chú trọng đặc trưng toàn cục ở hạt nhỏ và đường viền ở hạt lớn.
    - **Từ đâu mà thấy được**
      - Ma trận bản đồ nhiệt Shapley giữa 4 lớp:
      - Màu đỏ thể hiện vùng ảnh hưởng dương, màu xanh thể hiện ảnh hưởng âm;
      - IS và GS chịu chi phối bởi màu sắc toàn thể; MS và CS định hình qua viền ngoài.
- Cơ chế chú ý đối lập giữa đặc trưng toàn cục và đặc trưng đường viền biên.
  - Mô hình ưu tiên thu nhận đặc trưng toàn cục (global features) đối với ảnh hạt nhỏ và đặc trưng đường viền (edge features) đối với ảnh hạt lớn.
  - Các đặc trưng toàn cục của IS và GS như sự chuyển biến màu sắc và viền hạt gồ ghề cung cấp căn cứ phân biệt rõ rệt với pha trưởng thành.
  - Ảnh ở giai đoạn trưởng thành (MS) có màu nâu sẫm hoặc đen với đường biên nhẵn mịn, tạo tác động nghịch đối với xác suất dự đoán IS và GS.
  - Sự tách biệt về trọng số viền biên khẳng định tính đúng đắn khoa học của bộ tiêu chuẩn phân loại hình thái hạt AGS.
- Tương quan sinh học động học giữa giai đoạn phân cắt và chu kỳ khởi tạo mới.
  - Cấu trúc bên trong và các đặc trưng chi tiết của pha phân cắt (CS) tạo ảnh hưởng tương quan trực tiếp đến phân lớp khởi tạo (IS).
  - Các mảnh vỡ sinh khối tách ra từ hạt lão hóa ở giai đoạn CS trở thành mầm tiền hạt cho giai đoạn IS trong chu kỳ kế tiếp.
  - Mô hình học sâu nắm bắt chính xác quy luật sinh thái học tuần hoàn của bùn hạt hiếu khí trong điều kiện dòng chảy liên tục.
