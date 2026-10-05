### 4.5. Ablation Study

- Nghiên cứu cắt bỏ (ablation study) được tiến hành nhằm đánh giá tính hiệu quả của các chiến lược EXIT được đề xuất, cũng như tác động của việc tiền định nghĩa (predefining operations) và theo dõi các phép toán (tracking operations):
  - Bốn biến thể thực nghiệm được so sánh: SIGMA đầy đủ (full SIGMA), SIGMA không có tiền định nghĩa phép toán (SIGMA without predefining operations), SIGMA không theo dõi top-$2$ phép toán xuất hiện thường xuyên nhất (SIGMA without tracking the top-2 most frequent operations), và SIGMA không có chiến lược EXIT (SIGMA without EXIT strategies).
- Đánh giá hiệu quả của chiến lược EXIT đối với tỷ lệ chấp nhận (acceptance rate) và tỷ lệ trùng lặp (duplicate rate):
  - Khi không có chiến lược EXIT (SIGMA without EXIT), $36.6\%$ số đặc trưng sinh ra bị trùng lặp (duplicate rate), đồng nghĩa với việc gần $40\%$ cơ hội tạo đặc trưng bị lãng phí, khiến tỷ lệ chấp nhận đặc trưng bị kéo giảm xuống chỉ còn $9.9\%$.
  - Biến thể SIGMA hoàn chỉnh giải quyết triệt để vấn đề này theo đúng thiết kế: chiến lược EXIT giúp giảm $30\%$ tỷ lệ trùng lặp (duplicate rate giảm xuống còn $6.4\%$), qua đó nâng tỷ lệ chấp nhận đặc trưng lên $13.0\%$.
- Các biến thể cắt bỏ phép toán bộc lộ thiên vị kinh nghiệm cố hữu (inherent heuristic bias) của LLM trong xu hướng lựa chọn phép toán:
  - Khi không tiền định nghĩa các phép toán, LLM vẫn sinh ra $14.1\%$ đặc trưng dư thừa (redundant features), kết quả này tương đương với kịch bản top-$2$ phép toán thường xuyên nhất không được theo dõi lẫn không bị hạn chế.
  - LLM có xu hướng ưu tiên các cặp phép toán - đặc trưng (operation-feature pairings) cụ thể dựa trên đánh giá ban đầu, thay vì tích cực khám phá không gian rộng lớn các phương án thay thế.
  - Hệ quả là tiến trình tối ưu hóa bị giới hạn trong các phép toán ưa thích này, dẫn đến độ đa dạng sinh đặc trưng thấp; hiện tượng này càng trở nên nghiêm trọng khi việc sinh đặc trưng được chấp nhận gặp khó khăn.
  - Việc cập nhật không gian đặc trưng (khi các đặc trưng mới được chấp nhận) sẽ buộc LLM phải tư duy tìm kiếm các phép toán mới; do đó, cơ chế theo dõi (tracking) và cấm (forbidding) các phép toán xuất hiện quá nhiều đóng vai trò thiết yếu giúp nâng cao hiệu năng.
- Tồn tại sự đánh đổi (trade-off) giữa tỷ lệ lỗi mã (code error rate) và tỷ lệ trùng lặp (duplicate rate):
  - Việc cưỡng chế LLM phải sử dụng các phép toán ít thường xuyên hơn (infrequent operations) dẫn đến tỷ lệ lỗi sinh mã cao hơn: tỷ lệ lỗi mã của SIGMA đạt $5.6\%$, cao hơn $4\%$ so với các biến thể cắt bỏ khác (khoảng $1.4\%$).
  - Khi liên tục tiếp xúc với các cặp đặc trưng tương tự, LLM có xu hướng chọn các phép toán quen thuộc, an toàn cho việc sinh mã nhưng lại gây bùng nổ tỷ lệ trùng lặp.
- Phân tích tác động của các mô hình LLM nền tảng đối với hiệu năng của SIGMA:
  - Ba mô hình LLM tiêu biểu được khảo sát bao gồm: Qwen3-4B-Instruct (mô hình dày cỡ nhỏ - small dense), Qwen3-Coder-Next (tổng $80\text{ tỷ}$ tham số, kích hoạt $3\text{ tỷ}$ tham số, kiến trúc MoE), và Llama-3.1-70B (mô hình dày cỡ lớn - large dense).
  - Bảng 3 trình bày chi tiết hiệu năng của SIGMA khi sử dụng các LLM khác nhau theo kích thước tập dữ liệu:

| Dataset Size | Mean F1: Qwen3-4B | Mean F1: Qwen3-Coder | Mean F1: Llama-70B | Mean Rank: Qwen3-4B | Mean Rank: Qwen3-Coder | Mean Rank: Llama-70B | vs Qwen3-4B: Qwen3-Coder | vs Qwen3-4B: Llama-70B |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Small ($\le 2000$) | **71.95%** | 71.34% | 71.27% | **1.60** | 2.2 | 2.2 | -0.61% | -0.67% |
| Large ($> 2000$) | 83.37% | **83.51%** | 83.30% | 2.36 | **1.73** | 1.91 | +0.14% | -0.07% |
| All | **79.80%** | 79.71% | 79.54% | 2.12 | **1.88** | 2.00 | -0.10% | -0.26% |

  - *Ghi chú Table 3*: Llama-70B đại diện cho Llama-3.1-70B; kết quả tốt nhất được in đậm.
  - Phân tích hiện tượng quá khớp (overfitting) trên tập dữ liệu nhỏ:
    - Mặc dù các mô hình mạnh hơn có xu hướng đạt thứ hạng trung bình (mean rank) tốt hơn trên toàn bộ các tập dữ liệu (trong đó Qwen3-Coder-Next đạt thứ hạng tốt nhất là $1.88$ nhờ năng lực chuyên biệt cho tác vụ lập trình), hiệu năng trung bình (mean F1-score) không phải lúc nào cũng cải thiện tương ứng.
    - Hiện tượng này chủ yếu bắt nguồn từ các tập dữ liệu nhỏ ($\le 2000$ mẫu), nơi hiệu năng thể hiện phương sai cao hơn (higher variance): trong quá trình tối ưu hóa tuần tự (sequential optimization), các LLM mạnh hơn có khả năng tạo ra các đặc trưng tối ưu cục bộ trên tập xác thực (validation set), gây ra overfitting trên tập dữ liệu nhỏ.
    - Trái lại, trên các tập dữ liệu lớn ($> 2000$ mẫu), các mô hình quy mô lớn hơn liên tục cải thiện hiệu năng (Qwen3-Coder-Next đạt F1-score $83.51\%$, vượt Qwen3-4B $+0.14\%$).
    - Hiện tượng overfitting trên tập dữ liệu nhỏ này cũng từng được phát hiện trong lĩnh vực Tối ưu hóa Siêu tham số (Hyperparameter Optimization - HPO) (Schneider et al., 2025), cho thấy cần tiếp tục nghiên cứu các chiến lược giảm thiểu trong tương lai.
