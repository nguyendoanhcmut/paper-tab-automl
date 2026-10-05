## Appendix I Statistical Significance Analysis

* Đánh giá nghiêm ngặt ý nghĩa thống kê (statistical significance): Nhóm tác giả thực hiện phân tích thống kê bằng kiểm định xếp hạng có dấu Wilcoxon (Wilcoxon Signed-Rank Test) nhằm xác định mức cải thiện hiệu năng của SymboLLM-FE so với các baseline tiên tiến (state-of-the-art baselines) có ý nghĩa thống kê thực sự hay chỉ xuất phát từ biến thiên do hạt giống ngẫu nhiên (random seed variations).
* Tóm tắt kiểm định và khoảng tin cậy: Bảng 14 (Table 14) tóm tắt các giá trị $p$ trung vị (median $p$-values) và khoảng tin cậy 95% (95% Confidence Intervals - CI) của hiệu số trung bình ($\text{SymboLLM-FE} - \text{Best Baseline}$):
  * SymboLLM-FE đạt được mức cải thiện có ý nghĩa thống kê ($p < 0.05$) so với các baseline mạnh nhất trên 4 trong số 6 tập dữ liệu thực tế (real-world datasets).

| Dataset | SymboLLM-FE (Mean $\pm$ Std) | Best Baseline (Method & Mean) | Med. P-Value | 95% CI | Significant? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Credit-g | $77.00 \pm 1.63$ | CAAFE ($78.00$) | $0.2248$ | $[-2.65, 0.65]$ | No |
| Spaceship | $81.27 \pm 1.31$ | CAAFE ($80.99$) | $0.0125$ | $[0.08, 0.48]$ | Yes |
| Cmc | $57.97 \pm 0.73$ | FEBP ($57.93$) | $0.0312$ | $[0.01, 0.07]$ | Yes |
| Academic | $77.89 \pm 0.23$ | FEBP ($77.36$) | $0.0001$ | $[0.32, 0.74]$ | Yes |
| Ailerons | $5.02 \pm 0.46$ | CAAFE ($5.03$) | $0.9504$ | $[-0.43, 0.41]$ | No |
| Tesla | $2.16 \pm 0.06$ | OpenFE ($2.18$) | $0.0275$ | $[-0.038, -0.002]$ | Yes |

*Bảng 14: Phân tích ý nghĩa thống kê của SymboLLM-FE so với các baseline tốt nhất (Best Baselines). Cột "Significant?" biểu thị liệu giá trị trung vị $p < 0.05$ hay không. CI đại diện cho Khoảng tin cậy 95% (95% Confidence Interval) của sai khác trung bình ($\text{SymboLLM-FE} - \text{Best Baseline}$).*

* Kết quả trên tập dữ liệu Academic: Mức cải thiện đạt mức rất có ý nghĩa thống kê ($p < 0.001$, với giá trị $p$ trung vị là $0.0001$ và CI 95% là $[0.32, 0.74]$), chứng minh tính mạnh mẽ (robustness) của phương pháp trong các tác vụ phân loại đa lớp (multi-class classification) phức tạp.
* Kết quả trên Credit-g và Ailerons: Mặc dù kết quả trên Credit-g ($p = 0.2248$, CI 95%: $[-2.65, 0.65]$) và Ailerons ($p = 0.9504$, CI 95%: $[-0.43, 0.41]$) không đạt ngưỡng ý nghĩa thống kê ($p \ge 0.05$), SymboLLM-FE vẫn thể hiện hiệu năng cạnh tranh (competitive performance) với phương sai thấp (low variance).
* Kết quả trên tập dữ liệu Tesla: Ngược lại, đối với các tập dữ liệu như Tesla, dù mức tăng hiệu năng trung bình ở mức khiêm tốn (modest mean performance gains), phương sai thấp kết hợp với hướng cải thiện nhất quán mang lại kết quả có ý nghĩa thống kê ($p = 0.0275 < 0.05$, CI 95%: $[-0.038, -0.002]$), khẳng định các cải thiện cụ thể này không phải do ngẫu nhiên (not due to chance).
* Tính ổn định và tin cậy tổng thể: Các phát hiện này cùng nhau xác thực tính ổn định (stability) và độ tin cậy (reliability) trong năng lực kỹ thuật đặc trưng (feature engineering capabilities) của SymboLLM-FE trên đa dạng các loại tác vụ khác nhau.
