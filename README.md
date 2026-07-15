
# 🏥 AI Patient Medical History Summary & Recommendation System

An AI-powered healthcare application developed using **Python**, **SQLite**, and **Streamlit** that helps doctors quickly review a patient's medical history before consultation. The system retrieves patient records, generates a structured medical summary, provides personalized recommendations based on medical history, and allows downloading the report as a PDF.

---

## 📌 Project Overview

During patient consultations, doctors often spend valuable time reviewing previous medical records. This application simplifies that process by automatically retrieving patient information from a database and presenting a concise medical summary along with relevant recommendations.

The application is designed as a healthcare assistance tool to improve the efficiency of patient checkups.

---

## ✨ Features

- 🔍 Search patient by Patient ID
- 📋 Retrieve patient medical history from SQLite database
- 🩺 Generate structured medical summary
- 💡 Rule-based recommendation system
- 📄 Download patient report as PDF
- 🖥️ Interactive Streamlit dashboard
- 🗂️ Modular Python project structure

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application |
| SQLite | Database Management |
| ReportLab | PDF Report Generation |
| VS Code | Development Environment |

---

## 📂 Project Structure

```
AI-Patient-Medical-History-Summary-System/
│
├── app.py
├── create_database.py
├── database.py
├── summary.py
├── recommendation.py
├── pdf_generator.py
├── hospital.db
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── screenshots/
│   ├── dashboard.png
│   ├── patient_details.png
│   └── report_download.png
│
└── report/
    └── Project_Report.pdf
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Patient-Medical-History-Summary-System.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Patient-Medical-History-Summary-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📋 Application Workflow

1. Launch the Streamlit application.
2. Enter the Patient ID.
3. Retrieve patient medical history.
4. View the automatically generated medical summary.
5. Review personalized recommendations.
6. Download the medical report as a PDF.

---

## 📊 Database Fields

The SQLite database stores the following patient information:

- Patient ID
- Name
- Age
- Gender
- Blood Group
- Allergies
- Previous Surgeries
- Medical Conditions
- Current Medications
- Last Visit Date
- Doctor Notes

---

## 💡 Sample Recommendations

The system generates recommendations based on patient history.

Examples include:

- Monitor blood pressure regularly.
- Check blood sugar levels weekly.
- Schedule ECG every six months.
- Avoid Penicillin if allergic.
- Continue prescribed medications.
- Schedule regular follow-up visits.

---

## 📸 Screenshots

### Dashboard

<img width="1920" height="1080" alt="Screenshot (267)" src="https://github.com/user-attachments/assets/57bb72f1-a7cc-4417-aaee-cbb14eaeb22e" />


### Patient Summary

<img width="1920" height="1080" alt="Screenshot (264)" src="https://github.com/user-attachments/assets/84971cc9-3e5c-496d-a133-26f89d6e21f2" />


### PDF Report

<img width="1920" height="1080" alt="Screenshot (265)" src="https://github.com/user-attachments/assets/dedfedfb-400f-492a-b30e-43f78094965a" />


---

## 🚀 Future Enhancements

- 🤖 AI-based Medical Summary Generation using NLP
- 🧠 Disease Risk Prediction using TensorFlow
- 🔐 Doctor Login & Authentication
- ☁️ Cloud Database Integration
- 📅 Appointment Management
- 📈 Patient Analytics Dashboard
- 🏥 Electronic Health Record (EHR) Integration

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Python Programming
- Database Connectivity using SQLite
- Streamlit Web Application Development
- PDF Report Generation
- Modular Project Development
- Rule-Based Recommendation Systems
- Healthcare Application Development

---

## 👨‍💻 Author

**Vishal Vishwas Desai**

📧 Email: vd6414@gmail.com

🔗 LinkedIn: https://linkedin.com/in/vishal-desai-84b26a260

💻 GitHub: https://github.com/Vishal-desai

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
