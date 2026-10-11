## Abstract

- Dữ liệu bảng (tabular data), với tư cách là định dạng dữ liệu cốt lõi trong học máy (machine learning), thường thiếu năng lực phân biệt (discriminative power) cần thiết cho việc xây dựng mô hình hiệu năng cao do mức độ biểu đạt thông tin của đặc trưng (feature informativeness) không đủ.
- Kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE) khắc phục hạn chế này bằng cách tự động hóa quy trình tạo và lựa chọn đặc trưng, đảm bảo đồng thời hiệu năng mô hình và hiệu quả vận hành (operational efficiency).
- Các phương pháp tiếp cận AutoFE hiện tại gặp phải những thách thức cốt lõi:
  - AutoFE truyền thống (traditional AutoFE) thường tạo ra các đặc trưng có khả năng diễn giải kém (poor interpretability) do phụ thuộc vào các phép biến đổi toán học mù (blind mathematical transformations).
  - AutoFE dựa trên mô hình ngôn ngữ lớn (large language models - LLM-based AutoFE) đòi hỏi các vòng lặp đa vòng tốn kém (costly multi-round iterations) để sinh các đặc trưng có mức độ hữu dụng cao (high-utility features) nhằm tăng cường hiệu năng mô hình một cách hiệu quả, kèm theo các rủi ro nội tại về thiên kiến (bias) và ảo giác (hallucination).
- Bài báo đề xuất SymboLLM-FE, phương pháp kết hợp hồi quy ký hiệu (symbolic regression) với LLM cho kỹ thuật đặc trưng (feature engineering) nhằm giải quyết các thách thức trên:
  - Khai phá các công thức toán học giàu tính biểu đạt (mathematically expressive formulas) có tương quan mạnh với mục tiêu (target) thông qua hồi quy ký hiệu để tăng cường hiệu năng mô hình.
  - Tinh chỉnh các công thức này bằng LLM với tri thức tiên nghiệm phong phú (rich prior knowledge) để đảm bảo tính diễn giải (interpretability).
- Kết quả thực nghiệm trên sáu tập dữ liệu thực tế (six real-world datasets) và bốn cuộc thi Kaggle (four Kaggle competitions) chứng minh SymboLLM-FE vượt trội hơn các phương pháp AutoFE hiện có.
- SymboLLM-FE giải quyết đồng thời hai thách thức về khả năng diễn giải kém và số lượng vòng lặp lớn nhờ sử dụng cơ chế tinh chỉnh bằng LLM dựa trên nền tảng tiên nghiệm thống kê (statistical prior-grounded LLM refinement mechanism) và số lần gọi LLM chỉ ở mức một chữ số (single-digit LLM calls).
