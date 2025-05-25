1. Installation

#######################Install the following libraries using pip############################

numpy
streamlit
streamlit_option_menu
seaborn
matplotlib
plotly
pandas
joblib
scikit-learn
reportlab
pillow
fpdf2
pdfkit
wkhtmltopdf
weasyprint
chardet
streamlit-aggrid


#####################################################################

2. Main Files
(Backend Model)
File 1: IMPEx_eLSTM_Model_Training_and_Evaluation_Per_Course_Per_Sem.ipynb
This file trains and evaluates an enhanced LSTM model using the dataset synthetic_samples_Model4.csv. It processes this data to predict outcomes for each course and semester, and then saves the trained model to the file elstmg_Model_using_FSG4.h5.
(Deployment of IMPEx system)
File 2: App.py
This file provides a sidebar for navigation among pages (Overview, Model Monitoring, Insights, Reporting), applies a table background image, and includes error handling with traceback display.
File 3: Intro.py
Provides an introduction and overview of the Interactive Model Performance and Explainability (IMPEx) system, detailing its purpose, datasets used, and stages of analysis, along with contact information for the project team.
File 4: pdf_generator.py
Creates a PDF report with a summary of metrics related to a selected semester, including total courses and performance data, and incorporates dynamic content. It uses the reportlab library to format and generate the PDF document.
File 5: Summary.py
Generates a PDF report summarizing metrics and dynamic content for a selected semester, including charts and images for SHAP and LIME interpretability methods. It also defines functions to set a table background image and load data from CSV files, while the show function displays interactive Streamlit components for data visualization, including metrics, images, and model interpretability plots.
File 6: Insight.py
Provides an interactive dashboard for selecting semesters and courses, displaying related metrics and data from CSV files, and showing images for specific student matriculation numbers.
File 6: Maintenance.py
Displays a maintenance page within a Streamlit app that identifies courses needing redevelopment due to low average accuracy. It includes:
1. Image Display: Shows an image (AVG.png) related to course accuracy.
2. Data Display: Reads and displays the contents of AVG.csv, listing all courses with accuracy below 60%.
3. Page Display Control: Ensures the maintenance page is shown only once per session by using a session state variable.


#####################################################################
3. Deployment

To deploy the AcaPerforma System on the web using Streamlit, run the following file:
File 7: Streamlit Jupyter.ipynb

