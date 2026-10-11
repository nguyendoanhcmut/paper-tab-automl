### RSM description

* **Khái niệm và mục tiêu của phương pháp bề mặt đáp ứng (Response Surface Methodology - RSM)**:
    * **Định nghĩa**: RSM là một tập hợp các phương pháp toán học và thống kê được sử dụng để xây dựng, cải thiện và tối ưu hóa các quy trình kỹ thuật.
    * **Mục tiêu cốt lõi**: Công cụ hữu hiệu nhằm xác định các thiết lập biến đầu vào tối ưu (best input variable settings) và tối đa hóa đáp ứng (response) của quy trình hoặc sản phẩm.
    * **Phạm vi khảo sát yếu tố**: RSM có khả năng nghiên cứu đa yếu tố đồng thời (multiple factors), mặc dù trong thực tế thường tập trung phân tích tương tác giữa hai yếu tố chính.
    * **Mô hình hóa bề mặt đáp ứng**: Thông qua việc triển khai chuỗi thiết kế thực nghiệm thừa số toàn phần (full factorial Design of Experiments - DOE), RSM thiết lập bản đồ bề mặt đáp ứng và cung cấp các phương trình thực nghiệm mô tả định lượng cách thức các yếu tố đầu vào chi phối biến đáp ứng.

* **Công cụ phần mềm và tham số thiết kế Design-Expert**:
    * **Vai trò**: Design-Expert là một trong những gói phần mềm phổ biến và mạnh mẽ nhất được ứng dụng cho mô hình hóa RSM.
    * **Khả năng thiết kế linh hoạt**: Phần mềm cung cấp phạm vi tùy chọn thiết kế phong phú, xử lý linh hoạt các tham số phân loại (categorical parameters) và kết hợp hài hòa giữa các biến hỗn hợp (mixture variables) cùng biến quy trình (process variables).
    * **Quy trình ứng dụng trong thực nghiệm**: Sự kết hợp giữa RSM và Design-Expert cho phép:
        * Sàng lọc các thông số then chốt (screening essential parameters).
        * Xác định các điều kiện vận hành phù hợp (appropriate process settings).
        * Tìm kiếm công thức phối liệu tối ưu với hỗn hợp các thiết kế (formulation with a mixture of design).

* **Kiểm định thống kê qua phân tích phương sai (Analysis of Variance - ANOVA)**:
    * **Nguyên lý của ANOVA**: Là phương pháp thống kê được sử dụng để xác định sự tồn tại của những biến thiên đáng kể giữa giá trị trung bình (means) của hai hoặc nhiều nhóm dữ liệu so sánh.
    * **Chức năng trong RSM**: Đánh giá tầm quan trọng và mức độ có ý nghĩa thống kê của các biến độc lập cũng như các số hạng tương tác tác động lên biến đáp ứng.
    * **Kiểm định giả thuyết không (Null Hypothesis - $H_0$)**:
        * **Nội dung giả thuyết không**: Phát biểu rằng không có sự khác biệt đáng kể giữa các giá trị trung bình của các nhóm được so sánh.
        * **Tiêu chuẩn bác bỏ**: Nếu giả thuyết không bị chứng minh là sai (bị bác bỏ), giá trị trung bình giữa các nhóm so sánh có sự khác biệt thực chất (vary substantially), khẳng định yếu tố thực nghiệm có ảnh hưởng đáng kể đến quy trình.

* **Quy trình các bước triển khai mô hình hóa bề mặt đáp ứng (RSM Workflow)**:
    * **Bước 1 - Thiết kế yếu tố thực nghiệm**: Xác định các yếu tố đầu vào (biến độc lập), ký hiệu là $X_1, X_2, \dots, X_n$, và lựa chọn các mức giá trị (levels) phù hợp cho từng yếu tố.
    * **Bước 2 - Lập ma trận thực nghiệm**: Xây dựng ma trận thiết kế gồm tập hợp các thí nghiệm (từ thí nghiệm $1$ đến thí nghiệm $n$), trong đó mỗi lần chạy là một tổ hợp các mức yếu tố xác định.
    * **Bước 3 - Tiến hành thí nghiệm và thu thập dữ liệu**: Thực hiện các mẻ phản ứng thực nghiệm và đo đạc chính xác các biến đáp ứng đầu ra tương ứng.
    * **Bước 4 - Khớp mô hình toán học (Model Fitting)**: Khớp mô hình bề mặt đáp ứng dựa trên dữ liệu thực nghiệm bằng phân tích hồi quy (regression analysis) hoặc các kỹ thuật mô hình hóa phù hợp nhằm mô phỏng mối quan hệ $Y = f(X_1, X_2, \dots, X_n)$.
    * **Bước 5 - Tối ưu hóa điều kiện vận hành**: Sử dụng mô hình bề mặt đáp ứng để xác định mức yếu tố lý tưởng nhằm cực đại hóa hoặc cực tiểu hóa biến đáp ứng theo mục tiêu công nghệ.
    * **Bước 6 - Xác thực và kiểm định mô hình (Validation)**: Đánh giá độ chính xác và độ tin cậy của mô hình trong việc dự đoán kết quả tại các điểm dữ liệu chưa từng quan sát (unobserved data points); quy trình có thể lặp lại hoặc phân tích mở rộng tùy theo yêu cầu cụ thể.

