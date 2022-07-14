from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

default_args={
    'owner':"airflow",

    'start_date':dt.datetime(2022,7,13),
    'email':'thankiruchit007@gmail.com'
}
with DAG(
    dag_id="dates",default_args=default_args)as dag:

    task3_op = BashOperator(task_id='task3',bash_command="echo {{execution_date.strftime('%Y%m%d%H%M%S')}}",dag=dag)