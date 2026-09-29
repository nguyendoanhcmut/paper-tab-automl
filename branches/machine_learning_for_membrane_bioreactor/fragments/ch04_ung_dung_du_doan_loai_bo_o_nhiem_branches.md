# Cây Tri Thức: Ứng dụng Học máy trong MBR - Tổng quan và Dự đoán Loại bỏ Chất ô nhiễm

## 4. Ứng dụng Học máy trong MBR: Tổng quan và Dự đoán Loại bỏ Chất ô nhiễm

### 4.1 Tổng quan Tình hình Ứng dụng và Xu hướng Phát triển

#### 4.1.1 Thống kê Phân bố Nghiên cứu và Mô hình Học máy
- Số lượng công bố khoa học về ứng dụng học máy trong MBR tăng nhanh từ năm 2015. Tốc độ tăng trưởng đạt mức bùng nổ sau năm 2018.
- Trọng tâm nghiên cứu chia thành hai nhóm chính. Nghiên cứu dự đoán tắc nghẽn màng chiếm $67.1\%$. Nghiên cứu dự đoán hiệu suất loại bỏ chất ô nhiễm chiếm $34.3\%$.
- Mạng nơ-ron nhân tạo (ANN) giữ vai trò chủ đạo trong toàn bộ các ứng dụng. Tỷ lệ sử dụng ANN đạt trên $50\%$ trong dự đoán ô nhiễm và $72.9\%$ trong dự đoán tắc nghẽn.
- Mô hình Perceptron đa tầng (MLP) chiếm tỷ trọng cao nhất với $66.7\%$ ở mô hình xử lý chất ô nhiễm và $39.6\%$ ở mô hình tắc nghẽn màng.
- Mạng nơ-ron hàm cơ sở xuyên tâm (RBFNN) chiếm $18.8\%$ trong các nghiên cứu màng.
- Máy vector hỗ trợ (SVM/SVR) chiếm $18.8\%$ tổng số ứng dụng dự đoán tắc nghẽn.
- Mạng nơ-ron sâu (DNN) chiếm $8.3\%$ số lượng mô hình được thiết lập.
- Chiến lược tinh chỉnh siêu tham số thể hiện sự phân hóa rõ rệt:
  + Khoảng $56.3\%$ số nghiên cứu không dùng thuật toán tối ưu hóa tự động.
  + Khoảng $33.3\%$ nghiên cứu áp dụng các thuật toán tối ưu hóa thông minh.
  + Khoảng $8.3\%$ nghiên cứu sử dụng phương pháp kiểm định chéo (Cross-Validation).
- Giải thuật di truyền (GA) dẫn đầu nhóm thuật toán tối ưu hóa bầy đàn với $56.5\%$. Thuật toán tối ưu hóa bầy đàn hạt (PSO) đứng thứ hai với $18.9\%$. Các thuật toán khác gồm thuật toán đom đóm (FFA) và thuật toán bầy sói xám (GWO).

#### 4.1.2 Xu hướng Dịch chuyển từ Dự đoán Tĩnh sang Động học Chuỗi Thời gian
- Giai đoạn đầu tập trung vào các mô hình tĩnh truyền thống như hồi quy tuyến tính và MLP đơn giản. Các mô hình này dự đoán nồng độ đầu ra tại trạng thái ổn định.
- Giai đoạn hiện nay dịch chuyển mạnh sang dự đoán chuỗi thời gian liên tục. MBR vận hành với đặc tính động học thay đổi liên tục theo tải trọng thủy lực và nồng độ dòng vào.
- Kiến trúc mạng nơ-ron hồi quy với bộ nhớ ngắn-dài (LSTM) giúp mô hình nắm bắt phụ thuộc thời gian dài của quá trình tích tụ sinh khối.
- Mạng nơ-ron tích chập (CNN) và mạng kết nối dày đặc (DenseNet) được ứng dụng để trích xuất đặc trưng không gian từ dữ liệu cảm biến đa chiều và ảnh phổ.
- Mạng nơ-ron sóng nhỏ (WNN) kết hợp phân tích đa độ phân giải với mạng nơ-ron truyền thẳng. Mô hình này giúp nắm bắt các biến động tần số cao của chất lượng nước.

