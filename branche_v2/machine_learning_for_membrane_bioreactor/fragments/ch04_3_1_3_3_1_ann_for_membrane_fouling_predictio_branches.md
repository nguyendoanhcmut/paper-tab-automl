#### 3.3.1 ANN for membrane fouling prediction

- **Đặc tính mô hình và phân loại bài toán dự đoán tắc nghẽn màng (membrane fouling prediction)**: Mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) là mô hình học máy với năng lực khớp phi tuyến mạnh mẽ (strong nonlinear fitting capabilities), thể hiện hiệu suất tốt trong dự đoán tắc nghẽn màng:
  - Bài toán dự đoán tắc nghẽn màng được phân thành hai nhóm chính:
    - Dự đoán trạng thái lọc (filtration state prediction): bao gồm các biến trạng thái vận hành như thông lượng dòng thấm (flux), áp suất xuyên màng (Transmembrane Pressure - TMP), và độ thấm của màng (permeability).
    - Phân tích tắc nghẽn màng (membrane fouling analysis): bao gồm xác định dạng tắc nghẽn (fouling type), tỷ lệ phục hồi thông lượng (flux recovery rate), và năng lượng tương tác bề mặt màng (membrane interfacial energy).
  - Các phương thức cải tiến mô hình Perceptron đa tầng (Multilayer Perceptron - MLP) nhằm nâng cao độ chính xác dự đoán:
    - Tối ưu hóa thuật toán hoặc lựa chọn thuật toán huấn luyện (optimizing/training algorithms).
    - Thay đổi hàm kích hoạt của lớp ẩn (hidden layer activation function).
    - Điều chỉnh cấu trúc phân tầng hoặc phân cấp của mô hình (adjusting the model hierarchy).
  - Phân tích hệ số độ nhạy (sensitivity factor analysis) được áp dụng để diễn giải mô hình (model interpretation) hoặc nhận diện các thông số có ảnh hưởng quan trọng (significant parameters).

- **Tổng hợp các mô hình ANN dự đoán trạng thái lọc trong MBR (Table 2)**: Bảng 2 tóm tắt các nghiên cứu điển hình sử dụng các biến thể ANN để dự đoán trạng thái lọc trong hệ thống bể phản ứng sinh học màng (Membrane Bioreactor - MBR):

