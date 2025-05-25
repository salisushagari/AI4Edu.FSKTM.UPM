###########################################################################################
# This code is implemented by Dr.Anahita Ghazvini and Prof.Dr.Nurfadhlina Mohd sharef
#Email: anahitaghazvini@upm.edu.my;nurfadhlina@upm.edu.my
###########################################################################################
import streamlit as st
import pandas as pd
import base64
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import warnings
from io import BytesIO
import streamlit.components.v1 as components

warnings.filterwarnings("ignore")

def generate_pdf(selected_semester, total_courses, acc_greater_than_60, acc_less_than_60, dynamic_content, shap_image_path, lime_image_path, fir_image_path):
    buffer = BytesIO()

    # Create a PDF document
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Get default styles
    styles = getSampleStyleSheet()

    # Add content to the PDF
    content = []

    # Add title
    content.append(Paragraph(f"Summary Report - Semester: {selected_semester}", styles['Title']))

    # Add metrics
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Total Courses: {total_courses}", styles['Normal']))
    content.append(Paragraph(f"Courses with Acc >= 0.60: {acc_greater_than_60}", styles['Normal']))
    content.append(Paragraph(f"Courses with Acc < 0.60: {acc_less_than_60}", styles['Normal']))
    content.append(Spacer(1, 12))

    # Add dynamic content
    content.append(Paragraph("Dynamic Content:", styles['Heading2']))
    content.append(Spacer(1, 6))
    content.append(Paragraph(dynamic_content, styles['Normal']))

    # Add images
    if os.path.exists(shap_image_path):
        content.append(Image(shap_image_path, width=400, height=300))
    if os.path.exists(lime_image_path):
        content.append(Image(lime_image_path, width=400, height=300))
    if os.path.exists(fir_image_path):
        content.append(Image(fir_image_path, width=400, height=300))

    # Build the PDF
    pdf.build(content)
    buffer.seek(0)

    return buffer