#### 4.1.3 Phân tích Dung lượng Tham số và Tính Ổn định của Kiến trúc Mạng Nơ-ron
- Khả năng biểu diễn của mô hình phụ thuộc trực tiếp vào số lượng tham số huấn luyện (Weights và Biases).
- Mô hình MLP bộc lộ độ ổn định kém trên các tập dữ liệu thực nghiệm biến động mạnh. Hiện tượng này xuất phát từ việc khởi tạo trọng số ngẫu nhiên và nguy cơ rơi vào cực tiểu cục bộ.
- Tích hợp giải thuật tối ưu hóa toàn cục như GA hoặc PSO giúp cải thiện vượt bậc độ ổn định và giá trị $R^2$ của mạng MLP.
- Mạng WNN thể hiện hiệu năng xuất sắc với số lượng tham số rất khiêm tốn. Hàm kích hoạt wavelet dạng sóng cục bộ hóa giúp mạng đạt hệ số xác định $R^2 > 0.99$.
- Hàm kích hoạt Wavelet Morlet chuẩn hóa:
  $$\psi(x) = \cos(1.75 x) \exp\left(-\frac{x^2}{2}\right)$$
- Hàm biến đổi Wavelet liên tục với hệ số co giãn $a$ và độ dịch $b$:
  $$\psi_{a,b}(x) = \frac{1}{\sqrt{|a|}} \psi\left(\frac{x - b}{a}\right)$$
- Hàm kích hoạt RBF Gauss trong mạng RBFNN:
  $$\phi_j(x) = \exp\left(-\frac{\|x - c_j\|^2}{2\sigma_j^2}\right)$$
  trong đó $c_j$ là tâm cụm nơ-ron thứ $j$, $\sigma_j$ là độ rộng vùng tác động của hàm nhân.

#### 4.1.4 Bốn Giới hạn Cốt lõi của các Mô hình Học máy Hiện hành
- Hệ thống chỉ số đầu vào thiếu đồng bộ: Phần lớn mô hình dự đoán loại bỏ chất ô nhiễm bỏ qua các chỉ số lọc màng (MFI chỉ chiếm $20.8\%$) và đặc tính chất gây tắc nghẽn (CFI chiếm $0\%$).
- Thiếu kiểm chứng quy mô công nghiệp thực tế: Đa số nghiên cứu thực hiện ở quy mô phòng thí nghiệm (Lab-scale) hoặc mô hình thí điểm (Pilot-scale). Dữ liệu vận hành trạm quy mô lớn dài hạn còn khan hiếm.
- Rào cản thu thập dữ liệu trực tuyến thời gian thực: Các chỉ số sinh hóa như $\text{BOD}_5$, COD, TN, TP đòi hỏi thời gian phân tích phòng thí nghiệm từ vài giờ đến vài ngày. Điều này cản trở việc dự đoán và điều khiển vòng kín tức thời.
- Thiếu đóng góp vào việc hiểu sâu cơ chế sinh học: Các mô hình hoạt động như hộp đen toán học (Black-box). Mô hình thiếu sự tích hợp tri thức hóa lý và động học phản ứng bùn hoạt tính.

---

### 4.2 Hệ thống Hóa 5 Nhóm Biến số Đầu vào (Input Variables Framework)

```
                            HỆ THỐNG BIẾN SỐ ĐẦU VÀO MBR
                                         │
        ┌──────────────┬─────────────────┼────────────────┬──────────────┐
        ▼              ▼                 ▼                ▼              ▼
     Nhóm 1         Nhóm 2            Nhóm 3           Nhóm 4         Nhóm 5
      CCI            EI                OI               CFI            MFI
  (Chỉ số        (Chỉ số           (Chỉ số          (Đặc tính      (Chỉ số
   Nồng độ)       Môi trường)       Vận hành)        Chất bẩn)      Lọc màng)
        │              │                 │                │              │
   • COD, BOD     • pH, Temp        • HRT, SRT       • SMP, EPS     • TMP, Flux
   • MLSS, MLVSS  • DO, ORP         • Sục khí Qair   • Floc size    • Kháng lực R
   • TN, NH₄⁺-N   • OLR, EC         • Tỉ lệ lọc/nghỉ • Điện thế ζ   • Độ thấm Lm
   • TP, PO₄³⁻                      • Rửa ngược      • Độ nhớt μ    • ΔTMP/Δt
```

