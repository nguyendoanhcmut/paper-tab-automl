    * **Hình 5.** Phân bố tần suất sai số tương đối của mạng RBF theo số lượng mẫu huấn luyện
      * <img src="assets/fig_05_p6.jpeg" alt="Hình 5" />
      * **Hình này chứng minh điều gì**
        * Mạng RBF với số mẫu huấn luyện $\ge 10$ (10, 15, 20 mẫu) đạt độ chính xác cao khi sai số tương đối co hẹp về dải $[-0{,}03; 0{,}10]$ quanh mức 0, khắc phục sự phân tán lớn khi chỉ có 5 mẫu ($[-0{,}293; 0{,}386]$).
      * **Từ đâu mà thấy được**
        * Panel (a) (5 mẫu): tần suất sai số trải rộng từ $-0{,}29$ đến $0{,}39$ (đỉnh tần suất 10 tại $-0{,}07$ và 9 tại $0{,}10$).
        * Panel (b)–(d) (10, 15, 20 mẫu): các cột tần suất tập trung đột biến quanh 0 (đỉnh đạt 14–18 tại dải $-0{,}03$ đến $0{,}07$), các bin ngoài $[-0{,}03; 0{,}10]$ hầu như bằng 0 hoặc $\le 1$.
