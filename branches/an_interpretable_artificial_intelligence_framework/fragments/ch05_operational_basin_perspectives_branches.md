## 3.3. Điều kiện vận hành tối ưu cho MBR xử lý nước thải bán dẫn (Operational Basin)

### 3.3.1. Từ tầm quan trọng đặc trưng đến không gian vận hành khả thi

#### Giới hạn của SHAP và nguyên lý ánh xạ không gian khả thi
- Phân tích SHAP xác lập sự đồng thuận trên 16 thuật toán về chiều tác động của các thông số. SRT chi phối áp suất hút xuyên màng TMP theo hướng đơn điệu. HRT thiết lập trần thủy lực cho lưu lượng nước thấm. Lưu lượng sục khí Air tác động phi tuyến lên TMP với lợi nhuận giảm dần.
- Phân tích SHAP không thể chỉ ra tổ hợp thông số đầu vào để đạt đồng thời cả ba mục tiêu. Phương pháp này cũng không phát hiện được xung đột ràng buộc giữa các biến.
- Khung phương pháp luận giải quyết khoảng trống này bằng cách chuyển đổi độ quan trọng đặc trưng thành dải biên vận hành định lượng. Mô hình Extra Trees ánh xạ không gian khả thi trên đa tạp dữ liệu thực nghiệm.
- Ba tiêu chuẩn ràng buộc vận hành đồng thời gồm:
  - Áp suất hút xuyên màng: $\text{TMP} \in [-0.09, -0.03]\text{ bar}$.
  - Lưu lượng nước thấm lọc qua màng: $Q_{\text{permeate}} \in [1.5, 2.2]\text{ m}^3/\text{min}$.
  - Mức chất lỏng trong bể chứa cụm màng: $H_{\text{tank}} \in [65.0\%, 67.0\%]$.

#### Kỹ thuật lấy mẫu trên đa tạp thực tế (Manifold-Constrained Resampling)
- Kỹ thuật lấy mẫu hạt nhân hiệp phương sai cục bộ tạo ra $500{,}000$ trạng thái vận hành ứng viên trên đa tạp dữ liệu thực nghiệm.
- Thuật toán xác định $207{,}238$ trạng thái khả thi, chiếm tỷ lệ $41.4\%$ tổng số mẫu kiểm tra.
- Độ phân tán tập hợp trên 100 cây quyết định Extra Trees xác lập khoảng tin cậy $95\%$:
  - Sai số TMP đạt $\pm 0.008\text{ bar}$.
  - Sai số lưu lượng nước thấm đạt $\pm 0.17\text{ m}^3/\text{min}$.
  - Sai số mức chất lỏng bể màng đạt $\pm 0.71\%$.
- Hệ thống khuyến nghị vận hành sâu bên trong không gian khả thi thay vì vùng biên để phòng ngừa rủi ro vi phạm thủy lực.
- Khoảng cách láng giềng gần nhất trung vị từ điểm mẫu đến dữ liệu thực nghiệm đạt $0.121$ đơn vị chuẩn hóa. Khoảng cách này tương đương giá trị $0.119$ giữa các giờ vận hành thực tế.
- Mọi trạng thái dự báo đều là phép nội suy hợp lý trong không gian nhà máy từng trải qua. Các khuyến nghị đảm bảo tính khả thi vật lý tuyệt đối.
- Cửa sổ vận hành được xếp hạng theo tỷ lệ khả thi có điều kiện (Conditional Feasibility Rate). Phương pháp này ưu tiên vùng trạm đạt hiệu suất cao nhất thay vì vùng trạm lưu lại nhiều thời gian nhất.

