### 5.1 Main Results

- **Giao thức đánh giá thống nhất (Unified evaluation protocol)**: Bảng 1 (Table 1) và Bảng 2 (Table 2) lần lượt báo cáo độ chính xác phân loại (`classification accuracy`, $\uparrow$) và căn bậc hai sai số toàn phương trung bình hồi quy (`regression RMSE`, $\downarrow$) trên tất cả các tập dữ liệu và phương pháp theo một giao thức chuẩn hóa thống nhất.
  - Tất cả các phương pháp đều được kết hợp với cùng một bộ học cơ sở XGBoost (`XGBoost learner`).
  - Tất cả các phương pháp tiếp cận dựa trên mô hình ngôn ngữ lớn (`LLM-based approaches`) đều sử dụng chung một backbone đại diện duy nhất là Qwen3-8B.
  - Kết quả thực nghiệm được ghi nhận dưới dạng giá trị trung bình kèm độ lệch chuẩn ($\text{mean} \pm \text{std}$) qua $5$ lần phân chia dữ liệu ngẫu nhiên ($5\text{ splits}$).
  - Cột cơ sở (`Base`) thể hiện hiệu năng của mô hình XGBoost khi không sử dụng bất kỳ phương pháp kỹ nghệ đặc trưng tự động nào (`w/o FE`).
  - Nhóm các phương pháp so sánh đối chuẩn bao gồm:
    - *AutoFE cổ điển (`Classical AutoFE`)*: AutoFeat và OpenFE.
    - *AutoFE dựa trên LLM (`LLM-based FE`)*: CAAFE, FeatLLM và OCTree.
    - *AutoFE kết hợp LLM và giải thuật tiến hóa (`LLM+Evolutionary FE`)*: LLMFE.
    - *Phương pháp đề xuất*: TOPOFE.

#### Classification

- **Hiệu năng tổng thể vượt trội của TOPOFE trên bài toán phân loại (Overall classification performance)**: TOPOFE đạt hiệu năng tốt nhất trên $15/19$ tập dữ liệu thực nghiệm, đồng thời duy trì phương sai ổn định, có tính cạnh tranh cao và thường xuyên thấp hơn giữa các lần chạy.
  - Kết quả này chứng minh khả năng đạt trạng thái cân bằng thuận lợi giữa hiệu năng dự báo (`predictive performance`) và độ ổn định của quá trình tìm kiếm (`search stability`).
- **Mức cải thiện mở rộng một cách có hệ thống theo độ phức tạp của tập dữ liệu (Gains scale systematically with dataset complexity)**:
  - *Tập dữ liệu ít chiều, gần bão hòa (`near-saturated, low-dimensional datasets`)*: Trên các tập dữ liệu như `adult` ($n_{\text{inst}} = 48842, n_{\text{feat}} = 14$) và `tic-tac-toe` ($n_{\text{inst}} = 958, n_{\text{feat}} = 9$):
    - Các phương pháp cổ điển vẫn giữ được tính cạnh tranh cao: OpenFE đạt $0.9267 \pm 0.0013$ trên `adult` và dẫn đầu trên `tic-tac-toe` với $0.9999 \pm 0.0001$.
    - Biên độ vượt trội của TOPOFE ở mức cận biên/nhỏ: trên `adult` đạt $0.9268 \pm 0.0025$ (vượt nhẹ so với AutoFeat $0.9265 \pm 0.0011$ và Base $0.8611 \pm 0.0165$); trên `tic-tac-toe` xếp thứ hai với $0.9993 \pm 0.0220$.
    - Điều này xác nhận rằng việc tìm kiếm cấu trúc đa họ (`structured multi-family search`) không gây ra chi phí phụ trội (`overhead`) không cần thiết khi quá trình liệt kê đơn thuần (`enumeration`) đã đủ để bao quát không gian giải pháp.
  - *Tập dữ liệu độ phức tạp trung bình đòi hỏi tương tác hợp thành (`medium-complexity datasets requiring compositional interactions`)*:
    - Mức tăng hiệu năng trở nên đáng kể trên các tập dữ liệu yêu cầu các phép kết hợp tương tác phức tạp như `heart` ($n_{\text{inst}} = 918, n_{\text{feat}} = 11$), `balance-scale` ($n_{\text{inst}} = 625, n_{\text{feat}} = 4$), `credit-g` ($n_{\text{inst}} = 1000, n_{\text{feat}} = 20$), và `eucalyptus` ($n_{\text{inst}} = 736, n_{\text{feat}} = 19$).
    - TOPOFE vượt trội đáng kể so với phương pháp tốt thứ hai nhờ cơ chế chuyển giao liên họ được kích hoạt theo độ bão hòa (`saturation-triggered cross-family transfer`), giúp phát hiện ra các đặc trưng tương tác mà không một ngữ pháp đơn họ (`single-family grammar`) nào có thể tự trích xuất được:
      - Trên `heart`: TOPOFE đạt $0.9346 \pm 0.0015$ (tốt nhất), vượt xa OpenFE ($0.9199 \pm 0.0043$), AutoFeat ($0.8923 \pm 0.0012$), Base ($0.8696 \pm 0.0190$).
      - Trên `balance-scale`: TOPOFE đạt $0.9465 \pm 0.0046$ (tốt nhất), vượt trội so với AutoFeat ($0.8848 \pm 0.0079$), LLMFE ($0.8780 \pm 0.0093$), OpenFE ($0.8560 \pm 0.0036$), Base ($0.8320 \pm 0.0233$).
      - Trên `credit-g`: TOPOFE đạt $0.7878 \pm 0.0066$ (tốt nhất), vượt OpenFE ($0.7725 \pm 0.0221$), AutoFeat ($0.7629 \pm 0.0019$), Base ($0.7000 \pm 0.0237$).
      - Trên `eucalyptus`: TOPOFE đạt $0.6990 \pm 0.0094$ (tốt nhất), vượt OpenFE ($0.6766 \pm 0.0180$), AutoFeat ($0.6643 \pm 0.0213$), Base ($0.6724 \pm 0.0151$).
  - *Tập dữ liệu quy mô lớn (`large-scale datasets`)*:
    - Trên `diabetes` ($n_{\text{inst}} = 253680, n_{\text{feat}} = 21$): TOPOFE đạt hiệu năng cao nhất với độ chính xác $0.8524 \pm 0.0021$, trong khi phương pháp LLM-FE sụp đổ (`collapses`) xuống $0.8298 \pm 0.0054$ (thậm chí suy giảm sâu dưới mức Base $0.8491 \pm 0.0068$).
    - Trên `covtype` ($n_{\text{inst}} = 581012, n_{\text{feat}} = 54$): TOPOFE đạt độ chính xác dẫn đầu với $0.8774 \pm 0.0038$, vượt LLMFE ($0.8773 \pm 0.0087$), OpenFE ($0.8684 \pm 0.0006$), Base ($0.8652 \pm 0.0120$).
