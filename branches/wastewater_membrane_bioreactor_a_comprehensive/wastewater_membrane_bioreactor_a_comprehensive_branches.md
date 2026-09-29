---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Bể Sinh Học Màng Xử Lý Nước Thải: Đánh Giá Toàn Diện Về Trí Tuệ Nhân Tạo Có Thể Diễn Giải và Bản Sao Số

## CÂY TRI THỨC CHƯƠNG 1 VÀ CHƯƠNG 2: GIỚI THIỆU TỔNG QUAN MBR VÀ PHƯƠNG PHÁP LUẬN NGHIÊN CỨU

## Tóm tắt Tổng quan (Abstract)

### Bối cảnh công nghệ MBR và giá trị thực tiễn
- **Định vị công nghệ**: Bể phản ứng sinh học màng (Wastewater MBR) là giải pháp xử lý nước thải tiên tiến hàng đầu.
- **Chất lượng dòng thấm**: Hệ thống tạo ra nước sau xử lý đạt tiêu chuẩn xả thải khắt khe và tái sử dụng nước an toàn.
- **Phạm vi thương mại**: Công nghệ vận hành rộng khắp ở quy mô đô thị và nhiều ngành công nghiệp trên toàn cầu.

### Hai điểm nghẽn kỹ thuật cố hữu
- **Hiện tượng tắc nghẽn màng (Membrane Fouling)**: Tích tụ chất bẩn hữu cơ, hạt keo và polymer sinh học ngoại bào (EPS) làm suy giảm tính thấm.
- **Tiêu hao năng lượng vận hành cao**: Nhu cầu năng lượng sục khí lớn làm tăng chi phí vòng đời và dấu chân carbon.
- **Độ phức tạp thủy lực - sinh học**: Sự ghép nối giữa phân tách màng và bùn hoạt tính gây khó khăn cho việc kiểm soát quá trình.

### Chuỗi hội tụ ba tầng công nghệ thông minh (ML - XAI - DT)
- **Tầng dự đoán Machine Learning (ML)**: Thuật toán Ensemble, SVM và Deep Learning dự báo chính xác áp suất xuyên màng ($TMP$), lưu lượng thấm qua màng (flux), trở lực lọc và chất lượng nước.
- **Tầng diễn giải Explainable AI (XAI)**: Các kỹ thuật SHAP, LIME và Anchors làm sáng tỏ mô hình hộp đen và xác định đặc trưng chi phối.
- **Tầng tích hợp Digital Twin (DT)**: Bản sao ảo hợp nhất mô hình cơ chế, dữ liệu cảm biến thời gian thực và mô hình học máy để điều khiển tối ưu.

### Rào cản triển khai thực tế và đóng góp cốt lõi
- **Rào cản công nghiệp**: Đa số nghiên cứu dừng ở quy mô phòng thí nghiệm hoặc quy mô pilot.
- **Thiếu hụt dữ liệu chuẩn hóa**: Ngành xử lý nước thiếu các bộ dữ liệu đo kiểm công khai và đồng nhất.
- **Rủi ro vận hành**: Hiện tượng trôi dạt dữ liệu (data drift) và độ bất định chưa được định lượng đầy đủ trong các thuật toán.
- **Đóng góp của tổng quan**: Nghiên cứu tổng hợp có hệ thống mối liên kết giữa ba trụ cột ML, XAI và DT trong quản lý MBR thông minh.

---

## Chương 1: Giới thiệu Tổng quan MBR và Chuỗi Hội tụ ML-XAI-DT

### 1.1 Bối cảnh phát triển và Ưu thế công nghệ của MBR

#### Quy mô thương mại và xu hướng ứng dụng toàn cầu
- **Động lực phát triển**: Tình trạng khan hiếm nguồn nước ngọt và các tiêu chuẩn xả thải nghiêm ngặt thúc đẩy triển khai MBR toàn cầu.
- **Số lượng trạm vận hành**: Hơn 5.000 công trình xử lý nước thải sử dụng công nghệ MBR trên khắp các châu lục.
- **Dải công suất xử lý**: Hệ sinh thái thiết bị trải dài từ các trạm phân tán quy mô nhỏ ($10\text{ m}^3/\text{ngày}$) đến các trạm đô thị lớn ($>100.000\text{ m}^3/\text{ngày}$).
- **Lĩnh vực công nghiệp tiêu biểu**: Chế biến thực phẩm và đồ uống, dược phẩm, dệt nhuộm và lọc hóa dầu.
- **Khả năng thích ứng**: MBR xử lý hiệu quả nước thải công nghiệp nồng độ cao và phức tạp, vượt qua các giới hạn của công nghệ truyền thống.

#### Cơ chế ghép nối và ưu thế so với bùn hoạt tính truyền thống (CAS)
- **Cấu hình tích hợp**: Hệ thống ghép nối trực tiếp bùn vi sinh hoạt tính với quá trình phân tách màng áp lực.
- **Dạng module màng**: Sử dụng màng siêu lọc (UF) hoặc vi lọc (MF) dạng sợi rỗng (hollow-fiber) hoặc tấm phẳng (flat-sheet) đặt chìm trong bể hiếu khí.
- **Loại bỏ bể lắng thứ cấp**: Màng lọc thay thế hoàn toàn bể lắng trọng lực thứ cấp trong quy trình CAS.
- **Tiết kiệm mặt bằng xây dựng**: Tiết diện mặt bằng giảm từ 50% đến 70% so với trạm CAS có cùng công suất.
- **Tách biệt HRT và SRT**: Hệ thống cho phép duy trì thời gian lưu bùn ($SRT$) dài mà không bị ràng buộc bởi thời gian lưu nước ($HRT$).
- **Mật độ sinh khối cao**: Nồng độ chất rắn lơ lửng hỗn hợp bùn lỏng ($MLSS$) vận hành thường đạt từ $8.000\text{ mg/L}$ đến $15.000\text{ mg/L}$.

#### Chất lượng dòng thấm và tiềm năng tái sử dụng nước
- **Loại bỏ chất rắn lơ lửng**: Hiệu suất giữ lại toàn bộ hạt lơ lửng và vi khuẩn đạt mức gần 100%.
- **Chất lượng nước đầu ra cao**: Nước sau lọc có độ đục cực thấp, không chứa vi sinh vật gây bệnh, giảm đáng kể COD và chất dinh dưỡng ($N, P$).
- **Mục tiêu tái sử dụng**: Dòng thấm đáp ứng trực tiếp các tiêu chuẩn tái sử dụng phi sinh hoạt: cấp nước làm mát công nghiệp, tưới tiêu nông nghiệp và nạp lại tầng chứa nước.
- **Khả năng xử lý chất ô nhiễm mới nổi**: Quá trình lưu bùn dài hỗ trợ phân hủy sinh học các hợp chất vi ô nhiễm hữu cơ khó phân hủy.

---

### 1.2 Hai điểm nghẽn cố hữu trong vận hành MBR

#### Điểm nghẽn 1: Hiện tượng tắc nghẽn màng (Membrane Fouling)
- **Định nghĩa hiện tượng**: Tắc nghẽn màng là sự tích tụ liên tục của các chất bẩn lên bề mặt màng và bám vào bên trong cấu trúc lỗ rỗng.
- **Các thành phần gây nghẽn**:
  - Hợp chất hữu cơ hòa tan và chất keo vô cơ.
  - Các chất polymer sinh học ngoại bào của vi sinh vật ($EPS$).
  - Các sản phẩm vi sinh vật hòa tan ($SMP$).
- **Hệ quả thủy lực trực tiếp**:
  - Lưu lượng thấm qua màng ($J$) suy giảm nhanh chóng ở chế độ vận hành áp suất cố định.
  - Áp suất xuyên màng ($TMP$) tăng vọt khi duy trì lưu lượng lọc không đổi theo phương trình Darcy:
    $$TMP = J \cdot \mu \cdot R_t$$
    Trong đó $J$ là lưu lượng dòng thấm, $\mu$ là độ nhớt động học của nước lọc, và $R_t$ là tổng trở lực lọc của màng.
- **Cơ chế gia tăng trở lực lọc**:
  - Tổng trở lực lọc gồm nhiều thành phần nối tiếp:
    $$R_t = R_m + R_p + R_c$$
    Trong đó $R_m$ là trở lực nội tại của màng sạch, $R_p$ là trở lực bít tắc lỗ rỗng (pore blocking), và $R_c$ là trở lực của lớp bánh bùn (cake layer).
- **Hệ quả kinh tế và tuổi thọ**:
  - Tăng tần suất sục rửa khí ngược và rửa hóa chất phục hồi (CIP).
  - Hóa chất làm thoái hóa bề mặt polymer của màng, rút ngắn tuổi thọ và buộc phải thay màng sớm.
  - Tắc nghẽn màng chiếm tỷ trọng cao nhất trong tổng chi phí vòng đời dự án (LCC).
- **Tính phi tuyến và nhạy cảm**: Hiện tượng tắc nghẽn biến đổi phức tạp theo $MLSS$, nhiệt độ, $SRT$, tính chất nước thải và điều kiện thủy lực bể lọc.

#### Điểm nghẽn 2: Tiêu hao năng lượng vận hành cao (Elevated Energy Demand)
- **Cường độ tiêu thụ năng lượng đặc thù ($SEC$)**:
  - MBR tiêu tốn từ $0.4\text{ đến }1.5\text{ kWh/m}^3$ nước thải xử lý.
  - Mức tiêu hao năng lượng cao gấp hai lần so với công nghệ bùn hoạt tính truyền thống ($0.25 - 0.6\text{ kWh/m}^3$).
- **Cơ cấu tiêu thụ năng lượng của trạm MBR**:
  - Năng lượng sục khí làm sạch bề mặt màng (membrane air scouring): Chiếm từ $60\%\text{ đến }75\%$ tổng lượng điện tiêu thụ.
  - Năng lượng sục khí cấp oxy sinh học cho bể hiếu khí: Chiếm khoảng $15\%\text{ đến }20\%$.
  - Năng lượng bơm dòng thấm, bơm tuần hoàn bùn và bơm xả thải: Chiếm khoảng $10\%\text{ đến }15\%$.
- **Hệ quả môi trường và chi phí**:
  - Chi phí điện năng chiếm phần lớn chi phí vận hành trực tiếp ($OPEX$).
  - Nhu cầu điện năng lớn làm tăng lượng phát thải khí nhà kính gián tiếp, làm giảm lợi ích sinh thái của giải pháp tái sử dụng nước.

---

### 1.3 Tiềm năng Học máy và Rào cản mô hình hộp đen

#### Tiềm năng mô hình hóa phi tuyến của Machine Learning
- **Học trực tiếp từ dữ liệu**: ML trích xuất các mối quan hệ phi tuyến phức tạp giữa biến vận hành và đầu ra của hệ thống mà không cần giả định trước.
- **Khắc phục hạn chế của mô hình vật lý**: Các mô hình cơ chế (như ASM và lý thuyết bít lỗ rỗng) đòi hỏi xác định nhiều thông số động học phức tạp, khó áp dụng trực tiếp tại hiện trường.
- **Các thuật toán phổ biến trong MBR**:
  - Support Vector Machines ($SVM$) và Support Vector Regression ($SVR$).
  - Random Forest ($RF$) và Extreme Gradient Boosting ($XGBoost$).
  - Mạng nơ-ron hồi quy sâu ($RNN$), Long Short-Term Memory ($LSTM$), Gated Recurrent Unit ($GRU$).
- **Độ chính xác dự báo vượt trội**: ML đạt chỉ số tương quan $R^2$ cao và sai số dự báo $RMSE$ thấp hơn đáng kể so với mô hình hồi quy tuyến tính trong bài toán dự báo $TMP$ và flux.

#### Rào cản mô hình hộp đen (Black-box Barrier)
- **Thiếu tính minh bạch toán học**: Các cấu trúc nơ-ron nhiều tầng và mô hình tập hợp cây không giải trình được cơ chế biến đổi bên trong.
- **Rủi ro quyết định thảm họa**: Mô hình thuần dữ liệu có thể đưa ra các dự báo sai lệch nghiêm trọng khi gặp dữ liệu ngoại lai hoặc các sự cố thủy lực bất thường.
- **Kháng cự từ kỹ sư vận hành**: Người vận hành từ chối áp dụng các đề xuất điều khiển tự động nếu không hiểu rõ căn cứ kỹ thuật.
- **Rào cản quy chuẩn và pháp lý**: Cơ quan quản lý hạ tầng nước yêu cầu mọi thuật toán điều khiển tự động phải có khả năng kiểm toán và giải trình rõ ràng.

#### Vai trò của Trí tuệ Nhân tạo có Thể Giải thích (XAI)
- **Bóc tách quyết định của mô hình**: XAI lượng hóa mức độ đóng góp của từng biến đầu vào vào giá trị đầu ra dự báo.
- **Các công cụ XAI then chốt**:
  - SHAP (Shapley Additive exPlanations): Phân bổ giá trị đóng góp công bằng dựa trên lý thuyết trò chơi hợp tác.
  - LIME (Local Interpretable Model-agnostic Explanations): Xấp xỉ cục bộ hành vi mô hình phức tạp bằng mô hình tuyến tính đơn giản.
  - Anchors và PDP (Partial Dependence Plots): Xác định ngưỡng ràng buộc quy tắc và trực quan hóa xu hướng ảnh hưởng của biến.
- **Hợp thức hóa tri thức chuyên ngành**: Kỹ sư đối chiếu xếp hạng đóng góp đặc trưng của XAI với các quy luật sinh hóa và thủy lực màng để xác thực mô hình.

---

### 1.4 Chuỗi hội tụ ba tầng: Machine Learning - Explainable AI - Digital Twin

```
+-------------------------------------------------------------------------------+
|                      TẦNG 3: DIGITAL TWIN (VẬN HÀNH VÀ ĐIỀU KHIỂN)             |
|   - Bản sao số phản chiếu hai chiều thời gian thực với hệ thống vật lý        |
|   - Tích hợp mô hình cơ chế sinh học (ASM), mô hình màng và cảm biến SCADA   |
|   - Mô phỏng kịch bản, tối ưu hóa năng lượng sục khí và điều khiển đóng vòng  |
+---------------------------------------^---------------------------------------+
                                        |  Tích hợp ra quyết định
+---------------------------------------+---------------------------------------+
|                      TẦNG 2: EXPLAINABLE AI (MINH BẠCH VÀ GIẢI TRÌNH)         |
|   - Lượng hóa tầm quan trọng đặc trưng: SHAP values, LIME local weights       |
|   - Kiểm tra tính nhất quán với quy luật vật lý: Phát hiện tương quan giả     |
|   - Cung cấp giải trình tin cậy cho kỹ sư vận hành và cơ quan thẩm quyền      |
+---------------------------------------^---------------------------------------+
                                        |  Giải trình mô hình
+---------------------------------------+---------------------------------------+
|                      TẦNG 1: MACHINE LEARNING (DỰ BÁO VÀ HỌC TẬP DỮ LIỆU)     |
|   - Thuật toán cốt lõi: SVR, Random Forest, XGBoost, LSTM, Mạng nơ-ron sâu    |
|   - Biến dự báo: Tốc độ tăng TMP ($dTMP/dt$), suy giảm Flux, BOD/COD/N/P      |
|   - Học mối quan hệ phi tuyến động học từ chuỗi thời gian vận hành            |
+-------------------------------------------------------------------------------+
```

#### Tầng 1: Động cơ dự đoán Machine Learning (ML Predictive Engine)
- **Nhiệm vụ cốt lõi**: Khai phá dữ liệu lịch sử để dự báo động thái của hệ thống MBR.
- **Mục tiêu dự báo trọng tâm**:
  - Dự báo tốc độ nhảy vọt áp suất xuyên màng ($dTMP/dt$).
  - Dự báo suy giảm lưu lượng thấm qua màng dưới các chu kỳ sục khí khác nhau.
  - Dự báo nồng độ chất ô nhiễm đầu ra ($COD, NH_4^+-N, NO_3^--N, TN, TP$).
- **Hạn chế nếu đứng độc lập**: Thiếu độ tin cậy để điều khiển trực tiếp các van và máy thổi khí công nghiệp.

#### Tầng 2: Lớp diễn giải Explainable AI (XAI Interpretability Layer)
- **Nhiệm vụ cốt lõi**: Tạo lớp lọc minh bạch bao bọc lấy động cơ ML.
- **Chức năng định lượng**:
  - Tính toán giá trị SHAP cục bộ cho từng mẻ vận hành.
  - Xác định biến số nào đang gây ra hiện tượng tăng $TMP$ đột ngột (ví dụ: nhiệt độ dịch bùn giảm hay nồng độ $EPS$ tăng vọt).
- **Phát hiện tương quan giả (Spurious Correlations)**: Loại bỏ các mô hình học máy đưa ra dự báo đúng dựa trên dữ liệu nhiễu hoặc tương quan ngẫu nhiên.
- **Cầu nối người - máy**: Giúp kỹ sư tin tưởng phê duyệt các kế hoạch điều chỉnh thông số công nghệ.

#### Tầng 3: Tầng tích hợp vận hành Digital Twin (DT Operational Integration Layer)
- **Nhiệm vụ cốt lõi**: Tạo bản sao ảo thời gian thực của trạm MBR vật lý.
- **Ghép nối hai chiều (Bidirectional Coupling)**:
  - Nhận dữ liệu quan trắc liên tục từ hệ thống SCADA/IoT (lưu lượng, áp suất, DO, pH, MLSS).
  - Truyền tín hiệu điều khiển tối ưu ngược lại hệ thống phần cứng trạm xử lý.
- **Cấu trúc tích hợp lai (Hybrid Modeling Architecture)**:
  - Kết hợp mô hình cơ chế phản ánh quá trình bùn hoạt tính (Activated Sludge Models - ASM1, ASM2d).
  - Kết hợp mô hình cơ học dòng thấm màng (CFD và định luật Darcy).
  - Tích hợp các bộ dự đoán ML tốc độ cao để dự báo tương lai ngắn.
  - Tích hợp module giải thích XAI để hiển thị nguyên nhân trên giao diện vận hành HMI.
- **Mô phỏng kịch bản không rủi ro (What-if Simulation)**: Kiểm tra tác động của việc giảm 20% lưu lượng khí sục màng trước khi ra lệnh cho thiết bị chấp hành.

#### Tính phụ thuộc tuần tự giữa ba tầng
- Tầng ML cung cấp năng lực dự báo cho Tầng DT.
- Thiếu XAI, Tầng ML tạo ra rủi ro mất an toàn vận hành.
- Thiếu DT, Tầng XAI chỉ dừng lại ở các phân tích ngoại tuyến vô thưởng vô phạt.
- Sự kết hợp đồng thời cả ba thành phần là điều kiện tiên quyết để vận hành tự chủ trạm MBR.

---

### 1.5 Mục tiêu bài tổng quan và Khung khái niệm tích hợp

#### Bốn mục tiêu cốt lõi của bài viết
- **Mục tiêu 1**: Đánh giá phản biện hiệu năng dự đoán, hạn chế tập dữ liệu và khả năng tổng quát hóa của các mô hình ML đối với hiện tượng tắc nghẽn màng, nhu cầu năng lượng và chất lượng nước MBR.
- **Mục tiêu 2**: Phân tích sâu các kỹ thuật XAI trong việc diễn giải mô hình, loại bỏ thiên lệch dữ liệu và xây dựng quyết định minh bạch cho người vận hành.
- **Mục tiêu 3**: Định hình kiến trúc Digital Twin hoàn chỉnh cho MBR, đánh giá mức độ sẵn sàng công nghệ (TRL) và yêu cầu tích hợp module XAI vào nền tảng DT.
- **Mục tiêu 4**: Nhận diện các khoảng trống tri thức then chốt và đề xuất lộ trình chuyển giao công nghệ từ phòng thí nghiệm sang quy mô công nghiệp.

#### Khung khái niệm tích hợp (Kiến trúc Hình 1)
- **Nhóm thách thức vận hành**: Tắc nghẽn màng phức tạp, chi phí năng lượng sục khí cao, yêu cầu nước đầu ra khắt khe.
- **Nhóm công cụ phương pháp luận**: Máy học giám sát/không giám sát, phương pháp diễn giải hậu nghiệm (Post-hoc XAI), kiến trúc mạng số DT hai chiều.
- **Nhóm ứng dụng mục tiêu**: Tối ưu hóa chu kỳ rửa ngược, điều khiển sục khí thích ứng, cảnh báo sớm suy thoái màng, hỗ trợ vận hành trực tuyến.
- **Nhóm rào cản kỹ thuật cần giải quyết**: Thiếu dữ liệu quy mô trạm thực, độ bất định của cảm biến, hiện tượng trôi dạt mô hình sinh hóa.

---

## Chương 2: Phương pháp luận Nghiên cứu và Thu thập Dữ liệu

### 2.1 Chiến lược tìm kiếm và Cơ sở dữ liệu

#### Các cơ sở dữ liệu học thuật quốc tế
- **Cơ sở dữ liệu khai thác chính**:
  - Scopus (Elsevier).
  - Web of Science (Clarivate Analytics).
  - PubMed (National Institutes of Health).
- **Nguồn bổ sung đối chuẩn**: Các nghiên cứu chuyên sâu về cảm biến thông minh và thuật toán trên IEEE Xplore.

#### Khung thời gian rà soát
- **Khoảng thời gian**: Từ tháng 01 năm 2010 đến tháng 12 năm 2025 (chu kỳ 16 năm).
- **Lý do lựa chọn**:
  - Giai đoạn này chứng kiến sự bùng nổ thương mại hóa công nghệ MBR trên toàn cầu.
  - Giai đoạn này đánh dấu bước phát triển vượt bậc của khoa học dữ liệu và AI trong lĩnh vực kỹ thuật môi trường.

#### Chuỗi từ khóa tìm kiếm Boolean
- **Cấu trúc truy vấn tiêu chuẩn**:
  ```text
  ("membrane bioreactor" OR "MBR") 
  AND 
  ("machine learning" OR "artificial neural network" OR "deep learning" OR 
   "LSTM" OR "random forest" OR "support vector machine" OR 
   "explainable AI" OR "XAI" OR "SHAP" OR "LIME" OR "digital twin")
  ```
- **Phạm vi tài liệu**: Giới hạn ở các bài báo khoa học xuất bản trên các tạp chí quốc tế có bình duyệt độc lập bằng tiếng Anh.
- **Kỹ thuật rà soát bổ sung**: Rà soát thủ công danh mục tài liệu tham khảo (backward snowballing) để tránh bỏ sót các công trình bản lề.

---

### 2.2 Tiêu chí chọn lọc và Đánh giá chất lượng thực nghiệm

#### Tiêu chí lựa chọn đưa vào nghiên cứu (Inclusion Criteria)
- **Nội dung chuyên môn**: Nghiên cứu ứng dụng trực tiếp thuật toán ML, công cụ XAI hoặc nền tảng Digital Twin vào hệ thống MBR xử lý nước thải.
- **Tính nguyên bản**: Công trình công bố mô hình gốc, thuật toán cải tiến hoặc số liệu thực nghiệm đo đạc thực tế.
- **Định lượng hiệu năng**: Bài báo bắt buộc phải cung cấp đầy đủ các chỉ số đo lường hiệu suất thống kê chuẩn mực:
  - Hệ số xác định ($R^2$).
  - Sai số căn bậc hai trung bình ($RMSE$).
  - Sai số tuyệt đối trung bình ($MAE$).
  - Sai số phần trăm tuyệt đối trung bình ($MAPE$).

#### Tiêu chí loại trừ nghiên cứu (Exclusion Criteria)
- **Nghiên cứu thiếu định lượng**: Các bài viết mang tính định tính, báo cáo hội nghị ngắn hoặc không công bố chỉ số hiệu năng cụ thể.
- **Nghiên cứu thuần vật liệu**: Các công trình chỉ nghiên cứu hóa học chế tạo màng, biến tính bề mặt màng hoặc vật liệu nano mà không gắn với mô hình hóa vận hành hệ thống.
- **Trùng lặp nội dung**: Các bài viết tổng quan đơn thuần không có phân tích mô hình hóa chuyên sâu.

#### Bản chất phương pháp luận và Quản lý dữ liệu sơ cấp
- **Đặc trưng bài tổng quan**: Đây là nghiên cứu tổng quan tường thuật có phản biện sâu sắc (Critical Narrative Review).
- **Phân định phạm vi**: Bài viết không tiến hành phân tích gộp (meta-analysis) và không vẽ sơ đồ dòng PRISMA. Trọng tâm bài báo tập trung phân tích logic kỹ thuật, cơ chế liên kết và đánh giá phản biện công nghệ.
- **Bảng dữ liệu bổ sung chuẩn hóa (Supplementary Table S1)**:
  - Thu thập toàn diện dữ liệu cấp nghiên cứu của các bài báo sơ cấp.
  - Phân loại biến mục tiêu dự báo ($TMP$, flux, $COD$, nồng độ bùn).
  - Ghi nhận dải giá trị vận hành và đơn vị đo lường.
  - Đối chiếu phương pháp kiểm chứng chéo độc lập ngoài (External Validation) nhằm kiểm soát nguy cơ sai lệch dữ liệu.

