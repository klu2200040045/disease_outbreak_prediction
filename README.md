# disease_outbreak_prediction
# Improving Diabetes Prediction Model Accuracy

## Overview
This project aims to predict diabetes using the **Pima Indians Diabetes Dataset**. Initially, an **SVM (Support Vector Machine)** model was used, achieving an accuracy of **75%**. To improve performance, **undersampling, Tomek Links, SMOTE, and SMOTETomek** techniques were applied, achieving up to **81% accuracy**.

## Dataset
The dataset contains features like glucose level, BMI, age, insulin levels, and others, with the target variable being **Outcome (0: No Diabetes, 1: Diabetes)**. The dataset was imbalanced, with **more 0s than 1s**, which required resampling techniques.

## Model Selection
### Why SVM?
SVM is effective for high-dimensional datasets and works well when data is **linearly separable**. Initially, a **linear kernel** was used, but further resampling techniques improved results.

## Techniques Used for Accuracy Improvement
### 1. Undersampling (77% Accuracy)
- The majority class (0) was **randomly reduced** to match the minority class (1).
- While this balanced the dataset, it led to **loss of valuable majority class data**.

### 2. Tomek Links (79% Accuracy)
- **Tomek Links** is an undersampling technique that removes **overlapping majority class samples** close to the decision boundary.
- This helped in **better class separation**, leading to a slight accuracy boost.

### 3. SMOTE (74% Accuracy)
- **SMOTE (Synthetic Minority Over-sampling Technique)** generates **synthetic** minority class samples instead of duplicating existing ones.
- This technique increased dataset size but introduced **some noise**, slightly reducing accuracy.

### 4. SMOTETomek (81% Accuracy)
- **Combines SMOTE and Tomek Links**: SMOTE **adds synthetic minority samples**, while Tomek **removes overlapping majority samples**.
- This resulted in **better decision boundary learning**, achieving the **highest accuracy (81%)**.

## Results Summary
| Technique      | Accuracy |
|--------------|----------|
| Original SVM | 75%      |
| Undersampling | 77%      |
| Tomek Links  | 79%      |
| SMOTE        | 74%      |
| SMOTETomek   | 82%      |

## Next Steps
- Try **Decision Tree, Random Forest, or XGBoost** for further improvement.
- Perform **feature selection** to remove less important attributes.
- Experiment with **hyperparameter tuning** to optimize model performance.

## Conclusion
By applying **different data resampling techniques**, we significantly improved model accuracy from **75% to 81%**. **SMOTETomek** proved to be the most effective, as it balanced the dataset while preserving meaningful patterns.


