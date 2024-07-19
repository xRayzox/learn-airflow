from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.bash import BashOperator

default_args ={
    'owner':'Rayzo',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag_v6',
    default_args=default_args,
    start_date=datetime(2024,7,10,2),
    schedule_interval='@daily'
)as dag :
    task1= BashOperator(
        task_id='task1',
        bash_command="echo Hello World"
        )
    task2= BashOperator(
        task_id='task2',
        bash_command="echo Hey second"
        )
    task3= BashOperator(
        task_id='task3',
        bash_command="echo Hey third"
        )
    #task1.set_downstream(task2) 
    #task1.set_downstream(task3)

    #task1 >> task2
    #task1 >> task3
    task1 >> [task2,task3] 