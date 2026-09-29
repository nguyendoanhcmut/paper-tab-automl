## 3.2. Phân tích khả năng diễn giải quá trình (Process Interpretability Analysis)

### 3.2.1. Đồng thuận và phân kỳ tầm quan trọng đặc trưng giữa các mô hình (Consensus & Divergence)

#### 3.2.1.1. Đồng thuận tuyệt đối về vai trò của thời gian lưu bùn (SRT)
- Phân tích 48 hồ sơ SHAP: Nghiên cứu áp dụng SHAP cho $16$ mô hình trên $3$ biến mục tiêu (TMP, lưu lượng thấm, mực nước bể màng). Tổng số hồ sơ tầm quan trọng đặc trưng đạt $48$ (Hình 6A1–3).
- Đồng thuận tuyệt đối về TMP: $100\%$ ($16/16$) mô hình trên $6$ họ thuật toán đều xếp thời gian lưu bùn (SRT) ở vị trí số một với điểm số nhất quán tuyệt đối ($1.00$). Tỷ trọng đóng góp SHAP của SRT chiếm trên $40\%\text{--}50\%$ tổng độ quan trọng.
- Đồng thuận về mực nước bể màng: $15/16$ mô hình xếp SRT ở vị trí số một với thứ hạng trung bình đạt $1.07 \pm 0.25$. Mô hình mạng perceptron đa tầng (MLP) là ngoại lệ duy nhất.
- Thứ hạng lưu lượng thấm: Thứ hạng của biến lưu lượng thấm phân tán hơn giữa các thuật toán. Thời gian lưu thủy lực (HRT) đứng đầu ở $7/16$ mô hình với thứ hạng trung bình $2.28 \pm 1.39$. Biến SRT đạt thứ hạng trung bình $4.67 \pm 1.89$.
- Bản chất nội tại của dữ liệu: Sự hội tụ này chứng minh vai trò chi phối của SRT là thuộc tính vật lý của dữ liệu vận hành. Kết quả không phụ thuộc vào thiên kiến quy nạp (inductive bias) của bất kỳ thuật toán riêng lẻ nào.
- Tính vững chắc qua kiểm định: SRT giữ vị trí số một cho TMP và mực nước dưới mọi cấu hình chia dữ liệu. Thứ hạng này bảo toàn trong các thử nghiệm Blocked 24 h, Blocked 168 h và kiểm định theo thời gian. Thứ hạng duy trì ổn định ngay cả khi độ chính xác dự báo suy giảm.

#### 3.2.1.2. Phân kỳ mô hình và nguồn gốc sai lệch phương pháp luận
- Phân kỳ tại các biến thứ cấp: Các mô hình họ cây (Extra Trees, Random Forest, XGBoost) xếp tỷ lệ C/N ở vị trí cuối cùng đối với TMP. Ngược lại, các mô hình tuyến tính xếp C/N ở vị trí thứ ba hoặc cao hơn.
- Phân kỳ về lưu lượng sục khí: Lưu lượng sục khí đứng vị trí số một đối với lưu lượng thấm dưới phương pháp KernelSHAP. Biến này đứng thứ tư dưới phương pháp TreeSHAP.
- Cơ chế sai lệch của KernelSHAP: KernelSHAP ước tính giá trị Shapley qua các liên minh đặc trưng ngẫu nhiên. Phương pháp này phân bổ sai lệch khi các biến đầu vào có hiện tượng đa cộng tuyến.
- Cơ chế chính xác của TreeSHAP: TreeSHAP khai thác cấu trúc phân nhánh cây quyết định và phân bố điều kiện thực tế. Phương pháp này tính toán chính xác khi các biến có tương quan mạnh.
- Hiện tượng đồng biến giữa khí sục và HRT: Lưu lượng khí sục tăng cao trong các chu kỳ tải trọng lớn. Chu kỳ tải cao đồng thời nén ngắn thời gian lưu thủy lực HRT. KernelSHAP gộp một phần đóng góp của HRT vào lưu lượng khí.
- Lựa chọn mô hình chuẩn: Nghiên cứu sử dụng kết quả giải thích của Extra Trees làm chuẩn cho phân tích cơ chế vật lý.

### 3.2.2. Diễn giải cơ chế của các nhân tố chi phối chính (Mechanistic Interpretation)