#### Cấu trúc tương quan phi tuyến và tương tác giữa các biến vận hành
- Không gian vận hành khả thi tạo thành cấu trúc dải hẹp tương quan phi tuyến, không phải hình hộp chữ nhật độc lập.
- Quan hệ đối nghịch trực tiếp xuất hiện giữa MLSS và F/M với hệ số tương quan Pearson $r = -0.791$.
- Quan hệ đồng biến tạo thành dải dốc tăng dần xuất hiện giữa C/N và HRT.
- Giao điểm các dải khuyến nghị đơn lẻ thuộc vùng xác suất cao ($60\% - 100\%$) trong 20 trên 21 cặp biến. Hiệu suất này vượt trội so với mức nền $37.1\%$ của toàn hệ thống.
- Cặp biến SRT và HRT tạo ra tương tác phi cộng gộp duy nhất:
  - Khi xét riêng lẻ, dải tối ưu của SRT ($43.2 - 72.2\text{ ngày}$) và HRT ($5.875 - 6.381\text{ h}$) mang lại tỷ lệ đạt mục tiêu lần lượt là $77.0\%$ và $82.4\%$.
  - Khi kết hợp đồng thời hai dải tối ưu đơn lẻ, hệ thống chỉ ghi nhận 35 giờ vận hành thực tế. Tỷ lệ đạt mục tiêu giảm xuống còn $34.3\%$, thấp hơn mức nền $37.1\%$.
  - Cơ chế kỹ thuật: Khi duy trì SRT trong dải $43.2 - 72.2\text{ ngày}$, trạm thực tế hoạt động ở HRT $6.2 - 7.5\text{ h}$. Dải HRT ngắn $5.9 - 6.4\text{ h}$ chỉ xuất hiện khi tuổi bùn đạt $72 - 108\text{ ngày}$.
  - HRT ngắn đòi hỏi thông lượng nước cao. Việc duy trì thông lượng cao ở tuổi bùn thấp đòi hỏi tốc độ xả bùn hoạt tính (WAS) vượt quá giới hạn thiết bị trạm.
  - Quy tắc điều khiển: Người vận hành không cài đặt SRT và HRT độc lập. Cần cố định biến chậm SRT trước, sau đó xác định HRT phụ thuộc theo SRT.

---

### 3.3.2. Cấu trúc mật độ của các vùng khả thi (Feasible Windows)

#### Đòn bẩy sinh học và trần thủy lực của hệ thống
- Mức nền cơ sở của toàn hệ thống đạt tỷ lệ thỏa mãn đồng thời cả ba mục tiêu là $37.1\%$ ($1703$ trên $4593\text{ giờ}$ SCADA).
- HRT là đòn bẩy thủy lực nhạy nhất của hệ thống:
  - Tỷ lệ khả thi đạt đỉnh $82.8\%$ theo mô hình và $82.4\%$ theo dữ liệu thực tế trong dải $5.88 - 6.38\text{ h}$.
  - Tỷ lệ khả thi giảm đơn điệu về $0\%$ khi $\text{HRT} > 7.95\text{ h}$ trên cả mô hình lẫn số đo thực tế.
  - Cơ chế trần thủy lực: Với thể tích bể hiếu khí cố định ($8604\text{ m}^3$), giá trị $\text{HRT} > 8\text{ h}$ tương ứng với lưu lượng đầu vào quá thấp. Hệ thống không thể đạt mục tiêu lưu lượng nước thấm tối thiểu $1.5\text{ m}^3/\text{min}$.
- SRT chi phối trực tiếp áp suất TMP và tốc độ bám bẩn màng:
  - Tỷ lệ đạt mục tiêu đạt $77.0\%$ trong dải $43.2 - 72.2\text{ ngày}$, so với $32.3\%$ ngoài dải ($p < 0.001$).
  - Tỷ lệ đạt mục tiêu giảm liên tục theo tuổi bùn: $74.5\%$ ($77 - 84\text{ ngày}$), $59.0\%$ ($84 - 86\text{ ngày}$), $18.7\%$ ($87 - 92\text{ ngày}$) và $0\%$ ($> 108\text{ ngày}$).
  - Khuyến nghị vận hành: Giữ SRT dưới $85\text{ ngày}$ và duy trì trong dải mục tiêu $43.2 - 72.2\text{ ngày}$.
  - Ba nguồn bằng chứng độc lập cùng khẳng định dải tối ưu của SRT. Các bằng chứng gồm đồng thuận SHAP trên 16 mô hình, bề mặt khả thi đa tạp và số liệu đo thực tế trạm.

