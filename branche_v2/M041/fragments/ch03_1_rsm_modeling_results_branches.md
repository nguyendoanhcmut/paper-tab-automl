### RSM modeling results

* **Cơ sở dữ liệu và thiết lập biến số trong mô hình hóa phương pháp bề mặt đáp ứng (Response Surface Methodology - RSM)**:
    * **Khả năng dự báo phản ứng của hệ thống**: Phản ứng ở các nồng độ cụ thể của từng nguyên tố có thể được dự báo bằng phương trình biểu diễn theo các yếu tố thực tế (actual factors).
    * **Biến phụ thuộc (dependent variables)**: Dữ liệu thực nghiệm từ nghiên cứu của Ding và cộng sự (Ding et al. 2026 / tham chiếu 26) về hàm lượng chất dinh dưỡng và hiệu suất loại bỏ được sử dụng làm các biến phụ thuộc.
    * **Biến độc lập (independent variables)**: Thời gian (Time), $\text{pH}$ và hàm lượng tổng carbon hữu cơ ($\text{TOC}$) được sử dụng làm các biến độc lập cho mô hình hóa RSM.
    * **Đơn vị đo lường**: Các mức giá trị của từng yếu tố được liệt kê theo các đơn vị gốc ban đầu (original units).
    * **Công cụ phần mềm và thu thập dữ liệu thống kê**: Phần mềm chuyên gia (Design-Expert) được sử dụng để xây dựng mô hình dự báo theo phương pháp RSM; các đồ thị và kết quả thống kê đều được trích xuất trực tiếp từ phần mềm này.
    * **Dạng mô hình quy định theo cặp biến số độc lập**:
        * Các Phương trình từ (1) đến (4) dựa trên hai biến thời gian và nồng độ $\text{TOC}$ được xây dựng theo mô hình bậc hai (quadratic model).
        * Các Phương trình từ (5) đến (8) dựa trên hai biến thời gian và $\text{pH}$ được xây dựng theo mô hình bậc ba (cubic model).

* **Hệ phương trình hồi quy bậc hai dự báo theo thời gian và nồng độ TOC (Phương trình 1–4)**:
    * **Phương trình (1) - Nồng độ amonia nitơ ($\text{mg/L}$)**:
        $$\text{Ammonia Nitrogen concentrations} = 17.63922 - 0.020773 \times [\text{TOC}] - 1.14294 \times \text{Time} - 0.002362 \times [\text{TOC}] \times \text{Time} - 0.000049 \times [\text{TOC}]^2 + 0.039948 \times \text{Time}^2 \quad (1)$$
    * **Phương trình (2) - Hiệu suất loại bỏ amonia nitơ ($\%$)**:
        $$\text{Removal efficiency} = -17.34990 + 0.125461 \times [\text{TOC}] + 7.58606 \times \text{Time} + 0.015832 \times [\text{TOC}] \times \text{Time} + 0.000430 \times [\text{TOC}]^2 - 0.265073 \times \text{Time}^2 \quad (2)$$
    * **Phương trình (3) - Nồng độ phosphat ($\text{mg/L}$)**:
        $$\text{Phosphate concentrations} = +4.00800 - 0.021655 \times [\text{TOC}] - 0.174407 \times \text{Time} - 0.000850 \times [\text{TOC}] \times \text{Time} + 0.000106 \times [\text{TOC}]^2 + 0.006695 \times \text{Time}^2 \quad (3)$$
    * **Phương trình (4) - Hiệu suất loại bỏ phosphat ($\%$)**:
        $$\text{Removal efficiency} = -33.09859 + 0.708943 \times [\text{TOC}] + 5.77748 \times \text{Time} + 0.028554 \times [\text{TOC}] \times \text{Time} - 0.003467 \times [\text{TOC}]^2 - 0.221934 \times \text{Time}^2 \quad (4)$$

