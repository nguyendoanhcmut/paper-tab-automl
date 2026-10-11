  * **Bảng 6.** Thống kê các tập dữ liệu thực nghiệm (Dataset statistics).
    * <img src="assets/table_06_p18.png" alt="Bảng 6" />
    * **Hình này chứng minh điều gì**
      * Nghiên cứu thiết lập một hệ thống đánh giá thực nghiệm toàn diện gồm $29$ bộ dữ liệu dạng bảng phân bố trên 3 nhóm bài toán: phân loại nhị phân ($7$ bộ), phân loại đa lớp ($12$ bộ) và hồi quy ($10$ bộ) với dải kích thước mẫu và số chiều đặc trưng phong phú.
    * **Từ đâu mà thấy được**
      * Bảng phân định rõ ba nhóm bài toán: 7 tập Binary Classification, 12 tập Multi-class Classification, và 10 tập Regression.
      * Số chiều đặc trưng (#Features) dao động rộng từ $4$ đến $279$ (arrhythmia: $279$, myocardial: $111$, communities: $103$).
      * Kích thước mẫu (#Samples) trải từ cỡ nhỏ $315$ mẫu (plasma_retinol) đến cỡ lớn $581.012$ mẫu (covtype) và $253.680$ mẫu (cdc diabetes).
      * Nguồn thu thập và mã định danh (Source, ID/Name) minh chứng nguồn gốc dữ liệu từ OpenML, Kaggle, và UCI.
