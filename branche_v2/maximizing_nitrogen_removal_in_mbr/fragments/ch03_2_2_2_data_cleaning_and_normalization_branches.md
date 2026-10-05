### 2.2 Data cleaning and normalization

- Quy trình làm sạch dữ liệu và tiền xử lý thu được tập dữ liệu chuẩn mực
  - Tổng số mẫu quan sát hợp lệ sau khi sàng lọc đạt $2.191$ điểm dữ liệu cho phân tích học máy.
  - Các lỗi định dạng chuỗi số, dấu phẩy và khoảng trắng thừa được loại bỏ để chuyển đổi sang định dạng số thực.
  - Các giá trị khuyết thiếu được xử lý bằng thuật toán điền giá trị trung bình qua hàm SimpleImputer nhằm bảo toàn tính nhất quán thống kê.
- Chuẩn hóa đặc trưng bằng kỹ thuật thang đo độ lệch chuẩn (StandardScaler)
  - Biến đổi toàn bộ các biến đầu vào về phân phối có giá trị trung bình bằng 0 và phương sai bằng 1 ($\mu = 0, \sigma^2 = 1$).
  - Loại bỏ ảnh hưởng do sự chênh lệch lớn về đơn vị đo lường và thang đo giữa các biến vận hành khác nhau.
- Cơ sở khoa học trong việc lựa chọn $18$ biến đặc trưng vận hành
  - Nhiệt độ tại ba vùng kỵ khí, thiếu khí và hiếu khí phản ánh chính xác sự suy giảm hoạt tính nitrat hóa theo mùa trong mùa đông.
  - Thế oxy hóa - khử ($\text{ORP}$) và oxy hòa tan ($\text{DO}$) tại các phân vùng định lượng trạng thái redox quyết định hiệu suất khử nitrat và chuyển hóa của vi khuẩn $\text{PAO}$.
  - Nồng độ chất rắn lơ lửng dễ bay hơi ($\text{MLVSS}$) kết hợp với $\text{MLSS}$ giúp phân định sinh khối vi sinh vật hoạt tính với cặn trơ vô cơ.
  - Chỉ số thể tích bùn ($\text{SVI}$) theo dõi đặc tính lắng của bùn nhằm kiểm soát rủi ro thất thoát sinh khối qua màng.
  - Lưu lượng bùn tuần hoàn ($\text{Sludge-R}$) kiểm soát trực tiếp lượng nitrat hồi lưu về ngăn thiếu khí cho phản ứng khử nitrat.
  - Tập đặc trưng phản ánh đúng cơ chế động học sinh hóa của trạm xử lý, tạo nền tảng vững chắc cho phân tích giải thích bằng $\text{SHAP}$.
