## 4. Ý nghĩa thực tiễn và triển vọng tương lai (Implications and Outlook)

### 4.1 Khắc phục rào cản chi phí và tối ưu hóa giám sát bám bẩn màng
- Giải quyết bài toán khan hiếm dữ liệu sinh hóa chuyên sâu:
  - Đo đạc thông số vi sinh hòa tan (SMP) và polyme ngoại bào (EPS) tốn nhiều thời gian.
  - Phân tích EPS carbohydrate (EPSc) và EPS protein (EPSp) đòi hỏi quy trình chiết tách nhiệt hóa học phức tạp.
  - Các trạm MBR quy mô pilot hoặc trạm công nghiệp nhỏ thường thiếu ngân sách và nhân lực phân tích định kỳ.
  - Phương pháp học chuyển giao (Transfer Learning) giải quyết rào cản chi phí này.
  - Mô hình chuyển giao tri thức từ trạm nguồn giàu dữ liệu sang trạm đích thiếu dữ liệu.
  - Trạm đích không cần xây dựng cơ sở dữ liệu bám bẩn lại từ đầu.
- Tín hiệu quang phổ thay thế trực tuyến (Surrogate Fingerprints):
  - Phân tích ngoại tuyến các biến EPSc và EPSp gây ra độ trễ thời gian lớn.
  - Nhóm nghiên cứu đề xuất sử dụng tín hiệu quang phổ trực tuyến làm biến thay thế (surrogate markers).
  - Quang phổ tử ngoại - khả kiến (UV-vis) cung cấp thông tin liên tục về chất hữu cơ hòa tan.
  - Bản đồ huỳnh quang kích thích - phát xạ (EEM) ghi nhận nhanh các nhóm chất giống protein và humic [57].
  - Các dấu vân tay quang phổ này cho phép mô hình học máy tự thích ứng với biến động chất lượng nước theo thời gian thực.

### 4.2 Ứng dụng điều khiển dự báo cấp tiến và bản sao số (Digital Twin)
- Hệ thống điều khiển dự báo cấp tiến (Feedforward Control):
  - Mô hình LSTM tinh chỉnh (LSTM-FT) dự báo chính xác áp suất xuyên màng TMP trước nhiều giờ hoặc nhiều ngày.
  - Vận hành viên chủ động điều chỉnh cường độ sục khí màng trước khi áp suất tăng vọt.
  - Hệ thống tự động tối ưu hóa chu kỳ hút lọc và rửa ngược định kỳ.
  - Điều khiển cấp tiến triệt tiêu độ trễ phản hồi so với phương pháp điều khiển hồi tiếp truyền thống (Feedback Control).
- Kiến trúc bản sao số (Digital Twin) và giám sát thông minh IoT:
  - Bản sao số mô phỏng liên tục quá trình tích tụ lớp bánh bùn (cake layer) trên bề mặt màng.
  - Cảm biến IoT truyền dữ liệu vận hành gồm lưu lượng màng ($J$), TMP, oxy hòa tan (DO), pH, MLSS và nhiệt độ.
  - Thuật toán AI phân tích xu hướng tích lũy trở lực lọc và phát hiện sớm hiện tượng bám bẩn bất thường.
  - Hệ thống hỗ trợ ra quyết định xác định thời điểm tẩy rửa hóa chất tại chỗ (CIP) tối ưu (Hình S13).
  - Quy trình vận hành tối ưu giúp tiết kiệm năng lượng sục khí, giảm hóa chất tẩy rửa và kéo dài tuổi thọ màng.
- Khuyến nghị tần suất lấy mẫu tối thiểu cho các trạm pilot mới:
  - Giai đoạn khởi động trạm mới chỉ cần thu thập một chuỗi mẫu hóa lý ngắn hạn ghép cặp.
  - Tỷ lệ tinh chỉnh $40\%$ tương ứng với khoảng 16 đến 20 điểm đo thực nghiệm đầy đủ.
  - Sau khi nạp đủ lượng dữ liệu nhỏ này, mô hình hoàn thành quá trình tái hiệu chuẩn trọng số.
  - Sau giai đoạn tinh chỉnh, hệ thống chủ yếu dựa vào các cảm biến vận hành trực tuyến sẵn có để dự báo dài hạn.

