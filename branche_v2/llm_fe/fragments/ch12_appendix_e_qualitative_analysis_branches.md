## Phụ lục E: Phân tích Định tính (Appendix E: Qualitative Analysis)

### E.1 Phân tích Khả năng Diễn giải (Interpretability Analysis)

- **Sinh chương trình biến đổi đặc trưng bằng ngôn ngữ tự nhiên (Natural language programs & interpretability)**:
  - LLM-FE tạo ra các chương trình biến đổi đặc trưng (feature-transformation programs) đi kèm diễn giải bằng ngôn ngữ tự nhiên (natural language), qua đó hỗ trợ tối đa khả năng diễn giải (interpretability).
  - Mỗi chương trình đặc trưng được sinh ra đều trải qua quy trình đánh giá độc lập (independently evaluated); những chương trình đạt hiệu quả cao được lưu trữ vào bộ đệm kinh nghiệm phục vụ quá trình tinh chỉnh tiến hóa (evolutionary refinement).
  - Cơ chế này cho phép các đặc trưng hữu ích phát hiện ở giai đoạn đầu có thể tích hợp và cấu thành (compose) nên các đặc trưng bậc cao hơn (higher-order features) mà vẫn bảo toàn trọn vẹn tính tường minh và khả năng lý giải.

- **Đánh giá mức độ đóng góp thực chất bằng phân tích gán thuộc tính SHAP (Attribution analysis using SHAP values)**:
  - Nhằm xác định tính hữu dụng thực tế của các đặc trưng được sinh ra, nghiên cứu tiến hành phân tích gán thuộc tính (attribution analysis) thông qua các giá trị SHAP (SHapley Additive exPlanations values).
  - Kết quả phân tích khẳng định một tập con nhất quán các đặc trưng được LLM-FE khám phá đạt điểm số gán thuộc tính rất cao (high attribution scores).
  - Bằng chứng này chứng minh các đặc trưng mới thực sự đóng góp chủ động vào tiến trình dự đoán của mô hình, thay vì chỉ đóng vai trò như các thành phần tăng cường giả mạo hoặc dư thừa không được dùng đến (spurious or unused augmentations).

- **Định lượng tỷ lệ đặc trưng quan trọng trong top-$k$ theo SHAP (Table 15: Percentage of generated features ranked among top-$k$)**:
  - Dữ liệu định lượng từ Bảng 15 chứng minh sự hiện diện áp đảo của các đặc trưng do LLM-FE sinh ra trong nhóm các đặc trưng có tầm ảnh hưởng lớn nhất:
    - Có $16.67\%$ đặc trưng được sinh lọt vào nhóm top-$10$ đặc trưng có tác động mạnh mẽ nhất đến quyết định của mô hình.
    - Hơn $60\%$ (chính xác là $62.96\%$) đặc trưng xuất hiện trong nhóm top-$50$ thuộc tính quan trọng nhất.

| Thứ hạng (Top-$k$) | Tỷ lệ phần trăm (%) (Percentage) |
| :--- | :---: |
| Top-$10$ | $16.67$ |
| Top-$20$ | $25.93$ |
| Top-$30$ | $37.04$ |
| Top-$40$ | $57.41$ |
| Top-$50$ | $62.96$ |

### E.2 Độ Bền vững Trước Nhiễu (Robustness to Noise)

- **Thách thức của hiện tượng nhiễu trong dữ liệu thực tế (Noise challenge in real-world tabular data)**:
  - Nhiễu là thách thức phổ biến trong các tập dữ liệu bảng thực tế, xuất phát từ các khiếm khuyết của cảm biến (sensor imperfections), sai sót của con người (human errors), biến động môi trường (environmental variability), và các giới hạn phần cứng (hardware constraints).
  - Sự tha hóa dữ liệu này làm lu mờ các cấu trúc có ý nghĩa, gây cản trở nghiêm trọng đến khả năng học các mối quan hệ bản chất tiềm ẩn (true underlying relationships) của các mô hình học máy.

- **Thiết lập kiểm thử độ bền vững với nhiễu Gauss (Gaussian noise experimental setup)**:
  - Để đánh giá năng lực của LLM-FE trong việc khai thác tri thức tiên nghiệm (prior knowledge) kết hợp tìm kiếm tiến hóa nhằm duy trì hiệu quả trong điều kiện bất lợi, nghiên cứu bổ sung nhiễu Gauss (Gaussian noise) với độ lệch chuẩn $\sigma \in \{0.0, 0.01, 0.05, 0.1\}$ vào $6$ tập dữ liệu phân loại chỉ chứa đặc trưng số (numerical classification datasets).
  - Mô hình dự đoán được sử dụng là XGBoost, với mô hình nền tảng GPT-3.5-Turbo làm backbone cho tất cả các phương pháp dựa trên LLM.
  - Các phương pháp so sánh đối chuẩn bao gồm: Mô hình cơ sở không có kỹ thuật đặc trưng (Base), OpenFE, CAAFE, và LLM-FE.