#### 4.2.1 Nhóm 1: Chỉ số Nồng độ Thông thường (CCI - Conventional Concentration Indices)
- Tỷ lệ ứng dụng: Nhóm CCI chiếm tỷ lệ cao nhất trong các mô hình dự đoán xử lý ô nhiễm ($75.2\%$) và chiếm $60.4\%$ trong mô hình tắc nghẽn màng.
- Nhu cầu oxy hóa học (COD) và Nhu cầu oxy sinh hóa (BOD): Đo lường hàm lượng cơ chất hữu cơ trong dòng vào ($COD_{\text{in}}, BOD_{\text{in}}$) và dòng ra ($COD_{\text{eff}}, BOD_{\text{eff}}$).
- Tổng cacbon hữu cơ (TOC): Phản ánh tổng lượng cacbon hữu cơ hòa tan và không tan trong hệ thống phản ứng.
- Nồng độ bùn hoạt tính lơ lửng (MLSS) và Bùn lơ lửng dễ bay hơi (MLVSS): Phản ánh mật độ sinh khối vi sinh vật trong bể phản ứng.
- Các hợp chất Nitơ: Tổng nitơ (TN), Amoni ($NH_4^+$-$N$ hoặc $NH_3$-$N$), Nitrit ($NO_2^-$-$N$), Nitrat ($NO_3^-$-$N$).
- Các hợp chất Phốt pho: Tổng phốt pho (TP) và Phốt phát hòa tan ($PO_4^{3-}$).
- Tổng chất rắn lơ lửng dòng vào (TSS) và Tổng chất rắn hòa tan (TDS).
- Sản phẩm polyme sinh học hòa tan và gắn kết:
  + Polyme ngoại bào (EPS) gồm phân đoạn protein ($EPS_p$) và polysaccharide ($EPS_c$).
  + EPS bám lỏng lẻo (LB-EPS) và EPS bám chặt (TB-EPS).
  + Sản phẩm vi sinh vật hòa tan (SMP).

#### 4.2.2 Nhóm 2: Chỉ số Môi trường Dung dịch (EI - Environment Indices)
- Tỷ lệ ứng dụng: Nhóm EI xuất hiện trong $54.2\%$ mô hình dự đoán ô nhiễm.
- Nhiệt độ dung dịch ($T$, °C): Ảnh hưởng trực tiếp đến hoạt tính enzyme vi sinh, độ nhớt chất lỏng và hằng số phân hủy sinh học.
- Nồng độ oxy hòa tan (DO, mg/L): Yếu tố quyết định ranh giới giữa điều kiện hiếu khí, thiếu khí và kỵ khí.
- Độ pH: Tác động mạnh đến cân bằng ion hóa của amoni/amoniac ($NH_4^+ / NH_3$) và hiệu suất enzyme nitrat hóa.
- Thế oxy hóa khử (ORP, mV): Phản ánh trạng thái oxy hóa khử sinh hóa thực tế trong buồng phản ứng.
- Tải trọng hữu cơ thể tích (OLR, $\text{kg COD}/(\text{m}^3 \cdot \text{ngày})$):
  $$\text{OLR} = \frac{COD_{\text{in}} \cdot Q}{V} = \frac{COD_{\text{in}}}{\text{HRT}}$$
- Độ dẫn điện (EC, $\mu\text{S/cm}$) và Độ mặn (Salinity, g/L): Tác động đến áp suất thẩm thấu và cân bằng ion tế bào vi khuẩn.

#### 4.2.3 Nhóm 3: Chỉ số Vận hành Công nghệ (OI - Operation Indices)
- Tỷ lệ ứng dụng: Xuất hiện trong $62.5\%$ mô hình dự đoán chất lượng nước đầu ra.
- Thời gian lưu thủy lực (HRT, giờ):
  $$\text{HRT} = \frac{V}{Q}$$
  trong đó $V$ là thể tích bể phản ứng ($m^3$), $Q$ là lưu lượng nước cấp ($m^3/h$).
- Thời gian lưu bùn (SRT, ngày):
  $$\text{SRT} = \frac{V \cdot X}{Q_w \cdot X_w + Q_{\text{eff}} \cdot X_{\text{eff}}}$$
  trong đó $X$ là nồng độ MLSS trong bể, $Q_w$ và $X_w$ là lưu lượng và nồng độ bùn thải bỏ.
