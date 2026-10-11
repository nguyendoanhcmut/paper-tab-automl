## Abstract

- Hyperparameter tuning (tinh chỉnh siêu tham số) là quy trình quan trọng để tối đa hóa performance (hiệu năng) của bất kỳ mô hình neural network (mạng nơ-ron) nào.
- Nghiên cứu đề xuất factorial design of experiment (thiết kế thí nghiệm thừa số) để screening (sàng lọc) và response surface methodology (phương pháp bề mặt đáp ứng) để tối ưu hóa hyperparameter của $2$ thuật toán artificial neural network (mạng nơ-ron nhân tạo):
  - Feed-forward neural network (FFNN, mạng nơ-ron truyền thẳng) và radial basis function neural network (RBFNN, mạng nơ-ron hàm cơ sở xuyên tâm) được áp dụng để dự đoán permeate flux (thông lượng thấm) của palm oil mill effluent (nước thải nhà máy dầu cọ).
  - Permeate pump (bơm thấm) và transmembrane pressure (áp suất xuyên màng) của hệ thống submerged membrane bioreactor (SMBR, bể phản ứng sinh học màng ngập) là các input variables (biến đầu vào).
- $6$ hyperparameter của mô hình FFNN được đưa vào tối ưu hóa hyperparameter:
  - Bao gồm $4$ numerical factors (yếu tố số trị): neuron numbers (số lượng nơ-ron), learning rate (tốc độ học), momentum (động lượng), và epoch numbers (số chu kỳ huấn luyện).
  - Bao gồm $2$ categorical factors (yếu tố phân loại): training function (hàm huấn luyện) và activation function (hàm kích hoạt).
- RBFNN bao gồm $2$ numerical factors (yếu tố số trị): number of neurons (số lượng nơ-ron) và spreads (độ trải rộng).
- Phương pháp thông thường (conventional method: one-variable-at-a-time / một biến tại một thời điểm) được đem ra so sánh về optimization processing time (thời gian xử lý tối ưu hóa) và accuracy (độ chính xác) của mô hình.
- Các hyperparameter tối ưu thu được từ phương pháp đề xuất mang lại accuracy (độ chính xác) tốt với generalization error (sai số khái quát hóa) nhỏ hơn:
  - Simulation results (kết quả mô phỏng) cho thấy training performance (hiệu năng huấn luyện) cải thiện hơn $65\%$, giảm repetition (số lần lặp) và processing time (thời gian xử lý).
  - Phương pháp luận đề xuất có thể được ứng dụng cho bất kỳ loại neural network nào để tìm mức tối ưu của các thông số khác nhau.
- Key words (Từ khóa): computational time (thời gian tính toán), DoE implementation (triển khai DoE), neural network (mạng nơ-ron), optimization techniques (các kỹ thuật tối ưu hóa), submerged membrane bioreactor data (dữ liệu bể phản ứng sinh học màng ngập).

### Highlights

- Membrane fouling (nghẹt màng) trong filtration (quá trình lọc) là một quá trình phức tạp, và việc hiểu rõ dynamic behavior (hành vi động học) là rất quan trọng.
- Nghiên cứu tập trung vào mô hình động học dựa trên artificial neural network (ANN) và tối ưu hóa cho quá trình lọc submerged membrane bioreactor (SMBR).
- Cấu trúc ANN có khả năng mô hình hóa dynamic behavior (hành vi động học) của quá trình lọc trong các điều kiện bình thường.
- Phương pháp tối ưu hóa giúp cải thiện cấu trúc ANN cho việc phát triển mô hình lọc SMBR.
