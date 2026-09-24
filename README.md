# Doctor Patient API

A simple REST API built using FastAPI to manage Doctors and Patients.

## Tech Stack

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn
- In-memory storage

## Features

### Doctor APIs

- Create a doctor
- Get all doctors
- Get a doctor by ID

### Patient APIs

- Create a patient
- Get all patients

## Validation

- Doctor email must be valid.
- Patient age must be greater than 0.
- Pydantic models are used for request validation.
- HTTPException is used for error handling.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check whether API is running |
| POST | `/doctors` | Create a doctor |
| GET | `/doctors` | Get all doctors |
| GET | `/doctors/{doctor_id}` | Get doctor by ID |
| POST | `/patients` | Create a patient |
| GET | `/patients` | Get all patients |

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv