### D.2 Generalizability Analysis

- **Mục tiêu mở rộng phân tích tổng quát hóa**: Phần này mở rộng các kết quả thực nghiệm từ Mục 4.4 nhằm kiểm chứng toàn diện khả năng tổng quát hóa (generalizability) và sự cải thiện hiệu năng đạt được bởi LLM-FE trên nhiều khía cạnh khác nhau:
  - Khảo sát trên các mô hình dự đoán (prediction models) đa dạng bao gồm XGBoost, MLP (Multi-Layer Perceptron - Mạng nơ-ron truyền thẳng nhiều lớp), và TabPFN (Bảng 10).
  - Đánh giá trên nhiều mô hình ngôn ngữ lớn làm nền tảng (LLM backbones) khác nhau gồm GPT-4o-mini, Qwen2.5-72B-Instruct, và Gemini-2.5-Flash bên cạnh GPT-3.5-Turbo mặc định (Bảng 11).
  - Kiểm thử trên các mô hình dự đoán bổ sung có quy mô nhỏ hơn hoặc bản chất khác biệt như CatBoost và Hồi quy Logistic (Logistic Regression) (Bảng 12).
- **Kết luận bao quát**: Dữ liệu thực nghiệm từ Bảng 10, Bảng 11 và Bảng 12 chứng minh rằng LLM-FE vượt trội hơn các mô hình gốc (base models) tương ứng không qua kỹ thuật đặc trưng trên phần lớn các tập dữ liệu thực nghiệm ở cả hai tác vụ phân loại (classification) và hồi quy (regression).

#### Cải thiện Hiệu năng trên Đa dạng Mô hình Dự đoán (Bảng 10)

- **Thiết lập thực nghiệm đồng nhất (End-to-End Prediction Model Alignment)**:
  - Sử dụng trực tiếp chính mô hình dự đoán mục tiêu (XGBoost, MLP hoặc TabPFN) trong quá trình đánh giá độ thích nghi (fitness evaluation) để sinh đặc trưng, sau đó dùng chính mô hình đó để thực hiện suy luận (inference) trên tập kiểm thử.
  - LLM backbone được sử dụng để sinh đặc trưng trong thiết lập này là GPT-3.5-Turbo.
  - Kết quả được đo lường trung bình và độ lệch chuẩn ($\text{mean} \pm \text{std}$) qua 5 lần chia dữ liệu độc lập (five splits).
  - Thước đo đánh giá: Sai số căn bậc hai trung bình (RMSE - Root Mean Squared Error) cho các tập hồi quy (giá trị càng nhỏ thể hiện hiệu năng càng tốt) và Độ chính xác (Accuracy) cho các tập phân loại (giá trị càng lớn thể hiện hiệu năng càng tốt).

- **Hiệu năng vượt trội trên mô hình cây quyết định XGBoost**:
  - Trên toàn bộ 9 tập dữ liệu phân loại, XGBoost kết hợp với LLM-FE đều cải thiện độ chính xác so với mô hình gốc không có kỹ thuật đặc trưng (Base):
    - *breast-w*: tăng từ $0.956 \pm 0.012$ lên $0.973 \pm 0.009$.
    - *blood-transfusion*: tăng từ $0.742 \pm 0.012$ lên $0.751 \pm 0.036$.
    - *car*: tăng từ $0.995 \pm 0.003$ lên $0.999 \pm 0.001$.
    - *cmc*: tăng từ $0.528 \pm 0.030$ lên $0.535 \pm 0.019$.
    - *credit-g*: tăng từ $0.751 \pm 0.019$ lên $0.766 \pm 0.025$.
    - *eucalyptus*: tăng từ $0.655 \pm 0.024$ lên $0.668 \pm 0.027$.
    - *heart*: tăng từ $0.858 \pm 0.013$ lên $0.866 \pm 0.021$.
    - *pc1*: tăng từ $0.931 \pm 0.004$ lên $0.935 \pm 0.006$.
    - *vehicle*: tăng từ $0.754 \pm 0.016$ lên $0.769 \pm 0.027$.
  - Trên tất cả 5 tập dữ liệu hồi quy, LLM-FE giúp giảm RMSE đáng kể so với Base XGBoost:
    - *bike [101]*: RMSE giảm từ $4.094 \pm 0.096$ xuống $3.985 \pm 0.084$.
    - *crab [100]*: RMSE giảm từ $2.325 \pm 0.094$ xuống $2.211 \pm 0.124$.
    - *housing [104]*: RMSE giảm từ $4.845 \pm 0.191$ xuống $4.525 \pm 0.260$.
    - *insurance [103]*: RMSE giảm từ $5.269 \pm 0.260$ xuống $5.069 \pm 0.392$.
    - *wine [100]*: RMSE giảm từ $0.639 \pm 0.006$ xuống $0.612 \pm 0.007$.

