import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def display_general_statistics():
    st.write("### General Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total number of test subjects", "2105")
    col2.metric("Average diet quality score", "4.91")
    col1.metric("Average HDL cholesterol level", "59.67 mg/dL")
    col2.metric("Average LDL cholesterol level", "126.15 mg/dL")
    col1.metric("Average Systolic BP", "133.72 mm Hg")
    col2.metric("Average Diastolic BP", "90.25 mm Hg")

def display_distributions():
    st.write("### Distributions")
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))

    # Gender Distribution
    gender_labels = ['Male', 'Female']
    gender_sizes = [50.74, 49.26]
    gender_colors = ['#ff9999','#66b3ff']
    gender_explode = (0.1, 0)  # explode 1st slice

    axs[0].pie(gender_sizes, explode=gender_explode, labels=gender_labels, colors=gender_colors,
               autopct='%1.1f%%', shadow=True, startangle=140)
    axs[0].set_title('Gender Distribution')

    # Age Distribution
    age_labels = ['70-79', '80-89', '50-59', '60-69']
    age_sizes = [26.22, 25.08, 24.94, 23.75]
    age_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    age_explode = (0.1, 0, 0, 0)  # explode 1st slice

    axs[1].pie(age_sizes, explode=age_explode, labels=age_labels, colors=age_colors,
               autopct='%1.1f%%', shadow=True, startangle=140)
    axs[1].set_title('Age Distribution')

    # Ethnic Diversity
    eth_labels = ['Caucasian', 'African American', 'Asian', 'Others']
    eth_sizes = [60.33, 20.19, 9.36, 10.12]
    eth_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    eth_explode = (0.1, 0, 0, 0)  # explode 1st slice

    axs[2].pie(eth_sizes, explode=eth_explode, labels=eth_labels, colors=eth_colors,
               autopct='%1.1f%%', shadow=True, startangle=140)
    axs[2].set_title('Ethnic Diversity')

    # Adjust layout to ensure the plots fit well
    plt.tight_layout()
    st.pyplot(fig)

def display_parkinsons_diagnosis():
    st.write("### Parkinson's Diagnosis by Gender")
    labels = ['Male', 'Female']
    no = [415, 386]
    yes = [653, 651]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, no, width, label='No')
    rects2 = ax.bar(x + width/2, yes, width, label='Yes')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Gender')
    ax.set_ylabel('Number of Subjects')
    ax.set_title("Parkinson's Diagnosis by Gender")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    for rects in [rects1, rects2]:
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    st.pyplot(fig)
