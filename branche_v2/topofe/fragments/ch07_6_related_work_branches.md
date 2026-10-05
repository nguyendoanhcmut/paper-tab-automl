## 6 Related Work

### 6.1 Automatic Feature Engineering

- **Ba hình thái tiến hóa của kỹ thuật tạo đặc trưng tự động (Automated Feature Engineering - AutoFE)**: Lĩnh vực AutoFE đã phát triển qua ba mô hình tiếp cận chính gồm các phương pháp dựa trên tìm kiếm (search-based methods), các phương pháp định hướng bằng mô hình ngôn ngữ lớn (LLM-guided methods), và các phương pháp tiến hóa kết hợp LLM (LLM-evolutionary methods).
  - **Phương pháp dựa trên tìm kiếm (Search-based methods)**: Xem việc xây dựng đặc trưng như một bài toán tối ưu hóa tổ hợp (combinatorial optimization problem).
    - Sử dụng quy hoạch di truyền (genetic programming) [Olson and Moore, 2016], tìm kiếm vét cạn (exhaustive search) [Horn et al., 2019], và tìm kiếm tham lam (greedy search) [Zhang et al., 2023a].
    - Hạn chế: Tốn kém tài nguyên tính toán (computationally expensive) và không phân biệt miền dữ liệu (domain-agnostic) do thiếu định hướng ngữ nghĩa (semantic guidance).
  - **Phương pháp định hướng bằng LLM (LLM-guided methods)**: Tận dụng các mô hình ngôn ngữ tiền huấn luyện (pretrained LMs) để đề xuất các đặc trưng [Han et al., 2024, Ko et al., 2025, Nam et al., 2024] từ mô tả nhiệm vụ và siêu dữ liệu của tập dữ liệu (dataset metadata) [Hollmann et al., 2023a].
    - Các mở rộng gần đây áp dụng suy luận Cây-suy-nghĩ (Tree-of-Thought reasoning) [Zhang et al., 2025], các khung đa tác tử (multi-agent frameworks) [Ouyang et al., 2025], và các tác tử dựa trên ReAct (ReAct-based agents) [Burghardt et al., 2026] nhằm dẫn dắt quá trình khám phá đặc trưng.
    - Hạn chế: Phụ thuộc vào kỹ thuật gợi ý (prompting), dẫn đến việc lặp lại các đề xuất (repeated proposals), thiếu sự thích ứng đặc thù theo tập dữ liệu (no dataset-specific adaptation), và không có sự kết hợp xuyên họ biến đổi (no cross-family composition).
  - **Phương pháp tiến hóa kết hợp LLM (LLM-evolutionary methods)**: Kết hợp khả năng sinh đặc trưng của LLM với tìm kiếm tiến hóa (evolutionary search) [Abhyankar et al., 2025, Gong et al., 2025, Batista, 2025].
    - Ưu điểm và hạn chế: Dù cải thiện so với kỹ thuật gợi ý tĩnh (static prompting), các phương pháp này vận hành trên một quần thể đơn lẻ (single population) mà không có sự phân rã cấu trúc của không gian chương trình (structural decomposition of the program space); điều này ngăn cản quá trình lai ghép xuyên họ (precluding cross-family hybridization) và khiến tìm kiếm dễ bị hội tụ sớm (premature convergence) cục bộ trong một họ biến đổi vượt trội (dominant transformation family).
- **Giải pháp của TOPOFE**: Giải quyết trực tiếp các hạn chế trên thông qua phân rã đa đảo (multi-island decomposition), bộ nhớ thích ứng prompt (prompt adaptation memory), và chuyển giao xuyên họ dựa trên tô-pô (topology-guided cross-family transfer).

### 6.2 LLMs for Tabular Data Learning

