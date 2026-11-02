from fastapi import APIRouter

router = APIRouter(
    prefix="/appointments",
    tags=["Qabullar"]
)

appointments = []


@router.get("/")
def get_appointments():
    return appointments


@router.post("/")
def create_appointment(appointment: dict):
    appointments.append(appointment)

    return {
        "message": "Qabul muvaffaqiyatli yaratildi",
        "appointment": appointment
    }