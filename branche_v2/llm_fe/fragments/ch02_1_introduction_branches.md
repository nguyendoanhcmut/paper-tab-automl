## 1 Introduction

### Bối cảnh và Thách thức trong Kỹ thuật Đặc trưng Dữ liệu Bảng (Context & Challenges in Tabular Feature Engineering)
- **Tầm quan trọng cốt lõi của kỹ thuật tạo đặc trưng (Feature Engineering - FE)**:
  - Feature engineering (kỹ thuật tạo đặc trưng) là quá trình chuyển đổi raw data (dữ liệu thô) thành các đặc trưng có ý nghĩa phục vụ các mô hình học máy, đóng vai trò then chốt trong việc nâng cao predictive performance (hiệu năng dự đoán), đặc biệt là đối với tabular data (dữ liệu dạng bảng) (Domingos, 2012).
  - Trong nhiều tác vụ dự đoán trên dữ liệu bảng, các đặc trưng được thiết kế tốt giúp nâng cao vượt bậc hiệu năng của tree-based models (các mô hình dựa trên cây như XGBoost), thường vượt trội hơn cả deep learning models (các mô hình học sâu) vốn phụ thuộc vào learned representations (biểu diễn học được) (Grinsztajn et al., 2022).
  - Tuy nhiên, các tác vụ data-centric (lấy dữ liệu làm trung tâm) như kỹ thuật đặc trưng là một trong những quy trình tốn thời gian và tiêu hao tài nguyên tính toán nhất trong tabular learning workflow (quy trình học dữ liệu bảng) (Anaconda, 2020; Hollmann et al., 2024), do đòi hỏi các chuyên gia dữ liệu phải rà soát thủ công giữa không gian tổ hợp khổng lồ của các phép biến đổi khả dĩ.

- **Hạn chế của các phương pháp tự động hóa truyền thống (Classical AutoFE)**:
  - Các phương pháp kỹ thuật đặc trưng cổ điển (Kanter & Veeramachaneni, 2015; Khurana et al., 2016; 2018; Horn et al., 2020; Zhang et al., 2023) xây dựng không gian tìm kiếm rộng lớn các toán tử xử lý đặc trưng và sử dụng các thuật toán tối ưu hóa heuristic để lựa chọn đặc trưng hiệu quả.
  - *Điểm nghẽn*: Không gian tìm kiếm bị giới hạn chặt chẽ bởi các phép biến đổi tiền định (predefined transformations) được thiết kế thủ công, hoàn toàn thiếu khả năng tiếp cận và tích hợp domain knowledge (tri thức miền) (Zhang et al., 2023).
  - *Giá trị của tri thức miền*: Tri thức miền đóng vai trò như một invaluable prior (tiên nghiệm vô giá) giúp định hướng phát hiện các phép biến đổi phù hợp, làm giảm độ phức tạp tìm kiếm và tạo ra các đặc trưng vừa có tính giải thích cao (interpretable) vừa đạt hiệu quả vượt trội (Hollmann et al., 2024).

- **Thách thức của các phương pháp ứng dụng LLM hiện tại**:
  - Sự xuất hiện của Large Language Models (LLMs - các mô hình ngôn ngữ lớn) mang lại cơ hội đột phá nhờ kho tri thức miền phong phú được nhúng sẵn bên trong mô hình.
  - Tuy nhiên, các phương pháp khai thác LLM gần đây (Hollmann et al., 2024; Han et al., 2024) chủ yếu dựa vào direct prompting (câu nhắc trực tiếp) hoặc chỉ sử dụng validation scores (điểm kiểm định) đơn thuần để dẫn dắt quá trình sinh đặc trưng.
  - *Hệ quả*: Các cách tiếp cận này không khai thác được bài học kinh nghiệm từ lịch sử các thử nghiệm khám phá đặc trưng trước đó, dẫn đến việc chưa thể thiết lập mối liên kết suy luận có ý nghĩa giữa quá trình sinh đặc trưng và data-driven performance (hiệu năng định hướng bởi dữ liệu thực nghiệm).

