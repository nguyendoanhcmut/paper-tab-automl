## 1 Introduction

- **Vai trò và ưu điểm của công nghệ MBR trong xử lý và tái sử dụng nước thải**: Xử lý và tái sử dụng nước thải (wastewater treatment and reclamation) là chiến lược thiết yếu để giảm thiểu khủng hoảng nước do khan hiếm và ô nhiễm nước gây ra:
  - Công nghệ bioreactor màng (membrane bioreactor: MBR) kết hợp giữa phân tách màng (membrane separation) và xử lý sinh học (biological treatment) (Yamamoto et al., 1989).
  - MBR được sử dụng rộng rãi trong những năm gần đây nhờ các ưu điểm: chất lượng nước đầu ra (effluent quality) ổn định và xuất sắc, diện tích chiếm dụng nhỏ (small footprint), cùng lượng bùn dư phát sinh thấp (low residual sludge production) (Xiao et al., 2014; Krzeminski et al., 2017; Xiao et al., 2019; Qu et al., 2022).

- **Tắc nghẽn màng là rào cản hạn chế tính bền vững kỹ thuật - kinh tế của MBR**: Hiện tượng tắc nghẽn màng (membrane fouling) phát sinh trong quá trình vận hành MBR gây ra nhiều tác động tiêu cực (Xiao et al., 2019; Qu et al., 2022):
  - Dẫn đến suy giảm thông lượng (decreased flux) và suy giảm hiệu quả phân tách (deteriorated separation efficiency).
  - Làm gia tăng tiêu thụ năng lượng (increased energy consumption) và rút ngắn tuổi thọ của màng (shortened membrane lifespan).
  - Hạn chế tính bền vững kỹ thuật - kinh tế (techno-economic sustainability) của hệ thống (Xiao et al., 2019; Qu et al., 2022).

- **Ba nhóm yếu tố chi phối hiện tượng tắc nghẽn màng**: Tắc nghẽn màng có mối liên hệ chặt chẽ với đặc tính màng (membrane properties), đặc tính bùn lỏng (mixed liquor properties), và điều kiện vận hành (operating conditions):
  - Hành vi tắc nghẽn của các vật liệu màng (chẳng hạn như polyvinylidene fluoride [PVDF], polyethersulfone [PES], polyethylene [PE], và polyacrylonitrile [PAN]) biến thiên theo độ ưa nước/kỵ nước (hydrophilicity/hydrophobicity), cấu trúc lỗ rỗng (pore structure), và độ nhám bề mặt (surface roughness), tất cả đều tác động đến tương tác giữa màng và chất gây tắc nghẽn (membrane-foulant interaction) (Yamato et al., 2006; Zhang et al., 2008).
  - Màng kỵ nước nhìn chung dễ bị tắc nghẽn hơn so với màng ưa nước (Choi et al., 2002).

- **Tương tác giữa kích thước lỗ rỗng màng và kích thước chất gây tắc nghẽn**: Kích thước lỗ rỗng màng (membrane pore size) và kích thước chất gây tắc nghẽn (foulant size) đóng vai trò tương tác trong quá trình hình thành tắc nghẽn:
  - Các chất gây tắc nghẽn có kích thước tương đương với kích thước lỗ rỗng có thể làm bít tắc chặt các lỗ rỗng do cơ chế loại trừ kích thước (size exclusion) (Meireles et al., 1991).
  - Các chất gây tắc nghẽn có kích thước nhỏ có thể gây ra hiện tượng tắc nghẽn do hấp phụ (adsorptive fouling) bên trong lòng lỗ rỗng (Kawakatsu et al., 1993).
  - Dải phân bố kích thước lỗ rỗng (pore size distribution) hẹp hơn mang lại sự thuận lợi cho việc duy trì thông lượng ổn định (Shimizu et al., 1990; Meireles et al., 1991).

- **Tác động của độ nhám bề mặt màng ở các thang đo kích thước**: Độ nhám bề mặt màng (membrane surface roughness) chi phối hành vi lắng đọng và hấp phụ của chất gây tắc nghẽn (Xu et al., 2020):
  - Ở thang đo micromet ($\mu\text{m}$), độ nhám bề mặt ảnh hưởng đến động lực học chất lưu (fluid dynamics) đối với sự lắng đọng hạt.
  - Ở thang đo nanomet ($\text{nm}$), độ nhám bề mặt chi phối sự tiếp xúc giữa các phân tử (intermolecular contact) đối với quá trình hấp phụ chất gây tắc nghẽn.
  - Dữ liệu thực nghiệm chỉ ra rằng bề mặt màng nhẵn hơn có xu hướng cản trở sự hình thành và phát triển của lớp bánh cặn (cake layer formation) (Vatanpour et al., 2011; Sadeghi et al., 2013; Panda et al., 2015).

