### 4.5 Ablation Study

- **Mục tiêu và thiết lập thực nghiệm của nghiên cứu cắt bỏ thành phần (ablation study)**:
  - **Mục tiêu**: Đánh giá định lượng mức độ đóng góp độc lập của từng thành phần cốt lõi trong framework LLM-FE đối với hiệu năng tổng thể.
  - **Tập dữ liệu thử nghiệm**: Thực hiện trên nhóm classification datasets (tập dữ liệu phân loại) có quy mô dưới $10{,}000$ mẫu ($< 10{,}000$ samples) được liệt kê trong Table 2.
  - **Cấu hình mô hình thực nghiệm**: Sử dụng XGBoost làm prediction model (mô hình dự đoán) và GPT-3.5-Turbo làm LLM backbone (mô hình ngôn ngữ lớn nền tảng).
  - **Chỉ số đánh giá**: Báo cáo accuracy (độ chính xác) được tổng hợp (aggregated) và chuẩn hóa (normalized) trên toàn bộ các tập dữ liệu nhằm đảm bảo tính so sánh công bằng (fair comparison). Mô hình LLM-FE đầy đủ đạt độ chính xác chuẩn hóa là $0.687$.

- **Tác động của từng thành phần lên hiệu năng tổng thể của LLM-FE**:
  - **Hình 2.** Kết quả ablation study tổng hợp trên các tập dữ liệu phân loại
    - <img src="assets/fig_02_p8_vector.png" alt="Hình 2" />
    - **Hình này chứng minh điều gì**
      - Mọi thành phần đều đóng góp tích cực vào hiệu năng của LLM-FE, trong đó Evolutionary Refinement và Domain Knowledge đóng vai trò quyết định lớn nhất.
    - **Từ đâu mà thấy được**
      - Trục tung Accuracy sụt giảm từ $0.687$ (LLM-FE) xuống $0.644$ khi bỏ Data Examples, giảm mạnh còn $0.626$ khi bỏ Domain Knowledge, và thấp nhất là $0.587$ khi bỏ Evolutionary Refinement.
  - **Ảnh hưởng của cơ chế tinh chỉnh tiến hóa (w/o Evolutionary Refinement)**:
    - Việc loại bỏ cơ chế evolutionary refinement (tinh chỉnh tiến hóa) dẫn đến mức sụt giảm hiệu năng nghiêm trọng nhất trong tất cả các biến thể, đưa accuracy xuống còn $0.587$ (giảm $0.100$ so với LLM-FE gốc).
    - Kết quả này nhấn mạnh tầm quan trọng cốt lõi của iterative data-driven feedback (phản hồi lặp dựa trên dữ liệu) kết hợp cùng tri thức miền để sàng lọc và cải tiến các feature transforms (phép biến đổi đặc trưng).
  - **Ảnh hưởng của tri thức miền (w/o Domain Knowledge)**:
    - Trong cấu hình loại bỏ domain knowledge (tri thức miền), toàn bộ chi tiết đặc thù về tác vụ và tập dữ liệu bị xóa bỏ khỏi prompt (lời nhắc); tên các thuộc tính đặc trưng bị anonymized (ẩn danh hóa) bằng các ký hiệu giữ chỗ tổng quát như $C_1, C_2, \dots, C_n$.
    - Việc triệt tiêu hoàn toàn semantic meaning (ý nghĩa ngữ nghĩa) làm mất đi contextual insights (hiểu biết sâu về ngữ cảnh bài toán), khiến hiệu năng sụt giảm đáng kể xuống $0.626$ (giảm $0.061$).
    - Minh chứng vai trò then chốt của tri thức miền trong việc định hướng mô hình sinh ra các đặc trưng có ý nghĩa thực tiễn.
  - **Ảnh hưởng của các mẫu dữ liệu minh họa (w/o Data Examples)**:
    - Biến thể loại bỏ data examples (mẫu dữ liệu minh họa) chỉ gây ra mức sụt giảm nhẹ về hiệu năng, đạt accuracy $0.644$ (giảm $0.043$).
    - Nguyên nhân xuất phát từ việc LLM có thể gặp khó khăn trong việc nắm bắt toàn diện các sắc thái vi mô và quy luật phân phối phức tạp (nuances and patterns) chỉ từ một số ít mẫu dữ liệu được cung cấp trong prompt.
  - **Kết luận chung về kiến trúc**:
    - LLM-FE hưởng lợi rõ rệt từ sự hiệp đồng của tất cả các thành phần cấu thành, giúp framework đạt được sự cải thiện vượt trội trong kỹ thuật đặc trưng.
