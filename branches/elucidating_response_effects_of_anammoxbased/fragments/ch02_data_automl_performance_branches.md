## Chương 2: Đặc tính dữ liệu lớn và Hiệu năng dự đoán của AutoML

### 2.1 Phân tích thống kê các quy trình khử nitơ dựa trên Anammox

#### 2.1.1 So sánh chế độ vận hành: Bể mẻ và bể dòng liên tục
- Tập dữ liệu y văn gồm 2940 mẫu thu thập từ 28 công trình nghiên cứu độc lập.
- Biểu đồ hộp (box plots) thể hiện sự phân bố dữ liệu giữa các nhóm quy trình. Các điểm dị biệt (outliers) chỉ ra sự sai lệch đáng kể đôi khi xảy ra giữa các thí nghiệm độc lập.
- So sánh hiệu suất khử tổng nitơ vô cơ (TIN removal efficiency):
  + Bể mẻ (sequencing batch) đạt trung vị hiệu suất $78.18\%$.
  + Bể dòng liên tục (continuous flow) đạt trung vị hiệu suất $74.81\%$.
- Tính ổn định động học: Bể mẻ duy trì độ ổn định vận hành cao hơn đối với NLR, NiRR, NARR và NRR.
- Khả năng xử lý tải trọng cực cao ở bể dòng liên tục:
  + Các hệ thống UASB và EGSB vận hành liên tục ghi nhận các dải thông số động học cực đại:
    * Tải trọng nạp nitơ (NLR): $2.91 - 7.55\text{ kg N/m}^3\text{/d}$.
    * Tốc độ phản ứng nit hóa bởi vi khuẩn AOB (NiRR): $0.33 - 2.53\text{ kg N/m}^3\text{/d}$.
    * Tốc độ khử nitơ qua con đường Anammox (NARR): $0.02 - 3.92\text{ kg N/m}^3\text{/d}$.
    * Tốc độ khử tổng nitơ (NRR): $2.63 - 6.55\text{ kg N/m}^3\text{/d}$.
  + Cơ chế tạo tải trọng cao: Sự kết hợp giữa nồng độ nitơ đầu vào cao và thời gian lưu thủy lực (HRT) ngắn tạo điều kiện đẩy mạnh tải trọng xử lý (Du et al., 2016, Wang et al., 2024b).

#### 2.1.2 So sánh hình thái sinh khối: Bùn bông và bùn hạt
- Sự khác biệt về tải trọng vận hành giữa bùn bông (floc) và bùn hạt (aggregate) tương đồng với sự khác biệt giữa bể mẻ và bể dòng liên tục.
- Bùn hạt trong bể liên tục duy trì mức NLR rất cao.
- Khả năng giữ sinh khối mật độ cao của cấu trúc bùn hạt giúp ngăn ngừa rửa trôi vi sinh vật ở HRT ngắn.
- Dạng bùn hạt trong bể dòng liên tục thể hiện tiềm năng vượt trội để xử lý các nguồn nước thải nồng độ nitơ cao (Trigo et al., 2006, Tang et al., 2011).

#### 2.1.3 So sánh nguồn cơ chất: Nước thải nhân tạo và nước thải đô thị
- Đặc tính dòng ra giữa nước thải nhân tạo (synthetic wastewater) và nước thải đô thị (municipal wastewater) có sự tương đồng tổng thể.
- Mức độ ổn định động học trong vận hành:
  + Thí nghiệm dùng nước thải đô thị duy trì NLR, NiRR, NARR và NRR ổn định hơn.
  + Nguyên nhân: Đặc tính thành phần của nước thải đô thị tương đối đồng nhất giữa các nghiên cứu khác nhau (Luan et al., 2022, Wang et al., 2022a, Liu et al., 2024, Zhang et al., 2024).
- Biên độ biến thiên của nước thải nhân tạo:
  + Nước thải nhân tạo ghi nhận dải dao động nồng độ đầu vào rất rộng đối với COD, $\text{NH}_4^+-\text{N}$ và $\text{NO}_3^--\text{N}$ (Du et al., 2016, Wang et al., 2024b, Sobotka et al., 2024, Yang et al., 2024).
- Phân tích khám phá dữ liệu (EDA):
  + Biểu đồ EDA phân bố dữ liệu nước thải nhân tạo chiếm các vùng không gian rộng hơn ở các cặp biến: C/N so với $\text{NH}_4^+-\text{N}$ vào, C/N so với TIN vào, COD vào so với $\text{NH}_4^+-\text{N}$ vào, và COD vào so với TIN vào.
  + Các điểm dữ liệu của nước thải nhân tạo phân bố tập trung quanh các giá trị thiết kế cố định và ít dao động ngẫu nhiên.
  + Trái lại, nước thải đô thị thực tế luôn biến động mạnh theo thời gian thực (Jenni et al., 2014, Lackner et al., 2014).
  + Khuyến nghị kỹ thuật: Các nghiên cứu sử dụng nước thải nhân tạo cần bổ sung các kịch bản biến động nồng độ thực tế để nâng cao tính khả thi khi chuyển giao công nghệ.
- Phân bố dạng nitơ trong nước thải đô thị:
  + Nồng độ $\text{NH}_4^+-\text{N}$ thường chiếm trên $90\%$ tổng nồng độ TIN đầu vào trong nước thải đô thị thực tế (Zhang et al., 2024, Liu et al., 2023b).
  + Nồng độ $\text{NH}_4^+-\text{N}$ đầu vào và TIN đầu vào thể hiện mối tương quan cặp đôi tương đồng khi so sánh với các biến số vận hành khác.

#### 2.1.4 So sánh cấu hình công nghệ: Quy trình PNA, PDA và PNA kết hợp PDA
- Sự phân hóa hiệu suất khử nitơ giữa các quy trình Anammox:
  + Quy trình PNA và quy trình tích hợp PNA kết hợp PDA đạt hiệu suất khử TIN cao hơn rõ rệt so với quy trình PDA đơn thuần.
- Phân tích tương quan tuyến tính Pearson (PPMC):
  + Cả ba quy trình đều ghi nhận tương quan thuận giữa nồng độ đầu vào ($\text{NH}_4^+-\text{N}$ vào, TIN vào, NLR) và nồng độ đầu ra ($\text{NH}_4^+-\text{N}$ ra, $\text{NO}_2^--\text{N}$ ra, TIN ra).
  + Quy trình PNA thể hiện mối tương quan thuận mạnh nhất với hệ số Pearson đạt $r = 0.55 - 0.95$.
- Cơ chế kiểm soát sinh học trong quy trình PNA:
  + Vận hành PNA đòi hỏi ức chế triệt để vi khuẩn oxy hóa nitrit (NOB) và kích hoạt vi khuẩn oxy hóa amoni (AOB) (Klaus et al., 2017).
  + Hoạt tính của NOB và AOB chịu tác động trực tiếp từ nồng độ cơ chất nền bao gồm $\text{NO}_2^--\text{N}$, $\text{NH}_4^+-\text{N}$ và COD (Sinha and Annachhatre, 2007, Soliman and Eldyasti, 2018).
  + Sự nhạy cảm này tạo ra liên kết chặt chẽ giữa các biến đầu vào và đầu ra trong hệ PNA.

#### 2.1.5 Phân tích tương quan PPMC và loại bỏ đa cộng tuyến
- Ma trận PPMC cho toàn bộ 24 biến số (biến phân loại và biến liên tục) thể hiện mối tương quan cặp đôi mạnh giữa loại nước thải đầu vào, chủng vi khuẩn Anammox chiếm ưu thế, $\text{NO}_3^--\text{N}$ đầu vào và TIN đầu vào.
- Ngoại trừ mối tương quan tuyến tính mạnh giữa $\text{NH}_4^+-\text{N}$ đầu vào và TIN đầu vào, các biến đầu vào tiềm năng không xuất hiện hiện tượng đa cộng tuyến (multicollinearity).
- Kết luận lựa chọn đặc trưng: 15 biến vận hành hoàn toàn đáp ứng tiêu chuẩn để xây dựng các mô hình học máy dự đoán chính xác (Al-Duais et al., 2024).

