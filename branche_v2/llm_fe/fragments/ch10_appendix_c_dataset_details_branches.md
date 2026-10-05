## Phụ lục C: Chi tiết về các tập dữ liệu (Appendix C: Dataset Details)

- **Tổng quan về tập dữ liệu thực nghiệm**:
  - Nghiên cứu sử dụng một bộ sưu tập đa dạng gồm $29$ tập dữ liệu thực nghiệm, bao trùm $3$ nhóm bài toán học máy chủ đạo trên dữ liệu bảng (tabular data):
    1. *Phân loại nhị phân (Binary Classification)*: Gồm $7$ tập dữ liệu.
    2. *Phân loại đa lớp (Multi-class Classification)*: Gồm $12$ tập dữ liệu (tổng cộng $19$ tập dữ liệu phân loại).
    3. *Hồi quy (Regression)*: Gồm $10$ tập dữ liệu.
  - Các tập dữ liệu được tuyển chọn chủ yếu từ các nền tảng học máy uy tín và tiêu chuẩn trong cộng đồng nghiên cứu: OpenML (Vanschoren et al., 2014; Feurer et al., 2021), UCI Machine Learning Repository (Asuncion et al., 2007), và Kaggle.

### C.1 Tiêu chí Tuyển chọn và Cơ sở Phương pháp luận (Selection Criteria and Rationale)

- **Ưu tiên ngữ nghĩa của đặc trưng (Descriptive feature names)**:
  - Nhóm tác giả chủ đích tuyển chọn các tập dữ liệu có tên thuộc tính/đặc trưng mang ý nghĩa mô tả rõ ràng (descriptive feature names).
  - Loại bỏ hoàn toàn các tập dữ liệu chỉ chứa các mã định danh số thuần túy hoặc đã bị ẩn danh hóa (merely numerical identifiers, ví dụ `feat_1`, `feat_2`).
  - *Ý nghĩa đối với LLM*: Việc giữ nguyên tên đặc trưng giàu ngữ nghĩa là tiền đề cốt lõi giúp các mô hình ngôn ngữ lớn (Large Language Models - LLMs) kích hoạt và khai thác tri thức miền (domain knowledge) được tích lũy sẵn, từ đó đề xuất các biến đổi đặc trưng có căn cứ thực tế và lý giải được.
- **Tích hợp bản mô tả tác vụ ngữ cảnh (Contextual task description)**:
  - Mỗi tập dữ liệu đều đi kèm một bản mô tả tác vụ chi tiết (task description), làm rõ ngữ cảnh ứng dụng và mục tiêu dự đoán của bài toán.
  - Thông tin ngữ cảnh này giúp tăng cường sự thấu hiểu bài toán (enhancing contextual understanding) cho cả người sử dụng lẫn LLM trong quá trình tạo lập và tối ưu hóa đặc trưng.
- **Độ đa dạng về quy mô mẫu và chiều không gian (Scale and Dimensionality Diversity)**:
  - Phổ kích thước mẫu ($N$) trải dài từ các tập dữ liệu rất nhỏ ($315$ mẫu trong `plasma_retinol`, $452$ mẫu trong `arrhythmia`, $517$ mẫu trong `forest-fires`) cho tới các tập dữ liệu quy mô đồ sộ ($253{,}680$ mẫu trong `cdc diabetes` và $581{,}012$ mẫu trong `covtype`).
  - Chiều không gian thuộc tính ($D$) biến thiên mạnh mẽ: từ các tập dữ liệu có số chiều rất thấp ($4$ đặc trưng trong `blood-transfusion` và `balance-scale`) đến các tập dữ liệu số chiều cao (high-dimensional datasets) với hơn $50$ đặc trưng ($> 50$ features), đặc biệt có tập dữ liệu lên đến $279$ đặc trưng (`arrhythmia`).
  - Phổ dữ liệu đa dạng và toàn diện này phản ánh sát thực các kịch bản thực tế (real-world scenarios), tạo nên một khung kiểm thử vững chắc (robust evaluation framework) để đánh giá toàn diện năng lực của các thuật toán kỹ thuật đặc trưng tự động (Automated Feature Engineering - AutoFE).

### C.2 Thống kê Chi tiết các Tập dữ liệu Thực nghiệm (Table 6: Dataset Statistics)

