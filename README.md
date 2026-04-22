# LMS

Учебная платформа с REST API на Django REST Framework и фронтендом на React. Реализует базовый набор функций для управления учебным процессом.

## Технологический стек

| Часть | Технология |
|---|---|
| Backend | Django 5.2, Django REST Framework 3.16 |
| Аутентификация | JWT (djangorestframework-simplejwt) |
| База данных | PostgreSQL (psycopg2) |
| Frontend | React 19, Vite 7 |
| HTTP-клиент | Axios |
| Роутинг | React Router DOM 7 |

## Структура проекта

```
.
├── backend/
│   ├── api/             # Общие утилиты, базовые маршруты
│   ├── backend/         # Настройки Django (settings, urls, wsgi)
│   ├── schedule_app/    # Расписание
│   ├── events_app/      # Мероприятия
│   ├── Homework_app/    # Домашние задания
│   ├── exams_app/       # Экзамены
│   ├── journal_app/     # Журнал оценок
│   ├── teachers_app/    # Преподаватели
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── src/
    └── package.json
```

## Функциональность

- Аутентификация и авторизация через JWT
- Расписание занятий
- Мероприятия
- Домашние задания
- Экзамены
- Журнал оценок
- Управление преподавателями
- Административная панель Django

## Запуск

### Backend

Требования: Python 3.11+, PostgreSQL.

```bash
cd backend

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Создать файл `.env` по примеру:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=lms
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API доступно на `http://localhost:8000`, админка — `http://localhost:8000/admin`.

### Frontend

Требования: Node.js 18+.

```bash
cd frontend
npm install
npm run dev
```

Приложение доступно на `http://localhost:5173`.
