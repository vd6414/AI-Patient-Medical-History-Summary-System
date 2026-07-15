def generate_summary(patient):

    summary = f"""
===============================
PATIENT MEDICAL SUMMARY
===============================

Patient ID     : {patient['patient_id']}
Name           : {patient['name']}
Age            : {patient['age']}
Gender         : {patient['gender']}
Blood Group    : {patient['blood_group']}

-------------------------------
Medical History
-------------------------------

Diseases:
{patient['diseases']}

Allergies:
{patient['allergies']}

Previous Surgeries:
{patient['surgeries']}

Current Medications:
{patient['medications']}

Last Visit:
{patient['last_visit']}

Doctor Notes:
{patient['doctor_notes']}

===============================
"""

    return summary