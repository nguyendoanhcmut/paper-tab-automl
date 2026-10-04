## 5. Conclusions

- Mô hình cơ sở tiền huấn luyện ($\text{LSTM-base}$) cung cấp nền tảng dự đoán bám bẩn màng ($\text{membrane fouling}$) tin cậy và có khả năng giải thích cơ chế ($\text{mechanistically interpretable}$):
  - Mô hình được phát triển thông qua tiền huấn luyện ($\text{pretraining}$) trên dữ liệu thu thập từ 3 nhà máy nguồn giàu dữ liệu hơn ($\text{three data-richer source plants}$).
  - Phân tích $\text{SHAP}$ ($\text{SHapley Additive exPlanations}$) chỉ ra $\text{LSTM-base}$ học được các quy luật bám bẩn mang ý nghĩa vật lý thông qua các đặc trưng sinh hóa chủ đạo:
    - Carbohydrate của chất polyme ngoại bào ($\text{EPSc}$ - $\text{EPS carbohydrates}$).
    - Protein của chất polyme ngoại bào ($\text{EPSp}$ - $\text{EPS proteins}$).
    - Protein của sản phẩm vi sinh hòa tan ($\text{SMPp}$ - $\text{SMP proteins}$).
  - Mô hình không bị phụ thuộc vào một tín hiệu vận hành chi phối đơn lẻ ($\text{single dominant operational signal}$).
  - Các phát hiện được hỗ trợ bởi các đặc tính chung giữa các nhà máy nguồn:
    - Tín hiệu huỳnh quang dạng protein thơm của $\text{EPS}$ ($\text{EPS aromatic protein-like fluorescence}$).
    - Phân bố kích thước hạt bùn bông kết tụ ($\text{flocculated sludge particle-size distributions}$).
    - Xu hướng giữ lại ưu tiên $\text{SMP}$ của màng lọc ($\text{preferential retention of SMP by the membrane}$).
  - Kết quả khẳng định $\text{LSTM-base}$ cung cấp cơ sở tiền huấn luyện tin cậy và có thể diễn giải cơ chế cho quá trình học chuyển giao liên trạm ($\text{cross-plant transfer}$) tiếp theo.

- Quá trình tinh chỉnh ($\text{fine-tuning}$) nâng cao hiệu quả dự đoán áp suất xuyên màng ($\text{TMP}$ - $\text{Transmembrane Pressure}$) tại nhà máy đích xử lý nước thải sinh hoạt ($\text{domestic wastewater}$):
  - Mô hình LSTM tinh chỉnh ($\text{LSTM-FT}$) đạt hệ số xác định $R^2 = 0.89$ tại tỷ lệ tinh chỉnh $40\,\%$ ($\text{FT} = 40\,\%$).
  - Phân tích $\text{SHAP}$ và $\text{LOFO}$ ($\text{Leave-One-Feature-Out}$) chứng minh $\text{EPSc}$ tiếp tục duy trì vai trò chi phối, trong khi tầm quan trọng của $\text{EPSp}$ gia tăng sau khi tinh chỉnh.
  - Dưới điều kiện nước thải giàu sắt ($\text{Fe-enriched condition}$) tại nhà máy $\text{MBR}$ đích, sự gia tăng tầm quan trọng của $\text{EPSp}$ liên quan trực tiếp đến sự chuyển dịch sang các đặc tính $\text{EPS}$ giàu protein.
  - Cơ chế giải thích sự cải thiện độ chính xác dự đoán của quá trình tinh chỉnh:
    - Giữ lại nền tảng bám bẩn có thể chuyển giao lấy $\text{EPSc}$ làm trung tâm ($\text{transferable EPSc-centered fouling basis}$).
    - Tái hiệu chuẩn mô hình hướng tới các đặc tính $\text{EPS}$ giàu protein liên kết với sắt ($\text{Fe-associated, protein-enriched EPS characteristics}$) vốn liên kết mật thiết hơn với hiện tượng bám bẩn tại nhà máy đích.

- Thử nghiệm kiểm thực trên hệ thống $\text{MBR}$ xử lý nước thải công nghiệp ($\text{industrial wastewater MBR}$) khẳng định tính hiệu quả và độ ổn định xuyên kịch bản ($\text{cross-scenario stability}$):
  - Khung phương pháp luận duy trì tính hiệu quả dưới một bối cảnh bám bẩn màng khác biệt rõ rệt.
  - Khác với nhà máy đích xử lý nước thải sinh hoạt, $\text{SMPp}$ trở thành đặc trưng quan trọng thứ hai trong hệ thống $\text{MBR}$ công nghiệp.
  - Sự gia tăng đóng góp của $\text{SMPp}$ phản ánh tín hiệu $\text{SMP}$ dạng protein rõ nét hơn, gắn liền với các xáo trộn vận hành ($\text{operational disturbances}$) và hiện tượng phân hủy sinh khối ($\text{biomass decay}$).
  - Vị thế chi phối liên tục của $\text{EPSc}$ trong $\text{MBR}$ công nghiệp củng cố tính ổn định xuyên kịch bản của nền tảng bám bẩn có thể chuyển giao.
  - Mức phân bổ đóng góp tăng lên của $\text{SMPp}$ chứng minh quá trình tinh chỉnh có khả năng tái cân bằng trọng số thích ứng ($\text{adaptively reweight}$) đối với các tác nhân thúc đẩy bám bẩn đặc thù theo từng nhà máy.

