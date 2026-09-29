---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Elucidating response effects of anammox-based nitrogen removal processes for municipal wastewater using big data analysis and automated machine learning

## Chương 1: Tổng quan và Phương pháp nghiên cứu

### 1.1 Bối cảnh và Đặt vấn đề công nghệ Anammox dòng chính

#### 1.1.1 Vấn đề phú dưỡng hóa và hạn chế của bùn hoạt tính truyền thống
- Phú dưỡng hóa nguồn nước là vấn đề môi trường toàn cầu. Tình trạng này do phát thải quá mức nitơ ($N$) và phốt pho ($P$).
- Quy trình bùn hoạt tính truyền thống (Conventional Activated Sludge - CAS) loại bỏ nitơ qua hai bước. Bước một là nitrit hóa/nitrat hóa hiếu khí. Bước hai là khử nitrat thiếu khí.
- Quy trình CAS tiêu tốn nhiều năng lượng điện. Hệ thống cần sục khí liên tục để oxy hóa amoni ($\text{NH}_4^+$) thành nitrat ($\text{NO}_3^-$).
- Quá trình khử nitrat trong CAS đòi hỏi nguồn cacbon hữu cơ ngoại sinh. Nhu cầu này rất lớn khi tỷ lệ $\text{COD}/\text{N}$ trong nước thải thấp.
- Bùn sinh học dư thừa phát sinh rất nhiều. Điều này làm tăng chi phí xử lý và phát thải khí nhà kính.

#### 1.1.2 Đột phá kỹ thuật và ưu thế vượt trội của công nghệ Anammox
- Quá trình oxy hóa amoni kỵ khí (Anammox) loại bỏ nitơ trực tiếp. Vi khuẩn oxy hóa $\text{NH}_4^+$ bằng $\text{NO}_2^-$ thành $\text{N}_2$ trong điều kiện kỵ khí hoàn toàn.
- Công nghệ Anammox không cần bổ sung nguồn cacbon hữu cơ ngoại sinh. Do đó, công nghệ tiết kiệm $100\%$ nhu cầu cacbon hữu cơ.
- Nhu cầu cấp oxy hòa tan giảm xấp xỉ $60\%$. Nhờ đó, hệ thống tiết kiệm phần lớn năng lượng sục khí cơ học.
- Sản lượng bùn sinh học dư thừa giảm xấp xỉ $90\%$. Hệ số sản xuất sinh khối của vi khuẩn Anammox chỉ đạt $0{,}066\text{ mol sinh khối / mol NH}_4^+$.
- Nhờ các ưu thế trên, Anammox giảm mạnh chi phí vận hành cho các trạm xử lý nước thải đô thị (WWTPs).

#### 1.1.3 Thách thức kỹ thuật khi triển khai Anammox cho nước thải đô thị dòng chính
- Nồng độ tổng nitơ vô cơ trong nước thải đô thị dòng chính rất thấp. Nồng độ này thường đạt $\text{TIN} < 70\text{ mg N/L}$. Mức nồng độ thấp gây khó khăn cho việc duy trì sinh khối vi sinh.
- Tỷ lệ chất hữu cơ trên nitơ ($\text{COD}/\text{N}$) biến động lớn. Chất hữu cơ thúc đẩy vi khuẩn dị dưỡng phát triển và cạnh tranh không gian sống với vi khuẩn Anammox.
- Nhiệt độ nước thải vào mùa đông giảm sâu ($10 - 15\ ^\circ\text{C}$). Mức nhiệt thấp làm suy giảm tốc độ trao đổi chất của vi khuẩn Anammox.
- Nguồn cung cấp nitrit ($\text{NO}_2^-$) ổn định gặp nhiều rủi ro. Việc kiểm soát tích lũy nitrit trong dòng chính rất khó khăn.

#### 1.1.4 Cấu hình các quy trình công nghệ kết hợp cung cấp nitrit
- Quy trình Nitrit hóa một phần kết hợp Anammox (PNA): vi khuẩn oxy hóa amoni (AOB) oxy hóa khoảng $50\%$ amoni thành nitrit. Hệ thống phải ức chế hoàn toàn vi khuẩn oxy hóa nitrit (NOB).
- Quy trình Khử nitrat một phần kết hợp Anammox (PDA): vi khuẩn dị dưỡng khử $\text{NO}_3^-$ về $\text{NO}_2^-$. Quá trình này cung cấp cơ chất nitrit liên tục cho Anammox.
- Hệ thống kết hợp PNA và PDA: cấu hình này tích hợp các vùng hiếu khí và thiếu khí xen kẽ. Ví dụ điển hình gồm hệ thống AOA (Anaerobic/Oxic/Anoxic) và quy trình cấp dòng chia bậc (step-feed).

#### 1.1.5 Động lực và tính tất yếu ứng dụng học máy tự động (AutoML)
- Các nghiên cứu trước đây xây dựng mô hình học máy thủ công (manual machine learning). Quá trình tinh chỉnh thử-sai tốn nhiều thời gian và chi phí tính toán.
- Chất lượng của mô hình thủ công phụ thuộc kinh nghiệm của người thiết kế.
- Mô hình thủ công có khả năng tái lập kém trên các tập dữ liệu phức tạp.
- Nền tảng học máy tự động (AutoML) tự động hóa toàn bộ quy trình. AutoML tự xử lý dữ liệu, chọn thuật toán, chỉnh siêu tham số và tối ưu mô hình.
- AutoML kết hợp các phương pháp giải thích trực quan. Sự kết hợp này làm sáng tỏ các mối quan hệ phi tuyến phức tạp trong dữ liệu lớn Anammox.


### 1.2 Nguồn dữ liệu lớn và Phương pháp phân tích thống kê ban đầu

#### 1.2.1 Thu thập và sàng lọc bộ dữ liệu lớn chuẩn mực
- Nhóm tác giả tìm kiếm tài liệu hệ thống trên cơ sở dữ liệu Web of Science. Các từ khóa gồm: "Anaerobic ammonia oxidation", "mainstream anammox", "municipal wastewater", "partial nitrification", "partial denitrification".
- Nghiên cứu tuyển chọn $28$ công trình thực nghiệm chuẩn mực đáp ứng tính nhất quán (Table S9).
- Nghiên cứu này bổ sung các thông số vận hành quan trọng như HRT và NLR. Các phân tích meta trước đây (như Liu et al., 2020) đã bỏ qua các thông số này.
- Nhóm tác giả dùng phần mềm số hóa Origin để trích xuất $2.940$ mẫu dữ liệu thực nghiệm:
  - $1.927$ mẫu dữ liệu từ các hệ thống PDA.
  - $282$ mẫu dữ liệu từ các hệ thống PNA.
  - $731$ mẫu dữ liệu từ các hệ thống tích hợp PNA và PDA.

#### 1.2.2 Hệ thống 24 biến số công nghệ đầu vào và đầu ra
- Cơ sở dữ liệu quy chuẩn gồm 24 biến số kỹ thuật (Table S1).
- Nhóm 6 biến số phân loại (Categorical variables) gồm:
  - Chế độ vận hành: Nạp mẻ liên tục (Sequencing batch) hoặc Dòng chảy liên tục (Continuous flow).
  - Dạng hình thái bùn: Bùn bông lắng (Floc) hoặc Bùn hạt kết tụ (Aggregates / Granules).
  - Loại nước thải nạp: Nước thải nhân tạo (Synthetic wastewater) hoặc Nước thải đô thị thực tế (Municipal wastewater).
  - Chiến lược sinh khối: Tự làm giàu nội tại (Self-enrichment) hoặc Cấy giống bổ sung (Inoculation).
  - Loại quy trình Anammox: PNA, PDA, hoặc PNA kết hợp PDA.
  - Chi vi khuẩn Anammox chiếm ưu thế: *Candidatus* Brocadia, *Candidatus* Kuenenia, hoặc các chi vi khuẩn khác.
- Nhóm 9 biến số đầu vào liên tục (Continuous input variables):
  - Thời gian vận hành hệ phản ứng (Operation time, đơn vị: $\text{d}$).
  - Thời gian lưu thủy lực (HRT, đơn vị: $\text{h}$).
  - Tỷ lệ chất hữu cơ trên nitơ nạp (C/N ratio).
  - Nồng độ COD nạp ($\text{COD}_{inf}$, đơn vị: $\text{mg/L}$).
  - Nồng độ amoni nạp ($\text{NH}_{4,inf}^+\text{-N}$, đơn vị: $\text{mg/L}$).
  - Nồng độ nitrat nạp ($\text{NO}_{3,inf}^-\text{-N}$, đơn vị: $\text{mg/L}$).
  - Nồng độ nitrit nạp ($\text{NO}_{2,inf}^-\text{-N}$, đơn vị: $\text{mg/L}$).
  - Nồng độ tổng nitơ vô cơ nạp ($\text{TIN}_{inf}$, đơn vị: $\text{mg/L}$).
  - Tải trọng nạp nitơ thể tích (NLR, đơn vị: $\text{kg N/m}^3/\text{ngày}$).
  - Tổng số biến đầu vào tiềm năng là 15 biến (gồm 6 biến phân loại và 9 biến liên tục).
- Nhóm 7 biến số mục tiêu đầu ra (Continuous output variables) dự đoán độc lập:
  - Nồng độ amoni dòng ra ($\text{NH}_{4,eff}^+\text{-N}$, đơn vị: $\text{mg/L}$).
  - Nồng độ nitrat dòng ra ($\text{NO}_{3,eff}^-\text{-N}$, đơn vị: $\text{mg/L}$).
  - Nồng độ nitrit dòng ra ($\text{NO}_{2,eff}^-\text{-N}$, đơn vị: $\text{mg/L}$).
  - Nồng độ tổng nitơ vô cơ dòng ra ($\text{TIN}_{eff}$, đơn vị: $\text{mg/L}$).
  - Hiệu suất loại bỏ amoni ($\eta_{\text{NH}_4^+}$, đơn vị: $\%$).
  - Hiệu suất loại bỏ tổng nitơ vô cơ ($\eta_{\text{TIN}}$, đơn vị: $\%$).
  - Tốc độ loại bỏ nitơ qua con đường Anammox (NARR, đơn vị: $\text{kg N/m}^3/\text{ngày}$).

#### 1.2.3 Các công thức toán học và phương trình tính toán động học
- Tải trọng nạp nitơ thể tích (NLR):
  $$\text{NLR} = \frac{\text{TIN}_{inf}}{\text{HRT} \times 24} \quad \text{hoặc} \quad \text{NLR} = \frac{Q \times \text{TIN}_{inf}}{V} \quad (\text{kg N/m}^3/\text{ngày})$$