* **Hệ phương trình hồi quy bậc ba dự báo theo thời gian và pH (Phương trình 5–8)**:
    * **Phương trình (5) - Nồng độ amonia nitơ ($\text{mg/L}$)**:
        $$\begin{aligned} \text{Ammonia Nitrogen concentrations} = & -334.89544 + 149.23601 \times \text{pH} + 0.151816 \times \text{Time} - 0.500580 \times \text{pH} \times \text{Time} \\ & - 20.88410 \times \text{pH}^2 + 0.049813 \times \text{Time}^2 + 0.040872 \times \text{pH}^2 \times \text{Time} \\ & - 0.004006 \times \text{pH} \times \text{Time}^2 + 0.959895 \times \text{pH}^3 + 0.000776 \times \text{Time}^3 \quad (5) \end{aligned}$$
    * **Phương trình (6) - Hiệu suất loại bỏ amonia nitơ ($\%$)**:
        $$\begin{aligned} \text{Removal efficiency} = & +2410.12044 - 1027.68992 \times \text{pH} - 1.34714 \times \text{Time} + 3.45763 \times \text{pH} \times \text{Time} \\ & + 143.75809 \times \text{pH}^2 - 0.335549 \times \text{Time}^2 - 0.282310 \times \text{pH}^2 \times \text{Time} \\ & + 0.027494 \times \text{pH} \times \text{Time}^2 - 6.60451 \times \text{pH}^3 - 0.005249 \times \text{Time}^3 \quad (6) \end{aligned}$$
    * **Phương trình (7) - Nồng độ phosphat ($\text{mg/L}$)**:
        $$\begin{aligned} \text{Phosphate concentrations} = & -80.57145 + 34.59074 \times \text{pH} + 0.962919 \times \text{Time} - 0.352554 \times \text{pH} \times \text{Time} \\ & - 4.70673 \times \text{pH}^2 + 0.011279 \times \text{Time}^2 + 0.024569 \times \text{pH}^2 \times \text{Time} \\ & - 0.000451 \times \text{pH} \times \text{Time}^2 + 0.210722 \times \text{pH}^3 + 0.000012 \times \text{Time}^3 \quad (7) \end{aligned}$$
    * **Phương trình (8) - Hiệu suất loại bỏ phosphat ($\%$)**:
        $$\begin{aligned} \text{Removal efficiency} = & +2866.96551 - 1187.60916 \times \text{pH} - 32.37146 \times \text{Time} + 11.83435 \times \text{pH} \times \text{Time} \\ & + 161.73271 \times \text{pH}^2 - 0.378165 \times \text{Time}^2 - 0.824916 \times \text{pH}^2 \times \text{Time} \\ & + 0.015573 \times \text{pH} \times \text{Time}^2 - 7.24769 \times \text{pH}^3 - 0.000457 \times \text{Time}^3 \quad (8) \end{aligned}$$

* **Kiểm định ANOVA và các thông số đánh giá độ chính xác của mô hình RSM**:
    * **Độ có ý nghĩa thống kê của mô hình theo thời gian và TOC**:
        * Giá trị chuẩn định $F$ ($F\text{-value}$) đạt $196.39$ đối với nồng độ amonia nitơ phụ thuộc vào thời gian và nồng độ $\text{TOC}$, chứng minh mô hình có ý nghĩa thống kê cao.
        * Hệ số xác định dự báo $R^2$ đạt $0.9541$ đối với hiệu suất loại bỏ amonia nitơ theo thời gian và nồng độ $\text{TOC}$, xác nhận mô hình RSM đạt độ chính xác tốt.
        * Giá trị $F$ đạt $131.15$ đối với nồng độ phosphat theo thời gian và nồng độ $\text{TOC}$, khẳng định ý nghĩa thống kê của phương trình hồi quy.
        * Hệ số $R^2$ dự báo ($R^2_{\text{pred}} = 0.9385$) và $R^2$ hiệu chỉnh ($R^2_{\text{adj}} = 0.9535$) đối với nồng độ phosphat theo thời gian và nồng độ $\text{TOC}$ có sự tương thích hợp lý với độ lệch nhỏ hơn $0.2$.
    * **Độ chính xác và độ có ý nghĩa của mô hình theo thời gian và pH**:
        * Hệ số $R^2$ hiệu chỉnh đối với nồng độ amonia nitơ theo thời gian và $\text{pH}$ đạt $0.9723$.
        * Các số hạng của mô hình (model terms) đối với hiệu suất loại bỏ amonia nitơ theo thời gian và $\text{pH}$ đạt mức có ý nghĩa thống kê khi giá trị $P$ nhỏ hơn $0.0500$ ($P\text{-value} < 0.0500$).
        * Giá trị $F$ đối với nồng độ phosphat theo thời gian và $\text{pH}$ đạt $140.81$.
        * Giá trị $F$ đối với hiệu suất loại bỏ phosphat theo thời gian và $\text{pH}$ đạt $140.83$.
        * Phương pháp tính tổng bình phương sai số: Sử dụng Loại III từng phần (Type III partial sum of squares).

