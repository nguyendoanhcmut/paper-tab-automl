### 4.3. Comparison with Traditional AutoFE

- **Sự đánh đổi giữa số lượng đặc trưng và mức tăng hiệu năng (Hình 2(b)):**
  - Trong khi DFS và OpenFE cho phép kiểm soát tường minh số lượng đặc trưng được chấp nhận $K$, SIGMA và AutoFeat không hỗ trợ trực tiếp kiểm soát ngân sách đặc trưng (feature budget).
  - Do đó, trên đồ thị đánh đổi, SIGMA và AutoFeat được biểu diễn dưới dạng một điểm đơn lẻ, tương ứng với số lượng đặc trưng trung bình được tạo ra trên toàn bộ các tập dữ liệu.
  - Khi giữ lại toàn bộ đặc trưng sinh ra, DFS sinh trung bình $724.8$ đặc trưng và OpenFE sinh trung bình $1556$ đặc trưng trên mỗi tập dữ liệu.
  - Mặc dù đem lại mức tăng hiệu năng đáng kể, các phương pháp truyền thống thường đưa vào nhiều đặc trưng gây nhiễu (noisy features), khiến cơ chế tác động cốt lõi của chúng gần như không thể diễn giải được (uninterpretable).
  - Dưới các thiết lập có ràng buộc ngân sách, OpenFE vẫn duy trì năng lực sinh đặc trưng mạnh mẽ (do là phương pháp AutoFE truyền thống mạnh nhất hiện nay), trong khi hiệu năng của DFS chịu sự biến động rất lớn.

- **Hiệu quả sử dụng đặc trưng vượt trội của SIGMA:**
  - So với các phương pháp truyền thống, SIGMA đạt mức cải thiện hiệu năng gần $0.8\%$ F1-score với số lượng đặc trưng được chấp nhận trung bình chỉ là $5.4$ đặc trưng.
  - Điều này chứng minh SIGMA có khả năng tìm ra các đặc trưng triển vọng nhất ngay cả trong điều kiện bị ràng buộc ngân sách chặt chẽ, đồng thời cung cấp khả năng diễn giải rõ ràng cho các đặc trưng được sinh ra.

- **So sánh hiệu năng F1-score dưới cùng ngân sách đặc trưng $K = 20$ (Bảng 2):**
  - Dưới ngân sách đặc trưng cố định $K = 20$, SIGMA đạt kết quả F1-score rất cạnh tranh ($79.80\% \pm 0.23\%$, thứ hạng trung bình 2.69), chỉ chênh lệch tối thiểu $0.2\%$ so với OpenFE ($80.01\%$, thứ hạng trung bình 2.19).
  - Cả SIGMA và OpenFE đều vượt trội hơn hẳn so với baseline không dùng AutoFE ($79.09\%$, hạng 3.31), AutoFeat ($79.08\%$, hạng 3.44) và DFS ($79.27\%$, hạng 3.38).
  - Đáng chú ý, SIGMA đạt được kết quả này chỉ với xấp xỉ $5$ đặc trưng được chấp nhận (chính xác là trung bình $5.4$ đặc trưng), ít hơn rất nhiều so với toàn bộ ngân sách $K = 20$, cho thấy mức độ khai thác hiệu quả dung lượng đặc trưng vượt bậc.
  - Lợi thế về hiệu quả đặc trưng cao giúp SIGMA trở thành một giải pháp thay thế mang tính thực tiễn cao trong các môi trường triển khai bị hạn chế tài nguyên tính toán và lưu trữ.

- **Cấu trúc tô-pô đặc trưng sâu làm tiền đề cho nghiên cứu trường hợp (Case Study):**
  - Mặc dù phân tích định tính chi tiết về các đặc trưng này thuộc về Mục 4.4, sự vượt trội về mặt hiệu năng của SIGMA trên các tập dữ liệu như `jungle chess` ($92.62\%$ so với $90.41\%$ của OpenFE và $86.89\%$ của baseline) và `compass` ($77.97\%$ so với $77.27\%$ của OpenFE và $75.07\%$ của baseline) gắn liền với cấu trúc tô-pô đặc trưng phức tạp được minh họa trong Hình 3.
  - **Hình 3.** Cấu trúc tô-pô của các đặc trưng được sinh ra trên tập jungle chess và compass
    - <img src="assets/fig_03_p9_vector.png" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - SIGMA có khả năng sinh ra các đặc trưng lồng nhau với cấu trúc tô-pô sâu (độ sâu lên đến 9)
    - **Từ đâu mà thấy được**
      - Cây biểu thức biểu diễn đặc trưng (a) jungle chess với độ sâu 9 tầng phép toán và (b) compass
