### 4.3 LLM-FE Configuration

- **Mô hình ngôn ngữ lớn nền tảng (Backbone LLMs)**:
  - Các thử nghiệm sử dụng GPT-3.5-Turbo và Llama-3.1-8B-Instruct làm backbone LLMs (mô hình ngôn ngữ lớn nền tảng).
- **Cấu hình siêu tham số tìm kiếm tiến hóa (Evolutionary search hyperparameters)**:
  - **Nhiệt độ lấy mẫu (Sampling temperature)**: Thiết lập ở mức $t = 0.8$ nhằm kích thích tính khám phá (exploration) các giả thuyết đặc trưng đa dạng và phong phú.
  - **Mô hình đa đảo (Island-based evolutionary model)**: Vận hành với $m = 3$ islands (đảo tiến hóa độc lập) để quản lý các quần thể chương trình song song, hạn chế tối đa hội tụ cục bộ (local convergence).
  - **Số lượng chương trình sinh mỗi vòng lặp (Batch size per iteration)**: Tại mỗi iteration (vòng lặp), LLM sinh $b = 3$ feature transformation programs (chương trình biến đổi đặc trưng) cho mỗi prompt bằng mã nguồn Python.
- **Ngân sách thực thi và tính nhất quán đối chuẩn (Sampling budget consistency)**:
  - Để đảm bảo tính so sánh công bằng và nhất quán tuyệt đối với các baseline (fair comparison), LLM-FE được cấu hình với ngân sách cố định là $20$ mẫu sinh LLM ($20$ LLM samples) cho mỗi thực nghiệm.
- **Chiến lược tuyển chọn giải pháp tối ưu (Final program selection)**:
  - Lấy mẫu top $m$ (với $m$ là số lượng đảo, $m = 3$) feature discovery programs (chương trình khám phá đặc trưng) đạt điểm số cao nhất dựa trên validation scores (điểm đánh giá trên tập kiểm định) tương ứng của chúng.
- **Tài liệu tham khảo chi tiết triển khai**:
  - Appendix B.1 cung cấp chi tiết toàn diện về các thiết lập tham số, mẫu prompt, và giao thức thực thi bổ sung.

#### Hiệu năng trên các tập dữ liệu phân loại (Classification Datasets - Table 2)

- **Mô tả thiết lập và quy ước thực nghiệm (Experimental setup & conventions)**:
  - Đánh giá hiệu năng của mô hình XGBoost khi kết hợp với các phương pháp Feature Engineering (FE - kỹ thuật đặc trưng) khác nhau trên $19$ classification datasets (tập dữ liệu phân loại).
  - **Thước đo đánh giá**: Độ chính xác (Accuracy, giá trị càng cao thể hiện hiệu năng càng tốt). Báo cáo giá trị trung bình (mean) và độ lệch chuẩn (standard deviation) qua $5$ phân chia ngẫu nhiên (five splits).
  - **Quy ước ký hiệu**:
    - `✗`: Thời gian thực thi vượt quá $12$ giờ (đối với classical FE methods) hoặc thất bại do lỗi thực thi chương trình (đối với LLM-based FE methods).
    - **In đậm (bold)**: Chỉ ra phương pháp đạt hiệu năng tốt nhất (best performance).
    - <u>Gạch chân (underline)</u>: Chỉ ra phương pháp đạt hiệu năng tốt thứ hai (second-best performance).
    - $n$: Số lượng mẫu dữ liệu (number of samples).
    - $p$: Số lượng đặc trưng ban đầu (number of features).
  - **Các nhóm phương pháp so sánh**:
    - *Base*: XGBoost huấn luyện trực tiếp trên tập dữ liệu gốc (raw data).
    - *Classical FE Methods (Phương pháp FE cổ điển)*: AutoFeat và OpenFE.
    - *LLM-based FE Methods (Phương pháp FE dựa trên LLM)*: CAAFE, FeatLLM, và OCTree.
    - *LLM-FE*: Khung làm việc tìm kiếm chương trình tiến hóa đề xuất.

