from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
import unittest

def get_date():
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    return a+b

with DAG(
    dag_id='xcom_dag',
    schedule_interval='@daily',
    start_date=datetime(2022, 3, 1),
    catchup=False
) as dag:

    task_get_date = PythonOperator(
        task_id='get_date',
        python_callable=get_date,
        do_xcom_push=True
    )

class testsum(unittest.TestCase):
    def test_sum(self):
        assert get_date() == 40
         
        
