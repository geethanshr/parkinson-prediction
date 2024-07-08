import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the model
def load_model(model_file):
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
    return model

# Load the model and scaler
model = load_model('model1.pkl')
scaler = model.named_steps['scaler']  # Assuming 'scaler' is the name of your StandardScaler step

# Define your Streamlit app
def main():
    st.title('Random Forest Classifier Prediction App')

    # Add inputs for user to enter data
    st.sidebar.header('Input Parameters')
    # Example: you can add sliders or text boxes for users to input data

    # Example: you can add code to retrieve user inputs
    input_data = {
        'Rigidity': st.sidebar.slider('Rigidity', 0, 10, 5),
        'FunctionalAssessment': st.sidebar.slider('Functional Assessment', 0, 100, 50),
        'MoCA': st.sidebar.slider('MoCA', 0, 100, 50),
        'Tremor': st.sidebar.selectbox('Tremor', [0, 1]),
        'Bradykinesia': st.sidebar.slider('Bradykinesia', 0, 10, 5)
    }

    # Convert input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Perform scaling using the pre-fitted scaler
    input_scaled = scaler.transform(input_df)

    # Make predictions
    prediction = model.predict(input_scaled)

    # Display prediction
    st.subheader('Prediction')
    st.write(prediction)

if __name__ == '__main__':
    main()
