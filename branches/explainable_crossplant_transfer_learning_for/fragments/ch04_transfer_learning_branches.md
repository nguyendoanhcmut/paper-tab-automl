## 3.3 Hiệu năng và giải thích học chuyển giao (Transfer learning performance and interpretation)

### 3.3.1 Ảnh hưởng của tỷ lệ tinh chỉnh đến hiệu năng học chuyển giao (Effect of fine-tuning ratio on transfer learning performance)

#### 3.3.1.1 Hiệu năng khi chuyển giao trực tiếp (Zero-shot transfer, FT = 0%)
- Định nghĩa điều kiện chuyển giao trực tiếp: Tỷ lệ tinh chỉnh $FT = 0\%$ đại diện cho quá trình chuyển giao không mẫu (zero-shot transfer). Mô hình tiền huấn luyện từ trạm nguồn dự báo trực tiếp trên trạm đích mà không qua thích ứng dữ liệu đích.
- Suy giảm hiệu năng của mô hình nguồn: Cả hai mô hình LSTM và XGBoost tiền huấn luyện đều cho hệ số xác định thấp. Mô hình LSTM đạt $R^2 = 0.41$. Mô hình XGBoost đạt $R^2 = 0.39$.
- Nguyên nhân suy giảm dự báo: Phân tích PCA trước đó xác nhận sự tồn tại của độ lệch phân phối (distribution shift) có thể đo lường được giữa trạm nguồn và trạm đích.
- Giới hạn của chuyển giao trực tiếp: Việc chỉ áp dụng chuyển giao trực tiếp không đủ độ tin cậy để dự báo áp suất xuyên màng ($\text{TMP}$) tại trạm xử lý mới [53].

#### 3.3.1.2 Động học cải thiện hiệu năng theo tỷ lệ tinh chỉnh (FT từ 10% đến 50%)
- Bước nhảy vọt ban đầu của LSTM-FT: Mức tăng hiệu năng lớn nhất xuất hiện khi nâng tỷ lệ tinh chỉnh từ $FT = 0\%$ lên $FT = 10\%$. Hệ số xác định $R^2$ tăng vọt từ $0.41$ lên $0.81$ (Hình 5(a)).
- Quỹ đạo cải thiện tiệm tiến của LSTM-FT: Khi tăng dần $FT$ từ $10\%$ đến $40\%$, hiệu năng mô hình tiếp tục tăng trưởng ổn định. Tại $FT = 40\%$, mô hình đạt $R^2 = 0.89$, sai số $\text{RMSE} = 0.50\text{ kPa}$ và $\text{MAE} = 0.33\text{ kPa}$ (Hình 5(b) và (c)).
- Hiện tượng bão hòa tại mức tinh chỉnh cao: Khi tăng lên $FT = 50\%$, mức cải thiện sai số và tương quan so với mức $FT = 40\%$ chỉ mang tính thứ yếu, không đáng kể.
- Quỹ đạo thích ứng của XGBoost-FT: Mô hình XGBoost-FT cũng cải thiện hiệu năng khi tăng tỷ lệ $FT$, nhưng tốc độ tăng chậm và biên độ cải thiện thấp hơn nhiều so với LSTM-FT.
- Số liệu tiến hóa của XGBoost-FT: Hệ số $R^2$ của XGBoost-FT chỉ tăng từ $0.39$ ở $FT = 0\%$ lên $0.58$ ở $FT = 40\%$, và đạt $0.61$ ở $FT = 50\%$.

#### 3.3.1.3 Điểm bão hòa tối ưu và độ ổn định mô hình tại FT = 40%
- Vượt trội của mô hình chuỗi thời gian: LSTM-FT tạo ra bước nhảy hiệu năng lớn ngay ở các mức dữ liệu đích rất thấp ($FT = 10\%$) so với XGBoost-FT. Việc bổ sung dữ liệu vượt quá $40\%$ không mang lại lợi ích gia tăng rõ rệt.
- Bản chất học chuyển giao trong điều kiện khan hiếm dữ liệu: Hai mô hình thích ứng từ mạng tiền huấn luyện trạm nguồn phản ánh năng lực thích ứng với tập dữ liệu đích hạn chế ($N = 71$ bản ghi thực tế), thay vì phát triển mô hình truyền thống từ đầu.
- Phân tích phương sai và độ phân tán mô hình: Độ lệch chuẩn (standard deviation) qua các phân đoạn tinh chỉnh và các lần lặp ngẫu nhiên đạt giá trị lớn nhất tại $FT = 10\%$. Độ phân tán này giảm dần khi tăng $FT$ và đạt mức rất nhỏ tại $FT = 40\%$.
- Giao thức đánh giá độ vững: Quá trình đánh giá sử dụng tối đa 6 phân đoạn dữ liệu liên tục từ kho tinh chỉnh và thử nghiệm trên 5 hạt giống ngẫu nhiên (random seeds) cho mỗi phân đoạn giữ lại.
- Cơ chế ổn định: Lượng dữ liệu đích quá ít làm giảm tính vững chắc của quá trình thích ứng. Một lượng dữ liệu đích vừa phải ($FT = 40\%$) đã đủ để mô hình đạt trạng thái ổn định cao nhất. Do đó, $FT = 40\%$ được chọn làm điều kiện chuẩn cho các phân tích chuyên sâu tiếp theo.

