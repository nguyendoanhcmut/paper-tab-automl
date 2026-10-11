### 3.1. Conventional-based HPO method

- Phương pháp tối ưu hóa siêu tham số (HPO - hyperparameter optimization) thông thường được thực hiện bằng phương pháp một biến tại một thời điểm (OVAT - one-variable-at-a-time) dựa trên giá trị sai số bình phương trung bình ($MSE$ - mean squared error) thấp nhất:
  - Đối với mô hình mạng nơ-ron truyền thẳng (FFNN - feed-forward neural network), hiệu năng tối ưu đạt được thông qua việc tối ưu hóa $4$ siêu tham số số trị ($numerical\ hyperparameters$) và $2$ siêu tham số phân loại ($categorical\ hyperparameters$):
    - Các siêu tham số số trị gồm: số lượng nơ-ron ($number\ of\ neurons$), tốc độ học ($learning\ rate$), động lượng ($momentum$), và số lượng epoch ($number\ of\ epochs$).
    - Các siêu tham số phân loại gồm: hàm huấn luyện ($training\ function$) và hàm kích hoạt ($activation\ function$) (chi tiết tại Mục 3.1.1).
  - Đối với mô hình mạng nơ-ron hàm cơ sở xuyên tâm (RBFNN - radial basis function neural network), cấu hình tối ưu liên quan đến việc tối ưu hóa $2$ siêu tham số số trị:
    - Bao gồm số lượng nơ-ron ($number\ of\ neurons$) và độ trải rộng ($number\ of\ spreads$) (chi tiết tại Mục 3.1.2).

#### 3.1.1. Conventional-based FFNN training

- Quá trình tối ưu hóa số lượng nơ-ron trong lớp ẩn ($hidden\ layer$) được khảo sát với số nơ-ron biến thiên từ $1$ đến $30$, đòi hỏi $30$ lần chạy ($runs$):
  - Các cột (legend bars) biểu diễn giá trị $MSE$ cho mô hình FFNN-1 và FFNN-2 sử dụng hàm huấn luyện `trainlm`.
  - Các đường liền (solid lines) biểu diễn giá trị $MSE$ cho mô hình FFNN-3 và FFNN-4 sử dụng hàm huấn luyện `traingdm`.
  - Xu hướng tổng quát: biểu đồ cột thể hiện xu hướng giảm theo số lượng nơ-ron, trong khi đường liền thể hiện xu hướng tăng theo số lượng nơ-ron.
  - Giá trị $MSE$ thấp nhất của các mô hình:
    - FFNN-1 đạt $MSE$ thấp nhất là $0.0221$ tại $28$ nơ-ron.
    - FFNN-2 đạt $MSE$ thấp nhất là $0.0225$ tại $29$ nơ-ron.
    - FFNN-3 đạt $MSE$ thấp nhất là $0.0394$ tại $1$ nơ-ron.
    - FFNN-4 cho kết quả dự đoán tốt tại $3$, $7$, $8$, $11$, $13$, và $19$ nơ-ron với các giá trị $MSE$ tương ứng là $0.0352$, $0.0357$, $0.0382$, $0.0366$, $0.0343$, và $0.0317$.
    - Mức $11$ nơ-ron được chọn cho FFNN-4 vì đạt giá trị $MSE$ thấp nhất là $0.0317$.
  - Sự tương tác giữa số lượng nơ-ron và hàm kích hoạt ảnh hưởng đáng kể đến $MSE$ trong quá trình phát triển mô hình FFNN.
