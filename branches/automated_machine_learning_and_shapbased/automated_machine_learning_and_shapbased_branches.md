---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---

# Automated machine learning and SHAP-based interpretation of PFOA removal via electrochemical oxidation

## 1. Introduction and Overview

### 1.1 Document Frontmatter and Research Context

#### 1.1.1 Publication Metadata and Author Details
- Document Title: Automated machine learning and SHAP-based interpretation of PFOA removal via electrochemical oxidation.
- Author: Haitham Elnakar.
- Primary Affiliation: Department of Civil and Environmental Engineering, King Fahd University of Petroleum & Minerals (KFUPM), Dhahran 31261, Saudi Arabia.
- Secondary Affiliation: Interdisciplinary Research Center for Construction and Building Materials, KFUPM, Dhahran 31261, Saudi Arabia.
- Corresponding Author Contact: haitham.elnakar@kfupm.edu.sa.
- Journal Details: Published in *Desalination and Water Treatment*, Volume 325 (2026), Article 101598, Elsevier Inc.
- Article History: The journal received the manuscript on 19 August 2025. The author submitted revisions on 24 November 2025. The journal accepted the manuscript on 2 December 2025. The article appeared online on 4 December 2025.
- Licensing and Identifiers: Open access under the CC BY 4.0 license. The digital object identifier is $\text{DOI: } 10.1016/\text{j.dwt.2025.101598}$. The ISSN is 1944-3986.
- Topic Keywords: Perfluorooctanoic acid (PFOA), PFAS, Electrochemical oxidation (EO), Automated Machine Learning (AutoML), FLAML, SHAP.

#### 1.1.2 Abstract Summary and Key Quantitative Benchmarks
- Predictive Performance: The FLAML-optimized XGBoost model attained high predictive accuracy. The model achieved $\text{RMSE} = 3.97$ and $R^2 = 0.98$.
- Baseline Comparison: The optimized XGBoost model outperformed tuned Random Forest, Gradient Boosting, and Deep Learning models.
- Computational Overhead Reduction: The FLAML pipeline reduced computational runtime by $72\%$ compared to manual tuning procedures.
- Statistical Generalizability: Repeated holdout validation confirmed model stability across data partitions.
- Feature Attribution Hierarchy: SHAP analysis ranked electrolysis time and anode material as primary drivers. Electrolyte concentration and current density formed the secondary tier.
- Practical Applicability: The workflow establishes a reproducible benchmark to support environmental decision-making.

### 1.2 PFOA Toxicology and Environmental Regulation

#### 1.2.1 Chemical Architecture and Environmental Persistence
- Molecular Formula: Perfluorooctanoic acid has chemical formula $\text{CF}_3(\text{CF}_2)_6\text{COOH}$.
- Carbon-Fluorine Bonds: The perfluorinated alkyl chain contains strong covalent $\text{C}-\text{F}$ bonds.
- Chemical Stability: High bond energy prevents thermal, chemical, and biological breakdown.
- Environmental Persistence: Chemical recalcitrance causes pervasive contamination across aquatic and terrestrial ecosystems.
- Mineralization Target: Destructive treatment must mineralize PFOA into benign carbon dioxide ($\text{CO}_2$) and fluoride ions ($\text{F}^-$).

#### 1.2.2 Pathological Effects and Regulatory Standards
- Biological Hazards: PFOA bioaccumulates in human tissues and blood serum.
- Clinical Pathologies: Chronic exposure links to immunotoxicity, liver dysfunction, cardiovascular disease, and cancer.
- Oncogenic Classification: The International Agency for Research on Cancer (IARC) classifies PFOA as a Group 1 human carcinogen.
- Drinking Water Limit: The US Environmental Protection Agency (EPA) established a Maximum Contaminant Level (MCL) of $4\text{ ng/L}$.
- Industrial Remediation Need: Strict regulations demand scalable treatment systems for industrial wastewater streams.

### 1.3 Electrochemical Oxidation (EO) Pathways and Operational Complexities

#### 1.3.1 Dual Degradation Pathways and Mineralization Chemistry
- Destructive Remediation: Electrochemical oxidation mineralizes PFOA into benign $\text{CO}_2$ and $\text{F}^-$.
- Anodic Electron Transfer: Direct electron transfer occurs at the anode surface. This step produces perfluoroalkyl radicals and starts chain-shortening reactions.
- Hydroxyl Radical Oxidation: Water electrolysis generates reactive hydroxyl radicals ($\cdot\text{OH}$). These radicals attack intermediate degradation products.
- Reaction Synergy: Combined direct and indirect mechanisms mineralize the parent perfluoroalkyl structure.
- Anode Material Role: The anode composition governs oxygen evolution overpotential and determines overall reaction efficiency.

#### 1.3.2 Multi-Parameter Matrix and Operational Interdependence
- High Dimensionality: The electrochemical reactor depends on eight interacting operational parameters.
- Electrical Variables: Current density and electrode spacing control cell potential and energy consumption.
- Chemical Variables: Electrolyte composition, electrolyte concentration, initial PFOA concentration, and pH alter solution chemistry.
- Physical Variables: System temperature, electrolysis time, and water matrix constituents influence fluid dynamics and reaction rates.
- Variable Interactions: A change in one operational factor alters the response of other factors. Traditional one-factor tests fail to find global optima.

### 1.4 Machine Learning Bottlenecks and AutoML Capabilities

#### 1.4.1 Deficiencies in Conventional Machine Learning Workflows
- Manual Tuning Bottlenecks: Standard machine learning requires trial-and-error hyperparameter search by domain experts.
- Search Limitations: Grid search and random search waste computing resources in poor parameter regions.
- Accessibility Constraints: Complex manual workflows limit model adoption by environmental practitioners.
- Benchmark Accuracy: Prior studies reached $R^2 > 0.84$, but lacked automated tuning pipelines.

#### 1.4.2 Cost-Aware Bayesian Optimization with FLAML
- FLAML Architecture: Microsoft Research developed Fast Lightweight AutoML (FLAML) for automated algorithm selection and tuning.
- Cost-Aware Search: FLAML uses cost-aware Bayesian optimization. The search allocates compute budget dynamically.
- Low-Complexity Priority: The optimizer checks simple, fast-converging models before evaluating computationally heavy architectures.
- Anaerobic Digestion Benchmark: AutoML gradient boosting achieved $\text{MSE} = 17.0$ versus $\text{MSE} = 58.0$ for neural networks in microplastics digestion studies.
- Constructed Wetland Benchmark: AutoML models predicted antibiotic removal across training durations. The models reached $\text{MAE} = 9.94\text{--}13.68$ and $R^2 = 0.780\text{--}0.877$.

