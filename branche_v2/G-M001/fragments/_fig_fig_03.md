    * **Hình 3.** Quy trình tổng thể của phương pháp tinh chỉnh siêu tham số ANN-RSM đề xuất
      * <img src="assets/fig_03_p10.jpeg" alt="Hình 3" />
      * **Hình này chứng minh điều gì**
        * Quy trình đề xuất chuẩn hóa việc tối ưu siêu tham số ANN qua 3 giai đoạn khép kín: chuẩn bị dữ liệu, tối ưu hóa bằng RSM với DOE (sàng lọc 2 mức và CCD), và thẩm định độc lập có cơ chế phản hồi lặp theo độ thỏa dụng (desirability).
      * **Từ đâu mà thấy được**
        * Khối màu xanh lá (Data collection and preprocessing): Dữ liệu sau tiền xử lý được chia ngẫu nhiên thành 60% huấn luyện (Ttraining) cấp cho RSM và 40% kiểm định (Ttesting) đưa tới bước đánh giá.
        * Khối màu cam (Proposed ANN-RSM Hyperparameter optimization): Tiến hành sàng lọc 2 mức (2-level factorial), bổ sung điểm thực nghiệm CCD, kiểm định ANOVA/chẩn đoán (có vòng lặp cải thiện) và đề xuất nghiệm tối ưu theo hàm desirability.
        * Khối màu xanh dương (Model validation): Mạng được huấn luyện lại và kiểm tra; nhánh "No" tại "Test model good?" tạo vòng lặp quay lại nhận giải pháp tiếp theo từ RSM cho đến khi chọn được mô hình tối ưu nhất.
