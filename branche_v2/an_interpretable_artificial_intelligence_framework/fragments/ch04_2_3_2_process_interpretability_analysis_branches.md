### 3.2. Process interpretability analysis

#### 3.2.1. Cross-model feature importance consensus and divergence

- Phân tích SHAP (SHapley Additive exPlanations) áp dụng trên toàn bộ 16 mô hình và 3 biến mục tiêu tạo ra 48 hồ sơ tầm quan trọng đặc trưng (feature-importance profiles) (Hình 6A1--3; so sánh giữa TreeSHAP và KernelSHAP tại Hình S8A).
- Kết quả trung tâm thể hiện sự đồng thuận cao (consensus) giữa các mô hình học máy:
  - Bất chấp sự khác biệt trải rộng trên 6 họ thuật toán, toàn bộ 16 trên 16 mô hình đều xếp hạng thời gian lưu bùn (SRT, Sludge Retention Time) ở vị trí thứ nhất đối với áp suất xuyên màng (TMP, Transmembrane Pressure), đạt điểm số nhất quán (consistency score) là $1.00$.
  - 15 trên 16 mô hình xếp hạng SRT ở vị trí thứ nhất đối với mức nước bể màng (water level), với thứ hạng trung bình là $1.07 \pm 0.25$, trong đó mạng nơ-ron đa lớp (MLP, Multi-layer Perceptron) là ngoại lệ duy nhất:
  - **Hình 6.** Bản đồ nhiệt tầm quan trọng đặc trưng SHAP và biểu đồ beeswarm cho 16 mô hình
    - <img src="assets/fig_06_p9.jpeg" alt="Hình 6" />
    - **Hình này chứng minh điều gì**
      - Cột SRT đồng nhất màu đỏ sẫm ($1.0$) trên toàn bộ 16 mô hình cho TMP và 15 mô hình cho mức nước bể màng.
      - Biểu đồ beeswarm thể hiện SRT cao kéo giảm mạnh giá trị SHAP của TMP (đạt $-2.0$), trong khi HRT tối ưu quanh dải trung bình.
    - **Từ đâu mà thấy được**
      - Panel (A1--A3): Trục hoành gồm 7 đặc trưng đầu vào, trục tung gồm 16 mô hình học máy; thang màu biểu thị Normalized importance không thứ nguyên từ $0.0$ (xanh lam) đến $1.0$ (đỏ sẫm).
      - Panel (B1--B3): Trục hoành đo SHAP value (tác động lên đầu ra mô hình, không thứ nguyên), trục tung liệt kê 7 đặc trưng; màu điểm từ xanh lam (giá trị thấp) đến đỏ sẫm (giá trị cao).
  - Đối với lưu lượng nước lọc (permeate flow), mức độ đồng thuận phân tán hơn: thời gian lưu thủy lực (HRT, Hydraulic Retention Time) xếp hạng thứ nhất ở 7 trên 16 mô hình (thứ hạng trung bình $2.28 \pm 1.39$), so với thứ hạng trung bình $4.67 \pm 1.89$ của SRT.
- Sự hội tụ này chứng minh tính chi phối của SRT là thuộc tính nội tại của dữ liệu thực tế thay vì là thiên kiến quy nạp (inductive bias) của một mô hình học máy riêng lẻ:
  - Phân tích đa mô hình giải quyết hạn chế của các nghiên cứu mô hình đơn lẻ vốn không thể phân biệt được nguồn gốc của thuộc tính.
  - Tính đồng thuận này vẫn được bảo toàn dưới các thiết kế kiểm định: SRT duy trì vị trí xếp hạng thứ nhất cho TMP và mức nước bể màng dưới điều kiện kiểm định chặn khối 24 h (blocked $24\ \text{h}$), chặn khối 168 h (blocked $168\ \text{h}$) và huấn luyện theo trình tự thời gian (chronological training), ngay cả khi độ chính xác dự đoán bị suy giảm.
  - Thứ hạng của lưu lượng dòng thấm ngoài hai đặc trưng hàng đầu có độ ổn định thấp hơn và nên xem là mang tính chỉ dẫn tham khảo.