#### 1.4.3 Interpretability Integration Through SHAP Analyses
- SHAP Framework: SHapley Additive exPlanations uses cooperative game theory to calculate individual feature contributions.
- Mechanistic Alignment: SHAP attributions match known electrochemical oxidation kinetics.
- Transparent Optimization: Explainable outputs give operators clear evidence to adjust reactor setpoints safely.

### 1.5 Study Objectives and Methodological Framework

#### 1.5.1 Research Objectives and Automation Goals
- Core Objective: The study develops an automated and interpretable machine learning pipeline for PFOA removal.
- Predictive Goal: The workflow targets high predictive accuracy with $\text{RMSE} \le 4.00$ and $R^2 \ge 0.95$ without manual tuning.
- Optimization Budget Goal: The framework converges within a $300\text{ s}$ search limit, reducing tuning duration by $72\%$.
- Attribution Goal: The pipeline identifies primary operational drivers with model-based SHAP explanations.
- Portability Goal: The automated pipeline establishes a reproducible template for environmental remediation tasks.

#### 1.5.2 Evaluation Protocol and Architectural Decoupling
- Dataset Provenance: The study uses a curated experimental dataset from literature to permit direct comparability.
- Decoupled Pipeline Design: The framework separates the FLAML optimization engine from the final XGBoost predictive model.
- Statistical Cross-Validation: Repeated holdout splits verify model stability and prevent overfitting.
- Diagnostic Validation: Learning curve evaluations assess model generalizability across training sample sizes.

## 2. Methodology

### 2.1 Dataset Characteristics and Preprocessing

#### 2.1.1 Dataset Origin and Experimental Scope
- Source dataset: The study uses the experimental dataset from Alnaimat et al. [30].
- Target domain: The data record the electrochemical degradation of perfluorooctanoic acid ($\text{PFOA}$, $\text{C}_7\text{F}_{15}\text{COOH}$) in water.
- Experimental scope: The dataset contains distinct treatment trials. Operational variables and water characteristics define each trial.

#### 2.1.2 Input and Target Variables
- Continuous predictors:
  - Electrolysis duration ($t$, in $\text{min}$ or $\text{h}$).
  - Current density ($j$, in $\text{mA}\cdot\text{cm}^{-2}$).
  - Electrolyte concentration ($C_{\text{electrolyte}}$, in $\text{mM}$ or $\text{g}\cdot\text{L}^{-1}$).
  - Initial solution pH ($\text{pH}_0$).
  - Reaction temperature ($T$, in $^{\circ}\text{C}$).
  - Inter-electrode spacing ($d$, in $\text{mm}$ or $\text{cm}$).
- Categorical descriptors:
  - Anode material type (such as Boron-Doped Diamond [$\text{BDD}$], $\text{Ti}/\text{RuO}_2$, $\text{Ti}/\text{IrO}_2$, $\text{PbO}_2$, and $\text{Pt}$).
  - Cathode material type (such as stainless steel, graphite, and $\text{Pt}$).
  - Electrolyte chemical composition (such as $\text{Na}_2\text{SO}_4$, $\text{NaCl}$, and $\text{NaClO}_4$).
  - Water matrix type (such as deionized water, tap water, surface water, and wastewater effluent).
- Target variable:
  - $\text{PFOA}$ removal efficiency ($Y$, expressed as percentage, $\%$).
  - Removal equation:
    $$Y = \frac{C_0 - C_t}{C_0} \times 100\%$$
  - In this equation, $C_0$ is initial $\text{PFOA}$ concentration. $C_t$ is $\text{PFOA}$ concentration at time $t$.

#### 2.1.3 Exploratory Data Analysis and Collinearity Structure
- Correlation matrix: Figure S1 shows the Spearman rank-correlation ($\rho$) matrix with significance marks.
- Bivariate relations: Figure S2 shows scatter plots with locally weighted scatterplot smoothing ($\text{LOWESS}$) fits, Pearson ($r$), and Spearman ($\rho$) values.
- Empirical co-variation: Electrochemical predictors show moderate positive correlation ($|\rho| \approx 0.35\text{--}0.55$). For example, electrolysis time correlates with current density.
- Distribution diagnostic: Figure S3 plots the target distribution with a Shapiro-Wilk normality diagnostic.

#### 2.1.4 Preprocessing and Feature Encoding
- Standardization of continuous features: Distance-based models ($\text{KNN}$) and gradient-based models ($\text{DL}$) used standardized $z$-scores:
  $$z = \frac{x - \mu}{\sigma}$$
  where $\mu$ is sample mean and $\sigma$ is sample standard deviation. This scaling avoids numerical instability.
- Scale invariance of tree models: Tree learners ($\text{DT}$, $\text{RF}$, $\text{GBDT}$, and $\text{FLAML-XGBoost}$) trained on unscaled features. Tree split criteria are scale-invariant.
- One-hot encoding: The pipeline converted categorical features into binary indicator columns. This step maintains algorithm parity and enables grouped $\text{SHAP}$ evaluation.
- Low cardinality: Categorical variables have small cardinalities ($\le 6$ levels per field). This property restricts feature dimensionality and matrix sparsity.

### 2.2 Data Splitting and Evaluation Protocol

#### 2.2.1 Stratified Train-Test Partition
- Holdout split ratio: The protocol uses an $80:20$ train-to-test split.
- Stratification strategy: The split stratifies on anode material type. This method prevents covariate shift from uneven anode distributions.
- Target variable handling: The continuous target variable was not stratified. This choice complies with standard regression practices.
- Random seed: A fixed random seed ($\text{seed} = 42$) sets reproducible data splits.

#### 2.2.2 Protocol Evaluation and Diagnostics
- Split stability: Ten independent repetitions of the stratified $80:20$ partition measure performance stability across data splits.
- Stratification diagnostics: Figure S4 documents the sensitivity of the evaluation protocol to alternative splits.
- Nested cross-validation: Figure S5 summarizes the nested cross-validation diagnostics to evaluate internal model selection consistency.

### 2.3 Automated Model Selection via FLAML

#### 2.3.1 Cost-Aware AutoML Search Strategy
- Optimization framework: Fast Lightweight AutoML ($\text{FLAML}$) guides model selection and hyperparameter tuning.
- Search paradigm: $\text{FLAML}$ replaces manual grid searches with a cost-aware, budgeted search.
- Search execution: $\text{FLAML}$ starts with low-cost learners. It then allocates trials adaptively to promising model regions and prunes poor configurations.
- Wall-time budget: The framework enforced a strict search limit of $300\text{ s}$ ($5\text{ min}$).
- Optimization objective: The search minimized 5-fold cross-validation root mean squared error ($5\text{-fold CV RMSE}$):
  $$\text{CV RMSE} = \sqrt{\frac{1}{K} \sum_{k=1}^K \text{MSE}_k}$$
  where $K = 5$ folds.
