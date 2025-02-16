import os
import streamlit as st
from streamlit_option_menu import option_menu
import pickle

st.set_page_config(
    page_title="Prediction of Disease Outbreak",
    layout="wide",
    page_icon="🏥"
)

# Load Models
diabetes_model = pickle.load(open(r"C:\Users\reddy\Downloads\2.Prediction of Disease Outbreaks\training_models\diabetes_model2.pkl", "rb"))
heart_model = pickle.load(open(r"C:\Users\reddy\Downloads\2.Prediction of Disease Outbreaks\training_models\heart_model.pkl", "rb"))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        "Prediction of Disease Outbreak System",
        ["Diabetes", "Heart Disease"],
        menu_icon="hospital-fill",
        icons=["activity", "heart"],
        default_index=0
    )

# -------------- DIABETES PREDICTION ------------------
if selected == "Diabetes":
    st.title("Diabetes Prediction System Using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies", key="pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level", key="glucose")
    with col3:
        blood_pressure = st.text_input("Blood Pressure", key="bp")
    with col1:
        skin_thickness = st.text_input("Skin Thickness", key="skin")
    with col2:
        insulin = st.text_input("Insulin Level", key="insulin")
    with col3:
        BMI = st.text_input("BMI Value", key="bmi")
    with col1:
        diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function", key="pedigree")
    with col2:
        age = st.text_input("Age of the Person", key="age_diabetes")

    diab_diagnosis = " "
    
    if st.button("Diabetes Prediction"):
        try:
            user_input = [float(x) for x in [Pregnancies, glucose, blood_pressure, skin_thickness, insulin, BMI, diabetes_pedigree_function, age]]
            diab_prediction = diabetes_model.predict([user_input])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = "The person is diabetic."
            else:
                diab_diagnosis = "The person is not diabetic."
                
            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values.")

# -------------- HEART DISEASE PREDICTION ------------------
if selected == "Heart Disease":
    st.title("Heart Disease Prediction System Using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age", key="age_heart")
    with col2:
        sex = st.text_input("Sex (1 = Male, 0 = Female)", key="sex")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)", key="cp")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure", key="trestbps")
    with col2:
        chol = st.text_input("Serum Cholesterol (mg/dl)", key="chol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)", key="fbs")
    with col1:
        restecg = st.text_input("Resting ECG Results (0-2)", key="restecg")
    with col2:
        thalach = st.text_input("Max Heart Rate Achieved", key="thalach")
    with col3:
        exang = st.text_input("Exercise-Induced Angina (1 = Yes, 0 = No)", key="exang")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise", key="oldpeak")
    with col2:
        slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)", key="slope")
    with col3:
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", key="ca")
    with col1:
        thal = st.text_input("Thalassemia (0-3)", key="thal")

    heart_diagnosis = " "
    
    if st.button("Heart Disease Prediction"):
        try:
            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = "The person has heart disease."
            else:
                heart_diagnosis = "The person does not have heart disease."

            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values.")
