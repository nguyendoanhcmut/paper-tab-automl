### 3.4. Implications for PFAS treatment optimization

- Kết quả tầm quan trọng đặc trưng (feature importance) cung cấp hướng dẫn thực tiễn cho thiết kế bình phản ứng điện hóa (electrochemical reactor design):
  - Sự chi phối của thời gian điện phân (electrolysis time) chỉ ra rằng mức độ gia tăng hiệu quả loại bỏ chủ yếu do lượng điện tích truyền tích lũy (cumulative charge passage) quyết định.
  - Công tác lập kế hoạch vận hành (operational planning) cần ưu tiên bảo đảm đủ thời gian phản ứng trong phạm vi các ràng buộc về năng lượng và lưu lượng thông lượng xử lý (energy and throughput constraints).
  - Lựa chọn cực dương (anode selection) là một yếu tố có ảnh hưởng cao trong bảng xếp hạng mô hình XGBoost (Hình 3 / Fig. 3), phù hợp với các công bố trong y văn về cơ chế sinh gốc tự do phụ thuộc vào vật liệu (material-dependent radical generation).
    - Việc lựa chọn vật liệu cụ thể cần phải tương thích với chế độ mật độ dòng điện (current-density regime) mục tiêu và các ràng buộc về mặt chi phí.
    - Sự đánh đổi giữa hiệu năng và chi phí (performance–cost trade-offs) cần được đánh giá theo từng trường hợp cụ thể.
  - Các ảnh hưởng của nền nước (water-matrix effects) xếp thứ hạng thấp trong hồ sơ SHAP nhóm (grouped SHAP profile) (ví dụ: nhóm đặc trưng "Water Matrix" nằm gần đáy Hình 3 / Fig. 3).
    - Trong phạm vi khảo sát của nghiên cứu, việc chuyển giao công nghệ (technology transfer) sang các nền nước khác nhau có thể đòi hỏi ít nỗ lực tái tối ưu hóa hơn so với việc điều chỉnh các điểm đặt vận hành điện hóa (electrochemical setpoints) (với điều kiện cần được kiểm chứng trên các nền nước mới) $[45, 46]$.
- Độ chính xác dự đoán của FLAML hỗ trợ kiểm soát chặt chẽ hơn các điểm đặt vận hành (setpoint control, ví dụ: mật độ dòng điện và thời gian điện phân) nhằm phục vụ vận hành chú trọng tiết kiệm năng lượng (energy-aware operation) trong phạm vi miền khảo sát:
  - Các dự phóng năng lượng mang tính định lượng (quantitative energy projections, ví dụ: $\text{kWh}\cdot\text{m}^{-3}$) không được trích xuất từ các kết quả đầu ra của mô hình hiện tại.
  - Việc định lượng năng lượng đòi hỏi quy trình kiểm toán năng lượng điện chuyên biệt (dedicated electro-energy auditing) đi kèm kiểm chứng thực nghiệm.
- Khả năng tổng quát hóa (generalization capability) của mô hình trên các điều kiện vận hành trong tập dữ liệu gợi mở tiềm năng mở rộng học chuyển giao (transfer-learning extensions) sang các chất PFAS (per- and polyfluoroalkyl substances) liên quan (ví dụ: PFOS, GenX):
  - Khả năng mở rộng học chuyển giao phụ thuộc vào việc bao phủ các dải vận hành tương đương và cần có kiểm chứng độc lập từ bên ngoài (external validation) $[47]$.