- Quá trình tối ưu hóa tốc độ học ($learning\ rate$) và hệ số động lượng ($momentum\ coefficient$) được thực hiện với các giá trị từ $0.1$ đến $1$, yêu cầu $10$ lần chạy cho mỗi siêu tham số:
  - Đối với tốc độ học:
    - Giá trị $MSE$ tạo bởi hàm `traingdm` có xu hướng dao động mạnh giữa $0$ và $1$ khi tốc độ học thay đổi.
    - Giá trị $MSE$ tạo bởi hàm `trainlm` dao động ổn định trong phạm vi hẹp từ $0.022$ đến $0.027$.
    - Các giá trị tốc độ học mang lại kết quả dự đoán thuận lợi lần lượt là $0.8$ (cho FFNN-1), $0.4$ (cho FFNN-2), $0.1$ (cho FFNN-3), và $0.2$ (cho FFNN-4).
  - Đối với hệ số động lượng:
    - FFNN-1 đạt giá trị động lượng tối ưu tại $0.8$ với giá trị $MSE$ là $0.0221$.
    - FFNN-2 thể hiện xu hướng tăng giá trị $MSE$ trên biểu đồ cột theo số lượng động lượng, và $MSE$ thấp nhất đạt được tại $0.4$ ($0.0229$).
    - FFNN-3 và FFNN-4 thể hiện xu hướng tương tự nhau: duy trì tương đối nhất quán ở giai đoạn đầu, nhưng tăng dần về phía cuối dải động lượng.
    - Ở mô hình FFNN-3, các giá trị $MSE$ ban đầu thể hiện sự nhất quán nhẹ, sau đó tăng đột ngột tại các mức động lượng $0.7$, $0.9$, và $1$.
    - Các giá trị động lượng được lựa chọn là $0.5$ cho FFNN-3 và $0.6$ cho FFNN-4, đem lại các giá trị $MSE$ tương ứng là $0.0314$ và $0.0261$.
- Quá trình xác định số lượng epoch tối ưu ($optimal\ number\ of\ epochs$) cho các mô hình FFNN:
  - Giá trị $MSE$ cho FFNN-1 và FFNN-2 dao động ngẫu nhiên trong phạm vi $0.022$–$0.0227$.
  - Đối với FFNN-1, các giá trị epoch $300$ và $600$ đều có tiềm năng đem lại kết quả tốt với $MSE$ thấp hơn; giá trị epoch $300$ được chọn vì mang lại $MSE$ thấp nhất là $0.0223$.
  - FFNN-2 đạt giá trị $MSE$ thấp nhất là $0.0221$ tại $100$ epochs.
  - Đối với FFNN-3, tham số chu kỳ huấn luyện (nguồn ghi momentum) đạt giá trị tối ưu tại $700$ với giá trị $MSE$ là $0.0265$.
  - Đối với FFNN-4, giá trị $MSE$ từ $100$ đến $200$ epochs đầu tiên giảm đột ngột từ $0.0525$ xuống $0.0325$, sau đó ổn định quanh mức $0.0325$ cho đến cuối; FFNN-4 đạt kết quả tối ưu tại $600$ epochs với giá trị $MSE$ nhỏ nhất là $0.0314$.
- Đánh giá tổng quan về các siêu tham số FFNN được hiển thị chi tiết trong Hình 4:
  * **Hình 4.** <img src="assets/fig_04_p11.jpeg" alt="Hình 4" />
    * **(a) Số lượng nơ-ron (number of neurons):** Biến thiên từ $1$ đến $30$ ($30$ lần chạy). Cột biểu diễn $MSE$ của FFNN-1 và FFNN-2 (dùng hàm trainlm), đường liền biểu diễn $MSE$ của FFNN-3 và FFNN-4 (dùng hàm traingdm). Cột có xu hướng giảm, đường liền có xu hướng tăng. $MSE$ thấp nhất của FFNN-1, FFNN-2, FFNN-3 lần lượt tại $28$ ($0.0221$), $29$ ($0.0225$), và $1$ ($0.0394$). Với FFNN-4, chọn $11$ nơ-ron do đạt $MSE$ thấp nhất ($0.0317$).
    * **(b) Tốc độ học (learning rate):** Biến thiên từ $0.1$ đến $1$ ($10$ lần chạy). $MSE$ của traingdm dao động giữa $0$ và $1$, trong khi trainlm dao động trong khoảng $0.022$–$0.027$. Giá trị tối ưu cho FFNN-1, FFNN-2, FFNN-3, FFNN-4 lần lượt là $0.8$, $0.4$, $0.1$, $0.2$.
    * **(c) Động lượng (momentum):** Biến thiên từ $0.1$ đến $1$ ($10$ lần chạy). Giá trị tối ưu: FFNN-1 là $0.8$ ($MSE$ $0.0221$), FFNN-2 là $0.4$ ($MSE$ $0.0229$), FFNN-3 là $0.5$ ($MSE$ $0.0314$), FFNN-4 là $0.6$ ($MSE$ $0.0261$).
    * **(d) Số chu kỳ huấn luyện (epochs):** FFNN-1 và FFNN-2 dao động ngẫu nhiên trong khoảng $0.022$–$0.0227$. FFNN-1 chọn $300$ epochs ($MSE$ $0.0223$). FFNN-2 chọn $100$ epochs ($MSE$ $0.0221$). FFNN-3 tối ưu tại $700$ epochs ($MSE$ $0.0265$). FFNN-4 giảm đột ngột từ $100$–$200$ epochs (từ $0.0525$ xuống $0.0325$), ổn định và đạt tối ưu tại $600$ epochs ($MSE$ $0.0314$).