* **Nồng độ amonia nitơ và hiệu suất loại bỏ nhạy cảm với biến thiên thời gian hơn so với nồng độ TOC trên đồ thị đường đồng mức (Hình 1)**:
    - **Hình 1.** Đồ thị đường đồng mức nồng độ và hiệu suất khử Amonia Nitơ
      - <img src="assets/fig_01_p4.png" alt="Hình 1" />
      - **Hình này chứng minh điều gì**
        - Nồng độ Amonia Nitơ giảm từ $15\text{ mg/L}$ xuống $< 5\text{ mg/L}$, hiệu suất khử tăng từ $0\,\%$ lên $> 80\,\%$ khi tăng thời gian lên $15$–$20\text{ ngày}$.
      - **Từ đâu mà thấy được**
        - Panel (a, b): Ox là TOC ($40$–$120\text{ mg/L}$), Oy là Time ($0$–$20\text{ ngày}$); hiệu suất (b) đạt $80\,\%$ khi TOC $> 100\text{ mg/L}$ và Time $> 15\text{ ngày}$.
        - Panel (c, d): Ox là pH ($5$–$9$), Oy là Time ($0$–$20\text{ ngày}$); hiệu suất (d) đạt $80$–$100\,\%$ (vùng màu đỏ) khi Time $> 15\text{ ngày}$.
    * **Đặc tính tương tác giữa thời gian và nồng độ TOC**:
        * Vì thời gian và nồng độ $\text{TOC}$ là hai biến số độc lập riêng biệt, khi thời gian được giữ cố định, chỉ ghi nhận những biến đổi rất nhỏ ở nồng độ amonia nitơ khi thay đổi nồng độ $\text{TOC}$.
        * Tuy nhiên, các biến động trở nên rõ rệt khi thời gian thay đổi trong khi nồng độ $\text{TOC}$ giữ nguyên, chứng minh nồng độ amonia nitơ nhạy cảm với sự thay đổi thời gian hơn là nồng độ $\text{TOC}$.
        * Khi giảm nồng độ $\text{TOC}$ theo thời gian, nồng độ amonia nitơ tăng lên.
        * Độ nhạy của cả hiệu suất loại bỏ và nồng độ amonia đối với thời gian đều lớn hơn độ nhạy đối với nồng độ $\text{TOC}$.
        * Ghi nhận một xu hướng đảo ngược đối với hiệu suất loại bỏ dựa trên sự thay đổi đồng thời của thời gian và nồng độ $\text{TOC}$.

* **Hiệu suất khử amonia nitơ tăng theo thời gian lưu và đạt đỉnh ở dải pH từ $5\text{--}6$ và $7.5\text{--}8.5$ trên đồ thị 3D (Hình 2)**:
    - **Hình 2.** Đồ thị bề mặt 3D nồng độ và hiệu suất khử Amonia Nitơ
      - <img src="assets/fig_02_p5.png" alt="Hình 2" />
      - **Hình này chứng minh điều gì**
        - Thời gian lưu kéo dài đến $20\text{ ngày}$ chi phối việc hạ nồng độ amonia về sát $0\text{ mg/L}$, ít bị TOC tác động.
      - **Từ đâu mà thấy được**
        - (a, b): Trục Time ($0$–$20\text{ ngày}$) và TOC ($40$–$120\text{ mg/L}$); mặt cong dốc mạnh theo trục thời gian.
        - (c, d): Trục pH ($5$–$9$) và Time ($0$–$20\text{ ngày}$); mặt cong dạng vòm uốn phi tuyến rõ rệt theo trục pH.
    * **Tác động của tương tác thời gian - pH**:
        * Trong trường hợp thời gian - $\text{pH}$ đóng vai trò biến độc lập, hiệu suất loại bỏ tăng dần theo thời gian.
        * Hiệu suất loại bỏ cao nhất được ghi nhận trong các khoảng $\text{pH}$ từ $5\text{--}6$ và $7.5\text{--}8.5$.
        * Ở điều kiện $\text{pH}$ cố định, mức thay đổi hiệu suất loại bỏ do thay đổi $\text{pH}$ thấp hơn so với khi cố định thời gian.
        * Nồng độ amonia nitơ thể hiện độ nhạy đối với biến thiên thời gian cao hơn so với nồng độ $\text{TOC}$.
    * **Cơ chế sinh học và hóa học loại bỏ chất dinh dưỡng trong MBR vi tảo**:
        * **Hấp thụ dinh dưỡng bởi tế bào vi tảo**: Được xem là cơ chế chủ đạo để loại bỏ chất dinh dưỡng trong xử lý nước thải bằng vi tảo, do nitơ và photpho là hai nguyên tố thiết yếu để tổng hợp các hợp chất sinh học nội bào.
        * **Tác động tích cực của hàm lượng TOC**: Sự gia tăng hàm lượng $\text{TOC}$ thúc đẩy tốc độ sinh trưởng của vi tảo, nâng cao năng lực hấp thụ chất ô nhiễm và thể hiện xu hướng tương đồng ở nồng độ amonia nitơ và tổng photpho trong nước thải.
        * **Các phản ứng hóa học hỗ trợ**: Một số phản ứng hóa học như kết tủa hóa học (chemical precipitation) và bay hơi amoniac (ammonia volatilization) có thể loại bỏ một phần nitơ và photpho khỏi nước thải; tuy nhiên các cơ chế hóa học này chủ yếu chịu sự chi phối từ các biến động $\text{pH}$ do quá trình tăng sinh của vi tảo tạo ra.

