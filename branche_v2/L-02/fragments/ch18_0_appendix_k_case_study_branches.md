## Appendix K: Case Study

* **Tổng quan về các nghiên cứu tình huống (Case studies overview)**: Trình bày $8$ nghiên cứu tình huống thực nghiệm rút ra từ $2$ tập dữ liệu dạng bảng (tabular datasets) nhằm minh họa cách thức hoạt động và hiệu quả của SymboLLM-FE.
  * **Các tập dữ liệu thực nghiệm được sử dụng**:
    * Tập dữ liệu Spaceship Titanic (*Spaceship Titanic dataset*).
    * Tập dữ liệu CMC (*CMC dataset*).
  * **Mục tiêu phân tích**: Minh họa cơ chế SymboLLM-FE chuyển đổi các biểu thức hồi quy ký hiệu tối nghĩa (*opaque symbolic regression expressions*) thành các đặc trưng có khả năng diễn giải ngữ nghĩa (*semantically interpretable features*).
* **Cấu trúc 4 phần tiêu chuẩn của mỗi nghiên cứu tình huống (Four-part structure)**: Mỗi nghiên cứu tình huống tuân thủ chặt chẽ cấu trúc phân tích gồm $4$ phần định hình:
  * **Công thức hồi quy ký hiệu thô (*Raw symbolic regression formula*)**: Công thức toán học xuất phát cùng thước đo hiệu năng tương ứng (*performance metric*).
  * **Thách thức về khả năng diễn giải (*Interpretability challenge*)**: Vấn đề và sự khó hiểu về mặt ngữ nghĩa do biểu thức công thức đặt ra.
  * **Đặc trưng do LLM tạo ra (*LLM-generated feature*)**: Đặc trưng mới do mô hình ngôn ngữ lớn đề xuất kèm theo lý giải căn cứ (*accompanying rationale*).
  * **Diễn giải ngữ nghĩa bám sát miền tri thức (*Domain-grounded semantic interpretation*)**: Kết quả hiểu biết và góc nhìn ngữ nghĩa thực tiễn thu được từ quá trình tăng cường đặc trưng (*feature augmentation*).
