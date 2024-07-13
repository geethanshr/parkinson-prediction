import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# Import graphing functions
from graphing import display_general_statistics, display_distributions, display_parkinsons_diagnosis

# Load the models
with open('model1.pkl', 'rb') as f:
    model1 = pickle.load(f)

with open('model2.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open('model3.pkl', 'rb') as f:
    model3 = pickle.load(f)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Risk Assessment", "Statistics"],
        icons=["house", "bar-chart"],
        menu_icon="cast",
        default_index=0
    )

if selected == "Risk Assessment":
    st.title("Parkinson's Disease Risk Assessment")

    # General Details
    st.header("General Details")
    patient_name = st.text_input("Patient Name")

    # Demographic Details
    st.header("Demographic Details")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    ethnicity = st.selectbox("Ethnicity", ["Caucasian", "African American", "Asian", "Other"])

    # Lifestyle Factors
    st.header("Lifestyle Factors")
    bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, step=0.1)
    smoking = st.radio("Smoking", ["No", "Yes"])
    alcohol_consumption = st.slider("Alcohol Consumption (units per week)", 0, 20)
    physical_activity = st.slider("Physical Activity (hours per week)", 0, 10)
    diet_quality = st.slider("Diet Quality (0-10)", 0, 10)
    sleep_quality = st.slider("Sleep Quality (4-10)", 4, 10)

    # Medical History
    st.header("Medical History")
    family_history_parkinsons = st.radio("Family History of Parkinson's Disease", ["No", "Yes"])
    traumatic_brain_injury = st.radio("History of Traumatic Brain Injury", ["No", "Yes"])
    hypertension = st.radio("Hypertension", ["No", "Yes"])
    diabetes = st.radio("Diabetes", ["No", "Yes"])
    depression = st.radio("Depression", ["No", "Yes"])
    stroke = st.radio("History of Stroke", ["No", "Yes"])

    # Clinical Measurements
    st.header("Clinical Measurements")
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 180)
    diastolic_bp = st.slider("Diastolic Blood Pressure (mmHg)", 60, 120)
    cholesterol_total = st.slider("Total Cholesterol (mg/dL)", 150, 300)
    cholesterol_ldl = st.slider("LDL Cholesterol (mg/dL)", 50, 200)
    cholesterol_hdl = st.slider("HDL Cholesterol (mg/dL)", 20, 100)
    cholesterol_triglycerides = st.slider("Triglycerides (mg/dL)", 50, 400)

    # Cognitive and Functional Assessments
    st.header("Cognitive and Functional Assessments")
    updrs = st.number_input("UPDRS", min_value=0.0, max_value=199.0, step=0.5)
    moca = st.number_input("MoCA", min_value=0.0, max_value=30.0, step=0.1)
    functional_assessment = st.slider("Functional Assessment Score (0-10)", 0, 10)

    # Symptoms
    st.header("Symptoms")
    tremor = st.radio("Tremor", ["No", "Yes"])
    rigidity = st.radio("Rigidity", ["No", "Yes"])
    bradykinesia = st.radio("Bradykinesia", ["No", "Yes"])
    postural_instability = st.radio("Postural Instability", ["No", "Yes"])
    speech_problems = st.radio("Speech Problems", ["No", "Yes"])
    sleep_disorders = st.radio("Sleep Disorders", ["No", "Yes"])
    constipation = st.radio("Constipation", ["No", "Yes"])

    # Helper function to convert Yes/No to 1/0
    def yes_no_to_numeric(value):
        return 1 if value == "Yes" else 0

    # Prediction logic
    if st.button("Submit"):
        # Collect input data
        input_data = {
            'Rigidity': yes_no_to_numeric(rigidity),
            'FunctionalAssessment': functional_assessment,
            'MoCA': moca,
           
