## 2. Đặc tính chất lượng nước và Hiệu năng mô hình AutoML

### 3.1. Phân tích dữ liệu chất lượng nước và lựa chọn đặc trưng

#### 3.1.1. Thống kê mô tả và mức độ phân tán của các thông số chất lượng nước
- Phân phối tần suất dữ liệu: Biểu đồ phân phối tần suất (Histogram) kết hợp đường cong khớp tần số biểu diễn mật độ xuất hiện của 1339 mẫu quan trắc.
- Chỉ số định lượng mức độ biến thiên dữ liệu: Hệ số biến thiên ($CV$, tính theo phần trăm) và độ lệch chuẩn ($SD$) lượng hóa độ phân tán của các đặc trưng:
  $$CV = \frac{SD}{\text{Mean}} \times 100\%$$
- Các thông số có độ biến thiên dữ liệu mạnh nhất trong tập dữ liệu:
  - Nhiệt độ nước thô (T-RW): Độ lệch chuẩn $SD = 9.37^\circ\text{C}$, hệ số biến thiên $CV = 62\%$.
  - Nồng độ nitơ amoniac nước thô (NH3-N-RW): Độ lệch chuẩn $SD = 0.07\text{ mg/L}$, hệ số biến thiên $CV = 59\%$.
  - Độ đục nước thô (NTU-RW): Độ lệch chuẩn $SD = 2.58\text{ NTU}$, hệ số biến thiên $CV = 57\%$.
  - Nhiệt độ nước sạch sau xử lý (T-TW): Độ lệch chuẩn $SD = 8.77^\circ\text{C}$, hệ số biến thiên $CV = 54\%$.
- Các thông số có độ ổn định cao nhất trong toàn bộ chu trình xử lý:
  - Độ pH nước thô (pH-RW): Hệ số biến thiên $CV = 3\%$.
  - Độ pH nước sạch (pH-TW): Hệ số biến thiên $CV = 2\%$.
  - Độ dao động pH của nước thô và nước sạch duy trì ở mức tối thiểu xuyên suốt quá trình xử lý nước cấp.

#### 3.1.2. Quy luật biến thiên theo mùa và cơ chế lý hóa của quá trình keo tụ
- Tác động của chất lượng nước thô: Chất lượng nước thô quyết định trực tiếp độ an toàn của nguồn cấp nước sinh hoạt và nhu cầu tiêu hao chất keo tụ PACl.
- Quy luật biến thiên theo mùa của các chỉ số ô nhiễm: Nồng độ $CODMn$ và $NH_3-N$ thể hiện chu kỳ biến thiên rõ rệt giữa mùa hè và mùa đông.
- Cơ chế lý hóa trong giai đoạn mùa hè:
  - Nhiệt độ cao kết hợp lượng mưa lớn kích thích tảo sinh trưởng mạnh tại nguồn nước mặt.
  - Sinh khối tảo làm tăng vọt chỉ số pemanganat ($CODMn\text{-RW}$) và làm suy giảm chất lượng nước thô.
  - Nhiệt độ nước tăng làm giảm độ nhớt động lực học của môi trường nước.
  - Độ nhớt giảm thúc đẩy tốc độ khuếch tán và va chạm của các hạt keo tích điện trong dung dịch.
  - Hiệu ứng chuyển động nhiệt hỗ trợ tạo bông nhanh, qua đó làm giảm nhu cầu định liều hóa chất keo tụ.
- Cơ chế lý hóa trong giai đoạn mùa đông:
  - Nhiệt độ nước hạ thấp làm suy giảm độ tan và hệ số khuếch tán phân tử của chất keo tụ PACl.
  - Năng lượng hoạt hóa phản ứng tăng làm suy giảm tốc độ thủy phân của ion nhôm $Al^{3+}$.
  - Phản ứng tạo nhân bông keo diễn ra chậm chạp.
  - Bông cặn hình thành có cấu trúc xốp rỗng, hạt nhỏ mịn và tỷ trọng thấp khó lắng.
  - Người vận hành buộc phải tăng liều lượng châm PACl để đảm bảo hiệu quả lắng trong nước.
