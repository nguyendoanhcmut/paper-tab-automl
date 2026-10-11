## 5 Experiments

### 5.1 Experimental Setup

- **Tập dữ liệu thực nghiệm (Datasets)**:
  - Lựa chọn đa dạng các bộ dữ liệu mã nguồn mở và đáng tin cậy từ OpenML và Kaggle.
  - Các tập dữ liệu bao gồm ba tác vụ chính: phân loại nhị phân (binary classification), phân loại đa lớp (multi-class classification), và hồi quy (regression).
  - Trải rộng trên nhiều lĩnh vực khác nhau như tài chính (finance) và y tế/chăm sóc sức khỏe (healthcare).
  - Thông tin chi tiết về các bộ dữ liệu được cung cấp trong Appendix C.1 (gồm Credit-g, Spaceship, Cmc, Academic, Ailerons, Tesla).
- **Mô hình cơ sở xuôi dòng (Downstream Baselines)**:
  - Đánh giá trên nhiều mô hình dựa trên cây (tree-based models) và mô hình học sâu (deep learning models) nhằm xác thực tính tổng quát hóa (generalization) và khả năng thích ứng (adaptability) của SymboLLM-FE.
  - Mô hình dựa trên cây: CatBoost (Prokhorenkova et al., 2018) và XGBoost (Chen and Guestrin, 2016).
  - Mô hình học sâu: MLP (Gorishniy et al., 2021) và TabPFN (Hollmann et al., 2025).
  - Appendix C.2 cung cấp thông tin chi tiết về các mô hình cơ sở này cùng lưới siêu tham số đầy đủ (full hyperparameter grids).
- **Các phương pháp AutoFE đối chuẩn (Comparison AutoFE)**:
  - So sánh SymboLLM-FE với hai phương pháp AutoFE truyền thống (traditional AutoFE) là AutoFeat (Horn et al., 2019) và OpenFE (Zhang et al., 2023b).
  - So sánh với năm phương pháp AutoFE dựa trên LLM (LLM-based AutoFE): LLM-SELECT (Jeong et al., 2024), CAAFE (Hollmann et al., 2023b), OcTree (Nam et al., 2024), FEBP (Zou et al., 2026), và LLM-FE (Abhyankar et al., 2025), cùng với LLM-RANK.
  - Chi tiết về các phương pháp AutoFE đối chuẩn được trình bày trong Appendix C.3.
- **Thước đo đánh giá (Evaluation Metrics)**:
  - Đối với các tác vụ phân loại (classification tasks): đánh giá các thước đo gồm Độ chính xác (Accuracy), Diện tích dưới đường cong ROC (ROC-AUC - Area Under the Receiver Operating Characteristic Curve), và Điểm F1 (F1-score).
  - Đối với các tác vụ hồi quy (regression tasks): áp dụng Sai số toàn phương trung bình căn (RMSE - Root Mean Square Error), Sai số tuyệt đối trung bình (MAE - Mean Absolute Error), và Hệ số xác định ($R^2$ - R-squared).

### 5.2 Main Results