| Model | Optimization | Hidden layer activation function | Structural features | Input parameter | Output parameter | Training algorithm | Fitting performance | Ref. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ENN | - | - | 9-55-1 | $T$, SRT, TSS, ODR, TMP, $\text{d}\text{TMP}/\text{d}t$, Filtration and backwash time | Flux | - | $\text{AD} = 2.7\%$ | Geissler et al., 2005 |
| MLP | - | - | 3-5-1 | Backwash time, Operation time, Flux | Flux | LM | $R^2 = 0.99$ | Aidan et al., 2008 |
| MLP | GA | log-sigmoid | - | MLSS, TMP, Resistance | Flux | LM | $\text{MAPE} = 0.0331$ | Li et al., 2014 |
| MLP | GA | tan-sigmoid | 5-10-1 | Time, MLSS, COD, SRT, TSS | TMP, Permeability | LM | $R^2 = 0.98$ (cho cả TMP và Permeability) | Mirbagheri et al., 2015b |
| RBFNN | GA | RBF | 5-5-1 | Time, MLSS, COD, SRT, TSS | TMP, Permeability | LM | $R^2 = 0.98$ (TMP), $R^2 = 0.99$ (Permeability) | Mirbagheri et al., 2015b |
| MLP | GA | tan-sigmoid | 6-8-1 | Flux, Aeration ratio, Concentration of SMP and EPS, initial TMP, Running time | TMP | Bayesian rule | Relative $\text{MSE} = 0.024$ | Wang and Wu, 2015 |
| RBFNN | CV | RBF | 2-2-1 | Aeration volume, TMP | Flux | - | $R^2 = 0.80$ | 2017 |
| MLP | - | log-sigmoid | 6-5-1 | Influent (TN, $\text{NO}_3^--\text{N}$, TP), Effluent (TN, $\text{NO}_3^--\text{N}$, TP) | TMP | LM | $R^2 = 0.85$ | Schmitt et al., 2018 |
| Fuzzy-RBFNN | PSO | log-sigmoid | 2-14-49-1 | Flux, Membrane flux variation | Flux | - | $\text{MAPE} = 0.0287$ | Tao and Li, 2018 |
| MLP | PSO | - | - | Temperature, Flux, TMP, MLSS | Resistance | LM | $R^2 = 0.97$ | Hamedi et al., 2019 |
| MLP | - | tan-sigmoid | 4-8-1 | MLSS, EC, DO, Time | Flux | LM | $R^2 = 0.98$ | Hosseinzadeh et al., 2020 |
| RBFNN | - | RBF | 1-3-1 | Permeate pump pressure | Flux, TMP | LM | $R^2 > 0.90$ | Abdul Wahab et al. |
| MLP | - | tan-sigmoid | 1-5(7)-1 | Permeate pump pressure | Flux, TMP | LM | $R^2 > 0.88$ | Abdul Wahab et al. |
| RNN | - | - | - | EC, Flux | EC, Flux | - | $\text{RMSE} = 18\text{ mS/cm}$ (EC), $\text{RMSE} = 1.1\text{ LMH}$ (Flux) | Viet et al., 2021 |
| MLP | - | tan-sigmoid | 4-30-30-1, 4-5-5-5-5-5-5-1 | pH, EC, influent TN and $\text{NH}_3\text{-N}$ | Flux, Resistance | LM | Flux: $R^2 = 0.88$, Resistance: $R^2 = 0.86$ | Viet and Jang, 2021 |
| WNN | BA | Bandelet function | 5-12-2 | MLSS, Sludge particle size, EPS, SMP, Sludge viscosity, RH, Zeta potential | Flux, Membrane flux recovery rate | Gradient descent method | $\text{MAPE} = 0.032$ | Zhao et al., 2020 |
| MLP | - | - | 3-17-2 | MLSS, HRT, Time | Flux, COD removal rate | LM | $R^2 = 0.9996$ | Hazrati et al., 2017 |
| ANFIS | - | - | - | OLR, Effluent pH, MLSS, MLVSS | TMP | LM | $R^2 = 0.98$ | Taheri et al., 2021 |
| MLP | - | log-sigmoid | 6-9-1 | Time, Flux, influent COD, pH, MLSS, TMP rate of change | Permeability | - | $R^2 = 0.9985$ | Yao et al., 2022 |
| MLP | - | tan-sigmoid | 3-9-1 | Disc rotational speed, Membrane to disc gap, OLR | Permeability | LM | $R^2 = 0.999$ | Irfan et al., 2022 |
| MLP | CV | tan-sigmoid | 6-6-1 | Sludge filterability, MLVSS, pH, influent COD, $T$, Cleaning cycle | Permeability | BFGS | $R^2 = 0.93$ | Alkmim et al., 2020 |

  - *Ghi chú từ Bảng 2*: $\text{ENN} = \text{Elman neural network}$, $\text{ODR} = \text{oxygen decay rate}$ (tốc độ phân hủy oxy), $\text{EC} = \text{Electrical conductivity}$ (độ dẫn điện), $\text{ANFIS} = \text{adaptive network-based fuzzy inference system}$ (hệ suy luận mờ thích nghi dựa trên mạng nơ-ron), $\text{BFGS} = \text{Broyden-Fletcher-Goldfarb-Shanno}$, $\text{RH} = \text{relative hydrophobicity}$ (độ kỵ nước tương đối).

- **Tối ưu hóa thuật toán huấn luyện và tác động của quy mô tập dữ liệu**: Các thuật toán huấn luyện đa dạng cùng kỹ thuật tối ưu hóa giúp nâng cao độ chính xác mô hình hóa, đồng thời bộc lộ giới hạn khi kích thước mẫu hạn chế:
  - Thuật toán di truyền (Genetic Algorithm - GA) và logic mờ (fuzzy logic) đã được kết hợp vào các mô hình MLP cải tiến.
  - Các thuật toán huấn luyện phổ biến gồm Levenberg-Marquardt (LM), quy tắc Bayes (Bayesian rule), phương pháp hạ độ dốc (gradient descent), và thuật toán Broyden-Fletcher-Goldfarb-Shanno (BFGS).
  - Wang và Wu (2015) dự đoán áp suất xuyên màng TMP:
    - Biến đầu vào gồm lưu lượng dòng (flow rate), tỷ lệ sục khí (aeration ratio), TMP ban đầu (initial TMP), thời gian vận hành (running time), và nồng độ chất gây nghẽn đặc trưng gồm chất cao phân tử hòa tan (Soluble Microbial Products - SMP) cùng chất polyme ngoại bào (Extracellular Polymeric Substances - EPS).
    - Dự đoán điểm nhảy vọt của TMP (jump point of TMP) đạt sai số bình phương trung bình tương đối (Relative MSE) bằng $0.024$.
    - Kiến trúc mạng MLP có cấu trúc tô-pô $6\text{-}8\text{-}1$, trọng số và độ lệch (weight and bias) được tối ưu hóa bằng thuật toán GA, và mô hình được huấn luyện bằng quy tắc Bayes.
    - Kết quả chỉ ra rằng hiệu suất của MLP khi kích thước mẫu nhỏ (small sample sizes) kém ổn định hơn so với các mô hình toán học truyền thống (traditional mathematical models).
  - Alkmim và cộng sự (2020) mô hình hóa độ thấm màng (membrane permeability):
    - Thiết lập mạng MLP với cấu trúc tô-pô $6\text{-}6\text{-}1$, huấn luyện bằng thuật toán BFGS, và tối ưu hóa siêu tham số bằng kiểm định chéo (Cross-Validation - CV).
    - Biến đầu vào gồm khả năng lọc của bùn (sludge filterability), chất rắn bay hơi lơ lửng trong bùn lỏng (Mixed Liquor Volatile Suspended Solids - MLVSS), $\text{pH}$, COD dòng vào (influent COD), nhiệt độ ($T$), và chu kỳ làm sạch (cleaning cycle).
    - Mô hình đạt hệ số xác định $R^2 = 0.93$.
  - Đánh giá tổng hợp: Các thuật toán tối ưu hóa/huấn luyện cho thấy hiệu quả rõ rệt trong việc cải thiện mô hình, song tác động của kích thước mẫu đối với hiệu suất học máy trong xử lý tắc nghẽn màng vẫn là vấn đề cần lưu tâm.

