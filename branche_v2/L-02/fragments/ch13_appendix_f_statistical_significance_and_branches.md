## Appendix F: Statistical Significance and Stability Analysis of Ablation Study

* **Khung thực nghiệm và quy trình định lượng độ ổn định (Experimental framework and stability quantification):**
  * Nhằm đảm bảo tính vững chắc (robustness) và tính hợp lệ về mặt thống kê (statistical validity) của nghiên cứu cắt bỏ (ablation study), các thí nghiệm được tiến hành trong khuôn khổ kiểm định chéo (cross-validation framework) trên nhiều hạt giống ngẫu nhiên độc lập (multiple independent random seeds).
  * Báo cáo hiệu năng trung bình (mean performance) cùng với độ lệch chuẩn (standard deviation - $\text{Std}$) để định lượng độ ổn định (quantify stability) qua các lần chạy lặp lại.
  * Hiệu năng vượt trội và tính nhất quán của mô hình hoàn chỉnh (SymboLLM-FE - `Ours`):
    * Đạt độ chính xác trung bình (accuracy) cao nhất: $77.16\%$.
    * Đạt độ lệch chuẩn thấp nhất: $\pm 0.34$, phản ánh mức độ phân tán kết quả hẹp nhất giữa các lần chạy hạt giống độc lập.
    * Thể hiện tính nhất quán vượt trội (superior consistency) so với toàn bộ các biến thể cắt bỏ (ablated variants).

* **Tác động của từng thành phần lên độ ổn định và vai trò bộ lọc ngữ nghĩa của LLM (Component impact on stability & LLM semantic filter):**
  * Mức độ biến động cao ở các biến thể khuyết thiếu thành phần tối ưu hóa cấu trúc:
    * Biến thể thiếu bước sắp xếp đặc trưng theo tương quan Spearman (`w/o SP`): Độ chính xác giảm xuống $76.07\%$ và độ lệch chuẩn tăng lên $\pm 0.51$.
    * Biến thể thiếu cơ chế cửa sổ trượt mở rộng (`w/o ES`): Hiển thị mức độ biến động cao nhất với độ lệch chuẩn $\pm 0.58$ và độ chính xác chỉ đạt $75.92\%$.
    * Biến thể đường cơ sở ban đầu (`Baseline`): Đạt độ chính xác $75.81\%$ với độ lệch chuẩn $\pm 0.45$.
    * Biến thể loại bỏ mô hình ngôn ngữ lớn (`w/o LLM`): Đạt độ chính xác $76.84\%$ với độ lệch chuẩn $\pm 0.41$.
  * Vai trò bộ lọc ngữ nghĩa ổn định của LLM (LLM as a stable semantic filter):
    * Việc thiếu vắng các câu lệnh nhắc có cấu trúc (structured prompting) hoặc thuật toán tìm kiếm tiến hóa (evolutionary search) khiến phương sai (variance) tăng cao rõ rệt.
    * Điều này chỉ ra rằng sự tích hợp của mô hình ngôn ngữ lớn (LLMs) đóng vai trò như một bộ lọc ngữ nghĩa ổn định (stable semantic filter), giúp giảm thiểu hiệu quả sự biến động hiệu năng (reducing performance fluctuation).
    * Cơ chế này làm suy giảm đáng kể tính bất ổn định và dao động (volatility) thường xảy ra trong các quy trình tối ưu hóa ngẫu nhiên (stochastic optimization processes).