- **Hiệu năng và độ bền vững vượt trội của LLM-FE trong môi trường nhiễu**:
  - **Hình 10.** Tác động của các mức độ nhiễu lên hiệu năng mô hình XGBoost
    - <img src="assets/fig_10_p22.png" alt="Hình 10" />
    - **Hình này chứng minh điều gì**
      - LLM-FE duy trì độ chính xác cao nhất và thể hiện độ bền vững vượt trội nhất trước sự gia tăng của mức độ nhiễu so với mọi phương pháp đối chuẩn.
    - **Từ đâu mà thấy được**
      - Trục hoành biểu diễn mức nhiễu $\sigma \in \{0.0, 0.01, 0.05, 0.1\}$, trục tung Accuracy ($0.85 - 0.91$): đường LLM-FE luôn ở trên đỉnh (~$0.903 - 0.908$), vượt trội hơn hẳn OpenFE (~$0.880 - 0.891$), CAAFE (~$0.877 - 0.888$), và Base (~$0.851 - 0.860$).
  - Trên tất cả các cấp độ nhiễu, LLM-FE liên tục duy trì độ chính xác vượt trội và thể hiện độ bền vững cao hơn hẳn các giải pháp cạnh tranh, khẳng định khả năng chống chịu sự suy giảm chất lượng do nhiễu gây ra (resilience to noise-induced degradation).

### E.3 Tác động của Tri thức Miền (Impact of Domain Knowledge)

- **Vai trò định hướng của tri thức miền trong kỹ thuật đặc trưng (Role of domain knowledge in feature engineering)**:
  - Việc lồng ghép tri thức miền (domain knowledge) không chỉ cải thiện đáng kể độ chính xác của mô hình dự đoán mà còn cung cấp cơ sở lý giải xác đáng (justification) cho các biến đổi được chọn, mang lại quy trình kỹ thuật đặc trưng giàu tính diễn giải.
  - Tác động tích cực cả về mặt định tính lẫn định lượng được chứng minh cụ thể trên hai tập dữ liệu y sinh: tập `Breast-W` (phân biệt khối u lành tính và ác tính) và tập `Heart` (dự đoán nguy cơ bệnh tim mạch dựa trên các chỉ số bệnh nhân).

- **So sánh định lượng và định tính trên hai tập dữ liệu lâm sàng**:
  - **Hình 11.** Phân tích định lượng và định tính về tác động của tri thức miền trên tập dữ liệu Heart và Breast-W
    - <img src="assets/fig_09_p22.png" alt="Hình 11" />
    - **Hình này chứng minh điều gì**
      - Tri thức miền giúp LLM-FE tạo ra các đặc trưng mang ý nghĩa lâm sàng sâu sắc và nâng cao vượt bậc độ chính xác so với biến thể thiếu tri thức miền và các phương pháp AutoFE truyền thống.
    - **Từ đâu mà thấy được**
      - Hình 11(a) cho thấy XGBoost với LLM-FE đạt accuracy cao nhất trên Heart (~$0.866$) và Breast-W (~$0.970$), vượt OpenFE, AutoFeat và biến thể w/o Domain Knowledge; Hình 11(b)-(c) đối chiếu mã Python cho thấy đặc trưng có tri thức miền sở hữu lập luận y khoa thuyết phục thay vì tính toán vô nghĩa.

