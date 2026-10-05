# RUN REPORT: SIGMA (AutoFE)

- **Document Title**: SIGMA: SHAP-Guided Implicit-Trajectory Generation for Metadata-Free LLM-Based AutoFE
- **Document Slug**: `sigma_autofe`
- **Document Type**: `paper`
- **Domain**: `general`
- **Output Language**: `vi`
- **Input File**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/SIGMA_2608.17948.pdf`
- **Output Directory**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/sigma_autofe`

---

## 1. Execution Timeline & Phase Summary

| Phase | Description | Status | Subagents / Scripts |
|---|---|---|---|
| **Phase 1: Extract** | Text extraction (16 pages, 6,610 words) & Vector/raster figures (4 figures) | Complete | `extract_pdf.py`, `extract_figures.py` |
| **Phase 2: Page Images** | Page rasterization (Skipped: paper without exercises) | N/A | - |
| **Phase 3: Scout** | Structure mapping, skeleton creation, chunk routing | Complete | `branch_scout` (`structure.py`) |
| **Phase 4: Drill** | Parallel Markdown subtree extraction (14 chunks) | Complete | 14 × `branch_driller` (flash) |
| **Phase 5: Merge** | Assembly of fragments into primary tree under single H1 root | Complete | `merge_fragments.py` |
| **Phase 6: Audit** | Semantic verification and mechanical lineage check | Complete | `branch_verifier`, `verify_lineage.py` |
| **Phase 7: Render** | Interactive Markmap HTML mindmap compilation with KaTeX math | Complete | `compile_mindmap.js` |

---

## 2. Subagent Statistics

- **Total Subagents Spawned**: 16
  - `branch_scout`: 1
  - `branch_driller`: 14 (all ran concurrently in parallel)
  - `branch_verifier`: 1

---

## 3. Tree Metrics & Gate Scores

- **Merged Tree**: `sigma_autofe_branches.md` (548 lines, 78 KB)
- **Interactive Mindmap**: `sigma_autofe_branches.html` (121 KB, 390 nodes, 89 KaTeX math nodes)
- **Headings Count**: 22 headings (Single H1 root, structured down to H3/H4)
- **Figures Extracted & Embedded**: 4 figures
  - Figure 1: Tổng quan kiến trúc hệ thống SIGMA (`assets/fig_01_p2.png`)
  - Figure 2: Phân tích hiệu quả sử dụng token và đặc trưng (`assets/fig_02_p8_vector.png`)
  - Figure 3: Cấu trúc tô-pô của các đặc trưng được sinh ra (`assets/fig_03_p9_vector.png`)
  - Figure 4: Kết quả nghiên cứu bóc tách thành phần Ablation (`assets/fig_04_p10_vector.png`)
- **Exercises**: 0 (Paper format with no exercises)
- **Completeness Score**: **1.0** (Target $\ge 0.95$)
  - Section Coverage (weight 0.40): 1.0 (18 / 18 sections verified)
  - Depth (weight 0.30): 1.0 (18 / 18 sections compliant)
  - Grounding (weight 0.20): 1.0 (298 / 298 leaf bullets grounded)
  - Lexicon (weight 0.10): 1.0 (8 / 8 key terms resolved)
- **Lineage Gate**: **PASSED**
- **Warnings**: 23 (stylistic buzzword warnings such as 'vượt trội', 'toàn diện')

---

## 4. Key Artifacts

- Full Tree: [sigma_autofe_branches.md](file:///C:/antgravity%20workplace/ML/PAPER%20TAB%20AUTOML/llm_fe_papers/sigma_autofe/sigma_autofe_branches.md)
- Interactive Mind Map: [sigma_autofe_branches.html](file:///C:/antgravity%20workplace/ML/PAPER%20TAB%20AUTOML/llm_fe_papers/sigma_autofe/sigma_autofe_branches.html)
- Scout Manifest: [sigma_autofe_scout_manifest.json](file:///C:/antgravity%20workplace/ML/PAPER%20TAB%20AUTOML/llm_fe_papers/sigma_autofe/sigma_autofe_scout_manifest.json)
- Verification Report: [sigma_autofe_verification_report.json](file:///C:/antgravity%20workplace/ML/PAPER%20TAB%20AUTOML/llm_fe_papers/sigma_autofe/sigma_autofe_verification_report.json)
