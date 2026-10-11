#### 3.1.1. Identification of the most influential variables on ammonia removal

* Mô hình mạng nơ-ron nhân tạo (ANN - Artificial Neural Network) và phân tích thành phần chính (PCA - Principal Components Analysis) được phát triển nhằm nhận diện các biến số then chốt chi phối hiệu quả loại bỏ amoni (ammonia removal) trong hệ thống MBR.
* Kiến trúc mô hình ANN và phân bố trọng số khớp thần kinh (synaptic weights) (Fig. 3):
  - **Hình 3.** Kiến trúc mạng ANN và trọng số khớp thần kinh
    - <img src="assets/fig_03_p6.jpeg" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - Mô hình thiết lập cấu trúc gồm 13 biến đầu vào, 2 lớp ẩn (12 và 7 nơ-ron), 1 đầu ra removal cùng các số hạng chệch bias.
    - **Từ đâu mà thấy được**
      - Đọc từ trái sang phải: 13 biến vận hành đầu vào (từ filt đến perm), qua 2 lớp ẩn (12 và 7 nơ-ron), đến nơ-ron đầu ra removal.
      - Đường nối màu đen ghi nhận trọng số khớp thần kinh; đường màu xanh lam từ nút tròn $1$ biểu thị các số hạng chệch (bias).
  * Các đường liên kết màu đen thể hiện các kết nối giữa từng lớp và trọng số khớp thần kinh trên mỗi kết nối.
  * Các đường màu xanh lam biểu diễn số hạng chệch (bias term) được bổ sung ở từng bước tính toán của mạng.
* Hiệu năng hội tụ và sai số dự đoán của mô hình ANN (Fig. 4):
  * Mô hình đạt kết quả tốt trong việc mô phỏng ứng xử của MBR, ghi nhận sai số tuyệt đối trung bình MAE (Mean Absolute Error) ở mức hợp lý (bậc độ lớn $10^{-2}$) và sai số toàn phương trung bình MSE (Mean Squared Error) ở bậc độ lớn $10^{-4}$ (order of magnitude 10−4 (hình ghi MSE khoảng 20–30 (trục Oy 0–700), MAE khoảng 1–2 (trục Oy 0–24))), như minh họa tại Fig. 4:
  - **Hình 4.** Sai số MAE và MSE trong huấn luyện mô hình ANN
    - <img src="assets/fig_04_p7.jpeg" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Sai số giảm dốc đứng trong $10\text{--}15$ epoch đầu và tiệm cận ổn định từ epoch $20$ trên cả hai tập dữ liệu.
    - **Từ đâu mà thấy được**
      - Ox: số epoch ($0\text{--}100$). Oy: đồ thị trên biểu diễn MSE ($0\text{--}700$), đồ thị dưới biểu diễn MAE ($0\text{--}24$).
      - MSE tập training giảm từ $\sim 680$ về $\sim 20$, MAE giảm từ $\sim 22$ về $\sim 1.5$; đường cong phẳng dần sau epoch $15$.
      - Lưu ý: hình ghi MSE khoảng $20\text{--}30$ và MAE khoảng $1\text{--}2$, văn bản ghi bậc $10^{-4}$.
  * Quá trình học (learning process) và sự tiến triển của mô hình ANN qua các giai đoạn huấn luyện (training) và kiểm định (validation) ghi nhận sự sụt giảm đáng kể của cả MAE và MSE.
  * Sự suy giảm đồng thời của MAE và MSE chứng minh mô hình tự hiệu chỉnh thích ứng chặt chẽ với dữ liệu thực nghiệm và học được các quy luật tiềm ẩn.
