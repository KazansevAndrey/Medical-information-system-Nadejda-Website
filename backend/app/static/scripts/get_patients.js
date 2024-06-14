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
            const dep_patients_container = $('.patient-list')
            const doc_patients_container = $('.my-patients')
            dep_patients_container.empty();
            doc_patients_container.empty();
            data.patients_of_department.forEach(function(patient){
                console.log(patient)
                dep_patients_container.append(parients_template(patient))
            
            })
            data.patients_of_doctor.forEach(function(patient){
                console.log(patient)
                doc_patients_container.append(parients_template(patient)) 
            })
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
            depPatientsContainer.empty();
            docPatientsContainer.empty();

            data.patients_of_department.forEach(function(patient){
                console.log(patient)    
                depPatientsContainer.append(parients_template(patient))
            })

            data.patients_of_doctor.forEach(function(patient){
                console.log(patient)
                docPatientsContainer.append(parients_template(patient))
            });
        }
    });
};

function get_age(number, titles) {
    cases = [2, 0, 1, 1, 1, 2];
    return [number, titles[ (number%100>4 && number%100<20)? 2 : cases[(number%10<5)?number%10:5] ]].join(' ');
}

const parients_template = (patient) => `
    <a style='text-decoration:none; color:#000' href="/patient/${patient.id}" class="patient-item">
        <span><i class="fa-solid fa-clipboard-user" style="margin-right: 10px;"></i>${patient.last_name} ${patient.first_name} ${patient.surname}</span>
        <span>${get_age(patient.age, ['год', 'года', 'лет'])}, госпитализация: ${patient.receipt_date}</span>
    </a>
`;