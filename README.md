# 🩺 Predictor de Riesgo de Diabetes Tipo II

Modelo de Machine Learning que predice el riesgo de padecer Diabetes Tipo II a partir de factores clínicos y de estilo de vida.

## 📊 Dataset

- **Fuente:** [Kaggle - Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data/code)
- **Tamaño:** 100,000 pacientes
- **Variables:** edad, IMC, hipertensión, enfermedad cardíaca, historial de tabaquismo, glucosa en sangre, nivel de HbA1c

## 🤖 Modelo

Se utilizó **BalancedRandomForestClassifier** para manejar el desbalance de clases (ratio ~10:1 entre no diabéticos y diabéticos).

### Resultados

| Métrica   | Valor |
|-----------|-------|
| Recall    | 88%   |
| Precisión | 52%   |
| F1-Score  | 65%   |

> El recall es la métrica más importante en diagnósticos médicos: minimiza los falsos negativos (casos de diabetes no detectados).

## 🚀 Cómo ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/diabetes-predictor.git
cd diabetes-predictor
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Abrir el notebook
```bash
jupyter notebook diabetes.ipynb
```

## 📁 Estructura del proyecto

```
diabetes-predictor/
│
├── diabetes.ipynb          # Notebook principal con el modelo
├── diabetes_prediction_dataset.csv   # Dataset
├── requirements.txt        # Dependencias
└── README.md               # Este archivo
```

## 🛠️ Tecnologías

- Python
- Pandas
- Scikit-learn
- Imbalanced-learn
- Matplotlib / Seaborn
