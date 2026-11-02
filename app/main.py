from fastapi import FastAPI

from app.routers import patients
from app.routers import doctors
from app.routers import appointments


app = FastAPI(
    title="Shifoxona boshqaruv tizimi",
    description="Bemorlar, shifokorlar va qabullarni boshqarish API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Shifoxona boshqaruv tizimiga xush kelibsiz!"
    }


app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
