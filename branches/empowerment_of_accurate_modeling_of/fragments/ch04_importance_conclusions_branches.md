## Chương 4: Phân tích Tầm quan trọng Đặc trưng, Giới hạn và Kết luận

### 4.1 Phân tích độ quan trọng đặc trưng bằng phương pháp kết hợp (Ensemble Ranking Score)

#### Vị thế chi phối của nồng độ COD đầu vào (COD-in) và vai trò cảnh báo sớm
- Đặc trưng $COD\text{-in}$ giữ vị trí số một trong mọi mô hình và phương pháp giải thích (Hình 7).
- Giá trị $COD\text{-in}$ phản ánh trực tiếp tải nạp hữu cơ (OLR). Biến này đo lường nồng độ chất ô nhiễm vào bể AnMBR.
- Quá trình phân hủy kỵ khí phụ thuộc vào nồng độ cơ chất nạp. Nồng độ này duy trì hoạt tính trao đổi chất của sinh khối.
- Đặc trưng $COD\text{-in}$ đóng vai trò tín hiệu cảnh báo sớm (warning signal) đáng tin cậy cho dự đoán hiệu suất loại bỏ $COD\text{-re}$.
- Khi cảm biến phát hiện nồng độ $COD\text{-in}$ tăng vọt, hệ thống điều khiển tự động giảm lưu lượng nạp ($Q_{\text{in}}$).
- Việc giảm lưu lượng nạp làm tăng thời gian lưu thủy lực ($HRT$). Vi sinh vật có thêm thời gian để phân hủy cơ chất hữu cơ.

#### Vai trò nổi bật của ngày vận hành (OD) phản ánh động học phi tĩnh
- Biến $OD$ giữ vị trí quan trọng thứ hai khi đưa vào mô hình (Hình 7(c–g)). Thứ hạng này xuất hiện trên toàn bộ các cấu hình.
- Biến $OD$ đóng vai trò đại diện thời gian (time-proxy variable) cho động học phi tĩnh (non-stationary dynamics) của hệ AnMBR dài hạn.
- Sự tích lũy lớp bánh bùn (cake layer) và tắc nghẽn màng (membrane fouling) gia tăng liên tục theo thời gian vận hành.
- Quần xã vi sinh vật kỵ khí trải qua quá trình thích nghi liên tục. Cấu trúc sinh khối biến đổi theo số ngày vận hành thực tế.
- Giám sát vận hành AnMBR không thể chỉ dựa vào các chỉ số cảm biến tức thời (instantaneous sensor readings).
- Kỹ sư vận hành phải tích hợp lịch trình bảo dưỡng màng và sục rửa định kỳ phụ thuộc thời gian tích lũy ($OD$).

#### Sự biến thiên thứ hạng giữa các phương pháp giải thích (Tree-based, Permutation, SHAP)
- Ba phương pháp cho thấy sai khác thứ hạng rõ rệt (Hình 7(b, d, f, h)). Sự phân hóa này tập trung ở các đặc trưng bậc trung.
- Độ quan trọng Gini (Tree-based method) đo lường mức giảm độ tinh khiết chuẩn hóa trên các điểm rẽ nhánh cây quyết định.
- Độ quan trọng hoán vị (Permutation Importance) đo mức suy giảm hiệu năng $RMSE$ qua $K = 30$ lần xáo trộn ngẫu nhiên:
  $$i_j = s - \frac{1}{K} \sum_{k=1}^K s_{k,j}$$
- Ở đây, $s$ là điểm sai số gốc ($RMSE$). Giá trị $s_{k,j}$ là sai số sau khi hoán vị đặc trưng $j$ tại lần lặp $k$.
- Phương pháp SHAP (Shapley Additive exPlanations) tính toán đóng góp biên trung bình theo lý thuyết trò chơi hợp tác:
  $$\phi_i(f, x) = \sum_{S \subseteq S_{\text{all}} \setminus \{i\}} \frac{|S|!(M - |S| - 1)!}{M!} [f_x(S \cup \{i\}) - f_x(S)]$$
