import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the models
with open('model1.pkl', 'rb') as f:
    model1 = pickle.load(f)

with open('model2.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open('model3.pkl', 'rb') as f:
    model3 = pickle.load(f)

st.title("Parkinson's Disease Risk Assessment")

# General Details
st.header("General Details")
patient_name = st.text_input("Patient Name")

# Demographic Details
st.header("Demographic Details")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
ethnicity = st.selectbox("Ethnicity", ["Caucasian", "African American", "Asian", "Other"])
education_level = st.selectbox("Education Level", ["None", "High School", "Bachelor's", "Higher"])

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
updrs = st.slider("UPDRS Score (0-199)", 0, 199)
moca = st.slider("MoCA Score (0-30)", 0, 30)
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
    return 1.0 if value == "Yes" else 0.0

# Prediction logic
if st.button("Submit"):
    # Collect input data
    input_data = {
        'Rigidity': yes_no_to_numeric(rigidity),
        'FunctionalAssessment': float(functional_assessment),
        'MoCA': float(moca),
        'Tremor': yes_no_to_numeric(tremor),
        'Bradykinesia': yes_no_to_numeric(bradykinesia),
        'UPDRS': float(updrs),
        'PosturalInstability': yes_no_to_numeric(postural_instability)
    }

    # Select model and features
    if functional_assessment < 5 and updrs > 50:
        model = model1
        features = ['Rigidity', 'FunctionalAssessment', 'MoCA', 'Tremor', 'Bradykinesia']
    elif yes_no_to_numeric(tremor) == 1:
        model = model2
        features = ['UPDRS', 'Rigidity', 'FunctionalAssessment']
    else:
        model = model3
        features = ['Rigidity', 'Bradykinesia', 'PosturalInstability', 'UPDRS']

    # Prepare data for prediction
    data = pd.DataFrame({feature: [input_data[feature]] for feature in features})

    # Make prediction
    prediction = model.predict(data)

    # Display prediction result
    st.write("### Prediction Result")
    st.write(f"The predicted diagnosis for Parkinson's Disease is: {'Yes' if prediction[0] == 1 else 'No'}")
