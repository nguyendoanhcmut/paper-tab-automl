## Appendix L: Discussion on the Architectural Advantages and Mechanisms of SymboLLM-FE

* **Sự chuyển dịch mô thức cốt lõi (Core paradigmatic shift) trong việc ứng dụng LLM**:
  * Khung làm việc SymboLLM-FE thể hiện sự khác biệt căn bản so với các phương pháp luận hiện có như CAAFE và OcTree:
    * Thay vì sử dụng LLM như một bộ sinh đặc trưng không ràng buộc (unconstrained feature generator), SymboLLM-FE tái cấu hình LLM thành một bộ tích hợp đặc trưng tất định (deterministic feature integrator).
    * Sự phân kỳ về mặt kiến trúc này giải quyết triệt để sự đánh đổi truyền thống giữa tính sáng tạo ngữ nghĩa mở của LLM và độ chính xác toán học chặt chẽ.
* **Ba chiều không gian kiến trúc then chốt (Three critical architectural dimensions)**:
  * **Định hướng chức năng (Functional orientation)**:
    * Các phương pháp tiếp cận dạng sinh truyền thống (conventional generative approaches) dễ gặp phải hiện tượng trôi dạt ngữ nghĩa (semantic drift) và tạo ra các đầu ra dư thừa (redundant outputs) do bản chất mở không giới hạn (open-ended nature).
    * Ngược lại, SymboLLM-FE ràng buộc LLM chỉ tổng hợp và căn chỉnh các đặc trưng cơ sở (base features) hiện có thông qua phép hợp thành logic tường minh (explicit logical composition).
    * Cơ chế này đảm bảo tính nhất quán nghiêm ngặt giữa các đặc trưng được thiết kế (engineered features) và đa tạp dữ liệu nền tảng (underlying data manifold), ngăn chặn hoàn toàn việc suy diễn ra các đặc trưng không có căn cứ thực tế.
  * **Hiệu quả tính toán và khả năng mở rộng (Computational efficiency and scalability)**:
    * Mô thức tích hợp (integrator paradigm) triệt tiêu sự bùng nổ tổ hợp (combinatorial explosion) vốn là nhược điểm cố hữu của các không gian tìm kiếm dạng sinh (generative search spaces).
    * Bằng cách giới hạn không gian thao tác trong một không gian con ký hiệu được xác định rõ ràng (well-defined symbolic subspace):
      * Hồi quy ký hiệu (symbolic regression - SR) đóng vai trò tìm kiếm toàn cục tiến hóa (evolutionary global search), cắt tỉa không gian tìm kiếm tổ hợp từ quy mô hàm mũ $\mathcal{O}(2^n)$ xuống quy mô đa thức $\mathcal{O}(n^2)$ (thông qua sắp xếp sơ bộ tương quan Spearman và kỹ thuật cửa sổ trượt mở rộng).
      * LLM tập trung vào việc tinh chỉnh ngữ nghĩa cục bộ (local semantic refinement) và hợp nhất đặc trưng trong không gian con đã được sàng lọc, tạo nên sự hiệp đồng hiệu quả cao (synergy).
      * Khung làm việc giảm thiểu đáng kể độ trễ suy luận (inference latency) cũng như chi phí tính toán (computational overhead) trong quá trình tạo đặc trưng tự động.
  * **Khả năng diễn giải và kiểm soát (Interpretability and controllability)**:
    * Quy trình tích hợp được dẫn hướng bởi các quy tắc (rule-guided integration process) bảo toàn trọn vẹn nguồn gốc toán học và logic tường minh (explicit mathematical and logical provenance).
    * Toàn bộ các lộ trình suy diễn (derivation pathways) của các đặc trưng được tạo ra đều trở nên hoàn toàn minh bạch.
    * Cơ chế này giảm thiểu và loại bỏ hữu hiệu tính mờ đục (opacity) thường gắn liền với các cơ chế sinh dạng hộp đen (black-box generation mechanisms), cho phép người dùng và chuyên gia kiểm toán tường minh từng phép biến đổi.
* **Cơ chế tự động hóa triển khai hoàn toàn khép kín (Full deployment automation mechanism)**:
  * Toàn bộ quy trình (pipeline) của SymboLLM-FE vận hành độc lập và tự động, hoàn toàn không đòi hỏi bất kỳ sự can thiệp thủ công nào từ con người (zero manual intervention).
  * **Giao thức khép kín Sinh - Thực thi - Phản hồi (Closed-loop generate-execute-feedback protocol)**:
    * Các ngoại lệ phát sinh lúc chạy (runtime exceptions) trong mã trích xuất đặc trưng do LLM tạo ra sẽ được hệ thống tự động bắt giữ (automatically captured).
    * Lỗi được phân tích cú pháp thành các vết lỗi có cấu trúc (structured error traces).
    * Các vết lỗi này được phản hồi trực tiếp vào hệ thống dưới dạng các câu nhắc hiệu chỉnh (corrective prompts), kích hoạt quy trình tinh chỉnh lặp lại của LLM (iterative LLM refinement).
  * **So sánh với các cơ chế khôi phục lỗi trước đây**:
    * Cơ chế tự sửa lỗi (self-correcting mechanism) này tương đồng về mặt khái niệm với các chiến lược phục hồi lỗi trong CAAFE.
    * Tuy nhiên, SymboLLM-FE đạt được khả năng thực thi hoàn toàn tự trị (fully autonomous execution), qua đó bảo đảm độ tin cậy vận hành vững chắc (operational reliability) mà không phải chịu chi phí giám sát từ con người trong vòng lặp (eliminating human-in-the-loop overhead).
* **Triệt tiêu nguy cơ nhiễm bẩn dữ liệu và thiên kiến thuật toán ở cấp độ kiến trúc (Architectural elimination of data contamination and algorithmic bias)**:
  * SymboLLM-FE giải quyết tận gốc các lo ngại phổ biến về nguy cơ ô nhiễm dữ liệu (data contamination) và thiên kiến thuật toán (algorithmic bias) thường gặp trong các hệ thống vận hành bằng LLM:
    * Logic xây dựng đặc trưng được suy diễn hoàn toàn và độc quyền từ siêu dữ liệu cấp lược đồ (schema-level metadata) và các quy tắc suy luận ký hiệu (symbolic inference rules).
    * Quy trình được tách rời tuyệt đối (entirely decoupled) khỏi các mẫu dữ liệu lịch sử (historical dataset samples) cũng như các biến mục tiêu (target variables).
  * **Các lợi thế đảm bảo an toàn thuật toán và tính tổng quát hóa**:
    * Triệt tiêu hoàn toàn khả năng rò rỉ dữ liệu (data leakage) giữa tập huấn luyện và kiểm tra.
    * Ngăn chặn hiện tượng quá khớp (overfitting) với các tạo tác ngẫu nhiên đặc thù của tập dữ liệu (dataset-specific artifacts).
    * Ngăn ngừa sự lan truyền các thiên kiến gán nhãn lịch sử (propagation of historical annotation biases).
    * Tăng cường tính kháng nhiễu (robustness to noise) và tính ổn định số học trong không gian đặc trưng.
    * Đảm bảo năng lực tổng quát hóa vượt trội (superior generalization capacity) cùng tính công bằng thuật toán (algorithmic fairness) khi triển khai trên các kịch bản thực tế không đồng nhất (heterogeneous deployment scenarios).
