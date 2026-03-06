import streamlit as st
import pandas as pd
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split

# CONFIGURACIÓN DE LA PÁGINA:
st.set_page_config(
    page_title="Predictor de Diabetes Tipo II",
    page_icon="🩺",
    layout="centered"
)

# Personalozación de la app:
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main { background-color: #f8fafc; }

    .header-container {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a9f 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }

    .header-container h1 {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .header-container p {
        font-size: 1rem;
        opacity: 0.85;
        margin-top: 0.5rem;
    }

    .section-title {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #64748b;
        margin-bottom: 1rem;
        margin-top: 1.5rem;
    }

    .result-box-high {
        background: linear-gradient(135deg, #fff1f2, #ffe4e6);
        border: 2px solid #fda4af;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1.5rem;
    }

    .result-box-low {
        background: linear-gradient(135deg, #f0fdf4, #dcfce7);
        border: 2px solid #86efac;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1.5rem;
    }

    .result-emoji { font-size: 3rem; margin-bottom: 0.5rem; }

    .result-title-high {
        font-size: 1.5rem;
        font-weight: 700;
        color: #be123c;
        margin-bottom: 0.5rem;
    }

    .result-title-low {
        font-size: 1.5rem;
        font-weight: 700;
        color: #15803d;
        margin-bottom: 0.5rem;
    }

    .result-subtitle {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.6;
    }

    .prob-bar-container {
        margin-top: 1.5rem;
        background: #e2e8f0;
        border-radius: 999px;
        height: 12px;
        overflow: hidden;
    }

    .disclaimer {
        background: #f1f5f9;
        border-left: 4px solid #94a3b8;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.2rem;
        margin-top: 2rem;
        font-size: 0.85rem;
        color: #64748b;
        line-height: 1.6;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        background: linear-gradient(135deg, #1e3a5f, #2d6a9f);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem;
        font-size: 1rem;
        font-weight: 600;
        margin-top: 1.5rem;
        transition: opacity 0.2s;
    }

    div[data-testid="stButton"] > button:hover {
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)


# Cargando mi modelo de Ml de diabtes:
@st.cache_resource
def load_model():
    df = pd.read_csv("diabetes_prediction_dataset.csv")

    df["smoking_history"] = df["smoking_history"].replace({
        "current": 1, "never": 0, "No Info": 0,
        "ever": 1, "formerly": 1, "not current": 0, "former": 0
    }).astype(int)
    df["age"] = df["age"].astype(int)

    X = df[["age", "bmi", "hypertension", "heart_disease",
            "smoking_history", "blood_glucose_level", "HbA1c_level"]]
    y = df["diabetes"]

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.15, random_state=42)

    model = BalancedRandomForestClassifier(random_state=42, n_estimators=300)
    model.fit(X_train, y_train)
    return model


# Parte superior de la app:
st.markdown("""
<div class="header-container">
    <h1>🩺 Predictor de Diabetes Tipo II</h1>
    <p>Ingresa tus datos clínicos para evaluar tu riesgo</p>
</div>
""", unsafe_allow_html=True)

# Casillas del Formulario:
st.markdown('<p class="section-title">Datos personales</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Edad", min_value=1, max_value=100, value=30, step=1)
with col2:
    bmi = st.number_input("IMC (Índice de Masa Corporal)", min_value=10.0, max_value=100.0, value=25.0, step=0.1)

st.markdown('<p class="section-title">Historial médico</p>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    hypertension = st.selectbox("¿Tienes hipertensión?", options=["No", "Sí"])
with col4:
    heart_disease = st.selectbox("¿Tienes enfermedad cardíaca?", options=["No", "Sí"])

smoking = st.selectbox("Historial de tabaquismo", options=["No fumador", "Fumador / Ex-fumador"])

st.markdown('<p class="section-title">Resultados de laboratorio</p>', unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    glucose = st.number_input("Glucosa en sangre (mg/dL)", min_value=50, max_value=400, value=100, step=1)
with col6:
    hba1c = st.number_input("Nivel de HbA1c (%)", min_value=3.0, max_value=15.0, value=5.5, step=0.1)

# Evaluacion de la Predicción:
if st.button("Evaluar riesgo"):
    with st.spinner("Analizando..."):
        model = load_model()

        input_data = pd.DataFrame({
            "age": [age],
            "bmi": [bmi],
            "hypertension": [1 if hypertension == "Sí" else 0],
            "heart_disease": [1 if heart_disease == "Sí" else 0],
            "smoking_history": [1 if smoking == "Fumador / Ex-fumador" else 0],
            "blood_glucose_level": [glucose],
            "HbA1c_level": [hba1c]
        })

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        prob_diabetes = probabilities[1] * 100

        if prediction == 1:
            st.markdown(f"""
            <div class="result-box-high">
                <div class="result-emoji">⚠️</div>
                <div class="result-title-high">Riesgo elevado de Diabetes Tipo II</div>
                <div class="result-subtitle">
                    Los datos ingresados indican que esta persona se encuentra dentro
                    de la población con <strong>riesgo elevado</strong> de desarrollar Diabetes Tipo II.<br><br>
                    Probabilidad estimada: <strong>{prob_diabetes:.1f}%</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-box-low">
                <div class="result-emoji">✅</div>
                <div class="result-title-low">Riesgo bajo de Diabetes Tipo II</div>
                <div class="result-subtitle">
                    Los datos ingresados indican que esta persona se encuentra dentro
                    de la población con <strong>bajo riesgo</strong> de desarrollar Diabetes Tipo II.<br><br>
                    Probabilidad estimada: <strong>{prob_diabetes:.1f}%</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.progress(int(prob_diabetes))

# Un disclaimer (recomendacion medica):
st.markdown("""
<div class="disclaimer">
    ⚕️ <strong>Aviso médico:</strong> Esta herramienta es de carácter informativo y educativo.
    No reemplaza el diagnóstico de un profesional de la salud. Si tienes dudas sobre tu salud,
    consulta a tu médico.
</div>
""", unsafe_allow_html=True)
