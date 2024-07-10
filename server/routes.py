from flask import request, jsonify
from models import db, Doctor, Patient, Appointment, Department, Medication, MedicalRecord

def register_routes(app):
    # Doctor routes
    @app.route('/doctors', methods=['POST'])
    def add_doctor():
        data = request.get_json()
        if not data.get('name') or not data.get('specialty') or not isinstance(data.get('department_id'), int):
            return jsonify({"error": "Missing or invalid data"}), 400
        doctor = Doctor(name=data['name'], specialty=data['specialty'], department_id=data['department_id'])
        db.session.add(doctor)
        db.session.commit()
        return jsonify({"id": doctor.id}), 201

    @app.route('/doctors/<int:doctor_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_doctor(doctor_id):
        doctor = Doctor.query.get_or_404(doctor_id)
        if request.method == 'GET':
            return jsonify(doctor.to_dict())
        elif request.method == 'PUT':
            data = request.get_json()
            doctor.name = data.get('name', doctor.name)
            doctor.specialty = data.get('specialty', doctor.specialty)
            doctor.department_id = data.get('department_id', doctor.department_id)
            db.session.commit()
            return jsonify({'message': 'Doctor updated successfully'}), 200
        elif request.method == 'DELETE':
            db.session.delete(doctor)
            db.session.commit()
            return jsonify({'message': 'Doctor deleted successfully'}), 200

    # Patient routes
    @app.route('/patients', methods=['POST'])
    def add_patient():
        data = request.get_json()
        if not data.get('name') or not isinstance(data.get('age'), int) or data['age'] < 0 or not data.get('gender'):
            return jsonify({"error": "Missing or invalid data"}), 400
        patient = Patient(name=data['name'], age=data['age'], gender=data['gender'])
        db.session.add(patient)
        db.session.commit()
        return jsonify({"id": patient.id}), 201

    @app.route('/patients/<int:patient_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_patient(patient_id):
        patient = Patient.query.get_or_404(patient_id)
        if request.method == 'GET':
            return jsonify(patient.to_dict())
        elif request.method == 'PUT':
            data = request.get_json()
            patient.name = data.get('name', patient.name)
            patient.age = data.get('age', patient.age)
            patient.gender = data.get('gender', patient.gender)
            db.session.commit()
            return jsonify({'message': 'Patient updated successfully'}), 200
        elif request.method == 'DELETE':
            db.session.delete(patient)
            db.session.commit()
            return jsonify({'message': 'Patient deleted successfully'}), 200

    # Appointment routes
    @app.route('/appointments', methods=['POST'])
    def add_appointment():
        data = request.get_json()
        if not data.get('doctor_name') or not data.get('patient_name') or not data.get('appointment_date'):
            return jsonify({"error": "Missing or invalid data"}), 400
        appointment = Appointment(doctor_name=data['doctor_name'], patient_name=data['patient_name'], appointment_date=data['appointment_date'])
        db.session.add(appointment)
        db.session.commit()
        return jsonify({"id": appointment.id}), 201

    @app.route('/appointments/<int:appointment_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_appointment(appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
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

    # Department routes
    @app.route('/departments', methods=['POST'])
    def add_department():
        data = request.get_json()
        if not data.get('name'):
            return jsonify({"error": "Name is required"}), 400
        department = Department(name=data['name'])
        db.session.add(department)
        db.session.commit()
        return jsonify({"id": department.id}), 201

    @app.route('/departments/<int:department_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_department(department_id):
        department = Department.query.get_or_404(department_id)
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

    # Medication routes
    @app.route('/medications', methods=['POST'])
    def add_medication():
        data = request.get_json()
        if not data.get('name') or not data.get('dosage'):
            return jsonify({"error": "Name and dosage are required"}), 400
        medication = Medication(name=data['name'], dosage=data['dosage'])
        db.session.add(medication)
        db.session.commit()
        return jsonify({"id": medication.id}), 201

    @app.route('/medications/<int:medication_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_medication(medication_id):
        medication = Medication.query.get_or_404(medication_id)
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

    # Medical Record routes
    @app.route('/medical_records', methods=['POST'])
    def add_medical_record():
        data = request.get_json()
        if not data.get('patient_id') or not data.get('medication_id') or not data.get('diagnosis'):
            return jsonify({"error": "Missing or invalid data"}), 400
        medical_record = MedicalRecord(patient_id=data['patient_id'], medication_id=data['medication_id'], diagnosis=data['diagnosis'])
        db.session.add(medical_record)
        db.session.commit()
        return jsonify({"id": medical_record.id}), 201

    @app.route('/medical_records/<int:medical_record_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_medical_record(medical_record_id):
        medical_record = MedicalRecord.query.get_or_404(medical_record_id)
        if request.method == 'GET':
            return jsonify(medical_record.to_dict())
        elif request.method == 'PUT':
            data = request.get_json()
            medical_record.patient_id = data.get('patient_id', medical_record.patient_id)
            medical_record.medication_id = data.get('medication_id', medical_record.medication_id)
            medical_record.diagnosis = data.get('diagnosis', medical_record.diagnosis)
            db.session.commit()
            return jsonify({'message': 'Medical record updated successfully'}), 200
        elif request.method == 'DELETE':
            db.session.delete(medical_record)
            db.session.commit()
            return jsonify({'message': 'Medical record deleted successfully'}), 200

