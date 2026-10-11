## 1. Introduction

* **Bối cảnh và thách thức nghiêm trọng của hiện tượng tắc nghẽn màng trong công nghệ xử lý nước bằng bể phản ứng sinh học màng (MBR)**:
  * Công nghệ tách màng (membrane technology) đã và đang được ứng dụng rộng rãi và phổ biến trong lĩnh vực xử lý nước cấp và nước thải nhờ hiệu suất xử lý vượt trội, chất lượng nước đầu ra ổn định và dấu chân công trình nhỏ gọn.
  * Tuy nhiên, trở ngại kỹ thuật lớn nhất đối với công nghệ màng là hiện tượng tắc nghẽn màng (*membrane fouling*) (Lin et al., $2012$; Shen et al., $2019$; Zhang et al., $2017$, $2019$), làm gia tăng áp suất xuyên màng ($\text{TMP}$), suy giảm thông lượng lọc qua màng, đòi hỏi phải tiêu tốn hóa chất rửa màng và làm giảm tuổi thọ vận hành của màng lọc.
  * Hiện nay, những hiểu biết khoa học sâu sắc về cơ chế tắc nghẽn màng trong các ứng dụng xử lý nước, đặc biệt là trong các hệ thống bể phản ứng sinh học màng (Membrane Bioreactor – MBR), vẫn còn rất hạn chế và chưa đầy đủ (Lin et al., $2014\text{b}$; Meng et al., $2017$; Teng et al., $2018\text{b}$; Zhang et al., $2018$). Môi trường hỗn hợp bùn hoạt tính MBR chứa phức hợp vi sinh vật, chất ngoại bào ($\text{EPS}$), các chất hòa tan hữu cơ ($\text{SMP}$) và các ion vô cơ đa dạng, đặt ra thách thức cấp bách đòi hỏi cộng đồng nghiên cứu toàn cầu phải tiếp tục giải mã cơ chế bám bẩn.

* **Cơ chế bám dính chất gây tắc nghẽn (*foulant adhesion*): Sự chi phối quyết định của các lực tương tác bề mặt tầm ngắn so với động lực học chất lưu**:
  * Tắc nghẽn màng trong MBR về bản chất bắt nguồn từ sự bám dính ban đầu của các chất bẩn đa dạng (*foulants*) lên bề mặt màng hoặc sự phát triển và tích tụ của lớp bánh bùn/lớp chất bẩn (*foulant layer formation*) (Chen et al., $2016$, $2019$; Wang et al., $2014$; Zhang et al., $2013$).
  * MBR tạo ra một môi trường tương tác vô cùng phức tạp giữa các yếu tố thủy động học và hóa lý giao diện:
    * Lực thủy động lực học (*hydrodynamic forces*) sinh ra từ dòng sục khí bọt khí (*aeration*), khuấy trộn cơ học (*stirring*) và áp suất lọc kéo qua màng (*filtration*) đóng vai trò vận chuyển các phần tử chất bẩn trong dòng khối tiến sát về phía bề mặt màng.
    * Tuy nhiên, khả năng bám dính sau cùng của chất bẩn lên bề mặt màng hay bị cuốn trôi ngược lại vào pha lỏng không do lực thủy động quyết định đơn thuần, mà bị chi phối quyết định bởi các lực tương tác bề mặt tầm ngắn (*short-range interfacial interactions*) giữa các nhóm chức bề mặt của chất bẩn và bề mặt màng (Chen et al., $2012$, $2015$; Hoek và Agarwal, $2006$; Wang et al., $2013$).
  * Do đó, việc định lượng hóa chính xác các tương tác bề mặt này đóng vai trò then chốt hàng đầu để thấu hiểu và kiểm soát hiện tượng tắc nghẽn màng.

