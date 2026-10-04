### 3.2. Input features determination

- Sau bước lựa chọn đặc trưng định tính như trình bày ở Mục 2.2.2 (Section 2.2.2), $9$ biến đầu vào (nine input variables) còn lại được đánh giá thống kê:
  - Tài liệu bổ sung $\text{SI 3}$ xác định các biến có mối tương quan mang ý nghĩa thống kê được đánh dấu bằng các hình tròn ($p\text{-value} < 0.05$) trong số các đặc trưng đầu vào còn lại.
- Chỉ lưu lượng dòng vào (influent flow rate) được giữ lại nhằm đơn giản hóa cấu trúc mô hình:
  - Quyết định này dựa trên sự tương đồng giữa lưu lượng dòng vào và lưu lượng dòng ra (effluent flow rate), vốn thể hiện độ phục hồi thông lượng (flux recovery) đạt trên $97\,\%$.
- Áp suất xuyên màng ($\text{TMP}$ - transmembrane pressure) được đưa vào mô hình nhằm nâng cao khả năng chuyển giao của mô hình (model transferability):
  - Mặc dù $\text{TMP}$ có tương quan yếu với quá trình nitrat hóa (nitrification), việc giữ lại thông số này giúp mô hình tính đến hiện tượng tắc nghẽn màng không tuần hoàn (acyclic membrane fouling) trong vận hành dài hạn.
- Bản ghi làm sạch màng (membrane cleaning record) bị loại trừ khỏi tập đặc trưng:
  - Mặc dù biến này tương quan với $\text{TMP}$ và phản ánh nhu cầu bảo trì màng, nó bị loại bỏ nhằm tránh các sai lệch mang tính đặc thù theo vật liệu màng (material-specific biases).
- Tổng nitơ ($\text{TN}$ - total nitrogen) bị loại bỏ do mức đóng góp dự đoán không đáng kể (marginal predictive contribution) và tính không thực tiễn trong giám sát thời gian thực (real-time monitoring):
  - Mặc dù $\text{TN}$ có tương quan nhất định với đầu ra mục tiêu, cảm biến đo $\text{TN}$ có chi phí đắt đỏ và có chu kỳ đo dài ($30\text{--}60\text{ min}$, dựa trên các cảm biến $\text{TN}$ thương mại hiện có) so với các cảm biến giám sát $\text{NO}_3^-\text{-N}$ và $\text{NH}_4^+\text{-N}$.
- Bộ đặc trưng cuối cùng phục vụ dự đoán trạng thái nitrat hóa gồm $6$ đặc trưng đầu vào (six input features), bao gồm $3$ yếu tố vận hành (operational factors) và $3$ biến chất lượng nước (water quality variables):
  - $3$ yếu tố vận hành gồm: lưu lượng khí cấp (air flow rate), lưu lượng dòng vào (influent flow rate), và $\text{TMP}$.
  - $3$ biến chất lượng nước gồm: nồng độ $\text{COD}$ dòng ra (effluent $\text{COD}$), $\text{NO}_3^-\text{-N}$, và $\text{NH}_4^+\text{-N}$.
  - Tập đặc trưng tinh giản (streamlined feature set) này cân bằng giữa tính đơn giản của mô hình, độ chính xác và tính khả thi ứng dụng hiện trường trong giám sát quá trình nitrat hóa.
