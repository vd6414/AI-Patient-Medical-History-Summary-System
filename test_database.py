from database import get_patient_by_id

patient = get_patient_by_id(1)

if patient:
    print("Patient Found")
    print("--------------------------")

    print("ID :", patient["patient_id"])
    print("Name :", patient["name"])
    print("Age :", patient["age"])
    
    print("Gender :", patient["gender"])
    print("Blood Group :", patient["blood_group"])
    print("Diseases :", patient["diseases"])
    print("Medications :", patient["medications"])
    print("Allergies :", patient["allergies"])
    print("Doctor Notes :", patient["doctor_notes"])

else:
    print("Patient Not Found")