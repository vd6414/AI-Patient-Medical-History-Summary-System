import streamlit as st
import sqlite3

from summary import generate_summary
from recommendation import generate_recommendations
from pdf_generator import create_pdf

st.set_page_config(
    page_title="AI Patient Medical Summary",
    page_icon="🏥",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🏥 Hospital Dashboard")

st.sidebar.write("### AI Patient Medical Summary System")

st.sidebar.success("Python")
st.sidebar.success("SQLite")
st.sidebar.success("Streamlit")

st.sidebar.write("---")

st.sidebar.info(
"""
This application helps doctors quickly review
patient medical history before consultation.
"""
)

# ---------------- Header ---------------- #

st.title("🏥 AI Patient Medical History Summary System")

st.caption("Internship Project | Developed by Vishal Vishwas Desai")

st.write("---")

# ---------------- Statistics ---------------- #

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Patients", "5")

with c2:
    st.metric("Doctors", "12")

with c3:
    st.metric("Departments", "4")

st.write("---")

# ---------------- Search ---------------- #

search_type = st.radio(
    "Search Patient By",
    ["Patient ID", "Patient Name"]
)

conn = sqlite3.connect("hospital.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

patient = None

if search_type == "Patient ID":

    patient_id = st.number_input(
        "Enter Patient ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        cursor.execute(
            "SELECT * FROM patients WHERE patient_id=?",
            (patient_id,)
        )

        patient = cursor.fetchone()

else:

    name = st.text_input("Enter Patient Name")

    if st.button("Search"):

        cursor.execute(
            "SELECT * FROM patients WHERE name LIKE ?",
            ("%" + name + "%",)
        )

        patient = cursor.fetchone()

# ---------------- Result ---------------- #

if patient:

    st.success("Patient Record Found")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👤 Patient Information")

        st.write("**Name:**", patient["name"])
        st.write("**Age:**", patient["age"])
        st.write("**Gender:**", patient["gender"])
        st.write("**Blood Group:**", patient["blood_group"])

    with col2:

        st.subheader("📅 Visit Details")

        st.write("**Last Visit:**", patient["last_visit"])
        st.write("**Diseases:**", patient["diseases"])
        st.write("**Allergies:**", patient["allergies"])
        st.write("**Medication:**", patient["medications"])

    st.write("---")

    summary = generate_summary(patient)

    st.subheader("📄 Medical Summary")

    st.info(summary)

    st.write("---")

    st.subheader("💡 Recommendations")

    recommendations = generate_recommendations(patient)

    for rec in recommendations:

        st.success(rec)

    pdf_file = create_pdf(
        patient,
        summary,
        recommendations
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            "📄 Download Report",
            file,
            file_name=pdf_file
        )

elif patient is None:
    pass

else:

    st.error("Patient Not Found")

conn.close()

st.write("---")

st.caption("© 2026 AI Patient Medical History Summary System")