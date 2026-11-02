from fastapi import FastAPI

from app.application.use_cases.patient_service import PatientService
from app.infrastructure.adapters.memory_patient_repository import (
    MemoryPatientRepository
)
from app.presentation.api.patients import create_patient_router


app = FastAPI(
    title="Shifoxona boshqaruv tizimi",
    description="Toza va oltiyoqlama arxitektura asosidagi tizim",
    version="3.0.0"
)


repository = MemoryPatientRepository()

patient_service = PatientService(repository)

app.include_router(
    create_patient_router(patient_service)
)


@app.get("/")
def home():
    return {
        "message": "Shifoxona boshqaruv tizimiga xush kelibsiz!",
        "architecture": "Clean and Hexagonal Architecture"
    }