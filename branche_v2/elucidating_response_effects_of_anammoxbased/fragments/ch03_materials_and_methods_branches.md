## Materials and methods

### Data sources and analysis methods
- Thu thập dữ liệu từ y văn thông qua tìm kiếm trên cơ sở dữ liệu Web of Science nhằm làm sáng tỏ các mối quan hệ nội tại giữa các yếu tố trong quy trình khử nitơ dựa trên anammox (anammox-based nitrogen removal processes):
  - Các từ khóa tìm kiếm bao gồm: "Anaerobic ammonia oxidation", "mainstream anammox", "municipal wastewater", "partial nitrification", và "partial denitrification".
  - Tuyển chọn được $28$ nghiên cứu đáp ứng tiêu chí chứa đầy đủ và nhất quán các biến số liên quan đến quy trình anammox (Table S9).
  - So sánh với nghiên cứu phân tích gộp (meta-analysis) của Liu et al. (2020) thu thập dữ liệu từ $62$ nghiên cứu nhưng chưa xét đến các thông số vận hành như thời gian lưu thủy lực ($\text{HRT}$) và tải trọng nạp nitơ ($\text{NLR}$) vốn được sử dụng làm biến đầu vào trong nghiên cứu này.
- Tập dữ liệu tổng hợp gồm $2940$ mẫu từ các loại quy trình anammox khác nhau được thu thập và số hóa bằng phần mềm Origin:
  - $1927$ mẫu thuộc quy trình khử nitrat một phần kết hợp anammox ($\text{PDA}$).
  - $282$ mẫu thuộc quy trình nitrat hóa một phần kết hợp anammox ($\text{PNA}$).
  - $731$ mẫu thuộc quy trình kết hợp cả $\text{PDA}$ và $\text{PNA}$.
- Hệ thống biến số then chốt được phân loại và quản lý (Table S1):
  - Điều kiện vận hành ($\text{operation condition}$): vận hành mẻ nối tiếp ($\text{sequencing batch}$) hoặc dòng liên tục ($\text{continuous flow}$).
  - Hình thái bùn ($\text{sludge morphology}$): bùn bông ($\text{floc}$) hoặc bùn hạt kết tụ ($\text{aggregates}$).
  - Loại nước thải đầu vào ($\text{influent type}$): nước thải tổng hợp ($\text{synthetic wastewater}$) hoặc nước thải sinh hoạt đô thị ($\text{municipal wastewater}$).
  - Chiến lược làm giàu vi sinh ($\text{enrichment strategy}$): tự làm giàu ($\text{self-enrichment}$) hoặc cấy giống vi sinh ($\text{inoculation}$).
  - Loại quy trình anammox ($\text{anammox-based process type}$): $\text{PNA}$, $\text{PDA}$, hoặc $\text{PNA}$ kết hợp $\text{PDA}$.
  - Chi vi khuẩn anammox chiếm ưu thế ($\text{genera of dominant anammox bacteria}$).
  - Thời gian vận hành ($\text{operation time}$): tính theo ngày ($\text{d}$).
  - Thời gian lưu thủy lực ($\text{HRT}$): tính theo giờ ($\text{h}$).
  - Tỷ lệ carbon trên nitơ ($\text{C/N}$).
  - Các chỉ tiêu nước thải đầu vào: nhu cầu oxy hóa học ($\text{COD}$, $\text{mg/L}$), $\text{NH}_4^+-\text{N}$ ($\text{mg/L}$), $\text{NO}_3^--\text{N}$ ($\text{mg/L}$), $\text{NO}_2^--\text{N}$ ($\text{mg/L}$), và tổng nitơ vô cơ ($\text{TIN}$, $\text{mg/L}$).
  - Các chỉ tiêu nước thải đầu ra: $\text{NH}_4^+-\text{N}$ ($\text{mg/L}$), $\text{NO}_3^--\text{N}$ ($\text{mg/L}$), $\text{NO}_2^--\text{N}$ ($\text{mg/L}$), và $\text{TIN}$ ($\text{mg/L}$).
