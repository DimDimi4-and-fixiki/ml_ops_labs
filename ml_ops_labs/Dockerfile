FROM python:3.12-slim

ENV APP_PORT=8080
ENV WEB_VIEW_PORT=8501
ARG APP_PORT=$APP_PORT
ARG WEB_VIEW_PORT=$WEB_VIEW_PORT

# Устанавливаем рабочую директорию
WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Копируем файлы с зависимостями в контейнер
COPY README.md .
COPY pyproject.toml .
COPY requirements.lock .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.lock


# Копируем код приложения в контейнер
COPY src .

ENV PYTHONPATH "${PYTHONPATH}:/ml_ops_labs"

# Открываем порт, на котором будет работать приложение
EXPOSE $APP_PORT
EXPOSE $WEB_VIEW_PORT

# Запускаем web-api
CMD python src/ml_ops_labs/main.py

# Запускаем web-view
CMD ["streamlit", "run", "ml_ops_labs/web_view/index.py"]