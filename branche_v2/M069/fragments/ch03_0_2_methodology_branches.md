## 2. Methodology

* Nghiên cứu tuân theo một khung quy trình tích hợp gồm $4$ bước (four-step framework) nhằm mô hình hóa và kiểm soát chất lượng nước thải MPBR:
  * **Hình 1.** Quy trình 4 bước phát triển mô hình hồi quy logistic cho MPBR
    * <img src="assets/fig_01_p4.jpeg" alt="Hình 1" />
    * **Hình này chứng minh điều gì**
      * Chuỗi quy trình liên kết $N$ mô hình LR song song và tỷ số chênh ($OR$) vào vòng lặp thích ứng để tối ưu hóa tái sử dụng nước ($p_{reuse}$).
    * **Từ đâu mà thấy được**
      * Trục đọc từ trên xuống dưới qua 4 khối quy trình nối tiếp nhau bằng các mũi tên đỏ lớn (Step 1 đến Step 4).
      * Khối Step 2 biểu diễn mặt xác suất $p$ và bậc thang nồng độ $NH_4\text{-}N_{eff}$; khối Step 3 thể hiện đồ thị $OR$ theo nồng độ $0\text{--}16\text{ mg/L}$.
      * Khối Step 4 chứa chu trình mũi tên đỏ "iterative prediction" và đồ thị vận hành $0\text{--}100\text{ d}$ theo dõi xác suất tái sử dụng $p_{reuse}$.
  * Bước 1 (Step 1): Thu thập và tiền xử lý dữ liệu vận hành dài hạn từ hệ thống photobioreactor màng ngoài trời (outdoor membrane photobioreactor - MPBR).
    * Các dữ liệu thu thập bao gồm điều kiện dòng vào (tải nạp nitơ $NLR$, tải nạp phospho $PLR$), hoạt tính vi sinh vật (oxy hòa tan $DO$, oxy hòa tan cực đại $DO_{max}$), điều kiện môi trường xung quanh (bức xạ quang hợp hoạt dụng $PAR$, bức xạ cực đại $PAR_{max}$, nhiệt độ $T$, nhiệt độ cực đại $T_{max}$), thông số vận hành (thời gian lưu bùn $SRT$, thời gian lưu nước $HRT$, lưu lượng sục khí $F_{air}$), nồng độ amoni dòng ra ($NH_4\text{--}N_{eff}$), và thể tích nước tái sử dụng ($Q$).
  * Bước 2 (Step 2): Phát triển và kiểm định các mô hình hồi quy logistic (logistic regression - LR) song song phục vụ phân loại xác suất nồng độ $NH_4\text{--}N_{eff}$ và tiềm năng tái sử dụng nước ($p_{reuse}$).
    * Mô hình cho phép dự đoán nồng độ amoni dòng ra và xác suất tuân thủ ngưỡng quy chuẩn tái sử dụng dựa trên các biến đầu vào vận hành và môi trường.
  * Bước 3 (Step 3): Tiến hành phân tích độ nhạy cục bộ (local sensitivity analysis) và độ nhạy toàn cục (global sensitivity analysis) để nhận diện các biến số có ảnh hưởng then chốt và các tương tác giữa chúng.
    * Đánh giá định lượng tác động của từng thông số thông qua hệ số tỷ số chênh (odds ratio - $OR$) trên toàn bộ dải nồng độ $NH_4\text{--}N_{eff}$ từ $0$ đến $16\text{ mg N/L}$.
  * Bước 4 (Step 4): Đánh giá mô phỏng trên máy tính (in-silico evaluation) một chiến lược điều khiển giám sát đa biến (multivariable supervisory control strategy).
    * Chiến lược điều khiển tối ưu hóa đồng thời $4$ thông số then chốt gồm $SRT$, $HRT$, $F_{air}$ và $NLR$ nhằm cải thiện mức độ tuân thủ ngưỡng amoni và tối đa hóa sản lượng nước tái sử dụng.
