# Bối cảnh Toàn cục & Khung lý thuyết của LLM-FE

## 1. Giới thiệu & Thách thức Nghiên cứu
- **Tầm quan trọng của Kỹ thuật Đặc trưng (Feature Engineering - FE)**: Trong học máy với dữ liệu dạng bảng (tabular data), chất lượng của các biến đặc trưng quyết định hiệu năng của các mô hình dự đoán (đặc biệt là các mô hình cây như XGBoost, thường vượt trội hơn deep learning trên dữ liệu bảng). Tuy nhiên, FE thủ công đòi hỏi chuyên gia tốn rất nhiều thời gian và công sức để khám phá không gian tổ hợp khổng lồ.
- **Hạn chế của các phương pháp tự động truyền thống (AutoFE)**: Các công cụ như OpenFE hay AutoFeat hoạt động trong không gian toán tử tiền định cố định, thiếu khả năng tiếp cận tri thức ngữ nghĩa/tri thức miền (domain knowledge) về bản chất thực tế của các cột dữ liệu.
- **Hạn chế của các giải pháp dùng LLM trước đây**: Dù LLM chứa sẵn kho tri thức miền phong phú, các nghiên cứu gần đây (CAAFE, FeatLLM, OCTree) chủ yếu dựa vào prompt trực tiếp hoặc tối ưu hóa đơn luồng (single-path). Chúng không tận dụng được lịch sử thử nghiệm, không duy trì tính đa dạng giải pháp, và dễ bị thiên lệch chọn các toán tử toán học quá đơn giản (cộng, trừ, nhân, chia) hoặc rơi vào bẫy ghi nhớ (memorization).

## 2. Kiến trúc & Cơ chế Hoạt động của LLM-FE
LLM-FE mô hình hóa bài toán kỹ thuật đặc trưng dưới dạng **tìm kiếm chương trình (program search)** giải bài toán tối ưu hai cấp (bilevel optimization):
\max_T E(f^*(T(X_{\text{val}})), Y_{\text{val}}) \quad \text{subject to} \quad f^* \in \arg\min_f \mathcal{L}_f(f(T(X_{\text{tr}})), Y_{\text{tr}})
Khung làm việc gồm 4 bước vòng lặp tiến hóa:
1. **Sinh Đặc trưng Mới (New Feature Generation)**: Prompt đầu vào được cấu trúc chặt chẽ gồm: Chỉ dẫn (yêu cầu tạo đặc trưng phức tạp và diễn giải lý do), Đặc tả tập dữ liệu & Mẫu dữ liệu tuần tự hóa (serialized), Hàm đánh giá, và Các mẫu minh họa in-context tốt nhất từ các vòng lặp trước. LLM đóng vai trò toán tử đột biến và lai ghép ở cấp độ ngôn ngữ.
2. **Kỹ thuật Đặc trưng (Feature Engineering)**: Thực thi chương trình biến đổi được sinh bằng Python trên tập dữ liệu. Các chương trình lỗi cú pháp hoặc chạy quá thời gian giới hạn (30 giây) sẽ bị loại bỏ.
3. **Đánh giá Dựa trên Dữ liệu (Feature Evaluation)**: Huấn luyện mô hình dự đoán (XGBoost, MLP, TabPFN) trên tập dữ liệu đã tăng cường và tính điểm hiệu năng (Accuracy cho phân loại, RMSE cho hồi quy) trên tập validation để làm độ thích nghi (fitness score).
4. **Quản lý Kinh nghiệm (Experience Management)**: Sử dụng mô hình tiến hóa đa đảo ( = 3$ đảo độc lập). Các chương trình mới có điểm cao hơn kỷ lục của đảo sẽ được nạp vào đảo đó. Trong mỗi đảo, các chương trình được phân cụm theo chữ ký điểm số. Thuật toán chọn lọc Boltzmann được áp dụng để lấy mẫu in-context demonstrations nhằm vừa khai thác nghiệm tốt vừa bảo toàn tính đa dạng quần thể.

## 3. Các Kết quả Thực nghiệm Chính
- **Hiệu năng Vượt trội**: Thử nghiệm trên 19 tập dữ liệu phân loại và 10 tập dữ liệu hồi quy (OpenML, UCI, Kaggle). LLM-FE đạt thứ hạng trung bình tốt nhất (mean rank thấp nhất) so với cả baseline truyền thống (OpenFE, AutoFeat) và baseline LLM (CAAFE, FeatLLM, OCTree).
- **Phân tích Cắt bỏ (Ablation Study)**: Việc loại bỏ Tri thức miền (w/o Domain Knowledge) hoặc loại bỏ Tinh chỉnh tiến hóa (w/o Evolutionary Refinement) làm sụt giảm nghiêm trọng hiệu năng mô hình, chứng minh sự kết hợp giữa tri thức ngữ nghĩa và phản hồi thực nghiệm là thiết yếu.
- **Khắc phục Thiên lệch Toán tử**: Tìm kiếm tiến hóa thúc đẩy LLM khám phá các toán tử bậc cao (như groupbythenmean, sigmoid, residual) chiếm tới ~45% thay vì chỉ quanh quẩn ở các phép tính số học cơ bản.
- **Độ bền vững & Khả năng Chuyển giao**: LLM-FE duy trì ưu thế ngay cả khi dữ liệu bị thêm nhiễu Gaussian, kháng hiện tượng ghi nhớ (memorization), và các đặc trưng do XGBoost tối ưu có thể chuyển giao hiệu quả sang các kiến trúc khác như MLP hay TabPFN.