- Tính toán $6$ chỉ số toán học mô tả hiệu năng xử lý theo các công thức quy định tại Supporting Information (Text S1 [25]):
  - Tải trọng nạp nitơ: $\text{NLR}$ ($\text{kg/m}^3/\text{d}$).
  - Hiệu suất loại bỏ amoni: $\text{NH}_4^+-\text{N}$ removal efficiency ($\%$).
  - Hiệu suất loại bỏ tổng nitơ vô cơ: $\text{TIN}$ removal efficiency ($\%$).
  - Tốc độ phản ứng nitrat hóa bởi vi khuẩn oxy hóa amoniac ($\text{AOB}$): $\text{NiRR}$ ($\text{nitrification reaction rate by ammonia oxidation bacteria}$).
  - Tốc độ loại bỏ nitơ qua con đường phản ứng anammox: $\text{NARR}$ ($\text{nitrogen removal rate through the anammox reaction pathway}$).
  - Tốc độ loại bỏ nitơ tổng thể: $\text{NRR}$ ($\text{nitrogen removal rate}$).
- Phân tích sơ bộ mối quan hệ giữa các biến số thông qua biểu đồ hộp ($\text{box plots}$), phân tích dữ liệu khám phá ($\text{EDA}$ - Exploratory Data Analysis), và hệ số tương quan tích - mômen Pearson ($\text{PPMC}$ - Pearson product-moment correlation coefficient [22]).

### Model development and optimization
- Tuyển chọn tổng cộng $24$ biến từ tài liệu để làm các biến đầu vào và biến đầu ra cho các mô hình học máy hồi quy (regression machine learning models):
  - $6$ biến định tính dạng phân loại ($\text{categorical objects}$, Table S1): điều kiện vận hành, hình thái bùn, loại nước thải đầu vào, chiến lược làm giàu vi sinh, loại quy trình anammox, và chi vi khuẩn anammox chiếm ưu thế.
  - $15$ biến đầu vào tùy chọn ($\text{optional input variables}$): điều kiện vận hành, hình thái bùn, loại nước thải đầu vào, chiến lược làm giàu, loại quy trình, vi khuẩn anammox chiếm ưu thế, thời gian vận hành, $\text{HRT}$, $\text{C/N}$, $\text{COD}$ đầu vào, $\text{NH}_4^+-\text{N}$ đầu vào, $\text{NO}_3^--\text{N}$ đầu vào, $\text{NO}_2^--\text{N}$ đầu vào, $\text{TIN}$ đầu vào, và $\text{NLR}$.
  - $7$ biến đầu ra mục tiêu được dự đoán độc lập nhằm xác định mối quan hệ riêng biệt giữa các biến đầu vào với từng biến đầu ra: $\text{NH}_4^+-\text{N}$ đầu ra, $\text{NO}_3^--\text{N}$ đầu ra, $\text{NO}_2^--\text{N}$ đầu ra, $\text{TIN}$ đầu ra, hiệu suất khử $\text{NH}_4^+-\text{N}$, hiệu suất khử $\text{TIN}$, và $\text{NARR}$.
  - Lựa chọn các biến đầu vào dựa trên kết quả phân tích tương quan $\text{PPMC}$ nhằm loại bỏ hiện tượng đa cộng tuyến (multicollinearity) và giữ lại các đặc trưng có tương quan cao với biến đầu ra (Fig. S1 [29]).
- Phân chia ngẫu nhiên $2940$ mẫu dữ liệu thành ba tập con nhằm giảm thiểu sai số dự đoán và tránh hiện tượng không hội tụ dữ liệu:
  - Tập huấn luyện ($\text{training dataset}$): chiếm $70\,\%$ ($2070$ mẫu).
  - Tập kiểm thực ($\text{validation dataset}$): chiếm $15\,\%$.
  - Tập kiểm tra ($\text{testing dataset}$): chiếm $15\,\%$.
  - Tỷ số giữa kích thước mẫu huấn luyện và số lượng đặc trưng ($\text{SFR}$ - sample-size to feature-size ratio) đạt $138$ ($2070$ mẫu huấn luyện chia cho $15$ biến đầu vào), thỏa mãn ngưỡng $\text{SFR} \ge 100$ đảm bảo độ tin cậy và tiềm năng học máy cao [19, 29].
  - Quá trình chuẩn hóa giá trị số (theo giá trị trung bình $\text{mean}$ và độ lệch chuẩn $\text{standard deviation}$) được tích hợp sẵn trong nền tảng H2O AutoML.
