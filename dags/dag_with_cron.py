from datetime import datetime , timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner':'Rayzo',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_cron_v1',
    description='first',
    default_args=default_args,
    start_date=datetime.now(),
    schedule_interval='0 0 * * * '
)as dag :
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo sui helllllllllll'
    )

    task1