function showCodeStep() {
    var username = document.getElementById('iin').value;
    var password = document.getElementById('phone_number').value;

    if (username && password) {
        document.getElementById('step1').style.display = 'none';
        document.getElementById('step2').style.display = 'block';
    } else {
        alert('Пожалуйста, введите имя номер телефона и ИИН.');
    }
}

document.getElementById('myForm').addEventListener('submit', function(event) {
    var code = document.getElementById('code').value;
    if (!/^\d{4}$/.test(code)) {
        alert('Пожалуйста, введите 4-значный код.');
        event.preventDefault();
    }
});