- Two-level early stopping:
  - Iteration-level stopping: Prunes iterations in boosting models when validation loss stops decreasing.
  - Trial-level stopping: Terminates unpromising hyperparameter trials before full budgets expire.
- Convergence rule: The search stopped when validation error reached a plateau and the incumbent model did not change.

#### 2.3.2 Selected Optimal XGBoost Regressor Configuration
- Champion model: $\text{FLAML}$ selected an Extreme Gradient Boosting ($\text{XGBoost}$) regressor.
- Selected hyperparameter values:
  - Learning rate ($\eta$): $0.1403$
  - Number of estimators (`n_estimators`): $379$
  - Maximum leaf count (`max_leaves`): $13$
  - L1 regularization parameter (`alpha`, $\alpha$): $0.0995$
  - L2 regularization parameter (`lambda`, $\lambda$): $0.0010$
  - Row subsample fraction (`subsample`): $0.85$
  - Column subsample fraction (`colsample_bytree`): $0.83$
- Objective function: $\text{XGBoost}$ minimizes a regularized loss function:
  $$\mathcal{L}(\Theta) = \sum_{i=1}^n l(y_i, \hat{y}_i) + \sum_{m=1}^M \Omega(f_m)$$
  where tree complexity penalty $\Omega(f)$ is:
  $$\Omega(f) = \gamma T + \alpha \sum_{j=1}^T |w_j| + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
  Here $T$ is the number of terminal leaves, $w$ is the vector of leaf weights, $\alpha$ is L1 penalty, and $\lambda$ is L2 penalty.
- Bias-variance balance: The configuration combines a moderate learning rate with constrained leaf size and dual regularization to prevent overfitting.
- SI Table S1: Summarizes the full search space and selected parameters for $\text{XGBoost}$ and all baseline models.

### 2.4 Comparative Benchmarking and Statistical Validation

#### 2.4.1 Benchmark Models and Experimental Parity
- Baseline model suite: The study compared $\text{FLAML-XGBoost}$ against five baseline regressors:
  1. Decision Tree ($\text{DT}$)
  2. Random Forest ($\text{RF}$)
  3. Gradient Boosting Decision Tree ($\text{GBDT}$)
  4. Deep Learning Multi-Layer Perceptron ($\text{DL}$)
  5. k-Nearest Neighbors ($\text{KNN}$)
- Evaluation parity: All models received the identical one-hot encoded dataset under identical stratified $80:20$ train-test splits.
- Repeated evaluations: Ten independent repetitions of the stratified split quantify performance stability.

#### 2.4.2 Mathematical Performance Metrics
- Root Mean Squared Error ($\text{RMSE}$):
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
- Mean Absolute Error ($\text{MAE}$):
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
- Mean Absolute Percentage Error ($\text{MAPE}$):
  $$\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^n \left| \frac{y_i - \hat{y}_i}{y_i} \right|$$
- Pearson Correlation Coefficient ($\text{CC}$, $r$):
  $$r = \frac{\sum_{i=1}^n (y_i - \bar{y})(\hat{y}_i - \bar{\hat{y}})}{\sqrt{\sum_{i=1}^n (y_i - \bar{y})^2 \sum_{i=1}^n (\hat{y}_i - \bar{\hat{y}})^2}}$$
- Coefficient of Determination ($R^2$):
  $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$

#### 2.4.3 Statistical Hypothesis Testing and Effect Size
- Paired $t$-test: Paired two-tailed $t$-tests across ten repetitions evaluated pairwise performance differences at significance level $\alpha = 0.01$.
  - Test statistic:
    $$t = \frac{\bar{D}}{s_D / \sqrt{n}}$$
    where $\bar{D}$ is the mean paired metric difference, $s_D$ is the standard deviation of differences, and $n = 10$.
- Bonferroni correction: Controls the family-wise error rate across multiple hypothesis tests:
  $$\alpha_{\text{adjusted}} = \frac{\alpha}{m}$$
  where $m$ is the number of pairwise model comparisons.
- Cohen's $d$ effect size: Quantifies the standardized magnitude of differences:
  $$d = \frac{\bar{D}}{s_D}$$
  A value of $d > 0.8$ denotes a large effect size independent of sample size.

### 2.5 Interpretability via SHAP Analysis

#### 2.5.1 Game-Theoretic Formulation and TreeSHAP
- Shapley value formulation: SHapley Additive exPlanations ($\text{SHAP}$) allocate marginal contributions to features under cooperative game theory:
  $$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
  where $F$ is the complete feature set, $S$ is a feature subset, and $f_x(S)$ is the conditional expectation.
- Additive attribution property:
  $$f(x) = \phi_0 + \sum_{i=1}^M \phi_i(x)$$
  where $\phi_0 = \mathbb{E}[f(X)]$.
- TreeSHAP algorithm: Computes exact Shapley values in polynomial time $\mathcal{O}(T L D^2)$ for tree ensembles. Here $T$ is tree count, $L$ is leaf count, and $D$ is maximum tree depth.

#### 2.5.2 Grouped Categorical Feature Importances
- Grouping aggregation: Sums absolute $\text{SHAP}$ values across one-hot encoded levels of each parent categorical variable:
  $$I_C(x) = \sum_{j \in L_C} |\phi_j(x)|$$
  where $L_C$ is the set of one-hot indicator columns for categorical feature $C$ ($\text{Anode}$, $\text{Cathode}$, $\text{Electrolyte}$, and $\text{Water Matrix}$).
- Mean global importance:
  $$\bar{I}_C = \frac{1}{N} \sum_{k=1}^N \sum_{j \in L_C} |\phi_{k,j}|$$
  where $N$ is the total number of evaluated samples.

#### 2.5.3 Collinearity Mitigation via Conditional Permutation Importance (CPI)
- Collinearity challenge: Predictor correlations ($|\rho| \approx 0.35\text{--}0.55$) can induce attribution bias in standard TreeSHAP.
- CPI methodology: Resamples feature values conditionally within strata of correlated variables. This operation breaks predictor-target links while preserving predictor-predictor relationships.
- Concordance validation: Kendall's rank correlation coefficient ($\tau$) with $95\%$ confidence intervals (Supplementary Table S2) verifies agreement between grouped TreeSHAP and $\text{CPI}$ rankings:
  $$\tau = \frac{C - D}{\frac{1}{2} n(n-1)}$$
  where $C$ is the number of concordant pairs and $D$ is the number of discordant pairs.

