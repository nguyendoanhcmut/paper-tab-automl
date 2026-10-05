### 3.2 Correlation Analysis of Model Variables

- **Phân tích ma trận tương quan giữa các thông số hệ thống**:
  - Hệ số tương quan Pearson giữa pH đầu vào và hiệu suất loại bỏ COD đạt $r = 0.68$, thể hiện tính kiềm đóng vai trò ổn định nồng độ VFA.
  - Nồng độ $2,4\text{-DCP}$ tương quan nghịch vừa phải ($r = -0.52$) với tốc độ loại bỏ COD do độc tính ức chế enzyme.
  - Tương quan giữa COD đầu vào và hiệu suất loại bỏ COD có giá trị dương nhẹ ($r = 0.34$), phản ánh tải lượng cơ chất dồi dào kích thích sinh trưởng vi sinh.
  - Độ đục đầu vào và tổng chất rắn lơ lửng ($TSS$) có tương quan thuận cao ($r = 0.81$), khẳng định tính đồng nhất của nguồn nước thải tổng hợp.
  - Thời gian vận hành ($Time$) có tương quan dương nhẹ với độ ổn định ($r = 0.22$), chứng minh sinh khối có khả năng thích nghi tích lũy theo thời gian.
  - Ma trận tương quan bộc lộ tính độc lập tương đối giữa OLR và pH đầu vào ($r = -0.12$), cho phép mô hình học máy phân tách ảnh hưởng riêng biệt của từng biến.
  - Nồng độ COD đầu vào và tải lượng hữu cơ OLR có mối tương quan tuyến tính rất chặt chẽ ($r = 0.89$), phản ánh lưu lượng cấp liệu được giữ ổn định.
  - Mối tương quan nghịch giữa nồng độ $2,4\text{-DCP}$ và hiệu suất sinh khí methane ($r = -0.61$) khẳng định tác động ức chế trực tiếp lên quá trình methan hóa.
  - Độ đục đầu vào hầu như không có tương quan tuyến tính với hiệu suất loại bỏ COD ($r = 0.05$), đóng vai trò biến kiểm soát nhiễu nền.
  - Thời gian vận hành tương quan nghịch nhẹ với áp suất xuyên màng ban đầu ($r = -0.28$) do quá trình tích lũy bùn trên màng diễn ra từ từ.
  - **Hình 8.** Bản đồ nhiệt tương quan Pearson giữa các biến
    - <img src="assets/fig_08_p10.jpeg" alt="Hình 8" />
    - **Hình này chứng minh điều gì**
      - Xác định mức độ liên kết tuyến tính giữa 6 biến đầu vào và biến mục tiêu đầu ra.
    - **Từ đâu mà thấy được**
      - Ma trận các ô màu: pH và OLR có hệ số dương đậm với COD removal, trong khi 2,4-DCP và thời gian mang giá trị âm.
