# RUN_REPORT: interpretable_prediction_coagulant_dosage_automl_v2

## Document Overview
- **Document Title**: Interpretable prediction of coagulant dosage in drinking water treatment plant based on automated machine learning and SHAP method
- **Document Slug**: interpretable_prediction_coagulant_dosage_automl_v2
- **Document Type**: paper
- **Domain**: general
- **Language**: Vietnamese (technical terms in English with Vietnamese in parentheses)
- **Primary Markdown**: `C:\antgravity workplace\ML\PAPER TAB AUTOML\interpretable_prediction_coagulant_dosage_automl_v2\interpretable_prediction_coagulant_dosage_automl_v2_branches.md`
- **Rendered HTML**: `C:\antgravity workplace\ML\PAPER TAB AUTOML\interpretable_prediction_coagulant_dosage_automl_v2\interpretable_prediction_coagulant_dosage_automl_v2_branches.html`

## Phase Timings

| Phase | Start Time | End Time | Duration |
|---|---|---|---|
| Phase 1: Extract | 2026-10-04 08:55:33 | 2026-10-04 08:56:17 | 44 s |
| Phase 2: Scout | 2026-10-04 08:56:17 | 2026-10-04 09:13:55 | 17 min 38 s |
| Phase 3: Page images | 2026-10-04 09:13:55 | 2026-10-04 09:13:55 | 0 s (skipped, 0 exercises) |
| Phase 4: Drill | 2026-10-04 09:15:02 | 2026-10-04 09:33:23 | 18 min 21 s |
| Phase 5: Merge | 2026-10-04 09:33:23 | 2026-10-04 09:40:33 | 7 min 10 s |
| Phase 6: Audit | 2026-10-04 09:40:33 | 2026-10-04 09:47:26 | 6 min 53 s |
| Phase 7: Render | 2026-10-04 09:47:26 | 2026-10-04 09:47:47 | 21 s |
| Phase 8: Report | 2026-10-04 09:47:47 | 2026-10-04 09:48:10 | 23 s |

## Subagents Invoked

| Subagent Type | Count |
|---|---|
| `branch_scout` | 1 |
| `branch_driller` | 7 |
| `figure_driller` | 8 |
| `exercise_driller` | 0 |
| `exercise_verifier` | 0 |
| `fragment_verifier` | 7 |
| `branch_merger` | 1 |
| `branch_verifier` | 1 |
| **Total Subagents** | **25** |

## Verification Scores

### Fragment Verifier (FV) Scores
- `ch01` (Abstract): 1.0 (Numbers matched: 10/10, Claims covered: 13/13)
- `ch02` (1 Introduction): 1.0 (Numbers matched: 4/4, Claims covered: 17/17)
- `ch03` (2 Materials and methods): 1.0 (Numbers matched: 16/16, Claims covered: 16/16, Figures: 1/1)
- `ch04_1` (3.1 Analysis of water quality data and feature selection): 1.0 (Numbers matched: 23/23, Claims covered: 15/15, Figures: 2/2)
- `ch04_2` (3.2 Model comparison and optimization): 1.0 (Numbers matched: 23/23, Claims covered: 18/18, Figures: 2/2)
- `ch04_3` (3.3 SHAP interpretation): 1.0 (Numbers matched: 23/23, Claims covered: 21/21, Figures: 3/3)
- `ch05` (4 Conclusions): 1.0 (Numbers matched: 8/8, Claims covered: 12/12)

### Completeness Audit
- Section coverage: 1.0 (12 observed of 12 expected sections)
- Depth score: 1.0 (6 compliant of 6 applicable sections)
- Grounding score: 1.0 (265 grounded of 265 leaf bullets)
- Lexicon score: 1.0 (20 resolved of 20 declared key terms)
- **Total Completeness Score**: **1.0**

### Lineage Audit
- Script: `verify_lineage.py`
- Result: **LINEAGE PASSED**
- Errors: 0
- Warnings: 0

### Tree Metrics
- Total Headings: 13 (1 H1, 5 H2, 7 H3)
- Embedded Figures: 8 (100% anchored under claims)
- Exercises: 0 (0 passed)

## Skill Problems

1. **File**: `C:\Users\Admin\.gemini\config\skills\branches\SKILL.md`
   - **Section**: Subagents
   - **Problem**: Instruction specifies "Register each with define_subagent, using the prompt file as the system prompt". Main agent must not read other prompt files into context.
   - **What was done**: Provided instructions in `system_prompt` directing each subagent to view its own prompt file via `view_file` at start, protecting orchestrator context while enforcing exact subagent roles.

2. **File**: `C:\Users\Admin\.gemini\config\skills\branches\scripts\verify_lineage.py`
   - **Section**: BANNED_BUZZWORDS
   - **Problem**: Drillers translated English text ("superior / outperforming") into the Vietnamese word "vượt trội", which triggered `BANNED_BUZZWORDS` warnings in `verify_lineage.py`.
   - **What was done**: Replaced "vượt trội" with contextually neutral Vietnamese phrasing ("cao hơn rõ rệt", "tốt hơn", "hiệu quả hơn") across Markdown documents, resulting in 0 warnings and 0 errors.
