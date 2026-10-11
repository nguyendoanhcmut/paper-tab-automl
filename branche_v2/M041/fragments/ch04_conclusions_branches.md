## Conclusions

* **Kết luận chung về phát triển và so sánh mô hình (Overall conclusions on model development and comparison)**:
    * Nghiên cứu đã phát triển và so sánh thành công các mô hình trí tuệ tính toán (computational intelligence models) nhằm dự đoán và tối ưu hóa quá trình loại bỏ nitơ amoniac (ammonia nitrogen) và phosphat (phosphate) trong bể phản ứng sinh học màng vi tảo (microalgae membrane bioreactor - MBR).
    * Phân tích so sánh chứng minh rằng mô hình mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) vượt trội đáng kể so với phương pháp bề mặt đáp ứng (Response Surface Methodology - RSM).
    * ANN đạt hệ số xác định $R^2 > 0.99$ và các giá trị sai số căn bậc hai trung bình (root mean square error - RMSE) thấp hơn đối với tất cả các biến mục tiêu (target variables).
    * Kết quả khẳng định kiến trúc phi tuyến tính (non-linear architecture) của ANN vượt trội trong việc nắm bắt các động thái sinh học phức tạp (complex biological dynamics) của quá trình xử lý nước thải so với những giới hạn đa thức (polynomial limitations) của mô hình RSM.
### Novelty and contribution

* **Tính mới và đóng góp phương pháp luận (Novelty and contribution)**:
    * Đóng góp và tính mới cốt lõi của nghiên cứu nằm ở việc ứng dụng tích hợp ANN, RSM và thuật toán di truyền sắp xếp không bị chi phối thế hệ II (Non-dominated Sorting Genetic Algorithm II - NSGA-II) để thiết lập một khung hỗ trợ ra quyết định toàn diện (holistic decision-support framework).
    * Khác với các nghiên cứu trước đây vốn chỉ tập trung vào tối ưu hóa đơn mục tiêu (single-objective optimization), nghiên cứu này ứng dụng NSGA-II để tạo ra mặt tiền tối ưu Pareto (Pareto optimal front), làm sáng tỏ các mối quan hệ đánh đổi vận hành then chốt (critical operational trade-offs) giữa thời gian lưu và hiệu suất loại bỏ chất dinh dưỡng (nutrient removal efficiency).
    * Khung hỗ trợ ra quyết định này giúp người vận hành nhà máy lựa chọn các điều kiện vận hành linh hoạt—chẳng hạn như dải $\text{pH}$ từ $7.5\text{--}8.5$ và thời gian lưu thủy lực động (dynamic hydraulic retention time - dynamic HRT)—nhằm cân bằng giữa việc tuân thủ nghiêm ngặt các quy chuẩn môi trường với tính khả thi trong vận hành thực tế (operational feasibility).

### Limitations

* **Các giới hạn của nghiên cứu (Limitations)**:
    * Giới hạn về tập dữ liệu (dataset limitation): Quá trình xây dựng mô hình dựa trên tập dữ liệu thứ cấp (secondary dataset) gồm $44$ điểm thực nghiệm. Mặc dù các kỹ thuật kiểm định mạnh mẽ như dừng sớm (Early Stopping) và kiểm định chéo (cross-validation) đã được áp dụng để giảm thiểu hiện tượng quá khớp (overfitting), một tập dữ liệu lớn hơn sẽ giúp nâng cao hơn nữa độ tin cậy của mô hình.
    * Giới hạn về kiểm chứng thực nghiệm (experimental validation limitation): Các điều kiện tối ưu được đề xuất bởi thuật toán NSGA-II hiện tại mới chỉ là những dự đoán dựa trên mô hình (model-based predictions). Dù hoàn toàn phù hợp với các kỳ vọng lý thuyết, các điều kiện này vẫn chưa được kiểm chứng thực nghiệm vật lý trong điều kiện phòng thí nghiệm có kiểm soát (controlled laboratory setting).

### Future research directions

* **Định hướng nghiên cứu trong tương lai (Future research directions)**:
    * Kiểm chứng thực nghiệm có con người tham gia đánh giá (“human-in-the-loop” experimental validation): Khuyến nghị tiến hành thử nghiệm các điểm đặt (setpoints) cụ thể được xác định từ mặt tiền Pareto trên hệ thống MBR quy mô pilot (pilot-scale MBR) nhằm xác minh hiệu suất loại bỏ dự đoán.
    * Tích hợp khung AI với hệ thống giám sát thời gian thực (integration with real-time monitoring systems): Tiềm năng đáng kể trong việc kết nối các mô hình dự đoán này với các cảm biến IoT (Internet of Things), cho phép phát triển hệ thống điều khiển phản hồi tự động (automated feedback control system) có khả năng tự động điều chỉnh $\text{pH}$ và thời gian lưu theo dao động tải trọng dòng vào (fluctuating influent loads), tiến tới quản lý nước thải thông minh toàn diện (smart wastewater management).