* **Lý thuyết XDLVO cổ điển và hạn chế cốt tử đối với bề mặt màng có độ nhám tự nhiên**:
  * Nhằm định lượng hóa các tương tác giao diện này, lý thuyết Derjaguin–Landau–Verwey–Overbeek mở rộng (*extended DLVO* – $\text{XDLVO}$) đã được đề xuất và áp dụng rộng rãi (van Oss, $1995$; Hoek và Agarwal, $2006$; Ding et al., $2013$; Chen et al., $2017$). Lý thuyết $\text{XDLVO}$ phân tách tổng tương tác thành $3$ thành phần lực cơ bản:
    * Tương tác tán xạ Lifshitz-van der Waals ($\Delta G^{\text{LW}}$);
    * Tương tác tĩnh điện lớp điện kép ($\Delta G^{\text{EL}}$);
    * Tương tác phân cực axit-bazơ Lewis ($\Delta G^{\text{AB}}$) phản ánh tính ưa/kỵ nước bề mặt.
  * Hạn chế lớn nhất của lý thuyết $\text{XDLVO}$ truyền thống nằm ở việc mô hình hóa dựa trên giả định lý tưởng hóa bề mặt phẳng nhẵn hoàn hảo (*idealized smooth surfaces*) hoặc các xấp xỉ hình học đơn giản như bề mặt fractal hay phân bố nhám Gauss (Azeredo et al., $1999$; Hoek và Agarwal, $2006$; Shen et al., $2015$).
  * Trái lại, trong thực tế ứng dụng xử lý nước, hầu như toàn bộ các màng lọc polyme đều có bề mặt gồ ghề nhấp nhô tự nhiên (*naturally rough surfaces*) (Brant và Childress, $2002$; Hoek và Agarwal, $2006$; Wang et al., $2013$; Zhang et al., $2016$). Độ nhám cục bộ làm biến đổi sâu sắc phân bố trường lực và năng lượng tương tác giao diện so với mô hình phẳng nhẵn lý tưởng.
  * Sự mâu thuẫn giữa giả định lý thuyết và thực tiễn hình thái màng đòi hỏi phải phát triển lý thuyết $\text{XDLVO}$ để có thể áp dụng chuẩn xác cho các bề mặt nhám gồ ghề ngẫu nhiên.

* **Phương pháp XDLVO nâng cao (*advanced XDLVO approach*): Tích hợp AFM và tích phân phần tử bề mặt (SEI) cùng rào cản tính toán cực lớn**:
  * Các nỗ lực nghiên cứu đột phá gần đây (Hoek và Agarwal, $2006$; Chen et al., $2012$) đã đề xuất phương pháp $\text{XDLVO}$ nâng cao thông qua việc tích hợp hình học vi phân (*differential geometry*) và kỹ thuật tính toán số vào lý thuyết $\text{XDLVO}$.
  * Phương pháp này kết hợp bản đồ độ cao thực tế thu được từ kính hiển vi lực nguyên tử (Atomic Force Microscopy – $\text{AFM}$) với kỹ thuật tích phân phần tử bề mặt (Surface Element Integration – $\text{SEI}$), cho phép mô phỏng địa hình gồ ghề ngẫu nhiên và tính toán chính xác tương tác năng lượng giữa hai bề mặt có hình thái hình học tùy ý bất kỳ trong không gian $3$ chiều ($x, y, z$).
  * Sự ra đời của $\text{SEI}$-$\text{XDLVO}$ nâng cao đã mở rộng đáng kể lý thuyết giao diện và đem lại những góc nhìn khoa học mới mẻ về hành vi tắc nghẽn màng.
  * Tuy nhiên, phương pháp $\text{XDLVO}$ nâng cao gặp phải một rào cản kỹ thuật nghiêm trọng: **chi phí thời gian tính toán khổng lồ (*excessively computational time consumption*)**.
    * Việc giải các tích phân phần tử bề mặt hai lớp (thường là các tích phân kép Simpson – *double Simpson integrals*) trên ma trận lưới phần tử $\text{AFM}$ dày đặc tại một khoảng cách phân cách $d$ nhất định thường tiêu tốn đến vài giờ đồng hồ ($3\text{--}5\text{ giờ}$) chạy liên tục trên một trạm máy tính hiệu năng cao (*workstation*) (Teng et al., $2018\text{a}$, $2019$).
    * Do đó, để dựng nên một đường cong hoàn chỉnh biểu diễn phân bố tương tác bề mặt trên toàn bộ dải khoảng cách phân cách ngắn từ $0{,}158\text{ nm}$ đến $10\text{ nm}$, thời gian tính toán đòi hỏi là quá lớn (lên tới hàng trăm giờ CPU), trở thành nút thắt cổ chai cản trở việc ứng dụng thực tế và dự đoán nhanh chóng của phương pháp $\text{XDLVO}$ nâng cao, buộc các nhà khoa học phải tìm kiếm giải pháp tính toán thay thế.

