# RUN_REPORT: TopoFE (topofe)

## Document Information
- **Title**: TopoFE: Topology-Aware LLM-Guided Automated Feature Engineering
- **Slug**: `topofe`
- **Type**: `paper`
- **Domain**: `general`
- **Output Language**: `vi`
- **Input File**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/TopoFE_2607.23286.pdf`
- **Output Directory**: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/topofe/`

## Execution Summary
- **Phases Completed**:
  1. **Extract**: Text (22 pages, 41 TOC entries) & Figures (3 figures extracted with bounding boxes and captions).
  2. **Page Images**: Skipped (paper contains no exercise problems).
  3. **Scout**: `branch_scout` generated candidate sections, built `skeleton.json`, and produced `topofe_scout_manifest.json` with 19 parallel chunk routes.
  4. **Drill (Parallel)**: Spawned 19 `branch_driller` instances concurrently; all 19 completed without failures.
  5. **Merge**: `merge_fragments.py` aggregated 19 fragments into `topofe_branches.md` (1094 lines, 56 headings).
  6. **Audit**:
     - `branch_verifier` gave completeness score **1.0 / 1.0** across all 4 gates (Coverage: 1.0, Depth: 1.0, Grounding: 1.0, Lexicon: 1.0).
     - `verify_lineage.py` passed with 0 structural errors, 23 stylistic buzzword warnings.
  7. **Render**: `compile_mindmap.js` generated interactive HTML mindmap (187.8 KB, 684 nodes, 208 math formulas, verified katex, markmap-view, theme toggle).
  8. **Report**: Completed.

## Subagent Stats
- `branch_scout`: 1
- `branch_driller`: 19
- `branch_verifier`: 1
- Total subagents invoked: 21

## Verification Metrics
- **Headings Count**: 56
- **Figures Extracted & Embedded**: 3 (`fig_01`, `fig_02`, `fig_03`)
- **Exercises**: 0
- **Completeness Score**: 1.0 (PASSED)
- **Lineage Verification**: PASSED (23 buzzword warnings)

## Artifact Deliverables
- Markdown Tree: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/topofe/topofe_branches.md`
- Interactive HTML Mindmap: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/topofe/topofe_branches.html`
- Scout Manifest: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/topofe/topofe_scout_manifest.json`
- Verification Report: `C:/antgravity workplace/ML/PAPER TAB AUTOML/llm_fe_papers/topofe/topofe_verification_report.json`
