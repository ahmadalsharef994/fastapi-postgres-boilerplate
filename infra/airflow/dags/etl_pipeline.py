from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd

default_args = {
    'owner': 'ahmad',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def extract_users():
    res = requests.get("http://user_service:8001/users")
    users = res.json()
    df = pd.DataFrame(users)
    df.to_csv("/tmp/users.csv", index=False)

def extract_jobs():
    res = requests.get("http://job_service:8002/jobs")
    jobs = res.json()
    df = pd.DataFrame(jobs)
    df.to_csv("/tmp/jobs.csv", index=False)

with DAG(
    dag_id='etl_users_jobs',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    extract_users_task = PythonOperator(
        task_id="extract_users",
        python_callable=extract_users
    )

    extract_jobs_task = PythonOperator(
        task_id="extract_jobs",
        python_callable=extract_jobs
    )

    extract_users_task >> extract_jobs_task