#### 2.5.4 Interaction Dependencies and Leave-One-Out Stability
- SHAP dependence plots: Analyzed for the top three continuous features (electrolysis time, electrolyte concentration, and current density).
- Parameter interactions: Point colors show secondary electrochemical parameters to reveal two-way interaction patterns.
- Leave-one-out ($\text{LOO}$) stability test:
  - Recomputed grouped mean $|\text{SHAP}|$ after removing the top-ranked feature (electrolysis time).
  - Concordance metric: Kendall's $\tau = 0.600$ ($p = 0.136$, Figure S6) confirms feature hierarchy stability.
  - Epistemic note: The authors interpret all $\text{SHAP}$ outputs as model-based attributions rather than causal physical effects.

### 2.6 Reproducibility and Deployment Considerations

#### 2.6.1 Software Environment and Pinned Dependencies
- Execution runtime: Python 3.10.
- Pinned software versions:
  - $\text{FLAML} == 1.2.0$
  - $\text{SHAP} == 0.44.0$
  - $\text{scikit-learn} == 1.4.0$

#### 2.6.2 Containerized Pipeline Architecture
- Container system: Docker container encapsulation.
- Container scope: The Docker container encapsulates data preprocessing, model selection, hyperparameter tuning, validation, and interpretability routines.
- Reproducibility benefit: The container prevents software dependency drift and secures cross-platform execution. This design improves on unversioned scripts from earlier literature.

### 2.7 Methodological Contributions and Distinctions