- Sự phân kỳ giữa các mô hình mang tính hệ thống và bắt nguồn trực tiếp từ phương pháp giải thích (explainer):
  - Các mô hình tuyến tính xếp hạng tỷ lệ C/N ở vị trí thứ ba hoặc cao hơn đối với TMP, trong khi toàn bộ các mô hình dạng cây đều xếp C/N ở vị trí cuối cùng.
  - Tốc độ sục khí (aeration rate) xếp hạng thứ nhất đối với lưu lượng dòng thấm khi dùng KernelSHAP, nhưng xếp thứ tư khi dùng TreeSHAP.
  - KernelSHAP xấp xỉ giá trị Shapley thông qua các liên minh đặc trưng ngẫu nhiên nên làm nhập nhằng các đặc trưng có tương quan cao với nhau.
  - TreeSHAP khai thác cấu trúc phân nhánh chính xác của cây quyết định nên đạt độ tin cậy cao hơn khi các biến đầu vào tương quan với nhau.
  - Tốc độ sục khí (Air) và HRT đồng biến thiên trong vận hành thực tế (sục khí cao hơn được triển khai trong giai đoạn tải trọng cao vốn đồng thời nén ngắn HRT), dẫn đến KernelSHAP hấp thụ một phần đóng góp của HRT vào sục khí.
  - Toàn bộ các thảo luận cơ chế vận hành vật lý tiếp theo được xây dựng trên cơ sở các gán quyền quan trọng từ mô hình Extra Trees.

#### 3.2.2. Mechanistic interpretation of the dominant drivers

- Sự chi phối của SRT là phát hiện có khả năng diễn giải vật lý rõ ràng nhất trong toàn bộ phân tích:
  - SRT chi phối thành phần, hình thái và hoạt tính sinh học của quần xã bùn vi sinh.
  - Tại nhà máy này, SRT vận hành trong dải từ $43.3$ đến $108.3$ ngày (days), đặt toàn bộ phạm vi vận hành sâu trong chế độ sục khí kéo dài (extended-aeration regime).
- Dựa trên các biểu đồ phụ thuộc (dependence plot) và biểu đồ beeswarm của Extra Trees (Hình 6B1, Hình S9):
  - Giá trị SHAP mang giá trị dương ở dải $45\text{--}75$ ngày ($45\text{--}75\ \text{days}$).
  - Giá trị SHAP đi qua dải chuyển tiếp phân tán rộng ở $80\text{--}90$ ngày ($80\text{--}90\ \text{days}$), nơi tác động của SRT trở nên phụ thuộc mạnh vào các biến số đồng thời xuất hiện.
  - Giá trị SHAP suy giảm mạnh khi vượt qua $90$ ngày ($90\ \text{days}$), đạt mức $-0.3$ đến $-2.0$ tại khoảng $100\text{--}108$ ngày ($100\text{--}108\ \text{days}$).
- Hiện tượng tăng SRT làm xấu đi TMP thoạt nhìn dường như mâu thuẫn với nhận định truyền thống cho rằng tuổi bùn dài hơn sẽ giảm nghẹt màng thông qua hô hấp nội sinh và thủy phân các chất polymer ngoại bào (EPS, Extracellular Polymeric Substances) cùng các sản phẩm vi sinh vật hòa tan (SMP, Soluble Microbial Products):
  - Nhận định truyền thống nêu trên chỉ được thiết lập trong dải tuổi bùn dưới $30\text{--}40$ ngày ($30\text{--}40\ \text{days}$).
  - Tại cơ sở này, ngay cả mức SRT ngắn nhất cũng đã nằm sâu trong miền sục khí kéo dài, do đó lợi ích giảm thiểu EPS và SMP về cơ bản đã cạn kiệt.
  - Yếu tố biến đổi chủ yếu giữa $45$ và $108$ ngày ($45\ \text{and}\ 108\ \text{days}$) là sinh khối tích tụ: lượng bùn xả thải ít hơn làm nồng độ bùn hoạt tính (MLSS, Mixed Liquor Suspended Solids) tăng cao, đi kèm sự gia tăng độ nhớt bùn, độ dày bánh bùn và độ nén ép của bánh bùn, lấn át hoàn toàn lượng cắt giảm SMP còn sót lại.
  - Ở mức SRT rất dài, bông bùn bị chiếm ưu thế bởi các hạt trơ và khó phân hủy sinh học, tích tụ tạo thành lớp bánh bùn đặc quánh, khó hồi phục bằng cơ chế rửa ngược.
  - Cơ chế này tác động mạnh trong nước thải sản xuất bán dẫn, nơi các phân đoạn khó phân hủy sinh học từ chất cản quang (photoresist) và hóa chất tẩy rửa hấp phụ chọn lọc lên bề mặt màng PVDF.
- Logic cơ chế tương tự giải thích các biến mục tiêu khác:
  - Lưu lượng dòng thấm bị ức chế ở mức SRT dài nhất do độ nhớt bùn làm tăng trở lực thủy lực nội tại.
  - Mức nước bể màng tăng đơn điệu theo SRT.
- Dải chuyển tiếp $80\text{--}90$ ngày ($80\text{--}90\ \text{day}$) là vùng mà các quyết định vận hành quyết định kết quả hệ thống:
  - Tương tác giữa HRT và SRT ($0.056$; Hình S8B1) định lượng mối liên kết kép này.
  - Ở mức HRT ngắn, tổn thất do tăng SRT gây ra bởi sinh khối tích tụ được bù trừ một phần; ngược lại ở mức HRT dài, hai tác động tiêu cực này cộng dồn lên nhau.

