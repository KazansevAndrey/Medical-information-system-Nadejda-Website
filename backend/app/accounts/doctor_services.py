def get_doctor_full_name(request):
    doctor = request.user
    full_name = f"{doctor.last_name} {doctor.first_name} {doctor.surname}"
    return full_name