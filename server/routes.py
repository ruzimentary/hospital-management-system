from flask import Flask, request, jsonify, abort
from models import db, Doctor, Patient, Appointment, Department, Medication, MedicalRecord

app = Flask(__name__)

def validate_doctor(data):
    errors = []
    if not data.get('name'):
        errors.append('Name is required.')
    if not data.get('specialty'):
        errors.append('Specialty is required.')
    if not isinstance(data.get('department_id'), int):
        errors.append('Department ID must be an integer.')
    return errors

@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.get_json()
    errors = validate_doctor(data)
    if errors:
        return jsonify({"errors": errors}), 400

    doctor = Doctor(name=data['name'], specialty=data['specialty'], department_id=data['department_id'])
    db.session.add(doctor)
    db.session.commit()
    return jsonify({"id": doctor.id}), 201

def validate_patient(data):
    errors = []
    if not data.get('name'):
        errors.append('Name is required.')
    if not isinstance(data.get('age'), int) or data['age'] < 0:
        errors.append('Age must be a positive integer.')
    if data.get('gender') not in ['Male', 'Female']:
        errors.append('Gender must be either "Male" or "Female".')
    return errors

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    errors = validate_patient(data)
    if errors:
        return jsonify({"errors": errors}), 400

    patient = Patient(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(patient)
    db.session.commit()
    return jsonify({"id": patient.id}), 201

def validate_appointment(data):
    errors = []
    if not data.get('doctor_name'):
        errors.append('Doctor name is required.')
    if not data.get('patient_name'):
        errors.append('Patient name is required.')
    if not data.get('appointment_date'):
        errors.append('Appointment date is required.')
    return errors

@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()
    errors = validate_appointment(data)
    if errors:
        return jsonify({"errors": errors}), 400
    appointment = Appointment(doctor_name=data['doctor_name'], patient_name=data['patient_name'], appointment_date=data['appointment_date'])
    db.session.add(appointment)
    db.session.commit()
    return jsonify({"id": appointment.id}), 201

@app.route('/appointments/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(appointment.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        appointment.doctor_name = data.get('doctor_name', appointment.doctor_name)
        appointment.patient_name = data.get('patient_name', appointment.patient_name)
        appointment.appointment_date = data.get('appointment_date', appointment.appointment_date)
        db.session.commit()
        return jsonify({'message': 'Appointment updated successfully'}), 200
    elif request.method == 'DELETE':
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'}), 200

@app.route('/departments', methods=['POST'])
def add_department():
    data = request.get_json()
    if not data.get('name'):
        return jsonify({"error": "Name is required"}), 400
    department = Department(name=data['name'])
    db.session.add(department)
    db.session.commit()
    return jsonify({"id": department.id}), 201

@app.route('/departments/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_department(id):
    department = Department.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(department.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        department.name = data.get('name', department.name)
        db.session.commit()
        return jsonify({'message': 'Department updated successfully'}), 200
    elif request.method == 'DELETE':
        db.session.delete(department)
        db.session.commit()
        return jsonify({'message': 'Department deleted successfully'}), 200

@app.route('/medications', methods=['POST'])
def add_medication():
    data = request.get_json()
    if not data.get('name') or not data.get('dosage'):
        return jsonify({"error": "Name and dosage are required"}), 400
    medication = Medication(name=data['name'], dosage=data['dosage'])
    db.session.add(medication)
    db.session.commit()
    return jsonify({"id": medication.id}), 201

@app.route('/medications/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_medication(id):
    medication = Medication.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(medication.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        medication.name = data.get('name', medication.name)
        medication.dosage = data.get('dosage', medication.dosage)
        db.session.commit()
        return jsonify({'message': 'Medication updated successfully'}), 200
    elif request.method == 'DELETE':
        db.session.delete(medication)
        db.session.commit()
        return jsonify({'message': 'Medication deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)