- **Hiệu năng trên mô hình nền tảng dạng bảng TabPFN**:
  - LLM-FE tăng cường hiệu năng cho TabPFN trên hầu hết các tập phân loại:
    - *credit-g*: tăng mạnh từ $0.728 \pm 0.008$ lên $0.794 \pm 0.022$.
    - *car*: tăng từ $0.984 \pm 0.007$ lên $0.996 \pm 0.006$.
    - *blood-transfusion*: tăng nhẹ từ $0.790 \pm 0.012$ lên $0.791 \pm 0.011$.
    - *cmc*: tăng từ $0.563 \pm 0.030$ lên $0.566 \pm 0.036$.
    - *eucalyptus*: tăng từ $0.712 \pm 0.016$ lên $0.715 \pm 0.021$.
    - *pc1*: tăng từ $0.936 \pm 0.007$ lên $0.937 \pm 0.003$.
    - *vehicle*: tăng từ $0.852 \pm 0.016$ lên $0.856 \pm 0.028$.
    - *breast-w*: duy trì mức độ chính xác tương đương ($0.971 \pm 0.006$ so với $0.971 \pm 0.007$).
    - *heart*: dao động nhẹ ($0.882 \pm 0.025$ so với $0.880 \pm 0.021$).
  - Trên các tập hồi quy, TabPFN kết hợp LLM-FE đạt RMSE thấp hơn trên cả 5 tập dữ liệu:
    - *bike [101]*: giảm từ $3.795 \pm 0.094$ xuống $3.759 \pm 0.109$.
    - *crab [100]*: giảm từ $2.073 \pm 0.115$ xuống $2.065 \pm 0.134$.
    - *housing [104]*: giảm từ $4.338 \pm 0.081$ xuống $4.184 \pm 0.071$.
    - *insurance [103]*: giảm từ $4.653 \pm 0.237$ xuống $4.592 \pm 0.261$.
    - *wine [100]*: giảm từ $0.678 \pm 0.023$ xuống $0.676 \pm 0.024$.

- **Hiệu năng và tính nhạy cảm trên mạng nơ-ron MLP**:
  - Trên tác vụ phân loại, LLM-FE đem lại bước nhảy vọt hiệu năng rất lớn cho MLP trên các tập dữ liệu có quan hệ phi tuyến phức tạp:
    - *blood-transfusion*: tăng từ $0.674 \pm 0.071$ lên $0.782 \pm 0.017$ (tăng $+0.108$).
    - *credit-g*: tăng từ $0.558 \pm 0.144$ lên $0.633 \pm 0.101$ (tăng $+0.075$).
    - *vehicle*: tăng từ $0.583 \pm 0.062$ lên $0.673 \pm 0.043$ (tăng $+0.090$).
    - *eucalyptus*: tăng từ $0.414 \pm 0.064$ lên $0.456 \pm 0.062$.
    - *car*: tăng từ $0.929 \pm 0.019$ lên $0.950 \pm 0.009$.
    - *breast-w*: tăng từ $0.957 \pm 0.010$ lên $0.964 \pm 0.005$.
    - *cmc*: tăng từ $0.559 \pm 0.028$ lên $0.566 \pm 0.028$.
    - *heart*: tăng từ $0.840 \pm 0.010$ lên $0.844 \pm 0.006$.
    - *pc1*: suy giảm từ $0.931 \pm 0.002$ xuống $0.904 \pm 0.055$.
  - Trên tác vụ hồi quy, MLP ghi nhận sự cải thiện rõ trên *bike [101]* (RMSE giảm từ $1.205 \pm 0.028$ xuống $1.044 \pm 0.042$), *crab [100]* ($2.128 \pm 0.104$ xuống $2.110 \pm 0.106$) và giữ nguyên trên *wine [100]* ($0.728 \pm 0.005$ so với $0.728 \pm 0.003$).
  - Hiện tượng bất ổn định trên tập hồi quy của MLP: Trên hai tập *housing [104]* (từ $1.045 \pm 0.018$ vọt lên $9.183 \pm 0.734$) và *insurance [103]* (từ $1.189 \pm 0.070$ vọt lên $6.459 \pm 0.341$), MLP gặp hiện tượng bùng nổ sai số RMSE khi bổ sung đặc trưng do LLM-FE sinh ra. Điều này phản ánh tính nhạy cảm đặc thù của kiến trúc mạng nơ-ron sâu truyền thống đối với tỷ lệ co giãn (feature scaling) và các giá trị ngoại lai (outliers) sinh ra từ các biến đổi toán học phức tạp trong tác vụ hồi quy.