#### Bảng thông số vận hành khuyến nghị theo tỷ lệ đạt mục tiêu
- Dưới đây là các dải thông số vận hành tối ưu nhằm đạt đồng thời ba mục tiêu hiệu suất:

| Thông số | Đơn vị | Dải quan sát thực tế | Dải khuyến nghị (dựa trên tỷ lệ) | Tỷ lệ đạt mục tiêu trong / ngoài dải (%) | Hướng dẫn vận hành và hiệu quả kiểm định giữ lại |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SRT** | ngày | $43.3 - 108.4$ | $43.2 - 72.2$ | $77.0 \text{ / } 32.3$ | Giữ dưới $85\text{ ngày}$. Hướng tới $43.2 - 72.2\text{ ngày}$. Tỷ lệ đạt giảm xuống $< 20\%$ khi $> 87\text{ ngày}$. Mức tăng chuyển giao giữ lại ngoài thời gian đạt $+22.7\text{ pp}$. |
| **HRT** | h | $5.875 - 11.042$ | $5.875 - 6.381$ | $82.4 \text{ / } 32.1$ | Vận hành trong dải $5.9 - 6.4\text{ h}$. Tỷ lệ đạt giảm về $0\%$ khi $> 7.95\text{ h}$ do trần thủy lực giới hạn lưu lượng nước thấm. |
| **Air** | $\text{m}^3/\text{h}$ | $4470 - 7272$ | $4868 - 5892$ | $61.1 \text{ / } 34.4$ | Giữ trong dải $4868 - 5892\text{ m}^3/\text{h}$. Cung cấp đủ lực cắt bề mặt cho TMP mà không rơi vào chế độ sục khí phản ứng quá mức khi tải cao. |
| **MLSS** | mg/L | $1918 - 7630$ | $5580 - 6138$ | $67.6 \text{ / } 29.5$ | Vận hành trong dải $5580 - 6138\text{ mg/L}$. Đạt mức tăng chuyển giao ngoài thời gian cao nhất trong các đòn bẩy ($+30.9\text{ pp}$). |
| **C/N** | – | $4.80 - 17.52$ | $4.80 - 7.51$ | $55.0 \text{ / } 32.6$ | Biến giám sát, không phải điểm đặt cố định. Dải thuận lợi $4.80 - 7.51$ (vai phụ $11.3 - 12.9$ đạt $50.5\%$). Cần tái ước lượng định kỳ theo lịch xả bán dẫn. |
| **F/M** | $\text{ngày}^{-1}$ | $0.0117 - 0.0658$ | $0.0233 - 0.0252$ | $68.3 \text{ / } 33.5$ | Giữ dưới $\approx 0.03\text{ ngày}^{-1}$. Tăng xả bùn WAS đón đầu các chu kỳ xả thải hữu cơ cao. Chuyển giao ngoài thời gian tăng $+15.7\text{ pp}$. |
| **Glu** | L/min | $0.402 - 1.352$ | $0.705 - 1.352$ | $59.8 \text{ / } 31.3$ | Đòn bẩy có điều kiện, châm để duy trì cân bằng C/N. Không phải mục tiêu tối ưu hóa độc lập. |

#### Động lực học sục khí và nồng độ sinh khối
- Lưu lượng sục khí Air tối ưu hóa ứng suất cắt bề mặt màng:
  - Tỷ lệ đạt mục tiêu cao nhất đạt $61.1\%$ trong dải $4868 - 5892\text{ m}^3/\text{h}$. Tỷ lệ này giảm xuống $17.2\%$ khi khí sục vượt $6356\text{ m}^3/\text{h}$.
  - Áp suất TMP đạt điểm tối ưu tại dải khí sục $5500 - 6000\text{ m}^3/\text{h}$, nơi ứng suất cắt duy trì tính linh động của bánh bùn. Khí sục cao hơn không mang lại lợi ích giảm TMP.
  - Tương quan âm giữa khí sục và lưu lượng nước thấm đạt $r = -0.410$. Mối tương quan này xuất phát từ logic điều khiển khi tải cao, không do suy giảm thủy lực.
