### NSGA-II optimization

* **Thiết lập và nguyên lý bài toán tối ưu hóa đa mục tiêu bằng giải thuật di truyền sắp xếp không bị chi phối II (Non-dominated Sorting Genetic Algorithm II - NSGA-II)**:
  * **Mục tiêu tối ưu hóa đa biến (Multi-objective optimization framework)**: Giải quyết mối quan hệ đánh đổi phức tạp giữa các mục tiêu xung đột nhau (conflicting objectives) nhằm tối ưu hóa đồng thời hiệu quả loại bỏ các chất dinh dưỡng gồm nitơ amoniac (ammonia nitrogen - $\text{NH}_4^+$-$\text{N}$) và phosphat (phosphate - $\text{PO}_4^{3-}$) trong bể phản ứng sinh học màng vi tảo (microalgae membrane bioreactor - MBR).
  * **Xung đột giữa các mục tiêu công nghệ (Ammonia removal vs. Phosphate removal conflict)**:
    * Quá trình loại bỏ đồng thời nitơ và phosphat thường nảy sinh sự cạnh tranh về điều kiện sinh hóa; các thông số vận hành lý tưởng cho quá trình hấp thụ nitơ có thể không trùng khớp hoàn toàn với điều kiện tối ưu để vi tảo đồng hóa photpho.
    * Tồn tại sự đánh đổi nội tại giữa nồng độ chất ô nhiễm còn lại trong nước thải đầu ra (effluent concentration) và hiệu suất loại bỏ (removal efficiency): khi nồng độ cơ chất trong dòng ra giảm xuống mức cực thấp, tốc độ sinh trưởng và hấp thụ của vi tảo bị giới hạn bởi động học phản ứng, khiến việc gia tăng hiệu suất loại bỏ đòi hỏi phải đánh đổi bằng chi phí vận hành hoặc kéo dài thời gian lưu.
  * **Cấu trúc hàm mục tiêu và hàm thích nghi (Objective / Fitness Functions)**:
    * Bài toán được cấu trúc thành tối ưu hóa hai mục tiêu: cực tiểu hóa nghịch đảo hiệu suất khử ($1/\text{Removal Efficiency}$, đại diện cho việc cực đại hóa hiệu suất loại bỏ) và cực tiểu hóa nồng độ cơ chất dinh dưỡng trong dòng ra ($\text{Ammonia Nitrogen Concentration}$ hoặc $\text{Phosphate Concentration}$).
    * Các mô hình toán học đã phát triển—bao gồm mô hình phương pháp bề mặt đáp ứng (Response Surface Methodology - RSM) và mạng nơ-ron nhân tạo (Artificial Neural Network - ANN)—được sử dụng trực tiếp làm các hàm thích nghi (fitness functions/surrogate models) để ước lượng chính xác đáp ứng của hệ thống cho các cá thể giải thuật di truyền.
  * **Biên giới hạn không gian biến quyết định (Decision Variable Boundaries)**:
    * Quá trình tối ưu hóa bị ràng buộc nghiêm ngặt bởi miền giá trị thiết kế thực nghiệm:
      * Thời gian vận hành / thời gian lưu thủy lực ($\text{Time}$ / HRT): $0 \le \text{Time} \le 20\text{ ngày (days)}$.
      * Độ $\text{pH}$: $6 \le \text{pH} \le 9$ (tận dụng vùng đệm kiềm nhẹ tối ưu của quá trình quang hợp vi tảo).
      * Nồng độ tổng carbon hữu cơ (Total Organic Carbon - TOC): $40 \le \text{TOC} \le 120\text{ mg/L}$.
  * **Nguyên lý và cơ chế hình thành mặt biên Pareto (Pareto Optimal Front)**:
    * NSGA-II ứng dụng cơ chế sắp xếp không bị chi phối (non-dominated sorting), tính toán khoảng cách tập trung (crowding distance) nhằm duy trì độ phân tán đa dạng của quần thể, và cơ chế bảo toàn độ ưu tú (elitism) qua các thế hệ.
    * Thay vì chỉ tìm một nghiệm cực trị đơn lẻ mang tính cứng nhắc, giải thuật tạo lập một tập hợp nghiệm tối ưu không bị chi phối (non-dominated solutions) tạo thành mặt biên Pareto (Pareto front), đại diện cho các phương án thỏa hiệp tối ưu nhất giữa nồng độ dòng ra và hiệu suất xử lý.

