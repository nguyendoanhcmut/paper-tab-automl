### D.3 Khả năng chuyển giao của các đặc trưng được sinh (Transferability of Generated Features)

- **Mục tiêu và Động lực về Chuyển giao Đặc trưng (Feature Transfer)**:
  - Trong khi các phương pháp truyền thống thường sử dụng cùng một mô hình cho cả quá trình sinh đặc trưng (feature generation) lẫn quá trình suy luận (inference), nghiên cứu này chứng minh rằng các đặc trưng được tạo ra bởi một mô hình hoàn toàn có thể được tái sử dụng và phục vụ hiệu quả cho các mô hình khác.
  - Kế thừa tiếp cận từ Nam et al. (2024), nhóm tác giả sử dụng **XGBoost**—một mô hình dựa trên cây quyết định (decision tree-based model) có chi phí tính toán thấp và hiệu quả cao—để sinh ra các biến đặc trưng phục vụ cho các kiến trúc phức tạp hơn trong giai đoạn suy luận.

- **Phân tích Thực nghiệm và Đối sánh Hiệu năng (Bảng 13)**:
  - Bảng 13 trình bày kết quả phân tích so sánh của LLM-FE khi thực hiện chuyển giao đặc trưng sang hai kiến trúc mô hình khác nhau là MLP và TabPFN.
  - Các kết quả đo lường độ chính xác phân loại (Classification Accuracy $\uparrow$) đối với tác vụ phân loại và sai số căn bậc hai trung bình chuẩn hóa (Normalized Root-Mean-Square Error - NRMSE $\downarrow$) đối với tác vụ hồi quy, biểu diễn qua giá trị trung bình và độ lệch chuẩn ($\text{Mean} \pm \text{Std}$) sau 5 lần phân chia ngẫu nhiên (five random splits).
  - Các giá trị in đậm biểu thị hiệu năng tốt nhất trên từng kiến trúc mô hình.

| Kiến trúc (Architecture) | Phương pháp (Method) | LLM | Phân loại (Classification) ↑ | Hồi quy (Regression - NRMSE) ↓ |
| :--- | :--- | :--- | :---: | :---: |
| **MLP** | Base | – | $0.745 \pm 0.034$ | $0.871 \pm 0.027$ |
| | $\text{LLM-FE}_{\text{XGB}}$ | GPT-3.5-Turbo | $0.763 \pm 0.030$ | $0.848 \pm 0.017$ |
| | $\text{LLM-FE}$ | GPT-3.5-Turbo | $\mathbf{0.791 \pm 0.029}$ | $\mathbf{0.631 \pm 0.043}$ |
| **TabPFN** | Base | – | $0.852 \pm 0.028$ | $0.289 \pm 0.016$ |
| | $\text{LLM-FE}_{\text{XGB}}$ | GPT-3.5-Turbo | $0.861 \pm 0.017$ | $0.287 \pm 0.015$ |
| | $\text{LLM-FE}$ | GPT-3.5-Turbo | $\mathbf{0.863 \pm 0.018}$ | $\mathbf{0.286 \pm 0.015}$ |

- **Phân tích Chi tiết trên Từng Kiến trúc Mô hình**:
  - **Mạng Perceptron Đa lớp (Multi-Layer Perceptron - MLP)**:
    - Khi nhận các đặc trưng chuyển giao sinh từ XGBoost ($\text{LLM-FE}_{\text{XGB}}$), hiệu năng của MLP vượt trội hơn phiên bản cơ sở (`Base`) trên cả hai tác vụ: độ chính xác phân loại tăng từ $0.745 \pm 0.034$ lên $0.763 \pm 0.030$, và sai số NRMSE hồi quy giảm từ $0.871 \pm 0.027$ xuống $0.848 \pm 0.017$.
    - Khi tối ưu hóa đặc trưng trực tiếp bằng chính MLP thông qua LLM-FE, mô hình đạt mức cải thiện cao nhất ($\mathbf{0.791 \pm 0.029}$ cho phân loại và $\mathbf{0.631 \pm 0.043}$ cho hồi quy).
  - **Mạng Khớp Tiên nghiệm cho Dữ liệu Bảng (Prior-data Fitted Network - TabPFN)**:
    - Việc sử dụng các đặc trưng chuyển giao từ XGBoost ($\text{LLM-FE}_{\text{XGB}}$) nâng hiệu năng của TabPFN vượt qua bản `Base`: độ chính xác phân loại tăng từ $0.852 \pm 0.028$ lên $0.861 \pm 0.017$, còn sai số NRMSE giảm từ $0.289 \pm 0.016$ xuống $0.287 \pm 0.015$.
    - Mức hiệu năng này tiếp cận rất gần với kết quả khi tối ưu trực tiếp bằng TabPFN ($\text{LLM-FE}$ đạt $\mathbf{0.863 \pm 0.018}$ và $\mathbf{0.286 \pm 0.015}$).

- **Phát hiện Then chốt và Ý nghĩa Khoa học**:
  - **Cải thiện hiệu năng liên kiến trúc (Cross-architecture performance improvement)**: Các đặc trưng do XGBoost sinh ra đem lại sự tăng trưởng hiệu năng rõ rệt cho cả MLP và TabPFN so với các phiên bản cơ sở tương ứng.
  - **Nắm bắt đặc tính dữ liệu có ý nghĩa (Capturing meaningful data characteristics)**: Hiện tượng chuyển giao thành công chứng minh các biến đặc trưng do LLM-FE tạo ra nắm bắt được những thuộc tính dữ liệu mang ý nghĩa bản chất, có giá trị chung xuyên suốt nhiều hệ hình mô hình hóa (modeling paradigms) khác nhau thay vì chỉ hoạt động cục bộ trên một thuật toán đơn lẻ.
  - **Tính ứng dụng thực tiễn cao**: Do XGBoost có chi phí tính toán rẻ và tốc độ xử lý nhanh, việc sử dụng XGBoost để khám phá và sinh đặc trưng, sau đó chuyển giao sang các mô hình phức tạp hơn để suy luận là giải pháp khả thi giúp cân bằng tối ưu giữa chi phí tính toán và chất lượng mô hình.
