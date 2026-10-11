### 2.3. Quantification of interfacial interactions by the advanced XDLVO approach

* **Cơ sở lý thuyết XDLVO nâng cao và kỹ thuật tích phân phần tử bề mặt (Surface Element Integration - SEI):**
  * Trong các hệ thống màng lọc sinh học (MBR), hiện tượng bám bẩn màng được chi phối trực tiếp bởi các tương tác nhiệt động lực học liên bề mặt giữa các tác nhân gây nghẹt (hạt bùn hoạt tính, chất cao phân tử ngoại bào) và bề mặt màng phân tách.
  * Phương pháp XDLVO cổ điển giả định bề mặt màng và hạt chất bẩn là các mặt phẳng lý tưởng hoặc hình cầu trơn nhẵn hoàn hảo. Tuy nhiên, bề mặt màng thực tế luôn sở hữu độ nhám ngẫu nhiên (random roughness) với các mấp mô cấu trúc vi mô, làm thay đổi đáng kể phân bố khoảng cách cục bộ và phân bố lực tương tác so với mô hình hình học phẳng.
  * Để định lượng chính xác năng lượng tương tác giữa hạt bùn dạng hạt (particulate sludge) và bề mặt màng nhám ngẫu nhiên mô phỏng, kỹ thuật tích phân phần tử bề mặt (Surface Element Integration - SEI) được áp dụng toàn diện kết hợp với dữ liệu cấu trúc địa hình bề mặt thu nhận từ kính hiển vi lực nguyên tử (AFM).
  * Tổng năng lượng tương tác liên bề mặt $U^{\text{TOT}}(h)$ tại khoảng cách phân tách tiếp cận $h$ được cấu thành từ ba thành phần tương tác nhiệt động độc lập:
    $$U^{\text{TOT}}(h) = U^{\text{LW}}(h) + U^{\text{EL}}(h) + U^{\text{AB}}(h)$$
    trong đó $U^{\text{LW}}(h)$ là tương tác tán xạ Lifshitz–van der Waals, $U^{\text{EL}}(h)$ là tương tác lớp điện kép tĩnh điện (electrostatic double layer), và $U^{\text{AB}}(h)$ là tương tác axit–bazơ Lewis (acid–base / hydrophobic interaction).
  * Theo nguyên lý của kỹ thuật SEI, bề mặt hạt bùn hoạt tính (mô hình hóa dưới dạng hình cầu bán kính $R$) được chia thành các phần tử diện tích vi phân dạng vành khuyên đồng tâm. Năng lượng tương tác tích phân $U(h)$ giữa toàn bộ hạt bùn và màng nhám được xác định thông qua phép tích phân hai lớp trên toàn bộ miền tiếp xúc của hạt:
    $$U(h) = \iint_{\text{particulate}} \Delta G(h') \, r \, \mathrm{d}r \, \mathrm{d}\theta$$
    trong đó:
    * $r$ là bán kính của vành khuyên vi phân trên bề mặt hạt bùn hoạt tính (circular ring radius).
    * $\mathrm{d}r$ là vi phân bán kính vành khuyên (differential circular ring radius).
    * $\mathrm{d}\theta$ là góc vi phân tương ứng với cung tròn vi phân cấu thành vành khuyên (differential angle of the circular arc).
    * $h'$ là khoảng cách phân tách cục bộ từ phần tử vi phân của hạt đến bề mặt màng nhám tương ứng.
    * $\Delta G(h')$ là mật độ năng lượng tương tác đơn lẻ trên một đơn vị diện tích (energy per unit area) tại khoảng cách phân tách $h'$.

* **Các phương trình vi phân mật độ năng lượng tương tác liên bề mặt ($\Delta G(h)$):**
  * Theo lý thuyết XDLVO, ba thành phần mật độ năng lượng tương tác vi phân trên đơn vị diện tích phụ thuộc vào khoảng cách phân tách cục bộ $h$ được mô tả bằng các phương trình giải tích sau:
    1. **Tương tác axit–bazơ Lewis ($\Delta G^{\text{AB}}(h)$):**
       * Tương tác $\text{AB}$ suy giảm theo hàm mũ theo khoảng cách phân ly:
         $$\Delta G^{\text{AB}}(h) = \Delta G_{h_0}^{\text{AB}} \exp\left( \frac{h_0 - h}{\lambda} \right)$$
         trong đó $h_0$ là khoảng cách phân tách tiếp xúc cực tiểu tại trạng thái cân bằng cơ học ($h_0 = 0{,}158\text{ nm}$), bắt nguồn từ giới hạn khoảng cách phân tử tối thiểu ngăn cản hai bề mặt rắn chồng lấn vô hạn vào nhau; $\lambda$ là độ dài phân rã đặc trưng của tương tác axit–bazơ trong môi trường nước (decay length of AB interaction, được thiết lập chuẩn hóa bằng $\lambda = 0{,}60\text{ nm}$).
    2. **Tương tác tán xạ Lifshitz–van der Waals ($\Delta G^{\text{LW}}(h)$):**
       * Tương tác $\text{LW}$ suy giảm theo quy luật nghịch đảo bình phương khoảng cách giữa hai phần tử phẳng vi phân:
         $$\Delta G^{\text{LW}}(h) = \Delta G_{h_0}^{\text{LW}} \left( \frac{h_0^2}{h^2} \right)$$
    3. **Tương tác lớp điện kép tĩnh điện ($\Delta G^{\text{EL}}(h)$):**
       * Dựa trên phép xấp xỉ tuyến tính hóa phương trình Poisson–Boltzmann đối với điện thế bề mặt bất đối xứng giữa màng và hạt bẩn:
         $$\Delta G^{\text{EL}}(h) = \kappa \zeta_{\text{m}} \zeta_{\text{f}} \epsilon_r \epsilon_0 \left[ \frac{\zeta_{\text{m}}^2 + \zeta_{\text{f}}^2}{2 \zeta_{\text{m}} \zeta_{\text{f}}} \left( 1 - \coth(\kappa h) \right) + \frac{1}{\sinh(\kappa h)} \right]$$
         hoặc được biểu diễn tương đương qua hàm cosecant hyperbolic $\operatorname{csch}(\kappa h) = \frac{1}{\sinh(\kappa h)}$:
         $$\Delta G^{\text{EL}}(h) = \frac{\epsilon_r \epsilon_0 \kappa}{2} \left[ \left(\zeta_{\text{m}}^2 + \zeta_{\text{f}}^2\right) \left( 1 - \coth(\kappa h) \right) + 2 \zeta_{\text{m}} \zeta_{\text{f}} \operatorname{csch}(\kappa h) \right]$$
         trong đó $\kappa$ là nghịch đảo của độ dài sàng lọc Debye ($\kappa^{-1}$ biểu thị Debye screening length đặc trưng cho bề dày lớp điện kép trong dung dịch); $\zeta_{\text{m}}$ và $\zeta_{\text{f}}$ lần lượt là thế zeta (zeta potential) của bề mặt màng (chỉ số dưới $\text{m}$) và hạt chất gây nghẹt bùn hoạt tính (chỉ số dưới $\text{f}$); $\epsilon_r$ là hằng số điện môi tương đối của dung dịch nước và $\epsilon_0$ là độ điện thẩm chân không ($\epsilon_0 \approx 8{,}854 \times 10^{-12}\text{ F/m}$), với tích số $\epsilon_r \epsilon_0$ thể hiện độ điện thẩm tuyệt đối của môi trường chất lỏng (solution permittivity).

* **Xác định các thành phần năng lượng tương tác tại khoảng cách cân bằng cực tiểu ($h_0$):**
  * Tại khoảng cách tiếp xúc cân bằng cực tiểu $h_0 = 0{,}158\text{ nm}$, các hệ số năng lượng tương tác tiếp xúc $\Delta G_{h_0}^{\text{AB}}$, $\Delta G_{h_0}^{\text{LW}}$, và $\Delta G_{h_0}^{\text{EL}}$ được tính toán từ sức căng bề mặt thành phần của các pha tiếp xúc: pha màng ($\text{m}$), pha hạt bẩn ($\text{f}$), và pha môi trường nước ($\text{w}$):
    1. **Năng lượng tiếp xúc axit–bazơ ($\Delta G_{h_0}^{\text{AB}}$):**
       $$\Delta G_{h_0}^{\text{AB}} = 2 \left[ \sqrt{\gamma_{\text{w}}^{+}} \left( \sqrt{\gamma_{\text{m}}^{-}} + \sqrt{\gamma_{\text{f}}^{-}} - \sqrt{\gamma_{\text{w}}^{-}} \right) + \sqrt{\gamma_{\text{w}}^{-}} \left( \sqrt{\gamma_{\text{m}}^{+}} + \sqrt{\gamma_{\text{f}}^{+}} - \sqrt{\gamma_{\text{w}}^{+}} \right) - \sqrt{\gamma_{\text{m}}^{+} \gamma_{\text{f}}^{-}} - \sqrt{\gamma_{\text{m}}^{-} \gamma_{\text{f}}^{+}} \right]$$
       trong đó $\gamma^{+}$ và $\gamma^{-}$ lần lượt là thành phần sức căng bề mặt nhận electron (electron-acceptor) và cho electron (electron-donor) theo lý thuyết van Oss–Chaudhury–Good.
    2. **Năng lượng tiếp xúc tán xạ Lifshitz–van der Waals ($\Delta G_{h_0}^{\text{LW}}$):**
       $$\Delta G_{h_0}^{\text{LW}} = -2 \left( \sqrt{\gamma_{\text{m}}^{\text{LW}}} - \sqrt{\gamma_{\text{w}}^{\text{LW}}} \right) \left( \sqrt{\gamma_{\text{f}}^{\text{LW}}} - \sqrt{\gamma_{\text{w}}^{\text{LW}}} \right)$$
       trong đó $\gamma^{\text{LW}}$ là thành phần lực căng bề mặt vô hướng Lifshitz–van der Waals.
    3. **Năng lượng tiếp xúc tĩnh điện ($\Delta G_{h_0}^{\text{EL}}$):**
       $$\Delta G_{h_0}^{\text{EL}} = \frac{\epsilon_r \epsilon_0 \kappa}{2} \left[ \left(\zeta_{\text{f}}^2 + \zeta_{\text{m}}^2\right) \left( 1 - \coth(\kappa h_0) \right) + 2 \zeta_{\text{f}} \zeta_{\text{m}} \operatorname{csch}(\kappa h_0) \right]$$
  * Để thu nhận các tham số thành phần sức căng bề mặt ($\gamma_s^{\text{LW}}$, $\gamma_s^{+}$, $\gamma_s^{-}$) của từng mẫu rắn (ký hiệu $s$, đại diện cho màng hoặc bùn hoạt tính), phương trình Young mở rộng được thiết lập và giải đồng thời cho bộ ba chất lỏng chuẩn đo góc tiếp xúc (ký hiệu $l$):
    $$(1 + \cos\phi) \gamma_l^{\text{Tot}} = 2 \left( \sqrt{\gamma_s^{\text{LW}} \gamma_l^{\text{LW}}} + \sqrt{\gamma_s^{+} \gamma_l^{-}} + \sqrt{\gamma_s^{-} \gamma_l^{+}} \right)$$
    trong đó $\phi$ là góc tiếp xúc cân bằng đo được của chất lỏng thử nghiệm $l$ trên bề mặt chất rắn $s$, và $\gamma_l^{\text{Tot}} = \gamma_l^{\text{LW}} + 2\sqrt{\gamma_l^{+} \gamma_l^{-}}$ là tổng năng lượng bề mặt tự do của chất lỏng thăm dò.

* **Mô hình hóa hình học bề mặt màng nhám từ dữ liệu AFM và quan hệ khoảng cách không gian:**
  * Cấu trúc vi địa hình ngẫu nhiên của bề mặt màng được tái lập chính xác từ ma trận dữ liệu phân tích kính hiển vi lực nguyên tử (AFM) kết hợp với kỹ thuật phân chia lưới tam giác (triangulation technique), tạo nên một bề mặt đa diện liên tục gồm các mặt tam giác phẳng vi mô.
  * Dựa trên quan hệ hình học không gian giữa hạt bùn hình cầu (bán kính $R$) và bề mặt màng nhám gồ ghề, khoảng cách phân tách cục bộ $h$ từ một cung tròn vi phân trên hạt bùn đến bề mặt phẳng tham chiếu ngang của màng được thiết lập theo phương trình:
    $$h = R + D - \sqrt{R^2 - r^2} - z + z_{\max}$$
    trong đó:
    * $R$ là bán kính hình học của hạt bùn hoạt tính (particulate sludge radius).
    * $D$ là khoảng cách tiếp cận gần nhất từ đáy hạt bùn tới mặt phẳng ngang tham chiếu của màng (closest distance from the particulate sludge to the membrane planar surface).
    * $z_{\max}$ là giá trị độ cao đỉnh lớn nhất của các mấp mô trên bề mặt màng thu nhận từ ảnh AFM.
    * $z$ là độ cao cục bộ tại một điểm khảo sát $P(x, y, z)$ tương ứng trên bề mặt màng nhám.
  * Tọa độ độ cao $z$ của điểm $P$ nằm trên một mặt tam giác cục bộ (được xác định bởi ba đỉnh $P_1(x_1, y_1, z_1)$, $P_2(x_2, y_2, z_2)$, và $P_3(x_3, y_3, z_3)$ từ lưới AFM) được tính toán chính xác thông qua phương trình pháp tuyến mặt phẳng:
    $$\mathbf{n}(P_1, P_2, P_3) \cdot \vec{P_1 P} = (n_x, n_y, n_z) \cdot (x - x_1, y - y_1, z - z_1) = 0$$
    trong đó $\mathbf{n}(P_1, P_2, P_3) = \vec{P_1 P_2} \times \vec{P_1 P_3}$ là vectơ pháp tuyến đơn vị vuông góc với diện tích tam giác vi phân. Từ phương trình tích vô hướng bằng $0$, tọa độ độ cao $z$ được giải tường minh:
    $$z = z_1 - \frac{n_x (x - x_1) + n_y (y - y_1)}{n_z}$$

* **Thuật toán tích phân số Simpson kép và cấu hình tính toán mô phỏng:**
  * Việc thay thế các biểu thức năng lượng vi phân $\Delta G^{\text{AB}}(h)$, $\Delta G^{\text{LW}}(h)$, $\Delta G^{\text{EL}}(h)$ cùng quan hệ khoảng cách hình học phức tạp vào phương trình tích phân SEI tạo nên một hệ tích phân kép phi tuyến không có nghiệm giải tích giải trực tiếp.
  * Để giải quyết bài toán, thuật toán tích phân số Simpson phức hợp hai chiều (composite double Simpson's numerical integration rule) được triển khai:
    * Miền tích phân trên bề mặt tiếp xúc được chia lưới mịn thành $2000$ phần tử diện tích vi phân ($2000$ elements) nhằm đảm bảo sự hội tụ số học và triệt tiêu sai số làm tròn hình học.
    * Quá trình quét tương tác được thực hiện đối với khoảng cách phân tách $h$ biến thiên từ khoảng cách cân bằng cực tiểu $h_0 = 0{,}158\text{ nm}$ đến $12\text{ nm}$, được rời rạc hóa thành $60$ điểm phân tách độc lập ($60$ discrete points).
    * Toàn bộ thuật toán mô phỏng và xử lý số liệu được lập trình và vận hành trên nền tảng phần mềm MATLAB (phiên bản 2017b), chạy trên hệ thống máy trạm hiệu năng cao (HP Z8 G4 workstation) nhằm đáp ứng khối lượng tính toán khổng lồ (supercomputing workload).
  * Việc tích hợp mô hình màng nhám ngẫu nhiên vào kỹ thuật SEI đã nâng cấp căn bản năng lực dự báo của lý thuyết XDLVO truyền thống, tạo thành phương pháp XDLVO nâng cao (advanced XDLVO approach). Phương pháp này cho phép định lượng chính xác hàng rào năng lượng tương tác (energy barrier), thế năng tương tác hút dính, và cơ chế bám bẩn vi mô giữa hạt bùn và màng lọc trong các điều kiện vận hành MBR thực tế.