Bảng 1: So sánh động học hiệu năng dự báo theo tỷ lệ tinh chỉnh ($FT$) của mô hình LSTM-FT và XGBoost-FT.
| Tỷ lệ tinh chỉnh ($FT$) | LSTM-FT: $R^2$ | LSTM-FT: RMSE ($\text{kPa}$) | LSTM-FT: MAE ($\text{kPa}$) | XGBoost-FT: $R^2$ | Ghi chú trạng thái mô hình |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $0\%$ (Zero-shot) | $0.41$ | - | - | $0.39$ | Chuyển giao trực tiếp, lệch phân phối dữ liệu |
| $10\%$ | $0.81$ | - | - | - | Bước nhảy vọt lớn nhất, phương sai giữa các lần chạy cao |
| $20\%$ | - | - | - | - | Hiệu năng cải thiện tiệm tiến |
| $30\%$ | - | - | - | - | Cấu trúc phân bổ đặc trưng bắt đầu cân bằng |
| $40\%$ (Tối ưu) | $0.89$ | $0.50$ | $0.33$ | $0.58$ | Điểm bão hòa tối ưu, sai số tối thiểu, độ ổn định cao |
| $50\%$ | $0.89$ | - | - | $0.61$ | Lợi ích gia tăng bão hòa, cải thiện không đáng kể |

---

### 3.3.2 So sánh hiệu năng giữa mô hình đường cơ sở và các mô hình học chuyển giao (Performance comparison of baseline model and transfer learning models)

#### 3.3.2.1 Phân bố mẫu thử nghiệm và độ lệch dự báo TMP
- Miền giá trị mẫu thử nghiệm: Tập mẫu thử nghiệm tại trạm đích phân bố chủ yếu trong dải áp suất xuyên màng $\text{TMP} \approx 19\text{--}21.5\text{ kPa}$. Một số lượng ít mẫu thử phân bố ở dải $\text{TMP}$ thấp hơn từ $15.5\text{--}18\text{ kPa}$ (Hình 5(d)).
- Độ chụm quỹ đạo của LSTM-FT: Trong toàn bộ dải $\text{TMP}$, các điểm dự báo của LSTM-FT ($FT = 40\%$) phân bố sát nhất quanh đường phân giác lý tưởng ($y = x$), thể hiện độ tương thích cao nhất giữa giá trị dự báo và giá trị quan trắc thực tế.
- Sai lệch của mô hình đường cơ sở: Mô hình đường cơ sở (Baseline model huấn luyện thuần túy trên dữ liệu trạm đích) thể hiện các độ lệch phân tán ở mức trung bình.
- Độ phân tán nghiêm trọng của XGBoost-FT: Mô hình XGBoost-FT thể hiện vùng phân tán rộng nhất và rời xa rõ rệt nhất khỏi đường phân giác lý tưởng.

#### 3.3.2.2 So sánh định lượng giữa LSTM-FT, XGBoost-FT và Baseline
- Sai số của mô hình đường cơ sở trạm đích: Mô hình Baseline thuần túy chỉ sử dụng tập dữ liệu đích đạt $R^2 = 0.82$, sai số $\text{RMSE} = 0.63\text{ kPa}$ và $\text{MAE} = 0.45\text{ kPa}$.
- Cải thiện vượt trội của LSTM-FT: So với mô hình đường cơ sở, LSTM-FT giảm sai số $\text{RMSE}$ từ $0.63\text{ kPa}$ xuống $0.50\text{ kPa}$ (giảm $20.6\%$). Mô hình giảm sai số $\text{MAE}$ từ $0.45\text{ kPa}$ xuống $0.33\text{ kPa}$ (giảm $26.7\%$). Hệ số xác định $R^2$ tăng từ $0.82$ lên $0.89$.
- Thất bại của XGBoost-FT trong việc thích ứng: Mô hình XGBoost-FT không mang lại lợi thế chuyển giao. Sai số $\text{RMSE}$ tăng vọt lên $0.96\text{ kPa}$. Sai số $\text{MAE}$ tăng lên $0.81\text{ kPa}$. Hệ số xác định $R^2$ sụt giảm xuống mức thấp $0.58$.
- Khẳng định tính hiệu quả của mạng hồi quy: Phương pháp học chuyển giao phát huy tối đa hiệu quả khi kết hợp với cấu trúc mạng nơ-ron hồi quy LSTM, vượt qua cả mô hình nội tại trạm đích và mô hình cây quyết định tăng cường.