- Nồng độ bùn hoạt tính MLSS quyết định trở lực dòng thấm:
  - Tỷ lệ đạt mục tiêu tạo đường cong chữ U ngược: tăng từ $3.9\%$ ($< 3590\text{ mg/L}$) lên cực đại $67.6\%$ ($5580 - 6138\text{ mg/L}$ với $918\text{ giờ}$ ghi nhận), sau đó giảm xuống $25.1\%$ ($> 6138\text{ mg/L}$).
  - MLSS thấp làm giảm hiệu quả xử lý sinh học. MLSS cao làm tăng độ nhớt bùn và gây tắc nghẽn màng nghiêm trọng.
- Tải trọng hữu cơ F/M chi phối lớp gel sinh học:
  - Tỷ lệ đạt mục tiêu đạt cực đại $68.3\%$ trong dải $0.0233 - 0.0252\text{ ngày}^{-1}$, so với $15.0\%$ khi $\text{F/M} > 0.0373\text{ ngày}^{-1}$.
  - F/M cao kích thích vi sinh vật tiết các sản phẩm vi sinh hòa tan (SMP), đẩy nhanh quá trình bám bẩn lớp gel trên màng sợi rỗng.
  - Hướng dẫn vận hành: Khống chế $\text{F/M} < 0.03\text{ ngày}^{-1}$. Chủ động xả bùn khi hệ thống quản lý sản xuất báo trước chu kỳ xả thải hữu cơ cao.
- Tỷ lệ C/N và lưu lượng châm glucose Glu phản ánh chế độ xả thải hóa chất:
  - Tỷ lệ đạt mục tiêu của C/N đạt đỉnh $55.0\%$ tại dải $4.80 - 7.51$ và đỉnh phụ $50.5\%$ tại dải $11.3 - 12.9$. Cấu trúc hai đỉnh tương ứng với nước thải bóc tách photoresist giàu carbon và nước rửa khắc axit giàu nitơ.
  - Glucose đóng vai trò nguồn carbon ngoại sinh để ổn định C/N (dải tối ưu $0.705 - 1.352\text{ L/min}$, đạt $59.8\%$), tương quan rất yếu với F/M.

#### Kiểm chứng định lượng giữa dự báo mô hình và dữ liệu thực tế
- Mô hình được kiểm chứng đối đầu trên 70 khoảng bin phân vị thập phân (deciles) của 7 thông số đầu vào.
- Hệ số tương quan Pearson giữa tỷ lệ dự báo và tỷ lệ thực đo đạt $r = 0.988$ ($p = 9 \times 10^{-57}$).
- Hệ số tương quan hạng Spearman đạt $\rho = 0.984$.
- Độ lệch tuyệt đối trung bình (MAD) giữa dự báo và thực tế đạt $4.3$ điểm phần trăm.
- Sai số lạc quan hệ thống rất nhỏ, chỉ $+4.2$ điểm phần trăm. Hệ số tương quan trên từng biến dao động trong khoảng $r = 0.96 - 0.998$.
- Kết quả khẳng định mô hình tái lập chính xác tần suất đạt mục tiêu của trạm thực tế mà không cần căn chỉnh tham số.

---

### 3.3.3. Kiểm định cửa sổ vận hành trên giai đoạn dữ liệu giữ lại (Out-of-Time Validation)

#### Thiết kế kiểm định theo chuỗi thời gian độc lập
- Nghiên cứu kiểm tra năng lực suy rộng của cửa sổ vận hành trên giai đoạn dữ liệu thời gian tương lai chưa từng được học.
- Chuỗi dữ liệu SCADA 306 ngày được chia theo thời gian nghiêm ngặt. Tập huấn luyện gồm $70\%$ dữ liệu đầu (tháng 1 đến 7) để xác lập cửa sổ vận hành. Tập kiểm định độc lập gồm $30\%$ dữ liệu sau (tháng 8 đến 10/11).
- Quá trình kiểm định đánh giá trực tiếp tần suất đạt mục tiêu thực tế của trạm, độc lập hoàn toàn với sai số mô hình học máy.
- Cửa sổ vận hành rút ra từ 7 tháng đầu đặt điều kiện ưu tiên hàng đầu cho $\text{SRT} \le 84.5\text{ ngày}$ kết hợp với điều chỉnh thứ cấp của HRT.

