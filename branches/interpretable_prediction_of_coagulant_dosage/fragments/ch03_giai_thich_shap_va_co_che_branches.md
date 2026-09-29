## 3. Giải thích mô hình bằng phương pháp SHAP và Cơ chế keo tụ

### 3.1 Phân tích tầm quan trọng và chiều hướng tác động của đặc trưng toàn cục

#### 3.1.1 Thứ bậc tầm quan trọng đặc trưng toàn cục (Global Feature Importance)
- Thứ tự xếp hạng tổng thể (Fig 6a): Trục tung biểu diễn các đặc trưng xếp theo thứ tự giảm dần của giá trị SHAP trung bình tuyệt đối ($\text{mean}(|\text{SHAP value}|)$). Thứ bậc từ cao xuống thấp gồm: $\text{EC-RW} > \text{pH-TW} > \text{NH3-N-RW} > \text{CODMn-RW} > \text{T-RW} > \text{NTU-RW} > \text{WTR} > \text{NTU-TW} > \text{pH-RW}$.
- Độ lớn đóng góp dự đoán: Trục hoành biểu thị giá trị SHAP trung bình, phản ánh mức độ ảnh hưởng trung bình của từng đặc trưng lên đầu ra của mô hình. Giá trị SHAP càng lớn chứng tỏ đặc trưng đóng góp càng nhiều vào kết quả dự đoán.
- Nguyên lý vận hành nhà máy nước (DWTP Operational Principle): Mô hình xây dựng dựa trên dữ liệu quan trắc thực tế của nhà máy xử lý nước. Quy trình vận hành tuân thủ nguyên lý liên tục điều chỉnh liều lượng hóa chất theo phẩm chất nước thô để giữ nước sạch ổn định.
- Mối liên hệ nhân quả trực tiếp (Causal Link): Quan hệ giữa liều lượng hóa chất và chất lượng nước sạch mang tính nhân quả trực tiếp. Tuy nhiên, khi liều lượng vượt quá một ngưỡng nhất định, tác động biên của hóa chất lên chất lượng nước sạch hầu như không đáng kể.
- Giá trị kinh nghiệm vận hành thực tiễn: Quan hệ giữa liều lượng hóa chất và chất lượng nước thô phản ánh tri thức thực nghiệm của kỹ sư vận hành. Người vận hành dựa vào kinh nghiệm và phẩm chất nước thô để đặt liều châm đạt chuẩn nước sạch.
- Phân hóa tầm quan trọng giữa nước thô và nước sạch: Nước thô biến động rất mạnh theo mùa và chế độ thủy văn. Ngược lại, chất lượng nước sạch đầu ra luôn duy trì ổn định nghiêm ngặt. Do đó, các chỉ số nước thô đóng vai trò quan trọng hơn các chỉ số nước sạch trong cấu trúc mô hình.

#### 3.1.2 Động lực học chiều hướng tác động đặc trưng (SHAP Summary Analysis)
- Cấu trúc biểu đồ tổng hợp (Fig 6b Summary Plot): Mỗi điểm trên biểu đồ đại diện cho giá trị SHAP của một mẫu dữ liệu. Vị trí trên trục hoành thể hiện độ lớn và hướng tác động của giá trị SHAP.
- Mã màu biểu diễn giá trị gốc: Màu sắc thể hiện giá trị nguyên bản của đặc trưng. Màu đỏ đại diện cho giá trị thực tế cao. Màu xanh đại diện cho giá trị thực tế thấp.
- Nhóm biến thúc đẩy tăng liều châm ($\text{SHAP} > 0$): Các đặc trưng $\text{EC-RW}$, $\text{NH3-N-RW}$, $\text{CODMn-RW}$ và $\text{NTU-RW}$ phân bố điểm đỏ về phía bên phải trục $0$. Giá trị của các biến này càng cao sẽ thúc đẩy tăng liều châm PACl.
- Nhóm biến thúc đẩy giảm liều châm ($\text{SHAP} < 0$): Các đặc trưng $\text{pH-RW}$, $\text{T-RW}$ và $\text{WTR}$ thể hiện xu hướng ngược lại. Điểm đỏ phân bố về phía bên trái trục $0$. Giá trị các biến này càng cao sẽ làm giảm liều lượng chất keo tụ cần châm.
- Bản chất tác động của độ dẫn điện $\text{EC-RW}$: Giá trị $\text{EC-RW}$ cao biểu thị độ tinh khiết của nước thấp. Nguồn nước chứa nồng độ muối hòa tan, chất hữu cơ và ion kim loại cao.
- Cơ chế tác động điện tích của PACl: Cation nhôm trong PACl trung hòa điện tích bề mặt của các hạt lơ lửng và chất keo tích điện âm. Phản ứng này triệt tiêu lực đẩy tĩnh điện giữa các hạt và thúc đẩy quá trình kết tụ keo [50].
- Vai trò của lưu lượng xử lý nước (WTR): Giá trị $\text{WTR}$ cao tương ứng với giá trị SHAP thấp hơn. Điều này chỉ báo xu hướng giảm nhẹ liều lượng hóa chất tính trên một đơn vị thể tích khi trạm vận hành ở công suất cao.

