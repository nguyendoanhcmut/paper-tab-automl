## 4. Conclusions

* Nghiên cứu đã phát triển thành công khung mô hình hồi quy logistic (logistic regression - LR) dựa trên dữ liệu nhằm dự đoán theo xác suất nồng độ nitơ amoni dòng ra ($NH_4\text{–}N_{eff}$) và định lượng tiềm năng tái sử dụng nước trong hệ thống photobioreactor màng ngoài trời (outdoor membrane photobioreactor - MPBR, dung tích $470\text{ L}$) xử lý nước thải sinh hoạt tại Valencia:
  * Dựa trên $1{,}5\text{ năm}$ dữ liệu vận hành ở quy mô pilot, mô hình LR đã chứng minh khả năng dự báo và kiểm soát hiệu quả việc tuân thủ quy chuẩn amoni dòng ra ($NH_4\text{–}N_{eff} < 1{,}6\text{ mg N}\cdot\text{L}^{-1}$).
* Phân tích độ nhạy cục bộ (local sensitivity analysis) chỉ ra rằng hoạt tính quang hợp (oxy hòa tan trung bình và cực đại $DO$, $DO_{max}$) cùng nhiệt độ môi trường ($T$) tạo ra ảnh hưởng chi phối mạnh nhất lên $NH_4\text{–}N_{eff}$ dự đoán:
  * Tầm quan trọng của lưu lượng sục khí ($F_{air}$) gia tăng rõ rệt trong các đợt nồng độ amoni tăng cao (high-ammonium episodes).
  * Việc chỉ dựa thuần túy vào thời gian lưu thủy lực ($HRT$) và thời gian lưu bùn ($SRT$) là không đủ để duy trì hiệu suất vận hành tối ưu lâu dài dưới các điều kiện khí quyển ngoài trời biến động.
* Mô phỏng in-silico chiến lược điều khiển nâng cao — tối ưu hóa đồng thời 4 thông số: $SRT$, $HRT$, tải trọng nitơ ($NLR$) và $F_{air}$ — mang lại những cải thiện định lượng vượt bậc so với phương thức vận hành cố định thông số:
  * Dự phóng giảm $12\text{--}50\%$ nồng độ $NH_4\text{–}N_{eff}$ và giảm $32\text{--}38\%$ nhu cầu sục khí (aeration demand), qua đó tối đa hóa sản lượng nước thu hồi đạt chuẩn tái sử dụng ($p_{reuse}$).
  * Tiết kiệm $25\text{--}30\%$ năng lượng tiêu thụ (giảm từ $0{,}369\text{ kWh}\cdot\text{m}^{-3}$ xuống còn $0{,}260\text{--}0{,}277\text{ kWh}\cdot\text{m}^{-3}$) và gia tăng sản lượng nước tái sử dụng lên tới $750\text{ L}\cdot\text{m}^{-3}$ (mức tăng $5\text{--}67\%$).
* Khung điều khiển hồi quy logistic (LR) có thể triển khai thực tế trên hệ thống SCADA thông qua 5 kịch bản thu thập dữ liệu với các mức độ tự động hóa khác nhau từ mạng cảm biến cơ bản đến cấu hình lai nâng cao:
  * **Bảng 3.** Các kịch bản thu thập dữ liệu tích hợp khung điều khiển LR với hệ thống SCADA
    * <img src="assets/table_03_p18.png" alt="Bảng 3" />
    * **Bảng này chứng minh điều gì**
      * Cơ chế bù trừ giữa dữ liệu đo online và mô hình dự đoán: cơ sở hạ tầng cảm biến càng tối giản thì vai trò của cảm biến ảo càng tăng để duy trì đầu vào cho mô hình LR.
    * **Từ đâu mà thấy được**
      * Cột "Online measurements": giảm từ đầy đủ 7 biến ($Q$, $TN$, $DO$, $T$, $PAR$, $Q_w$, $X_w$) ở kịch bản A xuống tối thiểu chỉ gồm $Q$ và $T$ ở kịch bản E.
      * Cột "Predictive models or virtual sensors": chuyển từ không cần ("Not required") ở kịch bản A-B sang ước tính phần lớn biến ($DO$, $PAR$, $TN$, $TP$, $OD_{680}$) ở kịch bản E.
  * Các cấp độ thiết bị trải dài từ tự động hóa cao (kịch bản A: đo online $Q$, $TN$, $DO$, $T$, $PAR$, $Q_w$, $X_w$), tự động hóa trung bình (kịch bản B), mạng cảm biến cơ bản (kịch bản C: đo $Q$, $DO$, $T$, lưu lượng thải kết hợp ước tính $PAR$ từ dữ liệu khí tượng), đến cấu hình chuỗi thời gian lai (kịch bản D và E: chỉ cần đo online $Q$, $DO$, $T$ hoặc $Q$, $T$, kết hợp cảm biến ảo ước tính $DO$, $PAR$, $TN$, $TP$, $OD_{680}$ và đo kiểm định kỳ trong phòng thí nghiệm để hiệu chuẩn lại).
* Khung LR mở ra hướng tiếp cận triển vọng và có tính diễn giải cao (highly interpretable) thay thế các mô hình cơ chế phức tạp hoặc các thuật toán học máy "hộp đen" (black-box machine learning):
  * Giới hạn và phạm vi ứng dụng: phương pháp luận mới được thẩm định trên dữ liệu pilot và mô phỏng tính toán, do đó cần được kiểm chứng thêm trên các thiết kế bể phản ứng quy mô thực tế (full-scale), các đặc tính nước thải đầu vào biến động và các điều kiện khí hậu khác nhau.