- **Khoảng cách hiệu năng với LLM-FE và các lợi thế kiến trúc mang tính quyết định (LLM-FE performance gap and decisive architectural advantages)**:
  - Khoảng cách giữa LLM-FE và TOPOFE lớn nhất trên các tập dữ liệu đòi hỏi các phép kết hợp tương tác liên họ (`cross-family compositions`) như `balance-scale`, `heart`, và `cmc` ($n_{\text{inst}} = 1473, n_{\text{feat}} = 9$: TOPOFE đạt $0.5577 \pm 0.0078$ so với LLMFE $0.5170 \pm 0.0194$, OpenFE $0.5301 \pm 0.0112$, Base $0.5051 \pm 0.0075$).
  - Hiện tượng này cô lập và chứng minh rõ nét ba ưu thế kiến trúc cốt lõi của TOPOFE:
    - *Chuyên biệt hóa họ dị thể (`heterogeneous family specialization`)*: Duy trì bản sắc và tính đa dạng tìm kiếm giữa các nhóm toán tử độc lập.
    - *Tô pô chuyển giao học được (`learned transfer topology`)*: Điều phối luồng trao đổi đặc trưng giữa các họ một cách thích ứng dựa trên phản hồi hiệu năng.
    - *Bộ nhớ thích ứng prompt (`adaptive prompt memory`)*: Bảo tồn và khai thác kinh nghiệm tối ưu hóa riêng biệt cho từng nhánh tìm kiếm.
