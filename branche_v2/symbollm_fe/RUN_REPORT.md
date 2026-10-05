# Run Report: SymboLLM-FE Mindmap Extraction and Rendering

## Executive Summary
- **Document Title**: SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering on Tabular Data
- **Document Slug**: `symbollm_fe`
- **Document Type**: Paper (27 pages)
- **Domain**: General
- **Output Language**: Vietnamese (`vi`)
- **Primary Markdown Tree**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/symbollm_fe/symbollm_fe_branches.md`
- **Rendered Mindmap HTML**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/symbollm_fe/symbollm_fe_branches.html`
- **Total Headings**: 71
- **Embedded Figures**: 4 (Figures 1, 2, 3/Fig 5, 4/Fig 6)
- **Exercises / Case Studies**: 5 (5 passed)
- **Completeness Score ($C$)**: 1.00 / 1.00 (Threshold: $\ge 0.95$)
- **Lineage Verification**: PASSED (0 errors, 50 style/buzzword warnings)

---

## Phase Execution Details

### Phase 1: Extract
- **Text Layer Extraction**: PyMuPDF extracted 27 pages and 56 table-of-contents entries into `symbollm_fe.txt`.
- **Figure Extraction**: Extracted 6 raw assets into `assets/`, generating `figures_manifest.json`.

### Phase 2: Page Images
- **PDF Rasterization**: Rasterized 27 pages at 200 DPI into `pages/` for high-resolution visual evidence and case study auditing.

### Phase 3: Scout
- **Subagent**: `branch_scout` (conversation ID: `9b64b82a-9dca-4e44-9f30-236a83ded377`).
- Generated `candidates.json` and compiled `skeleton.json`.
- Established master skeleton with 58 sections and routing table with 28 parallel chunks.
- Extracted global lexicon, core thesis, and 5 case studies (worked examples) in Appendix K.

### Phase 4: Drill (Parallel)
- **Subagents**: 28 parallel `branch_driller` instances (Flash model).
- Every chunk drilled into structured claim bullets with KaTeX formula formatting and numeric preservation.
- Case studies (K.1 - K.5) drilled with step-by-step problem, givens, rules, solutions, and verification.
- Figures embedded as evidence blocks under citing claim bullets.
- All 28 fragments written to `fragments/`.

### Phase 5: Merge
- Executed `merge_fragments.py`.
- Merged 28 fragments into `symbollm_fe_branches.md` (1,273 lines, 71 headings).

### Phase 6: Audit
1. **Semantic Verification (`branch_verifier`)**:
   - Subagent conversation ID: `ef40a92d-471a-4f1c-94e9-48a7e153e9db`.
   - Section Coverage (weight 0.40): Score 1.00 (58/58 expected headings matched).
   - Depth (weight 0.30): Score 1.00 (14/14 compliant sections).
   - Grounding (weight 0.20): Score 1.00 (650/650 leaf bullets grounded, 0 vague leaves).
   - Lexicon (weight 0.10): Score 1.00 (8/8 key terms resolved).
   - **Completeness Score $C$**: 1.00 / 1.00 (PASSED).
2. **Structural Lineage (`verify_lineage.py`)**:
   - Audited heading hierarchy, single H1 root, evidence block nesting, and asset presence.
   - Fixed table label formatting to ensure clean claim bullet lineage.
   - Result: **LINEAGE PASSED** (0 errors).

### Phase 7: Render
- Executed `compile_mindmap.js`.
- Generated `symbollm_fe_branches.html` (181 KB, 747 nodes, 221 KaTeX math nodes).
- Verified bundle integrity: contains `katex.min.js`, `markmap-view`, and `id="theme-toggle"`.

---

## Metric Summary Table

| Metric | Target | Observed | Status |
| :--- | :---: | :---: | :---: |
| Chunks Routed | - | 28 | Complete |
| Drillers Spawned | 28 | 28 | All Succeeded |
| Merged Headings | - | 71 | Valid Hierarchy |
| Embedded Figures | 4 | 4 | Grounded Evidence |
| Worked Case Studies | 5 | 5 | All 5 Passed |
| Completeness Score ($C$) | $\ge 0.95$ | **1.00** | PASSED |
| Mechanical Lineage | PASSED | **PASSED** | PASSED |
| Rendered HTML Size | $> 1$ KB | **181 KB** | Verified |
