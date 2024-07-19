from airflow import DAG
from datetime import datetime ,timedelta
from airflow.operators.python import PythonOperator


default_args ={
    'owner':'Rayzo',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get',key='first_name')
    last_name = ti.xcom_pull(task_ids='get',key='last_name')
    age = ti.xcom_pull(task_ids='get_age',key='age')
    return print(f"hello world!{first_name}{last_name}{age}")

def get_name(ti):
    ti.xcom_push(key='first_name',value='jhonny')
    ti.xcom_push(key='last_name',value='fridman')
def get_age(ti):
    ti.xcom_push(key='age',value='23')

with DAG(
    dag_id='python_dag_V9',
    description='python_dag description',
    default_args=default_args,
    start_date=datetime(2024,7,10,2),
    schedule_interval='@daily'
)as dag :
    task1=PythonOperator(
        task_id='greet',
        python_callable=greet,
        

    )
    task2=PythonOperator(
        task_id='get',
        python_callable=get_name

    )
    task3=PythonOperator(
        task_id='get_age',
        python_callable=get_age

    )
    [task3,task2]>>task1

