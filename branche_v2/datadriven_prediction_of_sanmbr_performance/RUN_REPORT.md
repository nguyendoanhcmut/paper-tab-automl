# Execution Run Report: datadriven_prediction_of_sanmbr_performance

## Document Details
- **Title**: Data-Driven Prediction of SAnMBR Performance under Phenolic Shock Loads: A Comparative Machine Learning Study
- **Doc Slug**: `datadriven_prediction_of_sanmbr_performance`
- **Doc Type**: `paper`
- **Domain**: `general`
- **Output Language**: Vietnamese (technical terms in English)

## Pipeline Phases Summary
| Phase | Description | Status | Details |
|---|---|---|---|
| **Phase 1: Extract** | Text & figure extraction from PDF | Completed | 17 pages text extracted, 14 figures extracted to assets/ |
| **Phase 2: Page Images** | High-res page rasterization | N/A | Scientific paper without exercises / slides |
| **Phase 3: Scout** | Structure discovery & routing table | Completed | 13 chunks configured in routing table with 14 assigned figures |
| **Phase 4: Drill** | Section subtree generation | Completed | 13 fragments drilled according to `branch_driller_prompt.md` with KaTeX math/chem and real experimental values |
| **Phase 5: Merge** | Fragment assembly into unified tree | Completed | `merge_fragments.py` executed successfully, single H1 root, 22 headings, 427 lines |
| **Phase 6: Audit** | Lineage & structure validation | Completed | `verify_lineage.py` PASSED with 0 errors and 0 warnings |
| **Phase 7: Render** | Markmap HTML rendering | Completed | `compile_mindmap.js` compiled 343 nodes (97 KaTeX math nodes), size 110.4 KB |
| **Phase 8: Report** | Pipeline documentation & closure | Completed | Documented in `RUN_REPORT.md` and communicated to parent agent |

## Verification Statistics
- **Total Headings**: 22 (1 H1, 4 H2, 11 H3, 6 H4)
- **Total Tree Lines**: 427 lines
- **Total Markmap Nodes**: 343 nodes (97 KaTeX math nodes)
- **Figures Embedded**: 14 / 14 (100% coverage, each <= 10 lines, anchored under claim bullets)
- **Lineage Verification**: `PASSED` (0 errors, 0 warnings)
- **Banned Buzzwords**: 0
- **HTML Artifact**: `datadriven_prediction_of_sanmbr_performance_branches.html` (113,031 bytes)
- **Markdown Artifact**: `datadriven_prediction_of_sanmbr_performance_branches.md` (30,551 bytes)
