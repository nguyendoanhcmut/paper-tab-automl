### 4.3 LLM-FE Configuration

* **Các mô hình ngôn ngữ lớn nền tảng (backbone LLMs):**
  * Trong các thử nghiệm, nghiên cứu sử dụng GPT-3.5-Turbo và Llama-3.1-8B-Instruct làm các mô hình ngôn ngữ lớn nền tảng (backbone LLMs).
* **Tham số lấy mẫu và cấu hình quần đảo (sampling parameters and islands configuration):**
  * Nhiệt độ lấy mẫu (sampling temperature) được thiết lập ở mức $t = 0.8$.
  * Số lượng quần đảo trong mô hình tiến hóa được cấu hình là $m = 3$ đảo ($m = 3$ islands).
* **Sinh chương trình biến đổi đặc trưng (feature transformation program generation):**
  * Tại mỗi vòng lặp (iteration), LLM sinh $b = 3$ chương trình biến đổi đặc trưng (feature transformation programs) cho mỗi câu nhắc (per prompt) bằng ngôn ngữ Python.
  * Để đảm bảo tính nhất quán khi so sánh với các phương pháp cơ sở (baselines), LLM-FE cũng được cấu hình để sử dụng $20$ mẫu sinh LLM ($20$ LLM samples) cho mỗi thử nghiệm.
* **Lựa chọn chương trình khám phá đặc trưng (feature discovery program selection):**
  * Cuối cùng, quy trình lấy mẫu $m$ chương trình khám phá đặc trưng hàng đầu (top $m$ feature discovery programs, với $m$ là số lượng quần đảo) dựa trên điểm số kiểm định (validation scores) tương ứng của chúng.
* **Chi tiết triển khai bổ sung:**
  * Các chi tiết triển khai cụ thể hơn được cung cấp tại Phụ lục B.1 (Appendix B.1).
