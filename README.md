# Type II Diabetes Risk Predictor

A Machine Learning model designed to predict the likelihood that an evaluated individual may fall within the at-risk population for developing Type II Diabetes, based on the individual's clinical and lifestyle factors.

This model was developed with the goal of creating tools that facilitate the elaboration of preventive diagnoses against the development of Type II diabetes, a disease that has been on the rise in recent years. This represents an alarming public health concern, as diabetes is associated with other diseases and medical complications such as: blindness, cardiovascular disease, stroke, kidney disease, and lower limb amputation (WHO, 2024). In the long term, these complications strain healthcare systems by increasing the consumption of medical resources and overwhelming medical institutions with the management of diabetes-related conditions (GBD, 2025). It is important to highlight that, in 2021, according to the World Health Organization, more than one million deaths worldwide were linked to diabetes — a figure that has continued to rise in recent years (WHO, 2024).

While this model aims to be easily accessible to anyone who needs it and, in doing so, contribute to the prevention of diabetes development, it is important to acknowledge the limitations and challenges this model presents:

1). Among the independent variables, some values can only be obtained through blood tests.

2). The model was trained on variables that have a high correlation with a Type 2 diabetes diagnosis (such as age, BMI, blood glucose levels, etc.), but does not account for other fundamental factors such as: daily physical
- activity time, the patient's monthly income, carbohydrate intake, etc. — factors that, if considered, could be instrumental in better facilitating the development of preventive diagnoses against Type 2 diabetes.

Referencia Bibliográfica:

WHO, (14/11/2024), Diabetes. https://www.who.int/news-room/fact-sheets/detail/diabetes
GBD 2021 Diabetes Collaborators, (15/07/2025), Global, regional, and national burden of diabetes from 1990 to 2021, with projections of prevalence to 2050: a systematic analysis for the Global Burden of Disease Study 2021. https://pubmed.ncbi.nlm.nih.gov/37356446/


## Dataset:

- **Source:** [Kaggle - Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data/code)
- **Size:** 100,000 pacientes
- **Variables:** age, BMI, hypertension, heart disease, smoking history, blood glucose, HbA1c level

## Model:

**BalancedRandomForestClassifier** was used to handle class imbalance (a ~10:1 ratio between non-diabetic and diabetic cases).

### Results:

| Metric    | Value |
|-----------|-------|
| Recall    | 79%   |
| Precisión | 69%   |
| F1-Score  | 74%   |

Priority was given to **recall**, due to the importance of this metric when performing preventive medical diagnoses, as the goal is to minimize the occurrence of false negatives (undetected diabetes cases). While still maintaining a high F1-Score (74%), ensuring that the majority of those diagnosed with diabetes are true positives (Precision of 69%).


## how tu run: 

### 1. Clone the repository:
```bash
git clone https://github.com/quirozromero8-cmyk/diabetes-predictor.git
cd diabetes-predictor
```

### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. Open the notebook:
```bash
jupyter notebook diabetes.ipynb
```

## Project Structure:

```
diabetes-predictor/
│
├── diabetes.ipynb          
├── diabetes_prediction_dataset.csv   
├── requirements.txt        
└── README.md               
```

## Technologies Used:

- Python
- Pandas
- Scikit-learn
- Imbalanced-learn
- Matplotlib / Seaborn