### 3.2 Phân tích phụ thuộc biên và hiệu ứng ngưỡng phi tuyến của từng biến chất lượng nước

#### 3.2.1 Độ dẫn điện nước thô (EC-RW) và cơ chế nén lớp điện kép
- Ý nghĩa vật lý của $\text{EC-RW}$: Độ dẫn điện phản ánh tổng nồng độ các ion chất điện phân hòa tan trong nguồn nước thô tự nhiên.
- Dải tăng cường tuyến tính ($300\text{--}550\ \mu\text{S/cm}$): Trong khoảng từ $300\ \mu\text{S/cm}$ đến $550\ \mu\text{S/cm}$, $\text{EC-RW}$ duy trì mối quan hệ tăng cường gần như tuyến tính với liều lượng keo tụ.
- Hiệu ứng suy giảm biên ngoài khoảng tối ưu: Khi $\text{EC-RW} < 300\ \mu\text{S/cm}$ hoặc $\text{EC-RW} > 550\ \mu\text{S/cm}$, mối quan hệ chuyển sang xu hướng suy giảm biên (diminishing returns).
- Cơ chế nén lớp điện kép (Electric Double Layer Compression): Nồng độ ion chất điện giải cao làm gia tăng lực ion dung dịch. Lực ion cao nén mỏng bề dày lớp điện kép khuếch tán bao quanh các hạt keo, tạo điều kiện cho lực hút Van der Waals kéo các hạt dính kết lại với nhau.
- Tác động ức chế của pH thấp: Độ dẫn điện cao hỗ trợ nén lớp điện kép. Tuy nhiên, giá trị pH thấp sẽ ức chế quá trình hình thành kết tủa $\text{Al(OH)}_3$. Lúc này hệ thống đòi hỏi bổ sung liều châm PACl để bù trừ hiệu năng lắng.

#### 3.2.2 Hàm lượng Amoniac nước thô (NH3-N-RW) và cân bằng ion hóa
- Dạng tồn tại của Amoniac: Nitơ amoniac tồn tại đồng thời ở dạng amoniac tự do ($\text{NH}_3$) và ion amoni ($\text{NH}_4^+$). Tỷ lệ phân bố giữa hai dạng chất này chịu sự chi phối trực tiếp của giá trị pH và nhiệt độ nước.
- Khoảng tác động đồng biến tích cực ($0\text{--}0.2\ \text{mg/L}$): Trong phạm vi từ $0$ đến $0.2\ \text{mg/L}$, $\text{NH3-N-RW}$ tác động thuận chiều rõ rệt lên liều lượng châm PACl.
- Hiệu ứng bão hòa vượt ngưỡng $0.2\ \text{mg/L}$: Khi hàm lượng $\text{NH3-N-RW}$ vượt qua ngưỡng $0.2\ \text{mg/L}$, mối quan hệ đồng biến suy giảm độ dốc và đạt trạng thái bão hòa.
- Tương tác với nhiệt độ nước: Nhiệt độ cao thúc đẩy tốc độ thủy phân của chất keo tụ. Đồng thời, hàm lượng $\text{NH}_3\text{-N}$ thấp giúp giảm thiểu hiện tượng nhiễu cạnh tranh ion, cho phép kỹ sư vận hành điều chỉnh liều châm PACl chính xác theo kinh nghiệm chuyên môn.

