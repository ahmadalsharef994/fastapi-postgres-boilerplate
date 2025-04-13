FROM apache/airflow:2.8.1-python3.11

USER root
RUN pip install psycopg2-binary requests pandas

USER airflow
COPY dags/ /opt/airflow/dags/