- **Chi tiết kết quả thực nghiệm phân loại trên toàn bộ 19 tập dữ liệu (Bảng 1 - Table 1)**:
  - *15 tập dữ liệu TOPOFE đạt vị trí dẫn đầu (Best)*:
    - `adult`: TOPOFE ($0.9268 \pm 0.0025$) > OpenFE ($0.9267 \pm 0.0013$) > AutoFeat ($0.9265 \pm 0.0011$) > CAAFE ($0.8784 \pm 0.0052$) > LLMFE ($0.8708 \pm 0.0011$) > FeatLLM ($0.8671 \pm 0.0298$) > OCTree ($0.8668 \pm 0.0104$) > Base ($0.8611 \pm 0.0165$).
    - `balance-scale`: TOPOFE ($0.9465 \pm 0.0046$) > AutoFeat ($0.8848 \pm 0.0079$) > LLMFE ($0.8780 \pm 0.0093$) > OpenFE ($0.8560 \pm 0.0036$) > Base ($0.8320 \pm 0.0233$) = CAAFE ($0.8320 \pm 0.0054$) > FeatLLM ($0.8252 \pm 0.0315$) > OCTree ($0.7822 \pm 0.0241$).
    - `bank` ($n_{\text{inst}} = 45211, n_{\text{feat}} = 16$): TOPOFE ($0.9333 \pm 0.0182$) > OpenFE ($0.9297 \pm 0.0015$) > FeatLLM ($0.9097 \pm 0.0030$) > CAAFE ($0.9091 \pm 0.0031$) > LLMFE ($0.9054 \pm 0.0075$) > AutoFeat ($0.9020 \pm 0.0019$) > Base ($0.8991 \pm 0.0118$) > OCTree ($0.8985 \pm 0.0228$).
    - `breast-w` ($n_{\text{inst}} = 699, n_{\text{feat}} = 9$): TOPOFE ($0.9942 \pm 0.0014$) > FeatLLM ($0.9913 \pm 0.0252$) > OpenFE ($0.9906 \pm 0.0005$) > AutoFeat ($0.9728 \pm 0.0054$) > LLMFE ($0.9607 \pm 0.0036$) > OCTree ($0.9597 \pm 0.0130$) > Base ($0.9500 \pm 0.0096$) > CAAFE ($0.9429 \pm 0.0043$).
    - `car` ($n_{\text{inst}} = 1728, n_{\text{feat}} = 6$): TOPOFE ($0.9971 \pm 0.0051$) > OpenFE ($0.9913 \pm 0.0062$) > AutoFeat ($0.9872 \pm 0.0030$) > CAAFE ($0.9819 \pm 0.0080$) > OCTree ($0.9783 \pm 0.0164$) > LLMFE ($0.9734 \pm 0.0095$) > Base ($0.9671 \pm 0.0027$) > FeatLLM ($0.8150 \pm 0.0087$).
    - `diabetes`: TOPOFE ($0.8524 \pm 0.0021$) > FeatLLM ($0.8497 \pm 0.0040$) > Base ($0.8491 \pm 0.0068$) = CAAFE ($0.8491 \pm 0.0096$) > OpenFE ($0.8483 \pm 0.0005$) > OCTree ($0.8305 \pm 0.0069$) > LLMFE ($0.8298 \pm 0.0054$) > AutoFeat ($0.8012 \pm 0.0143$).
    - `cmc`: TOPOFE ($0.5577 \pm 0.0078$) > OpenFE ($0.5301 \pm 0.0112$) > AutoFeat ($0.5261 \pm 0.0108$) > LLMFE ($0.5170 \pm 0.0194$) > OCTree ($0.5111 \pm 0.0334$) > Base ($0.5051 \pm 0.0075$) = CAAFE ($0.5051 \pm 0.0115$) > FeatLLM ($0.4800 \pm 0.0020$).
    - `communities` ($n_{\text{inst}} = 1994, n_{\text{feat}} = 103$): TOPOFE ($0.7053 \pm 0.0043$) > CAAFE ($0.6992 \pm 0.0079$) > AutoFeat ($0.6991 \pm 0.0075$) > LLMFE ($0.6947 \pm 0.0105$) > Base ($0.6943 \pm 0.0239$) > OpenFE ($0.6936 \pm 0.0041$) > OCTree ($0.6917 \pm 0.0110$) > FeatLLM ($0.5938 \pm 0.0013$).
    - `covtype`: TOPOFE ($0.8774 \pm 0.0038$) > LLMFE ($0.8773 \pm 0.0087$) > OpenFE ($0.8684 \pm 0.0006$) > AutoFeat ($0.8668 \pm 0.0153$) > Base ($0.8652 \pm 0.0120$) = CAAFE ($0.8652 \pm 0.0076$) > FeatLLM ($0.8585 \pm 0.0081$) > OCTree ($0.8332 \pm 0.0115$).
    - `credit-g`: TOPOFE ($0.7878 \pm 0.0066$) > OpenFE ($0.7725 \pm 0.0221$) > AutoFeat ($0.7629 \pm 0.0019$) > LLMFE ($0.7500 \pm 0.0147$) > OCTree ($0.7373 \pm 0.0020$) > FeatLLM ($0.7124 \pm 0.0076$) > Base ($0.7000 \pm 0.0237$) = CAAFE ($0.7000 \pm 0.0107$).
    - `eucalyptus`: TOPOFE ($0.6990 \pm 0.0094$) > OpenFE ($0.6766 \pm 0.0180$) > Base ($0.6724 \pm 0.0151$) > AutoFeat ($0.6643 \pm 0.0213$) > LLMFE ($0.6514 \pm 0.0080$) > OCTree ($0.6416 \pm 0.0267$) > CAAFE ($0.6284 \pm 0.0093$) > FeatLLM ($0.6191 \pm 0.0062$).
    - `heart`: TOPOFE ($0.9346 \pm 0.0015$) > OpenFE ($0.9199 \pm 0.0043$) > AutoFeat ($0.8923 \pm 0.0012$) > FeatLLM ($0.8789 \pm 0.0160$) > Base ($0.8696 \pm 0.0190$) = CAAFE ($0.8696 \pm 0.0093$) > LLMFE ($0.8352 \pm 0.0163$) > OCTree ($0.8217 \pm 0.0093$).
    - `jungle-chess` ($n_{\text{inst}} = 44819, n_{\text{feat}} = 6$): TOPOFE ($0.8858 \pm 0.0104$) > OpenFE ($0.8707 \pm 0.0020$) > LLMFE ($0.8693 \pm 0.0146$) > Base ($0.8636 \pm 0.0019$) = CAAFE ($0.8636 \pm 0.0088$) > AutoFeat ($0.8446 \pm 0.0202$) > OCTree ($0.7796 \pm 0.0096$) > FeatLLM ($0.5915 \pm 0.0252$).
    - `myocardial` ($n_{\text{inst}} = 686, n_{\text{feat}} = 92$): TOPOFE ($0.7878 \pm 0.0066$) > LLMFE ($0.7847 \pm 0.0036$) > OCTree ($0.7827 \pm 0.0175$) > FeatLLM ($0.7824 \pm 0.0056$) > CAAFE ($0.7536 \pm 0.0114$) > Base ($0.7246 \pm 0.0087$) > AutoFeat ($0.7232 \pm 0.0138$) > OpenFE ($0.7217 \pm 0.0350$).
    - `vehicle` ($n_{\text{inst}} = 846, n_{\text{feat}} = 18$): TOPOFE ($0.7781 \pm 0.0073$) > CAAFE ($0.7647 \pm 0.0085$) > Base ($0.7617 \pm 0.0019$) > LLMFE ($0.7574 \pm 0.0033$) > OpenFE ($0.7541 \pm 0.0067$) > FeatLLM ($0.7519 \pm 0.0106$) > OCTree ($0.7416 \pm 0.0018$) > AutoFeat ($0.7342 \pm 0.0143$).
  - *4 tập dữ liệu ngoại lệ (TOPOFE xếp thứ hai hoặc thấp hơn)*:
    - `arrhythmia` ($n_{\text{inst}} = 452, n_{\text{feat}} = 279$): OpenFE dẫn đầu ($0.7344 \pm 0.0362$); TOPOFE xếp thứ hai ($0.7144 \pm 0.0203$); CAAFE ($0.7143 \pm 0.0127$); Base ($0.7053 \pm 0.0186$); AutoFeat ($0.6702 \pm 0.0371$); LLMFE ($0.6566 \pm 0.0129$); FeatLLM ($0.6561 \pm 0.0296$); OCTree ($0.6560 \pm 0.0335$).
    - `blood` ($n_{\text{inst}} = 748, n_{\text{feat}} = 4$): FeatLLM đạt cao nhất ($0.7749 \pm 0.0051$); CAAFE xếp thứ hai ($0.7733 \pm 0.0100$); TOPOFE đạt $0.7440 \pm 0.0129$; OCTree ($0.7246 \pm 0.0312$); LLMFE ($0.7208 \pm 0.0209$); OpenFE ($0.6924 \pm 0.0167$); AutoFeat ($0.6805 \pm 0.0056$); Base ($0.6733 \pm 0.0018$).
    - `pc1` ($n_{\text{inst}} = 1109, n_{\text{feat}} = 21$): FeatLLM dẫn đầu ($0.9605 \pm 0.0295$); TOPOFE xếp thứ hai ($0.9456 \pm 0.0066$, duy trì độ lệch chuẩn nhỏ hơn khoảng 4.5 lần so với FeatLLM); CAAFE ($0.9414 \pm 0.0101$); OpenFE ($0.9367 \pm 0.0254$); AutoFeat ($0.9313 \pm 0.0153$); LLMFE ($0.9312 \pm 0.0102$); OCTree ($0.9302 \pm 0.0186$); Base ($0.9214 \pm 0.0135$).
    - `tic-tac-toe` ($n_{\text{inst}} = 958, n_{\text{feat}} = 9$): OpenFE dẫn đầu ($0.9999 \pm 0.0001$); TOPOFE xếp thứ hai sát nút ($0.9993 \pm 0.0220$); AutoFeat ($0.9923 \pm 0.0012$); Base ($0.9896 \pm 0.0022$); CAAFE ($0.9896 \pm 0.0134$); LLMFE ($0.9896 \pm 0.0138$); OCTree ($0.9886 \pm 0.0058$); FeatLLM ($0.6582 \pm 0.0080$).