- **Vai trò gây tắc nghẽn của các thành phần trong bùn lỏng**: Hỗn hợp chất rắn lơ lửng trong bùn lỏng (mixed liquor suspended solids: MLSS), các chất polyme ngoại bào (extracellular polymeric substances: EPS), và các sản phẩm vi sinh hòa tan (soluble microbial products: SMP) đều góp phần gây tắc nghẽn màng trong MBR:
  - MLSS chịu trách nhiệm chính đối với hiện tượng tắc nghẽn tổng thể, đặc biệt ở các mức nồng độ trên $10\text{ mg/L}$.
  - EPS và SMP đóng vai trò chủ chốt gây ra hiện tượng tắc nghẽn không thuận nghịch về mặt vật lý (physically irreversible fouling).

- **Tác động của điều kiện vận hành MBR đến nồng độ các chất gây tắc nghẽn**: MLSS, EPS, và SMP có mối liên hệ mật thiết với các điều kiện vận hành MBR như thời gian lưu nước (hydraulic retention time: HRT), thời gian lưu bùn (sludge retention time: SRT), và tỷ lệ cơ chất trên vi sinh vật (food-to-microorganism rate: F/M) (Huang et al., 2011):
  - HRT quá ngắn hoặc SRT quá dài có thể dẫn đến nồng độ MLSS và SMP cao, làm trầm trọng thêm mức độ tắc nghẽn màng.
  - Nồng độ MLSS quá thấp một cách bất thường cũng có thể làm trầm trọng thêm tình trạng tắc nghẽn, có khả năng do sự giải phóng quá mức của EPS (Yoon, 2015).

- **Ba nhóm chiến lược kiểm soát tắc nghẽn màng chính**: Các chiến lược kiểm soát tắc nghẽn màng (fouling control strategies) được phân loại thành ba nhóm giải pháp chính (Meng et al., 2017):
  - **Điều hòa bùn lỏng (mixed liquor conditioning)**: Bổ sung các vật liệu như chất mang lơ lửng (suspended carriers), hạt (particles), chất keo tụ (coagulants), ozone, và các hóa chất khác (Wu and Huang, 2008; Kurita et al., 2014, 2015; Juntawang et al., 2017; Zhang et al., 2017; Zhang et al., 2022); các chất phụ gia này có khả năng điều chỉnh đặc tính của SMP và EPS, đồng thời tác động đến cấu trúc bông bùn (floc structure) (Wu et al., 2006; Wu and Huang, 2008; Juntawang et al., 2017; Zhang et al., 2017).
  - **Điều chỉnh điều kiện lọc (filtration conditions adjustment)**: Cường độ sục khí (aeration intensity) và chu kỳ lọc/nghỉ (filtration/relaxation intervals) ảnh hưởng trực tiếp đến tốc độ tắc nghẽn tổng thể và khả năng thuận nghịch của lớp bánh/gel (cake/gel layer reversibility) (Liu et al., 2020b); sục khí hoặc thổi khí (aeration / air scouring) giúp bóc tách và loại bỏ chất gây tắc nghẽn khỏi bề mặt màng bằng cách gia tăng lực cắt dòng chảy ngang (cross-flow shear).
  - **Làm sạch màng bị tắc nghẽn (physical/chemical cleaning of fouled membranes)**: Làm sạch vật lý (như rửa bằng nước máy, rửa bằng nước đầu ra của màng, rửa dòng so le [staggered flow], rửa ngược [backwash], và rửa siêu âm [ultrasonic cleaning]) giúp giảm nhẹ tắc nghẽn thuận nghịch (reversible fouling); trong khi đó, làm sạch hóa học (sử dụng axit, kiềm, chất oxy hóa, chất tạo phức [chelating agent], và chất hoạt động bề mặt [surfactants]) giúp giảm nhẹ sâu hơn hiện tượng tắc nghẽn không thuận nghịch (irreversible fouling).

- **Hạn chế hậu nghiệm và độ trễ của các biện pháp kiểm soát tắc nghẽn hiện hữu**: Các biện pháp kiểm soát tắc nghẽn màng hiện nay chủ yếu được tiến hành theo phương thức hậu nghiệm (a posteriori) dựa trên việc quan sát các hiện tượng tắc nghẽn đã xảy ra:
  - Can thiệp kiểm soát chỉ diễn ra sau khi ghi nhận hiện tượng gia tăng áp suất xuyên màng (transmembrane pressure: TMP), tạo ra một độ trễ nhất định giữa thời điểm tắc nghẽn phát sinh và thời điểm can thiệp kiểm soát.
  - Các biện pháp can thiệp không chuẩn xác có thể làm giảm hiệu quả xử lý, lãng phí năng lượng và hóa chất, đồng thời gây hư hại đến màng.
  - Cần áp dụng các biện pháp kiểm soát phù hợp với thời điểm và liều lượng chính xác.
  - Nhằm đạt được cảnh báo sớm (early warning) và kiểm soát kịp thời, việc phát triển mô hình có khả năng dự đoán xu hướng tắc nghẽn ngay từ giai đoạn khởi phát (fouling tendency in its infancy) đóng vai trò then chốt.

