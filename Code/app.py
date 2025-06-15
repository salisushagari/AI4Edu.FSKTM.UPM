###########################################################################################
# This code is implemented by Dr.Anahita Ghazvini and Prof.Dr.Nurfadhlina Mohd sharef
#Email: anahitaghazvini@upm.edu.my;nurfadhlina@upm.edu.my
###########################################################################################

import streamlit as st
from PIL import Image
import base64
from Pages.Model_monitoring import Summary
from Pages.Insights import Insight
from Pages.Reporting import Maintenance
#import Simulation
from Pages.Intro import Intro
import traceback  # Import the traceback module

# Function to set background image for tables
def set_table_background_image(image_path):
    try:
        table_image = Image.open(image_path)
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        st.markdown(
            f"""
            <style>
            table {{
                background: url('data:image/png;base64,{encoded_image}');
                background-size: cover;
                color: white;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Error loading the background image: {e}")

def main():
    try:
        # Set the background image for the tables
        table_background_image_path = "Code/LOGO.png"
        set_table_background_image(table_background_image_path)

        # Add an image at the top of the sidebar
        image_url = "code/UPM.png"
        st.sidebar.image(image_url, use_container_width=True, width=200)

        st.sidebar.header("Interactive Model Performance and Explainability (IMPEx)")

        # Initialize session state 
        if 'selected_courses' not in st.session_state:
            st.session_state.selected_courses = None

        # Main menu selection
        pages = {
            "Overview":Intro,
            "Model Monitoring": Summary,
            "Insights": Insight,
            "Reporting": Maintenance,
        }
        selected_page = st.sidebar.selectbox("Select an option", list(pages.keys()))



        page = pages[selected_page]
        page.show()

        if selected_page == "Maintenance":
            Maintenance.show_maintenance_page()

    except Exception as e:
        # Print the exception details
        st.error(f"An error occurred: {e}")
        st.write("Full traceback:")
        st.write(traceback.format_exc())

if __name__ == "__main__":
    main()