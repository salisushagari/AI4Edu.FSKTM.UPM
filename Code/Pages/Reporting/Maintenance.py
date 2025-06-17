###########################################################################################
# This code is implemented by Dr.Anahita Ghazvini and Prof.Dr.Nurfadhlina Mohd sharef
#Email: anahitaghazvini@upm.edu.my;nurfadhlina@upm.edu.my
###########################################################################################
import streamlit as st
import pandas as pd

def show_maintenance_page():
    if st.session_state.get('maintenance_page_shown', False):
        return  # Don't show the page if it has already been shown

    st.write("**These courses need to be redeveloped (according to low average accuracy):**")

    try:
        st.image("Code/Pages/Reporting/AVG.png", use_container_width=True)
    except Exception as e:
        st.error(f"Error displaying the image: {e}")

    # Read AVG.csv file and display its content
    avg_df = pd.read_csv("Code/Pages/Reporting/AVG.csv")
    st.write("**List of All Courses with Accuracy below 60%:**")
    st.write(avg_df)

    # Set a session state variable to indicate that the page has been shown
    st.session_state.maintenance_page_shown = True

# If this script is run directly, show the maintenance page
#if __name__ == "__main__":
    #show_maintenance_page()

# Add a show method to be called from app.py
def show():
    # Instead of calling show_maintenance_page directly, call the existing show method
    show_maintenance_page()