## Chương 3 (Phần 1): Cơ chế Tắc nghẽn Màng (3.1) và Các Mô hình Học máy Cơ bản / Dựa trên Hạt nhân (3.2)

### 3.1 Cơ chế Tắc nghẽn Màng và Bối cảnh Mô hình hóa Cơ chế

#### 3.1.1 Phân loại Tắc nghẽn Màng và Động học Tăng Áp suất Qua Màng (TMP)
- Bản chất vật lý của tắc nghẽn màng trong MBR:
  - Hiện tượng tích tụ chất rắn, polyme sinh học và hạt keo lên bề mặt màng hoặc bên trong lỗ rỗng mao quản.
  - Quá trình này làm suy giảm lưu lượng thấm nước và làm tăng áp suất qua màng (Transmembrane Pressure - TMP).
  - Tắc nghẽn màng diễn ra trên nhiều quy mô không gian và thời gian.
- Phân loại ba hình thái tắc nghẽn theo khả năng phục hồi kỹ thuật:
  - Tắc nghẽn có thể đảo ngược (Reversible fouling):
    - Tích tụ lớp bánh cặn (cake layer) lỏng lẻo bám trên bề mặt ngoài của màng lọc.
    - Người vận hành loại bỏ dễ dàng bằng các biện pháp vật lý thông thường.
    - Biện pháp xử lý gồm chu kỳ tạm dừng hút (relaxation) và sục rửa ngược định kỳ (backwashing).
  - Tắc nghẽn không thể đảo ngược (Irreversible fouling):
    - Chất bẩn bít tắc sâu vào lòng lỗ rỗng mao quản màng (pore blocking).
    - Polyme sinh học hấp phụ mạnh lên thành lỗ xốp của màng mỏng.
    - Rửa cơ học thông thường không thể loại bỏ trở lực này.
    - Trạm bắt buộc phải ngâm rửa bằng hóa chất chuyên dụng tại chỗ (Clean-In-Place - CIP) bằng dung dịch axit, kiềm hoặc chất oxy hóa.
  - Tắc nghẽn vĩnh viễn (Irrecoverable fouling):
    - Hiện tượng suy giảm tính thấm tích lũy sau nhiều năm vận hành liên tục.
    - Ngay cả quy trình rửa hóa chất nồng độ cao cũng không thể phục hồi độ thấm.
    - Nguyên nhân cốt lõi do lão hóa vật liệu polyme màng hoặc khoáng hóa không hòa tan ăn sâu vào cấu trúc màng.
    - Trạm phải loại bỏ và thay thế mô-đun màng mới.
- Động học tăng TMP hai giai đoạn (Two-stage TMP rise kinetics):
  - Ngưỡng lưu lượng thấm tới hạn (Critical Flux - $J_c$):
    - Khi lưu lượng vận hành thấp hơn $J_c$ ($J < J_c$), cặn tích tụ chậm và phần lớn có thể đảo ngược. Lực cắt bọt khí lấn át lực kéo đối lưu.
    - Khi lưu lượng vận hành vượt quá $J_c$ ($J > J_c$), tắc nghẽn không thể đảo ngược bùng phát dữ dội. Hiện tượng này rút ngắn chu kỳ làm sạch và tuổi thọ màng.
  - Giai đoạn 1 (Tăng TMP chậm và ổn định):
    - Diễn ra trong thời gian dài từ vài chục đến hàng trăm giờ lọc liên tục.
    - Polyme sinh học hòa tan và hạt keo hấp phụ từ từ vào vách lỗ màng.
    - Lớp bánh cặn mỏng ban đầu hình thành trên bề mặt.
    - Tốc độ tăng áp suất duy trì ở mức rất thấp: $\frac{d(TMP)}{dt} \approx \text{const} \ll 1\text{ kPa/h}$.
  - Giai đoạn 2 (Tăng vọt đột biến áp suất - TMP jump):
    - Khi các lỗ rỗng mao quản bị bít kín cục bộ, lưu lượng thấm cục bộ tại các vị trí màng còn lại tăng vượt ngưỡng tới hạn $J_c$.
    - Lớp bánh cặn bị nén ép cơ học dữ dội dưới gradient áp suất cao.
    - Độ rỗng của lớp bánh cặn giảm mạnh, đẩy trở lực thủy lực tăng phi tuyến.
    - Đồ thị TMP tăng vọt theo phương thẳng đứng. Áp suất nhanh chóng chạm ngưỡng bảo vệ quá áp của bơm hút, buộc trạm phải dừng lọc.

#### 3.1.2 Các Tác nhân Hóa sinh và Thông số Vận hành Chi phối
- Các tác nhân hóa sinh gây tắc nghẽn cốt lõi:
  - Chất polyme ngoại bào (Extracellular Polymeric Substances - EPS):
    - Hợp chất hữu cơ do vi sinh vật bùn hoạt tính tiết ra trong quá trình sinh trưởng và trao đổi chất.
    - EPS liên kết (Bound EPS): Bao bọc quanh thành tế bào vi khuẩn. Gồm lớp liên kết lỏng lẻo (LB-EPS) và lớp liên kết chặt chẽ (TB-EPS). Nồng độ LB-EPS tương quan thuận trực tiếp với trở lực bánh cặn và tốc độ tăng TMP.
    - Thành phần hóa sinh chính: Protein (tạo liên kết kỵ nước) và Polysaccharide / Carbohydrate (tạo mạng gel ưa nước kết dính).
  - Sản phẩm vi sinh vật hòa tan (Soluble Microbial Products - SMP):
    - Các đại phân tử hữu cơ hòa tan giải phóng khi vi khuẩn chuyển hóa cơ chất hoặc tự phân hủy nội sinh.
    - Kích thước hạt rất nhỏ (< 0.45 $\mu$m). SMP dễ thâm nhập sâu vào mạng mao quản màng, trực tiếp gây bít tắc lỗ rỗng không thể đảo ngược.
  - Polyme sinh học dạng keo (Colloidal biopolymers):
    - Cầu nối liên kết giữa pha hòa tan và pha lơ lửng, tạo cấu trúc cặn nhớt khó phân tách.
- Năm thông số vận hành then chốt chi phối động học tắc nghẽn:
  - Nồng độ chất rắn lơ lửng trong bùn lỏng (Mixed Liquor Suspended Solids - MLSS):
    - Quyết định khối lượng sinh khối sẵn có tạo thành lớp bánh cặn.
    - Nồng độ MLSS cao làm tăng độ nhớt biểu kiến của bùn lỏng, làm suy giảm hiệu quả cọ rửa bề mặt màng của bọt khí.
  - Thời gian lưu bùn (Sludge Retention Time - SRT):
    - Kiểm soát tốc độ sinh trưởng của sinh khối và trạng thái trao đổi chất tế bào.
    - SRT ngắn (< 10 ngày) thúc đẩy vi khuẩn tiết nhiều LB-EPS và SMP nhớt, làm trầm trọng hóa tắc nghẽn màng.
    - SRT tối ưu (15–30 ngày) giúp tạo bông bùn ổn định, giảm lượng polyme tự do.
    - SRT quá dài (> 50 ngày) tích lũy nhiều mảnh vụn trơ và khoáng chất, làm tăng độ nhớt bùn.
  - Thời gian lưu thủy lực (Hydraulic Retention Time - HRT):
    - Quy định tốc độ pha loãng và thời gian lưu giữ chất ô nhiễm keo trong bể phản ứng.
    - HRT ngắn làm tăng tải trọng hữu cơ thể tích, giảm thời gian tiếp xúc xử lý sinh học.
  - Nồng độ oxy hòa tan (Dissolved Oxygen - DO):
    - Chi phối sự cân bằng giữa quá trình chuyển hóa hiếu khí và thiếu khí / kỵ khí.
    - Nồng độ DO quá thấp (< 1.5 mg/L) kích thích vi khuẩn tiết nhiều chất nhầy bảo vệ, phá vỡ cấu trúc bông bùn.
  - Cường độ sục khí màng (Membrane Aeration Intensity):
    - Dòng bọt khí thô liên tục tạo ứng suất cắt thủy lực (shear stress) trên bề mặt màng.
    - Ứng suất cắt cuốn trôi các phần tử bùn bám dính, ức chế lớp bánh cặn phát triển dày thêm.
- Xung đột vận hành đa mục tiêu (Multi-Objective Trade-offs):
  - Tăng MLSS giúp tăng hiệu quả phân hủy sinh học nhưng lại đẩy nhanh tốc độ tắc nghẽn màng.
  - Tăng cường độ sục khí màng giúp kiểm soát lớp cặn bám nhưng tiêu thụ 60–75% tổng điện năng toàn trạm.
  - Mối quan hệ giữa các biến số mang tính phi tuyến cao và xung đột lẫn nhau. Mô hình giải tích đơn giản không thể mô tả trọn vẹn hiện tượng này.
- Cơ sở chọn lọc đặc trưng cho Học máy (Feature Engineering):
  - Nhóm thông số {MLSS, SRT, HRT, DO, Cường độ sục khí} tạo thành tập đặc trưng đầu vào nền tảng.
  - Việc chọn các biến này xuất phát từ bản chất cơ chế hóa sinh học thay vì lựa chọn ngẫu nhiên theo trực giác thực nghiệm.

#### 3.1.3 Mô hình Dãy Trở lực Thủy lực và Mô hình Bùn Hoạt tính (ASM)
- Mô hình dãy trở lực cơ học (Resistance-in-Series Model):
  - Biểu thức mở rộng của định luật Darcy:
    $$J = \frac{\Delta P}{\mu R_t} = \frac{\Delta P}{\mu (R_m + R_c + R_p)}$$
  - Giải thích các biến số và tham số:
    - $J$: Lưu lượng thấm qua màng (Permeate flux, đơn vị: $\text{m}^3/(\text{m}^2\cdot\text{s})$ hoặc $\text{L}/(\text{m}^2\cdot\text{h})$ - LMH).
    - $\Delta P$: Áp suất qua màng (TMP, đơn vị: $\text{Pa}$ hoặc $\text{kPa}$).
    - $\mu$: Độ nhớt động học của dòng nước thấm (Permeate viscosity, phụ thuộc trực tiếp vào nhiệt độ $T$, đơn vị: $\text{Pa}\cdot\text{s}$).
    - $R_t$: Tổng trở lực thủy lực của hệ thống (Total filtration resistance, đơn vị: $\text{m}^{-1}$).
    - $R_m$: Trở lực nội tại của màng sạch (Intrinsic membrane resistance).
    - $R_c$: Trở lực của lớp bánh cặn đảo ngược được (Reversible cake layer resistance).
    - $R_p$: Trở lực bít tắc mao quản và hấp phụ không đảo ngược (Irreversible pore blocking resistance).
- Giới hạn của mô hình dãy trở lực thuần túy:
  - Giả định tĩnh: Coi các đại lượng trở lực là hằng số hoặc tăng tuyến tính theo thời gian.
  - Bỏ qua hiện tượng nén ép phi tuyến của bánh cặn khi áp suất tăng cao.
  - Bỏ qua tính chất lưu biến phi Newton của bùn hoạt tính nồng độ cao.
  - Không thể tự thích ứng khi đặc tính nước thải đầu vào biến động bất thường.
- Mô hình bùn hoạt tính (Activated Sludge Models - ASM):
  - Họ mô hình chuẩn do IWA ban hành: ASM1 (chuyển hóa COD và nitơ), ASM2d (chuyển hóa nitơ và phốt pho sinh học), ASM3 (mô hình hóa tích lũy nội bào).
  - Khung chuẩn mô phỏng BSM-MBR: Ghép nối động học phân hủy sinh học với quá trình phân tách pha bằng màng.
- Rào cản mô hình hóa cơ chế trong vận hành thực tế:
  - Đo đạc trực tuyến các phân đoạn EPS và SMP theo thời gian thực tại hiện trường rất khó khăn và tốn kém.
  - Các tham số động học sinh học rất nhạy cảm với nhiệt độ nước và lịch sử thích nghi của bùn vi sinh.
  - Chi phí giải thuật số mô phỏng toàn phần rất cao, không đáp ứng yêu cầu tính toán tức thời trên hệ thống điều khiển thực tế.
  - Cấu hình MBR thẩm thấu (Osmotic MBR - OMBR): Ghép nối màng thẩm thấu thuận (Forward Osmosis - FO) sinh ra hiện tượng phân cực nồng độ nội (ICP) và ngoại (ECP), làm phương trình giải tích vượt quá khả năng giải số đơn giản.

#### 3.1.4 Cấu trúc Vật lý Trạm MBR và Luồng Dữ liệu Cảm biến SCADA
- Sơ đồ nguyên lý vật lý hệ thống MBR (tham chiếu Hình 2 của bài báo):
  - Cụm bể phản ứng sinh học hiếu khí (Aerated bioreactor): Chứa hỗn hợp bùn lỏng hoạt tính thực hiện quá trình oxy hóa sinh hóa.
  - Cụm mô-đun màng siêu lọc đặt chìm (Submerged UF membrane modules): Thiết kế dạng sợi rỗng (Hollow-fiber) hoặc tấm phẳng (Flat-sheet), làm việc dưới áp suất hút chân không âm.
  - Bơm hút nước thấm (Permeate extraction pump) và đường ống xả nước sau xử lý (Effluent outlet).
  - Tuyến tuần hoàn bùn (Sludge recycle line): Ổn định nồng độ MLSS đồng đều giữa các ngăn bể.
  - Tuyến xả bùn dư (Waste Activated Sludge - WAS): Kiểm soát chính xác giá trị thời gian lưu bùn SRT.
  - Hệ thống sục khí màng bọt thô (Coarse-bubble aeration): Bố trí phía dưới mô-đun màng để tạo lực cắt thủy lực cọ rửa liên tục.
  - Cụm đường ống rửa ngược (Backwash) và chu trình châm hóa chất làm sạch tại chỗ (CIP).
- Hệ thống thiết bị đo đạc cảm biến trực tuyến (Online sensors):
  - Cảm biến oxy hòa tan (DO probes) đo liên tục nồng độ DO trong bể sinh học.
  - Đầu dò áp suất qua màng (TMP transducers) gắn trực tiếp trên đường ống hút nước thấm.
  - Lưu lượng kế nước thải đầu vào (Influent flow meter) và lưu lượng kế nước thấm (Permeate flow meter).
  - Đầu đo độ đục trực tuyến (Online turbidity meter) phát hiện tức thời rủi ro rách màng hoặc bùn rò rỉ.
  - Đầu đo nhiệt độ bùn lỏng (Temperature sensors) bù sai số độ nhớt thủy lực.
- Luồng dữ liệu ba tầng từ thiết bị hiện trường đến trí tuệ nhân tạo:
  - Tầng 1 (Tầng vật lý hiện trường): Cảm biến đo đạc và truyền tín hiệu dòng điện / điện áp với chu kỳ từ 1 giây đến vài phút.
  - Tầng 2 (Tầng giám sát SCADA): Hệ thống SCADA tiếp nhận, tiền xử lý, gán nhãn thời gian và lưu trữ chuỗi thời gian vào cơ sở dữ liệu lịch sử.
  - Tầng 3 (Tầng phân tích AI & Bản sao số): Mô hình học máy đọc dữ liệu SCADA để dự báo sớm giá trị TMP và đưa ra chỉ dẫn điều khiển tối ưu.

---

### 3.2 Các Mô hình Học máy Cơ bản và Dựa trên Hạt nhân

#### 3.2.1 Mạng Nơ-ron Nhân tạo Nông (ANN, MLP, RBF)
- Cấu trúc và nguyên lý toán học của mạng nơ-ron nông:
  - Mạng Perceptron đa tầng (Multilayer Perceptron - MLP): Gồm một lớp đầu vào, một đến hai lớp ẩn nông và một lớp đầu ra.
  - Tín hiệu lan truyền qua các trọng số kết nối và hàm kích hoạt phi tuyến (Sigmoid, Tanh, ReLU).
  - Thuật toán lan truyền ngược (Backpropagation): Sử dụng phương pháp hạ gradient (Gradient Descent) để cập nhật ma trận trọng số nhằm giảm thiểu hàm mất mát sai số bình phương trung bình (MSE).
- Thực nghiệm điển hình của Mirbagheri và cộng sự (2015):
  - Hệ pilot MBR chìm vận hành liên tục trong 60 ngày.
  - Mục tiêu dự báo: Áp suất TMP và độ thấm màng (Permeability).
  - Tập biến đầu vào gồm 5 thông số: Thời gian vận hành ($t$), TSS, COD, SRT và MLSS.
  - So sánh đối đầu giữa hai kiến trúc mạng nơ-ron:
    - Mạng MLP truyền thống.
    - Mạng hàm cơ sở xuyên tâm (Radial Basis Function - RBF).
  - Kết quả so sánh: Cả hai mô hình đều đạt độ chính xác khả quan. Mạng RBF vượt trội hơn nhờ tốc độ hội tụ nhanh và ít nhạy cảm với việc khởi tạo trọng số ngẫu nhiên ban đầu. Đây là ưu thế lớn khi triển khai trực tuyến.
  - Kết luận nghiên cứu: Việc lựa chọn đúng biến đầu vào và đảm bảo tính đa dạng của dữ liệu quyết định năng lực tổng quát hóa của mạng.
- Thực nghiệm của Schmitt và cộng sự (2018):
  - Xây dựng mạng ANN lan truyền ngược dự báo tắc nghẽn màng cho hệ MBR thiếu khí - hiếu khí xử lý nước thải sinh hoạt.
  - Hiệu năng định lượng: Mô hình đạt hệ số xác định $R^2 = 0.850$ trên tập dữ liệu kiểm tra độc lập (held-out test data).
  - Ý nghĩa kết quả: Phản ánh biến động mạnh của nước thải thực tế và rào cản khi mô phỏng động học tắc nghẽn bằng số lượng biến đầu vào hạn chế.
- Hạn chế cố hữu của kiến trúc mạng nơ-ron nhân tạo nông:
  - Bề mặt hàm mất mát phi lồi khiến thuật toán dễ rơi vào các cực tiểu cục bộ (local minima).
  - Tốc độ huấn luyện chậm khi gặp dữ liệu nhiễu cao.
  - Quy trình dò tìm siêu tham số (số nơ-ron lớp ẩn, tốc độ học, hệ số quán tính) phụ thuộc hoàn toàn vào kỹ thuật thử-sai.
  - Xuất hiện nguy cơ quá khớp (overfitting) nghiêm trọng khi tập dữ liệu thực nghiệm có kích thước mẫu nhỏ.

#### 3.2.2 Máy Véc-tơ Hỗ trợ (SVM / SVR) và Biến thể Bình phương Tối thiểu (LSSVM)
- Hồi quy Véc-tơ Hỗ trợ (Support Vector Regression - SVR):
  - Áp dụng nguyên lý Tối thiểu hóa Rủi ro Cấu trúc (Structural Risk Minimization - SRM): Giới hạn biên trên của sai số khái quát hóa thay vì chỉ tối thiểu hóa sai số kinh nghiệm trên tập huấn luyện như ANN.
  - Kỹ thuật hạt nhân (Kernel Trick): Ánh xạ phi tuyến các véc-tơ dữ liệu từ không gian đầu vào sang không gian đặc trưng Hilbert vô hạn chiều. Mô hình xây dựng siêu phẳng hồi quy tuyến tính tối ưu trong không gian mới.
  - Hàm nhân cơ sở xuyên tâm Gauss (Gaussian RBF Kernel):
    $$K(x, x') = \exp\left(-\gamma \|x - x'\|^2\right)$$
    Trong đó: $\gamma = \frac{1}{2\sigma^2}$ đại diện cho tham số độ rộng vùng lân cận của hạt nhân; $\|x - x'\|^2$ là bình phương khoảng cách Euclid giữa hai véc-tơ dữ liệu đầu vào $x$ và $x'$.
  - Ưu thế tối ưu hóa: Bài toán quy hoạch bậc hai lồi (Convex Quadratic Programming - QP) đảm bảo nghiệm tìm được luôn là cực trị toàn cục duy nhất.
- Máy Véc-tơ Hỗ trợ Bình phương Tối thiểu (Least Squares Support Vector Machine - LSSVM):
  - Biến đổi công thức của Suykens và Vandewalle:
    - Thay thế hàm mất mát $\varepsilon$-insensitive trong SVM tiêu chuẩn bằng hàm mất mát sai số bình phương.
    - Chuyển đổi toàn bộ các ràng buộc bất đẳng thức phức tạp thành hệ ràng buộc đẳng thức tuyến tính.
  - Giải thuật toán học tương đương:
    - Điều kiện tối ưu Karush-Kuhn-Tucker (KKT) chuyển bài toán quy hoạch bậc hai thành việc giải một hệ phương trình đại số tuyến tính:
      $$\begin{bmatrix} 0 & \mathbf{1}_N^T \\ \mathbf{1}_N & \mathbf{\Omega} + \gamma^{-1} \mathbf{I}_N \end{bmatrix} \begin{bmatrix} b \\ \boldsymbol{\alpha} \end{bmatrix} = \begin{bmatrix} 0 \\ \mathbf{y} \end{bmatrix}$$
      Trong đó: $\mathbf{\Omega}_{i,j} = K(x_i, x_j)$ là phần tử ma trận hạt nhân, $\boldsymbol{\alpha} = [\alpha_1, \dots, \alpha_N]^T$ là véc-tơ nhân tử Lagrange, $b$ là hệ số chệch, và $\gamma$ là tham số điều chuẩn.
  - Tốc độ huấn luyện: Giảm mạnh thời gian tính toán và độ phức tạp phần mềm so với việc giải quy hoạch bậc hai trong SVR tiêu chuẩn.

#### 3.2.3 Đánh giá Thực nghiệm Đối sánh và Khoảng trống Dự báo Tuổi thọ Màng
- Nghiên cứu đối sánh của Hamedi và cộng sự (2019):
  - Bối cảnh thử nghiệm: Dự báo trở lực lọc màng tổng cộng ($R_t$) trên hệ MBR phòng thí nghiệm.
  - So sánh trực tiếp 4 thuật toán: Mạng MLP tiêu chuẩn (ANN-MLP), Mạng nơ-ron tối ưu hóa bầy đàn hạt (ANN-PSO), Lập trình biểu thức gen (Gene Expression Programming - GEP), và LSSVM.
  - Kết quả định lượng vượt trội:
    - Mô hình LSSVM đạt hiệu năng dẫn đầu tuyệt đối: $R^2 = 0.990$ và $\text{MSE} = 0.0002$.
    - LSSVM vượt trội hoàn toàn so với toàn bộ các biến thể mạng nơ-ron nhân tạo.
  - Phân tích độ nhạy (Sensitivity Analysis):
    - Xác định hai biến số chi phối mạnh nhất là Lưu lượng thấm ($J$) và Áp suất qua màng (TMP).
    - Kết quả xếp hạng biến số của mô hình học máy trùng khớp hoàn hảo với lý thuyết vật lý của mô hình dãy trở lực.
- Nghiên cứu MBR nước thải công nghiệp của Giwa và cộng sự (2020):
  - Ứng dụng ANN cho hệ MBR chìm xử lý nước thải công nghiệp kết hợp sinh hoạt tại Các Tiểu Vương quốc Ả Rập Thống nhất (UAE).
  - Đầu vào gồm đặc tính nước thải thô: Độ dẫn điện, pH, tổng chất rắn lơ lửng.
  - Đầu ra dự báo: Các thông số chất lượng nước sạch (COD, BOD, độ đục).
  - Phát hiện quan trọng: Hiệu năng của mạng ANN phụ thuộc chặt chẽ vào độ phong phú của dữ liệu khi nước thải biến động tải trọng lớn.
- Thử nghiệm của Nguyen và cộng sự (2021) và bài học về nguy cơ quá khớp:
  - So sánh Hồi quy Cây quyết định (Decision Tree Regression), SVR và Hồi quy tuyến tính để dự báo TMP nước thải sinh hoạt.
  - Cây quyết định ghi nhận chỉ số danh nghĩa $R^2 = 0.99$.
  - Khuyến cáo phản biện: Kết quả $R^2$ cao bất thường này do cây quyết định ghi nhớ cấu trúc nhiễu trên tập dữ liệu nhỏ từ một trạm duy nhất. Mô hình này không có khả năng tổng quát hóa thực tế.
- Khảo sát hệ thống của Queiroz và cộng sự (2022) và khoảng trống công nghệ:
  - Phân tích thống kê 57 công trình nghiên cứu ứng dụng ML dự báo vận hành MBR.
  - Tỷ lệ áp dụng mạng ANN chiếm tới 88% tổng số công trình.
  - Khoảng trống then chốt được phát hiện: Chưa có bất kỳ nghiên cứu nào sử dụng học máy để dự báo tuổi thọ màng (membrane lifespan) hoặc dự báo thời điểm cần thay thế cụm màng. Khoảng trống này gây thiệt hại kinh tế lớn cho các đơn vị vận hành thương mại.
