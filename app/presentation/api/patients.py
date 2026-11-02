from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.application.use_cases.patient_service import PatientService


def create_patient_router(service: PatientService):

    router = APIRouter(
        prefix="/patients",
        tags=["Bemorlar"]
    )

    class PatientCreate(BaseModel):
        full_name: str
        age: int = Field(gt=0, le=120)
        phone: str
        diagnosis: str

    @router.get("/")
    def get_patients():
        return service.get_all_patients()

    @router.post("/")
    def create_patient(patient: PatientCreate):
        try:
            return service.create_patient(
                full_name=patient.full_name,
                age=patient.age,
                phone=patient.phone,
                diagnosis=patient.diagnosis
            )
        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error)
            )

    @router.get("/{patient_id}")
    def get_patient(patient_id: int):
        patient = service.get_patient_by_id(patient_id)

        if patient is None:
            raise HTTPException(
                status_code=404,
                detail="Bemor topilmadi"
            )

        return patient

    return router