- Yêu cầu định liều chính xác: Nhà máy cần tính toán liều lượng PACl tối ưu dựa trên dữ liệu nước thô thời gian thực kết hợp biến động lịch sử.

#### 3.1.3. Ma trận tương quan hạng Spearman giữa các biến đầu vào và liều lượng PACl
- Nguyên lý đánh giá tương quan: Hệ số tương quan hạng Spearman ($r_s$) xác định mối quan hệ đơn điệu phi tuyến giữa các đặc trưng đầu vào và biến mục tiêu liều lượng PACl.
- Nhóm thông số tương quan mạnh với liều lượng châm PACl:
  - Nhiệt độ nước thô (T-RW): Hệ số $r_s = -0.71$. Nhiệt độ cao làm tăng tốc phản ứng thủy phân và giảm nhu cầu châm hóa chất.
  - Nồng độ nitơ amoniac nước thô (NH3-N-RW): Hệ số $r_s = 0.87$. Hàm lượng ion amoni cao đòi hỏi tăng liều lượng PACl để keo tụ tạp chất.
  - Độ pH nước thô (pH-RW): Hệ số $r_s = -0.90$. Nước thô có tính kiềm cao hỗ trợ phản ứng trung hòa axit giải phóng từ PACl.
  - Lưu lượng nước xử lý của nhà máy (WTR): Hệ số $r_s = -0.68$. Lưu lượng dòng chảy thay đổi làm biến đổi thời gian lưu thủy lực trong bể keo tụ.
- Nhóm thông số tương quan trung bình với liều lượng châm PACl:
  - Độ đục nước thô (NTU-RW): Hệ số $r_s = 0.45$. Hạt lơ lửng tăng đòi hỏi thêm hóa chất keo tụ để vô hiệu hóa điện thế zeta.
  - Độ dẫn điện nước thô (EC-RW): Hệ số $r_s = 0.56$. Nồng độ ion hòa tan phản ánh tải lượng tạp chất vô cơ cần keo tụ.
  - Chỉ số pemanganat nước thô (CODMn-RW): Hệ số $r_s = 0.56$. Hợp chất hữu cơ tự nhiên tiêu tốn ion nhôm qua phản ứng phức chất.
  - Độ dẫn điện nước sạch (EC-TW): Hệ số $r_s = 0.43$. Chỉ số phản ánh dư lượng ion khoáng sau chu trình keo tụ.
  - Độ đục nước sạch (NTU-TW): Hệ số $r_s = -0.23$. Liều lượng keo tụ đầy đủ giúp hạ thấp độ đục nước đầu ra.
- Nhóm thông số tương quan rất yếu:
  - Chỉ số pemanganat nước sạch (CODMn-TW): Hệ số $r_s = 0.011$. Mức độ liên kết tuyến tính và phi tuyến với liều châm PACl gần như bằng không.

#### 3.1.4. Phân tích đa cộng tuyến và thiết lập bộ 9 đặc trưng tối ưu
- Nhận diện hiện tượng đa cộng tuyến nghiêm trọng:
  - Cặp biến độ dẫn điện nước thô (EC-RW) và nước sạch (EC-TW) có tương quan tuyến tính rất cao với $r_s = 0.98$.
  - Cặp biến chỉ số pemanganat nước thô (CODMn-RW) và nhiệt độ nước sạch (T-TW) có hệ số $r_s = 0.91$.
  - Cặp biến độ dẫn điện nước thô (EC-RW) và nhiệt độ nước sạch (T-TW) có hệ số nghịch đảo cực mạnh với $r_s = -0.95$.
- Giải pháp loại bỏ biến dư thừa:
  - Mô hình chỉ giữ lại một đại diện từ mỗi nhóm thông số có tương quan tương hỗ vượt ngưỡng kiểm soát.
  - Loại bỏ đặc trưng EC-TW để tránh trùng lặp thông tin với EC-RW.
  - Loại bỏ đặc trưng T-TW do hiện tượng đa cộng tuyến mạnh với cả CODMn-RW và EC-RW.
  - Giữ lại hai đặc trưng chất lượng nước thô cốt lõi gồm EC-RW và CODMn-RW.
