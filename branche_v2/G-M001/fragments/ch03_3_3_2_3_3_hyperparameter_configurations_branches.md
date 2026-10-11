#### 2.3.3. Hyperparameter configurations

- Tối ưu hóa siêu tham số (hyperparameter optimization) đóng vai trò quyết định để đạt được hiệu suất cao trong mô hình mạng nơ-ron nhân tạo (ANN - artificial neural network):
  - Việc lựa chọn cẩn thận các dải giá trị phù hợp (appropriate ranges) cho các siêu tham số là điều thiết yếu.
  - Đối với cấu trúc mô hình mạng nơ-ron truyền thẳng (FFNN - feedforward neural network), quá trình huấn luyện liên quan đến nhiều siêu tham số dạng số (numerical hyperparameters):
    - Số lượng nơ-ron ($number\ of\ neurons$)
    - Tốc độ học ($learning\ rate$)
    - Số lượng epoch ($number\ of\ epochs$)
    - Hệ số động lượng ($momentum\ coefficient$)
  - Các yếu tố phân loại (categorical factors) như hàm huấn luyện ($training\ function$) và hàm kích hoạt ($activation\ function$) được xem xét để nâng cao hiệu suất dự đoán của mô hình ($model\ prediction\ performance$).

- Hàm kích hoạt ($activation\ function$, đôi khi được gọi là hàm truyền - $transfer\ function$) xác định cách thức tổng có trọng số của các đầu vào ($weighted\ sum\ of\ inputs$) được chuyển đổi thành đầu ra từ các nút trong một lớp của mạng:
  - Sự lựa chọn hàm kích hoạt ở lớp ẩn ($hidden\ layer$) và lớp đầu ra ($output\ layer$) ảnh hưởng đáng kể đến khả năng học của mạng từ tập dữ liệu huấn luyện ($training\ dataset$).
  - Lớp ẩn thường sử dụng các hàm phi tuyến tính ($nonlinear\ functions$), trong khi lớp đầu ra sử dụng hàm truyền tuyến tính `purelin` ($linear\ transfer\ function$).
  - Các hàm kích hoạt thường dùng trong lớp ẩn bao gồm sigmoid (hoặc logistic) và hyperbolic tangent ($\mathrm{Tanh}$) (Rasamoelina et al. $2020$).
  - Đơn vị tuyến tính chỉnh lưu ($\mathrm{ReLU}$ - rectified linear unit) gần đây trở nên phổ biến đối với các học viên và nhà nghiên cứu học sâu (deep learning researchers) nhờ tính đơn giản và hiệu suất huấn luyện vượt trội so với các hàm kích hoạt thông thường (Rasamoelina et al. $2020$).

- Các hàm huấn luyện ($training\ functions$) được sử dụng trong trường hợp này bao gồm Levenberg–Marquardt (`lm`) và gradient descent with momentum (`gdm`):
  - Hàm huấn luyện `lm` cung cấp các tính năng nổi bật:
    - Huấn luyện nhanh (fast training).
    - Hồi quy phi tuyến với sai số bình phương trung bình thấp ($MSE$ - mean squared error).
    - Các tính năng giảm thiểu dung lượng bộ nhớ (memory reduction features) (Keong et al. $2016$; Johnson Santhosh et al. $2021$).
  - Hàm huấn luyện `gdm` sở hữu các ưu điểm:
    - Tránh các điểm cực tiểu cục bộ (avoiding local minima).
    - Tăng tốc quá trình học (accelerating learning).
    - Ổn định sự hội tụ (stabilizing convergence) (Winiczenko et al. $2016$).
  - Hàm huấn luyện `gdm` phụ thuộc chủ yếu vào hai tham số: tốc độ học ($learning\ rate$) và tham số động lượng ($momentum\ parameters$).
  - Tác động của các loại hàm kích hoạt và hàm truyền khác nhau lên hiệu suất mạng của mô hình lọc SMBR cho POME (submerged membrane bioreactor filtration for palm oil mill effluent) cần phải được xác định rõ.