- Thông lượng lọc qua màng ($J$, $\text{L}/(\text{m}^2 \cdot \text{h})$): Đại lượng đo lưu lượng thể tích trên diện tích màng hiệu dụng.
- Cường độ sục khí ($Q_{\text{air}}$ hoặc $SAD_m$, $\text{m}^3/(\text{m}^2 \cdot \text{h})$): Cung cấp oxy hòa tan và tạo lực cắt thủy động lực học rung màng để giảm tắc nghẽn.
- Tỷ lệ lọc - nghỉ (Filtration-Relaxation Ratio): Chu kỳ xen kẽ giữa giai đoạn hút nước lọc và giai đoạn tạm dừng để màng tự phục hồi.
- Cường độ và thời gian rửa ngược (Backwash Duration and Flux): Chu kỳ bơm nước lọc hoặc dung dịch hóa chất ngược chiều để làm sạch lỗ rỗng màng.

#### 4.2.4 Nhóm 4: Đặc tính Chất gây Tắc nghẽn (CFI - Characteristic Foulant Indices)
- Tỷ lệ ứng dụng: Chiếm $0\%$ trong các mô hình dự đoán ô nhiễm trước đây. Tác giả nhấn mạnh đây là thiếu sót kỹ thuật lớn cần khắc phục.
- Nồng độ SMP và các phân đoạn EPS: Tác nhân chính gây bít tắc lỗ rỗng và kết tụ màng sinh học.
- Kích thước bông bùn hoạt tính (Floc size, $\mu\text{m}$) và Phân bố kích thước hạt bùn (PSD - Particle Size Distribution).
- Điện thế Zeta ($\zeta$, mV): Đo điện tích bề mặt bông bùn. Điện thế Zeta âm lớn cản trở sự kết cụm hạt bùn.
- Độ nhớt động lực học hỗn dịch bùn ($\mu$, $\text{mPa}\cdot\text{s}$): Thay đổi phi tuyến tính theo nồng độ MLSS và nhiệt độ.
- Chỉ số thể tích bùn (SVI, mL/g): Phản ánh khả năng lắng và độ xốp của bùn hoạt tính.
- Kích thước lỗ rỗng màng danh định ($d_p$, $\mu\text{m}$) và Hệ số tắc nghẽn màng ($K_b$).

#### 4.2.5 Nhóm 5: Chỉ số Lọc Màng (MFI - Membrane Filtration Indices) và Tham số Thời gian ($t$)
- Tỷ lệ ứng dụng: Chỉ có $20.8\%$ mô hình chất ô nhiễm tích hợp MFI. Tuy nhiên MFI chiếm tới $68.8\%$ trong mô hình tắc nghẽn màng.
- Áp suất xuyên màng (TMP, kPa): Chênh lệch áp suất động lực giữa phía cấp liệu và phía nước thẩm thấu:
  $$\text{TMP} = P_{\text{feed}} - P_{\text{permeate}}$$
- Tốc độ tăng áp suất xuyên màng theo thời gian ($\Delta \text{TMP}/\Delta t$): Đo lường gia tốc bám bẩn trên bề mặt màng.
- Tổng trở lực lọc thủy lực ($R_t$, $\text{m}^{-1}$): Xác định theo định luật Darcy kết hợp mô hình trở lực nối tiếp:
  $$J = \frac{\text{TMP}}{\mu \cdot R_t} = \frac{\text{TMP}}{\mu \cdot (R_m + R_c + R_p)}$$
  trong đó $R_m$ là trở lực màng sạch, $R_c$ là trở lực lớp bánh bùn trên bề mặt, $R_p$ là trở lực bít tắc lỗ rỗng màng không thuận nghịch.
- Độ thấm lọc của màng ($L_m$, $\text{L}/(\text{m}^2 \cdot \text{h} \cdot \text{bar})$):
  $$L_m = \frac{J}{\text{TMP}}$$
- Tham số thời gian vận hành tích lũy ($t$, giờ hoặc ngày): Biểu diễn tuổi thọ của màng và chu kỳ lão hóa vật liệu.

#### 4.2.6 Ma trận Tương quan và Tỷ lệ Ứng dụng Biến số Đầu vào

