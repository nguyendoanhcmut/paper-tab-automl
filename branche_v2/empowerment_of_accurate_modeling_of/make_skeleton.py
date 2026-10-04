import json
import os

skeleton = {
  "doc_slug": "empowerment_of_accurate_modeling_of",
  "doc_title": "Empowerment of accurate modeling of anaerobic membrane bioreactors by automated machine learning",
  "doc_type": "paper",
  "domain": "general",
  "max_heading_level": 4,
  "sections": [
    { "line": 18, "level": 2, "title": "Abstract" },
    { "line": 31, "level": 2, "title": "1. Introduction" },
    { "line": 131, "level": 2, "title": "2. Methods" },
    { "line": 138, "level": 3, "title": "2.1. Data" },
    { "line": 205, "level": 3, "title": "2.2. Modeling" },
    { "line": 263, "level": 3, "title": "2.3. Evaluation" },
    { "line": 344, "level": 3, "title": "2.4. Ablation studies" },
    { "line": 358, "level": 3, "title": "2.5. Feature ranking score" },
    { "line": 417, "level": 2, "title": "3. Results and discussion" },
    { "line": 418, "level": 3, "title": "3.1. AutoML for efficient AnMBR modeling" },
    { "line": 478, "level": 3, "title": "3.2. Improved ML performance with operation time as a feature" },
    { "line": 593, "level": 3, "title": "3.3. Impact of data volume on predictive performance" },
    { "line": 671, "level": 3, "title": "3.4. Ensemble feature-based importance analysis" },
    { "line": 721, "level": 3, "title": "3.5. Limitations and future perspectives" },
    { "line": 751, "level": 2, "title": "4. Conclusions" }
  ],
  "figure_ids": {
    "fig_01": 138,
    "fig_02": 418,
    "fig_03": 418,
    "fig_04": 478,
    "fig_05": 478,
    "fig_06": 593,
    "fig_07": 671
  },
  "drop_figures": [],
  "exercises": [],
  "rule_index": [
    { "title": "2.2. Modeling", "page": 3 },
    { "title": "2.3. Evaluation", "page": 3 },
    { "title": "2.4. Ablation studies", "page": 4 },
    { "title": "2.5. Feature ranking score", "page": 4 }
  ],
  "global_lexicon": {
    "core_thesis": "Nghiên cứu ứng dụng học máy tự động (FLAML AutoML) để mô hình hóa chính xác hiệu suất loại bỏ COD (COD-re) của hệ phản ứng màng sinh học kỵ khí (AnMBR) xử lý nước thải đô thị từ tập dữ liệu thực nghiệm nhỏ (185 mẫu), chứng minh hiệu quả vượt trội so với mạng nơ-ron sâu (R2 đạt 0.47, MAPE 3.11%), làm rõ vai trò cải thiện hiệu năng của biến thời gian vận hành (OD, nâng R2 lên 0.55), phát hiện hiện tượng suy giảm hiệu năng do dịch chuyển phân phối khi tăng kích thước dữ liệu không qua sàng lọc, và đề xuất khung xếp hạng đặc trưng kết hợp (Ensemble Ranking Score) xác định COD đầu vào (COD-in) là nhân tố chi phối hàng đầu.",
    "key_terms": [
      {
        "term": "AnMBR (Anaerobic Membrane Bioreactor)",
        "definition": "Bể phản ứng màng sinh học kỵ khí kết hợp phân hủy kỵ khí và lọc màng để xử lý nước thải với mức tiêu thụ năng lượng thấp, phát sinh ít bùn và có khả năng thu hồi biogas."
      },
      {
        "term": "AutoML (Automated Machine Learning)",
        "definition": "Học máy tự động hóa quy trình lựa chọn thuật toán, tiền xử lý và tinh chỉnh siêu tham số với sự can thiệp tối thiểu của chuyên gia học máy."
      },
      {
        "term": "FLAML (Fast and Lightweight AutoML)",
        "definition": "Thư viện học máy tự động nhanh và nhẹ của Microsoft Research, tối ưu hóa chi phí tìm kiếm mô hình chính xác dưới giới hạn thời gian tính toán."
      },
      {
        "term": "CFO (Cost-Frugal Optimization)",
        "definition": "Chiến lược tối ưu hóa tiết kiệm chi phí trong FLAML, bắt đầu từ các cấu hình mô hình chi phí thấp và dần nâng độ phức tạp khi có sự cải thiện hiệu năng."
      },
      {
        "term": "BlendSearch",
        "definition": "Thuật toán tìm kiếm kết hợp thăm dò toàn cục (global exploration) và tối ưu hóa cục bộ (local optimization) nhằm giảm chi phí tính toán tìm kiếm siêu tham số."
      },
      {
        "term": "COD-in (Influent Chemical Oxygen Demand)",
        "definition": "Nhu cầu oxy hóa học của nước thải đầu vào (mg/L), đặc trưng tải lượng hữu cơ nạp vào hệ thống và là biến quan trọng nhất dự đoán COD-re."
      },
      {
        "term": "COD-re (COD Removal Rate)",
        "definition": "Hiệu suất loại bỏ COD (%), biến mục tiêu dự đoán phản ánh hiệu quả xử lý chất hữu cơ của hệ thống AnMBR."
      },
      {
        "term": "OD (Operation Days)",
        "definition": "Số ngày vận hành liên tục của bể phản ứng (ngày), biến đại diện (proxy) cho động học tích lũy theo thời gian của màng sinh học và quá trình tắc nghẽn màng."
      },
      {
        "term": "ORP (Oxidation-Reduction Potential)",
        "definition": "Thế oxy hóa - khử (mV), chỉ số phản ánh trạng thái kỵ khí nghiêm ngặt của hỗn hợp bùn sinh học."
      },
      {
        "term": "HRT (Hydraulic Retention Time)",
        "definition": "Thời gian lưu thủy lực (giờ), thời gian lưu của nước thải trong bể (4–24 h cho AnMBR1, 10–24 h cho AnMBR2)."
      },
      {
        "term": "MLSS (Mixed Liquor Suspended Solids)",
        "definition": "Nồng độ chất rắn lơ lửng trong bùn lỏng (mg/L), đại diện cho tổng sinh khối và chất rắn trong bể."
      },
      {
        "term": "MLVSS (Mixed Liquor Volatile Suspended Solids)",
        "definition": "Nồng độ chất rắn lơ lửng dễ bay hơi (mg/L), chỉ thị trực tiếp hàm lượng sinh khối vi sinh vật hoạt tính."
      },
      {
        "term": "Tree-based Models",
        "definition": "Các mô hình học máy họ cây (Random Forest, Extra Trees, LightGBM, XGBoost, CatBoost), vượt trội so với mạng nơ-ron trên dữ liệu bảng kích thước nhỏ."
      },
      {
        "term": "Deep Neural Networks (DNNs)",
        "definition": "Các mạng nơ-ron sâu (FCN, CNN, DenseNet) từng được thử nghiệm nhưng gặp hiện tượng quá khớp nặng trên dữ liệu mẫu nhỏ dẫn đến R2 âm."
      },
      {
        "term": "Bland-Altman Analysis",
        "definition": "Phương pháp thống kê phân tích sự tương đồng giữa giá trị dự đoán và thực đo qua sai số trung bình (bias) và giới hạn thỏa thuận 95%."
      },
      {
        "term": "Distribution Shift",
        "definition": "Hiện tượng dịch chuyển phân phối thống kê giữa tập dữ liệu gốc M1 (185 mẫu) và tập mở rộng M2 (320 mẫu) làm suy giảm độ chính xác mô hình."
      },
      {
        "term": "Ensemble Feature Ranking Score",
        "definition": "Điểm xếp hạng đặc trưng kết hợp chuẩn hóa thứ tự từ Tree-based, Permutation và SHAP để so sánh nhất quán mức độ quan trọng giữa các phương pháp giải thích."
      },
      {
        "term": "Ablation Study",
        "definition": "Nghiên cứu triệt tiêu đánh giá định lượng đóng góp của từng nhóm biến đặc trưng và tập dữ liệu lên hiệu năng mô hình."
      }
    ],
    "key_entities": [
      "FLAML (Fast and Lightweight AutoML)",
      "Microsoft Research",
      "XGBoost",
      "LightGBM",
      "CatBoost",
      "Random Forest (RF)",
      "Extra Trees",
      "Fully Connected Network (FCN)",
      "Convolutional Neural Network (CNN)",
      "DenseNet (Densely Connected Convolutional Network)",
      "AnMBR1 (Membrane pore size 0.4 µm)",
      "AnMBR2 (Membrane pore size 0.05 µm)"
    ]
  },
  "global_context_pack": "# Global Context Pack: Empowerment of Accurate Modeling of Anaerobic Membrane Bioreactors by Automated Machine Learning\n\n## Core Thesis\nNghiên cứu ứng dụng học máy tự động (FLAML AutoML) để mô hình hóa chính xác hiệu suất loại bỏ COD (COD-re) của hệ phản ứng màng sinh học kỵ khí (AnMBR) xử lý nước thải đô thị từ tập dữ liệu thực nghiệm nhỏ (185 mẫu), chứng minh hiệu quả vượt trội so với mạng nơ-ron sâu (R^2 đạt 0.47, MAPE 3.11%), làm rõ vai trò cải thiện hiệu năng của biến thời gian vận hành (OD, nâng R^2 lên 0.55), phát hiện hiện tượng suy giảm hiệu năng do dịch chuyển phân phối khi tăng kích thước dữ liệu không qua sàng lọc, và đề xuất khung xếp hạng đặc trưng kết hợp (Ensemble Ranking Score) xác định COD đầu vào (COD-in) là nhân tố chi phối hàng đầu.\n\n## Output Language Policy\nVietnamese. Keep English technical terms as written, and add Vietnamese translations in parentheses on first use. Wrap all mathematical symbols, equations, and units in KaTeX format.\n\n## Key Terminology and Acronyms\n- **AnMBR (Anaerobic Membrane Bioreactor / Bể phản ứng màng sinh học kỵ khí)**: Combines anaerobic digestion with membrane filtration for low-energy wastewater treatment, low sludge production, and biogas recovery.\n- **AutoML (Automated Machine Learning / Học máy tự động)**: Automated framework for algorithm selection and hyperparameter optimization.\n- **FLAML (Fast and Lightweight AutoML)**: Microsoft Research library utilizing CFO and BlendSearch for cost-effective pipeline tuning.\n- **CFO (Cost-Frugal Optimization)**: Strategy prioritizing low-cost configurations before exploring complex model spaces.\n- **BlendSearch**: Blended search combining global exploration and local optimization.\n- **Key Features & Targets**:\n  - COD-in: Influent chemical oxygen demand ($mg/L$), dominant predictor.\n  - COD-re: Target COD removal rate (%).\n  - OD: Operation days ($d$), proxy feature capturing microbial biofilm dynamic succession and membrane fouling.\n  - Operational parameters: T-R (reactor temp, $^{\\circ}\\text{C}$), T-in (influent temp, $^{\\circ}\\text{C}$), T-env (ambient temp, $^{\\circ}\\text{C}$), pH-in, flux ($LMH$), ORP ($mV$), HRT ($h$), MLSS ($mg/L$), MLVSS ($mg/L$).\n- **Models**:\n  - Tree-based: Random Forest (RF), Extra Trees (EDT), LightGBM, XGBoost, CatBoost.\n  - Deep Learning benchmarks: Fully Connected Network (FCN), Convolutional Neural Network (CNN), DenseNet.\n- **Evaluation & Interpretation**:\n  - Metrics: $R^2$, $\\text{MAE}$, $\\text{RMSE}$, $\\text{MAPE}$.\n  - Bland-Altman analysis: Mean error and $95\\%$ limits of agreement ($\\mu \\pm 1.96\\sigma$).\n  - Ensemble Feature Ranking Score: Unified ranking combining Tree-based Gini importance, Permutation importance, and SHAP.\n\n## Section Overview\n- **Abstract**: Research background, breakthrough of AutoML over deep learning models on small datasets, impact of OD and data volume, and primary feature identification.\n- **1. Introduction**: Freshwater scarcity, activated sludge and AnMBR potential, laboratory experiment constraints, data-driven modeling bottlenecks, and motivation for applying AutoML.\n- **2. Methods**:\n  - 2.1 Data: Lab-scale AnMBR1 and AnMBR2 operation, dataset composition (M1: 185 samples, M2: 320 samples), and feature definitions.\n  - 2.2 Modeling: FLAML formulation, CFO, BlendSearch, and candidate model families.\n  - 2.3 Evaluation: Metrics ($R^2$, $\\text{MAE}$, $\\text{RMSE}$, $\\text{MAPE}$) and Bland-Altman formulation.\n  - 2.4 Ablation studies: Design of feature addition experiments and dataset expansion tests.\n  - 2.5 Feature ranking score: Formulation and rank normalization of Tree-based, Permutation, and SHAP methods.\n- **3. Results and discussion**:\n  - 3.1 AutoML for efficient AnMBR modeling: Superiority of AutoML ($R^2 = 0.47$, $\\text{MAPE} = 3.11\\%$) over FCN, CNN, and DenseNet ($R^2 < 0$), with narrower Bland-Altman agreement limits.\n  - 3.2 Improved ML performance with operation time as a feature: Adding OD increases $R^2$ to $0.55$, demonstrating its role as a key proxy for system dynamics.\n  - 3.3 Impact of data volume on predictive performance: Integrating uncurated additional data degrades performance due to distribution shift across distinct operating phases.\n  - 3.4 Ensemble feature-based importance analysis: COD-in identified as the most critical feature, followed by OD, temperature, and hydraulic variables.\n  - 3.5 Limitations and future perspectives: Small dataset extrapolation boundaries, need for multi-source integration, and autonomous operations.\n- **4. Conclusions**: Summary of AutoML effectiveness, ablation findings, and recommendations for wastewater AI modeling.\n"
}

out_file = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\branche_v2\empowerment_of_accurate_modeling_of\skeleton.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(skeleton, f, indent=2, ensure_ascii=False)
print("skeleton.json written cleanly.")
