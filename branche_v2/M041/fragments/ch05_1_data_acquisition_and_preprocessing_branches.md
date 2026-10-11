### Data acquisition and preprocessing

* **Nguồn dữ liệu thực nghiệm và mục tiêu nghiên cứu (Source dataset and study objective)**:
    * Dữ liệu thực nghiệm của nghiên cứu được kế thừa từ công trình của Ding et al. [23], tập trung vào quá trình xử lý nước thải nuôi trồng thủy sản biển (mariculture wastewater) trong bể phản ứng sinh học màng vi tảo (microalgae membrane bioreactor - MBR).
    * Công trình này đóng vai trò là một nghiên cứu tái phân tích bằng mô hình hóa tính toán (computational modeling reanalysis) nhằm trích xuất các quy luật tối ưu hóa chuyên sâu (optimization insights) chưa từng được khám phá trong nghiên cứu thực nghiệm gốc.
    * Tập dữ liệu bao gồm $44$ điểm dữ liệu thực nghiệm riêng biệt ($44$ distinct experimental data points / runs).

* **Các biến số đầu vào và đầu ra của mô hình (Model input and output variables)**:
    * **Biến đầu vào độc lập (Input variables)**:
        * Thời gian vận hành (Time): đơn vị tính bằng ngày (days), dải khảo sát từ $0$ đến $20\text{ ngày}$.
        * Độ $\text{pH}$: dải khảo sát từ $6$ đến $9$.
        * Tổng carbon hữu cơ (Total Organic Carbon - TOC): đơn vị tính bằng $\text{mg/L}$, dải nồng độ khảo sát từ $40$ đến $120\text{ mg/L}$.
    * **Biến đáp ứng đầu ra (Output response variables)**:
        * Nồng độ nitơ amoniac (Ammonia Nitrogen concentration, $\text{mg/L}$).
        * Nồng độ phosphat (Phosphate concentration, $\text{mg/L}$).
        * Hiệu suất loại bỏ nitơ amoniac tương ứng (Ammonia Nitrogen Removal Efficiency, $\%$).
        * Hiệu suất loại bỏ phosphat tương ứng (Phosphate Removal Efficiency, $\%$).

* **Kỹ thuật tiền xử lý và chuẩn hóa Min-Max (Data preprocessing and Min-Max normalization)**:
    * Để đảm bảo khả năng hội tụ hiệu quả (efficient convergence) trong suốt tiến trình huấn luyện mạng nơ-ron nhân tạo (artificial neural network - ANN), toàn bộ dữ liệu đầu vào và đầu ra đều được chuẩn hóa về khoảng $[0, 1]$.
    * Phương pháp chuẩn hóa Min-Max (Min-Max normalization technique) được áp dụng theo công thức Phương trình (9):
      $$X_{\text{norm}} = \frac{X_i - X_{\min}}{X_{\max} - X_{\min}}$$
      * $X_{\text{norm}}$: Giá trị đã chuẩn hóa (normalized value), nằm trong khoảng $[0, 1]$.
      * $X_i$: Giá trị thực nghiệm đo đạc thực tế (actual value).
      * $X_{\min}$: Giá trị nhỏ nhất (cực tiểu) của biến số tương ứng trong tập dữ liệu (minimum value of the dataset).
      * $X_{\max}$: Giá trị lớn nhất (cực đại) của biến số tương ứng trong tập dữ liệu (maximum value of the dataset).

* **Chiến lược phân chia tập dữ liệu mô hình hóa ANN (Dataset partitioning for ANN modeling)**:
    * Toàn bộ $44$ điểm dữ liệu thực nghiệm được phân chia ngẫu nhiên (randomly partitioned) thành 3 tập con phục vụ huấn luyện và đánh giá mô hình:
        * **Tập huấn luyện (Training subset - $70\%$, $\sim 31$ mẫu)**: Dùng để điều chỉnh và cập nhật các trọng số mạng (network weights) và độ lệch của mô hình ANN.
        * **Tập kiểm định (Validation subset - $15\%$, $\sim 6-7$ mẫu)**: Dùng để giám sát sai số và ngăn ngừa hiện tượng quá khớp (prevent overfitting) trong quá trình huấn luyện.
        * **Tập kiểm tra (Testing subset - $15\%$, $\sim 6-7$ mẫu)**: Dùng để đánh giá độc lập và khách quan khả năng tổng quát hóa (generalization capability) của mô hình trên tập dữ liệu hoàn toàn mới chưa từng thấy (unseen data).
