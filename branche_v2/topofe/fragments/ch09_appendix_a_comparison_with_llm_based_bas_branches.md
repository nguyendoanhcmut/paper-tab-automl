## Appendix A Comparison with LLM-based Baseline

- Phân tích đối chiếu toàn diện giữa TOPOFE và các phương pháp kỹ nghệ đặc trưng dựa trên mô hình ngôn ngữ lớn (LLM-based Feature Engineering) tiền nhiệm dọc theo 7 chiều kích kiến trúc cốt lõi.
  - Các phương pháp đường cơ sở (baselines) được so sánh bao gồm: CAAFE, FeatLLM, OCTree và LLM-FE.
  - Bảng tổng hợp đối chiếu 7 chiều kích kỹ thuật giữa TOPOFE và các baseline:
    | Chiều kích kiến trúc | CAAFE | FeatLLM | OCTree | LLM-FE | TOPOFE |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | **Chiến lược khám phá (Exploration Strategy)** | Khám phá tham lam, tuần tự quỹ đạo đơn | Nhiều truy vấn song song độc lập, không tương tác | Tối ưu hóa lặp tuần tự từng luật trên quỹ đạo đơn | Tiến hóa quần thể đơn chia thành các bộ đệm đảo (island buffers) | Tiến hóa đa đảo chuyên biệt theo họ toán tử, phối hợp chéo liên đảo khi bão hòa |
    | **Không gian tìm kiếm (Search Space)** | Biểu thức mã không ràng buộc (thực tế co cụm về số học đơn giản) | Thu hẹp chủ đích vào luật ngưỡng và luật thuộc lớp theo từng lớp | Luật ngôn ngữ tự nhiên không định nghĩa trước không gian toán tử | Toàn bộ chương trình biến đổi trên một ngữ pháp phẳng đơn lẻ | Phân vùng thành các không gian con có kiểu ngữ nghĩa; tổng hợp lai chéo họ |
    | **Quản lý bộ nhớ (Memory Management)** | Chỉ nhớ đặc trưng được chấp thuận và lỗi thực thi gần nhất | Phi trạng thái hoàn toàn (stateless, không lưu vết giữa các lần thử) | Lưu toàn bộ quỹ đạo lịch sử, điểm số và lập luận cây quyết định | Bộ đệm lưu trữ các chương trình điểm cao (chỉ lưu winner) | Bộ nhớ kép: Elite Archive (mẫu ưu tú) + Prompt Adaptation Memory (tín hiệu prefer/avoid) |
    | **Quản lý cá thể ưu tú (Elite Management)** | Không có archive tường minh (tập đặc trưng hiện tại là elite) | Không lưu giữ elite (ensemble trung bình tất cả lượt thử) | Chỉ giữ duy nhất luật tốt nhất cho mỗi đặc trưng | Elite buffer gom cụm theo điểm số, khử trùng lặp theo chữ ký hiệu năng | Elite archive có chặn kích thước từng đảo, khử trùng lặp theo cấu trúc cú pháp |
    | **Tín hiệu phản hồi cho LLM (Feedback Signal)** | Thay đổi hiệu năng vô hướng kèm thông báo lỗi thực thi | Không phản hồi lặp (chỉ có prompt few-shot tĩnh) | Điểm kiểm định kèm suy luận cây quyết định tóm tắt dữ liệu | Điểm kiểm định kèm chương trình điểm cao làm mẫu ngữ cảnh | Fitness score kèm mẫu ưu tú và tín hiệu prefer/avoid tóm tắt trải nghiệm tìm kiếm |
    | **Mục tiêu tối ưu hóa (Optimization Objective)** | Tối đa hóa hiệu năng phân loại trên tập kiểm định | Cực tiểu hóa hàm mất mát của mô hình đơn giản trên luật nhị phân | Cực tiểu hóa mất mát kiểm định độc lập cho từng luật | Tối đa hóa điểm kiểm định của chương trình tốt nhất tìm được | Hàm mục tiêu đa thành phần: hiệu năng, phạt tương quan dư thừa, độ ổn định fold, chi phí |
    | **Tính song song & Hiệu quả (Parallelism & Efficiency)** | Tuần tự nghiêm ngặt (inherently sequential) | Song song hiển nhiên (trivially parallel) | Tuần tự nghiêm ngặt (inherently sequential) | Song song về mặt nguyên lý | Song song theo thiết kế đa đảo; chi phí điều phối không đáng kể qua bão hòa |

### (i) Chiến lược khám phá (Exploration Strategy)

