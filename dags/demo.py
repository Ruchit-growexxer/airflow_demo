import pendulum

from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
    dag_id="mytrigger",
    start_date=pendulum.datetime(2022,7, 4, tz="UTC"),
    catchup=False,
    schedule_interval="@once",
    tags=['example'],
) as dag:
    trigger = TriggerDagRunOperator(
        task_id="test_trigger_dagrun",
        trigger_dag_id="mytrigger", 
        conf={"message": "Hello World"},
    )