#### 3.2.3 Nhu cầu oxy hóa học Permanganat nước thô (CODMn-RW) và cạnh tranh vị trí hoạt hóa
- Ý nghĩa chỉ số $\text{CODMn-RW}$: Chỉ số permanganat phản ánh tổng lượng chất hữu cơ tự nhiên và các hợp chất vô cơ có tính khử hiện diện trong khối nước.
- Vùng trơ dưới ngưỡng ($< 4\ \text{mg/L}$): Khi $\text{CODMn-RW} < 4\ \text{mg/L}$, giá trị SHAP duy trì gần trục $0$ và không xuất hiện tương quan rõ rệt với liều lượng hóa chất.
- Hiệu ứng ngưỡng đột biến trên $4\ \text{mg/L}$: Khi nồng độ $\text{CODMn-RW}$ vượt qua ngưỡng tới hạn $4\ \text{mg/L}$, giá trị SHAP tăng vọt theo chiều thẳng đứng.
- Cơ chế cạnh tranh vị trí hoạt hóa: Các phân tử chất hữu cơ hòa tan cạnh tranh trực tiếp vị trí hoạt hóa liên kết với ion $\text{Al}^{3+}$ và các polyme nhôm của PACl.
- Tiêu hao hóa chất do chất hữu cơ: Sự cạnh tranh vị trí hoạt hóa làm cạn kiệt lượng nhôm hữu hiệu dành cho kết tụ hạt cặn. Người vận hành bắt buộc phải tăng mạnh liều châm PACl để vô hiệu hóa lượng chất hữu cơ dư thừa này.

#### 3.2.4 Độ đục nước thô (NTU-RW) và hiện tượng nghịch đảo độ đục cực thấp
- Xu hướng đồng biến tổng thể: Thông thường, độ đục nước thô có tác động thúc đẩy dương đối với liều châm. Châm thêm lượng chất keo tụ phù hợp sẽ thúc đẩy các hạt cặn liên kết và lắng nhanh, phù hợp với kết quả của Vunain et al. [51].
- Hiện tượng nghịch đảo ở độ đục cực thấp ($\text{NTU-RW} < 2\ \text{NTU}$): Khi $\text{NTU-RW}$ giảm xuống dưới $2\ \text{NTU}$, giá trị SHAP bất ngờ đảo chiều tăng lên.
- Giới hạn khuếch tán và bắt giữ cặn (Diffusion Limitations): Trong điều kiện nước có độ đục cực thấp, các hạt keo phân tán quá thưa thớt trong thể tích nước. Khoảng cách lớn làm hạn chế tần suất va chạm nhiệt và giảm khả năng bắt giữ cặn của các bông hydroxit nhôm sau thủy phân [52-54].
- Bù trừ bằng cơ chế keo tụ quét (Sweep Coagulation): Kỹ sư vận hành bắt buộc phải tăng liều châm PACl để bù đắp các giới hạn khuếch tán và đảm bảo quá trình trung hòa điện tích diễn ra triệt để. Liều châm cao tạo ra mạng lưới kết tủa hydroxit nhôm dày đặc để quét sạch các hạt cặn phân tán.
- Hiện tượng tạo màng bao bọc của chất hữu cơ: Trong nguồn nước có đồng thời $\text{CODMn}$ cao và độ đục cao, các phân tử chất hữu cơ bao bọc xung quanh các hạt keo khoáng. Lớp màng hữu cơ này tạo thành hàng rào cản trở tĩnh điện và không gian. Nhà máy cần bổ sung thêm PACl để tăng cường trung hòa điện tích và phá vỡ lớp vỏ hữu cơ bảo vệ.

