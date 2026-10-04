import json

skeleton = {
  "doc_slug": "predictive_framework_for_membrane_fouling",
  "doc_title": "Predictive Framework for Membrane Fouling in Full-Scale Membrane Bioreactors (MBRs): Integrating AI-Driven Feature Engineering and Explainable AI (XAI)",
  "doc_type": "paper",
  "domain": "general",
  "max_heading_level": 4,
  "sections": [
    {"line": 47, "level": 2, "title": "Abstract"},
    {"line": 69, "level": 2, "title": "1. Introduction"},
    {"line": 228, "level": 2, "title": "2. Materials and Methods"},
    {"line": 229, "level": 3, "title": "2.1. MBR Process (Data Collection)"},
    {"line": 340, "level": 3, "title": "2.2. Exploratory Data Analysis (EDA)"},
    {"line": 345, "level": 4, "title": "2.2.1. Operational Feature Statistics"},
    {"line": 350, "level": 4, "title": "2.2.2. Pair Plot"},
    {"line": 357, "level": 4, "title": "2.2.3. Scatter Plot"},
    {"line": 361, "level": 4, "title": "2.2.4. Pearson Correlation"},
    {"line": 366, "level": 4, "title": "2.2.5. Normality Check"},
    {"line": 375, "level": 3, "title": "2.3. Preprocessing and Feature Engineering"},
    {"line": 387, "level": 4, "title": "2.3.1. Robust Scaling"},
    {"line": 397, "level": 4, "title": "2.3.2. Moving Average"},
    {"line": 417, "level": 3, "title": "2.4. Models"},
    {"line": 422, "level": 4, "title": "2.4.1. Statistical Models"},
    {"line": 511, "level": 4, "title": "2.4.2. Machine Learning Models"},
    {"line": 596, "level": 3, "title": "2.5. Explainable AI"},
    {"line": 603, "level": 4, "title": "2.5.1. Feature Importance"},
    {"line": 607, "level": 4, "title": "2.5.2. Shapley Additive Explanations"},
    {"line": 629, "level": 2, "title": "3. Results"},
    {"line": 630, "level": 3, "title": "3.1. Data Distribution and Correlation Analysis"},
    {"line": 631, "level": 4, "title": "3.1.1. Descriptive Statistics"},
    {"line": 802, "level": 4, "title": "3.1.2. Pair Plot Analysis"},
    {"line": 838, "level": 4, "title": "3.1.3. Pearson Correlation Analysis"},
    {"line": 1022, "level": 4, "title": "3.1.4. Application of Normality Check"},
    {"line": 1051, "level": 3, "title": "3.2. Application of Robust Scaling and Moving Average"},
    {"line": 1052, "level": 4, "title": "3.2.1. Application of Robust Scaling"},
    {"line": 1075, "level": 4, "title": "3.2.2. Application of Moving Average"},
    {"line": 1096, "level": 3, "title": "3.3. Model Performance Evaluation"},
    {"line": 1100, "level": 4, "title": "3.3.1. Model Performance Based on Raw Data"},
    {"line": 1314, "level": 4, "title": "3.3.2. Enhanced Model Performance with Robust Scaling and Moving Average"},
    {"line": 1453, "level": 3, "title": "3.4. Final Prediction Performance"},
    {"line": 1496, "level": 3, "title": "3.5. Explainable AI (XAI) for Membrane Fouling Prediction"},
    {"line": 1576, "level": 4, "title": "3.5.1. Feature Importance Analysis"},
    {"line": 1588, "level": 4, "title": "3.5.2. SHAP Analysis"},
    {"line": 1612, "level": 4, "title": "3.5.3. Implications for MBR Optimization"},
    {"line": 1635, "level": 2, "title": "4. Conclusions"}
  ],
  "figure_ids": {
    "fig_01": 229,
    "fig_03": 802,
    "fig_04": 1022,
    "fig_05": 1052,
    "fig_06": 1453,
    "fig_07": 1576,
    "fig_08": 1588
  },
  "drop_figures": ["fig_02"],
  "exercises": [],
  "rule_index": [
    {"title": "2.3.1. Robust Scaling", "page": 8},
    {"title": "2.3.2. Moving Average", "page": 8},
    {"title": "2.4.1. Statistical Models", "page": 8},
    {"title": "2.4.2. Machine Learning Models", "page": 9},
    {"title": "2.5. Explainable AI", "page": 10}
  ],
  "global_lexicon": {
    "core_thesis": "Nghiên cứu phát triển khung dự đoán tắc nghẽn màng (membrane fouling) cho hệ thống MBR quy mô thực tế bằng cách kết hợp kỹ thuật trích xuất đặc trưng AI (Moving Average, Robust Scaling) với các mô hình học máy (đặc biệt là CatBoost) và XAI (SHAP, Permutation Importance) nhằm nâng cao độ chính xác dự báo và giải thích động học tắc nghẽn phục vụ tối ưu hóa vận hành.",
    "key_terms": [
      {"term": "MBR (Membrane Bioreactor)", "definition": "Bể phản ứng sinh học màng kết hợp xử lý bùn hoạt tính sinh học và lọc màng."},
      {"term": "TMP (Transmembrane Pressure)", "definition": "Áp suất xuyên màng, thông số vật lý then chốt phản ánh mức độ tắc nghẽn màng."},
      {"term": "Spec. Flux (Specific Flux)", "definition": "Thông lượng riêng (tỷ số giữa Flux và TMP, LMH/kPa), chỉ số chuẩn hóa để theo dõi năng suất và suy giảm hiệu suất màng."},
      {"term": "MLSS (Mixed Liquor Suspended Solids)", "definition": "Nồng độ bùn hoạt tính lơ lửng trong bể MBR (mg/L)."},
      {"term": "F/M (Food-to-Microorganism ratio)", "definition": "Tỷ lệ thức ăn trên vi sinh vật (kgCOD/(kgMLSS·d)), yếu tố sinh học chi phối tải trọng hữu cơ và động học tắc nghẽn."},
      {"term": "SVI (Sludge Volume Index)", "definition": "Chỉ số thể tích bùn (mL/g), đánh giá khả năng lắng và tình trạng kết bông của bùn."},
      {"term": "SV30 (Sludge Volume after 30 min)", "definition": "Độ lắng bùn sau 30 phút (%)."},
      {"term": "COD RM (COD Removal Rate)", "definition": "Tỷ lệ loại bỏ COD của hệ thống (%)."},
      {"term": "Robust Scaling", "definition": "Kỹ thuật chuẩn hóa biến số sử dụng trung vị (median) và khoảng tứ phân vị (IQR) để loại trừ ảnh hưởng của giá trị ngoại lai."},
      {"term": "Moving Average (MA)", "definition": "Kỹ thuật trung bình trượt làm mịn biến động ngắn hạn để nắm bắt xu hướng suy thoái màng tích lũy trong chuỗi thời gian."},
      {"term": "CatBoost", "definition": "Thuật toán Gradient Boosting dựa trên cây quyết định đối xứng (symmetric decision trees), đạt độ chính xác cao nhất (R² = 0.8374) trong dự báo thông lượng riêng."},
      {"term": "SHAP (Shapley Additive Explanations)", "definition": "Phương pháp XAI dựa trên lý thuyết trò chơi hợp tác giúp lượng hóa tác động biên của từng giá trị đặc trưng lên kết quả dự đoán."},
      {"term": "Permutation Feature Importance", "definition": "Phương pháp đo lường tầm quan trọng đặc trưng bằng mức giảm hiệu suất khi xáo trộn ngẫu nhiên giá trị của đặc trưng đó."}
    ],
    "key_entities": [
      "Full-scale food wastewater treatment plant (Beijing, China)",
      "AnoxKaldnes / MBR unit",
      "CatBoost",
      "Random Forest",
      "XGBoost",
      "LightGBM",
      "Ridge Regression",
      "Lasso Regression",
      "ElasticNet",
      "SHAP"
    ]
  },
  "global_context_pack": "Khung dự đoán tắc nghẽn màng (Membrane Fouling) trên hệ thống MBR xử lý nước thải chế biến thực phẩm quy mô thực tế (114 m³/ngày, HRT 0.75 ngày) tại Bắc Kinh. Bài báo tích hợp kỹ thuật trích xuất đặc trưng AI (Robust Scaling xử lý nhiễu dữ liệu phi chuẩn, Moving Average cửa sổ 3-7 ngày làm mịn chuỗi thời gian) cùng các mô hình học máy (CatBoost, RF, XGBoost, LightGBM) và giải thích mô hình (Permutation Importance, SHAP). Kết quả cho thấy CatBoost kết hợp Moving Average cải thiện vượt bậc hiệu suất dự báo (R² từ 0.35 lên 0.8374), và XAI chỉ ra rằng tỷ lệ F/M (đặc biệt là F/M_MA5) là nhân tố chi phối mạnh mẽ nhất đến động học tắc nghẽn màng."
}

with open("skeleton.json", "w", encoding="utf-8") as f:
    json.dump(skeleton, f, indent=2, ensure_ascii=False)

print("Saved skeleton.json successfully")
