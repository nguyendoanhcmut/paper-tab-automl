# Paper Tab AutoML: Research Hub and Knowledge Trees

This repository contains 18 peer-reviewed research papers on machine learning in water and wastewater engineering. The collection spans 282 pages, 133 extracted figures, and verified knowledge trees.

## Core Summary

Water and wastewater treatment facilities face strict effluent limits and variable process conditions. Machine learning models predict system states and optimize operational controls. This repository organizes 18 key studies into structured knowledge trees and interactive mind maps.

Summary metrics:
- Total research papers: 18
- Total reviewed pages: 282
- Total extracted figures: 133
- Lineage verification rate: 100%
- Completeness audit score: C >= 0.95 across all papers

## Master Research Table

The table below lists all 18 papers with model architectures, target variables, and performance metrics.

| ID | Paper Title | Category / Domain | Machine Learning Models | Target Variable | Evaluation Metrics | Pages | Figures | Year | Journal |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| #01 | An Interpretable Artificial Intelligence Framework for Defining the Operational Basin of Full-Scale Membrane Bioreactors in Semiconductor Wastewater Treatment | AutoML & MBR Digital Twins | Extra Trees, XGBoost, LightGBM, Random Forest | TMP, Permeate Flow, Tank Water Level | R² > 0.94, 41.4% feasibility window | 17 | 11 | 2026 | Water Research |
| #02 | Automated Machine Learning and SHAP-Based Interpretation of PFOA Removal via Electrochemical Oxidation | AutoML & MBR Digital Twins | FLAML-optimized XGBoost, Random Forest, Extra Trees | PFOA Removal Efficiency (%) | R² = 0.92, RMSE = 4.31% | 9 | 4 | 2025 | J. Environ. Chem. Eng. |
| #03 | Chemometric Analysis for River Water Quality Assessment at the Intake of Drinking Water Treatment Plants | Surface Water Quality | Principal Component Analysis (PCA), Cluster Analysis (HCA) | Multi-sensor alignment, anomaly detection | PC1-3 capture > 78% variance | 10 | 7 | 2019 | Sci. Total Environ. |
| #04 | Elucidating Response Effects of Anammox-Based Nitrogen Removal Processes for Municipal Wastewater Using Big Data Analysis and Automated Machine Learning | AutoML & MBR Digital Twins | Auto-Sklearn, Gradient Boosting, CatBoost | Nitrogen Removal Rate, Effluent NH₄⁺-N | R² = 0.91, MAE = 1.82 mg/L | 16 | 5 | 2026 | Scientific Reports |
| #05 | Empowerment of Accurate Modeling of Anaerobic Membrane Bioreactors by Automated Machine Learning | AutoML & MBR Digital Twins | AutoML Automated Pipeline vs Deep Neural Networks | COD Removal Rate (%) | MAPE = 3.11% | 10 | 7 | 2026 | Bioresource Technol. |
| #06 | Explainable Cross-Plant Transfer Learning for Fouling Prediction in Data-Limited Pilot-Scale Membrane Bioreactors | AutoML & MBR Digital Twins | Transfer Learning, CatBoost, XGBoost | Membrane Fouling Rate (dTMP/dt) | Transfer R² = 0.88 with 15% target data | 14 | 8 | 2026 | J. Membr. Sci. |
| #07 | Interpretable Prediction of Coagulant Dosage in Drinking Water Treatment Plant Based on Automated Machine Learning and SHAP Method | Coagulation & DAF Systems | TPOT, LightGBM, TreeSHAP | Optimal Coagulant Dosage (mg/L) | R² = 0.952, RMSE = 1.14 mg/L | 11 | 8 | 2025 | Chem. Eng. J. |
| #08 | Machine Learning for Membrane Bioreactor Research: Principles, Methods, Applications, and a Tutorial | AutoML & MBR Digital Twins | Systematic Review: SVM, Random Forest, ANN | Filtration resistance, cake layer fouling | Meta-analysis of regression accuracy | 26 | 5 | 2024 | Front. Environ. Sci. Eng. |
| #09 | Predicting Nitrification Status in Aerobic Membrane Bioreactors by Interpretable Machine Learning Models | AutoML & MBR Digital Twins | Random Forest, Decision Trees, Ridge Regression | Nitrification Status, Effluent NH₄⁺-N | Accuracy = 96.4%, F1 = 0.95 | 16 | 6 | 2025 | Water Research |
| #10 | Predictive Framework for Membrane Fouling in Full-Scale Membrane Bioreactors: Integrating AI-Driven Feature Engineering and Explainable AI | AutoML & MBR Digital Twins | AutoFE, LightGBM, XGBoost, SHAP | Transmembrane Pressure (TMP) Progression | R² = 0.967, 7-day RMSE < 1.8 kPa | 26 | 8 | 2025 | MDPI Membranes |
| #11 | Wastewater Membrane Bioreactors: A Review of Explainable Artificial Intelligence and Digital Twin Applications | AutoML & MBR Digital Twins | SHAP, LIME, PDP, Physics-Informed Neural Networks | Digital twin fidelity, real-time control | Synthesis across industrial deployments | 26 | 3 | 2026 | MDPI Water |
| #12 | Data-Driven Prediction of SAnMBR Performance under Phenolic Shock Loads: A Comparative Machine Learning Study | AutoML & MBR Digital Twins | SVR (RBF Kernel), MLP, Random Forest, XGBoost | COD Removal, Effluent Quality | R² = 0.955 (SVR), RMSE = 18.2 mg/L | 17 | 14 | 2026 | Water Process Eng. |
| #13 | Enhanced Nitrogen Prediction and Mechanistic Process Analysis in High-Salinity Wastewater Treatment Using Interpretable Machine Learning Approach | High-Salinity Wastewater | CatBoost, Bayesian Optimization, Cross-Validation | Effluent NH₄⁺-N and Total Nitrogen | Test R² = 0.88 (NH₄⁺-N) and 0.91 (TN) | 10 | 5 | 2025 | Bioresource Technol. |
| #14 | Explainable AutoML-Driven Surface Water Quality Classification with Key Indicators Identification | Surface Water Quality | AutoML (LightGBM, XGBoost, Random Forest), SHAP | 5-Tier Water Quality Grade (Grades I to V) | Accuracy > 93.5%, Macro F1 = 0.912 | 11 | 8 | 2025 | Environ. Pollut. |
| #15 | Feature-Engineered Machine Learning for Daily-Scale Prediction of Effluent Total Phosphorus and Coagulant Dosing Optimization in Full-Scale DAF Systems | Coagulation & DAF Systems | XGBoost, MICE Imputation, Time-Lag Features | Effluent Total Phosphorus, Coagulant Dose | Test R² = 0.84, 18.3% chemical savings | 21 | 10 | 2026 | Chem. Eng. J. |
| #16 | Knowledge-Based Feature Selection Substantially Enhances Data-Driven Wastewater Treatment Modeling | Knowledge-Based Feature Selection KBFS | KBFS, XGBoost, Random Forest, Non-Linear Models | N₂O Emissions, Effluent Nitrate | 34.2% error drop, 2.1x seasonal gain | 13 | 5 | 2026 | Water Research |
| #17 | Maximizing Nitrogen Removal in a Membrane Bioreactor via Swing-Basin and Dissolved Oxygen Reduction: A Bio-Inspired Machine Learning Optimization Approach | AutoML & MBR Digital Twins | Neural Networks (ANN), Genetic Algorithms, PSO | Total Nitrogen Removal, Aeration DO Energy | TN dropped to 7.8 mg/L, energy cut 22.4% | 17 | 10 | 2026 | Desalination |
| #18 | Recognizing the State of Aerobic Granular Sludge over Its Life-Cycle in a Continuous-Flow Membrane Bioreactor with an Artificial Intelligence Approach | Aerobic Granular Sludge AGS & Vision AI | YOLOv8 Vision Model, t-SNE Clustering, SHAP | 4 Morphological Sludge States | mAP50 = 0.942, classification > 96.0% | 12 | 9 | 2025 | Bioresource Technol. |

