### 4. Conclusions and Document Backmatter

#### 4.1 Research Conclusions and Core Synthesis
##### 4.1.1 Automated Model Performance and Tuning Efficiency
- Automated Machine Learning Advantage: Automated machine learning with FLAML removes manual trial-and-error in electrochemical process modeling.
- Predictive Accuracy Achievement: The selected XGBoost model achieved $\text{RMSE} = 3.97$ and determination coefficient $R^2 = 0.98$.
- Baseline Comparison Results: The FLAML model outperformed Random Forest, Gradient Boosting, Deep Learning, and k-Nearest Neighbors.
- Statistical Significance Validation: Paired two-tailed t-tests with Bonferroni correction confirmed significant performance improvements ($p < 10^{-5}$).
- Optimization Time Reduction: FLAML decreased hyperparameter tuning time by $72\%$ compared to conventional grid and manual search workflows.
- Bounded Search Duration: The automated search completed all iterations within a strict wall-clock budget of $300\text{ s}$ ($5\text{ minutes}$).

##### 4.1.2 Verified Operational Drivers and Kinetic Principles
- Primary Operational Determinants: Interpretability analysis identified total electrolysis time and anode material as the primary operational drivers.
- Kinetic Theory Alignment: Feature importance rankings match electrochemical principles where cumulative charge controls pollutant destruction.
- Electrode Material Impact: Anode material governs the oxygen evolution overpotential and regulates the yield of reactive hydroxyl radicals.
- Secondary Operational Determinants: Electrolyte concentration and current density form a secondary tier of influential process variables.
- Non-Linear Dependency Attribution: SHAP values showed non-linear effects and parameter interactions without human selection bias.
- Operational Saturation Patterns: SHAP dependence plots revealed monotonic removal growth with electrolysis time and plateau effects at high current density.

#### 4.2 Methodological Innovations and Future Research Directions
##### 4.2.1 Pipeline Standardization and Software Containerization
- Containerized Execution Environment: The author encapsulated the modeling workflow inside a Docker container for complete cross-platform reproducibility.
- Software Dependencies: The software environment fixed exact library releases: Python 3.10, FLAML 1.2.0, SHAP 0.44.0, and scikit-learn 1.4.0.
- Mitigation of Environmental Drift: Containerization prevents package dependency conflicts and allows independent evaluation by third parties.
- Methodological Standardization: The standardized pipeline addresses the limitations of untracked scripting habits found in earlier research.
- Workflow Decoupling Strategy: The framework isolates the FLAML hyperparameter search phase from the final XGBoost model deployment.

##### 4.2.2 Future Directions and Remediation Expansion
- Physics-Informed Machine Learning: Future research will merge electrochemical transport equations with data-driven predictive architectures.
- Adaptive Process Control: Automated pipelines can connect to real-time sensors to adjust treatment conditions dynamically.
- Extended PFAS Scope: Researchers can adapt the methodology to short-chain perfluoroalkyl substances and modern replacements like GenX.
- Multi-Objective Process Targets: Future work must balance PFOA removal against electrical energy per order ($\text{EE/O}$) and total operational costs.
- Pilot-Scale Reactor Testing: Engineers must validate the framework on continuous-flow electrochemical reactors under industrial field conditions.

#### 4.3 Authorship, Ethics, and Institutional Support
##### 4.3.1 CRediT Authorship Contribution Statement
- Sole Research Attribution: Haitham Elnakar executed all aspects of the published study.
- Conceptualization and Methodology: Haitham Elnakar developed the conceptual framework and designed the automated machine learning methodology.
- Formal Analysis and Investigation: Haitham Elnakar performed the model training, statistical tests, and interpretability evaluations.
- Data Curation and Visualization: Haitham Elnakar processed the experimental records and generated all data figures.
- Writing the Original Draft: Haitham Elnakar wrote the initial manuscript draft.
- Review and Text Editing: Haitham Elnakar revised the draft and prepared the final published text.

##### 4.3.2 Conflict of Interest and Funding Declarations
- Conflict of Interest Disclosure: The author declares no known competing financial interests or personal relationships that influenced this study.
- Absence of Commercial Bias: The research proceeded independently without commercial sponsor involvement.
- Institutional Financial Support: King Fahd University of Petroleum and Minerals (KFUPM) supported this publication.
- Primary Academic Affiliation: Department of Civil and Environmental Engineering, KFUPM, Dhahran 31261, Saudi Arabia.
- Interdisciplinary Center Affiliation: Interdisciplinary Research Center for Construction and Building Materials, KFUPM, Dhahran 31261, Saudi Arabia.

#### 4.4 Appendix A: Supporting Information Inventory
##### 4.4.1 Exploratory and Diagnostic Visualizations (Figures S1 to S3)
- Online File Access: Supporting data is available online through the digital object identifier $\text{doi: } 10.1016/\text{j.dwt.2025.101598}$.
- Figure S1 (Predictor Correlation): A Spearman rank-correlation heatmap displays significance marks for associations among electrochemical predictors.
- Figure S2 (Bivariate Relationships): Pairwise scatterplots with LOWESS curves and correlation metrics illustrate collinearity ($|\rho| \approx 0.35\text{ to }0.55$).
- Figure S3 (Target Distribution): The histogram displays removal percentage distributions alongside a Shapiro-Wilk normality diagnostic.

