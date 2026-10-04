## 4. Conclusion

- **Khả năng cung cấp thông tin vận hành từ hồ sơ dữ liệu nhà máy quy mô công nghiệp thực tế**:
  - Hồ sơ dữ liệu vận hành của hệ thống màng phản ứng sinh học ngập quy mô thực tế đầy đủ ($\text{full-scale submerged MBR}$) xử lý nước thải sản xuất chất bán dẫn chứa đầy đủ thông tin để chỉ dẫn người vận hành về trạng thái vận hành nhà máy, với điều kiện các mô hình học máy được đánh giá và ứng dụng đúng phương pháp.
  - Kết luận này được củng cố và chứng minh bằng 3 phát hiện cốt lõi.

- **Phát hiện 1 — Thời gian lưu bùn ($\text{SRT}$) là yếu tố nền tảng chi phối hành vi màng lọc**:
  - Thời gian lưu bùn ($\text{SRT}$ - sludge retention time) là yếu tố quyết định nền tảng ($\text{foundational determinant}$) đối với hành vi của màng lọc với bằng chứng thực nghiệm đạt độ bền vững cao:
    - Toàn bộ $16$ thuật toán học máy đều xếp hạng $\text{SRT}$ ở vị trí thứ nhất ($1$) về mức độ ảnh hưởng đối với áp suất xuyên màng ($\text{TMP}$ - transmembrane pressure).
    - Thứ hạng số $1$ của $\text{SRT}$ được duy trì nhất quán qua các thiết kế kiểm định ($\text{validation designs}$) ngay cả khi độ chính xác dự đoán của bản thân mô hình bị suy giảm.
    - Tỷ lệ đạt mục tiêu đo đạc thực tế ($\text{measured attainment}$) suy giảm đơn điệu từ $77\%$ tại khoảng $43\text{--}72\text{ ngày}$ xuống dưới $20\%$ khi $\text{SRT}$ vượt quá $87\text{ ngày}$.
  - Cơ chế tắc nghẽn màng đảo ngược so với các hệ thống bùn hoạt tính truyền thống:
    - Do hệ thống vận hành hoàn toàn trong chế độ sục khí kéo dài ($\text{extended-aeration range}$), cơ chế tắc nghẽn chủ đạo là sự tích tụ sinh khối ($\text{biomass accumulation}$), độ nhớt chất lỏng gia tăng ($\text{elevated viscosity}$) và hiện tượng nén chặt lớp bánh bùn ($\text{cake compaction}$).
    - Cơ chế này thay thế cho động học của các chất cao phân tử ngoại bào ($\text{EPS}$ - extracellular polymeric substances) và các sản phẩm vi sinh hòa tan ($\text{SMP}$ - soluble microbial products) thường gặp trong các hệ thống tuổi bùn ngắn truyền thống ($\text{conventional short-sludge-age systems}$).
    - Do đó, kỳ vọng truyền thống cho rằng tuổi bùn dài hơn giúp giảm nhẹ tắc nghẽn màng ($\text{mitigates fouling}$) đã bị đảo ngược trong điều kiện vận hành này.

- **Phát hiện 2 — Nhận diện các trạng thái vận hành khả thi thỏa mãn ràng buộc hiệu suất**:
  - Bài toán mà hồ sơ dữ liệu vận hành nhà máy giải quyết hiệu quả không phải là dự báo diễn biến tiếp theo của nhà máy ($\text{what the plant will do next}$), mà là nhận diện những trạng thái vận hành có thể đạt tới ($\text{attainable operating states}$) thỏa mãn các ràng buộc hiệu suất kỹ thuật ($\text{performance constraints}$).
  - Cấu trúc mặt đáp ứng trên đa tạp vận hành liên kết thực tế:
    - Khi được ánh xạ trên đa tạp vận hành liên kết thực tế ($\text{real joint operating manifold}$) và phân cấp theo tỷ lệ đạt có điều kiện ($\text{conditional attainment rate}$), mặt đáp ứng tạo thành tái hiện tỷ lệ đạt đo đạc thực tế qua $70$ phân vùng vận hành ($70\text{ operating bins}$) với hệ số tương quan đạt $0.99$.
    - Phân tích xác lập một cửa sổ vận hành ($\text{operating window}$) hẹp hơn đáng kể so với bao hình khả thi về mặt kỹ thuật thuần túy ($\text{technically feasible envelope}$).

- **Phát hiện 3 — Giá trị thực tiễn và khả năng khái quát hóa theo thời gian của cửa sổ vận hành**:
  - Cửa sổ vận hành khuyến nghị mang lại giá trị thực tiễn vượt ra ngoài khoảng thời gian thu thập dữ liệu huấn luyện:
    - Các dải biên vận hành cố định dựa trên $7\text{ tháng}$ đầu tiên giúp nâng tỷ lệ đạt mục tiêu đồng thời ($\text{simultaneous attainment}$) từ $39.3\%$ lên $61.9\%$ trong $3\text{ tháng}$ vận hành kế tiếp.
    - Khi mô hình được tái khớp hàng ngày ($\text{refitted daily}$) trên hồ sơ dữ liệu tích lũy, mô hình dự đoán $\text{TMP}$ với sai số đạt $0.008\text{ bar}$ và hệ số xác định $R^2 = 0.871$ tại thời điểm $4\text{ tháng}$ vượt ngoài dữ liệu huấn luyện ban đầu.
    - Khả năng khái quát hóa theo thời gian ($\text{temporal generalisation}$) được quyết định bởi lịch trình làm mới dữ liệu ($\text{refresh schedule}$) thay vì bắt nguồn từ bất kỳ giới hạn nội tại nào của mô hình.

