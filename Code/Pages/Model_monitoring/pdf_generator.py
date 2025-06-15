###########################################################################################
# This code is implemented by Dr.Anahita Ghazvini and Prof.Dr.Nurfadhlina Mohd sharef
#Email: anahitaghazvini@upm.edu.my;nurfadhlina@upm.edu.my
###########################################################################################
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(selected_semester, total_courses, acc_greater_than_60, acc_less_than_60, course_above_data, course_below_data_original, dynamic_content):
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


    # Build the PDF
    pdf.build(content)
    buffer.seek(0)

    return buffer