## 7 Conclusion

* **Đề xuất khung làm việc TOPOFE cho kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE):**
  * TOPOFE là khung làm việc sinh đặc trưng tự động có hướng dẫn bởi mô hình ngôn ngữ lớn (Large Language Models - LLMs), mô hình hóa không gian tìm kiếm thành quá trình tiến hóa đa đảo có cấu trúc đồ thị (graph-structured multi-island evolution) trên các họ biến đổi không đồng nhất (heterogeneous transformation families).
  * Giải quyết ba hạn chế cốt lõi và căn bản của các phương pháp AutoFE hiện hữu:
    * *Động lực học tìm kiếm đồng nhất (homogeneous search dynamics):* Tránh sự suy thoái không gian tìm kiếm khi áp dụng chung một cơ chế tìm kiếm đơn điệu cho mọi loại đặc trưng.
    * *Truy vấn LLM không trạng thái (stateless LLM querying):* Khắc phục việc gọi LLM rời rạc không tích lũy ngữ cảnh lịch sử tìm kiếm.
    * *Tô pô di cư cứng nhắc (rigid migration topology):* Loại bỏ các cấu trúc liên kết tĩnh định sẵn vốn không thích ứng được với sự tương tác giữa các phép biến đổi.

* **Ba cơ chế kiến trúc trụ cột của TOPOFE:**
  * *Các đảo chuyên biệt hóa theo họ biến đổi (family-specialised islands):* Bảo toàn tính đa dạng của phép biến đổi (transformation diversity) ngay từ khâu thiết kế cấu trúc (by construction).
  * *Đồ thị tô pô có hướng học được (learned directed topology graph):* Định tuyến quá trình chuyển giao tri thức liên họ (cross-family transfer) hướng về các cặp đảo biến đổi mang lại hiệu quả thực nghiệm cao nhất (empirically productive island pairs).
  * *Tổng hợp lai qua trung gian LLM kích hoạt bởi sự bão hòa (saturation-triggered LLM-mediated hybrid synthesis):* Thực thi chuyển giao tri thức dưới dạng sinh chương trình hợp thành (compositional program generation) chuẩn xác vào thời điểm không gian tìm kiếm cục bộ (local search) tại đảo đã cạn kiệt.

* **Hiệu năng thực nghiệm vượt trội trên diện rộng:**
  * Đánh giá thực nghiệm trên $19$ bộ dữ liệu chuẩn phân loại (classification benchmarks) và $10$ bộ dữ liệu chuẩn hồi quy (regression benchmarks).
  * TOPOFE nhất quán vượt trội hơn tất cả các phương pháp cơ sở và đối chuẩn so sánh (consistently outperforms all baselines).
  * Mức cải thiện lớn nhất ghi nhận trên các tập dữ liệu đòi hỏi sự tương tác đặc trưng phức tạp giữa các họ biến đổi khác nhau (cross-family feature interactions).

* **Ba chỉ số đo lường chuyên biệt xác thực nền tảng cơ chế (mechanistic basis):**
  * *$\text{MPOC}$ và $\text{EffRank}$ (Effective Rank):* Chứng minh các tập đặc trưng do TOPOFE tạo ra có độ dư thừa thấp hơn (lower redundancy) và độ bao phủ không gian biểu diễn cao hơn (higher coverage) so với tất cả các phương pháp cạnh tranh.
  * *$\text{TGSS}$ (Topology Graph Specialisation Score):* Xác nhận đồ thị tô pô tiếp thu một cách đáng tin cậy tri thức chuyển giao đặc thù cho từng bài toán (task-specific transfer knowledge).
  * Mức độ chuyên biệt hóa đồ thị tô pô tương quan thuận trực tiếp (correlating directly) với mức cải thiện hiệu năng so với các đường cơ sở chỉ sử dụng đơn họ biến đổi (single-family baselines).

* **Khả năng chuyển giao kiến trúc và tính ổn định độc lập với mô hình:**
  * Các chương trình đặc trưng (feature programs) chuyển giao tin cậy (transfer reliably) qua các bộ dự đoán có kiến trúc khác biệt rõ rệt (architecturally distinct predictors).
  * Hiệu năng duy trì tính ổn định trên nhiều mô hình nền tảng LLM có năng lực suy luận khác nhau (LLM backbones of varying capability).
  * Khẳng định kết quả vượt trội được thúc đẩy bởi chính các cơ chế kiến trúc (architectural mechanisms) của khung làm việc chứ không phụ thuộc vào một mô hình cụ thể nào.

* **Ý nghĩa đóng góp lý luận và các định hướng nghiên cứu tương lai:**
  * Khẳng định tính bổ trợ liên họ (inter-family complementarity) là một đại lượng hoàn toàn có thể học được và khai thác được (learnable and exploitable quantity) mà các phương pháp AutoFE trước đây bỏ quên.
  * Mở ra các định hướng nghiên cứu đầy triển vọng:
    * Tự động quy nạp lược đồ họ biến đổi (automated family schema induction).
    * Lập lịch chuyển giao tri thức đặc thù theo từng loại bài toán (task-type-specific transfer scheduling).
    * Mở rộng khung làm việc sang các thiết lập dữ liệu bảng đa phương thức (multi-modal tabular settings).