| Dataset | $n_{\text{inst}}$ | $n_{\text{feat}}$ | Base | AutoFeat | OpenFE | CAAFE | FeatLLM | OCTree | LLMFE | TOPOFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| adult | $48842$ | $14$ | $0.8611 \pm 0.0165$ | $0.9265 \pm 0.0011$ | $\underline{0.9267 \pm 0.0013}$ | $0.8784 \pm 0.0052$ | $0.8671 \pm 0.0298$ | $0.8668 \pm 0.0104$ | $0.8708 \pm 0.0011$ | $\mathbf{0.9268 \pm 0.0025}$ |
| arrhythmia | $452$ | $279$ | $0.7053 \pm 0.0186$ | $0.6702 \pm 0.0371$ | $\mathbf{0.7344 \pm 0.0362}$ | $0.7143 \pm 0.0127$ | $0.6561 \pm 0.0296$ | $0.6560 \pm 0.0335$ | $0.6566 \pm 0.0129$ | $\underline{0.7144 \pm 0.0203}$ |
| balance-scale | $625$ | $4$ | $0.8320 \pm 0.0233$ | $\underline{0.8848 \pm 0.0079}$ | $0.8560 \pm 0.0036$ | $0.8320 \pm 0.0054$ | $0.8252 \pm 0.0315$ | $0.7822 \pm 0.0241$ | $0.8780 \pm 0.0093$ | $\mathbf{0.9465 \pm 0.0046}$ |
| bank | $45211$ | $16$ | $0.8991 \pm 0.0118$ | $0.9020 \pm 0.0019$ | $\underline{0.9297 \pm 0.0015}$ | $0.9091 \pm 0.0031$ | $0.9097 \pm 0.0030$ | $0.8985 \pm 0.0228$ | $0.9054 \pm 0.0075$ | $\mathbf{0.9333 \pm 0.0182}$ |
| breast-w | $699$ | $9$ | $0.9500 \pm 0.0096$ | $0.9728 \pm 0.0054$ | $0.9906 \pm 0.0005$ | $0.9429 \pm 0.0043$ | $\underline{0.9913 \pm 0.0252}$ | $0.9597 \pm 0.0130$ | $0.9607 \pm 0.0036$ | $\mathbf{0.9942 \pm 0.0014}$ |
| blood | $748$ | $4$ | $0.6733 \pm 0.0018$ | $0.6805 \pm 0.0056$ | $0.6924 \pm 0.0167$ | $\underline{0.7733 \pm 0.0100}$ | $\mathbf{0.7749 \pm 0.0051}$ | $0.7246 \pm 0.0312$ | $0.7208 \pm 0.0209$ | $0.7440 \pm 0.0129$ |
| car | $1728$ | $6$ | $0.9671 \pm 0.0027$ | $0.9872 \pm 0.0030$ | $\underline{0.9913 \pm 0.0062}$ | $0.9819 \pm 0.0080$ | $0.8150 \pm 0.0087$ | $0.9783 \pm 0.0164$ | $0.9734 \pm 0.0095$ | $\mathbf{0.9971 \pm 0.0051}$ |
| diabetes | $253680$ | $21$ | $0.8491 \pm 0.0068$ | $0.8012 \pm 0.0143$ | $0.8483 \pm 0.0005$ | $0.8491 \pm 0.0096$ | $\underline{0.8497 \pm 0.0040}$ | $0.8305 \pm 0.0069$ | $0.8298 \pm 0.0054$ | $\mathbf{0.8524 \pm 0.0021}$ |
| cmc | $1473$ | $9$ | $0.5051 \pm 0.0075$ | $0.5261 \pm 0.0108$ | $\underline{0.5301 \pm 0.0112}$ | $0.5051 \pm 0.0115$ | $0.4800 \pm 0.0020$ | $0.5111 \pm 0.0334$ | $0.5170 \pm 0.0194$ | $\mathbf{0.5577 \pm 0.0078}$ |
| communities | $1994$ | $103$ | $0.6943 \pm 0.0239$ | $0.6991 \pm 0.0075$ | $0.6936 \pm 0.0041$ | $\underline{0.6992 \pm 0.0079}$ | $0.5938 \pm 0.0013$ | $0.6917 \pm 0.0110$ | $0.6947 \pm 0.0105$ | $\mathbf{0.7053 \pm 0.0043}$ |
| covtype | $581012$ | $54$ | $0.8652 \pm 0.0120$ | $0.8668 \pm 0.0153$ | $0.8684 \pm 0.0006$ | $0.8652 \pm 0.0076$ | $0.8585 \pm 0.0081$ | $0.8332 \pm 0.0115$ | $\underline{0.8773 \pm 0.0087}$ | $\mathbf{0.8774 \pm 0.0038}$ |
| credit-g | $1000$ | $20$ | $0.7000 \pm 0.0237$ | $0.7629 \pm 0.0019$ | $\underline{0.7725 \pm 0.0221}$ | $0.7000 \pm 0.0107$ | $0.7124 \pm 0.0076$ | $0.7373 \pm 0.0020$ | $0.7500 \pm 0.0147$ | $\mathbf{0.7878 \pm 0.0066}$ |
| eucalyptus | $736$ | $19$ | $0.6724 \pm 0.0151$ | $0.6643 \pm 0.0213$ | $\underline{0.6766 \pm 0.0180}$ | $0.6284 \pm 0.0093$ | $0.6191 \pm 0.0062$ | $0.6416 \pm 0.0267$ | $0.6514 \pm 0.0080$ | $\mathbf{0.6990 \pm 0.0094}$ |
| heart | $918$ | $11$ | $0.8696 \pm 0.0190$ | $0.8923 \pm 0.0012$ | $\underline{0.9199 \pm 0.0043}$ | $0.8696 \pm 0.0093$ | $0.8789 \pm 0.0160$ | $0.8217 \pm 0.0093$ | $0.8352 \pm 0.0163$ | $\mathbf{0.9346 \pm 0.0015}$ |
| jungle-chess | $44819$ | $6$ | $0.8636 \pm 0.0019$ | $0.8446 \pm 0.0202$ | $\underline{0.8707 \pm 0.0020}$ | $0.8636 \pm 0.0088$ | $0.5915 \pm 0.0252$ | $0.7796 \pm 0.0096$ | $0.8693 \pm 0.0146$ | $\mathbf{0.8858 \pm 0.0104}$ |
| myocardial | $686$ | $92$ | $0.7246 \pm 0.0087$ | $0.7232 \pm 0.0138$ | $0.7217 \pm 0.0350$ | $0.7536 \pm 0.0114$ | $0.7824 \pm 0.0056$ | $0.7827 \pm 0.0175$ | $\underline{0.7847 \pm 0.0036}$ | $\mathbf{0.7878 \pm 0.0066}$ |
| pc1 | $1109$ | $21$ | $0.9214 \pm 0.0135$ | $0.9313 \pm 0.0153$ | $0.9367 \pm 0.0254$ | $0.9414 \pm 0.0101$ | $\mathbf{0.9605 \pm 0.0295}$ | $0.9302 \pm 0.0186$ | $0.9312 \pm 0.0102$ | $\underline{0.9456 \pm 0.0066}$ |
| tic-tac-toe | $958$ | $9$ | $0.9896 \pm 0.0022$ | $0.9923 \pm 0.0012$ | $\mathbf{0.9999 \pm 0.0001}$ | $0.9896 \pm 0.0134$ | $0.6582 \pm 0.0080$ | $0.9886 \pm 0.0058$ | $0.9896 \pm 0.0138$ | $\underline{0.9993 \pm 0.0220}$ |
| vehicle | $846$ | $18$ | $0.7617 \pm 0.0019$ | $0.7342 \pm 0.0143$ | $0.7541 \pm 0.0067$ | $\underline{0.7647 \pm 0.0085}$ | $0.7519 \pm 0.0106$ | $0.7416 \pm 0.0018$ | $0.7574 \pm 0.0033$ | $\mathbf{0.7781 \pm 0.0073}$ |

