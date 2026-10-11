### 2.5. Cluster analysis

* Phân tích cụm đa biến (multivariate cluster analysis) được tiến hành nhằm bổ sung cho diễn giải theo từng biến riêng lẻ (individual-variable interpretation) từ phân tích độ nhạy cục bộ (local sensitivity analysis):
  * Phân tích sử dụng các giá trị thực nghiệm của các biến vận hành, môi trường và chất lượng nước bao gồm: thời gian lưu thủy lực ($HRT$), thời gian lưu chất rắn ($SRT$), tải trọng nạp nitơ ($NLR$), tải trọng nạp phospho ($PLR$), bức xạ quang hợp hoạt dụng ($PAR$, $PAR$), nhiệt độ ($T$, $T$), mật độ quang tại bước sóng $680\text{ nm}$ ($OD_{680}$), oxy hòa tan ($DO$, $DO$), và nồng độ amoni ($NH_4\text{–}N$).
  * Trước khi phân cụm, các biến số được chuẩn hóa (standardized) nhằm ngăn chặn sự khác biệt về quy mô số học (numerical scales) ảnh hưởng đến kết quả phân tích.
* Các quan sát thực nghiệm được phân loại thành $4$ cụm (clusters) bằng thuật toán $K\text{--means}$:
  * Số lượng cụm được lựa chọn dựa trên thuật toán Ward (Ward's algorithm) để cực tiểu hóa phương sai bên trong các cụm (minimizing variance in clusters) cùng với thước đo khoảng cách Euclid (Euclidean distance measure).
  * Đặc tính cụm trung bình (mean cluster characteristics) và hồ sơ chuẩn hóa (standardized profiles) được trình bày tương ứng tại Bảng S13 (Table S13) và Hình S4 (Fig. S4) trong phần dữ liệu bổ sung.