- Ở đây, $M$ là tổng số biến đầu vào, $S$ là tập con các biến không chứa $i$, và $|S|$ là kích thước tập con.
- Đối với mô hình không có $OD$ huấn luyện trên tập gốc, nhiệt độ môi trường ($T\text{-env}$) xếp thứ hai (Hình 7(a)).
- Khi huấn luyện cùng dữ liệu bổ sung, chỉ số $pH\text{-in}$ lại vươn lên thành đặc trưng quan trọng thứ hai (Hình 7(e)).
- Các đặc trưng môi trường như $T\text{-env}$, $T\text{-in}$, và $pH\text{-in}$ thể hiện mức độ đóng góp thấp hơn nhiều so với $COD\text{-in}$.
- Khung điểm xếp hạng kết hợp (Ensemble Ranking Score) chuẩn hóa thứ tự từ $1$ (ít quan trọng nhất) đến $M$ (quan trọng nhất):
  $$R_j = \sum_{m \in \{\text{Tree, Perm, SHAP}\}} \text{Rank}_m(j)$$
- Điểm xếp hạng kết hợp giải quyết triệt để sự thiếu nhất quán giữa các tiên đề toán học riêng lẻ.

#### Tác động làm xáo trộn thứ tự đặc trưng khi thêm dữ liệu nhiễu (M2)
- Huấn luyện với tập dữ liệu mở rộng M2 (7–546 ngày, 320 mẫu) làm biến động mạnh thứ bậc đặc trưng.
- Kết quả giải thích của mô hình M2 (Hình 7(h)) sai lệch mạnh so với mô hình gốc (Hình 7(f)).
- Tương quan Spearman khẳng định các đặc trưng trong tập M2 ít liên kết với $COD\text{-re}$ (Hình S3 và S4).
- Tập M2 mang theo nhiễu từ các đợt vận hành không đồng nhất. Dữ liệu này gây ra hiện tượng dịch chuyển phân phối (distribution shift).
- Nhiễu ngẫu nhiên làm biến dạng cấu trúc phân nhánh cây và làm sai lệch giá trị Shapley biên.
- Kết quả này củng cố phát hiện ở Mục 3.3. Dữ liệu mở rộng M2 làm giảm độ chuẩn xác của mô hình học máy.

#### Ý nghĩa kỹ thuật và ứng dụng trong tự động hóa kiểm soát vận hành AnMBR
- Kết quả xếp hạng đặc trưng cho phép phân tầng mức độ ưu tiên của các biến điều khiển trong thực tế công nghệ.
- Thiết lập cơ chế kiểm soát phản hồi hai vòng lặp (dual-loop feedback control architecture):
  - Vòng lặp phản hồi nhanh (Fast response loop): Giám sát liên tục nồng độ $COD\text{-in}$ để điều chỉnh kịp thời tải lượng nạp hữu cơ.
  - Vòng lặp phản hồi chậm (Slow supervisory loop): Lập kế hoạch rửa ngược (backwash), sục khí biogas và ngâm hóa chất dựa trên biến $OD$.
- Tối ưu chi phí quan trắc. Đơn vị vận hành có thể giảm bớt các cảm biến thứ cấp có đóng góp dự báo thấp.
- Mô hình giúp đảm bảo hệ thống màng AnMBR vận hành an toàn. Hệ thống ngăn ngừa tắc nghẽn màng sớm và ổn định dòng ra xử lý nước thải.

### 4.2 Giới hạn nghiên cứu và định hướng phát triển tương lai

#### Tính chất chỉ dấu của kết quả so sánh trong thiết lập thực nghiệm
- Mô hình AutoML vượt trội so với các mạng nơ-ron sâu (FCN, CNN, DenseNet) trên cùng tỷ lệ chia dữ liệu cố định (9:1).
- Kết quả so sánh này mang tính chất chỉ dấu (indicative) trong phạm vi thiết lập thực nghiệm cụ thể của nghiên cứu.
- Các nhà nghiên cứu không nên coi kết quả này là sự vượt trội tuyệt đối trên mọi kịch bản và kiến trúc khác.
- Mô hình học máy dạng cây (Tree-based ML) gặp rào cản ngoại suy (extrapolation limitation) khi giá trị đầu vào vượt ngoài dải huấn luyện.
- Mô hình cây dự đoán kém chính xác khi $OD > 414$ ngày. Mô hình cũng giảm độ tin cậy khi $COD\text{-in}$ vượt ngưỡng cực đại.