#### Regression

- **Hiệu năng tổng thể vượt trội của TOPOFE trên bài toán hồi quy (Overall regression performance)**: TOPOFE đạt sai số RMSE thấp nhất trên $9/10$ tập dữ liệu hồi quy được khảo sát (Bảng 2 - Table 2).
  - FeatLLM và CAAFE không có mặt trong phép so sánh do được thiết kế riêng biệt cho các tác vụ phân loại (`classification tasks only`).
- **Mức độ giảm thiểu RMSE tỷ lệ thuận với độ phong phú của tương tác biến chéo (Improvements scaling consistently with cross-variable interaction richness)**:
  - *Mức giảm lớn nhất trên các tập dữ liệu phụ thuộc mạnh vào tương tác đa biến (`interaction-driven datasets`)*:
    - Trên tập `bike` ($n_{\text{inst}} = 17389, n_{\text{feat}} = 12$): TOPOFE giảm $28.7\%$ RMSE so với OCTree (TOPOFE đạt $3.0210 \pm 0.0202$ so với OCTree $4.2336 \pm 0.1273$, OpenFE $4.0471 \pm 0.0576$, Base $4.3494 \pm 0.0745$).
    - Trên tập `airfoil_self_noise` ($n_{\text{inst}} = 1503, n_{\text{feat}} = 6$): TOPOFE giảm $15.7\%$ RMSE so với LLM-FE (TOPOFE đạt $1.3000 \pm 0.0123$ so với LLMFE $1.5415 \pm 0.0162$, OpenFE $1.6143 \pm 0.0232$, Base $1.6701 \pm 0.0514$).
  - *Biên độ thu hẹp trên các tập dữ liệu mà một họ biến đổi đơn lẻ đã đáp ứng đủ (`single transformation family suffices`)*:
    - Trên tập `cpu` ($n_{\text{inst}} = 8192, n_{\text{feat}} = 10$): TOPOFE đạt $2.4719 \pm 0.0351$ so với OpenFE $2.4807 \pm 0.0904$, LLMFE $2.9035 \pm 0.1042$, Base $3.0352 \pm 0.1953$.
    - Trên tập `forest-fires` ($n_{\text{inst}} = 517, n_{\text{feat}} = 13$): TOPOFE đạt $0.1611 \pm 0.0221$ so với AutoFeat $0.1651 \pm 0.0152$, LLMFE $0.1676 \pm 0.0162$, Base $0.1751 \pm 0.1939$.
