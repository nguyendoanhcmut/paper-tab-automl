### K.6 Interpretability, Hallucination Mitigation, and Bias Analysis

* **Khung phân tích toàn diện về khả năng diễn giải, giảm thiểu ảo giác và độ chệch (Comprehensive analysis framework)**:
  * **Đánh giá kết hợp định tính và định lượng**: Phân tích toàn diện khả năng diễn giải mô hình (*model interpretability*), giảm thiểu ảo giác (*hallucination mitigation*), và độ chệch (*bias*) thông qua việc phối hợp giữa các nghiên cứu tình huống định tính (*qualitative case studies*) và các thước đo định lượng (*quantitative metrics*).
  * **Các nghiên cứu tình huống thực nghiệm**: Gồm $8$ nghiên cứu tình huống chi tiết (*eight detailed case studies*) được trình bày trong Phụ lục I (*Appendix I*), trong đó một ví dụ mang tính đại diện (*representative example*) được nhấn mạnh nhằm minh họa cơ chế cốt lõi (*core mechanism*).
* **Phân công lao động rõ rệt giữa SR và LLM (Division of labor between SR and LLMs)**:
  * **Vai trò của hồi quy biểu tượng (*Symbolic Regression - SR*)**: Đảm nhiệm khám phá các cấu trúc toán học hữu hiệu (*effective mathematical structures*) tiềm ẩn trong dữ liệu.
  * **Vai trò của mô hình ngôn ngữ lớn (*Large Language Model - LLM*)**: Truyền dẫn và bổ sung ngữ nghĩa đặc thù theo miền tri thức (*domain-specific semantics*).
  * **Cơ chế tinh chỉnh và chú giải đặc trưng của SymboLLM-FE**:
    * Trong khi SR tiêu chuẩn (*standard SR*) ban đầu tạo ra công thức lồng nhau mờ đục (*opaque nested formula*), SymboLLM-FE tinh chỉnh công thức thành một đặc trưng có cơ sở ngữ nghĩa vững chắc (*semantically grounded feature*).
    * LLM chú giải đặc trưng bằng cách liên kết nó với các nguyên lý/học thuyết chuyên ngành (*domain-specific doctrines*), nắm bắt chính xác các biến thiên phi tuyến (*non-linear changes*) trong các biến mục tiêu (*target variables*).
  * **Chuyển dịch mô thức minh bạch hóa (*Paradigm shift*)**: Sự hiệp đồng (*synergy*) giữa SR và LLM thúc đẩy bước chuyển dịch căn bản từ tính mờ đục của hộp đen (*black-box opacity*) sang tính minh bạch của hộp trắng (*white-box transparency*).
* **Xác thực tính diễn giải nội tại qua kiểm chứng độ trung thực và đơn giản hóa biểu thức (Intrinsic interpretability verification)**:
  * **Bản chất nội tại thay vì giải thích hậu nghiệm (*Intrinsic vs. post-hoc interpretability*)**: Nhằm chứng minh tính diễn giải mang bản chất nội tại (*intrinsic*) chứ không phải là sự hợp lý hóa hậu nghiệm (*post-hoc*), nghiên cứu tiến hành phân tích kiểm chứng độ trung thực (*fidelity verification*) và phân tích đơn giản hóa biểu thức (*expression simplification analysis*).
  * **Kiểm chứng độ trung thực (*Fidelity verification*)**:
    * Đo lường mức độ tương đồng giữa từng cặp công thức SR và đặc trưng được tinh chỉnh bởi LLM trên tập dữ liệu kiểm tra giữ lại (*hold-out set*).
    * Đạt độ trung thực cao trên cả $3$ phương diện: toán học (*mathematical fidelity*), cấu trúc (*structural fidelity*), và ngữ nghĩa (*semantic fidelity*).
    * Kết quả đảm bảo rằng các đặc trưng được tinh chỉnh tuân thủ nghiêm ngặt các tín hiệu thống kê ban đầu (*strictly adhere to original statistical signals*).
  * **Đơn giản hóa logic thực chất (*Genuine logical simplification*)**:
    * Quá trình tinh chỉnh của LLM cấu thành sự đơn giản hóa logic thực chất (*genuine logical simplification*) thay vì chỉ đơn thuần là việc đổi tên biến (*mere renaming*).
    * Giảm đáng kể số lượng toán tử trung bình (*average number of operators*) và độ sâu lồng nhau (*nesting depth*).
    * Tạo ra các biểu thức toán học cô đọng hơn (*more compact expressions*) và nâng cao rõ rệt khả năng đọc hiểu trực giác của con người (*human-readable expressions*).
* **Tính vững chắc và khả năng giảm thiểu ảo giác đa chiều (Robustness and multi-dimensional hallucination mitigation)**:
  * **Phân rã không gian ảo giác đa chiều (*Multi-dimensional hallucination decomposition*)**: Ảo giác của mô hình được phân rã thành nhiều chiều kích đo lường độc lập:
    * Lỗi thực thi (*execution failure*).
    * Trôi dạt ngữ nghĩa (*semantic drift*).
    * Bất thường về miền giá trị (*value range anomalies*).
  * **Hiệu năng kiểm soát ảo giác của SymboLLM-FE**:
    * SymboLLM-FE đạt điểm số giảm thiểu ảo giác toàn diện ở mức cao (*high comprehensive hallucination mitigation score*).
    * Tỷ lệ trôi dạt ngữ nghĩa (*semantic drift rate*) thấp hơn đáng kể so với các phương pháp đường cơ sở (*baseline methods*).
  * **Cơ chế ràng buộc bằng quy tắc SR (*Anchoring mechanism*)**: Việc neo giữ LLM bằng các quy tắc suy dẫn từ SR (*anchoring the LLM with SR rules*) thiết lập sự kiềm tỏa nền tảng lên không gian ảo giác (*fundamentally constrains the hallucination space*).
* **Phân tích độ chệch và bảo toàn thứ hạng tầm quan trọng đặc trưng (Bias analysis and rank preservation)**:
  * **Kiểm soát độ chệch phân phối toán tử (*Operator distribution bias*)**: Các thực nghiệm cho thấy độ chệch phân phối toán tử thấp hơn đáng kể so với các phương pháp hiện hành.
  * **Tính nhất quán xuyên tập dữ liệu (*Cross-dataset consistency*)**: SymboLLM-FE thể hiện tính nhất quán vượt trội xuyên suốt các tập dữ liệu khác nhau (*superior cross-dataset consistency*).
  * **Bảo toàn thứ hạng tầm quan trọng thống kê (*Feature importance rank preservation*)**:
    * Tương quan cao trong việc bảo toàn thứ hạng tầm quan trọng của đặc trưng (*high correlation in rank preservation of feature importance*).
    * Khẳng định LLM bảo toàn một cách trung thực tầm quan trọng mang tính thống kê được suy dẫn từ dữ liệu (*faithfully preserves statistical importance derived from data*), thay vì áp đặt các thiên kiến hay sở thích chủ quan (*rather than imposing subjective preferences*).