### Khung làm việc Tối ưu hóa Tiến hóa LLM-FE (LLM-FE Evolutionary Optimization Framework)
- **Đề xuất khung làm việc LLM-FE**:
  - Nghiên cứu giới thiệu **LLM-FE**, một khung làm việc mới tích hợp năng lực suy luận của LLM với các mô hình dự đoán dạng bảng và evolutionary search (tìm kiếm tiến hóa) nhằm hiện thực hóa quá trình tối ưu hóa đặc trưng hiệu quả.
  - LLM-FE vận hành theo một vòng lặp kín để sinh và đánh giá các giả thuyết biến đổi đặc trưng, sử dụng phản hồi hiệu năng từ mô hình dự đoán làm phần thưởng (reward) để nâng cao chất lượng đặc trưng.
  - LLM đóng vai trò như một knowledge-guided evolutionary optimizer (bộ tối ưu hóa tiến hóa được dẫn dắt bởi tri thức), thực hiện đột biến (mutating) các chương trình biến đổi đặc trưng thành công trước đó để sinh ra các đặc trưng mới hiệu quả hơn (Meyerson et al., 2024).

- **Cơ chế 4 giai đoạn của chu trình LLM-FE (Hình 1)**:
  - *(a) New Feature Generation (Sinh đặc trưng mới)*: Bắt đầu từ chương trình biến đổi ban đầu, LLM tiếp nhận prompt chứa đặc tả tác vụ, mô tả ngữ nghĩa các cột thuộc tính, và mẫu dữ liệu cụ thể để sinh ra các chương trình khám phá đặc trưng mới dưới dạng mã nguồn Python.
  - *(b) Feature Engineering (Biến đổi đặc trưng)*: Áp dụng chương trình biến đổi lên tập dữ liệu thô để tạo thành tập dữ liệu tăng cường (augmented dataset). Ví dụ: tính toán chỉ số kháng insulin qua công thức $\text{insulin\_resistance} = (\text{glucose} \times \text{insulin}) / 405$ và tương tác $\text{age\_bmi} = \text{age} \times \text{bmi}$.
  - *(c) Feature Evaluation (Đánh giá đặc trưng)*: Huấn luyện mô hình dự đoán (XGBoost, TabPFN, MLP) trên tập dữ liệu tăng cường và đánh giá điểm số (như validation accuracy $0.8034$, $0.8247$, v.v.) trên held-out validation set (tập kiểm định độc lập).
  - *(d) Experience Management (Quản lý kinh nghiệm)*: Lưu trữ các chương trình biến đổi đạt điểm cao vào bộ nhớ dài hạn đa đảo (multi-island memory buffer: Island $1$, Island $2$, $\dots$, Island $k$) để làm in-context demonstrations (mẫu minh họa ngữ cảnh) cho các vòng tinh chỉnh kế tiếp của LLM.
  - **Hình 1.** Tổng quan khung làm việc tối ưu hóa đặc trưng LLM-FE.
    - <img src="assets/fig_01_p2.png" alt="Hình 1" />
    - **Hình này chứng minh điều gì**
      - Quy trình lặp 4 bước kết hợp LLM, mô hình dự đoán và bộ nhớ tiến hóa đa đảo để tự động sinh và tinh chỉnh đặc trưng.
    - **Từ đâu mà thấy được**
      - Sơ đồ tương tác khép kín: (a) New Feature Generation, (b) Feature Engineering, (c) Feature Evaluation với mô hình ML, và (d) Experience Management qua các đảo lưu trữ (Island 1 đến Island k).

### So sánh với các Phương pháp Hiện có (Comparison with Existing Methods)
- **So sánh đa chiều giữa LLM-FE và các phương pháp cơ sở (Bảng 1)**:
  - Bảng 1 tổng hợp sự khác biệt cốt lõi giữa LLM-FE và các phương pháp kỹ thuật đặc trưng truyền thống lẫn các phương pháp dựa trên LLM theo 4 khía cạnh: Tri thức miền (Domain Knowledge), Dẫn dắt bởi phản hồi (Feedback Driven), Đặc trưng phức tạp (Complex Features), và Tinh chỉnh đa đặc trưng (Multi-Feature Refinement):