- Tổng quan của Schmitt & Do (2023) và Shi và cộng sự (2021):
  - Schmitt & Do: Khảo sát hơn 30 công trình mô hình hóa tắc nghẽn MBR. Hai tác giả xác định tính khan hiếm và tính đại diện của dữ liệu là rào cản lớn nhất. Nghiên cứu khuyến nghị phải đo đạc liên tục dài hạn.
  - Shi và cộng sự: Đánh giá rộng rãi ứng dụng ML trong các hệ thống màng lọc. Kết luận khẳng định các mô hình lai (Hybrid ML-mechanistic models - dùng công thức cơ chế để tính toán các biến đặc trưng đầu vào trước khi đưa vào ML) luôn vượt trội hơn mô hình hộp đen thuần túy, đặc biệt khi ngoại suy ngoài tập dữ liệu huấn luyện.

#### 3.2.4 Giới hạn Tính toán và Thách thức Mở rộng Quy mô Dữ liệu SCADA Lớn
- Bản chất bài toán đại số tuyến tính của mô hình hạt nhân:
  - Thuật toán LSSVM yêu cầu xây dựng và thao tác trực tiếp trên ma trận Gram (ma trận hạt nhân $\mathbf{\Omega}$) có kích thước $N \times N$, với $N$ là tổng số điểm dữ liệu huấn luyện.
  - Quá trình huấn luyện đòi hỏi thực hiện phép nghịch đảo ma trận hoặc phân rã Cholesky:
    $$\left(\mathbf{\Omega} + \gamma^{-1}\mathbf{I}_N\right)^{-1}$$
- Đánh giá độ phức tạp tính toán và bộ nhớ:
  - Độ phức tạp thời gian huấn luyện: $\mathcal{O}(N^3)$ phép toán số học.
  - Độ phức tạp không gian lưu trữ bộ nhớ: $\mathcal{O}(N^2)$ dung lượng RAM.
- Rào cản mở rộng trên chuỗi thời gian SCADA công nghiệp:
  - Trạm MBR hiện đại vận hành mạng cảm biến đa biến với chu kỳ lấy mẫu dày đặc từ 1 giây đến 1 phút.
  - Sau vài tháng vận hành, hệ thống ghi nhận hàng trăm nghìn đến hàng triệu bản ghi ($N > 10^5 - 10^6$).
  - Với $N = 100{,}000$, ma trận hạt nhân chiếm khoảng 80 GB bộ nhớ RAM và tiêu tốn hàng triệu tỷ phép tính dấu phẩy động. Các máy tính công nghiệp tại trạm xử lý không thể đáp ứng tải tính toán này.
  - Tính không thưa (Non-sparsity): Trong LSSVM, hầu như mọi nhân tử Lagrange $\alpha_i$ đều khác 0. Khi dự báo một điểm dữ liệu mới, mô hình phải tính toán tổng của toàn bộ $N$ hàm nhân, gây trễ nghiêm trọng cho tác vụ điều khiển thời gian thực.
- Nhu cầu cấp thiết chuyển đổi kiến trúc:
  - Giới hạn tính toán bậc ba $\mathcal{O}(N^3)$ tạo điểm nghẽn ngăn cản các mô hình hạt nhân mở rộng quy mô.
  - Xu hướng nghiên cứu bắt buộc phải dịch chuyển sang các mô hình tập hợp cây (Ensemble Methods: Random Forest, XGBoost) và các mô hình học sâu chuỗi thời gian (Deep Learning: LSTM, GRU) được phân tích chi tiết ở các phần tiếp theo.

## Cây Tri thức Chương 3 (Phần 2): Các Phương pháp Tập hợp, Học sâu, Giới hạn Dữ liệu và Kiểm chuẩn Thực nghiệm

## Chương 3 (Phần 2): Các Phương pháp Tập hợp, Học sâu, Giới hạn Dữ liệu và Kiểm chuẩn Thực nghiệm

### 3.3 Các phương pháp tập hợp và Học sâu trong mô hình hóa tắc nghẽn MBR

#### 3.3.1 Thuật toán Rừng ngẫu nhiên (Random Forest - RF) và Kỹ thuật đóng bao (Bagging)
- Bản chất và cơ chế đóng bao (Bootstrap Aggregating):
  - Thuật toán RF kết hợp dự đoán từ một tập hợp gồm nhiều cây quyết định độc lập.
  - Thuật toán huấn luyện mỗi cây trên một tập con dữ liệu ngẫu nhiên có hoàn lại từ tập dữ liệu gốc.
  - Tại mỗi nút phân nhánh, thuật toán chọn một tập con đặc trưng ngẫu nhiên thay vì quét toàn bộ biến đầu vào.
  - Cơ chế này giúp giảm phương sai (variance reduction) hiệu quả mà không làm tăng độ chệch (bias).
  - RF tạo ra khả năng chống quá khớp (overfitting resistance) vững chắc trước dữ liệu vận hành thực tế.
- Ưu thế kỹ thuật vượt trội trong dự đoán tắc nghẽn MBR:
  - RF xử lý đồng thời các biến đầu vào hỗn hợp, bao gồm cả biến liên tục và biến phân loại.
  - Mô hình có độ bền bỉ cao trước các điểm dữ liệu dị biệt (outliers) từ cảm biến SCADA.
  - RF cung cấp sẵn độ quan trọng của đặc trưng (built-in feature importance) mà không cần bước giải thích phụ trợ.
  - Độ quan trọng tính toán dựa trên mức giảm độ mờ Gini hoặc hoán vị ngẫu nhiên các đặc trưng đầu vào.
- Nghiên cứu kiểm chuẩn quy mô trạm thực của Kovacs et al. [26]:
  - Nghiên cứu thực hiện trên quy mô trạm xử lý nước thải đô thị thương mại đầy đủ (full-scale municipal WWTP).
  - Tập dữ liệu kiểm chuẩn chứa hơn 80.000 điểm mẫu đo đạc SCADA liên tục.
  - Mô hình RF đạt hệ số xác định vượt trội $R^2 = 0.927 - 0.996$ trên toàn bộ tập dữ liệu.
  - Sai số căn phương trung bình của RF đạt mức rất thấp $\text{RMSE} = 0.264 - 0.904\text{ kPa}$.
  - Nghiên cứu kiểm chứng mô hình qua bốn giai đoạn của chu kỳ lọc màng:
    - Giai đoạn tắc nghẽn ban đầu (initial fouling): hình thành lớp hấp phụ sinh học mỏng trên bề mặt màng.
    - Giai đoạn vận hành ổn định (stable operation): áp suất TMP tăng chậm và đồng đều theo thời gian.
    - Giai đoạn nén chặt bánh cặn muộn (late-stage compaction): áp suất TMP tăng vọt phi tuyến do bít tắc sâu.
    - Giai đoạn phục hồi sau rửa màng (post-cleaning recovery): đánh giá mức độ hoàn nguyên tính thấm của màng lọc.
- Giới hạn kỹ thuật và rào cản triển khai của RF:
  - Kích thước bộ nhớ RAM tăng tuyến tính theo số lượng cây quyết định trong cấu trúc tập hợp.
  - Yếu tố này cản trở việc nạp mô hình vào thiết bị cạnh (edge hardware) hoặc vi điều khiển thời gian thực.
  - Độ quan trọng đặc trưng từ RF mang tính toàn cục (global feature importance).
  - Giá trị toàn cục có thể che giấu các mối quan hệ phi tuyến cục bộ tại từng thời điểm.
  - Kỹ sư cần kết hợp thêm giá trị Shapley (SHAP) để giải thích chi tiết hành vi màng.

#### 3.3.2 Các thuật toán Tăng cường độ dốc nâng cao (XGBoost, LightGBM, CatBoost)
- Nguyên lý hoạt động của phương pháp Gradient Boosting:
  - Thuật toán xây dựng tuần tự các cây quyết định để cực tiểu hóa hàm tổn thất tổng quát.
  - Mỗi cây quyết định mới tập trung học và bù trừ sai số dư (residuals) của toàn bộ các cây trước đó.
  - Phương pháp đạt tốc độ hội tụ nhanh và độ chính xác dự báo cao với các quan hệ phi tuyến phức tạp.
- Khung thuật toán XGBoost (Extreme Gradient Boosting):
  - Tích hợp số hạng chính quy hóa L1 và L2 trực tiếp vào hàm mục tiêu để kiểm soát độ phức tạp của cây:
    $$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2 + \alpha \sum_{j=1}^T |w_j|$$
  - Áp dụng khai triển Taylor bậc hai của hàm tổn thất giúp tính toán trọng số lá tối ưu nhanh và chính xác:
    $$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ l\left(y_i, \hat{y}_i^{(t-1)}\right) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$
    trong đó $g_i$ và $h_i$ lần lượt là đạo hàm bậc nhất và bậc hai của hàm tổn thất.
  - Tích hợp kỹ thuật phân nhánh theo cột (column subsampling) và tìm kiếm điểm chia song song trên vi xử lý đa nhân.
- Khung thuật toán LightGBM (Light Gradient Boosting Machine):
  - Sử dụng chiến lược phân nhánh theo lá (leaf-wise tree growth) với độ sâu giới hạn thay vì phân nhánh theo tầng.
  - Kỹ thuật lấy mẫu một phía theo gradient (GOSS) giữ lại các mẫu gradient lớn và lấy mẫu ngẫu nhiên các mẫu nhỏ.
  - Kỹ thuật bó đặc trưng loại trừ lẫn nhau (EFB) gom các biến thưa độc lập để giảm số chiều không gian đặc trưng.
  - Các kỹ thuật này giúp giảm mạnh thời gian huấn luyện và mức tiêu thụ tài nguyên tính toán trên dữ liệu lớn.
- Khung thuật toán CatBoost (Categorical Boosting) và Thực nghiệm kiểm chuẩn [49]:
  - Kỹ thuật Ordered Boosting ngăn ngừa rò rỉ dữ liệu mục tiêu khi xử lý dữ liệu chuỗi thời gian.
  - Tự động mã hóa biến phân loại và xử lý giá trị khuyết thiếu mà không cần các bước tiền xử lý thủ công phức tạp.
  - Nghiên cứu của tác giả áp dụng CatBoost kết hợp XAI cho trạm MBR công nghiệp chế biến thực phẩm (food-processing WWTP).
  - Dữ liệu vận hành thực tế tại cơ sở này chứa nhiều tạp âm và biến động tải trọng lớn.
  - Mô hình đạt hệ số xác định $R^2 = 0.8374$.
  - Phân tích XAI chỉ ra hai nhân tố chi phối tắc nghẽn màng hàng đầu là tỷ lệ tải trọng F/M và nồng độ chất rắn lơ lửng MLSS.

#### 3.3.3 Mạng nơ-ron hồi quy chuỗi thời gian (LSTM và GRU)
- Bản chất động học thời gian của áp suất qua màng TMP:
  - Quá trình tắc nghẽn màng MBR mang bản chất phụ thuộc chuỗi thời gian tích lũy (inherently time-dependent).
  - Trạng thái áp suất TMP hiện tại lưu giữ lịch sử tích lũy của các biến động dòng thấm (permeate flux excursions).
  - Áp suất TMP cũng phản ánh toàn bộ các chu kỳ sục khí gián đoạn và sức khỏe bùn vi sinh qua nhiều ngày trước đó.
  - Các mô hình học tĩnh truyền thống (như ANN truyền thẳng) xem các mẫu là độc lập, làm mất mát thông tin động học chuỗi.
- Cấu trúc và cơ chế cổng của mạng Bộ nhớ dài ngắn hạn (LSTM - Long Short-Term Memory) [20]:
  - Ô trạng thái bộ nhớ trung tâm ($C_t$) duy trì dòng thông tin xuyên suốt chuỗi thời gian, giải quyết triệt để lỗi mất gradient.
  - Cổng quên (forget gate $f_t$) dùng hàm sigmoid ($\sigma$) để quyết định tỷ lệ thông tin cũ cần loại bỏ:
    $$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$
  - Cổng đầu vào (input gate $i_t$) phối hợp với trạng thái ứng viên ($\tilde{C}_t$) để quyết định thông tin mới nạp vào ô nhớ:
    $$i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$$
    $$\tilde{C}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$$
  - Cập nhật ô trạng thái bộ nhớ tại thời điểm $t$:
    $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
  - Cổng đầu ra (output gate $o_t$) tính toán trạng thái ẩn ($h_t$) phát ra ngoài mạng:
    $$o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$$
    $$h_t = o_t \odot \tanh(C_t)$$
- Cấu trúc Đơn vị hồi quy cổng rút gọn (Gated Recurrent Unit - GRU):
  - Tích hợp cổng quên và cổng đầu vào thành một cổng cập nhật duy nhất ($z_t$):
    $$z_t = \sigma(W_z [h_{t-1}, x_t] + b_z)$$
  - Sử dụng cổng tái lập ($r_t$) để điều chỉnh mức độ phụ thuộc vào trạng thái ẩn trong quá khứ:
    $$r_t = \sigma(W_r [h_{t-1}, x_t] + b_r)$$
  - Tính toán trạng thái ẩn ứng viên ($\tilde{h}_t$) và trạng thái ẩn cập nhật ($h_t$):
    $$\tilde{h}_t = \tanh(W_h [r_t \odot h_{t-1}, x_t] + b_h)$$
    $$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
  - Giảm khoảng 25% số lượng tham số so với LSTM, tăng tốc độ hội tụ trên các tập dữ liệu có quy mô vừa phải.
- Kết quả kiểm chuẩn thực nghiệm của Kovacs et al. [26]:
  - Mô hình ANN và LSTM cho sai số RMSE tổng thể cao hơn Random Forest trên tập dữ liệu SCADA lịch sử tĩnh.
  - Tuy nhiên, LSTM thể hiện năng lực vượt trội tại giai đoạn nén chặt bánh cặn muộn (late-stage fouling compaction).
  - Tại giai đoạn này, chuỗi lịch sử của dòng thấm và áp suất TMP nắm giữ các đặc trưng dự báo cốt lõi cho bước nhảy áp suất.
- Thách thức kỹ thuật và Giới hạn tài nguyên tính toán của LSTM:
  - Đòi hỏi kích thước dữ liệu lớn, thông thường từ hàng nghìn đến hàng chục nghìn bước thời gian để tránh quá khớp.
  - Chi phí tính toán huấn luyện và suy luận cao vượt bậc so với các mô hình RF hoặc SVM.
  - Yếu tố này gây khó khăn khi triển khai trực tiếp trên các bộ điều khiển khả trình công nghiệp (PLC) hiện hữu tại trạm.

#### 3.3.4 Kiến trúc lai, Cơ chế Tự chú ý và Mạng chuyên dụng MBR-Net
- Kiến trúc tích hợp không - thời gian (CNN-LSTM Hybrid):
  - Các lớp tích chập không gian (1D hoặc 2D CNN) đóng vai trò bộ lọc trích xuất các đặc trưng tương quan không gian.
  - Bộ lọc không gian gom cụm tín hiệu từ nhiều cảm biến đo đạc đồng thời (DO, nhiệt độ, MLSS, lưu lượng).
  - Các lớp LSTM tiếp nhận véc-tơ đặc trưng không gian để học động học tiến triển theo thời gian (temporal dynamics).
  - Kiến trúc lai giúp giảm suy hao thông tin và nắm bắt tốt tương tác đa biến trong bể phản ứng màng.
- Mô hình Transformer và Cơ chế Tự chú ý (Self-Attention) [46]:
  - Loại bỏ hoàn toàn cấu trúc hồi quy tuần tự, tính toán trực tiếp mức độ tương quan giữa tất cả các bước thời gian:
    $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
  - Cơ chế tự chú ý đa đầu (Multi-Head Attention) nắm bắt đồng thời các mẫu động học ở các thang đo thời gian khác nhau.
  - Mô hình theo dõi cả chu kỳ sục khí ngắn hạn và chu kỳ lão hóa màng dài hạn.
  - Transformer thiết lập chuẩn mực độ chính xác cao nhất trong các bài toán dự báo chuỗi thời gian môi trường.
  - Mô hình mở ra định hướng nghiên cứu tiên phong cho dự đoán tắc nghẽn MBR nhưng chưa có công trình phản biện nào đánh giá hệ thống.
  - Điểm nghẽn chính nằm ở yêu cầu dữ liệu khổng lồ và chi phí tính toán tỷ lệ bậc hai với chiều dài chuỗi $O(T^2)$.
- Mạng học sâu chuyên dụng MBR-Net [50]:
  - Kiến trúc học sâu tùy biến tích hợp mạng lưới vạn vật kết nối công nghiệp (Industrial IoT).
  - Thực hiện nhiệm vụ dự báo trước một ngày (one-day-ahead forecasting) áp suất qua màng TMP trong thời gian thực.
  - Đạt hệ số xác định $R^2 > 0.87$ trên hai tập dữ liệu kiểm thử độc lập từ cùng một trạm xử lý đô thị quy mô đầy đủ.
- Các kỹ thuật nén mô hình phục vụ triển khai phần cứng biên (Edge AI):
  - Kỹ thuật cắt tỉa mô hình (Model Pruning): loại bỏ các liên kết nơ-ron dư thừa, giảm kích thước mạng mà vẫn giữ độ chính xác.
  - Lượng tử hóa mô hình (Quantization): chuyển đổi định dạng số thực 32-bit (FP32) sang số nguyên 8-bit (INT8), tiết kiệm 75% bộ nhớ.
  - Chưng cất tri thức (Knowledge Distillation): chuyển giao tri thức từ mạng giáo viên phức tạp sang mạng học sinh gọn nhẹ để nhúng vào vi điều khiển.

#### 3.3.5 Ứng dụng mô hình AI trong hệ thống MBR thẩm thấu (OMBR)
- Đặc thù công nghệ của hệ thống OMBR (Osmotic Membrane Bioreactor) [22]:
  - Hệ thống OMBR tích hợp quá trình xử lý sinh học bùn hoạt tính với màng thẩm thấu thuận (Forward Osmosis - FO).
  - Quá trình phân tách vận hành nhờ chênh lệch áp suất thẩm thấu ($\Delta \pi$) giữa nước thải và dung dịch rút nồng độ cao.
  - Động học màng chịu sự chi phối phức tạp từ hiện tượng phân cực nồng độ bên trong (ICP) và bên ngoài (ECP).
  - Quá trình lọc còn chịu ảnh hưởng bởi sự pha loãng dung dịch rút và hiện tượng dòng muối ngược (reverse salt flux - RSF).
- Mô hình hóa bằng AI của Viet và Jang [22]:
  - Nhóm tác giả áp dụng các kiến trúc AI để dự đoán hiệu năng hệ thống OMBR xử lý nước thải đô thị.
  - Thông số đầu vào gồm các chỉ tiêu hóa lý nước cấp: pH, độ dẫn điện, nồng độ amoni ($\text{NH}_4\text{-N}$), tổng nitơ (TN), và tổng cacbon hữu cơ (TOC).
  - Biến mục tiêu dự báo gồm thông lượng nước qua màng (water flux) và trở lực tắc nghẽn màng (fouling resistance).
  - Mô hình đạt hệ số xác định cao $R^2 = 0.92 - 0.98$.
  - Phương pháp hướng dữ liệu giải quyết trọn vẹn các bậc tự do phức tạp mà không cần giải hệ phương trình truyền khối FO phi tuyến cao.

### 3.4 Giới hạn tập dữ liệu, Nguy cơ quá khớp và Khả năng tổng quát hóa liên cơ sở

#### 3.4.1 Cạm bẫy dữ liệu đơn trạm (Single-Site Trap) và Quy mô mẫu hạn chế
- Hiện tượng phụ thuộc vào dữ liệu đơn cơ sở trong y văn:
  - Đa số các nghiên cứu ML trong lĩnh vực MBR (hơn 85%) chỉ huấn luyện và kiểm chuẩn mô hình trên một cơ sở duy nhất.
  - Các tập dữ liệu phần lớn có quy mô phòng thí nghiệm hoặc mô hình pilot với kích thước từ vài trăm đến vài nghìn mẫu đo.
  - Nghiên cứu của Kovacs et al. [26] là ngoại lệ duy nhất ghi nhận tập dữ liệu quy mô trạm thực đô thị với hơn 80.000 mẫu SCADA.
- Nguy cơ quá khớp ẩn danh sau điểm số $R^2$ cao:
  - Các giá trị hệ số xác định rất cao trong phòng thí nghiệm (như $R^2 = 0.990$ của LSSVM [42] hay $R^2 = 0.92 - 0.98$ của OMBR [22]) cần được nhìn nhận thận trọng.
  - Khi huấn luyện và kiểm thử trên một chiến dịch vận hành đơn lẻ, điểm số $R^2$ cao phản ánh việc mô hình học thuộc cấu trúc nhiễu riêng biệt.
  - Mô hình cũng học thuộc tính tự tương quan thời gian của chiến dịch đó thay vì nắm bắt quy luật động học tổng quát.
  - Mô hình sẽ suy giảm độ chính xác nghiêm trọng khi đối mặt với điều kiện vận hành biến động ngoài thực địa.

#### 3.4.2 Lỗi rò rỉ thời gian (Data Leakage) và Chiến lược phân chia dữ liệu chuẩn xác
- Cơ chế phát sinh lỗi rò rỉ dữ liệu thời gian (Temporal Data Leakage):
  - Hầu hết các công trình nghiên cứu áp dụng kỹ thuật phân chia ngẫu nhiên tập huấn luyện và kiểm thử (random train-test split).
  - Phân chia ngẫu nhiên vi phạm nghiêm trọng tính đơn điệu thời gian của dữ liệu chuỗi quan trắc.
  - Thông tin ở các bước thời gian tương lai rò rỉ trực tiếp vào tập huấn luyện của quá khứ.
  - Lỗi rò rỉ này dẫn đến các chỉ số đánh giá ($R^2$, RMSE) lạc quan giả tạo, che giấu sự kém ổn định của mô hình.
- Khung tiêu chuẩn kiểm chuẩn chuỗi thời gian bắt buộc:
  - Bắt buộc áp dụng phương pháp kiểm chuẩn chéo phân khối theo thời gian (k-fold cross-validation with temporal blocking).
  - Người nghiên cứu cũng có thể dùng phương pháp kiểm chuẩn cửa sổ thời gian mở rộng (expanding window temporal split).
  - Các khối kiểm thử phải luôn nằm hoàn toàn phía sau các khối huấn luyện theo trục thời gian thực.
  - Cần báo cáo đường cong học tập (learning curves) biểu diễn sai số mô hình theo kích thước tập mẫu huấn luyện.
  - Bắt buộc đánh giá khả năng tổng quát hóa trên các giai đoạn vận hành độc lập về thời gian trước khi triển khai thực tế.

#### 3.4.3 Động học bùn vi sinh, Trôi dạt khái niệm (Concept Drift) và Thách thức vận hành vòng kín
- Cơ chế trôi dạt khái niệm trong hệ thống MBR thực địa:
  - Mối quan hệ thống kê giữa các biến vận hành đầu vào và áp suất TMP biến đổi liên tục theo thời gian thực.
  - Biến động nhiệt độ theo mùa ảnh hưởng sâu sắc đến độ nhớt của bùn lỏng và hoạt tính sinh học của vi sinh vật.
  - Các đợt xả thải công nghiệp đột ngột làm thay đổi tải trọng hữu cơ và nồng độ chất polyme ngoại bào EPS/SMP trong bể sinh học.
  - Quá trình lão hóa màng không thể phục hồi làm suy giảm vĩnh viễn cấu trúc lỗ rỗng và làm tăng trở lực nội tại ($R_m$).
- Khoảng cách giữa kiểm chứng SCADA lịch sử và Vận hành vòng kín (Closed-Loop Operational Deployment):
  - Việc kiểm chứng thành công trên dữ liệu SCADA lịch sử chỉ xác nhận mô hình tái tạo được các quy luật quá khứ trên một cơ sở tĩnh.
  - Vận hành vòng kín thời gian thực đòi hỏi mô hình phải hoạt động ổn định trước nhiều yếu tố bất định thực địa.
  - Các yếu tố này bao gồm hiện tượng trôi dạt cảm biến đo (sensor drift), nhiễu tín hiệu đo đạc, và độ trễ truyền dữ liệu mạng.
  - Hệ thống cũng phải ứng phó với sự cố hỏng hóc thiết bị cơ khí đột xuất trong quá trình vận hành liên tục.
  - Mô hình học máy bắt buộc phải trải qua quá trình kiểm thử trực tiếp trong điều kiện vòng kín trước khi giao quyền điều khiển tự động.

#### 3.4.4 Khả năng tổng quát hóa liên cơ sở (Cross-Site Generalization), Học chuyển giao và Thích ứng miền
- Thách thức suy giảm hiệu năng liên cơ sở (Cross-Site Performance Degradation):
  - Mô hình học máy huấn luyện tại một trạm MBR nguồn thường suy giảm độ chính xác nghiêm trọng khi áp dụng cho trạm MBR đích thứ hai.
  - Sự suy giảm này bắt nguồn từ hiện tượng lệch phân phối dữ liệu (dataset shift / domain shift).
  - Nguyên nhân xuất phát từ sự khác biệt về hình học mô-đun màng, chế độ thủy lực sục khí, và thành phần hóa lý nước thải.
  - Sự khác biệt về hệ sinh thái vi sinh vật bùn hoạt tính giữa các vùng địa lý cũng gây ra độ lệch lớn.
