//AJAX запрос для получения пациентов

function ShowPatients(){
    var departmentId = document.getElementById('department-select').value;

    newUrl = `/department/${departmentId}`
    history.pushState(null, '', newUrl);
    $.ajax({
        url: `/department/${departmentId}/fetch`, 
        data: {
            'department_id': departmentId
        },
        dataType: 'json',
        success: function(data) {
            $('#search-input').val('');
            var depPatientsContainer = $('.patient-list')
            var docPatiensContainer = $('.my-patients')
            var PatientsOfDepartmentIterations = data.patients_of_department.length
            var PatientsOfDoctorIterations = data.patients_of_doctor.length
            depPatientsContainer.empty();
            docPatiensContainer.empty();
            for (let i = 0; i < PatientsOfDepartmentIterations; i++) {
                var patient = data.patients_of_department[i];
                var reanimation = data.reanimations_of_department[i] 
                depPatientsContainer.append(patients_template(patient, reanimation))
            }

            for (let i = 0; i < PatientsOfDoctorIterations; i++) {
                var patient = data.patients_of_doctor[i];
                var reanimation = data.reanimations_of_doctor[i] 
                docPatiensContainer.append(patients_template(patient, reanimation))
            }
            color_patients_in_reanimation();
            }
        })}
 
function search_patients(){
    var departmentId = document.getElementById('department-select').value;
    var query = document.getElementById('search-input').value;
    $.ajax({
        url: `/department/${departmentId}/search_patients`, // URL для поиска пациентов
        data: {
            'q': query
        },
        dataType: 'json',
        success: function(data) {
            // Очищаем контейнеры с пациентами
            var depPatientsContainer = $('.patient-list');
            var docPatientsContainer = $('.my-patients');
            var patientsOfDepartmentIterations = data.patients_of_department.length
            var patientsOfDoctorIterations = data.patients_of_doctor.length

            depPatientsContainer.empty();
            docPatientsContainer.empty();
            
            for (let i = 0; i < patientsOfDepartmentIterations; i++) {
                var patient = data.patients_of_department[i];
                var reanimation = data.reanimations_of_department[i] 
                depPatientsContainer.append(patients_template(patient, reanimation))
            }

            for (let i = 0; i < patientsOfDoctorIterations; i++) {
                var patient = data.patients_of_doctor[i];
                var reanimation = data.reanimations_of_doctor[i] 
                docPatientsContainer.append(patients_template(patient, reanimation))
            }
            color_patients_in_reanimation();
            }
        })}

function color_patients_in_reanimation(){

    const patients = document.querySelectorAll('.patient-item');
    
    patients.forEach(patient =>{
    const status = patient.dataset.reanimation.toLowerCase();
    const patient_name = patient.querySelector('span')
    if(status=="true"){
        patient_name.style.color = "red";
        }
    })
}

function get_age(number, titles) {
    cases = [2, 0, 1, 1, 1, 2];
    return [number, titles[ (number%100>4 && number%100<20)? 2 : cases[(number%10<5)?number%10:5] ]].join(' ');
}

const patients_template = (patient, reanimation) => `
    <a data-reanimation='${reanimation}' style='text-decoration:none; color:#000' href="/patient/${patient.id}" class="patient-item">
        <span><i class="fa-solid fa-clipboard-user" style="margin-right: 10px;"></i>${patient.last_name} ${patient.first_name} ${patient.surname}</span>
        <span  id="shadow" >${get_age(patient.age, ['год', 'года', 'лет'])}, госпитализация: ${patient.receipt_date}</span>
    </a>
`;