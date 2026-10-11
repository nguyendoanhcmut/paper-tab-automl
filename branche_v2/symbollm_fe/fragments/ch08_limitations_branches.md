## Limitations

- SymboLLM-FE tồn tại hai hạn chế chính (main limitations):
  - **Gánh nặng chi phí thời gian trên tập dữ liệu số chiều cao**: Mặc dù đã áp dụng hai cơ chế chiến lược nhằm bảo đảm khả năng mở rộng (scalability) của SymboLLM-FE đối với các tập dữ liệu số chiều cao (high-dimensional datasets), phương pháp vẫn phải gánh chịu chi phí thời gian quá mức (prohibitive time overhead), làm giới hạn tính khả thi trong các kịch bản bị hạn chế tài nguyên (resource-constrained) hoặc đòi hỏi xử lý theo thời gian thực (real-time scenarios).
  - **Hạn chế trong việc nắm bắt hiệu ứng hiệp đồng giữa các biến không liền kề**: Chiến lược xây dựng tập con đặc trưng (subset construction strategy) sắp xếp các đặc trưng theo thứ tự độ quan trọng giảm dần và áp dụng một cửa sổ trượt liên tục (continuous sliding window), có thể không nắm bắt được các hiệu ứng hiệp đồng (synergistic effects) giữa các biến không nằm kế tiếp nhau (non-adjacent variables).
    - Cụ thể, khi hai hoặc nhiều đặc trưng có tương quan ngầm (implicitly correlated) nhưng không được định vị liên tiếp trong bảng xếp hạng đã sắp xếp, đóng góp dự đoán kết hợp (joint predictive contribution) của chúng đối diện với rủi ro bị bỏ sót.

### Acknowledgements

- Công trình nghiên cứu được hỗ trợ bởi:
  - Chương trình Trọng điểm của Quỹ Khoa học Giang Tô (Key Program of Jiangsu Science Foundation, mã số $BK20243012$).
  - Quỹ Khoa học Tự nhiên Quốc gia Trung Quốc (National Science Foundation of China, mã số $62306133$).
  - Dự án "111 Center" (No. $B26023$).
- Nhóm tác giả chân thành cảm ơn các phản biện vì những nhận xét mang tính xây dựng và các đề xuất sâu sắc.
