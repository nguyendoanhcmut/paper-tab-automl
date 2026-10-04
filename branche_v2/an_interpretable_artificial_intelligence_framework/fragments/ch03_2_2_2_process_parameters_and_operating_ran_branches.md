### 2.2. Process parameters and operating ranges

- Hệ thống giám sát liên tục (continuously monitored) ghi nhận $7$ thông số đầu vào (input parameters) mô tả điều kiện xử lý sinh học (biological treatment conditions) và trạng thái vận hành màng (membrane operating state):
  - Tốc độ châm glucose ($\text{Glu}$, glucose dosing rate): đại diện cho tải lượng hữu cơ bổ sung (surrogate for supplemental organic loading).
  - Nồng độ chất rắn lơ lửng trong bùn lỏng ($\text{MLSS}$, mixed liquor suspended solids).
  - Tốc độ sục khí ($\text{Air}$, aeration rate).
  - Tỷ lệ thức ăn trên vi sinh vật ($\text{F/M}$, food-to-microorganism ratio).
  - Tỷ lệ tổng cacbon hữu cơ trên tổng nitơ ($\text{C/N}$, ratio of total organic carbon to total nitrogen).
  - Thời gian lưu nước thủy lực ($\text{HRT}$, hydraulic retention time).
  - Thời gian lưu bùn ($\text{SRT}$, sludge retention time).
- Mô hình thực hiện dự báo $3$ biến mục tiêu đầu ra (target variables) đại diện cho các phương diện vận hành màng:
  - Áp suất xuyên màng ($\text{TMP}$, transmembrane pressure): chỉ thị chính cho hiện tượng nghẹt màng (primary fouling indicator).
  - Lưu lượng nước thấm qua màng ($\text{Flow}$, permeate flow rate): thước đo sản lượng làm việc (measure of productive output).
  - Mực nước trong bể màng ($\text{Level}$, membrane tank water level): chỉ số chỉ thị cân bằng thủy lực (indicator of hydraulic balance).
- Quy chuẩn đặt tên viết tắt và định nghĩa đại lượng thống nhất trong toàn bộ tài liệu:
  - Toàn bộ $10$ ký hiệu viết tắt ($\text{Glu}$, $\text{MLSS}$, $\text{Air}$, $\text{F/M}$, $\text{C/N}$, $\text{HRT}$, $\text{SRT}$, $\text{TMP}$, $\text{Flow}$ và $\text{Level}$) được sử dụng nhất quán xuyên suốt phần văn bản (text), bảng biểu (tables) và hình vẽ (figures), bao gồm cả phần tóm tắt (abstract) và từ khóa (keywords).
  - Tỷ lệ cacbon trên nitơ (carbon-to-nitrogen ratio) được đo lường dưới dạng $\text{TOC/TN}$; hai thuật ngữ này biểu thị cùng một đại lượng và chỉ ký hiệu $\text{C/N}$ được sử dụng từ đây về sau.
- Bảng đặc tính thống kê của tất cả các thông số đo lường (Table 1):
  - Bảng 1 (Table 1) tổng hợp các đặc tính thống kê (statistical characteristics) cho toàn bộ các thông số từ $4593$ bản ghi dữ liệu SCADA theo giờ:

| Đặc trưng (Feature) | Số lượng mẫu (Count) | Trung bình (Mean) | Độ lệch chuẩn (Std) | Nhỏ nhất (Min) | Lớn nhất (Max) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\text{Glu}\ (\text{L/min})$ | $4593$ | $0.6775$ | $0.1807$ | $0.4027$ | $1.3515$ |
| $\text{MLSS}\ (\text{mg/L})$ | $4593$ | $4889.5$ | $1075.2$ | $1919.4$ | $7628.8$ |
| $\text{Air}\ (\text{m}^3/\text{h})$ | $4593$ | $5945.7$ | $534.5$ | $4469.1$ | $7268.3$ |
| $\text{F/M}\ (1/\text{day})$ | $4593$ | $0.0275$ | $0.0078$ | $0.0118$ | $0.0658$ |
| $\text{C/N ratio}$ | $4593$ | $9.4314$ | $2.2581$ | $4.8040$ | $17.5029$ |
| $\text{HRT}\ (\text{h})$ | $4593$ | $7.3346$ | $0.7947$ | $5.8738$ | $11.0411$ |
| $\text{SRT}\ (\text{day})$ | $4593$ | $87.828$ | $14.564$ | $43.323$ | $108.333$ |
| $\text{TMP}\ (\text{bar})$ | $4593$ | $-0.122$ | $0.090$ | $-0.462$ | $-0.034$ |
| $\text{Flow}\ (\text{m}^3/\text{min})$ | $4593$ | $1.817$ | $0.257$ | $0.618$ | $2.289$ |
| $\text{Level (lv)}\ (\%)$ | $4593$ | $65.774$ | $1.114$ | $64.005$ | $73.942$ |

  - Dải vận hành thực tế của các thông số đầu vào (operating ranges of input features):
    - Tốc độ châm glucose ($\text{Glu}$): biến thiên từ $0.4027$ đến $1.3515\ \text{L/min}$ (trung bình $0.6775 \pm 0.1807\ \text{L/min}$).
    - Nồng độ bùn hoạt tính ($\text{MLSS}$): dao động từ $1919.4$ đến $7628.8\ \text{mg/L}$ (trung bình $4889.5 \pm 1075.2\ \text{mg/L}$).
    - Tốc độ cấp khí sục màng ($\text{Air}$): dao động từ $4469.1$ đến $7268.3\ \text{m}^3/\text{h}$ (trung bình $5945.7 \pm 534.5\ \text{m}^3/\text{h}$).
    - Tỷ lệ dinh dưỡng trên vi sinh ($\text{F/M}$): dao động từ $0.0118$ đến $0.0658\ 1/\text{day}$ (trung bình $0.0275 \pm 0.0078\ 1/\text{day}$).
    - Tỷ lệ cacbon trên nitơ ($\text{C/N}$): dao động từ $4.8040$ đến $17.5029$ (trung bình $9.4314 \pm 2.2581$).
    - Thời gian lưu nước thủy lực ($\text{HRT}$): dao động từ $5.8738$ đến $11.0411\ \text{h}$ (trung bình $7.3346 \pm 0.7947\ \text{h}$).
    - Thời gian lưu bùn ($\text{SRT}$): dao động từ $43.323$ đến $108.333\ \text{day}$ (trung bình $87.828 \pm 14.564\ \text{day}$).
  - Dải biến thiên của các biến mục tiêu đầu ra (operating ranges of target variables):
    - Áp suất xuyên màng ($\text{TMP}$): dao động từ $-0.462$ đến $-0.034\ \text{bar}$ (trung bình $-0.122 \pm 0.090\ \text{bar}$).
    - Lưu lượng nước thấm qua màng ($\text{Flow}$): dao động từ $0.618$ đến $2.289\ \text{m}^3/\text{min}$ (trung bình $1.817 \pm 0.257\ \text{m}^3/\text{min}$).
    - Mực nước trong bể màng ($\text{Level}$): dao động từ $64.005$ đến $73.942\,\%$ (trung bình $65.774 \pm 1.114\,\%$).
