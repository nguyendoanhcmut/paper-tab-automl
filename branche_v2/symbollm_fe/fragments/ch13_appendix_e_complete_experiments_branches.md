## Appendix E Complete Experiments

* Tiến hành đánh giá toàn diện và đầy đủ (full comprehensive evaluation) đối với SymboLLM-FE trong Bảng 10 (Table 10), Bảng 11 (Table 11) và Bảng 12 (Table 12):
  * SymboLLM-FE được so sánh một cách có hệ thống (systematically compared) với các phương pháp kỹ thuật đặc trưng tự động tối tân (state-of-the-art automated feature engineering - AutoFE) trên nhiều tập dữ liệu thực tế (multiple real-world datasets).
  * Các mô hình học máy xuôi dòng (downstream models) dùng để đánh giá và dự đoán bao gồm các mô hình dựa trên cây (tree-based models) như `CatBoost` và `XGBoost`, mô hình mạng nơ-ron truyền thẳng `MLP` (Multi-Layer Perceptron), và mô hình nền tảng dạng transformer cho dữ liệu bảng `TabPFN`.
  * Các tập dữ liệu thực nghiệm bao gồm bốn tác vụ phân loại (`Credit-g`, `Spaceship`, `Cmc`, `Academic`) và hai tác vụ hồi quy (`Ailerons`, `Tesla`).
  * Các phương pháp AutoFE cơ sở đối chuẩn gồm có `Baseline` (đặc trưng gốc chưa qua xử lý), các phương pháp truyền thống và dựa trên cây (`AutoFeat`, `OpenFE`, `OcTree`, `FEBP`), cùng các phương pháp AutoFE dựa trên LLM (`CAAFE`, `LLM-FE`, `LLM-RANK`).

### E.1 Full Results Across Real-World Datasets

* Đánh giá hiệu năng tổng thể trên các thước đo Accuracy và RMSE trong Bảng 10 (Table 10):
  * Đối với các tác vụ phân loại (`Credit-g`, `Spaceship`, `Cmc`, `Academic`), hiệu năng được đánh giá bằng độ chính xác Accuracy ($\uparrow$, giá trị càng cao càng tốt).
  * Đối với các tác vụ hồi quy (`Ailerons`, `Tesla`), hiệu năng được đo lường bằng căn bậc hai của sai số bình phương trung bình RMSE (Root Mean Squared Error, $\downarrow$, giá trị càng thấp càng tốt).
  * Kết quả thực nghiệm xác nhận SymboLLM-FE đạt được nhiều kết quả tốt nhất (in đậm trong bảng gốc) và tốt thứ nhì (gạch chân trong bảng gốc) nhất trên cả tác vụ phân loại và hồi quy.
  * Hiệu năng nổi bật của SymboLLM-FE trên từng mô hình xuôi dòng:
    * Trên `CatBoost`: SymboLLM-FE đạt kết quả tốt nhất trên `Cmc` ($74.86 \pm 2.44$), `Academic` ($88.02 \pm 0.66$), `Ailerons` ($\text{RMSE} = 4.08 \pm 0.55$), và `Tesla` ($\text{RMSE} = 2.41 \pm 0.06$).
    * Trên `XGBoost`: SymboLLM-FE duy trì vị thế dẫn đầu trên hầu hết các điểm chuẩn, đặc biệt vượt trội trên `Tesla` ($\text{RMSE} = 2.41 \pm 0.06$) so với `Baseline` ($2.72 \pm 0.14$).
    * Trên `MLP`: SymboLLM-FE giúp mô hình mạng nơ-ron duy trì hiệu năng cao và ổn định, khắc phục nhược điểm nhạy cảm với đặc trưng nhiễu.
    * Trên `TabPFN`: SymboLLM-FE chiếm lĩnh vị trí dẫn đầu trên `Spaceship` ($81.27 \pm 1.31$), `Cmc` ($57.97 \pm 0.73$), `Academic` ($77.89 \pm 0.23$), `Ailerons` ($\text{RMSE} = 5.02 \pm 0.46$), và `Tesla` ($\text{RMSE} = 2.16 \pm 0.06$).
