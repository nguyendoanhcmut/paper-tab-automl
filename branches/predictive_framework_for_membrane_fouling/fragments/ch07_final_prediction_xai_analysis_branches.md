## 3.4 - 3.5. Hiệu năng dự đoán cuối cùng và Phân tích giải thích XAI (Final Prediction & XAI Analysis)

### 3.4 Hiệu năng dự đoán chuỗi thời gian của mô hình CatBoost

#### 3.4.1 Chiến lược phân chia dữ liệu và thiết lập đồ thị chuỗi thời gian (Figure 5)
- Nghiên cứu áp dụng mô hình CatBoost cho kịch bản Case IV. Kịch bản này tích hợp chuẩn hóa Robust Scaling và trung bình động 5 ngày (MA5).
- Tập dữ liệu gồm 194 bản ghi vận hành hàng ngày liên tục của trạm MBR quy mô thực (Full-Scale MBR).
- Nhóm tác giả chia dữ liệu theo thứ tự thời gian để bảo toàn mối quan hệ phụ thuộc thời gian của chuỗi vận hành.
- Tập huấn luyện chiếm 80% dữ liệu ban đầu, tương ứng với 155 bản ghi.
- Tập kiểm tra chiếm 20% dữ liệu cuối cùng, tương ứng với 39 bản ghi chưa từng xuất hiện trong quá trình huấn luyện.
- Hình 5 biểu diễn đồ thị chuỗi thời gian giữa giá trị thực tế và giá trị dự đoán của Specific Flux ($J_s$).
- Đồ thị thể hiện giá trị thực tế bằng đường liền màu xanh lam.
- Đồ thị kết nối các điểm dữ liệu dự đoán bằng đường đứt nét màu đỏ.
- Thiết kế đường nối trực quan giúp người vận hành nhận diện rõ xu hướng tổng thể. Phương pháp này trực quan hơn biểu đồ điểm rời rạc trên chuỗi dữ liệu giới hạn.

#### 3.4.2 Các chỉ số định lượng đánh giá trên tập kiểm tra (Test Set Metrics)
- Mô hình CatBoost đạt hệ số xác định $R^2 = 0.7712$ trên tập kiểm tra độc lập (39 bản ghi cuối).
- Sai số bình phương trung bình gốc đạt mức rất thấp trên tập kiểm tra:
  $$\text{RMSE} = 0.0064$$
- Sai số tuyệt đối trung bình đạt giá trị tối thiểu:
  $$\text{MAE} = 0.0054$$
- Sai số phần trăm tuyệt đối trung bình đạt độ chuẩn xác cao:
  $$\text{MAPE} = 0.11\%$$
- Các chỉ số này đánh giá khách quan năng lực tổng quát hóa của mô hình trên dữ liệu kiểm tra mới hoàn toàn.
- Trước đó, quá trình huấn luyện và tối ưu hóa tổng thể Case IV đạt giá trị $R^2 = 0.8374$.
- Kết quả kiểm chứng khẳng định CatBoost nắm bắt tốt các tương tác phi tuyến phức tạp giữa thông số vận hành và độ nghẹt màng.
- Mô hình duy trì độ chuẩn xác dự báo cao dù kích thước tập dữ liệu chỉ gồm 194 bản ghi hàng ngày.

#### 3.4.3 Khả năng bám bắt biến động động học và giới hạn dữ liệu hiện trường
- Đường dự đoán màu đỏ bám sát biến động của Specific Flux, đặc biệt tại các đỉnh dao động mạnh.
- Khả năng này chứng minh mô hình thích ứng tốt với các điều kiện vận hành động của trạm xử lý.
- Một số sai lệch nhỏ xuất hiện ở các giai đoạn biến thiên đột ngột của dòng thải.
- Việc bổ sung thêm các biến trễ thời gian (lagged features) có thể tinh chỉnh độ chính xác ở các pha dao động nhanh.
- Tập dữ liệu 194 ngày không chứa các sự cố nghẹt nghiêm trọng hoặc chu kỳ rửa hóa chất (CIP) chuyên sâu.
- Dữ liệu phản ánh đúng độ dao động thông thường và tiến trình nghẹt màng vừa phải trong trạm MBR vận hành ổn định.
- Khung mô hình có thể tích hợp trực tiếp dữ liệu sự cố bổ sung để mở rộng khả năng dự báo rủi ro trong tương lai.