- Giải pháp Học chuyển giao (Transfer Learning):
  - Huấn luyện trước mô hình nền tảng trên tập dữ liệu SCADA phong phú từ một trạm nguồn quy mô lớn.
  - Đóng băng các tầng trích xuất đặc trưng cơ sở và tinh chỉnh các tầng đầu ra bằng một lượng dữ liệu nhỏ tại trạm đích mới.
- Giải pháp Thích ứng miền (Domain Adaptation):
  - Áp dụng các thuật toán tối ưu hóa nhằm cực tiểu hóa khoảng cách phân phối xác suất giữa không gian đặc trưng nguồn và đích.
  - Cả hai phương pháp đã chứng minh hiệu quả trong kỹ thuật môi trường tổng quát [17, 47] và là hướng nghiên cứu trọng tâm cho MBR.

#### 3.4.5 Bảng tổng hợp đối sánh kiểm chuẩn và Đánh giá rủi ro sai lệch (Bảng 1 và Bảng 2)
- Khung tiêu chí đánh giá mức độ rủi ro sai lệch (Bias Risk Evaluation Framework):
  - Đánh giá dựa trên hướng dẫn chuẩn mực kiểm chuẩn ML trong kỹ thuật môi trường [28, 48] và phản biện chuyên gia.
  - Mức rủi ro CAO (HIGH BIAS RISK): Nghiên cứu không có kiểm chuẩn ngoại kiểm độc lập và kích thước tập dữ liệu nhỏ hơn 500 mẫu.
  - Mức rủi ro TRUNG BÌNH (MODERATE BIAS RISK): Tập dữ liệu có kích thước lớn nhưng chỉ kiểm chuẩn trong phạm vi một cơ sở duy nhất.
  - Mức rủi ro THẤP (LOW BIAS RISK): Mô hình được kiểm chứng trên tối thiểu hai tập dữ liệu kiểm thử độc lập từ các trạm vận hành thực tế.
- Bảng 1: Phân tích so sánh toàn diện các nghiên cứu ML trong dự đoán tắc nghẽn MBR:

| Thuật toán ML | Biến mục tiêu | Quy mô trạm | $R^2$ tốt nhất | Kích thước tập dữ liệu ước tính | Kiểm chuẩn ngoại kiểm | Sai số RMSE / MSE | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ANN (MLP + RBF) | TMP / Độ thấm (TMP / permeability) | Quy mô thử nghiệm (Pilot) | Đạt yêu cầu (không công bố số liệu) | Không báo cáo (chiến dịch 60 ngày) | Không có (phân chia train-test) | Không báo cáo | [23] |
| ANN (Lan truyền ngược) | TMP, AO-MBR | Quy mô thử nghiệm (Pilot) | 0.850 | Không báo cáo (quy mô pilot) | Không có (phân chia train-test) | Không báo cáo | [25] |
| LSSVM (tối ưu nhất) | Trở lực tắc nghẽn (Fouling resistance) | Phòng thí nghiệm (Lab) | 0.990 | Không báo cáo (quy mô lab) | Không có (phân chia train-test) | $\text{MSE} = 0.0002$ | [42] |
| ANN-MLP | Trở lực tắc nghẽn (Fouling resistance) | Phòng thí nghiệm (Lab) | Thấp hơn LSSVM | Không báo cáo (quy mô lab) | Không có (phân chia train-test) | Lớn hơn LSSVM | [42] |
| Mô hình AI (OMBR) | Thông lượng nước + Trở lực tắc nghẽn | Phòng thí nghiệm (Lab) | 0.92–0.98 | Không báo cáo (lab OMBR) | Không có (phân chia train-test) | Đã báo cáo | [22] |
| Random Forest (tối ưu nhất) | TMP, trạm đô thị thương mại | Quy mô trạm thực (Full-scale) | 0.927–0.996 | >80.000 mẫu quan trắc | Không có (trạm đơn lẻ) | $\text{RMSE} = 0.264 - 0.904\text{ kPa}$ | [26] |
| LSTM | TMP, trạm đô thị thương mại | Quy mô trạm thực (Full-scale) | Thấp hơn RF (không báo cáo số cụ thể) | >80.000 mẫu quan trắc | Không có (trạm đơn lẻ) | Cao hơn RF | [26] |
| ANN | TMP, trạm đô thị thương mại | Quy mô trạm thực (Full-scale) | Thấp hơn RF (không báo cáo số cụ thể) | >80.000 mẫu quan trắc | Không có (trạm đơn lẻ) | Cao hơn RF | [26] |

- Bảng 2: So sánh phản biện các thuật toán ML chính yếu và Đánh giá rủi ro sai lệch:

| Thuật toán | Phân nhóm thuật toán | Điểm mạnh chính | Hạn chế cốt lõi | $R^2$ tốt nhất | Mức độ rủi ro sai lệch (Bias Risk) | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ANN (MLP + RBF) | Mạng ANN nông (Shallow ANN) | Tốc độ hội tụ nhanh. Xử lý tốt mối quan hệ phi tuyến giữa đầu vào và đầu ra. | Không báo cáo giá trị định lượng $R^2$. Khả năng tổng quát hóa chưa được kiểm chứng. | Không báo cáo | CAO (HIGH)¹ | [23] |
| ANN (Lan truyền ngược) | Mạng ANN nông (Shallow ANN) | Kiến trúc kinh điển đã thiết lập. Tính thực tế cao cho quy mô pilot. | Chỉ đạt $R^2 = 0.850$. Độ chính xác trung bình. Thiếu định lượng độ bất định. | 0.850 | CAO (HIGH)¹ | [24] |
| LSSVM | Dựa trên hạt nhân (Kernel-based) | Đạt $R^2$ cao nhất ở quy mô phòng thí nghiệm (0.99). Bền vững trên dữ liệu nhỏ. Tích hợp phân tích độ nhạy. | Không mở rộng được cho tập dữ liệu lớn. Thiếu năng lực mô hình hóa chuỗi thời gian. | 0.990 | CAO (HIGH)² | [42] |
| Mô hình AI (OMBR) | Đa dạng cấu trúc (Various) | Nắm bắt chính xác động lực áp suất thẩm thấu dẫn động. $R^2 = 0.92 - 0.98$. | Dữ liệu phòng thí nghiệm nhỏ. Chỉ kiểm chứng một cơ sở duy nhất. Không có kiểm chuẩn ngoại kiểm. | 0.92–0.98 | CAO (HIGH)¹ | [22] |
| Random Forest | Học tập hợp (Ensemble) | Độ chính xác cao nhất ở quy mô đầy đủ. Kháng ngoại lai tốt. Tích hợp độ quan trọng đặc trưng. Xử lý dữ liệu hỗn hợp. | Tốn nhiều bộ nhớ RAM. Độ quan trọng biến chỉ mang tính toàn cục. Chỉ kiểm chuẩn trên một trạm đơn lẻ. | 0.927–0.996 | TRUNG BÌNH (MODERATE)³ | [26] |
| LSTM | Học sâu (Mạng RNN) | Nắm bắt quan hệ phụ thuộc động học thời gian dài hạn. Tối ưu cho chuỗi thời gian TMP. | Đòi hỏi tập dữ liệu lớn. Chi phí tính toán cao. Độ chính xác kém hơn RF trong cùng nghiên cứu. | Thấp hơn RF | TRUNG BÌNH (MODERATE)³ | [26] |
| CatBoost + XAI | Tăng cường độ dốc (Gradient boosting) | Hiệu năng dự báo cao ở quy mô thực tế. XAI nhận diện rõ các nhân tố chi phối chính (F/M, MLSS). | Chỉ đạt $R^2$ trung bình (0.8374) trên dữ liệu công nghiệp nhiều tạp âm. Chỉ kiểm chứng một trạm thực phẩm duy nhất. | 0.8374 | TRUNG BÌNH (MODERATE)³ | [49] |
| MBR-Net (tùy biến) | Học sâu chuyên dụng (Deep learning) | Tích hợp IoT thời gian thực. $R^2 > 0.87$ trên hai tập kiểm thử độc lập. Hỗ trợ dự báo trước một ngày. | Phụ thuộc tính sẵn sàng của dữ liệu. Chỉ kiểm chứng trên một loại hình cơ sở. | >0.87 | THẤP (LOW)⁴ | [50] |

- Các ghi chú kỹ thuật giải trình mức độ rủi ro sai lệch:
  - Ghi chú 1: Mức độ rủi ro sai lệch phân loại theo tiêu chí Người phản biện 2. Mức Cao xảy ra khi nghiên cứu không có ngoại kiểm và dữ liệu dưới 500 mẫu. Mức Trung bình xảy ra khi dữ liệu lớn nhưng chỉ kiểm chuẩn đơn trạm. Mức Thấp đạt được khi kiểm chứng trên từ hai tập kiểm thử độc lập trở lên.
  - Ghi chú 2: Mô hình LSSVM chỉ huấn luyện trên dữ liệu phòng thí nghiệm. Số lượng mẫu không công bố nhưng phù hợp ngưỡng dưới 500 mẫu của các thí nghiệm ngắn ngày.
  - Ghi chú 3: Kiểm chuẩn thực hiện tại một trạm đô thị hoặc trạm công nghiệp duy nhất. Nghiên cứu chưa thực hiện kiểm chuẩn chéo liên cơ sở.
  - Ghi chú 4: Mô hình MBR-Net kiểm chứng trên hai tập kiểm thử độc lập từ cùng một trạm quy mô đầy đủ. Khả năng tổng quát hóa liên cơ sở giữa các trạm khác nhau cần tiếp tục nghiên cứu thêm.

## Chương 4: Trí tuệ Nhân tạo có thể Giải thích trong Hệ thống MBR (Explainable Artificial Intelligence in MBR Applications)

### 4.1 Yêu cầu bắt buộc về tính khả giải trong hệ thống nước có quản lý nghiêm ngặt

#### 4.1.1 Trách nhiệm pháp lý và an toàn môi trường trong vận hành MBR
- Rào cản triển khai Machine Learning (ML) trong ngành nước:
  - Ngành xử lý nước thải vận hành dưới các quy định môi trường pháp lý nghiêm ngặt.
  - Các hệ thống công nghiệp thông thường chấp nhận mô hình hộp đen khi mô hình giảm chi phí sản xuất.
  - Các nhà máy xử lý nước thải yêu cầu độ tin cậy tuyệt đối và khả năng giải trình nguyên nhân kỹ thuật trước các cơ quan quản lý nhà nước.
- Rủi ro pháp lý và an toàn vận hành:
  - Khuyến nghị giảm lưu lượng sục khí màng từ mô hình AI có thể gây hiện tượng tắc nghẽn màng không thể phục hồi (irreversible fouling).
  - Quyết định sai lầm của AI có thể làm gián đoạn quá trình lọc và gây vi phạm tiêu chuẩn xả thải ra nguồn tiếp nhận (permit violations).
  - Kỹ sư vận hành phải kiểm chứng tính hợp lý vật lý của mọi khuyến nghị điều khiển trong thời gian của ca trực (operating shift) [29, 51].
- Tiêu chuẩn chấp thuận mô hình điều khiển trong ngành nước:
  - Mô hình ML không chỉ cần độ chính xác dự báo cao.
  - Khuyến nghị điều khiển phải bảo đảm tính hợp lý kỹ thuật (engineering plausibility).
  - Hệ thống phải có khả năng lưu vết và lập tài liệu giải trình nguyên nhân cho từng quyết định (document decision rationale) [29].

#### 4.1.2 Rào cản tâm lý người vận hành và sự đánh đổi giữa hộp đen và hộp trắng
- Sự ngờ vực đối với mô hình hộp đen:
  - Người vận hành có tâm lý từ chối các chỉ thị tự động nếu không hiểu rõ mối liên hệ nhân quả vật lý.
  - Tâm lý e ngại rủi ro hình thành do hậu quả nghiêm trọng của các sự cố tràn bùn hoặc tắc nghẽn màng đột ngột.
- Luận điểm của Rudin về mô hình khả giải cố hữu:
  - Rudin [51] khẳng định các lĩnh vực ra quyết định tuần tự có rủi ro cao phải ưu tiên sử dụng mô hình có tính khả giải cố hữu (inherently interpretable models).
  - Phương pháp giải thích hậu kiểm (post-hoc explanations) có thể tạo ra ảo tưởng về tính minh bạch nếu mô hình xấp xỉ không khớp với thực tế.
- Giới hạn biểu diễn của mô hình hộp trắng trong MBR:
  - Động học tắc nghẽn màng trong MBR có tính phi tuyến mạnh, phụ thuộc nhiều biến trạng thái và biến thiên theo thời gian.
  - Các mô hình hộp trắng đơn giản (như hồi quy tuyến tính hoặc cây quyết định nông) không đủ năng lực biểu diễn để đạt độ chính xác cần thiết cho vận hành thực tế.
- Lựa chọn thực dụng từ XAI hậu kiểm:
  - Áp dụng các kỹ thuật XAI hậu kiểm (post-hoc XAI) trên các mô hình hộp đen hiệu năng cao (Random Forest, XGBoost, CatBoost, LSTM) là giải pháp thực tế nhất cho hệ thống MBR [48].
  - XAI tạo cầu nối giúp chuyên gia công nghệ đánh giá, kiểm chứng với quy luật động học bùn hoạt tính và thực thi hành động điều khiển kịp thời [29].

---

### 4.2 SHAP: Khung giải thích chủ đạo trong nghiên cứu MBR

#### 4.2.1 Nền tảng lý thuyết trò chơi hợp tác và công thức giá trị Shapley
- Cơ sở lý thuyết của SHAP (SHapley Additive exPlanations):
  - Phương pháp SHAP [52] xây dựng trên nền tảng lý thuyết trò chơi hợp tác của Lloyd Shapley.
  - Phương pháp xem các biến đặc trưng đầu vào như các người chơi trong một liên minh cùng đóng góp vào giá trị dự báo cuối cùng.
  - SHAP là khung giải thích xuất hiện phổ biến nhất trong các công bố nghiên cứu về MBR [53].
- Công thức toán học tính giá trị Shapley:
  - Giá trị đóng góp biên kỳ vọng $\phi_i$ của đặc trưng $i$ được xác định theo công thức:
    $$\phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} (f(S \cup \{i\}) - f(S))$$
  - Trong đó:
    - $N$: Tập hợp toàn bộ các đặc trưng đầu vào của mô hình.
    - $S$: Tập con các đặc trưng không chứa đặc trưng $i$ ($S \subseteq N \setminus \{i\}$).
    - $|S|$: Số lượng đặc trưng có trong tập hợp liên minh $S$.
    - $|N|$: Tổng số lượng đặc trưng đầu vào.
    - $f(S)$: Giá trị dự báo của mô hình khi chỉ sử dụng tập hợp đặc trưng $S$.
    - $f(S \cup \{i\}) - f(S)$: Đóng góp biên (marginal contribution) của đặc trưng $i$ khi tham gia vào tập hợp liên minh $S$.
    - $\frac{|S|!(|N|-|S|-1)!}{|N|!}$: Trọng số hoán vị ngẫu nhiên của các tập liên minh.

#### 4.2.2 Bốn thuộc tính toán học tiên đề của SHAP
- Tiên đề 1: Tính hiệu quả (Efficiency / Local Accuracy):
  - Tổng các giá trị đóng góp SHAP bằng chênh lệch giữa giá trị dự báo thực tế $f(x)$ và giá trị kỳ vọng cơ sở $\mathbb{E}[f(X)]$:
    $$\sum_{i=1}^{|N|} \phi_i(x) = f(x) - \mathbb{E}[f(X)] = f(x) - \phi_0$$
  - Thuộc tính bảo đảm phân bổ đầy đủ 100% sai lệch dự báo cho các biến đầu vào, không làm thất thoát thông tin.
- Tiên đề 2: Tính đối xứng (Symmetry):
  - Nếu hai đặc trưng $i$ và $j$ có đóng góp biên tương đương vào mọi liên minh khả dĩ ($f(S \cup \{i\}) = f(S \cup \{j\})$ với mọi $S \subseteq N \setminus \{i, j\}$):
    $$\phi_i = \phi_j$$
  - Thuộc tính bảo đảm sự công bằng tuyệt đối giữa các biến có vai trò tương đương.
- Tiên đề 3: Biến vô hiệu (Dummy / Null player / Missingness):
  - Nếu một đặc trưng $i$ không làm thay đổi giá trị dự báo trong bất kỳ liên minh nào ($f(S \cup \{i\}) = f(S)$ với mọi $S \subseteq N \setminus \{i\}$):
    $$\phi_i = 0$$
  - Thuộc tính loại bỏ hoàn toàn tác động của các biến nhiễu hoặc các biến không mang thông tin phân biệt.
- Tiên đề 4: Tính cộng (Additivity):
  - Nếu mô hình tổng thể là tổng của hai mô hình thành phần độc lập ($f = f_1 + f_2$):
    $$\phi_i(f_1 + f_2) = \phi_i(f_1) + \phi_i(f_2)$$
  - Thuộc tính cho phép tính toán giải thích nhất quán trên các mô hình kết hợp nhóm (ensemble models) như Random Forest hoặc Gradient Boosting.

#### 4.2.3 Đột phá tính toán: TreeSHAP so với KernelSHAP trên hệ thống SCADA
- Giới hạn tính toán của KernelSHAP:
  - KernelSHAP áp dụng cho mọi loại mô hình (model-agnostic) bằng phương pháp lấy mẫu xấp xỉ không gian đặc trưng.
  - Độ phức tạp tính toán tăng theo hàm số mũ: $\mathcal{O}(2^{|F|})$, với $|F|$ là số biến đặc trưng đầu vào.
  - Thời gian tính toán kéo dài khiến KernelSHAP không thể đáp ứng yêu cầu giám sát trực tuyến theo thời gian thực.
- Thuật toán TreeSHAP tối ưu hóa:
  - TreeSHAP tối ưu hóa riêng cho các mô hình cấu trúc cây (Decision Trees, Random Forest, XGBoost, CatBoost, LightGBM).
  - Thuật toán duyệt đệ quy qua các nhánh cây để theo dõi tỷ lệ mẫu đi qua các nút phân chia.
  - Độ phức tạp tính toán giảm xuống mức đa thức:
    $$\mathcal{O}(T \cdot L \cdot D^2)$$
  - Trong đó:
    - $T$: Tổng số lượng cây quyết định trong mô hình ensemble.
    - $L$: Số lượng lá tối đa trên mỗi cây.
    - $D$: Độ sâu tối đa của cây (thường $D \le 10$).
- Ý nghĩa triển khai SCADA thời gian thực:
  - TreeSHAP tạo ra giải thích định lượng trong vài mili-giây đến vài giây.
  - Tốc độ tính toán đáp ứng trọn vẹn chu kỳ quét dữ liệu của hệ thống SCADA tại nhà máy xử lý nước thải.
  - Hệ thống cho phép hiển thị tức thời nguyên nhân gây rủi ro tắc màng trên màn hình giám sát HMI của người vận hành.

#### 4.2.4 Phân tích SHAP cục bộ và toàn cục trong chẩn đoán suy giảm thông lượng
- Các công cụ trực quan hóa SHAP đa cấp:
  - Biểu đồ tóm tắt (Summary plot / Beeswarm plot): Thể hiện mức độ quan trọng toàn cục và hướng tác động (dương hoặc âm) của từng biến trên toàn bộ tập dữ liệu.
  - Biểu đồ phụ thuộc (Dependence plot): Thể hiện mối quan hệ phi tuyến giữa giá trị thực tế của một biến với giá trị SHAP, tích hợp tương tác với biến thứ hai.
  - Biểu đồ lực đẩy / Thác nước (Force plot / Waterfall plot): Phân tích nguyên nhân cho từng dự báo cục bộ riêng biệt, thể hiện sự giằng co giữa lực làm tăng rủi ro và lực làm giảm rủi ro.
- Kịch bản chẩn đoán cảnh báo tăng TMP trong 4 giờ tại nhà máy MBR đô thị:
  - Mô hình Random Forest cảnh báo áp suất xuyên màng (TMP) sẽ vượt ngưỡng vận hành trong vòng 4 giờ tới.
  - Phân tích Waterfall plot bóc tách đóng góp cụ thể của 4 biến quá trình:
    - $\text{MLSS} = +2.1\text{ kPa}$: Nồng độ bùn hoạt tính gần chạm ngưỡng trên, là nguyên nhân rủi ro hàng đầu.
    - $\text{HRT} = +1.4\text{ kPa}$: Thời gian lưu nước ngắn làm gia tăng tải trọng hữu cơ nạp vào bề mặt màng.
    - Cường độ sục khí (Aeration intensity) $= -0.8\text{ kPa}$: Tác động cắt thủy lực của bọt khí đang kìm hãm một phần tốc độ tắc nghẽn.
    - Lưu lượng nước đầu vào (Feed flow rate) $= +0.6\text{ kPa}$: Dòng vào dâng cao tạo áp lực ép chặt các hạt cặn lên bề mặt màng.
  - Tính hợp lý của quyết định vận hành:
    - Tổng giá trị SHAP cân bằng chính xác với mức tăng TMP dự báo (+3.3 kPa), thỏa mãn tính hiệu quả cục bộ.
    - Kỹ sư vận hành lập tức điều chỉnh tăng lưu lượng khí sục màng và kích hoạt sớm chu kỳ ngâm nghỉ (relaxation cycle).
    - Giải pháp dựa trực tiếp trên các biến đo SCADA quen thuộc, không đòi hỏi kiến thức chuyên sâu về ML [17, 25, 42].
- Cảnh báo hiện tượng rò rỉ dữ liệu (Data Leakage) và quá khớp (Overfitting):
  - Biểu đồ xếp hạng toàn cục phát hiện các biến phi vật lý (ví dụ: nhãn thời gian SCADA timestamp) có giá trị SHAP cao bất thường.
  - Tín hiệu này cảnh báo hiện tượng rò rỉ dữ liệu hoặc mô hình học mối tương quan giả (spurious correlations), giúp hiệu chỉnh tập dữ liệu trước khi triển khai thực tế [17, 53].

#### 4.2.5 Khám phá quy luật vật lý và động học nén bánh cặn qua SHAP chuỗi thời gian
- Kiểm chứng thực nghiệm trên quy mô thực (Full-scale MBR):
  - Nghiên cứu của Liang et al. [49]: Ứng dụng mô hình CatBoost kết hợp XAI cho hệ thống MBR xử lý nước thải chế biến thực phẩm.
  - Độ chính xác mô hình: Đạt hệ số xác định $R^2 = 0.8374$.
  - Phát hiện thuộc tính chi phối: Tỷ lệ thức ăn trên vi sinh vật ($F/M$) và nồng độ $\text{MLSS}$ là hai nhân tố chi phối chính đến tốc độ tắc nghẽn màng, hoàn toàn phù hợp với cơ chế sinh học phân hủy chất nền.
- Kiểm chứng trên hệ thống màng thẩm thấu xuôi (OMBR):
  - Nghiên cứu của Viet và Jang [22]: Ứng dụng mô hình dự báo AI trên hệ thống Osmotic MBR (OMBR).
  - Độ chính xác mô hình: Đạt $R^2 = 0.92\text{--}0.98$ cho dự báo thông lượng nước và trở lực tắc màng.
  - Quy luật vật lý thu nhận: Nồng độ dung dịch rút (draw solution concentration), pH nước đầu vào và độ dẫn điện (conductivity) là các biến chi phối chính, khớp với nguyên lý động lực áp suất thẩm thấu.
- Giám sát chẩn đoán bất thường từ dữ liệu SCADA:
  - Nghiên cứu của Newhart et al. [17]: Xây dựng khung giám sát dựa trên dữ liệu cho quản lý vận hành MBR.
  - Các mô hình ML huấn luyện trên dòng dữ liệu cảm biến SCADA thông thường phát hiện sớm các rối loạn quá trình trước khi xuất hiện suy giảm hiệu năng đo đếm được.
  - Nghiên cứu xác định các biến cảm biến giàu thông tin nhất để ước lượng trạng thái vận hành màng.
- Phát hiện sớm hiện tượng nén bánh cặn qua tiến hóa SHAP theo thời gian:
  - Khi màng bước vào chu kỳ lọc, giá trị SHAP của điểm đặt thông lượng và $\text{MLSS}$ tăng dần đơn điệu, phản ánh sự tích tụ liên tục của trở lực bánh cặn ($R_c$).
  - Giá trị SHAP âm của cường độ sục khí ban đầu lớn nhưng sau đó suy giảm dần hoặc đi vào vùng bão hòa.
  - Cơ chế vật lý: Lớp bùn chuyển đổi từ dạng cặn xốp dễ bóc tách bằng lực cắt khí sang lớp gel nén chặt (compacted gel layer) bám dính cao.
  - Ứng dụng chẩn đoán: Theo dõi đường cong SHAP động cung cấp chỉ báo sớm về điểm chuyển tiếp nghẹt màng nguy kịch, giúp rửa màng chủ động trước khi TMP chạm ngưỡng làm sạch [17, 53].

