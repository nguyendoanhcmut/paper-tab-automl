### 1. Introduction and Document Overview

#### 1.1 Document Frontmatter and Research Context

##### 1.1.1 Publication Metadata and Author Details
- Document Title: Automated machine learning and SHAP-based interpretation of PFOA removal via electrochemical oxidation.
- Author: Haitham Elnakar.
- Primary Affiliation: Department of Civil and Environmental Engineering, King Fahd University of Petroleum & Minerals (KFUPM), Dhahran 31261, Saudi Arabia.
- Secondary Affiliation: Interdisciplinary Research Center for Construction and Building Materials, KFUPM, Dhahran 31261, Saudi Arabia.
- Corresponding Author Contact: haitham.elnakar@kfupm.edu.sa.
- Journal Details: Published in *Desalination and Water Treatment*, Volume 325 (2026), Article 101598, Elsevier Inc.
- Article History: The journal received the manuscript on 19 August 2025. The author submitted revisions on 24 November 2025. The journal accepted the manuscript on 2 December 2025. The article appeared online on 4 December 2025.
- Licensing and Identifiers: Open access under the CC BY 4.0 license. The digital object identifier is $\text{DOI: } 10.1016/\text{j.dwt.2025.101598}$. The ISSN is 1944-3986.
- Topic Keywords: Perfluorooctanoic acid (PFOA), PFAS, Electrochemical oxidation, Automated Machine Learning (AutoML), FLAML, SHAP.

##### 1.1.2 Abstract Summary and Key Quantitative Benchmarks
- Predictive Performance: The FLAML-optimized XGBoost model attained high predictive accuracy. The model achieved $\text{RMSE} = 3.97$ and $R^2 = 0.98$.
- Baseline Comparison: The optimized XGBoost model outperformed tuned Random Forest, Gradient Boosting, and Deep Learning models.
- Computational Overhead Reduction: The FLAML pipeline reduced computational runtime by $72\%$ compared to manual tuning procedures.
- Statistical Generalizability: Repeated holdout validation confirmed model stability across data partitions.
- Feature Attribution Hierarchy: SHAP analysis ranked electrolysis time and anode material as primary drivers. Electrolyte concentration and current density formed the secondary tier.
- Practical Applicability: The workflow establishes a reproducible benchmark to support environmental decision-making.

#### 1.2 PFOA Toxicology and Environmental Regulation

##### 1.2.1 Chemical Architecture and Environmental Persistence
- Molecular Formula: Perfluorooctanoic acid has chemical formula $\text{CF}_3(\text{CF}_2)_6\text{COOH}$.
- Carbon-Fluorine Bonds: The perfluorinated alkyl chain contains strong covalent $\text{C}-\text{F}$ bonds.
- Chemical Stability: High bond energy prevents thermal, chemical, and biological breakdown.
- Environmental Persistence: Chemical recalcitrance causes pervasive contamination across aquatic and terrestrial ecosystems.
- Mineralization Target: Destructive treatment must mineralize PFOA into benign carbon dioxide ($\text{CO}_2$) and fluoride ions ($\text{F}^-$).

##### 1.2.2 Pathological Effects and Regulatory Standards
- Biological Hazards: PFOA bioaccumulates in human tissues and blood serum.
- Clinical Pathologies: Chronic exposure links to immunotoxicity, liver dysfunction, cardiovascular disease, and cancer.
- Oncogenic Classification: The International Agency for Research on Cancer (IARC) classifies PFOA as a Group 1 human carcinogen.
- Drinking Water Limit: The US Environmental Protection Agency (EPA) established a Maximum Contaminant Level (MCL) of $4\text{ ng/L}$.
- Industrial Remediation Need: Strict regulations demand scalable treatment systems for industrial wastewater streams.

#### 1.3 Electrochemical Oxidation Pathways and Operational Complexities

