## Appendix L Discussion on the Architectural Advantages and Mechanisms of SymboLLM-FE

- Khung làm việc SymboLLM-FE thể hiện sự khác biệt căn bản so với các phương pháp luận hiện tại như CAAFE và OcTree, chủ yếu thông qua sự chuyển dịch mô thức (paradigmatic shift) trong cách thức khai thác các mô hình ngôn ngữ lớn (Large Language Models - LLMs):
  - Thay vì sử dụng LLM như một bộ sinh đặc trưng không ràng buộc (unconstrained feature generator), SymboLLM-FE tái cấu trúc mô hình thành một bộ tích hợp đặc trưng tất định (deterministic feature integrator).
  - Sự phân kỳ kiến trúc (architectural divergence) này thể hiện rõ rệt qua ba khía cạnh then chốt: định hướng chức năng (functional orientation), hiệu quả tính toán cùng khả năng mở rộng (computational efficiency and scalability), và khả năng diễn giải cùng khả năng kiểm soát (interpretability and controllability).

### L.1 Functional Orientation

- Về định hướng chức năng (functional orientation), SymboLLM-FE khắc phục các hạn chế cố hữu của các phương pháp tiếp cận sinh truyền thống:
  - Các phương pháp tiếp cận sinh truyền thống (conventional generative approaches) dễ bị trôi dạt ngữ nghĩa (semantic drift) và tạo ra các kết quả đầu ra dư thừa (redundant outputs) do bản chất kết thúc mở (open-ended nature) của chúng.
  - Ngược lại, SymboLLM-FE ràng buộc LLM tổng hợp và căn chỉnh các đặc trưng cơ sở hiện có (existing base features) thông qua phép hợp thành logic tường minh (explicit logical composition).
  - Cơ chế hợp thành này bảo đảm tính nhất quán nghiêm ngặt (stringent consistency) giữa các đặc trưng được thiết kế (engineered features) và đa tạp dữ liệu tiềm ẩn bên dưới (underlying data manifold).

### L.2 Computational Efficiency and Scalability

- Về hiệu quả tính toán và khả năng mở rộng (computational efficiency and scalability), mô thức tích hợp giúp kiểm soát không gian tìm kiếm:
  - Mô thức bộ tích hợp (integrator paradigm) triệt tiêu sự bùng nổ tổ hợp (combinatorial explosion) vốn là nhược điểm cố hữu trong các không gian tìm kiếm sinh (generative search spaces).
  - Bằng cách giới hạn các thao tác tính toán trong một không gian con ký hiệu được xác định rõ ràng (well-defined symbolic subspace), khung làm việc cắt giảm đáng kể độ trễ suy luận (inference latency) và chi phí tính toán (computational overhead).

### L.3 Interpretability and Controllability

- Về khả năng diễn giải và khả năng kiểm soát (interpretability and controllability), quy trình tích hợp dựa trên quy tắc bảo đảm tính minh bạch toàn diện:
  - Quy trình tích hợp được định hướng bởi quy tắc (rule-guided integration process) bảo tồn trọn vẹn nguồn gốc toán học và logic tường minh (explicit mathematical and logical provenance).
  - Việc duy trì nguồn gốc này giúp các lộ trình suy dẫn (derivation pathways) của các đặc trưng được thiết kế trở nên hoàn toàn minh bạch (fully transparent).
  - Quy trình triệt tiêu hiệu quả tính mờ đục (opacity) thường gắn liền với các cơ chế sinh dạng hộp đen (black-box generation mechanisms).

### L.4 Deployment Automation and Elimination of Data Contamination and Bias

- Toàn bộ đường ống SymboLLM-FE vận hành tự động hóa triển khai (deployment automation) mà không đòi hỏi bất kỳ sự can thiệp thủ công nào (without any manual intervention):
  - Hệ thống thiết lập giao thức vòng lặp khép kín sinh-thực thi-phản hồi (closed-loop generate-execute-feedback protocol):
    - Các ngoại lệ thời gian chạy (runtime exceptions) phát sinh trong mã trích xuất đặc trưng được sinh ra sẽ tự động được ghi nhận và phân tích cú pháp thành các vết lỗi có cấu trúc (structured error traces).
    - Các vết lỗi này được đưa ngược trở lại dưới dạng lời nhắc hiệu chỉnh (corrective prompts) nhằm kích hoạt quá trình tinh chỉnh lặp lại của LLM (iterative LLM refinement).
  - Cơ chế tự sửa lỗi (self-correcting mechanism) này tương đồng với các chiến lược phục hồi lỗi được áp dụng trong CAAFE nhưng đạt được khả năng thực thi tự động hoàn toàn (fully autonomous execution).
  - Giao thức này bảo đảm độ tin cậy vận hành vững chắc (robust operational reliability) đồng thời loại bỏ chi phí giám sát của con người trong vòng lặp (eliminating human-in-the-loop overhead).
- SymboLLM-FE loại trừ tận gốc các rủi ro về nhiễm bẩn dữ liệu (data contamination) và thiên kiến thuật toán (algorithmic bias) ngay từ cấp độ kiến trúc (architectural level):
  - Logic xây dựng đặc trưng (feature construction logic) được suy dẫn độc quyền từ siêu dữ liệu cấp lược đồ (schema-level metadata) và các quy tắc suy luận ký hiệu (symbolic inference rules).
  - Quy trình suy dẫn được tách rời hoàn toàn (entirely decoupled) khỏi các mẫu dữ liệu lịch sử (historical dataset samples) hoặc các biến mục tiêu (target variables).
  - Khung làm việc ngăn chặn triệt để mọi khả năng rò rỉ dữ liệu (data leakage), hiện tượng quá khớp với các tạo tác đặc thù của tập dữ liệu (overfitting to dataset-specific artifacts), và sự lan truyền các thiên kiến gán nhãn lịch sử (propagation of historical annotation biases).
  - Thiết kế kiến trúc này đảm bảo năng lực khái quát hóa vượt trội (superior generalization capacity) cùng tính công bằng thuật toán (algorithmic fairness) xuyên suốt các kịch bản triển khai không đồng nhất (heterogeneous deployment scenarios).
