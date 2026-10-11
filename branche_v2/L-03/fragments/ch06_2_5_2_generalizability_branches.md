### 5.2 Generalizability

* Đánh giá tính tổng quát hóa (generalizability) nhằm kiểm chứng xem hiệu quả của $\text{TOPOFE}$ có bị phụ thuộc vào một mô hình nền tảng $\text{LLM}$ (LLM backbone) cụ thể hay không.
    * Khởi tạo $\text{TOPOFE}$ với ba mô hình nền tảng đại diện cho một phổ năng lực điển hình (representative capability range):
        * `Qwen2.5-Coder-7B` (Hui et al., $2024$): mô hình mã nguồn mở chuyên biệt cho mã nguồn (code-specialised open-source model).
        * `Qwen3-8B` (Yang et al., $2025\text{a}$): mô hình mã nguồn mở đa năng (general-purpose open-source model).
        * `GPT-4o-mini` (Hurst et al., $2024$): mô hình thương mại độc quyền có năng lực mạnh hơn (stronger proprietary model).
    * Tất cả các thành phần hệ thống khác của $\text{TOPOFE}$ đều được giữ nguyên đồng nhất giữa các cấu hình thử nghiệm.
* Bảng 3 xác lập hai phát hiện thực nghiệm quan trọng:
    * **Bảng 3.** Hiệu suất trung bình của TOPOFE trên tất cả các tập dữ liệu phân loại và hồi quy dưới ba mô hình nền tảng LLM
      * <img src="assets/table_03_p11.png" alt="Bảng 3" />
      * **Bảng này chứng minh điều gì**
        * TOPOFE duy trì hiệu suất mạnh mẽ và ổn định trên cả tác vụ phân loại và hồi quy bất kể mô hình LLM nền tảng là mã nguồn mở hay thương mại, khẳng định tính độc lập với mô hình nền (backbone-agnostic).
      * **Từ đâu mà thấy được**
        * Hàng phân loại (Accuracy ↑) đạt 0.8371 (QwenCode-7B), 0.8403 (Qwen3-8B) và 0.8468 (GPT-4o-mini); hàng hồi quy (RMSE ↓) đạt 2.6790, 2.6928 và 2.6342, cho thấy độ biến thiên hiệu suất rất nhỏ giữa các mô hình khác biệt về năng lực.
    * Phát hiện 1: $\text{TOPOFE}$ đạt hiệu suất mạnh mẽ và nhất quán trên cả ba mô hình nền tảng đối với cả hai loại tác vụ (phân loại và hồi quy).
        * Mức độ biến thiên hiệu suất nhỏ giữa các mô hình nền tảng vốn khác biệt về năng lực và phương pháp huấn luyện xác nhận rằng các cải tiến cốt lõi của $\text{TOPOFE}$ được thúc đẩy chủ yếu bởi các cơ chế kiến trúc (architectural mechanisms) và chỉ bị ảnh hưởng nhẹ bởi năng lực sinh của các $\text{LLM}$ (generative capability of LLMs).
        * Khung tiến hóa (evolutionary framework) bù đắp hiệu quả cho chất lượng đề xuất chương trình yếu hơn thông qua cơ chế chọn lọc lặp dựa trên độ thích nghi (iterative fitness-guided selection).
    * Phát hiện 2: Độ chính xác phân loại ($\text{Accuracy} \uparrow$) cải thiện đơn điệu (improves monotonically) theo năng lực của mô hình nền tảng:
        * Điểm số $\text{Accuracy}$ tăng dần theo năng lực mô hình: `QwenCode-7B` ($0.8371$) $\to$ `Qwen3-8B` ($0.8403$) $\to$ `GPT-4o-mini` ($0.8468$).
        * Kết quả này phù hợp với cơ chế mô hình mạnh hơn tạo ra nhiều chương trình tuân thủ lược đồ (schema-compliant programs) hơn ngay trong lần thử đầu tiên, giúp giảm lãng phí ngân sách đánh giá (wasted evaluation budget).
    * Kết quả trên tác vụ hồi quy ($\text{RMSE} \downarrow$):
        * Giá trị $\text{RMSE}$ của `QwenCode-7B` là $2.6790$, `Qwen3-8B` là $2.6928$, và `GPT-4o-mini` đạt $2.6342$.
        * Sai số hồi quy duy trì trong biên độ rất hẹp giữa các mô hình nền tảng khác nhau, khẳng định tính vững chắc của các đặc trưng sinh ra.
* Kết luận về tính khả thi thực tế: $\text{TOPOFE}$ độc lập với mô hình nền tảng (backbone-agnostic) theo nghĩa thực tiễn quan trọng, có thể triển khai trên nhiều ràng buộc tài nguyên đa dạng mà không cần sửa đổi kiến trúc (deployable across diverse resource constraints without architectural modification).