- **Sự mở rộng khoảng cách của LLM-FE do sụp đổ quần thể đơn (LLM-FE widening gap and single-population collapse)**:
  - Khoảng cách hiệu năng của LLM-FE so với TOPOFE ngày càng mở rộng khi độ phức tạp của dữ liệu tăng lên.
  - Hiện tượng này hoàn toàn nhất quán với việc thiết kế quần thể đơn (`single-population design`) của LLM-FE bị sụp đổ/hội tụ sớm vào một họ biến đổi chiếm ưu thế (`collapsing onto a dominant transformation family`), đánh mất tính đa dạng cần thiết để khám phá các cấu trúc biểu diễn mới.
- **Tính ổn định thống kê và triệt tiêu phương sai của LLM (Statistical stability and variance reduction)**:
  - Xét trên cả hai loại tác vụ phân loại và hồi quy, độ lệch chuẩn (`standard deviation`) thấp hơn một cách nhất quán của TOPOFE chứng minh rằng:
    - Bộ nhớ Thích ứng Prompt trên từng đảo (`per-island Prompt Adaptation Memory`).
    - Kết hợp cùng cơ chế tổng hợp đặc trưng ràng buộc theo lược đồ (`schema-constrained synthesis`).
    - Đã cùng nhau hạn chế và giảm thiểu hiệu quả tính bất ổn định cố hữu trong quá trình sinh tự do của LLM (`instability inherent in unconstrained LLM generation`).
