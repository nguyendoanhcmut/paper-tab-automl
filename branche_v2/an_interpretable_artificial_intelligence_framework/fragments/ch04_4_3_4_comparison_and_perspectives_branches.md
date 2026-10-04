### 3.4. Comparison and perspectives

#### 3.4.1. Predictive performance

- **Đặc điểm trọng tâm của các nghiên cứu tiền nhiệm trong y văn**:
  - Đa số các công trình trước đây tập trung vào xử lý nước thải đô thị hoặc nước thải sinh hoạt (municipal or domestic wastewater treatment), phần lớn tiến hành ở quy mô phòng thí nghiệm hoặc quy mô thử nghiệm (pilot or lab scales).
  - Các nghiên cứu trước thường chỉ cung cấp dự đoán đơn mục tiêu (single-target predictions), ví dụ như áp suất xuyên màng ($\text{TMP}$ - transmembrane pressure) hoặc các chỉ số tắc nghẽn màng (fouling indicators) như độ thấm (permeability) và lưu lượng dòng thấm nước (water flux) (Bảng S8).
  - Nghiên cứu [68] sử dụng mạng perceptron đa tầng (MLP - multilayer perceptron) và mạng bộ nhớ ngắn-dài (LSTM - long short-term memory) để dự đoán $\text{TMP}$ trong hệ thống màng phản ứng sinh học kỵ khí quy mô thử nghiệm lớn (large pilot-scale AnMBR) xử lý nước thải đô thị, đạt hệ số xác định $R^2 > 0.91$.
  - Nghiên cứu [69] sử dụng rừng ngẫu nhiên (random forest) để dự đoán hành vi tắc nghẽn màng trong $\text{AnMBR}$, đạt $R^2 = 0.906$.
  - Nghiên cứu [70] áp dụng hệ thống suy luận mờ thích ứng nơ-ron (ANFIS - adaptive neuro-fuzzy inference systems) để dự đoán lưu lượng dòng thấm trong $\text{MBR}$ thẩm thấu (osmotic MBRs), ghi nhận $R^2$ dao động trong khoảng từ $0.9755$ đến $0.9861$.
- **Hiệu suất dự đoán ba mục tiêu đồng thời tại quy mô công nghiệp thực tế của nghiên cứu hiện tại**:
  - Nghiên cứu áp dụng thuật toán hồi quy cây tăng cường ngẫu nhiên (Extra Trees regressor) ở quy mô thực tế đầy đủ (full scale) tại nhà máy xử lý nước thải sản xuất chất bán dẫn (semiconductor wastewater plant), nơi có biên độ dao động tải trọng lớn và các tiêu chuẩn xả thải nghiêm ngặt.
  - Dự đoán đồng thời ba biến đầu ra phụ thuộc lẫn nhau (interdependent outputs): $\text{TMP}$, lưu lượng dòng thấm (permeate flow), và mực nước bể màng (water level).
  - Dưới cơ chế chia tập ngẫu nhiên (random partition) tương đương với thiết kế kiểm định của các nghiên cứu tham chiếu:
    - $\text{TMP}$ đạt $R^2 = 0.988$.
    - Permeate flow đạt $R^2 = 0.933$.
    - Water level đạt $R^2 = 0.908$.
  - Dưới cơ chế chia tập phân khối $24\text{ giờ}$ ($24\text{-h}$ blocked partition) nhằm loại bỏ tương quan chuỗi giữa các điểm dữ liệu lân cận về mặt thời gian:
    - $\text{TMP}$ đạt $R^2 = 0.830$.
    - Permeate flow đạt $R^2 = 0.788$.
    - Water level đạt $R^2 = 0.564$.