---

### 2.2 Đánh giá mô hình dự đoán trên tập dữ liệu y văn (Table 1)

#### 2.2.1 Cấu hình không gian đặc trưng và phân chia tập dữ liệu huấn luyện
- Không gian 15 biến đầu vào bao gồm:
  + 6 biến phân loại: chế độ vận hành (operation condition), hình thái bùn (sludge morphology), loại nước thải đầu vào (influent type), chiến lược làm giàu sinh khối (enrichment strategy), loại quy trình Anammox (process type), chủng vi khuẩn Anammox chiếm ưu thế (dominant anammox bacteria).
  + 9 biến liên tục: thời gian vận hành (operation time), thời gian lưu thủy lực (HRT), tỷ lệ C/N, COD đầu vào, $\text{NH}_4^+-\text{N}$ đầu vào, $\text{NO}_3^--\text{N}$ đầu vào, $\text{NO}_2^--\text{N}$ đầu vào, TIN đầu vào, tải trọng NLR.
- 7 biến mục tiêu đầu ra được mô hình hóa độc lập:
  + Nồng độ dòng ra $\text{NH}_4^+-\text{N}$ ($\text{mg/L}$)
  + Nồng độ dòng ra $\text{NO}_3^--\text{N}$ ($\text{mg/L}$)
  + Nồng độ dòng ra $\text{NO}_2^--\text{N}$ ($\text{mg/L}$)
  + Nồng độ dòng ra TIN ($\text{mg/L}$)
  + Hiệu suất loại bỏ $\text{NH}_4^+-\text{N}$ ($\%$)
  + Hiệu suất loại bỏ TIN ($\%$)
  + Tốc độ khử nitơ Anammox NARR ($\text{kg N/m}^3\text{/d}$)
- Chiến lược phân chia tập dữ liệu:
  + Tổng số 2940 mẫu dữ liệu được phân chia ngẫu nhiên: 70% huấn luyện (training: 2070 mẫu), 15% kiểm thực (validation: 441 mẫu), 15% kiểm tra (testing: 441 mẫu).
  + Tỷ số kích thước mẫu trên số lượng đặc trưng:
    $$\text{SFR} = \frac{2070}{15} = 138$$
  + Tỷ số $\text{SFR} \ge 100$ đảm bảo độ tin cậy thống kê cao và ngăn ngừa hiện tượng không hội tụ dữ liệu.
- Thiết lập quy trình AutoML trên nền tảng H2O AutoML:
  + Tự động tối ưu hóa các thuật toán: DRF, XRT, GLM với chuẩn hóa chính quy, XGBoost, GBM, DNN.
  + Áp dụng tìm kiếm ngẫu nhiên nhanh kết hợp kiểm thực chéo 5 lần (5-fold cross-validation).
  + Giới hạn vận hành: tối đa 200 mô hình, thời gian tối đa 900 s.
  + Đánh giá qua 5 seeds phân chia dữ liệu ngẫu nhiên để loại bỏ sai số do chia tập dữ liệu.

#### 2.2.2 Cơ chế ưu việt của các thuật toán Boosting (GBM và XGBoost)
- Các thuật toán dạng GBM (GBM và XGBoost) chiếm ưu thế tuyệt đối về độ chính xác dự đoán trên tất cả 7 biến mục tiêu đầu ra.
- Cơ chế kỹ thuật tạo nên tính ưu việt của họ Boosting:
  + Tích hợp kỹ thuật chính quy hóa (regularization) mạnh mẽ giúp kiểm soát độ phức tạp của cây và chống quá khớp (overfitting).
  + Cơ chế tự động xử lý các giá trị dữ liệu khuyết thiếu (built-in missing value handling).
  + Thuật toán cắt tỉa cây hiệu quả (efficient tree pruning algorithms) ngăn chặn phân nhánh dư thừa.
  + Kiến trúc tính toán song song (parallel processing) tối ưu hóa tốc độ thực thi trên tập dữ liệu lớn.
  + Phương pháp xử lý dữ liệu mất cân bằng tiên tiến giúp duy trì độ chính xác đồng đều trên toàn dải dữ liệu.