#### 2.7.1 Methodological Advances Relative to Prior Literature
- Contrast with Alnaimat et al. [30] and traditional workflows:
  1. Cost-aware automated model selection: Replaces manual grid searches with $\text{FLAML}$. This step reduces tuning time by $72\%$ ($300\text{ s}$ budget). It identifies an optimal $\text{XGBoost}$ regressor.
  2. Repeated split statistical validation: Uses stratified $80:20$ partitioning with 10 independent repetitions. Evaluates models with paired two-tailed $t$-tests ($\alpha = 0.01$), Bonferroni corrections, and Cohen's $d$ effect sizes.
  3. Dual-method interpretability scheme: Combines grouped TreeSHAP with conditional permutation importance ($\text{CPI}$) to account for collinear predictors. Concordance statistics (Kendall's $\tau$) and $\text{LOO}$ tests confirm attribution stability.
  4. End-to-end containerized deployment: Encapsulates all components in Docker with pinned dependencies. This setup secures complete experimental reproducibility.

## 3. Results and Discussion

### 3.1 Model Performance and Statistical Validation

#### 3.1.1 Comparative Model Performance Across Evaluation Metrics
- Baseline Benchmark Comparison: The FLAML-optimized XGBoost model showed the best performance across all five evaluation metrics in Table 1.
- FLAML-Optimized XGBoost Error Metrics: The model achieved $\text{RMSE} = 3.97 \pm 0.45$. The model achieved $\text{MAE} = 2.93 \pm 0.31$. The model achieved $\text{MAPE} = 10.02 \pm 3.08\%$.
- FLAML-Optimized XGBoost Fit Metrics: The model reached correlation coefficient $\text{CC} = 0.99 \pm 0.0$. The coefficient of determination reached $R^2 = 0.98 \pm 0.01$.
- Random Forest Performance Metrics: Random Forest reached $\text{RMSE} = 8.05 \pm 1.02$. It reached $\text{MAE} = 5.97 \pm 0.57$. It achieved $\text{MAPE} = 25.17 \pm 10.94\%$. The model reached $\text{CC} = 0.96 \pm 0.01$ and $R^2 = 0.91 \pm 0.02$.
- Decision Tree Performance Metrics: The model reached $\text{RMSE} = 10.31 \pm 2.17$. It reached $\text{MAE} = 7.33 \pm 1.11$. It reached $\text{MAPE} = 24.75 \pm 13.5\%$. The model achieved $\text{CC} = 0.93 \pm 0.03$ and $R^2 = 0.86 \pm 0.07$.
- GBDT Performance Metrics: The GBDT model reached $\text{RMSE} = 9.35 \pm 0.77$. It reached $\text{MAE} = 7.49 \pm 0.58$. It achieved $\text{MAPE} = 32.39 \pm 10.18\%$. The model recorded $\text{CC} = 0.95 \pm 0.01$ and $R^2 = 0.89 \pm 0.01$.
- Deep Learning Performance Metrics: The DL model reached $\text{RMSE} = 12.41 \pm 1.46$. It reached $\text{MAE} = 8.9 \pm 0.55$. It reached $\text{MAPE} = 51.78 \pm 32.25\%$. The model recorded $\text{CC} = 0.9 \pm 0.02$ and $R^2 = 0.8 \pm 0.05$.
- K-Nearest Neighbors Performance Metrics: The KNN model reached $\text{RMSE} = 19.6 \pm 2.38$. It reached $\text{MAE} = 14.35 \pm 1.38$. It recorded $\text{MAPE} = 101.09 \pm 51.01\%$. The model reached $\text{CC} = 0.71 \pm 0.06$ and $R^2 = 0.49 \pm 0.11$.
- Relative Prediction Error Reduction: FLAML XGBoost achieved a $51\%$ reduction in prediction error compared to Random Forest.
- Explained Variance Increase: The model achieved a $7\%$ increase in explained variance relative to Random Forest.

Table 1: Mean and standard deviation of model performance metrics across 10 evaluation runs.
| Model | RMSE | MAE | MAPE (%) | CC | $R^2$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FLAML-optimized XGBoost | $3.97 \pm 0.45$ | $2.93 \pm 0.31$ | $10.02 \pm 3.08$ | $0.99 \pm 0.0$ | $0.98 \pm 0.01$ |
| Random Forest (RF) | $8.05 \pm 1.02$ | $5.97 \pm 0.57$ | $25.17 \pm 10.94$ | $0.96 \pm 0.01$ | $0.91 \pm 0.02$ |
| Decision Tree (DT) | $10.31 \pm 2.17$ | $7.33 \pm 1.11$ | $24.75 \pm 13.5$ | $0.93 \pm 0.03$ | $0.86 \pm 0.07$ |
| Gradient Boosting Decision Tree (GBDT) | $9.35 \pm 0.77$ | $7.49 \pm 0.58$ | $32.39 \pm 10.18$ | $0.95 \pm 0.01$ | $0.89 \pm 0.01$ |
| Deep Learning (DL) | $12.41 \pm 1.46$ | $8.9 \pm 0.55$ | $51.78 \pm 32.25$ | $0.9 \pm 0.02$ | $0.8 \pm 0.05$ |
| K-Nearest Neighbors (KNN) | $19.6 \pm 2.38$ | $14.35 \pm 1.38$ | $101.09 \pm 51.01$ | $0.71 \pm 0.06$ | $0.49 \pm 0.11$ |

#### 3.1.2 Paired Hypothesis Testing and Significance Analysis
- Statistical Significance Criterion: Paired t-tests compared each baseline model against FLAML-optimized XGBoost across all five metrics.
- Global Significance Threshold: The FLAML model exceeded baseline performance with statistical significance at $p < 10^{-5}$ across all metrics.
- Paired Tests Against Random Forest: The comparison gave $\text{RMSE } p = 9.616685 \times 10^{-7}$. It gave $\text{MAE } p = 1.547798 \times 10^{-7}$. It gave $\text{MAPE } p = 0.000610$. The test gave $\text{CC } p = 2.953061 \times 10^{-5}$. The test gave $R^2\text{ } p = 1.260622 \times 10^{-5}$.
- Paired Tests Against Decision Trees: The comparison gave $\text{RMSE } p = 3.20401610 \times 10^{-6}$. It gave $\text{MAE } p = 3.111270 \times 10^{-7}$. It yielded $\text{MAPE } p = 0.004675$. The test gave $\text{CC } p = 1.247765 \times 10^{-4}$. The test gave $R^2\text{ } p = 1.414884 \times 10^{-4}$.
- Paired Tests Against GBDT: The comparison gave $\text{RMSE } p = 1.106071 \times 10^{-8}$. It gave $\text{MAE } p = 5.052537 \times 10^{-9}$. It yielded $\text{MAPE } p = 0.000009$. The test gave $\text{CC } p = 2.678730 \times 10^{-8}$. The test gave $R^2\text{ } p = 1.228068 \times 10^{-8}$.
- Paired Tests Against Deep Learning: The comparison gave $\text{RMSE } p = 2.846609 \times 10^{-9}$. It gave $\text{MAE } p = 3.311756 \times 10^{-11}$. It yielded $\text{MAPE } p = 0.001801$. The test gave $\text{CC } p = 3.080667 \times 10^{-7}$. The test gave $R^2\text{ } p = 4.826925 \times 10^{-7}$.
- Paired Tests Against KNN: The comparison gave $\text{RMSE } p = 6.734575 \times 10^{-9}$. It gave $\text{MAE } p = 1.336126 \times 10^{-9}$. It yielded $\text{MAPE } p = 0.000225$. The test gave $\text{CC } p = 2.164031 \times 10^{-7}$. The test gave $R^2\text{ } p = 1.738757 \times 10^{-7}$.
- Bonferroni Correction: The reported p-values satisfy the Bonferroni adjustment threshold across repeated hypothesis tests.

Table 2: Paired t-test p-values comparing baseline models against FLAML-optimized XGBoost.
| Model | RMSE | MAE | MAPE | CC | $R^2$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Random Forest (RF) | $9.616685 \times 10^{-7}$ | $1.547798 \times 10^{-7}$ | $0.000610$ | $2.953061 \times 10^{-5}$ | $1.260622 \times 10^{-5}$ |
| Decision Tree (DT) | $3.20401610 \times 10^{-6}$ | $3.111270 \times 10^{-7}$ | $0.004675$ | $1.247765 \times 10^{-4}$ | $1.414884 \times 10^{-4}$ |
| Gradient Boosting Decision Tree (GBDT) | $1.106071 \times 10^{-8}$ | $5.052537 \times 10^{-9}$ | $0.000009$ | $2.678730 \times 10^{-8}$ | $1.228068 \times 10^{-8}$ |
| Deep Learning (DL) | $2.846609 \times 10^{-9}$ | $3.311756 \times 10^{-11}$ | $0.001801$ | $3.080667 \times 10^{-7}$ | $4.826925 \times 10^{-7}$ |
| K-Nearest Neighbors (KNN) | $6.734575 \times 10^{-9}$ | $1.336126 \times 10^{-9}$ | $0.000225$ | $2.164031 \times 10^{-7}$ | $1.738757 \times 10^{-7}$ |

#### 3.1.3 Multi-Metric Model Rankings
- FLAML-Optimized XGBoost Standing: The FLAML model ranked $1.0$ across all five metrics. Its overall average rank is $1.0$.
- Random Forest Standing: Random Forest ranked $2.0$ across four metrics and $3.0$ for MAPE. Its overall average rank is $2.2$.
- Intermediate Model Rankings: Decision Trees and GBDT achieved identical overall average ranks of $3.4$.
- Lower Model Rankings: Deep Learning held an average rank of $5.0$. KNN held an average rank of $6.0$.

Table 3: Model rankings across evaluation metrics.
| Model | RMSE Rank | MAE Rank | MAPE Rank | CC Rank | $R^2$ Rank | Average Rank |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FLAML-optimized XGBoost | $1.0$ | $1.0$ | $1.0$ | $1.0$ | $1.0$ | $1.0$ |
| Random Forest (RF) | $2.0$ | $2.0$ | $3.0$ | $2.0$ | $2.0$ | $2.2$ |
| Decision Tree (DT) | $4.0$ | $3.0$ | $2.0$ | $4.0$ | $4.0$ | $3.4$ |
| Gradient Boosting Decision Tree (GBDT) | $3.0$ | $4.0$ | $4.0$ | $3.0$ | $3.0$ | $3.4$ |
| Deep Learning (DL) | $5.0$ | $5.0$ | $5.0$ | $5.0$ | $5.0$ | $5.0$ |
| K-Nearest Neighbors (KNN) | $6.0$ | $6.0$ | $6.0$ | $6.0$ | $6.0$ | $6.0$ |

#### 3.1.4 Overfitting Diagnostics and Learning Curve Dynamics
- Repeated Holdout Design: Ten independent repetitions of the stratified $80:20$ train-test split evaluated model stability.
- Validation Score Trajectory: Figure 1 shows a monotonically decreasing validation RMSE as the training dataset size increases.
- Train-Validation Gap: The train-validation error gap remained stable at $\approx 3\text{--}4\text{ RMSE units}$ at maximum sample size.
- Overfitting Assessment: The stable error gap confirms absence of model divergence or overfitting under the experimental protocol.
- Protocol Sensitivity Verification: Supplementary Figure S4 verifies stratification stability. Supplementary Figure S5 records nested cross-validation diagnostics.

#### 3.1.5 Residual Distributions and Prediction Error Characteristics
- Residual Symmetry and Dispersion: Figure 2 shows that the FLAML model produced the narrowest and most symmetric residual distribution.
- Interquartile Range Magnitude: FLAML achieved an interquartile range ($\text{IQR}$) of $\approx 6\%$, showing minimal systematic bias across operating ranges.
- Baseline Algorithm Distortion: Conventional models displayed wide residual spreads and severe outlier points.
- Extreme Outlier Presence: K-nearest neighbors showed extreme negative residuals below $-70\%$. Deep learning exhibited a positive bias.
- Engineering Risk Mitigation: Tight residual dispersion prevents error propagation into downstream reactor energy calculations.

#### 3.1.6 Optimization Efficiency and Resource Budgeting
- Compute Budget Limit: FLAML converged to the optimal model within a fixed budget of $300\text{ seconds}$.
- Search Duration Reduction: The automated search decreased tuning time by $72\%$ compared to grid search from prior literature.
- Cost-Aware Search Advantage: The search engine tests low-cost models before it evaluates computationally heavy configurations.
- Practical Engineering Benefit: Rapid optimization removes barriers for environmental laboratories with limited computational resources.

### 3.2 Feature Importance and Electrochemical Mechanisms

#### 3.2.1 TreeSHAP Importance Attribution and Hierarchy
- Leading Operational Factor: Both FLAML XGBoost and Random Forest identified electrolysis time as the most influential variable in Figure 3.
- Primary Attribution Magnitudes: Electrolysis time registered a mean absolute SHAP value of $\approx 16.4$ in XGBoost. It reached $\approx 13.6$ in Random Forest.
- Anode Ranking Divergence: Anode material ranked second in XGBoost with a mean absolute SHAP value of $\approx 12.1\text{ percentage points}$.
- Random Forest Anode Attribution: Tuned Random Forest assigned a low mean absolute SHAP value of $\approx 1.5\text{--}2.0$ to anode material.
- Intermediate Importance Tier: XGBoost placed electrolyte concentration in the second tier with a mean absolute SHAP value of $\approx 6.5$.
- Current Density Attribution: Both models assigned high importance to current density ($\approx 5.9$ for XGBoost and $\approx 5.2$ for Random Forest).
- Secondary Input Hierarchy: Initial PFOA concentration, solution pH, temperature, and water matrix occupied the lower importance tiers.

#### 3.2.2 Electrolysis Time and Cumulative Charge Kinetics
- Charge Dependency Theory: PFOA degradation depends directly on cumulative applied charge passage during the process.
- Charge Formula: Total electrical charge relates to current and time via $Q = I \cdot t$, where $t$ is electrolysis time.
- Radical Formation Mechanism: Prolonged electrolysis maintains continuous generation of reactive hydroxyl radicals ($\cdot\text{OH}$).
- Recalcitrant Mineralization: Continuous radical availability drives the step-by-step breakdown of persistent perfluorinated alkyl chains into benign products.

#### 3.2.3 Anode Material Mechanics and Model Discrepancy
- Overpotential Significance: Anode composition dictates the oxygen evolution reaction ($\text{OER}$) overpotential.
- Boron-Doped Diamond Superiority: High-OER anodes like boron-doped diamond ($\text{BDD}$) maximize hydroxyl radical generation during PFAS oxidation.
- Algorithmic Architecture Cause: XGBoost captures nonlinear interactions between anode material and current density.
- Ensemble Dilution Effect: Random Forest averages individual decision trees, which dilutes subtle interaction effects.
- Permutation Importance Confirmation: Supplementary Table S2 confirms consistency between SHAP attributions and conditional permutation importance.

#### 3.2.4 Electrolyte Concentration and Solution Conductivity
- Conductivity Modulation: Electrolyte concentration ($10\text{--}100\text{ mM}$) directly controls solution conductivity ($1.2\text{--}12.5\text{ mS}\cdot\text{cm}^{-1}$).
- Kinetic Trade-Off: Moderate ionic strength increases hydroxyl radical production while suppressing parasitic oxygen evolution at the anode.
- Parasitic Side Reactions: High electrolyte concentrations ($> 50\text{ mM}$) cause radical scavenging and reduce overall oxidation efficiency.
- Second-Tier Magnitude: Electrolyte concentration registered a mean absolute SHAP value of $\approx 6.5\text{ percentage points}$.
- Mechanistic Consistency: XGBoost captures this kinetic trade-off between ionic mobility and radical consumption.

#### 3.2.5 Current Density, Initial Concentration, and Secondary Factors
- Current Density Radical Control: Proper current density maintains efficient radical production at the electrode interface.
- Parasitic Energy Losses: Excessively high current density accelerates unwanted oxygen evolution and increases electrical energy consumption.
- Initial Concentration Influence: Random Forest ranked initial PFOA concentration second due to sensitivity to pseudo-first-order concentration gradients.
- Solution pH Chemistry: Solution pH influences electrode surface charge and radical speciation.
- Thermal Effects: Operating temperature showed subtle effects within typical operational ranges compared to electrical variables.
- Water Matrix Stability: Water matrix ranked near the bottom of Figure 3, showing low impact within tested conditions.

### 3.3 Dose-Response Patterns and Stability of SHAP Explanations

#### 3.3.1 Nonlinear Continuous Feature Dose-Response Profiles
- Electrolysis Time Curve: Figure 4A shows a strongly monotonic increase in SHAP values as electrolysis time increases.
- Plateau Behavior: The contribution of electrolysis time starts negative at short times and plateaus between $20$ and $30\text{ percentage points}$.
- Electrolyte Concentration Response: Figure 4B shows a clear threshold pattern for electrolyte concentration.
- Concentration Penalty Zone: Sub-optimal electrolyte levels yield negative SHAP contributions, while extreme high concentrations cause penalties.
- Current Density Trajectory: Figure 4C shows an approximately monotonic increase in SHAP values across current density.
- Diminishing Return Regime: High current densities show diminishing marginal returns in removal efficiency contribution.

#### 3.3.2 Leave-One-Out Sensitivity and Explanation Stability
- Feature Removal Test: Removing electrolysis time and retraining the XGBoost model tested attribution stability in Figure S6.
- Hierarchy Retention: Anode material and current density remained in the leading importance tier after retraining.
- Stable Lower Tier: Initial pH, cathode material, temperature, and electrode spacing stayed in the secondary tier.
- Concordance Statistic: The ranking comparison yielded Kendall's rank correlation coefficient $\tau = 0.600$ with $p = 0.136$.
- Attribution Scope Distinction: All SHAP values represent statistical model attributions and not direct physical causal relationships.

### 3.4 Implications for PFAS Treatment Optimization

#### 3.4.1 Engineering Guidance for Electrochemical Reactor Design
- Cumulative Charge Prioritization: Operational design must allocate adequate electrolysis time ($60\text{--}180\text{ min}$) to achieve $> 90\%$ removal.
- Current Density Window: Engineers should operate reactors within $10\text{--}30\text{ mA}\cdot\text{cm}^{-2}$ to balance radical flux against cell voltage.
- Material Selection Strategy: Engineers must pair high-OER anodes ($\text{BDD}$) with compatible current density regimes to balance cost and oxidation rates.
- Water Matrix Transferability: Low matrix sensitivity indicates that treatment settings transfer across varied waters without extensive recalibration.

#### 3.4.2 Setpoint Control and Energy Auditing Requirements
- Precise Operational Windows: High model accuracy supports tight setpoint control for current density and operational duration.
- Energy Auditing Scope: The machine learning model does not predict volumetric energy consumption in $\text{kWh}\cdot\text{m}^{-3}$ directly.
- Empirical Energy Validation: Reactor deployment requires separate physical energy audits under verified pilot conditions.
- PFAS Transfer Learning: Model structure supports transfer learning to other PFAS targets like $\text{PFOS}$ and $\text{GenX}$.

### 3.5 Limitations and Future Directions

#### 3.5.1 Dataset Scope and Multi-System Generalizability
- External System Validation: Researchers must evaluate the modeling framework on external datasets from different reactor configurations.
- Chemical Spectrum Expansion: Future work must evaluate more PFAS compounds such as $\text{PFOS}$, short-chain homologs, and co-contaminants.
- Cross-Domain Transfer: Transfer learning algorithms can reuse learned representations to accelerate model training for new electrochemical systems.

#### 3.5.2 Multi-Objective Optimization and Real-Time Control
- Multi-Objective Scope: Optimization pipelines must balance PFOA removal, electrical energy consumption, and toxic byproduct formation.
- Byproduct Monitoring Targets: Models must account for hazardous byproducts, including shorter-chain perfluoroalkyl acids, chlorate, and perchlorate.
- Computational Trade-Offs: Future tools must optimize the balance between search speed and predictive performance.
- In Situ Dynamic Control: Connecting FLAML models to online physical sensors enables automated real-time process adjustments.

#### 3.5.3 Hybrid Modeling and Algorithmic Enhancements
- Physics-Informed ML Architecture: Integrating empirical boosted trees with electrochemical kinetic and mass transport equations improves interpretability.
- Native Categorical Splitting: Evaluating native categorical tree split algorithms will remove the need for one-hot encoding preprocessing.

## 4. Conclusions and Supporting Information

### 4.1 Research Conclusions and Core Synthesis
#### 4.1.1 Automated Model Performance and Tuning Efficiency
- Automated Machine Learning Advantage: Automated machine learning with FLAML removes manual trial-and-error in electrochemical process modeling.
- Predictive Accuracy Achievement: The selected XGBoost model achieved $\text{RMSE} = 3.97$ and determination coefficient $R^2 = 0.98$.
- Baseline Comparison Results: The FLAML model outperformed Random Forest, Gradient Boosting, Deep Learning, and k-Nearest Neighbors.
- Statistical Significance Validation: Paired two-tailed t-tests with Bonferroni correction confirmed significant performance improvements ($p < 10^{-5}$).
- Optimization Time Reduction: FLAML decreased hyperparameter tuning time by $72\%$ compared to conventional grid and manual search workflows.
- Bounded Search Duration: The automated search completed all iterations within a strict wall-clock budget of $300\text{ s}$ ($5\text{ minutes}$).

#### 4.1.2 Verified Operational Drivers and Kinetic Principles
- Primary Operational Determinants: Interpretability analysis identified total electrolysis time and anode material as the primary operational drivers.
- Kinetic Theory Alignment: Feature importance rankings match electrochemical principles where cumulative charge controls pollutant destruction.
- Electrode Material Impact: Anode material governs the oxygen evolution overpotential and regulates the yield of reactive hydroxyl radicals.
- Secondary Operational Determinants: Electrolyte concentration and current density form a secondary tier of influential process variables.
- Non-Linear Dependency Attribution: SHAP values showed non-linear effects and parameter interactions without human selection bias.
- Operational Saturation Patterns: SHAP dependence plots revealed monotonic removal growth with electrolysis time and plateau effects at high current density.

### 4.2 Methodological Innovations and Future Research Directions
#### 4.2.1 Pipeline Standardization and Software Containerization
- Containerized Execution Environment: The author encapsulated the modeling workflow inside a Docker container for complete cross-platform reproducibility.
- Software Dependencies: The software environment fixed exact library releases: Python 3.10, FLAML 1.2.0, SHAP 0.44.0, and scikit-learn 1.4.0.
- Mitigation of Environmental Drift: Containerization prevents package dependency conflicts and allows independent evaluation by third parties.
- Methodological Standardization: The standardized pipeline addresses the limitations of untracked scripting habits found in earlier research.
- Workflow Decoupling Strategy: The framework isolates the FLAML hyperparameter search phase from the final XGBoost model deployment.

#### 4.2.2 Future Directions and Remediation Expansion
- Physics-Informed Machine Learning: Future research will merge electrochemical transport equations with data-driven predictive architectures.
- Adaptive Process Control: Automated pipelines can connect to real-time sensors to adjust treatment conditions dynamically.
- Extended PFAS Scope: Researchers can adapt the methodology to short-chain perfluoroalkyl substances and modern replacements like GenX.
- Multi-Objective Process Targets: Future work must balance PFOA removal against electrical energy per order ($\text{EE/O}$) and total operational costs.
- Pilot-Scale Reactor Testing: Engineers must validate the framework on continuous-flow electrochemical reactors under industrial field conditions.

### 4.3 Authorship, Ethics, and Institutional Support
#### 4.3.1 CRediT Authorship Contribution Statement
- Sole Research Attribution: Haitham Elnakar executed all aspects of the published study.
- Conceptualization and Methodology: Haitham Elnakar developed the conceptual framework and designed the automated machine learning methodology.
- Formal Analysis and Investigation: Haitham Elnakar performed the model training, statistical tests, and interpretability evaluations.
- Data Curation and Visualization: Haitham Elnakar processed the experimental records and generated all data figures.
- Writing the Original Draft: Haitham Elnakar wrote the initial manuscript draft.
- Review and Text Editing: Haitham Elnakar revised the draft and prepared the final published text.

#### 4.3.2 Declaration of Competing Interest
- Conflict of Interest Disclosure: The author declares no known competing financial interests or personal relationships that influenced this study.
- Absence of Commercial Bias: The research proceeded independently without commercial sponsor involvement.

#### 4.3.3 Acknowledgment
- Institutional Financial Support: King Fahd University of Petroleum and Minerals (KFUPM) supported this publication.
- Primary Academic Affiliation: Department of Civil and Environmental Engineering, KFUPM, Dhahran 31261, Saudi Arabia.
- Interdisciplinary Center Affiliation: Interdisciplinary Research Center for Construction and Building Materials, KFUPM, Dhahran 31261, Saudi Arabia.

### 4.4 Appendix A: Supporting Information Inventory
#### 4.4.1 Exploratory and Diagnostic Visualizations (Figures S1 to S3)
- Online File Access: Supporting data is available online through the digital object identifier $\text{doi: } 10.1016/\text{j.dwt.2025.101598}$.
- Figure S1 (Predictor Correlation): A Spearman rank-correlation heatmap displays significance marks for associations among electrochemical predictors.
- Figure S2 (Bivariate Relationships): Pairwise scatterplots with LOWESS curves and correlation metrics illustrate collinearity ($|\rho| \approx 0.35\text{ to }0.55$).
- Figure S3 (Target Distribution): The histogram displays removal percentage distributions alongside a Shapiro-Wilk normality diagnostic.

#### 4.4.2 Validation Stability and Attribution Consistency (Figures S4 to S6)
- Figure S4 (Stratification Sensitivity): Boxplots summarize metric distributions across repeated data partitions stratified on anode material.
- Figure S5 (Nested Cross-Validation): Diagnostic plots confirm model selection consistency across nested cross-validation folds.
- Figure S6 (Leave-One-Out SHAP Stability): Feature importance stability evaluation after removing the top predictor (electrolysis time).
- Concordance Statistic: The leave-one-out test yielded a Kendall rank correlation $\tau = 0.600$ ($p = 0.136$), confirming stable secondary rankings.

#### 4.4.3 Hyperparameter Configurations and Rank Concordance (Tables S1 and S2)
- Table S1 (Search Space and Bounds): The table lists hyperparameter search ranges and evaluation budgets for all evaluated learners.
- Selected Tree Hyperparameters: Parameters include $\text{learning\_rate} = 0.1403$, $\text{n\_estimators} = 379$, and $\text{max\_leaves} = 13$.
- Selected Regularization Hyperparameters: Parameters include $\alpha = 0.0995$, $\lambda = 0.0010$, $\text{subsample} = 0.85$, and $\text{colsample\_bytree} = 0.83$.
- Table S2 (Importance Concordance): Agreement metrics compare grouped TreeSHAP rankings against Conditional Permutation Importance (CPI).
- Collinearity Independence: Kendall rank correlation values with $95\%$ confidence intervals confirmed that feature attributions remained reliable.

### 4.5 Data Availability and Repository Attribution
#### 4.5.1 Benchmark Dataset Provenance and Access
- Primary Data Source: The study evaluated experimental records compiled and published by Alnaimat et al. [30] in 2024.
- Source Article Citation: Alnaimat S., Mohsen O., Elnakar H., *J. Environ. Manage.* 370 (2024) 122857.
- Open Data Statement: The dataset is available through the cited reference in the methodology section.
- Direct Literature Parity: Evaluating the Alnaimat dataset enabled direct performance comparisons against earlier machine learning benchmarks.

#### 4.5.2 Feature Encoding and Preprocessing Parity
- Input Variable Scope: The dataset includes eight continuous and categorical electrochemical process variables.
- Categorical Field Encoding: One-hot encoding converted categorical variables (anode, cathode, electrolyte, water matrix) with cardinality $\le 6$.
- Continuous Feature Standardization: Z-score standardization scaled continuous features for distance-based and gradient-based algorithms.
- Tree Split Invariance: Tree-based learners trained on unscaled features because decision tree split criteria exhibit scale invariance.
- Stratified Partition Protocol: An 80:20 train-test partition stratified on anode type prevented covariate shift across training and test subsets.

### 4.6 Selected Literature References
#### 4.6.1 Automated Machine Learning and Explainable AI Foundations
- Fast Lightweight AutoML Framework: Wang et al. (2021) introduced the FLAML library for cost-aware hyperparameter optimization [27].
- Game-Theoretic Interpretability: Lundberg and Lee (2017) unified feature attributions through SHapley Additive exPlanations (SHAP) [33].
- Scalable Tree Boosting: Chen and Guestrin (2016) developed XGBoost as a scalable tree boosting system [43].
- Environmental ML Best Practices: Zhu et al. (2023, 2024) established the EMBRACE reporting checklist for machine learning in environmental engineering [22, 23].
- Wetland Treatment Modeling: Bao et al. (2023) used automated machine learning to predict antibiotic removal in constructed wetlands [28].
- Digestion Process Modeling: Xu et al. (2022) predicted microplastic impacts on anaerobic digestion methane production with AutoML [29].
- Water Plant Dosage Prediction: Feng et al. (2025) applied AutoML and SHAP to predict coagulant dosage in drinking water plants [24].

#### 4.6.2 Electrochemical PFAS Degradation and Environmental Standards
- Reference PFOA Benchmark: Alnaimat et al. (2024) modeled PFOA removal through electrochemical oxidation with machine learning [30].
- Drinking Water Regulations: US EPA (2025) established the Final PFAS National Primary Drinking Water Regulation with a $4\text{ ng/L}$ MCL [6].
- Strategic Remediation Policy: US EPA (2023) published the PFAS Strategic Roadmap detailing second-year remediation progress [47].
- Human Carcinogenicity Evaluation: Zahm et al. (2024) classified PFOA as carcinogenic to humans in Lancet Oncology (Group 1) [5].
- Electrochemical Review Foundations: Chaplin (2014) reviewed electrochemical advanced oxidation processes for water treatment [42].
- Anodic Oxidation Mechanisms: Panizza and Cerisola (2009) classified direct and mediated anodic oxidation mechanisms for organic pollutants [41].
- Wastewater Treatment Applications: Martínez-Huitle and Panizza (2018) surveyed electrochemical oxidation technologies for wastewater treatment [39].
- Novel Electrode Membranes: Liang et al. (2025) synthesized durable $\text{Ti}_4\text{O}_7$ heterojunction composite membranes for GenX electro-oxidation [14].
- Persulfate Activation Support: Samuel et al. (2024) enhanced PFOA degradation by electrochemically activating peroxydisulfate [15].
