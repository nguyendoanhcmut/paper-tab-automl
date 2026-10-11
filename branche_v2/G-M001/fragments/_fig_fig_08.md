    * **Hình 8.** Thông lượng dòng thấm và đồ thị tương quan thực nghiệm - dự báo của các mô hình FFNN trên tập kiểm tra (testing dataset)
      * <img src="assets/fig_08_p19.jpeg" alt="Hình 8" />
      * **Hình này chứng minh điều gì**
        * Tất cả 5 mô hình FFNN đều được kiểm chứng thành công trên tập kiểm tra (testing dataset) với độ chính xác cao và bám sát dữ liệu thực nghiệm; trong đó mô hình FFNN-2 đạt hiệu năng dự báo tốt nhất.
      * **Từ đâu mà thấy được**
        * Đồ thị chuỗi (a) cho thấy đường thông lượng dự báo của cả 5 mô hình bám rất sát thực nghiệm qua 1.600 điểm kiểm tra, trong đó FFNN-2 đạt MSE thấp nhất (0,0256), tiếp theo là FFNN-RSM (0,0264), FFNN-1 (0,0268), FFNN-4 (0,0290) và FFNN-3 (0,0343 có độ lệch nhẹ).
        * Đồ thị tương quan (b)–(f) thể hiện các điểm dữ liệu phân bố tập trung cao dọc đường hồi quy tuyến tính với hệ số tương quan R rất lớn: FFNN-2 đạt cao nhất (R = 0,9871; R² = 0,9744), kế tiếp là FFNN-RSM (0,9867), FFNN-1 (0,9865), FFNN-4 (0,9854) và FFNN-3 (0,9827).
