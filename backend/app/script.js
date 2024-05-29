function showCodeStep() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username && password) {
        document.getElementById('step1').style.display = 'none';
        document.getElementById('step2').style.display = 'block';
    } else {
        alert('Пожалуйста, введите имя пользователя и пароль.');
    }
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
    var code = document.getElementById('code').value;
    if (!/^\d{4}$/.test(code)) {
        alert('Пожалуйста, введите 4-значный код.');
        event.preventDefault();
    }
});
