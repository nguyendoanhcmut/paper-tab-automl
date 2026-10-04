### 3.5. Explainable AI (XAI) for Membrane Fouling Prediction

- Các kỹ thuật Trí tuệ nhân tạo có thể giải thích (Explainable AI - XAI) được áp dụng nhằm nâng cao khả năng diễn giải (interpretability) của mô hình học máy và tìm hiểu mức độ đóng góp của từng đặc trưng riêng lẻ (individual features) vào việc dự đoán tắc nghẽn màng (membrane fouling prediction).
  - Độ quan trọng của đặc trưng (Feature importance) được đánh giá thông qua ba thước đo: độ quan trọng tích hợp sẵn (built-in feature importance), độ quan trọng hoán vị (permutation importance), và các giá trị SHAP (SHAP values), được tổng hợp trong Bảng 10 (Table 10).
  - Hình 6 và Hình 7 trực quan hóa độ quan trọng của đặc trưng dưới nhiều góc nhìn khác nhau, hỗ trợ phân tích đa chiều (comprehensive analysis).

| Đặc trưng (Feature) | Built-In (%) | Permutation (%) | SHAP (%) |
| :--- | :---: | :---: | :---: |
| **F/M** | $12.05\,\%$ | $16.19\,\%$ | $13.23\,\%$ |
| **SV30** | $2.55\,\%$ | $1.39\,\%$ | $3.21\,\%$ |
| **SVI** | $3.40\,\%$ | $2.16\,\%$ | $2.83\,\%$ |
| **MLSS** | $9.22\,\%$ | $12.18\,\%$ | $10.03695\,\%$ |
| **DO** | $4.26\,\%$ | $0.82\,\%$ | $7.06\,\%$ |
| **pH** | $3.92\,\%$ | $2.06\,\%$ | $2.96\,\%$ |
| **Temp.** | $5.18\,\%$ | $3.70\,\%$ | $6.19\,\%$ |
| **COD RM** | $6.79\,\%$ | $1.64\,\%$ | $4.16\,\%$ |
| **F/M_MA5** | $22.65\,\%$ | $33.70\,\%$ | $26.17\,\%$ |
| **SV30_MA5** | $5.30\,\%$ | $3.28\,\%$ | $3.04\,\%$ |
| **SVI_MA5** | $4.47\,\%$ | $1.25\,\%$ | $2.54\,\%$ |
| **MLSS_MA5** | $3.56\,\%$ | $2.37\,\%$ | $3.05\,\%$ |
| **DO_MA5** | $2.93\,\%$ | $1.51\,\%$ | $3.38\,\%$ |
| **pH_MA5** | $9.16\,\%$ | $11.03\,\%$ | $7.19\,\%$ |
| **Temp._MA5** | $4.55\,\%$ | $6.71\,\%$ | $4.95\,\%$ |

#### 3.5.1. Feature Importance Analysis

- Các giá trị độ quan trọng đặc trưng thu được từ mô hình CatBoost (Bảng 10) làm nổi bật vai trò của $F/M\_MA5$ (giá trị trung bình trượt $5\text{ ngày}$ của tỷ lệ $F/M$) với mức đóng góp cao nhất trên cả ba thước đo độ quan trọng:
  - Tỷ lệ đóng góp đạt $22.65\,\%$ theo built-in feature importance.
  - Tỷ lệ đóng góp đạt $33.70\,\%$ theo permutation importance.
  - Tỷ lệ đóng góp đạt $26.17\,\%$ theo giá trị SHAP.
  - Kết quả này khẳng định các dao động ngắn hạn của tỷ lệ $F/M$ giữ vai trò cốt lõi trong hành vi tắc nghẽn màng.
- Các đặc trưng $F/M$, $MLSS$ và $pH\_MA5$ cũng được xác định là các yếu tố dự đoán then chốt (key predictive factors):
  - Sự kết hợp này chỉ ra rằng cả điều kiện vận hành tức thời lẫn các đặc trưng dựa trên chuỗi trung bình trượt đều ảnh hưởng đáng kể đến hiệu năng màng lọc.