#### 2.2.3 Bảng tổng hợp hiệu năng dự đoán trên tập dữ liệu y văn (Table 1)
Toàn bộ kết quả đối sánh hiệu năng dự đoán của các mô hình tối ưu được trích xuất trực tiếp từ Bảng 1:

| Mục tiêu dự đoán (Predicted target) | Mô hình tối ưu (Optimized model) | Huấn luyện MAE (Training MAE) | Huấn luyện $R^2$ (Training $R^2$) | Kiểm thực MAE (Validation MAE) | Kiểm thực $R^2$ (Validation $R^2$) | Kiểm tra MAE (Testing MAE) | Kiểm tra $R^2$ (Testing $R^2$) | Đơn vị đo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\text{NH}_4^+-\text{N}$ dòng ra | GBM | 0.171 | 0.994 | 1.951 | 0.914 | 1.889 | 0.928 | $\text{mg/L}$ |
| $\text{NO}_3^--\text{N}$ dòng ra | XGBoost | 0.048 | 0.998 | 1.677 | 0.727 | 1.626 | 0.824 | $\text{mg/L}$ |
| $\text{NO}_2^--\text{N}$ dòng ra | XGBoost | 0.004 | 0.999 | 0.546 | 0.949 | 0.496 | 0.962 | $\text{mg/L}$ |
| $\text{TIN}$ dòng ra | XGBoost | 0.215 | 0.996 | 3.141 | 0.916 | 3.366 | 0.910 | $\text{mg/L}$ |
| Hiệu suất loại bỏ $\text{NH}_4^+-\text{N}$ | XGBoost | 0.305 | 0.996 | 3.638 | 0.832 | 3.975 | 0.882 | $\%$ |
| Hiệu suất loại bỏ $\text{TIN}$ | XGBoost | 0.320 | 0.991 | 5.583 | 0.731 | 5.252 | 0.814 | $\%$ |
| Tốc độ khử nitơ Anammox (NARR) | XGBoost | 0.002 | 0.999 | 0.013 | 0.981 | 0.014 | 0.993 | $\text{kg N/m}^3\text{/d}$ |

#### 2.2.4 Phân tích chi tiết hiệu năng từng chỉ tiêu đầu ra
- Đánh giá trên tập huấn luyện (Training dataset):
  + Giá trị MAE đạt mức cực thấp trên toàn bộ các chỉ tiêu.
  + Hệ số xác định $R^2$ huấn luyện nằm trong dải tuyệt đối $0.991 - 0.999$.
  + Kết quả này khẳng định tập dữ liệu lớn thu thập từ y văn có chất lượng cao và khả năng huấn luyện xuất sắc.
- Đánh giá trên tập kiểm thực (Validation dataset):
  + Hiệu năng tập kiểm thực suy giảm tự nhiên so với tập huấn luyện nhưng vẫn đáp ứng tốt yêu cầu kỹ thuật với $R^2 = 0.727 - 0.981$.
  + Giá trị $R^2$ thấp nhất xuất hiện ở chỉ tiêu $\text{NO}_3^--\text{N}$ dòng ra ($R^2 = 0.727$) và hiệu suất khử TIN ($R^2 = 0.731$).