#### Ý nghĩa thống kê của các biến sinh khối (MLSS/MLVSS) so với cơ chế vi sinh
- Hai biến đặc trưng $MLSS$ và $MLVSS$ thể hiện mức độ đóng góp rất thấp vào hiệu năng mô hình học máy.
- Đóng góp thấp này chỉ phản ánh mối tương quan thống kê trên tập dữ liệu khảo sát hiện hành.
- Người vận hành không được diễn giải kết quả này thành kết luận về mặt cơ chế vật lý hoặc sinh học kỵ khí.
- Về mặt cơ chế sinh hóa, nồng độ bùn hoạt tính kỵ khí ($MLVSS$) giữ vai trò trung tâm phân hủy chất hữu cơ.
- Biến sinh khối xếp hạng thấp do tần suất phân tích thưa thớt (đo hàng tuần). Dải biến động thực tế của bùn cũng rất hẹp.
- Sai số tích lũy trong quy trình sấy cân phòng thí nghiệm làm suy giảm tín hiệu tương quan của biến sinh khối.

#### Bài học về tính nhất quán dữ liệu thay vì số lượng thuần túy
- Hiệu năng mô hình giảm sút khi tăng từ 185 lên 320 mẫu. Hiện tượng này đem lại bài học đắt giá về chất lượng dữ liệu.
- Quy mô dữ liệu lớn không đồng nghĩa với độ chính xác cao nếu dữ liệu thiếu tính đồng nhất ngữ cảnh vận hành.
- Hiện tượng dịch chuyển phân phối (distribution shift) giữa các giai đoạn thí nghiệm gây tổn hại nghiêm trọng cho giải thuật học máy.
- Quy trình chuẩn bị dữ liệu (data curation) cần ưu tiên độ tin cậy và tính nhất quán hơn việc gộp dữ liệu bừa bãi.
- Kỹ sư môi trường cần kiểm soát chặt chẽ điều kiện vận hành trước khi kết hợp dữ liệu từ nhiều nguồn khác nhau.

#### Nhu cầu chuyển đổi từ ước lượng điểm sang mô hình hóa xác suất (Probabilistic ML)
- Mô hình hiện tại chỉ cung cấp các ước lượng điểm tất định (deterministic point estimates) cho giá trị $COD\text{-re}$.
- Dự đoán điểm đơn lẻ bỏ qua độ bất định cố hữu. Hệ phản ứng sinh học kỵ khí luôn có động học dao động phức tạp.
- Các nghiên cứu tương lai cần tích hợp các hướng tiếp cận học máy xác suất (Probabilistic Machine Learning).
- Phương pháp hồi quy lượng vị (Quantile Regression), mạng Bayes (Bayesian Neural Networks) hoặc Conformal Prediction cần được nghiên cứu áp dụng.
- Mô hình xác suất cung cấp khoảng dự đoán (prediction intervals). Kỹ thuật này định lượng độ bất định và giúp ra quyết định an toàn.

### 4.3 Kết luận tổng quát và đóng góp khoa học

#### Tổng kết hiệu năng vượt trội và tính khả thi của FLAML AutoML
- Công trình giải quyết thành công rào cản chuyên môn khoa học dữ liệu cho kỹ sư vận hành xử lý nước thải.
- Khung FLAML AutoML chứng minh tính khả thi vượt trội trong việc xây dựng mô hình dự đoán hiệu suất AnMBR chính xác.
- Mô hình AutoML họ cây đảo ngược hoàn toàn $R^2$ âm của các mạng học sâu trước đây, nâng $R^2$ từ âm lên $+0.47$.
- Khi bổ sung biến thời gian vận hành $OD$, hệ số xác định $R^2$ tiếp tục tăng lên mức $0.55$.
- Mô hình đạt các chỉ số sai số rất thấp: $RMSE = 3.09\%$, $MAE = 2.76\%$, và $MAPE = 3.11\%$.
- Ngân sách thời gian tối ưu hóa rất tiết kiệm. Quá trình chỉ mất 300 giây nhờ hai thuật toán CFO và BlendSearch.
- Phân tích Bland-Altman xác nhận độ ổn định cao với hầu hết các sai số nằm gọn trong khoảng giới hạn thỏa thuận 95%.

