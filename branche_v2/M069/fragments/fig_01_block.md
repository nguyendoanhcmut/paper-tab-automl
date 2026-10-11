  * **Hình 1.** Quy trình 4 bước phát triển mô hình hồi quy logistic cho MPBR
    * <img src="assets/fig_01_p4.jpeg" alt="Hình 1" />
    * **Hình này chứng minh điều gì**
      * Chuỗi quy trình liên kết $N$ mô hình LR song song và tỷ số chênh ($OR$) vào vòng lặp thích ứng để tối ưu hóa tái sử dụng nước ($p_{reuse}$).
    * **Từ đâu mà thấy được**
      * Trục đọc từ trên xuống dưới qua 4 khối quy trình nối tiếp nhau bằng các mũi tên đỏ lớn (Step 1 đến Step 4).
      * Khối Step 2 biểu diễn mặt xác suất $p$ và bậc thang nồng độ $NH_4\text{-}N_{eff}$; khối Step 3 thể hiện đồ thị $OR$ theo nồng độ $0\text{--}16\text{ mg/L}$.
      * Khối Step 4 chứa chu trình mũi tên đỏ "iterative prediction" và đồ thị vận hành $0\text{--}100\text{ d}$ theo dõi xác suất tái sử dụng $p_{reuse}$.