#### Hiệu quả cải thiện tỷ lệ đạt mục tiêu và độ tin cậy thống kê
- Trạm ghi nhận 415 giờ vận hành rơi vào bên trong cửa sổ khuyến nghị trong giai đoạn giữ lại.
- Tỷ lệ đạt đồng thời cả ba tiêu chí hiệu suất bên trong cửa sổ đạt $61.9\%$, vượt trội so với mức nền $39.3\%$ ngoài cửa sổ ($37.1\%$ toàn trạm).
- Tỷ số chênh lệch khả năng đạt mục tiêu đạt $\text{Odds Ratio} = 3.89$ với mức ý nghĩa thống kê cao (kiểm định chính xác Fisher $p = 3 \times 10^{-29}$).
- Hiệu quả chuyển giao độc lập của từng biến điều khiển sinh học trên dữ liệu giữ lại:
  - Nồng độ bùn hoạt tính MLSS tăng $+30.9$ điểm phần trăm (mức tăng cao nhất trong các đòn bẩy).
  - Thời gian lưu bùn SRT tăng $+22.7$ điểm phần trăm.
  - Tải trọng hữu cơ F/M tăng $+15.7$ điểm phần trăm.
- Ba biến kiểm soát sinh học (SRT, MLSS, F/M) có chu kỳ can thiệp từ vài giờ đến vài ngày. Các biến này đạt độ bền vững chuyển giao cao nhất và giữ vai trò trung tâm trong giao thức vận hành.

---

### 3.3.4. Sự dịch chuyển tầm quan trọng đặc trưng và hàm ý kiểm soát thời gian thực

#### Hiện tượng dịch chuyển thứ hạng SHAP trong vùng khả thi
- Việc giới hạn không gian phân tích SHAP vào bên trong vùng khả thi làm thay đổi đáng kể thứ hạng quan trọng của các đặc trưng.
- Nguyên nhân: Các điều kiện vận hành cực đoan gây hại ($\text{SRT} > 100\text{ ngày}$, $\text{MLSS} > 7500\text{ mg/L}$, $\text{HRT} > 10\text{ h}$) đã bị loại bỏ hoàn toàn bởi các ràng buộc đầu ra.
- Khi loại bỏ các điều kiện cực đoan, các nguồn biến động ngắn hạn trở thành yếu tố chi phối chính.
- Mức độ quan trọng của tỷ lệ F/M đối với mức chất lỏng bể màng tăng vọt $87\%$, nhảy từ vị trí thứ 5 lên vị trí thứ 4.
- Trong toàn bộ dữ liệu, giá trị SRT và MLSS cực hạn chi phối phương sai mức nước. Hiện tượng này che khuất tác động ngắn hạn của tải lượng hữu cơ.
- Trong vùng khả thi, khi SRT và MLSS duy trì ở mức an toàn, F/M trở thành động lực chính dẫn dắt dao động mức bể màng theo từng giờ.

#### Chiến lược kiểm soát ba cấp tốc độ cho mức bể màng
- Dao động của F/M phản ánh trực tiếp chu kỳ xả thải theo mẻ của các công đoạn chế tạo linh kiện bán dẫn.
- Mức độ quan trọng của MLSS đối với mức nước bể màng cũng tăng đồng thời, định hình ba đòn bẩy điều khiển phản ứng nhanh:
  - **Tốc độ châm glucose Glu (thời gian phản ứng: vài phút)**: Ổn định tỷ lệ dinh dưỡng và kiểm soát tải hữu cơ tức thời.
  - **Lưu lượng xả bùn hoạt tính WAS (thời gian phản ứng: vài giờ)**: Điều chỉnh mật độ sinh khối và giải phóng thể tích bùn.
  - **Điều chỉnh F/M qua bể điều hòa lưu lượng (thời gian phản ứng: vài giờ)**: Giảm đỉnh nồng độ hữu cơ cấp vào bể phản ứng sinh học.
