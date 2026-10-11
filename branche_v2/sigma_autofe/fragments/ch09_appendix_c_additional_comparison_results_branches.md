## Appendix C. Additional Comparison Results of Different Metrics

* **Tổng quan về so sánh mở rộng trên các thước đo hiệu năng khác nhau (Additional Comparison Metrics)**:
  * Bên cạnh chỉ số Macro-F1 được sử dụng làm thước đo chính trong các thử nghiệm phần thân bài, Bảng 4 (Table 4) và Bảng 5 (Table 5) cung cấp kết quả so sánh tổng thể toàn diện trên hai chỉ số bổ sung: Accuracy (ACC - độ chính xác) và AUC-ROC (Area Under the Receiver Operating Characteristic Curve - diện tích dưới đường cong ROC đặc trưng hoạt động của bộ thu).
  * Các thử nghiệm so sánh được tiến hành trên hai nhóm phương pháp đối sánh:
    * Nhóm các phương pháp tạo đặc trưng tự động dựa trên LLM (LLM-based AutoFE): Baseline (không dùng AutoFE), CAAFE, OCTree, và SIGMA (Table 4).
    * Nhóm các phương pháp AutoFE truyền thống (traditional AutoFE) dưới cùng mức ngân sách đặc trưng (feature budget) là $20$: Baseline (không dùng AutoFE), AutoFeat, DFS, OpenFE, và SIGMA (Table 5).

* **So sánh tổng thể giữa các phương pháp AutoFE dựa trên LLM (Table 4: Overall accuracy (ACC) and AUC-ROC comparison of LLM-based AutoFE)**:
  * *Bảng tổng hợp kết quả thực nghiệm*:
    | Metric | Baseline (w.o. AutoFE) | CAAFE | OCTree | SIGMA |
    | :--- | :---: | :---: | :---: | :---: |
    | **Average ACC** | $79.22$ | $79.91 \pm 0.18$ | $79.10 \pm 0.14$ | $\mathbf{79.98 \pm 0.24}$ |
    | **Avg ACC Rank** | $2.50$ | $2.38$ | $3.12$ | $\mathbf{2.00}$ |
    | **Average AUC** | $87.01$ | $\mathbf{87.43 \pm 0.12}$ | $86.77 \pm 0.10$ | $87.41 \pm 0.04$ |
    | **Avg AUC Rank** | $2.44$ | $2.12$ | $3.38$ | $\mathbf{2.00}$ |
  * *Độ chính xác trung bình (Average ACC) và thứ hạng (Avg ACC Rank)*:
    * SIGMA thiết lập độ chính xác trung bình cao nhất ($79.98 \pm 0.24$), vượt qua CAAFE ($79.91 \pm 0.18$), Baseline ($79.22$), và OCTree ($79.10 \pm 0.14$).
    * SIGMA đạt thứ hạng trung bình tốt nhất về ACC ($\text{Avg ACC Rank} = 2.00$), dẫn đầu tuyệt đối so với CAAFE ($2.38$), Baseline ($2.50$), và OCTree ($3.12$).
  * *Chỉ số AUC-ROC trung bình (Average AUC) và thứ hạng (Avg AUC Rank)*:
    * SIGMA đạt AUC trung bình $87.41 \pm 0.04$, bám sát CAAFE ($87.43 \pm 0.12$) với mức chênh lệch không đáng kể ($0.02\%$), đồng thời vượt xa Baseline ($87.01$) và OCTree ($86.77 \pm 0.10$).
    * Độ lệch chuẩn của SIGMA trên AUC đạt mức thấp ấn tượng ($\pm 0.04$, nhỏ hơn 3 lần so với $\pm 0.12$ của CAAFE), khẳng định độ ổn định vượt trội của phương pháp qua các lần sinh đặc trưng.
    * Về thứ hạng trung bình AUC, SIGMA vươn lên vị trí dẫn đầu toàn diện với $\text{Avg AUC Rank} = 2.00$ (vượt qua CAAFE với $2.12$, Baseline với $2.44$, và OCTree với $3.38$).
  * *Phân tích ưu thế của SIGMA trước các mô hình LLM-based*:
    * OCTree bộc lộ hạn chế khi hiệu năng giảm sút so với Baseline trên cả hai thước đo ($79.10$ so với $79.22$ ở ACC; $86.77$ so với $87.01$ ở AUC), xếp hạng trung bình kém nhất trong nhóm ($3.12$ cho ACC và $3.38$ cho AUC).
    * SIGMA vượt qua hạn chế không có siêu dữ liệu ngữ nghĩa (metadata-free), đạt vị trí số 1 về thứ hạng tổng thể trên cả Accuracy lẫn AUC-ROC mà không cần thông tin mô tả ngữ nghĩa vốn là yêu cầu bắt buộc của CAAFE.

