## Abstract

- **Tầm quan trọng của dự đoán tắc nghẽn màng và thách thức dữ liệu thưa thớt**: Dự đoán chính xác hiện tượng tắc nghẽn màng ($membrane\ fouling\ prediction$) là yêu cầu thiết yếu cho điều khiển tiến dung ($feedforward\ control$) và vận hành tiêu thụ năng lượng thấp ($low-energy\ operation$) trong các bể phản ứng sinh học màng ($membrane\ bioreactors$ - MBR):
  - Việc phát triển mô hình tin cậy cho các nhà máy bị giới hạn dữ liệu ($data-limited\ plants$) gặp khó khăn do sự thưa thớt của các phép đo ($sparse\ measurements$) về chất polyme ngoại bào ($extracellular\ polymeric\ substances$ - EPS) và sản phẩm vi sinh vật hòa tan ($soluble\ microbial\ products$ - SMP) mang thông tin cơ chế ($mechanistically\ informative$).

- **Khung học chuyển giao liên nhà máy có khả năng giải thích**: Nhóm nghiên cứu thiết lập khung học chuyển giao liên nhà máy có khả năng giải thích ($explainable\ cross-plant\ transfer\ learning\ framework$) để dự đoán áp suất xuyên màng ($transmembrane\ pressure$ - TMP) cho các hệ thống MBR quy mô pilot bị giới hạn dữ liệu:
  - Các mô hình cơ sở ($base\ models$) gồm mạng bộ nhớ ngắn-dài ($Long\ short-term\ memory$ - LSTM) và tăng cường độ dốc cực đại ($extreme\ gradient\ boosting$ - XGBoost) được tiền huấn luyện ($pretrained$) trên ba nhà máy MBR nguồn ($three\ data-richer\ source\ MBRs$) xử lý nước thải sinh hoạt ($domestic\ wastewater$) có dung lượng dữ liệu lớn hơn.
  - Các mô hình cơ sở được tinh chỉnh ($fine-tuned$) bằng tập dữ liệu giới hạn từ một nhà máy mục tiêu xử lý nước thải sinh hoạt ($domestic\ target\ plant$).

- **Hiệu năng tiền huấn luyện trên miền nguồn và các động lực tắc nghẽn chủ đạo**: Các mô hình cơ sở đạt độ chính xác dự đoán TMP trên miền nguồn ($source-domain\ TMP$) với hệ số xác định lần lượt là $R^2 = 0.87$ (với LSTM) và $R^2 = 0.86$ (với XGBoost):
  - Phương pháp giải thích cộng tính SHapley ($SHapley\ Additive\ exPlanations$ - SHAP) xác định carbohydrate trong EPS ($\text{EPS}_c$), protein trong EPS ($\text{EPS}_p$) và protein trong SMP ($\text{SMP}_p$) là các động lực chi phối hiện tượng tắc nghẽn ($dominant\ fouling-related\ drivers$).

- **Giới hạn của chuyển giao trực tiếp và hiệu quả cải thiện qua tinh chỉnh**: Chuyển giao trực tiếp ($direct\ transfer$) mô hình từ nhà máy nguồn sang nhà máy mục tiêu mang lại độ chính xác hạn chế với $R^2 = 0.39\text{–}0.41$:
  - Kết quả này phản ánh rằng các mô hình cơ sở chưa thu nhận đầy đủ hành vi tắc nghẽn đặc thù của nhà máy mục tiêu.
  - Ngược lại, quá trình tinh chỉnh ($fine-tuning$) nâng cao độ chính xác dự đoán; mô hình LSTM sau tinh chỉnh (LSTM-FT) đạt $R^2 = 0.89$ ở tỷ lệ dữ liệu tinh chỉnh $40\%$ ($40\%\ fine-tuning\ ratio$).

- **Cơ chế chuyển dịch đặc trưng do dòng vào giàu sắt**: Phân tích SHAP và loại trừ từng đặc trưng ($leave-one-feature-out$ - LOFO) chỉ ra cơ chế tương tác:
  - $\text{EPS}_c$ duy trì vai trò là tín hiệu tắc nghẽn chuyển giao cốt lõi ($critical\ transferable\ fouling\ signal$).
  - $\text{EPS}_p$ gia tăng mức độ quan trọng sau quá trình tinh chỉnh ($fine-tuning$).
  - Sự chuyển dịch vai trò này phản ánh con đường tắc nghẽn liên quan đến $\text{EPS}_p$ bắt nguồn từ dòng vào giàu sắt ($\text{Fe}-enriched\ influent$) của trạm xử lý.

- **Kiểm chứng độc lập trên hệ thống MBR xử lý nước thải công nghiệp**: Khung làm việc được kiểm chứng trên một MBR quy mô pilot xử lý nước thải công nghiệp ($industrial\ wastewater$):
  - Mô hình LSTM-FT đạt hệ số xác định $R^2 \approx 0.9$ trên hệ thống MBR công nghiệp.
  - Protein trong SMP ($\text{SMP}_p$) xuất hiện dưới vai trò đặc trưng quan trọng ($critical\ feature$) đối với động học tắc nghẽn.

- **Khả năng tổng quát hóa và bảo toàn tri thức cơ chế**: Khung phương pháp bảo toàn thông tin tắc nghẽn chung xoay quanh EPS ($shared\ EPS-centered\ fouling\ information$), đồng thời tái hiệu chuẩn thích ứng các động lực đặc thù theo từng nhà máy ($adaptively\ recalibrating\ plant-specific\ drivers$):
  - Phương pháp cung cấp giải pháp khả thi cho bài toán dự đoán tắc nghẽn màng kết hợp tri thức cơ chế ($mechanism-informed\ fouling\ prediction$) trong các hệ thống MBR hạn chế dữ liệu.
