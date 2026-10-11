#### 3.4.1. Data characteristics and correlation analysis

* Thống kê mô tả xác định các quy luật biến thiên đặc thù giữa các thông số vận hành và các chỉ tiêu chất lượng nước (Bảng S2):
  * Nhu cầu oxy hóa học đầu vào (influent chemical oxygen demand - $\text{COD}$) có mức độ biến thiên trung bình với nồng độ trung bình $10684\text{ mg/L}$ và hệ số biến thiên (coefficient of variation - $\text{CV}$) là $26{,}2\%$, phản ánh điều kiện tải nạp hữu cơ dao động đáng kể.
  * $\text{COD}$ dòng ra (effluent $\text{COD}$) có $\text{CV}$ tương đối lớn hơn rõ rệt đạt $90{,}6\%$, thể hiện biên độ dao động rộng của hiệu suất xử lý qua các giai đoạn vận hành khác nhau, đặc biệt trong các giai đoạn sốc tải (shock loading).
  * Điều kiện môi trường trong hệ kỵ khí duy trì tính ổn định với thế oxy hóa khử (oxidation-reduction potential - $\text{ORP}$) liên tục âm từ $-510$ đến $-378\text{ mV}$ cùng $\text{CV}$ thấp ($6{,}1\%$), chứng minh trạng thái khử ổn định bên trong bể phản ứng.
  * Áp suất xuyên màng (transmembrane pressure - $\text{TMP}$) thể hiện độ biến thiên rất cao với $\text{CV} = 82\%$, cho thấy tắc nghẽn màng (membrane fouling) phát triển phi tuyến tính và phụ thuộc vào thời lượng của pha vận hành, gây khó khăn cho việc mô hình hóa dự báo.
  * Nồng độ $\text{NH}_4^+\text{-N}$ dòng ra gia tăng so với dòng vào chỉ ra hiện tượng tích tụ nitơ trong hệ thống và phản ánh năng lực khử nitơ hạn chế trong điều kiện kỵ khí nghiêm ngặt.
* Phân tích tương quan Pearson giữa các thông số đầu vào được lựa chọn cho hai mô hình dự báo thể hiện mức độ liên kết giữa các biến:
  * Đối với mô hình dự báo $\text{COD}$ dòng ra, các cặp thông số có tương quan chặt chẽ nhất gồm $\text{HRT}$ và tải nạp hữu cơ (organic loading rate - $\text{OLR}$) với $r = -0{,}98$, $\text{COD}$ đầu vào và $\text{OLR}$ với $r = 0{,}91$, cùng $\text{COD}$ đầu vào và $\text{NH}_4^+\text{-N}$ đầu vào với $r = 0{,}97$.
  * Sự liên kết toán học nội tại giải thích các hệ số tương quan cao này, do $\text{OLR}$ được tính trực tiếp từ nồng độ đầu vào và lưu lượng ($\text{OLR} = (\text{COD} \times Q)/V$ so với thời gian lưu thủy lực $\text{HRT} = V/Q$), trong đó tương quan âm rất mạnh giữa $\text{HRT}$ và $\text{OLR}$ ($r = -0{,}98$) phản ánh bản chất tỷ lệ nghịch toán học.
  * Thông số $\text{pH}$ đầu vào chỉ thể hiện tương quan yếu với các biến đầu vào khác ($r = -0{,}40\text{--}0{,}17$), cung cấp thông tin độc lập và đặc thù cho mô hình dự báo.
  * Ma trận tương quan Pearson giữa các thông số vận hành và chỉ tiêu chất lượng nước được thể hiện chi tiết trên bản đồ nhiệt:
    - **Hình 3.** Bản đồ nhiệt hệ số tương quan Pearson cho COD và TMP
      - <img src="assets/fig_03_p6.jpeg" alt="Hình 3" />
      - **Hình này chứng minh điều gì**
        - Ma trận xác định HRT và OLR tương quan nghịch ($r = -0.98$), COD đầu vào tương quan thuận với $\text{NH}_4^+$ đầu vào ($r = 0.97$) và OLR ($r = 0.91$); TMP tương quan nghịch với $\text{NH}_4^+$ dòng ra ($r = -0.63$), pH dòng ra ($r = -0.57$) và thuận với ORP ($r = 0.61$).
      - **Từ đâu mà thấy được**
        - Ma trận $10 \times 10$ ô với thanh màu từ $-1.00$ (xanh đậm) đến $1.00$ (đỏ đậm); đường chéo chính nhận giá trị $1.00$.
        - Cặp HRT–OLR màu xanh đậm ($-0.98$), Influent COD–Influent NH4 màu đỏ đậm ($0.97$); hàng TMP giao với Effluent NH4 màu xanh ($-0.63$), Effluent pH ($-0.57$) và ORP màu cam đỏ ($0.61$).
* Đối với mô hình dự báo $\text{TMP}$, cấu trúc tương quan thể hiện sự phân hóa rõ rệt so với mô hình dự báo $\text{COD}$:
  * Các biến có tương quan mạnh nhất với $\text{TMP}$ bao gồm $\text{NH}_4^+\text{-N}$ dòng ra với $r = -0{,}63$, $\text{ORP}$ với $r = 0{,}61$, và $\text{pH}$ dòng ra với $r = -0{,}57$.
  * Các thông số nước thải thô đầu vào chỉ thể hiện mức độ tương quan yếu với $\text{TMP}$ ($r = -0{,}44$).
  * Sự khác biệt này chứng minh tắc nghẽn màng chịu sự chi phối chủ yếu bởi các sản phẩm chuyển hóa sinh học (biological transformation products) và trạng thái oxy hóa khử (redox state), thay vì phụ thuộc trực tiếp vào các đặc tính ban đầu của nước thải thô.
  * Tương quan yếu giữa các thông số dòng vào và $\text{TMP}$ làm nổi bật bản chất đa diện và phức tạp của quá trình tắc nghẽn màng, đặt ra thách thức cho việc dự báo và khẳng định tính phù hợp của việc ứng dụng học máy (machine learning - $\text{ML}$) để thu nhận các mối quan hệ phi tuyến này.