##### 4.4.2 Validation Stability and Attribution Consistency (Figures S4 to S6)
- Figure S4 (Stratification Sensitivity): Boxplots summarize metric distributions across repeated data partitions stratified on anode material.
- Figure S5 (Nested Cross-Validation): Diagnostic plots confirm model selection consistency across nested cross-validation folds.
- Figure S6 (Leave-One-Out SHAP Stability): Feature importance stability evaluation after removing the top predictor (electrolysis time).
- Concordance Statistic: The leave-one-out test yielded a Kendall rank correlation $\tau = 0.600$ ($p = 0.136$), confirming stable secondary rankings.

##### 4.4.3 Hyperparameter Configurations and Rank Concordance (Tables S1 and S2)
- Table S1 (Search Space and Bounds): The table lists hyperparameter search ranges and evaluation budgets for all evaluated learners.
- Selected Tree Hyperparameters: Parameters include $\text{learning\_rate} = 0.1403$, $\text{n\_estimators} = 379$, and $\text{max\_leaves} = 13$.
- Selected Regularization Hyperparameters: Parameters include $\alpha = 0.0995$, $\lambda = 0.0010$, $\text{subsample} = 0.85$, and $\text{colsample\_bytree} = 0.83$.
- Table S2 (Importance Concordance): Agreement metrics compare grouped TreeSHAP rankings against Conditional Permutation Importance (CPI).
- Collinearity Independence: Kendall rank correlation values with $95\%$ confidence intervals confirmed that feature attributions remained reliable.

#### 4.5 Data Availability and Repository Attribution
##### 4.5.1 Benchmark Dataset Provenance and Access
- Primary Data Source: The study evaluated experimental records compiled and published by Alnaimat et al. [30] in 2024.
- Source Article Citation: Alnaimat S., Mohsen O., Elnakar H., *J. Environ. Manage.* 370 (2024) 122857.
- Open Data Statement: The dataset is available through the cited reference in the methodology section.
- Direct Literature Parity: Evaluating the Alnaimat dataset enabled direct performance comparisons against earlier machine learning benchmarks.

##### 4.5.2 Feature Encoding and Preprocessing Parity
- Input Variable Scope: The dataset includes eight continuous and categorical electrochemical process variables.
- Categorical Field Encoding: One-hot encoding converted categorical variables (anode, cathode, electrolyte, water matrix) with cardinality $\le 6$.
- Continuous Feature Standardization: Z-score standardization scaled continuous features for distance-based and gradient-based algorithms.
- Tree Split Invariance: Tree-based learners trained on unscaled features because decision tree split criteria exhibit scale invariance.
- Stratified Partition Protocol: An 80:20 train-test partition stratified on anode type prevented covariate shift across training and test subsets.

#### 4.6 Selected Literature References
##### 4.6.1 Automated Machine Learning and Explainable AI Foundations
- Fast Lightweight AutoML Framework: Wang et al. (2021) introduced the FLAML library for cost-aware hyperparameter optimization [27].
- Game-Theoretic Interpretability: Lundberg and Lee (2017) unified feature attributions through SHapley Additive exPlanations (SHAP) [33].
- Scalable Tree Boosting: Chen and Guestrin (2016) developed XGBoost as a scalable tree boosting system [43].
- Environmental ML Best Practices: Zhu et al. (2023, 2024) established the EMBRACE reporting checklist for machine learning in environmental engineering [22, 23].
- Wetland Treatment Modeling: Bao et al. (2023) used automated machine learning to predict antibiotic removal in constructed wetlands [28].
- Digestion Process Modeling: Xu et al. (2022) predicted microplastic impacts on anaerobic digestion methane production with AutoML [29].
- Water Plant Dosage Prediction: Feng et al. (2025) applied AutoML and SHAP to predict coagulant dosage in drinking water plants [24].

##### 4.6.2 Electrochemical PFAS Degradation and Environmental Standards
- Reference PFOA Benchmark: Alnaimat et al. (2024) modeled PFOA removal through electrochemical oxidation with machine learning [30].
- Drinking Water Regulations: US EPA (2025) established the Final PFAS National Primary Drinking Water Regulation with a $4\text{ ng/L}$ MCL [6].
- Strategic Remediation Policy: US EPA (2023) published the PFAS Strategic Roadmap detailing second-year remediation progress [47].
- Human Carcinogenicity Evaluation: Zahm et al. (2024) classified PFOA as carcinogenic to humans in Lancet Oncology (Group 1) [5].
- Electrochemical Review Foundations: Chaplin (2014) reviewed electrochemical advanced oxidation processes for water treatment [42].
- Anodic Oxidation Mechanisms: Panizza and Cerisola (2009) classified direct and mediated anodic oxidation mechanisms for organic pollutants [41].
- Wastewater Treatment Applications: Martínez-Huitle and Panizza (2018) surveyed electrochemical oxidation technologies for wastewater treatment [39].
- Novel Electrode Membranes: Liang et al. (2025) synthesized durable $\text{Ti}_4\text{O}_7$ heterojunction composite membranes for GenX electro-oxidation [14].
- Persulfate Activation Support: Samuel et al. (2024) enhanced PFOA degradation by electrochemically activating peroxydisulfate [15].
