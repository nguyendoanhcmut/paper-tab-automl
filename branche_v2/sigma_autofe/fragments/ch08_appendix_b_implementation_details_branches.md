## Appendix B. Implementation Details

* **Cấu hình chi tiết của các phương pháp Baseline truyền thống (Traditional Baseline Configurations)**:
  * **AutoFeat**:
    * Sử dụng thư viện Python chính thức (`official python library`).
    * Số bước tạo đặc trưng (feature engineering steps): `feateng_steps = 2`.
    * Số lượt chạy lựa chọn đặc trưng (feature selection runs): `featsel_runs = 3`.
  * **DFS (Deep Feature Synthesis)**:
    * Sử dụng thư viện Python chính thức (`official python library`).
    * Độ sâu tối đa của cây biến đổi đặc trưng: `max_depth = 2`.
    * Danh sách các hàm nguyên thủy biến đổi đặc trưng (`trans_primitives`): bao gồm các phép toán `add numeric` (cộng số học), `subtract numeric` (trừ số học), `multiply numeric` (nhân số học), `divide numeric` (chia số học), `natural logarithm` (logarit tự nhiên), `square root` (căn bậc hai), và `absolute` (giá trị tuyệt đối).
  * **OpenFE**:
    * Sử dụng thư viện Python chính thức (`official python library`).
    * Thiết lập theo các tham số mặc định (`default parameters`), bao gồm số luồng xử lý song song `n_jobs = 4` và chế độ theo dõi `verbose = False`.
* **Cấu hình chi tiết của các phương pháp Baseline dựa trên LLM (LLM-based Baseline Configurations)**:
  * **CAAFE**:
    * Sử dụng bản triển khai Python chính thức (`official Python implementation`).
    * Kết hợp với mô hình dự báo hạ nguồn XGBoost nhằm đảm bảo tính so sánh công bằng (`for fair comparison`).
  * **OCTree**:
    * Sử dụng mã nguồn Python chính thức (`official python code`).
* **Môi trường phần cứng, hạ tầng tính toán và thư viện thực thi (Hardware and Software Environment)**:
  * **Hạ tầng triển khai LLM**: Triển khai các mô hình ngôn ngữ lớn thông qua framework vLLM (Kwon et al., 2023) để hỗ trợ quá trình suy luận đạt hiệu năng cao và mở rộng quy mô dễ dàng (efficient and scalable inference).
  * **Tăng tốc mô hình hạ nguồn**: Sử dụng phiên bản GPU của XGBoost (Mitchell & Frank, 2017) cho mô hình dự báo nhằm loại bỏ hoàn toàn nút thắt cổ chai về mặt tính toán của CPU (eliminate the CPU bottleneck).
  * **Tính nhất quán của thực nghiệm**: Toàn bộ các mô hình baseline đều sử dụng bản triển khai chính thức cùng cấu hình chuẩn hóa để đảm bảo độ tin cậy và tính công bằng trong đánh giá so sánh.
