from fastapi import APIRouter
from app.schemas.patient import PatientSchema
from app.services.patient_service import (
    get_all_patients,
    add_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Bemorlar"]
)


@router.get("/")
def get_patients():
    return get_all_patients()


@router.post("/")
def create_patient(patient: PatientSchema):
    return add_patient(patient)