- **Hiệu năng vượt trội trên các bộ dữ liệu thực tế (Table 2)**:
  - SymboLLM-FE đạt được những cải thiện có ý nghĩa thống kê so với các phương pháp AutoFE truyền thống (mức tăng trung bình đạt $1.23\%$) và đạt độ chính xác cao hơn khoảng $1\%$ so với các phương pháp AutoFE dựa trên LLM.
  - Các kết quả thực nghiệm chi tiết với mô hình dự đoán xuôi dòng TabPFN được thể hiện trong Table 2:
    - Credit-g ($\uparrow$ Accuracy): Baseline $77.03 \pm 0.47$, AutoFeat $77.83 \pm 1.43$, OpenFE $76.50 \pm 3.34$, CAAFE $78.00 \pm 0.71$, OcTree $76.50 \pm 0.82$, FEBP $77.50 \pm 0.41$, LLM-FE $76.67 \pm 0.62$, LLM-RANK $77.50 \pm 0.82$, SymboLLM-FE $77.00 \pm 1.63$.
    - Spaceship ($\uparrow$ Accuracy): Baseline $80.79 \pm 1.27$, AutoFeat $80.76 \pm 1.17$, OpenFE $80.30 \pm 1.00$, CAAFE $80.99 \pm 1.00$, OcTree $80.79 \pm 1.15$, FEBP $80.85 \pm 1.29$, LLM-FE $80.22 \pm 0.96$, LLM-RANK $80.70 \pm 1.15$, SymboLLM-FE đạt cao nhất $81.27 \pm 1.31$.
    - Cmc ($\uparrow$ Accuracy): Baseline $57.85 \pm 0.89$, AutoFeat $57.85 \pm 0.32$, OpenFE $57.85 \pm 2.35$, CAAFE $57.78 \pm 1.28$, OcTree $57.85 \pm 1.52$, FEBP $57.93 \pm 0.48$, LLM-FE $57.29 \pm 2.20$, LLM-RANK $57.74 \pm 0.85$, SymboLLM-FE đạt cao nhất $57.97 \pm 0.73$.
    - Academic ($\uparrow$ Accuracy): Baseline $77.33 \pm 0.67$, AutoFeat $76.80 \pm 0.46$, OpenFE $76.42 \pm 0.61$, CAAFE $77.29 \pm 0.56$, OcTree $77.33 \pm 0.70$, FEBP $77.36 \pm 0.35$, LLM-FE $76.42 \pm 0.61$, LLM-RANK $77.25 \pm 0.19$, SymboLLM-FE đạt cao nhất $77.89 \pm 0.23$.
    - Ailerons ($\downarrow$ RMSE): Baseline $5.10 \pm 0.48$, AutoFeat $5.04 \pm 0.45$, OpenFE $5.26 \pm 0.49$, CAAFE $5.03 \pm 0.46$, OcTree $5.09 \pm 0.47$, FEBP $5.08 \pm 0.48$, LLM-FE $5.05 \pm 0.46$, LLM-RANK $5.10 \pm 0.48$, SymboLLM-FE đạt sai số thấp nhất $5.02 \pm 0.46$.
    - Tesla ($\downarrow$ RMSE): Baseline $2.39 \pm 0.09$, AutoFeat $2.38 \pm 0.00$, OpenFE $2.18 \pm 0.06$, CAAFE $2.66 \pm 0.09$, OcTree $2.43 \pm 0.10$, FEBP $2.41 \pm 0.08$, LLM-FE $2.39 \pm 0.09$, LLM-RANK $5.87 \pm 0.19$, SymboLLM-FE đạt sai số thấp nhất $2.16 \pm 0.06$.
  - Thực nghiệm mở rộng trên CatBoost, XGBoost và MLP trong Appendix E nhất quán chứng minh lợi thế hiệu năng ổn định của SymboLLM-FE trên nhiều kiến trúc mô hình khác nhau.
- **Đánh giá hiệu năng thực tế trên các cuộc thi Kaggle (Figure 3)**:
  - Đánh giá SymboLLM-FE trên bốn cuộc thi Kaggle (BNP, Obesity Risk, House Prices, Manufacturing) nhằm kiểm nghiệm hiệu năng trong thế giới thực.
  - SymboLLM-FE kết hợp TabPFN liên tục vượt trội hơn TabPFN gốc và OpenFE+TabPFN, đạt mức cải thiện điểm số trung bình là $2.5\,\text{pp}$.
  - **Hình 3.** So sánh điểm số trên các cuộc thi Kaggle
    - <img src="assets/fig_05_p7_vector.png" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - SymboLLM-FE+TabPFN vượt trội hơn TabPFN gốc (Baseline) và OpenFE+TabPFN trên cả 4 cuộc thi Kaggle.
    - **Từ đâu mà thấy được**
      - Điểm số thang đo BNP ($\uparrow$, Private/Public: $0.0, 0.1, 0.2, 0.3, 0.4, 0.5$), Obesity Risk ($\uparrow$, Private/Public: $0.0, 0.2, 0.4, 0.6, 0.8, 1.0$), House Prices ($\downarrow$, Public: $0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14$), Manufacturing ($\uparrow$, Private/Public: $0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7$).

### 5.3 Analysis of Generated Features

- **Mô thức sinh đặc trưng mới dựa trên hồi quy ký hiệu và LLM**:
  - SymboLLM-FE giới thiệu mô thức mới (như minh họa trong Figure 1) bằng cách kết hợp hồi quy ký hiệu (symbolic regression) song song cùng LLM và mô hình dự đoán xuôi dòng.
  - Thay vì phụ thuộc mù quáng vào các phép kết hợp toán học hoặc không gian ngữ nghĩa không định hướng, SymboLLM-FE tận dụng LLM như một động cơ tinh chỉnh (refinement engine) thay vì bộ sinh sơ cấp (primary generator).