## Thematic Domain Taxonomy

The library organizes the 18 papers into six distinct research domains.

### 1. AutoML and MBR Digital Twins
This domain covers membrane bioreactor operation and automated model optimization. Papers study transmembrane pressure increase, foulant accumulation, and biological degradation rates.
- Papers: #01, #02, #04, #05, #06, #08, #09, #10, #11, #12, #17
- Key models: Extra Trees, XGBoost, CatBoost, LightGBM, and Artificial Neural Networks
- Primary targets: Transmembrane pressure, chemical oxygen demand, and nitrogen removal

### 2. High-Salinity Wastewater
This domain studies biological nitrogen removal under elevated salinity and high osmotic pressure.
- Papers: #13
- Key models: CatBoost with Bayesian optimization and 10-fold cross-validation
- Primary targets: Effluent ammonium and total nitrogen concentrations

### 3. Surface Water Quality
This domain addresses river water quality assessment, sensor data alignment, and regulatory standard classification.
- Papers: #03, #14
- Key models: Principal component analysis, hierarchical cluster analysis, and ensemble tree models
- Primary targets: Multi-sensor physicochemical alignment and five-tier river water quality grades

### 4. Coagulation and DAF Systems
This domain focuses on automated coagulant dosing in water clarification and dissolved air flotation units.
- Papers: #07, #15
- Key models: Tree-based pipelines, TPOT automated optimization, and time-lag feature models
- Primary targets: Coagulant chemical dosage and effluent total phosphorus concentrations

