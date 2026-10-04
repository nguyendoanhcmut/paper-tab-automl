## 4 Conclusions

- Nghiên cứu phát triển mô hình dự đoán liều lượng châm chất keo tụ (coagulant dosing) trong nhà máy xử lý nước bằng AutoML (Automated Machine Learning - học máy tự động) và giải thích kết quả mô hình nhằm giải quyết vấn đề minh bạch (transparency) của mô hình dự đoán:
  - Mô hình RF (Random Forest - rừng ngẫu nhiên) phát triển bằng AutoML thể hiện hiệu năng cao trên tập dữ liệu kiểm tra:
    - Hệ số xác định đạt $R^2 = 0.96$.
    - Sai số toàn phương trung bình đạt $\text{RMSE} = 0.89$.
    - Sai số tuyệt đối trung bình đạt $\text{MAE} = 0.47$.
    - Mô hình mang lại chu kỳ phát triển nhanh hơn và độ chính xác dự đoán cao hơn so với các mô hình lựa chọn thủ công.
    - Mô hình đóng vai trò công cụ giá trị cho tác vụ dự đoán liều lượng châm chất keo tụ trong nhà máy xử lý nước.
  - Phương pháp giải thích mô hình dựa trên giá trị SHAP (Shapley Additive exPlanations - giải thích cộng tính Shapley) làm sáng tỏ ảnh hưởng của từng chỉ số chất lượng nước đến kết quả dự đoán:
    - Khi $\text{NTU-RW}$ (raw water turbidity - độ đục nước thô) ở mức thấp và tương đối ổn định, độ dẫn điện của nước thô (raw water conductivity) trở thành yếu tố ảnh hưởng lớn nhất đến liều lượng châm chất keo tụ.
    - Các chỉ số tiếp theo theo thứ tự mức độ ảnh hưởng gồm $\text{NH}_3\text{-N-RW}$ (raw water ammonia nitrogen - nitơ amoniac nước thô), $\text{COD}_{\text{Mn}}\text{-RW}$ (raw water permanganate index - chỉ số pemanganat nước thô), $\text{T-RW}$ (raw water temperature - nhiệt độ nước thô), và $\text{WTR}$ (water treatment rate - lưu lượng xử lý nước).
  - Mô hình tối ưu hóa dự đoán lượng hóa chất $\text{PACl}$ (polyaluminum chloride - chất keo tụ polyaluminium chloride) tiết kiệm hàng ngày:
    - Nguồn nước từ sông Dương Tử (Yangtze River): tiết kiệm $222\text{ kg}$ mỗi ngày ($11\,\%$).
    - Nguồn nước từ sông Loan Hà (Luanhe River): tiết kiệm $225\text{ kg}$ mỗi ngày ($8\,\%$).
    - Kết quả này nhấn mạnh vai trò then chốt của mô hình châm chất keo tụ trong việc cải thiện hiệu quả xử lý nước và tối ưu hóa sử dụng tài nguyên.