### 3.5 Khung giải thích mô hình Trí tuệ nhân tạo (XAI) cho độ nghẹt màng

#### 3.5.1 Phân tích độ quan trọng của đặc trưng (Feature Importance Analysis)
- Nghiên cứu so sánh ba phương pháp đánh giá độ quan trọng: Built-in Importance, Permutation Importance và SHAP.
- Bảng 10 tổng hợp tỷ lệ đóng góp của 15 đặc trưng vận hành và đặc trưng trung bình động:
  - Tỷ lệ F/M trung bình động 5 ngày ($\text{F/M\_MA5}$): Built-in = $22.65\%$, Permutation = $33.70\%$, SHAP = $26.17\%$.
  - Tỷ lệ $\text{F/M}$ tức thời: Built-in = $12.05\%$, Permutation = $16.19\%$, SHAP = $13.23\%$.
  - Nồng độ bùn hoạt tính $\text{MLSS}$: Built-in = $9.22\%$, Permutation = $12.18\%$, SHAP = $10.04\%$ (chính xác $10.03695\%$).
  - Nồng độ bùn hoạt tính trung bình động ($\text{MLSS\_MA5}$): Built-in = $3.56\%$, Permutation = $2.37\%$, SHAP = $3.05\%$.
  - Giá trị pH trung bình động ($\text{pH\_MA5}$): Built-in = $9.16\%$, Permutation = $11.03\%$, SHAP = $7.19\%$.
  - Giá trị $\text{pH}$ tức thời: Built-in = $3.92\%$, Permutation = $2.06\%$, SHAP = $2.96\%$.
  - Nhiệt độ trung bình động ($\text{Temp.\_MA5}$): Built-in = $4.55\%$, Permutation = $6.71\%$, SHAP = $4.95\%$.
  - Nhiệt độ tức thời ($\text{Temp.}$): Built-in = $5.18\%$, Permutation = $3.70\%$, SHAP = $6.19\%$.
  - Hiệu suất khử COD ($\text{COD RM}$): Built-in = $6.79\%$, Permutation = $1.64\%$, SHAP = $4.16\%$.
  - Tỷ số thể tích bùn lắng trung bình động ($\text{SV30\_MA5}$): Built-in = $5.30\%$, Permutation = $3.28\%$, SHAP = $3.04\%$.
  - Chỉ số thể tích bùn trung bình động ($\text{SVI\_MA5}$): Built-in = $4.47\%$, Permutation = $1.25\%$, SHAP = $2.54\%$.
  - Nồng độ oxy hòa tan trung bình động ($\text{DO\_MA5}$): Built-in = $2.93\%$, Permutation = $1.51\%$, SHAP = $3.38\%$.
  - Nồng độ oxy hòa tan tức thời ($\text{DO}$): Built-in = $4.26\%$, Permutation = $0.82\%$, SHAP = $7.06\%$.
  - Tỷ số thể tích bùn lắng tức thời ($\text{SV30}$): Built-in = $2.55\%$, Permutation = $1.39\%$, SHAP = $3.21\%$.
  - Chỉ số thể tích bùn tức thời ($\text{SVI}$): Built-in = $3.40\%$, Permutation = $2.16\%$, SHAP = $2.83\%$.
