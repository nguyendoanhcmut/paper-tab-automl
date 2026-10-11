    * **Hình 6.** Đồ thị phân tích ảnh hưởng và tương tác của các siêu tham số đến giá trị nghịch đảo sai số ($1/\text{MSE}$) của mô hình FFNN: (a) Đồ thị nhiễu loạn (perturbation plot), (b) Đồ thị một yếu tố số epoch, (c) Đồ thị bề mặt đáp ứng 3D tương tác giữa learning rate và momentum, (d) Đồ thị đường mức (contour plot) của learning rate và momentum
      * <img src="assets/fig_06_p15.jpeg" alt="Hình 6" />
      * **Hình này chứng minh điều gì**
        * Số lượng nơ-ron (yếu tố $A$) là yếu tố chi phối mạnh nhất đến $1/\text{MSE}$, đồng thời learning rate (tốc độ học, $B$) và momentum (động lượng, $C$) có tương tác phi tuyến rõ rệt, trong khi số epoch ($D$) hầu như không ảnh hưởng.
      * **Từ đâu mà thấy được**
        * Đồ thị nhiễu loạn (a) và đơn yếu tố (b): Yếu tố $A$ có độ dốc lớn nhất đưa $1/\text{MSE}$ từ $< 25$ tại $-1{,}000$ lên $> 46$ tại $+1{,}000$ (mức mã hóa), trong khi đường $D$ gần như nằm ngang phẳng quanh mức $37$ suốt dải $100\text{--}300\text{ epoch}$.
        * Đồ thị $3\text{D}$ (c) và đường mức (d): Tương tác giữa $B$ và $C$ tạo bề mặt vòm cong với các đường elip đồng tâm, đạt cực đại $1/\text{MSE} > 37{,}3$ trong khoảng learning rate $0{,}25\text{--}0{,}31$ và momentum $0{,}68\text{--}0{,}80$, vượt trội so với vùng giá trị thấp $< 30$.