#### 3.2.2.1. Nghịch lý SRT trong vùng vận hành hiếu khí kéo dài
- Dải vận hành SRT thực tế: Hệ thống MBR xử lý nước thải bán dẫn vận hành trong dải SRT từ $43.3$ đến $108.3\text{ ngày}$. Toàn bộ dải vận hành nằm trong chế độ hiếu khí kéo dài (extended-aeration).
- Phân bố giá trị SHAP của Extra Trees: Giá trị SHAP dương trong khoảng SRT $45\text{--}75\text{ ngày}$ (Hình 6B1, Hình S9). Giá trị SHAP giảm mạnh qua ngưỡng $90\text{ ngày}$. Chỉ số đạt mức $-0.3$ đến $-2.0$ tại dải $100\text{--}108\text{ ngày}$.
- Nghịch lý so với nước thải sinh hoạt: Y văn truyền thống xác định kéo dài SRT dưới $30\text{--}40\text{ ngày}$ giúp giảm tắc nghẽn màng. Cơ chế giảm tắc nhờ hô hấp nội bào tiêu thụ polymer ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP).
- Cạn kiệt lợi thế giảm SMP: Mức SRT thấp nhất tại nhà máy ($43.3\text{ ngày}$) đã vượt xa ngưỡng trên. Lợi ích phân hủy sinh học EPS và SMP đã cạn kiệt hoàn toàn.
- Suy giảm đơn điệu ở dải SRT siêu dài: Khi SRT tăng từ $45$ lên $108\text{ ngày}$, lưu lượng xả bùn giảm. Hiện tượng này làm tích tụ sinh khối và làm tăng nồng độ bùn hoạt tính (MLSS).

#### 3.2.2.2. Cơ chế tích tụ sinh khối và chất rắn trơ bán dẫn đặc thù
- Gia tăng độ nhớt và tính nén của bánh bùn: Lượng bùn xả thấp làm tăng độ nhớt biểu kiến của hỗn dịch bùn. Lớp bánh bùn trên bề mặt màng dày hơn và có độ nén ép cao hơn.
- Áp đảo hiệu ứng hòa tan: Sự gia tăng độ nhớt và trở lực bánh bùn ($R_c$) áp đảo hoàn toàn lượng giảm nhỏ của SMP dư. Hiện tượng này làm áp suất xuyên màng TMP tăng vọt.
- Tích tụ hạt trơ và hóa chất quang khắc: SRT kéo dài giữ lại các hạt mài siêu mịn silica từ nước thải CMP. Bông bùn tích tụ hợp chất khó phân hủy từ chất quang khắc (photoresist) và dung dịch tẩy rửa.
- Hấp phụ chọn lọc lên màng PVDF: Các hợp chất kỵ nước khó phân hủy bám dính lên bề mặt màng sợi rỗng PVDF. Lớp bám tạo thành lớp cặn đặc chắc và khó loại bỏ bằng rửa thủy lực.
- Tác động lên lưu lượng và mực nước: Độ nhớt bùn cao làm tăng lực cản thủy lực nội tại, làm giảm lưu lượng thấm. Đồng thời, mực nước bể màng tăng đơn điệu theo thời gian lưu bùn SRT.

#### 3.2.2.3. Vùng chuyển tiếp tới hạn tại ngưỡng 80–90 ngày
- Vùng chuyển tiếp phân tán rộng: Đồ thị phụ thuộc SHAP ghi nhận dải phân tán rộng trong khoảng SRT từ $80$ đến $90\text{ ngày}$.
- Trạng thái điều kiện hóa: Tại vùng $80\text{--}90\text{ ngày}$, tác động của SRT phụ thuộc mạnh vào các biến vận hành đi kèm. Các quyết định điều khiển vận hành quyết định trạng thái tắc nghẽn màng.
- Tương tác bậc hai HRT $\times$ SRT: Hệ số ghép cặp tương tác giữa HRT và SRT đạt giá trị $0.056$ (Hình S8B1).
- Cơ chế bù trừ tại HRT ngắn: Khi HRT ngắn, thông lượng nước qua bể lớn bù trừ một phần tác động tiêu cực của SRT cao.
- Cơ chế cộng gộp tiêu cực: Khi HRT vượt $9\text{ giờ}$ kết hợp với SRT trên $90\text{ ngày}$, hai yếu tố cộng gộp làm tăng vọt TMP.

