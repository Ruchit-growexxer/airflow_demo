import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOpeator
from datetime import timedelta
from airflow.utils.dates import days_ago

def my_func():
  print("Hey, This is Ruchit here.")
  