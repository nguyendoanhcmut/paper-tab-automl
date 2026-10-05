## 6 Conclusion

* SymboLLM-FE là một khung làm việc lai (hybrid framework) mạnh mẽ kết hợp tính chặt chẽ toán học của hồi quy ký hiệu (symbolic regression) với khả năng tinh chỉnh của các mô hình ngôn ngữ lớn (Large Language Models - LLMs) cho kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE).
  * Khung làm việc thể hiện các ưu thế nhất quán so với các phương pháp AutoFE hiện nay về hiệu năng, nâng cao khả năng diễn giải (interpretability) và đạt hiệu quả tính toán (efficiency) vượt trội hơn.
* Nghiên cứu đề xuất một giải pháp đáng tin cậy cho các tác vụ thực tế bằng cách tích hợp SymboLLM-FE làm mô-đun kỹ thuật đặc trưng (feature engineering module) với TabPFN.
  * Hiệu quả của phương pháp tiếp cận kết hợp này đã được chứng minh thực nghiệm trên các cuộc thi Kaggle.
* Các hướng nghiên cứu trong tương lai có thể khảo sát việc tích hợp các phương pháp AutoFE truyền thống với phân tích tập dữ liệu quy mô lớn nhằm suy dẫn có hệ thống các cơ chế sinh đặc trưng (feature generation mechanisms).
  * Các mẫu hình (patterns) và quy tắc (rules) được trích xuất có thể được hình thức hóa thành các nguyên lý kỹ thuật đặc trưng có cấu trúc (structured feature engineering principles).
  * Những nguyên lý có cấu trúc này sau đó có thể được sử dụng để tinh chỉnh (fine-tune) các mô hình LLM.