* **Kết quả tối ưu hóa đa mục tiêu cho Nitơ Amoniac (Ammonia Nitrogen Optimization)**:
  * **Động thái đánh đổi trên mặt biên Pareto (Hình 10a,b)**:
    * Đồ thị mặt biên Pareto giữa $1/\text{Removal Efficiency}$ và nồng độ Amonia Nitơ minh chứng rằng hiệu suất loại bỏ có xu hướng giảm khi nồng độ Amonia Nitơ tăng lên trong vùng khảo sát; mô hình được tối ưu hóa nhằm đồng thời đạt nồng độ Amonia Nitơ thấp nhất và hiệu suất khử cao nhất.
  * **Kết quả tối ưu hóa bằng mô hình mạng nơ-ron nhân tạo (ANN Optimization)**:
    * Phân tích đồ thị Pareto Front (Hình 10a) cho thấy điểm vận hành tối ưu của mô hình ANN đạt nồng độ Amonia Nitơ khoảng $1.932\text{ mg/L}$, với hiệu suất loại bỏ tương ứng đạt $87\,\%$.
    * Phân bố nghiệm trên đồ thị (a): nồng độ Amonia Nitơ tập trung trong dải hẹp từ $1.98319$ đến $1.983225\text{ mg/L}$, tương ứng $1/\text{Removal Efficiency}$ biến thiên từ $0.01149789$ về $0.01149787\text{ \%}$ (tương đương hiệu suất khử $\approx 86.97\,\%$ đến $87\,\%$).
  * **Kết quả tối ưu hóa bằng mô hình phương pháp bề mặt đáp ứng (RSM Optimization)**:
    * Khi tối ưu hóa mô hình RSM bằng NSGA-II để đạt hiệu suất loại bỏ cao nhất với hàm lượng Amonia Nitơ thấp nhất, điểm tối ưu ghi nhận nồng độ Amonia Nitơ khoảng $1.722\text{ mg/L}$ với hiệu quả loại bỏ đạt $87\,\%$.
    * Phân bố nghiệm trên đồ thị (b): nồng độ Amonia Nitơ nằm trong khoảng $1.7221$ đến $1.72223\text{ mg/L}$, với $1/\text{Removal Efficiency}$ giảm từ $0.01122774$ về $0.01122765\text{ \%}$ (tương đương hiệu suất khử thực tế $\approx 89.06\,\%$ đến $89.07\,\%$).
  * **Hình 10.** Mặt biên Pareto từ tối ưu hóa đa mục tiêu NSGA-II
    * <img src="assets/fig_11_p13.png" alt="Hình 10" />
    * **Hình này chứng minh điều gì**
      * Cả tối ưu hóa dựa trên ANN (a) và RSM (b) đều tạo thành mặt biên Pareto liên tục thể hiện sự đánh đổi giữa hai mục tiêu: cực tiểu hóa nồng độ Amonia Nitơ và cực đại hóa hiệu suất khử ($1/\text{Removal Efficiency}$ cực tiểu).
    * **Từ đâu mà thấy được**
      * Đồ thị (a) ANN: nồng độ Ammonia Nitrogen tăng từ $1.98319$ đến $1.983224\text{ mg/L}$ khi $1/\text{Removal efficiency}$ giảm từ $0.01149789$ về $0.01149787\text{ \%}$.
      * Đồ thị (b) RSM: nồng độ Ammonia Nitrogen tăng từ $1.7221$ đến $1.72223\text{ mg/L}$ khi $1/\text{Removal efficiency}$ giảm từ $0.01122774$ về $0.01122765\text{ \%}$.