Bảng 2: So sánh định lượng hiệu năng trên tập kiểm tra trạm đích tại $FT = 40\%$.
| Mô hình đánh giá | $R^2$ | RMSE ($\text{kPa}$) | MAE ($\text{kPa}$) | Tỷ lệ giảm RMSE so với Baseline | Tỷ lệ giảm MAE so với Baseline |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LSTM-FT** | $\mathbf{0.89}$ | $\mathbf{0.50}$ | $\mathbf{0.33}$ | $\mathbf{-20.6\%}$ | $\mathbf{-26.7\%}$ |
| **Target Baseline** | $0.82$ | $0.63$ | $0.45$ | Quy chuẩn cơ sở ($0\%$) | Quy chuẩn cơ sở ($0\%$) |
| **XGBoost-FT** | $0.58$ | $0.96$ | $0.81$ | $+52.4\%$ (Tăng sai số) | $+80.0\%$ (Tăng sai số) |

#### 3.3.2.3 Nguyên nhân kiến trúc LSTM vượt trội hơn XGBoost trong học chuyển giao chuỗi thời gian
- Bản chất tích lũy lịch sử của bám bẩn màng: Hiện tượng tắc nghẽn màng lọc trong hệ thống MBR diễn ra qua chuỗi tích tụ liên tục theo thời gian của các hạt keo, bông bùn và hợp chất cao phân tử trên bề mặt màng.
- Cơ chế bộ nhớ cổng của LSTM: Mạng LSTM sở hữu các cổng quên (forget gate), cổng vào (input gate) và cổng ra (output gate). Cấu trúc này cho phép lưu giữ thông tin phụ thuộc thời gian dài hạn và quy luật suy thoái màng từ trạm nguồn.
- Điểm yếu cố hữu của XGBoost dạng bảng: Cấu trúc cây quyết định phân vùng của XGBoost giả định các mẫu quan sát độc lập tĩnh. Thuật toán không nắm bắt được mối liên hệ chuỗi thời gian và sự phụ thuộc trễ của các chu kỳ lọc - rửa ngược.
- Hiện tượng quá khớp do cỡ mẫu nhỏ: Khi trạm đích bị hạn chế dữ liệu ($N = 41$ mẫu huấn luyện trong tổng số $71$ bản ghi), mô hình Baseline thuần túy dễ rơi vào hiện tượng quá khớp (overfitting) cục bộ. Trong khi đó, LSTM-FT tận dụng trọng số biểu diễn sâu trạm nguồn để dẫn hướng tối ưu hóa chính xác.

---

### 3.3.3 Giải thích đóng góp đặc trưng trong quá trình chuyển giao bằng LOFO và SHAP (LOFO and SHAP interpretation of feature contributions during transfer)