#### 3.2.5 Giá trị pH nước thô (pH-RW) và tương tác tĩnh điện trong môi trường kiềm yếu
- Vùng pH kiềm yếu thuận lợi ($8.0\text{--}8.4$): Trong khoảng $\text{pH-RW}$ từ $8.0$ đến $8.4$, liều lượng chất keo tụ yêu cầu giảm dần khi giá trị pH tăng lên.
- Tương tác điện tích trái dấu tối ưu: Môi trường kiềm yếu tạo điều kiện cho các dạng thủy phân mang điện tích dương của PACl tương tác tĩnh điện mạnh mẽ với các hạt tạp chất tích điện âm [55].
- Hiệu năng keo tụ vượt trội: Sự chênh lệch điện tích tối ưu giúp PACl thể hiện các đặc tính keo tụ vượt trội trong môi trường kiềm nhẹ [56]. Lượng hóa chất cần thiết để loại bỏ cặn bẩn giảm xuống mức tối thiểu.

#### 3.2.6 Nhiệt độ nước thô (T-RW) và động học nhiệt - độ nhớt môi trường
- Xu hướng tác động âm của nhiệt độ: Nhiệt độ nước thô thể hiện ảnh hưởng nghịch đảo đối với liều lượng châm PACl. Nước càng lạnh đòi hỏi liều lượng hóa chất châm vào càng lớn.
- Trở lực cơ học do độ nhớt tăng cao: Nhiệt độ nước suy giảm làm tăng độ nhớt động học của môi trường lỏng. Độ nhớt cao cản trở trực tiếp chuyển động nhiệt Brown tự do của các hạt lơ lửng trong nước [57].
- Kìm hãm va chạm và kết tụ bông keo: Chuyển động hạt bị kìm hãm làm giảm xác suất va chạm hiệu dụng giữa các hạt keo, gây bất lợi cho sự ổn định và phát triển của các khối bông cặn.
- Đặc tính thu nhiệt của phản ứng thủy phân: Quá trình thủy phân muối nhôm PACl là phản ứng thu nhiệt ($\Delta H > 0$). Nhiệt độ thấp làm chậm đáng kể tốc độ phản ứng thủy phân và làm chậm quá trình hình thành kết tủa $\text{Al(OH)}_3$.
- Yêu cầu bù trừ liều lượng: Người vận hành bắt buộc phải tăng cường liều châm PACl trong mùa lạnh để bù đắp sự suy giảm động học phản ứng và đạt hiệu quả keo tụ mong muốn [58].

#### 3.2.7 Giá trị pH nước sạch (pH-TW) và phản ứng giải phóng ion H+
- Dải phân bố tập trung hẹp ($7.6\text{--}7.8$): Các giá trị $\text{pH-TW}$ của nước sau xử lý tập trung chủ yếu trong một dải hẹp từ $7.6$ đến $7.8$.
- Tương quan tuyến tính âm rõ rệt: Giữa $\text{pH-TW}$ và lượng chất keo tụ châm vào tồn tại mối tương quan tuyến tính nghịch đảo rất mạnh mẽ.
- Cơ chế giải phóng ion $\text{H}^+$: Phản ứng thủy phân của PACl giải phóng các ion $\text{H}^+$ vào nguồn nước:
  $$\text{Al}^{3+} + 3\text{H}_2\text{O} \rightleftharpoons \text{Al(OH)}_3\downarrow + 3\text{H}^+$$
  Sự gia tăng ion $\text{H}^+$ tự do trung hòa bớt độ kiềm của nước và làm giảm trực tiếp giá trị pH của nước sạch đầu ra [59].

#### 3.2.8 Độ đục nước sạch (NTU-TW) và lưu lượng xử lý nước (WTR)
- Thiếu vắng quan hệ tuyến tính của $\text{NTU-TW}$: Kết quả quan sát không ghi nhận bất kỳ mối liên hệ tuyến tính rõ rệt nào giữa liều châm PACl và độ đục nước sạch $\text{NTU-TW}$. Kết quả này trái ngược với báo cáo trước đây của Chiavola [60].
- Cơ chế kiểm soát vận hành thực tế: Giá trị $\text{NTU-TW}$ chịu tác động đồng thời của chất lượng nước thô và liều châm hóa chất. Khi $\text{NTU-RW}$ tăng cao, người vận hành chủ động tăng liều PACl để giữ $\text{NTU-TW}$ ổn định đạt chuẩn cấp nước.
- Biên độ biến động tối thiểu của nước sạch: Nước sạch xuất xưởng từ nhà máy luôn duy trì độ đục ở mức rất thấp và ổn định với phương sai cực nhỏ. Do đó, $\text{NTU-TW}$ có mức độ ảnh hưởng rất thấp đến việc dự đoán liều lượng.
- Đặc trưng lưu lượng nước xử lý ($\text{WTR}$): Đại lượng $\text{WTR}$ nằm ở vị trí thứ 7 về tầm quan trọng. Giá trị $\text{WTR}$ tăng gắn liền với giá trị SHAP âm nhẹ, phản ánh hiệu ứng tối ưu hóa thủy lực khi lưu lượng nước qua trạm xử lý ổn định ở mức cao.

