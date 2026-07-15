import sqlite3

DATABASE_NAME = "hospital.db"


def get_connection():
    """
    Create and return a database connection.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def get_patient_by_id(patient_id):
    """
    Retrieve a patient record using Patient ID.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    conn.close()

    return patient