* **Động lực áp dụng mạng nơ-ron nhân tạo RBF (RBF ANN) như một bộ xấp xỉ vạn năng hiệu năng cao**:
  * Nguyên nhân gốc rễ dẫn đến sự bùng nổ thời gian tính toán trong phương pháp $\text{XDLVO}$ nâng cao bắt nguồn từ các mối quan hệ phi tuyến tính cực kỳ phức tạp giữa địa hình bề mặt vi mô (*surface topography*) và lực tương tác liên bề mặt (Cai et al., $2017\text{a}$; Teng et al., $2018\text{a}$; Zhao et al., $2015$).
  * Mạng nơ-ron nhân tạo (Artificial Neural Networks – $\text{ANN}$) là một công cụ thống kê và học máy mạnh mẽ lấy cảm hứng từ cấu trúc mạng thần kinh của não bộ con người (Iliyas et al., $2013$). Cấu trúc mạng trong $\text{ANN}$ có khả năng tự thích ứng và tự học (*self-learning*), cho phép tìm ra lời giải xấp xỉ tối ưu và chính xác nhất cho các mối quan hệ phi tuyến đa biến phức tạp (Curcio et al., $2006$; Dreiseitl và Ohno-Machado, $2002$; Iliyas et al., $2013$; Sun et al., $2018$).
  * Trong những năm gần đây, $\text{ANN}$ đã được ứng dụng rất thành công trong nhiều khía cạnh của công nghệ màng:
    * Kiểm soát quy trình siêu lọc ($\text{UF}$) và vi lọc ($\text{MF}$) (Basheer và Hajmeer, $2000$; Madaeni et al., $2010$);
    * Dự đoán hiệu suất lọc và độ suy giảm thông lượng của quá trình $\text{UF}$/$\text{MF}$ (Curcio et al., $2006$; Chew et al., $2018$);
    * Thiết lập mối tương quan giữa các yếu tố vận hành với hiện tượng tắc nghẽn màng (Corbatón-Báguena et al., $2016$);
    * Tối ưu hóa các thông số chế tạo màng polyme (Schmitt et al., $2018$).
  * Từ những tiền đề vững chắc đó, một giả thuyết khoa học quan trọng được đặt ra: $\text{ANN}$ có thể mô tả hoàn hảo mối quan hệ phi tuyến phức tạp giữa các đặc tính hóa lý bề mặt, hình thái độ nhám và các lực tương tác liên bề mặt trong quá trình bám dính chất bẩn.
  * Đặc biệt, mô hình mạng nơ-ron cơ sở bán kính (Radial Basis Function – $\text{RBF}$ $\text{ANN}$) có ưu thế vượt trội:
    * Đóng vai trò như một bộ xấp xỉ hàm vạn năng (*universal approximator*) có khả năng ánh xạ phi tuyến chính xác cao;
    * Tốc độ huấn luyện siêu nhanh, cấu trúc tầng ẩn dựa trên hàm kích hoạt cơ sở bán kính Gauss không đòi hỏi lặp lan truyền ngược gradient nhiều tầng phức tạp, giúp tránh được hoàn toàn nguy cơ rơi vào bẫy cực tiểu cục bộ (*local minima traps*) mà các mạng truyền thẳng nhiều tầng truyền thống ($\text{BP}$-$\text{ANN}$) thường gặp phải.
  * Một mạng $\text{ANN}$ sau khi được huấn luyện hoàn chỉnh có thể xuất trực tiếp kết quả năng lượng tương tác chỉ trong vài mili-giây, qua đó cắt giảm triệt để gánh nặng tính toán đồ sộ của phép tích phân số $\text{SEI}$.
  * Trước nghiên cứu này, chưa có bất kỳ công bố khoa học nào về việc khai thác và ứng dụng $\text{ANN}$ để dự đoán các tương tác liên bề mặt liên quan đến hiện tượng tắc nghẽn màng.

* **Mục tiêu nghiên cứu cốt lõi của bài báo (*Paper Objectives*)**:
  * Phát triển một mô hình mạng nơ-ron nhân tạo $\text{RBF}$ $\text{ANN}$ để dự đoán chính xác, tức thời và hiệu quả năng lượng tương tác liên bề mặt với bề mặt màng gồ ghề trong toàn bộ dải khoảng cách phân cách tầm ngắn từ $0{,}158\text{ nm}$ đến $10\text{ nm}$.
  * Sử dụng các mẫu chất gây tắc nghẽn bùn hoạt tính (*sludge foulants*) và màng phẳng poly(vinylidene fluoride) ($\text{PVDF}$) lấy trực tiếp từ hệ thống $\text{MBR}$ thực nghiệm để phục vụ tính toán và kiểm chứng.
  * Đặc trưng hóa toàn diện các đặc tính bề mặt của bùn và màng ($\text{PVDF}$), bao gồm thế zeta bề mặt, các thành phần năng lượng tự do bề mặt thông qua phép đo góc tiếp xúc, và cấu trúc độ nhám hình thái học bằng ảnh $\text{AFM}$.
  * Thiết lập cấu trúc và huấn luyện mạng $\text{RBF}$ $\text{ANN}$ để tính toán năng lượng tương tác giao diện dựa trên các thông số đầu vào gồm đặc tính bề mặt và khoảng cách phân cách $d$.
  * Minh chứng các lợi thế vượt trội của phương pháp $\text{RBF}$ $\text{ANN}$ thông qua việc so sánh đối chứng toàn diện với phương pháp tích phân số $\text{XDLVO}$ nâng cao về cả độ chính xác dự báo lẫn khả năng tiết kiệm thời gian tính toán.