### 4.3 Giới hạn hiện tại và định hướng nghiên cứu mở rộng
- Khoảng cách quy mô giữa hệ thống pilot và nhà máy xử lý nước thải quy mô thực tế (Full-Scale MBR):
  - Nghiên cứu hiện tại phát triển trên 4 hệ thống MBR quy mô pilot với điều kiện vận hành tương đối ổn định.
  - Tại nhà máy quy mô đầy đủ, thủy lực dòng chảy và phân bố bọt khí sục thay đổi theo không gian bể lọc [58].
  - Biến động tải trọng hữu cơ và lưu lượng nước thải đô thị biến thiên mạnh hơn so với trạm pilot.
  - Mối quan hệ tiền huấn luyện từ trạm pilot có thể chưa phản ánh hết động học bám bẩn phức tạp ở quy mô thương mại.
  - Nhóm tác giả kiến nghị mở rộng kiểm thực mô hình trên các tập dữ liệu lớn hơn từ nhiều vùng địa lý khác nhau.
- Đóng góp của bám bẩn vô cơ và tính chưa toàn diện của tập đặc trưng:
  - Hệ số xác định của mô hình đích đạt $R^2 = 0.89$, chưa đạt mức tuyệt đối ($1.00$).
  - Kết quả tẩy rửa hóa chất CIP tại trạm đích cho thấy sự hiện diện rõ nét của bám bẩn vô cơ chứa sắt (Fe fouling).
  - Tập dữ liệu đầu vào hiện tại tập trung chủ yếu vào các hợp chất hữu cơ sinh học (EPS và SMP).
  - Tập biến này chưa bao gồm nồng độ ion kim loại tự do ($\text{Fe}^{3+}$, $\text{Ca}^{2+}$, $\text{Mg}^{2+}$) và độ kiềm.
  - Bổ sung các chỉ số vô cơ sẽ giúp nâng cao độ chính xác dự báo khi nước thải đầu vào có nồng độ muối khoáng cao.
- Phát triển mô hình lai vật lý - trí tuệ nhân tạo (Hybrid Physical-AI Models):
  - Các mô hình thuần dữ liệu (data-driven) dễ mất tính khái quát khi gặp các sự cố quá tải đột ngột.
  - Hướng nghiên cứu tiếp theo sẽ kết hợp phương trình trở lực màng mắc nối tiếp (resistance-in-series) với mạng LSTM.
  - Mô hình vật lý cung cấp khung ràng buộc bảo toàn vật chất và thủy lực màng.
  - Mạng nơ-ron học các phi tuyến phức tạp sinh ra từ tương tác vi sinh và hóa học nước thải.
  - Cấu trúc lai giúp tăng độ tin cậy và đảm bảo tính giải thích vật lý vững chắc.

---

## 5. Kết luận then chốt của công trình (Key Conclusions)

### 5.1 Bốn kết luận khoa học và thực tiễn cốt lõi
- Kết luận 1: Tính khả thi của mô hình cơ sở tiền huấn luyện (LSTM-base) trên các trạm nguồn:
  - Nhóm tác giả xây dựng thành công mô hình cơ sở tiền huấn luyện trên dữ liệu tổng hợp từ 3 trạm MBR nguồn.
  - Phân tích SHAP chứng minh mô hình LSTM-base nắm bắt quy luật bám bẩn mang bản chất hóa lý rõ ràng.
  - Ba đặc trưng quyết định dự báo gồm EPSc, EPSp và SMPp, thay vì phụ thuộc đơn lẻ vào một biến vận hành.
  - Kết quả này phù hợp với các đặc tính chung của trạm nguồn: phổ huỳnh quang protein thơm, kích thước hạt bùn bông và xu hướng giữ lại SMP của màng lọc.
  - Mô hình LSTM-base tạo tiền đề tri thức vững chắc cho quá trình chuyển giao học máy sang các trạm mới.
- Kết luận 2: Vai trò của tỷ lệ tinh chỉnh (FT Ratio) và cơ chế hóa lý qua SHAP và LOFO:
  - Tinh chỉnh mô hình với tập dữ liệu nhỏ của trạm đích giúp cải thiện vượt bậc độ chính xác dự báo áp suất TMP.
  - Mô hình LSTM-FT đạt hệ số xác định $R^2 = 0.89$, $\text{RMSE} = 0.41\text{ kPa}$ và $\text{MAE} = 0.33\text{ kPa}$ ở mức $\text{FT} = 40\%$.
  - Phân tích SHAP và LOFO chỉ ra rằng biến EPSc tiếp tục đóng vai trò nền tảng bám bẩn ổn định.
  - Đồng thời, tầm quan trọng của biến EPSp tăng rõ rệt sau khi tinh chỉnh mô hình.
  - Sự thay đổi này phù hợp hoàn toàn với điều kiện nước thải giàu sắt ($10\text{--}30\text{ mg/L Fe}$) tại trạm đích.
  - Ion sắt liên kết mạnh với protein ngoại bào tạo thành lớp bám bẩn hữu cơ - vô cơ đặc thù.