### 3.2.3. Tác động của thông số thủy lực và sục khí (Hydraulic & Aeration Effects)

#### 3.2.3.1. Vai trò kiểm soát kép của thời gian lưu thủy lực (HRT)
- Thứ hạng của HRT: HRT đứng thứ hai đối với TMP ($2.33 \pm 0.47$) và đứng đầu đối với lưu lượng thấm trong các mô hình họ cây.
- Vai trò kiểm soát kép: HRT vừa kiểm soát tải trọng hữu cơ thể tích, vừa giới hạn công suất thủy lực của hệ thống.
- Dải tác động của HRT lên TMP: Mức HRT ngắn $6\text{--}7\text{ giờ}$ tạo đóng góp SHAP dương cho TMP. Đóng góp SHAP giảm đều khi HRT vượt $7\text{ giờ}$, đạt mức $-1.3$ đến $-2.2$ tại $10\text{--}11\text{ giờ}$.
- Ba cơ chế thực tế vận hành: Lý thuyết truyền thống cho rằng HRT ngắn để lại nhiều SMP dư gây tắc màng. Ba yếu tố vận hành thực tế tại nhà máy tạo nên kết quả ngược lại:
  1. Pha loãng nước thải: HRT ngắn xảy ra trong giai đoạn sản xuất bán dẫn cao điểm khi nước thải loãng hơn.
  2. Tích tụ sinh khối: Chu kỳ HRT dài trên $9\text{ giờ}$ trùng với giai đoạn giảm xả bùn, gây tích tụ sinh khối.
  3. Tần suất rửa màng: Hệ thống điều khiển tăng tần suất súc rửa ngược và chu kỳ nghỉ khi nhà máy chạy công suất cao.
- Đáp ứng phi đơn điệu của lưu lượng thấm: Lưu lượng thấm đạt cực đại tại khoảng HRT $6.5\text{--}7.5\text{ giờ}$. Khi vượt ngưỡng này, trần thủy lực giới hạn thông lượng tối đa do thể tích bể cố định ($HRT = V/Q$).

#### 3.2.3.2. Cơ chế cắt thủy động lực và hiện tượng bão hòa sục khí
- Thứ hạng của lưu lượng khí sục: Khí sục đứng thứ hai đối với mực nước ($0.216$), thứ ba đối với lưu lượng, nhưng chỉ đứng thứ sáu đối với TMP ($0.063$).
- Cơ chế bất đối xứng: Khí sục tạo lực cắt thủy động lực trên bề mặt màng. Lực cắt chi phối trực tiếp các đại lượng thủy lực dòng chảy và mực nước.
- Giới hạn của lực cắt khí: Ngược lại, TMP còn chịu kiểm soát bởi hiện tượng nghẹt lỗ xốp sâu và hấp phụ hóa học mà lực cắt không thể bóc tách.
- Đáp ứng phi đơn điệu của TMP với khí sục: Khi lưu lượng khí dưới $5000\text{ m}^3\text{/h}$, lực cắt không đủ làm lớp bánh bùn phát triển mất kiểm soát. Tăng khí sục từ $3500$ lên $5000\text{ m}^3\text{/h}$ giúp giảm nhanh TMP.
- Phân nhánh và bão hòa trên $6500\text{ m}^3\text{/h}$: Khi vượt $6500\text{ m}^3\text{/h}$, đáp ứng chia nhánh và hiệu quả chống tắc nghẽn bị bão hòa hoàn toàn.
- Giới hạn vật lý của bánh bùn: Sục khí mạnh chỉ có tác dụng khi bánh bùn còn mềm và xốp. Khi SRT dài và MLSS cao đã nén chặt lớp bánh bùn, khí sục không còn hiệu quả.
- Tác hại của sục khí quá mức: Sục khí quá mức còn làm vỡ bông bùn thành các hạt keo mịn, gây tắc nghẽn sâu trong lỗ màng.
- Tương tác Air $\times$ SRT lên mực nước: Hệ số tương tác đạt $0.1318$ (giá trị ngoài đường chéo lớn nhất trong ma trận SHAP, Hình S8B3). Hiệu quả của sục khí tăng mạnh ở SRT ngắn nhưng suy giảm rõ rệt ở SRT dài.