#### 3.3.3.1 Phân tích độ nhạy loại bỏ một đặc trưng (LOFO analysis tại FT = 40%)
- Giao thức phân tích LOFO: Phân tích Leave-One-Feature-Out (LOFO) đánh giá trực tiếp vai trò của từng biến đầu vào trên mô hình LSTM-FT tại điều kiện chuẩn $FT = 40\%$ (Hình 5(e)).
- Mô hình tham chiếu đầy đủ: Mô hình tham chiếu huấn luyện với toàn bộ các biến đầu vào đạt sai số $\text{MAE} = 0.33\text{ kPa}$.
- Quy chuẩn kiểm định thống kê: Sự suy giảm hiệu năng khi loại bỏ từng biến được kiểm tra qua kiểm định cặp dấu hạng Wilcoxon hai phía (paired two-sided Wilcoxon signed-rank tests, Bảng S10).
- Tác động áp đảo của EPSc: Việc loại bỏ đặc trưng polysaccharide ngoại bào ($\text{EPSc}$) gây ra tổn thất hiệu năng nghiêm trọng nhất. Sai số $\text{MAE}$ tăng vọt từ $0.33\text{ kPa}$ lên $0.37\text{ kPa}$ ($p \le 0.001$). Điều này xác nhận $\text{EPSc}$ là biến quan trọng nhất duy trì độ chính xác của LSTM-FT.
- Tác động của protein ngoại bào và tuổi bùn: Khi loại bỏ đặc trưng protein ngoại bào ($\text{EPSp}$) hoặc thời gian lưu giữ bùn ($\text{SRT}$), sai số $\text{MAE}$ cùng tăng lên mức $0.35\text{ kPa}$ với ý nghĩa thống kê cao ($p \le 0.001$).
- Tác động của thông lượng màng: Loại bỏ biến thông lượng ($\text{FLUX}$) làm tăng nhẹ sai số nhưng vẫn đạt độ tin cậy thống kê ($p \le 0.01$).
- Kết luận từ kiểm định LOFO: Các biến liên quan đến EPS, đặc biệt là $\text{EPSc}$ và $\text{EPSp}$, chi phối áp đảo hiệu năng mô hình chuyển giao. Các biến vận hành $\text{SRT}$ và $\text{FLUX}$ đóng vai trò bổ trợ thứ cấp.

Bảng 3: Kết quả phân tích độ nhạy loại bỏ từng biến (LOFO) của mô hình LSTM-FT tại $FT = 40\%$.
| Biến đầu vào bị loại trừ | MAE sau khi loại biến ($\text{kPa}$) | Mức tăng sai số so với chuẩn | Giá trị p (Wilcoxon test) | Mức độ ý nghĩa thống kê |
| :--- | :--- | :--- | :--- | :--- |
| **Mô hình tham chiếu (Đầy đủ)** | $\mathbf{0.33}$ | $0.00$ | - | Điểm chuẩn tham chiếu |
| $\text{EPSc}$ (EPS polysaccharide) | $0.37$ | $+0.04$ | $p \le 0.001$ | Tác động nghiêm trọng nhất |
| $\text{EPSp}$ (EPS protein) | $0.35$ | $+0.02$ | $p \le 0.001$ | Rất quan trọng |
| $\text{SRT}$ (Tuổi bùn) | $0.35$ | $+0.02$ | $p \le 0.001$ | Quan trọng |
| $\text{FLUX}$ (Thông lượng lọc) | - | Nhỏ hơn | $p \le 0.01$ | Có ý nghĩa thống kê |

#### 3.3.3.2 Động thái tiến hóa phân bổ giá trị SHAP qua các mức FT
- Trạng thái chuyển giao không mẫu ($FT = 0\%$): Biến $\text{EPSc}$ đứng vị trí số 1 tuyệt đối, chiếm tỷ trọng quy gán giá trị SHAP lớn nhất, vượt xa các biến $\text{MLVSS}$ và $\text{EPSp}$ (Hình 6(b), Hình S8(a)). Mô hình bảo toàn quán tính cấu trúc quy gán tập trung vào $\text{EPSc}$ học được từ trạm nguồn.
- Giai đoạn chuyển tiếp ($FT = 10\%\text{--}30\%$): Cấu trúc quy gán SHAP trở nên phân bổ đồng đều hơn. Mức đóng góp của $\text{EPSp}$ tăng trưởng rõ rệt. Đóng góp của $\text{EPSc}$, $\text{SRT}$ và $\text{MLVSS}$ tiến dần đến trạng thái tương đương nhau (Hình S9 và S10).
- Trạng thái hoàn thiện tối ưu ($FT = 40\%$): Hai biến $\text{EPSc}$ và $\text{EPSp}$ trở thành hai đặc trưng xếp hạng cao nhất. Tổng giá trị đóng góp của $\text{EPSc}$ và $\text{EPSp}$ chiếm hơn $50\%$ tổng quy gán toàn mô hình (Hình 6(c), Hình S8(b)).
- Trạng thái bão hòa ổn định ($FT = 50\%$): Cấu trúc phân hạng đặc trưng và giá trị SHAP tại $FT = 50\%$ gần như trùng khớp hoàn toàn với trạng thái tại $FT = 40\%$ (Hình S11). Điều này giải thích hiện tượng bão hòa hiệu năng khi tăng tỷ lệ dữ liệu đích.

