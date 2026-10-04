import json

skeleton = {
  "doc_slug": "predicting_nitrification_status_in_aerobic",
  "doc_title": "Predicting nitrification status in aerobic membrane bioreactors by interpretable machine learning models",
  "doc_type": "paper",
  "domain": "general",
  "max_heading_level": 4,
  "sections": [
    { "line": 0, "level": 2, "title": "Abstract" },
    { "line": 38, "level": 2, "title": "1. Introduction" },
    { "line": 113, "level": 2, "title": "2. Material and methods" },
    { "line": 114, "level": 3, "title": "2.1. Experiment method" },
    { "line": 141, "level": 3, "title": "2.2. Data-driven modelling" },
    { "line": 144, "level": 4, "title": "2.2.1. Binary classification: nitrification process evaluation" },
    { "line": 158, "level": 4, "title": "2.2.2. Qualitative analysis of inputs selection" },
    { "line": 173, "level": 4, "title": "2.2.3. Data preprocessing" },
    { "line": 181, "level": 4, "title": "2.2.4. Dataset splitting strategy" },
    { "line": 201, "level": 4, "title": "2.2.5. Statistical correlation analysis for inputs determination" },
    { "line": 209, "level": 4, "title": "2.2.6. Model-based interpretability: interpretable ML algorithms" },
    { "line": 235, "level": 4, "title": "2.2.7. Evaluation metrics and hyperparameter tuning criteria" },
    { "line": 270, "level": 4, "title": "2.2.8. Post hoc interpretability" },
    { "line": 296, "level": 2, "title": "3. Results analysis: data-driven model prediction" },
    { "line": 297, "level": 3, "title": "3.1. MBR performance and data collection" },
    { "line": 308, "level": 3, "title": "3.2. Input features determination" },
    { "line": 325, "level": 3, "title": "3.3. Nitrification status prediction without biocarriers addition" },
    { "line": 472, "level": 3, "title": "3.4. Cross-scenario test" },
    { "line": 498, "level": 2, "title": "4. Discussion and future perspective of sustainable operation" },
    { "line": 499, "level": 3, "title": "4.1. Data limitation and data collection" },
    { "line": 534, "level": 3, "title": "4.2. Trade-offs of input features for data-driven model structure" },
    { "line": 548, "level": 3, "title": "4.3. Model transferability improvement" },
    { "line": 571, "level": 3, "title": "4.4. Data-driven sustainable control" },
    { "line": 617, "level": 2, "title": "5. Conclusions" }
  ],
  "figure_ids": {
    "fig_01": 114,
    "fig_02": 144,
    "fig_03": 181,
    "fig_04": 325,
    "fig_05": 325,
    "fig_06": 571
  },
  "drop_figures": [],
  "exercises": [],
  "rule_index": [
    { "title": "2.2.1. Binary classification: nitrification process evaluation", "page": 4 },
    { "title": "2.2.7. Evaluation metrics and hyperparameter tuning criteria", "page": 6 },
    { "title": "2.2.8. Post hoc interpretability", "page": 6 }
  ],
  "global_lexicon": {
    "core_thesis": "Nghiên cứu đề xuất khung mô hình học máy có khả năng giải thích (interpretable ML) để giám sát và dự đoán trạng thái nitrat hóa trong màng phản ứng sinh học hiếu khí (MBR) xử lý nước xám tái sử dụng tại chỗ.",
    "key_terms": [
      { "term": "MBR", "definition": "Membrane Bioreactor - Bể phản ứng sinh học màng kết hợp xử lý sinh học và lọc màng." },
      { "term": "Greywater", "definition": "Nước xám - Nước thải sinh hoạt không chứa phân và nước tiểu (chiếm ~70% nước thải sinh hoạt)." },
      { "term": "Nitrification", "definition": "Quá trình nitrat hóa - Chuyển hóa sinh học amoni (NH4+) thành nitrit (NO2-) và nitrat (NO3-)." },
      { "term": "LR", "definition": "Logistic Regression - Mô hình hồi quy logistic." },
      { "term": "RF", "definition": "Random Forest - Mô hình rừng ngẫu nhiên dựa trên cây quyết định." },
      { "term": "XGB", "definition": "Extreme Gradient Boosting - Mô hình tăng cường độ dốc." },
      { "term": "SHAP", "definition": "SHapley Additive exPlanations - Phương pháp giải thích hậu kiểm dựa trên lý thuyết trò chơi hợp tác." },
      { "term": "TPR", "definition": "True Positive Rate (Tỷ lệ dương tính thật / Recall) - Tỷ lệ nhận diện đúng trạng thái nitrat hóa đầy đủ." },
      { "term": "FPR", "definition": "False Positive Rate (Tỷ lệ dương tính giả) - Tỷ lệ phân loại nhầm trạng thái nitrat hóa không đủ thành đủ." },
      { "term": "TMP", "definition": "Transmembrane Pressure - Áp suất xuyên màng." }
    ],
    "key_entities": [
      "Aerobic MBR", "Greywater", "Nitrification", "Logistic Regression", "Random Forest", "XGBoost", "SHAP"
    ]
  },
  "global_context_pack": "Nghiên cứu phát triển mô hình ML có thể giải thích (LR, RF, XGB) để dự đoán trạng thái nitrat hóa ('đầy đủ' hoặc 'không đủ') trong hệ thống MBR xử lý nước xám tái sử dụng tại chỗ. Sử dụng 6 đặc trưng đầu vào tương thích cảm biến (lưu lượng khí sục, lưu lượng vào, TMP, COD đầu ra, NO3--N đầu ra, NH4+-N đầu ra). Tối ưu hóa mô hình ưu tiên Precision để tránh điều khiển sai. Đánh giá cross-scenario giữa hệ thống không có giá thể sinh học (biocarriers) và có giá thể sinh học. Phân tích SHAP và KDE cung cấp giải thích cơ chế."
}

with open("C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/predicting_nitrification_status_in_aerobic/skeleton.json", "w", encoding="utf-8") as f:
    json.dump(skeleton, f, indent=2, ensure_ascii=False)
print("skeleton.json updated.")