- **Tiềm năng và giới hạn cố hữu của các mô hình thống kê truyền thống**: Các mô hình dự đoán và điều tiết dựa trên dữ liệu (data-driven prediction and regulation models) mang lại cách tiếp cận mới để kiểm soát chính xác hiện tượng tắc nghẽn màng, trong đó các mô hình thống kê truyền thống đã đạt được một số bước tiến ban đầu:
  - Zhang et al. (2012) đã thiết lập mô hình bình phương tối thiểu từng phần (partial least squares: PLS) đạt $R^2 = 0.84$ để dự đoán thông lượng màng từ các đặc tính bùn lỏng gồm nồng độ MLSS/EPS/SMP, độ kỵ nước tương đối, kích thước hạt trung bình, và áp suất thẩm thấu.
  - Chen et al. (2022) đã phát triển mô hình chuỗi thời gian (time series model) sử dụng nhiệt độ làm biến đồng biến (covariate) và các sự kiện làm sạch trực tuyến làm biến chuyển đổi (switching variables) để dự đoán xu hướng TMP trong bể MBR kỵ khí (anaerobic MBR: AnMBR) qua các mùa vụ, đạt $R^2 = 0.91$.
  - Mặc dù phản ánh tốt mối quan hệ giữa biến đầu vào và biến đầu ra, các mô hình thống kê truyền thống phụ thuộc vào tri thức tiên nghiệm (a priori knowledge) về các mối quan hệ này và bộc lộ các nhược điểm cố hữu:
    - (a) Độ chính xác khớp mẫu chưa đủ (insufficient fitting accuracy), khả năng tổng quát hóa yếu (weak generalization ability), và độ thích ứng kém với mẫu dữ liệu mới do đánh giá thấp độ phức tạp của các mối quan hệ thực tế.
    - (b) Hiệu quả tính toán thấp đối với phân tích dữ liệu lớn (big data analysis) và tốc độ hội tụ chậm khi xử lý nhiều biến có tương tác phức tạp do những giới hạn trong cấu trúc mô hình.
    - Tính đa dạng và mức độ phức tạp của nhiều biến tương tác lẫn nhau vốn là đặc tính cố hữu trong hệ thống tắc nghẽn màng thực tế, khiến việc ứng dụng các mô hình thống kê truyền thống gặp nhiều thách thức.

- **Đặc trưng và thế mạnh của Machine Learning trong dự đoán tắc nghẽn MBR**: Machine learning là bước phát triển thống kê gần đây đóng vai trò bổ trợ cho các mô hình thống kê truyền thống, thu hút sự chú ý ngày càng tăng trong kỹ thuật môi trường như một công nghệ trí tuệ nhân tạo tổng quát (general artificial intelligence technology) (Zhong et al., 2021):
  - Ra đời từ các mô hình thống kê nhưng có sự khác biệt: machine learning tập trung vào việc ước tính chính xác các hàm số phức tạp bằng máy tính, thay vì cung cấp các khoảng tin cậy thống kê (statistical confidence intervals) cho các hàm đó.
  - Các thuật toán machine learning tự động "học" từ kinh nghiệm (dữ liệu) để cải thiện hiệu năng của hệ thống (Bishop, 2006).
  - Với đặc tính của mô hình hộp đen (black-box model), machine learning sở hữu khả năng khớp mẫu mạnh mẽ, độ thích ứng tốt, và độ chính xác dự đoán cao khi giải quyết các bài toán có hàm phản ứng chưa biết (unknown response functions), mối quan hệ biến phức tạp, cùng khối lượng dữ liệu lớn.
  - Các thế mạnh này mở ra triển vọng thuận lợi cho việc dự đoán tắc nghẽn trong các hệ thống MBR; trong những năm gần đây, machine learning dần được áp dụng để dự đoán hiệu năng lọc màng (như thông lượng, độ cản [resistance], và độ thẩm thấu [permeability]), đồng thời mang lại cơ sở định lượng mới hỗ trợ phân tích cơ chế tắc nghẽn (Niu et al., 2022).

- **Cấu trúc nội dung của bài báo**: Nghiên cứu này triển khai ba nội dung chính:
  - Giới thiệu 4 mô hình machine learning thông dụng.
  - Đánh giá tổng quan các ứng dụng của mô hình machine learning trong việc dự đoán hiệu quả loại bỏ chất ô nhiễm (pollutant removal) và hiệu năng tắc nghẽn màng (fouling performance).
  - Phân tích các hạn chế của những mô hình hiện có nhằm hỗ trợ các nhà nghiên cứu trong tương lai phát triển các mô hình machine learning mới để nâng cao khả năng dự đoán tắc nghẽn trong MBR.