- Các phương pháp đường cơ sở khám phá theo quỹ đạo đơn độc lập hoặc hoán đổi lẫn nhau mà không có sự chuyên biệt hóa:
  - CAAFE áp dụng chiến lược tham lam và tuần tự: đề xuất từng đặc trưng ứng viên (candidate feature) đơn lẻ tại mỗi bước, chấp nhận hoặc loại bỏ dựa trên hiệu năng kiểm định (validation performance), và lặp lại trong một số lượng vòng lặp cố định.
  - FeatLLM thực thi nhiều truy vấn LLM độc lập song song, tuy nhiên các lượt thử nghiệm (trials) hoàn toàn cô lập và không bao giờ tương tác hay trao đổi thông tin với nhau.
  - OCTree tuân theo quy trình tối ưu hóa lặp trên một quỹ đạo đơn (single-trajectory iterative optimization), tinh chỉnh từng luật một trước khi chuyển sang xử lý đặc trưng tiếp theo.
  - LLM-FE thực hiện tìm kiếm tiến hóa (evolutionary search) trên một quần thể đơn lẻ được phân chia thành các bộ đệm đảo (island buffers), trong đó toán tử đột biến (mutation) và lai ghép (crossover) chỉ được hiện thực hóa ngầm định thông qua việc tạo sinh có điều kiện bằng câu nhắc (prompt-conditioned generation).
- TOPOFE duy trì các quỹ đạo tìm kiếm phân hóa theo thiên kiến quy nạp (inductive bias) và được điều phối chủ động:
  - Hệ thống tiến hóa song song nhiều đảo chuyên biệt hóa theo từng họ đặc trưng/toán tử (family-specialized islands), mỗi đảo sở hữu các toán tử đột biến và lai ghép tường minh do LLM dẫn dắt.
  - Tích hợp cơ chế khám phá liên đảo được kích hoạt theo ngưỡng bão hòa (saturation-triggered cross-island exploration) khi tiến trình nội đảo chậm lại.
  - Điểm khác biệt cốt lõi (essential delta): Mọi baseline đều đi theo một lộ trình duy nhất (CAAFE, OCTree), các lộ trình độc lập không tương tác (FeatLLM), hoặc các lộ trình hoán đổi tương đương (LLM-FE); trong khi đó ở TOPOFE, mỗi đảo nhận thức rõ loại đặc trưng chuyên biệt mà nó đang tìm kiếm và học được cách mượn thông tin/vật liệu từ các đảo khác một cách chiến lược.

### (ii) Không gian tìm kiếm (Search Space)

- Không gian tìm kiếm của các phương pháp cơ sở bị giới hạn hoặc suy thoái trong thực tế:
  - CAAFE cho phép các biểu thức mã không ràng buộc (unconstrained code expressions) trên lý thuyết, nhưng trong thực tế không gian này nhanh chóng suy thoái thành các tổ hợp số học đơn giản (simple arithmetic combinations).
  - FeatLLM chủ động thu hẹp không gian tìm kiếm vào các luật ngưỡng (threshold rules) và luật thuộc về lớp (membership rules) phân theo từng lớp (per-class) trên các đặc trưng riêng lẻ (individual features).
  - OCTree tìm kiếm trên các luật diễn đạt bằng ngôn ngữ tự nhiên (natural-language rules) và sau đó mới chuyển đổi thành mã thực thi, hoàn toàn không có một không gian toán tử được định nghĩa trước (no pre-defined operator space).
  - LLM-FE tìm kiếm trong không gian của toàn bộ các chương trình biến đổi đặc trưng hoàn chỉnh, nhưng chỉ dựa trên một ngữ pháp phẳng đơn lẻ không phân hóa (one undifferentiated grammar).
- TOPOFE thiết lập cấu trúc không gian chương trình có định kiểu ngữ nghĩa và hỗ trợ tổng hợp lai:
  - TOPOFE tìm kiếm toàn bộ các chương trình biến đổi đặc trưng nhưng phân vùng không gian thành các không gian con có kiểu ngữ nghĩa rõ ràng (semantically typed subspaces).
  - Mở rộng phạm vi tiếp cận đến các không gian kết hợp liên họ (joint compositional spaces between families) thông qua cơ chế tổng hợp lai (hybrid synthesis).
  - Điểm khác biệt cốt lõi: TOPOFE là phương pháp duy nhất phân rã không gian chương trình thành các không gian con có định kiểu và xem việc kết hợp chéo giữa các họ toán tử là mục tiêu được kích hoạt tường minh và có chủ đích; trái lại LLM-FE có độ biểu đạt thô tương đương nhưng dùng ngữ pháp phẳng, FeatLLM tự giới hạn vào luật đơn giản, còn CAAFE không bị ràng buộc trên lý thuyết nhưng lại nghèo nàn trong thực tế.

### (iii) Quản lý bộ nhớ (Memory Management)

