#### 3.2.2. RSM-based RBFNN training

- Regression analysis (phân tích hồi quy) được áp dụng trên dữ liệu design matrix (ma trận thiết kế) các hyperparameters (siêu tham số) của RBFNN để khớp giá trị đáp ứng MSE vào một quadratic model (mô hình bậc hai):
  - Biến đáp ứng MSE được chuyển đổi sang dạng logarit tự nhiên $\ln(\text{MSE})$.
  - Quadratic model (mô hình bậc hai) theo coded values (giá trị mã hóa) cho $\ln(\text{MSE})$ được biểu diễn bằng Phương trình $(16)$:
    $$\ln(\text{MSE}) = -3.6265 - 1.1606 A - 0.0109 B + 0.0649 AB + 1.0952 A^2 - 0.0086 B^2$$
    trong đó $A$ và $B$ lần lượt là coded values (giá trị mã hóa) của number of neurons (số lượng nơ-ron) và number of spreads (độ rộng spread).
  - Dấu dương ($+$) và dấu âm ($-$) lần lượt đại diện cho synergistic effects (hiệu ứng hiệp đồng) và antagonistic effects (hiệu ứng đối kháng) giữa mutual interaction (tương tác qua lại) và individual parameters (thông số đơn lẻ).
- Bảng $3$ trình bày kết quả ANOVA (phân tích phương sai) của quadratic model cho đáp ứng huấn luyện RBFNN-RSM:
  - Giá trị $F$-value cao nhất đạt $21809.26$ với $p$-value $< 0.0001$ khẳng định statistical significance (ý nghĩa thống kê) của mô hình (tổng bình phương $11.95$, bậc tự do $df = 5$, trung bình bình phương $2.39$).
  - Hệ số xác định $R^2 = 0.9999$ biểu thị tương quan rất mạnh giữa predicted response (giá trị đáp ứng dự đoán) và actual response (giá trị đáp ứng thực tế).
  - Adjusted $R^2$ (hệ số xác định hiệu chỉnh) đạt $0.9999$ gắn kết chặt chẽ với predicted $R^2$ (hệ số xác định dự báo) đạt $0.9993$, nhấn mạnh ý nghĩa của mô hình.
  - Adequate precision (độ chính xác thích hợp) đạt $344.6088$ (văn bản trích dẫn $344.6068$), thể hiện satisfactory signal-to-noise ratio (tỷ số tín hiệu trên nhiễu thỏa đáng), vượt xa ngưỡng mong muốn lớn hơn $4$ để điều hướng design space (không gian thiết kế).
  - Chi tiết ANOVA cho từng số hạng:
    - Nhân tố $A$ (number of neurons): tổng bình phương $8.08$, $df = 1$, trung bình bình phương $8.08$, $F$-value $= 73738.65$, $p$-value $< 0.0001$ (có ý nghĩa thống kê).
    - Nhân tố $B$ (number of spreads): tổng bình phương $0.0007$, $df = 1$, trung bình bình phương $0.0007$, $F$-value $= 6.47$, $p$-value $= 0.0384$ (có ý nghĩa thống kê).
    - Số hạng tương tác $AB$: tổng bình phương $0.0168$, $df = 1$, trung bình bình phương $0.0168$, $F$-value $= 153.69$, $p$-value $< 0.0001$ (có ý nghĩa thống kê).
    - Số hạng bậc hai $A^2$: tổng bình phương $3.31$, $df = 1$, trung bình bình phương $3.31$, $F$-value $= 30225.83$, $p$-value $< 0.0001$ (có ý nghĩa thống kê).
    - Số hạng bậc hai $B^2$: tổng bình phương $0.0002$, $df = 1$, trung bình bình phương $0.0002$, $F$-value $= 1.87$, $p$-value $= 0.2141$ (không có ý nghĩa thống kê).
    - Residual (phần dư): tổng bình phương $0.0008$, $df = 7$, trung bình bình phương $0.0001$.
    - Lack of fit (độ không phù hợp): tổng bình phương $0.0008$, $df = 3$, trung bình bình phương $0.0003$.
    - Pure error (sai số thuần túy): tổng bình phương $0.0000$, $df = 4$, trung bình bình phương $0.0000$.
    - Cor total (tổng cộng hiệu chỉnh): tổng bình phương $11.95$, $df = 12$.
- Tất cả các nhân tố chính ($A$ và $B$) cùng tương tác hai nhân tố ($AB$) đều có $p$-value $< 0.050$, cho thấy tác động đáng kể lên quá trình dự đoán:
  - First-order and second-order effects (hiệu ứng bậc một và bậc hai) của nơ-ron ($A$ và $A^2$) là các số hạng có ý nghĩa quyết định nhất trong đáp ứng $\ln(\text{MSE})$.
  - Ngược lại, số hạng bậc hai của spread ($B^2$) có $p$-value là $0.2141$, thể hiện ảnh hưởng rất ít đến đáp ứng.
- Đối chiếu giữa các giá trị đáp ứng $\ln(\text{MSE})$ thực tế và dự đoán dựa trên $13$ lượt chạy với nhiều cấu hình siêu tham số RBFNN sử dụng CCD (Central Composite Design - thiết kế tâm xoay phức hợp) được cung cấp trong Bảng $\text{S}4$:
  - Các giá trị thực tế và dự đoán thống nhất chặt chẽ, khẳng định khả năng ứng dụng của quadratic model (Phương trình $(16)$) trong việc thiết lập mối quan hệ giữa $\ln(\text{MSE})$ và các siêu tham số RBFNN.