* **Nồng độ phosphat và hiệu suất loại bỏ chịu sự chi phối mạnh bởi thời gian hơn so với nồng độ TOC trên đồ thị đường đồng mức (Hình 3)**:
    - **Hình 3.** Đồ thị đường đồng mức nồng độ và hiệu suất khử Phosphate
      - <img src="assets/fig_03_p6.png" alt="Hình 3" />
      - **Hình này chứng minh điều gì**
        - Hiệu suất khử phosphate đạt cực đại (> $80\%$, nồng độ < $1\text{ mg/L}$) khi thời gian lưu $20\text{ ngày}$, TOC $120\text{ mg/L}$ và pH $6.5\text{--}8.0$.
      - **Từ đâu mà thấy được**
        - (a, b) $Ox$: TOC ($40\text{--}120\text{ mg/L}$), $Oy$: thời gian ($0\text{--}20\text{ ngày}$); hiệu suất tăng từ $0\%$ lên > $80\%$ ở góc trên bên phải.
        - (c, d) $Ox$: pH ($5\text{--}10$), $Oy$: thời gian ($0\text{--}20\text{ ngày}$); nồng độ giảm xuống < $1\text{ mg/L}$ và hiệu suất cao nhất tại pH $6.5\text{--}8.0$.
    * **Biến động của nồng độ phosphat theo thời gian và TOC**:
        * Với thời gian và nồng độ $\text{TOC}$ là các biến độc lập, mức độ biến đổi của nồng độ phosphat do thay đổi nồng độ $\text{TOC}$ là thấp trong chế độ thời gian cố định.
        * Hàm lượng $\text{TOC}$ trong hệ thống vẫn duy trì ở mức cao qua các mốc thời gian diễn tiến.
        * Nồng độ phosphat nhạy cảm với biến thiên thời gian hơn so với biến thiên nồng độ $\text{TOC}$.
        * Nồng độ amonia nitơ giảm dần theo thời gian và nồng độ $\text{TOC}$; việc giảm nồng độ $\text{TOC}$ theo thời gian làm nồng độ amonia nitơ tăng lên.
        * Nồng độ phosphat và hiệu suất loại bỏ đều nhạy với thời gian hơn là nồng độ $\text{TOC}$; ghi nhận xu hướng đảo ngược của hiệu suất loại bỏ dựa trên biến động của nồng độ $\text{TOC}$ và thời gian.
    * **Vai trò của tải lượng TOC đầu vào và pH đối với vi tảo**:
        * Hàm lượng $\text{TOC}$ dòng vào ảnh hưởng đáng kể đến hiệu suất loại bỏ amonia nitơ: Khi hàm lượng $\text{TOC}$ đầu vào tăng lên, hiệu suất loại bỏ amonia nitơ trong nước thải dần được cải thiện rõ rệt.
        * Độ $\text{pH}$ tác động mạnh mẽ đến sự sinh trưởng của chủng vi tảo *P. helgolandica tsingtaoensis*, từ đó quyết định hiệu quả loại bỏ các chất ô nhiễm.

