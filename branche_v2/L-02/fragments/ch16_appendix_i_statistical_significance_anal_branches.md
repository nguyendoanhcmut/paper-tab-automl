## Appendix I: Statistical Significance Analysis

* **Mục tiêu và phương pháp kiểm định thống kê (Statistical testing objective and methodology)**:
  * Đánh giá nghiêm ngặt xem các cải thiện hiệu năng của SymboLLM-FE so với các baseline SOTA (state-of-the-art) mạnh nhất có thực sự mang ý nghĩa thống kê hay chỉ xuất phát từ biến thiên hạt giống ngẫu nhiên (random seed variations).
  * Sử dụng kiểm định tổng hạng Wilcoxon (Wilcoxon Signed-Rank Test) trên các phân phối kết quả thực nghiệm độc lập.

* **Tổng hợp kết quả phân tích ý nghĩa thống kê (Statistical significance analysis across datasets)**:
  * Bảng 14 tổng hợp giá trị $p$ trung vị (median $p$-values) và khoảng tin cậy $95\%$ (95% Confidence Interval - CI) của độ chênh lệch giá trị trung bình giữa SymboLLM-FE và baseline mạnh nhất: $(\text{SymboLLM-FE} - \text{Best Baseline})$.
  * Tiêu chí đánh giá ý nghĩa thống kê: Một kết quả được xác định là có ý nghĩa thống kê (Significant?) khi giá trị trung vị $\text{median } p < 0.05$.
  * Tỷ lệ thành công: SymboLLM-FE đạt mức cải thiện có ý nghĩa thống kê ($p < 0.05$) so với các baseline mạnh nhất trên $4$ trên $6$ tập dữ liệu thế giới thực ($4/6$ real-world datasets).
  * **Bảng 14.** Kiểm định ý nghĩa thống kê Wilcoxon của SymboLLM-FE so với Baseline tốt nhất
    * <img src="assets/table_14_p24.png" alt="Bảng 14" />
    * **Bảng này chứng minh điều gì**
      * Sự cải thiện của SymboLLM-FE đạt $p < 0.05$ và khoảng tin cậy 95% khẳng định tính ưu việt
    * **Từ đâu mà thấy được**
      * Cột p-value, Significant? (Yes) và khoảng tin cậy CI 95% của độ chênh lệch hiệu năng

* **Chi tiết kiểm định thống kê theo từng tập dữ liệu (Dataset-specific statistical validation)**:
  * **Tập dữ liệu Academic (Phân loại đa lớp phức tạp - Complex multi-class classification)**:
    * Hiệu năng: SymboLLM-FE đạt độ chính xác (Accuracy) $77.89 \pm 0.23\%$, vượt trội so với baseline tốt nhất là FEBP ($77.36\%$).
    * Mức ý nghĩa thống kê: Cải thiện đạt mức ý nghĩa cực kỳ cao với median $p = 0.0001$ ($p < 0.001$), đánh dấu kết quả có ý nghĩa thống kê vững chắc (Significant: Yes).
    * Khoảng tin cậy: $\text{95\% CI} = [0.32, 0.74]$ (toàn bộ nằm ở miền dương).
    * Ý nghĩa: Minh chứng cho tính vững chắc (robustness) vượt trội của SymboLLM-FE trong việc trích xuất và biến đổi đặc trưng cho các tác vụ phân loại đa lớp phức tạp.
  * **Tập dữ liệu Spaceship (Phân loại nhị phân)**:
    * Hiệu năng: SymboLLM-FE đạt độ chính xác $81.27 \pm 1.31\%$, vượt qua baseline CAAFE ($80.99\%$).
    * Mức ý nghĩa thống kê: Median $p = 0.0125 < 0.05$ (Significant: Yes).
    * Khoảng tin cậy: $\text{95\% CI} = [0.08, 0.48]$.
  * **Tập dữ liệu Cmc (Phân loại đa lớp)**:
    * Hiệu năng: SymboLLM-FE đạt độ chính xác $57.97 \pm 0.73\%$, vượt qua baseline FEBP ($57.93\%$).
    * Mức ý nghĩa thống kê: Median $p = 0.0312 < 0.05$ (Significant: Yes).
    * Khoảng tin cậy: $\text{95\% CI} = [0.01, 0.07]$.
  * **Tập dữ liệu Tesla (Hồi quy - Regression RMSE)**:
    * Hiệu năng: SymboLLM-FE đạt sai số RMSE là $2.16 \pm 0.06$, cải thiện so với baseline tốt nhất là OpenFE ($2.18$) (với metric RMSE, giá trị thấp hơn thể hiện chất lượng tốt hơn).
    * Mức ý nghĩa thống kê: Median $p = 0.0275 < 0.05$ (Significant: Yes).
    * Khoảng tin cậy: $\text{95\% CI} = [-0.038, -0.002]$ (khoảng chênh lệch hoàn toàn âm, biểu thị sự sụt giảm sai số nhất quán).
    * Cơ chế thống kê: Mặc dù mức tăng điểm trung bình có phần khiêm tốn (modest mean performance gains), nhưng phương sai cực thấp (low variance) kết hợp với chiều hướng cải thiện nhất quán (consistent improvement direction) mang lại kết quả có ý nghĩa thống kê cao, xác nhận mức cải thiện này không phải do yếu tố ngẫu nhiên (not due to chance).
  * **Các tập dữ liệu không đạt ngưỡng ý nghĩa thống kê ($p \ge 0.05$)**:
    * **Credit-g (Phân loại)**:
      * SymboLLM-FE đạt $77.00 \pm 1.63\%$ so với CAAFE đạt $78.00\%$.
      * Median $p = 0.2248 \ge 0.05$; $\text{95\% CI} = [-2.65, 0.65]$ (Significant: No).
    * **Ailerons (Hồi quy RMSE)**:
      * SymboLLM-FE đạt RMSE $5.02 \pm 0.46$ so với CAAFE đạt $5.03$.
      * Median $p = 0.9504 \ge 0.05$; $\text{95\% CI} = [-0.43, 0.41]$ (Significant: No).
    * Đặc tính vận hành: Dù không đạt ngưỡng có ý nghĩa thống kê trên hai tập dữ liệu này, SymboLLM-FE vẫn duy trì hiệu năng mang tính cạnh tranh cao (competitive performance) đi kèm mức phương sai thấp (low variance).

* **Kết luận về tính ổn định và độ tin cậy (Validation of stability and reliability)**:
  * Toàn bộ các kết quả kiểm định thống kê khẳng định tính ổn định (stability) và độ tin cậy (reliability) của năng lực kỹ thuật đặc trưng (feature engineering capabilities) từ SymboLLM-FE qua nhiều loại hình bài toán đa dạng.
