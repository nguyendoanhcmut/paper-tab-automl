### 5.6 Ablation Study

- **Thiết kế nghiên cứu cắt bỏ (ablation study setup) nhằm định lượng đóng góp kiến trúc**:
  - Nhằm định lượng đóng góp riêng lẻ của từng thành phần kiến trúc trong TOPOFE, nghiên cứu cắt bỏ có hệ thống được thực hiện bằng cách loại bỏ hoặc điều chỉnh lũy tiến các cơ chế then chốt trong khi cố định toàn bộ các thành phần còn lại.
  - Đánh giá $10$ biến thể được phân bổ vào $4$ nhóm tương ứng với các quyết định kiến trúc trọng yếu:
    - **Phân rã quần thể đảo (Island decomposition)**:
      - *(i) Single Pool*: loại bỏ phân rã đảo và cơ chế di cư (migration), rút gọn TOPOFE về tìm kiếm đơn quần thể (single-population search).
      - *(ii) Random Island*: phân chia quần thể thành các đảo ngẫu nhiên nhưng không gán theo họ phép biến đổi đặc trưng (without family-aware assignment).
    - **Chiến lược di cư (Migration strategy)**:
      - *(iii) w/o Inter-island Exchange*: duy trì phân rã theo họ nhưng vô hiệu hóa hoàn toàn việc trao đổi / di cư liên đảo (cross-island migration).
      - *(iv) Static Migration*: thay thế cơ chế chuyển giao kích hoạt khi bão hòa (saturation-triggered transfer) bằng di cư theo chu kỳ cố định (fixed-interval migration).
      - *(v) Stochastic Migration*: lựa chọn các đảo tiền thân (precursor islands) ngẫu nhiên đồng đều (uniformly at random).
    - **Cơ chế chuyển giao (Transfer mechanism)**:
      - *(vi) Direct Transfer (Direct Feature Transfer)*: sao chép trực tiếp các chương trình từ đảo tiền thân mà không thực hiện tổng hợp lai ghép (without hybrid synthesis).
      - *(vii) Unguided Hybridisation (Unguided Cross-Island Hybridization)*: cho phép tổng hợp lai ghép với các đảo tiền thân chọn ngẫu nhiên, vô hiệu hóa sự dẫn đường của cấu trúc tô-pô (disabling topology guidance).
      - *(viii) w/o Hybridisation (w/o Hybridization)*: bảo toàn việc chọn đảo tiền thân có dẫn đường tô-pô nhưng loại bỏ bước tổng hợp qua trung gian LLM (removes LLM-mediated synthesis).
    - **Phát hiện điểm bão hòa (Saturation detection)**:
      - *(ix) Correlation-Only (Correlation-Only Saturation)*: thay thế tiêu chuẩn bão hòa phức hợp bằng một tín hiệu tương quan đầu ra đơn lẻ (single output-correlation signal).
      - *(x) Multi-signal Saturation*: khôi phục đầy đủ cơ chế phát hiện bão hòa thích ứng đa tín hiệu (full multi-signal adaptive saturation detection) mà không có các thành phần toàn hệ thống khác.

- **Mức độ suy giảm hiệu năng (performance degradation) của các biến thể thực nghiệm (Hình 3)**:
  - **Hình 3.** Nghiên cứu cắt bỏ thành phần (Ablation study) của TOPOFE
    - <img src="assets/fig_03_p14_vector.png" alt="Hình 3" />
    - **Hình này chứng minh điều gì**
      - Mức độ suy giảm hiệu năng tương đối (%) của $10$ biến thể so với TOPOFE toàn phần trên cả hai loại tác vụ (phân loại và hồi quy), khẳng định tính thiết yếu của từng thành phần kiến trúc.
    - **Từ đâu mà thấy được**
      - Biểu đồ cột thể hiện mức suy giảm hiệu năng trung bình trên toàn bộ tập dữ liệu cho hai loại tác vụ (cột xanh đậm và xanh nhạt): `Single Pool` chịu mức suy giảm nặng nhất ($3.58\%$ và $8.24\%$), kế tiếp là `Random Island` ($3.28\%$ và $7.86\%$), trong khi `Multi-Signal Saturation` có mức suy giảm thấp nhất ($2.55\%$ và $6.42\%$).
  - Số liệu suy giảm chi tiết trên từng biến thể qua hai nhóm tác vụ:
    - `Single Pool`: suy giảm $3.58\%$ và $8.24\%$.
    - `Random Island`: suy giảm $3.28\%$ và $7.86\%$.
    - `w/o Inter-island Exchange`: suy giảm $3.15\%$ và $7.59\%$.
    - `Static Migration`: suy giảm $3.06\%$ và $7.38\%$.
    - `Stochastic Migration`: suy giảm $2.87\%$ và $7.29\%$.
    - `Direct Feature Transfer`: suy giảm $2.84\%$ và $7.21\%$.
    - `Unguided Cross-Island Hybridization`: suy giảm $2.79\%$ và $7.14\%$.
    - `w/o Hybridization`: suy giảm $2.83\%$ và $7.08\%$.
    - `Correlation-Only Saturation`: suy giảm $2.88\%$ và $6.75\%$.
    - `Multi-Signal Saturation`: suy giảm $2.55\%$ và $6.42\%$.

