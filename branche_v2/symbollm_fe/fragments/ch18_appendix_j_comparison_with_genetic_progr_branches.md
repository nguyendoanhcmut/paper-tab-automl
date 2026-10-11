## Appendix J Comparison with Genetic Programming Methods

* Thiết lập so sánh hiệu năng giữa SymboLLM-FE và các phương pháp quy hoạch di truyền (Genetic Programming - GP):
  * SymboLLM-FE được so sánh đối chuẩn trực tiếp với 5 biến thể Genetic Programming tiên tiến nhất (state-of-the-art GP variants): Baseline (GP cơ sở), Shapley-GP (Chen et al., 2017), LAS-GP (Zhang et al., 2025), SAM-GP (Bakurov et al., 2024), và Modular-MTGP (Zhang et al., 2023a).
  * Đánh giá so sánh hiệu năng toàn diện được thực hiện trên 6 tập dữ liệu đa dạng (six diverse datasets).
  * Quy ước thước đo đánh giá theo từng loại tác vụ:
    * Đối với các tác vụ phân loại (classification tasks) gồm Credit-g, Spaceship, Cmc, và Academic: báo cáo độ chính xác Accuracy ($\%$).
    * Đối với các tác vụ hồi quy (regression tasks) gồm Ailerons và Tesla: báo cáo sai số căn bậc hai trung bình RMSE (Root Mean Squared Error).
  * Bảng 15 trình bày chi tiết kết quả so sánh hiệu năng giữa SymboLLM-FE và các biến thể GP:
    | Dataset | Metric | Baseline | Shapley-GP<br>(Chen et al., 2017) | LAS-GP<br>(Zhang et al., 2025) | SAM-GP<br>(Bakurov et al., 2024) | Modular-MTGP<br>(Zhang et al., 2023a) | SymboLLM-FE |
    | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | **Credit-g** | Acc ↑ | $77.03$ | $77.28$ | $69.35$ | $77.20$ | $77.15$ | $77.00$ |
    | **Spaceship** | Acc ↑ | $80.79$ | $81.05$ | $81.12$ | $80.95$ | $80.88$ | $\mathbf{81.27}$ |
    | **Cmc** | Acc ↑ | $57.85$ | $57.92$ | $57.91$ | $57.08$ | $57.82$ | $\mathbf{57.97}$ |
    | **Academic** | Acc ↑ | $77.33$ | $77.65$ | $77.72$ | $77.55$ | $77.12$ | $\mathbf{77.89}$ |
    | **Ailerons** | RMSE ↓ | $5.10$ | $5.06$ | $5.04$ | $5.07$ | $5.08$ | $\mathbf{5.02}$ |
    | **Tesla** | RMSE ↓ | $2.39$ | $2.30$ | $2.28$ | $2.34$ | $2.36$ | $\mathbf{2.16}$ |

* Phân tích hiệu năng vượt trội và tính cạnh tranh của SymboLLM-FE:
  * SymboLLM-FE thể hiện hiệu năng tổng thể vượt trội (superior overall performance), vượt qua toàn bộ các biến thể Genetic Programming được so sánh trên đại đa số các tập dữ liệu.
  * Phương pháp ghi nhận mức tăng trưởng đặc biệt lớn trong các tác vụ hồi quy (significant gains in regression tasks):
    * Trên tập Ailerons, SymboLLM-FE đạt $\text{RMSE} = 5.02$, hạ thấp sai số so với LAS-GP ($5.04$), Shapley-GP ($5.06$), SAM-GP ($5.07$), Modular-MTGP ($5.08$), và Baseline ($5.10$).
    * Trên tập Tesla, SymboLLM-FE tạo ra bước nhảy vọt với $\text{RMSE} = 2.16$, giảm sâu so với LAS-GP ($2.28$), Shapley-GP ($2.30$), SAM-GP ($2.34$), Modular-MTGP ($2.36$), và Baseline ($2.39$).
  * Phương pháp chiếm lĩnh vị trí dẫn đầu trong hầu hết các điểm chuẩn phân loại (top rankings in most classification benchmarks):
    * Đạt thứ hạng cao nhất trên Spaceship ($81.27\%$), Cmc ($57.97\%$), và Academic ($77.89\%$).
    * Duy trì tính cạnh tranh cao ngay cả trong trường hợp duy nhất mà một biến thể GP giữ lợi thế dẫn trước nhỏ (marginal lead) là Credit-g ($77.00\%$ so với Shapley-GP đạt $77.28\%$).

* Tính ổn định, độ bền vững và các ưu thế kiến trúc của SymboLLM-FE:
  * SymboLLM-FE thể hiện độ ổn định (stability) và độ bền vững (robustness) cao hơn trên các phân phối dữ liệu đa dạng.
  * Phương pháp tránh được hiện tượng biến động hiệu năng thất thường (performance volatility) vốn thường xuyên xảy ra ở các phương pháp tìm kiếm tiến hóa (evolutionary search methods) (điển hình như LAS-GP bị sụt giảm hiệu năng mạnh xuống $69.35\%$ trên Credit-g).
  * Các kết quả thực nghiệm khẳng định SymboLLM-FE không chỉ tương đương mà thường xuyên vượt trội năng lực dự đoán của các phương pháp GP truyền thống lẫn tiên tiến.
  * SymboLLM-FE mang lại các lợi thế bổ sung mang tính quyết định bao gồm sự điều hướng ngữ nghĩa do LLM dẫn dắt (LLM-driven semantic guidance) và tốc độ hội tụ nhanh hơn (faster convergence).