- Kết luận 3: Khả năng thích ứng xuyên kịch bản (Cross-Scenario Adaptability) với nước thải công nghiệp:
  - Nhóm nghiên cứu thử nghiệm thành công mô hình trên trạm MBR xử lý nước thải công nghiệp hóa dầu và dược phẩm.
  - Khi chưa tinh chỉnh ($\text{FT} = 0\%$), mô hình nguồn hoàn toàn thất bại ($R^2 = -0.46$) do bản chất nước thải khác biệt sâu sắc.
  - Tinh chỉnh với tỷ lệ $\text{FT} = 40\%$ đưa hiệu năng mô hình lên mức xuất sắc với $R^2 = 0.90$ và $\text{MAE} = 0.54\text{ kPa}$.
  - Biến SMP protein (SMPp) vươn lên thành yếu tố dự báo quan trọng thứ hai, phản ánh sự phân hủy bùn do độc tính công nghiệp.
  - Biến EPSc vẫn duy trì vai trò dẫn đầu, khẳng định tính khái quát cao của khung học chuyển giao.
- Kết luận 4: Nền tảng ra quyết định kiểm soát bám bẩn có khả năng giải thích khoa học:
  - Nghiên cứu chứng minh tri thức bám bẩn chung có thể chuyển giao và tái hiệu chuẩn chính xác bằng lượng dữ liệu rất nhỏ.
  - Phân tích hóa lý độc lập biến quy trình thích ứng mô hình thành một hệ thống minh bạch, có cơ sở khoa học rõ ràng.
  - Công trình mở ra hướng tiếp cận mới trong việc dự báo TMP và hỗ trợ ra quyết định thông minh tại các trạm xử lý nước thải thiếu dữ liệu.

---

## 6. Đóng góp tác giả và thông tin mở rộng (Author Contributions and Extended Information)

### 6.1 Tuyên bố đóng góp của tác giả theo chuẩn CRediT
- Tác giả Xiaohang Han (Đồng tác giả thứ nhất):
  - Khởi xướng ý tưởng nghiên cứu (Conceptualization).
  - Quản lý và xử lý dữ liệu thực nghiệm (Data curation).
  - Phân tích dữ liệu định lượng (Formal analysis).
  - Thực hiện điều tra thực nghiệm (Investigation).
  - Phát triển phương pháp học chuyển giao (Methodology).
  - Lập trình kiến trúc mô hình học máy (Software).
  - Kiểm thực kết quả dự báo (Validation).
  - Xây dựng biểu đồ và đồ họa trực quan (Visualization).
  - Soạn thảo bản thảo gốc đầu tiên (Writing – original draft).
- Tác giả Liu Yang (Đồng tác giả thứ nhất):
  - Khởi xướng ý tưởng nghiên cứu (Conceptualization).
  - Quản lý và thẩm định dữ liệu (Data curation).
  - Phân tích dữ liệu định lượng (Formal analysis).
  - Thực hiện điều tra thực nghiệm (Investigation).
  - Hoàn thiện phương pháp nghiên cứu (Methodology).
  - Lập trình và thử nghiệm thuật toán (Software).
  - Kiểm thực hiệu năng mô hình (Validation).
  - Trực quan hóa kết quả phân tích SHAP và LOFO (Visualization).
  - Soạn thảo bản thảo gốc đầu tiên (Writing – original draft).
- Tác giả Huan Qin:
  - Quản lý dữ liệu quan trắc trạm MBR (Data curation).
  - Điều tra và hỗ trợ thí nghiệm (Investigation).
- Tác giả Shujuan Huang:
  - Quản lý dữ liệu hóa lý (Data curation).
  - Điều tra và theo dõi phân tích mẫu (Investigation).
- Tác giả Han Zhang:
  - Quản lý tập dữ liệu phân tích màng (Data curation).
  - Điều tra và thu thập thông số vận hành (Investigation).
- Tác giả Boyan Xu (Tác giả liên hệ / Giám sát):
  - Khởi xướng và định hướng ý tưởng khoa học (Conceptualization).
  - Huy động các nguồn tài trợ nghiên cứu (Funding acquisition).
  - Quản trị dự án và điều phối nhóm nghiên cứu (Project administration).
  - Giám sát toàn diện quá trình nghiên cứu (Supervision).
  - Đọc phản biện, rà soát và chỉnh sửa hoàn thiện bản thảo (Writing – review & editing).
