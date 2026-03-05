# 🩺 Predictor de Riesgo de Diabetes Tipo II

Modelo de Machine Learning que busca predecir la probabilidad que un individuo evaluado pueda encontrarse dentro de la población de riesgo de padecer Diabetes Tipo II, a partir de factores clínicos y de estilo de vida del evaluado.

Este modelo nace con el objetivo de desarrollar herramientas que faciliten la elaboración de diagnósticos preventivos contra el desarrollo de la diabetes tipo II, enfermedad que en los últimos años ha ido en aumento. Lo cual representa un problema alarmante para la salud pública, debido a que la diabetes está relacionada con otras enfermedades o complicaciones médicas como: la ceguera, enfermedades cardiovasculares, derrames cerebrales, enfermedades del riñón y amputación de miembros inferiores (OMS, 2024). Estas complicaciones, a largo plazo, perjudican los sistemas de salud al aumentar el gasto de los recursos médicos y saturar las instituciones médicas en la atención de condiciones derivadas de la diabetes. Es importante remarcar que, en el año 2021, según la Organización Mundial de la Salud, más de un millón de muertes en el mundo estuvieron relacionadas con la diabetes, cifra que en los últimos años continúa en aumento (OMS, 2024).

Si bien este modelo busca ser de fácil acceso para quien lo requiera y, de esa manera, contribuir con la prevención del desarrollo de la diabetes, como se mencionó anteriormente, es importante dar a conocer las debilidades o dificultades que presenta este modelo:

  1) De las variables independientes, hay valores que solo se pueden obtener a través de exámenes de sangre.
  2) El modelo se entrenó con variables que tienen una alta correlación con el diagnóstico de diabetes tipo 2 (como la edad, el IMC, niveles de glucosa en sangre, etc.), pero no tiene en cuenta otros factores fundamentales como: tiempo de actividad física diaria, ingresos mensuales del paciente, cantidad de carbohidratos que consume, etc. Factores que, si se tienen presentes, pueden ser fundamentales para facilitar, de mejor manera, el desarrollo de diagnósticos preventivos contra la diabetes tipo 2.

Referencia Bibliográfica:

WHO (14/11/2024). Diabetes. https://www.who.int/news-room/fact-sheets/detail/diabetes

## 📊 Dataset:

- **Fuente:** [Kaggle - Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data/code)
- **Tamaño:** 100,000 pacientes
- **Variables:** edad, IMC, hipertensión, enfermedad cardíaca, historial de tabaquismo, glucosa en sangre, nivel de HbA1c

## 🤖 Modelo:

Se utilizó **BalancedRandomForestClassifier** para manejar el desbalance de clases (ratio ~10:1 entre no diabéticos y diabéticos).

### Resultados:

| Métrica   | Valor |
|-----------|-------|
| Recall    | 78%   |
| Precisión | 74%   |
| F1-Score  | 75%   |

Se busco dar prioridad al **recall**, por ello el uso de BalancedRandomForestClassifier, debido a que es una de las metricas mas importante a la hora de la realizacion de diagnósticos médicos preventivos. Con ello minimizando la aparicion de falsos negativos (casos de diabetes no detectados).

Con un **racall** ndel 78%

## 🚀 Cómo ejecutar:

### 1. Clonar el repositorio:
```bash
git clone https://github.com/TU_USUARIO/diabetes-predictor.git
cd diabetes-predictor
```

### 2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 3. Abrir el notebook:
```bash
jupyter notebook diabetes.ipynb
```

## 📁 Estructura del proyecto:

```
diabetes-predictor/
│
├── diabetes.ipynb          # Notebook principal con el modelo
├── diabetes_prediction_dataset.csv   # Dataset
├── requirements.txt        # Dependencias
└── README.md               # Este archivo
```

## 🛠️ Tecnologías Implementadas:

- Python
- Pandas
- Scikit-learn
- Imbalanced-learn
- Matplotlib / Seaborn
