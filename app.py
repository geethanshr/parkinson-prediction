import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

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
            'Tremor': yes_no_to_numeric(tremor),
            'Bradykinesia': yes_no_to_numeric(bradykinesia),
            'UPDRS': updrs,
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

elif selected == "Statistics":
    st.title("Statistics")
    st.write("### General Statistics")
    st.write("Total number of test subjects: 2105")
    st.write("Average diet quality score: 4.91")
    st.write("Average HDL cholesterol level: 59.67 mg/dL")
    st.write("Average LDL cholesterol level: 126.15 mg/dL")

    st.write("### Gender Distribution")
    gender_labels = ['Male', 'Female']
    gender_sizes = [50.74, 49.26]
    gender_colors = ['#ff9999','#66b3ff']
    gender_explode = (0.1, 0)  # explode 1st slice

    fig1, ax1 = plt.subplots()
    ax1.pie(gender_sizes, explode=gender_explode, labels=gender_labels, colors=gender_colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    st.write("### Age Distribution")
    age_labels = ['70-79', '80-89', '50-59', '60-69']
    age_sizes = [26.22, 25.08, 24.94, 23.75]
    age_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    age_explode = (0.1, 0, 0, 0)  # explode 1st slice

    fig2, ax2 = plt.subplots()
    ax2.pie(age_sizes, explode=age_explode, labels=age_labels, colors=age_colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig2)

    st.write("### Ethnic Diversity")
    eth_labels = ['Caucasian', 'African American', 'Asian', 'Others']
    eth_sizes = [60.33, 20.19, 9.36, 10.12]
    eth_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    eth_explode = (0.1, 0, 0, 0)  # explode 1st slice

    fig3, ax2 = plt.subplots()
    ax2.pie(age_sizes, explode=age_explode, labels=age_labels, colors=age_colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig3)



