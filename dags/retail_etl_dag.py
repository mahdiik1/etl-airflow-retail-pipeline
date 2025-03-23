import datetime
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'Mahdi Ibn-Kabir',
    'depends_on_past': False,
    'start_date': datetime.datetime(2025, 1, 1),
    'retries': 1
}

def extract():
    os.system('python /usr/local/airflow/scripts/extract.py')

def transform():
    os.system('python /usr/local/airflow/scripts/transform.py')

def load():
    os.system('python /usr/local/airflow/scripts/load.py')

with DAG('retail_etl_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load
    )

    extract_task >> transform_task >> load_task
