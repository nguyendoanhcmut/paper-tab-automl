## Chương 3: Phân tích giải thích cơ chế loại bỏ NH4+-N, NO3--N và NO2--N

### 3.1 Xếp hạng độ quan trọng biến số cho nồng độ và hiệu suất khử NH4+-N

#### 3.1.1 Thứ tự độ quan trọng đối với nồng độ NH4+-N dòng ra
- Mô hình máy học GBM và XGBoost xếp hạng độ quan trọng của 15 biến đầu vào. Thứ tự giảm dần ảnh hưởng đến nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra gồm:
  $$\text{TIN nạp} > \text{C/N} > \text{NH}_4^+\text{-N nạp} > \text{Thời gian vận hành} > \text{Chi vi khuẩn Anammox chiếm ưu thế} > \text{HRT} > \text{NO}_3^-\text{-N nạp} > \text{Hình thái bùn} > \text{NLR} > \text{Loại quy trình} > \text{COD nạp} > \text{NO}_2^-\text{-N nạp} > \text{Chiến lược làm giàu} > \text{Điều kiện vận hành} > \text{Loại nước thải}$$
- Biến $\text{TIN}$ nạp giữ vị trí quan trọng số một (Hình 3(a)). Giá trị này kiểm soát tổng lượng nitơ đi vào hệ thống xử lý.
- Tỷ số $\text{C/N}$ giữ vị trí quan trọng thứ hai. Tỷ số này quyết định sự cạnh tranh giữa vi khuẩn dị dưỡng và vi khuẩn Anammox tự dưỡng.
- Nồng độ $\text{NH}_4^+$-$\text{N}$ nạp giữ vị trí quan trọng thứ ba. Đây là cơ chất trực tiếp của vi khuẩn Anammox.

#### 3.1.2 Thứ tự độ quan trọng đối với hiệu suất khử NH4+-N
- Nồng độ $\text{NO}_3^-$-$\text{N}$ nạp thể hiện độ quan trọng vượt bậc đối với hiệu suất loại bỏ $\text{NH}_4^+$-$\text{N}$ (Hình 3(e)).
- $\text{NO}_3^-$-$\text{N}$ đóng vai trò là chất nhận electron ban đầu cho quá trình khử nitrat một phần (PDA). Quá trình này khử $\text{NO}_3^-$ thành $\text{NO}_2^-$.
- Nồng độ $\text{NO}_2^-$ sinh ra cung cấp cơ chất thiết yếu cho phản ứng Anammox. Thiếu $\text{NO}_2^-$ sẽ làm suy giảm trực tiếp hiệu suất oxy hóa $\text{NH}_4^+$.

#### 3.1.3 Vai trò chi phối tuyệt đối của thành phần cacbon và nitơ đầu vào
- Bốn biến số gồm $\text{TIN}$ nạp, $\text{C/N}$, $\text{NH}_4^+$-$\text{N}$ nạp và $\text{NO}_3^-$-$\text{N}$ nạp chi phối việc loại bỏ $\text{NH}_4^+$-$\text{N}$.
- Phản ứng Anammox đòi hỏi tỷ lệ cơ chất nghiêm ngặt theo phương trình phản ứng sinh hóa:
  $$\text{NH}_4^+ + 1.32\text{NO}_2^- + 0.066\text{HCO}_3^- + 0.13\text{H}^+ \rightarrow 1.02\text{N}_2 + 0.26\text{NO}_3^- + 0.066\text{CH}_2\text{O}_{0.5}\text{N}_{0.15} + 2.03\text{H}_2\text{O}$$
- Quá trình loại bỏ $\text{NH}_4^+$-$\text{N}$ phụ thuộc hoàn toàn vào hoạt tính của vi khuẩn Anammox. Thành phần dinh dưỡng dòng vào tác động mạnh mẽ đến hoạt tính này.

