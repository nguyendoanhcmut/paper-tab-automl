## Appendix A. Supporting information

* Dữ liệu bổ trợ trực tuyến (Supplementary data):
  * Dữ liệu bổ trợ đi kèm bài báo được lưu trữ và truy cập công khai thông qua định danh đối tượng số $\text{doi:10.1016/j.jece.2026.123811}$.
  * Hồ sơ tài liệu bổ trợ (Supplementary Material) cung cấp các tập dữ liệu thực nghiệm chi tiết trong $120\text{ ngày}$ vận hành liên tục của hệ thống bể phản ứng sinh học màng kỵ khí nhiệt độ trung bình ($35 \pm 2^\circ\text{C}$, mesophilic AnMBR) xử lý nước rỉ rác trạm trung chuyển chất thải rắn sinh hoạt tại thành phố Trường Sa, tỉnh Hồ Nam.
  * Các nội dung bổ trợ bao gồm phân tích đặc tính lý hóa nước nạp, thống kê mô tả độ biến động thông số quá trình, kiểm định năng lực ngoại suy theo chuỗi thời gian, động thái tích tụ chất hữu cơ gây nghẹt màng, cấu trúc vi sinh vật và phân tích phần dư mô hình học máy (machine learning - ML).
* Tuyên bố về tính khả dụng của dữ liệu (Data availability):
  * Dữ liệu nghiên cứu, chuỗi số liệu vận hành và cấu hình mô hình học máy được cung cấp khi có yêu cầu hợp lý gửi trực tiếp đến các tác giả nghiên cứu ($\text{Data will be made available on request}$).
  * Việc chia sẻ dữ liệu theo yêu cầu nhằm đảm bảo tính minh bạch khoa học, tạo điều kiện thẩm định độc lập và hỗ trợ mở rộng ứng dụng mô hình hóa trong lĩnh vực xử lý nước thải nồng độ cao bằng công nghệ màng sinh học.
* Danh mục các bảng dữ liệu bổ trợ (Supplementary Tables):
  * Bảng bổ trợ S1 (Table S1) - Tóm tắt đặc tính hóa lý cơ bản của nước rỉ rác thô đầu vào:
    * Nguồn nước rỉ rác thu thập từ trạm trung chuyển rác thải sinh hoạt đô thị có thành phần phức tạp và biến động theo chu kỳ nén ép rác.
    * Nhu cầu oxy hóa học đầu vào ($\text{influent COD}$) trung bình đạt $10684\text{ mg/L}$, với dải biến động từ $6230\text{ mg/L}$ đến $16720\text{ mg/L}$.
    * Nồng độ amoni đầu vào ($\text{influent NH}_4^+-\text{N}$) duy trì ở mức cao từ $1200\text{ mg/L}$ đến $1850\text{ mg/L}$, tạo áp lực tích tụ amonia tự do tiềm ẩn trong hệ thống kỵ khí.
    * Giá trị pH của nước rỉ rác đầu vào dao động từ $6.1$ đến $7.4$.
  * Bảng bổ trợ S2 (Table S2) - Thống kê mô tả các thông số vận hành và chỉ tiêu chất lượng nước trong $120\text{ ngày}$:
    * COD đầu vào ghi nhận giá trị trung bình $10684\text{ mg/L}$ với hệ số biến thiên ($\text{CV}$) là $26.2\%$, cho thấy tải lượng hữu cơ biến đổi vừa phải theo nguồn thải.
    * COD dòng ra đạt hệ số biến thiên cao $\text{CV} = 90.6\%$, phản ánh sự dao động rõ nét của hiệu suất xử lý qua các pha tải trọng khác nhau khi thời gian lưu thủy lực (HRT) giảm từ $15\text{ ngày}$ xuống $5\text{ ngày}$ và tải trọng hữu cơ (OLR) tăng từ $4.5\text{ kg COD/m}^3\cdot\text{d}$ lên $8.0\text{ kg COD/m}^3\cdot\text{d}$.
    * Thế oxy hóa - khử (oxidation-reduction potential - ORP) duy trì trong dải khử âm sâu từ $-510\text{ mV}$ đến $-378\text{ mV}$ với hệ số biến thiên rất thấp $\text{CV} = 6.1\%$, xác nhận điều kiện kỵ khí sinh methane bên trong bể phản ứng diễn ra liên tục và ổn định.
    * Áp suất xuyên màng (transmembrane pressure - TMP) khởi đầu ở mức thấp $2.0\text{ kPa}$ và tăng lên tới $32.5\text{ kPa}$ trong giai đoạn nghẹt màng nghiêm trọng ở HRT ngắn.
  * Bảng bổ trợ S3 (Table S3) - Đánh giá kiểm định ngoại suy theo chuỗi thời gian dưới điều kiện sốc tải trọng của Giai đoạn III (Phase III shock-loading extrapolation test):
    * Tập dữ liệu được phân chia theo trình tự thời gian: $103\text{ mẫu}$ thuộc Giai đoạn I và II dùng để huấn luyện mô hình, trong khi $16\text{ mẫu}$ thuộc Giai đoạn III đóng vai trò tập kiểm tra độc lập nhằm đánh giá khả năng ứng phó với điều kiện sốc tải bất thường.
    * Kết quả dự đoán COD dòng ra và TMP bằng cả ba mô hình - rừng ngẫu nhiên (random forest - RF), extreme gradient boosting (XGBoost) và mạng nơ-ron nhân tạo (artificial neural network - ANN) - đều cho hệ số xác định âm ($R^2 < 0$) trên tập kiểm tra Giai đoạn III.
    * Phát hiện này chỉ ra rằng các mô hình học máy tuy có độ chính xác nội suy cao trong phạm vi dữ liệu phân bố quen thuộc (đạt $R^2 = 0.96$ với COD và $R^2 = 0.88$ với TMP trong kiểm định phân chia ngẫu nhiên $80:20$), nhưng bị suy giảm hiệu năng rõ rệt khi ngoại suy sang các kịch bản sốc tải vượt khỏi miền dữ liệu đã học.
