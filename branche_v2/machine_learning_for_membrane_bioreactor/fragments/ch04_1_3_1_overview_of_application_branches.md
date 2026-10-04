### 3.1 Overview of application

- **Xu hướng phát triển và trọng tâm nghiên cứu của mô hình học máy trong hệ thống MBR**: Kể từ năm 2015, số lượng nghiên cứu công bố về mô hình học máy (machine learning) – một công nghệ trí tuệ nhân tạo (artificial intelligence - AI) – trong hệ thống bể phản ứng sinh học màng (Membrane Bioreactor - MBR) gia tăng rõ rệt và tăng trưởng mạnh mẽ sau năm 2018 (Fig. S1 trong Appendix A):
  - Phân tích thống kê về mô hình, đặc trưng (features) và thuật toán tối ưu hóa (optimization) phản ánh chi tiết tiến trình nghiên cứu trong bài toán dự đoán hiệu suất MBR.
  - Tỷ lệ các công trình nghiên cứu tập trung vào dự đoán tắc nghẽn màng (membrane fouling) chiếm $67.1\%$.
  - Tỷ lệ các công trình nghiên cứu tập trung vào dự đoán hiệu quả loại bỏ chất ô nhiễm (pollutant removal) chiếm $34.3\%$.

- **Phân loại bảy nhóm đặc trưng thông số quy trình màng làm biến đầu vào mô hình**: Các đặc tính và thông số kỹ thuật của quy trình màng được phân loại thành bảy nhóm chính để làm biến đầu vào cho mô hình (model inputs):
  - Thông số thời gian ($t$ - time parameter).
  - Nhóm chỉ số nồng độ truyền thống (conventional concentration indices - CCI): bao gồm nhu cầu oxy hóa học (chemical oxygen demand - COD), tổng nitơ (total nitrogen - TN), và tổng phốt pho (total phosphorus - TP) trong dòng vào (influent) và dòng ra (effluent); tổng chất rắn lơ lửng trong dòng vào (influent TSS); chất rắn lơ lửng trong bùn lỏng (mixed liquor suspended solids - MLSS), cùng các thông số liên quan khác.
  - Nhóm chỉ số lọc màng (membrane filtration indices - MFI): bao gồm áp suất xuyên màng (transmembrane pressure - TMP), thông lượng màng (membrane flux), trở lực lọc (filtration resistance), tốc độ biến thiên áp suất xuyên màng theo thời gian ($\Delta\text{TMP}/\Delta t$), độ thấm màng (membrane permeability), cùng các thông số khác.
  - Nhóm chỉ số môi trường (environment indices - EI): bao gồm nhiệt độ ($T$), oxy hòa tan (dissolved oxygen - DO), $\text{pH}$, thế oxy hóa khử (oxidation reduction potential - ORP), tốc độ tải nạp hữu cơ (organic loading rate - OLR), cùng các thông số môi trường liên quan.
  - Nhóm chỉ số vận hành (operation indices - OI): bao gồm thời gian lưu bùn (solids retention time - SRT), thời gian lưu thủy lực (hydraulic retention time - HRT), tỷ lệ lọc - gián đoạn / thư giãn (filtration-relaxation ratio), cường độ sục khí (aeration intensity), cường độ/thời gian rửa ngược (backwash strength/time), cùng các thông số vận hành khác.
  - Nhóm chỉ số chất gây tắc nghẽn đặc trưng (characteristic foulant indices - CFI): bao gồm nồng độ các sản phẩm vi sinh vật hòa tan (soluble microbial products - SMP), chất polyme ngoại bào liên kết lỏng lẻo (loosely-bound extracellular polymeric substances - loosely-bound EPS), và chất polyme ngoại bào liên kết chặt chẽ (tightly-bound EPS).
  - Dữ liệu đo quang phổ (spectroscopic measurement results): bao gồm dữ liệu phổ (spectral data) và bản đồ ảnh xám phổ (spectral grayscale maps) được sử dụng làm đầu vào mô hình nhằm hỗ trợ tự động trích xuất đặc trưng phổ (automatic spectral features extraction).
  - Các thông số đặc tính bổ trợ khác: kích thước hạt bùn (sludge particle size), độ nhớt (viscosity), thế điện động zeta (zeta potential), hệ số gây bít tắc (blocking coefficient), kích thước lỗ màng (membrane pore size), v.v.
  - Biến đầu ra mô hình (model outputs): từ các đặc trưng đầu vào kể trên, các mô hình học máy thường xuất ra kết quả dự đoán về hiệu suất loại bỏ chất ô nhiễm và hiệu suất tắc nghẽn màng.