- Phương pháp Permutation importance (Hình 6) nhấn mạnh thêm vai trò chi phối của $F/M\_MA5$, cho thấy việc loại bỏ đặc trưng này dẫn đến mức suy giảm hiệu năng mô hình lớn nhất:
  - **Hình 6.** So sánh độ quan trọng đặc trưng bằng built-in và permutation
    - <img src="assets/fig_07_p21_vector.png" alt="Hình 6" />
    - **Hình này chứng minh điều gì**
      - $F/M\_MA5$ chiếm ưu thế chi phối lớn nhất khi hoán vị đặc trưng, theo sau bởi $F/M$, $MLSS$, $pH\_MA5$ và $Temp.$
    - **Từ đâu mà thấy được**
      - Trục Ox: 15 đặc trưng vận hành; Trục Oy: Độ quan trọng tương đối (`Relative Importance (%)`), dải giá trị $0\text{--}40\,\%$.
      - Cột Permutation (màu đỏ) của $F/M\_MA5$ đạt đỉnh cao nhất (> 40 %), trong khi cột Built-in (màu xanh lam) đạt xấp xỉ $25\,\%$.
  - Các đặc trưng đáng chú ý khác bao gồm $MLSS$, $pH\_MA5$ và nhiệt độ ($Temp.$), thể hiện tầm ảnh hưởng rõ rệt đến động học tắc nghẽn.

#### 3.5.2. SHAP Analysis

- Đồ thị tóm tắt SHAP (SHAP summary plot, Hình 7) cung cấp thông tin chuyên sâu về mức độ đóng góp của các đặc trưng bằng cách minh họa ảnh hưởng của từng giá trị đặc trưng riêng lẻ đến kết quả đầu ra của mô hình:
  - Các giá trị $F/M\_MA5$ cao hơn (biểu thị bằng màu đỏ) đóng góp dương vào dự đoán mức độ nghiêm trọng của hiện tượng nghẹt màng (membrane fouling severity), trong khi các giá trị thấp hơn (biểu thị bằng màu xanh lam) mang lại tác động ngược lại.
  - Xu hướng này cũng được quan sát tương tự đối với $F/M$ và $MLSS$, củng cố vai trò trọng yếu của nồng độ sinh khối (biomass concentration) và tải trọng hữu cơ (organic loading) trong tiến trình tắc nghẽn màng.
  - **Hình 7.** Biểu đồ tóm tắt SHAP minh họa tác động của từng đặc trưng
    - <img src="assets/fig_08_p22.png" alt="Hình 7" />
    - **Hình này chứng minh điều gì**
      - Giá trị cao của $F/M\_MA5$, $F/M$ và $MLSS$ làm tăng mức độ nghẹt màng; giá trị $pH\_MA5$ thấp làm gia tăng rủi ro tắc nghẽn.
    - **Từ đâu mà thấy được**
      - Trục Ox: Giá trị SHAP (`SHAP value`), dải $-0.006\text{--}0.010$, đường chuẩn trung hòa tại $0.000$; Trục Oy: 15 đặc trưng xếp theo tầm quan trọng giảm dần.
      - Thang màu bên phải: từ xanh lam (`Low`) đến đỏ (`High`); các điểm đỏ của $F/M\_MA5$ phân bố lệch sang phía dương (lên tới $> 0.010$), điểm xanh lệch sang phía âm.
- Các kỹ thuật XAI khám phá những hiểu biết mang tính bản chất về cơ chế tắc nghẽn, nhận diện tỷ lệ $F/M$ và $MLSS$ là các yếu tố chi phối, phù hợp với các nghiên cứu tắc nghẽn truyền thống [7,45].
  - Khác với các mô hình thuần túy thực nghiệm (purely empirical models) [40], khung phương pháp đề xuất cung cấp đồng thời độ chính xác cao ($R^2 = 0.8374$) và khả năng diễn giải, hỗ trợ người vận hành ưu tiên các thông số có thể chủ động can thiệp như kiểm soát tỷ lệ $F/M$.