| Nhóm biến số | Tỷ lệ trong Mô hình Ô nhiễm (%) | Tỷ lệ trong Mô hình Tắc nghẽn (%) | Các thông số đo đạc đại diện chính |
| :--- | :--- | :--- | :--- |
| **CCI** (Chỉ số nồng độ) | $75.2\%$ | $60.4\%$ | COD, BOD, TOC, MLSS, MLVSS, TN, TP, $NH_4^+$-$N$, $NO_3^-$-$N$ |
| **OI** (Chỉ số vận hành) | $62.5\%$ | $45.8\%$ | HRT, SRT, Thông lượng $J$, Cường độ sục khí $Q_{\text{air}}$, Chu kỳ rửa ngược |
| **EI** (Chỉ số môi trường) | $54.2\%$ | $38.5\%$ | Nhiệt độ $T$, pH, Nồng độ oxy hòa tan DO, Thế khử ORP, Độ mặn |
| **MFI** (Chỉ số lọc màng) | $20.8\%$ | $68.8\%$ | Áp suất TMP, Trở lực $R_t$, $R_m$, $R_c$, Độ thấm lọc $L_m$, $\Delta \text{TMP}/\Delta t$ |
| **CFI** (Đặc tính tắc nghẽn)| $0.0\%$ | $31.2\%$ | SMP, EPS bám lỏng/chặt, Kích thước bông bùn, Điện thế Zeta $\zeta$, SVI |
| **Thời gian** ($t$) | $18.5\%$ | $42.6\%$ | Thời gian vận hành tích lũy, Thời gian giữa hai chu kỳ rửa ngược |

---

### 4.3 Ứng dụng Dự đoán Hiệu suất Loại bỏ Chất ô nhiễm

#### 4.3.1 Dự đoán Động học Loại bỏ Hợp chất Hữu cơ (COD, BOD, TOC)
- Mục tiêu đầu ra: Nồng độ COD dòng ra ($COD_{\text{eff}}$) và Hiệu suất loại bỏ COD ($E_{\text{COD}}$) chiếm tới $79.2\%$ các mô hình khảo sát:
  $$E_{\text{COD}} = \frac{COD_{\text{in}} - COD_{\text{eff}}}{COD_{\text{in}}} \times 100\%$$
- Các biến đầu vào có trọng số quyết định: Nồng độ $COD_{\text{in}}$, thời gian lưu thủy lực (HRT), nồng độ sinh khối (MLSS) và nồng độ DO.
- Mô hình phương trình cân bằng vật chất truyền thống:
  $$\frac{dS}{dt} = \frac{Q}{V}(S_{\text{in}} - S) - \frac{\mu_{\max} S}{K_s + S} \frac{X}{Y}$$
  trong đó $S$ là nồng độ COD, $X$ là MLVSS, $\mu_{\max}$ là tốc độ sinh trưởng vi sinh tối đa, $K_s$ là hằng số bán bão hòa, $Y$ là hệ số sản lượng tế bào.
- Hiệu năng mô hình học máy:
  + Mạng MLP chuẩn và SVM đạt hệ số tương quan $R^2$ dao động trong khoảng $0.85$ đến $0.98$.
  + Nghiên cứu của Cai et al. (2019b) áp dụng mạng nơ-ron sóng nhỏ (WNN) cấu trúc 3-2-1 với đầu vào ($COD_{\text{in}}$, $NH_3$-$N_{\text{in}}$, Salinity). Mô hình đạt độ chính xác gần như tuyệt đối với $R^2 = 0.999$.
  + Nghiên cứu của Li et al. (2022) ứng dụng mạng DenseNet trên hệ thống AnMBR. Mô hình dự đoán $COD_{\text{eff}}$ và tốc độ sinh khí sinh học ($CH_4, N_2, CO_2$) đạt độ chính xác $97.4\%$, vượt trội hoàn toàn so với mạng FCN ($92.6\%$) và CNN ($91.8\%$).