| Dataset | XGBoost (Base) | XGBoost (LLM-FE) | MLP (Base) | MLP (LLM-FE) | TabPFN (Base) | TabPFN (LLM-FE) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Phân loại (Accuracy $\uparrow$)** | | | | | | |
| breast-w | $0.956 \pm 0.012$ | **$0.973 \pm 0.009$** | $0.957 \pm 0.010$ | $0.964 \pm 0.005$ | $0.971 \pm 0.006$ | $0.971 \pm 0.007$ |
| blood-transfusion | $0.742 \pm 0.012$ | $0.751 \pm 0.036$ | $0.674 \pm 0.071$ | $0.782 \pm 0.017$ | $0.790 \pm 0.012$ | **$0.791 \pm 0.011$** |
| car | $0.995 \pm 0.003$ | **$0.999 \pm 0.001$** | $0.929 \pm 0.019$ | $0.950 \pm 0.009$ | $0.984 \pm 0.007$ | $0.996 \pm 0.006$ |
| cmc | $0.528 \pm 0.030$ | $0.535 \pm 0.019$ | $0.559 \pm 0.028$ | **$0.566 \pm 0.028$** | $0.563 \pm 0.030$ | **$0.566 \pm 0.036$** |
| credit-g | $0.751 \pm 0.019$ | $0.766 \pm 0.025$ | $0.558 \pm 0.144$ | $0.633 \pm 0.101$ | $0.728 \pm 0.008$ | **$0.794 \pm 0.022$** |
| eucalyptus | $0.655 \pm 0.024$ | $0.668 \pm 0.027$ | $0.414 \pm 0.064$ | $0.456 \pm 0.062$ | $0.712 \pm 0.016$ | **$0.715 \pm 0.021$** |
| heart | $0.858 \pm 0.013$ | $0.866 \pm 0.021$ | $0.840 \pm 0.010$ | $0.844 \pm 0.006$ | **$0.882 \pm 0.025$** | $0.880 \pm 0.021$ |
| pc1 | $0.931 \pm 0.004$ | $0.935 \pm 0.006$ | $0.931 \pm 0.002$ | $0.904 \pm 0.055$ | $0.936 \pm 0.007$ | **$0.937 \pm 0.003$** |
| vehicle | $0.754 \pm 0.016$ | $0.769 \pm 0.027$ | $0.583 \pm 0.062$ | $0.673 \pm 0.043$ | $0.852 \pm 0.016$ | **$0.856 \pm 0.028$** |
| **Hồi quy (RMSE $\downarrow$)** | | | | | | |
| bike [101] | $4.094 \pm 0.096$ | $3.985 \pm 0.084$ | $1.205 \pm 0.028$ | **$1.044 \pm 0.042$** | $3.795 \pm 0.094$ | $3.759 \pm 0.109$ |
| crab [100] | $2.325 \pm 0.094$ | $2.211 \pm 0.124$ | $2.128 \pm 0.104$ | $2.110 \pm 0.106$ | $2.073 \pm 0.115$ | **$2.065 \pm 0.134$** |
| housing [104] | $4.845 \pm 0.191$ | $4.525 \pm 0.260$ | **$1.045 \pm 0.018$** | $9.183 \pm 0.734$ | $4.338 \pm 0.081$ | $4.184 \pm 0.071$ |
| insurance [103] | $5.269 \pm 0.260$ | $5.069 \pm 0.392$ | **$1.189 \pm 0.070$** | $6.459 \pm 0.341$ | $4.653 \pm 0.237$ | $4.592 \pm 0.261$ |
| wine [100] | $0.639 \pm 0.006$ | **$0.612 \pm 0.007$** | $0.728 \pm 0.005$ | $0.728 \pm 0.003$ | $0.678 \pm 0.023$ | $0.676 \pm 0.024$ |

