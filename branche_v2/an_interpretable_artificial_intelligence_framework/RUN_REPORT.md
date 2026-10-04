# Execution Run Report: an_interpretable_artificial_intelligence_framework

## Document Details
- **Title**: An interpretable artificial intelligence framework for defining the operational basin of full-scale membrane bioreactors in semiconductor wastewater treatment
- **Doc Slug**: `an_interpretable_artificial_intelligence_framework`
- **Doc Type**: `paper`
- **Domain**: `general`
- **Output Language**: Vietnamese (technical terms in English)

## Pipeline Phases Summary

| Phase | Description | Status | Details / Timings |
|---|---|---|---|
| **Phase 1: Extract** | Text & figure extraction from PDF | Pre-completed | Text extracted to `an_interpretable_artificial_intelligence_framework.txt`, 11 figures extracted to `assets/` |
| **Phase 2: Page Images** | High-res page rasterization | N/A | Scientific paper without exercise page crops |
| **Phase 3: Scout** | Structure discovery & routing | Completed | Subagent `branch_scout` (`b2cbe7e6-ddef-4192-9fb4-677278e88dd8`). Generated 21 chunks, 33 sections, 11 figures. |
| **Phase 4: Drill** | Parallel section drilling | Completed | 21 `branch_driller` subagents executed concurrently in a single call. All fragments generated to `fragments/`. |
| **Phase 5: Merge** | Fragment assembly into unified tree | Completed | `merge_fragments.py` executed successfully. 838 lines, 36 headings. |
| **Phase 6: Audit** | Lineage & structure validation | Completed | `verify_lineage.py` PASSED with 0 errors, 0 warnings. |
| **Phase 7: Render** | Markmap HTML rendering | Completed | `compile_mindmap.js` created 174 KB interactive HTML with KaTeX and theme toggle. 672 nodes, 274 math nodes. |
| **Phase 8: Report** | Pipeline documentation & closure | Completed | Generated `RUN_REPORT.md`. |

## Statistics
- **Total Headings**: 36 (1 H1, 5 H2, 17 H3, 13 H4)
- **Figures Embedded**: 11 / 11 (100% coverage, all nested under claim anchors with evidence blocks <= 10 lines)
- **Exercises**: 0 (0 passed)
- **Completeness**: 1.0 (100%)
- **Lineage Verification**: `PASSED` (0 errors, 0 warnings)
- **Warnings**: 0

## Deliverables
- **Markdown Branches**: `C:\antgravity workplace\ML\PAPER TAB AUTOML\branche_v2\an_interpretable_artificial_intelligence_framework\an_interpretable_artificial_intelligence_framework_branches.md`
- **Rendered Mindmap HTML**: `C:\antgravity workplace\ML\PAPER TAB AUTOML\branche_v2\an_interpretable_artificial_intelligence_framework\an_interpretable_artificial_intelligence_framework_branches.html`
- **Scout Manifest**: `C:\antgravity workplace\ML\PAPER TAB AUTOML\branche_v2\an_interpretable_artificial_intelligence_framework\an_interpretable_artificial_intelligence_framework_scout_manifest.json`
