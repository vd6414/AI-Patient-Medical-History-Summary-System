from database import get_patient_by_id
from summary import generate_summary

patient = get_patient_by_id(1)

summary = generate_summary(patient)

print(summary)