- Không gian 9 đặc trưng đầu vào cuối cùng ($X$):
  1. $WTR$: Lưu lượng nước thô cấp vào nhà máy ($\text{vạn tấn/ngày}$).
  2. $T\text{-RW}$: Nhiệt độ nước thô đầu vào ($^\circ\text{C}$).
  3. $pH\text{-RW}$: Giá trị pH của nước thô.
  4. $NH_3\text{-N-RW}$: Nồng độ nitơ amoniac nước thô ($\text{mg/L}$).
  5. $NTU\text{-RW}$: Độ đục nguồn nước thô ($\text{NTU}$).
  6. $EC\text{-RW}$: Độ dẫn điện nước thô ($\mu\text{S/cm}$).
  7. $CODMn\text{-RW}$: Chỉ số pemanganat nước thô ($\text{mg/L}$).
  8. $pH\text{-TW}$: Giá trị pH mục tiêu của nước sạch sau xử lý.
  9. $NTU\text{-TW}$: Độ đục mục tiêu của nước sạch sau xử lý ($\text{NTU}$).
- Biến đầu ra mục tiêu ($Y$): Liều lượng châm chất keo tụ PACl ($\text{mg/L}$). Bộ đặc trưng mô phỏng tương tác phức hợp giữa nước thô, hóa chất và nước thành phẩm.

### 3.2. So sánh hiệu năng và tối ưu hóa mô hình

#### 3.2.1. Cấu hình siêu tham số tối ưu của các thuật toán học máy đối chuẩn
- Phạm vi thuật toán so chuẩn: Nghiên cứu đối chiếu hiệu năng giữa AutoML TPOT với 5 thuật toán máy học tiêu chuẩn:
  - Cây quyết định (Decision Tree - DT).
  - Hồi quy véctơ hỗ trợ (Support Vector Regression - SVR).
  - K láng giềng gần nhất (K-Nearest Neighbors - KNN).
  - Hồi quy tuyến tính (Linear Regression - LR).
  - Cây tăng cường độ dốc (Gradient Boosting Tree - GBT).
- Bảng siêu tham số tối ưu của các thuật toán cơ sở:

| Loại mô hình | Tập siêu tham số tối ưu (Optimal Hyperparameters) | Ý nghĩa kỹ thuật của cấu hình tham số |
| :--- | :--- | :--- |
| **DT** | `max_depth = 8`, `min_samples_split = 10`, `min_samples_leaf = 5`, `max_features = 0.5`, `random_state = 42` | Giới hạn chiều sâu cây ở mức 8 để giảm thiểu quá khớp. Yêu cầu tối thiểu 10 mẫu để tách nhánh và 5 mẫu tại mỗi lá. |
| **SVR** | `C = 1`, `epsilon = 10`, `gamma = 'scale'` | Trọng số phạt sai số $C = 1$. Vùng dung sai không phạt lỗi $\epsilon = 10$. Hệ số hạt nhân RBF tự động điều chỉnh theo nghịch đảo phương sai dữ liệu. |
| **KNN** | `n_neighbors = 15`, `p = 1`, `metric = 'minkowski'` | Sử dụng 15 điểm láng giềng gần nhất. Áp dụng chuẩn khoảng cách Manhattan ($p = 1$) thay vì chuẩn Euclidean để tính khoảng cách vector. |
| **LR** | `fit_intercept = True`, `normalize = True`, `positive = False` | Tính toán hệ số chặn độc lập. Chuẩn hóa biến số về cùng thang đo phân bố. Không ràng buộc dấu dương cho các trọng số. |
| **GBT** | `n_estimators = 150`, `learning_rate = 0.1`, `max_depth = 5`, `min_samples_split = 8`, `subsample = 0.8`, `max_features = 'sqrt'` | Kết hợp 150 cây tuần tự với tốc độ học $\eta = 0.1$. Lấy mẫu ngẫu nhiên 80% dữ liệu huấn luyện cho mỗi cây. Chọn ngẫu nhiên căn bậc hai số đặc trưng. |

