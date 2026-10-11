## 1 Introduction

- **Đặc trưng và vai trò của dữ liệu bảng (Tabular data) trong các ứng dụng thực tế** (Altman and Krzywinski, 2017):
  - Dữ liệu bảng là định dạng dữ liệu có cấu trúc cao (highly structured data format), tổ chức thông tin thành các hàng và cột, trong đó mỗi hàng biểu diễn một mẫu hoặc cá thể độc lập (independent sample/instance), và mỗi cột tương ứng với một đặc trưng hoặc thuộc tính cụ thể (specific feature/attribute) (Sahakyan et al., 2021).
  - Dữ liệu bảng được ứng dụng sâu rộng trong các bài toán thực tế:
    - Lĩnh vực tài chính: chấm điểm tín dụng (credit scoring) (West, 2000) và dự đoán thị trường chứng khoán (stock market prediction) (Zhu et al., 2021).
    - Lĩnh vực y tế: chẩn đoán bệnh tật (disease diagnosis) (Yıldız and Kalayci, 2024) và phát triển dược phẩm (drug development) (Meijerink et al., 2020).
  - *Hạn chế nội tại*: Trong ứng dụng thực tế, dữ liệu bảng thường chịu tình trạng thiếu hụt lượng thông tin trong đặc trưng (insufficient feature informativeness) và tồn tại các tương tác bậc cao ngầm ẩn (implicit high-order interactions).
  - Các hạn chế cố hữu này tạo ra rào cản ngăn các mô hình nắm bắt hiệu quả cấu trúc dữ liệu tiềm ẩn, dẫn đến hiệu năng dự đoán dưới mức tối ưu (suboptimal predictive performance) (Sayed et al., 2025; Cheng et al., 2025b; Gorishniy et al., 2021).

- **Sự cần thiết của Kỹ thuật Đặc trưng Tự động (Automated Feature Engineering - AutoFE)**:
  - Trước khi thực hiện dự đoán, kỹ thuật đặc trưng (feature engineering) thường được áp dụng nhằm tăng cường mối quan hệ giữa các đặc trưng đầu vào và nhãn mục tiêu thông qua các thao tác sinh đặc trưng (feature generation) và lựa chọn đặc trưng (feature selection) (Ravishankar and Battineni, 2025).
  - Dữ liệu bảng sau xử lý được đưa vào các mô hình xuôi dòng (downstream models) để cải thiện độ chính xác dự đoán.
  - Trước đây, kỹ thuật đặc trưng phụ thuộc nặng nề vào việc xây dựng thủ công các đặc trưng chất lượng cao—quy trình đòi hỏi nhiều vòng lặp thử nghiệm tốn kém công sức và gia tăng đáng kể chi phí nhân lực (labour costs) (Susan and Tuteja, 2025).
  - AutoFE ra đời như một trọng tâm nghiên cứu cốt lõi nhằm tự động hóa và thuật toán hóa việc khám phá, xây dựng các đặc trưng hiệu quả để giảm thiểu công sức thủ công và nâng cao hiệu năng mô hình học máy (Khurana et al., 2016).

- **Cơ chế hoạt động và hạn chế về khả năng diễn giải của AutoFE truyền thống (Traditional AutoFE)**:
  - Các phương pháp AutoFE truyền thống tiêu biểu gồm: tối ưu hóa lai kết hợp tìm kiếm chùm (hybrid optimization with beam search) (Horn et al., 2019), cắt tỉa động (dynamic pruning) (Zhang et al., 2023b), và lựa chọn đặc trưng (feature selection) (Li et al., 2017; Cheng et al., 2025a).
  - Cơ chế tạo đặc trưng chủ yếu dựa vào các quy tắc biến đổi định sẵn (predefined transformation rules), tìm kiếm vét cạn (exhaustive search), hoặc các chiến lược tối ưu hóa (optimization-based strategies) để sinh các đặc trưng ứng viên (candidate features).
  - *Hạn chế về tính diễn giải (Poor interpretability)*: Dù cải thiện được hiệu năng mô hình, các đặc trưng sinh ra bởi AutoFE truyền thống thường là các tổ hợp toán học phức tạp hoàn toàn thiếu vắng ý nghĩa ngữ nghĩa tường minh (devoid of explicit semantic meaning), dẫn đến sự tách rời khỏi logic miền tri thức mà con người có thể hiểu được (human-understandable domain-specific logic).
  - *Hậu quả trong các lĩnh vực nhạy cảm*: Trong các kịch bản như khai phá nhân tố (factor mining) (Wang et al., 2025, 2026), khả năng diễn giải là yêu cầu bắt buộc để kiểm chứng cơ sở kinh tế (economic rationale) đằng sau các tín hiệu, đảm bảo tuân thủ pháp lý (regulatory compliance), và hỗ trợ chẩn đoán sai số hiệu quả. Nếu thiếu logic lập luận rõ ràng, mô hình rất khó phân biệt giữa quy luật dự đoán vững chắc và tương quan giả tạo (spurious correlations), làm suy giảm niềm tin vào các quyết định dự đoán.

