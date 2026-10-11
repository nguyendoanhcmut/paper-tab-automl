  * **Hình 7.** Biểu đồ bề mặt đáp ứng và đường mức huấn luyện RBFNN
    * <img src="assets/fig_07_p18.jpeg" alt="Hình 7" />
    * **Hình này chứng minh điều gì**
      * Số nơ-ron ($A$) chi phối phi tuyến mạnh đến sai số trong khi spread ($B$) biến thiên không đáng kể; xác lập cấu hình tối ưu tại $29$ nơ-ron và spread $1.5$ với độ thỏa dụng (desirability) bằng $1$.
    * **Từ đâu mà thấy được**
      * Đồ thị (a)–(c): Đường $A$ (nơ-ron) dốc mạnh dạng lòng chảo chạm đáy trong khoảng $13\text{--}31$, trong khi đường $B$ (spread) gần như nằm ngang với khoảng biến thiên $\ln(\text{MSE})$ rất hẹp ($-3.67$ đến $-3.61$).
      * Đồ thị (d, e): Bề mặt 3D và đường mức 2D chuyển từ vùng đỏ cực đại tại $A = 1$ sang thung lũng xanh lam cực tiểu ($\ln(\text{MSE}) \le -3.90776$) ở khoảng $13\text{--}31$ nơ-ron, hội tụ về nghiệm tối ưu $29$ nơ-ron và spread $1.5$.