### 3.3 Cơ chế keo tụ nâng cao và hiện tượng bảo vệ keo (Colloidal Protection)

#### 3.3.1 Trung hòa điện tích và cầu nối hấp phụ của PACl
- Hai cơ chế phản ứng cốt lõi: Hiệu quả xử lý của chất keo tụ Polyaluminum Chloride (PACl) phụ thuộc chủ yếu vào cơ chế trung hòa điện tích (charge neutralization) và cầu nối hấp phụ (adsorption bridging).
- Trung hòa điện tích bề mặt hạt keo: Khi hòa tan vào nước với liều lượng tối ưu, PACl nhanh chóng thủy phân thành các ion polyme nhôm mang điện tích dương cao. Các ion này hấp phụ lên bề mặt các hạt keo mang điện tích âm, đưa điện thế bề mặt về trạng thái trung hòa.
- Cầu nối hấp phụ tạo bông cặn lớn: Các chuỗi polyme nhôm mạch dài hoạt động như những cầu nối hóa lý liên kết các vi hạt keo riêng lẻ lại với nhau. Quá trình tạo cầu nối hình thành nên các khối bông cặn kích thước lớn có trọng lượng riêng cao và dễ dàng lắng đọng.

#### 3.3.2 Hiện tượng bảo vệ keo khi châm thừa hóa chất và suy giảm hiệu suất
- Hiện tượng bảo vệ keo (Colloidal Protection): Việc châm hóa chất PACl vượt quá ngưỡng bão hòa sẽ kích hoạt hiện tượng "bảo vệ keo", làm suy giảm nghiêm trọng hiệu quả xử lý [56, 61, 62].
- Hấp phụ quá mức các ion dương: Lượng ion nhôm hydroxit tích điện dương dư thừa tiếp tục bám dính dày đặc lên bề mặt các hạt keo đã được trung hòa điện tích.
- Hiện tượng đảo dấu điện thế bề mặt: Sự tích tụ ion dương quá mức dẫn đến hiện tượng đảo dấu điện tích bề mặt hạt keo từ âm sang dương ($\zeta > 0$).
- Biến đổi tính chất bề mặt từ kỵ nước thành ưa nước: Các hạt keo vốn có tính kỵ nước (hydrophobic) bị chuyển hóa thành các hạt keo ưa nước (hydrophilic) do lớp vỏ hydrat hóa bao bọc xung quanh.
- Hiện tượng tái ổn định keo (Restabilization): Lực đẩy tĩnh điện dương giữa các hạt keo tái xuất hiện và ngăn cản quá trình kết tụ. Các hạt keo bị tái ổn định và phân tán trở lại vào trong nước, làm giảm khả năng lắng đọng của bông cặn và kéo tụt hiệu quả khử độ đục của bể lắng.

#### 3.3.3 Rủi ro nồng độ nhôm dư hòa tan đối với an toàn cấp nước
- Nguy cơ từ việc châm thừa để chỉnh pH: Việc châm dư hóa chất PACl nhằm hạ thấp pH nước sạch đạt chuẩn sẽ gây hiện tượng tái ổn định keo và làm giảm hiệu suất keo tụ.
- Gia tăng nồng độ nhôm dư hòa tan: Châm hóa chất quá liều làm tăng lượng nhôm hòa tan tồn dư trong nước sau lắng, đe dọa trực tiếp đến tính an toàn và chất lượng nước sạch cung cấp cho người tiêu dùng [54].
- Tác hại của nhôm hòa tan đối với sức khỏe: Hàm lượng ion nhôm vượt ngưỡng cho phép có nguy cơ gây tích tụ sinh học và ảnh hưởng xấu đến hệ thần kinh con người.
- Gia tăng lượng bùn nhôm phát thải: Dư thừa PACl tạo ra lượng bùn hydroxit nhôm lớn. Khối lượng bùn thải tăng cao gây áp lực chi phí cho công tác xử lý và lưu trữ bùn thải nguy hại tại trạm xử lý.