- Giải thích các ký hiệu công thức NLR:
  - $\text{TIN}_{inf}$ là nồng độ tổng nitơ vô cơ nạp ($\text{mg N/L}$ hoặc $\text{g N/m}^3$).
  - $\text{HRT}$ là thời gian lưu thủy lực ($\text{h}$).
  - $Q$ là lưu lượng dòng thải nạp ($\text{m}^3/\text{ngày}$).
  - $V$ là thể tích làm việc của bể phản ứng ($\text{m}^3$).
- Hiệu suất loại bỏ amoni ($\eta_{\text{NH}_4^+}$):
  $$\eta_{\text{NH}_4^+} = \frac{\text{NH}_{4,inf}^+ - \text{NH}_{4,eff}^+}{\text{NH}_{4,inf}^+} \times 100\%$$
- Hiệu suất loại bỏ tổng nitơ vô cơ ($\eta_{\text{TIN}}$):
  $$\eta_{\text{TIN}} = \frac{\text{TIN}_{inf} - \text{TIN}_{eff}}{\text{TIN}_{inf}} \times 100\%$$
- Nồng độ tổng nitơ vô cơ được tính theo tổng ba thành phần:
  $$\text{TIN} = \text{NH}_4^+\text{-N} + \text{NO}_2^-\text{-N} + \text{NO}_{3}^-\text{-N}$$
- Phương trình phản ứng sinh hóa Anammox kinh điển (Strous et al., 1998):
  $$\text{NH}_4^+ + 1{,}32\,\text{NO}_2^- + 0{,}066\,\text{HCO}_3^- + 0{,}13\,\text{H}^+ \rightarrow 1{,}02\,\text{N}_2 + 0{,}26\,\text{NO}_3^- + 0{,}066\,\text{CH}_2\text{O}_{0{,}5}\text{N}_{0{,}15} + 2{,}03\,\text{H}_2\text{O}$$
- Tỷ lệ mol phản ứng lý thuyết: $1\text{ mol }\text{NH}_4^+$ tiêu thụ $1{,}32\text{ mol }\text{NO}_2^-$ và sinh ra $0{,}26\text{ mol }\text{NO}_3^-$.
- Tốc độ loại bỏ nitơ qua con đường Anammox (NARR):
  $$\text{NARR} = \frac{(\text{NH}_{4,inf}^+ - \text{NH}_{4,eff}^+) + (\text{NO}_{2,inf}^- - \text{NO}_{2,eff}^-) - \frac{(\text{NO}_{3,eff}^- - \text{NO}_{3,inf}^-)}{0{,}26}}{\text{HRT}}$$
- Công thức NARR khấu trừ lượng nitrat sinh học tạo ra nội tại với hệ số tỷ lượng $0{,}26$.
- Tốc độ phản ứng nitrit hóa của vi khuẩn oxy hóa amoni AOB (NiRR):
  $$\text{NiRR} = \frac{(\text{NO}_{2,eff}^- - \text{NO}_{2,inf}^-) + 1{,}32 \times (\text{NH}_{4,inf}^+ - \text{NH}_{4,eff}^-)}{\text{HRT}}$$
- Tốc độ loại bỏ tổng nitơ vô cơ của hệ thống (NRR):
  $$\text{NRR} = \frac{\text{TIN}_{inf} - \text{TIN}_{eff}}{\text{HRT}}$$

#### 1.2.4 Phân tích thống kê khám phá và kiểm tra tương quan PPMC
- Biểu đồ hộp (Box plots) thể hiện độ phân tán và trung vị dữ liệu giữa các nhóm thí nghiệm.
- Thí nghiệm nạp mẻ (Sequencing batch) cho trung vị hiệu suất khử TIN đạt $78{,}18\%$. Mức này cao hơn thí nghiệm dòng liên tục ($74{,}81\%$).
- Thí nghiệm nạp mẻ duy trì NLR, NiRR, NARR và NRR ổn định hơn.
- Nghiên cứu của Du et al. (2016) và Wang et al. (2024b) đạt giá trị tải trọng rất cao trong bể bùn hạt dòng liên tục:
  - Tải trọng nạp: $\text{NLR} = 2{,}91 - 7{,}55\text{ kg N/m}^3/\text{ngày}$.
  - Tốc độ nitrit hóa: $\text{NiRR} = 0{,}33 - 2{,}53\text{ kg N/m}^3/\text{ngày}$.
  - Tốc độ Anammox: $\text{NARR} = 0{,}02 - 3{,}92\text{ kg N/m}^3/\text{ngày}$.
  - Tốc độ khử nitơ tổng: $\text{NRR} = 2{,}63 - 6{,}55\text{ kg N/m}^3/\text{ngày}$.
- Phân tích EDA cho thấy nước thải đô thị có dải biến thiên NLR, NiRR, NARR hẹp và ổn định. Nồng độ amoni chiếm trên $90\%$ tổng nitơ nạp ($\text{TIN}_{inf}$).
- Hệ số tương quan Pearson (PPMC) đánh giá quan hệ tuyến tính giữa các cặp biến.
- Hệ thống PNA thể hiện tương quan thuận mạnh nhất giữa biến đầu vào và đầu ra ($r = 0{,}55 - 0{,}95$).
- Ngoại trừ cặp $\text{NH}_{4,inf}^+$ và $\text{TIN}_{inf}$, các biến đầu vào không có hiện tượng đa cộng tuyến mạnh. Vì vậy, mô hình tiếp nhận toàn bộ 15 biến đầu vào.


### 1.3 Phát triển và Tối ưu hóa mô hình với H2O AutoML

#### 1.3.1 Phân chia tập dữ liệu và chỉ số độ tin cậy mẫu (SFR)
- Toàn bộ $2.940$ mẫu dữ liệu được chia ngẫu nhiên thành ba tập con độc lập:
  - Tập huấn luyện (Training dataset): chiếm $70\%$ ($2.070$ mẫu dữ liệu).
  - Tập kiểm thực (Validation dataset): chiếm $15\%$ ($435$ mẫu dữ liệu).
  - Tập kiểm tra (Testing dataset): chiếm $15\%$ ($435$ mẫu dữ liệu).
- Tỷ lệ kích thước mẫu huấn luyện trên số đặc trưng đầu vào (SFR):
  $$\text{SFR} = \frac{N_{\text{train}}}{M_{\text{features}}} = \frac{2070}{15} = 138$$
- Giá trị $\text{SFR} = 138 \ge 100$ đạt tiêu chuẩn phương pháp luận EMBRACE. Chỉ số này bảo đảm độ tin cậy cao và ngăn chặn hiện tượng quá khớp (overfitting).

#### 1.3.2 Tiền xử lý dữ liệu và loại bỏ đa cộng tuyến
- Nền tảng H2O AutoML tự động chuẩn hóa dữ liệu số bằng phép biến đổi z-score:
  $$z = \frac{x - \mu}{\sigma}$$
- H2O tự động mã hóa các biến phân loại để thuật toán học máy xử lý hiệu quả.
- Ma trận PPMC được dùng để sàng lọc đặc trưng. Quá trình này loại bỏ các biến đa cộng tuyến và giữ lại biến có tương quan cao với đầu ra.

#### 1.3.3 Không gian thuật toán học máy đa dạng trong H2O AutoML
- Bảng xếp hạng (Leaderboard) của H2O AutoML tự động so sánh sáu dòng thuật toán:
  - Distributed Random Forest (DRF): tập hợp nhiều cây quyết định độc lập nhằm giảm phương sai dự đoán.
  - Extremely Randomized Trees (XRT): giải thuật cây cực ngẫu nhiên hóa nhằm tăng khả năng khái quát hóa.
  - Generalized Linear Model (GLM): mô hình tuyến tính tổng quát với bộ phạt chính quy hóa Elastic Net ($L_1$ và $L_2$).
  - eXtreme Gradient Boosting (XGBoost): thuật toán tăng cường độ dốc kết hợp chính quy hóa hàm mục tiêu.
  - Gradient Boosting Machine (GBM): giải thuật tăng cường độ dốc tuần tự tối ưu hóa hàm mất mát.
  - Deep Neural Networks (DNN): mạng nơ-ron học sâu nhiều lớp ẩn trích xuất các mẫu hình phi tuyến.

#### 1.3.4 Chiến lược điều chỉnh siêu tham số và thước đo đánh giá
- Nền tảng kết hợp thuật toán tìm kiếm ngẫu nhiên (Random search) và kiểm định chéo 5 nếp (5-fold cross-validation).
- Giới hạn dừng sớm: tối đa 200 mô hình hoặc thời gian huấn luyện chạm ngưỡng 900 giây. Hệ thống tự ngắt khi chạm một trong hai giới hạn.
- Nghiên cứu áp dụng 5 hạt giống ngẫu nhiên (Random seeds) độc lập để kiểm soát biến thiên phân tách dữ liệu.
- Sai số tuyệt đối trung bình (MAE) đánh giá độ lệch dự đoán:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
- Hệ số xác định ($R^2$) đánh giá mức độ tương thích của mô hình:
  $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
- Trong công thức trên: $y_i$ là giá trị đo thực nghiệm, $\hat{y}_i$ là giá trị dự đoán, và $\bar{y}$ là giá trị trung bình mẫu.


### 1.4 Thiết lập kiểm chứng thực nghiệm bằng hệ phản ứng UASB PDA-Anammox

#### 1.4.1 Cấu hình kỹ thuật và điều kiện vận hành hệ phản ứng UASB
- Nghiên cứu thiết lập hệ phản ứng UASB kỵ khí dòng chảy ngược ở quy mô phòng thí nghiệm.
- Thể tích làm việc hữu dụng của bể UASB là $V = 5{,}72\text{ L}$.
- Nhiệt độ phản ứng được giữ ổn định ở mức $35\ ^\circ\text{C}$ nhờ bể điều nhiệt tuần hoàn nước.
- Thời gian lưu thủy lực được duy trì cố định ở mức $\text{HRT} = 4\text{ h}$.
- Bể sử dụng nước thải nhân tạo với thành phần hóa chất chuẩn mực theo Xu et al. (2022a).

