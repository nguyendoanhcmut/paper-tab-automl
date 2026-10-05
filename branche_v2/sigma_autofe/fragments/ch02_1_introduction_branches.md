## 1. Introduction

- **Tự động hóa Kỹ thuật Đặc trưng (Automated Feature Engineering - AutoFE)** (Hutter et al., 2019) là thành phần then chốt trong Học máy Tự động (AutoML) (Ravishankar and Battineni, 2025):
  - Mục tiêu hàng đầu của AutoFE là tạo ra các đặc trưng mới nhằm nâng cao năng lực biểu diễn (representational power) của tập đặc trưng ban đầu, qua đó cải thiện hiệu suất và độ vững chắc (robustness) của AutoML.
  - AutoFE được ứng dụng rộng rãi trong nhiều lĩnh vực thực tế như tài chính và y tế (Hollmann et al., 2023; Lucas et al., 2020; Waring et al., 2020).

- **Hạn chế của các phương pháp AutoFE truyền thống**:
  - Chủ yếu tiếp cận theo khung mở rộng-thu giảm (expansion-reduction framework), khám phá không gian tổ hợp rộng lớn của các phép biến đổi đặc trưng được định nghĩa trước (predefined feature transformations) (Zhang et al., 2023; Hollmann et al., 2023).
  - Mặc dù mang lại hiệu năng cao khi có đủ ngân sách tìm kiếm, không gian tìm kiếm thủ công rất phức tạp để thiết kế và giới hạn phạm vi khám phá, dễ dẫn đến kết quả dưới mức tối ưu (sub-optimal) (Abhyankar et al., 2025).
  - Rất khó để diễn giải số lượng lớn các đặc trưng được sinh ra từ các phương pháp này.

- **Tiềm năng và rào cản của AutoFE dựa trên Mô hình Ngôn ngữ Lớn (LLMs)**:
  - Năng lực suy luận mạnh mẽ (Wei et al., 2022) và khả năng học trong ngữ cảnh (In-Context Learning - ICL) (Dong et al., 2024) của LLMs (Chang et al., 2024) mở ra hướng nghiên cứu tận dụng LLMs để nâng cao AutoFE thông qua tối ưu hóa tuần tự (sequential optimization).
  - Bằng việc cung cấp mô tả ngữ nghĩa (về đặc trưng và tác vụ) cùng thông tin thống kê (Fathollahzadeh et al., 2025), LLMs có thể sinh các đặc trưng có khả năng giải thích tốt dựa trên tri thức miền (domain knowledge) (Li et al., 2026; Han et al., 2024), đầy triển vọng cho Tác nhân Khoa học Dữ liệu (Data Science Agent - DS Agent) (Guo et al., 2024; Chen et al., 2025).
  - *Rào cản thiếu siêu dữ liệu (Metadata-free challenge)*: Giả định luôn có sẵn thông tin ngữ nghĩa làm giới hạn tính ứng dụng thực tế (Nam et al., 2024), đặc biệt trong các bộ dữ liệu y tế bảo vệ quyền riêng tư (privacy-preserving medical datasets) hoặc nhật ký cảm biến (sensor logs) nơi thông tin ngữ nghĩa không có sẵn hoặc không đáng tin cậy.
  - *Bùng nổ ngữ cảnh và thiên kiến trong quỹ đạo tối ưu (Context explosion & Trajectory bias)*: Sự mở rộng liên tục của quỹ đạo tối ưu hóa dùng cho ICL làm tăng nguy cơ vượt quá giới hạn độ dài ngữ cảnh (context length constraints) và gây thiên kiến vào các cặp đặc trưng-phép toán thành công trước đó; ngược lại, nếu loại bỏ hoàn toàn thông tin quỹ đạo, LLMs lại có xu hướng sinh ra các đặc trưng trùng lặp (duplicate generation).

- **Khung tối ưu hóa SIGMA (SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE)**:
  - SIGMA là khung tối ưu hóa ngữ cảnh cố định, có khả năng mở rộng (scalable constant-context optimization framework) dành cho AutoFE dựa trên LLM không cần siêu dữ liệu (metadata-free).
  - **Hình 1.** Tổng quan kiến trúc hệ thống SIGMA
    - <img src="assets/fig_01_p2.png" alt="Hình 1" />
    - **Hình này chứng minh điều gì**
      - Kiến trúc tích hợp SHAP-based feature grouping và chiến lược tối ưu implicit trajectory EXIT để duy trì context cố định
    - **Từ đâu mà thấy được**
      - Sơ đồ quy trình từ dữ liệu bảng ban đầu -> tính SHAP -> phân nhóm đặc trưng -> sinh đặc trưng nội/liên nhóm -> EXIT filter -> mô hình XGBoost
  - Tận dụng giá trị SHAP (SHapley Additive exPlanations) (Ponce-Bobadilla et al., 2024) để cung cấp tín hiệu nhận biết tác vụ (task-aware signals) phục vụ việc sinh đặc trưng theo nhóm mà không cần mô tả ngữ nghĩa.
  - Các đặc trưng đầu vào được phân thành 3 nhóm dựa trên giá trị SHAP: nhóm hàng đầu (top), nhóm hữu ích (useful), và nhóm yếu (weak), phục vụ sinh đặc trưng nội nhóm (intra-group) và liên nhóm (cross-group).
  - Giới thiệu cơ chế Quỹ đạo Ngầm ẩn Đặc trưng Lộ diện (EXposed-feature Implicit Trajectory - EXIT): khai thác thiên kiến ngữ cảnh mạnh của LLM đối với thông tin đầu vào và tính hiệu quả của các nhiễu loạn prompt nhỏ (minor prompt perturbations) để tăng cường tính đa dạng sinh đặc trưng.
  - EXIT sử dụng tập đặc trưng nhìn thấy được (visible feature set) làm đại diện (proxy) cho lịch sử tối ưu hóa, phản ánh quỹ đạo một cách ngầm ẩn thông qua thành phần đặc trưng thay vì liệt kê tường minh bằng token trong prompt, giúp loại bỏ chi phí mở rộng quỹ đạo.

- **Ba đóng góp chính của bài báo**:
  1. Đề xuất SIGMA: Khung AutoFE dựa trên LLM không cần siêu dữ liệu, thay thế mô tả ngữ nghĩa bằng tín hiệu tầm quan trọng SHAP và đưa ra chiến lược sinh theo nhóm để khám phá đặc trưng có cấu trúc.
  2. Đề xuất EXIT: Cho phép tối ưu hóa chân trời dài (long-horizon optimization) hiệu quả mà không cần đưa quỹ đạo tường minh vào prompt, giảm tỷ lệ sinh đặc trưng trùng lặp từ 37.2% xuống 6.8%.
  3. Đánh giá thực nghiệm toàn diện: SIGMA đạt hiệu năng tương đương với các phương pháp cơ sở dựa trên LLM hiện tại, đồng thời duy trì khả năng cạnh tranh với AutoFE truyền thống nhờ hiệu suất sử dụng đặc trưng cao (efficient feature utilization).
