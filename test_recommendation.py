from database import get_patient_by_id
from recommendation import generate_recommendations

patient = get_patient_by_id(1)

recommendations = generate_recommendations(patient)

print("RECOMMENDATIONS\n")

for i, rec in enumerate(recommendations, start=1):
    print(f"{i}. {rec}")