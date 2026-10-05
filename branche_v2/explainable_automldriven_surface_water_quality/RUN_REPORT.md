# RUN REPORT: Explainable AutoML-driven surface water quality classification with key indicators identification

- **Document Slug**: `explainable_automldriven_surface_water_quality`
- **Document Type**: Scientific Paper (`paper`)
- **Domain**: General (`general`)
- **Target Language**: Vietnamese with original English terms in parentheses
- **Timestamp**: 2026-10-05T15:43:00+07:00
- **Status**: Completed successfully (LINEAGE PASSED)

---

## 1. Execution Summary

| Phase | Description | Status | Details |
|---|---|---|---|
| **Phase 1: Extract** | Text & figure extraction from PDF | PASSED | Extracted 8 figures into `assets/` and full text into `explainable_automldriven_surface_water_quality.txt` |
| **Phase 2: Rasterize** | Page rasterization | SKIPPED | Paper without exercises; assets extracted directly |
| **Phase 3: Scout** | Structural analysis & chunk routing | PASSED | Manifest generated with 12 chunks in `routing_table` |
| **Phase 4: Drill** | Chunk extraction into Markdown subtrees | PASSED | 12 fragment files drilled with high claim density, KaTeX math/chemistry, and compliant evidence blocks |
| **Phase 5: Merge** | Assembly of master tree via `merge_fragments.py` | PASSED | 351 lines, 24 headings, single H1 root |
| **Phase 6: Audit** | Lineage verification via `verify_lineage.py` | PASSED | **0 errors, 0 warnings** |
| **Phase 7: Render** | Markmap compilation via `compile_mindmap.js` | PASSED | 309 nodes, 114 KaTeX math nodes, 107 KB HTML file |
| **Phase 8: Report** | Final run audit and telemetry | PASSED | Generated this report |

---

## 2. Lineage Audit Results

- **Tool**: `verify_lineage.py`
- **Result**: `LINEAGE PASSED`
- **Errors**: 0
- **Warnings**: 0
- **Structural Integrity**:
  - Exactly 1 H1 root.
  - Strict monotonic heading hierarchy (H1 -> H2 -> H3 -> H4) with no skipped levels.
  - No figure dump sections or gallery titles.
  - Every figure embedded exactly once in an evidence block (`< 10` lines).
  - Every evidence block anchored to a dedicated claim bullet.
  - Chapter 3 figure ratio `< 50%` (non-figure claim bullets dominate the chapter narrative).
  - All 8 figures verified on disk in `assets/`.
  - Zero banned buzzwords detected.

---

## 3. Key Document Metrics

- **Total Headings**: 24
  - H1: 1
  - H2: 6 (`Abstract`, `1 Introduction`, `2 Materials and methods`, `3 Results`, `4 Discussion`, `5 Conclusion`, `Data availability`)
  - H3: 13
  - H4: 4 (`3.2.1`, `3.2.2`, `4.2.1`, `4.2.2`)
- **Total Embedded Figures**: 8 (Fig. 1 to Fig. 8)
- **Total Exercises**: 0
- **KaTeX Formula & Chemistry Nodes**: 114
- **HTML Mind Map Size**: 107 KB

---

## 4. Primary Outputs

1. Primary Markdown Tree:
   `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/explainable_automldriven_surface_water_quality/explainable_automldriven_surface_water_quality_branches.md`
2. Standalone Interactive Mindmap:
   `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/explainable_automldriven_surface_water_quality/explainable_automldriven_surface_water_quality_branches.html`
3. Scout Manifest:
   `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/explainable_automldriven_surface_water_quality/explainable_automldriven_surface_water_quality_scout_manifest.json`
4. Figures Manifest:
   `C:/antgravity workplace/ML/PAPER TAB AUTOML/branche_v2/explainable_automldriven_surface_water_quality/figures_manifest.json`