#### 1.4.2 Tỷ lệ phối trộn sinh khối vi sinh vật cấy giống
- Bùn bông khử nitrat một phần (PD flocculent sludge): lấy từ hệ thống PD dùng glycerol vận hành dài hạn.
- Bùn hạt Anammox trưởng thành (Mature anammox granular sludge): thu nhận từ bể UASB Anammox ổn định.
- Tỷ lệ sinh khối cấy ban đầu: $1\text{ phần bùn bông PD} : 5\text{ phần bùn hạt Anammox}$ theo khối lượng sinh khối khô.

#### 1.4.3 Lộ trình vận hành 185 ngày và thu thập tập kiểm chứng độc lập
- Bể phản ứng UASB vận hành liên tục trong thời gian $185\text{ ngày}$.
- Quá trình vận hành gồm 6 giai đoạn kỹ thuật với các dải tỷ lệ C/N khác nhau (Table S10).
- Nhóm tác giả thu thập $185$ mẫu dữ liệu thực tế độc lập hàng ngày (Unseen experimental dataset). Tập dữ liệu này không tham gia vào quá trình huấn luyện mô hình.
- Các thông số đo gồm: $\text{NH}_{4,eff}^+$, $\text{NO}_{3,eff}^-$, $\text{NO}_{2,eff}^-$, $\text{TIN}_{eff}$, hiệu suất khử amoni, hiệu suất khử tổng nitơ và NARR.
- Tất cả các dạng nitơ được đo đạc theo Tiêu chuẩn Phân tích Nước và Nước thải Chuẩn mực (Standard Methods).


### 1.5 Phương pháp phân tích giải thích mô hình (Interpretable Analysis)

#### 1.5.1 Định lượng độ quan trọng biến số (Variable Importance)
- Phương pháp Variable Importance tính toán mức đóng góp của từng biến đặc trưng đầu vào.
- Giá trị đóng góp phản ánh mức độ giảm thiểu hàm mất mát của mô hình tối ưu.
- Kết quả giúp xếp hạng tầm ảnh hưởng của các biến công nghệ lên 7 biến mục tiêu đầu ra.

#### 1.5.2 Biểu đồ phụ thuộc riêng phần đơn biến (1D PDP) và hai biến (2D PDP)
- Biểu đồ phụ thuộc riêng phần một chiều (1D PDP) thể hiện đáp ứng biên của một biến đầu vào lên kết quả dự đoán. Biểu đồ giữ cố định các biến còn lại ở giá trị trung bình.
- Biểu đồ tương tác hai chiều (2D PDP) thay đổi đồng thời hai biến công nghệ trên lưới tọa độ.
- Biểu đồ 2D PDP minh họa bề mặt phản ứng tương tác và hỗ trợ xác định vùng vận hành tối ưu.

#### 1.5.3 Nền tảng thực thi Flow UI trên H2O AutoML
- Nghiên cứu thực hiện phân tích giải thích mô hình trên giao diện Flow UI của H2O AutoML phiên bản 3.46.0.
- Giao diện trực quan này bảo đảm tính minh bạch và độ tin cậy của toàn bộ kết quả phân tích.

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

## Chương 3: Phân tích giải thích cơ chế loại bỏ NH4+-N, NO3--N và NO2--N

### 3.1 Xếp hạng độ quan trọng biến số cho nồng độ và hiệu suất khử NH4+-N

#### 3.1.1 Thứ tự độ quan trọng đối với nồng độ NH4+-N dòng ra
- Mô hình máy học GBM và XGBoost xếp hạng độ quan trọng của 15 biến đầu vào. Thứ tự giảm dần ảnh hưởng đến nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra gồm:
  $$\text{TIN nạp} > \text{C/N} > \text{NH}_4^+\text{-N nạp} > \text{Thời gian vận hành} > \text{Chi vi khuẩn Anammox chiếm ưu thế} > \text{HRT} > \text{NO}_3^-\text{-N nạp} > \text{Hình thái bùn} > \text{NLR} > \text{Loại quy trình} > \text{COD nạp} > \text{NO}_2^-\text{-N nạp} > \text{Chiến lược làm giàu} > \text{Điều kiện vận hành} > \text{Loại nước thải}$$
- Biến $\text{TIN}$ nạp giữ vị trí quan trọng số một (Hình 3(a)). Giá trị này kiểm soát tổng lượng nitơ đi vào hệ thống xử lý.
- Tỷ số $\text{C/N}$ giữ vị trí quan trọng thứ hai. Tỷ số này quyết định sự cạnh tranh giữa vi khuẩn dị dưỡng và vi khuẩn Anammox tự dưỡng.
- Nồng độ $\text{NH}_4^+$-$\text{N}$ nạp giữ vị trí quan trọng thứ ba. Đây là cơ chất trực tiếp của vi khuẩn Anammox.

#### 3.1.2 Thứ tự độ quan trọng đối với hiệu suất khử NH4+-N
- Nồng độ $\text{NO}_3^-$-$\text{N}$ nạp thể hiện độ quan trọng vượt bậc đối với hiệu suất loại bỏ $\text{NH}_4^+$-$\text{N}$ (Hình 3(e)).
- $\text{NO}_3^-$-$\text{N}$ đóng vai trò là chất nhận electron ban đầu cho quá trình khử nitrat một phần (PDA). Quá trình này khử $\text{NO}_3^-$ thành $\text{NO}_2^-$.
- Nồng độ $\text{NO}_2^-$ sinh ra cung cấp cơ chất thiết yếu cho phản ứng Anammox. Thiếu $\text{NO}_2^-$ sẽ làm suy giảm trực tiếp hiệu suất oxy hóa $\text{NH}_4^+$.

#### 3.1.3 Vai trò chi phối tuyệt đối của thành phần cacbon và nitơ đầu vào
- Bốn biến số gồm $\text{TIN}$ nạp, $\text{C/N}$, $\text{NH}_4^+$-$\text{N}$ nạp và $\text{NO}_3^-$-$\text{N}$ nạp chi phối việc loại bỏ $\text{NH}_4^+$-$\text{N}$.
- Phản ứng Anammox đòi hỏi tỷ lệ cơ chất nghiêm ngặt theo phương trình phản ứng sinh hóa:
  $$\text{NH}_4^+ + 1.32\text{NO}_2^- + 0.066\text{HCO}_3^- + 0.13\text{H}^+ \rightarrow 1.02\text{N}_2 + 0.26\text{NO}_3^- + 0.066\text{CH}_2\text{O}_{0.5}\text{N}_{0.15} + 2.03\text{H}_2\text{O}$$
- Quá trình loại bỏ $\text{NH}_4^+$-$\text{N}$ phụ thuộc hoàn toàn vào hoạt tính của vi khuẩn Anammox. Thành phần dinh dưỡng dòng vào tác động mạnh mẽ đến hoạt tính này.

#### 3.1.4 Giải thích vị trí cuối bảng của biến loại nước thải
- Biến loại nước thải (nước thải nhân tạo hay nước thải đô thị thực tế) xếp cuối bảng độ quan trọng (Hình 3(a), (e)).
- Các công trình nghiên cứu thường đơn giản hóa nước thải đô thị thành các chỉ tiêu ô nhiễm cơ bản. Các chỉ tiêu này bao gồm $\text{COD}$, $\text{NH}_4^+$-$\text{N}$ và $\text{TIN}$.
- Mô hình học máy nhận diện trực tiếp các giá trị nồng độ ô nhiễm cụ thể.
- Sự khác biệt định tính giữa hai loại nước thải do đó bị che mờ trong tập dữ liệu. Điều này giải thích vì sao biến loại nước thải có ảnh hưởng thấp nhất.

#### 3.1.5 Vai trò của thời gian vận hành và chi vi khuẩn Anammox chiếm ưu thế
- Thời gian vận hành và chi vi khuẩn Anammox chiếm ưu thế giữ vị trí quan trọng thứ tư và thứ năm.
- Vi khuẩn Anammox có tốc độ tăng trưởng rất chậm. Thời gian nhân đôi sinh khối kéo dài từ 7 đến 14 ngày.
- Làm giàu sinh khối và chọn lọc chủng vi sinh thích nghi theo thời gian. Đây là yếu tố quyết định để tiêu thụ amoni triệt để.
- Các biến gồm hình thái bùn, loại quy trình, chiến lược làm giàu và điều kiện vận hành thể hiện độ quan trọng thấp hơn. Các hệ thống này đều vận hành theo cùng các con đường sinh hóa loại bỏ nitơ tương đương.


### 3.2 Phản ứng đơn biến (1D PDP) và tương tác hai chiều (2D PDP) của NH4+-N dòng ra

