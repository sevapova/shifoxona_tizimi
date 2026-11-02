from app.domain.entities.patient import Patient
from app.domain.ports.patient_repository import PatientRepository


class PatientService:

    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def get_all_patients(self):
        return self.repository.get_all()

    def create_patient(
        self,
        full_name: str,
        age: int,
        phone: str,
        diagnosis: str
    ):
        if age <= 0 or age > 120:
            raise ValueError("Bemor yoshi noto'g'ri")

        patient = Patient(
            id=0,
            full_name=full_name,
            age=age,
            phone=phone,
            diagnosis=diagnosis
        )

        return self.repository.add(patient)

    def get_patient_by_id(self, patient_id: int):
        return self.repository.get_by_id(patient_id)