def get_doctor_full_name(request):
    full_name = f"{request.last_name} {request.first_name} {request.surname}"
    return full_name