#### Khả năng Tổng quát hóa qua các Mô hình Ngôn ngữ Lớn Khác nhau (Bảng 11)

- **Đánh giá tính độc lập với LLM backbone**:
  - Nhằm kiểm tra xem thành công của LLM-FE có phụ thuộc độc quyền vào GPT-3.5-Turbo hay không, tác giả tiến hành thử nghiệm LLM-FE với 3 mô hình ngôn ngữ lớn tiên tiến khác thuộc các họ kiến trúc và nhà phát triển khác nhau:
    - **Qwen2.5-72B-Instruct**: Mô hình mã nguồn mở quy mô lớn (open-weight LLM) hàng đầu từ Alibaba Cloud.
    - **GPT-4o-mini**: Mô hình nhẹ, tối ưu hóa chi phí và tốc độ suy luận của OpenAI.
    - **Gemini-2.5-Flash**: Mô hình đa phương thức tốc độ cao thế hệ mới của Google.
  - Tất cả các thí nghiệm trong Bảng 11 đều sử dụng **XGBoost** làm mô hình dự đoán hạ nguồn cố định để so sánh trực tiếp năng lực kỹ thuật đặc trưng thuần túy của các LLM.

- **Kết quả nhất quán vượt trội so với Base model**:
  - Cả 3 mô hình LLM khi tích hợp vào khung tiến hóa LLM-FE đều vượt trội hơn mô hình XGBoost Base (không có feature engineering) trên hầu hết các tập dữ liệu. Điều này khẳng định cơ chế tìm kiếm tiến hóa và tối ưu hóa hai cấp của LLM-FE có tính tổng quát hóa cao và tương thích tốt với nhiều họ LLM khác nhau.
  - **Qwen2.5-72B-Instruct** thể hiện ưu thế vượt trội trên các bài toán phân loại:
    - Đạt độ chính xác tuyệt đối $1.000 \pm 0.000$ trên tập *car*.
    - Dẫn đầu trên *breast-w* ($0.974 \pm 0.006$), *credit-g* ($0.775 \pm 0.022$), *eucalyptus* ($0.678 \pm 0.028$), *heart* ($0.863 \pm 0.023$), *vehicle* ($0.770 \pm 0.020$).
    - Trên tác vụ hồi quy, Qwen2.5-72B đạt kết quả tốt nhất trên tập *wine [100]* với RMSE giảm xuống $0.610 \pm 0.004$ (so với Base là $0.639 \pm 0.006$).
  - **GPT-4o-mini** thể hiện năng lực nổi bật trên các tác vụ hồi quy phức tạp:
    - Đạt RMSE thấp nhất (tốt nhất) trên 4 trên 5 tập hồi quy: *bike [101]* ($3.928 \pm 0.186$ so với Base $4.094$), *crab [100]* ($2.193 \pm 0.132$ so với Base $2.325$), *housing [104]* ($4.430 \pm 0.126$ so với Base $4.845$), và *insurance [103]* ($5.100 \pm 0.351$ so với Base $5.269$).
    - Trên phân loại, dẫn đầu trên tập *cmc* ($0.538 \pm 0.016$) và *pc1* ($0.935 \pm 0.008$).
  - **Gemini-2.5-Flash** duy trì hiệu năng ổn định và cải thiện nhất quán:
    - Vượt qua Base trên tất cả các tập phân loại: *breast-w* ($0.961 \pm 0.011$), *blood-transfusion* ($0.747 \pm 0.023$), *car* ($0.997 \pm 0.005$), *cmc* ($0.534 \pm 0.024$), *credit-g* ($0.755 \pm 0.012$), *eucalyptus* ($0.659 \pm 0.032$), *pc1* ($0.934 \pm 0.009$), *vehicle* ($0.766 \pm 0.026$).
    - Cải thiện RMSE trên *bike [101]* ($3.960 \pm 0.119$), *crab [100]* ($2.273 \pm 0.154$), *housing [104]* ($4.769 \pm 0.393$), và *wine [100]* ($0.633 \pm 0.005$). Điểm ngoại lệ duy nhất là trên tập *insurance [103]* ($5.351 \pm 0.776$ so với Base $5.269 \pm 0.260$).