* Danh mục các hình ảnh bổ trợ (Supplementary Figures):
  * Hình bổ trợ S1 (Fig. S1) - Diễn biến tích tụ các chất polyme ngoại bào (EPS) và sản phẩm vi sinh vật hòa tan (SMP):
    * Định lượng nồng độ SMP, EPS liên kết lỏng lẻo (LB-EPS) và EPS liên kết chặt chẽ (TB-EPS) trong bùn hoạt tính kỵ khí và bùn bám màng.
    * Khi HRT giảm từ $9.5\text{ ngày}$ xuống $5\text{ ngày}$, hàm lượng của cả ba thành phần SMP, LB-EPS và TB-EPS đều gia tăng rõ rệt, do vi sinh vật tiết nhiều chất ngoại bào dưới áp lực tải trọng cao, làm gia tăng trở lực lọc của màng.
  * Hình bổ trợ S2 (Fig. S2) - Hiệu quả phục hồi tính thấm màng qua các công đoạn làm sạch:
    * Khảo sát độ dốc trở lực lọc ($K$-value) và độ suy giảm áp suất xuyên màng sau từng bước vệ sinh màng sợi rỗng polyvinylidene fluoride (PVDF).
    * Rửa vật lý chỉ giúp loại bỏ lớp cặn lỏng lẻo bề mặt và khôi phục một phần nhỏ độ thấm.
    * Quy trình rửa hóa chất kết hợp natri hypoclorit ($\text{NaClO}$) để oxy hóa hợp chất hữu cơ và axit citric để hòa tan cặn khoáng vô cơ mang lại hiệu quả tái tạo tính thấm cao nhất cho module màng.
  * Hình bổ trợ S3 (Fig. S3) - Động thái cấu trúc quần thể vi sinh vật và dự đoán chức năng sinh học:
    * Kết quả giải trình tự gen 16S rRNA ở cấp độ ngành (phylum) và lớp (class) cho thấy ngành Firmicutes chiếm tỷ lệ ưu thế cao và liên tục, thúc đẩy quá trình thủy phân và axit hóa các phân tử hữu cơ.
    * Ngành Proteobacteria giảm tỷ lệ tương đối khi HRT bị rút ngắn, gắn liền với sự tích tụ các hợp chất dạng mùn khó phân hủy.
    * Ngành Chloroflexi tăng trưởng mạnh từ $6.6\%$ lên $37.5\%$, cùng sự phong phú của họ Anaerolineaceae - nhóm vi khuẩn sợi tham gia định hình cấu trúc bùn, tăng tiết EPS và tạo lớp bánh bùn dày đặc gây tắc nghẽn màng.
  * Hình bổ trợ S4 (Fig. S4) - Phân tích phân bố phần dư (residual analysis) trên tập kiểm tra độc lập:
    * Phân tích phần dư COD dòng ra (bảng điều khiển a–c): Sai số phần dư của mô hình RF phân bố đối xứng và tập trung chặt chẽ quanh trục giá trị $0$, thể hiện độ ổn định cao trên toàn dải nồng độ COD, trong khi XGBoost và ANN cho độ phân tán sai số lớn hơn.
    * Phân tích phần dư áp suất xuyên màng TMP (bảng điều khiển d–f): Mô hình RF duy trì dải phân bố phần dư hẹp nhất so với XGBoost và ANN, mặc dù độ phân tán tăng dần ở mức TMP cao phản ánh tính bất định lớn hơn của hiện tượng nghẹt màng phi tuyến tính.
  * Hình bổ trợ S5 (Fig. S5) - Biểu đồ giá trị SHAP tuyệt đối trung bình (mean absolute SHAP values):
    * Lượng hóa mức độ đóng góp toàn cục của sáu biến số đầu vào trong mô hình RF tối ưu hóa.
    * Đối với bài toán dự đoán COD dòng ra: Thứ tự tầm quan trọng của các đặc trưng được xếp theo mức độ giảm dần là $\text{OLR} > \text{HRT} > \text{ORP} > \text{influent NH}_4^+-\text{N} > \text{influent COD} > \text{influent pH}$.
    * Đối với bài toán dự đoán TMP: Thứ tự tầm quan trọng của các đặc trưng được xếp theo mức độ giảm dần là $\text{effluent NH}_4^+-\text{N} > \text{effluent pH} > \text{ORP} > \text{influent pH} > \text{influent COD} > \text{influent NH}_4^+-\text{N}$.