#### 3.3.3.3 Cấu trúc quy gán đặc trưng tập trung vào EPS sau tinh chỉnh
- Sự tái định chuẩn trọng số: Quá trình tinh chỉnh không xóa bỏ tri thức nguồn mà tái định chuẩn (recalibrate) trọng số để phù hợp với môi trường sinh hóa mới.
- Vị thế song hành của hệ EPS: Kết quả LOFO và SHAP hội tụ tại một kết luận then chốt: $\text{EPSc}$ duy trì vai trò rường cột bất biến, trong khi $\text{EPSp}$ được đánh thức và nâng tầm ảnh hưởng để phản ánh cấu trúc lớp bám bẩn trạm đích.

---

### 3.3.4 Cơ chế khoa học giúp học chuyển giao dự báo chính xác bám bẩn màng tại trạm đích (Mechanistic physicochemical evidence for transfer learning)

#### 3.3.4.1 Vai trò nền tảng phổ quát của EPSc trong ma trận bám bẩn màng
- Tri thức bám bẩn phổ quát được bảo lưu: Tại $FT = 0\%$, mô hình tiền huấn luyện vẫn giữ được độ chính xác nhất định ($R^2 = 0.41$) nhờ cấu trúc quy gán tập trung vào $\text{EPSc}$. Quy luật polysaccharide thúc đẩy bám bẩn là một đặc tính phổ quát giữa các trạm xử lý sinh học.
- Nồng độ polysaccharide cao tại trạm đích: Phân tích thực nghiệm cho thấy nồng độ $\text{EPSc}$ tại trạm đích đạt mức rất cao là $49.6\text{ mg/L}$.
- Cơ chế tạo lớp bánh bùn ngậm nước: Polysaccharide mang nhiều nhóm chức ưa nước (-OH). Nồng độ $\text{EPSc}$ cao làm tăng khả năng giữ nước tự do và ức chế khả năng tách nước của bùn hoạt tính. Quá trình này hình thành lớp bánh bùn có độ hydrat hóa cao, độ nén ép lớn và sức cản thủy lực đặc biệt cao.
- Bằng chứng kiểm chứng qua thời gian hút mao dẫn: Trạm đích ghi nhận giá trị thời gian hút mao dẫn cao $\text{CST} = 49.45\text{ s}$ và thời gian hút mao dẫn riêng đạt $4.36\text{ s/(g/L)}$ (Hình 7(a)). Các số liệu này xác nhận $\text{EPSc}$ đại diện cho ma trận bám bẩn cốt lõi được bảo lưu nguyên vẹn qua quá trình chuyển giao.

#### 3.3.4.2 Tương tác Fe-EPS thúc đẩy vai trò EPSp và nén chặt lớp bánh bùn
- Hiện tượng gia tăng độ nhạy với EPSp: Khi mô hình đạt hiệu năng đỉnh cao tại $FT = 40\%$ ($R^2 = 0.89$), biến $\text{EPSp}$ vươn lên thành đặc trưng quan trọng thứ hai trong SHAP. Quá trình tinh chỉnh đã giúp mạng LSTM nhận thức được tín hiệu protein ngoại bào đặc thù của trạm đích.
- Dấu vết huỳnh quang protein thơm: Phổ ma trận kích thích - phát xạ huỳnh quang ($\text{EEM}$) của mẫu EPS trạm đích ghi nhận đỉnh tín hiệu vượt trội của các hợp chất giống protein thơm (aromatic protein-like peak, Hình 7(b)).
- Ảnh hưởng từ điều kiện châm sắt ($\text{Fe}^{3+}$): Nước thải đầu vào của trạm đích được bổ sung sắt nhằm tăng cường keo tụ photpho [54]. Nghiên cứu so sánh hai giai đoạn định lượng Fe tại bể khuấy trộn trước xử lý với nồng độ mục tiêu là $9\text{ mg/L}$ và $26\text{ mg/L}$ (Bảng S11).
- Tích lũy sắt và phản ứng tăng tiết EPSp: Khi liều lượng Fe tăng từ $9$ lên $26\text{ mg/L}$:
  - Hàm lượng sắt liên kết trong bùn tăng từ $45\text{ mg/g-MLVSS}$ lên $101\text{ mg/g-MLVSS}$.
  - Nồng độ $\text{EPSp}$ trong bùn tăng tương ứng từ $47.96\text{ mg/g-MLVSS}$ lên $62.30\text{ mg/g-MLVSS}$.