#### 3.1.4 Giải thích vị trí cuối bảng của biến loại nước thải
- Biến loại nước thải (nước thải nhân tạo hay nước thải đô thị thực tế) xếp cuối bảng độ quan trọng (Hình 3(a), (e)).
- Các công trình nghiên cứu thường đơn giản hóa nước thải đô thị thành các chỉ tiêu ô nhiễm cơ bản. Các chỉ tiêu này bao gồm $\text{COD}$, $\text{NH}_4^+$-$\text{N}$ và $\text{TIN}$.
- Mô hình học máy nhận diện trực tiếp các giá trị nồng độ ô nhiễm cụ thể.
- Sự khác biệt định tính giữa hai loại nước thải do đó bị che mờ trong tập dữ liệu. Điều này giải thích vì sao biến loại nước thải có ảnh hưởng thấp nhất.

#### 3.1.5 Vai trò của thời gian vận hành và chi vi khuẩn Anammox chiếm ưu thế
- Thời gian vận hành và chi vi khuẩn Anammox chiếm ưu thế giữ vị trí quan trọng thứ tư và thứ năm.
- Vi khuẩn Anammox có tốc độ tăng trưởng rất chậm. Thời gian nhân đôi sinh khối kéo dài từ 7 đến 14 ngày.
- Làm giàu sinh khối và chọn lọc chủng vi sinh thích nghi theo thời gian. Đây là yếu tố quyết định để tiêu thụ amoni triệt để.
- Các biến gồm hình thái bùn, loại quy trình, chiến lược làm giàu và điều kiện vận hành thể hiện độ quan trọng thấp hơn. Các hệ thống này đều vận hành theo cùng các con đường sinh hóa loại bỏ nitơ tương đương.

---

### 3.2 Phản ứng đơn biến (1D PDP) và tương tác hai chiều (2D PDP) của NH4+-N dòng ra

