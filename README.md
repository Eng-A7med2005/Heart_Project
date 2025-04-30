

---

# 🩺 Heart Disease Prediction App  

This is a **GUI application** built with `CustomTkinter` that allows users to input medical data and receive a **heart disease prediction** based on a trained machine learning model. The app provides an intuitive interface for users to enter their health parameters, processes the input, and displays the prediction with color-coded results.  

## ✨ Features  
✅ **User-Friendly Interface** – Built with `CustomTkinter`, featuring a clean and responsive layout.  
✅ **Machine Learning Integration** – Uses a pre-trained model (`Heart_disease_model.pkl`) to make predictions.  
✅ **Dynamic UI** – The layout adjusts dynamically to different screen sizes.  
✅ **Color-Coded Results** – Green for "No Heart Disease" and Red for "High Risk".  

## 🚀 How to Run  
### Note : You should install an older version of scikit-learn by :
```bash
   pip install -U scikit-learn==1.1.3
   ```

1. Install dependencies:  
   ```bash
   pip install customtkinter joblib
   ```
    
2. Place `Heart_disease_model.pkl` in the same directory.
    
3. Run the script:  
   ```bash
   python Model_GUI3.py
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

## 📷 GUI  
![Screenshot 2025-02-07 144538](https://github.com/user-attachments/assets/20de884b-4d45-4a97-9e50-02271bcd8ef7)  


## 🔄 Update: Streamlit Web Interface Added
We’ve added a fully functional and user-friendly Streamlit web interface for the Heart Disease Prediction project!
Now, you can try out the model directly through your browser without needing to run any code locally.

🚀 Live Demo:
👉 https://heartproject-aivolution-team.streamlit.app/

This interface allows users to input medical data, get instant predictions, and understand potential heart disease risks based on their values — all in a clean and accessible format.


---