- Số lượng epoch ($number\ of\ epochs$) hoặc chu kỳ huấn luyện ($training\ cycles$) mang tính quyết định trong việc định hình mô hình mạng:
  - Quá ít epoch sẽ giới hạn khả năng của mạng (limit the network's ability).
  - Quá nhiều epoch có thể dẫn đến hiện tượng quá khớp ($overfitting$) và tăng sai số ($increased\ error$) (Winiczenko et al. $2016$).
  - Khi huấn luyện mô hình FFNN với các hàm huấn luyện khác nhau (`br` - Bayesian regularization, `lm`, và `gd` - gradient descent), cài đặt tối đa cho số lượng epochs là $1,000$ (Keong et al. $2016$).

- Tham số tốc độ học ($learning\ rate$) có mục tiêu tìm kiếm không gian trọng số tối thiểu ($minimum\ weight\ space$):
  - Tốc độ học quá cao có thể dẫn đến sự dao động gia tăng trong $MSE$ ($increased\ oscillations\ in\ MSE$).
  - Tốc độ học quá thấp tạo ra các bước nhảy nhỏ hơn trong không gian trọng số ($smaller\ steps\ in\ the\ weight\ space$).
  - Tốc độ học thấp có thể làm giảm khả năng thoát khỏi các điểm cực tiểu cục bộ trên bề mặt sai số ($error\ surface$) của mạng.

- Tham số động lượng ($momentum$) quy định mức độ nhạy cảm và tính ổn định của quá trình thích nghi trọng số:
  - Động lượng thấp khiến mạng giảm độ nhạy với các gradient cục bộ ($less\ sensitivity\ of\ the\ network\ to\ local\ gradients$).
  - Động lượng cao có thể gây phân kỳ thích nghi ($divergence\ of\ adaptation$), dẫn đến các trọng số không thể sử dụng được ($unusable\ weights$).
  - Các giá trị tối ưu của tốc độ học và động lượng mang lại hành vi trơn tru (smooth behaviour) và tăng tốc độ hội tụ (speed up convergence) (Winiczenko et al. $2016$; Yousif & Kazem $2021$).
  - Các giá trị quá thấp của tốc độ học và động lượng làm chậm quá trình hội tụ, trong khi các giá trị quá cao có thể dẫn đến mất ổn định mạng ($network\ instability$) và phân kỳ huấn luyện ($training\ divergence$) (Winiczenko et al. $2016$; Yousif & Kazem $2021$).

- Số lượng nơ-ron trong lớp ẩn ($number\ of\ neurons\ in\ the\ hidden\ layer$) giữ vai trò then chốt đối với hiệu suất mạng:
  - Quá ít nơ-ron ẩn dẫn đến khả năng thích nghi hạn chế trong mô hình hóa mô phỏng (limited adaptation in simulation modelling).
  - Quá nhiều nơ-ron ẩn có thể dẫn đến lỗi bộ nhớ hệ thống (system memory errors), hiện tượng huấn luyện quá mức / quá khớp ($over\ training$) (Winiczenko et al. $2016$) và làm tăng thời gian tính toán ($calculation\ time$) (Nazghelichi et al. $2011$).
  - Không có phương pháp có hệ thống (systematic method) để xác định cấu trúc số lượng nơ-ron ẩn của mạng.
  - Cận trên ($upper\ bound$) cho số lượng nơ-ron ẩn nhằm đạt được xấp xỉ mạng nơ-ron chính xác theo đề xuất của Hecht-Nielsen ($1992$) được mô tả bởi Phương trình ($6$):
    $$N_a \le 2 N_b + 1 \tag{6}$$
    trong đó:
    - $N_a$ là số lượng nơ-ron ẩn ($number\ of\ hidden\ neurons$).
    - $N_b$ là số lượng đầu vào ($number\ of\ inputs$).
  - Mối quan hệ giữa số lượng mẫu dữ liệu huấn luyện và số lượng nơ-ron ẩn do Rogers & Dowla ($1994$) đề xuất nhằm ngăn ngừa vấn đề quá khớp ($overfitting\ issue$) trong dữ liệu huấn luyện được xác định bởi Phương trình ($7$):
    $$N_a \le \frac{N_u}{N_b + 1} \tag{7}$$
    trong đó:
    - $N_u$ là số lượng mẫu trong dữ liệu huấn luyện ($number\ of\ samples\ in\ the\ training\ data$).
    - $N_a$ là số lượng nơ-ron ẩn.
    - $N_b$ là số lượng đầu vào.

- Quy trình tối ưu hóa siêu tham số truyền thống (conventional HPO) dựa trên phương pháp một biến tại một thời điểm (OVAT - one-variable-at-a-time):
  - Đối với mô hình ANN truyền thống để tìm kiếm điều kiện tối ưu, các mạng được huấn luyện dưới dải rộng các thiết lập siêu tham số theo phương pháp OVAT.
  - Quá trình HPO truyền thống được thực hiện trên tập dữ liệu huấn luyện ($T_{\mathrm{training}}$).
  - Việc lựa chọn các siêu tham số FFNN và RBFNN (radial basis function neural network) tương ứng dựa trên tiêu chuẩn $MSE$ thấp nhất cho từng tham số, sau đó áp dụng cho tập dữ liệu kiểm tra ($T_{\mathrm{testing}}$) để xác minh độ tin cậy của các mô hình mạng.
  - Các tham số được xem xét để xây dựng cấu trúc mạng tối ưu trong nghiên cứu này gồm: số lượng nơ-ron trong lớp ẩn, tốc độ học, động lượng, số lượng epoch, số lượng spreads (độ trải rộng), hàm huấn luyện và hàm kích hoạt.
  - Dải giá trị của các siêu tham số cho các mô hình FFNN và RBFNN truyền thống được trình bày trong Bảng 1 (Table 1).

- Bảng 1 (Table 1 | The range of ANN hyperparameters for conventional models) thiết lập dải siêu tham số cho các mô hình ANN truyền thống:
  - **Phương pháp FFNN truyền thống (Conventional-based FFNN method):**
    - Nghiên cứu thiết lập $4$ biến thể mô hình: `FFNN-1`, `FFNN-2`, `FFNN-3`, `FFNN-4`.
    - **Ký hiệu A - Số lượng nơ-ron ($Number\ of\ neurons$):**
      - `FFNN-1`: Dải thiết lập $1\text{--}30$
      - `FFNN-2`: Dải thiết lập $1\text{--}30$
      - `FFNN-3`: Dải thiết lập $1\text{--}30$
      - `FFNN-4`: Dải thiết lập $1\text{--}30$
    - **Ký hiệu B - Tốc độ học ($Learning\ rate$):**
      - `FFNN-1`: Dải thiết lập $0.1\text{--}1$
      - `FFNN-2`: Dải thiết lập $0.1\text{--}1$
      - `FFNN-3`: Dải thiết lập $0.1\text{--}1$
      - `FFNN-4`: Dải thiết lập $0.1\text{--}1$
    - **Ký hiệu C - Động lượng ($Momentum$):**
      - `FFNN-1`: Dải thiết lập $0.1\text{--}1$
      - `FFNN-2`: Dải thiết lập $0.1\text{--}1$
      - `FFNN-3`: Dải thiết lập $0.1\text{--}1$
      - `FFNN-4`: Dải thiết lập $0.1\text{--}1$
    - **Ký hiệu D - Số lượng epoch ($Number\ of\ epochs$):**
      - `FFNN-1`: Dải thiết lập $100\text{--}1,000$
      - `FFNN-2`: Dải thiết lập $100\text{--}1,000$
      - `FFNN-3`: Dải thiết lập $100\text{--}1,000$
      - `FFNN-4`: Dải thiết lập $100\text{--}1,000$
    - **Ký hiệu E - Hàm huấn luyện ($Training\ function$):**
      - `FFNN-1`: `trainlm`
      - `FFNN-2`: `trainlm`
      - `FFNN-3`: `traingdm`
      - `FFNN-4`: `traingdm`
    - **Ký hiệu F - Hàm kích hoạt ($Activation\ function$):**
      - `FFNN-1`: `tansig`
      - `FFNN-2`: `ReLu`
      - `FFNN-3`: `tansig`
      - `FFNN-4`: `ReLu`
    - **Số lần lặp lại ($Number\ of\ repetitions$):**
      - `FFNN-1`: $60$
      - `FFNN-2`: $60$
      - `FFNN-3`: $60$
      - `FFNN-4`: $60$
    - *Bảng tổng hợp cấu hình Conventional-based FFNN method:*

| Ký hiệu (Symbol) | Siêu tham số (Hyperparameters) | Mô hình FFNN-1 | Mô hình FFNN-2 | Mô hình FFNN-3 | Mô hình FFNN-4 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **A** | Số lượng nơ-ron (Number of neurons) | $1\text{--}30$ | $1\text{--}30$ | $1\text{--}30$ | $1\text{--}30$ |
| **B** | Tốc độ học (Learning rate) | $0.1\text{--}1$ | $0.1\text{--}1$ | $0.1\text{--}1$ | $0.1\text{--}1$ |
| **C** | Động lượng (Momentum) | $0.1\text{--}1$ | $0.1\text{--}1$ | $0.1\text{--}1$ | $0.1\text{--}1$ |
| **D** | Số lượng epoch (Number of epochs) | $100\text{--}1,000$ | $100\text{--}1,000$ | $100\text{--}1,000$ | $100\text{--}1,000$ |
| **E** | Hàm huấn luyện (Training function) | `trainlm` | `trainlm` | `traingdm` | `traingdm` |
| **F** | Hàm kích hoạt (Activation function) | `tansig` | `ReLu` | `tansig` | `ReLu` |
| | Số lần lặp lại (Number of repetitions) | $60$ | $60$ | $60$ | $60$ |

  - **Phương pháp RBFNN truyền thống (Conventional-based RBFNN method):**
    - Nghiên cứu thiết lập mô hình: `RBFNN`.
    - **Ký hiệu A - Số lượng nơ-ron ($Number\ of\ neurons$):**
      - Dải thiết lập $1\text{--}30$
    - **Ký hiệu B - Số lượng độ trải rộng ($Number\ of\ spreads$):**
      - Dải thiết lập $0.5\text{--}3$
    - **Số lần lặp lại ($Number\ of\ repetitions$):**
      - $36$
    - *Bảng tổng hợp cấu hình Conventional-based RBFNN method:*

| Ký hiệu (Symbol) | Siêu tham số (Hyperparameters) | Thiết lập dải giá trị mô hình RBFNN (Range setting) |
| :--- | :--- | :---: |
| **A** | Số lượng nơ-ron (Number of neurons) | $1\text{--}30$ |
| **B** | Số lượng độ trải rộng (Number of spreads) | $0.5\text{--}3$ |
| | Số lần lặp lại (Number of repetitions) | $36$ |
