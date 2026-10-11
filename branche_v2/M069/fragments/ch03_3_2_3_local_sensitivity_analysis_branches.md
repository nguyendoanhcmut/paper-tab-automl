### 2.3. Local sensitivity analysis

* Phân tích tỷ số chênh (odds ratio - OR) được sử dụng để định lượng ảnh hưởng của các biến đầu vào mô hình hồi quy logistic (logistic regression - LR) lên xác suất dự đoán vượt ngưỡng nồng độ amoni dòng ra ($NH_4\text{–}N_{eff}$).
  * Tỷ số chênh biểu diễn sự thay đổi tỷ lệ khả dĩ (change in odds) tương ứng với mức gia tăng $\Delta x_i$ của các biến đầu vào theo phương trình (3):
    $$\text{OR} = \exp\left(\sum_{i=1}^{j} \alpha_i \cdot \Delta x_i\right)$$
  * Phép tính $\text{OR}$ giả định các mức nhiễu loạn tương đối (relative perturbations) $\Delta x_i / x_i = 0{,}05\text{--}0{,}30$ đối với các biến đầu vào LR được lựa chọn.
* Độ nhạy thu được phản ánh ảnh hưởng trực tiếp của từng biến trong cấu trúc toán học của mô hình LR đã hiệu chuẩn (calibrated LR model), thay vì thể hiện đầy đủ các quan hệ nhân quả sinh học cơ bản:
  * Nhiều biến số trong hệ thống photobioreactor màng (membrane photobioreactor - MPBR) có tính phụ thuộc lẫn nhau (interdependent); ví dụ, sự thay đổi thời gian lưu bùn (solids retention time - SRT) ảnh hưởng trực tiếp đến mật độ quang ở bước sóng $680\text{ nm}$ ($OD_{680}$, chỉ số gián tiếp biểu thị nồng độ sinh khối).
  * Do đó, phân tích này cung cấp một thứ bậc định lượng (quantitative ranking) về tầm quan trọng tương đối của các biến đầu vào phục vụ dự đoán.
* Hệ số độ nhạy không thứ nguyên (dimensionless sensitivity coefficient) $S_{x_i}$ được tính toán theo phương trình (4) nhằm cho phép so sánh giữa các biến và giữa các ngưỡng khác nhau:
  $$S_{x_i} = |\text{OR} - 1|$$
  * Hệ số $S_{x_i}$ đại diện cho mức biến thiên tỷ lệ (fractional change) của tỷ số chênh vượt ngưỡng $NH_4\text{–}N_{eff}$ xác định khi biến $x_i$ tăng từ $5\text{--}30\%$.
  * Giá trị $S_{x_i}$ càng cao thể hiện độ nhạy của mô hình đối với biến đầu vào đó càng lớn, giúp nhận diện các yếu tố chi phối then chốt (key drivers) quyết định hiệu suất dự đoán.
* Phân tích độ nhạy được thực hiện để đánh giá ảnh hưởng dài hạn của các biến kiểm soát vận hành chính gồm thời gian lưu bùn ($SRT$), thời gian lưu nước (hydraulic retention time - $HRT$), và tải trọng nitơ (nitrogen loading rate - $NLR$) lên sản lượng nước tái sử dụng (reclaimed water production).