- **Neo giữ thống kê và loại bỏ đặc trưng ảo giác**:
  - Việc neo đầu vào của LLM vào $\tau_i$ và tập công thức $P$ giúp gắn kết quá trình sinh đặc trưng vào thực tế thống kê (statistical reality).
  - Khung làm việc vòng khép kín giới hạn vai trò của LLM một cách chặt chẽ trong việc tối ưu hóa hiện thực mã nguồn và tích hợp logic quy nạp từ tri thức tiên nghiệm (prior knowledge).
  - Cơ chế này loại bỏ triệt để các đặc trưng ảo giác hoặc ngụy tạo (hallucinated or spurious features) thiếu cơ sở toán học, tạo ra các đặc trưng có khả năng diễn giải cao như điểm số nguy cơ triệu chứng có trọng số (weighted symptom scores, ví dụ `Infection_Exposure_Risk` trong Figure 1).
- **Cân bằng tối ưu giữa hiệu quả và năng lực dự đoán**:
  - Các ưu thế về hiệu quả của SymboLLM-FE được lượng hóa rõ ràng trong Table 1: đạt được sự cân bằng vượt trội giữa hiệu quả và năng lực dự đoán, đạt hiệu năng tổng thể cao nhất với điểm số mô hình là $80.02$.
  - SymboLLM-FE đạt hiệu năng đỉnh cao này trong khi chỉ sinh một tập đặc trưng tinh gọn gồm đúng $70$ đặc trưng.
  - Bằng cách giới hạn LLM ở vai trò tinh chỉnh, SymboLLM-FE cắt giảm mạnh không gian tìm kiếm và chi phí hội tụ, chỉ cần đúng $4$ lượt gọi API và kết thúc toàn bộ quy trình với chi phí thời gian vượt trội, thể hiện hiệu suất tính toán xuất sắc cùng tính diễn giải đặc trưng.

### 5.4 Generalization of SymboLLM-FE

- **Khả năng thích ứng trên các xương sống LLM khác nhau (Table 3)**:
  - Kết quả thực nghiệm trong Table 1 (và chi tiết trong Table 3) cho thấy sự thích ứng của SymboLLM-FE với các mô hình LLM nền tảng khác nhau:
    - CatBoost: GPT-4 đạt $75.41 \pm 0.51\%$, GPT-o1 đạt $78.21 \pm 0.20\%$, DeepSeek-R1 đạt $77.95 \pm 0.36\%$.
    - TabPFN: GPT-4 đạt $76.83 \pm 0.42\%$, GPT-o1 đạt $78.58 \pm 0.39\%$, DeepSeek-R1 đạt độ chính xác cao nhất là $79.49 \pm 0.57\%$.
  - Cả GPT-o1 và DeepSeek-R1 đều vượt trội đáng kể so với GPT-4 về độ chính xác phân loại trên cả CatBoost và TabPFN.
- **Mối tương quan với năng lực suy luận của LLM**:
  - Tính hiệu quả của SymboLLM-FE gắn liền chặt chẽ với năng lực suy luận (reasoning capability) của LLM.
  - Việc áp dụng các mô hình LLM mạnh hơn có thể nâng cao hơn nữa hiệu quả của quy trình kỹ thuật đặc trưng tự động.

### 5.5 Estimation of Running Costs for SymboLLM-FE

- **Khả năng mở rộng tính toán từ số mũ xuống đa thức**:
  - Phân tích hiệu quả toàn diện xác thực khả năng mở rộng tính toán của SymboLLM-FE: chiến lược cửa sổ mở rộng - trượt định hướng bởi tương quan Spearman thu hẹp hiệu quả không gian tìm kiếm đặc trưng từ độ phức tạp hàm mũ $\mathcal{O}(2^n)$ xuống độ phức tạp đa thức $\mathcal{O}(n^2)$.
- **Chi phí vận hành thực tế tuân thủ biên số học (Table 4)**:
  - Table 4 xác nhận số lượng công thức ứng viên tuân thủ nghiêm ngặt các biên số học đã dẫn xuất, làm cho thời gian chạy cục bộ tỷ lệ tuyến tính với số công thức và kích thước tập dữ liệu trong giai đoạn hồi quy ký hiệu đầu tiên:
    - Credit-g: $66$ công thức SR, thời gian SR $4.23\,\text{mins}$, $3$ lần gọi LLM, $2331$ token mỗi lần gọi.
    - Spaceship: $36$ công thức SR, thời gian SR $2.01\,\text{mins}$, $4$ lần gọi LLM, $1201$ token mỗi lần gọi.
    - Cmc: $21$ công thức SR, thời gian SR $0.89\,\text{mins}$, $3$ lần gọi LLM, $1159$ token mỗi lần gọi.
    - Academic: $190$ công thức SR, thời gian SR $25.34\,\text{mins}$, $4$ lần gọi LLM, $3587$ token mỗi lần gọi.
    - Ailerons: $171$ công thức SR, thời gian SR $30.24\,\text{mins}$, $5$ lần gọi LLM, $3250$ token mỗi lần gọi.
    - Tesla: $15$ công thức SR, thời gian SR $2.54\,\text{mins}$, $2$ lần gọi LLM, $1147$ token mỗi lần gọi.