- Cơ chế tối ưu hóa tự động của AutoML TPOT:
  - TPOT áp dụng giải thuật lập trình di truyền (Genetic Programming) trên khung thư viện DEAP.
  - Thuật toán tự động tìm kiếm đường ống (pipeline) xử lý học máy tối ưu nhất mà không cần can thiệp thủ công.
  - TPOT tự động chọn mô hình Rừng ngẫu nhiên (Random Forest - RF) làm thuật toán hồi quy tối ưu toàn cục.

#### 3.2.2. Đánh giá định lượng hiệu năng trên tập huấn luyện và kiểm thử
- Bảng so sánh hiệu năng chi tiết giữa các mô hình học máy:

| Loại mô hình | Tập huấn luyện: RMSE (mg/L) | Tập huấn luyện: MAE (mg/L) | Tập huấn luyện: $R^2$ | Tập kiểm thử: RMSE (mg/L) | Tập kiểm thử: MAE (mg/L) | Tập kiểm thử: $R^2$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **AutoML: RF** | **0.07** | **0.02** | **1.00** | **0.89** | **0.47** | **0.96** |
| **GBT** | 1.06 | 0.74 | 0.96 | 1.41 | 0.97 | 0.91 |
| **LR** | 1.68 | 1.21 | 0.89 | 1.81 | 1.34 | 0.84 |
| **DT** | 0.00 | 0.00 | 1.00 | 2.07 | 0.66 | 0.80 |
| **KNN** | 2.90 | 1.91 | 0.68 | 3.46 | 2.55 | 0.43 |
| **SVR** | 4.81 | 2.85 | 0.13 | 4.45 | 2.89 | 0.06 |

- Hiệu năng xuất sắc của mô hình AutoML RF:
  - Trên tập huấn luyện: Mô hình đạt $\text{RMSE} = 0.07\text{ mg/L}$, $\text{MAE} = 0.02\text{ mg/L}$ và hệ số xác định $R^2 = 1.00$.
  - Trên tập kiểm thử độc lập: Mô hình đạt $\text{RMSE} = 0.89\text{ mg/L}$ (kết quả kiểm định chéo đạt $0.95 \pm 0.11\text{ mg/L}$), $\text{MAE} = 0.47\text{ mg/L}$ ($0.47 \pm 0.83\text{ mg/L}$) và $R^2 = 0.96$.
  - Mô hình RF vượt trội hơn toàn bộ các thuật toán đối chuẩn còn lại trên mọi tiêu chuẩn sai số.

#### 3.2.3. Phân tích nguyên nhân chênh lệch hiệu năng và so sánh với nghiên cứu tiền nhiệm
- Cơ chế vượt trội của mô hình học kết hợp trong AutoML:
  - Giải thuật di truyền TPOT ưu tiên lựa chọn các cấu trúc tổ hợp cây (Ensemble Learning).
  - Mô hình tổ hợp thể hiện ưu thế vượt trội trên các bộ dữ liệu dạng bảng có kích thước vừa và nhỏ ($N = 1339$).
  - Thuật toán cân bằng hoàn hảo giữa độ chệch và phương sai (bias-variance balance), ngăn ngừa hiện tượng quá khớp dữ liệu.
- Phân tích nguyên nhân quá khớp của cây quyết định (DT):
  - Mô hình DT đạt kết quả tuyệt đối trên tập huấn luyện ($\text{RMSE} = 0.00\text{ mg/L}$, $R^2 = 1.00$).
  - Hiệu năng suy giảm mạnh trên tập kiểm thử ($\text{RMSE} = 2.07\text{ mg/L}$, $R^2 = 0.80$).
  - Thuật toán DT đơn lẻ ghi nhớ các điểm ngoại lai và nhiễu ngẫu nhiên thay vì học quy luật tổng quát của dữ liệu.
