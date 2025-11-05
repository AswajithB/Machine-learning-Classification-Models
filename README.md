# 🏦 Loan Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/ML-Classification-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📘 Overview
This project predicts whether a loan application will be approved or not using machine learning techniques.  
The dataset includes applicant demographic and financial details.  
To address class imbalance, **SMOTE (Synthetic Minority Oversampling Technique)** was applied to ensure balanced class distribution.

---

## 📊 Dataset
The dataset contains details of applicants and their loan application status.

| Column | Description |
|---------|--------------|
| Gender | Applicant's gender |
| Married | Marital status |
| Dependents | Number of dependents |
| Education | Education level |
| Self_Employed | Employment type |
| ApplicantIncome | Monthly income of applicant |
| CoapplicantIncome | Monthly income of co-applicant |
| LoanAmount | Loan amount requested |
| Loan_Amount_Term | Term of the loan (in months) |
| Credit_History | Credit history meets guidelines or not |
| Property_Area | Type of area (Urban/Semiurban/Rural) |
| Loan_Status | Target variable (Y = Approved, N = Not Approved) |

## 📂 Dataset
Dataset used: [loan.csv](loan_prediction/loan.csv)


---

## ⚙️ Technologies Used
- Python 🐍  
- Pandas, NumPy – Data processing  
- Matplotlib, Seaborn – Visualization  
- Scikit-Learn – Modeling & evaluation  
- Imbalanced-learn (SMOTE) – Data balancing  
- Flask – Web app deployment  

---

## 🧠 Model Building
The following classification models were trained and evaluated:

| Model | Purpose |
|--------|----------|
| Logistic Regression | Final selected model |
| Random Forest Classifier | Ensemble baseline |
| Support Vector Machine (SVM) | Margin-based classifier |
| Decision Tree Classifier | Interpretability check |
| K-Nearest Neighbors (KNN) | Distance-based classifier |
| Naive Bayes | Probabilistic model |
| Gradient Boosting | Boosted ensemble |
| AdaBoost | Adaptive boosting method |

**Data Preprocessing Steps**
1. Handled missing values  
2. Label-encoded categorical features  
3. Standardized numerical columns  
4. Applied **SMOTE** to balance classes  
5. Performed model training and comparison  

---

## 📈 Results
After evaluating all models, **Logistic Regression** was chosen as the final model due to its strong and stable performance after applying SMOTE.



## 🖥️ User Interface Preview
<img src="loan_prediction/static/images/loan_ui.png" width="700">

---

---

## 🍷 **Wine Type Classification using Machine Learning**


```markdown
# 🍷 Wine Type Classification using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/ML-Classification-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📘 Overview
This project predicts the **type of wine** (Red or White) based on physicochemical properties such as acidity, pH, alcohol content, and more.  
To handle class imbalance, **SMOTE (Synthetic Minority Oversampling Technique)** was applied.  
After testing multiple models, **Logistic Regression** was chosen as the final model using **cross-validation** for robust evaluation.

---

## 📊 Dataset
The dataset includes chemical properties of wine samples.

| Column | Description |
|---------|--------------|
| Fixed Acidity | Non-volatile acids in wine |
| Volatile Acidity | Acetic acid concentration |
| Citric Acid | Citric acid level |
| Residual Sugar | Sugar remaining after fermentation |
| Chlorides | Salt content |
| Free Sulfur Dioxide | SO₂ in free form |
| Total Sulfur Dioxide | Total SO₂ |
| Density | Density of wine |
| pH | Acidity level |
| Sulphates | Sulphate concentration |
| Alcohol | Alcohol content (%) |
| Type | Target (Red / White) |

## 📂 Dataset
Dataset used: [wine-quality-white-and-red.csv](wine_type/wine-quality-white-and-red.csv)

---

## ⚙️ Technologies Used
- Python 🐍  
- Pandas, NumPy – Data cleaning  
- Matplotlib, Seaborn – Visualization  
- Scikit-Learn – Modeling & evaluation  
- Imbalanced-learn (SMOTE) – Data balancing  
- Flask – Deployment  

---

## 🧠 Model Building
Models used for evaluation:
- Logistic Regression ✅ *(Final Model after Cross-Validation)*  
- Random Forest Classifier  
- Support Vector Machine (SVM)

**Data Pipeline**
1. Feature normalization  
2. Label encoding for categorical features  
3. Applied **SMOTE** for class balancing  
4. Trained models and validated using **k-fold cross-validation**  

---

## 📈 Results
After evaluating all models, **Logistic Regression** was chosen as the final model after Cross-Validation

## 🖥️ App Interface
<img src="wine_type/static/images/wine_ui.png" width="700">
<img src="wine_type/static/images/wine_ui_result.png" width="700">

---


