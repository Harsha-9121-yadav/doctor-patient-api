from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


# =========================
# DOCTOR MODELS
# =========================

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    email: EmailStr
    is_active: bool


# =========================
# PATIENT MODELS
# =========================

class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    phone: str


# =========================
# IN-MEMORY STORAGE
# =========================

doctors = []
patients = []

next_doctor_id = 1
next_patient_id = 1


# =========================
# HOME API
# =========================

@app.get("/")
def home():
    return {"message": "Doctor Patient API is running"}


# =========================
# DOCTOR APIs
# =========================

# Create doctor
@app.post("/doctors", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate):
    global next_doctor_id

    new_doctor = {
        "id": next_doctor_id,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }

    doctors.append(new_doctor)

    next_doctor_id += 1

    return new_doctor


# Get all doctors
@app.get("/doctors", response_model=List[DoctorResponse])
def get_doctors():
    return doctors


# Get doctor by ID
@app.get("/doctors/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int):

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# =========================
# PATIENT APIs
# =========================

# Create patient
@app.post("/patients", response_model=PatientResponse)
def create_patient(patient: PatientCreate):
    global next_patient_id

    new_patient = {
        "id": next_patient_id,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }

    patients.append(new_patient)

    next_patient_id += 1

    return new_patient


# Get all patients
@app.get("/patients", response_model=List[PatientResponse])
def get_patients():
    return patients