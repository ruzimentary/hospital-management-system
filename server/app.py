from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Doctor, Patient, Appointment, Department, Medication, MedicalRecord
import routes  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Register routes
routes.register_routes(app)

@app.route('/')
def home():
    return "Welcome to the Hospital Management System!"

if __name__ == '__main__':
    app.run(debug=True)