from dataclasses import dataclass


@dataclass
class Patient:
    id: int
    full_name: str
    age: int
    phone: str
    diagnosis: str