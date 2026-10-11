## 4. Conclusion

* Nghiên cứu đã tích hợp phân tích thực nghiệm với mô hình hóa học máy (machine learning - ML) nhằm làm sáng tỏ quá trình chuyển hóa chất hữu cơ và hành vi nghẹt màng (membrane fouling) trong hệ thống bể phản ứng sinh học màng kỵ khí (anaerobic membrane bioreactor - AnMBR) xử lý nước rỉ rác trạm trung chuyển (transfer station landfill leachate) có nồng độ chất ô nhiễm cao trong $120\text{ ngày}$ vận hành.
* Các thông số vận hành thực nghiệm, đặc biệt là thời gian lưu thủy lực (hydraulic retention time - HRT) và tải trọng hữu cơ (organic loading rate - OLR), chi phối mạnh mẽ đến hiệu quả xử lý và độ ổn định của hệ thống:
  * Hiệu quả loại bỏ nhu cầu oxy hóa học (chemical oxygen demand - COD) duy trì ở mức $>80\%$ xuyên suốt tất cả các giai đoạn vận hành.
  * Các giai đoạn gia tăng tải trọng đã kích hoạt sự tăng nhanh áp suất xuyên màng (transmembrane pressure - TMP) từ $2\text{ kPa}$ lên $32.5\text{ kPa}$, phản ánh độ nhạy cảm cao của động học nghẹt màng trước các biến động vận hành.
  * Nồng độ $\text{NH}_4^+-\text{N}$ trong dòng ra duy trì ở mức cao do quá trình phân hủy kỵ khí khoáng hóa nitơ hữu cơ mà không diễn ra quá trình nitrat hóa, đóng vai trò như một chỉ thị sinh học quan trọng đối với trạng thái nghẹt màng.
* Mô hình rừng ngẫu nhiên (Random Forest - RF) đạt hiệu năng dự đoán tổng thể tốt nhất cho cả hai biến mục tiêu trên tập kiểm tra độc lập (independent test set):
  * Đối với COD dòng ra (effluent COD): RF mang lại độ chính xác cao nhất với $R^2 = 0.96$ và sai số căn bậc hai trung bình $\text{RMSE} = 331.50\text{ mg/L}$.
  * Đối với dự đoán TMP: RF thể hiện kết quả vượt hơn rõ rệt so với Extreme Gradient Boosting (XGBoost) và Mạng nơ-ron nhân tạo (Artificial Neural Network - ANN) trên tập kiểm tra độc lập, đạt $R^2 = 0.88$ và $\text{RMSE} = 3.86\text{ kPa}$, so với $R^2 = 0.560$ và $\text{RMSE} = 7.50\text{ kPa}$ của XGBoost, cùng $R^2 = 0.54$ và $\text{RMSE} = 7.59\text{ kPa}$ của ANN.
* Phân tích SHapley Additive exPlanations (SHAP) xác định các biến số dự đoán quan trọng liên kết với mô hình cho từng mục tiêu:
  * Đối với effluent COD: OLR, HRT và thế oxy hóa - khử (oxidation-reduction potential - ORP) là các biến dự đoán then chốt chi phối kết quả mô hình.
  * Đối với TMP: $\text{NH}_4^+-\text{N}$ dòng ra, pH dòng ra và ORP đóng góp mạnh nhất vào kết quả dự đoán TMP.
* Các mô hình ML có khả năng giải thích (interpretable ML models) cung cấp các hiểu biết chẩn đoán hữu ích phục vụ tối ưu hóa hiệu suất vận hành AnMBR và kiểm soát nghẹt màng:
  * Mô hình thể hiện độ tin cậy cao hơn khi thực hiện phép nội suy (interpolation) trong phạm vi dải thông số vận hành đã được quan sát trong nghiên cứu.
  * Giới hạn của mô hình nằm ở khả năng ngoại suy (extrapolation) đối với các điều kiện sốc tải (shock-loading conditions) chưa từng xuất hiện trong tập dữ liệu huấn luyện.
* Ý nghĩa kỹ thuật và định hướng nghiên cứu tiếp theo đòi hỏi mở rộng quy mô dữ liệu:
  * Cần xây dựng các bộ dữ liệu đa điểm (multi-site datasets) với quy mô lớn hơn.
  * Cần kiểm chứng và thẩm định mô hình trên dải điều kiện sốc tải rộng hơn trước khi triển khai ứng dụng thực tế ở quy mô công nghiệp (industrial deployment).
