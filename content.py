import streamlit as st

def by_the_team():
    #st.title("By the Team")

    #st.write("### Gourav")
    st.markdown(
        """
        <div style="border: 1px solid #e6e6e6; padding: 20px; border-radius: 10px;">
            <a href="https://www.linkedin.com/in/gourav-pandey-a4505a29a/" target="_blank">
                <img src="https://media.licdn.com/dms/image/D5603AQFDLRLPwQ3n5A/profile-displayphoto-shrink_400_400/0/1718229540129?e=1728518400&v=beta&t=VFpe8wrta4oPO6ExWyOUVRpLS_IZ7hVvgXhOqdQoz_U" style="width: 100px; height: 100px; vertical-align: middle;">
                Gourav's LinkedIn
            </a>
            <p><strong>About the Model:</strong> <a href="https://www.linkedin.com/posts/gourav-pandey-a4505a29a_parkinson-analysis-report-activity-7226810548565291008-vRf9?utm_source=share&utm_medium=member_desktop">Click here</a></p>
            <blockquote>
                    <p><strong>Challenges Tackled:</strong></p>
                    <p>"While Preparing the Model Architecture, to carry EDA leads was a challenge since the models were trained over a smaller data (but more relevant data) for a particular values of features and Diagnosis. Train-Test split within the same data poses often a less accuracy threat compared to the accuracy determined by the project environment."</p>
                </blockquote>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    #st.write("### Geethansh's Contributions")
    st.markdown(
        """
        <div style="border: 1px solid #e6e6e6; padding: 20px; border-radius: 10px;">
            <a href="https://www.linkedin.com/in/geethanshr/" target="_blank">
                <img src="https://media.licdn.com/dms/image/v2/D5603AQFzsfTn7n38tA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1707495990589?e=1733356800&v=beta&t=fKwmaymNzI3ZgC1AdObeqDGhCvDPKFjzaE8n9sfC2M8" style="width: 100px; height: 100px; vertical-align: middle;">
                Geethansh's LinkedIn
            </a>
            <p><strong>About the deployment:</strong> <a href="https://www.linkedin.com/posts/geethanshr_parkinson-prediction-model-deployment-activity-7226810543355912192-9TU3?utm_source=share&utm_medium=member_desktop">Click here</a></p>
            <blockquote>
                    <p><strong>Challenges Tackled:</strong></p>
                    <p>"I wasted half day debugging incompatibility between ML model and Scikit-Learn. Read through to save time and avoid repeating the error. The latest version of Scikit-Learn didn't recognize the trees in my RandomForestClassifier. As developers, data scientists, and engineers, we often overlook one of the most crucial aspects of ML/Dev Ops—version control. Version control isn’t just a best practice—it’s a necessity in our fast-paced tech world. Let’s make it a priority to manage our environments carefully and avoid those costly and time-consuming surprises!"</p>
                </blockquote>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
