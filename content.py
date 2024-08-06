import streamlit as st

def by_the_team():
    #st.title("By the Team")

    st.write("### Shivam's Contributions")
    st.markdown(
        """
        <div style="border: 1px solid #e6e6e6; padding: 20px; border-radius: 10px;">
            <a href="https://www.linkedin.com/in/geethanshr/" target="_blank">
                <img src="https://media.licdn.com/dms/image/D5635AQFsyf2F1HdMJA/profile-framedphoto-shrink_400_400/0/1707495992128?e=1723564800&v=beta&t=tokb0f-cZJU3JtLjwWD4QcS-UC9AV2hVnd-0vpKGCHw" style="width: 100px; height: 100px; vertical-align: middle;">
                Geethansh's LinkedIn
            </a>
            <p><strong>Project Link:</strong> <a href="#">Project</a></p>
            <p><strong>Challenges Tackled:</strong></p>
            <ul>
                <li><strong>Problem 1:</strong> Description of how the problem was solved.</li>
                <li><strong>Problem 2:</strong> Description of how the problem was solved.</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("### Gourav")
    st.markdown("""
    <blockquote>
        [![Gourav's LinkedIn](https://img.shields.io/badge/Gourav-LinkedIn-blue)](https://www.linkedin.com/in/gourav/)
        <br><br>
        **Project Link:** [Project](#)
        <br><br>
        **Challenges Tackled:**
        <br><br>
        - **Problem 1:** Description of how the problem was solved.
        <br><br>
        - **Problem 2:** Description of how the problem was solved.
    </blockquote>
    """, unsafe_allow_html=True)