| Dataset | $n$ | $p$ | Base | Classical FE Methods: AutoFeat | Classical FE Methods: OpenFE | LLM-based FE Methods: CAAFE | LLM-based FE Methods: FeatLLM | LLM-based FE Methods: OCTree | LLM-FE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| adult | 48.8k | 14 | 0.873 ± 0.002 | ✗ | <u>0.873 ± 0.002</u> | 0.872 ± 0.002 | 0.842 ± 0.003 | 0.870 ± 0.002 | **0.874 ± 0.003** |
| arrhythmia | 452 | 279 | 0.657 ± 0.019 | ✗ | ✗ | ✗ | ✗ | ✗ | **0.659 ± 0.018** |
| balance-scale | 625 | 4 | 0.856 ± 0.020 | 0.925 ± 0.036 | <u>0.986 ± 0.009</u> | 0.966 ± 0.029 | 0.800 ± 0.037 | 0.882 ± 0.022 | **0.990 ± 0.013** |
| bank-marketing | 45.2k | 16 | 0.906 ± 0.003 | ✗ | 0.906 ± 0.002 | **0.907 ± 0.002** | **0.907 ± 0.002** | 0.900 ± 0.002 | **0.907 ± 0.002** |
| breast-w | 699 | 9 | 0.956 ± 0.012 | 0.956 ± 0.019 | 0.956 ± 0.014 | 0.960 ± 0.009 | 0.967 ± 0.015 | <u>0.969 ± 0.009</u> | **0.970 ± 0.009** |
| blood-transfusion | 748 | 4 | 0.742 ± 0.012 | 0.738 ± 0.014 | 0.747 ± 0.025 | 0.749 ± 0.017 | **0.771 ± 0.016** | <u>0.755 ± 0.026</u> | 0.751 ± 0.036 |
| car | 1728 | 6 | 0.995 ± 0.003 | <u>0.998 ± 0.003</u> | <u>0.998 ± 0.003</u> | **0.999 ± 0.001** | 0.808 ± 0.037 | 0.995 ± 0.004 | **0.999 ± 0.001** |
| cdc diabetes | 253k | 21 | 0.849 ± 0.001 | ✗ | 0.849 ± 0.001 | 0.849 ± 0.001 | 0.849 ± 0.001 | 0.849 ± 0.001 | **0.849 ± 0.001** |
| cmc | 1473 | 9 | 0.528 ± 0.029 | 0.505 ± 0.015 | 0.517 ± 0.007 | 0.524 ± 0.016 | 0.479 ± 0.015 | 0.525 ± 0.027 | **0.531 ± 0.019** |
| communities | 1.9k | 103 | 0.706 ± 0.016 | ✗ | 0.704 ± 0.009 | 0.707 ± 0.013 | 0.593 ± 0.012 | <u>0.708 ± 0.016</u> | **0.711 ± 0.012** |
| covtype | 581k | 54 | 0.870 ± 0.001 | ✗ | **0.885 ± 0.007** | 0.872 ± 0.003 | 0.554 ± 0.001 | 0.832 ± 0.002 | <u>0.882 ± 0.003</u> |
| credit-g | 1000 | 20 | 0.751 ± 0.019 | 0.757 ± 0.017 | <u>0.758 ± 0.017</u> | 0.751 ± 0.020 | 0.707 ± 0.034 | 0.753 ± 0.021 | **0.766 ± 0.015** |
| eucalyptus | 736 | 19 | 0.655 ± 0.024 | 0.664 ± 0.028 | 0.663 ± 0.033 | **0.679 ± 0.024** | ✗ | 0.658 ± 0.041 | <u>0.668 ± 0.027</u> |
| heart | 918 | 11 | 0.858 ± 0.013 | 0.857 ± 0.021 | 0.854 ± 0.020 | 0.849 ± 0.023 | <u>0.865 ± 0.030</u> | 0.852 ± 0.022 | **0.866 ± 0.021** |
| jungle_chess | 44.8k | 6 | 0.869 ± 0.001 | ✗ | 0.900 ± 0.004 | <u>0.901 ± 0.038</u> | 0.577 ± 0.002 | 0.869 ± 0.002 | **0.969 ± 0.004** |
| myocardial | 1.7k | 111 | 0.784 ± 0.023 | ✗ | 0.787 ± 0.026 | **0.789 ± 0.023** | 0.778 ± 0.023 | 0.787 ± 0.031 | **0.789 ± 0.023** |
| pc1 | 1109 | 21 | 0.931 ± 0.004 | 0.931 ± 0.014 | 0.931 ± 0.009 | 0.929 ± 0.005 | 0.933 ± 0.007 | <u>0.934 ± 0.007</u> | **0.935 ± 0.006** |
| tic-tac-toe | 958 | 9 | 0.998 ± 0.002 | **1.000 ± 0.000** | 0.994 ± 0.006 | 0.996 ± 0.003 | 0.653 ± 0.037 | 0.997 ± 0.003 | <u>0.998 ± 0.005</u> |
| vehicle | 846 | 18 | 0.754 ± 0.016 | **0.788 ± 0.018** | <u>0.785 ± 0.008</u> | 0.771 ± 0.019 | 0.744 ± 0.035 | 0.753 ± 0.036 | 0.769 ± 0.013 |
| **Mean Rank** | — | — | 3.95 | 5.11 | 3.63 | 3.47 | 5.11 | 4.05 | **1.42** |

