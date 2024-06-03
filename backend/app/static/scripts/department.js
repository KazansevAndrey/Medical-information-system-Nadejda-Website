document.addEventListener('DOMContentLoaded', function() {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const doctorIcon = document.querySelector('.doctor');

    dropdownToggle.addEventListener('click', function(event) {
        event.preventDefault();
        dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    document.addEventListener('click', function(event) {
        if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });

    const buttons = document.querySelectorAll('.btn_block2');
    const patientList = document.querySelector('.patient-list');
    const searchInput = document.querySelector('#search-input');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            buttons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            // Insert code here to handle switching between all patients and my patients.
        });
    });

    searchInput.addEventListener('input', function() {
        const filter = searchInput.value.toLowerCase();
        const patients = patientList.querySelectorAll('.patient-item');
        patients.forEach(patient => {
            const name = patient.querySelector('span').textContent.toLowerCase();
            if (name.includes(filter)) {
                patient.style.display = '';
            } else {
                patient.style.display = 'none';
            }
        });
    });
});
const patientItems = document.querySelectorAll('.patient-item');

patientItems.forEach(patientItem => {
    patientItem.addEventListener('click', function() {
        // Получаем имя пациента для использования в URL новой страницы
        const patientName = this.querySelector('span').textContent;
        // Формируем URL для перехода на другую страницу с подробной информацией о пациенте
        const newPageURL = 'patient_details.html?name=' + encodeURIComponent(patientName);
        // Перенаправляем на новую страницу
        window.location.href = newPageURL;
    });

    // Добавляем стили для изменения внешнего вида курсора при наведении на пациента
    patientItem.style.cursor = 'pointer';
    patientItem.addEventListener('mouseenter', function() {
        this.style.backgroundColor = '#f1f1f1'; // Изменяем фон при наведении
    });
    patientItem.addEventListener('mouseleave', function() {
        this.style.backgroundColor = ''; // Возвращаем исходный фон при уходе курсора
    });
});


//AJAX запрос для получения пациентов

ShowPatients()