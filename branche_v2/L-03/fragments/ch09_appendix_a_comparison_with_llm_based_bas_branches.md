## Appendix A: Comparison with LLM-based Baseline

* **Mục tiêu so sánh tổng quan**: So sánh và tổng kết các khác biệt cốt lõi giữa TOPOFE và các phương pháp kỹ thuật đặc trưng tự động dựa trên mô hình ngôn ngữ lớn (LLM-based Automated Feature Engineering - AutoFE) khác, bao gồm CAAFE, FeatLLM, OCTree và LLM-FE, xuyên suốt 7 khía cạnh thiết kế kiến trúc.

* **(i) Chiến lược khám phá (Exploration Strategy):**
  * **CAAFE**: Khám phá theo chiến lược tham lam và tuần tự (*greedily and sequentially*): đề xuất từng đặc trưng ứng viên đơn lẻ tại một thời điểm, chấp nhận (*accept*) hoặc từ chối (*reject*) dựa trên hiệu năng trên tập kiểm định (*validation performance*), và lặp lại quy trình này trong một số lượng vòng lặp cố định (*fixed number of iterations*).
  * **FeatLLM**: Thực thi đồng thời nhiều truy vấn LLM độc lập song song (*independent LLM queries in parallel*), nhưng các thử nghiệm (*trials*) hoàn toàn tách biệt và không bao giờ tương tác với nhau (*never interact with one another*).
  * **OCTree**: Tuân theo quy trình tối ưu hóa lặp đơn quỹ đạo (*single-trajectory iterative optimization*), tinh chỉnh từng quy tắc một trước khi chuyển sang xử lý đặc trưng tiếp theo.
  * **LLM-FE**: Thực hiện tìm kiếm tiến hóa (*evolutionary search*) trên một quần thể đơn lẻ được phân tách thành các bộ đệm đảo (*island buffers*), trong đó các toán tử đột biến (*mutation*) và lai ghép (*crossover*) được hiện thực hóa một cách ngầm định (*implicitly*) thông qua quá trình sinh phụ thuộc câu nhắc (*prompt-conditioned generation*).
  * **TOPOFE**: Tiến hóa song song nhiều đảo chuyên biệt hóa theo từng họ toán tử (*family-specialized islands*), mỗi đảo sở hữu các toán tử đột biến và lai ghép tường minh do LLM điều khiển (*explicit LLM-driven mutation and crossover operators*), đồng thời bổ sung tầng khám phá liên đảo được kích hoạt bởi sự bão hòa (*saturation-triggered cross-island exploration*).
  * **Điểm khác biệt căn bản (*Essential delta*)**: Mọi phương pháp đối chuẩn đều khám phá theo:
    * Hoặc một đường dẫn duy nhất (CAAFE, OCTree);
    * Hoặc các đường dẫn độc lập không tương tác (FeatLLM);
    * Hoặc các đường dẫn có thể thay thế cho nhau (*interchangeable paths*) mà không có sự phân hóa chuyên biệt (LLM-FE).
    * Ngược lại, TOPOFE là phương pháp duy nhất có các đường dẫn tìm kiếm được phân hóa dựa trên thiên kiến quy nạp (*differentiated by inductive bias*) và được phối hợp một cách chủ động (*actively coordinated*): từng đảo nhận biết rõ loại đặc trưng chuyên biệt mà nó đang tìm kiếm và học được đảo nào khác để tiếp nhận chuyển giao tri thức (*learns which other island to borrow from*).