- **Bảng thống kê toàn diện $29$ tập dữ liệu (Bảng 6)**:
  - Thống kê chi tiết các tham số cốt lõi gồm: Tên tập dữ liệu (Dataset), Số lượng đặc trưng (#Features), Số lượng mẫu (#Samples), Nguồn gốc dữ liệu (Source), và Mã định danh hoặc Tên tác vụ trên kho lưu trữ (ID/Name):

| Nhóm bài toán (Category) | Tập dữ liệu (Dataset) | Số đặc trưng (#Features) | Số mẫu (#Samples) | Nguồn (Source) | Định danh / Tên lưu trữ (ID/Name) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Phân loại nhị phân (Binary Classification)** | `adult` | $14$ | $48{,}842$ | OpenML | 1590 |
| | `blood-transfusion` | $4$ | $748$ | OpenML | 1464 |
| | `bank-marketing` | $16$ | $45{,}211$ | OpenML | 1461 |
| | `breast-w` | $9$ | $699$ | OpenML | 15 |
| | `credit-g` | $20$ | $1{,}000$ | OpenML | 31 |
| | `tic-tac-toe` | $9$ | $958$ | OpenML | 50 |
| | `pc1` | $21$ | $1{,}109$ | OpenML | 1068 |
| **Phân loại đa lớp (Multi-class Classification)** | `arrhythmia` | $279$ | $452$ | OpenML | 5 |
| | `balance-scale` | $4$ | $625$ | OpenML | 11 |
| | `car` | $6$ | $1{,}728$ | OpenML | 40975 |
| | `cmc` | $9$ | $1{,}473$ | OpenML | 23 |
| | `eucalyptus` | $19$ | $736$ | OpenML | 188 |
| | `jungle_chess` | $6$ | $44{,}819$ | OpenML | 41027 |
| | `vehicle` | $18$ | $846$ | OpenML | 54 |
| | `cdc diabetes` | $21$ | $253{,}680$ | Kaggle | `diabetes-health-indicators-dataset` |
| | `heart` | $11$ | $918$ | Kaggle | `heart-failure-prediction` |
| | `communities` | $103$ | $1{,}994$ | UCI | `communities-and-crime` |
| | `covtype` | $54$ | $581{,}012$ | UCI | `covertype` |
| | `myocardial` | $111$ | $1{,}700$ | UCI | `myocardial-infarction-complications` |
| **Hồi quy (Regression)** | `airfoil_self_noise` | $6$ | $1{,}503$ | OpenML | 44957 |
| | `cpu_small` | $12$ | $8{,}192$ | OpenML | 562 |
| | `diamonds` | $9$ | $53{,}940$ | OpenML | 42225 |
| | `plasma_retinol` | $13$ | $315$ | OpenML | 511 |
| | `forest-fires` | $13$ | $517$ | OpenML | 42363 |
| | `housing` | $9$ | $20{,}640$ | OpenML | 43996 |
| | `crab` | $8$ | $3{,}893$ | Kaggle | `crab-age-prediction` |
| | `insurance` | $7$ | $1{,}338$ | Kaggle | `us-health-insurancedataset` |
| | `bike` | $11$ | $17{,}389$ | UCI | `bike-sharing-dataset` |
| | `wine` | $10$ | $4{,}898$ | UCI | `wine-quality` |

### C.3 Phân tích Đặc tính Cấu trúc và Phân phối Dữ liệu (Structural & Distributional Analysis)

- **Đặc trưng nhóm Phân loại nhị phân (Binary Classification)**:
  - *Phân phối số chiều và mẫu*: Số lượng thuộc tính nằm trong khoảng từ $4$ (`blood-transfusion`) đến $21$ (`pc1`). Số lượng mẫu dao động từ $699$ (`breast-w`) đến $48{,}842$ (`adult`).
  - *Nguồn cung cấp*: Toàn bộ $7/7$ ($100\%$) tập dữ liệu phân loại nhị phân được trích xuất từ OpenML với mã định danh công khai, đảm bảo tính thuận tiện cao trong tái lập thực nghiệm.
  - *Miền ứng dụng*: Đại diện cho các tác vụ quan trọng như dự báo thu nhập kinh tế-xã hội (`adult`), tiếp thị ngân hàng (`bank-marketing`), thẩm định tín dụng cá nhân (`credit-g`), chẩn đoán lâm sàng (`blood-transfusion`, `breast-w`), phát hiện lỗi phần mềm (`pc1`), và nhận dạng trạng thái trò chơi cờ (`tic-tac-toe`).

- **Đặc trưng nhóm Phân loại đa lớp (Multi-class Classification)**:
  - *Phân phối số chiều và mẫu*: Số lượng thuộc tính trải rộng từ $4$ (`balance-scale`) đến $279$ (`arrhythmia`). Số mẫu dao động từ $452$ (`arrhythmia`) đến $581{,}012$ (`covtype`).
  - *Nguồn cung cấp*: Phân bổ đa dạng từ $3$ nguồn gồm $7$ tập từ OpenML, $3$ tập từ UCI (`communities`, `covtype`, `myocardial`), và $2$ tập từ Kaggle (`cdc diabetes`, `heart`).
  - *Nhóm tập dữ liệu nhiều chiều (High-dimensional subset)*: Danh mục này bao hàm toàn bộ $4$ tập dữ liệu có số lượng thuộc tính vượt mốc $50$ ($> 50$ features):
    - `covtype`: $54$ đặc trưng, $581{,}012$ mẫu (phân loại loại che phủ rừng quy mô rất lớn).
    - `communities`: $103$ đặc trưng, $1{,}994$ mẫu (dự báo tội phạm và nhân khẩu học cộng đồng).
    - `myocardial`: $111$ đặc trưng, $1{,}700$ mẫu (dự đoán biến chứng sau nhồi máu cơ tim).
    - `arrhythmia`: $279$ đặc trưng, $452$ mẫu (bài toán y tế số chiều cao với tỷ số số chiều trên số mẫu $D/N > 0.61$).

- **Đặc trưng nhóm Hồi quy (Regression)**:
  - *Phân phối số chiều và mẫu*: Số lượng thuộc tính có độ tập trung cao trong khoảng từ $6$ (`airfoil_self_noise`) đến $13$ (`plasma_retinol`, `forest-fires`). Quy mô mẫu trải rộng từ $315$ (`plasma_retinol`) đến $53{,}940$ (`diamonds`).
  - *Nguồn cung cấp*: Bao gồm $6$ tập từ OpenML, $2$ tập từ Kaggle (`crab`, `insurance`), và $2$ tập từ UCI (`bike`, `wine`).
  - *Miền ứng dụng*: Bao phủ các hiện tượng tự nhiên và xã hội phức tạp như động lực học âm thanh cánh máy bay (`airfoil_self_noise`), thời gian tải hệ thống tính toán (`cpu_small`), kinh tế thị trường (`diamonds`, `housing`), y sinh học (`plasma_retinol`, `insurance`), cháy rừng và khí tượng (`forest-fires`), sinh thái học biển (`crab`), điều phối giao thông công cộng (`bike`), và hóa học thực phẩm (`wine`).