### 3.4 Đánh giá độ tin cậy mô hình AutoML và ưu thế vượt trội của phương pháp SHAP

#### 3.4.1 Kiểm định nguy cơ quá khớp (Overfitting) trong chuỗi TPOT
- Rủi ro lý thuyết của hệ thống AutoML: Hệ thống AutoML (TPOT) có nguy cơ đối mặt với hiện tượng quá khớp (overfitting) trong quá trình tự động tìm kiếm đường ống tối ưu và điều chỉnh siêu tham số.
- Đánh giá thực nghiệm qua hệ số xác định $R^2$: Mặc dù mô hình đạt hệ số xác định hoàn hảo $R^2 = 1.00$ trên tập huấn luyện (training set), kết quả kiểm định chéo lặp lại và kiểm tra trên tập kiểm tra độc lập (testing set) vẫn duy trì giá trị rất cao $R^2 = 0.96$.
- Tính khái quát hóa của mô hình tối ưu: Sự thống nhất cao giữa kết quả kiểm định chéo và tập kiểm tra độc lập khẳng định mô hình TPOT được kiểm soát tốt và không xảy ra hiện tượng quá khớp dữ liệu.

#### 3.4.2 Năng lực bóc tách tương tác phi tuyến và hành vi ngưỡng của Tree SHAP
- Giới hạn của các mô hình tuyến tính cổ điển: Các phương pháp phân tích thống kê tuyến tính truyền thống không thể nắm bắt được các quy luật tác động phi tuyến phức tạp trong quy trình keo tụ.
- Nhận diện chính xác hành vi phản ứng ngưỡng: Phương pháp SHAP đã bóc tách thành công hành vi phản ứng ngưỡng của các thông số then chốt, tiêu biểu là bước nhảy tại mốc $4\ \text{mg/L}$ của $\text{CODMn-RW}$ và ngưỡng $2\ \text{NTU}$ của $\text{NTU-RW}$.
- Nâng cao tính giải thích và độ tin cậy: Tree SHAP vượt qua ranh giới thống kê tuyến tính, cung cấp cơ sở khoa học vững chắc giúp kỹ sư hiểu rõ cơ chế vận hành nội tại của mô hình học máy.

### 3.5 Giải thích cục bộ cho các mẫu thực nghiệm vận hành điển hình (Local Explanations)

#### 3.5.1 Mẫu mùa đông nguồn nước Sông Loan Hà: Điều kiện liều cao cực trị
- Thời điểm thu mẫu và nguồn nước thô: Mẫu thử nghiệm được thu thập vào tháng 2 trong điều kiện mùa đông lạnh giá, với nguồn nước thô khai thác trực tiếp từ Sông Loan Hà (Luanhe River).
- Mức liều châm dự đoán vượt ngưỡng: Mô hình dự đoán mức liều châm PACl lên tới $34.9\ \text{mg/L}$, cao hơn rất nhiều so với giá trị kỳ vọng trung bình của tập kiểm tra ($14.5\ \text{mg/L}$).
- Điều kiện chất lượng nước thô mùa đông:
  + Nhiệt độ nước thô rất thấp: $\text{T-RW} = 3.8\ ^\circ\text{C}$ (gây cản trở động học thủy phân).
  + Nhu cầu oxy hóa học cao vượt ngưỡng: $\text{CODMn-RW} = 5.46\ \text{mg/L}$ (vượt xa ngưỡng tới hạn $4\ \text{mg/L}$).
  + Độ dẫn điện rất cao: $\text{EC-RW} = 600.6\ \mu\text{S/cm}$ (vượt ngưỡng bão hòa $550\ \mu\text{S/cm}$).
  + Hàm lượng amoniac cao: $\text{NH3-N-RW} = 0.36\ \text{mg/L}$ (vượt ngưỡng tác động mạnh $0.2\ \text{mg/L}$).
  + Độ đục nước thô ở mức trung bình: $\text{NTU-RW} = 7.19\ \text{NTU}$.

