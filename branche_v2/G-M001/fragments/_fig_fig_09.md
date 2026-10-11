    * **Hình 9.** Thông lượng dòng thấm và đồ thị tương quan thực nghiệm - dự báo của các mô hình RBFNN trên tập kiểm tra (testing dataset)
      * <img src="assets/fig_09_p20.jpeg" alt="Hình 9" />
      * **Hình này chứng minh điều gì**
        * Cả mô hình RBFNN thông thường và RBFNN-RSM đều đạt độ chính xác dự báo rất cao và tương đương nhau trên tập dữ liệu kiểm tra, chứng minh cấu trúc tối ưu của RBFNN-RSM duy trì trọn vẹn hiệu năng dự báo.
      * **Từ đâu mà thấy được**
        * Đồ thị (a): Đường dự báo của RBFNN và RBFNN-RSM bám rất sát giá trị thực nghiệm qua toàn bộ 1600 mẫu kiểm tra với sai số toàn phương trung bình rất nhỏ ($\text{MSE} \approx 0{,}0264\text{--}0{,}0265$).
        * Đồ thị (b, c): Điểm dữ liệu phân bố tập trung cao dọc theo đường hồi quy tuyến tính với hệ số tương quan xuất sắc ($R = 0{,}9867$, $R^2 = 0{,}9734$ ở RBFNN; $R = 0{,}9857$, $R^2 = 0{,}9715$ ở RBFNN-RSM).
