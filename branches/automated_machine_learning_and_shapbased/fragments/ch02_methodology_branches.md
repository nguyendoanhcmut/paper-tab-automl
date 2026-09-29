### 2. Methodology

#### 2.1 Dataset Characteristics and Preprocessing

##### 2.1.1 Dataset Origin and Experimental Scope
- Source dataset: The study uses the experimental dataset from Alnaimat et al. [30].
- Target domain: The data record the electrochemical degradation of perfluorooctanoic acid ($\text{PFOA}$, $\text{C}_7\text{F}_{15}\text{COOH}$) in water.
- Experimental scope: The dataset contains distinct treatment trials. Operational variables and water characteristics define each trial.

##### 2.1.2 Input and Target Variables
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

##### 2.1.3 Exploratory Data Analysis and Collinearity Structure
- Correlation matrix: Figure S1 shows the Spearman rank-correlation ($\rho$) matrix with significance marks.
- Bivariate relations: Figure S2 shows scatter plots with locally weighted scatterplot smoothing ($\text{LOWESS}$) fits, Pearson ($r$), and Spearman ($\rho$) values.
- Empirical co-variation: Electrochemical predictors show moderate positive correlation ($|\rho| \approx 0.35\text{--}0.55$). For example, electrolysis time correlates with current density.
- Distribution diagnostic: Figure S3 plots the target distribution with a Shapiro-Wilk normality diagnostic.

##### 2.1.4 Preprocessing and Feature Encoding
- Standardization of continuous features: Distance-based models ($\text{KNN}$) and gradient-based models ($\text{DL}$) used standardized $z$-scores:
  $$z = \frac{x - \mu}{\sigma}$$
  where $\mu$ is sample mean and $\sigma$ is sample standard deviation. This scaling avoids numerical instability.
- Scale invariance of tree models: Tree learners ($\text{DT}$, $\text{RF}$, $\text{GBDT}$, and $\text{FLAML-XGBoost}$) trained on unscaled features. Tree split criteria are scale-invariant.
- One-hot encoding: The pipeline converted categorical features into binary indicator columns. This step maintains algorithm parity and enables grouped $\text{SHAP}$ evaluation.
- Low cardinality: Categorical variables have small cardinalities ($\le 6$ levels per field). This property restricts feature dimensionality and matrix sparsity.

#### 2.2 Data Splitting and Evaluation Protocol

##### 2.2.1 Stratified Train-Test Partition
- Holdout split ratio: The protocol uses an $80:20$ train-to-test split.
- Stratification strategy: The split stratifies on anode material type. This method prevents covariate shift from uneven anode distributions.
- Target variable handling: The continuous target variable was not stratified. This choice complies with standard regression practices.
- Random seed: A fixed random seed ($\text{seed} = 42$) sets reproducible data splits.

##### 2.2.2 Protocol Evaluation and Diagnostics
- Split stability: Ten independent repetitions of the stratified $80:20$ partition measure performance stability across data splits.
- Stratification diagnostics: Figure S4 documents the sensitivity of the evaluation protocol to alternative splits.
- Nested cross-validation: Figure S5 summarizes the nested cross-validation diagnostics to evaluate internal model selection consistency.

#### 2.3 Automated Model Selection via FLAML

##### 2.3.1 Cost-Aware AutoML Search Strategy
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

##### 2.3.2 Selected Optimal XGBoost Regressor Configuration
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

#### 2.4 Comparative Benchmarking and Statistical Validation

##### 2.4.1 Benchmark Models and Experimental Parity
- Baseline model suite: The study compared $\text{FLAML-XGBoost}$ against five baseline regressors:
  1. Decision Tree ($\text{DT}$)
  2. Random Forest ($\text{RF}$)
  3. Gradient Boosting Decision Tree ($\text{GBDT}$)
  4. Deep Learning Multi-Layer Perceptron ($\text{DL}$)
  5. k-Nearest Neighbors ($\text{KNN}$)
- Evaluation parity: All models received the identical one-hot encoded dataset under identical stratified $80:20$ train-test splits.
- Repeated evaluations: Ten independent repetitions of the stratified split quantify performance stability.

##### 2.4.2 Mathematical Performance Metrics
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

##### 2.4.3 Statistical Hypothesis Testing and Effect Size
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

#### 2.5 Interpretability via SHAP Analysis

##### 2.5.1 Game-Theoretic Formulation and TreeSHAP
- Shapley value formulation: SHapley Additive exPlanations ($\text{SHAP}$) allocate marginal contributions to features under cooperative game theory:
  $$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
  where $F$ is the complete feature set, $S$ is a feature subset, and $f_x(S)$ is the conditional expectation.