- **Ý nghĩa phương pháp luận của việc đối sánh hiệu suất dự đoán**:
  - Cả hai cơ chế phân chia tập dữ liệu đều được công bố vì việc so sánh với các độ chính xác đơn mục tiêu trong y văn chỉ có ý nghĩa khi dựa trên cùng một nguyên tắc phân chia dữ liệu tương đồng, và các nghiên cứu được trích dẫn đều dùng phép chia ngẫu nhiên trên các chuỗi dữ liệu có tự tương quan tương tự.
  - Mục tiêu của công trình không nhằm tuyên bố mức độ chính xác cao nhất từng được công bố, mà nhằm chứng minh một mô hình học tập hợp đơn lẻ (single ensemble learner) đạt được độ chính xác cạnh tranh trên ba mục tiêu ràng buộc lẫn nhau tại quy mô công nghiệp đầy đủ.
  - Mô hình không chịu chi phí tính toán lớn (computational overhead) như các kiến trúc mạng hồi quy lặp (recurrent architectures).
  - Cấu trúc bài toán đa mục tiêu phản ánh đúng thực tế vận hành: động học thủy lực (hydraulic dynamics) và quá trình tắc nghẽn màng không thể được tối ưu hóa một cách độc lập rời rạc.

#### 3.4.2. Optimization approach

- **Khoảng trống về khả năng giải thích (interpretability) trong y văn so sánh**:
  - Khoảng trống lớn nhất trong các công trình nghiên cứu so sánh không nằm ở độ chính xác dự đoán mà ở tính khả giải (interpretability), khía cạnh mà hầu hết các nghiên cứu đối chuẩn không báo cáo.
  - Khung phương pháp kết hợp ước lượng mật độ nhân (KDE - kernel density estimation), phân tích vùng khả thi (feasible-region analysis), biểu đồ bầy ong SHAP (SHAP beeswarm), phân tích phụ thuộc SHAP (SHAP dependence analysis) và hệ số tương quan Pearson.
  - Khung phương pháp được áp dụng đồng thời trong hai ngữ cảnh phân tích: toàn bộ hồ sơ dữ liệu vận hành (Mục 3.2) và vùng vận hành khả thi (feasible operating region, Mục 3.3).
  - Phân tích hai ngữ cảnh (dual-context analysis) là một đóng góp mang tính phương pháp luận, vì thứ hạng độ quan trọng của nhiều biến số bị thay đổi đáng kể khi phân tích giới hạn trong phạm vi chế độ khả thi (viable regime).
  - Sự dịch chuyển thứ hạng mang lại các hàm ý trực tiếp cho điều khiển thời gian thực mà phân tích đơn ngữ cảnh không thể bộc lộ.
  - Mức tăng $87\%$ về độ quan trọng của tỷ số thức ăn trên vi sinh vật ($\text{F/M}$ - food-to-microorganism ratio) đối với mực nước bể màng trong vùng khả thi là minh chứng rõ nhất, xác định một đòn bẩy điều khiển gần thời gian thực (near-real-time control lever) mà phân tích SHAP trên toàn bộ tập dữ liệu đã che giấu phía sau các biến biến thiên chậm chiếm ưu thế (dominant slow variables).
- **Phân biệt bản chất thuật ngữ "tối ưu hóa" (optimization) giữa nghiên cứu và y văn**:
  - Điểm khác biệt rõ nét nhất nằm ở định nghĩa và phạm vi ứng dụng của thuật ngữ "tối ưu hóa".
  - Trong đa số các nghiên cứu so sánh có báo cáo hoạt động tối ưu hóa, thuật ngữ này chỉ việc tối ưu hóa mô hình (model optimization, Bảng S8), bao gồm tinh chỉnh siêu tham số (hyperparameter tuning), tìm kiếm kiến trúc mạng (architecture search), hoặc lựa chọn chiến lược huấn luyện (training strategy selection).
  - Chỉ duy nhất công trình [71] áp dụng tối ưu hóa cho các điều kiện vận hành (operating conditions) thay vì tham số mô hình, sử dụng thuật toán di truyền (GA - genetic algorithm) để xác định tổ hợp đầu vào nhằm cực tiểu hóa một mục tiêu tắc nghẽn đơn lẻ.