- Ba đòn bẩy thời gian thực giúp khống chế mức nước bể màng dưới ngưỡng an toàn $67.0\%$ khi sản xuất cao điểm. Người vận hành không cần chờ chu kỳ điều chỉnh SRT kéo dài nhiều tuần.
- Thứ hạng của C/N cũng tăng lên đối với TMP và lưu lượng nước thấm. C/N đóng vai trò thông số giám sát động cần tái ước lượng định kỳ theo tiến độ sản xuất của xưởng đúc wafer.
- Khuyến nghị vận hành đạt sự hội tụ từ ba nguồn chứng cứ. Các chứng cứ gồm đồng thuận SHAP trên 16 mô hình, bề mặt khả thi đa tạp và số đo thực tế SCADA.

---

## 3.4. So sánh và triển vọng (Comparison & Perspectives)

### 3.4.1. Hiệu suất dự đoán

#### Đối sánh hiệu năng với các nghiên cứu MBR tiền nhiệm
- Các nghiên cứu học máy MBR trước đây chủ yếu tập trung vào nước thải sinh hoạt hoặc đô thị ở quy mô phòng thí nghiệm và quy mô pilot. Các công trình trước thường chỉ dự báo một biến mục tiêu đơn lẻ như TMP hoặc lưu lượng nước thấm:
  - Mô hình MLP và LSTM dự báo TMP cho trạm pilot AnMBR xử lý nước thải đô thị đạt $R^2 > 0.91$ [68].
  - Rừng ngẫu nhiên (Random Forest) dự báo tắc nghẽn màng trong trạm AnMBR đạt $R^2 = 0.906$ [69].
  - Hệ suy luận mờ thích ứng nơ-ron (ANFIS) dự báo lưu lượng nước thấm trong MBR thẩm thấu đạt $R^2 = 0.9755 - 0.9861$ [70].
- Nghiên cứu triển khai Extra Trees trên hệ thống MBR công nghiệp quy mô $1125\text{ m}^3/\text{h}$ với $4593\text{ giờ}$ SCADA thực tế. Nguồn thải bán dẫn có biến động tải lượng rất lớn.
- Mô hình giải quyết đồng thời ba biến đầu ra phụ thuộc lẫn nhau, phản ánh chân thực động lực học vận hành thực tế.

#### Tác động của cấu trúc phân vùng dữ liệu lên độ chính xác
- Dưới thiết kế phân vùng ngẫu nhiên (Random Partition) tương đương các nghiên cứu trước, Extra Trees đạt độ chính xác cao:
  - Áp suất hút xuyên màng TMP đạt $R^2 = 0.988$.
  - Lưu lượng nước thấm qua màng đạt $R^2 = 0.933$.
  - Mức chất lỏng bể chứa màng đạt $R^2 = 0.908$.
- Dưới thiết kế phân vùng khối 24 giờ (24-h Blocked Partition) nhằm loại bỏ rò rỉ dữ liệu do tự tương quan chuỗi thời gian:
  - TMP đạt $R^2 = 0.830$.
  - Lưu lượng nước thấm đạt $R^2 = 0.788$.
  - Mức chất lỏng bể màng đạt $R^2 = 0.564$.
- Việc công bố song song cả hai sơ đồ phân vùng đảm bảo tính minh bạch học thuật khi so sánh với tài liệu tiền nhiệm. Mô hình tập hợp Extra Trees đạt hiệu năng xuất sắc trên ba mục tiêu mà không chịu gánh nặng tính toán lớn của mạng nơ-ron tái hồi RNN/LSTM.

---

### 3.4.2. Tiếp cận tối ưu hóa