| Phương pháp (Method) | Tri thức miền (Domain Knowledge) | Dẫn dắt bởi phản hồi (Feedback Driven) | Đặc trưng phức tạp (Complex Features) | Tinh chỉnh đa đặc trưng (Multi-Feature Refinement) |
| :--- | :---: | :---: | :---: | :---: |
| AutoFeat (Horn et al., 2020) | ✗ | ✗ | ✓ | ✗ |
| OpenFE (Zhang et al., 2023) | ✗ | ✗ | ✓ | ✗ |
| FeatLLM (Han et al., 2024) | ✓ | ✗ | ✗ | ✗ |
| CAAFE (Hollmann et al., 2024) | ✓ | ✓ | ✗ | ✗ |
| OCTree (Nam et al., 2024) | ✓ | ✓ | ✗ | ✗ |
| **LLM-FE** | **✓** | **✓** | **✓** | **✓** |

- **Phân tích ưu thế toàn diện của LLM-FE**:
  - *Hạn chế của phương pháp cổ điển*: AutoFeat và OpenFE hỗ trợ các phép biến đổi toán tử phức tạp nhưng hoàn toàn thiếu tri thức ngữ cảnh miền và không có phản hồi từ mô hình dự đoán downstream.
  - *Hạn chế của phương pháp LLM đi trước*: FeatLLM chỉ sinh các luật nhị phân tĩnh; CAAFE và OCTree có sử dụng phản hồi kiểm định nhưng chỉ sinh các đặc trưng đơn giản (Küken et al., 2024) hoặc bị giới hạn trong việc tinh chỉnh một quy tắc duy nhất tại một thời điểm.
  - *Tính vượt trội của LLM-FE*: Là phương pháp duy nhất tích hợp đồng thời cả 4 tiêu chuẩn, LLM-FE tận dụng tri thức miền từ LLM kết hợp với tối ưu hóa tiến hóa có phản hồi dữ liệu để liên tục sinh và tinh chỉnh các tập đặc trưng phức tạp, đa biến.

- **Hiệu năng thực nghiệm và khả năng chuyển giao**:
  - LLM-FE được đánh giá trên các mô hình ngôn ngữ nền tảng Llama-3.1-8B-Instruct (Dubey et al., 2024) và GPT-3.5-Turbo (OpenAI, 2023) xuyên suốt các tác vụ phân loại và hồi quy trên nhiều tập dữ liệu bảng.
  - Khung làm việc liên tục vượt trội hơn các phương pháp FE tiên tiến nhất, tạo ra các đặc trưng có ý nghĩa ngữ cảnh giúp cải thiện rõ rệt hiệu năng của các mô hình dự đoán dạng bảng phổ biến như XGBoost (Chen & Guestrin, 2016), TabPFN (Hollmann et al., 2023), và MLP (Gorishniy et al., 2021).

### Các Đóng góp Chính của Nghiên cứu (Key Contributions)
- **Mô hình hóa kỹ thuật đặc trưng như bài toán tối ưu hóa tiến hóa**:
  - Giới thiệu LLM-FE, một khung làm việc mới mô hình hóa bài toán kỹ thuật đặc trưng dưới dạng tối ưu hóa tiến hóa được định hướng bởi LLM (LLM-guided evolutionary optimization), kết hợp chặt chẽ tri thức miền, đánh giá dựa trên dữ liệu thực nghiệm, và bộ nhớ dài hạn để phục vụ tinh chỉnh lặp.
- **Hiệu năng vượt trội và tính tổng quát hóa cao (Generalizability)**:
  - Minh chứng qua thực nghiệm rằng LLM-FE vượt trội nhất quán so với các phương pháp cơ sở hiện đại nhất (SOTA baselines), đồng thời thể hiện khả năng tổng quát hóa xuất sắc trên nhiều mô hình dự đoán (predictors) và nhiều mô hình ngôn ngữ nền tảng (LLM backbones) khác nhau.
- **Nghiên cứu cắt bỏ toàn diện (Comprehensive Ablation Study)**:
  - Thực hiện phân tích cắt bỏ chi tiết để chứng minh vai trò thiết yếu của từng thành phần: tri thức miền (domain knowledge), tìm kiếm tiến hóa (evolutionary search), phản hồi định hướng dữ liệu (data-driven feedback), và các mẫu dữ liệu cụ thể (data samples) trong việc dẫn dắt LLM khám phá không gian đặc trưng hiệu quả và phát hiện các đặc trưng có tác động lớn nhất.