- Sự thiếu hụt hoặc phi đối xứng trong cơ chế lưu vết lịch sử tìm kiếm ở các baseline:
  - CAAFE chỉ ghi nhớ tập đặc trưng đã được chấp nhận và lỗi thực thi gần nhất; các đặc trưng bị từ chối hoàn toàn không để lại dấu vết, dẫn đến hiện tượng LLM lặp lại các ý tưởng thất bại gần như trùng lặp (near-duplicates of failed ideas).
  - FeatLLM hoàn toàn phi trạng thái (fully stateless); mỗi lượt thử nghiệm là một lệnh gọi LLM độc lập và không tồn tại bộ nhớ liên kết giữa các lượt.
  - OCTree lưu giữ toàn bộ quỹ đạo tối ưu hóa lịch sử gồm các luật trước đó, điểm số tương ứng và lập luận đi kèm, rồi gửi lại toàn bộ khối lượng thông tin này cho LLM trong mỗi lượt gọi prompt.
  - LLM-FE duy trì một bộ đệm chứa các chương trình đạt điểm cao, nhưng chỉ lưu trữ duy nhất các ứng viên chiến thắng (stores winners only).
- TOPOFE thiết kế kiến trúc bộ nhớ kép (dual memory) cân bằng giữa mẫu thành công và bài học thất bại:
  - Kho lưu trữ ưu tú (Elite Archive): bảo tồn các chương trình mẫu mực (exemplar programs) có chất lượng cao nhất để tái sử dụng.
  - Bộ nhớ thích ứng câu nhắc (Prompt Adaptation Memory - PAM): tóm tắt cả lịch sử các ý tưởng được chấp thuận lẫn các ý tưởng bị từ chối của từng đảo thành một tín hiệu ngôn ngữ tự nhiên cô đọng "nên ưu tiên / nên tránh" (compact "prefer/avoid" signal), liên tục được cập nhật trong suốt quá trình tìm kiếm.
  - Lợi thế kỹ thuật: Ngăn ngừa việc lãng phí tài nguyên tính toán vào các biến thể của những ý tưởng đã thất bại, đồng thời chủ động định hướng LLM tập trung vào các hướng biến đổi tiềm năng.

### (iv) Quản lý cá thể ưu tú (Elite Management)

- Hạn chế về tính đa dạng và cơ chế lưu trữ cá thể ưu tú trong các baseline:
  - CAAFE không có kho lưu trữ tường minh: tập hợp đặc trưng hiện đang được chấp nhận đóng vai trò mặc định là tập ưu tú.
  - FeatLLM hoàn toàn không lưu giữ cá thể ưu tú; mô hình kết hợp cuối cùng chỉ đơn thuần tính trung bình đầu ra của tất cả các lượt thử nghiệm.
  - OCTree chỉ giữ lại duy nhất một luật đạt điểm cao nhất cho mỗi đặc trưng, hoàn toàn không duy trì một quần thể ứng viên đằng sau.
  - LLM-FE duy trì bộ đệm cá thể ưu tú gom cụm theo điểm số (score-clustered elite buffer) để lấy mẫu minh họa trong ngữ cảnh (in-context demonstrations), và khử trùng lặp chương trình dựa trên chữ ký hiệu năng (performance signature).
- TOPOFE áp đặt tính mới về cấu trúc và duy trì đa dạng cú pháp cho kho ưu tú:
  - TOPOFE duy trì một kho lưu trữ ưu tú có giới hạn kích thước theo từng đảo (bounded per-island elite archive), trong đó bắt buộc áp đặt tiêu chí tính mới về cấu trúc (structural novelty): các ứng viên có độ tương đồng cú pháp quá lớn với các thành viên hiện có sẽ bị loại bỏ.
  - Kho lưu trữ ưu tú thực hiện vai trò kép (dual role): vừa làm tập mẫu minh họa trong ngữ cảnh (in-context demonstration pool), vừa làm nguồn vật liệu hiến tặng (donor material) cho toán tử lai ghép chéo giữa các đảo (cross-island hybridization).
  - Tầm quan trọng của việc khử trùng lặp theo cấu trúc: Giữ cho kho lưu trữ luôn đa dạng cả về mặt hành vi lẫn cú pháp, ngăn ngừa tình trạng các cá thể cha mẹ dư thừa sinh ra các thế hệ con cháu trùng lặp và kém hiệu quả.

### (v) Tín hiệu phản hồi thông tin cho LLM (Feedback Signal to the LLM)