- Quy trình thiết lập mô hình tự động và tối ưu hóa trên nền tảng H2O AutoML (Text S2):
  - Tự động tối ưu hóa và so sánh nhiều thuật toán học máy gồm: Distributed Random Forest ($\text{DRF}$), Extremely Randomized Trees ($\text{XRT}$), Generalized Linear Model có chuẩn hóa ($\text{GLM with regularization}$), eXtreme Gradient Boosting ($\text{XGBoost}$), Gradient Boosting Machines ($\text{GBM}$), và mạng nơ-ron sâu ($\text{deep neural networks}$) để xây dựng bảng xếp hạng mô hình ($\text{modeling leaderboard}$) (Fig. 1).
    - **Hình 1.** Sơ đồ quy trình AutoML phân tích dữ liệu lớn hệ thống anammox
      - <img src="assets/fig_01_p3.png" alt="Hình 1" />
      - **Hình này chứng minh điều gì**
        - Khung tích hợp liên kết từ thu thập dữ liệu, phân chia tập mẫu ($70\,\%$, $15\,\%$, $15\,\%$), huấn luyện $6$ họ thuật toán đến giải thích mô hình qua PDP.
      - **Từ đâu mà thấy được**
        - Luồng mũi tên từ Data Collection qua Feature Selection, Variable Compositions sang Dataset Formation, nạp vào H2O AutoML để xuất Leaderboard và Interpretable Analysis.
        - Khối Candidate Models đánh dấu tích đỏ tại eXtreme Gradient Boosting và gradient boosting machines thể hiện hai thuật toán tối ưu được lựa chọn.
  - Ứng dụng kết hợp tìm kiếm ngẫu nhiên nhanh ($\text{fast random search}$) và kiểm thực chéo $5$ nếp ($\text{fivefold cross-validation}$) nhằm gia tăng tốc độ huấn luyện và nâng cao hiệu năng mô hình.
  - Cấu hình giới hạn tài nguyên của H2O AutoML: số lượng mô hình tối đa là $200$ và thời gian chạy tối đa là $900\text{ s}$ (tiến trình AutoML dừng lại ngay khi chạm một trong hai ngưỡng giới hạn).
  - Thiết lập $5$ giá trị hạt giống ngẫu nhiên ($\text{seeds}$) khác nhau cho việc phân chia dữ liệu nhằm kiểm soát sự chênh lệch hiệu năng dự báo phát sinh từ cách chia tập mẫu.
  - Đánh giá hiệu năng tốt nhất trên tập huấn luyện, kiểm thực và kiểm tra của các mô hình ứng viên thông qua sai số tuyệt đối trung bình ($\text{MAE}$ - Mean Absolute Error) và hệ số xác định ($R^2$ - Coefficient of Determination).

### Experimental validation of candidate models
- Kiểm chứng hiệu năng của các mô hình ứng viên bằng tập dữ liệu thực nghiệm độc lập chưa từng được học ($\text{unseen experimental dataset}$) gồm $185$ mẫu:
  - Các mô hình ứng viên gồm $\text{DRF}$, $\text{XRT}$, $\text{XGBoost}$, $\text{GBM}$, $\text{Generalized Linear Model}$, và $\text{deep neural networks}$ được huấn luyện trên cùng một tập dữ liệu huấn luyện ($2070$ mẫu) và cùng được kiểm tra trên tập thực nghiệm độc lập này.
- Thiết lập hệ thống thực nghiệm bể phản ứng dòng chảy ngược qua lớp bùn kỵ khí ($\text{UASB}$ - Up-flow Anaerobic Sludge Blanket) vận hành quy trình $\text{PDA}$ nhằm khảo sát hiệu năng $\text{PDA}$ dưới các tỷ lệ $\text{C/N}$ khác nhau:
  - Thể tích làm việc của bể phản ứng: $5.72\text{ L}$.
  - Hỗn hợp bùn cấy giống: phối trộn bùn bông $\text{PD}$ (từ bể phản ứng $\text{PD}$ vận hành dài hạn dùng glycerol) và bùn hạt anammox trưởng thành (từ bể phản ứng $\text{UASB anammox}$) theo tỷ lệ sinh khối $1:5$ rồi cấy vào bể $\text{PDA UASB}$.
  - Nước thải đầu vào: chuẩn bị bằng nước thải tổng hợp ($\text{synthetic wastewater}$).
  - Điều kiện vận hành: duy trì nhiệt độ phản ứng ở $35\,^\circ\text{C}$ bằng bể ổn nhiệt, thời gian lưu thủy lực ($\text{HRT}$) cố định ở $4\text{ h}$.
  - Các biến phân loại của thực nghiệm được tóm tắt tại Table S9.
