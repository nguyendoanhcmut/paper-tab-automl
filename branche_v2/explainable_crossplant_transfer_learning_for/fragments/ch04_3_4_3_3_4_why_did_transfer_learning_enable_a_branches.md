#### 3.3.4. Why did transfer learning enable accurate membrane fouling prediction in the target plant?

- Do SHAP và LOFO chỉ xác định các biến có mức độ liên quan tới mô hình ($model-relevant\ variables$) thay vì cơ chế nhân quả ($causal\ mechanisms$), sự thay đổi phân bổ trọng số ($attribution\ changes$) được diễn giải đối chiếu với các bằng chứng hóa lý độc lập ($independent\ physicochemical\ evidence$) từ nhà máy mục tiêu:
  - Việc đối chiếu độc lập giúp làm sáng tỏ bản chất vật lý của các tín hiệu dự báo thu nhận được qua quá trình học chuyển giao.

- Bằng chứng hóa lý độc lập xác nhận mô hình phân bổ đặc trưng lấy EPS làm trung tâm và phản ánh ma trận bùn gắn kết với sắt tại nhà máy mục tiêu:
  - **Hình 7.** Bằng chứng hóa lý củng cố phân bổ đặc trưng xoay quanh EPS
    - <img src="assets/fig_07_p10.jpeg" alt="Hình 7" />
    - **Hình này chứng minh điều gì**
      - Sự tích lũy sắt gắn liền với bùn cản trở tách nước, tăng độ nhớt và tạo lớp bánh tắc nghẽn hữu cơ chứa sắt khó rửa trôi.
    - **Từ đâu mà thấy được**
      - Tính chất bùn (a, d): trục $y$ ghi $\text{CST}$ ($0\text{--}80\text{ s}$), $\text{CST}$ riêng ($0\text{--}8\text{ s/(g/L)}$), độ nhớt ($0\text{--}60\text{ mPa}\cdot\text{s}$), độ nhớt riêng ($0\text{--}12\text{ mPa}\cdot\text{s/(g/L)}$).
      - Phổ huỳnh quang (b, c): trục tung $\text{Ex}$ ($200\text{--}550\text{ nm}$), trục hoành $\text{Em}$ ($250\text{--}550\text{ nm}$); vùng protein thơm của EPS đạt cường độ huỳnh quang cao nhất.
      - Rửa CIP (e, f): trục tung nồng độ $\text{Fe}$ ($0\text{--}50\text{ mg/L}$) và $\text{TOC}$ ($0\text{--}50\text{ mg/L}$); nồng độ tăng mạnh ở dung dịch sau rửa axit và sau rửa kiềm.

- Tại $\text{FT} = 0$, mô hình phân bổ đặc trưng vẫn bị chi phối bởi $\text{EPS}_c$ và mô hình giữ lại hiệu năng dự báo ở mức trung bình ($R^2 = 0.41$):
  - Cấu trúc dự báo lấy $\text{EPS}_c$ làm trung tâm do mô hình cơ sở học được vẫn có khả năng áp dụng một phần ($partially\ applicable$) cho nhà máy mục tiêu.
  - Nồng độ $\text{EPS}_c$ tại nhà máy mục tiêu tương đối cao ($49.6\text{ mg/L}$), khẳng định hiện tượng tắc nghẽn liên quan đến polysaccharide tiếp tục đóng vai trò quan trọng.
  - Hàm lượng polysaccharide gia tăng nâng cao khả năng giữ nước ($water\ retention$) và làm giảm khả năng tách nước của bùn ($sludge\ dewaterability$), thúc đẩy sự hình thành lớp bánh bùn có độ hydrat hóa cao ($highly\ hydrated$), dễ bị nén ($compressible$) và có trở lực cao ($high-resistance\ fouling\ layer$).
  - Diễn giải này nhất quán với giá trị thời gian hút mao dẫn tương đối cao ($\text{CST} = 49.45\text{ s}$) và $\text{CST}$ riêng đạt $4.36\text{ s/(g/L)}$ ghi nhận tại nhà máy mục tiêu (Fig. 7(a)).
  - $\text{EPS}_c$ đại diện cho đặc tính ma trận tắc nghẽn màng dùng chung giữa các nhà máy ($shared\ membrane-fouling\ matrix\ characteristic\ across\ plants$), duy trì lượng thông tin ổn định trong dự báo chuyển giao.

