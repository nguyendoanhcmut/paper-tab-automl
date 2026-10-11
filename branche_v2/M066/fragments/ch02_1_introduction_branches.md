## 1. Introduction

* **Đặc tính và thách thức quản lý nước rỉ rác tại trạm trung chuyển chất thải rắn đô thị (MSW transfer station leachate)**
    * Quá trình đô thị hóa nhanh và mức sống nâng cao làm gia tăng mạnh lượng chất thải rắn đô thị (MSW - municipal solid waste), tạo áp lực lớn lên hệ thống quản lý chất thải đô thị.
    * Hệ thống quản lý chất thải đô thị bao gồm $3$ giai đoạn liên kết chặt chẽ: thu gom đầu nguồn (front-end collection), trung chuyển chặng giữa (mid-end transfer), và xử lý cuối vòng đời (end-of-life treatment).
    * Trạm trung chuyển chất thải (waste transfer stations) đóng vai trò là mắt xích liên kết then chốt giữa khâu thu gom và bãi xử lý/thải bỏ cuối cùng.
    * Nước rỉ rác phát sinh tại các trạm trung chuyển có thành phần hóa lý phức tạp, chứa nồng độ rất cao các chất hữu cơ, amoniac ($\text{ammonia}$), sản phẩm vi sinh hòa tan (SMP - soluble microbial products), chất rắn lơ lửng (suspended solids) và các hợp chất độc hại.
    * Nếu không được xử lý phù hợp, các chất ô nhiễm từ nước rỉ rác có thể gây tổn hại nghiêm trọng đến môi trường đất, nước mặt, nước ngầm và khí quyển.
    * Quản lý nước rỉ rác tại trạm trung chuyển thường chịu nhiều hạn chế thực tế: mặt bằng không gian chật hẹp, rào cản chi phí kinh tế đối với các công nghệ xử lý nâng cao, và việc thực thi quy định chưa đầy đủ trong một số trường hợp.
    * Hệ quả là nước rỉ rác tại trạm trung chuyển thường bị lưu trữ không đạt chuẩn hoặc xả thải trực tiếp khi chưa qua xử lý tối thiểu, làm gia tăng rủi ro ô nhiễm môi trường.

* **Ưu thế và thách thức vận hành của công nghệ bể phản ứng màng sinh học kỵ khí (AnMBR)**
    * Công nghệ bể phản ứng màng kỵ khí (AnMBR - anaerobic membrane bioreactor) nhận được sự quan tâm lớn như một giải pháp xử lý và tái sử dụng hiệu quả đối với nước thải công nghiệp và đô thị có tải lượng ô nhiễm cao.
    * AnMBR kết hợp phân hủy sinh học kỵ khí với quá trình phân tách màng lọc, sở hữu nhiều ưu điểm: tạo nước đầu ra chất lượng cao, diện tích mặt bằng nhỏ gọn (compact footprint), sản sinh lượng bùn thấp và có tiềm năng thu hồi năng lượng dưới dạng khí mê-tan ($\text{CH}_4$).
    * Hiện tượng tắc nghẽn/bám bẩn màng (membrane fouling) là thách thức nghiêm trọng nhất, cản trở khả năng vận hành ổn định và hiệu quả kinh tế lâu dài của hệ thống AnMBR.
    * Bám bẩn màng làm gia tăng áp suất xuyên màng (TMP - transmembrane pressure), suy giảm lưu lượng thấm qua màng (permeate flux), làm tăng tần suất làm sạch và chi phí bảo trì, ảnh hưởng đến tính khả thi lâu dài của công nghệ.
    * Các chiến lược kiểm soát bám bẩn màng thường được áp dụng bao gồm tiền xử lý dòng vào (influent pre-treatment), tăng cường độ sục khí (aeration intensity), và điều hòa hóa học hỗn hợp bùn lỏng (chemical conditioning).
    * Tuy nhiên, các giải pháp truyền thống này thường tiêu tốn nhiều năng lượng, chi phí cao hoặc không đủ hiệu quả trước các dòng thải có thành phần biến động mạnh như nước rỉ rác.

* **Cơ chế bám bẩn màng phức tạp và hạn chế của các mô hình động học truyền thống**
    * Bám bẩn màng trong AnMBR hình thành từ sự tích tụ của lớp bánh bùn (cake layer) trên bề mặt màng, cùng các chất polyme ngoại bào (EPS - extracellular polymeric substances) và sản phẩm vi sinh hòa tan (SMP).
    * Sự tiến triển bám bẩn màng thể hiện tính phi tuyến động học phức tạp, chịu tác động tương hỗ theo thời gian giữa đặc tính nước đầu vào, điều kiện vận hành thủy lực và biến động cấu trúc quần thể vi sinh vật.
    * Các mô hình động học và cơ chế truyền thống gặp nhiều khó khăn trong việc nắm bắt và dự báo hiện tượng bám bẩn phi tuyến trong điều kiện tải trọng biến thiên đột ngột.