def set_table_background_image(image_path):
    st.markdown(
        f"""
        <style>
            .css-1rhbuit-Table {{
                background-image: url("{image_path}");
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def load_data(selected_semester, suffix=''):
    data_path = f"{selected_semester}{suffix}"
    try:
        data = pd.read_csv(f"{data_path}.csv")
        return data
    except FileNotFoundError:
        st.warning(f"Data file not found at the specified path: {data_path}.csv")
        return None
    except pd.errors.EmptyDataError:
        st.warning(f"Data file is empty: {data_path}.csv")
        return None
    except Exception as e:
        st.warning(f"Error loading data: {e}")
        return None

def show():
    if 'button_clicks' not in st.session_state:
        st.session_state.button_clicks = {'redevelopment': 0, 'proceed': 0}

    selected_semester = st.selectbox(
        '**Choose Semester:**',
        ('Sem1-2020', 'Sem2-2020', 'Sem1-2021', 'Sem2-2021')
    )

    data = load_data(selected_semester)

    if data is not None:
        total_courses = len(data)
        acc_greater_than_60 = 36
        acc_less_than_60 = 1

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Courses", total_courses)

        with col2:
            st.metric("Total Courses with Acc >= 0.60", acc_greater_than_60)

        with col3:
            st.metric("Total Courses with Acc < 0.60", acc_less_than_60)

        st.write(f"**Performance of all courses during the {selected_semester} session 2020-2021:**", style={'font-size': '18px'})

        # Display the corresponding image based on the selected semester
        st.image(f"{selected_semester}.png", use_column_width=True)

        st.write("<span style='color: green;'>**Courses with Accuracy above and equal >=60:**</span>",
                 unsafe_allow_html=True,
                 style={'font-size': '18px'})
        course_above_data = load_data(f"{selected_semester}_Courseabove")
        if course_above_data is not None:
            st.dataframe(course_above_data)

        st.write("<span style='color: red;'>**Courses with Accuracy below than <60:**</span>",
                 unsafe_allow_html=True,
                 style={'font-size': '18px'})
        course_below_data_original = load_data(f"{selected_semester}_Coursebelow")
        st.dataframe(course_below_data_original)

        course_below_data = load_data(selected_semester, suffix='_Coursebelow')
        if course_below_data is not None:
            if 'Course' in course_below_data.columns:
                selected_courses_below_60 = st.multiselect("Select courses", course_below_data['Course'])
                filtered_course_below_data = course_below_data[
                    course_below_data['Course'].isin(selected_courses_below_60)]
        # handling and displaying the data

        st.session_state.selected_courses_summary_below_60 = filtered_course_below_data
        st.write(filtered_course_below_data)
        st.subheader("SHAP Values to Optimize and Debug ML Models")
        # dropdown here, before SHAP or other interpretations
        feature_importance_type = st.selectbox(
        "Select SHAP Visualization Type:",
         ["Global SHAP Values (Bar Plot)", 
          "Global SHAP Values (Beeswarm Plot)", 
          "Local Individual SHAP Values (Waterfall Plot)", 
          "Local Individual SHAP Values (Force Plot)",
          "Local Individual SHAP Values (Stacked Force Plot)"],
          index=0  # Default to the first option
         )

        interpretability_method = ["SHAP", "LIME", "FI"]
        filtered_course_below_data['Interpretability Method'] = interpretability_method[0]

        for method in interpretability_method:
            if method != "Choose Method":
                semester_suffix = selected_semester[-4:]
        if feature_importance_type == "Global SHAP Values (Bar Plot)":
            
            st.markdown("""
                **SHAP Bar Plot:** The SHAP bar chart illustrates the factors with the most significant influence on predictions. 
              Longer bars represent greater impact, while shorter bars indicate less influence. 
              Referring to the SHAP bar plot, the top three features with the highest bar lengths are Gender, Age, and Country. 
            """)
            st.image(f"SHAPBAR{semester_suffix}.png", caption="SHAP Interpretability")

        elif feature_importance_type == "Global SHAP Values (Beeswarm Plot)":
            st.markdown("""
                **SHAP Beeswarm Plot:** The Beeswarm plot offers detailed insights for early grade prediction, unlike the Bar plot.It reveals how feature values relate to predictions, showing longer red points for Gender and Age on the positive side, indicating higher predicted grades.Conversely, for Country and Type Sponsor, red points are prominent on the negative side, suggesting lower predicted grades. Both bar and Beeswarm plots provided the same ranked features due to mean and mean absolute of SHAP values, confirming reliability.In summary, while Bar plots offer a general overview, Beeswarm plots provide deeper insights into feature influence on predicted grades.
            """)
            st.image(f"SHAPBee{semester_suffix}.png", caption="SHAP Interpretability")
        elif feature_importance_type == "Local Individual SHAP Values (Waterfall Plot)":
            st.markdown("""
                **SHAP Waterfall Plot:** The waterfall model provides a comprehensive display of a single prediction. In this visualization, the list of input variables is presented on the left side of the plot, arranged from top to bottom.The grey value next to each variable represents its value in these particular instances.On the right side of the illustration, each variable is depicted with arrows: red arrows indicate variables such as Percentage_Feq_W1-7, Gender, Age, and Type_Sponsor that push our model to predict a higher grade, while blue arrows indicate that attributes like FreqW1,FreqW2,and Country push our model to predict a lower grade.In this plot, the model predicted the value for the course 'ANALITIK BISNES' as f(x) = 0.542.
            """)
            st.image(f"SHAPWater{semester_suffix}.png", caption="SHAP Interpretability")
        elif feature_importance_type == "Local Individual SHAP Values (Force Plot)":
            st.markdown("""
                **SHAP Force Plot:** Force plots offer a clearer and more concise visualization compared to the computationally expensive waterfall method, highlighting key factors leading to higher-grade predictions. This visualization confirms that the predicted value, which is 0.55, aligns closely with the predicted value observed in the waterfall plot.The variables, namely Percentage_Feq_W1-7, Gender, Age, and Type_Sponsor, are depicted in red on the left side of the plot, indicating their positive contribution towards a higher-grade prediction. Conversely, features such as FreqW1, FreqW2, and Country are represented in blue on the right side, suggesting they contribute to a lower-grade prediction. The length of the arrows in the force plot corresponds to the magnitude of the SHAP values, with longer arrows indicating features that have a higher impact on the prediction. 
            """)
            st.image(f"SHAPForce{semester_suffix}.png", caption="SHAP Interpretability")

        elif feature_importance_type == "Local Individual SHAP Values (Stacked Force Plot)":
            st.markdown("""
                **SHAP Stacked Force Plot:** The stacked force plot visualizes individual predictions made by our model. On the x-axis are the magnitudes of the feature contributions (Shapley values), while the y-axis shows the model’s prediction output. Each slice of blue depicts an individual feature’s corresponding Shapley value. Blue marks features that decreased the model’s prediction, while red features increased the model’s prediction. The final prediction for that user is determined where the blue and red segments meet on the plot.
            """)
            html_content = open(f"SHAPSTACK{semester_suffix}.html", 'r').read()
            components.html(html_content, width=800, height=600)

        st.subheader("Interpret Black Box Models using LIME (Local Interpretable Model-Agnostic Explanations)")
        # dropdown here, before SHAP or other interpretations
        feature_importance_type = st.selectbox(
        "Select LIME Visualization Type:",
         ["LIME Feature Importance"],
          index=0  # Default to the first option
         )
        if feature_importance_type == "LIME Feature Importance":
           st.markdown("""
               **LIME Feature Importance Plot:** In the LIME Feature Importance bar plot, green bars represent positive weights, meaning that features such as Age, Percentage_StudentW1-7, Type_Sponsor, and Gender positively influence our model's prediction. Conversely, red bars indicate negative weights, where features of Country, FreqW1, and FreqW2 are contribute in the opposite direction, potentially leading to a lower grade for course ANALITIK BISNES. Larger weights signify a greater influence of the feature (Age) on our model's decision-making process. """)
           st.image(f"LIMEBAR{semester_suffix}.png", caption="LIME Local Explanation for Course ANALITIK BISNES")

