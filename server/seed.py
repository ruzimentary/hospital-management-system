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

def seed_phase_2():
    # Create Appointments
    app1 = Appointment(doctor_name="Dr. John Mwangi", patient_name="Alice Njeri", appointment_date=datetime(2023, 7, 10, 10, 0))
    app2 = Appointment(doctor_name="Dr. Mary Wanjiru", patient_name="Michael Kiprono", appointment_date=datetime(2023, 7, 11, 11, 0))
    app3 = Appointment(doctor_name="Dr. Peter Otieno", patient_name="Grace Achieng", appointment_date=datetime(2023, 7, 12, 9, 0))

    db.session.add_all([app1, app2, app3])
    db.session.commit()
    app2 = Appointment(doctor_name="Dr. Mary Wanjiru", patient_name="Michael Kiprono", appointment_date=datetime(2023, 7, 11, 11, 0))
    app3 = Appointment(doctor_name="Dr. Peter Otieno", patient_name="Grace Achieng", appointment_date=datetime(2023, 7, 12, 9, 0))

    db.session.add_all([app1, app2, app3])
    db.session.commit()

    # Create Medications
    med1 = Medication(name="Aspirin", dosage="100mg")
    med2 = Medication(name="Ibuprofen", dosage="200mg")
    med3 = Medication(name="Paracetamol", dosage="500mg")

    db.session.add_all([med1, med2, med3])
    db.session.commit()

def seed_phase_3():
    # Create Medical Records
    mr1 = MedicalRecord(patient_id=1, medication_id=1, diagnosis="Hypertension")
    mr2 = MedicalRecord(patient_id=2, medication_id=2, diagnosis="Migraine")
    mr3 = MedicalRecord(patient_id=3, medication_id=3, diagnosis="Flu")

    db.session.add_all([mr1, mr2, mr3])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_phase_1()
        seed_phase_2()
        seed_phase_3()