* Phân tích thành phần chính PCA: Scree plot, tiêu chí lựa chọn và phương sai giải thích (Fig. 5):
  * Đồ thị đoạn dốc (scree plot) xác định số lượng thành phần chính (PC - Principal Component) được giữ lại (Fig. 5a):
    * Tiêu chí Kaiser (Kaiser criterion): các PC có giá trị riêng (eigenvalue) lớn hơn 1 được giữ lại [51].
    * Phép thử đoạn dốc (scree test): giữ lại các PC nằm trước điểm khuỷu (elbow point) trên đường cong scree plot [52].
    * Ba thành phần chính đầu tiên ($PC_1$, $PC_2$, $PC_3$) đều thỏa mãn đồng thời cả hai tiêu chí trên.
  * Đánh giá hệ số xác định $R^2$ và mức độ gia tăng độ phức tạp mô hình (Fig. 5b):
    * Bổ sung thêm các PC sau thành phần thứ ba không mang lại ý nghĩa thực tiễn, do giá trị $R^2$ không gia tăng đủ nhiều để biện minh cho độ phức tạp cao hơn của mô hình (Fig. 5):
  - **Hình 5.** Scree plot và giá trị $R^2$ của mô hình PCA
    - <img src="assets/fig_05_p7.jpeg" alt="Hình 5" />
    - **Hình này chứng minh điều gì**
      - 3 thành phần chính đầu tiên tối ưu để giữ lại thông tin với eigenvalue $> 1$ và $R^2 > 0.75$.
    - **Từ đâu mà thấy được**
      - Panel (a): PC 1–3 có eigenvalue $> 1$ ($3.04$, $2.43$, $1.18$) và giải thích lần lượt $22.9\ \%$, $17.8\ \%$, $9.8\ \%$ biến thiên.
      - Panel (b): Cột $R^2$ vượt $0.75$ ở PC 3; điểm cải thiện $R^2$ giảm từ $1.00$ xuống dưới $0.10$ ở PC 4.
    * Đồ thị chỉ hiển thị 10 PC đầu tiên nhằm mục đích đơn giản hóa; mục tiêu chính của PCA là giảm số chiều dữ liệu (data dimensionality reduction), do đó giữ lại càng ít thành phần càng tối ưu chừng nào sự thất thoát thông tin nằm trong ngưỡng chấp nhận được.
    * Với 3 PC đầu tiên, mô hình giải thích được $55\%$ tổng biến thiên của dữ liệu (data variation), đủ để khảo sát các mối liên hệ mạnh nhất giữa các biến số [57].
    * Mô hình PCA đạt hiệu năng thỏa đáng với hệ số xác định $R^2 = 0{,}772$, được đánh giá là mức độ tốt theo tiêu chuẩn của Eriksson et al. [58].
* Xếp hạng mức độ quan trọng tương đối của các biến đầu vào theo mô hình ANN (Fig. 6):
  * Phân tích độ nhạy (sensitivity analysis) từ mô hình ANN xác lập thứ tự tầm quan trọng tương đối đối với hiệu quả loại bỏ amoni (Fig. 6):
  - **Hình 6.** Tầm quan trọng tương đối của các biến đầu vào ANN
    - <img src="assets/fig_06_p8.jpeg" alt="Hình 6" />
    - **Hình này chứng minh điều gì**
      - SRT và fCOD có tầm quan trọng tương đối cao nhất đối với mô hình loại bỏ amoni, trong khi phosp thấp nhất.
    - **Từ đâu mà thấy được**
      - Ox: tầm quan trọng tương đối, thang đo $0.0$–$1.0$. Oy: 10 biến đầu vào theo thứ tự giảm dần.
      - Chiều dài thanh ngang đạt cực đại tại SRT ($1.0$), kế tiếp là fCOD ($\sim 0.95$), và thấp nhất tại phosp ($\sim 0.64$).
  * Chỉ 10 biến đầu vào quan trọng nhất được biểu diễn trên biểu đồ nhằm mục đích đơn giản hóa, do tầm quan trọng tương đối của các biến còn lại ở mức quá thấp.
