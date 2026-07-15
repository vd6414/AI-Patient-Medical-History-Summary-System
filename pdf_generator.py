from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(patient, summary, recommendations):

    filename = f"{patient['name'].replace(' ', '_')}_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Patient Medical Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Name:</b> {patient['name']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Age:</b> {patient['age']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Gender:</b> {patient['gender']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Blood Group:</b> {patient['blood_group']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Medical Summary</b>", styles["Heading2"]))
    story.append(Paragraph(summary.replace("\n","<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/><b>Recommendations</b>", styles["Heading2"]))

    for rec in recommendations:
        story.append(Paragraph(rec, styles["BodyText"]))

    doc.build(story)

    return filename