- Cơ chế nén chặt và bám dính bề mặt màng: Các phân tử protein chứa nhiều chuỗi bên kỵ nước. Sự gia tăng nồng độ $\text{EPSp}$ kết hợp với cầu nối cation đa hóa trị $\text{Fe}^{3+}$ thúc đẩy liên kết liên phân tử, làm tăng tính kỵ nước cục bộ và cường độ kết tụ bông bùn. Hiện tượng này gia tăng độ bám dính lên bề mặt màng và nén đặc lớp bánh bùn [46, 55].
- Bằng chứng đo độ nhớt bùn: Hỗn dịch bùn trạm đích có độ nhớt biểu kiến lên tới $50.03\text{ mPa}\cdot\text{s}$ và độ nhớt riêng đạt $9.46\text{ mPa}\cdot\text{s/(g/L)}$ (Hình 7(d)). Các giá trị này chứng minh tính nén chặt cao của ma trận bùn giàu Fe-EPSp.

#### 3.3.4.3 Bằng chứng thực nghiệm từ quy trình rửa hóa chất tại chỗ (Two-step CIP)
- Giao thức rửa hóa chất hai giai đoạn: Màng lọc trước khi rửa được tháo cạn và tráng sạch bằng nước sau lọc. Quy trình CIP gồm 2 bước liên tiếp: rửa axit citric ($\text{CA}$, $15\text{ g/L}$, $\text{pH} = 2.5$) sau đó rửa natri hypoclorit ($\text{NaClO}$, $1\text{ g/L}$, $\text{pH} = 10$).
- Giai đoạn hòa tan sắt bằng axit citric: Trong dung dịch rửa axit citric, nồng độ sắt tổng số tăng đột biến từ $0.62\text{ mg/L}$ lên $43.02\text{ mg/L}$ (Hình 7(e)). Kết quả này chứng minh sự tồn tại của một lượng lớn các hợp chất chứa sắt kết tủa trong lớp bám bẩn.
- Giai đoạn oxy hóa chất hữu cơ bằng NaClO: Trong dung dịch rửa kiềm oxy hóa $\text{NaClO}$, nồng độ tổng cacbon hữu cơ ($\text{TOC}$) tăng vọt từ $5.19\text{ mg/L}$ lên $43.22\text{ mg/L}$ (Hình 7(f)). Đồng thời nồng độ sắt tổng số tiếp tục tăng từ $1.85\text{ mg/L}$ lên $11.16\text{ mg/L}$.
- Bản chất lớp bám bẩn chính: Sự giải phóng đồng thời của hợp chất hữu cơ bị oxy hóa và các ion kim loại sắt, cùng với sự chênh lệch lớn giữa COD hòa tan ($\text{SCOD} = 93\text{ mg/L}$) và COD tổng số ($\text{TCOD} = 271\text{ mg/L}$), khẳng định lớp bám bẩn bề mặt màng không hình thành từ chất hữu cơ hòa tan đơn thuần. Lớp tắc nghẽn chủ đạo là một ma trận hữu cơ liên kết bùn hoạt tính kết hợp chặt chẽ với các thành phần vô cơ chứa sắt.

#### 3.3.4.4 Cơ chế suy giảm đóng góp của SMPp do sự xuyên màng không giữ lại
- Xu hướng hạ thấp tỷ trọng của SMPp: Phân tích SHAP cho thấy đóng góp của protein hòa tan ($\text{SMPp}$) giảm dần sau khi mô hình được tinh chỉnh.
- Phổ huỳnh quang của SMP và nước sau lọc: Mặc dù phổ huỳnh quang EEM của dịch SMP trạm đích có tín hiệu protein thơm vùng kích thích thấp (Hình 7(c)), phổ EEM của dòng nước sau lọc (effluent) cũng xuất hiện các dải huỳnh quang mở rộng tương đồng tại tọa độ $\text{Ex/Em} \approx 220\text{--}250 / 300\text{--}460\text{ nm}$ (Hình S12).
- Hiện tượng xuyên màng tự do: Sự trùng lặp quang phổ huỳnh quang chứng minh phần lớn các phân tử protein hòa tan kích thước nhỏ không bị màng lọc giữ lại mà đi xuyên qua các lỗ màng vào nước thành phẩm.
- Nhận thức chuẩn xác của mạng nơ-ron: Vì $\text{SMPp}$ tự do thoát qua màng nên nó không tham gia tích cực vào việc tạo thành lớp bánh bám bẩn bề mặt. Mạng LSTM-FT sau tinh chỉnh đã học được thực tế vật lý này và tự động giảm bớt trọng số quy gán cho $\text{SMPp}$.