- Tóm lại, các giá trị $MSE$ thấp nhất đạt được bởi mô hình FFNN khi sử dụng hàm huấn luyện `trainlm` so với `traingdm`:
  - Điều này bắt nguồn từ các ưu điểm của thuật toán Levenberg–Marquardt, bao gồm quá trình huấn luyện nhanh chóng và hiệu quả cao trong khớp hàm (hồi quy phi tuyến - nonlinear regression), dẫn đến giá trị $MSE$ thấp hơn (Ibrahim & Wahab $2022$).

#### 3.1.2. Conventional-based RBFNN training

- Quá trình tối ưu hóa số lượng nơ-ron và độ trải rộng ($number\ of\ spreads$) trong huấn luyện mô hình RBFNN:
  - Tương tự như FFNN, số lượng nơ-ron biến thiên từ $1$ đến $30$, đòi hỏi $30$ lần chạy ($runs$).
  - Số lượng độ trải rộng biến thiên từ $0.5$ đến $3$ với gia số $0.5$, đòi hỏi $6$ lần chạy.
  - Đối với số lượng nơ-ron: các giá trị $MSE$ giảm đột ngột và sau đó hơi ổn định ở các giá trị cực tiểu bắt đầu từ $8$ cho đến $30$ nơ-ron, với $MSE$ dao động tương ứng trong khoảng từ $0.0315$ đến $0.0251$.
  - Đối với độ trải rộng: $MSE$ thể hiện xu hướng tăng theo số lượng spread, sau đó giảm nhẹ sau khi số lượng spread được đặt bằng $2$.
  - Giá trị $MSE$ thấp nhất thu được:
    - Đối với số lượng nơ-ron: đạt thấp nhất tại $30$ nơ-ron với $MSE = 0.0251$.
    - Đối với độ trải rộng: đạt thấp nhất tại giá trị spread là $0.5$ với $MSE = 0.0235$.
- Kết quả huấn luyện và ảnh hưởng của các siêu tham số RBFNN được thể hiện trong Hình 5:
  * **Hình 5.** <img src="assets/fig_05_p12.jpeg" alt="Hình 5" />
    * **(a) Số lượng nơ-ron trong RBFNN (number of neurons):** Biến thiên từ $1$ đến $30$ ($30$ lần chạy). Giá trị $MSE$ giảm đột ngột rồi hơi ổn định ở các giá trị tối thiểu từ $8$ đến $30$ nơ-ron ($MSE$ từ $0.0315$ đến $0.0251$). Giá trị $MSE$ thấp nhất đạt tại $30$ nơ-ron ($0.0251$).
    * **(b) Độ trải rộng (number of spreads):** Biến thiên từ $0.5$ đến $3$ với bước tăng $0.5$ ($6$ lần chạy). $MSE$ có xu hướng tăng theo số lượng spread, sau đó giảm nhẹ sau khi spread được đặt bằng $2$. Giá trị $MSE$ thấp nhất thu được tại spread $= 0.5$ ($0.0235$).
