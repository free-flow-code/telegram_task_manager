FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV DB_FILENAME=mydb.sqlite3
ENV SERVER_TZ=Europe/Moscow

CMD alembic upgrade head && python main.py