- Tác giả How Yong Ng (Giáo sư, Tác giả liên hệ / Giám sát):
  - Khởi xướng khung lý thuyết và định hướng ứng dụng (Conceptualization).
  - Huy động nguồn tài trợ và cơ sở vật chất (Funding acquisition).
  - Định hướng và giám sát chuyên môn cao cấp (Supervision).
  - Phản biện chuyên sâu, rà soát và hoàn thiện bản thảo (Writing – review & editing).

### 6.2 Cam kết lợi ích, tài trợ và tính khả dụng của dữ liệu
- Tuyên bố xung đột lợi ích (Declaration of Competing Interests):
  - Nhóm tác giả khẳng định không có bất kỳ xung đột lợi ích tài chính hoặc quan hệ cá nhân nào ảnh hưởng đến công trình nghiên cứu này.
- Khung tài trợ nghiên cứu (Acknowledgement):
  - Quỹ Học giả Thái Sơn tỉnh Sơn Đông (Taishan Scholar Foundation of Shandong Province), mã số tài trợ `tsqn202312222`.
  - Quỹ Khoa học Tự nhiên Quốc gia Trung Quốc (National Natural Science Foundation of China - NSFC), mã số tài trợ `42406133`.
  - Quỹ Nghiên cứu Cơ bản và Nghiên cứu Cơ bản Ứng dụng tỉnh Quảng Đông (Guangdong Province Foundation), mã số tài trợ `2023A1515110786`.
  - Nhóm tác giả gửi lời cảm ơn trân trọng tới các thành viên nhóm nghiên cứu của Giáo sư How Yong Ng tại Singapore (bao gồm Wei Hao Loh, David Imanuel Tanaka và các cộng sự).
  - Các cộng sự đã tích cực hỗ trợ thu thập dữ liệu vận hành từ các trạm MBR quy mô pilot.
  - Toàn bộ dữ liệu chỉ sử dụng duy nhất cho mục đích mô phỏng và mô hình hóa trí tuệ nhân tạo.
  - Mọi thông tin định danh nhạy cảm hoặc mang tính bảo mật đều được ẩn danh và mã hóa trước khi phân tích.
- Khả dụng của dữ liệu (Data Availability):
  - Dữ liệu nghiên cứu sẵn sàng được cung cấp khi nhận được yêu cầu hợp lý gửi trực tiếp đến tác giả liên hệ.
- Dữ liệu bổ sung trực tuyến (Supplementary Data):
  - Dữ liệu và hình ảnh bổ sung (Phụ lục từ Hình S1 đến S13 và các Bảng S1 đến S8) được lưu trữ tại cổng thông tin Elsevier.
  - Đường dẫn truy cập định danh số: `https://doi.org/10.1016/j.memsci.2026.126065`.

### 6.3 Phân loại các tài liệu tham khảo cốt lõi của nghiên cứu
- Nhóm 1: Trí tuệ nhân tạo và học máy trong xử lý nước thải và bám bẩn MBR:
  - Niu et al. (2022) [2]: Tổng quan phân tích ứng dụng trí tuệ nhân tạo trong dự báo bám bẩn màng suốt 20 năm qua. Tạp chí *Water Research*.
  - Meng et al. (2017) [3]: Tổng quan cập nhật về cơ chế và biện pháp kiểm soát bám bẩn trong bể phản ứng sinh học màng. Tạp chí *Water Research*.
  - Xiao et al. (2019) [4]: Đánh giá hiện trạng và thách thức của các trạm MBR quy mô thương mại đầy đủ. Tạp chí *Bioresource Technology*.
  - Zhu et al. (2025) [7]: Ứng dụng học máy dự báo bám bẩn màng trong các nhà máy xử lý nước thải MBR đặt ngập. Tạp chí *Environmental Science & Technology*.
  - Kovacs et al. (2022) [8]: Dự báo bám bẩn màng và phân tích độ không đảm bảo bằng học máy tại nhà máy xử lý nước thải. Tạp chí *Journal of Membrane Science*.
  - Lai et al. (2025) [14]: Nguyên lý, phương pháp và hướng dẫn thực hành ứng dụng học máy trong nghiên cứu MBR. Tạp chí *Frontiers of Environmental Science & Engineering*.
  - Lai et al. (2026) [15]: Giám sát bám bẩn thông minh trong các công nghệ xử lý nước thải dựa trên màng lọc. Tạp chí *Nature Sustainability*.
