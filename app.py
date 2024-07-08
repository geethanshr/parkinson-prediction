import streamlit as st
import pandas as pd
import pickle

# Load the model from the pickle file
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model1 = load_model()

# Define the main function for the Streamlit app
def main():
    st.title('Parkinson\'s Disease Diagnosis Prediction')
    st.write('Enter the following parameters to get a diagnosis prediction:')

    # Create input fields for the user to enter data
    rigidity = st.number_input('Rigidity', min_value=0, max_value=100, value=50)
    functional_assessment = st.number_input('Functional Assessment', min_value=0, max_value=100, value=50)
    moca = st.number_input('MoCA', min_value=0, max_value=100, value=50)
    tremor = st.selectbox('Tremor', options=[0, 1])
    bradykinesia = st.number_input('Bradykinesia', min_value=0, max_value=100, value=50)

    # Create a dictionary of the input data
    input_data = {
        'Rigidity': rigidity,
        'FunctionalAssessment': functional_assessment,
        'MoCA': moca,
        'Tremor': tremor,
        'Bradykinesia': bradykinesia
    }

    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make prediction using the loaded model
    prediction = model_1.predict(input_df)

    # Display the prediction result
    st.write('### Prediction:')
    if prediction[0] == 0:
        st.write('No Parkinson\'s Disease')
    else:
        st.write('Parkinson\'s Disease')

if __name__ == '__main__':
    main()
