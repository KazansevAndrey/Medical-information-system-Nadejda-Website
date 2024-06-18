
// Функция для закрытия всплывающего окна
function closePopup() {
    document.getElementById('popup1').style.display = 'none';
}

// Функция для редактирования дневника
function editDiary(diary_types) {
    // Найти все элементы с классом item-date
    const items = document.querySelectorAll('.item-date');
    items.forEach(item => {
        const key = item.getAttribute('data-key');
        const editable = item.getAttribute('data-editable') !== 'false';

        // Проверить, можно ли редактировать данный элемент
        if (editable) {
            const value = item.textContent;

            // Если элемент является "Вид дневника", заменить его селектом
            if (key === 'diary_type') {
                const select = document.createElement('select');
                select.setAttribute('data-key', key);
                const diaryTypesArray = diary_types;
                const options = [];
                
                diary_types.forEach(type => {
                    options.push(type);
                })

                options.forEach(option => {
                    const optionElement = document.createElement('option');
                    optionElement.value = option;
                    optionElement.textContent = option;
                    if (option === value) {
                        optionElement.selected = true;
                    }
                    select.appendChild(optionElement);
                });

                item.replaceWith(select);
            } else {
                // Создать поле textarea и заменить им текст
                const textarea = document.createElement('textarea');
                textarea.value = value;
                textarea.setAttribute('data-key', key);
                textarea.style.height = `${textarea.scrollHeight}px`; // Устанавливаем высоту в зависимости от содержания
                textarea.addEventListener('input', autoResize); // Добавляем обработчик для автоматического изменения высоты
                item.replaceWith(textarea);
            }
        }
    });

    // Изменить кнопку "Редактировать" на "Сохранить"
    const editButton = document.querySelector('button[id=writeDiary]');
    editButton.textContent = 'Сохранить';
    editButton.setAttribute('onclick', 'saveDiary()');
}

// Функция для автоматического изменения высоты textarea
function autoResize(event) {
    event.target.style.height = 'auto';
    event.target.style.height = `${event.target.scrollHeight}px`;
}

// Функция для сохранения изменений дневника
function saveDiary() {
    // Создать объект с данными для отправки на сервер
    const data = {};
    const inputs = document.querySelectorAll('textarea[data-key], select[data-key]');
    inputs.forEach(input => {
        const key = input.getAttribute('data-key');
        const value = input.value;
        data[key] = value;

        // Заменить поле ввода или селект обратно на текст
        const span = document.createElement('span');
        span.className = 'item-date';
        span.setAttribute('data-key', key);
        span.textContent = value;
        input.replaceWith(span);
    });

    // Отправить запрос на сервер
    fetch('update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Функция для получения CSRF токена
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
        } else {
            alert('Ошибка при сохранении данных');
        }
    }).catch(error => {
        console.error('Error:', error);
    });

    // Изменить кнопку "Сохранить" обратно на "Редактировать"
    const saveButton = document.querySelector('button[onclick="saveDiary()"]');
    saveButton.textContent = 'Редактировать';
    saveButton.setAttribute('onclick', 'editDiary()');
}

// Функция для удаления дневника
function deleteDiary(patient_id) {
    // Отправить запрос на сервер
    fetch('delete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Функция для получения CSRF токена
        },
    }).then(response => {
        if (response.ok) {
            closePopup();
            window.location.href = "/patient/"+ patient_id ;
        } else {
            alert('Ошибка при удалении дневника');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

// Функция для получения CSRF токена из cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