* **Tiềm năng ứng dụng của học máy (ML) và nhu cầu về mô hình giải thích được (Interpretable ML)**
    * Các kỹ thuật học máy (ML - machine learning) chứng minh năng lực mô hình hóa hiệu quả các mối quan hệ phi tuyến phức tạp trong các hệ thống môi trường.
    * Các thuật toán ML phổ biến như mạng nơ-ron nhân tạo (ANN - artificial neural networks), hồi quy vector hỗ trợ (SVR - support vector regression), tăng cường độ dốc cực trị (XGBoost - extreme gradient boosting), và rừng ngẫu nhiên (RF - random forest) đã được ứng dụng rộng rãi để giám sát và tối ưu hóa quá trình xử lý nước thải.
    * ML hỗ trợ dự đoán hiệu suất loại bỏ chất ô nhiễm, chất lượng dòng ra, phát tín hiệu cảnh báo sớm thời gian thực và cải thiện kiểm soát vận hành.
    * Hạn chế của các nghiên cứu ML trước đây:
        * Phần lớn các mô hình ML hiện hữu tập trung vào các hệ thống xử lý nước thải đô thị hoặc công nghiệp có điều kiện vận hành tương đối ổn định.
        * Rất ít nghiên cứu khảo sát các dòng thải nồng độ ô nhiễm cao và dao động mạnh như nước rỉ rác, nơi thành phần dòng vào và tải trọng biến thiên đột ngột theo thời gian.
        * Các mô hình trước đây chủ yếu được huấn luyện để nội suy trong phạm vi dữ liệu lịch sử hạn hẹp, thiếu độ ổn định và tin cậy khi gặp các dao động tải trọng bất thường hoặc xáo trộn vận hành.
    * Nhu cầu cấp thiết: Cần xây dựng các khung mô hình hóa động thích ứng, có khả năng tích hợp dữ liệu cảm biến thời gian thực nhằm dự đoán tin cậy hành vi hệ thống trong các kịch bản vận hành thay đổi.

* **Mục tiêu nghiên cứu và phương pháp tiếp cận của bài báo**
    * Vận hành hệ thống AnMBR trong $120\text{ ngày}$ liên tục để xử lý nước rỉ rác thực tế từ trạm trung chuyển chất thải rắn đô thị.
    * Khảo sát có hệ thống các điều kiện thời gian lưu thủy lực (HRT - hydraulic retention time) và tải trọng hữu cơ (OLR - organic loading rate) khác nhau để đánh giá hiệu suất loại bỏ $\text{COD}$, biến đổi nitơ và hành vi bám bẩn màng.
    * Đánh giá sự phát triển bám bẩn thông qua giám sát vận hành, đánh giá hiệu năng chống bám bẩn, phân tích thành phần chất bám bẩn (foulants) và phân bố kích thước hạt (particle size distribution).
    * Phân tích cấu trúc quần thể vi sinh vật và sự dịch chuyển chức năng nhằm làm sáng tỏ mối liên kết giữa động thái vi sinh vật, hiệu suất xử lý của bể phản ứng và sự hình thành bám bẩn màng.
    * Phát triển và so sánh $3$ thuật toán ML gồm RF, ANN và XGBoost để dự đoán nồng độ $\text{COD}$ đầu ra và giá trị $\text{TMP}$ dựa trên các thông số vận hành dòng vào và dòng ra thường quy.
    * Tối ưu hóa siêu tham số mô hình thông qua tìm kiếm ngẫu nhiên (randomized search) kết hợp kiểm thực chéo $5$ lần ($5\text{-fold cross-validation}$).
    * Ứng dụng phương pháp SHAP (SHapley Additive exPlanations) để bóc tách tính đóng góp và xếp hạng mức độ quan trọng của các biến đầu vào đối với dự đoán $\text{COD}$ và $\text{TMP}$.
    * Cung cấp ranh giới vận hành định lượng (quantitative operational boundary), bộ dự đoán chất bám bẩn đảo ngược (reversed foulant predictor), và khung chẩn đoán tinh gọn cảm biến (sensor-lite diagnostic framework) có khả năng giải thích, hỗ trợ quản lý nước rỉ rác bằng AnMBR bền vững và tin cậy tại các trạm trung chuyển chất thải.
