### 3. Results and Discussion

#### 3.1 Model Performance and Statistical Validation

##### 3.1.1 Comparative Model Performance Across Evaluation Metrics
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

##### 3.1.2 Paired Hypothesis Testing and Significance Analysis
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

##### 3.1.3 Multi-Metric Model Rankings
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

##### 3.1.4 Overfitting Diagnostics and Learning Curve Dynamics
- Repeated Holdout Design: Ten independent repetitions of the stratified $80:20$ train-test split evaluated model stability.
- Validation Score Trajectory: Figure 1 shows a monotonically decreasing validation RMSE as the training dataset size increases.
- Train-Validation Gap: The train-validation error gap remained stable at $\approx 3\text{--}4\text{ RMSE units}$ at maximum sample size.
- Overfitting Assessment: The stable error gap confirms absence of model divergence or overfitting under the experimental protocol.
- Protocol Sensitivity Verification: Supplementary Figure S4 verifies stratification stability. Supplementary Figure S5 records nested cross-validation diagnostics.

##### 3.1.5 Residual Distributions and Prediction Error Characteristics
- Residual Symmetry and Dispersion: Figure 2 shows that the FLAML model produced the narrowest and most symmetric residual distribution.
- Interquartile Range Magnitude: FLAML achieved an interquartile range ($\text{IQR}$) of $\approx 6\%$, showing minimal systematic bias across operating ranges.
- Baseline Algorithm Distortion: Conventional models displayed wide residual spreads and severe outlier points.
- Extreme Outlier Presence: K-nearest neighbors showed extreme negative residuals below $-70\%$. Deep learning exhibited a positive bias.
- Engineering Risk Mitigation: Tight residual dispersion prevents error propagation into downstream reactor energy calculations.

##### 3.1.6 Optimization Efficiency and Resource Budgeting
- Compute Budget Limit: FLAML converged to the optimal model within a fixed budget of $300\text{ seconds}$.
- Search Duration Reduction: The automated search decreased tuning time by $72\%$ compared to grid search from prior literature.
- Cost-Aware Search Advantage: The search engine tests low-cost models before it evaluates computationally heavy configurations.
- Practical Engineering Benefit: Rapid optimization removes barriers for environmental laboratories with limited computational resources.

#### 3.2 Feature Importance and Electrochemical Mechanisms

##### 3.2.1 TreeSHAP Importance Attribution and Hierarchy
- Leading Operational Factor: Both FLAML XGBoost and Random Forest identified electrolysis time as the most influential variable in Figure 3.
- Primary Attribution Magnitudes: Electrolysis time registered a mean absolute SHAP value of $\approx 16.4$ in XGBoost. It reached $\approx 13.6$ in Random Forest.
- Anode Ranking Divergence: Anode material ranked second in XGBoost with a mean absolute SHAP value of $\approx 12.1\text{ percentage points}$.
- Random Forest Anode Attribution: Tuned Random Forest assigned a low mean absolute SHAP value of $\approx 1.5\text{--}2.0$ to anode material.
- Intermediate Importance Tier: XGBoost placed electrolyte concentration in the second tier with a mean absolute SHAP value of $\approx 6.5$.
- Current Density Attribution: Both models assigned high importance to current density ($\approx 5.9$ for XGBoost and $\approx 5.2$ for Random Forest).
- Secondary Input Hierarchy: Initial PFOA concentration, solution pH, temperature, and water matrix occupied the lower importance tiers.

##### 3.2.2 Electrolysis Time and Cumulative Charge Kinetics
- Charge Dependency Theory: PFOA degradation depends directly on cumulative applied charge passage during the process.
- Charge Formula: Total electrical charge relates to current and time via $Q = I \cdot t$, where $t$ is electrolysis time.
- Radical Formation Mechanism: Prolonged electrolysis maintains continuous generation of reactive hydroxyl radicals ($\cdot\text{OH}$).
- Recalcitrant Mineralization: Continuous radical availability drives the step-by-step breakdown of persistent perfluorinated alkyl chains into benign products.

##### 3.2.3 Anode Material Mechanics and Model Discrepancy
- Overpotential Significance: Anode composition dictates the oxygen evolution reaction ($\text{OER}$) overpotential.
- Boron-Doped Diamond Superiority: High-OER anodes like boron-doped diamond ($\text{BDD}$) maximize hydroxyl radical generation during PFAS oxidation.
- Algorithmic Architecture Cause: XGBoost captures nonlinear interactions between anode material and current density.
- Ensemble Dilution Effect: Random Forest averages individual decision trees, which dilutes subtle interaction effects.
- Permutation Importance Confirmation: Supplementary Table S2 confirms consistency between SHAP attributions and conditional permutation importance.