- **Tối ưu hóa điều kiện vận hành đa mục tiêu trên đa tạp khả thi (manifold-constrained feasible input space)**:
  - Đây là nghiên cứu đầu tiên trong y văn học máy ứng dụng cho $\text{MBR}$ thực hiện tối ưu hóa điều kiện vận hành đa mục tiêu trong không gian đầu vào khả thi chịu ràng buộc đa tạp.
  - Phương pháp thỏa mãn đồng thời ba ràng buộc hiệu suất màng và lập bản đồ cấu trúc liên kết của $207{,}238$ trạng thái đạt được yêu cầu này.
  - Khác biệt về mặt bản chất so với phương pháp tìm kiếm bằng thuật toán di truyền đơn mục tiêu: thay vì trả về một điểm tối ưu đơn lẻ, phân tích tạo ra một mặt xác suất có điều kiện (conditional probability surface) trên toàn bộ không gian vận hành có thể đạt tới.
  - Cho phép xác định các vùng mà hệ thống đạt độ bền vững cao nhất trước các nhiễu loạn thông thường (resilient to routine perturbation), phân biệt rõ với ranh giới khả thi thuần túy về mặt kỹ thuật.
  - Đóng góp luận điểm phương pháp luận có thể chuyển giao rộng rãi: vùng khả thi cần được lấy mẫu trên đa tạp vận hành liên kết (joint operating manifold) thay vì lấy mẫu độc lập theo các dải biên (marginal ranges), và các khuyến nghị vận hành phải được phân cấp theo tỷ lệ đạt có điều kiện (conditional attainment rate) thay vì theo mật độ các điểm khả thi (density of feasible points).
- **Đóng góp thực tiễn từ sự phân tách giữa vùng khả thi và vùng lõi đạt chuẩn cao (high-attainment core)**:
  - Sự phân biệt giữa biên khả thi và vùng lõi đạt chuẩn mang ý nghĩa thực tiễn quan trọng:
    - Đối với thời gian lưu bùn ($\text{SRT}$ - solids retention time): bao hình khả thi mở rộng vượt mức $95\text{ ngày}$, trong khi tỷ lệ đạt mục tiêu đo đạc thực tế khi $\text{SRT} > 87\text{ ngày}$ giảm xuống dưới $20\%$.
    - Đối với thời gian lưu nước thủy lực ($\text{HRT}$ - hydraulic retention time): bao hình khả thi đạt tới $7.65\text{ giờ}$, trong khi tỷ lệ đạt mục tiêu khi $\text{HRT} > 7.95\text{ giờ}$ bằng $0\%$.
    - Đối với tỷ số $\text{F/M}$: bao hình khả thi mở rộng tới $0.037\text{ ngày}^{-1}$, trong khi tỷ lệ đạt mục tiêu khi $\text{F/M} > 0.037\text{ ngày}^{-1}$ chỉ đạt $15\%$.
  - Người vận hành nếu chỉ dựa vào ranh giới khả thi từ phân tích thỏa mãn ràng buộc thông thường sẽ kết luận rằng các dải cận trên này là chấp nhận được, trong khi thực tế chúng tiềm ẩn xác suất cao vi phạm một hoặc nhiều mục tiêu hiệu suất.
  - Các mục tiêu vận hành được phân cấp theo tỷ lệ trong Bảng 4, xây dựng từ $207{,}238$ trạng thái khả thi được đánh giá và đối chiếu kiểm chứng qua $4593\text{ giờ}$ vận hành thực tế, cung cấp bằng chứng thực nghiệm vững chắc mà ranh giới khả thi đơn thuần không thể cung cấp.

#### 3.4.3. Perspectives and future strategies

