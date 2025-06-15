###########################################################################################
# This code is implemented by Dr.Anahita Ghazvini and Prof.Dr.Nurfadhlina Mohd sharef
#Email: anahitaghazvini@upm.edu.my;nurfadhlina@upm.edu.my
###########################################################################################
import streamlit as st
import pandas as pd

def show():
    # Display additional information
    st.write(
        """
        # **Interactive Model Performance and Explainability (IMPEx)**

        Interactive Model Performance and Explainability Evaluation (IMPEx) system is developed to support interaction in machine learning through case studies in academic support. This system employs two sets of time series data:
        1)  Assessment dataset and
        2)  Learning Management System (LMS) dataset.

        The assessment dataset provides information about the undergraduate program for 3720 students in Computer Science at a public university, and the LMS dataset provides details of each student's access log reports collected from Universiti Putra Malaysia (UPM) LMS (PutraBLAST).

        This system is built based on an enhanced deep time series model and offers Explainable Deep Time Series Analysis for Transparent Educational Insight through three stages:
        1) Model monitoring,
        2) Editing, and
        3) Reporting.

        This research is based on the research grant for Interactive Machine Learning based on Deep Reinforcement Learning and Generative Adversarial Network Hybrid for Digital Twin
        (FA2386-21-1-4050).

        For more information, you can contact:
        - **Principal Investigator of the project:** Associate Professor Dr. Nurfadhlina Mohd Sharef (nurfadhlina@upm.edu.my)
        - **Postdoctoral Researcher:** Dr. Anahita Ghazvini(anahitaghazvini@upm.edu.my)
        - **Other Project Members:**
          - Associate Professor Dr. Norwati Mustapha
          - Associate Professor Dr. Razali Yaakob
          - Dr. Khairul Azhar Kasmiran
          - Professor Dr. Lee Lai Soon
          - Associate Professor Dr. Raja Kamil Raja
        """
    )


show()