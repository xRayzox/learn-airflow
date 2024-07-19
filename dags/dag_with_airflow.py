from airflow.decorators import dag , task

from datetime import datetime, timedelta

default_args = {
    'owner': 'Rayzo',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

@dag(dag_id='dag_with_api',
     default_args=default_args,
     start_date=datetime(2024,7,10,2),
     schedule_interval='@daily')
def greet():

    @task(multiple_outputs=True)
    def get_name():
        return {'firstname':'Rayzo', 'lastname':'kusha'}
    
    @task()
    def get_age():
        return 23
    
    @task()
    def gett(firstname,lastname,age):
        print(f"hello{firstname}{lastname} {age}")

    name_dict = get_name()
    age = get_age()
    gett(firstname=name_dict['firstname'],
         lastname=name_dict['lastname'], 
         age=age)


sui=greet()