- **Phân tích định tính ca bệnh lý tim mạch (Heart Dataset Case Study)**:
  - *LLM-FE có tri thức miền*: Mô hình nhận thức được vai trò trọng yếu của chỉ số cholesterol huyết thanh trong sức khỏe tim mạch và đề xuất tạo đặc trưng `Log_Cholesterol` thông qua phép biến đổi logarit:
    ```python
    def modify_features(df_input) -> pd.DataFrame:
        """    
        Thought: Taking the logarithm of serum cholesterol   
                 may help normalize the distribution and 
                 emphasize the impact of extreme values.
        Feature: Log_Cholesterol | Log_Cholesterol = Logarithm(Cholesterol)
        """
        df_output = df_input.copy()
        # Calculate Log_Cholesterol
        df_output['Log_Cholesterol'] = df_output['Cholesterol'].apply(lambda x: np.log(x) if x > 0 else 0)
        return df_output
    ```
    Biến đổi này giúp chuẩn hóa phân phối dữ liệu, giảm thiểu tác động tiêu cực của các giá trị ngoại lai (outliers) và ổn định phương sai (stabilize variance).
  - *Biến thể loại bỏ tri thức miền (w/o Domain Knowledge)*: Do các cột bị ẩn danh thành $C_1, C_2, \dots$, mô hình ghép nối tùy tiện các biến phân loại để tính tần suất `C_1_freq` và giá trị trung bình gom nhóm `C_3_mean_by_C_1 = df_output.groupby('C_1')['C_3'].transform('mean')`, tạo ra các biến đổi khó diễn giải và làm suy giảm hiệu năng mô hình (Hình 11(a)).

- **Phân tích định tính ca chẩn đoán ung thư vú (Breast-W Dataset Case Study)**:
  - *LLM-FE có tri thức miền*: Mô hình nhận diện được tương tác sinh học giữa số lượng hạch nhân bình thường (`Normal_Nucleoli`) và số lượng phân bào (`Mitoses`), từ đó đề xuất chỉ số hoạt tính tăng sinh `proliferation_activity`:
    ```python
    def modify_features(df_input) -> pd.DataFrame:
        """
        Thought: Interaction between normal nucleoli and mitoses could capture 
                 the proliferative activity and potentially enhance the predictive 
                 power for malignancy.
        Feature: proliferation_activity | proliferation_activity = Normal_Nucleoli*Mitoses
        """
        df_output = df_input.copy()
        # Calculate the proliferation activity
        df_output['proliferation_activity'] = df_output['Normal_Nucleoli'] * df_output['Mitoses']
        return df_output
    ```
    Đây là một thước đo có ý nghĩa sinh học rõ rệt phản ánh mức độ ác tính của khối u, mang lại bước nhảy vọt về hiệu năng phân loại.
  - *Biến thể loại bỏ tri thức miền (w/o Domain Knowledge)*: Thiếu vắng ngữ cảnh y khoa, mô hình chỉ tạo ra một phép tính trung bình đơn giản của toàn bộ các cột từ $C_0$ đến $C_8$ (`avg_C = df_output[['C_0', ..., 'C_8']].mean(axis=1)`), hoàn toàn thiếu vắng tính giải thích và giá trị lâm sàng (clinical significance).

### E.4 Tác động của Tiến hóa Đa đảo (Impact of Multi-Island Evolution)

- **Cơ chế phân vùng và đánh đổi giữa thăm dò và khai thác (Exploration vs. exploitation trade-off)**:
  - Tại bước khởi tạo, không gian khám phá đặc trưng được phân vùng thành $k$ đảo độc lập (independent islands) bằng cách chia đều tập đặc trưng ứng viên ban đầu.
  - Với một ngân sách tính toán cố định gồm $T$ vòng lặp (iterations), mỗi đảo nhận được xấp xỉ $T/k$ vòng lặp; do đó, tham số $k$ đóng vai trò cốt lõi điều phối sự đánh đổi giữa thăm dò (exploration) và khai thác (exploitation):
    - Giá trị $k$ nhỏ cho phép đào sâu tinh chỉnh bên trong từng đảo riêng lẻ, nhấn mạnh tính khai thác (exploitation).
    - Giá trị $k$ lớn khuyến khích thăm dò diện rộng (broad exploration) thông qua nhiều quỹ đạo tìm kiếm độc lập nhưng có chiều sâu tinh chỉnh nông hơn.

- **Đánh giá thực nghiệm với các cấu hình số đảo khác nhau (Table 16: Effect of the number of islands)**:
  - Nghiên cứu khảo sát ba thiết lập đại diện với $k = 1, 3, 5$ trên $6$ tập dữ liệu phân loại, báo cáo giá trị trung bình và độ lệch chuẩn qua $5$ lần chia ngẫu nhiên (Table 16).
  - Số lượng đảo ở mức vừa phải ($k = 3$) mang lại sự cân bằng tối ưu và nhất quán nhất giữa tính đa dạng thăm dò và chiều sâu tinh chỉnh:
    - Sử dụng một đảo duy nhất ($k = 1$) hạn chế độ đa dạng của các đặc trưng được khám phá.
    - Sử dụng quá nhiều đảo ($k = 5$) làm phân tán ngân sách tính toán, khiến chiều sâu tinh chỉnh của từng quỹ đạo bị suy giảm.
  - Hiệu năng tổng thể của mô hình rất vững chắc trên các cấu hình đảo; các quỹ đạo tìm kiếm độc lập bổ trợ hiệu quả cho nhau và đem lại kết quả ổn định khi ngân sách tính toán được phân bổ hợp lý.

