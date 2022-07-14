import datetime
import pathlib
from airflow.models import DAG
from airflow.operators.bash import BashOperator

def test_bash_operator(tmp_path):
  with DAG(dag_id="test_dag",start_date=datetime.datetime(2022,7,14),schedule_interval="@daily")as dag:
    outputs=tmp_path/ "output.txt"
    test=BashOperator(task_id="test",bash_command="echo {{ ds_nodash }} > "+str(outputs))
    dag.clear()
    test.run(
      start_date=dag.start_date,end_date=dag.start_date, ignore_first_depends_on_past=True,ignore_ti_state=True
    )
    assert outputs.read_text() == "20220714\n"

      