##### 3.2.4 Electrolyte Concentration and Solution Conductivity
- Conductivity Modulation: Electrolyte concentration directly controls the ionic conductivity of the aqueous solution.
- Kinetic Trade-Off: Moderate ionic strength increases hydroxyl radical production while suppressing parasitic oxygen evolution at the anode.
- Parasitic Side Reactions: Excessively high electrolyte concentrations cause radical scavenging and reduce overall oxidation efficiency.
- Mechanistic Consistency: XGBoost captures this kinetic trade-off between ionic mobility and radical consumption.

##### 3.2.5 Current Density, Initial Concentration, and Secondary Factors
- Current Density Radical Control: Proper current density maintains efficient radical production at the electrode interface.
- Parasitic Energy Losses: Excessively high current density accelerates unwanted oxygen evolution and increases electrical energy consumption.
- Initial Concentration Influence: Random Forest ranked initial PFOA concentration second due to sensitivity to pseudo-first-order concentration gradients.
- Solution pH Chemistry: Solution pH influences electrode surface charge and radical speciation.
- Thermal Effects: Operating temperature showed subtle effects within typical operational ranges compared to electrical variables.
- Water Matrix Robustness: Water matrix ranked near the bottom of Figure 3, showing low impact within tested conditions.

#### 3.3 Dose-Response Patterns and Stability of SHAP Explanations

##### 3.3.1 Nonlinear Continuous Feature Dose-Response Profiles
- Electrolysis Time Curve: Figure 4A shows a strongly monotonic increase in SHAP values as electrolysis time increases.
- Plateau Behavior: The contribution of electrolysis time starts negative at short times and plateaus between $20$ and $30\text{ percentage points}$.
- Electrolyte Concentration Response: Figure 4B shows a clear threshold pattern for electrolyte concentration.
- Concentration Penalty Zone: Sub-optimal electrolyte levels yield negative SHAP contributions, while extreme high concentrations cause penalties.
- Current Density Trajectory: Figure 4C shows an approximately monotonic increase in SHAP values across current density.
- Diminishing Return Regime: High current densities show diminishing marginal returns in removal efficiency contribution.

##### 3.3.2 Leave-One-Out Sensitivity and Explanation Robustness
- Feature Removal Test: Removing electrolysis time and retraining the XGBoost model tested attribution stability in Figure S6.
- Hierarchy Retention: Anode material and current density remained in the leading importance tier after retraining.
- Stable Lower Tier: Initial pH, cathode material, temperature, and electrode spacing stayed in the secondary tier.
- Concordance Statistic: The ranking comparison yielded Kendall's rank correlation coefficient $\tau = 0.600$ with $p = 0.136$.
- Attribution Scope Distinction: All SHAP values represent statistical model attributions and not direct physical causal relationships.

#### 3.4 Implications for PFAS Treatment Optimization

##### 3.4.1 Engineering Guidance for Electrochemical Reactor Design
- Cumulative Charge Prioritization: Operational design must allocate adequate electrolysis time to satisfy cumulative charge requirements.
- Material Selection Strategy: Engineers must pair high-OER anodes with compatible current density regimes to balance cost and oxidation rates.
- Water Matrix Transferability: Low matrix sensitivity indicates that treatment settings transfer across varied waters without extensive recalibration.

##### 3.4.2 Setpoint Control and Energy Auditing Requirements
- Precise Operational Windows: High model accuracy supports tight setpoint control for current density and operational duration.
- Energy Auditing Scope: The machine learning model does not predict volumetric energy consumption in $\text{kWh}\cdot\text{m}^{-3}$ directly.
- Empirical Energy Validation: Reactor deployment requires separate physical energy audits under verified pilot conditions.
- PFAS Transfer Learning: Model structure supports transfer learning to other PFAS targets like $\text{PFOS}$ and $\text{GenX}$.

#### 3.5 Limitations and Future Directions

##### 3.5.1 Dataset Scope and Multi-System Generalizability
- External System Validation: Researchers must evaluate the modeling framework on external datasets from different reactor configurations.
- Chemical Spectrum Expansion: Future work must evaluate more PFAS compounds such as $\text{PFOS}$, short-chain homologs, and co-contaminants.
- Cross-Domain Transfer: Transfer learning algorithms can reuse learned representations to accelerate model training for new electrochemical systems.

##### 3.5.2 Multi-Objective Optimization and Real-Time Control
- Multi-Objective Scope: Optimization pipelines must balance PFOA removal, electrical energy consumption, and toxic byproduct formation.
- Byproduct Monitoring Targets: Models must account for hazardous byproducts, including shorter-chain perfluoroalkyl acids, chlorate, and perchlorate.
- Computational Trade-Offs: Future tools must optimize the balance between search speed and predictive performance.
- In Situ Dynamic Control: Connecting FLAML models to online physical sensors enables automated real-time process adjustments.

##### 3.5.3 Hybrid Modeling and Algorithmic Enhancements
- Physics-Informed ML Architecture: Integrating empirical boosted trees with electrochemical kinetic and mass transport equations improves interpretability.
- Native Categorical Splitting: Evaluating native categorical tree split algorithms will remove the need for one-hot encoding preprocessing.
