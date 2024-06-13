function FilterRecords(patient_id){
    var category = document.getElementById('categories_select').value;
    var data = document.getElementById('data').value;
    var list_type = document.getElementById('list_type').value;
    $.ajax({
        url: `/patient/${patient_id}/sorting`, 
        data: {
            'category': category,
            'data':data,
            'list_type':list_type
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