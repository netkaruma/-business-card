

const likeButtons = document.querySelectorAll('.like-button');

likeButtons.forEach(button => {
    button.addEventListener('click', () => {
        const likeCount = button.previousElementSibling; // Считываем текущий счетчик лайков
        let currentCount = parseInt(likeCount.textContent); // Текущее значение лайков

        const isLiked = button.classList.contains('liked'); // Проверяем, поставлен ли лайк
        const action = isLiked ? 0 : 1; // 0 — снимаем лайк, 1 — ставим лайк

        // Сохраняем старое значение, чтобы при ошибке можно было восстановить
        const oldCount = currentCount;
        let csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        // Отправляем запрос на сервер
        fetch('comments/update-like/', {
            method: 'POST',
            headers: {
                "X-CSRFToken" : csrfToken,
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `likeAction=${action}&comment=${button.closest(".user-comment").getAttribute("comment-id")}`
        })
        .then(response => response.json()) // Ожидаем ответ от сервера
        .then(data => {
            if (data.success) {
                // Если сервер подтвердил успешное выполнение, обновляем интерфейс
                likeCount.textContent = isLiked ? currentCount - 1 : currentCount + 1;
                button.classList.toggle('liked'); // Переключаем класс лайка
            } else {
                // Если сервер вернул ошибку, отменяем изменения
                likeCount.textContent = oldCount; // Восстанавливаем старое количество лайков
                button.classList.toggle('liked'); // Восстанавливаем состояние кнопки
                console.error('Ошибка при обновлении лайка');
            }
        })
        .catch(error => {
            // В случае ошибки отменяем изменения и выводим ошибку
            likeCount.textContent = oldCount; // Восстанавливаем старое количество лайков
            button.classList.toggle('liked');
            console.error('Ошибка при отправке запроса:', error);
        });
    });
});
// Функция для переключения отображения кнопок авторизации
function toggleAuthButtons() {
    const buttons = document.querySelector('.auth-buttons');
    if (buttons.style.display === 'flex') {
        buttons.style.display = 'none';
    } else {
        buttons.style.display = 'flex';
    }
}
// // Модальное окно для палитры
// function openModal() {
//     document.getElementById('colorModal').style.display = 'block';
// }

// function closeModal() {
//     document.getElementById('colorModal').style.display = 'none';
// }
function hexToRgb(hex) {
    let bigint = parseInt(hex.slice(1), 16);
    return [(bigint >> 16) & 255, (bigint >> 8) & 255, bigint & 255];
}

function updateColors() {
    let color1 = document.getElementById("colorPicker1").value;
    let alpha = document.getElementById("alphaSlider").value;
    
    
    let rgb = hexToRgb(color1);
    let rgbaColor = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${alpha})`;
    
    document.documentElement.style.setProperty('--color-design', rgbaColor);
}

document.getElementById("colorPicker1").addEventListener("input", updateColors);
document.getElementById("alphaSlider").addEventListener("input", updateColors);

// updateColors();

function submitColor() {
    let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

    let color = document.getElementById("colorPicker1").value;
    let alpha = document.getElementById("alphaSlider").value;
    
    let rgb = hexToRgb(color);
    let rgbaColor = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${alpha})`;

    fetch(saveColorUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ color: rgbaColor })
    })
}

// Функция для открытия модального окна
function openModal(id) {
    const modal = document.getElementById(id);
    modal.style.display = 'flex'; // Показываем модальное окно
}

// Функция для закрытия модального окна
function closeModal(id) {
    const modal = document.getElementById(id);
    modal.style.display = 'none'; // Скрываем модальное окно
}

// // Функция для отправки формы (например, при логине или регистрации)
// function submitForm(type) {
//     alert(type === 'login' ? 'Вход выполнен!' : 'Регистрация успешна!');
//     closeModal(type === 'login' ? 'loginModal' : 'registerModal');
// }

// Убедитесь, что модальные окна скрыты при загрузке страницы
// window.onload = function() {
//     const modals = document.querySelectorAll('.modal');
//     modals.forEach(modal => modal.style.display = 'none');
// };



document.querySelector('.close').addEventListener('click', function() {
    document.getElementById('loginModal').style.display = 'none';
        });

window.addEventListener('click', function(event) {
    let modal = document.getElementById('loginModal');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

function closeNotification() {
var notification = document.getElementById('notifications');
notification.classList.add('hide');

// Убираем уведомление через 0.5s (время, которое длится анимация)
setTimeout(function() {
    notification.style.display = 'none';
});
}
