//AJAX запрос для получения пациентов

function ShowPatients(){
    var departmentId = document.getElementById('department-select').value;
    console.log(departmentId);
    $.ajax({
        url: '/department/fetch_patients', 
        data: {
            'department_id': departmentId
        },
        dataType: 'json',
        success: function(data) {
            const container = $('.patient-list')
            container.empty();
            data.patient_list.forEach(function(patient){
                console.log(patient)
                html = `
                <div class="patient-item">
                <span><i class="fa-solid fa-clipboard-user"></i> ${patient.last_name} ${patient.first_name} ${patient.surname}</span>
                <span>${get_age(patient.age, ['год', 'года', 'лет'])}, госпитализация: ${patient.receipt_date}</span></div>`
                container.append(html)
            })

            }

        })}
 

function get_age(number, titles) {
    cases = [2, 0, 1, 1, 1, 2];
    return [number, titles[ (number%100>4 && number%100<20)? 2 : cases[(number%10<5)?number%10:5] ]].join(' ');
}