- Additive attribution property:
  $$f(x) = \phi_0 + \sum_{i=1}^M \phi_i(x)$$
  where $\phi_0 = \mathbb{E}[f(X)]$.
- TreeSHAP algorithm: Computes exact Shapley values in polynomial time $\mathcal{O}(T L D^2)$ for tree ensembles. Here $T$ is tree count, $L$ is leaf count, and $D$ is maximum tree depth.

##### 2.5.2 Grouped Categorical Feature Importances
- Grouping aggregation: Sums absolute $\text{SHAP}$ values across one-hot encoded levels of each parent categorical variable:
  $$I_C(x) = \sum_{j \in L_C} |\phi_j(x)|$$
  where $L_C$ is the set of one-hot indicator columns for categorical feature $C$ ($\text{Anode}$, $\text{Cathode}$, $\text{Electrolyte}$, and $\text{Water Matrix}$).
- Mean global importance:
  $$\bar{I}_C = \frac{1}{N} \sum_{k=1}^N \sum_{j \in L_C} |\phi_{k,j}|$$
  where $N$ is the total number of evaluated samples.

##### 2.5.3 Collinearity Mitigation via Conditional Permutation Importance (CPI)
- Collinearity challenge: Predictor correlations ($|\rho| \approx 0.35\text{--}0.55$) can induce attribution bias in standard TreeSHAP.
- CPI methodology: Resamples feature values conditionally within strata of correlated variables. This operation breaks predictor-target links while preserving predictor-predictor relationships.
- Concordance validation: Kendall's rank correlation coefficient ($\tau$) with $95\%$ confidence intervals (Supplementary Table S2) verifies agreement between grouped TreeSHAP and $\text{CPI}$ rankings:
  $$\tau = \frac{C - D}{\frac{1}{2} n(n-1)}$$
  where $C$ is the number of concordant pairs and $D$ is the number of discordant pairs.

##### 2.5.4 Interaction Dependencies and Leave-One-Out Stability
- SHAP dependence plots: Analyzed for the top three continuous features (electrolysis time, electrolyte concentration, and current density).
- Parameter interactions: Point colors show secondary electrochemical parameters to reveal two-way interaction patterns.
- Leave-one-out ($\text{LOO}$) stability test:
  - Recomputed grouped mean $|\text{SHAP}|$ after removing the top-ranked feature (electrolysis time).
  - Concordance metric: Kendall's $\tau = 0.600$ ($p = 0.136$, Figure S6) confirms feature hierarchy stability.
  - Epistemic note: The authors interpret all $\text{SHAP}$ outputs as model-based attributions rather than causal physical effects.

#### 2.6 Reproducibility and Deployment Considerations

##### 2.6.1 Software Environment and Pinned Dependencies
- Execution runtime: Python 3.10.
- Pinned software versions:
  - $\text{FLAML} == 1.2.0$
  - $\text{SHAP} == 0.44.0$
  - $\text{scikit-learn} == 1.4.0$

##### 2.6.2 Containerized Pipeline Architecture
- Container system: Docker container encapsulation.
- Container scope: The Docker container encapsulates data preprocessing, model selection, hyperparameter tuning, validation, and interpretability routines.
- Reproducibility benefit: The container prevents software dependency drift and secures cross-platform execution. This design improves on unversioned scripts from earlier literature.

#### 2.7 Methodological Contributions and Distinctions

##### 2.7.1 Methodological Advances Relative to Prior Literature
- Contrast with Alnaimat et al. [30] and traditional workflows:
  1. Cost-aware automated model selection: Replaces manual grid searches with $\text{FLAML}$. This step reduces tuning time by $72\%$ ($300\text{ s}$ budget). It identifies an optimal $\text{XGBoost}$ regressor.
  2. Repeated split statistical validation: Uses stratified $80:20$ partitioning with 10 independent repetitions. Evaluates models with paired two-tailed $t$-tests ($\alpha = 0.01$), Bonferroni corrections, and Cohen's $d$ effect sizes.
  3. Dual-method interpretability scheme: Combines grouped TreeSHAP with conditional permutation importance ($\text{CPI}$) to account for collinear predictors. Concordance statistics (Kendall's $\tau$) and $\text{LOO}$ tests confirm attribution stability.
  4. End-to-end containerized deployment: Encapsulates all components in Docker with pinned dependencies. This setup secures complete experimental reproducibility.