- Bể phản ứng $\text{PDA UASB}$ vận hành liên tục trong $185\text{ d}$ qua $6$ giai đoạn với các điều kiện nước thải đầu vào biến thiên (Table S10):
  - Phương pháp đo đạc: nồng độ các dạng nitơ trong các mẫu nước được đo theo Tiêu chuẩn Phương pháp Thử nghiệm Chuẩn ($\text{Standard Methods}$).
  - Biến thiên hiệu năng xử lý của thực nghiệm gồm $\text{NH}_4^+-\text{N}$, $\text{NO}_3^--\text{N}$, $\text{NO}_2^--\text{N}$, $\text{TIN}$ dòng ra, hiệu suất khử $\text{NH}_4^+-\text{N}$, hiệu suất khử $\text{TIN}$ và $\text{NARR}$ được đối chiếu trực tiếp giữa giá trị thực tế và giá trị mô hình dự báo (Fig. 5).
    - **Hình 5.** So sánh giá trị dự báo và thực tế trên tập thực nghiệm
      - <img src="assets/fig_05_p10.png" alt="Hình 5" />
      - **Hình này chứng minh điều gì**
        - Các mô hình tối ưu theo sát diễn biến động học thực tế của $7$ chỉ tiêu nitơ xuyên suốt $185\text{ d}$ vận hành qua $6$ giai đoạn biến thiên điều kiện đầu vào.
      - **Từ đâu mà thấy được**
        - Trục hoành $Ox$: Operation time ($\text{d}$), từ $0$ đến $200\text{ d}$; điểm thực tế (vòng tròn rỗng) và dự báo (chấm đặc) bám sát nhau.
        - Bảng (a)-(d): Trục tung $Oy$ đo nồng độ dòng ra ($\text{mg/L}$) của $\text{NH}_4^+-\text{N}$ ($0-50$), $\text{NO}_3^--\text{N}$ ($0-35$), $\text{NO}_2^--\text{N}$ ($0-15$), $\text{TIN}$ ($0-80$).
        - Bảng (e)-(g): Trục tung $Oy$ đo hiệu suất khử $\text{NH}_4^+-\text{N}$ ($20-100\,\%$, e), hiệu suất khử $\text{TIN}$ ($20-100\,\%$, f) và $\text{NARR}$ ($0.05-0.25\text{ kg/m}^3/\text{d}$, g).

### Interpretable analysis
- Sử dụng các phương pháp giải thích mô hình (interpretable methods) gồm độ quan trọng của biến ($\text{variable importance}$), biểu đồ phụ thuộc một phần một chiều ($1\text{D PDP}$) và hai chiều ($2\text{D PDP}$) để phân tích các mô hình ứng viên tối ưu do thuật toán AutoML tạo ra cho từng biến đầu ra:
  - Độ quan trọng của biến ($\text{variable importance}$): tính toán tầm quan trọng của các đặc trưng mẫu và mô tả định lượng mức đóng góp của từng đặc trưng đối với bài toán phân loại hoặc hồi quy.
  - Biểu đồ phụ thuộc một phần ($\text{PDP}$): biểu diễn mối quan hệ hàm số giữa một hoặc hai biến đặc trưng ($1\text{D PDP}$ hoặc $2\text{D PDP}$) tác động lên kết quả dự đoán của mô hình.
  - Nguyên lý hoạt động của $2\text{D PDP}$: thay đổi đồng thời giá trị của hai đặc trưng được chọn trong khi cố định giá trị của tất cả các đặc trưng còn lại, sau đó tính toán kết quả dự đoán để thể hiện tác động kết hợp ($\text{combined effect}$) của hai biến lên đầu ra.
  - Nền tảng thực thi: các phân tích giải thích mô hình được thực hiện trực tiếp trên giao diện dòng chảy Flow UI của nền tảng H2O AutoML (`https://h2o-release.s3.amazonaws.com/h2o/rel-3.46.0/6/docs-website/h2o-docs/flow.html`).