- **Chi tiết kết quả thực nghiệm hồi quy trên toàn bộ 10 tập dữ liệu (Bảng 2 - Table 2, đo bằng RMSE $\downarrow$)**:
  - *Tập `airfoil_self_noise`*: TOPOFE ($1.3000 \pm 0.0123$) < LLMFE ($1.5415 \pm 0.0162$) < OpenFE ($1.6143 \pm 0.0232$) < AutoFeat ($1.6265 \pm 0.1701$) < Base ($1.6701 \pm 0.0514$) = OCTree ($1.6701 \pm 0.0763$).
  - *Tập `bike`*: TOPOFE ($3.0210 \pm 0.0202$) < OpenFE ($4.0471 \pm 0.0576$) < OCTree ($4.2336 \pm 0.1273$) < Base ($4.3494 \pm 0.0745$) = LLMFE ($4.3494 \pm 0.2363$) < AutoFeat ($4.4713 \pm 0.1830$).
  - *Tập `cpu`*: TOPOFE ($2.4719 \pm 0.0351$) < OpenFE ($2.4807 \pm 0.0904$) < LLMFE ($2.9035 \pm 0.1042$) < OCTree ($3.0087 \pm 0.1007$) < Base ($3.0352 \pm 0.1953$) < AutoFeat ($3.0670 \pm 0.1306$).
  - *Tập `crab` ($n_{\text{inst}} = 3893, n_{\text{feat}} = 8$)*: TOPOFE ($2.2585 \pm 0.0512$) < LLMFE ($2.3489 \pm 0.1800$) < AutoFeat ($2.4073 \pm 0.0741$) < OCTree ($2.4222 \pm 0.0254$) < Base ($2.4700 \pm 0.1039$) < OpenFE ($2.4807 \pm 0.1341$).
  - *Tập `diamond` ($n_{\text{inst}} = 53940, n_{\text{feat}} = 9$)*: TOPOFE ($5.4711 \pm 0.2299$) < AutoFeat ($5.5654 \pm 0.1203$) < LLMFE ($5.6901 \pm 0.2363$) < Base ($5.8112 \pm 0.0522$) < OCTree ($5.8208 \pm 0.0609$) < OpenFE ($5.9627 \pm 0.0573$).
  - *Tập `forest-fires` ($n_{\text{inst}} = 517, n_{\text{feat}} = 13$)*: TOPOFE ($0.1611 \pm 0.0221$) < AutoFeat ($0.1651 \pm 0.0152$) < LLMFE ($0.1676 \pm 0.0162$) < OCTree ($0.1740 \pm 0.1956$) < Base ($0.1751 \pm 0.1939$) < OpenFE ($0.2121 \pm 0.1313$).
  - *Tập `housing` ($n_{\text{inst}} = 20640, n_{\text{feat}} = 9$)*: TOPOFE ($4.6714 \pm 0.1723$) < OCTree ($4.8148 \pm 0.1256$) < Base ($4.8168 \pm 0.2270$) < OpenFE ($4.8213 \pm 0.1457$) < LLMFE ($4.8597 \pm 0.2111$) < AutoFeat ($5.1293 \pm 0.1553$).
  - *Tập `insurance` ($n_{\text{inst}} = 1338, n_{\text{feat}} = 7$, tập duy nhất OpenFE dẫn đầu)*: OpenFE ($4.8053 \pm 0.2061$) < TOPOFE ($4.8843 \pm 0.1802$) < OCTree ($4.9810 \pm 0.2513$) < LLMFE ($5.0812 \pm 0.3133$) < AutoFeat ($5.1103 \pm 0.1670$) < Base ($5.2817 \pm 0.2510$).
  - *Tập `plasma` ($n_{\text{inst}} = 315, n_{\text{feat}} = 13$)*: TOPOFE ($2.1950 \pm 0.0451$) < OpenFE ($2.2409 \pm 0.1554$) < AutoFeat ($2.2840 \pm 0.1397$) < LLMFE ($2.2835 \pm 0.2358$) < Base ($2.3577 \pm 0.0455$) < OCTree ($2.3677 \pm 0.1007$).
  - *Tập `wine` ($n_{\text{inst}} = 2554, n_{\text{feat}} = 11$)*: TOPOFE ($0.5936 \pm 0.0098$) < OpenFE ($0.6557 \pm 0.0455$) < LLMFE ($0.6619 \pm 0.0719$) < AutoFeat ($0.6847 \pm 0.0252$) < Base ($0.6911 \pm 0.0684$) = OCTree ($0.6911 \pm 0.0822$).

