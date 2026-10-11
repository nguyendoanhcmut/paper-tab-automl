## 1. Introduction

* Ngành công nghiệp dệt nhuộm (textile industry) đang phát triển mạnh mẽ và trở thành nhân tố đóng góp quan trọng cho sự phát triển kinh tế quốc dân của nhiều quốc gia:
    * Ngành dệt nhuộm có xu hướng tiêu thụ lượng nước rất lớn và hơn $90\%$ lượng nước tiêu thụ chuyển thành nước thải.
    * Nước thải dệt nhuộm chứa nồng độ độ mặn (salinity) cao với $5\text{--}6\%$ $\text{NaCl}$, độ màu (color), chất rắn (solids), nhu cầu oxy hóa học (chemical oxygen demand - $\text{COD}$) và kim loại nặng (heavy metals).
    * Việc xả thải nước thải từ ngành dệt nhuộm vào các thủy vực tự nhiên tạo ra mối nguy hại tiềm tàng lớn đối với sinh vật thủy sinh và sức khỏe cộng đồng do độc tính cao (high toxicity) và khả năng gây đột biến (mutagenicity).
    * Nước thải dệt nhuộm có thể được xử lý bằng các quy trình sinh học hiếu khí (aerobic) và kỵ khí (anaerobic), cũng như các quy trình hóa lý (physio-chemical processes) như keo tụ (coagulation) và tạo bông (flocculation).
    * Phương pháp xử lý sinh học, đặc biệt là quy trình kỵ khí, nổi bật nhờ chi phí thấp và hiệu quả cao.
* Bể phản ứng sinh học màng kỵ khí (anaerobic membrane bioreactors - AnMBR) kết hợp quy trình xử lý sinh học kỵ khí với công nghệ tách màng (membrane separation technology), mang lại nhiều ưu thế trong xử lý nước thải dệt nhuộm:
    * Hệ AnMBR thể hiện các ưu điểm vượt trội bao gồm hiệu quả khử màu cao, tiết kiệm năng lượng, thu hồi khí sinh học (biogas recovery) và phát sinh bùn thấp (low sludge production).
    * Nghiên cứu của Yurtsever và cộng sự (2015) trên nước thải dệt nhuộm nhân tạo (synthetic textile wastewater) chỉ ra rằng AnMBR có thể đạt hiệu quả khử màu hoàn toàn và hiệu suất loại bỏ $\text{COD}$ đạt khoảng $94\%$.
    * Nghiên cứu của Berkessa và cộng sự (2020) đánh giá tính khả thi của bể phản ứng màng động học kỵ khí (anaerobic dynamic membrane bioreactor) trong xử lý nước thải phẩm nhuộm anthraquinone (anthraquinone dye) cho thấy có thể loại bỏ $98.5\%$ $\text{COD}$ hòa tan và hơn $97.5\%$ độ màu.
    * Tuy nhiên, nước thải dệt nhuộm không chỉ chứa phẩm nhuộm mà còn chứa nhiều hóa chất trợ ngấm/phụ trợ (auxiliary chemicals) và các hợp chất ức chế (inhibitory compounds) có thể ảnh hưởng tiêu cực đến hiệu suất xử lý.
    * Nghiên cứu của Yurtsever và cộng sự (2020) khi khảo sát hiệu suất xử lý của AnMBR đối với nước thải dệt nhuộm thực tế (real textile wastewater) ghi nhận hiệu suất loại bỏ $\text{COD}$ chỉ đạt $84\%$.
