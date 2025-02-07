

---

# 🩺 Heart Disease Prediction App  

This is a **GUI application** built with `CustomTkinter` that allows users to input medical data and receive a **heart disease prediction** based on a trained machine learning model. The app provides an intuitive interface for users to enter their health parameters, processes the input, and displays the prediction with color-coded results.  

## ✨ Features  
✅ **User-Friendly Interface** – Built with `CustomTkinter`, featuring a clean and responsive layout.  
✅ **Machine Learning Integration** – Uses a pre-trained model (`Heart_disease_model.pkl`) to make predictions.  
✅ **Dynamic UI** – The layout adjusts dynamically to different screen sizes.  
✅ **Color-Coded Results** – Green for "No Heart Disease" and Red for "High Risk".  

## 🚀 How to Run  
1. Install dependencies:  
   ```bash
   pip install customtkinter joblib
   ```  
2. Place `Heart_disease_model.pkl` in the same directory.  
3. Run the script:  
   ```bash
   python Model_GUI.py
   ```  

## 📌 Input Parameters  
- **Age**  
- **Sex (Male/Female)**  
- **Chest Pain Type**  
- **Resting Blood Pressure**  
- **Cholesterol Level**  
- **Fasting Blood Sugar**  
- **Resting ECG Results**  
- **Maximum Heart Rate**  
- **Exercise-Induced Angina**  
- **Oldpeak (ST Depression)**  
- **ST Slope**  

## 🎯 Prediction Output  
- **Green Message** → "You are not diagnosed with heart disease."  
- **Red Message** → "Unfortunately, you have an 85% chance of having heart disease. Please consult a doctor."  

## 📷 Screenshot  
*(Attach a screenshot of the UI here)*  

---