#### Khác biệt giữa tối ưu hóa tham số mô hình và tối ưu hóa vận hành
- Phần lớn tài liệu MBR học máy dùng thuật ngữ "tối ưu hóa" để chỉ việc tinh chỉnh siêu tham số mô hình hoặc tìm kiếm kiến trúc mạng (AutoML).
- Nghiên cứu [71] từng áp dụng thuật toán di truyền (GA) để tìm điều kiện vận hành. Tuy nhiên công trình đó chỉ giải quyết bài toán đơn mục tiêu nhằm giảm tắc màng.
- Đây là nghiên cứu đầu tiên tối ưu hóa điều kiện vận hành đa mục tiêu trên đa tạp dữ liệu thực tế cho MBR. Phương pháp đáp ứng đồng thời cả ba tiêu chuẩn hiệu suất.

#### Bản đồ xác suất liên tục so với thuật toán tối ưu hóa điểm đơn lẻ
- Thuật toán GA hoặc tối ưu hóa bầy đàn (PSO) truyền thống chỉ tìm ra một điểm vận hành đơn lẻ mang tính cục bộ. Điểm này rất nhạy cảm với sai số mô hình và không cung cấp biên độ dung sai an toàn.
- Phương pháp lập bản đồ vùng vận hành khả thi tạo ra bề mặt xác suất có điều kiện liên tục trên $207{,}238$ trạng thái thực tế.
- Bề mặt xác suất giúp người vận hành nhận diện các vùng có khả năng chống chịu cao trước các biến động tải lượng thường nhật.
- Không gian khả thi cần được lấy mẫu trên đa tạp kết hợp thực tế thay vì quét độc lập từng chiều biên. Khuyến nghị vận hành phải được xếp hạng theo tỷ lệ đạt mục tiêu có điều kiện thay vì mật độ mẫu.

#### Phân biệt ranh giới khả thi kỹ thuật và vùng lõi đạt mục tiêu cao
- Ranh giới khả thi toán học rộng hơn rất nhiều so với vùng vận hành an toàn thực tế:
  - Vùng bao khả thi của SRT mở rộng tới trên $95\text{ ngày}$, nhưng tỷ lệ đạt mục tiêu thực tế trên $87\text{ ngày}$ giảm xuống dưới $20\%$.
  - Vùng bao khả thi của HRT kéo dài đến $7.65\text{ h}$, nhưng tỷ lệ đạt mục tiêu thực tế trên $7.95\text{ h}$ rơi về $0\%$.
  - Vùng bao khả thi của F/M kéo dài đến $0.037\text{ ngày}^{-1}$, nhưng tỷ lệ đạt mục tiêu thực tế trên ngưỡng này chỉ còn $15.0\%$.
- Phân tích thỏa mãn ràng buộc thông thường dễ hướng người vận hành đến các điểm biên có rủi ro vi phạm cao. Việc xếp hạng theo tỷ lệ đạt mục tiêu thiết lập ranh giới an toàn thực chất, bảo vệ hệ thống trước sự cố công nghệ.

---

### 3.4.3. Triển vọng và chiến lược tương lai

#### Khả năng chuyển giao công nghệ và giá trị thực tiễn
- Mô hình huấn luyện trên dữ liệu SCADA lịch sử hỗ trợ chỉ dẫn vận hành trực tiếp. Trạm không cần phân tích hóa lý bổ sung trong phòng thí nghiệm.
- Khung phân tích SHAP hai ngữ cảnh so sánh toàn bộ dữ liệu với vùng khả thi. Phương pháp này giúp phát hiện các biến điều khiển phản ứng nhanh cho quy trình công nghiệp đa đầu ra.
- Quy trình vận hành được xếp hạng theo bằng chứng thực nghiệm rõ ràng. Mỗi khuyến nghị đều đi kèm tỷ lệ đạt mục tiêu thực tế và chứng minh hiệu quả trên tập dữ liệu giữ lại độc lập.

