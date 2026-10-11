# Run Report - M030

- Document: `Artificial Neural Networks and Multivariate Statistical Process Control to improve ammonia removal on membrane bioreactors treating refinery wastewater`
- Doc Slug: `M030`
- Doc Type: `paper`
- Domain: `general`
- Max Heading Level: `4`
- Language: `vi`

## Pipeline Phases & Timings
- Phase 1 (Extract): Text and figures extracted to `M030.txt` and `assets/`.
- Phase 2 (Page Images): Skipped (scientific paper without worked exercises).
- Phase 3 (Scout): `branch_scout` generated `skeleton.json` and `M030_scout_manifest.json` (10 routing chunks).
- Phase 4 (Drill):
  - 13 `figure_driller` subagents executed in parallel for all figures and tables.
  - 10 `branch_driller` subagents executed in parallel across all chunks.
- Phase 5 (Merge): `merge_fragments.py` assembled full tree with 20 headings and 621 lines.
- Phase 6 (Audit):
  - `fragment_verifier` audited `ch03_1` (Score: 1.0) and `ch04_1_1` (Score: 1.0).
  - `branch_verifier` evaluated merged tree (Completeness Score: 1.00 / 1.00).
  - `verify_lineage.py` passed (`LINEAGE PASSED`).
  - `gate_paper.py` passed (`GATE PASSED`).
- Phase 7 (Render): `compile_mindmap.js` generated interactive Markmap HTML mindmap (`M030_branches.html`, 530 nodes, 179 math nodes, 149 KB).

## Subagent Counts
- Total Subagents Spawned: 27
  - `branch_scout`: 1
  - `figure_driller`: 14 (13 active + 1 transient retry)
  - `branch_driller`: 10
  - `fragment_verifier`: 2
  - `branch_verifier`: 1

## Verification Scores
- Completeness Score: 1.00 (Pass threshold: >= 0.95)
  - Section coverage: 1.00 (18/18 compliant)
  - Depth: 1.00 (18/18 compliant)
  - Grounding: 1.00 (401/401 grounded leaves, 0 vague)
  - Lexicon: 1.00 (10/10 resolved)
- Lineage Check: LINEAGE PASSED
- Gate Paper Check: GATE PASSED

## Warnings
- [WARN] Table recall mismatch: 3 table caption(s) found, but 2 table crop(s) extracted (Table 3 descriptive statistics spanned page layout).
- [WARN] 14 buzzword occurrences noted by verify_lineage.py ('vượt trội', 'toàn diện').