#### 3.5.2 Phân tích Waterfall Plot và Decision Plot mẫu mùa đông
- Phân tích biểu đồ thác nước (Fig 8a Waterfall Plot): Biểu đồ thể hiện chi tiết quá trình dịch chuyển từ giá trị kỳ vọng cơ sở $E[f(x)] = 14.5\ \text{mg/L}$ lên giá trị dự đoán cuối cùng $f(x) = 34.9\ \text{mg/L}$.
- Tác nhân chi phối hàng đầu $\text{CODMn-RW}$: Nồng độ $\text{CODMn-RW} = 5.46\ \text{mg/L}$ vượt ngưỡng $4\ \text{mg/L}$ tạo ra bước nhảy SHAP dương lớn nhất, đóng vai trò nhân tố chủ chốt kéo tăng mạnh liều lượng dự đoán.
- Đóng góp cộng dồn của các đặc trưng đồng biến: Các biến $\text{EC-RW}$, $\text{NTU-RW}$ và $\text{NH3-N-RW}$ đều duy trì giá trị $\text{SHAP} > 0$, hiệp đồng đẩy mức liều châm lên cao.
- Đóng góp không đáng kể của pH và lưu lượng: Mức độ đóng góp của hai đặc trưng $\text{pH-RW}$ và $\text{WTR}$ đối với mẫu này gần như bằng $0$.
- Phân tích biểu đồ quyết định (Fig 8b Decision Plot): Biểu đồ biểu diễn trực quan quỹ đạo tích lũy của từng đặc trưng vượt qua mức trung bình $14.5\ \text{mg/L}$ để đạt giá trị xuất ra $34.9\ \text{mg/L}$.
- Tính hợp lý theo tri thức chuyên gia: Dựa trên đánh giá tổng thể về chất lượng nước thô khắc nghiệt mùa đông, quyết định tăng vọt liều châm PACl hoàn toàn phù hợp với kinh nghiệm vận hành thực tiễn của nhà máy.

#### 3.5.3 Mẫu mùa hè nguồn nước Sông Dương Tử: Điều kiện liều thấp tối ưu
- Thời điểm thu mẫu và nguồn nước thô: Mẫu thử nghiệm được thu thập vào tháng 5 trong điều kiện mùa hè ấm áp, với nguồn nước thô khai thác từ Sông Dương Tử (Yangtze River).
- Mức liều châm dự đoán dưới trung bình: Mô hình dự đoán mức liều châm PACl chỉ đạt $8.57\ \text{mg/L}$, thấp hơn rõ rệt so với giá trị kỳ vọng trung bình ($14.5\ \text{mg/L}$).
- Điều kiện chất lượng nước thuận lợi mùa hè:
  + Nhiệt độ nước thô ấm áp: $\text{T-RW} = 22.34\ ^\circ\text{C}$ (nhiệt độ thuận lợi cho phản ứng thủy phân).
  + Độ dẫn điện nước thô thấp: $\text{EC-RW} = 290.2\ \mu\text{S/cm}$ (dưới ngưỡng tối thiểu $300\ \mu\text{S/cm}$).
  + Hàm lượng chất hữu cơ rất thấp: $\text{CODMn-RW} = 2.6\ \text{mg/L}$ (thấp hơn nhiều so với ngưỡng phản ứng $4\ \text{mg/L}$).
  + Giá trị pH nước thô kiềm nhẹ: $\text{pH-RW} = 8.15$ (môi trường kiềm tối ưu cho PACl).
  + Giá trị pH nước sạch sau xử lý: $\text{pH-TW} = 7.906$.