#### Khuyến nghị thực tiễn cho nghiên cứu xử lý nước thải quy mô phòng thí nghiệm và pilot
- Triển khai khung FLAML AutoML làm công cụ tiêu chuẩn cho mô hình hóa các bài toán xử lý nước thải dữ liệu mẫu nhỏ.
- Khuyến nghị đưa biến thời gian vận hành tích lũy ($OD$) vào danh mục biến bắt buộc khi quan trắc bể phản ứng màng.
- Áp dụng khung Ensemble Ranking Score để phân tích độ quan trọng đặc trưng, tránh các sai lệch từ một giải thuật đơn lẻ.
- Tận dụng quy trình nghiên cứu triệt tiêu (Ablation study) tự động của AutoML để chọn lọc tập đặc trưng tối giản và hiệu quả.
- Tái định hướng đầu tư cảm biến: Tập trung vào cảm biến giám sát liên tục $COD\text{-in}$ và kiểm soát lịch bảo trì theo $OD$.

### 4.4 Thông tin bổ trợ và Đóng góp tác giả

#### Đóng góp tác giả theo chuẩn CRediT
- Tác giả Junjie Yu:
  - Soạn thảo bản thảo ban đầu (Writing – original draft).
  - Trực quan hóa dữ liệu và đồ thị (Visualization).
  - Lập trình và thử nghiệm phần mềm (Software).
  - Thực hiện điều tra thực nghiệm (Investigation).
- Tác giả Zhonghua Zheng:
  - Rà soát và biên tập chuyên môn (Writing – review & editing).
  - Cung cấp và điều phối tài nguyên nghiên cứu (Resources).
  - Xây dựng phương pháp luận nghiên cứu (Methodology).
  - Thực hiện điều tra thực nghiệm (Investigation).
- Tác giả Jialing Ni:
  - Rà soát và biên tập bản thảo (Writing – review & editing).
  - Đóng góp tài nguyên nghiên cứu (Resources).
- Tác giả Jiayuan Ji:
  - Định hướng và khởi xướng ý tưởng nghiên cứu (Conceptualization).
  - Phát triển phương pháp luận (Methodology).
  - Quản trị và kiểm tra chất lượng dữ liệu (Data curation).
  - Thu nhận các nguồn tài trợ nghiên cứu (Funding acquisition).
  - Viết bản thảo gốc cùng rà soát biên tập (Writing – original draft, review & editing).
  - Thực hiện điều tra thực nghiệm (Investigation).

#### Tuyên bố xung đột lợi ích, tài trợ nghiên cứu và dữ liệu bổ sung
- Tuyên bố xung đột lợi ích: Nhóm tác giả tuyên bố không có xung đột lợi ích. Không có quan hệ tài chính hoặc cá nhân nào ảnh hưởng đến bài báo.
- Tài trợ từ Quỹ Xúc tiến Khoa học Nhật Bản: Quỹ JSPS KAKENHI tài trợ cho nghiên cứu này theo Mã hợp đồng JP24K17380.
- Tài trợ xây dựng cơ sở dữ liệu: Quỹ JIC Foundation tài trợ một phần việc xây dựng dữ liệu qua Mã số 2022-7.
- Hỗ trợ nguồn lực học thuật: Đại học Manchester cấp quỹ khởi động nghiên cứu cho tác giả Zhonghua Zheng.
- Hỗ trợ biên tập ngôn ngữ: Công ty Editage thực hiện hiệu đính tiếng Anh chuyên môn cho bài viết.
- Dữ liệu bổ trợ trực tuyến (Appendix A): Tài liệu bổ trợ được lưu trữ trực tuyến tại địa chỉ https://doi.org/10.1016/j.jenvman.2026.128801.
- Tính khả dụng của dữ liệu (Data availability): Nhóm nghiên cứu không có quyền chia sẻ công khai bộ dữ liệu gốc. Quy định bảo mật dự án không cho phép công bố dữ liệu này.