* **Kiểm định ý nghĩa thống kê và phân tích khoảng tin cậy (Statistical significance testing and confidence intervals):**
  * Phương pháp kiểm định thống kê:
    * Thực hiện các kiểm định t bắt cặp (paired t-tests) giữa SymboLLM-FE và từng biến thể cắt bỏ nhằm đánh giá nghiêm ngặt ý nghĩa thống kê của mức độ chênh lệch hiệu năng.
    * Đánh giá tính ổn định và sự khác biệt phân phối qua các phép kiểm định thống kê lặp lại (như Wilcoxon signed-rank tests) trên các hạt giống ngẫu nhiên lặp lại.
  * Mức ý nghĩa thống kê ($p$-values):
    * Kết quả xác nhận SymboLLM-FE vượt trội có ý nghĩa thống kê so với toàn bộ các đường cơ sở và biến thể cắt bỏ, với các giá trị $p$-value nằm sâu dưới ngưỡng ý nghĩa $\alpha = 0.05$:
      * So với `Baseline`: $p < 0.001$, khác biệt đạt ý nghĩa thống kê (Significant: Yes).
      * So với `w/o SP`: $p < 0.001$, khác biệt đạt ý nghĩa thống kê (Significant: Yes).
      * So với `w/o ES`: $p < 0.001$, khác biệt đạt ý nghĩa thống kê (Significant: Yes).
      * So với biến thể cắt bỏ mạnh nhất (`w/o LLM`): Mức cải thiện vẫn đạt ý nghĩa thống kê rõ nét với $p = 0.0142 < 0.05$ (Significant: Yes).
  * Phân tích khoảng tin cậy 95% (95% Confidence Intervals - CI):
    * Khoảng tin cậy $95\%$ của các mô hình:
      * `Ours` (SymboLLM-FE): $[76.49, 77.83]$.
      * `Baseline`: $[74.93, 76.69]$.
      * `w/o SP`: $[75.07, 77.07]$.
      * `w/o ES`: $[74.78, 77.06]$.
      * `w/o LLM`: $[76.03, 77.65]$.
    * Sự chồng lấn tối thiểu (minimal overlap) giữa khoảng tin cậy của SymboLLM-FE và các biến thể cắt bỏ, đặc biệt là các biến thể thiếu các thành phần then chốt (`Baseline`, `w/o ES`, `w/o SP`), củng cố tính vững chắc của kết luận.
  * Xác thực tính tất yếu của từng thành phần (Validation of component necessity):
    * Các kết quả này không chỉ xác thực tính tất yếu của từng thành phần (necessity of each component) gồm SP, ES và LLM, mà còn khẳng định phương pháp đề xuất nâng cao đồng thời cả năng lực dự đoán (predictive performance) lẫn độ ổn định của quá trình sinh đặc trưng (feature generation stability).

* **Phân tích định lượng thống kê từ Bảng 13 (Statistical analysis of ablation study results):**
  * **Bảng 13.** Phân tích thống kê kết quả nghiên cứu cắt bỏ ablation study
    * <img src="assets/table_13_p22.png" alt="Bảng 13" />
    * **Bảng này chứng minh điều gì**
      * Mức suy giảm hiệu năng có ý nghĩa thống kê khi loại bỏ từng thành phần SP, ES, LLM
    * **Từ đâu mà thấy được**
      * Các giá trị p-value và khoảng tin cậy CI của độ lệch hiệu năng trong bảng
  * Tổng hợp chi tiết các chỉ số thống kê từ Bảng 13:
    * `Baseline`: Accuracy $= 75.81\%$, $\text{Std} = \pm 0.45$, $95\%\text{ CI} = [74.93, 76.69]$, $p\text{-value (vs. Ours)} < 0.001$, Đạt ý nghĩa thống kê (Significant: Yes).
    * `w/o SP` (Loại bỏ tiền sắp xếp đặc trưng theo tương quan Spearman): Accuracy $= 76.07\%$, $\text{Std} = \pm 0.51$, $95\%\text{ CI} = [75.07, 77.07]$, $p\text{-value (vs. Ours)} < 0.001$, Đạt ý nghĩa thống kê (Significant: Yes).
    * `w/o ES` (Loại bỏ phương pháp cửa sổ trượt mở rộng): Accuracy $= 75.92\%$, $\text{Std} = \pm 0.58$, $95\%\text{ CI} = [74.78, 77.06]$, $p\text{-value (vs. Ours)} < 0.001$, Đạt ý nghĩa thống kê (Significant: Yes).
    * `w/o LLM` (Loại bỏ sinh đặc trưng dựa trên LLM): Accuracy $= 76.84\%$, $\text{Std} = \pm 0.41$, $95\%\text{ CI} = [76.03, 77.65]$, $p\text{-value (vs. Ours)} = 0.0142$, Đạt ý nghĩa thống kê (Significant: Yes).
    * `Ours` (SymboLLM-FE đầy đủ thành phần): Accuracy $= 77.16\%$, $\text{Std} = \pm 0.34$, $95\%\text{ CI} = [76.49, 77.83]$, $p\text{-value (vs. Ours)} = -$, Chuẩn đối sánh chính (Significant: $-$).