#### 4.3.2 Dự đoán Quá trình Chuyển hóa và Loại bỏ Hợp chất Nitơ (TN, NH₄⁺-N, NO₃⁻-N)
- Các biến mục tiêu liên quan đến nitơ chiếm $58.3\%$ số lượng mô hình công bố.
- Bản chất động học sinh học gồm hai công đoạn liên hợp:
  + Quá trình nitrat hóa hiếu khí chuyển hóa amoni thành nitrit và nitrat:
    $$NH_4^+ + 1.5 O_2 \xrightarrow{\text{AOB}} NO_2^- + H_2O + 2H^+$$
    $$NO_2^- + 0.5 O_2 \xrightarrow{\text{NOB}} NO_3^-$$
    Tốc độ phản ứng phụ thuộc mạnh vào nồng độ DO và kiềm:
    $$r_{\text{nit}} = \mu_{\text{max,AUT}} \left( \frac{S_{NH}}{K_{NH} + S_{NH}} \right) \left( \frac{S_O}{K_O + S_O} \right) X_{\text{AUT}}$$
  + Quá trình khử nitrat thiếu khí chuyển nitrat thành khí nitơ:
    $$NO_3^- + 1.08 \text{CH}_3\text{OH} + 0.24 H_2\text{CO}_3 \rightarrow 0.056 C_5H_7O_2N + 0.47 N_2 \uparrow + 1.68 H_2O + HCO_3^-$$
- Ứng dụng mô hình học máy:
  + Mô hình chuỗi thời gian LSTM của Yaqub et al. (2020) cho hệ $A^2/O$-MBR dự đoán loại bỏ $NH_3$-$N$ đạt sai số toàn phương trung bình siêu nhỏ $\text{MSE} = 0.0047$.
  + Mạng lai thông minh GA-ANN và PSO-ANN tối ưu trọng số liên kết giúp xử lý hoàn hảo tương tác phi tuyến phức tạp giữa nồng độ DO, ORP và tỷ lệ hồi lưu bùn ($R^2 > 0.90$).
  + Kim et al. (2021b) kết hợp quang phổ cận hồng ngoại (NIRS) với mạng MLP cấu trúc 5-9-1. Mô hình dự đoán chính xác hàm lượng $TN_{\text{eff}}$, $NH_3$-$N_{\text{eff}}$, $NO_2^-$-$N$ và $NO_3^-$-$N$ với $R^2 > 0.97$.

#### 4.3.3 Dự đoán Quá trình Tích lũy và Loại bỏ Phốt pho (TP, PO₄³⁻)
- Cơ chế loại bỏ phốt pho sinh học tăng cường (EBPR):
  + Sinh vật tích lũy polyphosphate (PAO) giải phóng phốt phát trong điều kiện kỵ khí. PAO hấp thụ lượng lớn phốt phát vượt mức (Luxury Uptake) trong điều kiện hiếu khí.
  + Phốt pho được loại bỏ vật lý khỏi hệ thống thông qua việc xả bùn dư ($Q_w$).
- Tác động hỗ trợ của màng lọc: Màng vi lọc/siêu lọc giữ lại hoàn toàn sinh khối chứa phốt pho. Màng ngăn chặn hiện tượng trôi bông bùn như trong bể lắng truyền thống.
- Dự đoán bằng học máy:
  + Mirbagheri et al. (2015b) sử dụng mô hình RBFNN cấu trúc 5-5-1 cho hệ MBR chìm. Đầu vào gồm $BOD_{\text{in}}$, $COD_{\text{in}}$, $NH_3$-$N$, TP, TDS, HRT, MLVSS và pH. Mô hình dự đoán $TP_{\text{eff}}$ đạt $R^2 > 0.98$.
  + Yaqub et al. (2020) ứng dụng mạng LSTM dự đoán động học loại bỏ TP đạt độ khớp cao trên chuỗi dữ liệu vận hành thực tế.
  + Các biến đầu vào mang tính quyết định bao gồm tỷ số $COD/TP$, chu kỳ kỵ khí-hiếu khí, thời gian lưu bùn SRT và pH hỗn dịch.

#### 4.3.4 Dự đoán Loại bỏ Vi chất Ô nhiễm Nguy hại (Trace Organic Pollutants)
- Nhóm vi chất ô nhiễm bao gồm dược phẩm, thuốc kháng sinh, hợp chất gây rối loạn nội tiết (EDCs), chất hoạt động bề mặt và hóa chất công nghiệp.
- Tỷ lệ nghiên cứu còn khiêm tốn với $16.7\%$ số lượng công bố.
- Cơ chế loại bỏ kép trong hệ màng MBR:
  + Cơ chế hấp phụ và phân hủy sinh học bởi màng sinh học và bùn hoạt tính với thời gian lưu bùn dài (High SRT).
  + Cơ chế cản lọc cơ học bởi kích thước lỗ màng và lớp bánh lọc động sinh học (Dynamic cake layer).
