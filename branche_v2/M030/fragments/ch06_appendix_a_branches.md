## Appendix A

- Bảng A1 (Table A1) tổng hợp kết quả kiểm định thống kê phi tham số Wilcoxon-Mann-Whitney (Wilcoxon-Mann-Whitney nonparametric statistical test) nhằm so sánh các mẫu vận hành giữa trạng thái trong kiểm soát (in-control operations) và ngoài kiểm soát (out-of-control operations) của hệ thống MBR quy mô pilot [74].
  - Kiểm định được thiết lập ở mức ý nghĩa $1\,\%$ ($\alpha = 0.01$) để kiểm tra xem giá trị trung vị (medians) của các biến số gồm hiệu suất loại bỏ amoniac (Removal), nhiệt độ (Temp), thời gian lưu bùn (SRT) và nồng độ COD dòng vào (fCOD) có sự khác biệt có ý nghĩa thống kê giữa hai trạng thái vận hành hay không.
  - Quy mô mẫu kiểm định:
    - Nhóm 1 (Group 1 - In-control): trạng thái vận hành bình thường, nằm trong giới hạn kiểm soát thống kê, gồm $n_1 = 272$ mẫu dữ liệu.
    - Nhóm 2 (Group 2 - Out-of-control): trạng thái vận hành bất thường hoặc suy giảm hiệu suất, ngoài giới hạn kiểm soát thống kê, gồm $n_2 = 46$ mẫu dữ liệu.
- Chi tiết các biến số giám sát và kết quả kiểm định thống kê trong Bảng A1 (Table A1):
  - Biến hiệu suất loại bỏ amoniac (Removal):
    - Giá trị thống kê kiểm định (Statistic): $12{,}512$.
    - Mức ý nghĩa thống kê ($p$-Value): $2.07\text{e-}27$ ($2.07 \times 10^{-27}$).
    - Nhận xét và phát hiện: Giá trị $p \ll 0.01$ khẳng định mức độ chênh lệch có ý nghĩa thống kê cực kỳ cao; giá trị hiệu suất loại bỏ amoniac ở trạng thái ngoài kiểm soát thấp hơn đáng kể so với trạng thái trong kiểm soát.
  - Biến nhiệt độ vận hành (Temp):
    - Giá trị thống kê kiểm định (Statistic): $5976$.
    - Mức ý nghĩa thống kê ($p$-Value): $1.22\text{e-}4$ ($1.22 \times 10^{-4}$).
    - Nhận xét và phát hiện: Giá trị $p < 0.01$ xác nhận nhiệt độ vận hành của hệ thống ở trạng thái ngoài kiểm soát thấp hơn đáng kể so với trạng thái trong kiểm soát.
  - Biến thời gian lưu bùn (SRT - Sludge Retention Time):
    - Giá trị thống kê kiểm định (Statistic): $9913$.
    - Mức ý nghĩa thống kê ($p$-Value): $2.68\text{e-}13$ ($2.68 \times 10^{-13}$).
    - Nhận xét và phát hiện: Giá trị $p \ll 0.01$ chứng minh thời gian lưu bùn ở trạng thái ngoài kiểm soát bị rút ngắn đáng kể so với trạng thái trong kiểm soát.
  - Biến nồng độ COD dòng nạp vào bể (fCOD - Influent Chemical Oxygen Demand):
    - Giá trị thống kê kiểm định (Statistic): $9722$.
    - Mức ý nghĩa thống kê ($p$-Value): $1.86\text{e-}9$ ($1.86 \times 10^{-9}$).
    - Nhận xét và phát hiện: Giá trị $p \ll 0.01$ xác nhận nồng độ COD trong dòng nước thải nạp vào ở trạng thái ngoài kiểm soát cao hơn đáng kể so với trạng thái trong kiểm soát.
- Bảng tổng hợp dữ liệu kiểm định Wilcoxon-Mann-Whitney (Table A1):

| Group 1 (Nhóm 1) | Group 2 (Nhóm 2) | $n_1$ | $n_2$ | Variable (Biến số) | Statistic (Giá trị thống kê) | $p$-Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| In-control | Out-of-control | $272$ | $46$ | Removal | $12{,}512$ | $2.07\text{e-}27$ |
| In-control | Out-of-control | $272$ | $46$ | Temp | $5976$ | $1.22\text{e-}4$ |
| In-control | Out-of-control | $272$ | $46$ | SRT | $9913$ | $2.68\text{e-}13$ |
| In-control | Out-of-control | $272$ | $46$ | fCOD | $9722$ | $1.86\text{e-}9$ |

- Ý nghĩa kiểm định đối với chẩn đoán và kiểm soát quá trình MBR:
  - Tất cả $4$ biến số phân tích đều đạt mức ý nghĩa $p < 0.01$, củng cố định lượng cho các kết quả biểu diễn trên đồ thị hộp (boxplots ở Hình 11) và kết quả phân tích đóng góp từ mô hình MSPC-PCA.
  - Kết quả kiểm định xác nhận vững chắc rằng điều kiện vận hành ngoài kiểm soát (suy giảm hiệu suất khử amoniac) của hệ thống MBR xử lý nước thải nhà máy lọc dầu liên hệ chặt chẽ với sự sụt giảm nhiệt độ, sự suy giảm thời gian lưu bùn (SRT ngắn gây nguy cơ rửa trôi vi khuẩn nitrat hóa), và sự gia tăng đột biến của tải lượng COD dòng vào (fCOD cao làm tăng tỷ lệ $\text{C/N}$, kích thích vi khuẩn dị dưỡng cạnh tranh gay gắt với vi khuẩn nitrat hóa).