* Phân tích tương quan giữa các biến vận hành và hiệu quả loại bỏ amoni theo mô hình PCA (Fig. 7):
  * Biểu đồ tải trọng (loading plot) từ mô hình PCA làm sáng tỏ các mối tương quan qua lại giữa các biến số (Fig. 7):
  - **Hình 7.** Tương quan PCA giữa các biến và loại bỏ amoni
    - <img src="assets/fig_07_p9.jpeg" alt="Hình 7" />
    - **Hình này chứng minh điều gì**
      - Các thành phần PC1–PC3 lượng hóa tương quan giữa biến vận hành và loại bỏ amoni qua góc kẹp véc-tơ ($0^\circ$ thuận, $90^\circ$ độc lập, $180^\circ$ nghịch).
    - **Từ đâu mà thấy được**
      - Trục tọa độ: 3 vòng tròn tương quan biểu diễn các cặp PC1 ($22.9\ \%$), PC2 ($17.8\ \%$) và PC3 ($9.8\ \%$) trong dải $[-1.0, 1.0]$.
      - Véc-tơ removal (giải thích biến thiên $\ge 0.4$) nằm cùng góc phần tư với temp và ammonia, ngược hướng với perm và fCOD.
  * Mối quan hệ tương quan được chỉ thị bởi góc giữa các mũi tên véc-tơ: góc $0^\circ$ tương ứng tương quan thuận hoàn toàn, góc $90^\circ$ tương ứng không tương quan (độc lập), và góc $180^\circ$ tương ứng tương quan nghịch hoàn toàn.
* Nhận diện các biến có ảnh hưởng chi phối lớn nhất đến loại bỏ amoni:
  * Theo đồng thuận của cả hai mô hình ANN và PCA:
    * Các biến có tác động tích cực lớn nhất đến loại bỏ amoni là thời gian lưu bùn (SRT - sludge retention time), nhiệt độ vận hành (operating temperature), và nồng độ amoni đầu vào (influent ammonia concentration).
    * Các biến có tác động tiêu cực đáng kể nhất gồm nồng độ COD đầu vào (influent COD), nồng độ dầu mỡ đầu vào (OG - oil and grease), và độ thấm của màng (membrane permeability).
  * Đối chiếu với mô hình ANN của Zhang, Chen và Jiang [14–16]:
    * Các tác giả ứng dụng mô hình ANN dự đoán hiệu suất loại bỏ amoni trong các trạm xử lý nước thải (WWTP - wastewater treatment plants) áp dụng các quy trình sinh học khác nhau dựa trên 5 biến: lưu lượng dòng vào (inlet flow rate), pH, nồng độ amoni đầu vào, COD và nồng độ tổng phospho.
    * Kết quả của Zhang et al. cũng ghi nhận COD đầu vào là yếu tố ảnh hưởng chủ đạo (phù hợp với nghiên cứu này); tuy nhiên, nồng độ amoni đầu vào trong nghiên cứu của họ lại không ảnh hưởng đáng kể đến hiệu quả loại bỏ, trái ngược với kết quả ghi nhận tại hệ thống MBR này.
