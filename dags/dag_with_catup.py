from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.bash import BashOperator

default_args ={
    'owner':'Rayzo',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_catchupV1',
    description='first',
    default_args=default_args,
    start_date=datetime(2024,7,10,2),
    schedule_interval='@daily',
    catchup=False
)as dag :
   task1=BashOperator(
      task_id='task1',
      bash_command='echo helloooooooooo world'
   )
   task1