- Phân tích nguyên nhân thất bại của mô hình hồi quy véctơ hỗ trợ (SVR):
  - Mô hình SVR thể hiện sai số lớn nhất với $R^2 = 0.13$ ở tập huấn luyện và $R^2 = 0.06$ ở tập kiểm thử.
  - Thuật toán SVR cực kỳ nhạy cảm với việc tinh chỉnh bộ ba siêu tham số $C$, $\epsilon$ và $\gamma$.
  - Không gian quan hệ chất lượng nước chứa nhiều biến đổi phi tuyến đột ngột khiến siêu phẳng SVR không hội tụ tối ưu.
- So sánh đối chuẩn với mô hình CNN-GRU của Kim và cộng sự:
  - Nghiên cứu của Kim et al. ứng dụng mạng tích chập kết hợp cổng hồi quy (CNN-GRU) để dự đoán liều lượng PAC.
  - Mô hình CNN-GRU đạt hệ số $R^2 > 0.8$ trên cả hai tập dữ liệu huấn luyện và kiểm thử.
  - Hạn chế: Kiến trúc học sâu chuỗi thời gian không gian đưa vào độ phức tạp thừa thãi và gây dư thừa thông tin.
  - Các nhân tố chi phối chính của phản ứng keo tụ là các thuộc tính lý hóa tĩnh (pH, độ đục, nhiệt độ, độ dẫn điện) thay vì quy luật trễ thời gian.
- So sánh đối chuẩn với mô hình học sâu của Lin và cộng sự:
  - Nghiên cứu của Lin et al. ứng dụng mô hình học sâu (Deep Learning) để dự đoán chất keo tụ PAC và muối sulfate.
  - Mô hình của Lin et al. đạt sai số $\text{RMSE} = 3.55\text{ mg/L}$ và hệ số $R^2 = 0.94$.
  - Mô hình AutoML RF trong nghiên cứu này giảm mạnh sai số dự đoán ($\text{RMSE} = 0.89\text{ mg/L}$ so với $3.55\text{ mg/L}$) và nâng cao độ chính xác ($R^2 = 0.96$ so với $0.94$).

#### 3.2.4. Phân bố mật độ sai số và độ ổn định của mô hình AutoML RF
- Biểu đồ khớp dữ liệu thực nghiệm (Fig. 4a, 4b):
  - Đường dự báo của mô hình bám sát gần như trùng khớp với đường biến thiên thực tế của mẫu quan trắc.
  - Mô hình phản ứng nhạy bén trước các bước nhảy liều lượng châm đột biến mà không bị trễ pha.
- Biểu đồ mật độ phân tán (Scatter Density Plot, Fig. 4c, 4d):
  - Các cặp giá trị liều châm PACl thực tế và dự đoán phân bố dày đặc tập trung dọc theo đường chéo lý tưởng $y = x$.
  - Độ lệch hệ thống tiềm ẩn (systematic bias) của mô hình duy trì ở mức tối thiểu.
- Phân tích biên độ sai số kiểm thử:
  - Nồng độ chất rắn lơ lửng, hạt keo và tạp chất trong nguồn nước thô nhìn chung ở mức thấp.
  - Mức độ dao động của $pH\text{-RW}$ và $NTU\text{-RW}$ diễn ra rất hẹp giúp hệ thống keo tụ ổn định.
  - Đại đa số sai số tuyệt đối ghi nhận trên tập kiểm thử đều nằm dưới ngưỡng $20\text{ mg/L}$.

#### 3.2.5. Tối ưu hóa liều lượng châm PACl theo nguồn nước và hiệu quả kinh tế
- Hạn chế của phương pháp định liều thủ công:
  - Người vận hành châm hóa chất theo kinh nghiệm cảm tính thường châm dư (over-dosing) để đảm bảo an toàn.
  - Thao tác thủ công gây lãng phí hóa chất nghiêm trọng và làm tăng nồng độ ion nhôm dư trong nước sinh hoạt.