| Số lượng đảo (# Islands $k$) | `adult` | `bank` | `cmc` | `car` | `breast-w` | `vehicle` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0.874 \pm 0.002$ | $\mathbf{0.908 \pm 0.003}$ | $0.532 \pm 0.017$ | $\mathbf{0.999 \pm 0.003}$ | $0.966 \pm 0.014$ | $0.761 \pm 0.012$ |
| $3$ | $0.874 \pm 0.002$ | $0.907 \pm 0.002$ | $\mathbf{0.535 \pm 0.019}$ | $\mathbf{0.999 \pm 0.001}$ | $\mathbf{0.973 \pm 0.009}$ | $0.769 \pm 0.013$ |
| $5$ | $0.874 \pm 0.003$ | $0.907 \pm 0.003$ | $0.528 \pm 0.010$ | $0.998 \pm 0.003$ | $0.969 \pm 0.014$ | $\mathbf{0.773 \pm 0.015}$ |

### E.5 Tác động của Tinh chỉnh Tiến hóa (Impact of Evolutionary Refinement)

- **Cơ chế vượt cực trị địa phương thông qua tìm kiếm tiến hóa (Escaping local optima)**:
  - So sánh đối chiếu tiến trình tối ưu giữa LLM-FE đầy đủ và biến thể loại bỏ tinh chỉnh tiến hóa (w/o Evolutionary Refinement) minh chứng rõ nét ưu thế của tìm kiếm tiến hóa.
  - Trong khi biến thể không tiến hóa nhanh chóng bị đình trệ (plateau / stagnate) do vướng vào các cực trị địa phương (local optima), LLM-FE liên tục cải thiện độ chính xác kiểm định (validation accuracy) qua từng thế hệ tối ưu hóa.
  - Cụ thể trên tập dữ liệu `PC1`, biến thể không tiến hóa đi ngang và ngừng cải thiện chỉ sau $7$ vòng lặp (seven iterations); trên tập `Balance-Scale`, nó đình trệ hoàn toàn chỉ sau $5$ vòng lặp (five iterations).
  - Cơ chế tinh chỉnh tiến hóa của LLM-FE mang lại quy trình tối ưu hóa bền bỉ và mạnh mẽ hơn, giúp mô hình vượt thoát các bẫy cục bộ để đạt độ chính xác kiểm định vượt trội trên cả hai tập dữ liệu nói trên cũng như trên toàn bộ các tập thử nghiệm.

- **Phân tích quỹ đạo hiệu năng kiểm định qua các vòng lặp (Performance Trajectory Analysis across 12 Datasets)**:
  - **Hình 12.** Phân tích quỹ đạo hiệu năng kiểm định theo số vòng lặp tối ưu
    - <img src="assets/fig_11_p24_vector.png" alt="Hình 12" />
    - **Hình này chứng minh điều gì**
      - Tinh chỉnh tiến hóa giúp LLM-FE liên tục thoát khỏi cực trị địa phương và cải thiện độ chính xác kiểm định, trong khi biến thể không tiến hóa nhanh chóng bị đình trệ.
    - **Từ đâu mà thấy được**
      - Trên 12 tập dữ liệu qua $20$ vòng lặp (Iterations $0 - 20$), đường LLM-FE (đỏ tam giác) liên tục bứt phá lên các mức accuracy cao hơn, trong khi biến thể w/o Evolutionary Refinement (vàng tròn nét đứt) sớm đi ngang (plateau) ở mức thấp (điển hình dừng sau $5$ vòng lặp ở Balance-Scale và sau $7$ vòng lặp ở Pc1).
  - Quỹ đạo hiệu năng chi tiết trên $12$ tập dữ liệu phân loại (`Adult`, `Bank`, `Balance-Scale`, `Eucalyptus`, `Blood`, `Car`, `Cmc`, `Heart`, `Credit-g`, `Junglechess`, `Tic-tac-toe`, `Pc1`) khẳng định sự cần thiết của vòng lặp phản hồi thực nghiệm để liên tục sàng lọc và nhân rộng các đặc trưng tối ưu.
