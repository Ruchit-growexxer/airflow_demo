from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from hello import HelloOperator
import datetime as dt
import pendulum

default_args={
    'owner':"airflow",
    'start_date':dt.datetime(2022,7,13),
    'email':'thankiruchit007@gmail.com'
}
with DAG(
    dag_id="demos",default_args=default_args)as dag:

    hello = HelloOperator(task_id="demo",a=20,b=20)
    assert hello == 30 