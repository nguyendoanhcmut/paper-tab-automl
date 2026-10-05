## 2 METHODS

- Khung phương pháp nghiên cứu dự đoán nồng độ $T\text{-}P$ đầu ra theo thang ngày và tối ưu hóa vận hành hệ thống DAF gồm 3 giai đoạn kế tiếp:
  - Giai đoạn 1 (Tiền xử lý và kỹ nghệ đặc trưng): Thu thập dữ liệu đa nguồn, sàng lọc ngoại lai theo $3\sigma$, điền khuyết dữ liệu chuỗi thời gian bằng thuật toán MICE và kỹ nghệ đặc trưng tích hợp cơ chế thủy lực, động học ngắn hạn cùng biến đổi theo mùa.
  - Giai đoạn 2 (Phát triển và đánh giá mô hình): Huấn luyện 4 thuật toán học máy hồi quy trên tập đặc trưng kỹ nghệ, tối ưu hóa siêu tham số bằng kỹ thuật Bayesian Optimization và đánh giá độ chính xác qua các chỉ số thống kê tiêu chuẩn ($R^2$, $\text{RMSE}$, $\text{MAE}$).
  - Giai đoạn 3 (Giải thích mô hình và tối ưu hóa vận hành): Áp dụng phương pháp SHAP định lượng tầm quan trọng và tương tác giữa các đặc trưng, thiết lập mô phỏng tự hồi quy theo kịch bản để phân tích độ nhạy của $T\text{-}P$ đầu ra trước các mức điều chỉnh liều lượng phèn sắt $Fe_2(SO_4)_3$.