- **Đặc tính mô hình hóa dự đoán tắc nghẽn màng và loại bỏ chất ô nhiễm trong MBR (Figure 5)**: Nghiên cứu thống kê cấu trúc dữ liệu đầu vào, kiến trúc thuật toán học máy, phương pháp tối ưu hóa siêu tham số và chỉ số đầu ra mục tiêu giữa bài toán dự đoán tắc nghẽn màng và bài toán dự đoán loại bỏ chất ô nhiễm:
  - **Figure 5: MBR machine learning application overview**
    - ![Figure 5](assets/fig_05_p12.jpeg)
    - **Hình này chứng minh điều gì**
      - Thống kê tỷ lệ phân bố biến đầu vào, cấu trúc giải thuật, tối ưu hóa và chỉ số đầu ra giữa bài toán tắc nghẽn màng (a) và xử lý chất ô nhiễm (b).
      - Mạng nơ-ron ANN (đặc biệt là MLP) chiếm tỷ trọng áp đảo ở cả hai nhóm; mô hình tắc nghẽn màng có cấu trúc đa dạng và áp dụng nhiều giải thuật tối ưu hơn.
    - **Từ đâu mà thấy được**
      - Panel (a) Dự đoán tắc nghẽn màng: đầu vào chủ đạo MFI ($68.8\%$) và CCI ($60.4\%$); ANN ($72.9\%$); tối ưu hóa gồm không tối ưu ($56.3\%$), thuật toán thông minh ($33.3\%$); đầu ra chủ yếu là Flux ($52.7\%$).
      - Panel (b) Dự đoán xử lý chất ô nhiễm: đầu vào chủ đạo CCI ($79.2\%$), OI ($62.5\%$), EI ($54.2\%$); MLP ($66.7\%$); không tối ưu ($75\%$); đầu ra tập trung vào C ($79.2\%$), N ($58.3\%$), P ($37.5\%$).
      - Lưu ý: hình ghi $79.2\%$, văn bản ghi $75.2\%$ cho tỷ lệ đầu vào CCI trong mô hình dự đoán loại bỏ chất ô nhiễm ở panel (b).
  - Đặc tính của mô hình dự đoán tắc nghẽn màng MBR (Figure 5a):
    - Nhóm đặc trưng đầu vào chiếm tỷ trọng cao nhất là MFI ($68.8\%$) và CCI ($60.4\%$).
    - Thông lượng màng (membrane flux) được chọn làm chỉ số đại diện hàng đầu cho hiệu suất tắc nghẽn màng với tỷ lệ $52.7\%$ (theo sau là TMP với $14.6\%$, độ thấm permeability với $12.7\%$, trở lực resistance với $7.23\%$, dạng tắc nghẽn type of fouling với $3.6\%$, năng lượng tương tác interfacial energy với $3.6\%$, phục hồi thông lượng flux recovery với $1.8\%$, tuổi thọ màng membrane life với $1.8\%$, và tiêu thụ năng lượng energy consumption với $1.8\%$).
    - Mô hình mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) chiếm $72.9\%$ tổng số mô hình được thiết lập, tập trung chủ yếu vào các cấu trúc tương đối đơn giản gồm mạng Perceptron đa tầng (Multilayer Perceptron - MLP) chiếm $39.6\%$ và mạng nơ-ron hàm cơ sở xuyên tâm (Radial Basis Function Neural Network - RBFNN) chiếm $18.8\%$.
    - Mạng nơ-ron sâu (Deep Neural Network - DNN) và máy vector hỗ trợ (Support Vector Machine - SVM) lần lượt chiếm tỷ lệ $8.3\%$ và $18.8\%$; các mô hình còn lại gồm mô hình cây (tree model) chiếm $6.3\%$, mạng Elman (ENN) chiếm $4.2\%$, mạng nơ-ron wavelet (WNN) chiếm $2.1\%$, và học không giám sát (unsupervised learning) chiếm $2.1\%$.
    - Về tối ưu hóa và tinh chỉnh mô hình (model tuning): hơn một nửa số mô hình ($56.3\%$) không áp dụng thuật toán tối ưu hóa nào, $33.3\%$ lựa chọn thuật toán tối ưu hóa thông minh (intelligent optimization algorithms), và $8.3\%$ áp dụng kiểm định chéo (Cross-Validation - CV) đơn giản để tối ưu hóa tham số.
    - Trong nhóm thuật toán tối ưu hóa thông minh, giải thuật di truyền (Genetic Algorithm - GA) chiếm ưu thế với $56.5\%$ (chiếm $18.8\%$ tổng thể), tiếp theo là tối ưu hóa bầy đàn (Particle Swarm Optimization - PSO) với $18.9\%$ (chiếm $6.3\%$ tổng thể); các thuật toán khác gồm tối ưu hóa lai (hybrid optimization) chiếm $4.2\%$, ủ mô phỏng (Simulated Annealing - SA) chiếm $2.1\%$, thuật toán bầy dơi (Bat algorithm) chiếm $2.1\%$, và tối ưu hóa thích nghi (adaptive optimization) chiếm $2.1\%$.
  - Đặc tính của mô hình dự đoán hiệu quả loại bỏ chất ô nhiễm trong MBR (Figure 5b):
    - Biến đầu vào hoàn toàn không sử dụng nhóm chỉ số chất gây tắc nghẽn đặc trưng CFI ($0\%$).
    - Phần lớn mô hình sử dụng các nhóm đặc trưng đầu vào gồm CCI chiếm $75.2\%$ (hình ghi $79.2\%$), OI chiếm $62.5\%$, và EI chiếm $54.2\%$; chỉ có $20.8\%$ số mô hình tích hợp nhóm chỉ số MFI vào đặc trưng đầu vào (thời gian $t$ chiếm $4.2\%$, các biến khác chiếm $20.8\%$).
    - Về chỉ số đầu ra mục tiêu: $79.2\%$ mô hình hướng đến dự đoán các chỉ số liên quan đến carbon cốt lõi (như COD dòng ra và tỷ lệ loại bỏ COD); các chỉ số liên quan đến nitơ (tỷ lệ loại bỏ và nồng độ dòng ra của TN, $\text{NH}_3\text{-N}$, $\text{NO}_3^-\text{-N}$) theo sau với $58.3\%$; chỉ số liên quan đến phốt pho (P) chiếm $37.5\%$; chỉ có $16.7\%$ mô hình dự đoán các chất ô nhiễm hữu cơ dạng vết (trace organic pollutants); các chỉ số khác chiếm $16.7\%$.
    - Về cấu trúc mô hình: tỷ lệ đáng kể các mô hình sử dụng họ ANN, trong đó MLP là lựa chọn phổ biến nhất với $66.7\%$ (WNN chiếm $12.5\%$, RBFNN chiếm $8.3\%$, DNN chiếm $8.3\%$, và tree model chiếm $4.2\%$).
    - So với bài toán dự đoán tắc nghẽn màng, các mô hình dự đoán loại bỏ chất ô nhiễm thường có cấu trúc đơn giản hơn, với tỷ lệ áp dụng thuật toán tối ưu hóa thấp hơn ($75\%$ không dùng thuật toán tối ưu hóa, GA chiếm $12.5\%$, và CV chiếm $12.5\%$).

