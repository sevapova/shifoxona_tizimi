patients = []

def get_all_patients():
    return patients


def add_patient(patient):
    new_patient = {
        "id": len(patients) + 1,
        "full_name": patient.full_name,
        "age": patient.age,
        "phone": patient.phone,
        "diagnosis": patient.diagnosis
    }

    patients.append(new_patient)

    return new_patient