- **Hai hình thái tiến bộ chính trong học dữ liệu bảng (Tabular Data Learning)**: Các nghiên cứu gần đây hội tụ về mô hình nền tảng cho dữ liệu bảng (tabular foundation models) và các phương pháp dữ liệu bảng dựa trên LLM (LLM-based tabular methods).
  - **Mô hình nền tảng cho dữ liệu bảng (Tabular foundation models)**: Hướng tới khả năng chuyển giao xuyên bảng (cross-table transferability) thông qua tiền huấn luyện quy mô lớn (large-scale pretraining).
    - Xấp xỉ suy luận Bayes (Bayesian inference approximation) thông qua Mạng khớp dữ liệu tiên nghiệm (Prior-Data Fitted Networks - PFNs) [Hollmann et al., 2023b, 2025].
    - Mở rộng quy mô ở cấp độ kiến trúc (architecture-level scaling) phục vụ học theo ngữ cảnh (in-context learning) [Gardner et al., 2024, Arazi et al., 2026, Qu et al., 2025].
    - Suy luận tăng cường truy xuất (retrieval-augmented inference) mà không cần tinh chỉnh đặc thù theo nhiệm vụ (without task-specific fine-tuning) [Ma et al., 2025].
  - **Phương pháp dữ liệu bảng dựa trên LLM (LLM-based tabular methods)**: Tái mục đích (repurpose) các mô hình ngôn ngữ tiền huấn luyện cho nhiều tác vụ:
    - Dự đoán ít mẫu (few-shot prediction) [Hegselmann et al., 2023, Dinh et al., 2022].
    - Khái quát hóa ngữ nghĩa (semantic generalization) thông qua siêu dữ liệu dạng văn bản (textual metadata) [Ye et al., 2024a, Kim et al., 2024, Yan et al.].
    - Các tác vụ bổ trợ (auxiliary tasks) gồm tăng cường dữ liệu (data augmentation) [Zhang et al., 2023b, Borisov et al.], làm sạch dữ liệu (data cleaning) [Bendinelli et al.], và sinh đặc trưng (feature generation) [Hollmann et al., 2023a].
- **Khoảng trống nghiên cứu và mục tiêu của TOPOFE**: Bất chấp các tiến bộ trên, các phương pháp hiện tại phần lớn dựa vào sự thích ứng theo từng nhiệm vụ (per-task adaptation) và thiếu cơ chế tìm kiếm có nguyên tắc (principled search mechanisms) trên không gian đặc trưng; TOPOFE được thiết kế chuyên biệt để cung cấp cơ chế này.

### 6.3 LLM-guided Evolutionary Search

- **Tích hợp LLM làm toán tử tiến hóa (Evolutionary Operators)**: Một khối lượng nghiên cứu ngày càng gia tăng ứng dụng LLM làm toán tử tiến hóa trên nhiều lĩnh vực:
  - Tối ưu hóa prompt (prompt optimization) [Guo et al., 2023, Fernando et al., Suzgun et al., 2026, Agrawal et al.].
  - Khám phá chương trình và thuật toán (program and algorithm discovery) [Šurina et al., Assumpção et al., 2025, Novikov et al., 2025, Sharma, Lange et al., 2025].
  - Khám phá khoa học (scientific discovery) [Shojaee et al., Yang et al., 2025b, Chen et al., 2026, Abhyankar et al., 2026].
- **Động lực học quần thể (Population Dynamics) trong các hệ thống hiện có**: Các hệ thống khác nhau chủ yếu ở phương thức quản lý quần thể:
  - Sử dụng MAP-Elites [Novikov et al., 2025].
  - Tiến hóa dựa trên đảo (island-based evolution) [Assumpção et al., 2025].
  - Tối ưu hóa đường biên Pareto (Pareto frontier optimization) [Agrawal et al.].
  - Chọn lọc thúc đẩy bởi độ đa dạng (diversity-driven selection) [Sharma].
  - Các khung nâng cao kết hợp đồng tiến hóa (co-evolution) và phản tư siêu cấp (meta-reflection) [Liu et al., Ye et al., 2024b], hoặc tiến hóa tác tử lặp (iterative agent evolution) [Yuan et al., 2025, Shang et al.].
- **Hạn chế của các phương pháp hiện hữu và vai trò của TOPOFE**: Mặc dù hiệu quả, các phương pháp hiện tại vẫn xem không gian tìm kiếm là đồng nhất về mặt cấu trúc (structurally uniform) và không tích hợp phân rã ngữ nghĩa (semantic decomposition), điều kiện hóa đề xuất thích ứng với nhiệm vụ (task-adaptive proposal conditioning), hay chuyển giao kích hoạt khi bão hòa (saturation-triggered transfer) — tất cả những yếu tố này đều đóng vai trò cốt lõi trong TOPOFE.