#### 3.2.3.3. Tương quan nghịch biểu kiến giữa sục khí và lưu lượng thấm
- Tương quan nghịch biểu kiến: Dữ liệu quan sát cho thấy lưu lượng khí sục có tương quan nghịch với lưu lượng thấm.
- Bản chất vận hành thực tế: Đây không phải là sự suy giảm thấm do lực cản vật lý. Trong hệ thống MBR chìm hút cưỡng bức, máy bơm hút quy định trực tiếp thông lượng thấm.
- Tương quan phản ánh logic điều khiển: Người vận hành duy trì khí sục thấp khi tải trọng thấp và màng chịu ít áp lực thủy lực. Họ tăng mạnh khí sục để ứng phó khi tải cao hoặc khi màng tắc nghẽn làm giảm lưu lượng.
- Khả năng phân tách của TreeSHAP: TreeSHAP gỡ bỏ tương quan nhiễu này, xếp khí sục ở vị trí thứ tư sau HRT, SRT và C/N.
- Bản chất dữ liệu quan sát: Hiện tượng này là minh chứng cho việc dữ liệu quan sát ghi nhận mối liên kết thống kê chứ không phải quan hệ nhân quả trực tiếp.

### 3.2.4. Động lực sinh học thứ cấp (Secondary Biological Drivers)

#### 3.2.4.1. Nồng độ bùn hoạt tính MLSS và trở lực bánh bùn
- Thứ hạng của MLSS: MLSS đứng thứ ba đối với TMP ($3.33 \pm 1.35$) và đứng thứ ba đối với mực nước ($3.87 \pm 1.15$).
- Đáp ứng chữ U ngược đối với TMP: Đóng góp SHAP xấp xỉ $0$ tại dải MLSS $2000\text{--}3000\text{ mg/L}$. Giá trị SHAP đạt cực đại tại khoảng $6000\text{--}6500\text{ mg/L}$. Chỉ số rơi mạnh xuống $-1.5$ khi MLSS vượt $7000\text{--}7500\text{ mg/L}$ do trở lực bánh bùn tăng đột biến.
- Quy luật trở lực bánh bùn: Kết quả phù hợp với định luật tăng gần bậc hai của trở lực bánh bùn theo MLSS trên màng PVDF ($R_c \propto \text{MLSS}^2$).
- Tương tác MLSS $\times$ SRT: Hệ số tương tác đạt giá trị $0.042$.
- Tác động khuếch đại ở SRT ngắn: Hiện tượng tắc bùn khuếch đại ở SRT ngắn vì bùn non chứa nhiều EPS làm tăng độ nén của bánh lọc.

#### 3.2.4.2. Tỷ lệ thức ăn trên vi sinh F/M và quá trình tự phân hủy nội bào
- Thứ hạng của F/M: Tỷ lệ F/M đứng thứ tư đối với TMP.
- Vùng tối ưu của F/M đối với TMP: Đóng góp SHAP đạt đỉnh tại dải $0.030\text{--}0.035\text{ ngày}^{-1}$. Giá trị SHAP suy giảm ở mức F/M cao hơn do vi sinh vật sản sinh thừa SMP tạo lớp gel nhầy bám màng.
- Đáp ứng chữ U đối với mực nước: Mực nước bể màng tăng dốc đứng khi F/M vượt ngưỡng $0.05\text{ ngày}^{-1}$.
- Cơ chế tự phân hủy ở F/M thấp: Khi F/M giảm dưới $0.02\text{ ngày}^{-1}$, quần thể vi sinh vật thiếu chất dinh dưỡng. Hiện tượng hô hấp nội bào tự phân giải tế bào phóng thích SMP gây tắc nghẽn lỗ xốp màng nghiêm trọng.

