### 2.4. Ablation studies

* Nghiên cứu cắt bỏ (ablation studies) được tiến hành nhằm đánh giá mức độ đóng góp của các đặc trưng (features) khác nhau đối với hiệu suất dự đoán của các mô hình học máy (ML models - Machine Learning models).
    * Kỹ thuật ablation study đánh giá tác động của các thành phần cụ thể (chẳng hạn như đặc trưng, tham số, hoặc dữ liệu) bằng cách loại bỏ hoặc thay đổi chúng, sau đó quan sát các biến đổi tương ứng về hiệu suất mô hình.
    * Việc so sánh hiệu suất giữa các mô hình có và không có những đặc trưng cụ thể cho phép suy luận mức độ ảnh hưởng của từng đặc trưng lên quá trình mô hình hóa.
* Nghiên cứu đánh giá cụ thể tác động của $5$ đặc trưng vận hành và hóa sinh lên hiệu suất mô hình:
    * $\text{OD}$ (operation days - số ngày vận hành).
    * $\text{ORP}$ (oxidation-reduction potential - thế oxy hóa - khử).
    * $\text{HRT}$ (hydraulic retention time - thời gian lưu nước thủy lực).
    * $\text{MLSS}$ (mixed liquor suspended solids - nồng độ chất rắn lơ lửng trong bùn lỏng).
    * $\text{MLVSS}$ (mixed liquor volatile suspended solids - nồng độ chất rắn lơ lửng bay hơi trong bùn lỏng).
* Tác động của việc mở rộng quy mô dữ liệu được khảo sát thông qua tập dữ liệu mở rộng (extended dataset), do nghiên cứu thu thập được lượng dữ liệu lớn hơn so với nghiên cứu trước đây.
* Toàn bộ dữ liệu huấn luyện (training data), dữ liệu kiểm tra (testing data) cũng như các tham số huấn luyện mô hình (model training parameters) được duy trì nhất quán với thiết lập trước đó xuyên suốt quá trình thực hiện ablation studies.