#### 3.5.4 Phân tích Waterfall Plot và Decision Plot mẫu mùa hè
- Phân tích biểu đồ thác nước (Fig 8c Waterfall Plot): Biểu đồ minh họa bước dịch chuyển làm sụt giảm liều châm từ giá trị kỳ vọng $14.5\ \text{mg/L}$ xuống mức $8.57\ \text{mg/L}$.
- Vai trò kéo giảm chi phối của $\text{pH-TW}$: Đặc trưng $\text{pH-TW} = 7.906$ tạo ra tác động tiêu cực mạnh nhất lên liều lượng dự đoán. Mức châm PACl thấp sẽ bảo đảm không giải phóng quá nhiều ion $\text{H}^+$, duy trì pH nước sạch ở mức cao.
- Sự đồng thuận kéo giảm liều của các yếu tố nước thô: Các đặc trưng $\text{T-RW} = 22.34\ ^\circ\text{C}$, $\text{EC-RW} = 290.2\ \mu\text{S/cm}$ và $\text{CODMn-RW} = 2.6\ \text{mg/L}$ đều có giá trị SHAP mang dấu âm đồng nhất.
- Đóng góp mờ nhạt của amoniac và lưu lượng: Sự đóng góp của $\text{NH3-N-RW}$ và $\text{WTR}$ vào sai khác dự đoán không đáng kể.
- Phân tích biểu đồ quyết định (Fig 8d Decision Plot): Biểu đồ minh họa chi tiết cách thức các đặc trưng đồng loạt bẻ lái dự đoán dịch chuyển về phía dưới mức trung bình $14.5\ \text{mg/L}$, ấn định kết quả tại $8.57\ \text{mg/L}$.
- Phù hợp kinh nghiệm vận hành thực tiễn: Khi chất lượng nước thô sạch, nhiệt độ ấm và ít chất hữu cơ, quyết định chủ động cắt giảm liều lượng châm PACl xuống dưới mức trung bình là hoàn toàn chính xác và khoa học.

### 3.6 Hàm ý kỹ thuật vận hành và định hướng công nghệ keo tụ bền vững

#### 3.6.1 Hỗ trợ quyết định vận hành chính xác và tiết giảm hóa chất tại DWTP
- Tối ưu hóa kiểm soát liều châm: Mô hình xây dựng trong nghiên cứu này tối ưu hóa việc định lượng hóa chất keo tụ, cho phép châm hóa chất chính xác tại các nhà máy xử lý nước.
- Hạn chế lạm dụng hóa chất: Kiểm soát tự động giúp giảm thiểu đáng kể tình trạng lạm dụng hóa chất quá liều trong quá trình keo tụ cặn bẩn.
- Nâng cao tính minh bạch cho hệ thống: Việc ứng dụng phương pháp giải thích SHAP giúp vạch rõ các yếu tố cốt lõi và quy luật tác động chi phối mức tiêu hao chất keo tụ.
- Hỗ trợ kỹ sư ra quyết định chuẩn xác: Các đồ thị giải thích trực quan giúp nhân viên vận hành nhà máy đưa ra các quyết định điều hành khoa học và hợp lý hơn, vừa tránh châm dư hóa chất vừa bảo đảm chất lượng nước sạch đầu ra.

#### 3.6.2 Tích hợp công nghệ tiền xử lý và chất keo tụ sinh học thân thiện môi trường
- Giảm thiểu tác động môi trường trong thực tế: Để giảm thiểu các tác động tiêu cực đến môi trường do việc sử dụng hóa chất keo tụ, nhà máy cần tiếp tục cải tiến các giải pháp công nghệ bổ trợ.
- Tích hợp các quy trình tiền xử lý: Kết hợp mô hình dự đoán liều lượng với các quy trình tiền xử lý như tiền clo hóa (pre-chlorination) hoặc hấp phụ bằng than hoạt tính để giảm thiểu nhu cầu tiêu thụ chất keo tụ.
- Phát triển chất keo tụ sinh học xanh: Đẩy mạnh nghiên cứu và ứng dụng các chất keo tụ sinh học có nguồn gốc tự nhiên và bền vững (như chitosan, chất tạo bông vi sinh vật).
- Khai thác công nghệ quang xúc tác tiên tiến: Ứng dụng công nghệ quang xúc tác (photocatalytic technologies) [63, 64] để phân hủy chất ô nhiễm hữu cơ trước khi vào bể keo tụ.
- Giảm thiểu phụ thuộc tài nguyên và rủi ro bùn thải: Ứng dụng công nghệ mới giúp giảm sự phụ thuộc vào các nguồn tài nguyên không tái tạo, đồng thời triệt tiêu các rủi ro môi trường do cặn hóa chất và sản phẩm phụ (như bùn hydroxit nhôm) gây ra.