- **Các đóng góp cấu trúc và ba lĩnh vực thúc đẩy thực tiễn vận hành**:
  - Năm đóng góp cấu trúc chính của công trình gồm:
    1. Triển khai ứng dụng quy mô thực tế tại nhà máy xử lý nước thải công nghiệp bán dẫn.
    2. Dự đoán đồng thời ba biến đầu ra phụ thuộc lẫn nhau.
    3. Đánh giá đối chuẩn 16 thuật toán thuộc sáu họ mô hình dưới bốn thiết kế kiểm định.
    4. Phân tích khả giải đa mô hình trong hai ngữ cảnh vận hành.
    5. Tối ưu hóa ràng buộc trên đa tạp được thẩm định bằng tỷ lệ đạt đo đạc thực tế và kiểm chứng trên dữ liệu tương lai ngoài khoảng thời gian (out of time).
  - Thúc đẩy thực tiễn vận hành trong ba lĩnh vực cụ thể:
    - Lĩnh vực 1: Các mô hình huấn luyện trên dữ liệu vận hành lịch sử của một hệ thống $\text{MBR}$ công nghiệp phức tạp có thể hỗ trợ định hướng vận hành mà không cần phân tích bổ sung trong phòng thí nghiệm, với điều kiện mô hình được đánh giá dưới dạng mặt đáp ứng (response surfaces) trên không gian vận hành có thể đạt tới và được thẩm định dựa trên kết quả đo đạc thực tế thay vì chỉ dựa vào năng lực dự báo đơn thuần.
    - Lĩnh vực 2: Phân tích khả giải thực hiện trong vùng khả thi thay vì trên toàn bộ bao hình lịch sử bộc lộ các dịch chuyển quan trọng về độ quan trọng của đặc trưng có ý nghĩa điều khiển, cung cấp khuôn mẫu có thể nhân rộng cho các mô hình quy trình công nghiệp đa đầu ra khác.
    - Lĩnh vực 3: Xây dựng quy trình vận hành được xếp hạng theo bằng chứng (evidence-graded operating protocol), trong đó mỗi khuyến nghị đều đi kèm tỷ lệ đạt mục tiêu đo đạc tường minh và khẳng định rõ khả năng chuyển giao trên khoảng thời gian kiểm chứng giữ lại độc lập.
- **Ba phương thức thẩm định độc lập cho vùng vận hành khuyến nghị**:
  - Vùng vận hành được kiểm chứng độc lập qua ba phương thức:
    - Đối soát với tỷ lệ đạt mục tiêu đo đạc thực tế của nhà máy trên toàn không gian vận hành.
    - Thẩm định trên giai đoạn dữ liệu ba tháng được giữ lại hoàn toàn khỏi quá trình phân tích.
    - Đánh giá trên một đơn nguyên màng lọc song song độc lập (independent parallel membrane train).
  - Cung cấp cơ sở bằng chứng thực nghiệm vững chắc hơn so với phương pháp phân tích chia tập đơn lẻ trên một chu kỳ thời gian đơn nhất.
- **Các ranh giới kỹ thuật và giới hạn của khung phương pháp**:
  - Kết quả kiểm chứng vẫn dựa trên dữ liệu lịch sử chứ chưa phải thử nghiệm đối chứng trực tiếp (controlled trial), do đó một phần mối liên hệ có thể chịu tác động từ các biến nằm ngoài mô hình, rõ nét nhất là tuổi thọ màng (membrane age) và lịch sử rửa màng (cleaning history).
  - Bước kế tiếp cần triển khai là tiến hành thử nghiệm tiến cứu (prospective trial) luân phiên áp dụng chiến lược khuyến nghị và chiến lược hiện hành giữa hai đơn nguyên siêu lọc ($\text{UF}$ - ultrafiltration) song song để chia sẻ chung điều kiện nước thải đầu vào.
  - Ba giới hạn kỹ thuật cụ thể cần lưu ý:
    - Các mô hình được huấn luyện trên một cơ sở duy nhất với cấu hình màng $\text{UF}$ bằng $\text{PVDF}$ đơn lẻ; phương pháp luận có thể chuyển giao nhưng các khoảng giá trị số mang tính đặc thù cho từng địa điểm (site-specific).
    - Khung phương pháp mô tả đa tạp mà nhà máy đã trải qua trong quá khứ và không được thiết kế để ngoại suy sang các chế độ vận hành chưa từng xuất hiện trong dữ liệu; tuổi thọ màng, tần suất rửa màng và độ dẫn điện của nước sau lọc là các biến đầu vào tiềm năng nhất cần bổ sung.
    - Quy gán SHAP chỉ định lượng mối liên kết thống kê trong phân phối dữ liệu huấn luyện chứ không chứng minh mối quan hệ nhân quả vật lý; việc khẳng định các cơ chế vật lý đề xuất đòi hỏi phải thực hiện khám nghiệm màng (membrane autopsy), đo thế zeta (zeta-potential) và phân đoạn chất hữu cơ trong dòng thấm (filtrate organic fractionation).
