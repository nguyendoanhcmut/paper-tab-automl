## Abstract

* **Thách thức cốt lõi của kỹ thuật đặc trưng tự động cho dữ liệu dạng bảng:**
  * Kỹ thuật đặc trưng tự động (Automatic feature engineering - AutoFE) cho dữ liệu dạng bảng (tabular data) đòi hỏi phải khám phá các phép biến đổi giàu thông tin (informative transformations) từ một không gian chương trình (program space) có quy mô bùng nổ tổ hợp và tính chất dị thể (combinatorially large and heterogeneous).

* **Ba hạn chế căn bản của các hướng tiếp cận AutoFE hiện tại:**
  * Các phương pháp cổ điển (classical methods) phụ thuộc vào các thư viện toán tử cố định (fixed operator libraries) với khả năng biểu đạt hạn chế (limited expressivity).
  * Các phương pháp dựa trên mô hình ngôn ngữ lớn (Large Language Models - LLMs) tạo các đề xuất từ những câu lệnh nhắc tĩnh (static prompts) mà không lưu giữ lại kinh nghiệm tìm kiếm trước đó (prior search experience).
  * Các phương pháp tiến hóa (evolutionary methods) áp dụng các chính sách di cư cố định (fixed migration policies), bỏ qua độ hữu dụng chuyển giao liên họ (cross-family transfer utility) mang tính đặc thù theo từng nhiệm vụ cụ thể (task-specific).

* **Khung làm việc đề xuất: $\text{TOPOFE}$:**
  * $\text{TOPOFE}$ mô hình hóa bài toán AutoFE dưới dạng tìm kiếm chương trình tiến hóa đa đảo có cấu trúc đồ thị (graph-structured multi-island evolutionary program search).
  * Không gian biến đổi (transformation space) được phân hoạch thành các họ nhất quán về mặt ngữ nghĩa (semantically coherent families), trong đó mỗi họ được khám phá chuyên sâu bởi một đảo riêng biệt (dedicated island) thông qua các toán tử đột biến (mutation) và lai ghép (crossover) dưới sự dẫn dắt của LLM.
  * Mỗi đảo duy trì một Bộ nhớ thích ứng câu lệnh nhắc (Prompt Adaptation Memory) nhằm tích lũy phản hồi chấp nhận/từ chối (accept/reject feedback), giúp định hướng các đề xuất tiếp theo tiến vào các vùng tìm kiếm hiệu quả mà không cần cập nhật tham số mô hình (without parameter updates).
  * Để điều phối quá trình khám phá toàn cục (global exploration), $\text{TOPOFE}$ học động một đồ thị tô-pô có hướng (directed topology graph) với trọng số cạnh mã hóa độ hữu dụng chuyển giao thực nghiệm (empirical transfer utility) giữa các họ biến đổi.
  * Quá trình chuyển giao liên đảo (cross-island transfer) được kích hoạt bởi cơ chế phát hiện bão hòa thích ứng (adaptive saturation detection) và thực hiện thông qua tổng hợp lai do LLM làm trung gian (LLM-mediated hybrid synthesis), cho phép khám phá các chương trình đặc trưng có tính hợp thành (compositional feature programs) vốn không thể hình thành từ quá trình tìm kiếm cục bộ riêng lẻ (isolated local search).

* **Kết quả thực nghiệm và các phát hiện chính:**
  * Thực nghiệm trên $29$ tập dữ liệu dạng bảng chứng minh $\text{TOPOFE}$ liên tục vượt trội so với hầu hết các phương pháp AutoFE tiên tiến nhất (state-of-the-art AutoFE methods) trên cả nhiệm vụ phân loại (classification) và hồi quy (regression).
  * Vượt trên hiệu năng dự đoán (predictive performance), $\text{TOPOFE}$ tạo ra các tập đặc trưng có độ dư thừa thấp hơn (lower redundancy) và độ bao phủ biểu diễn cao hơn (higher representational coverage).
  * Đồ thị tô-pô học được tự động tích lũy cấu trúc chuyển giao đặc thù theo nhiệm vụ có ý nghĩa, tương quan chặt chẽ với mức cải thiện hiệu năng hạ nguồn (downstream gains).
  * Các chương trình đặc trưng được khám phá có khả năng chuyển giao đáng tin cậy qua nhiều mô hình dự đoán hạ nguồn (downstream predictors) và các kiến trúc LLM nền tảng (LLM backbones) khác nhau, chứng minh các cải tiến bắt nguồn trực tiếp từ cấu trúc tìm kiếm và cơ chế điều phối thích ứng của $\text{TOPOFE}$ thay vì phụ thuộc vào năng lực sinh đặc thù của mô hình nền tảng.