- Nhóm 2: Học chuyển giao liên trạm và xử lý dữ liệu chuỗi thời gian môi trường:
  - Wang et al. (2026) [24]: Phá vỡ các ốc đảo dữ liệu bằng phương pháp mô hình hóa dựa trên chuyển giao tri thức giữa các nhà máy xử lý nước thải. Tạp chí *Process Safety and Environmental Protection*.
  - Cao et al. (2024) [53]: Khả năng chuyển giao của các mô hình học máy đối với nguồn nước ngầm ô nhiễm tự nhiên. Tạp chí *Environmental Science & Technology*.
  - Elahi et al. (2025) [25]: Khả năng tổng quát hóa và học chuyển giao trong dự báo vượt ngưỡng vi khuẩn chỉ thị tại các bãi biển. Tạp chí *Environmental Science & Technology*.
  - Chen et al. (2025) [36]: Tinh chỉnh mô hình LSTM phục vụ chuyển tiếp liền mạch trong mô hình hóa thủy văn từ tiền huấn luyện đến ứng dụng. Tạp chí *Environmental Modelling & Software*.
  - Ribeiro et al. (2018) [33]: Học chuyển giao kết hợp hiệu chỉnh mùa vụ phục vụ dự báo tiêu thụ năng lượng giữa các tòa nhà. Tạp chí *Energy and Buildings*.
- Nhóm 3: Cơ chế hóa lý của chất polyme ngoại bào (EPS) và sản phẩm vi sinh hòa tan (SMP):
  - Mannina et al. (2023) [17]: Mô hình hóa các quá trình sinh học trong hệ thống MBR tập trung vào vai trò của SMP và EPS. Tạp chí *Water Research*.
  - Lin et al. (2014) [46]: Tổng quan chuyên sâu về EPS trong MBR: đặc tính, vai trò bám bẩn và chiến lược kiểm soát. Tạp chí *Journal of Membrane Science*.
  - Poorasgari et al. (2015) [41]: Khả năng chịu nén của lớp bám bẩn bánh bùn trong các hệ thống MBR. Tạp chí *Journal of Membrane Science*.
  - Chen et al. (2017) [45]: Hành vi bám bẩn của SMP và EPS trong MBR kỵ khí ngập nước xử lý nước thải nồng độ thấp ở nhiệt độ phòng. Tạp chí *Journal of Membrane Science*.
  - Shen et al. (2015) [47]: Tác động của kích thước hạt bông bùn đến động học bám bẩn màng trong MBR ngập nước. Tạp chí *Chemical Engineering Journal*.
  - Ding et al. (2020) [51]: Khảo sát dài hạn hành vi bám bẩn màng trong MBR kỵ khí xử lý nước thải đô thị ở hai mức nhiệt độ. Tạp chí *Membranes*.
- Nhóm 4: Ảnh hưởng của ion sắt (Fe) và bám bẩn vô cơ:
  - Gao et al. (2024) [54]: Làm rõ vai trò của muối sắt clorua ($FeCl_3$) trong việc thu hồi cacbon từ nước thải đô thị nồng độ thấp và cơ chế tác động lên bông bùn. Tạp chí *Journal of Cleaner Production*.
  - Peng et al. (2022) [55]: Ảnh hưởng của các dạng và thành phần EPS khác nhau đến quá trình kết tụ bùn hạt hiếu khí. Tạp chí *Chemosphere*.
  - Su et al. (2025) [56]: Độ bền và tính ổn định của màng polyme trong các hệ thống MBR xử lý nước thải công nghiệp. Tạp chí *Journal of Environmental Chemical Engineering*.
- Nhóm 5: Giám sát quang phổ trực tuyến và vận hành MBR quy mô thực tế:
  - Lai et al. (2026) [57]: Điều khiển bám bẩn cấp tiến định hướng bởi cảnh báo sớm từ quang phổ huỳnh quang và UV trực tuyến phục vụ vận hành MBR tiết kiệm năng lượng. Tạp chí *Water Research*.
  - Delrue et al. (2011) [58]: Mối quan hệ giữa đặc tính bùn hoạt tính, điều kiện vận hành và bám bẩn trên hai nhà máy MBR quy mô thương mại đầy đủ. Tạp chí *Desalination*.
  - Takefuji (2026) [27]: Các giới hạn của phương pháp giải thích dựa trên SHAP trong ứng dụng môi trường và lọc màng. Tạp chí *Water Research*.
