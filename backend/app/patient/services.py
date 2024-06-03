from .models import Patient

def get_patient_full_name(patient):
    patient_full_name = f"{patient.last_name} {patient.first_name} {patient.surname}"
    return patient_full_name

def get_patients_full_names(patients):
    patients_full_names = []
    for patient in patients:
        patients_full_names.append(get_patient_full_name(patient))   
    return patients_full_names