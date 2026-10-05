### 2.4 Model evaluation

- Hệ thống chỉ tiêu định lượng đánh giá hiệu năng mô hình trên tập kiểm tra.
  - Ma trận nhầm lẫn (confusion matrix) gồm lưới $5 \times 5$ tính cả lớp nền (background class) để trực quan hóa tương quan giữa giá trị thực tế và giá trị dự đoán.
  - Độ chính xác (Precision) đo lường tỷ lệ các dự đoán mẫu dương tính là chính xác.
  - Độ thu hồi (Recall) phản ánh tỷ lệ phát hiện thành công các mẫu dương tính từ tập dữ liệu thực tế.
  - Điểm $F1\text{-score}$ dao động trong khoảng từ $0$ đến $1$, là trung bình điều hòa dung hòa giữa Precision và Recall.
  - Quy trình đánh giá được hiện thực hóa bằng thư viện scikit-learn trong môi trường Python 3.10.12.
- Hàm mất mát phân loại Cross Entropy Loss (CE Loss) định lượng sai lệch phân phối xác suất.
  - Công thức tính hàm mất mát phân loại đa lớp:
    $$\text{CE Loss} = -\sum_{i=1}^{C} y_i \log(p_i)$$
  - Trong đó $C$ là tổng số lượng phân lớp đối tượng.
  - Ký hiệu $p_i$ là xác suất dự đoán của mô hình cho lớp thứ $i$.
  - Biến nhị phân $y_i = 1$ nếu nhãn thực tế thuộc về lớp $i$, và $y_i = 0$ cho các trường hợp còn lại.
  - Khi xác suất dự đoán tiệm cận $1$, giá trị mất mát tiệm cận $0$; khi xác suất tiệm cận $0$, hàm mất mát tăng vọt.
- Hàm mất mát vị trí Mean Squared Error (MSE) hiệu chỉnh sai lệch tọa độ khung bao.
  - Sai lệch giữa tọa độ tâm $(x, y)$ cùng kích thước $(w, h)$ của khung bao dự đoán và thực tế được tối thiểu hóa qua phương trình:
    $$\text{MSE} = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2$$
  - Trong đó $N$ là tổng số mẫu khung bao cần đánh giá.
  - Đại lượng $y_i$ biểu thị giá trị nhãn thực tế của mẫu thứ $i$.
  - Đại lượng $\hat{y}_i$ biểu thị giá trị tọa độ hoặc kích thước dự đoán tương ứng từ mô hình.
