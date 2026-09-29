# Paper Tab AutoML

10 research papers on **AutoML for water and wastewater treatment** with deep knowledge trees and interactive Markmap mind maps.

## Contents

### Papers (PDFs)

| # | Paper | Pages |
|---|---|---|
| 1 | An Interpretable AI Framework for Defining the Operational Basin of Full-Scale MBRs in Semiconductor Wastewater Treatment | ~14 |
| 2 | Automated Machine Learning and SHAP-based Interpretation of PFOA Removal via Electrochemical Oxidation | ~9 |
| 3 | Elucidating Response Effects of Anammox-based Nitrogen Removal for Municipal Wastewater Using Big Data Analysis and AutoML | ~12 |
| 4 | Empowerment of Accurate Modeling of Anaerobic MBRs by Automated Machine Learning | ~10 |
| 5 | Explainable Cross-Plant Transfer Learning for Fouling Prediction in Data-Limited Pilot-Scale MBRs | ~14 |
| 6 | Interpretable Prediction of Coagulant Dosage in DWTP Based on AutoML and SHAP | ~12 |
| 7 | Machine Learning for MBR Research: Principles, Methods, Applications, and a Tutorial | ~20 |
| 8 | Predicting Nitrification Status in Aerobic MBRs by Interpretable ML Models | ~14 |
| 9 | Predictive Framework for Membrane Fouling in Full-Scale MBRs: Integrating AI-Driven Feature Engineering and XAI | ~16 |
| 10 | Wastewater MBR: A Comprehensive Review of XAI and Digital Twin Applications | ~18 |

### Knowledge Trees (`branches/`)

Each paper has its own subdirectory under `branches/` containing:

```
branches/<paper_slug>/
├── <slug>_branches.md               ← Full merged Markdown knowledge tree
├── <slug>_branches.html             ← Interactive Markmap mind map (open in browser)
├── <slug>_scout_manifest.json       ← Structural skeleton and glossary
├── <slug>_verification_report.json  ← 4-gate completeness audit
├── doc_text.txt                     ← Extracted text from PDF
├── meta.json                        ← Paper metadata
└── fragments/                       ← Per-chapter Markdown trees
    ├── ch01_*_branches.md
    ├── ch02_*_branches.md
    └── ...
```

## How to Use

1. Open any `*_branches.html` file in a browser to view the interactive mind map.
2. Read `*_branches.md` files for structured Markdown knowledge trees.
3. Use `fragments/` for selective chapter-level reading.

## Pipeline

Generated using the `/branches` skill with a multi-agent pipeline:
- **branches-scout**: Scans structure, builds routing table
- **branch_driller**: Recursive L3–L6 extraction (spawns child drillers for large sections)
- **fragment_verifier**: Audits each fragment against source text (numeric fidelity, formula completeness, key claims)
- **branch_merger**: Assembles fragments into unified tree
- **branches-verifier**: 4-gate completeness audit (coverage, depth, grounding, lexicon)
- **mindmap_renderer**: Compiles Markdown to standalone HTML via Markmap + KaTeX

## License

Papers are copyrighted by their respective publishers. Knowledge trees are derivative works for personal research use.