| Dataset | Base (XGBoost) | Qwen2.5-72B | GPT-4o-mini | Gemini-2.5-Flash |
| :--- | :--- | :--- | :--- | :--- |
| **Phân loại (Accuracy $\uparrow$)** | | | | |
| breast-w | $0.956 \pm 0.012$ | **$0.974 \pm 0.006$** | $0.969 \pm 0.011$ | $0.961 \pm 0.011$ |
| blood-transfusion | $0.742 \pm 0.012$ | **$0.750 \pm 0.029$** | $0.749 \pm 0.022$ | $0.747 \pm 0.023$ |
| car | $0.995 \pm 0.003$ | **$1.000 \pm 0.000$** | $0.999 \pm 0.001$ | $0.997 \pm 0.005$ |
| cmc | $0.528 \pm 0.029$ | $0.534 \pm 0.016$ | **$0.538 \pm 0.016$** | $0.534 \pm 0.024$ |
| credit-g | $0.751 \pm 0.019$ | **$0.775 \pm 0.022$** | $0.764 \pm 0.028$ | $0.755 \pm 0.012$ |
| eucalyptus | $0.655 \pm 0.024$ | **$0.678 \pm 0.028$** | $0.670 \pm 0.022$ | $0.659 \pm 0.032$ |
| heart | $0.858 \pm 0.013$ | **$0.863 \pm 0.023$** | $0.857 \pm 0.016$ | $0.847 \pm 0.012$ |
| pc1 | $0.931 \pm 0.004$ | $0.934 \pm 0.004$ | **$0.935 \pm 0.008$** | $0.934 \pm 0.009$ |
| vehicle | $0.754 \pm 0.016$ | **$0.770 \pm 0.020$** | $0.761 \pm 0.027$ | $0.766 \pm 0.026$ |
| **Hồi quy (RMSE $\downarrow$)** | | | | |
| bike [101] | $4.094 \pm 0.096$ | $4.027 \pm 0.322$ | **$3.928 \pm 0.186$** | $3.960 \pm 0.119$ |
| crab [100] | $2.325 \pm 0.094$ | $2.262 \pm 0.203$ | **$2.193 \pm 0.132$** | $2.273 \pm 0.154$ |
| housing [104] | $4.845 \pm 0.191$ | $4.813 \pm 0.344$ | **$4.430 \pm 0.126$** | $4.769 \pm 0.393$ |
| insurance [103] | $5.269 \pm 0.260$ | $5.108 \pm 0.296$ | **$5.100 \pm 0.351$** | $5.351 \pm 0.776$ |
| wine [100] | $0.639 \pm 0.006$ | **$0.610 \pm 0.004$** | $0.616 \pm 0.006$ | $0.633 \pm 0.005$ |

#### Cải thiện Hiệu năng trên CatBoost và Hồi quy Logistic (Bảng 12)

- **Mở rộng sang các mô hình dự đoán kích thước nhỏ và đơn giản**:
  - Bên cạnh các mô hình phức tạp như XGBoost, MLP và TabPFN, nghiên cứu đánh giá thêm tính hiệu quả của LLM-FE trên:
    - **Hồi quy Logistic (Logistic Regression)**: Mô hình tuyến tính cơ bản, đại diện cho lớp thuật toán đơn giản, có khả năng diễn giải cao nhưng giới hạn trong việc nắm bắt tương tác phi tuyến.
    - **CatBoost**: Mô hình tăng cường gradient dựa trên cây quyết định đối xứng (symmetric/oblivious decision trees), được thiết kế tối ưu hóa mạnh mẽ cho dữ liệu phân loại.
  - Thử nghiệm được thực hiện trên 9 tập dữ liệu phân loại, báo cáo Accuracy trung bình và độ lệch chuẩn ($\text{mean} \pm \text{std}$) qua 5 lần chia dữ liệu.