- **Các quan sát then chốt từ Bảng 2**:
  - **Thứ hạng vượt trội**: LLM-FE đạt Mean Rank là $1.42$, vượt trội rõ rệt so với toàn bộ các baselines (CAAFE $3.47$, OpenFE $3.63$, Base $3.95$, OCTree $4.05$, AutoFeat $5.11$, FeatLLM $5.11$).
  - **Tính bền vững trên dữ liệu phức tạp**: Trên tập dữ liệu `arrhythmia` ($n = 452, p = 279$), tất cả $5$ phương pháp đối chuẩn đều gặp lỗi hoặc vượt quá giới hạn thời gian (`✗`), trong khi LLM-FE là phương pháp duy nhất hoàn thành thành công và nâng cao độ chính xác ($0.659 \pm 0.018$ so với Base $0.657 \pm 0.019$).
  - **Hạn chế về chi phí thời gian của phương pháp cổ điển**: AutoFeat bị quá thời gian giới hạn $12$ giờ trên $7$ tập dữ liệu có quy mô mẫu lớn hoặc số chiều cao (`adult`, `arrhythmia`, `bank-marketing`, `cdc diabetes`, `communities`, `covtype`, `jungle_chess`, `myocardial`).

#### Hiệu năng trên các tập dữ liệu hồi quy (Regression Datasets - Table 3)

- **Mô tả thiết lập và quy ước thực nghiệm (Experimental setup & conventions)**:
  - Đánh giá hiệu năng của XGBoost với các phương pháp FE trên $10$ regression datasets (tập dữ liệu hồi quy).
  - **Thước đo đánh giá**: RMSE (Root Mean Squared Error - Sai số toàn phương trung bình, giá trị càng thấp thể hiện hiệu năng càng tốt). Báo cáo mean và standard deviation qua $5$ phân chia ngẫu nhiên (five splits).
  - **Ký hiệu**: **In đậm (bold)** thể hiện hiệu năng tốt nhất; <u>Gạch chân (underline)</u> thể hiện hiệu năng tốt thứ hai; $n$ là số mẫu; $p$ là số đặc trưng.
  - **Các nhóm phương pháp so sánh**:
    - *Base*: XGBoost trên dữ liệu gốc.
    - *Classical FE Methods*: AutoFeat và OpenFE.
    - *LLM-based FE Methods*: Base LLM và OCTree (CAAFE và FeatLLM không hỗ trợ bài toán hồi quy trong mã nguồn công khai).
    - *LLM-FE*: Khung làm việc đề xuất.