##### 1.3.1 Dual Degradation Pathways and Mineralization Chemistry
- Destructive Remediation: Electrochemical oxidation mineralizes PFOA into benign $\text{CO}_2$ and $\text{F}^-$.
- Anodic Electron Transfer: Direct electron transfer occurs at the anode surface. This step produces perfluoroalkyl radicals and starts chain-shortening reactions.
- Hydroxyl Radical Oxidation: Water electrolysis generates reactive hydroxyl radicals ($\cdot\text{OH}$). These radicals attack intermediate degradation products.
- Reaction Synergy: Combined direct and indirect mechanisms mineralize the parent perfluoroalkyl structure.
- Anode Material Role: The anode composition governs oxygen evolution overpotential and determines overall reaction efficiency.

##### 1.3.2 Multi-Parameter Matrix and Operational Interdependence
- High Dimensionality: The electrochemical reactor depends on eight interacting operational parameters.
- Electrical Variables: Current density and electrode spacing control cell potential and energy consumption.
- Chemical Variables: Electrolyte composition, electrolyte concentration, initial PFOA concentration, and pH alter solution chemistry.
- Physical Variables: System temperature, electrolysis time, and water matrix constituents influence fluid dynamics and reaction rates.
- Variable Interactions: A change in one operational factor alters the response of other factors. Traditional one-factor tests fail to find global optima.

#### 1.4 Machine Learning Bottlenecks and AutoML Capabilities

##### 1.4.1 Deficiencies in Conventional Machine Learning Workflows
- Manual Tuning Bottlenecks: Standard machine learning requires trial-and-error hyperparameter search by domain experts.
- Search Limitations: Grid search and random search waste computing resources in poor parameter regions.
- Accessibility Constraints: Complex manual workflows limit model adoption by environmental practitioners.
- Benchmark Accuracy: Prior studies reached $R^2 > 0.84$, but lacked automated tuning pipelines.

##### 1.4.2 Cost-Aware Bayesian Optimization with FLAML
- FLAML Architecture: Microsoft Research developed Fast Lightweight AutoML (FLAML) for automated algorithm selection and tuning.
- Cost-Aware Search: FLAML uses cost-aware Bayesian optimization. The search allocates compute budget dynamically.
- Low-Complexity Priority: The optimizer checks simple, fast-converging models before evaluating computationally heavy architectures.
- Anaerobic Digestion Benchmark: AutoML gradient boosting achieved $\text{MSE} = 17.0$ versus $\text{MSE} = 58.0$ for neural networks in microplastics digestion studies.
- Constructed Wetland Benchmark: AutoML models predicted antibiotic removal across training durations. The models reached $\text{MAE} = 9.94\text{--}13.68$ and $R^2 = 0.780\text{--}0.877$.

##### 1.4.3 Interpretability Integration Through SHAP Analyses
- SHAP Framework: SHapley Additive exPlanations uses cooperative game theory to calculate individual feature contributions.
- Mechanistic Alignment: SHAP attributions match known electrochemical oxidation kinetics.
- Transparent Optimization: Explainable outputs give operators clear evidence to adjust reactor setpoints safely.

#### 1.5 Study Objectives and Methodological Framework

##### 1.5.1 Research Objectives and Automation Goals
- Core Objective: The study develops an automated and interpretable machine learning pipeline for PFOA removal.
- Predictive Goal: The workflow gives high predictive accuracy without manual intervention.
- Attribution Goal: The pipeline identifies primary operational drivers with model-based SHAP explanations.
- Portability Goal: The automated pipeline establishes a reproducible template for environmental remediation tasks.

##### 1.5.2 Evaluation Protocol and Architectural Decoupling
- Dataset Provenance: The study uses a curated experimental dataset from literature to permit direct comparability.
- Decoupled Pipeline Design: The framework separates the FLAML optimization engine from the final XGBoost predictive model.
- Statistical Cross-Validation: Repeated holdout splits verify model stability and prevent overfitting.
- Diagnostic Validation: Learning curve evaluations assess model generalizability across training sample sizes.