- Đánh giá trên tập kiểm tra (Testing dataset):
  + Hiệu năng tập kiểm tra đạt mức rất cao với $R^2 = 0.814 - 0.993$.
  + Chỉ số $R^2$ tập kiểm tra cao hơn tập kiểm thực do thuật toán xếp hạng bảng dẫn đầu (leaderboard) dựa trực tiếp trên kết quả kiểm tra độc lập.
  + Mô hình dự đoán NARR bằng XGBoost đạt hiệu năng vượt trội nhất với $\text{Testing MAE} = 0.014\text{ kg N/m}^3\text{/d}$ và $\text{Testing } R^2 = 0.993$.
  + Mô hình dự đoán $\text{NO}_2^--\text{N}$ dòng ra bằng XGBoost đạt $\text{Testing MAE} = 0.496\text{ mg/L}$ và $\text{Testing } R^2 = 0.962$.

---

### 2.3 Kiểm định mô hình trên tập dữ liệu thực nghiệm độc lập (Table 2)

#### 2.3.1 Thiết kế hệ thực nghiệm UASB PDA kiểm chứng độc lập
- Mô hình phản ứng thực nghiệm:
  + Bể phản ứng dòng hướng lên qua tầng bùn kỵ khí (UASB) ứng dụng quy trình PDA.
  + Dung tích làm việc hiệu dụng: $5.72\text{ L}$.
  + Chế độ nhiệt độ: Duy trì liên tục ở $35^\circ\text{C}$ nhờ bể điều nhiệt.
  + Thời gian lưu thủy lực (HRT): Cố định ở $4\text{ h}$.
- Đặc tính sinh khối cấy:
  + Bùn bông khử nitrat một phần (PD flocculent sludge) thu hồi từ bể PD dùng glycerol vận hành dài hạn.
  + Bùn hạt Anammox thuần thục (mature anammox granular sludge) lấy từ bể UASB Anammox.
  + Tỷ lệ phối trộn sinh khối cấy ban đầu: $1:5$ (bùn bông PD : bùn hạt Anammox).
- Quy trình vận hành và tập dữ liệu kiểm chứng:
  + Bể vận hành liên tục trong 185 ngày qua 6 giai đoạn với các điều kiện nước thải nhân tạo khác nhau.
  + Toàn bộ 185 mẫu dữ liệu đo đạc thực tế cấu thành tập dữ liệu chưa từng thấy (unseen experimental dataset).
  + Toàn bộ mô hình tối ưu đã huấn luyện từ 2070 mẫu y văn được đưa vào kiểm định trực tiếp trên 185 mẫu này mà không trải qua quá trình tinh chỉnh lại (fine-tuning).

#### 2.3.2 Bảng kiểm định mô hình trên tập dữ liệu thực nghiệm chưa từng thấy (Table 2)
Toàn bộ dữ liệu kiểm nghiệm thực tế từ Bảng 2 được trích xuất chi tiết:

| Mục tiêu dự đoán (Predicted target) | Mô hình tối ưu (Optimized model) | Sai số tuyệt đối trung bình (MAE) | Hệ số xác định ($R^2$) | Đơn vị đo |
| :--- | :--- | :--- | :--- | :--- |
| $\text{NH}_4^+-\text{N}$ dòng ra | GBM | 1.686 | 0.945 | $\text{mg/L}$ |
| $\text{NO}_3^--\text{N}$ dòng ra | XGBoost | 2.196 | 0.725 | $\text{mg/L}$ |
| $\text{NO}_2^--\text{N}$ dòng ra | GBM | 1.045 | 0.563 | $\text{mg/L}$ |
| $\text{TIN}$ dòng ra | GBM | 3.407 | 0.899 | $\text{mg/L}$ |
| Hiệu suất loại bỏ $\text{NH}_4^+-\text{N}$ | GBM | 4.514 | 0.867 | $\%$ |
| Hiệu suất loại bỏ $\text{TIN}$ | GBM | 3.375 | 0.882 | $\%$ |
| Tốc độ khử nitơ Anammox (NARR) | Deep learning | 0.013 | 0.677 | $\text{kg N/m}^3\text{/d}$ |