#### 3.3.4.5 Bản chất nhận thức của mô hình học chuyển giao qua tinh chỉnh
- Tóm tắt cơ chế ba mũi nhọn:
  1. Bảo lưu tri thức bám bẩn polysaccharide ngoại bào ($\text{EPSc}$) mang tính phổ quát chuyển giao từ trạm nguồn.
  2. Tái hiệu chỉnh để nâng cao độ nhạy với tín hiệu protein ngoại bào ($\text{EPSp}$) do tương tác giàu sắt đặc thù tại trạm đích.
  3. Giảm bớt sự phụ thuộc vào protein hòa tan ($\text{SMPp}$) vì thành phần này đi xuyên qua màng lọc.

---

### 3.3.5 Khả năng thích ứng xuyên kịch bản sang MBR xử lý nước thải công nghiệp (Cross-scenario adaptability to an industrial wastewater MBR)

#### 3.3.5.1 Bối cảnh vận hành khắc nghiệt và đặc tính bùn nước thải công nghiệp
- Quy mô kiểm chứng độc lập: Thử nghiệm thẩm định bổ sung thực hiện trên hệ thống MBR quy mô pilot xử lý nước thải công nghiệp hỗn hợp hóa dầu và dược phẩm.
- Thách thức phân phối khắc nghiệt: Nước thải công nghiệp có thành phần hóa học phức tạp, tải trọng hữu cơ biến động mạnh và động học sinh khối thường xuyên chịu các cú sốc tải vận hành.
- Diễn biến áp suất bất thường: Đồ thị $\text{TMP}$ thể hiện một xu hướng tăng dài hạn kèm theo nhiều đợt dao động đột biến do các sự cố kỹ thuật thực tế (Hình 8(a)).
- So sánh các thông số hóa lý cốt lõi: Nước thải và bùn công nghiệp có các chỉ số $\text{TCOD}$, $\text{SCOD}$, $\text{MLSS}$ và $\text{MLVSS}$ cao hơn vượt trội so với các trạm nguồn sinh hoạt (Hình 8(b)).
- Các đặc trưng bám bẩn tương đồng then chốt:
  - Hàm lượng $\text{EPSc}$ trạm công nghiệp đạt $43.6 \pm 20.2\text{ mg/L}$, nằm sát dải trạm nguồn ($32.3\text{--}43.5\text{ mg/L}$).
  - Hàm lượng $\text{EPSp}$ đạt $256.8 \pm 126.7\text{ mg/L}$, cùng bậc độ lớn với trạm nguồn ($184\text{--}229\text{ mg/L}$).
  - Hàm lượng $\text{SMPc}$ đạt $6.9 \pm 5.0\text{ mg/L}$, nằm hoàn toàn trong dải trạm nguồn ($5.2\text{--}11.5\text{ mg/L}$).
  - Sự giao thoa này là cơ sở vật lý cho phép học chuyển giao thành công qua các kịch bản nước thải khác biệt sâu sắc.

#### 3.3.5.2 Hiệu năng chuyển giao không mẫu và phục hồi vượt bậc sau tinh chỉnh (FT = 40%)
- Giới hạn khi chưa tinh chỉnh ($FT = 0\%$): Mô hình LSTM nguồn chỉ đạt hiệu năng khiêm tốn trên MBR công nghiệp với $R^2 = 0.46$ (Hình 8(c)). Tri thức trạm nguồn chỉ nắm bắt được một phần động học $\text{TMP}$.
- Bước nhảy vọt sau tinh chỉnh tại $FT = 40\%$: Áp dụng quy trình tinh chỉnh theo thời gian thực chuẩn hóa mà không cần thay đổi kiến trúc mô hình giúp phục hồi hiệu năng xuất sắc:
  - Hệ số xác định $R^2$ tăng vọt từ $0.46$ lên $0.89$ (và đạt $0.90$ trên đồ thị phân tán Hình 8(c)).
  - Sai số $\text{MAE}$ giảm mạnh $68.6\%$ so với mức $FT = 0\%$.
  - Sai số $\text{RMSE}$ giảm mạnh $54.7\%$ so với mức $FT = 0\%$.
- Khẳng định tính tương thích thực tế: Khung học chuyển giao có khả năng áp dụng linh hoạt trên nền nước thải công nghiệp mà không đòi hỏi tái cấu trúc thuật toán hay tối ưu hóa siêu tham số phức tạp.

