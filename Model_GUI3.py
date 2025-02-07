import customtkinter as ctk
import joblib

# Load the trained model
mod = joblib.load("Heart_disease_model.pkl")


def submit():
    input_data = [
        int(age_entry.get()),  # Age
        sex_mapping[sex_var.get()],  # Sex
        chest_pain_mapping[chest_pain_var.get()],  # ChestPainType
        int(resting_bp_entry.get()),  # RestingBP
        int(cholesterol_entry.get()),  # Cholesterol
        int(fasting_bs_var.get()),  # FastingBS
        resting_ecg_mapping[resting_ecg_var.get()],  # RestingECG
        int(max_hr_entry.get()),  # MaxHR
        exercise_angina_mapping[exercise_angina_var.get()],  # ExerciseAngina
        float(oldpeak_entry.get()),  # Oldpeak
        st_slope_mapping[st_slope_var.get()],  # ST_Slope
    ]

    prediction = mod.predict([input_data])[0]  # Get prediction

    if prediction == 0:
        result_text = "You are not diagnosed with heart disease."
        result_label.configure(text=result_text, fg_color="green", text_color="white")
    else:
        result_text = "Unfortunately, you have an 85% chance of having heart disease. Please consult a doctor."
        result_label.configure(text=result_text, fg_color="red", text_color="white")


# Mappings
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

# GUI Setup
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Heart Disease Prediction")
root.geometry("600x800")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

ctk.CTkLabel(root, text="Heart Disease Prediction", font=("Arial", 22, "bold")).pack(
    pady=10
)

frame = ctk.CTkFrame(root)
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Inputs Grid Layout
input_frame = ctk.CTkFrame(frame)
input_frame.pack(fill="both", expand=True)

labels = [
    "Age:",
    "Sex:",
    "Chest Pain Type:",
    "RestingBP:",
    "Cholesterol:",
    "FastingBS:",
    "RestingECG:",
    "MaxHR:",
    "Exercise Angina:",
    "Oldpeak:",
    "ST Slope:",
]

data_widgets = [
    ctk.CTkEntry(input_frame, width=200, height=35),
    ctk.CTkOptionMenu(
        input_frame,
        variable=ctk.StringVar(value="Male"),
        values=list(sex_mapping.keys()),
        width=200,
        height=35,
    ),
    ctk.CTkOptionMenu(
        input_frame,
        variable=ctk.StringVar(value="Asymptomatic"),
        values=list(chest_pain_mapping.keys()),
        width=200,
        height=35,
    ),
    ctk.CTkEntry(input_frame, width=200, height=35),
    ctk.CTkEntry(input_frame, width=200, height=35),
    ctk.CTkOptionMenu(
        input_frame,
        variable=ctk.StringVar(value="0"),
        values=["0", "1"],
        width=200,
        height=35,
    ),
    ctk.CTkOptionMenu(
        input_frame,
        variable=ctk.StringVar(value="Normal"),
        values=list(resting_ecg_mapping.keys()),
        width=200,
        height=35,
    ),
    ctk.CTkEntry(input_frame, width=200, height=35),
    ctk.CTkOptionMenu(
        input_frame,
        variable=ctk.StringVar(value="No"),
        values=list(exercise_angina_mapping.keys()),
        width=200,
        height=35,
    ),
    ctk.CTkEntry(input_frame, width=200, height=35),
    ctk.CTkOptionMenu(
        input_frame,
        variable=ctk.StringVar(value="Flat"),
        values=list(st_slope_mapping.keys()),
        width=200,
        height=35,
    ),
]

for i, (label_text, widget) in enumerate(zip(labels, data_widgets)):
    ctk.CTkLabel(input_frame, text=label_text, font=("Arial", 14)).grid(
        row=i // 2, column=(i % 2) * 2, pady=5, padx=10, sticky="w"
    )
    widget.grid(row=i // 2, column=(i % 2) * 2 + 1, pady=5, padx=10, sticky="w")

(
    age_entry,
    sex_var,
    chest_pain_var,
    resting_bp_entry,
    cholesterol_entry,
    fasting_bs_var,
    resting_ecg_var,
    max_hr_entry,
    exercise_angina_var,
    oldpeak_entry,
    st_slope_var,
) = data_widgets

# Buttons Grid Layout
button_frame = ctk.CTkFrame(frame)
button_frame.pack(pady=10)

submit_button = ctk.CTkButton(
    button_frame,
    text="Predict",
    command=submit,
    fg_color="#007bff",
    text_color="white",
    corner_radius=10,
    width=200,
    height=40,
)
submit_button.grid(row=0, column=0, padx=10, pady=5)

# Result Label with Frame
result_frame = ctk.CTkFrame(frame, fg_color="#333")
result_frame.pack(pady=10, padx=20, fill="x")
result_label = ctk.CTkLabel(result_frame, text="", font=("Arial", 16))
result_label.pack(pady=10)

root.mainloop()