- Đặc trưng $\text{F/M\_MA5}$ giữ vị trí thống trị tuyệt đối với đóng góp cao nhất trên cả ba tiêu chuẩn đánh giá.
- Phương pháp Permutation Importance (Hình 6) chỉ ra việc hoán vị $\text{F/M\_MA5}$ làm giảm độ chính xác mô hình mạnh nhất.
- Kết quả khẳng định các biến chuyển đổi trung bình động phản ánh tác động tích lũy thời gian tốt hơn các biến tức thời.

#### 3.5.2 Phân tích đóng góp đa chiều SHAP (Multidimensional SHAP Analysis)
- Biểu đồ tóm tắt SHAP (Figure 7) minh họa phân phối giá trị SHAP và chiều tác động của từng đặc trưng lên Specific Flux.
- Màu sắc biểu diễn độ lớn của giá trị đặc trưng: màu đỏ thể hiện giá trị cao, màu xanh lam thể hiện giá trị thấp.
- Giá trị $\text{F/M\_MA5}$ cao (chấm đỏ) đóng góp dương vào dự báo mức độ nghẹt màng, làm suy giảm Specific Flux.
- Giá trị $\text{F/M\_MA5}$ thấp (chấm xanh) tương ứng với trạng thái hạn chế nghẹt màng và duy trì độ thấm thủy lực.
- Tỷ lệ $\text{F/M}$ tức thời và nồng độ $\text{MLSS}$ thể hiện cùng chiều tác động tiêu cực lên độ thông lượng riêng.
- Tổng tỷ lệ đóng góp SHAP của nhóm $\text{F/M}$ và $\text{MLSS}$ đạt $49.44\%$ ($26.17\% + 13.23\% + 10.04\%$), chi phối gần một nửa dự báo.
- Kết quả định lượng của XAI củng cố chặt chẽ các mô hình cơ chế truyền thống về màng lọc sinh học.
- Tải trọng hữu cơ $\text{F/M}$ cao kích thích vi sinh vật tiết chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP).
- Nồng độ $\text{MLSS}$ cao làm tăng độ nhớt động học của bùn và gia tăng tốc độ bồi tụ lớp bánh cặn (cake layer).
- Phân tích SHAP của $\text{pH\_MA5}$ chỉ ra độ pH thấp làm gia tăng rủi ro nghẹt màng do suy giảm hoạt tính vi sinh và biến đổi màng sinh học.
- Nhiệt độ nước thải cao tương quan thuận với độ ổn định Specific Flux nhờ làm giảm độ nhớt của nước lọc qua mao quản màng.

#### 3.5.3 Ý nghĩa kỹ thuật đối với tối ưu hóa vận hành hệ thống MBR thực tế
- Mô hình CatBoost kết hợp XAI cung cấp công cụ dự báo minh bạch thay thế mô hình hộp đen truyền thống.
- Cán bộ trạm xử lý có thể tối ưu hóa vận hành thực tế dựa trên các khuyến nghị định lượng của XAI:
  - Kiểm soát tỷ lệ F/M thông qua điều tiết lưu lượng nạp nước thải và cân đối tải lượng hữu cơ đầu vào.
  - Điều chỉnh chu kỳ xả bùn dư để duy trì nồng độ MLSS ở ngưỡng an toàn, hạn chế độ dày lớp bánh cặn.
  - Giám sát độ kiềm và bổ sung hóa chất ổn định để giữ pH_MA5 quanh vùng trung tính, bảo vệ bùn hoạt tính.
- Việc tích hợp các biến trung bình động vào hệ thống giám sát SCADA giúp dự báo sớm xu hướng tắc nghẽn ngắn hạn.
- Đơn vị quản lý có thể tối ưu hóa chi phí đầu tư thiết bị đo bằng cách ưu tiên cảm biến online cho F/M, MLSS và pH.
- Mô hình cung cấp cơ sở dữ liệu tin cậy để lập lịch rửa màng chủ động trước khi áp suất xuyên màng TMP tăng vọt.
- Phương pháp tiền xử lý dữ liệu với Robust Scaling và Moving Average giúp mô hình dễ dàng mở rộng sang các trạm MBR khác.