- **So sánh các cơ chế sinh đặc trưng và mô hình diễn giải giữa ba thế hệ AutoFE**:
  - AutoFE truyền thống dựa trên các chồng toán tử mù (blind operator stacks), mang lại hiệu năng cao nhưng khả năng diễn giải kém; AutoFE dựa trên LLM mang lại sự rõ ràng về ngữ nghĩa nhưng dễ bất ổn về hiệu năng; SymboLLM-FE kết hợp hồi quy ký hiệu với LLM để đạt đồng thời độ chính xác dự đoán cao và tính minh bạch có thể diễn giải bởi con người.
  - **Hình 1.** Phân tích so sánh cơ chế sinh đặc trưng và mô hình diễn giải giữa các phương pháp AutoFE (Traditional AutoFE, LLM-based AutoFE, và SymboLLM-FE)
    - <img src="assets/fig_01_p2.jpeg" alt="Hình 1" />
    - **Hình này chứng minh điều gì**
      - AutoFE truyền thống đạt điểm mô hình cao nhưng thiếu tính diễn giải; LLM-based AutoFE có tính diễn giải cao nhưng hiệu năng suy giảm; SymboLLM-FE đạt đồng thời điểm mô hình vượt trội và tính minh bạch dễ diễn giải
    - **Từ đâu mà thấy được**
      - Traditional AutoFE xếp chồng toán tử mù (Blind Operator Stack) sinh công thức thuần toán ($x_1^2 + 2x_1 x_2 + x_2^2$, $\min(x_1, x_2)$, $\frac{\ln x_1}{\sqrt{x_2}}$), Model Score tăng ($\uparrow$) nhưng Interpretability bị đánh dấu chéo đỏ ($\times$)
      - LLM-based AutoFE dùng LLM sinh đặc trưng dạng luật logic ngữ nghĩa (`Risk_Indicator`), Interpretability đạt tích xanh ($\checkmark$) nhưng Model Score giảm ($\downarrow$)
      - SymboLLM-FE phối hợp Hồi quy ký hiệu + LLM sinh đặc trưng gán trọng số ngữ nghĩa (`Infection_Exposure_Risk`), cả Model Score lẫn Interpretability đều đạt ($\uparrow$, $\checkmark$)

- **Tiềm năng và hai thách thức then chốt của AutoFE dựa trên Mô hình Ngôn ngữ Lớn (LLM-based AutoFE)**:
  - *Tiềm năng*: Sự phát triển của các mô hình ngôn ngữ lớn (LLMs) mang lại cơ hội mới nhờ năng lực hiểu ngữ nghĩa (semantic understanding) (Hollmann et al., 2023b), suy luận logic (logical reasoning) (Zou et al., 2026), và định hướng tri thức (knowledge guidance) (Nam et al., 2024).
  - LLM-based AutoFE tận dụng tri thức tiên nghiệm phong phú (rich prior knowledge) và khả năng hiểu ngữ cảnh để tự động phát hiện mối quan hệ tiềm năng giữa các đặc trưng trong dữ liệu bảng thô, xây dựng đặc trưng mới giàu tính diễn giải qua các phép toán và quy tắc logic thay vì tìm kiếm vét cạn.
  - *Thách thức 1 (Chi phí tính toán và lặp lại khổng lồ)*: Quá trình sinh đặc trưng nâng cao hiệu năng đòi hỏi tương tác lặp lại nhiều vòng với mô hình xuôi dòng để xác thực và tinh chỉnh, gây ra chi phí tính toán nghiêm trọng (prohibitive computational overhead) và hạn chế khả năng mở rộng (limited scalability) (Abhyankar et al., 2025).
  - *Thách thức 2 (Ảo giác và thiên kiến ngầm ẩn)*: Sự nhạy cảm cố hữu của LLM đối với ảo giác (hallucinations) và thiên kiến ngầm ẩn (implicit biases) dễ dẫn đến việc sinh các đặc trưng không hợp lệ về mặt ngữ nghĩa (semantically invalid) hoặc thiếu công bằng (unfair features), làm tổn hại nặng nề độ tin cậy và tính toàn vẹn dự đoán của mô hình xuôi dòng (Cheng et al., 2026; Han et al., 2024).

