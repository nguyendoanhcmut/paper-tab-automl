### 2.7. Evaluation of model performance

- **Hiệu năng của mô hình được đánh giá thông qua các chỉ số $R^2$, $\text{RMSE}$ và $\text{MAE}$**:
  - Các thước đo hiệu năng mô hình (model performance) bao gồm hệ số xác định ($R^2$), căn bậc hai sai số toàn phương trung bình ($\text{RMSE}$ - root mean square error), và sai số tuyệt đối trung bình ($\text{MAE}$ - mean absolute error).
  - Chi tiết về các chỉ số đánh giá được trình bày tại Text S10.
- **Khả năng diễn giải mô hình (model interpretability) được kiểm tra thông qua các phân tích $\text{LOFO}$ và $\text{SHAP}$ (Fig. 1(e))**:
  - Phân tích loại trừ từng đặc trưng ($\text{LOFO}$ - leave-one-feature-out) và phân tích giải thích cộng tính Shapley ($\text{SHAP}$ - SHapley Additive exPlanations) được áp dụng để làm rõ cơ chế dự đoán và vai trò của các đặc trưng (Fig. 1(e)).
  - Chi tiết về phân tích $\text{LOFO}$ được trình bày trong Text S11.
  - Chi tiết về phân tích $\text{SHAP}$ được trình bày trong Text S12.