* **Dạng phương trình hồi quy đa thức trong RSM**:
    * **Mô hình hồi quy đa thức bậc hai (Quadratic RSM model)**: Mô hình bề mặt đáp ứng bậc hai được biểu diễn tổng quát theo phương trình:
      $$Y = \beta_0 + \sum_{i=1}^{k} \beta_i X_i + \sum_{i=1}^{k} \beta_{ii} X_i^2 + \sum_{i=1}^{k} \sum_{j=1}^{k} \beta_{ij} X_i X_j + \varepsilon \quad (10)$$
        * $Y$: Biến đáp ứng phụ thuộc (response variable).
        * $X_i, X_j$: Các biến độc lập đầu vào (independent variables).
        * $\beta_0$: Hệ số chặn / hằng số tự do (intercept constant).
        * $\beta_i$: Các hệ số hồi quy tuyến tính (linear coefficients).
        * $\beta_{ii}$: Các hệ số hồi quy bậc hai thuần túy (quadratic coefficients).
        * $\beta_{ij}$: Các hệ số hồi quy tương tác tích chéo (interaction / cross-product coefficients).
        * $\varepsilon$: Số hạng sai số ngẫu nhiên (random error term).
    * **Cân nhắc cấu trúc đa thức bậc hai và bậc ba (Quadratic vs. Cubic polynomial forms)**:
        * Dạng bậc hai (quadratic) là cấu trúc chuẩn mực được lựa chọn trong nghiên cứu nhờ khả năng nắm bắt độ cong bề mặt đáp ứng và tương tác đa biến mà không đòi hỏi số lượng điểm thí nghiệm quá lớn.
        * Dạng bậc ba (cubic) hoặc bậc cao hơn trong Design-Expert thường được kiểm tra để phát hiện phi tuyến phức tạp, nhưng có nguy cơ gây quá khớp (overfitting) hoặc thiếu bậc tự do (aliasing/lack of fit) nếu không có đủ điểm thực nghiệm bổ sung.

* **Cấu hình thiết kế thực nghiệm trong nghiên cứu**:
    * **Các biến phụ thuộc (biến đáp ứng đầu ra)**: Nồng độ nitơ amoniac (ammonia nitrogen concentrations), nồng độ phosphat (phosphate concentrations) và hiệu suất loại bỏ tương ứng (removal efficiency, $\%$).
    * **Các biến độc lập (yếu tố đầu vào) và dải giá trị khảo sát**:
        * Tổng carbon hữu cơ (Total Organic Carbon - TOC): $40\text{ đến }120\text{ mg/L}$.
        * Độ pH: $6\text{ đến }9$.
        * Thời gian phản ứng (Time): $0\text{ đến }20\text{ ngày}$.
    * **Phương pháp thiết kế thực nghiệm**:
        * Nghiên cứu ứng dụng thiết kế phức hợp tâm (Central Composite Design - CCD) kết hợp với các đợt chạy Box-Behnken, tạo ra $33$ và $44$ mẻ thực nghiệm.
        * Thiết kế CCD cho phép khảo sát toàn diện tác động riêng lẻ và hiệu ứng tương hỗ đồng thời của các yếu tố (TOC, pH, thời gian) lên hiệu quả khử chất dinh dưỡng trong bể phản ứng sinh học màng vi tảo (microalgae MBR).

* **So sánh tổng quan với các nghiên cứu mô hình hóa MBR vi tảo gần đây (Table 2)**:
    * **Wang và cộng sự (2024)**: Ứng dụng mô hình MLP-ANN trên hệ thống AnMBR quy mô pilot; phân tích khả năng giải thích (interpretability investigation) xác nhận tính hiệu quả của MLP trong dự báo hiện tượng nghẽn màng ở cả phạm vi cục bộ lẫn toàn cục.
    * **Amari và cộng sự (2023)**: Khảo sát màng sinh khối vi tảo, nồng độ $\text{NO}_3^-\text{-N}$ và pH trong MBR bằng ANN, RSM và NSGA-II; xác định điều kiện tối ưu cho màng sinh khối vi tảo tại nồng độ $2.884\text{ mg/L}$ và thời gian $6.589\text{ ngày}$.
    * **Asrami và cộng sự (2022)**: Nghiên cứu MBR vi tảo xử lý nước rỉ rác bãi chôn lấp bằng ANN và NSGA-II; khẳng định năng lực tối ưu hóa hiệu quả vượt trội của thuật toán NSGA-II.
    * **Nghiên cứu hiện tại (Present work)**: Ứng dụng khung tích hợp đồng thời ANN, RSM và NSGA-II để mô hình hóa và tối ưu hóa quá trình loại bỏ chất dinh dưỡng trong MBR vi tảo; kết quả chứng minh độ chính xác vượt trội ("significant level of precision") trong mô phỏng hành vi của hệ thống sinh học vi tảo.
