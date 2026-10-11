### 2.2. Dataset preprocessing

* **Quy mô và nguồn gốc bộ dữ liệu thực nghiệm**:
  * Bộ dữ liệu được thiết lập dựa trên $525\text{ ngày}$ vận hành dài hạn của hệ thống bể phản ứng sinh học màng kỵ khí quy mô pilot lớn (pilot-scale anaerobic membrane bioreactor - AnMBR) xử lý nước thải đô thị thực (real municipal wastewater).
  * Toàn bộ các mô hình học máy đều sử dụng $7\text{ đặc trưng đầu vào}$ (input features) bao gồm:
    * Tải trọng hữu cơ của AnMBR (organic load rate - OLR).
    * Nồng độ chất rắn lơ lửng trong nước thải đầu vào (suspended solids in the influent - SS).
    * Nồng độ protein ($\text{EPS}_p$) trong các chất polyme ngoại bào (extracellular polymeric substances - EPS) của bùn.
    * Nồng độ polysaccharide ($\text{EPS}_c$) trong EPS của bùn.
    * Nồng độ chất rắn lơ lửng trong hỗn hợp bùn (mixed liquor-suspended solids - MLSS).
    * Nhiệt độ của bể phản ứng sinh học (bioreactor temperature - Temp).
    * Thông lượng lọc của màng (flux).
  * Biến mục tiêu đầu ra (target output) của các mạng nơ-ron: Áp suất xuyên màng (transmembrane pressure - TMP).

* **Tần suất thu thập dữ liệu và phương pháp xử lý dữ liệu khuyết thiếu (Missing Data Imputation)**:
  * Tần suất lấy mẫu không đồng bộ giữa các thông số:
    * Dữ liệu nhiệt độ (Temp) và thông lượng (flux) được thu thập hàng ngày (daily).
    * Các biến số còn lại (OLR, influent SS, $\text{EPS}_p$, $\text{EPS}_c$, MLSS) được lấy mẫu và đo đạc định kỳ mỗi $2\text{ ngày}$ ($2\text{ days}$).
  * Phương pháp gán quan sát cuối cùng về phía trước (last observation carried forward - LOCF):
    * Phương pháp gán giá trị LOCF được sử dụng để xử lý dữ liệu bị khuyết thiếu phát sinh do quá trình thu thập dữ liệu bất đồng bộ (asynchronous data gathering).
    * Nguyên lý LOCF: Đây là chiến lược tiêu chuẩn để xử lý dữ liệu khuyết trong các nghiên cứu theo thời gian hoặc chuỗi thời gian (longitudinal or time-series studies); khi một điểm dữ liệu trong một khoảng thời gian nhất định bị khuyết, giá trị quan sát gần nhất trước đó sẽ được điền vào để lấp khoảng trống (Woolley et al., 2009).

* **Phân bố thống kê của bộ dữ liệu (Dataset Distribution)**:
  * Sự phân bố của các đặc trưng đầu vào và biến mục tiêu đầu ra được trình bày chi tiết trong Bảng 2:
    * Tải trọng hữu cơ OLR: giá trị cực đại $2.04\text{ g/(L}\cdot\text{d)}$, cực tiểu $0.11\text{ g/(L}\cdot\text{d)}$, trung bình $0.90\text{ g/(L}\cdot\text{d)}$, độ lệch chuẩn $\text{STD} = 0.51\text{ g/(L}\cdot\text{d)}$.
    * Chất rắn lơ lửng dòng vào SS: cực đại $478.00\text{ mg/L}$, cực tiểu $128.00\text{ mg/L}$, trung bình $223.51\text{ mg/L}$, $\text{STD} = 42.58\text{ mg/L}$.
    * Nồng độ protein trong EPS bùn ($\text{EPS}_p$): cực đại $136.33\text{ mg/g VSS}$, cực tiểu $32.82\text{ mg/g VSS}$, trung bình $57.13\text{ mg/g VSS}$, $\text{STD} = 21.56\text{ mg/g VSS}$.
    * Nồng độ polysaccharide trong EPS bùn ($\text{EPS}_c$): cực đại $124.18\text{ mg/g VSS}$, cực tiểu $9.00\text{ mg/g VSS}$, trung bình $16.41\text{ mg/g VSS}$, $\text{STD} = 13.60\text{ mg/g VSS}$.
    * Nồng độ MLSS: cực đại $15.28\text{ mg/L}$, cực tiểu $5.62\text{ mg/L}$, trung bình $9.22\text{ mg/L}$, $\text{STD} = 2.03\text{ mg/L}$ (ghi chú theo nguyên văn bảng; tương đương $5.62 - 15.28\text{ g/L}$ trong bùn kỵ khí).
    * Nhiệt độ bể phản ứng Temp: cực đại $28.20^\circ\text{C}$, cực tiểu $16.10^\circ\text{C}$, trung bình $24.89^\circ\text{C}$, $\text{STD} = 2.55^\circ\text{C}$.
    * Thông lượng lọc Flux: cực đại $17.83\text{ LMH}$, cực tiểu $2.08\text{ LMH}$, trung bình $9.36\text{ LMH}$, $\text{STD} = 4.44\text{ LMH}$.
    * Biến mục tiêu TMP: giá trị cực đại $25.61\text{ kPa}$, cực tiểu $0.15\text{ kPa}$, trung bình $6.57\text{ kPa}$, và độ lệch chuẩn $\text{STD} = 6.24\text{ kPa}$.
  * **Bảng 2.** Phân bố tập dữ liệu huấn luyện và kiểm thử mô hình.
    * <img src="assets/table_02_p4.png" alt="Bảng 2" />
    * **Bảng này chứng minh điều gì**
      * Thống kê mô tả đầy đủ miền giá trị (Max, Min, Average, STD) của 7 biến đặc trưng đầu vào và biến mục tiêu TMP trong suốt 525 ngày vận hành AnMBR pilot.
    * **Từ đâu mà thấy được**
      * Cột Features gồm 7 thông số vận hành và hóa sinh; cột Target là áp suất qua màng TMP.
      * Các hàng Min, Max, Average và STD xác định khoảng biến thiên và độ lệch chuẩn của từng biến số.

