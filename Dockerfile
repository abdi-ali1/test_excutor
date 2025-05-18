FROM python:3.13-slim-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
COPY celery_app.py .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9001"]