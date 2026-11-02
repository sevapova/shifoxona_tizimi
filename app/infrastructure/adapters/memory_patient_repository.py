from typing import List, Optional

from app.domain.entities.patient import Patient
from app.domain.ports.patient_repository import PatientRepository


class MemoryPatientRepository(PatientRepository):

    def __init__(self):
        self.patients = []
        self.next_id = 1

    def get_all(self) -> List[Patient]:
        return self.patients

    def add(self, patient: Patient) -> Patient:
        patient.id = self.next_id

        self.patients.append(patient)

        self.next_id += 1

        return patient

    def get_by_id(self, patient_id: int) -> Optional[Patient]:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient

        return None