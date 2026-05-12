FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD python manage.py migrate --no-input && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