* Khung phương pháp và chiến lược điều khiển được đánh giá xuyên suốt $4$ chiến dịch đo đạc vận hành thực nghiệm độc lập (Periods 1--4):
  * **Bảng 1.** Thông số vận hành thực nghiệm MPBR ngoài trời qua 4 giai đoạn
    * <img src="assets/table_01_p5.png" alt="Bảng 1" />
    * **Bảng này chứng minh điều gì**
      * Bốn chiến dịch cung cấp tập dữ liệu gồm 190 ngày vận hành với tải nạp nitơ ($NLR$) biến thiên từ $13.0$ đến $20.5\text{ gN}\cdot\text{d}^{-1}$.
    * **Từ đâu mà thấy được**
      * Các dòng Period 1–4, cột "Days of operation": thời gian vận hành lần lượt là 37, 36, 28 và 89 ngày.
      * Cột "NLR" và "$\text{F}_{\text{air}}$": tải nitơ cao nhất ở Period 4 ($20.5 \pm 5.1\text{ gN}\cdot\text{d}^{-1}$), lưu lượng sục khí duy trì $0.22\text{--}0.24\text{ vvm}$.
  * Giai đoạn 1 (Period 1, từ tháng 11/2016 đến tháng 01/2017, tổng cộng $37\text{ ngày}$ vận hành):
    * Mục tiêu nghiên cứu: Khảo sát ảnh hưởng của chiều dài đường truyền ánh sáng (light path) lên hiệu suất quang hợp của vi tảo.
    * Điều kiện vận hành thực nghiệm: $SRT = 4{,}5 \pm 0{,}2\text{ ngày}$, $HRT = 1{,}5 \pm 0{,}10\text{ ngày}$, $F_{air} = 0{,}23 \pm 0{,}01\text{ vvm}$, $NLR = 15{,}8 \pm 8{,}2\text{ gN}\cdot\text{d}^{-1}$.
  * Giai đoạn 2 (Period 2, từ tháng 01/2017 đến tháng 03/2017, tổng cộng $36\text{ ngày}$ vận hành):
    * Mục tiêu nghiên cứu: Tối ưu hóa các thông số $SRT/HRT$ phục vụ loại bỏ chất dinh dưỡng bằng vi tảo.
    * Điều kiện vận hành thực nghiệm: $SRT = 4{,}5\text{--}6\text{ ngày}$, $HRT = 1{,}5 \pm 0{,}10\text{ ngày}$, $F_{air} = 0{,}23 \pm 0{,}00\text{ vvm}$, $NLR = 13{,}0 \pm 2{,}8\text{ gN}\cdot\text{d}^{-1}$.
  * Giai đoạn 3 (Period 3, từ tháng 08/2017 đến tháng 09/2017, tổng cộng $28\text{ ngày}$ vận hành):
    * Mục tiêu nghiên cứu: Tiếp tục tối ưu hóa $SRT/HRT$ cho quá trình loại bỏ chất dinh dưỡng của vi tảo trong điều kiện bức xạ và nhiệt độ cao.
    * Điều kiện vận hành thực nghiệm: $SRT = 3 \pm 0{,}1\text{ ngày}$, $HRT = 1{,}25 \pm 0{,}10\text{ ngày}$, $F_{air} = 0{,}24 \pm 0{,}03\text{ vvm}$, $NLR = 16{,}0 \pm 2{,}4\text{ gN}\cdot\text{d}^{-1}$.
  * Giai đoạn 4 (Period 4, từ tháng 02/2018 đến tháng 05/2018, tổng cộng $89\text{ ngày}$ vận hành):
    * Mục tiêu nghiên cứu: Khảo sát ảnh hưởng của $SRT$ đến sự cạnh tranh giữa vi tảo và vi khuẩn oxy hóa amoni (ammonia-oxidizing bacteria - AOB).
    * Điều kiện vận hành thực nghiệm: $SRT = 2{,}5\text{--}4{,}5\text{ ngày}$, $HRT = 1{,}25 \pm 0{,}10\text{ ngày}$, $F_{air} = 0{,}22 \pm 0{,}04\text{ vvm}$, $NLR = 20{,}5 \pm 5{,}1\text{ gN}\cdot\text{d}^{-1}$.