- Các giá trị SHAP đối với $pH\_MA5$ và nhiệt độ ($Temp.$) thể hiện mối liên hệ rõ rệt với cơ chế màng sinh học:
  - Giá trị $pH$ thấp hơn có xu hướng làm gia tăng rủi ro tắc nghẽn màng, nhất quán với các nghiên cứu trước đây về hoạt tính vi sinh và quá trình hình thành màng sinh học (biofilm formation) [7].
  - Phân tích XAI kiểm chứng định lượng tỷ lệ $F/M$ và $MLSS$ là các yếu tố chi phối (đóng góp $> 25\,\%$ vào các kết quả dự đoán), củng cố các mô hình cơ chế trước đó [1] từng nhận diện hai thông số này là tác nhân chủ chốt điều khiển độ nhớt của bùn (sludge viscosity) và sự tạo thành lớp bánh bùn (cake layer formation).
  - Nhiệt độ cao hơn tương quan với sự gia tăng độ ổn định của thông lượng (flux stability), cho thấy điều kiện nhiệt tác động trực tiếp đến hiệu năng lọc (filtration performance).

#### 3.5.3. Implications for MBR Optimization

- Sự tích hợp các kỹ thuật XAI chứng minh các đặc trưng phụ thuộc thời gian (chuỗi trung bình trượt) tăng cường năng lực dự đoán của mô hình, đặc biệt đối với các biến động ngắn hạn của các chỉ số tắc nghẽn màng:
  - Việc đưa các mối quan hệ phụ thuộc thời gian (temporal dependencies) vào hệ thống giám sát thời gian thực có thể nâng cao độ chính xác dự đoán và hiệu quả ra quyết định vận hành.
- Việc nhận diện $F/M\_MA5$ và $MLSS$ là các biến số then chốt định hướng chiến lược kiểm soát quy trình cần tập trung tối ưu hóa các thông số này để giảm thiểu rủi ro nghẹt màng.
- Mô hình CatBoost được xác định là giải pháp phù hợp nhất cho phân tích dựa trên AI về các yếu tố tắc nghẽn màng và dự đoán thông lượng riêng ($Spec.\ Flux$):
  - Hiệu năng dự đoán của CatBoost được tăng cường rõ rệt khi kết hợp với các kỹ thuật nâng cao như chuẩn hóa thang đo mạnh (robust scaling) và trung bình trượt (moving average).
  - Các kỹ thuật này được kỳ vọng mở rộng khả năng áp dụng mô hình CatBoost trên nhiều kịch bản vận hành MBR thực tế.
  - Việc tích hợp các kỹ thuật tiền xử lý và kỹ thuật đặc trưng này cũng được kỳ vọng cải thiện hiệu năng cho các mô hình phân tích và dự đoán AI khác.
  - Tính phổ quát (universality) và khả năng mở rộng (scalability) của các mô hình dự đoán tắc nghẽn MBR được cải thiện đáng kể khi ứng dụng kỹ thuật đặc trưng phù hợp, chuẩn hóa robust scaling và trung bình trượt điều chỉnh theo dữ liệu thực địa thực tế.
- Kết quả nghiên cứu khẳng định mô hình CatBoost kết hợp các phương pháp luận XAI cung cấp phương pháp tiếp cận tin cậy và có khả năng diễn giải cho bài toán dự đoán tắc nghẽn màng trong hệ thống MBR:
  - Thông qua việc khai thác độ quan trọng của đặc trưng, các kỹ sư vận hành có thể tinh chỉnh chiến lược kiểm soát, tối ưu hóa việc phân bổ cảm biến (sensor deployments) và gia tăng tính bền vững trong xử lý nước thải bằng công nghệ màng.