* Độ mặn cao trong nước thải dệt nhuộm ức chế hiệu suất xử lý sinh học và gây gia tăng tắc nghẽn màng (membrane fouling):
    * Sự ức chế hiệu suất xử lý bắt nguồn từ tác động tiêu cực của nồng độ muối cao lên hoạt tính trao đổi chất của vi sinh vật, từ đó làm giảm hiệu quả phân hủy chất ô nhiễm.
    * Nghiên cứu của Chen và cộng sự (2019) đánh giá tác động của độ mặn ($\text{NaCl}$ $0\text{--}40\text{ g/L}$) lên AnMBR chỉ ra rằng hiệu suất loại bỏ $\text{COD}$ bị ức chế, suy giảm từ $96.4\%$ xuống $77.7\%$.
    * Độ mặn cao không chỉ ảnh hưởng đến hiệu suất xử lý mà còn dẫn đến hiện tượng tắc nghẽn màng nghiêm trọng hơn, nhiều khả năng do sự gia tăng hàm lượng sản phẩm vi sinh vật hòa tan (soluble microbial products - SMP) dưới áp lực muối cao (high salt stress).
    * Các nghiên cứu trước đây đánh giá tác động của độ mặn lên hiệu suất AnMBR chủ yếu tập trung vào cấu hình bể phản ứng khuấy trộn liên tục (continuous stirred tank reactor - CSTR).
    * Hệ AnMBR cấu hình tầng bùn kỵ khí dòng chảy ngược (upflow anaerobic sludge blanket - UASB) dường như có khả năng giảm thiểu tắc nghẽn màng so với cấu hình CSTR nhờ sự lắng đọng lớp cặn nghẽn (fouling layer deposition) ít hơn.
    * UASB là một bể phản ứng kỵ khí tốc độ cao (high-rate anaerobic reactor) điển hình thường được ứng dụng trong xử lý nước thải dệt nhuộm, do đó việc sử dụng AnMBR cấu hình UASB rất thuận lợi cho việc cải tạo/nâng cấp (refurbishment) các trạm xử lý hiện hữu.
    * Tuy nhiên, các nghiên cứu về tác động của độ mặn đối với hệ AnMBR cấu hình UASB trong xử lý nước thải dệt nhuộm hiện còn rất hạn chế.
* Quá trình sinh học trong AnMBR diễn ra phức tạp, tạo tiền đề cho việc ứng dụng các thuật toán máy học (machine learning - ML) nhằm mô hình hóa và dự đoán hiệu suất:
    * Hiệu suất xử lý của AnMBR chịu ảnh hưởng bởi nhiều yếu tố, trong khi mối quan hệ giữa các biến số vận hành và hiệu quả loại bỏ chất ô nhiễm vẫn chưa được làm sáng tỏ sâu sắc.
    * Máy học là kỹ thuật phân loại (classification) và hồi quy (regression) dựa trên dữ liệu hoặc kinh nghiệm trong quá khứ, hiện được ứng dụng rộng rãi trong lĩnh vực xử lý nước thải.
    * Một số mô hình đã được xây dựng để dự đoán hiệu suất AnMBR, chẳng hạn như nghiên cứu của Huang và cộng sự (2018) đã sử dụng mô hình mạng nơ-ron lan truyền ngược (back propagation neural network - BPNN) để dự đoán hiệu suất AnMBR (loại bỏ $\text{COD}$ và kháng sinh) trong xử lý nước thải dược phẩm.
    * Tuy nhiên, rất ít nghiên cứu xem xét việc đưa tác động của độ mặn vào các mô hình dự đoán hiệu suất xử lý của hệ AnMBR.
    * Adaboost (Adaptive Boosting), cây quyết định (decision trees) và rừng ngẫu nhiên (random forests) là các thuật toán máy học tiêu biểu:
        * Thuật toán Adaboost kết hợp nhiều bộ phân loại yếu (weak classifiers) thành một bộ phân loại mạnh (strong classifier), mang lại hiệu năng phân loại cao và có khả năng dự đoán tốt nồng độ chất ô nhiễm.
        * So với cây quyết định và rừng ngẫu nhiên, Adaboost có xu hướng đạt độ chính xác cao hơn và ít xảy ra hiện tượng quá khớp (overfitting), mang lại các dự đoán sát với thực tế hơn.
* Mục tiêu và nội dung chính của nghiên cứu này:
    * Mục tiêu chung: đánh giá tác động của độ mặn lên hệ AnMBR màng gốm (ceramic membrane) cấu hình UASB trong xử lý nước thải dệt nhuộm nhân tạo.
    * Đánh giá tác động của việc tăng dần từng bước độ mặn ($0\text{--}20\text{ g/L}$ $\text{NaCl}$) đến quá trình khử màu (decolorization), phân hủy chất hữu cơ (organic degradation), quá trình kỵ khí (anaerobic process) và hiện tượng tắc nghẽn màng của hệ AnMBR màng gốm cấu hình UASB.
    * Phân tích cấu trúc quần xã vi sinh vật (microbial community structure) nhằm làm rõ sự biến đổi của quần thể vi sinh vật dưới các mức áp lực muối khác nhau.
    * Xây dựng mô hình dự đoán $\text{COD}$ đầu ra (effluent $\text{COD}$) dựa trên thuật toán máy học Adaboost nhằm thiết lập mối quan hệ giữa $\text{COD}$ đầu ra và các yếu tố môi trường trong AnMBR.
