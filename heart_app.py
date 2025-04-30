import streamlit as st
import joblib


loaded_model = joblib.load('Heart_disease_model_FF.pkl')


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

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center;'>💓 Heart Disease Prediction</h1>
    <h3 style='text-align: center;'>By AIvolution Team</h3>
    """,
    unsafe_allow_html=True
)


with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        sex = st.selectbox("Sex", list(sex_mapping.keys()))
        chest_pain = st.selectbox("Chest Pain Type", list(chest_pain_mapping.keys()))
        resting_bp = st.number_input("Resting Blood Pressure", min_value=0, value=120)
        cholesterol = st.number_input("Cholesterol", min_value=0, value=200)
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["0", "1"])

    with col2:
        resting_ecg = st.selectbox("Resting ECG", list(resting_ecg_mapping.keys()))
        max_hr = st.number_input("Max Heart Rate Achieved", min_value=0, value=150)
        exercise_angina = st.selectbox("Exercise Induced Angina", list(exercise_angina_mapping.keys()))
        oldpeak = st.number_input("Oldpeak", min_value=0.0, value=1.0, step=0.1)
        st_slope = st.selectbox("ST Slope", list(st_slope_mapping.keys()))

    submit_button = st.form_submit_button("Predict")

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

    if prediction == 0:
        st.success("✅ You are not diagnosed with heart disease.")
    else:
        st.error("⚠️ Unfortunately, you have an 85% chance of having heart disease. Please consult a doctor.")