* **Phân chia tập dữ liệu và xáo trộn ngẫu nhiên (Data Partitioning & Shuffling)**:
  * Tỷ lệ phân chia tập dữ liệu: Bộ dữ liệu được phân chia ngẫu nhiên thành tập huấn luyện (training set) và tập kiểm thử (test set) theo tỷ lệ $9:1$ ($90\%$ dành cho huấn luyện và $10\%$ dành cho kiểm thử) (Zhu et al., 2023).
  * Mục đích xáo trộn dữ liệu (shuffling data) và loại bỏ tính tuần tự:
    * Dù dữ liệu gốc mang đặc tính chuỗi thời gian (temporal characteristics), mục tiêu trọng tâm của nghiên cứu là so sánh hiệu năng giữa mô hình Perceptron đa lớp (multilayer perceptron - MLP) và Mạng bộ nhớ ngắn-dài hạn (long short-term memory - LSTM) trong bối cảnh phi tuần tự (non-sequential context).
    * Thông qua thao tác xáo trộn ngẫu nhiên dữ liệu, việc phân chia chuyển đổi tính chất từ một bộ dữ liệu chuỗi thời gian sang một bộ dữ liệu tổng quát (general dataset).
    * Lợi ích kép của thao tác xáo trộn:
      * Nâng cao khả năng tổng quát hóa của mô hình (improved model generalization).
      * Giải quyết triệt để mối lo ngại về rò rỉ dữ liệu tiềm ẩn (addressed potential data leakage concerns), do thứ tự thời gian không còn là một yếu tố can thiệp sau khi dữ liệu đã được xáo trộn.

* **Chuẩn hóa đặc trưng đầu vào (Input Feature Normalization / Standardization)**:
  * Vai trò của chuẩn hóa đối với mô hình mạng nơ-ron:
    * Chuẩn hóa hoặc tiêu chuẩn hóa các đặc trưng đầu vào mang lại lợi ích thiết thực cho các mô hình học máy, đặc biệt là mạng nơ-ron nhân tạo (neural networks).
    * Nếu không chuẩn hóa đầu vào, các thuật toán tối ưu hóa như phương pháp hạ gradient (gradient descent) có thể gặp khó khăn trong việc đạt tới sự hội tụ do hành vi dao động (oscillatory behavior) của gradient, đặc biệt khi thang đo của các đặc trưng có sự biến thiên lớn.
    * Mặc dù trong một số thuật toán học máy nhất định, chênh lệch lớn về miền giá trị số học có thể khiến các biến có thang đo lớn hơn gây ảnh hưởng bất cân xứng lên mô hình (Ozsahin et al., 2022), mục tiêu chủ đạo của việc chuẩn hóa trong các mô hình mạng nơ-ron của nghiên cứu này là thúc đẩy sự hội tụ hiệu quả và ổn định trong suốt quá trình huấn luyện (promote efficient and stable convergence during training).
  * Tính tương thích với các kỹ thuật điều chuẩn (Regularization):
    * Tầm quan trọng của việc đồng nhất thang đo đặc trưng càng tăng lên rõ rệt khi áp dụng các kỹ thuật điều chuẩn (regularization techniques).
    * Thang đo nhất quán đảm bảo trọng số (weight) của không có bất kỳ đặc trưng nào bị phạt (unfairly penalized) một cách không công bằng chỉ do thang đo số học ban đầu của đặc trưng đó.
  * Hàm tiêu chuẩn hóa (Standardization Function) - Công thức (1):
    * Phương pháp chuẩn hóa được sử dụng để giải quyết vấn đề thang đo và tạo điều kiện thuận lợi cho việc so sánh, phân tích các đặc trưng:
      $$X_{\text{standardized}} = \frac{X - \mu}{\sigma} \quad (1)$$
    * Trong đó:
      * $X$ là giá trị đặc trưng ban đầu (original features).
      * $\mu$ là giá trị trung bình (mean) của đặc trưng.
      * $\sigma$ là độ lệch chuẩn (standard deviation) của đặc trưng.
    * Thuộc tính sau chuẩn hóa: Sau khi tiêu chuẩn hóa, các đặc trưng đều có giá trị trung bình xấp xỉ $0$ ($\mu \approx 0$) và độ lệch chuẩn xấp xỉ $1$ ($\sigma \approx 1$).
    * Tác động bảo toàn phân bố: Phép biến đổi này tối ưu hóa hiệu năng của các mô hình học máy mà vẫn duy trì nguyên vẹn hình dạng phân bố ban đầu (original distribution shape) của các đặc trưng.
  * Môi trường và công cụ hiện thực hóa:
    * Quá trình tiêu chuẩn hóa được thực hiện bằng công cụ `StandardScaler` thuộc thư viện học máy Scikit-learn dành cho ngôn ngữ lập trình Python (phiên bản `3.9.16`).
