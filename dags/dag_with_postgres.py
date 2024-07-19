from datetime import datetime ,timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args ={
    'owner':'Rayzo',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='Postgres_dag',
    default_args=default_args,
    start_date=datetime(2024,7,1,2),
    schedule_interval='@daily'
)as dag :
    task1=PostgresOperator(
        task_id='postgres',
        postgres_conn_id='Postgres_con',
        sql=""" 
        Create table if not exists drag_runs(
        dt date,
        dag_id character varying,
        primary key (dt, dag_id)
        )
        """

    ) 
    task2=PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='Postgres_con',
        sql=""" 
        insert into drag_runs(dt,dag_id) values('{{ds}}', '{{dag.dag_id}}')
        """
    )
    task3=PostgresOperator(
        task_id='delete_data_from_table',
        postgres_conn_id='Postgres_con',
        sql=""" 
        delete from drag_runs where dt = '{{ds}}' and dag_id = '{{dag.dag_id}}'
        """
    )
    task1 >> task3>> task2