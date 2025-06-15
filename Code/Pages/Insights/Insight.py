###########################################################################################
# This code is implemented by Dr.Anahita Ghazvini and Prof.Dr.Nurfadhlina Mohd sharef
#Email: anahitaghazvini@upm.edu.my;nurfadhlina@upm.edu.my
###########################################################################################
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import os

courses = [
    "Select Course",
    "AGEN KOMPUTERAN",
    "ANALISIS DAN REKA BENTUK PERMAINAN KOMPUTER",
    "ANALISIS DAN REKA BENTUK RANGKAIAN",
    "ANTARA RANGKAIAN",
    "APLIKASI BERGERAK",
    "FORENSIK KOMPUTER",
    "KESELAMATAN PANGKALAN DATA",
    "KESELAMATAN SISTEM KOMPUTER",
    "KENYATAAN MAYA",
    "KOMPUTERAN CERDAS",
    "KRIPTOGRAFI",
    "KUALITI PERISIAN",
    "ORGANISASI KOMPUTER DAN BAHASA HIMPUNAN",
    "PEMBANGUNAN APLIKASI BERGERAKII",
    "PEMBANGUNAN APLIKASI PANGKALAN DATA",
    "PEMBANGUNAN APLIKASI WEB",
    "PEMBANGUNAN PERISIAN SELAMAT",
    "PEMBANGUNAN PERMAINAN KOMPUTER",
    "PENDIGITAN AUDIO TAMPAK",
    "PENGATURCARAAN C++",
    "PENGATURCARAAN KOMPUTER I",
    "PENGATURCARAAN KOMPUTER II",
    "PENGATURCARAAN PYTHON",
    "PENGATURCARAAN SELARI DAN TERAGIH",
    "PENGKOMPUTAN SELARI DAN TERAGIH",
    "PENGURUSAN RANGKAIAN",
    "PENGUJIAN PERISIAN",
    "PENYELENGGARAAN DAN EVOLUSI PERISIAN",
    "PERDAGANGAN ELEKTRONIK",
    "PROJEK KEJURUTERAAN PERISIAN BERPASUKAN",
    "SELECT COURSE",
    "SISTEM BERASASKAN PENGETAHUAN",
    "SISTEM PENGOPERASIAN",
    "STATISTIK BAGI SAINS KOMPUTER",
    "STRUKTUR DATA DAN ALGORITMA",
    "STRUKTUR DISKRET",
    "PENGATURCARAAN SHELL"
]

# Define filename mappings for Matric No
filename_mappings = {
    '579619': '579619.csv',
    '262219': '262219.csv',
    '127219': '127219.csv'
}

def show_image(matric_no):
    image_path = f"Code/Pages/Insights/{matric_no}.png"
    if os.path.exists(image_path):
        st.image(image_path, caption=f"Matric No: {matric_no}")

def show():
    if 'button_clicks' not in st.session_state:
        st.session_state.button_clicks = {'redevelopment': 0, 'proceed': 0}

    selected_semester = st.selectbox(
        '**Choose Semester:**',
        ('Select Semester', 'Sem1-2020', 'Sem2-2020', 'Sem1-2021', 'Sem2-2021'),
        key="semester_selectbox"
    )
    st.write(f"You have selected the Semester: {selected_semester}")

    selected_course = st.selectbox(
        '**Choose Course:**',
        courses,
        key="course_selectbox"
    )
    st.write(f"You have selected the course: {selected_course}")

 
    if selected_course == "AGEN KOMPUTERAN":
        total_weeks = 7
        Most_week_Participation = 7
        Least_week_Participation = 4
        Acc = 98.59
        metrics_text = f"""
        <span style='font-size:small ; color:Red'>**Total Weeks:** {total_weeks}</span> | 
        <span style='font-size: small; color:blue'>**Most Week Participation:** {Most_week_Participation}</span> | 
        <span style='font-size: small; color:orange'>**Least Week Participation:** {Least_week_Participation}</span> | 
        <span style='font-size: small; color:green'>**Accuracy(%):** {Acc}</span>
        """
        col1, col2 = st.columns([4, 1])
        with col1:
             st.markdown(metrics_text, unsafe_allow_html=True)

        with col2:
            if st.checkbox("**Verification Analysis:** ", value=False):
                st.image("Code/Pages/Insights/Verification_analysis_visulization/PredictVSActual2020.png", use_container_width=True)

        # Display the content of "AGEN KOMPUTERAN.csv"
        file_path = 'Code/Pages/Insights/AGEN KOMPUTERAN.csv'
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            st.write(df)
        else:
            st.write("")

    selected_matric_no = st.selectbox(
        '**Choose Metric No:**',
        ('Select Metric No', '579619', '262219', '127219'),
        key="matric_selectbox"
    )
    st.write(f"You have selected the Metric No: {selected_matric_no}")

    #file_path = filename_mappings.get(f'Code/Pages/Insights/{selected_matric_no}.csv')
    file_path = f'Code/Pages/Insights/{selected_matric_no}.csv'
    if file_path is not None and os.path.exists(file_path):
        df = pd.read_csv(file_path)
        st.write(df)
    else:
        st.write("")

    show_image(selected_matric_no)

show()