* **Kết quả tối ưu hóa đa mục tiêu cho Phosphat (Phosphate Optimization)**:
  * **Động thái đánh đổi trên mặt biên Pareto (Hình 10c,d)**:
    * Mặt biên Pareto biểu diễn mối quan hệ giữa $1/\text{Removal Efficiency}$ và nồng độ Phosphat cho thấy hiệu suất loại bỏ giảm khi nồng độ phosphat tăng lên, phản ánh quy luật cân bằng động học trong sự đồng hóa photpho của quần thể vi tảo.
  * **Kết quả tinh chỉnh mô hình ANN với NSGA-II**:
    * Theo công bố trong văn bản, mô hình ANN được điều chỉnh bằng NSGA-II đạt điểm tối ưu với nồng độ phosphat $9.5\text{ mg/L}$ và hiệu suất loại bỏ đạt $99\,\%$.
    * *Đối chiếu đồ thị thực tế Hình 10c*: Trục hoành đồ thị mang thang đo tỷ lệ $\times 10^{-3}$, cho thấy nồng độ phosphat thực tế trên biên Pareto là khoảng $9.5 \times 10^{-3}\text{ mg/L}$ ($0.0095\text{ mg/L}$) trong dải từ $9.4985 \times 10^{-3}$ đến $9.5015 \times 10^{-3}\text{ mg/L}$, ứng với $1/\text{Removal Efficiency}$ nằm trong khoảng $0.01000394$ đến $0.01000396\text{ \%}$ (tương đương hiệu suất khử $\approx 99.96\,\%$); số liệu $9.5\text{ mg/L}$ trong bài báo xuất phát từ việc lược bỏ hệ số tỷ lệ thang đo khi diễn giải bằng lời văn.
  * **Kết quả tối ưu hóa mô hình RSM với NSGA-II**:
    * Theo công bố trong văn bản, mô hình RSM được tối ưu hóa với NSGA-II đạt hàm lượng phosphat lý tưởng là $0.002\text{ mg/L}$ cùng hiệu quả làm sạch đạt $99\,\%$.
    * *Đối chiếu đồ thị thực tế Hình 10d*: Trục hoành đồ thị ghi nhận nồng độ phosphat biến thiên từ $0.201496$ đến $0.201514\text{ mg/L}$ (xấp xỉ $0.2015\text{ mg/L}$), với $1/\text{Removal Efficiency}$ nằm trong khoảng $0.01067439$ đến $0.01067447\text{ \%}$ (tương đương hiệu suất khử thực tế $\approx 93.68\,\%$); giá trị văn bản $0.002\text{ mg/L}$ và $99\,\%$ phản ánh sự khác biệt so với tọa độ trục số hiển thị trên đồ thị RSM.
  * **So sánh hiệu năng Pareto giữa mô hình ANN và RSM**:
    * Biên Pareto tối ưu hóa bởi ANN đạt nồng độ phosphat thấp hơn vượt bậc ($\sim 9.5 \times 10^{-3}\text{ mg/L}$) so với mô hình RSM ($\sim 0.2015\text{ mg/L}$), khẳng định khả năng xấp xỉ chính xác của mạng nơ-ron giúp NSGA-II khám phá được các giải pháp công nghệ ưu việt hơn.
  * **Hình 10.** (tiếp theo) Mặt biên Pareto và không gian biến quyết định
    * <img src="assets/fig_12_p14.png" alt="Hình 10 (tiếp theo)" />
    * **Hình này chứng minh điều gì**
      * Biên Pareto thể hiện sự đánh đổi giữa giảm nồng độ phosphate và tăng hiệu suất khử qua mô hình ANN và RSM.
      * Tối ưu hóa bằng ANN đạt nồng độ phosphate thấp hơn đáng kể ($\sim 9.5 \times 10^{-3}\text{ mg/L}$) so với RSM ($\sim 0.2015\text{ mg/L}$).
    * **Từ đâu mà thấy được**
      * Panel (c) ANN: $\text{Ox}$ nồng độ phosphate ($9.4985 \times 10^{-3}$ - $9.5015 \times 10^{-3}\text{ mg/L}$), $\text{Oy}$ $1/\text{Removal efficiency}$ ($0.01000394$ - $0.01000396\,\%$).
      * Panel (d) RSM: $\text{Ox}$ nồng độ phosphate ($0.201496$ - $0.201514\text{ mg/L}$), $\text{Oy}$ $1/\text{Removal efficiency}$ ($0.01067439$ - $0.01067447\,\%$).
      * Xu hướng đường cong dốc xuống: khi nồng độ phosphate tăng thì nghịch đảo hiệu suất giảm (hiệu suất khử tăng).

* **Ý nghĩa kỹ thuật và hỗ trợ ra quyết định vận hành (Operational Trade-offs and Decision Support)**:
  * **Tính linh hoạt trong điều hành hệ thống**: Khác với một điểm cài đặt cố định duy nhất, tập hợp nghiệm tối ưu Pareto cung cấp cho người vận hành nhà máy xử lý nước thải một dải phương án điều khiển linh hoạt; trong các thời điểm tải trọng thủy lực biến động mạnh, nhà vận hành có thể chủ động chuyển dịch điểm làm việc trên mặt biên Pareto để cân đối giữa yêu cầu xả thải khắt khe và chi phí năng lượng/thời gian lưu.
  * **Công cụ hỗ trợ ra quyết định mạnh mẽ**: Sự kết hợp giữa mô hình học máy (ANN/RSM) và giải thuật NSGA-II xác lập một khung tính toán AI tin cậy, chuyển đổi các mô phỏng lý thuyết thành công cụ hỗ trợ ra quyết định thiết thực trong quản lý và vận hành bền vững hệ thống xử lý nước thải bằng vi tảo.
