FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose prometheus-fastapi-instrumentator

EXPOSE 8003
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