- Các hình thức phản hồi hiệu năng và dữ liệu của các baseline:
  - CAAFE phản hồi một giá trị vô hướng biểu thị mức độ thay đổi hiệu năng kèm theo các thông báo lỗi thực thi (nếu có).
  - FeatLLM không cung cấp bất kỳ phản hồi lặp nào (no iterative feedback); LLM chỉ quan sát các ví dụ few-shot cố định.
  - OCTree phản hồi điểm kiểm định kết hợp với lập luận suy diễn từ cây quyết định (decision-tree reasoning) bằng ngôn ngữ tự nhiên, qua đó cung cấp cho LLM tri thức về cấu trúc của tập dữ liệu.
  - LLM-FE phản hồi điểm kiểm định cùng các chương trình đạt điểm cao làm mẫu minh họa trực tiếp trong ngữ cảnh câu nhắc.
- Điểm khác biệt bản chất giữa TOPOFE và OCTree trong nhóm "phản hồi phong phú" (rich feedback):
  - TOPOFE cung cấp phản hồi tích hợp gồm: điểm thích nghi (fitness score), các chương trình mẫu mực ưu tú (elite exemplars), và tín hiệu ưu tiên đúc kết từ bộ nhớ câu nhắc (distilled preference signal from prompt memory).
  - Tính trực giao của thông tin phản hồi: Cây quyết định của OCTree tóm tắt cấu trúc dữ liệu (summarizes the data), trong khi bộ nhớ câu nhắc của TOPOFE tóm tắt kinh nghiệm tìm kiếm (summarizes the search experience).
  - TOPOFE chủ động định hướng phân phối đề xuất của LLM bằng một bản đúc kết tích lũy rõ ràng về việc những vùng nào trong không gian tìm kiếm là hiệu quả và vùng nào là ngõ cụt ("dead regions").

### (vi) Mục tiêu tối ưu hóa đa thành phần (Optimization Objective)

- Các baseline chỉ tập trung vào một chỉ số hiệu năng duy nhất:
  - CAAFE tối đa hóa hiệu năng phân loại trên tập kiểm định downstream.
  - FeatLLM cực tiểu hóa hàm mất mát của một mô hình đơn giản được khớp trên các đặc trưng luật nhị phân.
  - OCTree cực tiểu hóa mất mát kiểm định cho từng luật một cách hoàn toàn độc lập.
  - LLM-FE tối đa hóa điểm kiểm định của chương trình tốt nhất tìm được.
- TOPOFE thiết lập hàm mục tiêu chất lượng đặc trưng đa tiêu chí (multi-criteria property):
  - TOPOFE là phương pháp duy nhất tối ưu hóa một hàm mục tiêu tường minh đa thành phần kết hợp:
    1. Hiệu năng dự đoán mô hình hạ nguồn (downstream predictive performance).
    2. Thành phần phạt độ dư thừa (redundancy penalty) dựa trên hệ số tương quan từng cặp giữa các đặc trưng (pairwise feature correlations).
    3. Thành phần độ ổn định (stability term) tưởng thưởng sự nhất quán của đặc trưng qua các fold kiểm định (validation folds).
    4. Thành phần chi phí tính toán (computational cost term).
  - Hệ quả kỹ thuật: Việc chuẩn hóa chất lượng đặc trưng thành bài toán đa tiêu chí giúp TOPOFE vượt trội độc tôn cả về chỉ số giảm độ dư thừa lẫn độ bao phủ không gian con (subspace-coverage metrics), thay vì chỉ theo đuổi độ chính xác dự đoán thuần túy.

### (vii) Khả năng song song hóa và hiệu quả tính toán (Parallelism and Efficiency)

- Khả năng mở rộng và mức độ phụ thuộc tính toán giữa các phương pháp:
  - CAAFE và OCTree có bản chất tuần tự nghiêm ngặt (inherently sequential): mỗi vòng lặp phụ thuộc hoàn toàn vào kết quả của vòng lặp liền trước, không thể tận dụng tính toán phân tán.
  - FeatLLM có các lượt thử nghiệm độc lập nên có thể chạy song song một cách hiển nhiên (trivially parallel).
  - LLM-FE có thể song song hóa các đảo về mặt nguyên lý.
- Thiết kế song song hóa tự nhiên và chi phí điều phối tối thiểu của TOPOFE:
  - TOPOFE được thiết kế song song ngay từ cấu trúc cốt lõi (parallel by design): việc đánh giá và sinh đặc trưng trên các đảo diễn ra hoàn toàn độc lập với nhau.
  - Thời gian thực thi theo đồng hồ thực (wall-clock time) trên mỗi thế hệ được quyết định bởi đảo chạy chậm nhất, thay vì tăng tuyến tính theo tổng số lượng ứng viên được đánh giá.
  - Cơ chế trao đổi vật liệu di truyền liên đảo chỉ được kích hoạt khi bão hòa (saturation-triggered transfer) thay vì diễn ra liên tục, giúp chi phí điều phối (coordination overhead) ở mức không đáng kể.
