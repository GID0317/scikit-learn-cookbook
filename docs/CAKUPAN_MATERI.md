# Cakupan Materi Chapter 1–8

Pemetaan materi buku **scikit-learn Cookbook, Third Edition** (John Sukup, Packt, 2025) ke pembahasan notebook. Halaman mengacu pada nomor cetak buku. Baris mengelompokkan konsep yang dijelaskan bersama; jumlah baris bukan jumlah seluruh subjudul buku. Subjudul prosedural seperti Getting ready dan How it works dibahas dalam recipe terkait. Contoh tambahan dinyatakan dalam notebook.

## Chapter 1: Common Conventions and API Elements of scikit-learn

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Introduction to scikit-learn’s design philosophy | 2 | [Design Philosophy](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#design-philosophy) |
| Understanding estimators; fit and predict | 3 | [Understanding Estimators](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#understanding-estimators) |
| fit_predict and KMeans | 4 | [Understanding Estimators](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#understanding-estimators) |
| Transformers and the transform() method; fit_transform | 4 | [Transformers and the transform Method](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#transformers-and-the-transform-method) |
| Handling custom estimators and transformers; mixins | 7 | [Handling Custom Estimators and Transformers](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#handling-custom-estimators-and-transformers) |
| Pipelines and workflow automation; MLOps | 7 | [Pipelines and Workflow Automation](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#pipelines-and-workflow-automation) |
| Common attributes and methods; coef_, intercept_, score | 8 | [Common Attributes and Methods](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#common-attributes-and-methods) |
| Hyperparameter tuning with search methods; get_params/set_params | 10 | [Hyperparameter Tuning with Search Methods](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#hyperparameter-tuning-with-search-methods) |
| Working with metadata: Tags and more; metadata routing | 11 | [Working with Metadata: Tags and Routing](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#working-with-metadata-tags-and-routing) |
| Best practices for API usage | 11 | [Best Practices for API Usage](../notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb#best-practices-for-api-usage) |

## Chapter 2: Pre-Model Workflow and Data Preprocessing

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| The impact of raw data on model performance | 14 | [Handling Missing Data](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#handling-missing-data) |
| Common data issues; cleaning and preparing data | 14 | [Handling Missing Data](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#handling-missing-data) |
| Handling missing data; SimpleImputer | 16 | [Handling Missing Data](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#handling-missing-data) |
| KNNImputer | 18 | [KNNImputer](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#knnimputer) |
| IterativeImputer | 19 | [IterativeImputer](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#iterativeimputer) |
| Scaling techniques: StandardScaler, MinMaxScaler, Normalizer | 21 | [Scaling Techniques](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#scaling-techniques) |
| Encoding categorical variables; OneHotEncoder, LabelEncoder, ColumnTransformer | 25 | [Encoding Categorical Variables](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#encoding-categorical-variables) |
| Introduction to pipelines; what is a pipeline? | 32 | [Introduction to Pipelines](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#introduction-to-pipelines) |
| Visualizing pipelines | 35 | [Visualizing Pipelines](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#visualizing-pipelines) |
| Feature engineering; PolynomialFeatures, KBinsDiscretizer | 36 | [Feature Engineering](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#feature-engineering) |
| RFE and SelectFromModel | 40 | [Feature Engineering](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#feature-engineering) |
| Practical exercises on data preprocessing | 42 | [Practical Exercise on Data Preprocessing](../notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb#practical-exercise-on-data-preprocessing) |

## Chapter 3: Dimensionality Reduction Techniques

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Introduction to dimensionality reduction | 46 | [Principal Component Analysis (PCA)](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#principal-component-analysis-pca) |
| Why dimensionality reduction is essential | 46 | [Principal Component Analysis (PCA)](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#principal-component-analysis-pca) |
| Theoretical foundations of dimensionality reduction | 47 | [Principal Component Analysis (PCA)](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#principal-component-analysis-pca) |
| Transforming datasets with PCA | 48 | [Principal Component Analysis (PCA)](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#principal-component-analysis-pca) |
| Maximizing class separability with LDA | 55 | [Linear Discriminant Analysis (LDA)](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#linear-discriminant-analysis-lda) |
| Differences between PCA and LDA | 58 | [Linear Discriminant Analysis (LDA)](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#linear-discriminant-analysis-lda) |
| t-SNE and data visualization | 60 | [t-SNE for Data Visualization](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#t-sne-for-data-visualization) |
| Guidelines for selecting dimensionality reduction techniques | 64 | [Practical Exercises on Dimensionality Reduction](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#practical-exercises-on-dimensionality-reduction) |
| Practical steps for selection; impact on model performance; trade-offs | 66 | [Practical Exercises on Dimensionality Reduction](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#practical-exercises-on-dimensionality-reduction) |
| Example 1: PCA with logistic regression | 67 | [Practical Exercises on Dimensionality Reduction](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#practical-exercises-on-dimensionality-reduction) |
| Example 2: t-SNE for visualization | 67 | [Practical Exercises on Dimensionality Reduction](../notebooks/chapter_03_dimensionality_reduction_techniques.ipynb#practical-exercises-on-dimensionality-reduction) |

## Chapter 4: Building Models with Distance Metrics and Nearest Neighbors

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Introduction to distance metrics | 70 | [Distance Metrics Overview](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#distance-metrics-overview) |
| Understanding KNNs | 71 | [Understanding k-nearest neighbors (KNN)](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#understanding-k-nearest-neighbors-knn) |
| Distance metrics overview; Euclidean, Manhattan, Minkowski | 75 | [Distance Metrics Overview](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#distance-metrics-overview) |
| Hyperparameter tuning in KNN | 81 | [Hyperparameter Tuning in KNN](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#hyperparameter-tuning-in-knn) |
| Evaluating KNN performance | 83 | [Evaluating KNN Performance](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#evaluating-knn-performance) |
| Understanding evaluation metrics | 88 | [Evaluating KNN Performance](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#evaluating-knn-performance) |
| Exercise 1: Building a KNN classifier | 90 | [Practical Exercises with KNN Models](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#practical-exercises-with-knn-models) |
| Exercise 2: Tuning hyperparameters with grid search | 90 | [Practical Exercises with KNN Models](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#practical-exercises-with-knn-models) |
| Exercise 3: Evaluating a KNN classifier | 90 | [Practical Exercises with KNN Models](../notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb#practical-exercises-with-knn-models) |

## Chapter 5: Linear Models and Regularization

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Introduction to linear models | 94 | [Introduction to Linear Models](../notebooks/chapter_05_linear_models_and_regularization.ipynb#introduction-to-linear-models) |
| Ridge and Lasso regression | 99 | [Ridge and Lasso Regression](../notebooks/chapter_05_linear_models_and_regularization.ipynb#ridge-and-lasso-regression) |
| ElasticNet and regularization | 105 | [ElasticNet and Regularization](../notebooks/chapter_05_linear_models_and_regularization.ipynb#elasticnet-and-regularization) |
| Regularization theory and practice | 110 | [ElasticNet and Regularization](../notebooks/chapter_05_linear_models_and_regularization.ipynb#elasticnet-and-regularization) |
| Regression and regularization; polynomial regression | 112 | [Polynomial Regression](../notebooks/chapter_05_linear_models_and_regularization.ipynb#polynomial-regression) |
| Regression and regularization; spline regression | 117 | [Spline Regression](../notebooks/chapter_05_linear_models_and_regularization.ipynb#spline-regression) |
| Exercise 1: Implementing ridge regression | 120 | [Practical Exercises with Linear Models and Regularization](../notebooks/chapter_05_linear_models_and_regularization.ipynb#practical-exercises-with-linear-models-and-regularization) |
| Exercise 2: Implementing Lasso regression | 121 | [Practical Exercises with Linear Models and Regularization](../notebooks/chapter_05_linear_models_and_regularization.ipynb#practical-exercises-with-linear-models-and-regularization) |
| Exercise 3: Implementing ElasticNet regression | 121 | [Practical Exercises with Linear Models and Regularization](../notebooks/chapter_05_linear_models_and_regularization.ipynb#practical-exercises-with-linear-models-and-regularization) |

## Chapter 6: Advanced Logistic Regression and Extensions

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Overview of logistic regression | 124 | [Overview of Logistic Regression](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#overview-of-logistic-regression) |
| Multiclass classification techniques | 129 | [Multiclass Classification Techniques](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#multiclass-classification-techniques) |
| Regularization in logistic regression | 136 | [Regularization in Logistic Regression](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#regularization-in-logistic-regression) |
| Multilabel classification concepts | 143 | [Multilabel Classification Concepts](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#multilabel-classification-concepts) |
| Model evaluation metrics | 150 | [Model Evaluation Metrics](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#model-evaluation-metrics) |
| Exercise 1: Building a regularized logistic regression model | 155 | [Practical Exercises with Advanced Logistic Regression](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#practical-exercises-with-advanced-logistic-regression) |
| Exercise 2: Evaluating multiclass logistic regression | 155 | [Practical Exercises with Advanced Logistic Regression](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#practical-exercises-with-advanced-logistic-regression) |
| Exercise 3: Visualizing logistic regression results | 155 | [Practical Exercises with Advanced Logistic Regression](../notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb#practical-exercises-with-advanced-logistic-regression) |

## Chapter 7: Support Vector Machines and Kernel Methods

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Introduction to SVMs; margin, support vectors, SVR | 158 | [Introduction to SVMs](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#introduction-to-svms) |
| Kernel functions and their applications | 164 | [Kernel Functions and Their Applications](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#kernel-functions-and-their-applications) |
| Tuning SVM parameters | 171 | [Tuning SVM Parameters](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#tuning-svm-parameters) |
| SVMs in high-dimensional spaces | 176 | [SVMs in High-Dimensional Spaces](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#svms-in-high-dimensional-spaces) |
| Evaluating SVM models | 180 | [Evaluating SVM Models](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#evaluating-svm-models) |
| Exercise 1: Building a simple SVM classifier | 185 | [Practical Exercises with SVMs](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#practical-exercises-with-svms) |
| Exercise 2: Tuning SVM parameters with grid search | 186 | [Practical Exercises with SVMs](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#practical-exercises-with-svms) |
| Exercise 3: Visualizing SVM decision boundaries | 186 | [Practical Exercises with SVMs](../notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb#practical-exercises-with-svms) |

## Chapter 8: Tree-Based Algorithms and Ensemble Methods

| Materi buku | Halaman cetak | Pembahasan notebook |
| --- | --- | --- |
| Introduction to decision trees | 188 | [Introduction to Decision Trees](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#introduction-to-decision-trees) |
| Random forests and bagging | 193 | [Random Forests and Bagging](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#random-forests-and-bagging) |
| Gradient boosting machines | 198 | [Gradient Boosted Machines](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#gradient-boosted-machines) |
| Hyperparameter tuning for trees and ensembles | 202 | [Hyperparameter Tuning for Trees and Ensembles](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#hyperparameter-tuning-for-trees-and-ensembles) |
| Comparing ensemble methods | 207 | [Comparing Ensemble Methods](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#comparing-ensemble-methods) |
| Exercise 1: Building and evaluating a decision tree classifier | 211 | [Practical Exercises with Tree-Based Models](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#practical-exercises-with-tree-based-models) |
| Exercise 2: Hyperparameter tuning with random forests | 211 | [Practical Exercises with Tree-Based Models](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#practical-exercises-with-tree-based-models) |
| Exercise 3: Comparing gradient boosting and random forest | 212 | [Practical Exercises with Tree-Based Models](../notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb#practical-exercises-with-tree-based-models) |

## Asal Kode

Chapter 1 mereproduksi contoh pada buku halaman 1–12 karena repo penerbit tidak menyediakan notebook bab tersebut. Chapter 2–8 mengadaptasi seluruh sel kode utama dan exercise solutions dari repo penerbit. Pemetaan tiap sel terdapat pada [CODE_SOURCES.json](CODE_SOURCES.json); metadata sel menyimpan source_path dan source_cell_index. Bagian konseptual tanpa contoh kode tetap dijelaskan.

Lingkup pengumpulan dengan deadline yang dinyatakan pada dokumen tugas adalah Chapter 1–5 dan Chapter 6–8. Buku mempunyai Chapter 9–13; bab tersebut belum termasuk notebook pada repo ini.