- **Ý nghĩa mở rộng về tiêu chí đánh giá mô hình học máy công nghiệp**:
  - Tính tự tương quan chuỗi và hạn chế của phương pháp chia tập ngẫu nhiên:
    - Các bản ghi dữ liệu công nghiệp theo giờ có tính tự tương quan chuỗi mạnh mẽ, khiến cho độ chính xác đo lường trên các phân vùng chia ngẫu nhiên ($\text{random partitions}$) thực chất phản ánh phép nội suy ($\text{interpolation}$) giữa các giờ lân cận thay vì khả năng khái quát hóa sang các điều kiện vận hành mới.
    - Ngược lại, quy gán độ quan trọng đặc trưng ($\text{feature attributions}$) chứng minh tính ổn định bền vững qua các sơ đồ phân chia dữ liệu khác nhau.
  - Tính khả giải giữ vai trò quyết định trong thực tiễn vận hành:
    - Khả năng giải thích mô hình ($\text{interpretability}$), chứ không phải độ chính xác danh nghĩa trên đầu đề ($\text{headline accuracy}$), mới là thuộc tính thực sự vượt qua kiểm chứng khắt khe và cần mang trọng số quyết định trong công tác vận hành.
    - Đầu ra hữu ích nhất không phải là một công cụ dự báo đơn thuần ($\text{predictor}$), mà là một bản đồ phân cấp không gian vận hành ($\text{graded map of the operating space}$), trong đó mỗi khuyến nghị vận hành đều gắn liền với tần suất mà nhà máy đã đạt được các mục tiêu hiệu suất trên thực tế.
  - Chuyển dịch từ quản lý thụ động sang chủ động thông qua thử nghiệm tiến cứu:
    - Bước chuyển dịch từ quản lý màng thụ động ($\text{reactive management}$) sang quản lý màng chủ động ($\text{proactive management}$) phụ thuộc ít hơn vào việc tiếp tục gia tăng độ chính xác dự đoán, mà phụ thuộc chủ yếu vào việc kiểm chứng các chỉ dẫn vận hành dựa trên những kết quả mà nhà máy có thể xác minh được.
    - Định hướng triển khai cuối cùng đòi hỏi các thử nghiệm tiến cứu ($\text{prospective trials}$) nhằm kiểm tra xem liệu việc tuân thủ các chỉ dẫn này có tạo ra sự cải thiện tương ứng như dữ liệu thực nghiệm đã liên kết hay không.

- **Đóng góp của các tác giả theo danh mục CRediT (CRediT authorship contribution statement)**:
  - Yujae Jeon: Viết bản thảo gốc ($\text{Writing – original draft}$), Thẩm định ($\text{Validation}$), Điều tra nghiên cứu ($\text{Investigation}$), Phân tích hình thức ($\text{Formal analysis}$), Khái niệm hóa ($\text{Conceptualization}$).
  - Duc Anh Nguyen: Phương pháp luận ($\text{Methodology}$), Phân tích hình thức ($\text{Formal analysis}$).
  - Kim Anh Nguyen Thi: Phần mềm ($\text{Software}$), Điều tra nghiên cứu ($\text{Investigation}$).
  - Quoc Thai Nong: Phần mềm ($\text{Software}$), Điều tra nghiên cứu ($\text{Investigation}$).
  - Am Jang: Viết – rà soát và chỉnh sửa ($\text{Writing – review \& editing}$), Thẩm định ($\text{Validation}$), Giám sát ($\text{Supervision}$), Thu xếp tài trợ ($\text{Funding acquisition}$), Phân tích hình thức ($\text{Formal analysis}$).

- **Tuyên bố về xung đột lợi ích (Declaration of competing interest)**:
  - Các tác giả tuyên bố không có bất kỳ xung đột lợi ích tài chính ($\text{competing financial interests}$) hoặc mối quan hệ cá nhân nào được biết có thể ảnh hưởng đến kết quả nghiên cứu được báo cáo trong bài báo.

- **Lời cảm ơn và nguồn kinh phí tài trợ (Acknowledgements)**:
  - Công trình nghiên cứu được hỗ trợ bởi Viện Công nghiệp & Công nghệ Môi trường Hàn Quốc ($\text{KEITI}$ - Korea Environmental Industry & Technology Institute) thông qua Dự án Phát triển Công nghệ Khử mặn Kỹ thuật số và Thu hồi Tài nguyên Nước muối ($\text{Digital Desalination and Brine Resource Recovery Technology Development Project}$), được tài trợ bởi Bộ Khí hậu, Năng lượng và Môi trường Hàn Quốc ($\text{MCEE}$ - Korea Ministry of Climate, Energy and Environment) theo mã số hợp đồng tài trợ $\text{RS-2025-02032971}$ ($2025$, $02032971$).