#### 3.2.3. Hydraulic and aeration effects

- HRT xếp thứ hai đối với TMP ($2.33 \pm 0.47$) và xếp thứ nhất đối với lưu lượng dòng thấm trong số các mô hình dạng cây hàng đầu:
  - Kết quả này phản ánh vai trò kép của HRT vừa kiểm soát tải trọng hữu cơ vừa kiểm soát công suất thủy lực.
  - HRT ngắn trong dải $6\text{--}7\ \text{h}$ mang lại giá trị SHAP dương cho TMP và mức đóng góp giảm dần đều khi vượt trên $7\ \text{h}$, đạt mức $-1.3$ đến $-2.2$ tại $10\text{--}11\ \text{h}$.
- Kỳ vọng truyền thống thường cho kết quả ngược lại vì HRT ngắn sẽ để lại nhiều SMP dư thừa hơn, nhưng ba đặc điểm vận hành quy mô thực tế dung hòa mâu thuẫn này:
  - HRT ngắn tương ứng với lưu lượng xử lý cao, tại nhà máy này trùng hợp với giai đoạn sản xuất tích cực tạo ra nước thải loãng hơn.
  - Giai đoạn HRT dài trên $9\ \text{h}$ đồng xuất hiện với việc giảm xả bùn và do đó tích tụ nhiều sinh khối hơn.
  - Trong quá trình vận hành thông lượng cao, hệ thống điều khiển duy trì tần suất các chu kỳ rửa ngược (backwash) và nghỉ sục (relaxation) dày hơn.
- Đối với lưu lượng dòng thấm, mối quan hệ phụ thuộc diễn ra phi đơn điệu với điểm tối ưu nằm gần $6.5\text{--}7.5\ \text{h}$ trước khi chạm trần giới hạn thủy lực, theo nguyên lý $\text{HRT} = V/Q$ với thể tích bể $V$ cố định.
- Tốc độ sục khí (aeration rate) xếp thứ hai đối với mức nước bể màng (giá trị $0.216$) và thứ ba đối với lưu lượng dòng thấm, nhưng chỉ xếp thứ sáu đối với TMP (giá trị $0.063$):
  - Sự bất đối xứng này xuất phát từ cơ chế vận hành: sục khí tác động thông qua lực cắt thủy động lực học tại bề mặt màng, kiểm soát trực tiếp các đầu ra thủy lực hơn so với TMP vốn bị chi phối thêm bởi tắc nghẽn nội mao quản và hấp phụ mà lực cắt không thể đánh bật.
  - Đối với TMP, mối quan hệ phụ thuộc mang tính phi đơn điệu: sục khí không đủ dưới khoảng $5000\ \text{m}^3/\text{h}$ làm tắc nghẽn màng diễn ra không kiểm soát, và đáp ứng phân nhánh ở mức trên khoảng $6500\ \text{m}^3/\text{h}$ vì sục khí cao chỉ giảm nghẹt khi lớp bánh bùn còn chịu tác động của lực cắt, nhưng mất hiệu lực khi SRT dài và MLSS cao đã củng cố lớp bánh bùn thành khối đặc chắc.
  - Đối với mức nước bể màng, tương tác mạnh giữa sục khí và SRT ($\text{Air} \times \text{SRT}$ đạt $0.1318$, số hạng ngoài đường chéo lớn nhất trên tất cả các mục tiêu; Hình S8B3) cho thấy lợi ích của sục khí bổ sung được khuếch đại ở SRT thấp và suy giảm ở SRT cao.
- Tốc độ sục khí cũng thể hiện mối liên hệ âm biểu kiến đối với lưu lượng dòng thấm:
  - Đây không phải sự suy giảm cơ học đối với thông lượng màng: trong hệ thống MBR ngập nước vận hành bằng bơm hút, lưu lượng dòng thấm do bơm hút áp đặt.
  - Mối liên hệ âm phản ánh logic điều khiển vận hành: mức sục khí thấp xuất hiện trong giai đoạn tải trọng thấp khi màng chịu ứng suất thủy lực tối thiểu, trong khi sục khí cao được kích hoạt phản ứng trong giai đoạn tải trọng cao hoặc khi màng tắc nghẽn tích cực lúc lưu lượng đã bị hạn chế sẵn.
  - TreeSHAP giải quyết một phần hiện tượng nhiễu này, xếp hạng sục khí ở vị trí thứ tư đối với lưu lượng dòng thấm sau HRT, SRT và C/N, nhưng mối liên hệ dư thừa còn lại được truyền dẫn qua sự đồng biến thiên với HRT và SRT thay vì hiệu ứng thủy động trực tiếp.
  - Đây là ví dụ điển hình minh chứng tại sao biểu đồ phụ thuộc từ dữ liệu nhà máy quan sát chỉ ghi nhận mối liên hệ tương quan chứ không nhất thiết phản ánh cơ chế nhân quả.

