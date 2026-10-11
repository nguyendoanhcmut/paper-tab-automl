### 3.5. SHAP feature importance analysis

* Do mô hình rừng ngẫu nhiên ($\text{Random Forest - RF}$) đạt hiệu năng tập kiểm tra độc lập tốt nhất cho cả $\text{COD}$ nước ra và $\text{TMP}$, phương pháp phân tích $\text{SHAP}$ (SHAP analysis) được áp dụng cho các mô hình $\text{RF}$ cuối cùng nhằm giải thích các liên kết dự đoán ở cấp độ mô hình [19]:
  * Giá trị $\text{SHAP}$ tuyệt đối trung bình (mean absolute SHAP values) được trình bày tại Fig. S5, trong khi các biểu đồ tóm tắt $\text{SHAP}$ (SHAP summary plots) được thể hiện ở Fig. 5.
* Phân tích $\text{SHAP}$ đối với bài toán dự đoán $\text{COD}$ nước ra xác định thứ bậc quan trọng của các biến đầu vào theo thứ tự giảm dần (Fig. 5a): $\text{OLR} > \text{HRT} > \text{ORP} > \text{influent NH}_4^+\text{-N} > \text{influent COD} > \text{influent pH}$:
  * **Hình 5.** Biểu đồ SHAP về tầm quan trọng của các biến số
    * <img src="assets/fig_05_p8.jpeg" alt="Hình 5" />
    * **Hình này chứng minh điều gì**
      * Xác định thứ bậc đóng góp: OLR chi phối lớn nhất đối với COD nước ra, $\text{Effluent NH}_4^+\text{-N}$ chi phối lớn nhất đối với TMP.
    * **Từ đâu mà thấy được**
      * Panel (a): Trục tung xếp độ quan trọng giảm dần ($\text{OLR} > \text{HRT} > \text{ORP}$); OLR có độ phân tán SHAP lớn nhất (đến $> 3000$).
      * Panel (b): Trục tung xếp $\text{Effluent NH}_4^+\text{-N} > \text{Effluent pH} > \text{ORP}$; dải SHAP của $\text{Effluent NH}_4^+\text{-N}$ trải rộng nhất (đến gần $1{,}0$).
  * Tải trọng thể tích hữu cơ (organic loading rate - $\text{OLR}$) thể hiện mức đóng góp lớn nhất vào đầu ra của mô hình:
    * Giá trị $\text{OLR}$ cao nhìn chung liên kết với các giá trị $\text{SHAP}$ dương và nồng độ $\text{COD}$ nước ra dự đoán cao hơn.
    * Giá trị $\text{OLR}$ thấp chủ yếu đóng góp các giá trị $\text{SHAP}$ âm, biểu thị nồng độ $\text{COD}$ nước ra dự đoán thấp hơn.
    * Quy luật này phù hợp với vai trò vận hành của tải trọng hữu cơ, khi tải trọng gia tăng làm tăng gánh nặng xử lý lên bể phản ứng và làm giảm hiệu suất loại bỏ $\text{COD}$.
  * Thời gian lưu thủy lực (hydraulic retention time - $\text{HRT}$) thể hiện xu hướng đối nghịch:
    * Giá trị $\text{HRT}$ dài hơn nhìn chung liên kết với các giá trị $\text{SHAP}$ âm và mức $\text{COD}$ dự đoán thấp hơn.
    * Điều này phù hợp với việc kéo dài thời gian tiếp xúc và cải thiện quá trình phân hủy sinh học (biodegradation) [20].
  * Thế oxy hóa khử (oxidation-reduction potential - $\text{ORP}$) đóng góp vào dự đoán $\text{COD}$:
    * Điều kiện khử mạnh hơn nhìn chung liên kết với nồng độ $\text{COD}$ dự đoán thấp hơn, phản ánh môi trường kỵ khí thuận lợi hơn cho quá trình phân hủy chất hữu cơ.
  * Do $\text{OLR}$, $\text{HRT}$ và $\text{COD}$ đầu vào ($\text{influent COD}$) có liên hệ vận hành với nhau, thứ bậc $\text{SHAP}$ được diễn giải là các mối liên kết mô hình học được thay vì các tác động nhân quả độc lập.