- **Tác động của LLM-FE đối với Hồi quy Logistic (Logistic Regression)**:
  - Các đặc trưng mới được sinh bởi LLM-FE giúp mở rộng không gian biểu diễn cho mô hình tuyến tính, biến đổi các quan hệ phi tuyến trong dữ liệu gốc thành các dạng biểu diễn phân tách tuyến tính thuận lợi hơn.
  - Cải thiện độ chính xác rõ rệt trên các tập dữ liệu:
    - *breast-w*: tăng từ $0.955 \pm 0.014$ lên $0.962 \pm 0.008$.
    - *credit-g*: tăng từ $0.764 \pm 0.006$ lên $0.780 \pm 0.015$.
    - *cmc*: tăng từ $0.520 \pm 0.019$ lên $0.525 \pm 0.012$.
    - *car*: tăng từ $0.690 \pm 0.017$ lên $0.696 \pm 0.031$.
    - *pc1*: tăng từ $0.931 \pm 0.003$ lên $0.935 \pm 0.003$.
  - Duy trì hiệu năng ổn định trên *blood-transfusion* ($0.799 \pm 0.014$ so với $0.799 \pm 0.009$).
  - Có sự suy giảm không đáng kể trên *eucalyptus* ($0.671 \pm 0.036$ xuống $0.667 \pm 0.042$), *heart* ($0.877 \pm 0.021$ xuống $0.872 \pm 0.025$), và *vehicle* ($0.772 \pm 0.028$ xuống $0.769 \pm 0.015$).

- **Tác động của LLM-FE đối với CatBoost**:
  - LLM-FE mang lại mức cải thiện đáng kể trên các tập dữ liệu có cấu trúc khó:
    - *eucalyptus*: tăng vượt bậc từ $0.436 \pm 0.027$ lên $0.509 \pm 0.050$ (tăng $+0.073$).
    - *cmc*: tăng từ $0.518 \pm 0.028$ lên $0.548 \pm 0.027$ (tăng $+0.030$).
    - *blood-transfusion*: tăng từ $0.742 \pm 0.012$ lên $0.751 \pm 0.036$.
    - *breast-w*: tăng từ $0.957 \pm 0.009$ lên $0.962 \pm 0.008$.
    - *pc1*: tăng từ $0.929 \pm 0.005$ lên $0.932 \pm 0.012$.
    - *vehicle*: tăng từ $0.719 \pm 0.045$ lên $0.725 \pm 0.033$.
    - *car*: duy trì mức độ chính xác gần như hoàn hảo $0.999 \pm 0.001$.
  - Biến động giảm nhẹ trên hai tập: *credit-g* ($0.714 \pm 0.046$ xuống $0.700 \pm 0.021$) và *heart* ($0.845 \pm 0.015$ xuống $0.839 \pm 0.018$).

| Dataset | Logistic Regression (Base) | Logistic Regression (LLM-FE) | CatBoost (Base) | CatBoost (LLM-FE) |
| :--- | :--- | :--- | :--- | :--- |
| breast-w | $0.955 \pm 0.014$ | **$0.962 \pm 0.008$** | $0.957 \pm 0.009$ | **$0.962 \pm 0.008$** |
| blood-transfusion | **$0.799 \pm 0.014$** | **$0.799 \pm 0.009$** | $0.742 \pm 0.012$ | $0.751 \pm 0.036$ |
| car | $0.690 \pm 0.017$ | $0.696 \pm 0.031$ | **$0.999 \pm 0.001$** | **$0.999 \pm 0.001$** |
| cmc | $0.520 \pm 0.019$ | $0.525 \pm 0.012$ | $0.518 \pm 0.028$ | **$0.548 \pm 0.027$** |
| credit-g | $0.764 \pm 0.006$ | **$0.780 \pm 0.015$** | $0.714 \pm 0.046$ | $0.700 \pm 0.021$ |
| eucalyptus | **$0.671 \pm 0.036$** | $0.667 \pm 0.042$ | $0.436 \pm 0.027$ | $0.509 \pm 0.050$ |
| heart | **$0.877 \pm 0.021$** | $0.872 \pm 0.025$ | $0.845 \pm 0.015$ | $0.839 \pm 0.018$ |
| pc1 | $0.931 \pm 0.003$ | **$0.935 \pm 0.003$** | $0.929 \pm 0.005$ | $0.932 \pm 0.012$ |
| vehicle | **$0.772 \pm 0.028$** | $0.769 \pm 0.015$ | $0.719 \pm 0.045$ | $0.725 \pm 0.033$ |