* **Hiệu suất khử phosphat đạt tối đa trong các dải pH từ $5\text{--}5.5$ và $7.5\text{--}8$ theo mô hình bề mặt 3D (Hình 4)**:
    - **Hình 4.** Đồ thị bề mặt 3D nồng độ và hiệu suất khử Phosphate
      - <img src="assets/fig_05_p7.png" alt="Hình 4" />
      - **Hình này chứng minh điều gì**
        - Kéo dài thời gian đến $20\text{ ngày}$ hạ nồng độ photphat xuống dưới $1\text{ mg/L}$; chệch khỏi pH 7–8 làm hiệu suất sụt giảm rõ rệt.
      - **Từ đâu mà thấy được**
        - Panel (a, b): trục thời gian ($0\text{--}20\text{ ngày}$) và TOC ($40\text{--}120\text{ mg/L}$); hiệu suất (b) tạo vồng cực đại ở $20\text{ ngày}$.
        - Panel (c, d): trục thời gian ($0\text{--}20\text{ ngày}$) và pH ($5\text{--}10$); nồng độ (c) chạm đáy dưới $1\text{ mg/L}$ và hiệu suất (d) đạt đỉnh tại pH 7–8.
    * **Phân tích động thái khử phosphat theo không gian 3 chiều**:
        * Hiệu suất loại bỏ phosphat gia tăng theo thời gian khi thời gian - $\text{pH}$ được thiết lập làm biến độc lập.
        * Khoảng giá trị $\text{pH}$ từ $5\text{--}5.5$ và $7.5\text{--}8$ đem lại hiệu quả làm sạch tối đa (maximum clearance effectiveness).
        * Tại một mốc thời gian không đổi, mức độ biến đổi hiệu suất loại bỏ do thay đổi $\text{pH}$ gây ra cao hơn so với mức độ biến đổi khi giữ $\text{pH}$ không đổi.
        * Nồng độ phosphat thể hiện độ nhạy đối với biến thiên $\text{pH}$ cao hơn so với biến thiên thời gian.

* **Đánh giá mức độ phù hợp của mô hình qua đồ thị phần dư và tương quan thực tế - dự báo (Hình 5)**:
    - **Hình 5.** Đồ thị phần dư và tương quan thực tế - dự báo của RSM
      - <img src="assets/fig_04_p7.png" alt="Hình 5" />
      - **Hình này chứng minh điều gì**
        - Mô hình dự báo sát nồng độ ammonia nitrogen ở cả 3 mức TOC ($40$, $80$, $120\text{ mg/L}$).
      - **Từ đâu mà thấy được**
        - Panel (a): Ox giá trị thực nghiệm ($0$–$16\text{ mg/L}$), Oy RSM dự báo; các điểm bám sát Equality Line.
        - Panel (b): Ox RSM dự báo ($0$–$17.5\text{ mg/L}$), Oy phần dư; các điểm phân tán quanh Zero Line.
    - **Hình 5.** (tiếp theo) Đồ thị phần dư và kiểm định mô hình RSM
      - <img src="assets/fig_06_p8.png" alt="Hình 5 (tiếp theo)" />
      - **Hình này chứng minh điều gì**
        - Mô hình RSM dự báo sát nồng độ ammonia nitrogen theo pH (c, d) và phosphate theo TOC, pH (e–h).
      - **Từ đâu mà thấy được**
        - Panel (c, e, g): Ox giá trị thực nghiệm ($0$–$16\text{ mg/L}$ ammonia nitrogen, $0$–$3.5\text{ mg/L}$ phosphate), Oy RSM dự báo; các điểm bám sát Equality Line.
        - Panel (d, f, h): Ox RSM dự báo, Oy phần dư; các điểm phân tán sát Zero Line trong khoảng $[-1.5, 1.1]$ (ammonia) và $[-0.5, 0.4]$ (phosphate).
    * **Mô hình phần dư và thực tế - dự báo cho nồng độ amonia nitơ (Hình 5a và 5d)**:
        * Đồ thị mô hình phần dư và thực tế - dự báo phản ánh nồng độ amonia nitơ theo các mối quan hệ thời gian - nồng độ $\text{TOC}$ và thời gian - $\text{pH}$.
        * Mức độ tập trung của các điểm dữ liệu dọc theo đường chéo (diagonal line) đóng vai trò là thước đo chuẩn mực đánh giá kết quả thực nghiệm so với giá trị dự báo kỳ vọng.
        * Khoảng cách giữa các điểm chấm tới đường chéo phản ánh mức độ trùng khớp cao giữa giá trị thực nghiệm và dự đoán, khẳng định mô hình đề xuất có khả năng dự báo chuẩn xác nồng độ amonia nitơ theo thời gian và $\text{pH}$.
    * **Mô hình phần dư và thực tế - dự báo cho nồng độ phosphat (Hình 5e và 5h)**:
        * Đồ thị mô hình phần dư cùng các giá trị thực tế và dự báo của nồng độ phosphat tương ứng theo thời gian - nồng độ $\text{TOC}$ và thời gian - $\text{pH}$ tiếp tục chứng minh sự phân bố sát sao của các điểm quanh đường chéo.
        * Các dự đoán về động thái của nồng độ phosphat và amonia trong hệ thống MBR vi tảo được thiết lập từ bộ dữ liệu thực nghiệm đạt sự tương đồng và thống nhất rất cao.