| Dataset | $n_{\text{inst}}$ | $n_{\text{feat}}$ | Base | AutoFeat | OpenFE | OCTree | LLMFE | TOPOFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| airfoil_self_noise | $1503$ | $6$ | $1.6701 \pm 0.0514$ | $1.6265 \pm 0.1701$ | $1.6143 \pm 0.0232$ | $1.6701 \pm 0.0763$ | $\underline{1.5415 \pm 0.0162}$ | $\mathbf{1.3000 \pm 0.0123}$ |
| bike | $17389$ | $12$ | $4.3494 \pm 0.0745$ | $4.4713 \pm 0.1830$ | $\underline{4.0471 \pm 0.0576}$ | $4.2336 \pm 0.1273$ | $4.3494 \pm 0.2363$ | $\mathbf{3.0210 \pm 0.0202}$ |
| cpu | $8192$ | $10$ | $3.0352 \pm 0.1953$ | $3.0670 \pm 0.1306$ | $\underline{2.4807 \pm 0.0904}$ | $3.0087 \pm 0.1007$ | $2.9035 \pm 0.1042$ | $\mathbf{2.4719 \pm 0.0351}$ |
| crab | $3893$ | $8$ | $2.4700 \pm 0.1039$ | $2.4073 \pm 0.0741$ | $2.4807 \pm 0.1341$ | $2.4222 \pm 0.0254$ | $\underline{2.3489 \pm 0.1800}$ | $\mathbf{2.2585 \pm 0.0512}$ |
| diamond | $53940$ | $9$ | $5.8112 \pm 0.0522$ | $\underline{5.5654 \pm 0.1203}$ | $5.9627 \pm 0.0573$ | $5.8208 \pm 0.0609$ | $5.6901 \pm 0.2363$ | $\mathbf{5.4711 \pm 0.2299}$ |
| forest-fires | $517$ | $13$ | $0.1751 \pm 0.1939$ | $\underline{0.1651 \pm 0.0152}$ | $0.2121 \pm 0.1313$ | $0.1740 \pm 0.1956$ | $0.1676 \pm 0.0162$ | $\mathbf{0.1611 \pm 0.0221}$ |
| housing | $20640$ | $9$ | $4.8168 \pm 0.2270$ | $5.1293 \pm 0.1553$ | $4.8213 \pm 0.1457$ | $\underline{4.8148 \pm 0.1256}$ | $4.8597 \pm 0.2111$ | $\mathbf{4.6714 \pm 0.1723}$ |
| insurance | $1338$ | $7$ | $5.2817 \pm 0.2510$ | $5.1103 \pm 0.1670$ | $\mathbf{4.8053 \pm 0.2061}$ | $4.9810 \pm 0.2513$ | $5.0812 \pm 0.3133$ | $\underline{4.8843 \pm 0.1802}$ |
| plasma | $315$ | $13$ | $2.3577 \pm 0.0455$ | $2.2840 \pm 0.1397$ | $\underline{2.2409 \pm 0.1554}$ | $2.3677 \pm 0.1007$ | $2.2835 \pm 0.2358$ | $\mathbf{2.1950 \pm 0.0451}$ |
| wine | $2554$ | $11$ | $0.6911 \pm 0.0684$ | $0.6847 \pm 0.0252$ | $\underline{0.6557 \pm 0.0455}$ | $0.6911 \pm 0.0822$ | $0.6619 \pm 0.0719$ | $\mathbf{0.5936 \pm 0.0098}$ |
