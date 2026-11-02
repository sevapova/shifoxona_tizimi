from pydantic import BaseModel


class PatientSchema(BaseModel):
    full_name: str
    age: int
    phone: str
    diagnosis: str