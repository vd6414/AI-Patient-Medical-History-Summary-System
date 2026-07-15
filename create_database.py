import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    blood_group TEXT,
    allergies TEXT,
    surgeries TEXT,
    diseases TEXT,
    medications TEXT,
    last_visit TEXT,
    doctor_notes TEXT
)
""")

patients = [

(
1,"John Doe",45,"Male","O+",
"Penicillin,Nuts",
"Appendectomy (2015)",
"Migraine,Hypertension",
"Aspirin",
"2025-01-05",
"Monitor BP every month"
),

(
2,"Emily Smith",31,"Female","A+",
"None",
"None",
"Diabetes",
"Metformin",
"2025-03-18",
"Monitor blood sugar weekly"
),

(
3,"Michael Brown",60,"Male","B+",
"Seafood",
"Heart Bypass (2021)",
"Heart Disease",
"Atorvastatin",
"2025-04-12",
"ECG every 6 months"
),

(
4,"Sarah Johnson",27,"Female","AB+",
"Dust",
"None",
"Asthma",
"Inhaler",
"2025-06-08",
"Carry inhaler at all times"
),

(
5,"David Wilson",52,"Male","A-",
"None",
"Knee Surgery (2019)",
"Diabetes,Hypertension",
"Metformin,Amlodipine",
"2025-05-20",
"Encourage daily exercise"
)
]



cursor.executemany("""
INSERT OR REPLACE INTO patients
VALUES(?,?,?,?,?,?,?,?,?,?,?)
""",patients)

conn.commit()

conn.close()

print("Database Created Successfully")