* **(ii) Không gian tìm kiếm (Search Space):**
  * **CAAFE**: Không gian tìm kiếm gồm các biểu thức mã lệnh không ràng buộc (*unconstrained code expressions*), nhưng trên thực tế (*in practice*) thường bị suy biến (*collapse*) thành các phép tổ hợp số học đơn giản (*simple arithmetic combinations*).
  * **FeatLLM**: Chủ động giới hạn không gian tìm kiếm trong phạm vi các quy tắc ngưỡng (*per-class threshold rules*) và quy tắc thành viên (*membership rules*) theo từng lớp trên các đặc trưng riêng lẻ (*individual features*).
  * **OCTree**: Tìm kiếm trên không gian các quy tắc bằng ngôn ngữ tự nhiên (*natural-language rules*) mà sau đó mới được chuyển đổi sang mã thực thi, hoàn toàn không có không gian toán tử định sẵn (*no pre-defined operator space*).
  * **LLM-FE**: Tìm kiếm trong không gian của toàn bộ các chương trình biến đổi đặc trưng hoàn chỉnh (*full feature-transformation programs*), nhưng chỉ dựa trên một ngữ pháp đồng nhất, không phân hóa (*undifferentiated grammar*).
  * **TOPOFE**: Cũng tìm kiếm trong không gian các chương trình biến đổi hoàn chỉnh, nhưng thực hiện phân vùng (*partitions*) không gian đó thành các không gian con có kiểu ngữ nghĩa (*semantically typed subspaces*), đồng thời mở rộng khả năng tiếp cận các không gian kết hợp đồng thời (*joint compositional spaces*) giữa các họ toán tử thông qua cơ chế tổng hợp lai (*hybrid synthesis*).
  * **Điểm khác biệt căn bản**: TOPOFE là phương pháp duy nhất phân rã không gian chương trình thành các không gian con định kiểu và coi việc kết hợp liên họ (*cross-family compositions*) là các mục tiêu tường minh, được kích hoạt có chủ đích (*deliberately-triggered targets*):
    * LLM-FE có cùng khả năng biểu đạt thô (*raw expressiveness*) nhưng chỉ có một ngữ pháp phẳng;
    * FeatLLM chủ ý tự giới hạn vào các quy tắc đơn giản;
    * CAAFE về nguyên tắc là không ràng buộc nhưng thực tế lại chỉ tạo ra các biểu thức đơn giản.

* **(iii) Quản lý bộ nhớ (Memory Management):**
  * **CAAFE**: Chỉ ghi nhớ các đặc trưng đã được chấp nhận và lỗi thực thi gần nhất (*most recent execution error*); các đặc trưng bị từ chối hoàn toàn không để lại dấu vết, dẫn đến nguy cơ lặp lại các ý tưởng thất bại tương tự (*near-duplicates of failed ideas can recur*).
  * **FeatLLM**: Hoàn toàn không lưu trạng thái (*fully stateless*); mỗi lần thử nghiệm là một lượt gọi LLM độc lập và không có bất kỳ bộ nhớ nào xuyên suốt các lần thử nghiệm.
  * **OCTree**: Lưu giữ toàn bộ quỹ đạo tối ưu hóa (*full optimization trajectory*) của các quy tắc trước đó, điểm số đánh giá, cùng với chuỗi lập luận liên quan, và gửi lại toàn bộ thông tin này cho LLM trong mỗi lượt gọi.
  * **LLM-FE**: Duy trì một bộ đệm chứa các chương trình đạt điểm số cao (*buffer of high-scoring programs*), nhưng chỉ lưu trữ duy nhất các ứng viên chiến thắng (*winners only*).
  * **TOPOFE**: Duy trì cơ chế bộ nhớ kép (*dual memory*):
    * Một kho lưu trữ tinh hoa (*elite archive*) lưu các chương trình mẫu mực (*exemplar programs*).
    * Một Bộ nhớ Thích ứng Câu nhắc (*Prompt Adaptation Memory - PAM*) tóm tắt cả lịch sử các ứng viên được chấp nhận lẫn bị từ chối của từng đảo thành một tín hiệu ngôn ngữ tự nhiên cô đọng "ưu tiên/tránh" (*compact natural-language "prefer/avoid" signal*), được cập nhật liên tục trong suốt tiến trình tìm kiếm.

