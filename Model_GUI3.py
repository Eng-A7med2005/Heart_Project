import customtkinter as ctk
import joblib
import numpy as np

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

loaded_model = joblib.load("Heart_disease_model_FF.pkl")
sex_mapping = {"Male": 1, "Female": 0}
chest_pain_mapping = {"Asymptomatic": 0, "Non-Anginal Pain": 1, "Atypicaّّl Angina": 2, "Typical Angina": 3}
resting_ecg_mapping = {"Normal": 0, "ST-T Abnormality": 1, "Left Ventricular Hypertrophy": 2}
exercise_angina_mapping = {"No": 0, "Yes": 1}
st_slope_mapping = {"Flat": 0, "Up": 1, "Down": 2}

app = ctk.CTk()
app.geometry("800x650")
app.title("💓 Heart Disease Prediction by AIvolution Team")
title = ctk.CTkLabel(app, text="💓 Heart Disease Prediction", font=ctk.CTkFont(size=26, weight="bold"))
title.pack(pady=(20, 0))

subtitle = ctk.CTkLabel(app, text="By AIvolution Team", font=ctk.CTkFont(size=18))
subtitle.pack(pady=(0, 20))
input_frame = ctk.CTkFrame(app)
input_frame.pack(padx=20, pady=10, fill="both", expand=True)
entries = {}

def add_input(label_text, row, widget_type, options=None, default=None):
    label = ctk.CTkLabel(input_frame, text=label_text)
    label.grid(row=row, column=0, padx=10, pady=8, sticky="w")
    if widget_type == "entry":
        entry = ctk.CTkEntry(input_frame)
        entry.insert(0, str(default))
    elif widget_type == "combo":
        entry = ctk.CTkComboBox(input_frame, values=list(options.keys()))
        entry.set(list(options.keys())[0])
    entries[label_text] = entry
    entry.grid(row=row, column=1, padx=10, pady=8, sticky="ew")

add_input("Age", 0, "entry", default=30)
add_input("Sex", 1, "combo", options=sex_mapping)
add_input("Chest Pain Type", 2, "combo", options=chest_pain_mapping)
add_input("Resting Blood Pressure", 3, "entry", default=120)
add_input("Cholesterol", 4, "entry", default=200)
add_input("Fasting Blood Sugar > 120 mg/dl", 5, "combo", options={"0": 0, "1": 1})
add_input("Resting ECG", 6, "combo", options=resting_ecg_mapping)
add_input("Max Heart Rate Achieved", 7, "entry", default=150)
add_input("Exercise Induced Angina", 8, "combo", options=exercise_angina_mapping)
add_input("Oldpeak", 9, "entry", default=1.0)
add_input("ST Slope", 10, "combo", options=st_slope_mapping)
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=18))
result_label.pack(pady=10)

def predict():
    try:
        input_data = [
            float(entries["Age"].get()),
            sex_mapping[entries["Sex"].get()],
            chest_pain_mapping[entries["Chest Pain Type"].get()],
            float(entries["Resting Blood Pressure"].get()),
            float(entries["Cholesterol"].get()),
            int(entries["Fasting Blood Sugar > 120 mg/dl"].get()),
            resting_ecg_mapping[entries["Resting ECG"].get()],
            float(entries["Max Heart Rate Achieved"].get()),
            exercise_angina_mapping[entries["Exercise Induced Angina"].get()],
            float(entries["Oldpeak"].get()),
            st_slope_mapping[entries["ST Slope"].get()],
        ]

        prediction = loaded_model.predict([input_data])[0]

        if prediction == 0:
            result_label.configure(text="✅ You are not diagnosed with heart disease.", text_color="green")
        else:
            result_label.configure(
                text="⚠️ You have a high chance of heart disease. Please consult a doctor.",
                text_color="red"
            )

    except Exception as e:
        result_label.configure(text=f"❌ Error: {e}", text_color="orange")

predict_btn = ctk.CTkButton(app, text="Predict", command=predict)
predict_btn.pack(pady=10)
app.mainloop()
