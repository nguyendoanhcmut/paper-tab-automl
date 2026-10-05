# Execution Run Report: recognizing_the_state_of_aerobic

## Document Details
- **Title**: Recognizing the state of aerobic granular sludge over its life-cycle in a continuous-flow membrane bioreactor with an artificial intelligence approach
- **Doc Slug**: `recognizing_the_state_of_aerobic`
- **Doc Type**: `paper`
- **Domain**: `general`
- **Output Language**: Vietnamese (technical terms in English)

## Pipeline Phases Summary
| Phase | Description | Status | Details |
|---|---|---|---|
| **Phase 1: Extract** | Text & figure extraction from PDF | Completed | 12 pages text extracted, 9 figures extracted to assets/ |
| **Phase 2: Page Images** | High-res page rasterization | N/A | Scientific paper without exercise page crops |
| **Phase 3: Scout** | Structure discovery & routing | Completed | 16 chunks routed in manifest |
| **Phase 4: Drill** | Section subtree generation | Completed | 16 fragments synthesized with KaTeX formulas and exact figure evidence blocks |
| **Phase 5: Merge** | Fragment assembly into unified tree | Completed | `merge_fragments.py` executed successfully (373 lines, 19 headings) |
| **Phase 6: Audit** | Lineage & structure validation | Completed | `verify_lineage.py` PASSED with 0 errors and 0 warnings |
| **Phase 7: Render** | Markmap HTML rendering | Completed | `compile_mindmap.js` generated interactive HTML (332 nodes, 70 KaTeX math nodes, 107.5 KB) |
| **Phase 8: Report** | Pipeline documentation & closure | Completed | Generated `RUN_REPORT.md` |

## Statistics
- **Total Headings**: 19
- **Figures Embedded**: 9 / 9 (100% coverage, all nested under claim anchors)
  - `fig_01`: Neo vào mục 2.2 Data collection and feature classification
  - `fig_02`: Neo vào mục 2.3 Machine learning model
  - `fig_03`: Neo vào mục 3.1 Model training and testing
  - `fig_04`: Neo vào mục 3.2 Confusion matrix
  - `fig_05`: Neo vào mục 3.3 Analysis of the model evaluation parameter
  - `fig_06`: Neo vào mục 3.4 Cluster analysis
  - `fig_07`: Neo vào mục 3.5 SHAP
  - `fig_08`: Neo vào mục 3.6 Model prediction and statistics
  - `fig_09`: Neo vào mục 3.6 Model prediction and statistics
- **Lineage Verification**: `LINEAGE PASSED` (0 errors, 0 warnings)
- **Mindmap File**: `recognizing_the_state_of_aerobic_branches.html`
