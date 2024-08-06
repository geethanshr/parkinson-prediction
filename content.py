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
            <p><strong>About the Model:</strong> <a href="#">Click here</a></p>
            <blockquote>
                    <p><strong>Challenges Tackled:</strong></p>
                    <p>"While Preparing the Model Architecture, to carry EDA leads was a challenge since the models were trained over a smaller data (but more relevant data) for a particular values of features and Diagnosis. Train-Test split within the same data poses often a less accuracy threat compared to the accuracy determined by the project environment."</p>
                    <p>"The features of the Dataset were less straight forward and more numerically organized that are often not a direct field to ask for the patients. Alcohol Consumption for instance was units per week, Functional Assessment with similar layout were field where the Parameter were numerical but over what span of time and precision they are being determined, couldn't greet a direct address from the team at the initial level"</p>
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
                <img src="https://media.licdn.com/dms/image/D5635AQFsyf2F1HdMJA/profile-framedphoto-shrink_400_400/0/1707495992128?e=1723564800&v=beta&t=tokb0f-cZJU3JtLjwWD4QcS-UC9AV2hVnd-0vpKGCHw" style="width: 100px; height: 100px; vertical-align: middle;">
                Geethansh's LinkedIn
            </a>
            <p><strong>About the deployment:</strong> <a href="https://www.linkedin.com/posts/geethanshr_powerbi-nocode-businessintelligence-activity-7210502366268207104-Cjix?utm_source=share&utm_medium=member_desktop">Click here</a></p>
            <blockquote>
                    <p><strong>Challenges Tackled:</strong></p>
                    <p>"One of the major challenges we faced was integrating multiple data sources. We overcame this by using advanced ETL processes."</p>
                    <p>"Another challenge was ensuring data privacy and security. We implemented strict access controls and encryption techniques."</p>
                </blockquote>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