- Thiết lập ngưỡng chất lượng nước sạch mục tiêu cho mô hình RF:
  - Nguồn nước mặt Sông Dương Tử (Yangtze River): Đặt chuẩn $\text{NTU-TW} = 0.2\text{ NTU}$, $\text{CODMn-TW} = 1.2\text{ mg/L}$, $\text{pH-TW} = 8.0$, $\text{NH}_3\text{-N-TW} = 0.01\text{ mg/L}$.
  - Nguồn nước mặt Sông Loan Hà (Luanhe River): Đặt chuẩn $\text{NTU-TW} = 0.3\text{ NTU}$, $\text{CODMn-TW} = 1.5\text{ mg/L}$, $\text{pH-TW} = 8.0$, $\text{NH}_3\text{-N-TW} = 0.01\text{ mg/L}$.
- Hiệu quả tối ưu hóa đối với nguồn nước Sông Dương Tử:
  - Chu kỳ khai thác: Kéo dài liên tục 9 tháng mỗi năm, từ tháng 3 đến tháng 11.
  - Đặc tính vận hành: Liều châm thủ công dao động từ $8$ đến $30\text{ mg/L}$.
  - Cơ chế keo tụ: Mùa xuân và mùa hè nhiệt độ cao làm PACl thủy phân nhanh. Vi tảo tích điện âm phát triển mạnh làm tăng nhu cầu hóa chất trung hòa điện tích.
  - Kết quả kiểm soát: Mô hình triệt tiêu lượng châm dư thừa theo kinh nghiệm, giảm mức tiêu hao $222\text{ kg PACl/ngày}$.
  - Giá trị kinh tế: Tiết kiệm chi phí hóa chất $180.7\text{ Nhân dân tệ (RMB)/ngày}$, tương đương giảm $11\%$ tổng lượng tiêu thụ PACl hàng năm của nguồn nước này.
- Hiệu quả tối ưu hóa đối với nguồn nước Sông Loan Hà:
  - Chu kỳ khai thác: Kéo dài 3 tháng mùa đông lạnh, từ tháng 12 đến tháng 2 năm sau.
  - Đặc tính vận hành: Liều châm thủ công dao động ở mức rất cao, từ $10$ đến $35\text{ mg/L}$.
  - Cơ chế keo tụ: Nhiệt độ nước mùa đông hạ thấp làm phản ứng thủy phân nhôm kém hoàn toàn. Bông cặn nhỏ và xốp nhẹ, kết hợp nguy cơ ô nhiễm nguồn phân bón nông nghiệp.
  - Kết quả kiểm soát: Mô hình triệt tiêu hiện tượng châm bù quá mức do tâm lý lo sợ nhiệt độ thấp, giảm mức tiêu hao $225\text{ kg PACl/ngày}$.
  - Giá trị kinh tế: Tiết kiệm chi phí hóa chất $183.2\text{ Nhân dân tệ (RMB)/ngày}$, tương đương giảm $8\%$ tổng lượng tiêu thụ PACl hàng năm của nguồn nước này.
- Lợi ích tổng hợp trên toàn nhà máy xử lý nước cấp:
  - Tỷ trọng phân bổ khai thác: Nguồn Sông Dương Tử chiếm $75\%$ thời gian ($9/12$ tháng). Nguồn Sông Loan Hà chiếm $25\%$ thời gian ($3/12$ tháng).
  - Tỷ lệ tiết kiệm bình quân gia quyền: Mô hình AutoML RF cắt giảm chính xác $10.25\%$ tổng khối lượng hóa chất keo tụ PACl cho toàn nhà máy trong một năm vận hành:
    $$\Delta_{\text{PACl}} = \left(11\% \times \frac{9}{12}\right) + \left(8\% \times \frac{3}{12}\right) = 8.25\% + 2.00\% = 10.25\%$$
  - Ý nghĩa kỹ thuật và môi trường: Mô hình đảm bảo chất lượng nước thành phẩm đạt chuẩn an toàn nghiêm ngặt. Hệ thống hạ thấp chi phí vận hành và giảm thiểu tác động xả thải hóa chất ra môi trường.
