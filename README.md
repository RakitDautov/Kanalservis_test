# Kanalservis_test

Проект разворачивается в контейнерах Docker.
Приложение получает данные из таблицы Google Sheets через API,
добавляет их в свою базу данных (обновляет их каждую минуту),
добавляет значение цены в рублях, по текущему курсу ЦБ (обновляет каждый будний день в 10 утра),
проверяет день доставки, если он совпадает с текущим, отправляет сообщение на телеграм.
У проекта есть одна web страничка '/home', где можно увидеть все данные из базы.

### Стек технологий

    Python, Django, PostgreSQL, Docker, docker-compose, Celery, Google API, 
    google-auth, nginx, gunicorn, redis

### Запуск
    
- Создайте .env файл с данными для PostgreSQL и Telegram Bot в корневую папку проекта
``` DB_ENGINE, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT, TOKEN, CHAT_ID ```
- Подключиться в телеграмме к боту рассылки
- Создайте файл credentials.json в папке с Dockerfile с данными для Google API
- Из папки с docker-compose.yml запустите команду
``` docker-compose up --build ```

### Ссылка на таблицу

    https://docs.google.com/spreadsheets/d/1TrAJ4OnOk_KQiAnuK2W54-LCoUwrVfYvYfhDtPo_4Js/edit#gid=0
  
### Автор работы
  
    Даутов Ракит Маратович