#### 2.3.3 Phân tích hiệu năng tổng quát hóa và so sánh chuẩn đối sánh
- Năng lực dự báo các thông số nitơ cốt lõi:
  + Các mô hình đạt độ chính xác dự đoán cao ($R^2 = 0.725 - 0.945$) đối với 5 chỉ tiêu quan trọng: $\text{NH}_4^+-\text{N}$ dòng ra ($R^2 = 0.945$), $\text{NO}_3^--\text{N}$ dòng ra ($R^2 = 0.725$), $\text{TIN}$ dòng ra ($R^2 = 0.899$), hiệu suất khử $\text{NH}_4^+-\text{N}$ ($R^2 = 0.867$) và hiệu suất khử $\text{TIN}$ ($R^2 = 0.882$).
- Đối sánh hiệu năng dự đoán nitrit ($\text{NO}_2^--\text{N}$):
  + Mô hình GBM đạt giá trị $\text{MAE} = 1.045\text{ mg/L}$ ($R^2 = 0.563$).
  + So sánh chuẩn đối sánh: Kết quả này vượt trội đáng kể so với mô hình cây hồi quy kết hợp (ensemble regression trees) của Huang et al. (2023) với $\text{MAE} = 3.428\text{ mg/L}$.
  + Mô hình hiện tại đạt sai số thấp hơn nhiều dù mô hình của Huang et al. (2023) phải sử dụng thêm nhiều biến đo đạc trực tiếp (ngày vận hành, $\text{NH}_4^+-\text{N}$ vào, $\text{NO}_2^--\text{N}$ vào, pH dòng ra, DO dòng ra).
- Năng lực dự báo động học Anammox (NARR):
  + Thuật toán Deep learning đạt giá trị $\text{MAE} = 0.013\text{ kg N/m}^3\text{/d}$ và $R^2 = 0.677$.
  + Đường giá trị dự báo của mô hình bám sát chặt chẽ xu thế dao động thực tế của phản ứng Anammox trong suốt 185 ngày vận hành.

#### 2.3.4 Nguyên nhân gây suy giảm độ chính xác cục bộ tại các chỉ tiêu nhạy cảm
- Độ chính xác dự đoán của $\text{NO}_2^--\text{N}$ dòng ra ($R^2 = 0.563$) và NARR ($R^2 = 0.677$) thấp hơn so với các chỉ tiêu nitơ khác do ba nguyên nhân cơ chế chính:
  1. Hiện tượng biến động mạnh và bất ổn định cục bộ: Nồng độ $\text{NO}_2^--\text{N}$ và giá trị NARR trong các thí nghiệm Anammox có biên độ dao động và tính chất tạo bông/kết tụ không đồng đều rất lớn giữa các chu kỳ phản ứng.
  2. Lan truyền sai số trong tính toán gián tiếp: Tốc độ NARR không được đo trực tiếp bằng cảm biến. NARR được tính toán thông qua công thức toán học kết hợp nhiều biến số nồng độ và lưu lượng. Sai số đo đạc từ từng biến thành phần bị tích lũy và khuếch đại trong giá trị NARR cuối cùng.
  3. Thiếu hụt các biến số cơ chế nhạy cảm trong tập dữ liệu tổng hợp:
     * Dữ liệu y văn thiếu vắng các thông số động học vi sinh quan trọng như độ pH theo thời gian thực và nồng độ oxy hòa tan (DO).
     * Dữ liệu không ghi nhận đầy đủ sự hiện diện của các chất hữu cơ gây ức chế chuyên biệt đối với vi khuẩn Anammox và vi khuẩn khử nitrat.
- Kết luận chung về khả năng tổng quát hóa:
  + Mặc dù có sự suy giảm độ chính xác cục bộ ở hai chỉ tiêu nhạy cảm, các mô hình tối ưu từ H2O AutoML vẫn mô phỏng chính xác xu thế biến thiên thực nghiệm.
  + Kết quả kiểm chứng trên tập dữ liệu hoàn toàn chưa từng thấy chứng minh các mô hình học máy xây dựng từ dữ liệu lớn y văn có năng lực tổng quát hóa (generalization ability) vượt trội trong việc kiểm soát và tối ưu hóa các quy trình khử nitơ dựa trên Anammox.
