#### 2.2.1. Binary classification: nitrification process evaluation

- Dự đoán trạng thái nitrat hóa (nitrification status) đòi hỏi xác định mối quan hệ định lượng giữa nồng độ các dạng nitơ trong bể phản ứng (reactor): $\mathrm{NO_3^--N}$, $\mathrm{NO_2^--N}$ và $\mathrm{NH_4^+-N}$.
  - Trong quá trình đồng thời nitrat hóa và khử nitrat (simultaneous nitrification and denitrification - SND) bên trong MBR, nồng độ $\mathrm{NO_3^--N}$ thường cao hơn nồng độ $\mathrm{NO_2^--N}$ và $\mathrm{NH_4^+-N}$ khi điều kiện sục khí đầy đủ (sufficient aeration).
  - Tỷ lệ nồng độ $\mathrm{NO_3^--N}$ duy trì ở mức cao là nhân tố then chốt cho quá trình chuyển hóa và loại bỏ nitơ hiệu quả (Huang et al., 2022; Paetkau and Cicek, 2011).
- Điều kiện nitrat hóa đầy đủ (sufficient nitrification) được định nghĩa là trạng thái trong đó nồng độ $\mathrm{NO_3^--N}$ vượt quá tổng nồng độ của $\mathrm{NO_2^--N}$ và $\mathrm{NH_4^+-N}$.
  - Tiêu chí định lượng của trạng thái nitrat hóa đầy đủ được biểu diễn bằng bất đẳng thức: $[\mathrm{NO_3^--N}] > [\mathrm{NO_2^--N}] + [\mathrm{NH_4^+-N}]$.
  - Trạng thái đáp ứng điều kiện $[\mathrm{NO_3^--N}] > [\mathrm{NO_2^--N}] + [\mathrm{NH_4^+-N}]$ được gán nhãn dương tính ("Positive").
  - Trạng thái không đáp ứng điều kiện trên ($[\mathrm{NO_3^--N}] \le [\mathrm{NO_2^--N}] + [\mathrm{NH_4^+-N}]$) được gán nhãn âm tính ("Negative"), tương ứng với mức nitrat hóa không đủ (insufficient).
- Mục tiêu chính của mô hình dữ liệu (data-driven model) cho dự đoán quá trình xử lý là phân loại nhị phân (binary classification) xem quá trình nitrat hóa đạt mức đầy đủ hay không đủ.
  - Phân loại nhị phân đóng vai trò định nghĩa biến mục tiêu đầu ra cho các thuật toán học máy trong toàn bộ nghiên cứu.
- Quy trình phát triển mô hình dữ liệu giám sát nitrat hóa trong MBR được thiết lập có hệ thống từ phân loại nhị phân đến đánh giá và điều khiển.
  - **Hình 2.** Lưu đồ phát triển và đánh giá mô hình dữ liệu
    - <img src="assets/fig_02_p3.jpeg" alt="Hình 2" />
    - **Hình này chứng minh điều gì**
      - Khung làm việc mô hình hóa phân loại trạng thái nitrat hóa từ dữ liệu thô đến kiểm thử và phân tích tầm quan trọng đặc trưng.
    - **Từ đâu mà thấy được**
      - Dòng xử lý từ trên xuống bắt đầu từ Raw data (Sec 2.1) qua Binary classification (Sec 2.2.1), Data preprocessing (Sec 2.2.3) đến Data-splitting strategy (Sec 2.2.4).
      - Dữ liệu phân tách thành nhóm Training & validation ($80\,\%$) và hai nhóm kiểm thử: Test group không biocarrier ($20\,\%$, Sec 3.3) cùng Further test bổ sung biocarrier (Sec 3.4).
      - Ba thuật toán (Logistic regression, Random forest, Extreme gradient boosting) được hiệu chuẩn với tiêu chí độ chính xác cao nhất (Sec 2.2.7) trước khi đưa vào Model testing.