* Cơ chế giải thích ảnh hưởng mạnh của nồng độ amoni đầu vào (influent ammonia concentration):
  * Nồng độ amoni cao trong dòng nạp thúc đẩy động học của phản ứng nitrat hóa (nitrification reaction kinetics) [59].
  * Làm tăng tốc độ sinh trưởng của vi khuẩn nitrat hóa theo mô hình động học Monod (Monod's relation).
  * Nồng độ amoni cao hơn trong nước thải cấp vào bể MBR trực tiếp làm tăng tải lượng amoni bị oxy hóa (oxidized ammonia load) [60].
* Cơ chế giải thích ảnh hưởng của nhiệt độ vận hành (operating temperature) và biến động pH:
  * Tốc độ sinh trưởng của vi khuẩn nitrat hóa gia tăng theo hàm mũ theo nhiệt độ [61], giải thích vai trò ảnh hưởng vượt trội của nhiệt độ đến hiệu quả loại bỏ amoni.
  * Nghiên cứu của Leite [62] về các yếu tố chi phối loại bỏ amoni trong nước thải lọc dầu bằng phân tích thống kê đa biến (đánh giá DO, pH, nhiệt độ, amoni đầu vào, phenol, sunfua, OG và COD) cũng ghi nhận mối quan hệ tương quan thuận rất mạnh giữa nhiệt độ vận hành và hiệu quả xử lý amoni.
  * Phản ứng nitrat hóa sinh ra ion $\text{H}^+$ như một sản phẩm cuối cùng, trực tiếp làm giảm giá trị pH môi trường, lý giải mối tương quan nghịch giữa loại bỏ amoni và pH (quan sát này cũng phù hợp với công bố của Leite [62]).
  * Sự suy giảm pH là một hàm số phụ thuộc vào độ kiềm (alkalinity) [59]; tuy nhiên cơ sở dữ liệu thực nghiệm không có đủ dữ liệu độ kiềm để tiếp tục đánh giá sâu hơn mối liên hệ này.
* Cơ chế giải thích tương quan thuận mạnh mẽ của thời gian lưu bùn (SRT):
  * Ưu điểm cốt lõi của công nghệ MBR so với công nghệ bùn hoạt tính truyền thống CAS (conventional activated sludge) là tính độc lập giữa SRT và thời gian lưu thủy lực HRT (hydraulic retention time), cho phép vận hành MBR ở mức SRT cao hơn nhiều so với CAS thông thường.
  * Giá trị SRT cao hơn thúc đẩy quá trình thích nghi của bùn (sludge acclimatization), nhờ đó nâng cao năng lực loại bỏ các hợp chất ô nhiễm [8].
  * Khả năng giữ lại hoàn toàn sinh khối của màng lọc đảm bảo độ đa dạng vi sinh vật phong phú trong bể sinh học, đóng góp vào hiệu quả phân hủy nhiều loại chất ô nhiễm [63].
  * Tốc độ sinh trưởng của vi khuẩn nitrat hóa chậm hơn đáng kể so với vi khuẩn dị dưỡng (heterotrophic bacteria), do đó cần duy trì SRT đủ dài để vi khuẩn nitrat hóa kịp phát triển và tích lũy trước khi bị rửa trôi (washout) khỏi hệ thống [59].
  * Các yếu tố trên lý giải mối tương quan thuận mạnh mẽ giữa SRT và loại bỏ amoni, nhất quán với các nghiên cứu trước đây [64].
* Cơ chế giải thích tác động tiêu cực mạnh mẽ của COD đầu vào (influent COD) và tỷ lệ C/N:
  * Tác động tiêu cực của COD đầu vào bắt nguồn từ ảnh hưởng trực tiếp của thông số này lên cộng đồng vi sinh vật.
  * Nồng độ COD đầu vào cao tạo ra tỷ lệ C/N cao trong hệ thống xử lý sinh học, kích thích sự bùng phát của vi khuẩn dị dưỡng, dẫn đến cạnh tranh gay gắt về cơ chất và oxy hòa tan (DO - dissolved oxygen), gây ức chế sự sinh trưởng của vi khuẩn nitrat hóa [60].
  * Thí nghiệm của Sepehri và Sarrafzadeh [65] trên hệ thống MBR làm giàu bùn nitrat hóa (NAS - nitrifying-enriched activated sludge) đã chứng minh hiệu suất nitrat hóa vượt trội của NAS so với bùn CAS: tỷ lệ loại bỏ amoni đạt $100\%$ ở NAS so với chỉ $43\%$ ở CAS; nồng độ nitrat sinh ra đạt $37{,}5\text{ mg L}^{-1}$ ở NAS so với $6{,}6\text{ mg L}^{-1}$ ở CAS.
  * Brasil et al. [66] cũng chứng minh tỷ lệ C/N thấp hơn (kết hợp nhiệt độ cao hơn) tạo môi trường thuận lợi cho vi khuẩn nitrat hóa và cải thiện rõ rệt hiệu quả loại bỏ amoni.
  * Hệ thống MBR trong nghiên cứu này vận hành ở tỷ lệ C/N đầu vào rất cao ($20{,}0 \pm 11{,}1$), do đó quá trình loại bỏ amoni bị ảnh hưởng tiêu cực mạnh mẽ bởi biến thiên nồng độ COD đầu vào.
* Cơ chế giải thích tác động ức chế độc tính của nồng độ dầu mỡ đầu vào (influent OG):
  * Nồng độ OG đầu vào cao gây ức chế chuyển hóa trao đổi chất đối với vi khuẩn nitrat hóa; ngay cả ở nồng độ thấp, các hợp chất độc hại cũng có thể cản trở hoạt tính vi khuẩn và làm tổn hại đến việc loại bỏ amoni [67].
  * Qin et al. (2007) khi thử nghiệm MBR xử lý nước thải nhà máy lọc dầu liên tục trong hơn hai tháng nhận thấy: trong hai tuần vận hành đầu tiên, hiệu suất loại bỏ amoni chỉ đạt $20\text{--}40\%$ do hàm lượng OG đầu vào quá cao ($53\text{--}153\text{ mg L}^{-1}$); hiệu quả nitrat hóa chỉ đạt mức cao khi nồng độ OG đầu vào giảm xuống dưới $20\text{ mg L}^{-1}$.
  * Trong hệ thống MBR nghiên cứu, nồng độ OG đầu vào ghi nhận mức cao lên tới $48\text{ mg L}^{-1}$ (cực đại $48{,}4\text{ ppm}$), tác động ức chế độc học này giải thích cho các đợt suy giảm hiệu quả loại bỏ amoni.
* Cơ chế giải thích tác động tiêu cực của độ thấm màng (membrane permeability) thông qua rút ngắn HRT:
  * Độ thấm màng cao làm gia tăng thông lượng và rút ngắn thời gian lưu thủy lực HRT, dẫn đến thời gian tiếp xúc của nước thải trong bể không đủ để vi khuẩn nitrat hóa kịp oxy hóa lượng amoni hiện diện.
  * Song et al. [68] đã chứng minh khi HRT giảm xuống dưới ngưỡng giới hạn ($6{,}5$ ngày), sự nitrat hóa không hoàn toàn gây sụt giảm hiệu suất loại bỏ nitơ tổng thể.
  * HRT cũng là nhân tố quyết định duy trì cấu trúc cộng đồng vi sinh vật; Ni et al. [69] nghiên cứu MBR ở các kích thước lỗ màng ($0{,}40$ và $0{,}05\ \mu\text{m}$) ở $25^\circ\text{C}$ xác nhận sự biến đổi cấu trúc cộng đồng vi sinh vật diễn ra đồng điệu và nhất quán với các biến đổi của HRT.
* Vai trò của MLVSS và giá trị biểu thị của độ lọc bùn (sludge filterability):
  * MLVSS có mức độ ảnh hưởng ít quan trọng hơn nhiều trong cả hai mô hình, phản ánh rằng để tăng hiệu quả loại bỏ amoni, việc chỉ nâng cao nồng độ bùn sinh khối thuần túy là không đủ.
  * Điều kiện cốt lõi là phải duy trì mật độ đủ lớn của các vi sinh vật oxy hóa amoni chuyên biệt trong hệ thống; kết quả này củng cố các nhận định khoa học rằng MLVSS không phải là chỉ thị thích hợp cho hoạt tính sinh lý của sinh khối [70, 71].
  * Sepehri và Sarrafzadeh [65] chỉ ra rằng bùn giàu vi khuẩn nitrat hóa (NAS) có khả năng lọc tốt gấp đôi so với CAS, cho thấy độ lọc bùn cao hơn (sludge filterability) liên quan trực tiếp đến nồng độ vi khuẩn nitrat hóa cao hơn và đi kèm hiệu quả loại bỏ amoni vượt trội.
  * Hiệu ứng này được cả hai mô hình PCA và ANN phản ánh thông qua ảnh hưởng tích cực của độ lọc bùn đối với quá trình loại bỏ amoni.
