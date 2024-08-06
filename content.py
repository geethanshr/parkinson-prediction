import numpy as np
import streamlit as st

def by_the_team():
    st.title("By the Team")

    st.write("### Shivam's Contributions")
    st.markdown("""
    <blockquote>
        [![Shivam's LinkedIn](https://img.shields.io/badge/Shivam-LinkedIn-blue)](https://www.linkedin.com/in/shivam/)
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

    st.write("### Gourav's Contributions")
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