- **Tối ưu hóa hàm kích hoạt lớp ẩn bằng hàm RBF và hàm sóng (Wavelet/Bandelet)**: Việc thay đổi hàm kích hoạt lớp ẩn giúp nâng cao năng lực mô hình hóa phi tuyến các thông số tắc nghẽn phức tạp:
  - Mạng nơ-ron hàm cơ sở xuyên tâm (Radial Basis Function Neural Network - RBFNN):
    - Mirbagheri và cộng sự (2015a) áp dụng mô hình RBFNN tối ưu hóa bằng thuật toán GA để dự đoán TMP và độ thấm màng từ $5$ chỉ số đầu vào: thời gian vận hành (operating time), tổng chất rắn lơ lửng (Total Suspended Solids - TSS), COD, thời gian lưu bùn (Solids Retention Time - SRT), và chất rắn lơ lửng trong bùn lỏng (Mixed Liquor Suspended Solids - MLSS).
    - Mô hình đạt hệ số xác định $R^2 > 0.98$.
    - Phân tích độ nhạy (sensitivity analysis) chỉ ra thời gian vận hành và nồng độ MLSS của bùn lỏng là các yếu tố ảnh hưởng mang tính chi phối.
  - Mạng nơ-ron Bandelet (Bandelet neural network / Wavelet Neural Network - WNN):
    - Zhao và cộng sự (2020) sử dụng hàm Bandelet (dạng xấp xỉ của hàm sóng wavelet) làm hàm kích hoạt lớp ẩn với cấu trúc mạng $5\text{-}12\text{-}2$.
    - Mạng được huấn luyện bằng phương pháp hạ độ dốc (gradient descent) và tích hợp thuật toán dơi (Bat Algorithm - BA) để tối ưu hóa tham số.
    - Dự đoán thông lượng màng và tỷ lệ phục hồi thông lượng màng (membrane flux recovery rate) dựa trên các tính chất của bùn lỏng: MLSS, kích thước hạt bùn (sludge particle size), EPS, SMP, độ nhớt của bùn (sludge viscosity), độ kỵ nước tương đối (relative hydrophobicity - RH), và điện thế zeta (zeta potential).
    - Đạt sai số phần trăm tuyệt đối trung bình $\text{MAPE} = 0.032$ (tương đương sai số tương đối $3.2\%$) trên toàn bộ tập dữ liệu.

