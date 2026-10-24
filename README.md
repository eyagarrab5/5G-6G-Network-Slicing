# 5G/6G Network Slicing Optimization with Machine Learning

## Overview

Network slicing is a key technology in 5G and beyond-5G networks that enables multiple virtual networks to operate on shared physical infrastructure. Each slice is designed to meet different Quality of Service (QoS) requirements depending on the application.

This project explores the use of Machine Learning to classify network traffic for 5G/6G network slicing. The objective is to evaluate different classification algorithms and identify an effective approach for distinguishing traffic associated with different service types, including:

- **eMBB (Enhanced Mobile Broadband):** High-bandwidth applications such as video streaming.
- **mMTC (Massive Machine-Type Communications):** Large-scale IoT deployments involving numerous connected devices.
- **URLLC (Ultra-Reliable Low-Latency Communications):** Applications requiring very low latency and high reliability.

The project was carried out as an academic team project at ESPRIT by a team of six members.

## Objectives

- Explore Machine Learning approaches for 5G/6G network traffic classification.
- Compare multiple classification algorithms under a consistent evaluation framework.
- Improve model performance through feature engineering and data preprocessing.
- Investigate anomaly detection as part of the data analysis pipeline.
- Evaluate model generalization using stratified five-fold cross-validation.
- Analyze classification performance using standard evaluation metrics.

## Dataset

The project used two datasets:

| Network generation | Number of samples |
|---|---:|
| 5G | 8,958 |
| 6G | 10,000 |

The datasets were used to investigate network traffic classification across the relevant network slicing service categories.

*Note: Add the original dataset sources, feature descriptions, and target-label definitions here if they are available and permitted to be shared.*

## Methodology

### 1. Data Preparation and Feature Engineering

The data preparation workflow focused on preparing the datasets for model training and evaluation. Feature engineering was used to improve the information available to the classification models.

### 2. Model Development and Comparison

Four Machine Learning algorithms were developed and compared:

- **XGBoost**
- **Random Forest**
- **Logistic Regression**
- **Multi-Layer Perceptron (MLP)**

Comparing these models helped assess their ability to distinguish network traffic classes and identify a strong-performing approach.

### 3. Anomaly Detection

Anomaly detection techniques were incorporated into the workflow to investigate unusual data patterns and support model development.

### 4. Model Validation

Stratified five-fold cross-validation was used to evaluate model performance across multiple data splits while preserving class proportions in each fold.

### 5. Performance Evaluation

The models were evaluated using classification metrics, including:

- Accuracy
- F1-score

Additional metrics and confusion matrices can be included if available in the original experiments.

## Results

The best reported result on the 6G dataset was achieved by **XGBoost**.

| Metric | Result |
|---|---:|
| Accuracy | 97.5% |
| F1-score | 0.978 |
| Validation strategy | Stratified 5-fold cross-validation |

These results indicate strong classification performance on the evaluated 6G dataset. They should be interpreted in the context of the dataset, class distribution, preprocessing workflow, and validation setup.

## Technologies

- **Language:** Python
- **Machine Learning:** XGBoost, Random Forest, Logistic Regression, MLP
- **Data Processing:** Feature engineering and data preprocessing
- **Model Evaluation:** Stratified cross-validation, accuracy, F1-score
- **Additional techniques:** Anomaly detection

*Add the exact libraries used in your implementation, such as pandas, NumPy or scikit-learn, only if they were part of the project.*

## Key Takeaways

This project provided practical experience in:

- Comparing Machine Learning algorithms for telecommunications applications.
- Preparing datasets and engineering relevant features.
- Evaluating classification models using cross-validation.
- Investigating anomaly detection in network-related data.
- Applying data-driven approaches to 5G/6G network slicing challenges.
- Collaborating on a technical project within a six-member team.

## Project Information

- **Institution:** ESPRIT, Tunisia
- **Project type:** Academic team project
- **Team size:** 6 members
- **Project area:** Machine Learning, Telecommunications, 5G/6G Networks
- **Primary task:** Network traffic classification for network slicing

## Future Improvements

Potential directions for further development include:

- Evaluating class-specific precision, recall and F1-scores.
- Analyzing confusion matrices to identify frequently misclassified service types.
- Investigating model robustness under different traffic distributions.
- Exploring lightweight models for resource-constrained network environments.
- Studying how classification outputs could support dynamic network slice allocation and QoS optimization.

---

**Disclaimer:** This project evaluates Machine Learning models for network traffic classification. High classification performance alone does not demonstrate that live network resources were dynamically allocated or that end-to-end network slicing was optimized in a deployed 5G/6G environment.
