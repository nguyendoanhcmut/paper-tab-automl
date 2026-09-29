# -*- coding: utf-8 -*-
import os

content = """## 5. Ứng dụng Học máy trong Dự đoán Tắc nghẽn Màng (Membrane Fouling)

### 5.1 Tắc nghẽn Màng: Trọng tâm Nghiên cứu Lớn nhất của MBR

#### 5.1.1 Bản chất Vật lý, Hóa học và Sinh học của Hiện tượng Tắc nghẽn Màng
- Khái niệm Tắc nghẽn Màng: Tắc nghẽn màng là sự tích tụ vật chất trên bề mặt màng hoặc bên trong mao quản màng.
- Phân loại Tác nhân Gây bẩn (Foulants): Tắc nghẽn gồm chất hữu cơ, vô cơ, sinh học và hỗn hợp.
- Tắc nghẽn Hữu cơ (Organic Fouling): Hợp chất keo và hòa tan gồm polysaccharides, proteins và humic substances. Các chất này chi phối nhiều giai đoạn tắc nghẽn (Lin et al., 2014, Xu et al., 2020).
- Tắc nghẽn Vô cơ (Inorganic Fouling và Scaling): Các muối khoáng kết tủa như $\\text{CaCO}_3$, $\\text{CaSO}_4$, muối phosphate, hydroxide sắt và silica bám vào màng.
- Tắc nghẽn Sinh học (Biofouling): Vi sinh vật bám dính, sinh trưởng và tạo lớp màng sinh học (biofilm). Lớp này liên kết nhờ polyme ngoại bào (EPS).
- Tắc nghẽn Hỗn hợp (Composite Fouling): Chất hữu cơ, vi sinh vật và ion $\\text{Ca}^{2+}$, $\\text{Mg}^{2+}$ tương tác đồng thời. Quá trình này tạo cặn bẩn bền vững.
- Phân loại theo Khả năng Phục hồi:
  - Tắc nghẽn Thuận nghịch (Reversible Fouling): Lực cắt thủy lực, sục khí hoặc rửa ngược (backwash) loại bỏ được lớp cặn bẩn này.
  - Tắc nghẽn Bất thuận nghịch (Irreversible Fouling): Chất bẩn bám dính mạnh hoặc bít sâu lỗ rỗng. Vận hành viên phải dùng hóa chất $\\text{NaOCl}$, $\\text{NaOH}$ hoặc citric acid.
- Mối Liên hệ Nội tại giữa Xử lý Ô nhiễm và Tắc nghẽn Màng:
  - Quá trình xử lý trong MBR kết hợp bùn hoạt tính sinh học và giữ lại vật lý qua màng.
  - Sự hình thành tắc nghẽn màng gắn liền trực tiếp với quá trình phân hủy chất ô nhiễm.
  - Tắc nghẽn màng có tính phi tuyến rất cao giữa các thông số.
  - Độ phức tạp này tạo tiềm năng lớn cho mô hình học máy phát huy ưu thế mô phỏng.

#### 5.1.2 Tác động Vận hành và Các Chỉ số Trạng thái Màng Cần Dự đoán
- Tác động Tiêu cực của Tắc nghẽn Màng:
  - Làm suy giảm nghiêm trọng thông lượng lọc màng ($J$).
  - Làm tăng đột ngột áp suất xuyên màng ($TMP$). Hiện tượng này tạo nên bước nhảy vọt $TMP$ ($TMP$ jump).
  - Gia tăng điện năng tiêu thụ của máy thổi khí và bơm hút màng.
  - Làm giảm tuổi thọ sợi màng. Hiện tượng này làm tăng chi phí thay màng mới.
- Phân loại Hai Nhóm Bài toán Dự đoán Tắc nghẽn trong Học máy:
  - Nhóm 1: Dự đoán trạng thái lọc (Filtration state prediction).
  - Nhóm 2: Phân tích tắc nghẽn màng (Membrane fouling analysis).
- Các Biến Mục tiêu Đo lường Trạng thái Lọc:
  - Áp suất Xuyên màng ($TMP$): Đơn vị là $\\text{kPa}$ hoặc $\\text{bar}$. $TMP$ biểu thị chênh lệch áp suất qua màng tại một thông lượng lọc xác định.
  - Thông lượng Lọc ($J$ hay Flux): Đơn vị là $\\text{L}/(\\text{m}^2\\cdot\\text{h})$ (viết tắt là $\\text{LMH}$). $J$ đo thể tích nước sạch qua một đơn vị diện tích màng trong một giờ.
  - Tốc độ Tăng Áp suất Xuyên màng ($dTMP/dt$): Đơn vị là $\\text{kPa/h}$ hoặc $\\text{kPa/d}$. Đạo hàm theo thời gian này xác định tốc độ tích tụ chất bẩn.
  - Độ thấm Thủy lực của Màng (Permeability, ký hiệu $P$): $P = \\frac{J}{TMP}$, đơn vị là $\\text{LMH/bar}$. Chỉ số này đánh giá trực tiếp năng lực dẫn chất lỏng của màng.
  - Tổng Trở lực Lọc Thủy lực ($R_t$): Đơn vị tính là $\\text{m}^{-1}$. Định luật Darcy mở rộng mô tả mối quan hệ giữa các biến:
    $$J = \\frac{TMP}{\\mu \\cdot R_t} = \\frac{TMP}{\\mu \\cdot (R_m + R_p + R_c)}$$
    Trong đó:
    - $J$ là thông lượng lọc ($\\text{m}^3/(\\text{m}^2\\cdot\\text{s})$).
    - $TMP$ là áp suất xuyên màng ($\\text{Pa}$).
    - $\\mu$ là độ nhớt động học của chất lỏng lọc ($\\text{Pa}\\cdot\\text{s}$).
    - $R_m$ là trở lực thủy lực bản thân màng sạch ($\\text{m}^{-1}$).
    - $R_p$ là trở lực do bít tắc lỗ rỗng màng ($\\text{m}^{-1}$).
    - $R_c$ là trở lực của lớp bánh bùn bám trên bề mặt màng ($\\text{m}^{-1}$).
- Các Biến Mục tiêu Đo lường Phân tích Tắc nghẽn Màng:
  - Phân loại Dạng Tắc nghẽn (Fouling Type): Nhận diện bít lỗ rỗng hoàn toàn, bít trung gian, bít tiêu chuẩn, hoặc lắng đọng bánh bùn.
  - Tỷ lệ Phục hồi Thông lượng Lọc ($FRR$ - Flux Recovery Rate): Đơn vị tính là $\\%$. Công thức xác định:
    $$FRR = \\left(\\frac{J_c}{J_0}\\right) \\times 100\\%$$
    Trong đó $J_c$ là thông lượng sau khi rửa màng. Ký hiệu $J_0$ là thông lượng ban đầu của màng sạch.
  - Năng lượng Liên diện Bề mặt Màng (Membrane Interfacial Energy): Đơn vị tính là $\\text{mJ/m}^2$. Đại lượng này định lượng lực tương tác bám dính giữa hạt bùn và vật liệu màng.

### 5.2 Ứng dụng Mạng Nơ-ron Nhân tạo (ANN) Dự đoán Tắc nghẽn Màng

#### 5.2.1 Tổng quan Kiến trúc và Các Kỹ thuật Tối ưu Hóa Mạng ANN
- Năng lực Học Phi tuyến của ANN: Mạng nơ-ron nhân tạo có khả năng xấp xỉ hàm phi tuyến mạnh mẽ. ANN mô hình hóa chính xác tương tác phức tạp giữa bùn hoạt tính và màng lọc.
- Ba Hướng Cải tiến Mô hình MLP (Multilayer Perceptron):
  - Tối ưu hóa Thuật toán Huấn luyện: Thay thế giải thuật hạ độ dốc bằng Levenberg-Marquardt (LM), Quasi-Newton BFGS, hoặc điều hòa Bayes (Bayesian regularization).
  - Tùy chỉnh Hàm Kích hoạt Tầng Ẩn: Ứng dụng hàm log-sigmoid, tan-sigmoid, hàm cơ sở Gauss (RBF), hoặc hàm sóng Bandelet.
  - Tối ưu hóa Cấu trúc Phân tầng: Tinh chỉnh số tầng và số nơ-ron qua CV, giải thuật di truyền (GA) hoặc bầy hạt (PSO).
- Phân tích Độ nhạy (Sensitivity Factor Analysis): Kỹ thuật này trích xuất tầm quan trọng tương đối của từng biến đầu vào. Phương pháp này giải mã cấu trúc hộp đen của mô hình.

#### 5.2.2 Bảng Tổng hợp và Đối sánh Thực nghiệm Các Mô hình ANN (Table 2)
- Dữ liệu Thực nghiệm: Bảng 2 hệ thống hóa các nghiên cứu dùng ANN dự đoán trạng thái lọc MBR.

| Mô hình | Thuật toán Tối ưu | Hàm Kích hoạt Tầng ẩn | Cấu trúc Mạng ($I\\text{-}H\\text{-}O$) | Thông số Đầu vào (Inputs) | Thông số Đầu ra (Outputs) | Thuật toán Huấn luyện | Hiệu năng Khớp Thực nghiệm | Tài liệu Trích dẫn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ENN | - | - | 9-55-1 | $T$, SRT, TSS, ODR, $TMP$, $dTMP/dt$, Thời gian lọc và rửa ngược | Thông lượng lọc ($J$) | - | $AD = 2.7\\%$ | Geissler et al., 2005 |
| MLP | - | - | 3-5-1 | Thời gian rửa ngược, Thời gian vận hành, Thông lượng lọc ($J$) | Thông lượng lọc ($J$) | LM | $R^2 = 0.99$ | Aidan et al., 2008 |
| MLP | GA | log-sigmoid | - | MLSS, $TMP$, Trở lực màng ($R_t$) | Thông lượng lọc ($J$) | LM | $MAPE = 0.0331$ | Li et al., 2014 |
| MLP | GA | tan-sigmoid | 5-10-1 | Thời gian, MLSS, COD, SRT, TSS | $TMP$, Độ thấm ($P$) | LM | $TMP$: $R^2 = 0.98$, $P$: $R^2 = 0.98$ | Mirbagheri et al., 2015b |
| RBFNN | GA | RBF | 5-5-1 | Thời gian, MLSS, COD, SRT, TSS | $TMP$, Độ thấm ($P$) | LM | $TMP$: $R^2 = 0.98$, $P$: $R^2 = 0.99$ | Mirbagheri et al., 2015b |
| MLP | GA | tan-sigmoid | 6-8-1 | Thông lượng $J$, Tỷ lệ sục khí, Nồng độ SMP và EPS, $TMP$ ban đầu, Thời gian vận hành | $TMP$ (xác định điểm nhảy $TMP$) | Bayesian rule | $\\text{Relative MSE} = 0.024$ | Wang và Wu, 2015 |
| RBFNN | CV | RBF | 2-2-1 | Thể tích sục khí, $TMP$ | Thông lượng lọc ($J$) | - | $R^2 = 0.80$ | 2017 |
| MLP | - | log-sigmoid | 6-5-1 | Dòng vào (TN, $\\text{NO}_3^-$-N, TP), Dòng ra (TN, $\\text{NO}_3^-$-N, TP) | $TMP$ | LM | $R^2 = 0.85$ | Schmitt et al., 2018 |
| Fuzzy-RBFNN | PSO | log-sigmoid | 2-14-49-1 | Thông lượng $J$, Độ biến thiên thông lượng màng | Thông lượng lọc ($J$) | - | $MAPE = 0.0287$ | Tao và Li, 2018 |
| MLP | PSO | - | - | Nhiệt độ $T$, Thông lượng $J$, $TMP$, MLSS | Trở lực lọc ($R_t$) | LM | $R^2 = 0.97$ | Hamedi et al., 2019 |
| MLP | - | tan-sigmoid | 4-8-1 | MLSS, EC, DO, Thời gian | Thông lượng lọc ($J$) | LM | $R^2 = 0.98$ | Hosseinzadeh et al., 2020 |
| RBFNN | - | RBF | 1-3-1 | Áp suất bơm hút thẩm thấu | Thông lượng $J$, $TMP$ | LM | $R^2 > 0.90$ | Abdul Wahab et al. |
| MLP | - | tan-sigmoid | 1-5(7)-1 | Áp suất bơm hút thẩm thấu | Thông lượng $J$, $TMP$ | LM | $R^2 > 0.88$ | Abdul Wahab et al. |
| RNN | - | - | - | EC, Thông lượng lọc ($J$) | EC, Thông lượng lọc ($J$) | - | EC: $RMSE = 18\\text{ mS/cm}$, $J$: $RMSE = 1.1\\text{ LMH}$ | Viet et al., 2021 |
| MLP | - | tan-sigmoid | 4-30-30-1 | pH, EC, Dòng vào (TN, $\\text{NH}_3$-N) | Thông lượng lọc ($J$) | LM | $R^2 = 0.88$ | Viet và Jang, 2021 |
| MLP | - | tan-sigmoid | 4-5-5-5-5-5-5-1 | pH, EC, Dòng vào (TN, $\\text{NH}_3$-N) | Trở lực lọc ($R_t$) | LM | $R^2 = 0.86$ | Viet và Jang, 2021 |
| WNN | BA | Bandelet | 5-12-2 | MLSS, Kích thước hạt bùn, EPS, SMP, Độ nhớt bùn, RH, Thế Zeta | Thông lượng $J$, Tỷ lệ phục hồi $FRR$ | Gradient descent | $MAPE = 0.032$ ($3.2\\%$) | Zhao et al., 2020 |
| MLP | - | - | 3-17-2 | MLSS, HRT, Thời gian | Thông lượng $J$, Tỷ lệ khử COD | LM | $R^2 = 0.9996$ | Hazrati et al., 2017 |
| ANFIS | - | - | - | Tải trọng OLR, pH dòng ra, MLSS, MLVSS | $TMP$ | LM | $R^2 = 0.98$ | Taheri et al., 2021 |
| MLP | - | log-sigmoid | 6-9-1 | Thời gian, Flux, COD vào, pH, MLSS, Tốc độ thay đổi $TMP$ | Độ thấm ($P$) | - | $R^2 = 0.9985$ | Yao et al., 2022 |
| MLP | - | tan-sigmoid | 3-9-1 | Tốc độ quay đĩa, Khe hở màng-đĩa, Tải nạp OLR | Độ thấm ($P$) | LM | $R^2 = 0.999$ | Irfan et al., 2022 |
| MLP | CV | tan-sigmoid | 6-6-1 | Khả năng lọc của bùn, MLVSS, pH, COD vào, $T$, Chu kỳ rửa | Độ thấm ($P$) | BFGS | $R^2 = 0.93$ | Alkmim et al., 2020 |

- Chú thích thuật ngữ trong bảng: ENN là Elman Neural Network. ODR là Oxygen Decay Rate. EC là Electrical Conductivity. ANFIS là Adaptive Network-based Fuzzy Inference System. BFGS là Broyden-Fletcher-Goldfarb-Shanno. RH là Relative Hydrophobicity. BA là Bat Algorithm. WNN là Wavelet/Bandelet Neural Network. LM là Levenberg-Marquardt. AD là Average Deviation. MAPE là Mean Absolute Percentage Error.

#### 5.2.3 Phân tích Chi tiết Các Công trình Nghiên cứu Điển hình
- Nghiên cứu của Aidan et al. (2008):
  - Nhóm tác giả xây dựng mô hình MLP với cấu trúc 3-5-1.
  - Biến đầu vào gồm thời gian rửa ngược, thời gian vận hành và thông lượng ban đầu.
  - Thuật toán Levenberg-Marquardt (LM) mang lại tốc độ hội tụ cao.
  - Mô hình đạt hệ số xác định thực nghiệm rất cao với $R^2 = 0.99$.
- Nghiên cứu của Li et al. (2014):
  - Nhóm tác giả dùng giải thuật di truyền (GA) tối ưu hóa trọng số khởi tạo của mạng MLP.
  - Tầng ẩn sử dụng hàm kích hoạt phi tuyến log-sigmoid.
  - Biến đầu vào gồm MLSS, áp suất $TMP$ và trở lực màng.
  - Mô hình dự đoán thông lượng lọc ($J$) đạt sai số tuyệt đối trung bình $MAPE = 0.0331$ ($3.31\\%$).
- Nghiên cứu của Mirbagheri et al. (2015a, 2015b):
  - Nhóm tác giả đối sánh hai kiến trúc mạng: MLP cấu trúc 5-10-1 (hàm tan-sigmoid) và RBFNN cấu trúc 5-5-1 (hàm Gauss).
  - Thuật toán GA tối ưu cấu trúc mạng. Thuật toán LM thực hiện huấn luyện.
  - Biến đầu vào gồm thời gian, MLSS, COD, SRT và TSS.
  - Hiệu năng mô hình: Cả MLP và RBFNN đều đạt $R^2 = 0.98$ khi dự đoán $TMP$.
  - Khi dự đoán độ thấm ($P$), RBFNN đạt $R^2 = 0.99$ còn MLP đạt $R^2 = 0.98$.
  - Phân tích độ nhạy chỉ ra thời gian vận hành và nồng độ MLSS chi phối mạnh mẽ nhất đến tắc nghẽn màng.
- Nghiên cứu của Wang và Wu (2015):
  - Nhóm nghiên cứu thiết lập mô hình MLP cấu trúc 6-8-1 với hàm tan-sigmoid.
  - Giải thuật GA tối ưu hóa trọng số và bias. Quy tắc điều hòa Bayes (Bayesian rule) thực hiện huấn luyện mạng.
  - Biến đầu vào gồm: Thông lượng $J$, tỷ lệ sục khí, nồng độ SMP và EPS, $TMP$ ban đầu và thời gian vận hành.
  - Mô hình nhận diện chính xác bước nhảy áp suất ($TMP$ jump) với $\\text{Relative MSE} = 0.024$.
  - Phát hiện quan trọng: Mô hình MLP trên tập dữ liệu nhỏ kém ổn định hơn mô hình toán truyền thống.
- Nghiên cứu của Alkmim et al. (2020):
  - Mô hình MLP cấu trúc 6-6-1 dùng giải thuật Quasi-Newton BFGS và kiểm định chéo CV.
  - Biến đầu vào gồm: Độ lọc của bùn (sludge filterability), MLVSS, pH, COD vào, nhiệt độ $T$ và chu kỳ làm sạch.
  - Mô hình dự đoán độ thấm màng đạt $R^2 = 0.93$. Kết quả khẳng định vai trò tích cực của thuật toán huấn luyện.
- Nghiên cứu của Zhao et al. (2020):
  - Nhóm tác giả phát triển mạng nơ-ron Bandelet cấu trúc 5-12-2. Mô hình dùng hàm Bandelet làm hàm kích hoạt tầng ẩn.
  - Thuật toán hạ độ dốc huấn luyện mạng. Thuật toán đàn dơi (Bat Algorithm - BA) tối ưu siêu tham số.
  - Biến đầu vào gồm 7 đặc tính bùn: MLSS, kích thước hạt, EPS, SMP, độ nhớt, độ kỵ nước tương đối (RH) và thế Zeta.
  - Mô hình dự đoán đồng thời thông lượng $J$ và tỷ lệ phục hồi $FRR$. Sai số đạt $MAPE = 3.2\\%$ trên toàn bộ tập dữ liệu.
- Nghiên cứu của Geissler et al. (2005):
  - Nhóm tác giả dùng mạng nơ-ron hồi quy Elman (ENN) cấu trúc 9-55-1 dự đoán thông lượng màng.
  - Biến đầu vào gồm: Nhiệt độ $T$, SRT, TSS, tốc độ suy giảm oxy (ODR), $TMP$, $dTMP/dt$, thời gian lọc và rửa ngược.
  - Mô hình đạt độ lệch trung bình thực nghiệm $AD = 2.7\\%$.
  - Phân tích độ nhạy chứng minh chế độ rửa ngược tối ưu là áp suất cao kết hợp chu kỳ ngắn.
- Nghiên cứu của Viet et al. (2021) và Viet & Jang (2021):
  - Viet et al. (2021) dùng mô hình RNN dự đoán độ dẫn điện ($EC$) và thông lượng ($J$) trong hệ OMBR suốt 40 ngày.
  - Mô hình đạt sai số $RMSE = 18\\text{ mS/cm}$ đối với $EC$. Mô hình đạt sai số $RMSE = 1.1\\text{ LMH}$ đối với thông lượng lọc.
  - Viet và Jang (2021) phát triển các mạng MLP tầng ẩn sâu với cấu trúc 4-30-30-1 và 4-5-5-5-5-5-5-1.
  - Các mô hình dự đoán thành công thông lượng lọc ($R^2 = 0.88$) và trở lực lọc ($R^2 = 0.86$) từ pH, EC, TN và $\\text{NH}_3$-N.

#### 5.2.4 Ứng dụng ANN Phân tích Năng lượng và Tương tác Liên diện Bề mặt Màng
- Dự đoán Năng lượng Tiêu thụ trên Đơn vị Nước sạch:
  - Chen et al. (2012) phát triển mô hình MLP dự đoán điện năng trên một mét khối nước ở trạm MBR quy mô thực.
  - Biến đầu vào gồm công suất sục khí sinh học, sục khí màng, lưu lượng tuần hoàn bùn và thông lượng lọc.
  - Mô hình đạt hệ số xác định $R^2 > 0.55$, giúp tối ưu hóa chi phí vận hành trạm xử lý.
- Định lượng Năng lượng Bề mặt Liên diện Màng (Membrane Interfacial Energy):
  - Zhao et al. (2019) thiết lập mô hình RBFNN định lượng năng lượng liên diện màng sinh học MBR.
  - Biến đầu vào gồm góc tiếp xúc của 3 chất lỏng chuẩn (nước, glycerol, diiodomethane) trên bề mặt bùn và màng.
  - Đầu vào còn có thế zeta của bề mặt bùn và màng cùng khoảng cách giữa hạt bùn và màng.
  - Thời gian tính toán của RBFNN chỉ bằng khoảng $1/50$ thời gian của phương pháp giải tích XDLVO mở rộng.
- Chẩn đoán Tắc nghẽn bằng Xử lý Ảnh với Mạng Nơ-ron Tích chập (CNN):
  - Shi et al. (2022) ứng dụng mạng CNN tích hợp cơ chế tập trung (Attention Mechanism).
  - Mô hình nhận tập ảnh thang độ xám (grayscale images) bề mặt màng để chẩn đoán phân loại trạng thái tắc nghẽn.
  - Độ chính xác chẩn đoán thực nghiệm đạt mức $98\\%$.
- Phương pháp Học Không Giám sát (Unsupervised Learning):
  - Woo et al. (2022) ứng dụng thuật toán phân cụm không giám sát để phân tích cơ chế tắc nghẽn màng. Nghiên cứu hỗ trợ tối ưu hóa quy trình rửa lọc.

#### 5.2.5 Phân tích Chuyên sâu Bốn Kiến trúc Mạng Nơ-ron Cốt lõi
- Mạng Nơ-ron Nhiều Tầng Truyền thẳng (MLP và BPNN):
  - Cấu trúc: Mô hình gồm 3 thành phần liên kết: tầng vào ($I$), một hoặc nhiều tầng ẩn ($H$), và tầng ra ($O$).
  - Thuật toán Lan truyền ngược (Back-Propagation): Tín hiệu lan truyền thuận để tính sai số đầu ra. Thuật toán lan truyền ngược đạo hàm hàm mất mát qua quy tắc chuỗi để hiệu chỉnh trọng số $W$ và độ lệch $b$.
  - Ưu điểm: Cấu trúc toán học đơn giản, tốn ít tài nguyên tính toán, khả năng xấp xỉ phi tuyến mạnh.
  - Nhược điểm: BPNN dễ rơi vào cực tiểu cục bộ (local minima). Mạng nhạy cảm với trọng số ban đầu và không có bộ nhớ quá khứ.
- Mạng Nơ-ron Hồi quy Elman (ENN):
  - Cấu trúc Nút Ngữ cảnh (Context Layer): ENN lưu đầu ra của tầng ẩn tại bước trước ($t-1$) vào tầng ngữ cảnh. Tầng này phản hồi lại tầng ẩn tại bước hiện tại ($t$).
  - Phương trình Toán học của ENN:
    $$h(t) = f_H\\left(W_{ih} x(t) + W_{ch} h(t-1) + b_h\\right)$$
    $$y(t) = f_O\\left(W_{ho} h(t) + b_o\\right)$$
    Trong đó: $x(t)$ là vector đầu vào tại thời điểm $t$. Ký hiệu $h(t)$ là trạng thái tầng ẩn. Ký hiệu $h(t-1)$ là trạng thái ngữ cảnh lưu vết. Ký hiệu $y(t)$ là đầu ra mạng. Các ma trận $W_{ih}, W_{ch}, W_{ho}$ là trọng số liên kết. Các vector $b_h, b_o$ là ngưỡng lệch.
  - Ưu điểm: Phản ánh trực tiếp động học trễ của quá trình bám bẩn màng. ENN đạt độ chính xác cao hơn MLP tĩnh khi mô phỏng chuỗi thời gian lọc.
- Mạng Nơ-ron Tích chập (CNN):
  - Cấu trúc: Mô hình gồm các lớp tích chập (Convolutional layers), kích hoạt ReLU, lớp gộp (Pooling) và tầng kết nối đầy đủ.
  - Cơ chế Toán học: Toán tử tích chập 2 chiều quét qua ma trận điểm ảnh với bộ lọc hạt nhân $K$:
    $$S(i, j) = (I * K)(i, j) = \\sum_{m} \\sum_{n} I(i-m, j-n) K(m, n)$$
  - Ứng dụng: Nhận diện cấu trúc cặn bẩn qua ảnh vi thể bề mặt màng hoặc bản đồ quang phổ huỳnh quang 3 chiều (3D-EEM).
- Mạng Nơ-ron Bộ nhớ Dài-Ngắn hạn (LSTM) và Mạng Nơ-ron Hồi quy (RNN):
  - Cấu trúc Khối Ô nhớ (Memory Cell): LSTM điều khiển luồng thông tin qua cổng quên ($f_t$), cổng vào ($i_t$) và cổng ra ($o_t$). Ô nhớ trung tâm ($C_t$) duy trì thông tin dài hạn.
  - Hệ Phương trình Toán học Điều khiển LSTM:
    $$f_t = \\sigma\\left(W_f \\cdot [h_{t-1}, x_t] + b_f\\right)$$
    $$i_t = \\sigma\\left(W_i \\cdot [h_{t-1}, x_t] + b_i\\right)$$
    $$\\tilde{C}_t = \\tanh\\left(W_c \\cdot [h_{t-1}, x_t] + b_c\\right)$$
    $$C_t = f_t \\odot C_{t-1} + i_t \\odot \\tilde{C}_t$$
    $$o_t = \\sigma\\left(W_o \\cdot [h_{t-1}, x_t] + b_o\\right)$$
    $$h_t = o_t \\odot \\tanh(C_t)$$
    Trong đó: $\\sigma$ là hàm sigmoid chuẩn hóa về khoảng $[0, 1]$. Ký hiệu $\\odot$ là phép nhân Hadamard từng phần tử. Ký hiệu $C_t$ là trạng thái ô nhớ lưu giữ thông tin dài hạn. Ký hiệu $h_t$ là vector trạng thái ẩn đầu ra.
  - Ưu thế Tuyệt đối: LSTM triệt tiêu hiện tượng tiêu biến đạo hàm (vanishing gradient) trên chuỗi thời gian dài. Mô hình lưu giữ dữ liệu nhiều chu kỳ lọc và phát hiện sớm bước nhảy vọt $TMP$ ($TMP$ jump).

### 5.3 Ứng dụng các Mô hình Học máy Khác và Mô hình Lai (Hybrid AI)

#### 5.3.1 Máy Véc-tơ Hỗ trợ (SVM / SVR) và Biến thể Bình phương Tối thiểu (LSSVM)
- Nguyên lý Học Thống kê: Mô hình hồi quy véc-tơ hỗ trợ (SVR) hoạt động theo nguyên lý giảm thiểu rủi ro cấu trúc. SVR kiểm soát độ phức tạp để ngăn ngừa hiện tượng quá khớp (overfitting).
- Hàm nhân Gauss (RBF Kernel): SVR dùng hàm nhân RBF để chiếu dữ liệu lên không gian đặc trưng nhiều chiều:
  $$K(x_i, x_j) = \\exp\\left(-\\gamma \\|x_i - x_j\\|^2\\right)$$
  Với $\\gamma$ là tham số độ rộng của hàm nhân.
- Nghiên cứu Thực nghiệm của Hamedi et al. (2019):
  - Nhóm tác giả áp dụng mô hình máy véc-tơ hỗ trợ bình phương tối thiểu (LSSVM).
  - Biến đổi Toán học: LSSVM thay thế các bất đẳng thức ràng buộc bằng hệ phương trình đại số tuyến tính:
    $$\\begin{bmatrix} 0 & \\mathbf{1}^T \\\\ \\mathbf{1} & \\mathbf{\\Omega} + \\gamma^{-1} \\mathbf{I} \\end{bmatrix} \\begin{bmatrix} b \\\\ \\mathbf{\\alpha} \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ \\mathbf{y} \\end{bmatrix}$$
    Trong đó $\\mathbf{\\Omega}_{ij} = K(x_i, x_j)$. Vector $\\mathbf{\\alpha}$ là nhân tử Lagrange. Tham số $b$ là hệ số chệch.
  - Biến đầu vào gồm: MLSS, $TMP$, thông lượng lọc $J$ và nhiệt độ nước $T$.
  - Biến đầu ra: Trở lực lọc màng ($R_t$).
  - Đối sánh Hiệu năng: LSSVM đạt $R^2 = 0.99$.
  - LSSVM vượt trội hơn mô hình lai PSO-MLP ($R^2 = 0.96$).
  - LSSVM vượt trội hơn mô hình lập trình biểu thức gen GEP ($R^2 = 0.98$).
- Ưu thế Kỹ thuật của SVM/LSSVM: Khả năng khái quát hóa vượt trội trên tập dữ liệu kích thước nhỏ và vừa. Thuật toán tìm ra nghiệm cực tiểu toàn cục duy nhất.

#### 5.3.2 Rừng Ngẫu nhiên (Random Forest) và Các Cây Quyết định Phân cấp
- Nguyên lý Hoạt động của Random Forest (RF):
  - RF là phương pháp học tổ hợp (Ensemble learning) dựa trên kỹ thuật đóng bao (Bagging) từ nhiều cây quyết định.
  - Thuật toán chọn ngẫu nhiên tập dữ liệu con có hoàn lại (bootstrap). Thuật toán cũng chọn ngẫu nhiên tập đặc trưng con tại mỗi điểm phân nhánh.
- Nghiên cứu Thực nghiệm của Li et al. (2020):
  - Cấu trúc Mô hình: Mô hình RF thiết lập 300 cây quyết định với 2 biến đặc trưng tại mỗi nút phân chia.
  - Tiền xử lý bằng Phân tích Thành phần Chính (PCA): Tác giả dùng PCA để sàng lọc biến và loại bỏ đa cộng tuyến (multicollinearity).
  - Biến đầu vào chọn lọc gồm nồng độ MLSS, áp suất $TMP$ và trở lực màng.
  - Biến đầu ra: Thông lượng lọc màng ($J$).
  - Đối sánh Hiệu năng: Mô hình RF đạt $R^2 = 0.95$. RF vượt trội hơn mô hình SVM ($R^2 = 0.92$) và mô hình MLP ($R^2 = 0.89$).
- Định lượng Mức độ Quan trọng của Đặc trưng (Feature Importance):
  - RF cung cấp chỉ số suy giảm độ tinh khiết Gini hoặc sai số mẫu ngoài bao (Out-Of-Bag Importance).
  - Kết quả phân tích chứng minh protein và polysaccharide trong SMP và EPS đóng vai trò chi phối tăng trở lực màng.
  - Đặc tính Mô hình: RF xử lý tốt dữ liệu đa chiều và phi tuyến. RF không đòi hỏi phân phối chuẩn của dữ liệu.

#### 5.3.3 Các Mô hình Lai Thông minh Kết hợp Giải thuật Siêu phỏng sinh (Metaheuristic Hybrid AI)
- 1. Mô hình Lai GA-BP (Genetic Algorithm kết hợp BPNN):
  - Cơ chế Hoạt động: Giải thuật di truyền (GA) mô phỏng tiến hóa tự nhiên gồm chọn lọc, lai ghép và đột biến.
  - GA tìm kiếm toàn cục để xác định trọng số khởi tạo $W_0$ và ngưỡng lệch $b_0$ tối ưu cho mạng BPNN.
  - Khắc phục Nhược điểm: GA loại bỏ sự phụ thuộc khởi tạo ngẫu nhiên của BPNN. Thuật toán giúp mạng tránh rơi vào cực tiểu cục bộ.
  - Bằng chứng Thực nghiệm: Wang và Wu (2015) và Mirbagheri et al. (2015b) chứng minh GA-BP đạt $R^2 > 0.98$. Mô hình tăng tốc độ hội tụ và giảm độ nhạy với nhiễu.
- 2. Mô hình Lai PSO-BP (Particle Swarm Optimization kết hợp BPNN):
  - Cơ chế Hoạt động: Thuật toán tối ưu hóa bầy hạt (PSO) mô phỏng hành vi di chuyển bầy đàn của chim hoặc cá. Mỗi hạt tương ứng với một bộ tham số mạng nơ-ron.
  - Phương trình Cập nhật Vận tốc và Vị trí của Hạt:
    $$v_{i, d}^{(t+1)} = w \\cdot v_{i, d}^{(t)} + c_1 r_1 \\left(pbest_{i, d} - x_{i, d}^{(t)}\\right) + c_2 r_2 \\left(gbest_d - x_{i, d}^{(t)}\\right)$$
    $$x_{i, d}^{(t+1)} = x_{i, d}^{(t)} + v_{i, d}^{(t+1)}$$
    Trong đó: $w$ là trọng số quán tính. Ký hiệu $c_1, c_2$ là các hệ số gia tốc học tập cá nhân và xã hội. Ký hiệu $r_1, r_2$ là các số ngẫu nhiên phân bố trong đoạn $[0, 1]$. Ký hiệu $pbest_i$ là vị trí tốt nhất của cá nhân hạt $i$. Ký hiệu $gbest$ là vị trí tốt nhất của toàn bầy hạt.
  - Ứng dụng Thực nghiệm: Hamedi et al. (2019) dùng PSO tối ưu cấu trúc MLP đạt $R^2 = 0.97$. Tao và Li (2018) kết hợp PSO với mạng Fuzzy-RBFNN đạt sai số $MAPE = 0.0287$.
- 3. Hệ Suy luận Mờ Thích ứng Nơ-ron (ANFIS - Adaptive Neuro-Fuzzy Inference System):
  - Cơ chế Tích hợp: ANFIS kết hợp cấu trúc suy luận mờ Takagi-Sugeno-Kang (TSK) với khả năng tự học của mạng nơ-ron. Mô hình chuyển đổi dữ liệu cảm biến thành các luật mờ IF-THEN dễ hiểu.
  - Cấu trúc 5 Tầng Chức năng của ANFIS:
    - Tầng 1 (Tầng Mờ hóa): Tính toán độ thuộc của biến đầu vào qua hàm liên thuộc dạng Gauss hoặc Bell:
      $$O_{1, i} = \\mu_{A_i}(x) = \\exp\\left(-\\frac{1}{2}\\left(\\frac{x - c_i}{\\sigma_i}\\right)^2\\right)$$
    - Tầng 2 (Tầng Tính Luật Mờ): Thực hiện phép nhân logic để xác định độ kích hoạt của từng luật:
      $$O_{2, i} = w_i = \\mu_{A_i}(x) \\cdot \\mu_{B_i}(y)$$
    - Tầng 3 (Tầng Chuẩn hóa Trọng số Luật): Tính toán tỷ lệ kích hoạt tương đối của từng luật:
      $$O_{3, i} = \\bar{w}_i = \\frac{w_i}{\\sum_{k} w_k}$$
    - Tầng 4 (Tầng Kết luận Luật): Tính giá trị đầu ra của từng luật tuyến tính con:
      $$O_{4, i} = \\bar{w}_i f_i = \\bar{w}_i \\left(p_i x + q_i y + r_i\\right)$$
    - Tầng 5 (Tầng Giải mờ Tổng hợp): Tính toán đầu ra cuối cùng bằng phép cộng dồn tất cả các luật:
      $$O_{5, 1} = y = \\sum_{i} \\bar{w}_i f_i$$
  - Bằng chứng Thực nghiệm: Taheri et al. (2021) áp dụng ANFIS để dự đoán $TMP$ từ OLR, pH, MLSS và MLVSS với $R^2 = 0.98$.
  - Ưu điểm Nổi bật: ANFIS cung cấp tính minh bạch cơ chế rất cao. Kỹ sư vận hành có thể đọc hiểu và hiệu chỉnh trực tiếp các luật mờ chuyên gia.
- 4. Mạng Nơ-ron Sóng kết hợp Giải thuật Đàn dơi (BA-WNN):
  - Zhao et al. (2020) áp dụng giải thuật dơi (Bat Algorithm - BA) để tối ưu hóa mạng nơ-ron Bandelet. Thuật toán này mô phỏng cơ chế định vị bằng sóng siêu âm.
  - Mô hình dự đoán chính xác cả thông lượng $J$ và tỷ lệ phục hồi $FRR$ với sai số chỉ $3.2\\%$.

#### 5.3.4 Bàn luận Kỹ thuật: Quy mô Mẫu Dữ liệu, Đa cộng tuyến và Khả thi Vận hành Trực tuyến
- Độ nhạy với Quy mô Mẫu Dữ liệu (Sample Size Impact):
  - Các mạng nơ-ron sâu và MLP đòi hỏi số lượng mẫu dữ liệu lớn để đạt độ khái quát hóa cao.
  - Khi tập mẫu huấn luyện nhỏ ($N < 100$), mô hình MLP kém ổn định hơn mô hình toán truyền thống (Wang và Wu, 2015).
  - Khi dữ liệu hạn chế, các mô hình SVM, LSSVM và Random Forest đạt độ ổn định cao hơn. Các mô hình này không bị quá khớp.
- Hiện tượng Đa cộng tuyến giữa các Biến Môi trường (Multicollinearity):
  - Tương quan Chéo: Các thông số bùn như MLSS, COD, pH, độ nhớt, EPS và SMP thường tương quan chặt chẽ với nhau.
  - Đưa toàn bộ các biến này vào mô hình dễ gây đa cộng tuyến và làm sai lệch trọng số hồi quy.
  - Giải pháp Kỹ thuật: Sử dụng PCA hoặc phân tích độ nhạy để loại bỏ đặc trưng dư thừa trước khi huấn luyện (Li et al., 2020).
- Thách thức và Định hướng Quan trắc Trực tuyến (Online Real-time Monitoring):
  - Hạn chế Đo đạc: Nhiều nghiên cứu phụ thuộc vào các biến ngoại tuyến như SMP, EPS hoặc góc tiếp xúc bề mặt. Các chỉ tiêu này không thể đo liên tục ngoài hiện trường.
  - Định hướng Thực tế: Mô hình điều khiển tự động thời gian thực cần ưu tiên các biến đo được bằng cảm biến trực tuyến.
  - Biến Trực tuyến Khả thi: Các biến gồm $TMP$, thông lượng $J$, tốc độ tăng áp $dTMP/dt$, độ dẫn điện EC, pH, DO, nhiệt độ $T$ và sục khí màng.
"""

target_path = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\branche\machine_learning_for_membrane_bioreactor\fragments\ch05_ung_dung_du_doan_tac_nghen_mang_branches.md"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Successfully wrote {len(content.strip().splitlines())} lines to {target_path}")
