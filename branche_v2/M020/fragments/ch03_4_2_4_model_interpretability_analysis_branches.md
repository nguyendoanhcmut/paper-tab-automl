### 2.4. Model interpretability analysis

* **Khái niệm và sự cần thiết của tính khả giải thích trong học máy (ML interpretability)**: Tính khả giải thích trong học máy (machine learning - ML) thể hiện năng lực nắm bắt và giải thích các quyết định cũng như lập luận suy diễn đằng sau các mô hình.
  * **Hạn chế hộp đen của mô hình học máy**: Dù được chấp nhận và ứng dụng rộng rãi, phần lớn các mô hình ML đều có bản chất mờ đục (mostly opaque).
  * **Đánh giá độ tin cậy và quyết định thực thi**: Việc thấu hiểu căn nguyên dẫn tới các kết quả dự đoán đóng vai trò sống còn trong việc đánh giá mức độ tin cậy (assessing trust), xác định xem người vận hành có nên đưa ra hành động dựa trên dự đoán hay triển khai một mô hình mới hay không (Lipton, 2017).
  * **Giá trị ứng dụng trong dự đoán tắc nghẽn màng**: Trong bài toán dự đoán tắc nghẽn màng (membrane fouling prediction), phân tích tính khả giải thích giúp diễn giải cơ chế mô hình và cung cấp những hiểu biết sâu sắc (insights) về các thông số gây tắc nghẽn, tạo điều kiện thuận lợi cho công tác theo dõi và kiểm tra hệ thống (facilitate inspection).

* **Phương pháp giải thích cộng tính Shapley (SHapley Additive exPlanations - SHAP)**: Kỹ thuật diễn giải tiên tiến nhất (state-of-the-art interpreting technique) SHAP (Lundberg and Lee, 2017) được áp dụng cho mô hình mạng Perceptron đa lớp (multilayer perceptron - MLP) nhằm đánh giá khả năng giải thích và kiểm tra tác động của các thông số đầu vào đối với hiện tượng tắc nghẽn màng.
  * **Mục tiêu định lượng**: SHAP được sử dụng để tính toán các giá trị SHAP (SHAP values) nhằm lượng hóa mức độ quan trọng và ý nghĩa của từng đặc trưng đầu vào đối với kết quả dự đoán.

* **Công thức toán học của giá trị Shapley (Shapley values formulation)**: Giá trị SHAP được xác định thông qua Phương trình (17) dựa trên lý thuyết trò chơi hợp tác (cooperative game theory):
  $$\phi_i(f, x) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N| - |S| - 1)!}{|N|!} [f(S \cup \{i\}) - f(S)] \quad (17)$$
  * $\phi_i(f, x)$: Đại diện cho giá trị SHAP của đặc trưng $i$ đối với một dự đoán cụ thể được đưa ra bởi mô hình $f$ trên một cá thể/mẫu dữ liệu $x$ (instance $x$).
  * $N$: Tập hợp tất cả các đặc trưng đầu vào (set of all features).
  * $S$: Một liên minh các đặc trưng (coalition of features) không chứa đặc trưng $i$ ($S \subseteq N \setminus \{i\}$).
  * $|S|$ và $|N|$: Biểu diễn số lượng phần tử (lực lượng) tương ứng trong tập liên minh $S$ và toàn bộ tập đặc trưng $N$.
  * $f(S)$: Kết quả dự đoán được mô hình thực hiện trên mẫu $x$ với các đặc trưng trong liên minh $S$.
  * $f(S \cup \{i\})$: Kết quả dự đoán được mô hình thực hiện trên mẫu $x$ với các đặc trưng trong liên minh $S$ cộng thêm đặc trưng $i$.
  * $[f(S \cup \{i\}) - f(S)]$: Đóng góp biên (marginal contribution) của đặc trưng $i$ khi được đưa vào liên minh $S$.
  * **Cơ chế tính toán**: Giá trị SHAP của một đặc trưng được tính toán bằng cách xem xét toàn bộ các liên minh đặc trưng khả dĩ (all possible feature coalitions) cùng với đóng góp biên tương ứng của chúng theo trọng số tổ hợp xác suất.

* **Các khía cạnh phân tích diễn giải mô hình MLP**: Nhằm xác thực tính hợp lý (reasonableness) của mô hình dự đoán tắc nghẽn màng và thấu hiểu rõ hơn cách thức các thông số đầu vào chi phối sự biến đổi của áp suất xuyên màng (transmembrane pressure - TMP modification), nghiên cứu khảo sát ba khía cạnh dựa trên giá trị SHAP:
  * **Độ quan trọng của đặc trưng (Feature importance)**: Định lượng và xếp hạng mức độ ảnh hưởng tương đối của từng biến số đầu vào đối với dự đoán TMP.
  * **Khả năng giải thích toàn cục (Global interpretability / global explanations)**: Đánh giá xu hướng và hướng tác động tổng thể (tăng hoặc giảm) của từng đặc trưng trên toàn bộ tập dữ liệu.
  * **Khả năng giải thích cục bộ (Local interpretability / local explanations)**: Phân tích chi tiết tiến trình ra quyết định và sự tích lũy đóng góp của từng đặc trưng cho từng trường hợp dự đoán riêng biệt của mẫu thử nghiệm.
