### Practical implications and environmental relevance

* **Ý nghĩa thực tiễn và mở rộng quy mô (Scale-up and practical engineering insights)**:
    * Kết quả tối ưu hóa từ khung tính toán kết hợp ANN và NSGA-II cung cấp các thông số định hướng then chốt phục vụ mở rộng quy mô (scale-up) và vận hành hệ thống bể phản ứng sinh học màng vi tảo (microalgae MBRs).
    * Mô hình xác định khoảng $\text{pH}$ tối ưu cho quá trình loại bỏ chất dinh dưỡng nằm trong dải từ $7.5$ đến $8.5$.
    * Từ góc độ kỹ thuật công trình thực tế (practical engineering perspective), dải $\text{pH}\ 7.5\text{--}8.5$ tạo nên một cửa sổ vận hành (operational window) rất thuận lợi cho công nghệ màng sinh học.
* **Cơ chế tự điều hòa pH và tối ưu chi phí vận hành (pH self-regulation and OPEX reduction)**:
    * Hoạt động quang hợp của vi tảo tiêu thụ tự nhiên lượng $\text{CO}_2$ hòa tan trong hỗn dịch bùn lỏng (mixed liquor), dẫn tới xu hướng tự nâng cao chỉ số $\text{pH}$ của môi trường phản ứng.
    * Nhờ cơ chế kiềm hóa tự nhiên này, việc duy trì bioreactor trong dải kiềm nhẹ ($\text{pH}\ 7.5\text{--}8.5$) chỉ đòi hỏi lượng hóa chất đệm bổ sung (axit hoặc bazơ) ở mức tối thiểu.
    * Việc giảm thiểu hóa chất đệm giúp cắt giảm đáng kể chi phí vận hành (Operational Expenditure - OPEX) của hệ thống xử lý.
    * Hạn chế hóa chất bổ sung đồng thời ngăn ngừa nguy cơ ô nhiễm hóa chất thứ cấp (secondary chemical contamination) đối với nguồn nước đầu ra (effluent).
* **Đánh đổi vận hành giữa thời gian lưu và chi phí đầu tư (Operational trade-off: HRT vs. CAPEX)**:
    * Phân tích biến số "Thời gian" (Time), đại diện cho thời gian lưu thủy lực (Hydraulic Retention Time - HRT), làm sáng tỏ mối quan hệ đánh đổi vận hành cốt lõi (critical operational trade-off).
    * Mô hình dự đoán rằng mục tiêu tối đa hóa hiệu suất loại bỏ chất ô nhiễm đạt mức $> 90\%$ đòi hỏi thời gian lưu phải vượt trên $12\text{ ngày}$ ($> 12\text{ ngày}$).
    * Mức hiệu suất $> 90\%$ giúp đáp ứng nghiêm ngặt các quy chuẩn xả thải môi trường tại các nguồn nước nhạy cảm nhằm ngăn ngừa hiện tượng phú dưỡng (eutrophication).
    * Tuy nhiên, thời gian lưu kéo dài trên $12\text{ ngày}$ đòi hỏi dung tích bể phản ứng lớn hơn, làm gia tăng đáng kể chi phí vốn đầu tư xây dựng ban đầu (Capital Expenditure - CAPEX).
* **Hỗ trợ ra quyết định linh hoạt thông qua mặt biên Pareto (Decision-support via Pareto front)**:
    * Tối ưu hóa đa mục tiêu với mặt biên Pareto (Pareto front) đem lại công cụ điều hành giá trị cho các kỹ sư vận hành nhà máy (plant operators).
    * Thay vì phải bám sát một điểm đặt cố định cứng nhắc (single rigid setpoint), người vận hành có thể căn cứ vào mô hình để điều chỉnh linh hoạt quy trình theo tải lượng thực tế.
    * Trong các giai đoạn đỉnh tải thủy lực (peak hydraulic load), trạm xử lý có thể chủ động lựa chọn nghiệm không bị chi phối (non-dominated solution) với thời gian lưu ngắn hơn (ví dụ: $8\text{--}10\text{ ngày}$) mà vẫn duy trì hiệu quả xử lý trong ngưỡng quy chuẩn xả thải cho phép.
    * Việc lựa chọn thời gian lưu $8\text{--}10\text{ ngày}$ giúp tránh tình trạng gượng ép đạt hiệu suất lý thuyết tối đa vốn có thể gây nghẽn hoặc quá tải hệ thống (system bottleneck).
    * Khả năng thích ứng linh hoạt này chứng minh khung trí tuệ nhân tạo đề xuất là một công cụ hỗ trợ ra quyết định đáng tin cậy cho công tác quản lý nước thải bền vững.
* **So sánh đối chứng với các nghiên cứu tiền nhiệm (Benchmarking against previous microalgae MBR studies)**:
    * Nghiên cứu tiến hành so sánh đối chứng toàn bộ kết quả mô hình hóa, dự đoán và tối ưu hóa hành vi hệ thống MBR vi tảo với các công trình công bố gần đây.
    * Trong điều kiện hỗn dưỡng (mixotrophic circumstances) với glucose và các hợp chất hữu cơ khác, lượng sinh khối vi tảo tăng cao trong môi trường dinh dưỡng hỗn hợp giúp hiệu suất loại bỏ nitơ và photpho cao hơn so với điều kiện tự dưỡng quang năng thuần túy (photoautotrophic settings).
    * Hiệu quả loại bỏ chất ô nhiễm trong các nghiên cứu trước đây thấp hơn đáng kể so với kết quả đạt được trong nghiên cứu này, dù hiện tượng thực nghiệm quan sát có nhiều nét tương đồng.
    * Chế độ nuôi cấy liên tục (continuous culture) trong thí nghiệm tạo điều kiện cho hệ thống bể phản ứng vận hành ổn định, thúc đẩy vi tảo nhanh chóng đạt trạng thái sinh trưởng cân bằng (steady-state microalgae growth) và nâng cao hiệu quả khử chất ô nhiễm.
    * Khung thuật toán kết hợp ANN, RSM và NSGA-II trong công trình hiện tại tích hợp xử lý đồng thời nitơ và photpho với độ chính xác cao so với các mô hình trước chỉ tập trung vào một khía cạnh riêng lẻ.
        * **Bảng 2.** So sánh với các nghiên cứu mô hình hóa MBR vi tảo gần đây
            * <img src="assets/table_02_p15.png" alt="Bảng 2" />
            * **Bảng này chứng minh điều gì**
                * Nghiên cứu hiện tại áp dụng đồng thời ANN, RSM và NSGA-II để xử lý dinh dưỡng trong MBR vi tảo với độ chính xác cao.
            * **Từ đâu mà thấy được**
                * Cột "System" và "Algorithms": hàng "Present work" tích hợp cả 3 phương pháp cho khử dinh dưỡng, so với chỉ MLP-ANN dự báo nghẽn màng (Wang et al.) hay nước rỉ rác (Asrami et al.).
                * Cột "Results": hàng "Present work" khẳng định mô hình và tối ưu hóa đạt độ chính xác đáng kể ("significant level of precision") trên hệ MBR vi tảo.