| Dataset | $n$ | $p$ | Base | Classical FE Methods: AutoFeat | Classical FE Methods: OpenFE | LLM-based FE Methods: Base LLM | LLM-based FE Methods: OCTree | LLM-FE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| airfoil_self_noise [100] | 1503 | 6 | 1.572 ± 0.084 | 1.531 ± 0.118 | 1.631 ± 0.111 | <u>1.507 ± 0.150</u> | 1.572 ± 0.079 | **1.451 ± 0.059** |
| bike [101] | 17389 | 11 | 4.094 ± 0.096 | 4.222 ± 0.123 | <u>4.089 ± 0.140</u> | 4.149 ± 0.101 | 4.094 ± 0.096 | **3.985 ± 0.084** |
| cpu_small [100] | 8192 | 10 | 2.857 ± 0.223 | 2.896 ± 0.197 | 2.822 ± 0.190 | <u>2.798 ± 0.226</u> | 2.832 ± 0.192 | **2.733 ± 0.249** |
| crab [100] | 3893 | 8 | 2.325 ± 0.094 | 2.266 ± 0.078 | <u>2.221 ± 0.010</u> | 2.309 ± 0.135 | 2.280 ± 0.087 | **2.211 ± 0.124** |
| diamond [102] | 53940 | 9 | 5.479 ± 0.063 | 5.521 ± 0.143 | <u>5.384 ± 0.084</u> | 5.422 ± 0.075 | 5.479 ± 0.063 | **5.356 ± 0.134** |
| forest-fires [101] | 517 | 13 | 0.163 ± 0.009 | 0.163 ± 0.010 | <u>0.161 ± 0.013</u> | 0.165 ± 0.018 | 0.162 ± 0.007 | **0.156 ± 0.008** |
| housing [104] | 20640 | 9 | 4.845 ± 0.191 | 4.776 ± 0.271 | <u>4.628 ± 0.105</u> | 4.961 ± 0.457 | 4.845 ± 0.191 | **4.525 ± 0.260** |
| insurance [103] | 1338 | 7 | 5.269 ± 0.260 | 5.098 ± 0.323 | 5.085 ± 0.286 | 5.112 ± 0.362 | **4.969 ± 0.331** | <u>5.069 ± 0.392</u> |
| plasma_retinol [102] | 315 | 13 | <u>2.352 ± 0.196</u> | 2.478 ± 0.217 | 2.363 ± 0.195 | 2.384 ± 0.200 | 2.362 ± 0.204 | **2.278 ± 0.248** |
| wine [100] | 4898 | 10 | 0.639 ± 0.006 | 0.633 ± 0.007 | <u>0.631 ± 0.009</u> | 0.639 ± 0.009 | 0.639 ± 0.006 | **0.612 ± 0.007** |
| **Mean Rank** | — | — | 4.55 | 4.45 | <u>2.80</u> | 4.40 | 3.70 | **1.10** |

- **Các quan sát then chốt từ Bảng 3**:
  - **Thứ hạng trung bình dẫn đầu áp đảo**: LLM-FE đạt Mean Rank là $1.10$, vượt trội hơn tất cả các đối chuẩn (OpenFE $2.80$, OCTree $3.70$, Base LLM $4.40$, AutoFeat $4.45$, Base $4.55$).
  - **Tỷ lệ chiến thắng vượt bậc**: LLM-FE đạt hiệu năng tốt nhất (bold) trên $9/10$ tập dữ liệu hồi quy và đạt vị trí thứ hai (underline) trên tập còn lại (`insurance`).