* **(iv) Quản lý tinh hoa (Elite Management):**
  * **CAAFE**: Không có kho lưu trữ tinh hoa tường minh (*no explicit archive*); tập đặc trưng đang được chấp nhận ở thời điểm hiện tại đóng vai trò là tập tinh hoa duy nhất.
  * **FeatLLM**: Hoàn toàn không lưu giữ bất kỳ cá thể tinh hoa nào; mô hình kết hợp cuối cùng (*final ensemble*) chỉ đơn giản lấy trung bình đầu ra của toàn bộ các thử nghiệm.
  * **OCTree**: Chỉ lưu giữ duy nhất một quy tắc đạt điểm cao nhất cho mỗi đặc trưng (*best-scoring rule per feature*), hoàn toàn không duy trì một quần thể ứng viên phía sau (*no population behind it*).
  * **LLM-FE**: Duy trì một bộ đệm tinh hoa phân cụm theo điểm số (*score-clustered elite buffer*), được lấy mẫu để cung cấp các mẫu minh họa trong ngữ cảnh (*in-context demonstrations*), và khử trùng lặp các chương trình dựa trên đặc trưng nhận diện hiệu năng (*performance signature*).
  * **TOPOFE**: Duy trì một kho lưu trữ tinh hoa có giới hạn dung lượng cho từng đảo (*bounded per-island elite archive*) và áp đặt tính mới về cấu trúc (*structural novelty*): các ứng viên có cú pháp quá tương đồng với các thành viên hiện có sẽ bị loại bỏ.
  * **Vai trò kép và tầm quan trọng của kho tinh hoa trong TOPOFE**:
    * Kho lưu trữ vừa làm nguồn cung cấp mẫu minh họa trong ngữ cảnh (*in-context demonstration pool*), vừa làm vật liệu hiến tặng (*donor material*) cho quá trình lai ghép liên đảo (*cross-island hybridization*).
    * Việc khử trùng lặp theo cấu trúc giúp kho tinh hoa duy trì sự đa dạng cả về hành vi (*behaviorally*) lẫn cú pháp (*syntactically*). Điều này có ý nghĩa sống còn vì các cá thể tinh hoa đóng vai trò là cá thể cha mẹ phục vụ lai ghép và chuyển giao; nếu cha mẹ bị dư thừa (*redundant parents*) thì thế hệ con sinh ra cũng sẽ bị dư thừa (*redundant offspring*).

* **(v) Tín hiệu phản hồi dẫn dắt LLM (Optimization ObjectivM):**
  * *Đặc thù thuật ngữ trong tài liệu*: Tiêu đề trong nguyên bản văn bản in là *"Optimization ObjectivM"*, tập trung phân tích bản chất của tín hiệu phản hồi được gửi về cho LLM định hướng sinh đặc trưng.
  * **CAAFE**: Chỉ phản hồi một giá trị thay đổi hiệu năng dạng vô hướng (*scalar performance change*) kèm theo thông báo lỗi thực thi (nếu có).
  * **FeatLLM**: Không cung cấp bất kỳ phản hồi lặp nào (*no iterative feedback*); LLM chỉ quan sát các ví dụ trong câu nhắc few-shot ban đầu.
  * **OCTree**: Phản hồi các điểm số kiểm định kết hợp với lập luận suy diễn từ cây quyết định (*decision-tree reasoning*) được diễn đạt bằng ngôn ngữ tự nhiên, cung cấp cho LLM tri thức về cấu trúc của tập dữ liệu (*structural knowledge about the dataset*).
  * **LLM-FE**: Phản hồi các điểm số kiểm định kèm theo các chương trình có điểm cao đóng vai trò làm mẫu minh họa trong ngữ cảnh (*in-context exemplars*).
  * **TOPOFE**: Phản hồi đồng thời điểm độ thích nghi (*fitness score*), các chương trình mẫu mực từ kho tinh hoa (*elite exemplars*), và tín hiệu định hướng sở thích đã được chắt lọc (*distilled preference signal*) từ bộ nhớ câu nhắc (*prompt memory*).
  * **Khác biệt cốt lõi trong nhóm "phản hồi phong phú" (*rich feedback*)**:
    * Cây quyết định của OCTree tóm tắt thuộc tính dữ liệu (*summarizes the data*).
    * Bộ nhớ câu nhắc của TOPOFE tóm tắt kinh nghiệm tìm kiếm (*summarizes the search experience*).
    * Hai hình thức phản hồi có cấu trúc này mang tính trực giao (*orthogonal*). Nhờ đó, TOPOFE định hướng phân phối đề xuất (*proposal distribution*) của LLM bằng một bản ghi chép lũy tích, rõ ràng về những khu vực nào trong không gian tìm kiếm là hiệu quả và khu vực nào là bế tắc (*productive or dead regions*).

