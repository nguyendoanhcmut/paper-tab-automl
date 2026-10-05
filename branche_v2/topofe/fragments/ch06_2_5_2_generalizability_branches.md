### 5.2 Generalizability

- **Mục tiêu đánh giá tính tổng quát hóa (Generalizability)**: Đánh giá xem hiệu quả của TOPOFE có bị phụ thuộc vào một mô hình ngôn ngữ lớn nền tảng (LLM backbone) cụ thể hay không.
- **Cấu hình thực nghiệm đối chuẩn 3 LLM backbone**: TOPOFE được khởi tạo trên 3 mô hình trải rộng trên dải năng lực đại diện (representative capability range), trong đó toàn bộ các thành phần hệ thống khác đều được giữ nguyên không đổi:
  - **Qwen2.5-Coder-7B** ([Hui et al., 2024]): Mô hình mã nguồn mở chuyên biệt hóa về mã nguồn (code-specialised open-source model).
  - **Qwen3-8B** ([Yang et al., 2025a]): Mô hình mã nguồn mở đa năng (general-purpose open-source model).
  - **GPT-4o-mini** ([Hurst et al., 2024]): Mô hình thương mại/độc quyền (proprietary model) có năng lực mạnh hơn.
- **Kết quả hiệu năng trung bình trên các tập dữ liệu (Bảng 3)**: Hiệu năng trung bình của TOPOFE trên tất cả các tập dữ liệu phân loại và hồi quy dưới 3 LLM backbone được tổng hợp như sau:

| Task | QwenCode-7B | Qwen3-8B | GPT-4o-mini |
| :--- | :---: | :---: | :---: |
| Classification ($\text{Accuracy} \uparrow$) | $0.8371$ | $0.8403$ | $0.8468$ |
| Regression ($\text{RMSE} \downarrow$) | $2.6790$ | $2.6928$ | $2.6342$ |

- **Phát hiện 1 — Tính nhất quán cao giữa các backbone nhờ cơ chế kiến trúc**: TOPOFE đạt hiệu năng vững chắc và nhất quán trên cả 3 backbone đối với cả hai dạng tác vụ (phân loại và hồi quy).
  - Sự biến thiên hiệu năng nhỏ giữa các backbone (dù khác biệt lớn về năng lực và phương pháp huấn luyện) khẳng định rằng các mức tăng hiệu năng cốt lõi của TOPOFE được thúc đẩy chủ yếu bởi các cơ chế kiến trúc của hệ thống, chỉ bị ảnh hưởng nhẹ bởi năng lực sinh (generative capability) của LLM.
  - Khung làm việc tiến hóa (evolutionary framework) bù đắp hiệu quả cho chất lượng đề xuất ban đầu kém hơn của mô hình nhỏ thông qua cơ chế chọn lọc lặp có hướng dẫn bởi độ thích nghi (iterative fitness-guided selection).
- **Phát hiện 2 — Cải thiện đơn điệu theo năng lực mô hình và tối ưu hóa ngân sách đánh giá**: Độ chính xác phân loại ($\text{Accuracy}$) tăng đơn điệu theo năng lực của backbone ($0.8371 \rightarrow 0.8403 \rightarrow 0.8468$).
  - Kết quả này nhất quán với việc các mô hình mạnh hơn sinh ra nhiều chương trình tuân thủ lược đồ (schema-compliant programs) hơn ngay từ lần thử đầu tiên.
  - Việc sinh mã chuẩn xác từ lần đầu giúp giảm thiểu lãng phí ngân sách đánh giá (wasted evaluation budget) do phải hủy bỏ hoặc sửa các chương trình lỗi cú pháp.
- **Kết luận về tính độc lập với mô hình nền tảng (Backbone-agnostic)**: Các kết quả khẳng định TOPOFE có tính độc lập với backbone (backbone-agnostic) trên phương diện thực tiễn rõ rệt, có khả năng triển khai linh hoạt trên các ràng buộc tài nguyên đa dạng mà không cần chỉnh sửa kiến trúc.
