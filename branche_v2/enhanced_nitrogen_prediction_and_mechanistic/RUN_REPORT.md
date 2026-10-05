# Execution Run Report: enhanced_nitrogen_prediction_and_mechanistic

## Document Details
- **Title**: Enhanced nitrogen prediction and mechanistic process analysis in high-salinity wastewater treatment using interpretable machine learning approach
- **Doc Slug**: `enhanced_nitrogen_prediction_and_mechanistic`
- **Doc Type**: `paper`
- **Domain**: `general`
- **Output Language**: Vietnamese (technical terms preserved in English)
- **Path**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/enhanced_nitrogen_prediction_and_mechanistic`

## Pipeline Phases Summary
| Phase | Description | Status | Details |
|---|---|---|---|
| **Phase 1: Extract** | Text & figure extraction from PDF | Completed | 10 pages extracted to text, 5 figures extracted to `assets/` |
| **Phase 2: Page Images** | High-res page rasterization | N/A | Scientific paper without exercise page crops |
| **Phase 3: Scout** | Structure discovery & routing | Completed | 14 chunks routed in `enhanced_nitrogen_prediction_and_mechanistic_scout_manifest.json` |
| **Phase 4: Drill** | Section subtree generation | Completed | 14 fragments synthesized strictly per `branch_driller_prompt.md`, restoring all H4 sections (2.3.1–2.3.4 & 3.1.1–3.1.2) |
| **Phase 5: Merge** | Fragment assembly into unified tree | Completed | `merge_fragments.py` executed successfully into `enhanced_nitrogen_prediction_and_mechanistic_branches.md` (342 lines, 23 headings) |
| **Phase 6: Audit** | Lineage & structure validation | Completed | `verify_lineage.py` passed with **0 errors and 0 warnings** (`LINEAGE PASSED`) |
| **Phase 7: Render** | Markmap HTML rendering | Completed | `compile_mindmap.js` compiled 294 nodes (159 KaTeX nodes) into 119.8 KB standalone HTML |
| **Phase 8: Report** | Pipeline documentation & closure | Completed | Documented run report and communicated results to parent orchestrator |

## Experimental & Mechanistic Validation
- **Model Hierarchy**: CatBoost outperformed 5 benchmark models (LightGBM, Random Forest, XGBoost, GBDT, AdaBoost).
- **Exact Metrics**:
  - Test set $NH_4^+\text{-N}_{out}$: $R^2 = 0.88$, $RMSE = 4.27\ \text{mg/L}$
  - Test set $TN_{out}$: $R^2 = 0.91$, $RMSE = 4.35\ \text{mg/L}$
  - 10-fold CV: $R^2 = 0.78 \pm 0.09$ ($NH_4^+\text{-N}_{out}$), $0.86 \pm 0.06$ ($TN_{out}$)
  - Input Features: 13 variables including $NO_3^-\text{-N}_{out}$ as input feature
  - Target Outputs: 2 variables ($NH_4^+\text{-N}_{out}$ and $TN_{out}$)
- **Figures Verification**:
  - Fig. 1 (`assets/fig_01_p3.jpeg`): MBR experimental apparatus schematic (Section 2.1)
  - Fig. 2 (`assets/fig_02_p4.jpeg`): Feature distributions, correlation heatmap, and 10-fold CV results (Section 2.3.4)
  - Fig. 3 (`assets/fig_03_p6.jpeg`): Global SHAP summary feature importance (Section 3.2)
  - Fig. 4 (`assets/fig_04_p7.jpeg`): Local SHAP explanations - Force plots (a-b) and Waterfall plots (c-d) (Section 3.3)
  - Fig. 5 (`assets/fig_05_p8.jpeg`): Partial dependence plots (PDP) across 12 panels (Section 3.4)
  - All figure evidence blocks $\le 5$ lines ($\le 10$ limit), figure share $< 38\%$ per section ($< 50\%$ threshold), 0 banned buzzwords.

## Output Files
- Primary Tree: `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/enhanced_nitrogen_prediction_and_mechanistic/enhanced_nitrogen_prediction_and_mechanistic_branches.md`
- Interactive Mind Map: `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/enhanced_nitrogen_prediction_and_mechanistic/enhanced_nitrogen_prediction_and_mechanistic_branches.html`
- Manifest: `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/enhanced_nitrogen_prediction_and_mechanistic/enhanced_nitrogen_prediction_and_mechanistic_scout_manifest.json`
- Figures Manifest: `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/enhanced_nitrogen_prediction_and_mechanistic/figures_manifest.json`
