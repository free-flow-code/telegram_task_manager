# Task Manager (telegram bot)

Телеграм-бот для создания и хранения личного списка задач.

### Стек

- Python 3.10, Aiogram3
- SQLite, SQLAlchemy, Alembic

## Установка и запуск

Клонируйте репозиторий. Создайте виртуальное окружение. Установите зависимости командой:
```shell
pip install -r requirements.txt
```

В корне проекта создайте `.env` файл с переменными:
```shell
BOT_TOKEN=7526578432:AAF8hTJ4dFCloqB6eWjHR7Ibjc8-I-jtF43F
DB_FILENAME=mydb.sqlite3
SERVER_TZ=Europe/Moscow
```
где:
```shell
`BOT_TOKEN` токен телеграм бота, обязательная переменная
`DB_FILENAME` название файля БД (необязательно), по умолчанию 'mydb.sqlite3'
`SERVER_TZ` временная зона (необязательно), по умолчанию 'Europe/Moscow'
```

Примените миграции командой:
```shell
alembic upgrade head
```

И запустите бота:
```shell
python main.py
```