* **So sánh với các phương pháp AutoFE truyền thống dưới ngân sách 20 đặc trưng (Table 5: Overall accuracy (ACC) and AUC-ROC comparison of traditional methods under a feature budget of 20)**:
  * *Bảng tổng hợp kết quả thực nghiệm*:
    | Dataset / Metric | Baseline (w.o. AutoFE) | AutoFeat | DFS | OpenFE | SIGMA |
    | :--- | :---: | :---: | :---: | :---: | :---: |
    | **Average ACC** | $79.22$ | $79.36$ | $79.39$ | $\mathbf{80.18}$ | $79.98 \pm 0.24$ |
    | **Avg ACC Rank** | $3.38$ | $3.06$ | $3.44$ | $\mathbf{2.38}$ | $2.69$ |
    | **Average AUC** | $87.01$ | $87.30$ | $87.09$ | $\mathbf{87.60}$ | $87.41 \pm 0.04$ |
    | **Avg AUC Rank** | $3.38$ | $2.81$ | $3.44$ | $\mathbf{2.50}$ | $2.81$ |
  * *Độ chính xác trung bình (Average ACC) và thứ hạng*:
    * SIGMA đạt $79.98 \pm 0.24$, vượt trội so với Baseline ($79.22$), AutoFeat ($79.36$), và DFS ($79.39$).
    * Thứ hạng trung bình theo ACC của SIGMA đạt $2.69$, giữ vị trí thứ 2 trong tất cả các phương pháp, xếp trên AutoFeat ($3.06$), Baseline ($3.38$), DFS ($3.44$), và chỉ đứng sau OpenFE ($80.18$, hạng $2.38$).
  * *Chỉ số AUC-ROC trung bình (Average AUC) và thứ hạng*:
    * SIGMA đạt $87.41 \pm 0.04$, vượt Baseline ($87.01$), DFS ($87.09$), và AutoFeat ($87.30$).
    * Về thứ hạng trung bình AUC, SIGMA đạt $2.81$, đồng hạng 2 cùng AutoFeat ($2.81$), vượt trội so với Baseline ($3.38$) và DFS ($3.44$).
  * *Hiệu quả sử dụng đặc trưng vượt trội của SIGMA so với AutoFE truyền thống*:
    * Các phương pháp truyền thống (AutoFeat, DFS, OpenFE) bắt buộc phải sử dụng đủ ngân sách tối đa $20$ đặc trưng được chọn lọc thủ công hoặc tìm kiếm toàn diện (`feature budget of 20`).
    * Ngược lại, SIGMA đạt hiệu năng cạnh tranh tương đương và áp sát OpenFE trong khi vượt qua AutoFeat và DFS, dù chỉ cần sinh ra trung bình $5.4$ đặc trưng mới và hoàn toàn không phụ thuộc vào siêu dữ liệu ngữ nghĩa.

* **Ghi nhận các bộ dữ liệu có hiệu năng vượt trội**:
  * Qua các chỉ số đánh giá (kết hợp quan sát từ các phân tích thực nghiệm trên 16 bộ dữ liệu chuẩn), SIGMA thể hiện sự vượt trội vượt bậc trên nhiều bộ dữ liệu đại diện:
    * *credit-g*: Đạt bước nhảy vọt hiệu năng rõ rệt, vượt toàn bộ các phương pháp truyền thống (OpenFE, DFS, AutoFeat) và các phương pháp LLM-based khác.
    * *compass*: Thiết lập mức cải thiện ấn tượng nhất, vượt trội hoàn toàn so với mô hình cơ sở và các phương pháp AutoFE truyền thống cũng như CAAFE.
    * *jungle chess*: Thể hiện năng lực khai phá đặc trưng tương tác phi tuyến tính phức tạp khi vượt qua OpenFE và bỏ xa các phương pháp còn lại.
    * *eucalyptus* và *electricity*: Đạt điểm số bứt phá mạnh mẽ so với Baseline và các đối thủ cạnh tranh chính, củng cố tính hiệu quả của cơ chế tạo đặc trưng dựa trên SHAP và quỹ đạo ẩn EXIT.
