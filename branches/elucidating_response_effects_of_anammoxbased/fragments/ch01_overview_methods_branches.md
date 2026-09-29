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

---

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

---

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

---

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

---

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