#### 3.2.1 Động học đơn biến (1D PDP) của nồng độ amoni dòng ra
- Động học theo thời gian vận hành (Hình S4(a)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra giảm đơn điệu theo thời gian vận hành.
  - Quần xã vi sinh vật thích nghi và trưởng thành qua các giai đoạn sau, giúp nâng cao hiệu suất xử lý nước thải.
- Động học theo tỷ lệ $\text{C/N}$ (Hình S4(b)):
  - Biểu đồ 1D PDP xác định dải tối ưu hẹp của tỷ số $\text{C/N}$ từ $2.72$ đến $6.32$.
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra đạt mức thấp nhất trong dải tối ưu này.
  - Khi $\text{C/N} < 2.72$: Nước thải thiếu hụt cacbon hữu cơ. Quá trình khử nitrat một phần (PDA) suy giảm, không cung cấp đủ lượng $\text{NO}_2^-$ làm cơ chất cho Anammox.
  - Khi $\text{C/N} > 6.32$: Lượng cacbon hữu cơ dư thừa kích thích vi khuẩn dị dưỡng phát triển mạnh. Vi khuẩn dị dưỡng cạnh tranh không gian sống và cơ chất, ức chế vi khuẩn Anammox.
  - Kết quả này phù hợp với công bố của Miao et al. (2018). Nghiên cứu cho thấy hiệu suất khử $\text{NH}_4^+$-$\text{N}$ tăng đều đặn khi tăng tỷ số $\text{C/N}$ từ $1.1$ lên $2.5$.
- Ngưỡng tới hạn của amoni và tổng nitơ nạp (Hình S4(c), (d)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng vọt khi $\text{NH}_4^+$-$\text{N}$ nạp đạt ngưỡng tới hạn $62.32\text{ mg/L}$.
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng vọt khi $\text{TIN}$ nạp đạt ngưỡng tới hạn $91.08\text{ mg/L}$.
  - Nước thải đô thị thực tế thường có nồng độ nitơ thấp hơn hai ngưỡng tới hạn này. Do đó, các công nghệ dựa trên Anammox rất phù hợp để xử lý nước thải đô thị dòng chính.

#### 3.2.2 Tương tác bề mặt phản ứng hai biến (2D PDP) của NH4+-N dòng ra
- Tương tác giữa $\text{TIN}$ nạp và tỷ lệ $\text{C/N}$ (Hình 4(a)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra đạt điểm cực tiểu $4.23\text{ mg/L}$ tại $\text{C/N} = 2.75$ và $\text{TIN}$ nạp từ $18.85\text{ mg/L}$ đến $87.76\text{ mg/L}$.
  - Khi $\text{TIN}$ nạp vượt quá $87.76\text{ mg/L}$, nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng vọt lên $17.0\text{ mg/L}$.
  - Cơ chế: Tại cùng một tỷ số $\text{C/N}$, tăng $\text{TIN}$ nạp kéo theo sự gia tăng của nồng độ $\text{COD}$ nạp tuyệt đối. Lượng $\text{COD}$ cao thúc đẩy vi khuẩn dị dưỡng tăng sinh, chiếm diện tích sống và ức chế sinh khối Anammox.
- Tương tác giữa $\text{C/N}$ và $\text{NH}_4^+$-$\text{N}$ nạp (Hình 4(d)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra duy trì mức thấp từ $7.17\text{ mg/L}$ đến $10.74\text{ mg/L}$ trên dải rộng.
  - Vùng vận hành ổn định này kéo dài từ $\text{C/N} = 2.36$ đến $9.62$ và $\text{NH}_4^+$-$\text{N}$ nạp từ $13.83\text{ mg/L}$ đến $213.84\text{ mg/L}$.
  - Dải tối ưu này rộng hơn dải tương tác của $\text{TIN}$ nạp. Nguyên nhân do $\text{TIN}$ chứa cả các dạng nitơ oxy hóa ($\text{NO}_3^-$-$\text{N}$ và $\text{NO}_2^-$-$\text{N}$).
- Tương tác giữa $\text{TIN}$ nạp và $\text{NH}_4^+$-$\text{N}$ nạp (Hình 4(b)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng mạnh khi tăng đồng thời cả $\text{NH}_4^+$-$\text{N}$ nạp và $\text{TIN}$ nạp. Kết quả này hoàn toàn thống nhất với động học 1D PDP.
- Tương tác giữa Thời gian vận hành và Dinh dưỡng nạp (Hình 4(c), (f)):
  - Thời gian vận hành kết hợp với $\text{TIN}$ nạp làm giảm nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra từ $32.16\text{ mg/L}$ xuống còn $4.68\text{ mg/L}$.
  - Thời gian vận hành kết hợp với $\text{NH}_4^+$-$\text{N}$ nạp làm giảm nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra từ $20.46\text{ mg/L}$ xuống còn $4.12\text{ mg/L}$.
  - Quá trình thuần hóa sinh khối kéo dài giúp hệ vi sinh vật tăng cường năng lực xử lý tải nạp cao.
- Tương tác giữa Thời gian vận hành và tỷ lệ $\text{C/N}$ (Hình 4(e)):
  - Bề mặt 2D PDP thể hiện cấu trúc đỉnh và thung lũng phức tạp nhất.
  - Vùng nồng độ $\text{NH}_4^+$-$\text{N}$ cực tiểu ổn định nhất duy trì tại dải $\text{C/N}$ từ $2.75$ đến $6.48$. Kết quả này tương đồng chặt chẽ với phân tích 1D PDP.


### 3.3 Phân tích độ quan trọng biến số và động học phát sinh NO3--N và NO2--N dòng ra

#### 3.3.1 Thứ tự độ quan trọng đối với NO3--N và NO2--N dòng ra
- Thứ tự độ quan trọng đối với nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra (Hình 3(b)):
  $$\text{Thời gian vận hành} > \text{NO}_3^-\text{-N nạp} > \text{HRT} > \text{TIN nạp} > \text{COD nạp} > \text{Loại quy trình}$$
- Thứ tự độ quan trọng đối với nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra (Hình 3(c)):
  $$\text{TIN nạp} > \text{Thời gian vận hành} > \text{NO}_3^-\text{-N nạp} > \text{NH}_4^+\text{-N nạp} > \text{NLR} > \text{Chi vi khuẩn Anammox chiếm ưu thế}$$
- Đặc điểm phân hóa: $\text{HRT}$ và $\text{COD}$ nạp kiểm soát mạnh phản ứng khử nitrat để điều hòa $\text{NO}_3^-$-$\text{N}$. Trong khi đó, $\text{TIN}$ nạp và $\text{NLR}$ chi phối mức độ tích lũy cơ chất trung gian $\text{NO}_2^-$-$\text{N}$.

#### 3.3.2 Động học đơn biến (1D PDP) của NO2--N và đỉnh tích lũy tại mốc 30 ngày
- Hiện tượng tích lũy nitrit ở mốc thời gian 30 ngày (Hình S7(a)):
  - Nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra đạt đỉnh cục bộ rõ rệt ở mốc thời gian vận hành 30 ngày.
  - Sau mốc 30 ngày, phản ứng của $\text{NO}_2^-$-$\text{N}$ giảm nhanh và biến thiên tương đồng với $\text{NO}_3^-$-$\text{N}$.
- Cơ chế sinh học vi sinh:
  - Ở giai đoạn bắt đầu vận hành, lượng $\text{NO}_2^-$ sinh ra nhiều hơn lượng $\text{NO}_2^-$ tiêu thụ.
  - Phản ứng nitrit hóa một phần (PN) hoặc khử nitrat một phần (PD) tạo ra nhiều $\text{NO}_2^-$:
    $$\text{PN: } \text{NH}_4^+ + 1.5\text{O}_2 \rightarrow \text{NO}_2^- + \text{H}_2\text{O} + 2\text{H}^+$$
    $$\text{PD: } \text{NO}_3^- + 0.28\text{CH}_3\text{COOH} \rightarrow \text{NO}_2^- + 0.56\text{CO}_2 + 0.68\text{H}_2\text{O} + 0.12\text{OH}^-$$
  - Vi khuẩn Anammox chưa trưởng thành và chưa tích lũy đủ sinh khối để tiêu thụ lượng $\text{NO}_2^-$ này.
  - Nghiên cứu của Yang et al. (2024) chứng minh tỷ lệ đóng góp của Anammox vào loại bỏ nitơ chỉ đạt $13.8\%$ ở giai đoạn $36 - 75\text{ ngày}$. Tỷ lệ này tăng vọt lên $67.1\%$ ở giai đoạn $216 - 258\text{ ngày}$.

#### 3.3.3 Tác động của HRT và COD nạp lên nồng độ NO3--N dòng ra
- Tác động của thời gian lưu thủy lực $\text{HRT}$ lên $\text{NO}_3^-$-$\text{N}$ (Hình S5(b)):
  - Xuất hiện đỉnh tích lũy nitrat mạnh tại dải $\text{HRT}$ từ $10.47\text{ h}$ đến $15.13\text{ h}$.
  - Theo Yang et al. (2024), $\text{HRT} = 10\text{ h}$ không mang lại hiệu quả cho quy trình Anammox và làm trầm trọng thêm tình trạng thiếu cacbon hữu cơ.
  - Kéo dài $\text{HRT}$ lên $17\text{ h}$ giúp mở rộng thời gian lưu vùng thiếu khí từ $5.67\text{ h}$ lên $8.50\text{ h}$. Nhờ đó, $\text{NO}_3^-$-$\text{N}$ dòng ra trung bình giảm sâu từ $14.46\text{ mg/L}$ xuống còn $9.79\text{ mg/L}$.
  - Kéo dài $\text{HRT}$ điều tiết sự cạnh tranh nitrit giữa vi khuẩn khử nitrat và vi khuẩn Anammox.
  - Rút ngắn $\text{HRT} < 9.95\text{ h}$ giúp giảm tích lũy $\text{NO}_3^-$-$\text{N}$ nhờ rửa trôi vi khuẩn oxy hóa nitrit (NOB).
- Tác động của nồng độ $\text{COD}$ nạp lên $\text{NO}_3^-$-$\text{N}$ (Hình S5(c)):
  - Khi $\text{COD} < 189.87\text{ mg/L}$: Thiếu hụt cacbon hữu cơ làm suy giảm hoạt tính khử nitrat dị dưỡng, gây tích lũy $\text{NO}_3^-$-$\text{N}$.
  - Khi $\text{COD} > 316.46\text{ mg/L}$: Nồng độ chất hữu cơ cao gây ức chế vi khuẩn Anammox, làm suy giảm hiệu suất loại bỏ nitơ toàn hệ thống.
  - Dải nồng độ $\text{COD}$ nạp tối ưu nằm trong khoảng $200.42 - 305.91\text{ mg/L}$.

#### 3.3.4 Tác động của dinh dưỡng nạp và tải trọng NLR lên NO3--N và NO2--N
- Tác động của $\text{TIN}$ nạp và $\text{NO}_3^-$-$\text{N}$ nạp lên $\text{NO}_3^-$-$\text{N}$ dòng ra (Hình S5(d), (e)):
  - Khi $\text{TIN}$ nạp thấp ($< 55.33\text{ mg/L}$), nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra duy trì ở mức cao từ $6.85\text{ mg/L}$ đến $7.82\text{ mg/L}$.
  - Sau đó, nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra tăng dần từ $4.41\text{ mg/L}$ lên $7.42\text{ mg/L}$ theo $\text{NO}_3^-$-$\text{N}$ nạp. Nồng độ này tăng từ $4.45\text{ mg/L}$ lên $5.81\text{ mg/L}$ theo $\text{TIN}$ nạp.
- Tác động của tải trọng nạp $\text{NLR}$ lên $\text{NO}_2^-$-$\text{N}$ dòng ra (Hình S7(e)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ nạp, $\text{NO}_3^-$-$\text{N}$ nạp và $\text{TIN}$ nạp tăng đều thúc đẩy tăng nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra (Hình S7(b)-(d)).
  - Tải trọng nạp nitơ thấp ($\text{NLR} < 0.95\text{ kg N/m}^3/\text{ngày}$) gây tích lũy $\text{NO}_2^-$-$\text{N}$ cao ở mức $4.57\text{ mg/L}$.
  - Khi $\text{NLR} > 0.95\text{ kg N/m}^3/\text{ngày}$, nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra giảm nhanh xuống $2.51\text{ mg/L}$ và duy trì ổn định.


### 3.4 Tác động tương hỗ đa biến (2D PDP) của HRT, COD và thành phần nitơ lên NO3--N và NO2--N

#### 3.4.1 Tương tác giữa Thời gian vận hành và NO3--N nạp qua con đường DNRA
- Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra đạt đỉnh cao nhất ở giai đoạn đầu vận hành kết hợp nồng độ $\text{NO}_3^-$-$\text{N}$ nạp cao (Hình S6(a)).
- Khi kéo dài thời gian vận hành, hệ thống Anammox gia tăng mạnh mẽ năng lực loại bỏ $\text{NO}_3^-$-$\text{N}$.
- Cơ chế chuyển hóa: $\text{NO}_3^-$-$\text{N}$ được tiêu thụ qua con đường khử nitrat dị hóa thành amoni (DNRA: Dissimilatory Nitrate Reduction to Ammonium):
  $$\text{NO}_3^- \rightarrow \text{NO}_2^- \rightarrow \text{NH}_4^+$$
- Lượng $\text{NO}_2^-$ và $\text{NH}_4^+$ sinh ra tiếp tục được vi khuẩn Anammox chuyển hóa thành khí $\text{N}_2$. Chuỗi phản ứng liên hoàn này giúp triệt tiêu hoàn toàn lượng nitrat tồn dư.

#### 3.4.2 Tương hỗ phức tạp giữa HRT và các thành phần dinh dưỡng nạp
- Đỉnh nồng độ $\text{NO}_3^-$-$\text{N}$ xuất hiện cố định tại dải $\text{HRT}$ từ $10.47\text{ h}$ đến $10.98\text{ h}$ xuyên suốt toàn bộ thời gian vận hành (Hình S6(b)).
- Thiết lập $\text{HRT} < 9.95\text{ h}$ giúp hạn chế tích lũy $\text{NO}_3^-$-$\text{N}$ trên toàn bộ các dải nồng độ $\text{NO}_3^-$-$\text{N}$ nạp (Hình S6(e)).
- Tương tác giữa $\text{HRT}$ và $\text{TIN}$ nạp (Hình S6(h)):
  - Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra đạt mức thấp khi kết hợp $\text{HRT}$ cao ($> 15.64\text{ h}$) với $\text{TIN}$ nạp cao.
  - Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra cũng đạt mức thấp khi kết hợp $\text{HRT}$ thấp ($< 9.95\text{ h}$) với $\text{TIN}$ nạp thấp.
  - Ngược lại, duy trì $\text{HRT}$ cao ($> 15.64\text{ h}$) ở mức $\text{TIN}$ nạp thấp thúc đẩy tích lũy $\text{NO}_3^-$-$\text{N}$. Điều kiện này tạo thuận lợi cho vi khuẩn NOB phát triển.

#### 3.4.3 Cấu trúc hai thung lũng nồng độ NO3--N giữa COD nạp và HRT
- Tương tác giữa $\text{COD}$ nạp và $\text{HRT}$ thể hiện tính chất phi tuyến phức tạp nhất trên bề mặt 2D PDP (Hình S6(i)).
- Mô hình xác định hai thung lũng nồng độ $\text{NO}_3^-$-$\text{N}$ cực thấp:
  - Thung lũng 1: $\text{COD}$ nạp $200.42 - 305.91\text{ mg/L}$ kết hợp với $\text{HRT} < 9.95\text{ h}$ (rửa trôi vi khuẩn NOB).
  - Thung lũng 2: $\text{COD}$ nạp $200.42 - 305.91\text{ mg/L}$ kết hợp với $\text{HRT}$ từ $11.50\text{ h}$ đến $12.54\text{ h}$ (đủ thời gian cho phản ứng khử nitrat).
- Kỹ sư công nghệ có thể lựa chọn một trong hai vùng vận hành này để cực tiểu hóa nồng độ nitrat đầu ra.

#### 3.4.4 Tương tác giữa các chất dinh dưỡng nạp và điểm tối ưu tuyệt đối
- Mối tương quan thuận giữa nồng độ $\text{NO}_3^-$-$\text{N}$ nạp và $\text{NO}_3^-$-$\text{N}$ dòng ra được xác nhận trên toàn dải đo (Hình S6(f), (g)).
- Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra tăng cao ở vùng $\text{TIN}$ nạp thấp trên mọi khoảng $\text{COD}$ nạp (Hình S6(j)). Nguyên nhân do tỷ lệ $\text{NH}_4^+$-$\text{N}$ chiếm phần lớn trong $\text{TIN}$, làm mất cân bằng cơ chất khử nitrat thiếu khí.
- Điểm vận hành tối ưu tuyệt đối:
  - Phối hợp $\text{TIN}$ nạp từ $59.38\text{ mg/L}$ đến $87.76\text{ mg/L}$ và $\text{COD}$ nạp từ $200.42\text{ mg/L}$ đến $305.91\text{ mg/L}$.
  - Sự kết hợp này đạt nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra thấp kỷ lục, chỉ từ $1.39\text{ mg/L}$ đến $1.64\text{ mg/L}$.

#### 3.4.5 Động học tương tác điều tiết NO2--N dòng ra
- Động học bề mặt 2D PDP của $\text{NO}_2^-$-$\text{N}$ dòng ra thể hiện xu hướng giảm mạnh khi vận hành dài hạn kết hợp với:
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ nạp (Hình S8(a)).
  - Nồng độ $\text{NO}_3^-$-$\text{N}$ nạp (Hình S8(b)).
  - Nồng độ $\text{TIN}$ nạp (Hình S8(c)).
  - Tải trọng nạp $\text{NLR}$ (Hình S8(d)).
- Vận hành dài hạn làm giảm gần như hoàn toàn lượng $\text{NO}_2^-$-$\text{N}$ dòng ra trong các hệ thống Anammox thành công.
- Tương tác giữa các thành phần nitơ nạp và tải trọng $\text{NLR}$ (Hình S8(e)-(j)):
  - $\text{NO}_2^-$-$\text{N}$ dòng ra liên hệ trực tiếp với tải nạp nitơ của hệ thống.
  - Quá trình PD và PN là hai nguồn cung cấp $\text{NO}_2^-$ chủ yếu. Quá trình Anammox tiêu thụ phần lớn lượng $\text{NO}_2^-$ này.
  - Tải nạp nitơ quá cao gây quá tải hệ thống. Hiện tượng này dẫn đến tích lũy $\text{NO}_2^-$-$\text{N}$ nếu sinh khối Anammox chưa đáp ứng kịp.

## Chương 4: Cơ chế điều tiết tổng nitơ vô cơ (TIN) và Tốc độ phản ứng Anammox (NARR)

### 4.1 Phân tích độ quan trọng biến số và đáp ứng đơn biến (1D PDP) cho TIN dòng ra và hiệu suất khử TIN

#### 4.1.1 Thứ bậc quan trọng của các thông số đầu vào đối với TIN dòng ra và hiệu suất xử lý
- Thứ bậc quan trọng của các biến đầu vào đối với nồng độ TIN dòng ra (Hình 2d):
  - Biến quan trọng nhất: TIN nạp.
  - Vị trí thứ hai: Thời gian vận hành.
  - Các vị trí tiếp theo: $\text{NO}_3^--\text{N}$ nạp > HRT > $\text{NH}_4^+-\text{N}$ nạp > NLR.
- Nồng độ TIN dòng ra phụ thuộc trực tiếp vào tổng lượng nitơ nạp và thời gian thích nghi của hệ vi sinh.
- Thứ bậc quan trọng của các biến đầu vào đối với hiệu suất khử TIN có sự dịch chuyển rõ rệt (Hình 2f):
  - Nhóm thông số nguồn cacbon hữu cơ giữ vai trò chi phối hàng đầu: COD nạp và tỷ lệ C/N.
  - Các thông số vận hành thủy lực và tải trọng đóng vai trò quan trọng kế tiếp: HRT và NLR.
  - Cơ chế kiểm soát: Nguồn cacbon quyết định hiệu quả khử nitrat một phần (PDA) hoặc cạnh tranh vi sinh dị dưỡng.
  - Đồng thời, HRT và NLR kiểm soát thời gian tiếp xúc của cơ chất với sinh khối vi sinh vật.

#### 4.1.2 Động học đáp ứng đơn biến (1D PDP) của nồng độ TIN dòng ra
- Ảnh hưởng của thời gian vận hành lên nồng độ TIN dòng ra (Hình S9a):
  - Nồng độ TIN dòng ra giảm đơn điệu và liên tục theo thời gian vận hành.
  - Hiện tượng này phản ánh sự thuần hóa, làm giàu và gia tăng sinh khối của vi khuẩn Anammox trong bùn sinh học.
- Tác động phi tuyến của thời gian lưu thủy lực (HRT) lên nồng độ TIN dòng ra (Hình S9b):
  - Cả dải HRT ngắn ($< 6.84\text{ h}$) và dải HRT dài ($> 24.45\text{ h}$) đều duy trì nồng độ TIN dòng ra ở mức rất thấp.
  - Dải HRT trung gian tạo ra vùng tích lũy nitơ do sự mất cân bằng giữa tốc độ chuyển hóa cơ chất và lưu lượng dòng chảy.
- Ngưỡng nồng độ tới hạn làm bùng phát nồng độ TIN dòng ra (Hình S9c, S9d, S9e):
  - Ngưỡng nồng độ $\text{NH}_4^+-\text{N}$ nạp tới hạn: $181.18\text{ mg/L}$.
  - Ngưỡng nồng độ $\text{NO}_3^--\text{N}$ nạp tới hạn: $50.07\text{ mg/L}$.
  - Ngưỡng nồng độ TIN nạp tới hạn: $95.87\text{ mg/L}$.
  - Cơ chế bão hòa: Khi nồng độ cơ chất vượt qua các ngưỡng trên, tốc độ chuyển hóa của hệ Anammox bị bão hòa.
  - Lượng cơ chất dư thừa thoát ra ngoài làm tăng nồng độ TIN dòng ra.
- Đáp ứng của nồng độ TIN dòng ra đối với tải trọng nitơ (NLR) (Hình S9f):
  - Giá trị TIN dòng ra không tăng tuyến tính theo sự gia tăng của NLR đơn thuần.
  - Nguyên nhân: NLR chịu sự chi phối đồng thời của TIN nạp và HRT theo phương trình động học:
    $$NLR = \frac{TIN_{inf} \times 24}{1000 \times HRT}$$
  - Mối quan hệ tương hỗ này ngăn cản tác động đơn biến độc lập của NLR lên nồng độ dòng ra.

#### 4.1.3 Động học đáp ứng đơn biến (1D PDP) của hiệu suất khử TIN
- Mối quan hệ giữa thời gian vận hành và hiệu suất khử TIN (Hình S11a):
  - Hiệu suất khử TIN tăng trưởng liên tục và tiệm cận mức bình nguyên ổn định theo thời gian vận hành.
  - Xu hướng này xác nhận mức độ hoàn thiện cấu trúc hạt bùn và sự ổn định của cộng đồng vi sinh vật.
- Tác động của HRT lên hiệu suất khử TIN (Hình S11e):
  - Hiệu suất khử TIN đạt đỉnh ở hai khoảng HRT tách biệt: HRT ngắn ($< 6.84\text{ h}$) và HRT dài ($> 24.45\text{ h}$).
  - Kết quả này nhất quán với xu hướng cực tiểu hóa nồng độ TIN dòng ra tại hai khoảng HRT này.
- Các giá trị vận hành tối ưu đơn biến mang lại hiệu suất khử TIN cao nhất (Hình S11b, S11c, S11d, S11f):
  - Nồng độ TIN nạp tối ưu: $TIN_{inf} = 87.76\text{ mg/L}$.
  - Nồng độ COD nạp tối ưu: $COD_{inf} = 179.33\text{ mg/L}$.
  - Tỷ lệ dinh dưỡng C/N tối ưu: $\text{C/N} = 2.95$.
  - Tải trọng nạp nitơ tối ưu: $NLR = 0.49\text{ kg N/m}^3\text{/d}$.
- Cơ chế sinh hóa tại điểm làm việc tối ưu:
  - Giá trị $\text{C/N} = 2.95$ và $COD_{inf} = 179.33\text{ mg/L}$ cung cấp vừa đủ electron cho phản ứng khử nitrat một phần.
  - Tỷ lệ này ức chế sự phát triển lấn át của vi khuẩn dị dưỡng hoàn toàn.
  - Nhờ đó, hệ thống bảo toàn sinh khối và cơ chất cho vi khuẩn Anammox.

### 4.2 Phản ứng bề mặt tương tác hai chiều (2D PDP) cho TIN và vùng vận hành tối ưu

#### 4.2.1 Bản đồ tương tác hai chiều (2D PDP) kiểm soát nồng độ TIN dòng ra
- Tương tác giữa Thời gian vận hành và các thông số vận hành (Hình S10a, S10e):
  - Nồng độ TIN dòng ra giảm mạnh khi tăng thời gian vận hành trong cả hai biểu đồ tương tác với HRT và NLR.
  - Hệ thống lâu năm có sinh khối dày đặc giúp bảo vệ phản ứng Anammox trước các biến động tải trọng.
- Tương tác giữa Thời gian vận hành và nồng độ nitơ đầu vào (Hình S10b, S10c, S10d):
  - Nồng độ TIN dòng ra tăng khi $\text{NH}_4^+-\text{N}$ nạp, $\text{NO}_3^--\text{N}$ nạp và TIN nạp tăng cao.
  - Tuy nhiên, hệ thống có thời gian vận hành dài kiểm soát nồng độ nitơ dòng ra tốt hơn hệ thống mới khởi động.
- Cấu trúc các vùng trũng nồng độ (thung lũng tối ưu) của TIN dòng ra trên mặt phẳng HRT và nitơ nạp (Hình S10f, S10g, S10h):
  - Nồng độ TIN dòng ra đạt các giá trị cực tiểu tại bốn dải HRT đặc thù:
    1. Dải HRT cực ngắn: $HRT < 8.91\text{ h}$.
    2. Dải HRT trung bình thấp: $HRT = 11.50 - 12.54\text{ h}$.
    3. Dải HRT trung bình cao: $HRT = 15.64 - 17.20\text{ h}$.
    4. Dải HRT dài: $HRT > 24.45\text{ h}$.
- Tương tác giữa HRT và NLR đối với TIN dòng ra (Hình S10i):
  - Khi hệ thống chịu mức NLR cao, HRT dài ($> 24.45\text{ h}$) và HRT cực ngắn ($< 2.18\text{ h}$) tạo ra TIN dòng ra thấp nhất.
  - Tại HRT cực ngắn kết hợp NLR cao, tốc độ dòng chảy lớn thúc đẩy chuyển khối cơ chất vào hạt bùn Anammox.

#### 4.2.2 Hai chế độ vận hành phối hợp tối ưu (Matching Operational Regimes) cho hiệu suất khử TIN
- Tương tác đa biến với thời gian vận hành (Hình S12a - S12e):
  - Hiệu suất khử TIN tăng rõ rệt khi kéo dài thời gian vận hành kết hợp với các mức tải đầu vào thấp.
  - Các mức tải đầu vào thấp bao gồm: TIN nạp thấp, COD nạp thấp, C/N thấp và NLR thấp.
- Mô hình ghép nối hai vùng vận hành tối ưu từ biểu đồ tương tác 2D PDP giữa TIN nạp và HRT (Hình S12g):
  - Vùng 1 (Chế độ nồng độ nạp thấp - Tốc độ nhanh):
    + Khoảng TIN nạp tối ưu: $71.54 - 87.76\text{ mg/L}$.
    + Khoảng HRT tối ưu: $0.63 - 6.84\text{ h}$.
    + Đặc điểm: Hiệu suất khử TIN đạt đỉnh cao nhất, giảm thiểu dung tích công trình và tối ưu hóa chi phí đầu tư.
    + Khả năng ứng dụng: Vùng 1 phù hợp với xử lý nước thải đô thị dòng chính có nồng độ chất ô nhiễm trung bình và lưu lượng lớn.
  - Vùng 2 (Chế độ nồng độ nạp cao - Lưu giữ kéo dài):
    + Khoảng TIN nạp tối ưu: $> 108.03\text{ mg/L}$.
    + Khoảng HRT tối ưu: $24.45 - 26\text{ h}$.
    + Đặc điểm: Chế độ này duy trì hiệu suất khử TIN cao đối với dòng thải có nồng độ đậm đặc nhờ kéo dài thời gian tiếp xúc.
    + Khả năng ứng dụng: Phù hợp cho xử lý dòng bên (sidestream), nước thải công nghiệp hoặc nước rỉ rác có nồng độ nitơ cao.
- Tương tác giữa TIN nạp với COD nạp và NLR (Hình S12f, S12h):
  - TIN nạp kết hợp COD nạp: Hiệu suất khử TIN cao nhất tại $TIN_{inf} = 71.54 - 87.76\text{ mg/L}$ và $COD_{inf} = 200.42 - 221.52\text{ mg/L}$.
  - TIN nạp kết hợp NLR: Dải $TIN_{inf} = 71.54 - 87.76\text{ mg/L}$ luôn mang lại hiệu suất đỉnh độc lập với biến thiên của NLR.
- Tác động phối hợp của COD nạp lên hiệu suất khử TIN (Hình S12i, S12j):
  - COD nạp kết hợp HRT: Hiệu suất khử TIN đạt đỉnh khi COD nạp từ $168.78 - 200.42\text{ mg/L}$ cùng HRT $0.63 - 6.84\text{ h}$ hoặc $24.45 - 26\text{ h}$.
  - COD nạp kết hợp NLR: Khoảng COD nạp $168.78 - 200.42\text{ mg/L}$ đảm bảo hiệu suất khử TIN tối ưu trên mọi dải tải trọng NLR.

#### 4.2.3 Đánh giá khả năng tương thích công nghệ và điều kiện áp dụng cho nước thải đô thị
- Tương thích nguồn cacbon:
  - Dải COD nạp tối ưu ($168.78 - 200.42\text{ mg/L}$) trùng khớp hoàn toàn với dải COD điển hình của nước thải đô thị ($150 - 250\text{ mg/L}$).
  - Hệ thống không cần bổ sung nguồn cacbon hữu cơ ngoại sinh.
- Yêu cầu về ngưỡng nồng độ nitơ nạp:
  - Hệ thống Anammox yêu cầu nồng độ TIN nạp đạt ngưỡng $70 - 90\text{ mg/L}$ (tối ưu tại $71.54 - 87.76\text{ mg/L}$) để phát huy công suất tối đa.
  - Thách thức: Nước thải đô thị thông thường chỉ có nồng độ TIN khoảng $30 - 60\text{ mg/L}$.
  - Giải pháp kỹ thuật: Áp dụng công nghệ tiền xử lý hoặc tách dòng để nâng nồng độ TIN lên dải hiệu năng đỉnh.

### 4.3 Phân tích độ nhạy và cơ chế thúc đẩy tốc độ phản ứng Anammox (NARR)

#### 4.3.1 Động học đơn biến (1D PDP) và mối quan hệ nghịch đảo giữa HRT với NARR
- Xếp hạng độ quan trọng biến số cho chỉ số NARR (Hình 2g):
  - Các biến ảnh hưởng cốt lõi gồm: HRT, NLR, TIN nạp, $\text{NO}_2^--\text{N}$ nạp, COD nạp và $\text{NH}_4^+-\text{N}$ nạp.
- Mối quan hệ nghịch đảo giữa HRT và NARR (Hình S13a):
  - Giá trị NARR giảm đơn điệu khi tăng HRT.
  - Cơ sở toán học: Phương trình tính toán tốc độ chuyển hóa theo đường Anammox có dạng:
    $$NARR = \frac{\Delta S_{N,anammox}}{HRT}$$
  - HRT nằm ở mẫu số của phương trình. Do đó, giảm HRT trực tiếp làm tăng giá trị động học NARR.
- Mối quan hệ đồng biến giữa các biến tải trọng nitơ và NARR (Hình S13b, S13c, S13d, S13f):
  - NARR tăng đơn điệu theo NLR, TIN nạp, $\text{NO}_2^--\text{N}$ nạp và $\text{NH}_4^+-\text{N}$ nạp.
  - Cơ chế sinh lý: Nồng độ cơ chất dồi dào kích hoạt hoạt tính trao đổi chất của vi khuẩn Anammox.
- Đáp ứng của NARR đối với COD nạp (Hình S13e):
  - NARR giữ mức ổn định và không đổi khi COD nạp dưới $506.33\text{ mg/L}$.
  - NARR tăng đột biến khi COD nạp vượt qua ngưỡng $506.33\text{ mg/L}$.
  - Cơ chế: Mức COD cao thúc đẩy vi khuẩn khử nitrat một phần (PDA) cung cấp lượng lớn $\text{NO}_2^-$ cho vi khuẩn Anammox.

#### 4.3.2 Ngưỡng bùng nổ hoạt tính Anammox trên bề mặt tương tác hai chiều (2D PDP)
- Ngưỡng giới hạn kích hoạt bùng nổ phản ứng NARR:
  - Biểu đồ 2D PDP xác định NARR tăng vọt khi đồng thời vượt các ngưỡng sau:
    - Tải trọng nitơ: $NLR > 1.28\text{ kg N/m}^3\text{/d}$.
    - Tổng nitơ nạp: $TIN_{inf} > 176.89\text{ mg/L}$.
    - Nitrit nạp: $\text{NO}_2^--\text{N}_{inf} > 18.78\text{ mg/L}$.
    - Amoni nạp: $\text{NH}_4^+-\text{N}_{inf} > 152.61\text{ mg/L}$.
    - COD nạp: $COD_{inf} > 506.33\text{ mg/L}$ (xác nhận trên Hình S14a, S14b, S14c, S14d).
- Cặp ghép phối hợp cơ chất tạo phản ứng NARR cực đại (Hình S14e):
  - Đỉnh phản ứng NARR cao nhất xuất hiện khi kết hợp đồng thời $TIN_{inf} > 176.94\text{ mg/L}$ và $\text{NO}_2^--\text{N}_{inf} > 18.78\text{ mg/L}$.
  - Sự kết hợp này cung cấp đầy đủ chất nhận electron ($\text{NO}_2^-$), giải phóng tối đa tiềm năng trao đổi chất của vi khuẩn.
- Phối hợp giữa thông số thủy lực và tải trọng kích thích NARR cực đại (Hình S14f - S14j):
  - Giá trị NARR tăng mạnh khi duy trì HRT ngắn ở ngưỡng $HRT < 7.36\text{ h}$.
  - NARR đạt cực đại khi kết hợp điều kiện $HRT < 7.36\text{ h}$ với $NLR > 2.18\text{ kg N/m}^3\text{/d}$ và $\text{NH}_4^+-\text{N}$ nạp $> 148.53\text{ mg/L}$.
  - Lưu ý tài liệu gốc ghi nhận giá trị số 148.53 với đơn vị in nhầm thành $\text{kg/m}^3\text{/d}$ thay vì $\text{mg/L}$.

#### 4.3.3 Khả năng thích ứng của hệ thống Anammox dưới áp lực tải trọng nitơ cao
- Tính thích ứng của hệ sinh học Anammox:
  - Hoạt tính NARR đạt đỉnh khi kết hợp tải trọng nitơ lớn và thời gian lưu thủy lực ngắn.
  - Kết quả chứng minh vi khuẩn Anammox không bị suy giảm hoạt tính khi chịu tải trọng cao.
- Ý nghĩa kỹ thuật trong công nghệ môi trường:
  - Hệ thống xử lý sinh học dựa trên Anammox hoàn toàn đáp ứng áp lực xử lý lớn trong các trạm xử lý nước thải hiện đại.
  - Kết quả này cho phép thiết kế các bể phản ứng sinh học nhỏ gọn, tiết kiệm diện tích và giảm chi phí năng lượng sục khí.

## Chương 5: Ứng dụng kỹ thuật thực tiễn, Giới hạn nghiên cứu và Định hướng tương lai

### 5.1 Khuyến nghị kỹ thuật vận hành trạm xử lý nước thải dòng chính ứng dụng Anammox
#### 5.1.1 Đánh giá cấu hình công nghệ và đặc tính nguồn nước nạp
- Lựa chọn cấu hình bể phản ứng và dạng hình thái sinh khối:
  - Bể phản ứng dòng chảy liên tục (continuous flow reactor) vận hành với bùn hạt vi sinh vật (microbial aggregates) là giải pháp tối ưu nhất.
  - Cấu trúc bùn hạt Anammox duy trì mật độ sinh khối cao hơn cấu trúc bùn bông (floc).
  - Cấu hình này giúp hệ thống tiếp nhận và xử lý tải trọng ô nhiễm nitơ cao trong điều kiện dòng chảy biến động.
- Khoảng cách giữa thực nghiệm nước thải nhân tạo và nước thải đô thị:
  - Phần lớn nghiên cứu phòng thí nghiệm sử dụng nước thải nhân tạo với thành phần hóa lý đơn giản.
  - Nước thải đô thị thực tế có thành phần cơ chất phức tạp và nồng độ chất ô nhiễm dao động liên tục.
  - Sự khác biệt lớn này làm suy giảm ý nghĩa thực tế của các mô hình huấn luyện từ dữ liệu nước thải nhân tạo.
  - Kỹ sư vận hành cần hiệu chuẩn lại mô hình dự báo và thông số điều khiển dựa trên đặc tính nước thải thực tế tại hiện trường.
#### 5.1.2 Chiến lược kiểm soát theo phân loại quy trình Anammox (PNA so với PDA)
- Quy trình Nitrit hóa một phần kết hợp Anammox (PNA):
  - Quy trình PNA và quy trình PNA kết hợp PDA đạt hiệu suất khử TIN cao hơn quy trình PDA đơn lẻ.
  - Nồng độ nitơ dòng vào và dòng ra trong quy trình PNA có tương quan thuận rất mạnh, với hệ số tương quan đạt từ 0.55 đến 0.95.
  - Mức tương quan cao này chứng tỏ quy trình PNA rất nhạy cảm với biến động của dòng vào.
  - Hệ thống PNA đòi hỏi hệ thống giám sát liên tục và chiến lược điều khiển nghiêm ngặt hơn quy trình PDA.
- Quy trình Khử nitrat một phần kết hợp Anammox (PDA):
  - Quy trình PDA duy trì nồng độ nitơ dòng ra ổn định hơn trước các biến động tải trọng dòng vào.
  - Cấu hình phối hợp PNA và PDA giúp hệ thống vừa đạt hiệu suất khử nitơ cao, vừa tăng cường tính ổn định vận hành.
#### 5.1.3 Hướng dẫn định lượng chi tiết cho từng chỉ tiêu chất lượng dòng ra
- Kiểm soát nồng độ $\text{NH}_4^+$-N dòng ra:
  - Duy trì tỷ lệ $\text{C/N}$ nạp trong khoảng từ 2.72 đến 6.32.
  - Duy trì nồng độ TIN dòng vào trong dải từ 18.85 đến 87.76 mg/L.
  - Nồng độ $\text{NH}_4^+$-N dòng ra tăng vọt khi $\text{NH}_4^+$-N dòng vào vượt 62.32 mg/L hoặc TIN dòng vào vượt 91.08 mg/L.
  - Nước thải đô thị thông thường có nồng độ nitơ thấp hơn hai ngưỡng trên, rất thuận lợi cho công nghệ Anammox dòng chính.
- Kiểm soát nồng độ $\text{NO}_3^-$-N dòng ra:
  - Vi khuẩn Anammox sản sinh $\text{NO}_3^-$-N như một sản phẩm phụ của chu trình oxy hóa amoni kỵ khí.
  - Theo hệ số tỷ lượng phản ứng sinh hóa, Anammox tạo ra 0.26 mol $\text{NO}_3^-$-N khi oxy hóa 1 mol $\text{NH}_4^+$-N.
  - $\text{NO}_3^-$-N chiếm phần lớn nồng độ tổng nitơ vô cơ (TIN) trong dòng ra của trạm xử lý.
  - Vận hành hệ thống theo các ngưỡng định lượng sau để cực tiểu hóa $\text{NO}_3^-$-N dòng ra:
    - Nồng độ COD dòng vào: duy trì trong dải 200.42 – 305.91 mg/L.
    - Thời gian lưu thủy lực (HRT): duy trì $\text{HRT} < 9.95\text{ h}$ hoặc trong khoảng 11.50 – 12.54 h.
    - Nồng độ TIN dòng vào: duy trì trong dải 59.38 – 87.76 mg/L.
    - Tải trọng nạp nitơ (NLR): vận hành ở mức $\text{NLR} > 0.95\text{ kg N/m}^3\text{/d}$.
- Tối ưu hóa hiệu suất khử tổng nitơ vô cơ (TIN) tổng thể:
  - Duy trì nồng độ COD dòng vào ở mức thấp từ 168.78 đến 200.42 mg/L để đạt hiệu suất khử TIN cao nhất.
  - Phối hợp các cặp thông số TIN dòng vào và HRT theo chiến lược tương thích:
    - Cặp tương thích 1 (TIN thấp - HRT ngắn): nồng độ TIN dòng vào từ 71.54 đến 87.76 mg/L kết hợp $\text{HRT}$ ngắn từ 0.63 đến 6.84 h.
    - Cặp tương thích 2 (TIN cao - HRT dài): nồng độ TIN dòng vào $> 108.03\text{ mg/L}$ kết hợp $\text{HRT}$ dài từ 24.45 đến 26 h.
    - Tránh phối hợp cặp thông số không tương thích (như nạp TIN cao với HRT ngắn) vì sẽ làm suy giảm nghiêm trọng hiệu suất khử TIN.
- Nâng cao tốc độ loại bỏ nitơ Anammox (NARR):
  - Chỉ số NARR phản ánh trực tiếp hoạt tính chuyển hóa sinh học của quần thể vi khuẩn Anammox trong bể phản ứng.
  - NARR tăng rõ rệt khi tải trọng nạp nitơ tăng và thời gian lưu thủy lực giảm.
  - Thiết lập chế độ vận hành theo các ngưỡng sau để tối đa hóa chỉ số NARR:
    - Thời gian lưu thủy lực: duy trì $\text{HRT} < 7.36\text{ h}$.
    - Tải trọng nạp nitơ: duy trì $\text{NLR} > 1.28\text{ kg N/m}^3\text{/d}$ (đặc biệt hiệu quả khi $\text{NLR} > 2.18\text{ kg N/m}^3\text{/d}$).
    - Nồng độ TIN dòng vào: nạp ở mức $\text{TIN} > 176.89\text{ mg/L}$ (kết hợp $\text{TIN} > 176.94\text{ mg/L}$ và $\text{NO}_2^-\text{-N} > 18.78\text{ mg/L}$ cho phản ứng NARR cao nhất).
    - Nồng độ $\text{NO}_2^-$-N dòng vào: nạp ở mức $> 18.78\text{ mg/L}$.
    - Nồng độ $\text{NH}_4^+$-N dòng vào: nạp ở mức $> 152.61\text{ mg/L}$ (hoặc $> 148.53\text{ mg/L}$).
  - Đề xuất giải pháp kỹ thuật phối trộn nguồn nước:
    - Nước thải đô thị thực tế thường có nồng độ nitơ thấp hơn ngưỡng kích hoạt NARR tối đa.
    - Phối trộn nước thải đô thị với một tỷ lệ nước thải công nghiệp giàu nitơ để kích hoạt tối đa năng lực khử của vi khuẩn Anammox.

### 5.2 Các giới hạn tồn tại trong nghiên cứu mô hình hóa hiện tại
#### 5.2.1 Hiện tượng suy giảm độ chính xác dự đoán ở các chỉ tiêu nhạy cảm
- Đánh giá sai số trên các tập dữ liệu thực nghiệm:
  - Các mô hình học máy tối ưu từ AutoML đạt độ chính xác cao trên tập kiểm tra y văn, với $R^2$ từ 0.814 đến 0.993.
  - Độ chính xác dự đoán giảm nhẹ khi kiểm chứng trên tập dữ liệu thực nghiệm độc lập 185 mẫu của bể UASB:
    - Nồng độ $\text{NO}_2^-$-N dòng ra: mô hình GBM chỉ đạt $R^2 = 0.563$ ($\text{MAE} = 1.045\text{ mg/L}$).
    - Tốc độ phản ứng Anammox (NARR): mô hình Deep Learning chỉ đạt $R^2 = 0.677$ ($\text{MAE} = 0.013\text{ kg N/m}^3\text{/d}$).
    - Nồng độ $\text{NO}_3^-$-N dòng ra: mô hình XGBoost đạt $R^2 = 0.725$ ($\text{MAE} = 2.196\text{ mg/L}$).
- Nguyên nhân kỹ thuật dẫn đến sự suy giảm độ chính xác:
  - Sự khác biệt về điều kiện vận hành và cấu trúc cộng đồng vi sinh vật giữa tập huấn luyện y văn và thực nghiệm độc lập.
  - Các biến số đầu ra như $\text{NO}_2^-$-N, $\text{NO}_3^-$-N và NARR có độ nhạy rất cao với các biến động công nghệ.
  - Nitrit tồn tại như hợp chất trung gian không bền, nồng độ dao động mạnh và gây tích lũy sai số đo đạc qua các bước phản ứng.
- Đề xuất bổ sung biến số giám sát trực tuyến thời gian thực:
  - Nồng độ oxy hòa tan (DO) trong môi trường phản ứng.
  - Giá trị pH dung dịch.
  - Thế oxy hóa khử (ORP).
  - Nồng độ định lượng của các chất hữu cơ gây ức chế sinh học đặc thù.
#### 5.2.2 Hạn chế bản chất của chỉ số COD tổng trong mô tả chất hữu cơ phức tạp
- Thiếu hụt thông tin về cấu trúc hóa học phân tử:
  - Chỉ số COD tổng chỉ đo lượng oxy hóa học cần thiết để oxy hóa toàn bộ cơ chất hữu cơ.
  - COD không phân biệt được các dạng hợp chất hữu cơ và nhóm chức hóa học cấu thành.
  - Nước thải đô thị thực tế chứa nhiều hợp chất hữu cơ đa dạng với cấu trúc hóa học sai khác.
- Cơ chế tác động phân tử của các nhóm thế hữu cơ lên hệ sinh thái Anammox:
  - Nhóm thế alkyl và hydroxyl ($-\text{CH}_3, -\text{OH}$):
    - Làm thay đổi tính kỵ nước của bề mặt tế bào vi khuẩn.
    - Cản trở quá trình khuếch tán cơ chất qua màng tế bào.
    - Gây ảnh hưởng xấu đến độ bền liên kết và độ ổn định của bùn hạt vi sinh vật.
  - Nhóm thế halogen ($-\text{Cl}, -\text{F}$):
    - Đóng góp trực tiếp vào độc tính sinh học đối với hệ sinh thái bùn vi sinh.
    - Gây ức chế mạnh hoạt tính enzym trao đổi chất của vi khuẩn Anammox.
- Hạn chế đối với mô hình học máy:
  - Việc biểu diễn toàn bộ chất hữu cơ bằng một chỉ số COD duy nhất làm mất đi dữ liệu về các nhóm chất độc hại.
  - Các thuật toán học máy không thể nhận diện và học được cơ chế ức chế riêng biệt của từng hợp chất hữu cơ.
#### 5.2.3 Thiếu hụt quy mô dữ liệu hệ vi sinh vật và cấu trúc cộng đồng
- Bất cân xứng về dung lượng dữ liệu:
  - Cơ sở dữ liệu hiện tại tập trung chủ yếu vào các thông số vận hành hóa lý và thủy lực thông thường.
  - Dung lượng dữ liệu phân tích sinh học phân tử và giải trình tự gen vi sinh vật còn rất nhỏ.
- Hạn chế trong cách tiếp cận biến số vi sinh hiện tại:
  - Dữ liệu vi sinh vật mới chỉ được đưa vào dưới dạng một biến phân loại thô sơ về chi Anammox chiếm ưu thế.
  - Dữ liệu chưa nắm bắt được mối quan hệ hợp tác và cạnh tranh giữa Anammox với các vi sinh vật cộng sinh khác (AOB, NOB, vi khuẩn khử nitrat dị dưỡng).
- Định hướng nghiên cứu dữ liệu sinh học:
  - Cần xây dựng quy trình thu thập và chuẩn hóa dữ liệu giải trình tự cộng đồng vi sinh vật độ phân giải cao.
  - Sử dụng học máy để khai phá dữ liệu hệ gen nhằm cung cấp hiểu biết sâu sắc hơn về cơ chế sinh học trong hệ thống xử lý nước thải.

### 5.3 Định hướng phát triển Digital Twin kết hợp vi sinh vật học chính xác và Kết luận
#### 5.3.1 Khái niệm Digital Twin thông tin sinh học (Biology-informed Digital Twins)
- Kiến trúc mô phỏng bản sao số thế hệ mới:
  - Xây dựng bản sao kỹ thuật số tích hợp dữ liệu cảm biến công nghệ trực tuyến với dữ liệu dấu vân tay cộng đồng vi sinh vật độ phân giải cao (high-dimensional microbial community fingerprints).
  - Kết hợp thông tin đa tầng omics (genomics, transcriptomics, metabolomics) với các mô hình động học quá trình và thuật toán học máy.
- Chức năng giám sát và cảnh báo thông minh:
  - Nhận diện sớm các dấu hiệu suy thoái hệ vi sinh vật (suy giảm AOB, bùng phát vi khuẩn NOB, mất cân bằng bùn hạt).
  - Tự động điều chỉnh các thông số vận hành (lưu lượng khí cấp, HRT, tỷ lệ tuần hoàn bùn, dòng nạp cơ chất) trước khi xảy ra hiện tượng suy giảm chất lượng nước dòng ra.
#### 5.3.2 Chuyển đổi mô hình sang quản lý chính xác hệ vi sinh vật (Precision Microbiome Management)
- Dịch chuyển mô thức vận hành công nghệ:
  - Dịch chuyển từ phương thức điều khiển thủy lực theo kinh nghiệm truyền thống (empirical hydraulic control) sang quản lý chính xác hệ vi sinh vật (precision microbiome management).
  - Vận hành trạm xử lý dựa trên nguyên tắc chủ động kiến tạo vi môi trường tối ưu cho vi khuẩn Anammox và vi sinh vật cộng sinh.
- Chiến lược tối ưu hóa đa yếu tố (multifactor optimization):
  - Áp dụng các thuật toán học máy để khai phá các mối quan hệ ẩn giữa biến số hệ vi sinh vật và hiệu quả xử lý thực tế.
  - Đảm bảo trạm xử lý nước thải đô thị dòng chính vận hành liên tục, ổn định và đạt hiệu suất xử lý nitơ cao nhất.
#### 5.3.3 Kết luận toàn diện của công trình nghiên cứu
- Ưu thế công nghệ qua khai phá dữ liệu lớn:
  - Phân tích dữ liệu lớn khẳng định bể phản ứng dòng liên tục sử dụng bùn hạt Anammox có năng lực xử lý vượt trội đối với tải trọng nitơ cao.
  - Quy trình PNA có độ nhạy nạp cao hơn, trong khi quy trình phối hợp PNA và PDA đạt hiệu suất khử TIN tối ưu.
- Hiệu năng xuất sắc của nền tảng AutoML:
  - Thuật toán AutoML tự động hóa quy trình xây dựng các mô hình dự báo hiệu năng cao cho toàn bộ các chỉ tiêu chất lượng dòng ra chính.
  - Các mô hình dựa trên thuật toán tăng cường độ dốc (GBM và XGBoost) đạt độ chính xác dự báo cao nhất:
    - Tập kiểm tra y văn: $R^2 = 0.814\text{ – }0.993$.
    - Tập thực nghiệm kiểm chứng độc lập 185 mẫu UASB: $R^2 = 0.725\text{ – }0.945$ đối với các chỉ tiêu nồng độ nitơ dòng ra.
  - Kết quả chứng minh khả năng tổng quát hóa xuất sắc của các mô hình trên các tập dữ liệu độc lập chưa từng thấy trong quá trình huấn luyện.
- Ý nghĩa kỹ thuật của phân tích giải thích mô hình (PDP):
  - Phân tích 1D PDP và 2D PDP xác lập các ngưỡng vận hành định lượng tin cậy cho kỹ thuật môi trường:
    - Kiểm soát $\text{NH}_4^+$-N dòng ra: tỷ lệ $\text{C/N}$ từ 2.72 đến 6.32, nồng độ TIN dòng vào từ 18.85 đến 87.76 mg/L.
    - Cực tiểu hóa $\text{NO}_3^-$-N dòng ra: nồng độ COD dòng vào từ 200.42 đến 305.91 mg/L, $\text{NLR} > 0.95\text{ kg N/m}^3\text{/d}$, $\text{HRT} < 9.95\text{ h}$ hoặc trong khoảng 11.50 – 12.54 h.
    - Tối ưu hóa hiệu suất khử TIN: nồng độ COD dòng vào từ 168.78 đến 200.42 mg/L, ghép nối TIN thấp (71.54 – 87.76 mg/L) với HRT ngắn (0.63 – 6.84 h).
    - Thúc đẩy tốc độ Anammox NARR: duy trì $\text{HRT} < 7.36\text{ h}$, $\text{NLR} > 1.28\text{ kg N/m}^3\text{/d}$ và TIN dòng vào $> 176.89\text{ mg/L}$.
  - Các khuyến nghị kỹ thuật giải quyết căn bản bài toán mất ổn định trong vận hành công nghệ Anammox xử lý nước thải đô thị dòng chính.
