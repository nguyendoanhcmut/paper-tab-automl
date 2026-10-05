### 4.2 Rationality and practicality of key water quality indicators screening

#### 4.2.1 A cost-effective nationwide indicator set

- **Giải pháp tối ưu hóa chi phí cho hệ thống quan trắc quốc gia**:
  - Tiêu chuẩn quốc gia GB3838-2002 yêu cầu quan trắc đến $24$ chỉ tiêu cơ bản, gây áp lực tài chính và kỹ thuật rất lớn cho việc vận hành thực địa.
  - Phân tích SHAP xác định bộ ba chỉ số ($\text{COD}_{\text{Mn}}$, $\text{TP}$, $\text{DO}$) nắm giữ phần lớn thông tin cần thiết, đạt Weighted $\text{F1} = 0.9205 \pm 0.0097$.
- **Hiệu năng cao hơn quy tắc đánh giá đơn nhân tố truyền thống (Rule-Based Baseline)**:
  - So sánh trực tiếp giữa Auto-sklearn và quy tắc đơn nhân tố cứng nhắc trên cùng tập $3$ chỉ số (Bảng 3).
  - Auto-sklearn đạt điểm Weighted $\text{F1}$ cao hơn có ý nghĩa thống kê ($0.9205 \pm 0.0097$ so với $0.8976 \pm 0.0038$).
  - Năng lực phân loại chính xác hơn trên toàn bộ các cấp nước, đặc biệt đối với Cấp kém V ($\text{WV}$) khi điểm F1 đạt $0.8285$ so với $0.6968$ của quy tắc chuẩn (mức cải thiện tương đối $18.9\%$).
  - Khả năng mô hình hóa các tương tác phi tuyến phức tạp giúp mô hình thông minh nhận diện chính xác các nguồn nước ô nhiễm nặng mà quy tắc cứng nhắc bỏ sót.
- **Giá trị kinh tế và khả năng nhân rộng tại các nước đang phát triển**:
  - Việc thu gọn mạng lưới quan trắc về $3$ chỉ tiêu then chốt giúp cắt giảm đáng kể chi phí đầu tư thiết bị và hóa chất phân tích trong phòng thí nghiệm.
  - Phương pháp tinh giản này mở ra khả năng triển khai hệ thống giám sát tự động rộng khắp tại các vùng có nguồn lực hạn chế.

#### 4.2.2 Regional heterogeneity

- **Nguyên nhân phân hóa áp lực ô nhiễm giữa các lưu vực**:
  - Tại hai lưu vực phía Bắc (Tùng Liêu và Hoàng Hà), chỉ số amoni ($\text{NH}_3\text{-N}$) thay thế oxy hòa tan ($\text{DO}$) do tải lượng ô nhiễm nitơ nhân sinh đặc biệt nghiêm trọng.
  - Lưu vực Tùng Liêu ghi nhận lượng phát thải nitơ nhân sinh ròng (NANI) lên tới $9453\text{ kg N km}^{-2}\text{ yr}^{-1}$, cao hơn nhiều so với các lưu vực phía Nam.
  - Lưu vực Hoàng Hà chịu áp lực ô nhiễm nguồn phân tán nông nghiệp nặng nề nhất Trung Quốc, đóng góp tới $42.67\%$ tổng lượng phát thải tổng nitơ ($\text{TN}$) nông nghiệp toàn quốc.
- **Cơ chế thủy văn 'tải lượng cao, dòng chảy thấp' (High load, low flow)**:
  - Dòng chảy mặt hàng năm của sông Liêu Hà ($36.7\text{ km}^3$) và sông Hoàng Hà ($52.1\text{ km}^3$) thấp hơn một bậc độ lớn so với sông Trường Giang và Châu Giang (đều vượt quá $300\text{ km}^3$).
  - Sông Hoàng Hà phải tưới tiêu cho $13\%$ diện tích đất canh tác cả nước nhưng chỉ chiếm $3\%$ tổng lượng dòng chảy sông ngòi quốc gia.
  - Nguồn nước hạn chế khiến chất ô nhiễm nitơ bị cô đặc với nồng độ cực cao mà không có đủ dung tích pha loãng như các dòng sông phía Nam.
  - Nồng độ chất ô nhiễm nguyên phát như $\text{NH}_3\text{-N}$ phản ánh sự suy thoái nguồn nước nhạy bén và trực tiếp hơn so với các phản ứng sinh thái thứ cấp như $\text{DO}$.