#### 3.2.4. Secondary biological drivers

- Nồng độ bùn hoạt tính (MLSS) xếp thứ ba đối với TMP ($3.33 \pm 1.35$) và đối với mức nước bể màng ($3.87 \pm 1.15$):
  - Biểu đồ phụ thuộc TMP có dạng chữ U đảo ngược (inverted-U): đóng góp gần bằng 0 ở mức $2000\text{--}3000\ \text{mg/L}$, đạt cực đại gần $6000\text{--}6500\ \text{mg/L}$, sau đó sụt giảm mạnh xuống $-1.5$ ở mức $7000\text{--}7500\ \text{mg/L}$ do trở lực bánh bùn tăng phi tỷ lệ.
  - Xu hướng này phù hợp với định luật tỷ lệ gần bậc hai (near-quadratic scaling) được ghi nhận cho hệ thống màng sợi rỗng PVDF.
  - Tương tác $\text{MLSS} \times \text{SRT}$ ($0.042$) xác nhận hiệu ứng khuếch đại ở mức SRT ngắn hơn, nơi bùn giàu EPS làm tăng độ nén của bánh bùn.
- Tỷ lệ chất nền trên vi sinh vật (F/M, Food-to-Microorganism ratio) xếp thứ tư đối với TMP:
  - Mức đóng góp đạt cực đại gần $0.030\text{--}0.035\ \text{day}^{-1}$ và suy giảm ở các giá trị cao nhất, nơi sự tăng sinh quá mức SMP đẩy nhanh tốc độ tắc nghẽn lớp gel.
  - Đối với mức nước bể màng, F/M thể hiện dạng đường cong chữ U với mức tăng dốc đứng khi vượt trên $0.05\ \text{day}^{-1}$.
- Tốc độ châm glucose xếp thứ năm đối với TMP, thể hiện tác động khiêm tốn và phần lớn mang tính gián tiếp thông qua biến số MLSS và F/M.
- Tỷ lệ C/N (Carbon-to-Nitrogen ratio) xếp thứ bảy đối với TMP trong các mô hình dạng cây:
  - Giá trị đóng góp giảm đơn điệu từ mức dương ở $5\text{--}7$ xuống mức $-0.3$ ở $14\text{--}16$.
  - Điều kiện giàu cacbon thiếu nitơ thúc đẩy vi sinh vật tổng hợp EPS giàu carbohydrate và tạo điều kiện cho vi khuẩn dạng sợi phát triển làm giảm khả năng lọc.
  - Sự phân kỳ giữa các họ mô hình đối với biến C/N bắt nguồn từ tương quan với MLSS và F/M, minh họa thêm giá trị của việc so sánh đa mô hình.

#### 3.2.5. Interaction structure and methodological implications

- So sánh giữa TreeSHAP trên 9 mô hình dạng cây với KernelSHAP trên 7 mô hình không phải dạng cây bộc lộ độ lệch hướng nhất quán (Hình S8A):
  - Đối với TMP, cả hai phương pháp đều đồng thuận về sự thống trị của SRT (giá trị $0.530$ so với $0.458$) và vị trí thứ hai của HRT ($0.143$), trong đó MLSS phân kỳ nhiều nhất ($0.144$ so với $0.109$).
  - Đối với lưu lượng dòng thấm, sự phân kỳ lớn nhất xuất hiện ở tốc độ sục khí: xếp thứ nhất dưới KernelSHAP ($0.243$) và xếp thứ tư dưới TreeSHAP ($0.150$), đứng sau HRT ($0.318$), C/N ($0.230$) và F/M ($0.160$).
  - Đối với mức nước bể màng, hai phương pháp hoàn toàn đồng thuận.
- Quy luật hệ thống cho thấy KernelSHAP đánh giá quá cao đòn bẩy của các biến ngắn hạn dễ điều chỉnh và làm suy giảm tầm quan trọng của các biến sinh học biến thiên chậm vốn chi phối kết quả, củng cố việc sử dụng TreeSHAP cho hướng dẫn vận hành.
- Ma trận tương tác (Hình S8) xác định các cặp liên kết mạnh nhất:
  - $\text{HRT} \times \text{SRT}$ đối với TMP ($0.056$) và lưu lượng ($0.0510$).
  - $\text{MLSS} \times \text{SRT}$ đối với TMP ($0.042$).
  - $\text{Air} \times \text{SRT}$ đối với mức nước bể màng ($0.1318$).
- Các mối phụ thuộc phi cộng tính này cung cấp cơ sở định lượng để xử lý đồng thời 7 biến đầu vào trong Mục 3.3 thay vì tối ưu hóa đơn lẻ từng biến một.