- **Phân tích cơ chế và đóng góp của phân rã quần thể đảo (Island decomposition)**:
  - Mức sụt giảm hiệu năng lớn nhất xảy ra ở biến thể `Single Pool` ($3.58\%$ và $8.24\%$), xác nhận rằng tìm kiếm đơn quần thể phi cấu trúc (unstructured single-population search) là điểm nghẽn chính: khi không có phân rã đảo, không gian tìm kiếm nhanh chóng sụp đổ về các mẫu biến đổi áp đảo (dominant transformation patterns), dẫn đến hiện tượng hội tụ sớm (premature convergence) và triệt tiêu độ đa dạng.
  - Mức cải thiện khi chuyển từ `Random Island` ($3.28\% / 7.86\%$) sang `w/o Inter-island Exchange` ($3.15\% / 7.59\%$) chứng minh rằng việc phân rã nhận thức theo họ biến đổi (family-aware decomposition) đóng góp cấu trúc quy nạp có ý nghĩa vượt trội so với phân vùng ngẫu nhiên đơn thuần: nâng cao hiệu suất tối ưu hóa cục bộ nhờ điều kiện hóa các đề xuất của LLM trên một ngữ cảnh toán tử đồng nhất (homogeneous operator context).

- **Phân tích cơ chế và vai trò của chiến lược di cư (Migration strategy)**:
  - Hiệu quả chuyển giao liên đảo phụ thuộc mang tính quyết định vào cả thời điểm kích hoạt chuyển giao (timing) lẫn chất lượng của đảo tiền thân (precursor quality).
  - Biến thể `Static Migration` làm lãng phí ngân sách chuyển giao do kích hoạt di cư ngay cả khi tiến trình tìm kiếm cục bộ vẫn đang hoạt động hiệu quả và sinh lời (productive).
  - Biến thể `Stochastic Migration` suy giảm hiệu năng nghiêm trọng hơn ($2.87\% / 7.29\%$) do đưa vào các phép biến đổi không liên quan về mặt cấu trúc (structurally unrelated transformations), làm xáo trộn và phá vỡ các quần thể đã thích nghi tối ưu cục bộ (locally adapted populations).

- **Phân tích vai trò của cơ chế chuyển giao và tổng hợp lai ghép (Transfer mechanism & Hybrid synthesis)**:
  - Các thử nghiệm cắt bỏ cơ chế chuyển giao xác nhận tính tất yếu của quá trình tổng hợp kết hợp (compositional synthesis): biến thể `Direct Transfer` chỉ đem lại lợi ích hạn chế ($2.84\% / 7.21\%$) do các chương trình sao chép vẫn bị giới hạn trong thiên vị quy nạp của họ gốc (source family's inductive bias).
  - Quá trình tổng hợp qua trung gian LLM (LLM-mediated synthesis) giải quyết triệt để rào cản này bằng cách kiến tạo các chương trình liên họ (spanning multiple families) vốn không thể tiếp cận nếu chỉ dựa vào tìm kiếm nội bộ trong đảo (intra-island search alone).
  - Biến thể `Unguided Hybridization` vẫn ở mức dưới tối ưu ($2.79\% / 7.14\%$) dù có kích hoạt tổng hợp lai ghép, chứng minh rằng sự dẫn đường của cấu trúc tô-pô (topology guidance) và tổng hợp lai ghép có mối quan hệ đồng vận (synergistic): cơ chế chọn đảo tiền thân qua học hỏi đảm bảo quá trình lai ghép nhắm trúng các cặp họ bổ trợ lẫn nhau (complementary family pairs), tối đa hóa khả năng đưa vào các cấu trúc dự đoán không dư thừa (non-redundant predictive structure).

- **Phân tích vai trò của cơ chế phát hiện điểm bão hòa thích ứng (Saturation detection)**:
  - Các thử nghiệm bóc tách xác nhận cơ chế phát hiện đình trệ đa tín hiệu (multi-signal stagnation detection) là thành phần thiết yếu.
  - Biến thể `Correlation-Only Saturation` suy giảm hiệu năng đáng kể ($2.88\% / 6.75\%$) do chỉ riêng tương quan đầu ra (output correlation) không thể phân biệt giữa đình trệ thực sự (genuine stagnation) và sự dư thừa thoáng qua (transient redundancy): một đảo có thể bị đình trệ về mặt hiệu năng nhưng vẫn duy trì tương quan thấp, hoặc có thể thể hiện tương quan cao do vài đề xuất trùng lặp cá biệt trong khi toàn cục vẫn đang sinh lời tốt.
  - Tiêu chuẩn phức hợp đa tín hiệu (multi-signal composite criterion) phân biệt chính xác hai trạng thái trên, chỉ kích hoạt chuyển giao liên đảo khi tiến trình tìm kiếm cục bộ thực sự cạn kiệt (genuinely exhausted) trên toàn bộ các phương diện về độ đa dạng và hiệu năng.