### 5. Knowledge-Based Feature Selection (KBFS)
This domain integrates biological domain knowledge into feature engineering routines. Models predict biological nutrient removal and greenhouse gas emissions.
- Papers: #16
- Key models: Domain-guided feature selection algorithms coupled with gradient boosted trees
- Primary targets: Nitrous oxide emissions and effluent nitrate concentrations

### 6. Aerobic Granular Sludge (AGS) and Vision AI
This domain applies computer vision to identify granular sludge morphology during continuous-flow operations.
- Papers: #18
- Key models: YOLOv8 object detection, t-SNE dimensional reduction, and Shapley feature attribution
- Primary targets: Four morphological granule stages, granule size distribution, and disintegration events

## Web Research Hub Overview

The project includes an interactive web application to examine the library.

### Visual Styling and Typography
- Palette: Warm Charcoal base (`#121110`, `#1a1816`) with Terracotta Red accents (`#c2410c`, `#ea580c`).
- Font family: Geist Sans for clean text hierarchy and Geist Mono for technical metrics and IDs.
- Numbered badges: Orange monospace badges (`#01` to `#18`) tag every paper card and modal reader header.

### Four-Tab Interactive Reader Suite
The reader modal displays four integrated views for each paper:
1. Mind Map Tab: Renders an interactive Markmap diagram with zoom, pan, and collapsible nodes.
2. Knowledge Tree Tab: Shows the full Markdown tree with mathematical equations rendered via KaTeX.
3. Figures Gallery Tab: Displays all high-resolution figures with complete captions and full lightbox view.
4. Benchmarks Tab: Details model architectures, training hyperparameters, and validation results.

## Lineage and Verification Guarantee

Every knowledge tree in this repository passed a four-gate verification audit.

The four audit gates verify:
1. Gate 1 (Coverage): Confirms over 95% section and data coverage from original source texts.
2. Gate 2 (Depth): Enforces recursive decomposition from level 3 down to level 6 sub-nodes.
3. Gate 3 (Grounding): Preserves exact numerical values, formulas, and units without hallucination.
4. Gate 4 (Lexicon): Retains environmental engineering and machine learning technical terms.

Audit results:
- Completeness score: C >= 0.95 across all 18 papers
- Verification defects: 0 defects across all 18 papers
- Lineage check: 100% verified against original publisher publications

## Local Quickstart

Complete these steps to run the research hub on your local machine.

### 1. Clone the Repository
Clone this repository to your local computer:
```bash
git clone https://github.com/nguyenduchoanganh/paper-tab-automl.git
cd paper-tab-automl
```

### 2. Start a Local Web Server
Start a lightweight HTTP server with Python:
```bash
python -m http.server 8000
```

### 3. Open the Research Hub
Open your browser and navigate to:
```
http://localhost:8000
```

You can switch between Grid View and List View. You can also filter papers by domain or search by model name.

## Directory Structure

```
paper-tab-automl/
├── index.html                           # Main web research hub interface
├── README.md                            # Documentation and master index
├── branche_v2/                          # Research papers knowledge repository
│   ├── papers_catalog.json              # Complete catalog metadata for 18 papers
│   ├── <paper_slug>/                    # Paper directories
│   │   ├── <slug>_branches.html         # Interactive Markmap HTML mind map
│   │   ├── <slug>_branches.md           # Full Markdown knowledge tree
│   │   ├── figures_manifest.json        # Figure metadata and captions
│   │   └── assets/                      # Extracted figures and diagrams
│   └── translate/                       # Bilingual and translated documents
```

## Citation and License

Original research papers remain the intellectual property of their respective publishers (Elsevier, Nature Portfolio, Springer, MDPI). Knowledge trees and visual interfaces belong to this repository under open academic research use.
