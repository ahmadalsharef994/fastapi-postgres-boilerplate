FROM python:3.12-slim

WORKDIR /api_gateway

COPY . /api_gateway

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary websockets python-dotenv

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