---

### 4.3 LIME, Đồ thị phụ thuộc một phần (PDP) và Các phương pháp dựa trên Gradient

#### 4.3.1 Mô hình giải thích cục bộ thay thế LIME
- Cơ chế hoạt động của LIME (Local Interpretable Model-agnostic Explanations):
  - LIME [27] tạo một mô hình thay thế cục bộ (local surrogate model) có cấu trúc tuyến tính đơn giản xung quanh điểm dự báo cụ thể $x$.
  - Phương pháp tạo ra các mẫu nhiễu (perturbations) trong vùng lân cận, gán trọng số theo khoảng cách tới $x$ và tối ưu hóa hàm mục tiêu:
    $$\xi(x) = \arg\min_{g \in G} \mathcal{L}(f, g, \pi_x) + \Omega(g)$$
  - Trong đó:
    - $f$: Mô hình hộp đen ban đầu cần giải thích.
    - $g \in G$: Mô hình giải thích cục bộ đơn giản (hồi quy tuyến tính hoặc cây quyết định nông).
    - $\pi_x(z)$: Hàm trọng số khoảng cách lân cận giữa mẫu nhiễu $z$ và điểm mẫu $x$.
    - $\mathcal{L}(f, g, \pi_x)$: Độ sai lệch cục bộ giữa dự báo của $f$ và mô hình giải thích $g$.
    - $\Omega(g)$: Tham số ràng buộc độ phức tạp của mô hình giải thích $g$.
- Ưu điểm và nhược điểm kỹ thuật của LIME:
  - Ưu điểm: Tốc độ tính toán nhanh trong phạm vi mili-giây, độc lập hoàn toàn với cấu trúc mô hình gốc.
  - Nhược điểm: Tính bất ổn định cao do phụ thuộc vào thuật toán lấy mẫu ngẫu nhiên. Hai lần chạy cùng một mẫu có thể cho ra hệ số khác nhau. Phương pháp nhạy cảm với việc chọn bán kính vùng lân cận (kernel width) [27, 55].
  - Khoảng trống nghiên cứu: Chưa có nhiều công trình so sánh định lượng có hệ thống giữa LIME và SHAP trong bối cảnh kiểm soát tắc nghẽn MBR.

#### 4.3.2 Đồ thị phụ thuộc một phần (PDP) và Đường cong kỳ vọng điều kiện cá thể (ICE)
- Khái niệm và công thức tính PDP:
  - PDP [48] trực quan hóa tác động biên trung bình của một hoặc hai biến mục tiêu $x_S$ lên đầu ra dự báo của mô hình:
    $$\hat{f}_S(x_S) = \frac{1}{n} \sum_{i=1}^n f(x_S, x_C^{(i)})$$
  - Trong đó $x_C$ là tập hợp tất cả các đặc trưng còn lại trong tập dữ liệu $n$ mẫu quan trắc.
- Phân tích đường cong ICE (Individual Conditional Expectation):
  - ICE bóc tách chi tiết tác động biên cho từng cá thể mẫu riêng biệt, tránh hiện tượng triệt tiêu dị biệt do lấy trung bình của PDP.
- Phát hiện ngưỡng chuyển tiếp phi Newton của bùn hoạt tính:
  - Đường cong PDP cho thấy khi $\text{MLSS} < 10\text{--}12\text{ g/L}$, tốc độ gia tăng TMP duy trì ở mức thấp và ổn định (đặc trưng của huyền phù loãng).
  - Khi $\text{MLSS} \ge 10\text{--}12\text{ g/L}$, đường cong PDP dốc đứng đột ngột, phản ánh quá trình bùn chuyển pha sang chất lỏng phi Newton có độ nhớt cao.
  - Đường cong ICE chỉ ra ngưỡng chuyển tiếp này bị dịch chuyển bởi nhiệt độ nước thải ($T$) và tuổi bùn (SRT), giải thích tại sao các điểm đặt cố định truyền thống thường thất bại theo mùa [48].

#### 4.3.3 Các phương pháp phân bổ thuộc tính dựa trên Gradient cho mô hình chuỗi thời gian sâu
- Cơ chế đạo hàm đồ thị tính toán:
  - Các phương pháp phân bổ dựa trên gradient (Vanilla Gradients, Integrated Gradients, Guided Backpropagation, Grad-CAM) đo lường độ nhạy của đầu ra thông qua vi phân giải tích của đồ thị tính toán nơ-ron [28, 54].
  - Áp dụng trên các kiến trúc mạng học sâu chuỗi thời gian như LSTM hoặc mạng tích hợp Convolutional-LSTM trong xử lý nước.
- Kỹ thuật Grad-CAM cho mạng nơ-ron tích chập (CNN):
  - Grad-CAM (Gradient-weighted Class Activation Mapping) sử dụng gradient của điểm số dự báo chảy vào lớp tích chập cuối cùng để tạo bản đồ nhiệt trực quan.
  - Trong chẩn đoán MBR, Grad-CAM định vị các vùng không gian hoặc các dải phổ tín hiệu cảm biến rung động, áp suất mang dấu hiệu tắc nghẽn cục bộ.
