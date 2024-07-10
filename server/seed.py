from app import app
from models import db, Doctor, Patient, Appointment, Department, Medication, MedicalRecord
from datetime import datetime

def seed_phase_1():
    # Create Departments
    dept1 = Department(name="Cardiology")
    dept2 = Department(name="Neurology")
    dept3 = Department(name="Pediatrics")

    db.session.add_all([dept1, dept2, dept3])
    db.session.commit()

    # Create Doctors
    doc1 = Doctor(name="Dr. John Mwangi", specialty="Cardiologist", department_id=dept1.id)
    doc2 = Doctor(name="Dr. Mary Wanjiru", specialty="Neurologist", department_id=dept2.id)
    doc3 = Doctor(name="Dr. Peter Otieno", specialty="Pediatrician", department_id=dept3.id)

    db.session.add_all([doc1, doc2, doc3])
    db.session.commit()

    # Create Patients
    pat1 = Patient(name="Alice Njeri", age=30, gender="Female")
    pat2 = Patient(name="Michael Kiprono", age=45, gender="Male")
    pat3 = Patient(name="Grace Achieng", age=22, gender="Female")

    db.session.add_all([pat1, pat2, pat3])
    db.session.commit()