- Khi tỷ lệ tinh chỉnh tăng lên $\text{FT} = 40\%$, hiệu năng mô hình cải thiện đạt $R^2 = 0.89$ và $\text{EPS}_p$ vươn lên thành đặc trưng quan trọng thứ hai:
  - Quá trình tinh chỉnh gia tăng độ nhạy của mô hình đối với các đặc tính EPS liên quan đến protein tại nhà máy mục tiêu.
  - Phổ huỳnh quang EEM của EPS tại nhà máy mục tiêu xuất hiện đỉnh nổi trội tương tự protein thơm ($dominant\ aromatic\ protein-like\ peak$) (Fig. 7(b)), đồng nhất với dấu ấn EPS liên quan đến protein ở các nhà máy nguồn.
  - Sự gia tăng tầm quan trọng của $\text{EPS}_p$ (protein thơm) được giả thuyết là do dòng vào giàu sắt ($\text{Fe}-enriched\ influent$) trong hệ thống MBR $[54]$.
  - Hai giai đoạn châm $\text{Fe}$ thượng nguồn vào bể trộn dòng vào trước tiền xử lý với liều lượng mục tiêu $9\text{ mg/L}$ và $26\text{ mg/L}$ (Table S11) xác nhận quá trình tích lũy $\text{Fe}$ và đáp ứng thành phần EPS.
  - Khi liều lượng $\text{Fe}$ tăng, hàm lượng $\text{Fe}$ liên kết với bùn tăng từ $45$ lên $101\text{ mg/g-MLVSS}$, đồng thời $\text{EPS}_p$ tăng từ $47.96$ lên $62.30\text{ mg/g-MLVSS}$.
  - Điều kiện giàu $\text{Fe}$ tạo nên thành phần EPS giàu protein hơn, lý giải sự gia tăng mức độ phân bổ trọng số của $\text{EPS}_p$ sau khi tinh chỉnh.
  - Hàm lượng protein trong EPS cao hơn làm gia tăng tính kỵ nước ($stronger\ hydrophobicity$) và khả năng kết tụ bông bùn ($greater\ floc\ aggregation$), tạo điều kiện thuận lợi cho sự bám dính bề mặt màng và làm cô đặc lớp bánh bùn ($cake-layer\ densification$) $[46,55]$.
  - Cơ chế này phù hợp với độ nhớt bùn tương đối cao ($50.03\text{ mPa}\cdot\text{s}$) và độ nhớt riêng đạt $9.46\text{ mPa}\cdot\text{s/(g/L)}$ tại nhà máy mục tiêu (Fig. 7(d)).
  - Sự gia tăng phân bổ SHAP của $\text{EPS}_p$ phản ánh quá trình tinh chỉnh đã tái hiệu chuẩn mô hình hướng về các đặc tính EPS liên quan đến protein vốn biểu hiện rõ nét dưới điều kiện giàu sắt của nhà máy mục tiêu.

- Kết quả quy trình làm sạch tại chỗ ($\text{CIP}$) hai bước xác nhận mối liên hệ giữa đáp ứng EPS liên quan đến sắt và thành phần lớp tắc nghẽn tích tụ:
  - Trước khi thực hiện CIP, cụm màng được tháo cạn và rửa sạch bằng nước thấm qua ($filtrate$).
  - Quy trình CIP hai bước gồm rửa bằng axit citric ($15\text{ g/L}$, $\text{pH} = 2.5$) tiếp theo là rửa bằng natri hypoclorit ($1\text{ g/L}$, $\text{pH} = 10$), với các mẫu thu thập ngay trước và sau mỗi bước rửa (ký hiệu tương ứng là B-CA, A-CA, B-NaClO, A-NaClO).
  - Trong giai đoạn rửa bằng axit citric (CA), nồng độ tổng $\text{Fe}$ tăng mạnh từ $0.62$ lên $43.02\text{ mg/L}$ (Fig. 7(e)), chỉ ra sự giải phóng lượng lớn các hợp phần chứa sắt khỏi lớp tắc nghẽn.
  - Trong giai đoạn rửa bằng $\text{NaClO}$ tiếp theo, nồng độ $\text{TOC}$ tăng từ $5.19$ lên $43.22\text{ mg/L}$ (Fig. 7(f)), đồng thời tổng $\text{Fe}$ cũng tăng từ $1.85$ lên $11.16\text{ mg/L}$, phản ánh sự giải phóng của chất hữu cơ có thể oxy hóa cùng các thành phần chứa sắt.
  - Nồng độ $\text{SCOD}$ thấp hơn đáng kể so với $\text{TCOD}$ tại nhà máy mục tiêu ($93$ so với $271\text{ mg/L}$), khẳng định lớp tắc nghẽn chủ đạo không do các chất hữu cơ hòa tan đơn thuần tạo thành mà liên kết chặt chẽ với ma trận hữu cơ gắn với bùn chứa các hợp phần liên quan đến sắt.

- Sự suy giảm phân bổ trọng số của $\text{SMP}_p$ sau tinh chỉnh phản ánh việc mô hình giảm bớt nhấn mạnh vào thông tin protein hòa tan:
  - Phổ EEM của SMP tại nhà máy mục tiêu xuất hiện đặc trưng protein thơm kích thích thấp rõ rệt ($pronounced\ low-excitation\ aromatic\ protein-like\ feature$) (Fig. 7(c)).
  - Phổ EEM của dòng nước đầu ra ($effluent\ EEM$) biểu hiện các vùng huỳnh quang rộng hơn với $\text{Ex/Em} \approx 220\text{–}250 / 300\text{–}460\text{ nm}$ chồng lấn một phần với vùng tương tự protein kích thích thấp trong SMP (Fig. S12).
  - Vùng phổ chồng lấn này chỉ ra một phần tín hiệu chất hữu cơ hòa tan dạng protein kích thích thấp không bị hệ thống màng giữ lại hoàn toàn.
  - Sự sụt giảm phân bổ trọng số của $\text{SMP}_p$ sau tinh chỉnh không loại trừ đóng góp của nó vào hiện tượng tắc nghẽn, nhưng chứng minh $\text{SMP}_p$ ít liên kết với lớp chất tắc nghẽn chủ đạo tích tụ trên màng tại nhà máy mục tiêu so với các biến liên quan đến EPS.

- Quá trình tinh chỉnh mô hình LSTM đạt được cơ chế thích ứng chọn lọc đối với các đặc tính tắc nghẽn màng:
  - Tinh chỉnh bảo toàn thông tin tắc nghẽn có khả năng chuyển giao liên quan đến $\text{EPS}_c$ tại nhà máy MBR mục tiêu.
  - Mô hình tái hiệu chuẩn tín hiệu đặc thù theo nhà máy liên quan đến $\text{EPS}_p$.
  - Mô hình giảm nhấn mạnh vào $\text{SMP}_p$ do thành phần này ít đại diện cho lớp tắc nghẽn chủ đạo bị giữ lại trên bề mặt màng.