- Công thức Integrated Gradients (IG):
  - Tính tích phân gradient dọc theo đường nối từ điểm tham chiếu đường cơ sở $x'$ đến đầu vào $x$:
    $$\text{IG}_i(x) = (x_i - x'_i) \times \int_{0}^{1} \frac{\partial f(x' + \alpha (x - x'))}{\partial x_i} d\alpha$$
- Khám phá cửa sổ thời gian quyết định tắc nghẽn MBR:
  - Bản đồ phân bổ gradient trên mô hình LSTM xác định các bước thời gian mang thông tin quyết định cao nhất đối với giá trị TMP hiện tại.
  - Cửa sổ thời gian then chốt nằm trong khoảng $2\text{--}8\text{ giờ}$ ngay trước thời điểm xuất hiện bước nhảy TMP.
  - Cơ chế vật lý: Đây là thang thời gian đặc trưng của quá trình tích tụ các chất ngoại bào (EPS/SMP), tạo mầm bánh cặn và nén chặt cấu trúc màng, cung cấp cơ sở định lịch rửa ngược và sục khí [28].

#### 4.3.4 Bảng 2: So sánh toàn diện các phương pháp XAI trong hệ thống MBR
(Tổng hợp đối chiếu từ Table 3 trong tài liệu gốc và các bằng chứng thực nghiệm vận hành MBR)

| Phương pháp XAI | Phạm vi giải thích | Loại mô hình tương thích | Độ phức tạp tính toán | Bằng chứng thực nghiệm trong MBR / Xử lý nước | Ưu điểm cốt lõi | Nhược điểm và Hạn chế |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SHAP** (Shapley Additive exPlanations) | Cục bộ + Toàn cục (Local & Global) | Độc lập mô hình (Model-agnostic). Tối ưu hóa trên mô hình Cây (Tree-based) | Trung bình - Cao (KernelSHAP: $\mathcal{O}(2^{|F|})$. TreeSHAP: $\mathcal{O}(T \cdot L \cdot D^2)$) | Liang et al. ($R^2 = 0.8374$), Viet & Jang ($R^2 = 0.92\text{--}0.98$), Newhart et al. [17, 22, 49, 53] | Nền tảng lý thuyết trò chơi toán học vững chắc. Thỏa mãn 4 tiên đề. Tính cộng cục bộ chính xác. Phát hiện động học nén bánh cặn. | Tốn kém tài nguyên tính toán đối với dữ liệu lớn nếu không dùng mô hình dạng cây. Đòi hỏi giả định độc lập biến nền. |
| **LIME** (Local Interpretable Model-agnostic Explanations) | Cục bộ (Local) | Độc lập mô hình (Model-agnostic) | Thấp - Trung bình (Vài mili-giây trên mẫu đơn lẻ) | Phát hiện bất thường cảm biến SCADA, phân loại suy thoái chất lượng nước [27, 55] | Tốc độ trích xuất cực nhanh. Phù hợp bảng điều khiển vận hành thời gian thực. Trực quan qua hệ số tuyến tính. | Kết quả bất ổn định do lấy mẫu ngẫu nhiên nhiễu. Nhạy cảm cao với bán kính vùng lân cận. Không cung cấp bức tranh toàn cục. |
| **PDP / ICE** (Partial Dependence / Individual Conditional Expectation) | Toàn cục (PDP) + Bóc tách cá thể (ICE) | Độc lập mô hình (Model-agnostic) | Thấp ($\mathcal{O}(n \cdot K)$ với $K$ điểm lưới khảo sát) | Nhận diện ngưỡng chuyển tiếp nồng độ bùn $\text{MLSS} = 10\text{--}12\text{ g/L}$, phân tích đường cong vận hành [48] | Trực quan hóa trực tiếp mối quan hệ phi tuyến. Nhận diện các điểm uốn vật lý. ICE chỉ ra sự biến thiên theo nhiệt độ và SRT. | Giả định tính độc lập giữa các biến khảo sát và các biến còn lại. Bỏ qua tương tác phức tạp đa biến trên không gian cao chiều. |
| **Integrated Gradients** (và Grad-CAM / Gradient) | Cục bộ theo chuỗi thời gian và không gian (Temporal / Spatial Local) | Mạng nơ-ron khả vi (Deep Neural Networks, LSTM, CNN-LSTM) | Thấp (Tính đạo hàm giải tích trên đồ thị tính toán) | Dự báo TMP bằng LSTM, xác định cửa sổ trễ quyết định $2\text{--}8\text{ giờ}$ trước khi tắc nghẽn [28, 54] | Nắm bắt chính xác động học trễ chuỗi thời gian. Giải tích trực tiếp trên đồ thị mạng. Tính toán nhanh trên GPU. | Chỉ áp dụng cho các cấu trúc mạng nơ-ron khả vi. Nhạy cảm với việc định nghĩa điểm cơ sở tham chiếu (baseline). |
| **ANCHORS** | Cục bộ dạng luật (Rule-based Local) | Độc lập mô hình (Model-agnostic) | Cao (Tìm kiếm tổ hợp không gian trạng thái) | Trích xuất luật if-then trong nghiên cứu lý thuyết vận hành MBR [27] | Cung cấp các điều kiện biên rõ ràng, dễ hiểu cho người vận hành không chuyên tin học. Độ bao phủ và độ chính xác cao. | Chi phí tính toán tìm kiếm luật cao. Khó biểu diễn cho các biến số liên tục có biến thiên phức tạp trong xử lý nước. |

## Chương 5: Tối ưu hóa Năng lượng Tiêu thụ trong Hệ thống MBR bằng Học máy

### 5.1 Cấu trúc tiêu thụ năng lượng và Mục tiêu tối ưu hóa

#### 5.1.1 Suất tiêu hao năng lượng riêng (SEC) và Cấu trúc chi phí vận hành
- Chi phí năng lượng trong vận hành MBR:
  - Chi phí điện năng là khoản chi phí vận hành (OPEX) lớn nhất trong hệ thống MBR, chỉ đứng sau chi phí thay màng định kỳ.
  - Quá trình sục khí tiêu thụ phần lớn điện năng của toàn bộ trạm xử lý.
- Dải giá trị suất tiêu hao năng lượng riêng (SEC - Specific Energy Consumption):
  - Suất tiêu hao năng lượng riêng biểu thị lượng điện năng tiêu thụ trên một đơn vị thể tích nước xử lý ($\text{kWh/m}^3$).
  - Hệ thống MBR tiêu thụ điện năng tổng cộng trong khoảng $0.4\text{--}1.5\text{ kWh/m}^3$.
  - Mức tiêu thụ năng lượng trung bình của trạm MBR điển hình dao động trong khoảng $0.8\text{--}1.1\text{ kWh/m}^3$ [15].
  - Mức tiêu hao năng lượng của MBR cao gấp $2\text{--}3\text{ lần}$ so với công nghệ bùn hoạt tính truyền thống (CAS - Conventional Activated Sludge).
  - Trạm xử lý bằng công nghệ CAS truyền thống chỉ tiêu thụ khoảng $0.3\text{--}0.6\text{ kWh/m}^3$.
- Biến thiên năng lượng theo cấu hình trạm và tính chất nước thải:
  - Khảo sát thực nghiệm của Germain và cộng sự [57] chỉ ra nhu cầu năng lượng riêng biến động lớn giữa các cấu hình MBR khác nhau.
  - Đánh giá đối chuẩn (benchmarking) giữa các trạm đòi hỏi phải chuẩn hóa cẩn thận theo độ mạnh của nước thải đầu vào (influent strength) và các mục tiêu chất lượng xử lý [57].
  - Các yếu tố chính chi phối phân bố SEC gồm chiến lược điều khiển sục khí, điểm đặt thông lượng màng ($J$) và khả năng lắng của bùn hoạt tính [15].

#### 5.1.2 Phân bổ các thành phần năng lượng trong trạm MBR
- Tỷ trọng tiêu thụ điện năng giữa các phân hệ thiết bị:
  - Sục khí màng (thổi bọt khí thô cọ rửa bề mặt màng): Chiếm $60\%\text{--}75\%$ tổng điện năng tiêu thụ của toàn bộ trạm MBR.
  - Sục khí sinh học (thổi bọt khí mịn cấp oxy hòa tan cho vi sinh vật hiếu khí): Chiếm $15\%\text{--}20\%$ tổng điện năng tiêu thụ.
  - Hệ thống bơm hút màng (bơm thấm qua màng) và bơm bùn tuần hoàn: Chiếm $10\%\text{--}15\%$ tổng điện năng tiêu thụ.
- Bằng chứng kiểm chuẩn mô hình cơ chế từ Verrecht và cộng sự [56]:
  - Tác giả xây dựng mô hình năng lượng cơ chế và kiểm chuẩn trên hai trạm MBR quy mô thực tế.
  - Kết quả xác định tổng năng lượng dành cho sục khí cọ rửa màng kết hợp sục khí xử lý sinh học tiêu tốn từ $0.4\text{--}0.8\text{ kWh/m}^3$.
  - Sục khí cọ rửa cơ học nhằm hạn chế phân cực nồng độ và bám cặn chiếm tỷ trọng áp đảo trong tổng nhu cầu sục khí.

#### 5.1.3 Các chiến lược điều khiển sục khí truyền thống và Giới hạn kỹ thuật
- Điều khiển lưu lượng khí theo điểm đặt cố định (Fixed air flow rate setpoints):
  - Kỹ sư xác định các điểm đặt lưu lượng khí cố định trong các thử nghiệm vận hành ban đầu (commissioning trials).
  - Máy thổi khí duy trì tốc độ sục khí cọ rửa màng ở mức thiết kế cực đại liên tục trong suốt quá trình vận hành.
  - Chế độ cố định không xét đến điều kiện tắc nghẽn thực tế trên bề mặt màng.
  - Trạm gặp tình trạng sục khí dư thừa liên tục (systematic over-aeration), gây lãng phí năng lượng lớn trong các giai đoạn màng còn sạch (ngay sau chu kỳ rửa ngược hoặc sau khi tẩy rửa hóa chất CIP).
- Điều khiển hồi tiếp tích phân tỷ lệ (PI) theo oxy hòa tan ($DO$ feedback control):
  - Bộ điều khiển PI điều chỉnh tốc độ cấp khí sinh học dựa trên giá trị nồng độ oxy hòa tan ($DO$) đo trực tuyến.
  - Cơ chế này nâng cao hiệu quả sử dụng năng lượng của hệ thống sục khí sinh học bọt mịn.
  - Cơ chế không quản lý và không điều khiển trực tiếp hệ thống sục khí bọt thô cọ rửa màng.
  - Thành phần tiêu thụ năng lượng lớn nhất (sục khí màng, chiếm $60\%\text{--}75\%$) tiếp tục hoạt động ở chế độ điều khiển vòng hở (open-loop control) [36].
- Các phương thức tiết giảm năng lượng cơ học thông thường:
  - Sục khí ngắt quãng (Intermittent aeration): Vận hành máy thổi khí luân phiên theo chu kỳ thời gian cố định (ví dụ chu kỳ $10\text{ s}$ bật / $10\text{ s}$ tắt).
  - Kiểm soát tỷ lệ sục khí riêng: Theo dõi tỷ lệ sục khí trên diện tích màng ($SAD_m$, $\text{m}^3/(\text{m}^2\cdot\text{h})$) hoặc tỷ lệ sục khí trên thể tích nước thấm thu hồi ($SAD_p$, $\text{m}^3_{\text{air}}/\text{m}^3_{\text{permeate}}$).
  - Giới hạn vận hành: Các chu kỳ bật tắt cố định không thích ứng kịp thời với biến động tải lượng hữu cơ, biến động lưu lượng bùn và sự hình thành lớp bánh cặn bất thường.

#### 5.1.4 Cân bằng động đa mục tiêu và Vai trò của Học máy (ML)
- Bản chất động học phi tuyến của quá trình cọ rửa màng:
  - Tốc độ sục khí cọ rửa tối ưu không phải là một thông số vận hành cố định [58].
  - Nhu cầu sục khí cọ rửa tối ưu phụ thuộc đồng thời vào trạng thái tắc nghẽn hiện tại (chiều dày và độ nén của lớp bánh cặn), độ nhớt của bùn lỏng (mixed-liquor viscosity), điểm đặt thông lượng màng ($J$) và tuổi thọ màng.
  - Các cảm biến chuẩn của mạng SCADA nhà máy không thể đo trực tiếp các đại lượng này theo thời gian thực [58].
- Bài toán đánh đổi đa mục tiêu (Trade-off):
  - Mục tiêu 1: Giảm tối đa lưu lượng thổi khí để cắt giảm chi phí điện năng vận hành máy thổi.
  - Mục tiêu 2: Duy trì ứng suất cắt thủy lực đủ mạnh để ngăn chặn các chất bẩn bám dính và giữ áp suất qua màng ($TMP$) dưới ngưỡng tới hạn.
  - Nguy cơ đánh đổi: Việc cắt giảm sục khí cọ rửa quá mức làm gia tăng tốc độ tích tụ hạt bùn và polymer ngoại bào (EPS/SMP), gây hiện tượng vọt áp $TMP$ đột ngột, làm giảm tuổi thọ màng sợi rỗng/tấm phẳng và tăng vọt chi phí hóa chất tẩy rửa CIP.
- Vai trò và Trường hợp ứng dụng tự nhiên của Học máy (ML-based aeration optimization):
  - Mô hình ML tiếp nhận luồng dữ liệu liên tục từ các cảm biến SCADA trực tuyến ($TMP$, lưu lượng thấm, $DO$, nhiệt độ, độ đục).
  - Mô hình ML dự báo chính xác tốc độ sục khí cọ rửa tối thiểu cần thiết để duy trì $TMP$ dưới ngưỡng tắc nghẽn tới hạn trong điều kiện vận hành hiện tại.
  - Mô hình cho phép điều chỉnh động lưu lượng khí: Giảm sục khí khi điều kiện vận hành thuận lợi và tự động tăng sục khí khi phát hiện nguy cơ tắc nghẽn gia tăng.
  - Kiến trúc ML cung cấp năng lực ánh xạ phi tuyến, đa biến phức tạp mà các phương pháp giải tích truyền thống không thể đáp ứng [17, 38].

---

### 5.2 Bằng chứng thực nghiệm về giảm tiêu hao năng lượng và Khoảng trống nghiên cứu

#### 5.2.1 Phân định ranh giới giữa Điều khiển cơ chế (ASM) và Điều khiển học máy (ML)
- Cảnh báo về sự nhầm lẫn kỹ thuật trong y văn:
  - Nhiều tài liệu nghiên cứu đánh đồng kết quả tiết kiệm năng lượng của mô hình cơ chế sinh hóa với mô hình dữ liệu học máy.
  - Sự đánh đồng này dẫn đến việc phóng đại mức độ sẵn sàng và trưởng thành thực tế của công nghệ học máy trong tối ưu hóa năng lượng MBR.
- Hai trường phái điều khiển năng lượng riêng biệt:
  - Trường phái 1 - Điều khiển cơ chế dựa trên mô hình bùn hoạt tính (ASM-based mechanistic control): Sử dụng các phương trình vi phân mô tả quá trình chuyển hóa sinh học (mô hình ASM1 hoặc ASM2d) kết hợp với thuật toán hồi tiếp tỷ lệ tích phân (PI).
  - Trường phái 2 - Điều khiển dựa trên dữ liệu học máy (ML-based data-driven control): Sử dụng các thuật toán học máy huấn luyện trên dữ liệu quá khứ và thời gian thực để dự báo và tối thiểu hóa nhu cầu năng lượng.
- Phân nhóm kết quả tiết kiệm năng lượng trong y văn MBR:
  - Nhóm kết quả 1: Mức tiết kiệm năng lượng đã xác thực thực nghiệm (Validated energy savings) đo đạc trực tiếp tại các nhà máy đang vận hành ở quy mô thực tế bằng chiến lược điều khiển cơ chế hoặc điều khiển hồi tiếp.
  - Nhóm kết quả 2: Mức tiết kiệm dự phóng (Projected savings) công bố trong các nghiên cứu mô phỏng số hoặc các thử nghiệm điều khiển ở quy mô pilot, nơi thuật toán và điều kiện biên thay đổi giữa các bài báo và kết quả tiết kiệm không trực tiếp đến từ thuật toán ML.

#### 5.2.2 Bằng chứng thực nghiệm điển hình từ các công trình nghiên cứu
- Công trình thực nghiệm điển hình của Sun và cộng sự (Sun et al., 2016) [59]:
  - Quy mô triển khai: Trạm xử lý nước thải MBR quy mô công nghiệp thực tế (Full-scale operational plant).
  - Phương pháp điều khiển: Mô phỏng mô hình bùn hoạt tính (ASM) kết hợp bộ điều khiển hồi tiếp tỷ lệ tích phân (ASM + PI feedback control) cho hệ thống sục khí.
  - Cơ chế vận hành: Mô hình ASM dự báo nhu cầu oxy vi sinh theo thời gian thực để tự động điều chỉnh điểm đặt sục khí sinh học.
  - Kết quả định lượng: Đạt mức giảm $20\%$ nhu cầu năng lượng sục khí của máy thổi khí.
  - Suất tiêu hao năng lượng: Hạ mức tiêu thụ năng lượng riêng toàn trạm xuống còn $0.45\text{ kWh/m}^3$.
  - Mốc đối chuẩn so sánh: Thấp hơn đáng kể so với mức cơ sở quy mô pilot $0.73\text{ kWh/m}^3$ do Verrecht và cộng sự thiết lập [14].
  - Ranh giới kỹ thuật then chốt: Thuật toán điều khiển của Sun et al. là điều khiển PI dựa trên mô hình cơ chế ASM, không phải là mô hình học máy (ML). Mức giảm $20\%$ năng lượng sục khí là mốc chuẩn xác thực cho điều khiển dựa trên mô hình cơ chế chứ không phải minh chứng riêng cho thuật toán ML.
- Nghiên cứu mô phỏng chuẩn BSM-MBR của Verrecht và cộng sự (Verrecht et al., 2010) [14]:
  - Nền tảng thử nghiệm: Mô hình mô phỏng chuẩn Benchmark Simulation Model cho MBR (BSM-MBR).
  - Phương pháp: Tối ưu hóa kịch bản vận hành trên nền tảng mô hình ASM (ASM scenario optimization).
  - Cơ chế tác động: Tinh chỉnh thời gian lưu bùn (SRT) và lưu lượng bùn tuần hoàn nội bộ.
  - Kết quả: Xác lập mốc tiêu thụ năng lượng riêng cơ sở quy mô pilot là $0.73\text{ kWh/m}^3$.
- Dải tiết kiệm năng lượng công bố trong các nghiên cứu mô phỏng:
  - Các công trình nghiên cứu mô phỏng và tối ưu hóa thiết kế MBR báo cáo mức giảm điện năng lý thuyết trong khoảng $15\%\text{--}35\%$ (hoặc phổ biến trong dải $15\%\text{--}25\%+$).
  - Các kết quả này phần lớn xuất phát từ mô phỏng số hoặc quy mô pilot với các thuật toán biến thiên, chưa chứng minh được sự đóng góp riêng biệt của ML trên hiện trường.

#### 5.2.3 Bảng tổng hợp các nghiên cứu tối ưu hóa năng lượng trong MBR (Bảng 3)
- Bảng tổng hợp các mốc chuẩn suất tiêu hao năng lượng và bằng chứng tối ưu hóa thực nghiệm (Tổng hợp từ Table 4 trong bài báo gốc):

| Quy mô nghiên cứu (Scale) | Phương pháp tiếp cận / Điều khiển (Method) | Phát hiện chính và Cơ chế vận hành (Key Finding) | Chỉ số năng lượng đã xác thực (Confirmed Energy Metric) | Tài liệu trích dẫn (Reference) |
| :--- | :--- | :--- | :--- | :--- |
| Quy mô thực tế (Full-scale) | Mô hình năng lượng cơ chế (Mechanistic energy model) | Mô hình được kiểm chuẩn thực nghiệm với sai số nằm trong phạm vi $20\%$ trên tất cả các thông số vận hành của nhà máy. | Năng lượng sục khí tiêu thụ: $0.4\text{--}0.8\text{ kWh/m}^3$ | Verrecht et al. [56] |
| Mô phỏng chuẩn BSM-MBR (BSM-MBR simulation) | Tối ưu hóa kịch bản mô hình ASM (ASM scenario optimization) | Giảm tiêu hao năng lượng vận hành bằng cách tinh chỉnh điểm đặt thời gian lưu bùn (SRT) và lưu lượng dòng tuần hoàn bùn nội bộ. | Mốc đối chuẩn quy mô pilot: $0.73\text{ kWh/m}^3$ | Verrecht et al. [14] |
| Đa trạm quy mô thực tế (Multiple full-scale) | Khảo sát thực nghiệm diện rộng (Empirical survey) | Phân tích đối chuẩn chi tiết trên nhiều trạm MBR thương mại hoạt động trong các điều kiện tải trọng và cấu hình khác nhau. | Dải tiêu thụ năng lượng điển hình: $0.8\text{--}1.1\text{ kWh/m}^3$ | Krzeminski et al. [15] |
| Quy mô thực tế (Full-scale) | Điều khiển hồi tiếp tích phân tỷ lệ dựa trên ASM (ASM + PI feedback control) | Điều khiển sục khí động học dựa trên dự báo nhu cầu oxy của mô hình ASM giúp giảm tải cho hệ thống máy thổi khí mà vẫn bảo đảm hiệu quả nitrat hóa. | Tổng tiêu thụ: $0.45\text{ kWh/m}^3$ (Giảm $20\%$ năng lượng sục khí máy thổi) | Sun et al. [59] |

- Phân tích tương quan giữa biến điều khiển và nguy cơ tắc nghẽn màng:
  - Các biến điều khiển chủ yếu trong các nghiên cứu gồm lưu lượng máy thổi khí sục màng ($Q_{air}$), lưu lượng sục khí sinh học, chu kỳ sục khí ngắt quãng và tỷ lệ bùn tuần hoàn ($Q_r$).
  - Mọi chiến lược giảm công suất máy thổi cọ rửa màng đều làm suy giảm ứng suất cắt bề mặt màng. Điều này đòi hỏi thuật toán điều khiển phải giám sát liên tục tốc độ gia tăng áp suất $\text{d}TMP/\text{d}t$ để tự động can thiệp sục khí bù trước khi xảy ra tắc nghẽn nghiêm trọng không thể phục hồi.

#### 5.2.4 Phân định ranh giới then chốt và Khoảng trống nghiên cứu thực tế
- Sự chênh lệch giữa tiềm năng mô phỏng và thực tế nhà máy:
  - Tiềm năng giảm năng lượng $15\%\text{--}35\%$ chủ yếu tồn tại trong môi trường mô phỏng toán học lý tưởng với giả định điều kiện biên không đổi.
  - Trạm xử lý thực tế đối mặt với biến động lưu lượng lớn, dao động thành phần chất ô nhiễm theo giờ, hiện tượng trôi dạt cảm biến và độ trễ phản hồi cơ học của hệ thống đường ống và máy thổi.
- Thực trạng thiếu vắng kiểm chứng học máy vòng kín quy mô thương mại:
  - Số lượng nghiên cứu ứng dụng ML chuyên sâu vào tối ưu hóa nhu cầu sục khí MBR hiện vẫn còn rất khan hiếm trong y văn học thuật.
  - Chưa có nghiên cứu bình duyệt nào chứng minh được con số tiết kiệm năng lượng định lượng đến từ một thuật toán điều khiển ML triển khai trực tiếp tại nhà máy MBR quy mô thực tế.
  - Kết quả giảm $20\%$ của Sun et al. hoàn toàn dựa trên thuật toán điều khiển hồi tiếp PI tích hợp mô hình cơ chế ASM, không phải là kết quả của thuật toán ML độc lập.
- Các định hướng nghiên cứu ưu tiên cấp bách:
  - Phát triển và xác thực mô hình tối ưu hóa sục khí động học dựa trên ML kết nối trực tiếp với luồng dữ liệu SCADA thời gian thực.
  - Triển khai các thử nghiệm điều khiển vòng kín (Closed-loop control) dài hạn trên các trạm MBR quy mô công nghiệp thực tế.
  - Thiết lập quy trình hạch toán và kiểm toán năng lượng độc lập, minh bạch và nghiêm ngặt để đo lường chính xác hiệu quả năng lượng thực tế do thuật toán ML mang lại.
- Cầu nối tích hợp sang kiến trúc Bản sao số (Digital Twin):
  - Giải quyết đồng thời bài toán dự đoán tắc nghẽn màng và bài toán tối ưu hóa năng lượng ở quy mô vận hành thực tế đòi hỏi một khung kiến trúc hợp nhất.
  - Khung kiến trúc cần kết hợp năng lực dự báo của mô hình ML, tính minh bạch kiểm toán của công cụ XAI và các quy luật động học của mô hình cơ chế ASM thành một công cụ vận hành cập nhật liên tục.
  - Công nghệ Bản sao số (Digital Twin) cung cấp tầng tích hợp kỹ thuật này để chuyển đổi từ giám sát bị động sang điều khiển tối ưu tự trị vòng kín (chuyển tiếp sang Chương 6).

## Chương 6: Khung Kiến trúc Bản sao Số cho Hệ thống MBR

### 6.1 Kiến trúc, Các thành phần và Các bậc trưởng thành công nghệ của Bản sao Số

#### 6.1.1 Khái niệm nền tảng và Đặc trưng cốt lõi của Bản sao Số
- Khái niệm khởi nguồn:
  - Khái niệm Digital Twin (DT) do Grieves đưa ra lần đầu trong sản xuất công nghiệp [30].
  - Công nghệ này mở rộng sang hàng không vũ trụ, hạ tầng năng lượng và sản xuất thông minh [32].
- Ba thành phần cốt lõi của Digital Twin công nghiệp theo Fuller và cộng sự [31]:
  - Thực thể vật lý (Physical entity): Trang bị hệ thống cảm biến và cơ cấu chấp hành.
  - Thực thể ảo (Virtual entity): Mô phỏng thực thể vật lý trên các thang thời gian tương ứng.
  - Lớp kết nối dữ liệu (Data connection layer): Đồng bộ hóa trạng thái liên tục hai chiều giữa miền vật lý và miền ảo.
- Đặc trưng mô hình ảo đa độ trung thực (Multi-fidelity virtual entity) [33]:
  - Mô hình ảo kết hợp mô hình cơ chế vật lý có độ chính xác cao cho biến đổi chậm.
  - Mô hình ảo tích hợp mô hình học máy dữ liệu (ML) có tốc độ xử lý nhanh cho biến động vận hành.
  - Sự kết hợp này đảm bảo tính khả thi tính toán thời gian thực và độ chính xác dự báo.
- Mục tiêu giá trị gia tăng trong hệ thống MBR theo Wang và cộng sự:
  - Tác giả xác định quản lý tắc nghẽn màng MBR và tối ưu hóa sục khí là hai mục tiêu giá trị cao nhất.
  - Hệ thống giúp tiết kiệm năng lượng toàn trạm và nâng cao chất lượng nước sau xử lý.
  - Hệ thống tối ưu hóa đồng thời quá trình sinh học, quá trình lọc màng và định lượng hóa chất.

#### 6.1.2 Bốn lớp kiến trúc kỹ thuật của Bản sao Số MBR
- Lớp 1 - Lớp thực thể vật lý và cảm biến đo lường (Physical & Sensing Layer):
  - Mạng SCADA hiện hữu của trạm xử lý MBR.
  - Cảm biến trực tuyến thu nhận dữ liệu gồm oxy hòa tan ($DO$), độ đục, áp suất chuyển màng ($TMP$), lưu lượng thấm ($J$), nhiệt độ ($T$), lưu lượng khí sục ($Q_{air}$).
  - Cơ cấu chấp hành vật lý gồm máy thổi khí, bơm hút màng và các van điều tiết.
- Lớp 2 - Lớp truyền thông và tiền xử lý dữ liệu (Communication & Preprocessing Layer):
  - Đường ống dữ liệu thời gian thực truyền dữ liệu lên nền tảng đám mây hoặc máy chủ biên (Edge computing) [37, 61].
  - Mạng SCADA truyền dữ liệu cảm biến thô định kỳ mỗi $1\text{ phút}$ về cơ sở dữ liệu chuỗi thời gian.
  - Hệ thống tự động kiểm tra chất lượng dữ liệu, loại bỏ giá trị bất thường và điền khuyết thiếu bằng nội suy.
- Lớp 3 - Lớp lõi mô hình hóa thứ bậc (Hierarchical Modeling Layer):
  - Phân mô hình cơ chế sinh học: Ứng dụng mô hình bùn hoạt tính ASM1 hoặc ASM2d để mô phỏng động học sinh học [34, 35].
  - Phân mô hình cơ chế màng: Ứng dụng mô hình trở lực nối tiếp (Resistance-in-series) để phân tích cơ chế tắc nghẽn [36].
  - Phân mô hình học máy: Ứng dụng mô hình Random Forest hoặc LSTM để dự báo động thái TMP [22, 26].
  - Phân mô hình chất lượng nước: Ứng dụng mô hình Gradient Boosting để dự báo nồng độ ô nhiễm nước đầu ra.
  - Mô-đun giải thích tính năng: Ứng dụng thuật toán SHAP để tính toán mức độ đóng góp thuộc tính thời gian thực [53].
  - Phân mô hình cân bằng năng lượng: Mô phỏng tiêu thụ điện năng của hệ thống sục khí và bơm [14, 56].
- Lớp 4 - Lớp giao diện vận hành và điều khiển chấp hành (Interface & Actuation Control Layer):
  - Bảng điều khiển giao diện người vận hành (Operator Dashboard) hiển thị trực quan dự báo và giải thích SHAP.
  - Hệ thống cung cấp cơ chế phê duyệt hoặc ghi đè quyết định từ nhân viên vận hành (Human-in-the-loop).
  - Vòng điều khiển gửi tín hiệu cài đặt ngược về SCADA để điều chỉnh van thổi khí, bơm màng hoặc chu trình rửa màng CIP.

#### 6.1.3 Ba bậc trưởng thành công nghệ (Maturity Tiers) và Hiện trạng triển khai
- Bậc I - Bản sao số mô tả (Tier I: Descriptive DT):
  - Năng lực: Giám sát trạng thái trạm theo thời gian thực, bảng điều khiển cảm biến, quản lý cảnh báo ngưỡng vượt, phân tích xu hướng lịch sử.
  - Yêu cầu dữ liệu: Dữ liệu mạng SCADA và các cảm biến đo trực tuyến.
  - Độ phức tạp triển khai: Thấp (Low).
  - Hiện trạng ứng dụng MBR: Đã thương mại hóa và ứng dụng phổ biến tại nhiều nhà máy MBR quy mô thực tế [5, 15].
  - Minh chứng kỹ thuật: Rodríguez-Alonso và cộng sự triển khai nền tảng vi dịch vụ trên kiến trúc điện toán biên cho toàn bộ trạm xử lý [61].
- Bậc II - Bản sao số dự đoán (Tier II: Predictive DT):
  - Năng lực: Dự báo trước $12 - 72\text{ h}$ quỹ đạo áp suất TMP, suy giảm lưu lượng thấm, chất lượng nước đầu ra và nhu cầu điện năng.
  - Chuyển đổi vận hành: Giúp người vận hành đưa ra quyết định chủ động thay vì phản ứng thụ động sau sự cố.
  - Yêu cầu dữ liệu: Dữ liệu SCADA kết hợp số liệu phân tích phòng thí nghiệm và mô hình ML đã huấn luyện.
  - Độ phức tạp triển khai: Trung bình (Medium).
  - Hiện trạng ứng dụng MBR: Đã xác thực trên mô phỏng BSM-MBR [24, 36] và kiểm chứng độc lập trên dữ liệu SCADA quy mô thực tế (Kovacs et al., 2022 [26]). Trạm thực tế chưa đưa vào vận hành cố vấn vòng kín liên tục.
- Bậc III - Bản sao số kê đơn và Tự trị (Tier III: Prescriptive DT):
  - Năng lực: Tối ưu hóa đa mục tiêu vòng kín tự trị (Closed-loop autonomous optimization), kiểm thử kịch bản giả định (What-if scenario testing), giải trình quyết định điều khiển bằng XAI.
  - Hành động thực thi: Tự động điều chỉnh điểm đặt sục khí ($DO$, $Q_{air}$), điều khiển lưu lượng thấm ($J$) và tự động lập lịch làm sạch màng CIP.
  - Cơ chế an toàn: Mô phỏng vòng kín đánh giá trước hệ quả điều khiển trước khi tác động lên hệ thống vật lý.
  - Yêu cầu dữ liệu: Bản sao số toàn diện kết hợp cơ cấu chấp hành tự động, mô-đun XAI và lớp thẩm định an toàn.
  - Độ phức tạp triển khai: Cao (High).
  - Hiện trạng ứng dụng MBR: Đang ở giai đoạn đề xuất kiến trúc lý thuyết. Chưa có công bố nào triển khai Bậc III kèm XAI trên trạm MBR quy mô thực tế tính đến tháng 12 năm 2025 [33, 37].
- Xu hướng công bố khoa học trong ngành nước:
  - Khảo sát 147 nghiên cứu từ năm 2015 đến tháng 5 năm 2025 cho thấy số lượng bài báo Digital Twin tăng từ 1 bài (năm 2015) lên 41 bài (năm 2024) [60].
  - Trong 147 nghiên cứu trên có 41 nghiên cứu tập trung vào xử lý nước thải.
  - Công nghệ đang chuyển biến rõ rệt từ nghiên cứu ý niệm sang các khung kiến trúc triển khai có cấu trúc.

### 6.2 Tích hợp XAI vào Kiến trúc Ra quyết định của Bản sao Số

#### 6.2.1 Vai trò then chốt của XAI trong hệ thống Bản sao Số
- Cầu nối minh bạch và hỗ trợ ra quyết định:
  - XAI tạo thành lớp trung gian minh bạch giữa công cụ dự báo ML và quyết định điều khiển downstream [62, 63].
  - XAI cung cấp định dạng trực quan dễ hiểu gồm biểu đồ thác nước SHAP (SHAP waterfall chart), biểu đồ thanh xếp hạng thuộc tính cục bộ (Ranked bar plot) hoặc tóm tắt văn bản [64].
  - Người vận hành đánh giá tính hợp lý của dự báo dựa trên hiện trạng công nghệ trước khi thực thi lệnh [64].
- Ba chức năng vận hành cốt lõi của XAI trong kiến trúc Digital Twin:
  - Tạo nhật ký kiểm toán gần thời gian thực (Near-real-time audit trail):
    - Hệ thống lưu lại bối cảnh giải thích đi kèm từng khuyến nghị điều khiển của mô hình.
    - Chức năng này nâng cao tính truy xuất nguồn gốc, trách nhiệm giải trình và phục vụ rà soát hậu kiểm trong các đợt kiểm tra quy định [65].
  - Hỗ trợ người vận hành ghi đè có căn cứ khoa học (Informed operator override):
    - Người vận hành không tiếp nhận hoặc bác bỏ mù quáng khuyến nghị của mô hình ML.
    - Giá trị SHAP chỉ rõ biến quy trình nào đang thúc đẩy dự báo áp suất TMP hoặc chất lượng nước.
    - Người vận hành phân biệt chính xác giữa biến động công nghệ thực tế và tín hiệu giả tạo do lỗi cảm biến đo (Measurement artefact) [17, 66].
  - Cảnh báo sớm hiện tượng trôi dạt khái niệm (Concept drift warning):
    - Sự dịch chuyển bất thường trong phân phối xếp hạng SHAP báo hiệu trôi dạt dữ liệu hoặc trạng thái vận hành nằm ngoài vùng học của mô hình [48, 67].
    - Tín hiệu này kích hoạt người vận hành kiểm tra thủ công trước khi hệ thống tiếp tục điều khiển tự động.
- Yêu cầu chức năng bắt buộc để xây dựng niềm tin:
  - Tao và cộng sự [32] cùng Barricelli và cộng sự [33] xác định khả năng giải thích là yêu cầu thiết kế bắt buộc cho Digital Twin công nghiệp đáng tin cậy.
  - Nhân viên vận hành thường ghi đè và từ chối các khuyến nghị khó hiểu khi gặp điều kiện vận hành mới, làm triệt tiêu giá trị của bản sao số.
  - XAI là điều kiện chức năng tiên quyết để xây dựng niềm tin cho việc chuyển đổi từ Bậc II (Dự đoán) sang Bậc III (Kê đơn tự trị) [37].

#### 6.2.2 Quy trình làm việc 5 giai đoạn tích hợp XAI (Hình 3 / Luồng quyết định)
- Giai đoạn 1 - Thu thập và tiền xử lý luồng dữ liệu SCADA thời gian thực:
  - Thu nhận luồng dữ liệu cảm biến thô từ trạm vật lý qua mạng SCADA theo chu kỳ $1\text{ phút}$.
  - Các thông số gồm $DO$, $TMP$, lưu lượng thấm $J$, độ đục, nhiệt độ và lưu lượng khí sục màng $Q_{air}$.
  - Dữ liệu được kiểm tra chất lượng, xử lý ngoại lai, nội suy điền giá trị khuyết thiếu và lưu trữ vào cơ sở dữ liệu chuỗi thời gian.
- Giai đoạn 2 - Dự báo trạng thái hệ thống bằng động cơ ML:
  - Động cơ ML tiếp nhận dữ liệu cảm biến thời gian thực và chuỗi dữ liệu lịch sử gần nhất.
  - Mô hình Random Forest hoặc LSTM dự báo quỹ đạo TMP trước $12 - 72\text{ h}$.
  - Mô hình Gradient Boosting ước tính nồng độ các chất ô nhiễm trong dòng nước đầu ra.
- Giai đoạn 3 - Tính toán giá trị giải thích thuộc tính bằng mô-đun SHAP:
  - Mô-đun SHAP tính toán giá trị đóng góp của từng biến số cho từng dự báo theo thời gian thực.
  - Hệ thống xuất biểu đồ đóng góp có xếp hạng thứ tự, xác định rõ mức độ và chiều hướng tác động của từng thông số vận hành lên kết quả dự báo.
- Giai đoạn 4 - Hiển thị trực quan trên bảng điều khiển giao diện người vận hành:
  - Bảng điều khiển hiển thị đồng thời giá trị dự báo và biểu đồ giải thích SHAP tương ứng.
  - Người vận hành xem xét, đánh giá cơ sở kỹ thuật và phê duyệt khuyến nghị trước khi kích hoạt hành động điều khiển.
- Giai đoạn 5 - Thực thi điều khiển và lưu vết nhật ký kiểm toán tự động:
  - Lệnh điều khiển được chuyển đến lớp chấp hành để điều chỉnh điểm đặt sục khí, lưu lượng bơm hút hoặc chu trình rửa màng CIP.
  - Hệ thống tự động ghi giá trị dự báo kèm toàn bộ giá trị giải thích SHAP vào nhật ký kiểm toán nhằm phục vụ thanh tra quy định và rà soát kỹ thuật sau vận hành.
  - Kiến trúc này đảm bảo XAI gắn liền vào cấu trúc ra quyết định, không phải mô-đun gắn thêm tùy chọn.

#### 6.2.3 Bảng so sánh các bậc trưởng thành và Bản đồ nhiệt mức độ trưởng thành nghiên cứu (Bảng 5 và Hình 3)
- Bảng tổng hợp các bậc trưởng thành Digital Twin trong hệ thống MBR (Bảng 5 trong bài báo):
  - Bậc I (Mô tả - Descriptive):
    - Năng lực vận hành: Giám sát thời gian thực, bảng điều khiển trực quan, quản lý hệ thống cảnh báo.
    - Yêu cầu dữ liệu: Dữ liệu mạng SCADA và các cảm biến đo trực tuyến.
    - Độ phức tạp kỹ thuật: Thấp (Low).
    - Trạng thái nghiên cứu: Đã triển khai thương mại rộng rãi trên quy mô thực tế [5, 15].
  - Bậc II (Dự đoán - Predictive):
    - Năng lực vận hành: Dự báo TMP, dự đoán chất lượng nước đầu ra, phát hiện sự cố trước $12 - 72\text{ h}$.
    - Yêu cầu dữ liệu: SCADA kết hợp số liệu phân tích phòng thí nghiệm và mô hình ML đã huấn luyện.
    - Độ phức tạp kỹ thuật: Trung bình (Medium).
    - Trạng thái nghiên cứu: Đã xác thực trên mô phỏng và dữ liệu trạm quy mô đầy đủ [24, 26, 36].
  - Bậc III (Kê đơn và Tự trị - Prescriptive):
    - Năng lực vận hành: Tối ưu hóa tự trị vòng kín, thử nghiệm kịch bản giả định (What-if), giải trình quyết định bằng XAI.
    - Yêu cầu dữ liệu: Bản sao số đầy đủ kết hợp cơ cấu chấp hành, mô-đun XAI và lớp thẩm định an toàn.
    - Độ phức tạp kỹ thuật: Cao (High).
    - Trạng thái nghiên cứu: Chưa có công bố triển khai trên trạm MBR quy mô thực tế trong tài liệu bình duyệt [33, 37].
- Phân tích bản đồ nhiệt mức độ trưởng thành nghiên cứu (Research Maturity Heat Map - Hình 3):
  - Ba tiêu chí đánh giá mức độ trưởng thành:
    - Khối lượng bằng chứng từ các tài liệu được bình duyệt đồng nghiệp (Peer-reviewed evidence volume).
    - Mức độ sẵn có của các kiểm chứng vận hành trên quy mô thực tế (Full-scale operational validation).
    - Mức độ triển khai thực tế tại các cơ sở xử lý nước đang hoạt động (Documented deployment in commissioned facilities).
  - Bốn cấp độ đánh giá định tính:
    - Cao (High): Cơ sở bằng chứng vững chắc, nhiều nghiên cứu độc lập cho kết quả nhất quán.
    - Vừa (Moderate): Cơ sở bằng chứng đang phát triển, có một số kiểm chứng trên pilot hoặc quy mô thực tế.
    - Mới xuất hiện (Emerging): Lĩnh vực được công nhận, bằng chứng mới dừng ở đề xuất khái niệm, mô phỏng hoặc thử nghiệm phòng thí nghiệm.
    - Thấp (Low): Không tìm thấy bằng chứng bình duyệt trong các đợt tìm kiếm có cấu trúc.
  - Ba quy luật chính rút ra từ bản đồ nhiệt Hình 3:
    - Quy luật 1 - Dự báo tắc nghẽn màng (Fouling prediction): Đạt mức Cao (High) về cơ sở bằng chứng và năng lực dự báo mô hình. Mức độ tích hợp khả năng giải thích XAI, kiểm chứng quy mô đầy đủ và mức độ sẵn sàng triển khai đều ở mức Mới xuất hiện (Emerging). Năng lực dự báo bằng ML đang phát triển vượt xa khả năng triển khai thực tế.
    - Quy luật 2 - Diễn giải hỗ trợ bởi XAI (XAI-supported interpretation): Đạt mức Cao (High) về tích hợp khả năng giải thích. Tuy nhiên kiểm chứng quy mô đầy đủ ở mức Thấp (Low) và mức độ sẵn sàng triển khai ở mức Mới xuất hiện (Emerging). Ứng dụng XAI trong hệ thống MBR hiện nay phần lớn vẫn là nghiên cứu học thuật.
    - Quy luật 3 - Triển khai Bản sao số (Digital Twin deployment): Thể hiện mức độ trưởng thành thấp nhất trong các lĩnh vực, đạt xếp hạng Mới xuất hiện (Emerging) hoặc Thấp (Low) trên toàn bộ 5 khía cạnh. Chưa có trạm MBR quy mô thực tế nào vận hành bản sao số được công bố trong tài liệu bình duyệt.
  - Ý nghĩa định hướng nghiên cứu: Các ô có mức độ trưởng thành thấp liên kết trực tiếp với 9 khoảng trống nghiên cứu được phân tích trong Chương 7, tạo lộ trình ưu tiên cho các nghiên cứu tiếp theo.

## 7. Chín Khoảng trống Nghiên cứu Then chốt và Định hướng Tương lai (Research Gaps and Future Directions)

### 7.1. Khoảng trống 1: Khan hiếm tập dữ liệu chuẩn mở đa cơ sở (Scarcity of Benchmark Datasets)

#### 7.1.1. Thực trạng dữ liệu đơn cơ sở và sự suy giảm hiệu năng do dịch chuyển tập dữ liệu (Dataset Shift)
- Giới hạn quy mô dữ liệu nghiên cứu: Phần lớn nghiên cứu chỉ huấn luyện và kiểm định mô hình trên tập dữ liệu của một cơ sở đơn lẻ.
- Hạn chế về khung thời gian quan trắc: Dữ liệu vận hành thường chỉ được thu thập trong vài tuần hoặc vài tháng. Khoảng thời gian ngắn này cản trở việc đánh giá khả năng tổng quát hóa liên cơ sở.
- Hiện tượng suy giảm độ chính xác: Khi áp dụng mô hình sang công trình MBR khác, hiệu năng dự báo suy giảm đáng kể.
- Nguyên nhân từ dịch chuyển phân phối dữ liệu (dataset shift): Mối quan hệ thống kê giữa đặc trưng đầu vào và tắc nghẽn màng khác nhau giữa các nhà máy. Dữ liệu một cơ sở không thể bao quát các biến thiên này.
- Thiếu vắng bộ dữ liệu chuẩn mực cộng đồng: Ngành học máy xử lý nước thải hiện chưa có bộ dữ liệu chuẩn. Ngành nước thiếu công cụ tương đương ImageNet trong thị giác máy tính.
- Nhu cầu cấp thiết về nền tảng dữ liệu mở Open-MBR: Cộng đồng khoa học cần xây dựng kho dữ liệu vận hành MBR mở và đa cơ sở [17, 24, 47].
- Phạm vi dữ liệu cần thu thập: Kho dữ liệu cần bao quát đa dạng công suất và cấu hình màng. Bộ dữ liệu phải đại diện cho nhiều tính chất nước thải và vùng khí hậu.
- Giới hạn của nền tảng mô phỏng BSM-MBR: Nền tảng BSM-MBR cung cấp môi trường mô phỏng giá trị [36, 50]. Tuy nhiên, dữ liệu mô phỏng không tái hiện đầy đủ đặc tính phi dừng, độ nhiễu và các ràng buộc vận hành thực tế.

#### 7.1.2. Thách thức tổng quát hóa liên cơ sở và giải pháp thích ứng miền
- Khác biệt hình học module màng: Dạng hình học module màng sợi rỗng (hollow-fiber) và màng tấm phẳng (flat-sheet) tạo ra các chế độ thủy động lực học rất khác nhau.
- Biến động hệ vi sinh vật bùn hoạt tính: Cấu trúc quần xã vi sinh vật thay đổi liên tục theo thành phần nước thải cục bộ và nhiệt độ môi trường.
- Sai lệch cửa sổ thông số vận hành: Mỗi cơ sở duy trì các khoảng thời gian lưu bùn (SRT) và thời gian lưu thủy lực (HRT) riêng biệt.
- Xung tải xả thải công nghiệp bất thường: Các đợt xả thải công nghiệp tạo ra biến động tải trọng đột ngột và biên độ lớn. Các biến động này thường vắng mặt trong tập dữ liệu huấn luyện định kỳ.
- Ứng dụng học chuyển giao (Transfer Learning): Kỹ sư lấy mô hình tiền huấn luyện từ nhà máy giàu dữ liệu. Sau đó, họ tinh chỉnh mô hình bằng ít dữ liệu tại trạm đích.
- Áp dụng thích ứng miền (Domain Adaptation): Phương pháp này giảm thiểu sự sai lệch phân phối giữa không gian đặc trưng nguồn và không gian mục tiêu.
- Bằng chứng thực nghiệm từ kỹ thuật môi trường: Transfer Learning và Domain Adaptation đã chứng minh hiệu quả trong các ứng dụng quan trắc chất lượng nước [17, 47].
- Định hướng ưu tiên nghiên cứu: Các nghiên cứu MBR đa cơ sở cần ưu tiên thử nghiệm hai phương pháp trên các tập dữ liệu chuẩn mở dùng chung.

---

### 7.2. Khoảng trống 2: Thiếu hụt định lượng độ bất định trong dự đoán (Absence of Uncertainty Quantification - UQ)

#### 7.2.1. Rủi ro vận hành của dự báo điểm đơn lẻ (Point Predictions)
- Thực trạng áp đảo của dự báo tất định: Hầu hết nghiên cứu hiện nay chỉ cung cấp giá trị dự báo điểm đơn lẻ cho các thông số MBR.
- Thiếu hụt khoảng tin cậy: Rất ít nghiên cứu công bố khoảng dự đoán (prediction intervals) hoặc giới hạn tin cậy (confidence bounds) đi kèm dự báo điểm.
- Tầm quan trọng của độ bất định trong vận hành thực tế: Giá trị bất định định hướng trực tiếp hành vi của hệ thống điều khiển tự động.
- Minh họa tác động điều khiển áp suất xuyên màng (TMP): Sai số dự báo TMP mức $\pm 2\text{ kPa}$ tạo ra phản ứng điều khiển rất khác. Mức đáp ứng này khác biệt lớn so với sai số $\pm 12\text{ kPa}$.
- Yêu cầu an toàn cho Bản sao số Cấp độ III (Tier III Prescriptive DT): Hệ thống AI ra quyết định vòng kín bắt buộc phải có biên bất định. Điều này đảm bảo an toàn tuyệt đối khi vận hành tự động.

#### 7.2.2. Phương pháp luận định lượng độ bất định: Mạng Bayes, Conformal Prediction và Monte Carlo Dropout
- Mạng nơ-ron Bayes (Bayesian Neural Networks - BNNs): Thuật toán gán phân phối xác suất lên các trọng số mạng thay vì sử dụng trọng số điểm cố định.
- Đặc điểm và rào cản của BNNs: BNNs cung cấp cơ sở toán học chặt chẽ để định lượng độ bất định. Tuy nhiên, phương pháp đòi hỏi tài nguyên tính toán rất lớn.
- Kỹ thuật Conformal Prediction: Phương pháp thiết lập các bảo đảm bao phủ không phụ thuộc phân phối (distribution-free coverage guarantees) dựa trên giả định khả hoán.
- Ưu thế tính toán của Conformal Prediction: Thuật toán có chi phí tính toán thấp. Kỹ thuật này đang được ứng dụng rộng rãi trong các hệ thống kỹ thuật đòi hỏi an toàn cao [28, 48].
- Kỹ thuật Monte Carlo Dropout: Kỹ thuật kích hoạt ngẫu nhiên lớp dropout trong giai đoạn suy luận để ước tính khoảng tin cậy với chi phí thấp.
- Định hướng nghiên cứu tương lai: Các nhóm nghiên cứu cần đánh giá hệ thống các phương pháp UQ trên các mô hình học máy ứng dụng cho công nghệ MBR.

---

### 7.3. Khoảng trống 3: Thiếu vắng triển khai Bản sao số tích hợp XAI ở quy mô thực tế (Lack of Full-Scale DT Deployments with Integrated XAI)

#### 7.3.1. Rào cản kỹ thuật và an ninh mạng ở quy mô công nghiệp
- Thực trạng nghiên cứu quy mô nhỏ: Toàn bộ công trình Digital Twin (DT) cho MBR chỉ dừng ở mô phỏng. Một số thử nghiệm khác chỉ triển khai ở quy mô pilot phòng thí nghiệm.
- Thiếu hụt triển khai cấp độ cao ngoài hiện trường: Chưa có nghiên cứu nào công bố hệ thống DT Cấp II hoặc III tại hiện trường. Toàn bộ trạm xử lý đô thị quy mô thực chưa có hệ thống này.
- Thiếu hụt tích hợp giải thích đồng thời: Chưa có hệ thống thực địa nào tạo giải thích XAI tức thời. Nhân viên vận hành chưa thể nhận khuyến nghị AI song song với giám sát.
- Thách thức hiệu chuẩn cảm biến: Cảm biến tại trạm xử lý đối mặt với hiện tượng trôi tín hiệu và bám bẩn sinh học nhanh chóng.
- Yêu cầu độ tin cậy của đường ống dữ liệu (Data Pipeline): Hệ thống truyền dẫn dữ liệu SCADA lên nền tảng DT đòi hỏi tính toàn vẹn và độ trễ thấp.
- Hạ tầng tính toán và an ninh mạng: Việc kết nối điều khiển công nghiệp với thuật toán đám mây làm tăng nguy cơ tấn công mạng.

#### 7.3.2. Yêu cầu tổ chức, trách nhiệm pháp lý và hợp tác liên ngành
- Quản trị thay đổi và đào tạo nhân sự: Đơn vị vận hành cần thích ứng với quy trình vận hành khuyến nghị bởi trí tuệ nhân tạo.
- Khung trách nhiệm hợp đồng (Contractual Liability): Trách nhiệm pháp lý khi xảy ra sự cố nghẹt màng chưa rõ ràng [33, 37]. Cơ chế phân định trách nhiệm khi vi phạm chuẩn xả thải tự động còn thiếu.
- Thiếu hụt tài liệu trong y văn học thuật: Các yếu tố tổ chức và pháp lý hầu như chưa được phân tích trong các bài báo khoa học.
- Mô hình hợp tác liên ngành mẫu mực: Nghiên cứu kiểm chứng quy mô thực của Kovacs và cộng sự [26] nêu bật giá trị hợp tác ba bên. Mô hình này kết nối nhà máy nước, đơn vị công nghệ và viện nghiên cứu.
- Lộ trình tạo lập bằng chứng thực nghiệm: Các bên cần thiết lập chương trình thử nghiệm dài hạn để làm tiền đề cho việc thương mại hóa và cấp phép công nghệ.

---

### 7.4. Khoảng trống 4: Hạn chế trong đặc tính hóa động học nước thải đầu vào (Dynamic Influent Characterization Limitations)

#### 7.4.1. Sự thiếu hụt của cảm biến SCADA thông thường trước các xung tải trọng
- Hạn chế của thiết bị đo SCADA truyền thống: Các đầu đo hiện hữu chỉ thu thập các chỉ số gộp như $\text{COD}$, $\text{BOD}$, $\text{TSS}$, độ đục, $\text{DO}$, $\text{pH}$ và độ dẫn điện.
- Tính chất gộp của thông số dòng vào: Các chỉ số trên chỉ phản ánh bức tranh tổng quát của hỗn hợp nước thải đi vào bể sinh học.
- Tác động của nước thải công nghiệp đột xuất: Sự kiện xả thải công nghiệp đưa vào hệ thống các chất độc hại và chất hoạt động bề mặt.
- Ảnh hưởng của hiện tượng nước mưa thâm nhập: Nước mưa thâm nhập pha loãng dòng vào và thay đổi đột ngột tải trọng thủy lực.
- Biến thiên chu kỳ ngày đêm của nước thải sinh hoạt: Nồng độ ô nhiễm hữu cơ và chất rắn dao động mạnh theo từng khung giờ trong ngày.
- Bất cập của phương pháp lấy mẫu hỗn hợp: Mẫu gộp 24 giờ và cảm biến trực tuyến phản ứng chậm không bắt kịp các xung dao động nhanh [3, 22].
- Hậu quả nghẹt màng bất ngờ: Các biến động động học không được đặc tính hóa là nguyên nhân chính gây ra các đợt tắc nghẽn màng nghiêm trọng.

#### 7.4.2. Tích hợp cảm biến quang phổ học nâng cao và công cụ sinh học phân tử vào tầng cảm biến DT
- Cảm biến quang phổ hấp thụ trực tuyến UV-Vis: Thiết bị cung cấp dữ liệu quang phổ liên tục để phát hiện nhanh các nhóm hợp chất hữu cơ hòa tan đặc thù.
- Đo quang phổ huỳnh quang (Fluorescence Spectrophotometry): Công nghệ này nhận diện các tín hiệu protein-like và humic-like. Các tín hiệu này thuộc chất cao phân tử ngoại bào (EPS) và chất hòa tan vi sinh (SMP).
- Chụp cắt lớp kết hợp quang học (Optical Coherence Tomography - OCT): Kỹ thuật OCT hỗ trợ quan sát trực tiếp bề mặt màng theo thời gian thực. Phương pháp này định lượng cấu trúc lớp bánh bùn (cake layer) với độ chính xác cao.
- Công cụ dấu vân tay cộng đồng vi sinh vật (Microbial Fingerprinting): Kỹ thuật sinh học phân tử giúp theo dõi sự biến đổi cấu trúc quần xã vi sinh vật gây tắc nghẽn sinh học.
- Nâng cao năng lực dự báo mô hình ML: Tích hợp chuỗi dữ liệu cao tần vào tầng cảm biến DT giúp mô hình cảnh báo sớm. Thuật toán nhận diện kịp thời các sự cố nhiễu động nguy hiểm.

---

### 7.5. Khoảng trống 5: Rào cản và khung công nhận pháp lý cho XAI (Regulatory Dimension and Acceptance Frameworks)

#### 7.5.1. Khoảng cách giữa lý thuyết XAI học thuật và thực tiễn cấp phép môi trường
- Nền tảng lý thuyết phát triển nhanh: Y văn học thuật đã chứng minh rõ tiềm năng của XAI [29, 51]. Công cụ này xây dựng niềm tin cho hệ thống quản lý nước thông minh.
- Thiếu vắng tiền lệ pháp lý thực tế: Chưa có nghiên cứu nào ghi nhận giải thích SHAP định hình điều kiện cấp phép môi trường. Tiền lệ pháp lý cho XAI trong ngành nước vẫn hoàn toàn trống.
- Thiếu tác động trong thanh tra thực tế: Đầu ra XAI chưa từng ảnh hưởng đến kết luận thanh tra hay giấy phép vận hành. Cơ quan quản lý chưa dùng XAI để điều chỉnh quy chuẩn xả thải.
- Đứt gãy giữa lý thuyết và pháp lý: Tồn tại khoảng cách lớn giữa năng lực thuật toán trong phòng thí nghiệm và cơ chế pháp lý quản lý nhà máy nước thải.
- Nguy cơ pháp lý khi tự động hóa: Đơn vị vận hành lo ngại rủi ro khi dùng mô hình chưa cấp phép. Nếu xả thải vượt ngưỡng, nhà máy phải chịu xử phạt hành chính nặng.

#### 7.5.2. Xây dựng tiêu chuẩn bằng chứng, kiểm toán và ca sử dụng được công nhận
- Đối thoại với cơ quan quản lý: Cộng đồng kỹ thuật môi trường cần làm việc chặt chẽ với cơ quan quản lý môi trường để thống nhất khung pháp lý.
- Xây dựng tiêu chuẩn bằng chứng kiểm định: Hai bên cần lập tiêu chuẩn định lượng để kiểm tra XAI. Tiêu chuẩn này xác nhận tính chính xác và an toàn của các giải thích thuật toán.
- Xác định phạm vi các ca sử dụng được chấp thuận: Quy định cần phân định rõ hai nhóm quy trình. Nhóm một cho phép AI tự động điều khiển. Nhóm hai bắt buộc con người giám sát trực tiếp.
- Yêu cầu lưu vết kiểm toán (Audit-trail Requirements): Hệ thống phải lưu trữ toàn bộ quyết định điều khiển và giải thích thuật toán để phục vụ công tác thanh tra độc lập.
- Điều kiện tiên quyết để chuyển giao công nghệ: Xây dựng khung pháp lý là bước bắt buộc để đưa hệ thống DT tích hợp XAI từ nghiên cứu vào ứng dụng thương mại.

---

### 7.6. Khoảng trống 6: Chi phí kinh tế phát triển và bảo trì mô hình ML (Economic Cost of ML Model Development and Retraining)

#### 7.6.1. Cơ cấu chi phí vòng đời: Đầu tư ban đầu và vận hành duy trì
- Yêu cầu nguồn lực phát triển hệ thống ML: Xây dựng mô hình MBR cấp công nghiệp đòi hỏi nguồn lực lớn. Doanh nghiệp phải đầu tư vào hạ tầng dữ liệu, chuyên gia và máy chủ tính toán.
- Chi phí phát triển ban đầu (Initial Development Costs):
  - Khảo sát và chuẩn hóa hệ thống cảm biến: Chi phí kiểm định thiết bị đo và cải tạo hệ thống SCADA.
  - Làm sạch dữ liệu lịch sử SCADA: Quá trình chuẩn hóa cơ sở dữ liệu quá khứ thường tiêu tốn nhiều tháng nhân công.
  - Lập trình mô hình và kiểm định chéo: Kinh phí dành cho các chu kỳ đào tạo và kiểm định thuật toán.
  - Hồ sơ pháp lý phê duyệt thay đổi quy trình: Chi phí hoàn thiện thủ tục đánh giá an toàn và tác động môi trường.
- Chi phí vận hành thường xuyên (Ongoing Maintenance Costs):
  - Tái huấn luyện mô hình định kỳ (Periodic Retraining): Nhu cầu tái huấn luyện phát sinh liên tục trong thực tế. Quá trình này bắt buộc khi tính chất nước thay đổi, thay màng hoặc đổi cấu hình trạm.
  - Thiết bị điện toán biên (Edge Computing Hardware): Chi phí khấu hao và bảo trì phần cứng xử lý tại trạm.
  - Bảo mật thông tin và an toàn mạng IT: Chi phí duy trì bản quyền phần mềm và ngăn ngừa xâm nhập.
  - Đào tạo liên tục cho kỹ thuật viên: Kinh phí nâng cao kỹ năng cho đội ngũ vận hành nhà máy.

#### 7.6.2. Nhu cầu phân tích chi phí - lợi ích định lượng đối với đơn vị vận hành
- Thiếu hụt báo cáo tài chính trong nghiên cứu: Các bài báo khoa học hiện nay hầu như không công bố chi phí phát triển và bảo trì hệ thống ML.
- Khoảng trống thông tin kinh tế: Chưa có nghiên cứu bình duyệt nào công bố bảng phân tích chi phí - lợi ích (cost-benefit analysis). Báo cáo toàn diện cho trạm MBR ứng dụng ML vẫn chưa xuất hiện.
- Khó khăn trong việc ra quyết định đầu tư: Đơn vị quản lý nước thiếu cơ sở đánh giá tính khả thi kinh tế. Họ không thể so sánh chi phí giữa ML và điều khiển cổ điển.
- Yêu cầu chuẩn mực cho nghiên cứu tương lai: Nghiên cứu tương lai cần công bố chi phí phát triển, kiểm định và bảo trì hàng năm. Các số liệu tài chính này phải đi kèm chỉ số ^2$, $	ext{RMSE}$ hay $	ext{MAPE}$.
- Khuyến nghị đánh giá tiền khả thi: Doanh nghiệp cần thực hiện đánh giá tiền khả thi chi tiết theo từng cơ sở. Bước đánh giá này phải hoàn thành trước khi đầu tư hệ thống ML.

---

### 7.7. Khoảng trống 7: Yêu cầu về nguồn nhân lực vận hành hệ thống DT và XAI (Human Capital and Workforce Requirements)

#### 7.7.1. Sự thiếu hụt nhân lực liên ngành MLOps và kỹ thuật xử lý nước
- Đòi hỏi kỹ năng chuyên môn phức hợp: Hệ thống Bản sao số Cấp II và III đòi hỏi kỹ năng phức hợp. Kỹ sư phải thành thạo kỹ thuật dữ liệu, MLOps và điều khiển quá trình.
- Thực trạng thiếu hụt kỹ sư kép trong ngành nước: Đa số đơn vị cấp thoát nước thiếu đội ngũ kỹ sư chuyên môn kép. Họ không có nhân sự am hiểu đồng thời công nghệ vi sinh và AI.
- Rào cản chuyển giao công nghệ do nhân lực: Khoảng cách ứng dụng thực tiễn bắt nguồn từ sự thiếu hụt nhân lực. Đây là rào cản về lực lượng lao động, không chỉ là rào cản công nghệ.
- Nguy cơ phụ thuộc nhà thầu ngoài: Thiếu năng lực nội bộ khiến trạm nước phụ thuộc nhà thầu phần mềm ngoài. Tình trạng này làm tăng chi phí và gây rủi ro vận hành.

#### 7.7.2. Định lượng nhu cầu nhân sự và xây dựng chương trình đào tạo
- Trách nhiệm công bố thông số nhân sự trong nghiên cứu: Nghiên cứu DT cần nêu rõ định biên nhân sự tối thiểu. Báo cáo phải mô tả chi tiết yêu cầu kỹ năng của kỹ thuật viên vận hành.
- Xây dựng mô đun đào tạo tương tác người - máy: Nhà phát triển cần thiết kế giao diện XAI trực quan. Giao diện này giúp công nhân vận hành hiểu rõ căn cứ ra quyết định của thuật toán.
- Thiết lập chương trình đào tạo chuyển đổi nghề nghiệp: Viện nghiên cứu và doanh nghiệp cần tổ chức các khóa bồi dưỡng MLOps. Chương trình đào tạo tập trung vào ứng dụng thực tế cho kỹ sư môi trường.
- Chuẩn hóa quy trình vận hành tiêu chuẩn (SOP): Đơn vị vận hành cần chuẩn hóa quy trình can thiệp thủ công (SOP). Tài liệu hướng dẫn xử lý khi hệ thống AI đưa ra quyết định sai lệch.

---

### 7.8. Khoảng trống 8: Thiếu đối chuẩn hệ thống với các phương pháp điều khiển phi-ML (Inadequate Baselines and Benchmarking against Non-ML Alternatives)

#### 7.8.1. Thực trạng đối chuẩn thiếu khách quan trong các nghiên cứu học máy
- Vị thế của các bộ điều khiển kinh điển: Bộ điều khiển PID và điều khiển mờ (Fuzzy Logic) rất phổ biến trong trạm MBR. Các thiết bị này có chi phí lắp đặt thấp và độ tin cậy đã chứng minh.
- Thiếu hụt đường cơ sở so sánh tương đương: Rất ít nghiên cứu ML so sánh đối chuẩn với bộ điều khiển PID hoặc Fuzzy Logic. Thực nghiệm đối chứng trong cùng điều kiện vận hành còn hiếm hoi.
- Thiên lệch trong việc chọn mốc so sánh: Tác giả thường so sánh mô hình ML với vận hành thủ công không tối ưu. Một số nghiên cứu chỉ so sánh với mô hình hồi quy tuyến tính thô sơ.
- Thiếu định lượng giá trị gia tăng thực chất: Thiếu mốc so chuẩn tiên tiến khiến ngành nước khó đánh giá công nghệ. Nhà máy không thể định lượng lợi ích gia tăng thực tế từ thuật toán ML.
- Bỏ qua các thuật toán điều khiển dự báo dựa trên mô hình cơ chế (Mechanistic MPC): Bộ điều khiển MPC cơ chế dựa trên mô hình bùn hoạt tính ASM đạt hiệu quả cao. Tuy nhiên, các bài báo ML hiếm khi so sánh với công nghệ này.

#### 7.8.2. Quy định bắt buộc tích hợp PID và Fuzzy Logic làm đường cơ sở đối chứng
- Tiêu chuẩn hóa phương pháp đánh giá: Nghiên cứu tương lai phải đưa PID tinh chỉnh và Fuzzy Logic làm đường cơ sở. Đây là yêu cầu bắt buộc khi công bố hiệu năng thuật toán mới.
- Đánh giá toàn diện đa tiêu chí: Nghiên cứu cần so sánh thuật toán ML với điều khiển cổ điển qua nhiều chỉ tiêu. Các tiêu chí gồm mức giảm TMP, độ ổn định dòng thấm, điện năng và tuổi thọ màng.
- Định vị miền ứng dụng tối ưu của ML: Bài báo cần xác định rõ miền làm việc tối ưu của ML. Phân tích phải chỉ ra các kịch bản mà ML vượt trội so với vòng lặp phản hồi kín.
- Phối hợp lai ghép giữa điều khiển cổ điển và AI: Các tác giả nên kết hợp cấu trúc lai giữa điều khiển cổ điển và AI. Mạng nơ-ron đóng vai trò bù sai số hoặc tinh chỉnh động $, $, $ cho bộ PID.

---

### 7.9. Khoảng trống 9: Dấu chân carbon và tiêu hao năng lượng tính toán của AI (Carbon and Computational Energy Footprint of AI)

#### 7.9.1. Gánh nặng tiêu thụ điện năng từ huấn luyện mô hình sâu và suy luận biên
- Tiêu hao năng lượng trong giai đoạn huấn luyện: Huấn luyện mô hình sâu như LSTM hoặc Transformer tiêu tốn nhiều điện năng. Quá trình xử lý các tập dữ liệu SCADA khổng lồ tạo ra phát thải lớn.
- Tiêu hao năng lượng trong giai đoạn suy luận liên tục: Hoạt động suy luận thời gian thực trên phần cứng biên (Edge AI) tiêu thụ điện liên tục. Thiết bị tại trạm đòi hỏi nguồn năng lượng 24/7.
- Nghịch lý môi trường của AI trong ngành xử lý nước: Mục tiêu của MBR thông minh là tiết kiệm năng lượng và giảm phát thải. Dấu chân carbon của phần cứng AI có thể làm triệt tiêu lợi ích môi trường này.
- Tác động nhiệt và làm mát trung tâm dữ liệu: Nhu cầu tản nhiệt cho các cụm máy chủ phân tích dữ liệu cục bộ góp phần gia tăng phát thải gián tiếp.

#### 7.9.2. Minh bạch hóa năng lượng tính toán để bảo toàn mục tiêu giảm phát thải của MBR
- Đo lường và báo cáo điện năng tính toán: Nghiên cứu MBR ứng dụng AI cần công bố điện năng huấn luyện mô hình. Tác giả cũng phải đo lường năng lượng tiêu hao trên mỗi lượt dự đoán (kWh/prediction).
- Đánh giá cân bằng năng lượng thực (Net Energy Balance): Nghiên cứu cần lập phương trình cân bằng năng lượng thực tế. Phương trình so sánh điện năng sục khí tiết kiệm với điện năng hệ thống AI tiêu thụ:
  $$\Delta E_{\text{net}} = E_{\text{saved, aeration}} - (E_{\text{train}} + E_{\text{inference}} + E_{\text{infrastructure}})$$
- Phát triển mô hình học máy tiết kiệm năng lượng (Green AI): Kỹ sư cần ưu tiên giải pháp học máy xanh (Green AI). Các kỹ thuật gồm lượng tử hóa mô hình (quantization) và cắt tỉa trọng số (pruning) để giảm công suất tính.
- Đánh giá vòng đời phát thải (LCA) cho các giải pháp số: Đơn vị nghiên cứu cần đưa hạ tầng công nghệ vào đánh giá vòng đời (LCA). Phương pháp này lượng hóa toàn diện phát thải của nhà máy MBR thông minh.

## Chương 8: Kết luận Tổng hợp, Lộ trình Triển khai Thực tế và Tổng quan Tài liệu Tham khảo (Conclusions, Operational Implementation Roadmap & Foundational Reference Synthesis)

### 8.1 Tổng kết 4 mục tiêu nghiên cứu và Đánh giá thực trạng công nghệ (Synthesis of Four Review Objectives & State-of-the-Art Assessment)

#### 8.1.1 Mục tiêu 1: Đánh giá năng lực các thuật toán ML trong dự đoán tắc nghẽn màng và TMP (ML Performance in Membrane Fouling & TMP Prediction)
- Dự báo tắc nghẽn màng và áp suất TMP đạt độ chính xác cao. Độ tin cậy này tăng mạnh trong giai đoạn nghiên cứu gần đây.
- Các mô hình dựa trên hạt nhân và mô hình học máy tập hợp đạt hệ số xác định $R^2 = 0.85 - 0.99$.
- Mô hình Least Squares Support Vector Machines (LSSVM) đạt $R^2 = 0.990$ trên dữ liệu phòng thí nghiệm và pilot.
- Thuật toán Random Forest (RF) vượt trội hơn mạng nơ-ron nhân tạo truyền thống (ANN) trên dữ liệu vận hành thực tế.
- Nghiên cứu của Kovacs et al. [26] kiểm chứng RF trên hơn 80.000 mẫu dữ liệu SCADA công nghiệp.
- Mô hình RF đạt $R^2 = 0.927 - 0.996$ trên dữ liệu trạm xử lý nước thải. Chỉ số $\text{RMSE}$ đạt $0.264 - 0.904\text{ kPa}$.
- Kiểm chứng lịch sử trên dữ liệu SCADA lưu trữ không tương đương với kiểm chứng vận hành thực tế.
- Dữ liệu trực tuyến luôn gặp hiện tượng trôi dạt cảm biến. Nhiễu ngẫu nhiên và độ trễ truyền dữ liệu cũng gây cản trở.
- Chưa có nghiên cứu nào kiểm chứng ML điều khiển vòng kín trên nhà máy MBR đang hoạt động trực tiếp.
- Nhà máy phải kiểm chuẩn mô hình theo từng trạm cụ thể trước khi triển khai công nghiệp.
- Trạm xử lý cần lập các rào chắn quản trị an toàn để chống tràn bể hoặc rách màng.

#### 8.1.2 Mục tiêu 2: Đánh giá vai trò của XAI trong việc giải mã cơ chế vật lý - sinh học MBR (XAI Frameworks for Mechanistic Process Transparency)
- Các công cụ XAI loại bỏ tính chất "hộp đen" của các mô hình học máy.
- Khung giải thích SHAP dựa trên nền tảng toán học của lý thuyết trò chơi hợp tác.
- Phân tích SHAP xác định bốn biến số chi phối hàng đầu: MLSS, SRT, HRT và cường độ sục khí ($J_{\text{air}}$).
- Kết quả SHAP phù hợp với các quy luật động học vi sinh. Kết quả này cũng tương thích với hiện tượng truyền khối màng.
- Phân tích SHAP cung cấp bằng chứng kỹ thuật có thể hành động trực tiếp cho kỹ sư vận hành.
- SHAP giải thích áp suất lọc tăng vọt do tích tụ polyme ngoại bào EPS và chất vi sinh hòa tan SMP.
- Phương pháp LIME xây dựng mô hình tuyến tính cục bộ. Mô hình này giúp giải thích nhanh các dự báo tức thời.
- Biểu đồ phụ thuộc riêng phần PDP chỉ rõ các ngưỡng vận hành phi tuyến trong bể phản ứng màng.
- Phân tích PDP phát hiện ngưỡng tới hạn $\text{MLSS} = 10 - 12\text{ g/L}$. Bùn vượt ngưỡng này sẽ tăng độ nhớt đột ngột.
- Tính minh bạch từ XAI đáp ứng các yêu cầu kiểm toán nghiêm ngặt từ cơ quan quản lý nhà nước.

#### 8.1.3 Mục tiêu 3: Xác minh bằng chứng thực nghiệm về tối ưu hóa năng lượng vận hành (Empirical Evidence of Operational Energy Optimization)
- Tiêu thụ năng lượng của MBR dao động từ $0.4$ đến $1.5\text{ kWh/m}^3$. Mức này cao gấp hai lần công nghệ bùn hoạt tính truyền thống.
- Sục khí màng và sục khí sinh học chiếm 60% đến 75% tổng điện năng của trạm xử lý.
- Điều khiển phản hồi dựa trên mô hình cơ chế đã giảm 20% điện sục khí tại trạm thực tế.
- Công trình của Sun et al. [59] thiết lập chuẩn đối sánh thực nghiệm với mức tiêu thụ $0.45\text{ kWh/m}^3$.
- Đa số nghiên cứu tối ưu hóa năng lượng bằng ML mới chỉ thực hiện trên mô phỏng số.
- Chưa có công trình nào kiểm chứng mức tiết kiệm năng lượng trực tiếp từ ML tại trạm thực tế.
- Khoảng cách giữa mô phỏng và kiểm chứng thực nghiệm tại trạm MBR là khoảng trống lớn nhất.
- Tối ưu hóa khí cấp bằng ML cần gắn kèm ràng buộc an toàn để tránh gây tắc màng nặng.

#### 8.1.4 Mục tiêu 4: Định hình kiến trúc Digital Twin 3 bậc trưởng thành và tích hợp XAI (Digital Twin Architecture & XAI Integration Framework)
- Khung kiến trúc Digital Twin tích hợp mô hình cơ chế bùn hoạt tính ASM với mô hình học máy.
- Kiến trúc Digital Twin trong công nghệ MBR gồm 3 bậc trưởng thành công nghệ.
- Bậc I (Tier I - Descriptive DT) thu thập dữ liệu SCADA trực tuyến. Hệ thống giám sát trạng thái và phát cảnh báo vượt ngưỡng.
- Bậc II (Tier II - Predictive DT) dự báo trước 12 đến 72 giờ về TMP, lưu lượng và chất lượng nước.
- Bậc III (Tier III - Prescriptive DT) tự động tính toán phương án tối ưu và điều khiển vòng kín.
- Việc nhúng module XAI vào kiến trúc ra quyết định của Digital Twin là yêu cầu chức năng bắt buộc.
- Module XAI xây dựng niềm tin cho kỹ sư vận hành trước khi chuyển giao quyền điều khiển tự hành.
- Chưa có trạm MBR thực tế nào trên thế giới đạt đến mức độ triển khai Digital Twin Bậc III tích hợp XAI.
- Sự kết hợp giữa dự báo ML, minh bạch hóa XAI và mô phỏng số tạo nên lộ trình khả thi nhất.

#### 8.1.5 Tổng hợp chín khoảng trống nghiên cứu then chốt và Tầm nhìn hội tụ (Nine Critical Research Gaps & Convergence Vision)
- Khoảng trống 1: Khan hiếm các bộ dữ liệu đối chuẩn mở thu thập từ nhiều nhà máy MBR thực tế.
- Khoảng trống 2: Thiếu công cụ định lượng độ bất định đã hiệu chuẩn trong dự báo vận hành.
- Khoảng trống 3: Chưa có bằng chứng triển khai Digital Twin Bậc III tại trạm xử lý quy mô lớn.
- Khoảng trống 4: Cảm biến thông thường không đo kịp biến động thành phần nước thải đầu vào.
- Khoảng trống 5: Thiếu khung pháp lý và quy chuẩn kỹ thuật công nhận các quyết định tự động từ AI.
- Khoảng trống 6: Báo cáo thiếu minh bạch về chi phí phát triển và bảo trì mô hình học máy.
- Khoảng trống 7: Thiếu hụt nhân lực có kỹ năng kết hợp giữa kỹ thuật môi trường nước và MLOps.
- Khoảng trống 8: Thiếu đối chuẩn hệ thống giữa giải thuật AI với bộ điều khiển PID hoặc Fuzzy.
- Khoảng trống 9: Chưa đo lường dấu chân carbon và điện năng tính toán của mô hình học sâu.
- Lộ trình phát triển yêu cầu sự hội tụ của ba trụ cột: dự báo ML, giải thích XAI và Digital Twin.
- Ngành nước cần đầu tư đồng bộ vào hạ tầng dữ liệu mở và liên minh hợp tác đa ngành.

### 8.2 Lộ trình chuyển đổi từ Nghiên cứu sang Triển khai Công nghiệp (Operational Transition Roadmap)

#### 8.2.1 Giai đoạn 1: Chuẩn hóa dữ liệu SCADA và xây dựng mô hình dự báo ngoại tuyến (Offline Predictive DT)
- Doanh nghiệp thiết lập hạ tầng thu thập SCADA với chu kỳ lấy mẫu từ 1 phút đến 5 phút.
- Quy trình tiền xử lý dữ liệu giúp loại bỏ nhiễu, điền giá trị khuyết và bù trôi cảm biến áp suất.
- Trạm lắp đặt máy quang phổ UV-Vis và cảm biến huỳnh quang 2D để theo dõi chất lượng nước đầu vào.
- Nhóm kỹ thuật xây dựng mô hình Random Forest hoặc LSTM ngoại tuyến để dự báo áp suất TMP.
- Tập dữ liệu được phân chia theo chuỗi thời gian liên tục nhằm ngăn chặn hiện tượng rò rỉ thông tin.
- Mô hình tích hợp công cụ định lượng độ bất định đã hiệu chuẩn để cung cấp khoảng tin cậy 95%.
- Kỹ sư kiểm định chéo mô hình qua các mùa thời tiết để đánh giá khả năng thích ứng tải lượng.

#### 8.2.2 Giai đoạn 2: Tích hợp XAI thời gian thực và phát triển trợ lý đề xuất (Human-in-the-loop Advisory DT)
- Kỹ sư tích hợp module TreeSHAP tốc độ cao trực tiếp vào luồng dữ liệu của trạm xử lý.
- Thời gian tính toán giá trị SHAP dưới 1 giây cho mỗi chu kỳ nhằm đảm bảo tính trực tuyến.
- Giao diện người - máy hiển thị trực quan các yếu tố đóng góp hàng đầu vào nguy cơ tắc màng.
- Hệ thống phát hiện sớm hiện tượng nén bánh bùn dựa trên giá trị SHAP của nồng độ MLSS.
- Nhóm vận hành dùng biến động giá trị SHAP để phát hiện hiện tượng trôi dạt phân phối dữ liệu.
- Kỹ sư vận hành giữ quyền phê duyệt tối cao. AI đề xuất khuyến nghị, con người ra quyết định cuối cùng.
- Nhà máy đào tạo kỹ năng kép về công nghệ xử lý nước và phân tích biểu đồ AI cho nhân sự.

#### 8.2.3 Giai đoạn 3: Triển khai điều khiển tự hành vòng kín có giám sát (Safe Closed-loop Autonomous DT)
- Digital Twin gửi tín hiệu điều khiển trực tiếp đến bộ điều khiển logic lập trình được PLC.
- Trạm giới hạn phạm vi điều khiển tự hành trong dải hẹp, như lưu lượng khí sục màng trong khoảng $\pm 10\%$.
- Hệ thống kết hợp mô hình học máy với bộ điều khiển MPC để ổn định áp suất qua màng.
- Hệ thống tự động điều chỉnh chu kỳ rửa ngược khí và xả bùn theo tốc độ bám bẩn dự báo.
- Vòng điều khiển khóa chặt nồng độ COD, amoni ($NH_4^+$) và tổng photpho trong giới hạn quy chuẩn.
- Hệ thống tự ngắt quyền điều khiển tự hành khi các biến số tiệm cận ngưỡng ranh giới kỹ thuật.

#### 8.2.4 Cơ chế quản trị an toàn và tuân thủ vận hành (Governance Safeguards)
- Trạm lắp đặt hệ thống ngắt an toàn cơ học độc lập hoàn toàn với phần mềm trí tuệ nhân tạo.
- Kỹ sư sử dụng nút bấm khẩn cấp và van xả áp cơ học để chuyển ngay về chế độ bằng tay.
- Hệ thống lưu trữ nhật ký kiểm toán bất biến trên cơ sở dữ liệu phân tán chống chỉnh sửa.
- Nhật ký ghi lại từng khuyến nghị của AI, giá trị SHAP tương ứng và danh tính kỹ sư phê duyệt.
- Hệ thống tuân thủ toàn diện tiêu chuẩn an ninh mạng công nghiệp cho cơ sở hạ tầng nước thiết yếu.
- Đơn vị vận hành xây dựng báo cáo giải trình thuật toán phục vụ thanh tra môi trường định kỳ.

### 8.3 Tổng hợp và Đánh giá các Nguồn Tài liệu Tham khảo Nền tảng (Foundational Reference Synthesis)

#### 8.3.1 Các nhóm tác giả và công trình nghiên cứu tiên phong (Pioneering Authors & Milestone Studies)
- Simon Judd (2008, 2010): Xuất bản cuốn sách "The MBR Book" [1] và bài báo tổng quan nền tảng [5]. Tác giả xác lập tiêu chuẩn thiết kế, định mức năng lượng và mô hình chi phí vòng đời trạm MBR.
- Fangang Meng et al. (2009, 2017): Công bố hai bài tổng quan trên tạp chí *Water Research* [8, 11]. Công trình làm rõ cơ chế tắc màng, tương tác sinh học và động học hình thành EPS cùng SMP.
- David J. Kovacs et al. (2022): Nhóm tác giả kiểm chứng Random Forest trên hơn 80.000 mẫu SCADA thực tế [26]. Công trình công bố trên *Journal of Membrane Science* và phân tích độ bất định dự báo.
- Jian Sun et al. (2016): Công bố trên *Water Research* về mức giảm 20% điện năng sục khí tại trạm lớn [59]. Nhóm nghiên cứu kết hợp mô phỏng động học quá trình với điều khiển phản hồi nồng độ oxy hòa tan DO.
- B. Verrecht et al. (2008, 2010): Tiên phong xây dựng mô hình tiêu thụ năng lượng sục khí màng sợi rỗng ngập nước [56]. Nhóm tác giả hạch toán chi phí đầu tư và vận hành cho nhà máy MBR lớn [14].
- Kathryn B. Newhart et al. (2019): Xuất bản bài tổng quan toàn diện trên *Water Research* [17]. Tác giả phân tích dữ liệu và ứng dụng các thuật toán học máy trong nhà máy xử lý nước thải.
- P. Krzeminski et al. (2017): Xuất bản nghiên cứu tổng quan then chốt trên *Journal of Membrane Science* [15]. Nghiên cứu phân tích giải pháp tiết kiệm năng lượng, kiểm soát tắc màng và đánh giá chu kỳ sống LCA.
- M. Henze, W. Gujer et al. (1999, 2006): Nhóm chuyên gia IWA xây dựng các mô hình bùn hoạt tính ASM1, ASM2d và ASM3 [34, 35]. Đây là nền tảng động học vi sinh cốt lõi cho mọi kiến trúc Digital Twin MBR.
- S.M. Lundberg và S.-I. Lee (2017, 2020): Hai tác giả phát triển khung lý thuyết SHAP thống nhất [52]. Tác giả giới thiệu thuật toán TreeSHAP tối ưu hóa trên tạp chí *Nature Machine Intelligence* [53].
- M.T. Ribeiro et al. (2016, 2018): Nhóm tác giả sáng lập phương pháp giải thích mô hình cục bộ LIME [55]. Nhóm phát triển thuật toán neo Anchors cho các bài toán phân loại phức tạp [27].
- Cynthia Rudin (2019): Tác giả công bố bài xã luận trên *Nature Machine Intelligence* [51]. Bài viết phản đối dùng mô hình hộp đen giải thích hậu nghiệm trong các quyết định rủi ro cao.

#### 8.3.2 Phân bố ấn phẩm trên các tạp chí và diễn đàn khoa học hàng đầu (Leading Journals & Venues Distribution)
- Tạp chí *Water Research* (IWA / Elsevier) dẫn đầu với 10 ấn phẩm nền tảng [8, 11, 14, 17, 36, 40, 56, 57, 59]. Tạp chí công bố các nghiên cứu về mô hình hóa bùn hoạt tính ASM và thử nghiệm năng lượng thực tế.
- Tạp chí *Journal of Membrane Science* (Elsevier) đóng góp 7 ấn phẩm then chốt [4, 6, 9, 10, 15, 26, 42]. Diễn đàn chuyên sâu về động học lọc màng, rửa hóa chất CIP và kiểm chứng học máy trên dữ liệu SCADA.
- Tạp chí *Desalination* (Elsevier) công bố các công trình về màng thẩm thấu thuận FO-MBR và lọc nước tái sử dụng [41].
- Tạp chí *Bioresource Technology* (Elsevier) chuyên sâu về xử lý sinh học nước thải công nghiệp phức tạp và ứng dụng AI [3, 63].
- Tạp chí *Environmental Science & Technology* (ACS) xuất bản nghiên cứu dự báo tắc màng MBR bằng học máy giải thích được [50].
- Các tạp chí liên ngành (*Membranes*, *Sensors*, *Engineering*) công bố nghiên cứu mới về Digital Twin và chuẩn mực XAI [37, 60, 61, 65].

#### 8.3.3 Bảng tổng hợp các ấn phẩm nền tảng phân theo nhóm chuyên đề kỹ thuật (Structured Reference Categorization Table)

| Nhóm chuyên đề | Tác giả tiêu biểu | Năm | Tạp chí / NXB | Đóng góp kỹ thuật cốt lõi | Mã trích dẫn |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cơ chế tắc nghẽn và Động học MBR kinh điển** | Judd, S. | 2010 | Elsevier (Book) | Xác lập nguyên lý toàn diện, thông số thủy lực và phân tích kinh tế MBR | [1] |
| | Meng et al. | 2009, 2017 | Water Research | Cơ chế bám bẩn bề mặt, tương tác sinh học - màng và động học EPS/SMP | [8, 11] |
| | Le-Clech et al. | 2006 | J. Membr. Sci. | Tổng quan cơ chế tắc nghẽn màng trong xử lý nước thải bằng MBR | [4] |
| | Drews, A. | 2010 | J. Membr. Sci. | Đặc trưng hóa hiện tượng tắc màng, nguyên nhân và biện pháp khắc phục | [9] |
| | Wang et al. | 2014 | J. Membr. Sci. | Động học làm sạch màng và quy trình tẩy rửa hóa chất trong trạm MBR | [10] |
| | Henze et al. | 2006 | IWA Publishing | Hệ mô hình bùn hoạt tính ASM1, ASM2d và ASM3 cho xử lý sinh học | [34] |
| | Fenu et al. | 2010 | Water Research | Ứng dụng mô hình ASM cho MBR và hiệu chỉnh các đặc thù công nghệ màng | [40] |
| **Học máy trong Dự báo Tắc nghẽn và Vận hành** | Kovacs et al. | 2022 | J. Membr. Sci. | Kiểm chứng Random Forest trên 80.000 mẫu SCADA và định lượng độ bất định | [26] |
| | Newhart et al. | 2019 | Water Research | Tổng quan ứng dụng phân tích dữ liệu và học máy trong nhà máy xử lý nước thải | [17] |
| | Kamali et al. | 2021 | Chem. Eng. J. | Ứng dụng trí tuệ nhân tạo như công cụ bền vững trong xử lý nước MBR | [16] |
| | Schmitt & Do | 2017, 2018 | ESPR / BEJ | Ứng dụng mạng nơ-ron ANN dự báo tắc nghẽn màng trong MBR thiếu khí - hiếu khí | [24, 25] |
| | Viet & Jang | 2021 | J. Environ. Chem. Eng. | Mô hình học máy dự báo hiệu năng lọc và tắc màng trong hệ thống OMBR | [22] |
| | Hamedi et al. | 2019 | Chem. Eng. Res. Des. | Công cụ xác định dựa trên AI để nghiên cứu hiện tượng tắc màng MBR | [42] |
| | Frontistis et al. | 2023 | Environments | Hiện trạng, thách thức và triển vọng triển khai học máy trong hệ MBR | [47] |
| | Zhu et al. | 2025 | Environ. Sci. Technol. | Dự báo tắc nghẽn màng MBR ngập nước quy mô trạm thực tế bằng học máy | [50] |
| | Liang et al. | 2025 | Processes | Khung dự báo tắc màng kết hợp kỹ thuật trích xuất đặc trưng và XAI | [49] |
| **Trí tuệ Nhân tạo có thể Giải thích được (XAI)** | Lundberg & Lee | 2017, 2020 | NeurIPS / Nat. Mach. Intell. | Khung lý thuyết SHAP thống nhất và thuật toán TreeSHAP tối ưu hóa | [52, 53] |
| | Ribeiro et al. | 2016, 2018 | ACM KDD / AAAI | Phương pháp giải thích cục bộ LIME và thuật toán neo Anchors | [27, 55] |
| | Rudin, C. | 2019 | Nat. Mach. Intell. | Nguyên lý phản đối hộp đen và ưu tiên mô hình tự giải thích cho hạ tầng rủi ro | [51] |
| | Barredo et al. | 2020 | Inf. Fusion | Phân loại học, cơ hội và thách thức của XAI hướng tới AI có trách nhiệm | [28] |
| | Adadi & Berrada | 2018 | IEEE Access | Khảo sát tổng quan về các phương pháp giải thích mô hình hộp đen AI | [29] |
| | Leichtmann et al. | 2023 | Comput. Hum. Behav. | Tác động của XAI đến niềm tin và hành vi con người trong việc ra quyết định rủi ro | [64] |
| | Goncalves & Correia | 2025 | J. Cybersecur. Priv. | Khung kỹ thuật XAI đáp ứng các yêu cầu minh bạch pháp lý và GDPR | [65] |
| | Sheik et al. | 2025 | Eng. Appl. Artif. Intell. | Ứng dụng XAI trong các nhà máy xử lý nước thải sinh học và góc nhìn tương lai | [66] |
| | Teixeira et al. | 2025 | Springer (Conf.) | Phát hiện trôi dạt dữ liệu bằng SHAP để tái huấn luyện mô hình thông minh | [67] |
| **Kiến trúc Digital Twin và Tối ưu hóa Năng lượng** | Sun et al. | 2016 | Water Research | Cắt giảm 20% điện sục khí qua mô phỏng quá trình và áp dụng tại trạm lớn | [59] |
| | Verrecht et al. | 2008, 2010 | Water Research | Mô hình tiêu thụ năng lượng sục khí và hạch toán chi phí trạm MBR sợi rỗng | [14, 56] |
| | Krzeminski et al. | 2017 | J. Membr. Sci. | Tổng quan tiết kiệm năng lượng, kiểm soát tắc màng và đánh giá chu kỳ sống LCA | [15] |
| | Maere et al. | 2011 | Water Research | Mô hình mô phỏng chuẩn BSM-MBR so sánh chiến lược điều khiển và vận hành | [36] |
| | Wang et al. | 2024 | Engineering | Đánh giá kỹ thuật về kiến trúc Digital Twin trong xử lý nước thải | [37] |
| | Ghorbani Bam et al. | 2025 | Water | Ứng dụng Digital Twin trong ngành nước và tổng quan các thách thức triển khai | [60] |
| | Rodríguez-Alonso et al. | 2024 | Sensors | Nền tảng Digital Twin cho nhà máy xử lý nước sử dụng kiến trúc microservices | [61] |
| | Xu & Liu | 2025 | Water | Tối ưu hóa thông số vận hành và kiến trúc điều khiển MBR tích hợp AI | [62] |
| | Wei et al. | 2025 | Bioresour. Technol. | Dự báo nitơ và phân tích cơ chế xử lý nước mặn bằng học máy giải thích được | [63] |