- **Cơ chế tinh chỉnh LLM và tách rời chi phí token**:
  - Cơ chế tinh chỉnh LLM ở giai đoạn hai hoạt động như một bộ lọc ngữ nghĩa thay vì bộ sinh tự do, duy trì xấp xỉ $4$ lần gọi API trên mọi tác vụ bất kể số chiều dữ liệu.
  - Tổng lượng token tiêu thụ được tách rời hoàn toàn khỏi kích thước mẫu dữ liệu, chỉ tỷ lệ thuận với ngữ cảnh tác vụ và dung lượng kho công thức.
  - Kiến trúc tinh giản này giúp SymboLLM-FE vượt trội đáng kể so với các phương pháp AutoFE dựa trên LLM hiện có, chẳng hạn như FEBP ($43.71\,\text{mins}$ trong Zou et al., 2026), về cả hiệu quả tính toán lẫn tính kinh tế chi phí.

### 5.6 Ablation Study

- **Thiết lập nghiên cứu cắt bỏ**:
  - Tiến hành nghiên cứu cắt bỏ toàn diện trên nhiều tập dữ liệu với các hạt ngẫu nhiên độc lập nhằm định lượng đóng góp của từng thành phần và khẳng định tính cần thiết của chúng.
  - Đánh giá các biến thể mô hình bằng cách loại bỏ có hệ thống các mô-đun then chốt: tiền sắp xếp đặc trưng theo Spearman (SP.), cơ chế cửa sổ mở rộng - trượt (ES.), và sinh đặc trưng định hướng bởi LLM (LLM).
- **Đóng góp của từng thành phần đến độ chính xác (Figure 4)**:
  - Kết quả trên Figure 4 chứng minh mọi thành phần đều đóng vai trò thiết yếu để đạt hiệu năng tối ưu:
    - Baseline (mô hình gốc): $75.81\%$
    - w/o SP. (loại bỏ tiền sắp xếp Spearman): $76.07\%$
    - w/o ES. (loại bỏ cửa sổ mở rộng - trượt): $75.92\%$
    - w/o LLM (loại bỏ tinh chỉnh LLM): $76.84\%$
    - Ours (khung làm việc hoàn chỉnh SymboLLM-FE): $77.16\%$
  - **Hình 4.** Nghiên cứu cắt bỏ (Ablation study) của SymboLLM-FE
    - <img src="assets/fig_06_p9_vector.png" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Mọi thành phần (SP., ES., LLM) đều không thể thiếu để đạt độ chính xác tối ưu $77.16\%$ so với baseline $75.81\%$.
    - **Từ đâu mà thấy được**
      - Biểu đồ cột biểu diễn Accuracy (%) với các mốc trục tung $75.0, 75.5, 76.0, 76.5, 77.0, 77.5, 78.0$, các cột giá trị tương ứng: Baseline (75.81), w/o SP. (76.07), w/o ES. (75.92), w/o LLM (76.84), Ours (77.16).
- **Phân tích vai trò chuyên sâu của từng mô-đun**:
  - Việc loại bỏ tiền sắp xếp Spearman (SP.) gây suy giảm nhẹ hiệu năng, chứng minh việc ưu tiên đặc trưng theo tương quan mục tiêu cung cấp không gian tìm kiếm hiệu quả hơn cho hồi quy ký hiệu so với lấy mẫu ngẫu nhiên.
  - Việc thiếu vắng cơ chế cửa sổ mở rộng - trượt (ES.) khiến hiệu năng sụt giảm nghiêm trọng (xuống $75.92\%$), chứng tỏ cơ chế có cấu trúc này mang tính quyết định để nắm bắt các tương tác đặc trưng bậc cao mà lấy mẫu ngẫu nhiên bỏ lỡ, khẳng định tính đúng đắn của chiến lược giảm độ phức tạp mà không làm giảm chất lượng đặc trưng.
  - Một khoảng cách sụt giảm đáng kể khác diễn ra khi loại bỏ tinh chỉnh LLM (w/o LLM, đạt $76.84\%$), xác nhận các quy tắc ký hiệu thô thường mắc phải sự dư thừa hoặc cài đặt dưới mức tối ưu, trong khi LLM đóng vai trò bộ tích hợp ngữ nghĩa trọng yếu giúp tối ưu hóa hiệu quả mã lệnh và kết hợp các quy tắc để tăng cường khả năng tổng quát hóa.