* Đánh giá năng lực phân biệt và sai số tuyệt đối qua ROC-AUC và MAE trong Bảng 11 (Table 11):
  * Tác vụ phân loại được đánh giá qua diện tích dưới đường cong ROC (ROC-AUC, $\uparrow$, giá trị càng cao càng tốt), định lượng khả năng phân tách xác suất giữa các lớp.
  * Tác vụ hồi quy được đánh giá qua sai số tuyệt đối trung bình MAE (Mean Absolute Error, $\downarrow$, giá trị càng thấp càng tốt).
  * SymboLLM-FE liên tục thể hiện năng lực vượt trội hoặc tương đương với các baseline mạnh nhất trên mọi tập dữ liệu và mô hình xuôi dòng, minh chứng các đặc trưng sinh ra có chất lượng biểu diễn cao và phân bố ổn định.
* Đánh giá chất lượng phân loại nâng cao và độ giải thích phương sai qua F1-Score và $R^2$ trong Bảng 12 (Table 12):
  * Tác vụ phân loại được đo lường bằng F1-Score ($\uparrow$, giá trị càng cao càng tốt), phản ánh sự cân bằng tối ưu giữa độ chính xác (Precision) và độ phủ (Recall), đặc biệt hữu ích trên các tập dữ liệu mất cân bằng nhãn.
  * Tác vụ hồi quy được đo lường bằng hệ số xác định $R^2$ ($\uparrow$, giá trị càng cao càng tốt), biểu thị tỷ lệ phương sai của biến mục tiêu được giải thích bởi mô hình.
  * SymboLLM-FE tiếp tục giữ vững vị trí tốt nhất và tốt thứ nhì xuyên suốt các mô hình `CatBoost`, `XGBoost`, `MLP`, và `TabPFN`, chứng minh tính ưu việt đồng bộ trên đa dạng góc độ đánh giá thống kê.

### E.2 Model Comparisons Across Metrics

* Độ vững chãi liên mô hình (cross-model robustness) xuyên suốt các kiến trúc học máy:
  * Cho dù mô hình xuôi dòng là mô hình dựa trên cây (tree-based model như `CatBoost`, `XGBoost`), mạng nơ-ron (neural network như `MLP`), hay mô hình nền tảng dạng transformer (`TabPFN`), SymboLLM-FE liên tục cải thiện hoặc duy trì hiệu năng ở mức hàng đầu (top performance).
  * Khắc phục hoàn toàn hiện tượng quá khớp (overfitting) hoặc phụ thuộc vào loại mô hình cụ thể, khẳng định các đặc trưng tạo bởi hồi quy ký hiệu và LLM có giá trị thông tin phổ quát (general informativeness).
* So sánh đối chuẩn với các phương pháp AutoFE dựa trên LLM (LLM-based AutoFE):
  * So với các phương pháp AutoFE dựa trên LLM thuần túy (`CAAFE`, `LLM-FE`, `LLM-RANK`), SymboLLM-FE đạt được hiệu năng vượt trội hơn trên nhiều tác vụ thực nghiệm.
  * Nguyên nhân xuất phát từ kiến trúc lai độc đáo: hồi quy ký hiệu (Symbolic Regression) đảm nhiệm việc khám phá cấu trúc toán học khách quan gắn chặt với nhãn mục tiêu, trong khi LLM đóng vai trò bộ tích hợp tất định (deterministic integrator) đưa tri thức tiên nghiệm vào tinh chỉnh thay vì sinh đặc trưng ngẫu nhiên.
  * Kết quả này xác thực tính hiệu quả (effectiveness) và năng lực khái quát hóa (generalization capability) vượt bậc của SymboLLM-FE so với các tiếp cận AutoFE hiện hành.