* **(vi) Hàm mục tiêu tối ưu hóa (Feedback Signal to the LLM):**
  * *Đặc thù thuật ngữ trong tài liệu*: Tiêu đề trong nguyên bản văn bản in là *"Feedback Signal to the LLM"*, nhưng nội dung tập trung phân định hàm mục tiêu toán học và tiêu chí chất lượng mà phương pháp tối ưu hóa.
  * **CAAFE**: Tối đa hóa hiệu năng phân loại trên tập kiểm định (*validation classification performance*).
  * **FeatLLM**: Tối thiểu hóa hàm mất mát (*loss*) của một mô hình đơn giản được khớp trên các đặc trưng quy tắc nhị phân (*binary rule features*).
  * **OCTree**: Tối thiểu hóa hàm mất mát kiểm định một cách độc lập cho từng quy tắc (*minimizes validation loss for each rule independently*).
  * **LLM-FE**: Tối đa hóa điểm kiểm định của chương trình tốt nhất tìm được (*validation score of the best program found*).
  * **TOPOFE**: Là phương pháp duy nhất tối ưu hóa một hàm mục tiêu đa thành phần tường minh (*explicitly multi-term objective*) tích hợp:
    1. Hiệu năng mô hình dự đoán ở hạ nguồn (*downstream predictive performance*);
    2. Thành phần phạt độ dư thừa (*redundancy penalty*) tính trên hệ số tương quan từng cặp giữa các đặc trưng (*pairwise feature correlations*);
    3. Thành phần độ ổn định (*stability term*) tưởng thưởng tính nhất quán của đặc trưng qua các tập gấp kiểm định (*validation folds*);
    4. Thành phần chi phí tính toán (*computational cost term*).
  * **Ý nghĩa cơ chế**: Mọi phương pháp đối chuẩn đều xem hiệu năng dự đoán là tiêu chí duy nhất (*sole criterion*), trong khi TOPOFE hình thức hóa chất lượng đặc trưng thành một thuộc tính đa tiêu chí (*multi-criteria property*). Đây chính là nguyên nhân giải thích vì sao TOPOFE giành chiến thắng vượt trội trên cả các thước đo độ dư thừa ($\text{MPOC}$) lẫn độ bao phủ không gian con ($\text{EffRank}$), thay vì chỉ tập trung vào độ chính xác đơn thuần (*accuracy alone*).

* **(vii) Tính song song và hiệu quả tính toán (Parallelism and Efficiency):**
  * **CAAFE và OCTree**: Vốn mang bản chất tuần tự (*inherently sequential*); mỗi vòng lặp bắt buộc phải chờ đợi kết quả của vòng lặp trước đó.
  * **FeatLLM**: Các thử nghiệm độc lập có thể thực hiện song song hóa một cách hiển nhiên (*trivially parallel*).
  * **LLM-FE**: Về mặt nguyên tắc, các đảo tiến hóa có khả năng song song hóa được (*parallelizable in principle*).
  * **TOPOFE**: Được thiết kế để song song hóa ngay từ cấu trúc (*parallel by design*):
    * Việc đánh giá hiệu năng trên các đảo là hoàn toàn độc lập với nhau (*mutually independent*), do đó thời gian thực tế (*wall-clock time*) trên mỗi thế hệ được quyết định bởi hòn đảo chậm nhất chứ không bị tỷ lệ thuận theo tổng số lượng cá thể ứng viên.
    * Cơ chế chuyển giao tri thức liên đảo chỉ được kích hoạt khi phát hiện bão hòa (*saturation-triggered*) thay vì truyền tin liên tục (*continuous transfer*), giúp giữ cho chi phí điều phối (*coordination overhead*) ở mức tối thiểu và không đáng kể (*negligible*).
