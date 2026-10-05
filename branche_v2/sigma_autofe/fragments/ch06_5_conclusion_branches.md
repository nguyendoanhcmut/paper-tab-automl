## 5. Conclusion

* **Tóm tắt đóng góp chính của khung tối ưu hóa SIGMA (Main Contributions)**:
  * *Đề xuất khung tối ưu hóa*: Bài báo đề xuất SIGMA, một khung tối ưu hóa với độ dài ngữ cảnh không đổi (scalable constant-context optimization framework) mới lạ và có khả năng mở rộng quy mô cho kỹ thuật tạo đặc trưng tự động dựa trên mô hình ngôn ngữ lớn mà không cần siêu dữ liệu ngữ nghĩa (metadata-free LLM-based AutoFE).
  * *Định hướng tác vụ bằng giá trị SHAP*: Thay vì phụ thuộc vào thông tin ngữ nghĩa (semantic information), SIGMA khai thác các giá trị SHAP (SHAP values) để định hướng quá trình sinh đặc trưng nhận biết tác vụ (task-aware generation), đồng thời giới thiệu chiến lược sinh đặc trưng theo nhóm (grouped generation strategy) nhằm khám phá không gian đặc trưng có cấu trúc (structured feature exploration).
  * *Kiểm soát quỹ đạo ngầm định với EXIT*: Để kích hoạt khả năng tối ưu hóa chu kỳ dài (long-horizon optimization) với tỷ lệ sinh đặc trưng trùng lặp thấp (low duplicate generation rate), SIGMA giới thiệu cơ chế EXIT nhằm sử dụng các đặc trưng được phơi bày trực tiếp trong prompt (exposed features), theo dõi và định hướng quỹ đạo tối ưu theo phương thức ngầm định (implicit way).
  * *Kết quả thực nghiệm vượt trội*: Thực nghiệm chứng minh SIGMA đạt hiệu năng tương đương với các mô hình cơ sở dựa trên LLM hiện tại (LLM-based baselines) trong khi duy trì độ dài ngữ cảnh gần như không đổi (nearly constant context), đồng thời giữ vững tính cạnh tranh với các phương pháp AutoFE truyền thống (traditional AutoFE) nhờ hiệu quả khai thác và sử dụng đặc trưng cao (efficient feature utilization).
* **Các hạn chế còn tồn tại (Limitations)**:
  * *Ràng buộc thao tác còn yếu*: Các ràng buộc thao tác/phép biến đổi (operation restrictions) hiện tại vẫn còn lỏng lẻo, dẫn đến tỷ lệ trùng lặp đặc trưng sinh ra (duplicate rate) vẫn ở mức xấp xỉ $7\%$ (nearly $7\%$).
  * *Giới hạn phạm vi bài toán*: SIGMA hiện chỉ tập trung chuyên biệt vào bài toán phân loại trên dữ liệu bảng (tabular classification task); bài toán hồi quy (regression task) cũng như các thiết lập mở rộng khác vẫn chưa được xử lý và cần được xem xét.
  * *Nguy cơ quá khớp (Overfitting)*: Tồn tại hiện tượng quá khớp với tập kiểm định (validation set), được phản ánh qua sự suy giảm hiệu năng (performance degradation) trên tập kiểm thử (đặc biệt là nguy cơ quá khớp trên các tập dữ liệu có kích thước rất nhỏ).
* **Hướng phát triển trong tương lai (Future Work)**:
  * *Mở rộng tập dữ liệu và bài toán*: Tập trung tích hợp và đánh giá trên các tập dữ liệu đa dạng hơn, mở rộng hỗ trợ cho bài toán hồi quy (regression task) cũng như các miền dữ liệu đa phương thức.
  * *Nâng cao phương pháp lựa chọn thao tác*: Giải quyết triệt để vấn đề quá khớp (overfitting) và cải thiện hơn nữa hiệu năng thông qua việc tiếp cận cơ chế lựa chọn phép toán/thao tác (operation selection approach) mạnh mẽ hơn.
* **Tính sẵn có của mã nguồn (Code Availability)**:
  * Mã nguồn của SIGMA được công khai tại kho lưu trữ: `https://github.com/shiralab/SIGMA/`.