- **Mô hình hóa chuỗi thời gian cho tắc nghẽn màng biến thiên bằng mạng nơ-ron hồi quy (RNN và ENN)**: Mạng nơ-ron hồi quy thích hợp cho việc dự đoán tắc nghẽn màng biến thiên theo thời gian (time-varying membrane fouling) nhờ ưu thế xử lý dữ liệu dạng chuỗi tuần tự (sequential data):
  - Mạng nơ-ron Elman (Elman Neural Network - ENN) là dạng sơ khai của RNN với các ô nhớ cục bộ (local memory cells) và liên kết phản hồi cục bộ (local feedback connections), được ứng dụng dự đoán tắc nghẽn màng từ giai đoạn đầu:
    - Geissler và cộng sự (2005) thiết lập mô hình ENN với cấu trúc tô-pô $9\text{-}55\text{-}1$ để dự đoán thông lượng màng với độ lệch trung bình (Average Deviation - AD) là $2.7\%$.
    - Thông qua phân tích độ nhạy, nghiên cứu xác định điều kiện rửa ngược màng tối ưu là rửa ngược ở áp suất cao với khoảng thời gian ngắn (high-pressure backwash with short intervals).
  - Ứng dụng RNN dự đoán diễn tiến dài hạn:
    - Viet và cộng sự (2021) thiết lập mô hình RNN để dự đoán độ dẫn điện của bùn lỏng (mixed liquor conductivity) và thông lượng màng của bể phản ứng sinh học màng thẩm thấu (osmosis membrane bioreactor) trong thời gian $40\text{ ngày}$.
    - Mô hình đạt sai số thỏa đáng với sai số căn bậc hai trung bình $\text{RMSE} = 18\text{ mS/cm}$ (đối với độ dẫn điện) và $\text{RMSE} = 1.1\text{ LMH}$ (đối với thông lượng màng).
  - Ý nghĩa đối với công tác vận hành:
    - Việc xem xét các yếu tố diễn tiến theo chuỗi thời gian (time-series development factors) hỗ trợ dự đoán tắc nghẽn màng chính xác hơn.
    - Phân tích diễn giải mô hình (model interpretation) hỗ trợ thiết kế các điều kiện vận hành và lưu trình công nghệ tối ưu, đóng góp vào quá trình vận hành tinh gọn của hệ thống MBR.

- **Ứng dụng mô hình ANN trong phân tích tắc nghẽn màng nâng cao (membrane fouling analysis)**: Mở rộng các kiến trúc mạng nơ-ron (MLP, RBFNN, RNN, CNN) sang phân tích cơ chế, cân bằng năng lượng và thị giác máy tính:
  - Dự đoán tiêu thụ năng lượng hệ MBR quy mô thực tế:
    - Chen và cộng sự (2012) phát triển mô hình MLP sử dụng công suất sục khí quá trình sinh học (bioprocess aeration capacity), công suất sục khí màng (membrane aeration capacity), lưu lượng tuần hoàn bùn lỏng (mixed liquor recirculation flowrate), và thông lượng màng làm biến đầu vào.
    - Dự đoán mức tiêu thụ năng lượng trên một đơn vị sản xuất nước (energy consumption per unit water production) trong hệ MBR quy mô đầy đủ (full-scale MBR) với $R^2 > 0.55$.
  - Định lượng năng lượng tương tác liên diện màng:
    - Zhao và cộng sự (2019) thiết lập mô hình RBFNN để định lượng năng lượng tương tác bề mặt màng MBR (membrane interfacial energy).
    - Biến đầu vào gồm góc tiếp xúc của nước/glycerol/diiodomethane trên bề mặt bùn và màng, điện thế zeta của bề mặt bùn và màng, cùng khoảng cách giữa các hạt bùn và bề mặt màng.
    - Thời gian tính toán mà mô hình RBFNN yêu cầu chỉ xấp xỉ $1/50$ so với phương pháp Derjaguin-Landau-Verwey-Overbeek mở rộng giải tích (analytically extended DLVO method).
  - Phân loại tắc nghẽn màng bằng mạng tích chập kết hợp cơ chế chú ý:
    - Shi và cộng sự (2022) thiết lập mô hình mạng nơ-ron tích chập (Convolutional Neural Network - CNN) dựa trên cơ chế chú ý (attention mechanism).
    - Mô hình sử dụng tập ảnh mức xám đã qua xử lý (processed grayscale image set) làm đầu vào để phân loại tắc nghẽn màng với độ chính xác chẩn đoán (diagnostic accuracy) đạt $98\%$.
  - Khai thác học máy không giám sát:
    - Bên cạnh học có giám sát, các phương pháp học không giám sát (unsupervised learning) cũng được ứng dụng để phân tích tắc nghẽn màng phục vụ tối ưu hóa quy trình vận hành (Woo et al., 2022).
  - Đánh giá tiềm năng và rào cản ứng dụng thực tiễn:
    - Mặc dù giám sát trực tuyến (online monitoring) chưa khả dụng cho phần lớn các đặc trưng đầu vào trong các ứng dụng phân tích chuyên sâu nói trên, các mô hình vẫn thể hiện năng lực phân tích mạnh mẽ.
    - Các nghiên cứu này mang lại góc nhìn mới giúp phân tích cơ chế tắc nghẽn màng và cung cấp cơ sở mô hình hóa phục vụ kiểm soát tắc nghẽn màng có định hướng.