#### Ranh giới áp dụng và định hướng phát triển thực nghiệm
- Nghiên cứu xác lập bốn ranh giới kỹ thuật cần lưu ý:
  - **Bản chất dữ liệu**: Kết quả dựa trên dữ liệu quan sát SCADA lịch sử, chưa qua thử nghiệm đối chứng ngẫu nhiên (Randomized Controlled Trial).
  - **Tính đặc thù trạm**: Mô hình xây dựng cho một nhà máy duy nhất với cấu hình màng sợi rỗng PVDF UF. Phương pháp luận có thể chuyển giao toàn diện, nhưng các dải số định lượng cần hiệu chỉnh theo từng trạm.
  - **Miền nội suy đa tạp**: Mô hình chỉ hoạt động tin cậy trong không gian dữ liệu trạm từng trải qua. Cần bổ sung các biến đầu vào triển vọng gồm tuổi thọ màng, lịch sử rửa hóa chất CIP và độ dẫn điện dòng thải.
  - **Bản chất của SHAP**: Giá trị SHAP định lượng mối liên kết thống kê trên phân phối dữ liệu, không chứng minh quan hệ nhân quả vật lý tuyệt đối. Việc xác nhận cơ chế đòi hỏi mổ xẻ màng (autopsy), đo thế zeta và phân đoạn hữu cơ dịch lọc.
- Định hướng tiếp theo: Triển khai thử nghiệm lâm sàng luân phiên chiến lược điều khiển giữa hai nhánh màng UF song song có chung nước đầu vào. Tích hợp mô hình vào Bản sao số (Digital Twin) và Hệ thống hỗ trợ ra quyết định thời gian thực (Real-time DSS).

---

## 4. Kết luận (Conclusion)

### 4.1. Đóng góp cốt lõi của khung AI giải thích được
- Nghiên cứu xây dựng khung AI giải thích đa mô hình đầu tiên cho trạm MBR bán dẫn quy mô $1125\text{ m}^3/\text{h}$. Khung AI định nghĩa thành công không gian vận hành tối ưu.
- Extra Trees đạt độ chính xác và tính ổn định cao trên cả ba biến mục tiêu phụ thuộc lẫn nhau. Kết quả gồm TMP ($R^2 = 0.988$), lưu lượng thấm ($R^2 = 0.933$) và mức bể màng ($R^2 = 0.908$).
- Phân vùng khối 24 giờ chứng minh năng lực tổng quát hóa của Extra Trees. Thuật toán khắc phục triệt để hiện tượng tự tương quan chuỗi thời gian công nghiệp.

### 4.2. Khám phá cơ chế vật lý và ý nghĩa thực tiễn cho vận hành MBR
- **Cơ chế tắc màng đơn điệu của SRT trong chế độ hiếu khí kéo dài**: 16 thuật toán SHAP xác nhận tăng SRT làm tích tụ sinh khối trơ. Quá trình này làm tăng độ nhớt bùn và nén chặt bánh bùn ($R^2 = 0.988$). Kết quả bác bỏ quan niệm truyền thống cho rằng tuổi bùn cao giúp giảm tắc nghẽn màng.
- **Xác lập bản đồ không gian khả thi trên đa tạp dữ liệu thực nghiệm**: Phương pháp xác lập dải thông số vận hành hành động được. Việc tuân thủ dải khuyến nghị nâng tỷ lệ đạt mục tiêu từ mức nền $37.1\%$ lên tới $82.4\%$.
- **Kiểm chứng độc lập trên dữ liệu tương lai giữ lại**: Tỷ lệ đạt mục tiêu thực tế trong cửa sổ đạt $61.9\%$ so với $39.3\%$ ngoài cửa sổ. Tỷ số chênh lệch đạt $\text{Odds Ratio} = 3.89$ ($p < 0.001$).
- **Duy trì độ chính xác ngoại suy dài hạn**: Tái huấn luyện mô hình hàng ngày duy trì sai số dự báo TMP trong phạm vi $\pm 0.008\text{ bar}$. Hệ số xác định đạt $R^2 = 0.871$ sau 4 tháng kiểm định ngoại suy liên tục.
- **Chuyển dịch tư duy quản lý màng**: Khung phương pháp luận ưu tiên tính giải thích quy trình. Bản đồ khả thi phân tầng thực nghiệm thay thế việc chỉ theo đuổi độ chính xác danh nghĩa trên dữ liệu tự tương quan.
