import streamlit as st
import joblib

# Load the trained model
loaded_model = joblib.load('Heart_disease_model_FF.pkl')

# Mapping dictionaries
sex_mapping = {"Male": 1, "Female": 0}
chest_pain_mapping = {
    "Asymptomatic": 0,
    "Non-Anginal Pain": 1,
    "Atypical Angina": 2,
    "Typical Angina": 3,
}
resting_ecg_mapping = {
    "Normal": 0,
    "ST-T Abnormality": 1,
    "Left Ventricular Hypertrophy": 2,
}
exercise_angina_mapping = {"No": 0, "Yes": 1}
st_slope_mapping = {"Flat": 0, "Up": 1, "Down": 2}

# Page settings
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        }
        h1, h3 {
            text-align: center;
        }
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown(
    """
    <div class="main">
        <h1>💓 Heart Disease Prediction</h1>
        <h3>By AIvolution Team</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Prediction Form
with st.form("prediction_form"):
    st.markdown("### 📝 Enter Your Health Data:")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=0, max_value=120, value=30)
        sex = st.selectbox("🧑 Sex", list(sex_mapping.keys()))
        chest_pain = st.selectbox("❤️ Chest Pain Type", list(chest_pain_mapping.keys()))
        resting_bp = st.number_input("💉 Resting Blood Pressure (mm Hg)", min_value=0, value=120)
        cholesterol = st.number_input("🧪 Cholesterol (mg/dl)", min_value=0, value=200)
        fasting_bs = st.selectbox("🍬 Fasting Blood Sugar > 120 mg/dl?", ["0", "1"])

    with col2:
        resting_ecg = st.selectbox("🩺 Resting ECG", list(resting_ecg_mapping.keys()))
        max_hr = st.number_input("🏃 Max Heart Rate Achieved", min_value=0, value=150)
        exercise_angina = st.selectbox("🚴 Exercise Induced Angina", list(exercise_angina_mapping.keys()))
        oldpeak = st.number_input("📉 Oldpeak (ST Depression)", min_value=0.0, value=1.0, step=0.1)
        st_slope = st.selectbox("📈 ST Slope", list(st_slope_mapping.keys()))

    submit_button = st.form_submit_button("💡 Predict")

# Prediction Output
if submit_button:
    input_data = [
        age,
        sex_mapping[sex],
        chest_pain_mapping[chest_pain],
        resting_bp,
        cholesterol,
        int(fasting_bs),
        resting_ecg_mapping[resting_ecg],
        max_hr,
        exercise_angina_mapping[exercise_angina],
        oldpeak,
        st_slope_mapping[st_slope],
    ]

    prediction = loaded_model.predict([input_data])[0]

    st.markdown("---")
    st.markdown("### 🧾 Prediction Result:")
    if prediction == 0:
        st.success("✅ Great news! You are **not diagnosed** with heart disease.")
    else:
        st.error("⚠️ Unfortunately, there's an **85% chance** you may have heart disease.\n\nPlease consult a doctor as soon as possible.")