* Phân tích $\text{SHAP}$ đối với mô hình $\text{RF}$ dự đoán $\text{TMP}$ xác lập thứ bậc mức độ quan trọng rõ rệt giữa các biến số (Fig. 5b): $\text{effluent NH}_4^+\text{-N} > \text{effluent pH} > \text{ORP} > \text{influent pH} > \text{influent COD} > \text{influent NH}_4^+\text{-N}$:
  * Nồng độ amoni dòng ra ($\text{effluent NH}_4^+\text{-N}$) cao nhìn chung gắn liền với giá trị $\text{SHAP}$ dương, biểu thị mức $\text{TMP}$ dự đoán cao hơn; ngược lại, $\text{effluent NH}_4^+\text{-N}$ thấp đóng góp giá trị $\text{TMP}$ dự đoán thấp hơn.
  * Mối liên kết này được diễn giải thận trọng như một tín hiệu chẩn đoán trạng thái sinh học và hóa học của bể phản ứng, thay vì bằng chứng trực tiếp cho thấy $\text{NH}_4^+\text{-N}$ gây tắc nghẽn màng.
  * Amoni và amoni tự do (free ammonia) được ghi nhận gây ức chế hoạt tính vi sinh vật kỵ khí và làm biến đổi đặc tính bùn:
    * Tiền xử lý bằng amoni tự do có thể thúc đẩy quá trình hòa tan và thủy phân bùn [32].
    * Nồng độ amoni tự do ảnh hưởng đến sự sản sinh chất polymer ngoại bào (extracellular polymeric substances - $\text{EPS}$) và các đặc tính hóa lý của bùn [33].
    * Trong các hệ thống $\text{MBR}$ khử nitơ, $\text{EPS}$ và các chất chuyển hóa vi sinh vật gồm protein, polysaccharide và các chất humic góp phần làm gia tăng mức độ tắc nghẽn màng nghiêm trọng [34].
    * Thành phần $\text{EPS}$ và sự dịch chuyển quần xã vi sinh vật có liên quan chặt chẽ với độ ổn định của quá trình khử nitơ và sự kết tụ của bùn [35].
* Giá trị $\text{pH}$ dòng ra ($\text{effluent pH}$) và $\text{ORP}$ đóng góp đáng kể vào dự đoán $\text{TMP}$, cho thấy điều kiện axit-bazơ và trạng thái oxy hóa khử liên kết mật thiết với trạng thái tắc nghẽn màng:
  * Thông số $\text{pH}$ phản ánh nhiều quá trình gián tiếp nhưng liên quan chặt chẽ đến tắc nghẽn trong các hệ thống màng sinh học kỵ khí ($\text{AnMBR}$) xử lý nước thải nồng độ cao:
    * Cân bằng amoni tự do có thể gây ức chế hoạt tính sinh metan (methanogenic activity) và chi phối quá trình giải phóng các sản phẩm vi sinh vật hòa tan (soluble microbial products - $\text{SMP}$).
    * Điện tích bề mặt và xu hướng tạo gel của $\text{EPS}$ làm thay đổi độ nén chặt của lớp bánh bùn (cake layer) và trở lực lọc.
    * Quá trình kết tủa vô cơ tham gia cấu thành các lớp tắc nghẽn hỗn hợp hữu cơ - vô cơ.
  * Do $\text{effluent NH}_4^+\text{-N}$ và $\text{effluent pH}$ là các biến số ở hạ lưu hoặc được đo đồng thời, mô hình dự đoán $\text{TMP}$ cần được hiểu là mô hình cảm biến mềm chẩn đoán (diagnostic soft-sensing model) hơn là mô hình cảnh báo sớm dự báo tương lai khắt khe.
  * Kết quả $\text{SHAP}$ cung cấp các mối liên hệ có thể diễn giải được giữa các biến vận hành quan trắc định kỳ và hành vi biến thiên của $\text{TMP}$, nhưng không xác lập mối quan hệ nhân quả cơ chế độc lập.
* Phạm vi nghiên cứu và các giới hạn kỹ thuật được ghi nhận nhằm định hướng ứng dụng thực tế:
  * Mô hình được xây dựng trên dữ liệu từ một bể phản ứng quy mô phòng thí nghiệm đơn lẻ ($4\text{ L}$ thể tích làm việc) xử lý nước rỉ rác từ một trạm trung chuyển, do đó việc ngoại suy trực tiếp sang các hệ thống quy mô đầy đủ hoặc các thành phần nước rỉ rác khác cần được xem xét thận trọng.
  * Thời gian vận hành $120\text{ ngày}$, dù mang lại nhiều thông tin giá trị, vẫn bao quát khoảng điều kiện hẹp hơn so với các ứng dụng công nghiệp dài hạn điển hình.
  * Phân tích $\text{SHAP}$ chỉ giới hạn trong phạm vi các biến đầu vào sẵn có và chưa bao hàm các thông số sinh học hoặc hóa lý liên quan khác có thể chi phối hành vi hệ thống.
  * Sự tồn tại của hiện tượng cộng tuyến (collinearity), đặc biệt giữa $\text{OLR}$, $\text{HRT}$ và $\text{influent COD}$, có thể ảnh hưởng đến việc diễn giải tầm quan trọng của các đặc trưng; do đó kết quả $\text{SHAP}$ phục vụ việc hỗ trợ diễn giải mô hình thay vì thiết lập cơ chế nhân quả.
  * Các mô hình hiện tại dự đoán $\text{COD}$ nước ra và $\text{TMP}$ mà không trực tiếp tích hợp động học quần xã vi sinh vật hoặc dữ liệu thành phần chất gây tắc nghẽn màng.
  * Các nghiên cứu tương lai cần ưu tiên thu thập dữ liệu từ nhiều cấu hình $\text{AnMBR}$ đa dạng để nâng cao khả năng khái quát hóa của mô hình và cho phép áp dụng học chuyển giao (transfer learning).
  * Việc tích hợp các luồng dữ liệu đa tần số, quan trắc trực tuyến và các chỉ thị sinh học sẽ nâng cao hơn nữa khả năng dự đoán các biến chuyển hiệu năng nhanh và đặc tính tắc nghẽn màng.