- Khung học chuyển giao có khả năng giải thích thiết lập nền tảng thực tiễn cho dự đoán $\text{TMP}$ và hỗ trợ ra quyết định:
  - Nghiên cứu chứng minh thông tin bám bẩn chia sẻ có thể chuyển giao giữa các nhà máy $\text{MBR}$ và được tái hiệu chuẩn chọn lọc bằng lượng dữ liệu giới hạn từ nhà máy đích.
  - Bằng chứng hóa lý độc lập mang lại khả năng giải thích khoa học ($\text{scientifically interpretable}$) cho quá trình thích ứng mô hình.
  - Khung làm việc cung cấp nền tảng ứng dụng thực tiễn cho việc dự đoán $\text{TMP}$ tin cậy và hỗ trợ ra quyết định kiểm soát bám bẩn thích ứng theo nhà máy tại các hệ thống $\text{MBR}$ bị hạn chế dữ liệu ($\text{data-limited MBRs}$).

- Tuyên bố đóng góp của các tác giả ($\text{CRediT authorship contribution statement}$):
  - Xiaohang Han: Hình thành ý tưởng ($\text{Conceptualization}$), quản lý dữ liệu ($\text{Data curation}$), phân tích chính thức ($\text{Formal analysis}$), điều tra thực nghiệm ($\text{Investigation}$), phương pháp luận ($\text{Methodology}$), phần mềm ($\text{Software}$), kiểm thực ($\text{Validation}$), trực quan hóa ($\text{Visualization}$), soạn thảo bản thảo gốc ($\text{Writing – original draft}$).
  - Liu Yang: Hình thành ý tưởng ($\text{Conceptualization}$), quản lý dữ liệu ($\text{Data curation}$), phân tích chính thức ($\text{Formal analysis}$), điều tra thực nghiệm ($\text{Investigation}$), phương pháp luận ($\text{Methodology}$), phần mềm ($\text{Software}$), kiểm thực ($\text{Validation}$), trực quan hóa ($\text{Visualization}$), soạn thảo bản thảo gốc ($\text{Writing – original draft}$).
  - Huan Qin: Quản lý dữ liệu ($\text{Data curation}$), điều tra thực nghiệm ($\text{Investigation}$).
  - Shujuan Huang: Quản lý dữ liệu ($\text{Data curation}$), điều tra thực nghiệm ($\text{Investigation}$).
  - Han Zhang: Quản lý dữ liệu ($\text{Data curation}$), điều tra thực nghiệm ($\text{Investigation}$).
  - Boyan Xu: Hình thành ý tưởng ($\text{Conceptualization}$), huy động tài trợ ($\text{Funding acquisition}$), quản trị dự án ($\text{Project administration}$), giám sát ($\text{Supervision}$), viết – rà soát và chỉnh sửa ($\text{Writing – review \& editing}$).
  - How Yong Ng: Hình thành ý tưởng ($\text{Conceptualization}$), huy động tài trợ ($\text{Funding acquisition}$), giám sát ($\text{Supervision}$), viết – rà soát và chỉnh sửa ($\text{Writing – review \& editing}$).

- Tuyên bố về xung đột lợi ích ($\text{Declaration of competing interests}$):
  - Các tác giả tuyên bố không có xung đột lợi ích tài chính hoặc mối quan hệ cá nhân nào có thể ảnh hưởng đến công trình nghiên cứu được báo cáo trong bài báo.

- Lời cảm ơn và nguồn tài trợ nghiên cứu ($\text{Acknowledgement}$):
  - Nghiên cứu nhận hỗ trợ tài chính từ Quỹ Học giả Thái Sơn tỉnh Sơn Đông ($\text{Taishan Scholar Foundation of Shandong Province}$) theo mã tài trợ số $\text{tsqn202312222}$.
  - Nghiên cứu được hỗ trợ bởi Quỹ Khoa học Tự nhiên Quốc gia Trung Quốc ($\text{National Natural Science Foundation of China}$) theo mã tài trợ $42406133$.
  - Nghiên cứu được tài trợ bởi Quỹ Nghiên cứu Cơ bản và Nghiên cứu Cơ bản Ứng dụng tỉnh Quảng Đông ($\text{Basic and Applied Basic Research Foundation of Guangdong Province}$) theo mã tài trợ $\text{2023A1515110786}$.
  - Các tác giả cảm ơn các thành viên trong nhóm nghiên cứu của Giáo sư How Yong Ng tại Singapore (như Wei Hao Loh, David Imanuel Tanaka, và các cộng sự) vì sự hỗ trợ giá trị trong việc thu thập dữ liệu vận hành từ các nhà máy $\text{MBR}$ quy mô pilot (ghi nhận tại trang 12 của bài báo).
  - Dữ liệu được sử dụng độc quyền cho mô hình hóa và mô phỏng dựa trên $\text{AI}$ trong nghiên cứu này; tất cả thông tin nhạy cảm, bảo mật hoặc nhận dạng đều đã được ẩn danh hoặc che giấu trước khi phân tích.

- Dữ liệu bổ sung và tính khả dụng của dữ liệu ($\text{Supplementary data and data availability}$):
  - Dữ liệu bổ sung trực tuyến của bài báo được cung cấp tại liên kết DOI: $\text{https://doi.org/10.1016/j.memsci.2026.126065}$.
  - Dữ liệu nghiên cứu sẵn sàng được cung cấp khi có yêu cầu hợp lý gửi đến tác giả ($\text{Data will be made available on request}$).