- Thách thức của mô hình học máy:
  + Nồng độ chất ô nhiễm cực thấp ở ngưỡng nanogram hoặc microgram trên lít ($ng/L$ - $\mu g/L$).
  + Cơ chế chuyển hóa động học phân kỳ phức tạp khiến mạng nơ-ron ANN truyền thống kém hiệu quả hơn dự đoán các chỉ số thông thường.
  + Các mô hình cây quyết định (Random Forest, XGBoost) và mô hình tối ưu bầy đàn thể hiện tiềm năng vượt trội trong việc phân loại và dự đoán nồng độ vết.
  + Wolf et al. (2001, 2003) tiên phong ứng dụng MLP dự đoán thành công khả năng loại bỏ các phân tử hữu cơ độc hại gốc clo và hợp chất thơm trong nước thải công nghiệp.

#### 4.3.5 Bảng Tổng hợp Nghiên cứu Thực nghiệm và Kiến trúc Mô hình Tiêu biểu

| Nhóm tác giả & Năm | Loại hình công nghệ MBR | Cấu trúc mô hình ML | Các biến đầu vào chính (Inputs) | Các biến mục tiêu dự đoán (Outputs) | Hiệu năng dự đoán thực nghiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kim et al. (2021b)** | MBR phòng thí nghiệm + Phổ NIRS | MLP (5-11-6, 5-9-1, 5-9-2) | Dữ liệu quang phổ hấp thụ cận hồng ngoại (NIRS) | $COD_{\text{eff}}$, TN, $NH_3$-$N$, $NO_2^-$, $NO_3^-$, $PO_4^{3-}$, SMP, EPS | $R^2 > 0.97$ cho toàn bộ các chỉ tiêu chất lượng |
| **Mirbagheri et al. (2015b)** | MBR ngập nước (Xử lý nước thải đô thị & công nghiệp) | RBFNN (5-5-1) | $BOD_{\text{in}}$, $COD_{\text{in}}$, $NH_3$-$N$, TP, TDS, HRT, MLVSS, pH | $BOD_{\text{eff}}$, $COD_{\text{eff}}$, $NH_3$-$N_{\text{eff}}$, $TP_{\text{eff}}$ | $R^2 > 0.98$ trên toàn bộ tập kiểm tra |
| **Cai et al. (2019b)** | MBR sợi rỗng | WNN (3-2-1) | $COD_{\text{in}}$, $NH_3$-$N_{\text{in}}$, Độ mặn (Salinity) | $COD_{\text{eff}}$, $NH_3$-$N_{\text{eff}}$ | COD đạt $R^2 = 0.999$, $NH_3$-$N$ đạt $R^2 = 0.997$ |
| **Li et al. (2022)** | Bể phản ứng sinh học màng kỵ khí (AnMBR) | DenseNet, CNN, FCN | Nhiệt độ môi trường, Nhiệt độ nước vào, pH vào, $COD_{\text{in}}$, Nhiệt độ bùn, Thông lượng $J$ | pH ra, $COD_{\text{eff}}$, Tỷ lệ khử COD, Sản lượng khí sinh học ($CH_4, N_2, CO_2$), ORP | DenseNet đạt độ chính xác $97.4\%$ (FCN $92.6\%$, CNN $91.8\%$) |
| **Yaqub et al. (2020)** | Hệ thống liên hợp $A^2/O$-MBR | LSTM (Long Short-Term Memory) | $TOC_{\text{in}}$, TN, TP, COD, $NH_3$-$N$, SS, DO, ORP, MLSS | Tỷ lệ loại bỏ TN, TP, $NH_3$-$N$ | Loại bỏ $NH_3$-$N$ tối ưu với sai số $\text{MSE} = 0.0047$ |
| **Wolf et al. (2001, 2003)** | MBR công nghiệp | MLP liên kết truyền thẳng | Chỉ số ô nhiễm cơ bản, Tải trọng hữu cơ, Điều kiện sục khí | Nồng độ vết các hợp chất vi ô nhiễm hữu cơ nguy hại | Dự đoán chính xác xu hướng suy giảm nồng độ vết |
