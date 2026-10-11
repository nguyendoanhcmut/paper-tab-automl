### 3.1. AnMBR performance

* Đánh giá hiệu năng của hệ thống AnMBR quy mô pilot lớn (large pilot-scale AnMBR) trong xử lý nước thải sinh hoạt đô thị (municipal wastewater) suốt quá trình vận hành dài hạn (long-term operation):
  * **Điều kiện vận hành và biến thiên tải trọng**:
    * Thời gian lưu nước thủy lực (hydraulic retention time - HRT) được rút ngắn định kỳ qua các mức: $48\text{ h} \rightarrow 24\text{ h} \rightarrow 12\text{ h} \rightarrow 8\text{ h} \rightarrow 6\text{ h}$.
    * Nhiệt độ vận hành được ổn định ở ba pha tương ứng xấp xỉ $25\ ^\circ\text{C}$, $20\ ^\circ\text{C}$, và $15\ ^\circ\text{C}$.
    * Tải trọng hữu cơ (organic loading rate - OLR) của AnMBR dao động trong dải từ $0{,}11$ đến $2{,}04\text{ g/L/d}$.
    * Nồng độ chất rắn lơ lửng đầu vào (influent SS concentration) dao động từ $128$ đến $478\text{ mg/L}$.
    * Các dao động nồng độ đầu vào phản ánh điều kiện thực tế khi triển khai, chứng minh tính khả thi của hệ thống AnMBR trong việc chống chịu và thích ứng với biến thiên OLR.
* Hiệu suất xử lý và loại bỏ COD (chemical oxygen demand - nhu cầu oxy hóa học):
  * Hiệu suất loại bỏ COD (COD removal efficiency) đạt trên $90\%$ ở nhiệt độ $25\ ^\circ\text{C}$ và $20\ ^\circ\text{C}$.
  * Hiệu suất loại bỏ COD duy trì ở mức $85\%$ khi nhiệt độ giảm xuống $15\ ^\circ\text{C}$.
  * Nồng độ COD dòng ra (effluent COD concentration) duy trì dưới $50\text{ mg/L}$ ở cả ba giai đoạn nhiệt độ vận hành.
  * Toàn bộ hiệu suất xử lý của hệ thống AnMBR được thể hiện trong Table 1.
* Sản lượng khí sinh học (biogas production) và thu hồi năng lượng (energy recovery):
  * Tốc độ sinh biogas (biogas production rate) đạt $0{,}06 - 0{,}10\text{ L/L}$ nước thải thô (raw wastewater).
  * Suất sinh biogas theo tải lượng hữu cơ phân hủy đạt $0{,}16 - 0{,}27\text{ L/g}$ COD bị loại bỏ (removed COD) trong suốt giai đoạn vận hành ổn định.
  * Tỷ lệ phần trăm $\text{CH}_4$ trong biogas sinh ra được duy trì ở mức $76\% - 79\%$.
  * Các chỉ số trên chứng minh hệ thống AnMBR đạt khả năng thu hồi năng lượng thỏa đáng (satisfactory energy recovery) (Sun et al., 2015).
* Động thái áp suất xuyên màng (transmembrane pressure - TMP) và cơ chế tắc nghẽn màng (membrane fouling):
  * Trong giai đoạn HRT $48 - 8\text{ h}$ ở nhiệt độ $25\ ^\circ\text{C}$ và $20\ ^\circ\text{C}$, giá trị TMP tương đối ổn định và duy trì dưới $10\text{ kPa}$ với thông lượng (flux) từ $2$ đến $15\text{ LMH}$.
  * Khi nồng độ chất rắn lơ lửng trong hỗn dịch bùn (mixed liquor suspended solids - MLSS) tiếp tục tăng dần do HRT bị rút ngắn xuống $6\text{ h}$ kết hợp nhiệt độ vận hành hạ xuống $15\ ^\circ\text{C}$, TMP tăng vọt vượt ngưỡng $25\text{ kPa}$ ở mức thông lượng $17{,}83\text{ LMH}$.
  * Ảnh hưởng của MLSS lên hiện tượng tắc nghẽn màng bị khuếch đại (magnified) khi HRT bị rút ngắn (Kong et al., 2021a).
  * Biến thiên nồng độ chất polyme ngoại bào (extracellular polymeric substances - EPS) của bùn làm trầm trọng thêm mức độ tắc nghẽn màng khi nhiệt độ môi trường giảm thấp (Rong et al., 2022a).
* Ý nghĩa đối với việc xây dựng tập dữ liệu huấn luyện mô hình (dataset construction):
  * Mô hình phát triển trong nghiên cứu chứa đựng nhiều biến thiên điều kiện vận hành qua giai đoạn kéo dài.
  * Bộ dữ liệu bao hàm đầy đủ hiệu năng màng ở cả giai đoạn ổn định (stable stage) và giai đoạn tắc nghẽn màng (fouling stage).
  * Nhờ đó, tập dữ liệu có tính khái quát (generality) cao hơn đáng kể so với các nghiên cứu ngắn hạn có ít biến động về điều kiện vận hành.
