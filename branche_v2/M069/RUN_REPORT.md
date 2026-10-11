# Pipeline Run Report: M069

## Document Information
- **Title**: Data-driven compliance: Optimising MPBR performance for ammonium removal and maximum water reuse for EU standards
- **Slug**: M069
- **Type**: paper
- **Language**: Vietnamese (vi)

## Execution Summary
- **Input PDF**: `C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\pdfs\M069.pdf`
- **Output Directory**: `C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\branches_v2\M069`
- **Primary Markdown**: `C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\branches_v2\M069\M069_branches.md`
- **Compiled Mindmap**: `C:\Users\Admin\.gemini\antigravity\scratch\mbr_opcond_survey\branches_v2\M069\M069_branches.html`

## Subagent Statistics
- **branch_scout**: 1
- **branch_driller**: 17 (chunks: ch01 to ch06)
- **figure_driller**: 11 (fig_01, fig_02, table_01, fig_03, fig_04, fig_05, fig_06, fig_07, table_02, fig_08, table_03)
- **fragment_verifier**: 17
- **branch_verifier**: 1
- **Total Subagents Spawned**: 47

## Verification & Quality Gates
- **Completeness Score**: 1.00 (`M069_verification_report.json`)
  - Section Coverage (0.40): 1.0 (22/22 observed)
  - Depth (0.30): 1.0 (12/12 compliant)
  - Grounding (0.20): 1.0 (380/380 leaf bullets grounded)
  - Lexicon (0.10): 1.0 (15/15 terms resolved)
- **Lineage Verification (`verify_lineage.py`)**: PASSED
  - Total Headings: 23
  - Embedded Evidence Blocks: 10 figures/tables
  - Block length: All <= 10 lines
  - Anchors: All properly nested under claim bullets
- **Compliance Gate (`gate_paper.py`)**: PASSED

## Warnings
- Unused asset: `assets/fig_02_p5_vector.png` (decorative caption banner, dropped intentionally from tree).
- Minor stylistic buzzword warnings in source translation handled appropriately.
