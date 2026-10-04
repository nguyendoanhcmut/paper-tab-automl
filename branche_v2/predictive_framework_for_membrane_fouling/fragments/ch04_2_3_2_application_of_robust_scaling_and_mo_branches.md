### 3.2. Application of Robust Scaling and Moving Average

#### 3.2.1. Application of Robust Scaling

- Phương pháp robust scaling được áp dụng để chuẩn hóa tập dữ liệu và giảm thiểu ảnh hưởng của các giá trị ngoại lai (outliers) trước sự hiện diện của phân phối phi chuẩn (non-normal distributions) cùng các giá trị cực trị (extreme values).
  - Robust scaling chuẩn hóa phân phối đặc trưng nhưng vẫn bảo toàn cấu trúc tương đối (relative structure) giữa các điểm dữ liệu.
  - Khác với phương pháp chuẩn hóa tiêu chuẩn (standard scaling chuẩn hóa dựa trên giá trị trung bình $\mu$ và độ lệch chuẩn $\sigma$), robust scaling căn tâm dữ liệu quanh trung vị (median) và tỷ lệ hóa theo khoảng tứ phân vị ($IQR = Q_3 - Q_1$).
  - Phép biến đổi dựa trên $IQR$ bảo đảm các biến số có phân phối đuôi dày (heavy-tailed distributions) và giá trị ngoại lai cực trị không làm ảnh hưởng bất lợi đến hiệu suất mô hình.
- Phân phối dữ liệu chuyển dịch từ mức phân tán lớn giữa các đặc trưng ban đầu sang thang đo đồng nhất với trung vị quy về $0$ sau robust scaling:
  - Tập dữ liệu ban đầu (Figure 4a) thể hiện độ biến thiên lớn giữa các đặc trưng, trong đó một số biến như nồng độ bùn hoạt tính lơ lửng ($MLSS$) có độ lớn cách biệt so với các biến khác, tiềm ẩn nguy cơ làm mô hình phân bổ trọng số không cân xứng.
  - Sau chuẩn hóa robust scaling (Figure 4b), tất cả đặc trưng được chuyển đổi về cùng thang đo với trung vị căn quanh giá trị $0$, giúp phân phối giữa các biến có tính tương đồng cao và ngăn các đặc trưng chiếm ưu thế làm sai lệch dự đoán của mô hình.
  - Các giá trị ngoại lai vẫn được bảo toàn để nhận diện nhưng mức độ ảnh hưởng của chúng giảm đáng kể, bảo đảm phương pháp mô hình hóa ổn định và có khả năng khái quát hóa (generalizability) cao hơn.
  - **Hình 4.** Phân phối đặc trưng trước (a) và sau (b) robust scaling
    - <img src="assets/fig_05_p16.png" alt="Hình 4" />
    - **Hình này chứng minh điều gì**
      - Robust scaling triệt tiêu chênh lệch độ lớn giữa $MLSS$ và các biến khác, đưa mọi phân phối về trung vị quanh $0$ trong khi vẫn giữ nguyên các giá trị ngoại lai nhận diện được.
    - **Từ đâu mà thấy được**
      - Trục hoành $Ox$: 11 đặc trưng vận hành và mục tiêu ($F/M$, $SV_{30}$, $SVI$, $MLSS$, $DO$, $pH$, $Temp.$, $Flux$, $COD\ RM$, $TMP$, $Spec.\ Flux$).
      - Panel (a) dữ liệu gốc ($0$ đến $12{,}000$): hộp $MLSS$ nằm ở mức $7{,}000$–$8{,}600$ (trung vị $\approx 8{,}000$), các biến còn lại bị ép sát đáy $0$.
      - Panel (b) sau chuẩn hóa ($-25$ đến $5$): trung vị toàn bộ 11 biến hội tụ về $0$; ngoại lai âm sâu nhất xuất hiện tại $SV_{30}$ ($< -20$) và $pH$ ($\approx -5$).
- Việc triển khai robust scaling giúp tập dữ liệu phù hợp hơn cho các ứng dụng học máy (machine learning) nhờ các phép biến đổi bất biến theo thang đo (scale-invariant transformations).
  - Phép biến đổi bất biến theo thang đo tăng cường tốc độ hội tụ (convergence) và khả năng diễn giải (interpretability) của mô hình.
  - Quá trình tiền xử lý bảo đảm độ quan trọng của đặc trưng (feature importance) phản ánh đúng các quy luật cốt lõi (underlying patterns) thay vì bị chi phối bởi chênh lệch độ lớn số học (numerical disparities), nâng cao độ vững chắc (robustness) và hiệu suất dự đoán của mô hình.

#### 3.2.2. Application of Moving Average

- Hiện tượng nghẹt màng (membrane fouling) trong các hệ thống $MBR$ diễn tiến tích lũy dần theo thời gian do sự tích tụ của các điều kiện vận hành và hoạt tính vi sinh vật (microbial activity), thay vì xảy ra tức thời.
  - Việc tích hợp các đặc trưng phụ thuộc thời gian (time-dependent features) là yêu cầu thiết yếu nhằm nắm bắt các quy luật cốt lõi trong động học nghẹt màng (fouling dynamics).
  - Dữ liệu chất lượng nước và thông số vận hành thường biểu hiện các dao động ngắn hạn do sai số đo đạc (measurement variability).
  - Việc áp dụng trung bình trượt (Moving Average - $MA$) giúp giảm thiểu nhiễu và làm nổi bật các xu hướng dài hạn, tạo lập tập dữ liệu ổn định và tin cậy hơn.
- Mô hình dự đoán cần tính đến tác động lịch sử (historical impact) của các điều kiện vận hành lên tình trạng nghẹt màng hiện tại thay vì chỉ phụ thuộc vào các phép đo tại từng thời điểm riêng lẻ (individual time-point measurements).
  - Cách tiếp cận này đóng vai trò đặc biệt cốt lõi đối với các thuật toán học máy như Gradient Boosting Machine ($GBM$) và $XGBoost$.
  - Phương pháp này được áp dụng vào Section 3.3.2 để tiền xử lý dữ liệu chuỗi thời gian (time-series data) thông qua làm mịn các dao động và nắm bắt xu hướng dài hạn, cho phép mô hình học các hiệu ứng tích lũy (cumulative effects) của điều kiện vận hành lên động học nghẹt màng.
- Cửa sổ trung bình trượt tối ưu (optimal moving average window) được xác định bằng cách đánh giá có hệ thống các chu kỳ dịch chuyển theo ngày (day-shifting periods) khác nhau cho từng đặc trưng đầu vào trong phạm vi chu kỳ $1$ tuần (one-week period).
  - Hiệu suất mô hình được so sánh đối với từng chu kỳ dựa trên hệ số xác định ($R^2$) và sai số căn bậc hai trung bình bình phương ($RMSE$).
  - Khung cửa sổ hiệu quả nhất sau đó được lựa chọn và áp dụng cho các phân tích kế tiếp trong nghiên cứu.
