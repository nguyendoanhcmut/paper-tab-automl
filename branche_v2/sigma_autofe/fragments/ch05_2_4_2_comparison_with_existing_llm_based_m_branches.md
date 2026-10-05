### 4.2. Comparison with Existing LLM-Based Methods

- **So sánh hiệu năng F1-score của các phương pháp AutoFE dựa trên LLM (Bảng 1)**:
  - Thử nghiệm sử dụng mô hình nền tảng Qwen3-4B-Instruct-2507 trên 16 bộ dữ liệu phân loại dạng bảng (tabular classification datasets).
  - SIGMA đạt hiệu năng cạnh tranh trực tiếp với CAAFE (phương pháp khai thác mô tả ngữ nghĩa chi tiết): điểm F1 trung bình đạt $79.80 \pm 0.23$ so với $79.78 \pm 0.18$ của CAAFE.
  - Kết quả này chứng minh rằng các phương pháp AutoFE dựa trên LLM hoàn toàn có thể sinh các đặc trưng hiệu quả cao mà không cần phụ thuộc vào mô tả ngữ nghĩa (metadata-free).
  - So với OCTree (phương pháp cùng không sử dụng siêu dữ liệu), SIGMA vượt trội một cách nhất quán trên phần lớn các bộ dữ liệu (F1 trung bình $79.80$ so với $79.02 \pm 0.31$ của OCTree).
  - Thứ hạng trung bình (Avg Rank): SIGMA đạt thứ hạng cao nhất trong toàn bộ các phương pháp so sánh với $2.06$, vượt trội hơn CAAFE ($2.31$), Baseline không dùng AutoFE ($2.75$) và OCTree ($2.81$).

- **Phân tích hiệu quả sử dụng token prompt trong quá trình tối ưu hóa**:
  - Cả hai khung AutoFE dựa trên LLM trước đó đều bộc lộ xu hướng gia tăng liên tục độ dài prompt qua các bước tối ưu hóa liên tiếp.
  - CAAFE không thiết lập giới hạn trên cho lịch sử quỹ đạo, dẫn đến sự bùng nổ độ dài ngữ cảnh vượt quá 15,000 token (đạt đỉnh tới 15,786 token), làm hạn chế chân trời tối ưu hóa do chi phí tính toán tăng vọt.
  - OCTree áp dụng giới hạn quỹ đạo bằng cách chỉ lưu lại 7 đặc trưng có hiệu năng tốt nhất (top-7 performing features), giúp giữ mức tiêu thụ token thấp ($\approx 1,034$ token).
  - Tuy nhiên, việc giới hạn của OCTree khiến quá trình tối ưu hóa dễ bị mắc kẹt tại cực trị địa phương (local optima) khi LLM không thể sinh ra đặc trưng tốt hơn top-7; việc thiếu sự tiến hóa của prompt buộc hệ thống chỉ dựa vào lấy mẫu ngẫu nhiên (stochastic sampling) để thoát bế tắc, dẫn đến hiệu năng tổng thể dưới mức trung bình.
  - Ngược lại, SIGMA duy trì độ dài ngữ cảnh gần như không đổi trong suốt các bước lặp, thể hiện qua độ biến thiên token đỉnh - đáy nhỏ nhất (dao động trong khoảng 520 đến 1,739 token), cho phép tinh chỉnh lặp lại bền vững trên chân trời dài hạn (long-horizon optimization) mà không gặp hiện tượng bùng nổ chi phí.
  - Do SIGMA sinh 2 đặc trưng ở mỗi bước lặp, ngân sách 50 đặc trưng hoàn thành chỉ sau 25 bước lặp (Step 25) thay vì 50 bước như các phương pháp khác.
  - **Hình 2.** Phân tích hiệu quả sử dụng token và đặc trưng của các phương pháp
    - <img src="assets/fig_02_p8_vector.png" alt="Hình 2" />
    - **Hình này chứng minh điều gì**
      - SIGMA duy trì độ dài prompt token gần như không đổi qua các bước lặp so với sự bùng nổ ngữ cảnh của CAAFE và OCTree
    - **Từ đâu mà thấy được**
      - Đồ thị (a): trục hoành là bước lặp (Step 0-50, SIGMA 25 bước), trục tung là Prompt tokens (thang log), CAAFE tăng vọt đến >15k token, OCTree ~1k token, SIGMA ổn định hằng số
  - Cơ chế EXIT (EXposed-feature Implicit Trajectory) thay thế chiến lược bị động (phụ thuộc vào khả năng tự thân của LLM) bằng sự định hướng chủ động: EXIT chủ động điều chỉnh các đặc trưng bộc lộ (exposed features) trong prompt nhằm giảm xác suất đồng xuất hiện của các đặc trưng trùng lặp, ngăn ngừa rơi vào cực trị địa phương.

- **Kết luận tổng thể về so sánh với các phương pháp LLM-based**:
  - Khung AutoFE dựa trên LLM vẫn đạt được hiệu năng vượt trội ngay cả khi hoàn toàn vắng mặt thông tin ngữ nghĩa.
  - Bằng cách cung cấp quỹ đạo ngầm định thông qua các đặc trưng bộc lộ, EXIT giúp SIGMA duy trì độ dài ngữ cảnh ổn định trong suốt chu trình lặp, mở ra khả năng tối ưu hóa dài hạn trên quy mô lớn.