Bảng 4: Hiệu năng chuyển giao mô hình LSTM trên hệ thống MBR nước thải công nghiệp.
| Điều kiện tinh chỉnh | $R^2$ | Biến thiên MAE so với $FT = 0\%$ | Biến thiên RMSE so với $FT = 0\%$ | Đánh giá trạng thái mô hình |
| :--- | :--- | :--- | :--- | :--- |
| **$FT = 0\%$ (Zero-shot)** | $0.46$ | Điểm chuẩn gốc ($0\%$) | Điểm chuẩn gốc ($0\%$) | Nắm bắt được xu thế thô, sai số lớn do sốc tải |
| **$FT = 40\%$ (Sau tinh chỉnh)** | $\mathbf{0.89\text{--}0.90}$ | $\mathbf{-68.6\%}$ (Giảm sâu) | $\mathbf{-54.7\%}$ (Giảm sâu) | Khôi phục dự báo chính xác cao, thích ứng hoàn hảo |

#### 3.3.5.3 Tái hiệu chỉnh cấu trúc SHAP: Sự trỗi dậy của SMPp do sốc tải sinh khối
- Bảo tồn vị trí số 1 của EPSc: Phân tích SHAP sau tinh chỉnh cho thấy $\text{EPSc}$ tiếp tục giữ vị thế đặc trưng quan trọng nhất (Hình 8(d)), tái khẳng định vai trò trụ cột bất biến của polysaccharide.
- Vươn lên vị trí số 2 của protein hòa tan: Khác biệt hoàn toàn với trạm sinh hoạt đích (nơi $\text{EPSp}$ đứng thứ 2), tại MBR công nghiệp, biến $\text{SMPp}$ vươn lên thành đặc trưng quan trọng thứ hai sau tinh chỉnh.
- Cơ chế giải thích nồng độ SMPp tăng vọt: Nồng độ $\text{SMPp}$ trung bình trong MBR công nghiệp đạt tới $27.6 \pm 17.4\text{ mg/L}$, cao gấp đôi so với các trạm nguồn ($10.8\text{--}13.8\text{ mg/L}$).
- Ảnh hưởng của sốc tải độc tính và suy thoái tế bào: Trong nước thải công nghiệp hóa dược, các đợt sốc tải hóa chất gây độc tính ức chế vi sinh vật, làm giảm mật độ bùn $\text{MLSS}$ và $\text{MLVSS}$ [56].
- Quá trình phân hủy tế bào sinh khối giải phóng ồ ạt các protein hòa tan ($\text{SMPp}$) vào dịch hỗn dịch.
- Hình thành bám bẩn từ keo protein công nghiệp: Dịch SMP trong trạm công nghiệp bị chi phối bởi protein thay vì carbohydrate. Khối lượng lớn protein hòa tan tích tụ dưới điều kiện biến động vận hành đóng vai trò là tác nhân chính gây tắc nghẽn lỗ màng và kết tụ lớp bám bẩn. Mô hình sau tinh chỉnh đã thích ứng chính xác với tín hiệu $\text{SMPp}$ trỗi dậy này.

#### 3.3.5.4 Tính phổ quát và linh hoạt của khung học chuyển giao xuyên kịch bản
- Tính thống nhất của cơ chế bám bẩn xuyên hệ thống: Khung học chuyển giao thành công giữa các kịch bản nước thải không phải vì cơ chế bám bẩn hoàn toàn đồng nhất, mà vì mô hình tách biệt được hai nhóm tri thức:
  - **Tri thức bất biến chung (Transferable Core)**: Quy luật bám bẩn nền do $\text{EPSc}$ chi phối được bảo toàn qua mọi hệ thống MBR.
  - **Tri thức thích ứng cục bộ (Plant-Specific Adaptation)**: Quá trình tinh chỉnh tái định chuẩn linh hoạt cấu trúc quy gán hướng về tác nhân xung yếu nhất của từng trạm:
    - Trạm sinh hoạt giàu sắt: Tái định chuẩn nhạy bén với $\text{EPSp}$ (tương tác keo tụ kết dính Fe-Protein).
    - Trạm công nghiệp chịu sốc tải: Tái định chuẩn nhạy bén với $\text{SMPp}$ (suy thoái sinh khối giải phóng protein hòa tan).
- Ý nghĩa công nghệ: Nghiên cứu cung cấp giải pháp dự báo bám bẩn màng đáng tin cậy cho các trạm MBR mới vận hành hoặc trạm công nghiệp thiếu dữ liệu lịch sử dài hạn, giải quyết rào cản khan hiếm dữ liệu trong công nghệ màng sinh học.
