from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialty': self.specialty,
            'department_id': self.department_id
        }

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    medical_records = db.relationship('MedicalRecord', backref='patient', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'date': self.date
        }

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String, db.ForeignKey('doctor.name'), nullable=False)
    patient_name = db.Column(db.String, db.ForeignKey('patient.name'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'doctor_name': self.doctor_name,
            'patient_name': self.patient_name,
            'appointment_date': self.appointment_date
        }

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    doctors = db.relationship('Doctor', backref='department', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    medical_records = db.relationship('MedicalRecord', backref='medication', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dosage': self.dosage
        }

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    diagnosis = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'medication_id': self.medication_id,
            'diagnosis': self.diagnosis
        }