- Residual analysis (phân tích phần dư) củng cố các kết luận thống kê:
  - Hình $\text{S}6(a)$ hiển thị normal probability diagram of studentized residuals (biểu đồ xác suất chuẩn của phần dư student hóa), trong đó các điểm phân bố cụm sát đường thẳng, minh chứng cho model adequacy (tính thỏa đáng của mô hình).
  - Hình $\text{S}6(b)$ hiển thị đồ thị phần dư so với giá trị đáp ứng dự đoán, cho thấy sự phân tán ngẫu nhiên trên toàn đồ thị giữa hai đường giới hạn đỏ ($-4.5612$ và $+4.5612$), khẳng định tính thỏa đáng của mô hình và không có sai số đáng ngờ.
- Response surface and contour plots (biểu đồ bề mặt đáp ứng và đường mức) cùng perturbation scheme (sơ đồ nhiễu loạn) làm rõ tác động phi tuyến của các siêu tham số và xác định vùng tối ưu:
  * **Hình 7.** Biểu đồ bề mặt đáp ứng và đường mức huấn luyện RBFNN
    * <img src="assets/fig_07_p18.jpeg" alt="Hình 7" />
    * **Hình này chứng minh điều gì**
      * Số nơ-ron ($A$) chi phối phi tuyến mạnh đến sai số trong khi spread ($B$) biến thiên không đáng kể; xác lập cấu hình tối ưu tại $29$ nơ-ron và spread $1.5$ với độ thỏa dụng (desirability) bằng $1$.
    * **Từ đâu mà thấy được**
      * Đồ thị (a)–(c): Đường $A$ (nơ-ron) dốc mạnh dạng lòng chảo chạm đáy trong khoảng $13\text{--}31$, trong khi đường $B$ (spread) gần như nằm ngang với khoảng biến thiên $\ln(\text{MSE})$ rất hẹp ($-3.67$ đến $-3.61$).
      * Đồ thị (d, e): Bề mặt 3D và đường mức 2D chuyển từ vùng đỏ cực đại tại $A = 1$ sang thung lũng xanh lam cực tiểu ($\ln(\text{MSE}) \le -3.90776$) ở khoảng $13\text{--}31$ nơ-ron, hội tụ về nghiệm tối ưu $29$ nơ-ron và spread $1.5$.
  - Perturbation scheme (sơ đồ nhiễu loạn) so sánh ảnh hưởng của $2$ siêu tham số ($A$: nơ-ron và $B$: spread) tại reference point (điểm tham chiếu) được minh họa ở Hình $7(a)$:
    - Đường $A$ (nơ-ron) thể hiện độ cong giảm mạnh tới một điểm cụ thể rồi tăng dần theo $\ln(\text{MSE})$.
    - Ngược lại, đường $B$ (spread) duy trì xu hướng không đổi nằm ngang dọc theo điểm giữa.
  - Hình $7(b)$ và $7(c)$ vẽ đáp ứng $\ln(\text{MSE})$ tương ứng theo số lượng nơ-ron và số lượng spread:
    - Nhân tố $A$ tác động tương đối lớn hơn lên những thay đổi tại điểm tham chiếu, trong khi nhân tố $B$ có ảnh hưởng tối thiểu.
    - Đường cong trong Hình $7(c)$ cho thấy số lượng spread tăng đáng kể ở giai đoạn đầu, sau đó giảm dần theo $\ln(\text{MSE})$, củng cố kết quả phân tích thống kê từ Bảng $3$ về ý nghĩa của tất cả các siêu tham số RBFNN đối với $\ln(\text{MSE})$.
  - Sự chuyển đổi của số lượng spread từ không có ý nghĩa trong two-level factorial design (thiết kế nhân tố hai mức, Hình $\text{S}4(b)$) thành có ý nghĩa trong RSM xuất phát từ việc thiết kế hai mức không phù hợp để nắm bắt các mối quan hệ phức tạp hơn hoặc độ cong trên bề mặt đáp ứng khi khảo sát nhiều mức (lớn hơn $2$ mức).
  - Hình $7(d)$ và $7(e)$ lần lượt trình bày 3D surface plot (biểu đồ bề mặt 3D) và 2D contour plot (biểu đồ đường mức 2D) của $\ln(\text{MSE})$ theo các tổ hợp số lượng nơ-ron và spread:
    - Vùng màu đỏ thể hiện mức $\ln(\text{MSE})$ cao nhất, trong khi vùng màu xanh lam thể hiện mức $\ln(\text{MSE})$ thấp nhất.
    - Giá trị cực tiểu của $\ln(\text{MSE})$ xuất hiện trong khoảng $13\text{--}31$ nơ-ron.
  - Thiết lập mục tiêu tối ưu hóa số trị: số lượng nơ-ron và số lượng spread được đặt ở chế độ 'trong khoảng' ('in range'), còn biến đáp ứng MSE được đặt ở chế độ 'cực tiểu' ('minimum').
  - RSM đề xuất các giá trị tối ưu gồm $29$ nơ-ron và $1.5$ spread để cực tiểu hóa $\ln(\text{MSE})$ với desirability value (giá trị mong muốn) đạt $1$.
  - Các thông số tối ưu này được áp dụng để dự đoán permeate flux (thông lượng dòng thấm) trong hệ thống màng sinh học ngập nước xử lý POME (Palm Oil Mill Effluent - nước thải nhà máy dầu cọ).
