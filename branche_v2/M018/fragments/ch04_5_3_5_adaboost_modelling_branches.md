### 3.5. Adaboost modelling

* Mô hình Adaboost (Adaptive Boosting) có thể được sử dụng để dự đoán nồng độ COD dòng ra (effluent COD) ở các mức độ mặn khác nhau (Fig. 8):
    ![Fig. 8. Adaboost modelling of effluent COD concentration: (a) training performance, (b) test performance, (c) total performance.](assets/fig_08_p9.jpeg)
    * **(a) Hiệu suất tập huấn luyện (Training):** Tương quan giữa COD mô phỏng và đo đạc đạt $R^2 = 0{,}9051$, $\text{RMSE} = 9{,}88\text{ mg/L}$ trong dải nồng độ COD khoảng $100\text{--}300\text{ mg/L}$.
    * **(b) Hiệu suất tập kiểm tra (Test):** Đạt $R^2 = 0{,}8027$, $\text{RMSE} = 14{,}84\text{ mg/L}$ (văn bản bài báo ghi nhầm thành số liệu của tập train: $R^2 = 0{,}9051$, $\text{RMSE} = 9{,}88\text{ mg/L}$).
    * **(c) Hiệu suất tổng thể (Total):** Toàn bộ dữ liệu đạt $R^2 = 0{,}8797$, $\text{RMSE} = 16{,}45\text{ mg/L}$; các điểm dự báo bám sát đường hồi quy tuyến tính lý tưởng.
* Phân chia tập dữ liệu và tối ưu hóa tham số mô hình:
    * Các giá trị tối ưu của các thông số then chốt được tối ưu hóa trên tập huấn luyện (training set, chiếm $70\%$) sử dụng hàm mục tiêu sai số toàn phương trung bình ($RMSE$).
    * Mô hình đã qua huấn luyện được áp dụng mô phỏng hồi quy trên tập kiểm tra (test set, chiếm $30\%$) để phân tích COD dòng ra.
* Hiệu suất dự đoán trên tập kiểm tra (test set):
    * Hệ số xác định $R^2$ trên tập kiểm tra đạt $0{,}9051$ (hình ghi $0{,}8027$).
    * Sai số toàn phương trung bình $RMSE$ trên tập kiểm tra là $9{,}88\text{ mg/L}$ (hình ghi $14{,}84\text{ mg/L}$).
* Đánh giá độ chính xác tổng thể của mô hình Adaboost:
    * Ngoại trừ một vài giá trị ngoại lệ (outliers), các giá trị dự đoán của mô hình Adaboost khớp tốt với các giá trị đo đạc thực nghiệm.
    * Sai số tuyệt đối trung bình (average absolute error) chỉ ở mức $3{,}07\%$.
    * Hệ số xác định tổng thể $R^2$ đạt $0{,}8797$.
* Giới hạn và định hướng mở rộng mô hình:
    * Do giới hạn trong thiết kế thí nghiệm, mô hình có thể không ngoại suy tốt vượt ra ngoài một số thiết lập thực nghiệm nhất định.
    * Việc mở rộng kích thước tập dữ liệu từ các kịch bản AnMBR độ mặn cao đa dạng trong tương lai được kỳ vọng sẽ nâng cao độ chính xác dự đoán COD dòng ra của mô hình Adaboost.