#### 3.2.1 Động học đơn biến (1D PDP) của nồng độ amoni dòng ra
- Động học theo thời gian vận hành (Hình S4(a)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra giảm đơn điệu theo thời gian vận hành.
  - Quần xã vi sinh vật thích nghi và trưởng thành qua các giai đoạn sau, giúp nâng cao hiệu suất xử lý nước thải.
- Động học theo tỷ lệ $\text{C/N}$ (Hình S4(b)):
  - Biểu đồ 1D PDP xác định dải tối ưu hẹp của tỷ số $\text{C/N}$ từ $2.72$ đến $6.32$.
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra đạt mức thấp nhất trong dải tối ưu này.
  - Khi $\text{C/N} < 2.72$: Nước thải thiếu hụt cacbon hữu cơ. Quá trình khử nitrat một phần (PDA) suy giảm, không cung cấp đủ lượng $\text{NO}_2^-$ làm cơ chất cho Anammox.
  - Khi $\text{C/N} > 6.32$: Lượng cacbon hữu cơ dư thừa kích thích vi khuẩn dị dưỡng phát triển mạnh. Vi khuẩn dị dưỡng cạnh tranh không gian sống và cơ chất, ức chế vi khuẩn Anammox.
  - Kết quả này phù hợp với công bố của Miao et al. (2018). Nghiên cứu cho thấy hiệu suất khử $\text{NH}_4^+$-$\text{N}$ tăng đều đặn khi tăng tỷ số $\text{C/N}$ từ $1.1$ lên $2.5$.
- Ngưỡng tới hạn của amoni và tổng nitơ nạp (Hình S4(c), (d)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng vọt khi $\text{NH}_4^+$-$\text{N}$ nạp đạt ngưỡng tới hạn $62.32\text{ mg/L}$.
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng vọt khi $\text{TIN}$ nạp đạt ngưỡng tới hạn $91.08\text{ mg/L}$.
  - Nước thải đô thị thực tế thường có nồng độ nitơ thấp hơn hai ngưỡng tới hạn này. Do đó, các công nghệ dựa trên Anammox rất phù hợp để xử lý nước thải đô thị dòng chính.

#### 3.2.2 Tương tác bề mặt phản ứng hai biến (2D PDP) của NH4+-N dòng ra
- Tương tác giữa $\text{TIN}$ nạp và tỷ lệ $\text{C/N}$ (Hình 4(a)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra đạt điểm cực tiểu $4.23\text{ mg/L}$ tại $\text{C/N} = 2.75$ và $\text{TIN}$ nạp từ $18.85\text{ mg/L}$ đến $87.76\text{ mg/L}$.
  - Khi $\text{TIN}$ nạp vượt quá $87.76\text{ mg/L}$, nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng vọt lên $17.0\text{ mg/L}$.
  - Cơ chế: Tại cùng một tỷ số $\text{C/N}$, tăng $\text{TIN}$ nạp kéo theo sự gia tăng của nồng độ $\text{COD}$ nạp tuyệt đối. Lượng $\text{COD}$ cao thúc đẩy vi khuẩn dị dưỡng tăng sinh, chiếm diện tích sống và ức chế sinh khối Anammox.
- Tương tác giữa $\text{C/N}$ và $\text{NH}_4^+$-$\text{N}$ nạp (Hình 4(d)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra duy trì mức thấp từ $7.17\text{ mg/L}$ đến $10.74\text{ mg/L}$ trên dải rộng.
  - Vùng vận hành ổn định này kéo dài từ $\text{C/N} = 2.36$ đến $9.62$ và $\text{NH}_4^+$-$\text{N}$ nạp từ $13.83\text{ mg/L}$ đến $213.84\text{ mg/L}$.
  - Dải tối ưu này rộng hơn dải tương tác của $\text{TIN}$ nạp. Nguyên nhân do $\text{TIN}$ chứa cả các dạng nitơ oxy hóa ($\text{NO}_3^-$-$\text{N}$ và $\text{NO}_2^-$-$\text{N}$).
- Tương tác giữa $\text{TIN}$ nạp và $\text{NH}_4^+$-$\text{N}$ nạp (Hình 4(b)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra tăng mạnh khi tăng đồng thời cả $\text{NH}_4^+$-$\text{N}$ nạp và $\text{TIN}$ nạp. Kết quả này hoàn toàn thống nhất với động học 1D PDP.
- Tương tác giữa Thời gian vận hành và Dinh dưỡng nạp (Hình 4(c), (f)):
  - Thời gian vận hành kết hợp với $\text{TIN}$ nạp làm giảm nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra từ $32.16\text{ mg/L}$ xuống còn $4.68\text{ mg/L}$.
  - Thời gian vận hành kết hợp với $\text{NH}_4^+$-$\text{N}$ nạp làm giảm nồng độ $\text{NH}_4^+$-$\text{N}$ dòng ra từ $20.46\text{ mg/L}$ xuống còn $4.12\text{ mg/L}$.
  - Quá trình thuần hóa sinh khối kéo dài giúp hệ vi sinh vật tăng cường năng lực xử lý tải nạp cao.
- Tương tác giữa Thời gian vận hành và tỷ lệ $\text{C/N}$ (Hình 4(e)):
  - Bề mặt 2D PDP thể hiện cấu trúc đỉnh và thung lũng phức tạp nhất.
  - Vùng nồng độ $\text{NH}_4^+$-$\text{N}$ cực tiểu ổn định nhất duy trì tại dải $\text{C/N}$ từ $2.75$ đến $6.48$. Kết quả này tương đồng chặt chẽ với phân tích 1D PDP.

---

### 3.3 Phân tích độ quan trọng biến số và động học phát sinh NO3--N và NO2--N dòng ra

#### 3.3.1 Thứ tự độ quan trọng đối với NO3--N và NO2--N dòng ra
- Thứ tự độ quan trọng đối với nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra (Hình 3(b)):
  $$\text{Thời gian vận hành} > \text{NO}_3^-\text{-N nạp} > \text{HRT} > \text{TIN nạp} > \text{COD nạp} > \text{Loại quy trình}$$
- Thứ tự độ quan trọng đối với nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra (Hình 3(c)):
  $$\text{TIN nạp} > \text{Thời gian vận hành} > \text{NO}_3^-\text{-N nạp} > \text{NH}_4^+\text{-N nạp} > \text{NLR} > \text{Chi vi khuẩn Anammox chiếm ưu thế}$$
- Đặc điểm phân hóa: $\text{HRT}$ và $\text{COD}$ nạp kiểm soát mạnh phản ứng khử nitrat để điều hòa $\text{NO}_3^-$-$\text{N}$. Trong khi đó, $\text{TIN}$ nạp và $\text{NLR}$ chi phối mức độ tích lũy cơ chất trung gian $\text{NO}_2^-$-$\text{N}$.

#### 3.3.2 Động học đơn biến (1D PDP) của NO2--N và đỉnh tích lũy tại mốc 30 ngày
- Hiện tượng tích lũy nitrit ở mốc thời gian 30 ngày (Hình S7(a)):
  - Nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra đạt đỉnh cục bộ rõ rệt ở mốc thời gian vận hành 30 ngày.
  - Sau mốc 30 ngày, phản ứng của $\text{NO}_2^-$-$\text{N}$ giảm nhanh và biến thiên tương đồng với $\text{NO}_3^-$-$\text{N}$.
- Cơ chế sinh học vi sinh:
  - Ở giai đoạn bắt đầu vận hành, lượng $\text{NO}_2^-$ sinh ra nhiều hơn lượng $\text{NO}_2^-$ tiêu thụ.
  - Phản ứng nitrit hóa một phần (PN) hoặc khử nitrat một phần (PD) tạo ra nhiều $\text{NO}_2^-$:
    $$\text{PN: } \text{NH}_4^+ + 1.5\text{O}_2 \rightarrow \text{NO}_2^- + \text{H}_2\text{O} + 2\text{H}^+$$
    $$\text{PD: } \text{NO}_3^- + 0.28\text{CH}_3\text{COOH} \rightarrow \text{NO}_2^- + 0.56\text{CO}_2 + 0.68\text{H}_2\text{O} + 0.12\text{OH}^-$$
  - Vi khuẩn Anammox chưa trưởng thành và chưa tích lũy đủ sinh khối để tiêu thụ lượng $\text{NO}_2^-$ này.
  - Nghiên cứu của Yang et al. (2024) chứng minh tỷ lệ đóng góp của Anammox vào loại bỏ nitơ chỉ đạt $13.8\%$ ở giai đoạn $36 - 75\text{ ngày}$. Tỷ lệ này tăng vọt lên $67.1\%$ ở giai đoạn $216 - 258\text{ ngày}$.

#### 3.3.3 Tác động của HRT và COD nạp lên nồng độ NO3--N dòng ra
- Tác động của thời gian lưu thủy lực $\text{HRT}$ lên $\text{NO}_3^-$-$\text{N}$ (Hình S5(b)):
  - Xuất hiện đỉnh tích lũy nitrat mạnh tại dải $\text{HRT}$ từ $10.47\text{ h}$ đến $15.13\text{ h}$.
  - Theo Yang et al. (2024), $\text{HRT} = 10\text{ h}$ không mang lại hiệu quả cho quy trình Anammox và làm trầm trọng thêm tình trạng thiếu cacbon hữu cơ.
  - Kéo dài $\text{HRT}$ lên $17\text{ h}$ giúp mở rộng thời gian lưu vùng thiếu khí từ $5.67\text{ h}$ lên $8.50\text{ h}$. Nhờ đó, $\text{NO}_3^-$-$\text{N}$ dòng ra trung bình giảm sâu từ $14.46\text{ mg/L}$ xuống còn $9.79\text{ mg/L}$.
  - Kéo dài $\text{HRT}$ điều tiết sự cạnh tranh nitrit giữa vi khuẩn khử nitrat và vi khuẩn Anammox.
  - Rút ngắn $\text{HRT} < 9.95\text{ h}$ giúp giảm tích lũy $\text{NO}_3^-$-$\text{N}$ nhờ rửa trôi vi khuẩn oxy hóa nitrit (NOB).
- Tác động của nồng độ $\text{COD}$ nạp lên $\text{NO}_3^-$-$\text{N}$ (Hình S5(c)):
  - Khi $\text{COD} < 189.87\text{ mg/L}$: Thiếu hụt cacbon hữu cơ làm suy giảm hoạt tính khử nitrat dị dưỡng, gây tích lũy $\text{NO}_3^-$-$\text{N}$.
  - Khi $\text{COD} > 316.46\text{ mg/L}$: Nồng độ chất hữu cơ cao gây ức chế vi khuẩn Anammox, làm suy giảm hiệu suất loại bỏ nitơ toàn hệ thống.
  - Dải nồng độ $\text{COD}$ nạp tối ưu nằm trong khoảng $200.42 - 305.91\text{ mg/L}$.

#### 3.3.4 Tác động của dinh dưỡng nạp và tải trọng NLR lên NO3--N và NO2--N
- Tác động của $\text{TIN}$ nạp và $\text{NO}_3^-$-$\text{N}$ nạp lên $\text{NO}_3^-$-$\text{N}$ dòng ra (Hình S5(d), (e)):
  - Khi $\text{TIN}$ nạp thấp ($< 55.33\text{ mg/L}$), nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra duy trì ở mức cao từ $6.85\text{ mg/L}$ đến $7.82\text{ mg/L}$.
  - Sau đó, nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra tăng dần từ $4.41\text{ mg/L}$ lên $7.42\text{ mg/L}$ theo $\text{NO}_3^-$-$\text{N}$ nạp. Nồng độ này tăng từ $4.45\text{ mg/L}$ lên $5.81\text{ mg/L}$ theo $\text{TIN}$ nạp.
- Tác động của tải trọng nạp $\text{NLR}$ lên $\text{NO}_2^-$-$\text{N}$ dòng ra (Hình S7(e)):
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ nạp, $\text{NO}_3^-$-$\text{N}$ nạp và $\text{TIN}$ nạp tăng đều thúc đẩy tăng nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra (Hình S7(b)-(d)).
  - Tải trọng nạp nitơ thấp ($\text{NLR} < 0.95\text{ kg N/m}^3/\text{ngày}$) gây tích lũy $\text{NO}_2^-$-$\text{N}$ cao ở mức $4.57\text{ mg/L}$.
  - Khi $\text{NLR} > 0.95\text{ kg N/m}^3/\text{ngày}$, nồng độ $\text{NO}_2^-$-$\text{N}$ dòng ra giảm nhanh xuống $2.51\text{ mg/L}$ và duy trì ổn định.

---

### 3.4 Tác động tương hỗ đa biến (2D PDP) của HRT, COD và thành phần nitơ lên NO3--N và NO2--N

#### 3.4.1 Tương tác giữa Thời gian vận hành và NO3--N nạp qua con đường DNRA
- Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra đạt đỉnh cao nhất ở giai đoạn đầu vận hành kết hợp nồng độ $\text{NO}_3^-$-$\text{N}$ nạp cao (Hình S6(a)).
- Khi kéo dài thời gian vận hành, hệ thống Anammox gia tăng mạnh mẽ năng lực loại bỏ $\text{NO}_3^-$-$\text{N}$.
- Cơ chế chuyển hóa: $\text{NO}_3^-$-$\text{N}$ được tiêu thụ qua con đường khử nitrat dị hóa thành amoni (DNRA: Dissimilatory Nitrate Reduction to Ammonium):
  $$\text{NO}_3^- \rightarrow \text{NO}_2^- \rightarrow \text{NH}_4^+$$
- Lượng $\text{NO}_2^-$ và $\text{NH}_4^+$ sinh ra tiếp tục được vi khuẩn Anammox chuyển hóa thành khí $\text{N}_2$. Chuỗi phản ứng liên hoàn này giúp triệt tiêu hoàn toàn lượng nitrat tồn dư.

#### 3.4.2 Tương hỗ phức tạp giữa HRT và các thành phần dinh dưỡng nạp
- Đỉnh nồng độ $\text{NO}_3^-$-$\text{N}$ xuất hiện cố định tại dải $\text{HRT}$ từ $10.47\text{ h}$ đến $10.98\text{ h}$ xuyên suốt toàn bộ thời gian vận hành (Hình S6(b)).
- Thiết lập $\text{HRT} < 9.95\text{ h}$ giúp hạn chế tích lũy $\text{NO}_3^-$-$\text{N}$ trên toàn bộ các dải nồng độ $\text{NO}_3^-$-$\text{N}$ nạp (Hình S6(e)).
- Tương tác giữa $\text{HRT}$ và $\text{TIN}$ nạp (Hình S6(h)):
  - Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra đạt mức thấp khi kết hợp $\text{HRT}$ cao ($> 15.64\text{ h}$) với $\text{TIN}$ nạp cao.
  - Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra cũng đạt mức thấp khi kết hợp $\text{HRT}$ thấp ($< 9.95\text{ h}$) với $\text{TIN}$ nạp thấp.
  - Ngược lại, duy trì $\text{HRT}$ cao ($> 15.64\text{ h}$) ở mức $\text{TIN}$ nạp thấp thúc đẩy tích lũy $\text{NO}_3^-$-$\text{N}$. Điều kiện này tạo thuận lợi cho vi khuẩn NOB phát triển.

#### 3.4.3 Cấu trúc hai thung lũng nồng độ NO3--N giữa COD nạp và HRT
- Tương tác giữa $\text{COD}$ nạp và $\text{HRT}$ thể hiện tính chất phi tuyến phức tạp nhất trên bề mặt 2D PDP (Hình S6(i)).
- Mô hình xác định hai thung lũng nồng độ $\text{NO}_3^-$-$\text{N}$ cực thấp:
  - Thung lũng 1: $\text{COD}$ nạp $200.42 - 305.91\text{ mg/L}$ kết hợp với $\text{HRT} < 9.95\text{ h}$ (rửa trôi vi khuẩn NOB).
  - Thung lũng 2: $\text{COD}$ nạp $200.42 - 305.91\text{ mg/L}$ kết hợp với $\text{HRT}$ từ $11.50\text{ h}$ đến $12.54\text{ h}$ (đủ thời gian cho phản ứng khử nitrat).
- Kỹ sư công nghệ có thể lựa chọn một trong hai vùng vận hành này để cực tiểu hóa nồng độ nitrat đầu ra.

#### 3.4.4 Tương tác giữa các chất dinh dưỡng nạp và điểm tối ưu tuyệt đối
- Mối tương quan thuận giữa nồng độ $\text{NO}_3^-$-$\text{N}$ nạp và $\text{NO}_3^-$-$\text{N}$ dòng ra được xác nhận trên toàn dải đo (Hình S6(f), (g)).
- Nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra tăng cao ở vùng $\text{TIN}$ nạp thấp trên mọi khoảng $\text{COD}$ nạp (Hình S6(j)). Nguyên nhân do tỷ lệ $\text{NH}_4^+$-$\text{N}$ chiếm phần lớn trong $\text{TIN}$, làm mất cân bằng cơ chất khử nitrat thiếu khí.
- Điểm vận hành tối ưu tuyệt đối:
  - Phối hợp $\text{TIN}$ nạp từ $59.38\text{ mg/L}$ đến $87.76\text{ mg/L}$ và $\text{COD}$ nạp từ $200.42\text{ mg/L}$ đến $305.91\text{ mg/L}$.
  - Sự kết hợp này đạt nồng độ $\text{NO}_3^-$-$\text{N}$ dòng ra thấp kỷ lục, chỉ từ $1.39\text{ mg/L}$ đến $1.64\text{ mg/L}$.

#### 3.4.5 Động học tương tác điều tiết NO2--N dòng ra
- Động học bề mặt 2D PDP của $\text{NO}_2^-$-$\text{N}$ dòng ra thể hiện xu hướng giảm mạnh khi vận hành dài hạn kết hợp với:
  - Nồng độ $\text{NH}_4^+$-$\text{N}$ nạp (Hình S8(a)).
  - Nồng độ $\text{NO}_3^-$-$\text{N}$ nạp (Hình S8(b)).
  - Nồng độ $\text{TIN}$ nạp (Hình S8(c)).
  - Tải trọng nạp $\text{NLR}$ (Hình S8(d)).
- Vận hành dài hạn làm giảm gần như hoàn toàn lượng $\text{NO}_2^-$-$\text{N}$ dòng ra trong các hệ thống Anammox thành công.
- Tương tác giữa các thành phần nitơ nạp và tải trọng $\text{NLR}$ (Hình S8(e)-(j)):
  - $\text{NO}_2^-$-$\text{N}$ dòng ra liên hệ trực tiếp với tải nạp nitơ của hệ thống.
  - Quá trình PD và PN là hai nguồn cung cấp $\text{NO}_2^-$ chủ yếu. Quá trình Anammox tiêu thụ phần lớn lượng $\text{NO}_2^-$ này.
  - Tải nạp nitơ quá cao gây quá tải hệ thống. Hiện tượng này dẫn đến tích lũy $\text{NO}_2^-$-$\text{N}$ nếu sinh khối Anammox chưa đáp ứng kịp.