- **Khung làm việc đề xuất SymboLLM-FE**:
  - SymboLLM-FE kết hợp hồi quy ký hiệu (symbolic regression) và LLM để sinh các đặc trưng vừa có cơ sở toán học vừa có thể diễn giải, giúp tối ưu hóa hiệu năng mô hình.
  - Vận hành thông qua đường ống phối hợp hai giai đoạn (two-stage collaborative pipeline):
    - *Giai đoạn 1 - Xây dựng công thức bằng hồi quy ký hiệu*: Áp dụng chiến lược cửa sổ mở rộng - trượt (expanding-sliding window strategy) dựa trên phân tích tương quan Spearman (Spearman correlation analysis) để giảm không gian tìm kiếm từ cấp số mũ $\mathcal{O}(2^n)$ xuống đa thức $\mathcal{O}(n^2)$, cho phép hồi quy ký hiệu sinh ra các công thức ứng viên rõ ràng, có cơ sở toán học vững chắc.
    - *Giai đoạn 2 - Tinh chỉnh đặc trưng bằng LLM*: Tận dụng LLM để đưa các tiên nghiệm miền cụ thể (domain-specific priors) vào các công thức toán học chưa rõ nghĩa ngữ nghĩa, biến đổi chúng thành mã thực thi có ý nghĩa ngữ nghĩa thông qua suy luận chuỗi tư duy (chain-of-thought reasoning).
  - Vòng lặp tinh chỉnh vừa xác thực giá trị sử dụng của đặc trưng thông qua hiệu năng bộ dự đoán xuôi dòng, vừa đảm bảo sự tương thích với logic nghiệp vụ, đạt được sự cân bằng vững chắc giữa hiệu năng cao và tính minh bạch dễ diễn giải đối với con người.

- **Hiệu quả tính toán và chi phí API vượt trội của SymboLLM-FE so với các phương pháp AutoFE (Bảng 1)**:
  - Bảng 1 so sánh hiệu năng dự đoán, số lượng đặc trưng sinh ra, và số lượt gọi API giữa các phương pháp AutoFE truyền thống và AutoFE dựa trên LLM:

| Phương pháp AutoFE | Số đặc trưng sinh ra (Generated Features) | Điểm số mô hình (Score) | Số lượt gọi API (API Call) |
| :--- | :---: | :---: | :---: |
| AutoFeat | 2 | 79.75 | − |
| OpenFE | 1436 | 79.53 | − |
| CAAFE | 30 | 79.94 | 10 |
| OcTree | 50 | 79.52 | 50 |
| FEBP | 200 | 79.36 | 29 |
| LLM-FE | 30 | 79.59 | 35 |
| LLM-RANK | − | 78.86 | 7 |
| **SymboLLM-FE** | **70** | **80.02** | **4** |

  - *Ghi chú Table 1*: AutoFeat và OpenFE là các phương pháp AutoFE truyền thống không sử dụng LLM. LLM-RANK không sinh đặc trưng vì đóng vai trò bộ chọn lọc đặc trưng (feature selector).
  - SymboLLM-FE đạt điểm số cao nhất ($80.02$) trong khi chỉ tiêu tốn số lượt gọi LLM API ở mức một chữ số ($4$ lượt gọi), giảm đáng kể chi phí tính toán so với các phương pháp LLM-based AutoFE khác (OcTree cần $50$ cuộc gọi, LLM-FE cần $35$, FEBP cần $29$, CAAFE cần $10$).

- **Bốn đóng góp chính của bài báo**:
  - *Đóng góp 1 - Phân tích thực nghiệm toàn diện*: Chỉ ra rằng AutoFE truyền thống bị hạn chế bởi tính diễn giải kém, trong khi AutoFE dựa trên LLM đối mặt với thử nghiệm lặp tốn kém, ảo giác (hallucination) và thiên kiến ngầm ẩn (implicit bias).
  - *Đóng góp 2 - Đề xuất khung SymboLLM-FE*: Giải quyết các thách thức của AutoFE hiện nay bằng cách kết hợp hồi quy ký hiệu để khai phá đặc trưng tăng cường hiệu năng, sau đó tinh chỉnh qua LLM để nâng cao tính diễn giải ngữ nghĩa.
  - *Đóng góp 3 - Đánh giá thực nghiệm quy mô lớn*: Thực nghiệm trên sáu bộ dữ liệu thực tế và bốn cuộc thi Kaggle chứng minh hiệu năng vượt trội và khả năng khái quát hóa (generalizability) của SymboLLM-FE so với các phương pháp AutoFE hiện tại.
  - *Đóng góp 4 - Cơ chế tinh chỉnh tinh gọn với số lượt gọi LLM tối thiểu*: Giải quyết đồng thời thách thức kép về tính diễn giải kém và chi phí lặp thử nghiệm khổng lồ bằng cơ chế tinh chỉnh LLM dựa trên nền tảng tiên nghiệm thống kê (statistical prior-grounded LLM refinement mechanism) chỉ với số lượt gọi LLM ở mức một chữ số (single-digit LLM calls, $4$ lượt gọi).