- **Mối tương quan giữa dung lượng mô hình, độ ổn định và số lượng tham số trong các mô hình ANN**: Phân tích mối quan hệ giữa hệ số xác định ($R^2$) và số lượng tham số trong các mô hình ANN khác nhau cho thấy dung lượng mô hình (model's capacity) được phản ánh trực tiếp qua số lượng tham số (Fig. S2 trong Appendix A):
  - Độ ổn định của mô hình MLP kém hơn, chịu ảnh hưởng tiềm tàng từ đặc tính tập dữ liệu hoặc cấu hình thiết lập tham số mô hình.
  - Việc đưa vào các thuật toán tối ưu hóa như GA giúp cải thiện hiệu suất chung của mô hình, có khả năng bắt nguồn từ tối ưu hóa thuật toán hoặc sự tinh chỉnh quy trình huấn luyện tham số.
  - Mô hình mạng nơ-ron wavelet (WNN) đạt kết quả khả quan với số lượng tham số khiêm tốn, nhiều khả năng nhờ vào việc xây dựng hàm kích hoạt phức tạp hơn (more complex activation function).

- **Đánh giá tổng thể và bốn giới hạn cốt lõi của công nghệ học máy trong hệ thống MBR**: Học máy là công cụ thịnh hành và đạt hiệu suất thỏa đáng trong các ứng dụng MBR, song cần nhìn nhận bốn hạn chế kỹ thuật chính:
  - Hệ thống chỉ số chưa đầy đủ (incomplete indicator system).
  - Thiếu hụt kiểm chứng trên công trình kỹ thuật quy mô thực tế (lack of full-scale engineering validation).
  - Khó khăn trong việc triển khai dự đoán theo thời gian thực (difficulty of real-time prediction).
  - Chưa đóng góp vào việc nâng cao hiểu biết sâu sắc về bản chất cơ chế quy trình (lack of process understanding contribution).