#### 3.2.4.3. Bổ sung Glucose và tỷ lệ C/N trong nước thải bán dẫn
- Thứ hạng và tác động của Glucose: Glucose đứng thứ năm đối với TMP với tác động gián tiếp thông qua MLSS và F/M.
- Nhu cầu châm nguồn carbon: Nước thải bán dẫn giàu nitơ nhưng thiếu hụt carbon hữu cơ cho quá trình khử nitrat sinh học.
- Liều lượng bổ sung Glucose: Châm thiếu glucose làm suy giảm sinh khối vi khuẩn khử nitrat. Châm thừa glucose kích thích vi sinh vật tiết màng nhầy keo tụ polymer ngoại bào (EPS), làm tăng áp suất TMP.
- Thứ hạng của tỷ lệ C/N: C/N đứng thứ bảy đối với TMP trong các mô hình họ cây. Đóng góp SHAP giảm đơn điệu từ giá trị dương ở C/N $5\text{--}7$ xuống $-0.3$ ở dải $14\text{--}16$.
- Cơ chế bất lợi của C/N cao: Môi trường giàu carbon thiếu nitơ kích thích vi sinh vật tiết nhiều polysaccharide trong EPS. Điều kiện này kích thích vi khuẩn dạng sợi phát triển, gây xốp bùn và làm suy giảm khả năng lọc.
- Phân kỳ giữa các họ mô hình: Mô hình tuyến tính xếp C/N ở vị trí thứ ba do hiện tượng đa cộng tuyến với MLSS và F/M. Phân tích đa mô hình giúp nhận diện sai lệch này.

### 3.2.5. Cấu trúc tương tác và hàm ý phương pháp (Interaction Structure & Implications)

#### 3.2.5.1. So sánh độ lệch phương pháp luận giữa TreeSHAP và KernelSHAP
- So sánh chín mô hình họ cây và bảy mô hình phi cây: So sánh phân bổ Shapley cho thấy sai lệch có hệ thống về hướng ước tính giữa TreeSHAP và KernelSHAP (Hình S8A).
- Đồng thuận trên mục tiêu TMP: Cả hai phương pháp cùng xác định SRT chiếm ưu thế tuyệt đối (TreeSHAP đạt $0.530$, KernelSHAP đạt $0.458$). Hai phương pháp cùng xếp HRT ở vị trí thứ hai với giá trị $0.143$. Biến MLSS có độ lệch lớn nhất giữa hai phương pháp ($0.144$ so với $0.109$).
- Phân kỳ lớn trên mục tiêu lưu lượng: KernelSHAP xếp khí sục ở vị trí thứ nhất ($0.243$). TreeSHAP xếp khí sục ở vị trí thứ tư ($0.150$), đứng sau HRT ($0.318$), C/N ($0.230$) và F/M ($0.160$).
- Đồng thuận trên mục tiêu mực nước: Cả hai phương pháp cho kết quả thống nhất cao đối với mực nước bể màng.
- Sai lệch hệ thống của KernelSHAP: KernelSHAP phóng đại vai trò của các biến vận hành ngắn hạn dễ điều chỉnh như khí sục. Đồng thời, KernelSHAP đánh giá thấp các biến sinh học biến thiên chậm nhưng chi phối kết quả như SRT và MLSS.
- Khuyến nghị phương pháp: Các nhà vận hành cần sử dụng TreeSHAP để định hướng kiểm soát và điều khiển quy trình MBR thực tế.

#### 3.2.5.2. Ma trận tương tác bậc hai và yêu cầu tối ưu hóa đa biến
- Cặp tương tác HRT $\times$ SRT: Hệ số ghép nối đạt $0.056$ đối với TMP và đạt $0.0510$ đối với lưu lượng thấm (Hình S8).
- Cặp tương tác MLSS $\times$ SRT: Hệ số ghép nối đạt $0.042$ đối với mục tiêu TMP.
- Cặp tương tác Air $\times$ SRT: Hệ số ghép nối đạt $0.1318$ đối với mục tiêu mực nước bể màng. Đây là giá trị ghép cặp tương tác ngoài đường chéo lớn nhất trong toàn bộ nghiên cứu.
- Bản chất phi cộng gộp: Các mối tương quan phi tuyến chứng minh phương pháp tối ưu hóa đơn biến độc lập sẽ thất bại.
- Yêu cầu kiểm soát đồng thời: Vận hành trạm MBR bắt buộc phải tối ưu hóa đồng thời toàn bộ bảy thông số đầu vào. Phần 3.3 triển khai phương pháp tối ưu hóa đa mục tiêu dựa trên nền tảng tương tác này.
